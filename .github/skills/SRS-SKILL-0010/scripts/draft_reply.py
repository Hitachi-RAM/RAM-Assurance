"""Prepare a reply and leave it as a draft. There is no code here that sends.

Search this file for a Send click and you will not find one, which is the
point: the control is the absence, not a flag that defaults to off.

The realistic failure is not sending by accident -- it is drafting into the
WRONG message. Two paths, both gated on the message matching what the user
named. Outlook desktop over COM is the default: --thread N names an item from
the last read_mail.py listing and Reply() starts from that item, so the reply
stays in the conversation and no conversation row has to be clicked. The
browser path (--web) replies to whatever is open, and has to poll the open
header first, because the web client keeps painting the previously open item
for several seconds after routing.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outlook_com as O  # noqa: E402
import srs_m365 as M  # noqa: E402

BANNER = "[Drafted by Frederick Bourgoin's GitHub Copilot assistant - please review before sending]"

JS_OPEN_HEADER = r"""
() => {
  const subj = document.querySelector(
      '[role="heading"][aria-level="1"], div[aria-label*="Subject" i], h1');
  const from = document.querySelector(
      '[data-testid="SenderPersona"], span[title*="@"], [aria-label*="From" i]');
  return {
    subject: subj ? (subj.innerText || '').trim() : '',
    sender: from ? (from.innerText || from.getAttribute('title') || '').trim() : ''
  };
}
"""

JS_CLICK_COMMAND = r"""
(names) => {
  for (const wanted of names) {
    for (const b of document.querySelectorAll('button,[role="menuitem"]')) {
      const label = (b.getAttribute('aria-label') || b.innerText || '').trim();
      if (label.toLowerCase() === wanted.toLowerCase()) {
        const r = b.getBoundingClientRect();
        if (r.width > 0 && r.height > 0) { b.click(); return wanted; }
      }
    }
  }
  return null;
}
"""

JS_COMPOSE_STATE = r"""
() => {
  const sel = ['div[aria-label="Message body"][contenteditable="true"]',
               'div[contenteditable="true"][role="textbox"]'];
  for (const s of sel) {
    for (const el of document.querySelectorAll(s)) {
      const r = el.getBoundingClientRect();
      if (r.width > 100 && r.height > 20) {
        return {found: true, selector: s, text: el.innerText || '',
                x: r.x + r.width / 2, y: r.y + 30};
      }
    }
  }
  return {found: false};
}
"""


def header_matches(actual: dict, subject: str, sender: str) -> bool:
    """Token overlap, not string equality.

    The list shows a trimmed subject and the reading pane shows the full one;
    the address book shows `TESTER Carol` where the mail says
    `Carol Tester`.

    Short words are dropped because they carry no identity -- but when that
    leaves only ONE word, the gate is no longer identifying a message. Asking
    for "TTC Line 2" collapsed to {line} and matched "Line management policy",
    which is a reply drafted against the wrong conversation. When a request
    reduces to a single word, the whole phrase must appear in the subject
    instead, so "Timesheets" still works and "TTC Line 2" no longer matches a
    line-management mail.
    """
    got_subj = M.clean(actual.get("subject", "")).lower()
    got_from = M.clean(actual.get("sender", "")).lower()
    if subject:
        asked = M.clean(subject).lower().strip()
        want = {w for w in asked.split() if len(w) > 3}
        have = set(got_subj.split())
        if not want:
            return False
        if len(want) < 2:
            if asked not in got_subj:
                return False
        elif len(want & have) < max(2, len(want) // 2):
            return False
    if sender:
        # Local part only. Splitting the whole address on "@" keeps the
        # domain, and since everyone shares one company domain that would make
        # every sender match every other sender.
        local = M.clean(sender).lower().split("@")[0]
        parts = [p for p in re.split(r"[.\s_\-]+", local) if len(p) > 2]
        if not parts or not any(p in got_from or p in got_subj for p in parts):
            return False
    return True


def reply_com(entry_id: str, mode: str, subject: str, sender: str,
              lines: list) -> int:
    """Reply over Outlook desktop. Save() only -- there is no Send() here.

    This path exists because the browser one has to find the message by
    clicking the conversation row it was listed at, and a collapsed
    conversation opens its chevron instead of the message. Starting from the
    item itself removes the whole problem, and Reply() keeps the thread.
    """
    try:
        app, ns = O.connect()
        original = O.by_entry_id(ns, entry_id)
    except O.OutlookUnavailable as exc:
        print(f"  {exc}")
        return 2

    # Same gate as the browser path: the message must be the one asked for.
    got_subject = str(O.safe(original, "Subject"))
    got_sender = (str(O.safe(original, "SenderName")) + " "
                  + str(O.safe(original, "SenderEmailAddress")))
    if not header_matches({"subject": got_subject, "sender": got_sender},
                          subject, sender):
        print("  The message at that position is not the one you described.\n"
              f"    found    : {got_subject!r} from {got_sender.strip()!r}\n"
              f"    you asked: {subject!r} from {sender!r}\n"
              "  Nothing was drafted.")
        return 1

    draft = {"reply": original.Reply,
             "reply-all": original.ReplyAll,
             "forward": original.Forward}[mode]()
    body = "\n".join(lines)
    draft.Body = body + "\n\n" + str(O.safe(draft, "Body"))
    if mode == "forward":
        print("  Forward has no recipient yet. Add one in Outlook before "
              "sending -- this skill will not choose one for you.")
    draft.Save()

    new_id = str(O.safe(draft, "EntryID"))
    if not new_id:
        print("  Outlook accepted the draft but returned no id, so it cannot "
              "be read back. Check it by eye in Drafts.")
        return 1
    saved = O.by_entry_id(ns, new_id)
    actual, readable = O._read(saved, "Body")
    probe = " ".join(body.split())[:60]
    if readable and probe and probe not in " ".join(str(actual).split()):
        print("  The saved draft does not contain the text that was written. "
              "Do not send it until this is understood.")
        return 1

    print(f"  {mode} prepared against: {got_subject[:80]!r}")
    if readable:
        print(f"  Saved to Drafts, {len(body)} characters verified present, "
              f"conversation preserved.")
    else:
        print(f"  Saved to Drafts, {len(body)} characters written. Your Outlook "
              f"policy blocked reading the body back, so it could NOT be "
              f"checked programmatically -- read it in Drafts.")
    print("\n  It has NOT been sent. Read it in Drafts and send it yourself.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Prepare an Outlook reply. It is never sent by this skill.")
    ap.add_argument("--body", required=True, help="file containing the reply text")
    ap.add_argument("--subject", default="", help="subject of the message to reply to")
    ap.add_argument("--sender", default="", help="who it is from")
    ap.add_argument("--thread", type=int,
                    help="reply to item N of the last read_mail.py listing")
    ap.add_argument("--mode", choices=["reply", "reply-all", "forward"],
                    default="reply")
    ap.add_argument("--no-banner", action="store_true",
                    help="omit the 'drafted by an assistant' line")
    ap.add_argument("--web", action="store_true",
                    help="reply to the message open in the browser instead")
    args = ap.parse_args()

    if not (args.subject or args.sender):
        print("  Refusing to draft without --subject or --sender. Without one "
              "of them there is nothing to check the open message against, and "
              "a reply typed into the wrong thread is the failure that matters.")
        return 2

    text = Path(args.body).read_text(encoding="utf-8").strip()
    if not text:
        print("  The body file is empty. Nothing to draft.")
        return 2
    body_lines, unwrapped = O.unwrap(text)
    if unwrapped:
        print(f"  {unwrapped} hard-wrapped line(s) were joined back into "
              f"paragraphs, so the mail reflows to the reader's window.")
    lines = ([] if args.no_banner else [BANNER, ""]) + body_lines

    if not args.web:
        listing = Path(__file__).resolve().parent.parent / "_last_listing.json"
        if args.thread is None:
            print("  Give --thread N to say which message of the last "
                  "read_mail.py listing to reply to, or --web to reply to "
                  "whatever is open in the browser.")
            return 2
        if not listing.exists():
            print(f"  No listing to count from. Run read_mail.py first.")
            return 2
        items = json.loads(listing.read_text(encoding="utf-8")).get("items", [])
        if not 1 <= args.thread <= len(items):
            print(f"  There is no item {args.thread}; the listing holds "
                  f"{len(items)}.")
            return 2
        entry_id = items[args.thread - 1].get("entry_id", "")
        if not entry_id:
            print("  That listing came from the browser and carries no Outlook "
                  "id. Re-run read_mail.py without --web, or use --web here.")
            return 2
        return reply_com(entry_id, args.mode, args.subject, args.sender, lines)

    if M.sync_playwright is None:
        print("Playwright is not installed.  py -m pip install playwright")
        return 2

    with M.sync_playwright() as pw:
        browser, page = M.attach(pw, M.URLS["mail"])
        try:
            page.wait_for_load_state("domcontentloaded", timeout=60000)
            M.require_sign_in(page)
            M.dismiss_prompts(page)

            header = M.poll(
                lambda: (lambda h: h if header_matches(h, args.subject, args.sender) else None)(
                    M.js(page, JS_OPEN_HEADER) or {}),
                seconds=30)
            if not header:
                actual = M.js(page, JS_OPEN_HEADER) or {}
                print("  The open message does not match what you asked for.\n"
                      f"    open now : {M.clean(actual.get('subject'))!r} "
                      f"from {M.clean(actual.get('sender'))!r}\n"
                      f"    you asked: {args.subject!r} from {args.sender!r}\n"
                      "  Open the right message and run this again. Nothing "
                      "was typed.")
                return 1
            print(f"  Replying to: {M.clean(header['subject'])[:80]!r}")

            command = {"reply": ["Reply"], "reply-all": ["Reply all", "Reply All"],
                       "forward": ["Forward"]}[args.mode]
            if not M.poll(lambda: M.js(page, JS_CLICK_COMMAND, command), seconds=20):
                print(f"  Could not find the {args.mode} command. Nothing was typed.")
                return 1
            page.wait_for_timeout(2500)
            M.dismiss_prompts(page)

            state = M.poll(lambda: (lambda s: s if s.get("found") else None)(
                M.js(page, JS_COMPOSE_STATE) or {}), seconds=25)
            if not state:
                print("  The reply form did not open. Nothing was typed.")
                return 1

            existing = M.clean(state.get("text", ""))
            if existing and BANNER[:40] not in existing:
                print("  There is already text in this reply that this skill "
                      "did not write:\n"
                      f"    {existing[:120]!r}\n"
                      "  That is yours. Stopping rather than overwriting it.")
                return 1

            # Click first: the box only gains focus as a side effect of being
            # cleared, so inserting into an already-empty box types into
            # nothing at all and reports success.
            page.mouse.click(state["x"], state["y"])
            page.wait_for_timeout(400)
            for n, line in enumerate(lines):
                if n:
                    page.keyboard.press("Enter")
                if line:
                    # insert_text rather than type(): type() drops characters
                    # on anything long, silently.
                    page.keyboard.insert_text(line)

            page.wait_for_timeout(800)
            after = M.clean((M.js(page, JS_COMPOSE_STATE) or {}).get("text", ""))
            wanted = M.clean("\n".join(lines))
            ok = wanted[:200] in after
            print(f"\n  Draft prepared: {len(after)} characters in the reply box.")
            print(f"  Content check: {'matches what was written' if ok else 'DOES NOT MATCH -- read it before sending'}")
            if not M.dismiss_prompts(page):
                pass
            page.screenshot(path="draft_ready.png")
            print("  Screenshot: draft_ready.png")
            print("\n  It has NOT been sent. The window is open; read it, change "
                  "it, and press Send yourself if you agree with it.")
            return 0 if ok else 1
        finally:
            M.release(browser, keep_open=True)  # the unsent draft must survive


if __name__ == "__main__":
    sys.exit(main())
