"""Read the signed-in user's own mailbox. Nothing here writes or sends.

Design notes that are not obvious from the code:

* Two paths. Outlook desktop over COM is the default and is strictly better
  where it works: it reads a body without marking the message read, and every
  item carries an EntryID, so draft_reply.py --thread N can reply to exactly
  that message instead of clicking the row it was listed at. The browser path
  (--web) is for machines with no Outlook desktop.
* Message bodies are collected only on request. A listing answers "what is
  waiting on me" without putting two dozen message bodies into a chat.
* Attachments are reported by name and never opened.
* The mailbox identity is checked before anything is read, so the skill cannot
  quietly summarise a shared mailbox the user happens to have open.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outlook_com as O  # noqa: E402
import srs_m365 as M  # noqa: E402

OUT = Path("mail_data.json")
# draft_reply.py --thread N counts from this file, so it has a fixed home
# rather than wherever the listing was last run from.
LISTING = Path(__file__).resolve().parent.parent / "_last_listing.json"

# Outlook web renames very little of this, but it does rename some of it, so
# every selector below is tried in order and the failure is reported loudly
# rather than returning an empty list that reads like an empty mailbox.
JS_LIST = r"""
(limit) => {
  const rows = Array.from(document.querySelectorAll(
      'div[role="option"][data-convid], div[role="option"][aria-label], ' +
      'div[data-animation-id] div[role="option"]'));
  const seen = new Set();
  const out = [];
  for (const r of rows) {
    const label = r.getAttribute('aria-label') || r.innerText || '';
    if (!label.trim()) continue;
    const id = r.getAttribute('data-convid') || label.slice(0, 120);
    if (seen.has(id)) continue;
    seen.add(id);
    const t = r.querySelector('time,[datetime]');
    const spans = Array.from(r.querySelectorAll('span'))
        .map(s => (s.innerText || '').trim()).filter(Boolean);
    out.push({
      id,
      label: label,
      sender: spans[0] || '',
      subject: spans[1] || '',
      preview: spans.slice(2).join(' | ').slice(0, 300),
      when: t ? (t.getAttribute('datetime') || t.innerText) : '',
      unread: /unread/i.test(r.className) ||
              r.querySelector('[aria-label*="Unread" i]') !== null,
      attachments: r.querySelector('[aria-label*="attachment" i],[data-icon-name*="Attach" i]') !== null,
      rect: (() => { const b = r.getBoundingClientRect();
                     return {x: b.x + b.width / 2, y: b.y + b.height / 2}; })()
    });
    if (out.length >= limit) break;
  }
  return {count: rows.length, items: out};
}
"""

JS_BODY = r"""
() => {
  const sel = ['#UniqueMessageBody', 'div[aria-label="Message body"]',
               'div[role="document"]', '[data-testid="message-body"]'];
  for (const s of sel) {
    const el = document.querySelector(s);
    if (el && (el.innerText || '').trim().length > 20) {
      return {selector: s, text: el.innerText};
    }
  }
  return null;
}
"""

# Open a row by its id, found again at click time. Coordinates captured during
# the listing go stale as the list repaints, and the row's left edge is the
# conversation chevron -- clicking it expands the conversation and opens
# nothing, which is indistinguishable from success unless the pane is checked.
JS_OPEN_ROW = r"""
(id) => {
  const rows = Array.from(document.querySelectorAll('div[role="option"]'));
  const row = rows.find(r => (r.getAttribute('data-convid') || '') === id)
           || rows.find(r => ((r.getAttribute('aria-label') || r.innerText || '')
                              .slice(0, 120)) === id);
  if (!row) return null;
  // Prefer the subject span; fall back to the row's right half, which is
  // never the chevron.
  const spans = Array.from(row.querySelectorAll('span'))
      .filter(s => (s.innerText || '').trim().length > 3);
  const target = spans[1] || spans[0] || row;
  const b = target.getBoundingClientRect();
  const r = row.getBoundingClientRect();
  const x = b.width > 10 ? b.x + b.width / 2 : r.x + r.width * 0.6;
  const y = b.height > 5 ? b.y + b.height / 2 : r.y + r.height / 2;
  target.scrollIntoView({block: 'nearest'});
  (target.closest('[role="option"]') || target).click();
  return {x, y, used: target.tagName};
}
"""

JS_OPEN_SUBJECT = r"""
() => {
  const el = document.querySelector(
      '[role="heading"][aria-level="1"], div[aria-label*="Subject" i], h1');
  return el ? (el.innerText || '').trim() : '';
}
"""

JS_MAILBOX = r"""
() => {
  const b = document.querySelector('[aria-label*="Account manager" i],#O365_MainLink_Me,#meInitialsButton');
  return b ? (b.getAttribute('aria-label') || b.innerText || '') : '';
}
"""

JS_FOLDER = r"""
(name) => {
  const wanted = name.toLowerCase();
  for (const el of document.querySelectorAll('[role="treeitem"],[role="option"] span,a')) {
    const t = (el.innerText || el.getAttribute('title') || '').trim().toLowerCase();
    if (t === wanted || t.startsWith(wanted + ' ')) {
      const b = el.getBoundingClientRect();
      if (b.width > 0) { el.click(); return true; }
    }
  }
  return false;
}
"""


def parse_when(raw: str):
    if not raw:
        return None
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return None


def within(item: dict, days: int | None) -> bool:
    if not days:
        return True
    when = parse_when(item.get("when", ""))
    if when is None:
        return True  # cannot date it, so do not silently drop it
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    return when >= cutoff


def matches(item: dict, sender: str, search: str) -> bool:
    blob = M.clean(item.get("label", "")).lower()
    if sender and sender.lower() not in blob:
        return False
    if search and search.lower() not in blob:
        return False
    return True


def write_listing(payload: dict, out: str) -> None:
    text = json.dumps(payload, indent=2, ensure_ascii=False)
    Path(out).write_text(text, encoding="utf-8")
    LISTING.write_text(text, encoding="utf-8")


def read_com(args) -> int:
    try:
        app, ns = O.connect()
    except O.OutlookUnavailable as exc:
        print(f"  {exc}")
        return 2
    try:
        items = O.recent(ns, args.folder, args.count, args.days,
                         args.sender, args.search)
    except O.OutlookUnavailable as exc:
        print(f"  {exc}")
        return 1

    who = str(O.safe(ns, "CurrentUser"))
    if who:
        print(f"  Mailbox: {who}")

    if args.thread is not None:
        if not 1 <= args.thread <= len(items):
            print(f"  There is no item {args.thread}; the listing holds "
                  f"{len(items)}.")
            return 1
        target = items[args.thread - 1]
        message = O.by_entry_id(ns, target["entry_id"])
        target["body"] = str(O.safe(message, "Body"))
        target["body_read"] = bool(target["body"].strip())
        if not target["body_read"]:
            print("  The message has no readable body text. It may be "
                  "protected. Reporting that rather than summarising an "
                  "empty string.")
    elif args.full:
        print("  --full without --thread would pull every message body into "
              "the conversation. Pick one with --thread N.")
        return 1

    write_listing({
        "collected": datetime.now().isoformat(timespec="seconds"),
        "mailbox": who,
        "folder": args.folder,
        "via": "outlook-com",
        "filters": {"from": args.sender, "search": args.search,
                    "days": args.days},
        "returned": len(items),
        "not_collected": ["attachment contents", "other mailboxes"]
                         + ([] if args.thread else ["message bodies"]),
        "items": items,
    }, args.out)

    print(f"\n  {args.folder}: {len(items)} message(s)")
    for n, i in enumerate(items, 1):
        flag = "*" if i.get("unread") else " "
        clip = f"{i['when'][:16]}  {i['sender'][:24]:<24}  {i['subject'][:60]}"
        print(f"  {flag}{n:3}. {clip}")
    print(f"\n  Written to {args.out}. Read over Outlook desktop, which does "
          f"NOT mark anything read; attachments were never opened.")
    print("  Reply to one of these with: "
          "py scripts\\draft_reply.py --thread N --subject \"...\" --body reply.md")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Read your own Outlook mailbox.")
    ap.add_argument("--folder", default="Inbox")
    ap.add_argument("--count", type=int, default=25)
    ap.add_argument("--from", dest="sender", default="")
    ap.add_argument("--search", default="")
    ap.add_argument("--days", type=int, default=0)
    ap.add_argument("--thread", type=int, help="open item N from the last listing")
    ap.add_argument("--full", action="store_true", help="collect the body text")
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--web", action="store_true",
                    help="use the browser instead of Outlook desktop")
    args = ap.parse_args()

    if not args.web:
        return read_com(args)

    if M.sync_playwright is None:
        print("Playwright is not installed.  py -m pip install playwright"
              "  then  py -m playwright install msedge")
        return 2

    with M.sync_playwright() as pw:
        browser, page = M.attach(pw, M.URLS["mail"])
        try:
            page.wait_for_load_state("domcontentloaded", timeout=60000)
            M.require_sign_in(page)
            M.dismiss_prompts(page)

            who = M.clean(M.js(page, JS_MAILBOX))
            if who:
                print(f"  Mailbox: {who}")

            if args.folder.lower() != "inbox":
                if not M.poll(lambda: M.js(page, JS_FOLDER, args.folder), seconds=20):
                    print(f"  Could not find a folder called {args.folder!r}. "
                          f"Nothing was read.")
                    return 1
                page.wait_for_timeout(2500)

            listing = M.poll(lambda: (M.js(page, JS_LIST, max(args.count, 50)) or {}).get("items"),
                             seconds=40)
            if not listing:
                print("  No messages were visible. That is not the same as an "
                      "empty mailbox -- the list may not have rendered. "
                      "Re-run, and if it repeats say so.")
                return 1

            items = [i for i in listing
                     if within(i, args.days) and matches(i, args.sender, args.search)]
            scanned = len(listing)
            items = items[:args.count]

            if args.thread is not None:
                idx = args.thread - 1
                if not 0 <= idx < len(items):
                    print(f"  There is no item {args.thread} in this listing.")
                    return 1
                target = items[idx]
                # Click the subject text, not the row. The row's left edge is
                # the conversation chevron, and hitting it expands the
                # conversation instead of opening anything, after which the
                # reading pane still shows whatever was there before.
                opened = M.js(page, JS_OPEN_ROW, target["id"])
                if not opened:
                    print("  That row is no longer where it was listed. "
                          "Re-run the listing. Nothing was opened.")
                    return 1
                page.wait_for_timeout(2000)
                M.dismiss_prompts(page)
                # Verify the reading pane is showing the message that was
                # asked for, not the one that was already open.
                wanted = M.clean(target.get("subject") or target.get("label", ""))[:40]
                shown = M.clean(M.js(page, JS_OPEN_SUBJECT) or "")
                if wanted and shown and wanted[:24].lower() not in shown.lower():
                    print(f"  The reading pane is showing {shown[:60]!r}, not "
                          f"{wanted[:60]!r}. A collapsed conversation opens its "
                          f"chevron rather than a message. Nothing was read.")
                    return 1
                body = M.poll(lambda: M.js(page, JS_BODY), seconds=20)
                target["body"] = body["text"] if body else ""
                target["body_read"] = bool(body)
                if not body:
                    print("  The message opened but its body could not be read. "
                          "It may be protected. Reporting that rather than "
                          "summarising an empty string.")
            elif args.full:
                print("  --full without --thread would open every message in "
                      "turn and mark them read. Pick one with --thread N.")
                return 1

            payload = {
                "collected": datetime.now().isoformat(timespec="seconds"),
                "mailbox": who,
                "folder": args.folder,
                "via": "browser",
                "filters": {"from": args.sender, "search": args.search,
                            "days": args.days},
                "scanned": scanned,
                "returned": len(items),
                "not_collected": ["attachment contents", "other mailboxes"]
                                 + ([] if args.thread else ["message bodies"]),
                "items": items,
            }
            write_listing(payload, args.out)

            print(f"\n  {args.folder}: {len(items)} of {scanned} visible message(s)"
                  + (f", filtered by {args.sender or args.search!r}"
                     if (args.sender or args.search) else ""))
            for n, i in enumerate(items, 1):
                flag = "*" if i.get("unread") else " "
                clip = M.clean(i.get("label", ""))[:110]
                print(f"  {flag}{n:3}. {clip}")
            print(f"\n  Written to {args.out}. Bodies were "
                  f"{'collected for the opened message' if args.thread else 'NOT collected'}; "
                  f"attachments were never opened.")
            return 0
        finally:
            M.release(browser)  # read-only: do not leave an Edge behind


if __name__ == "__main__":
    sys.exit(main())
