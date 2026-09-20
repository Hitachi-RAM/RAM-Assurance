"""Compose a NEW mail and leave it as a draft. Nothing here sends.

The reply path exists in draft_reply.py; this one starts from nothing, which
moves the risk. Replying has a gate on the open message; composing has no such
anchor, so the whole risk is the recipient.

Two paths. Outlook desktop over COM is the default, because everything it sets
is a property that can be read back off the saved draft -- the subject, the
body, the resolved SMTP address of every recipient. The browser path (--web)
exists for machines with no Outlook desktop, and is weaker for exactly the
reason this skill cares about: a recipient chip shows a display name and hides
the address, so the only moment an address can be checked is while the
suggestion is still on screen. A migrated colleague appears twice in the
address book under one display name, so "exactly one suggestion" is never a
safe assumption either.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outlook_com as O  # noqa: E402
import srs_m365 as M  # noqa: E402

BANNER = "[Drafted by an assistant on the sender's behalf - please review before sending]"

JS_NEW_MAIL = r"""
() => {
  for (const b of document.querySelectorAll('button,[role="menuitem"]')) {
    const label = (b.getAttribute('aria-label') || b.innerText || '').trim();
    if (/^(New mail|New message|New Mail)$/i.test(label)) {
      const r = b.getBoundingClientRect();
      if (r.width > 0) { b.click(); return label; }
    }
  }
  return null;
}
"""

# aria-label matched EXACTLY. A loose /to|recipient/ pattern also matches Cc,
# Bcc and any address field the reading pane happens to be showing.
#
# A field is looked up by several candidate names, against BOTH aria-label and
# placeholder. OWA labelled the subject box "Add a subject" and then moved that
# string to the placeholder, labelling the input "Subject" -- one rename that
# took the whole browser path out, because the locator had a single candidate.
JS_FIELD = r"""
(spec) => {
  const names = Array.isArray(spec.name) ? spec.name : [spec.name];
  const hit = (text) => {
    if (!text) return false;
    const t = text.trim().toLowerCase();
    return names.some(n => spec.exact ? t === n : t.startsWith(n));
  };
  for (const el of document.querySelectorAll(
        'input,[role="textbox"],[contenteditable="true"]')) {
    if (hit(el.getAttribute('aria-label'))
        || (!spec.exact && hit(el.getAttribute('placeholder')))) {
      const r = el.getBoundingClientRect();
      if (r.width > 20 && r.height > 5) {
        return {x: r.x + r.width / 2, y: r.y + r.height / 2};
      }
    }
  }
  return null;
}
"""

JS_PICK_SUGGESTION = r"""
(address) => {
  const wanted = address.toLowerCase();
  const options = Array.from(document.querySelectorAll('[role="option"]'))
      .filter(o => (o.innerText || '').toLowerCase().includes(wanted));
  if (!options.length) return null;
  const o = options[0];
  const r = o.getBoundingClientRect();
  if (r.width < 20) return null;
  const cx = r.x + r.width / 2, cy = r.y + r.height / 2;
  // Confirm the element under the cursor is still this option: the suggestion
  // list reorders while it loads, and clicking a stale rectangle picks a
  // different person.
  let hit = document.elementFromPoint(cx, cy);
  while (hit && hit !== o) hit = hit.parentElement;
  if (hit !== o) return null;
  return {x: cx, y: cy, text: (o.innerText || '').trim(), matches: options.length};
}
"""

# The resolved recipient chips. Several candidate shapes, because the previous
# three all stopped matching: a To field visibly holding three chips returned an
# empty list, and an empty list was printed as nothing at all -- indisputable
# from a clean run. An absence and a locked door look identical, so this now
# returns null when it cannot find the container, and [] only when it can see
# the container and it is genuinely empty.
JS_PILLS = r"""
() => {
  const wells = Array.from(document.querySelectorAll(
        '[data-testid="recipient-well"], [aria-label="To"], [aria-label="Cc"]'));
  const chips = new Set();
  for (const w of wells) {
    for (const p of w.querySelectorAll(
          '[role="button"], [role="listitem"], .ms-PickerPersona-container,'
        + ' [class*="PickerPersona"], [class*="personaCell"], span[title]')) {
      const t = (p.getAttribute('title') || p.innerText
                 || p.getAttribute('aria-label') || '').trim();
      if (t && t.length < 120) chips.add(t);
    }
  }
  if (chips.size) return Array.from(chips);
  // Nothing matched. Say whether there was even a container to look in.
  return wells.length ? [] : null;
}
"""

JS_BODY = r"""
() => {
  for (const el of document.querySelectorAll(
        'div[aria-label="Message body"][contenteditable="true"],'
      + 'div[contenteditable="true"][role="textbox"]')) {
    const r = el.getBoundingClientRect();
    if (r.width > 200 && r.height > 40) {
      return {found: true, text: el.innerText || '',
              x: r.x + r.width / 2, y: r.y + 30};
    }
  }
  return {found: false};
}
"""

# Read a field back after typing into it. Typing is not evidence of arrival.
# The predicate must be the one used to FIND the field, or a rename makes the
# read-back silently look at nothing.
JS_FIELD_VALUE = r"""
(names) => {
  const wanted = Array.isArray(names) ? names : [names];
  const hit = (text) => {
    if (!text) return false;
    const t = text.trim().toLowerCase();
    return wanted.some(n => t.startsWith(n));
  };
  for (const el of document.querySelectorAll(
        'input,[role="textbox"],[contenteditable="true"]')) {
    if (hit(el.getAttribute('aria-label')) || hit(el.getAttribute('placeholder'))) {
      return (el.value !== undefined && el.value !== null)
             ? el.value : (el.innerText || '');
    }
  }
  return null;
}
"""

SUBJECT_NAMES = ["subject", "add a subject"]


def add_recipient(page, field: str, address: str) -> str | None:
    """Type an address, verify the suggestion, click it. None if not resolved."""
    spot = M.poll(lambda: M.js(page, JS_FIELD, {"name": field, "exact": True}),
                  seconds=20)
    if not spot:
        return None
    page.mouse.click(spot["x"], spot["y"])
    page.wait_for_timeout(300)
    page.keyboard.insert_text(address)

    # Poll rather than sleep: a fixed wait for this list failed one run in five.
    option = M.poll(lambda: M.js(page, JS_PICK_SUGGESTION, address),
                    seconds=20, interval=2)
    if not option:
        return None
    if option.get("matches", 1) > 1:
        print(f"  {address}: {option['matches']} address-book entries match. "
              f"A migrated colleague appears twice under one display name -- "
              f"check the recipient before sending.")
    page.mouse.click(option["x"], option["y"])
    page.wait_for_timeout(1000)
    M.dismiss_prompts(page)
    return M.clean(option["text"])[:60]


def compose_com(to, cc, subject: str, lines: list) -> int:
    """Outlook desktop. Save() only -- Send() appears nowhere in this file."""
    try:
        app, ns = O.connect()
    except O.OutlookUnavailable as exc:
        print(f"  {exc}")
        return 2

    body = "\n".join(lines)
    mail = app.CreateItem(O.OL_MAIL_ITEM)
    mail.Subject = subject
    mail.Body = body

    people = O.resolve(mail, to, kind=1) + O.resolve(mail, cc, kind=2)
    blocked = [p for p in people if p["blocked"]]
    unresolved = [p for p in people if not p["resolved"] and not p["blocked"]]
    if unresolved:
        for p in unresolved:
            print(f"  The address book does not recognise {p['requested']!r}.")
        print("  Nothing was saved. A draft addressed to an unresolved "
              "recipient is the one that goes to the wrong person.")
        return 1

    if blocked:
        # Policy denies the address book. The addresses came from the person
        # running this; they are used exactly as given and never inferred.
        print("  Your Outlook policy does not allow this to use the address "
              "book, so the recipients could NOT be checked against it.")
        O.address_plainly(mail, to, cc)
        for p in blocked:
            print(f"    {p['kind']:<3} {p['requested']}   (not verified)")

    mail.Save()
    entry_id = str(O.safe(mail, "EntryID"))
    if not entry_id:
        print("  Outlook accepted the draft but returned no id, so it cannot "
              "be read back and checked. Open Drafts and check it by eye.")
        return 1

    problems, unchecked = O.verify_draft(ns, entry_id, subject, body)
    print("  Saved to Drafts:")
    for p in people:
        if p["blocked"]:
            continue
        print(f"    {p['kind']:<3} {p['name']}  <{p['address'] or 'address not exposed'}>")
    if problems:
        print("\n  The saved draft does not match what was asked for:")
        for p in problems:
            print(f"    - {p}")
        print("  The draft is in your Drafts folder. Do not send it until this "
              "is understood.")
        return 1
    print(f"    subject  {subject}")
    if "body" in unchecked:
        print(f"    body     {len(body)} characters, written but NOT read back")
    else:
        print(f"    body     {len(body)} characters, verified present")
    if unchecked:
        print(f"\n  Your Outlook policy blocked reading back: "
              f"{', '.join(unchecked)}. The draft IS saved; it simply could not "
              f"be checked programmatically. Read it in Drafts before sending.")
    print("\n  It has NOT been sent. Read it in Drafts and send it yourself.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Compose a new Outlook draft. It is never sent by this skill.")
    ap.add_argument("--to", action="append", required=True,
                    help="recipient address; repeat for several")
    ap.add_argument("--cc", action="append", default=[])
    ap.add_argument("--subject", required=True)
    ap.add_argument("--body", required=True, help="file containing the message")
    ap.add_argument("--no-banner", action="store_true")
    ap.add_argument("--web", action="store_true",
                    help="use the browser instead of Outlook desktop")
    args = ap.parse_args()

    text = Path(args.body).read_text(encoding="utf-8").strip()
    if not text:
        print("  The body file is empty. Nothing to draft.")
        return 2
    if not args.subject.strip():
        print("  A subject is required. An unsubjected mail to a colleague is "
              "a small discourtesy the sender will not notice until it is sent.")
        return 2
    body_lines, unwrapped = O.unwrap(text)
    if unwrapped:
        print(f"  {unwrapped} hard-wrapped line(s) were joined back into "
              f"paragraphs, so the mail reflows to the reader's window.")
    lines = ([] if args.no_banner else [BANNER, ""]) + body_lines

    print(f"  Preparing (NOT sending):\n    Subject: {args.subject}\n"
          f"    To: {', '.join(args.to)}"
          + (f"\n    Cc: {', '.join(args.cc)}" if args.cc else "") + "\n")

    if not args.web:
        return compose_com(args.to, args.cc, args.subject, lines)

    if M.sync_playwright is None:
        print("Playwright is not installed.  py -m pip install playwright")
        return 2

    with M.sync_playwright() as pw:
        browser, page = M.attach(pw, M.URLS["mail"])
        try:
            page.wait_for_load_state("domcontentloaded", timeout=60000)
            M.require_sign_in(page)
            page.wait_for_timeout(2000)
            M.dismiss_prompts(page)

            if not M.poll(lambda: M.js(page, JS_NEW_MAIL), seconds=25):
                print("  Could not find the New mail command. Nothing was created.")
                return 1
            page.wait_for_timeout(2500)
            M.dismiss_prompts(page)

            resolved = []
            for address in args.to:
                who = add_recipient(page, "to", address)
                if not who:
                    print(f"  No address-book match for {address!r}. Stopping "
                          f"with the draft open and nothing sent.")
                    return 1
                resolved.append(who)
            for address in args.cc:
                who = add_recipient(page, "cc", address)
                if not who:
                    print(f"  No address-book match for Cc {address!r}. Stopping.")
                    return 1
                resolved.append(f"cc: {who}")

            spot = M.poll(lambda: M.js(page, JS_FIELD,
                                       {"name": SUBJECT_NAMES, "exact": False}),
                          seconds=15)
            if not spot:
                print("  The subject field never appeared, so the subject was "
                      "not set. Stopping with the draft open. An earlier "
                      "version skipped this field and still reported success, "
                      "and the draft went out for review with no subject.")
                return 1
            page.mouse.click(spot["x"], spot["y"])
            page.keyboard.insert_text(args.subject)
            page.wait_for_timeout(400)
            written = M.js(page, JS_FIELD_VALUE, SUBJECT_NAMES) or ""
            if M.clean(written) != M.clean(args.subject):
                print(f"  The subject field holds {written!r}, not "
                      f"{args.subject!r}. Stopping with the draft open.")
                return 1

            state = M.poll(lambda: (lambda s: s if s.get("found") else None)(
                M.js(page, JS_BODY) or {}), seconds=20)
            if not state:
                print("  The message body did not open. The draft is open with "
                      "recipients and subject; nothing was sent.")
                return 1
            # OWA drops the signature into every new compose, so a body is not
            # empty to begin with. The baseline is what was there BEFORE typing;
            # only a change from that means somebody else has been in the window.
            baseline = M.clean(state.get("text", ""))
            page.mouse.click(state["x"], state["y"])
            page.wait_for_timeout(400)
            # Land at the very top, or the message is written under the signature.
            page.keyboard.press("Control+Home")
            for n, line in enumerate(lines):
                if n:
                    page.keyboard.press("Enter")
                if line:
                    page.keyboard.insert_text(line)
            page.wait_for_timeout(800)

            after = M.clean((M.js(page, JS_BODY) or {}).get("text", ""))
            wanted = M.clean("\n".join(lines))
            ok = wanted[:200] in after
            # The signature was in the baseline; it must still be there.
            signature_kept = not baseline or baseline[-120:] in after

            raw_pills = M.js(page, JS_PILLS)
            pills = ([M.clean(p) for p in raw_pills if M.clean(p)]
                     if isinstance(raw_pills, list) else None)
            page.bring_to_front()
            M.dismiss_prompts(page)
            page.wait_for_timeout(600)
            page.screenshot(path="draft_ready.png")

            print(f"  Recipients resolved: {'; '.join(resolved)}")
            if pills:
                print(f"  Chips on the form: {len(pills)}  ({'; '.join(pills)})")
                if len(pills) > len(resolved):
                    print(f"  WARNING: {len(pills)} chips for {len(resolved)} "
                          f"recipient(s). Check for duplicates before sending.")
            else:
                # Silence here once hid a draft addressed to the same man three
                # times: the query matched nothing and printed nothing.
                print("  I could NOT read the recipient chips back from the "
                      "page, so I cannot confirm who is on this draft or "
                      "whether anyone was added twice.")
                print("  Check the To and Cc fields by eye before sending.")
            print(f"  Body: {len(after)} characters. "
                  f"{'Matches what was written.' if ok else 'DOES NOT MATCH -- read it.'}")
            if baseline and not signature_kept:
                print("  WARNING: the text that was in the body before typing "
                      "(your signature) is no longer there. Check the draft.")
            print("\n  It has NOT been sent. Check the recipients by eye -- a "
                  "resolved chip shows a display name, not an address -- then "
                  "press Send yourself.")
            print("  Screenshot: draft_ready.png")
            return 0 if ok else 1
        finally:
            M.release(browser, keep_open=True)  # the unsent draft must survive


if __name__ == "__main__":
    sys.exit(main())
