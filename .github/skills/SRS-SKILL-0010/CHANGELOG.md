# Changelog — SRS-SKILL-0010 Outlook Interaction

## 1.3.1 — 2026-09-18

**Found during a live demo: with the desktop path blocked by policy and the
browser path broken by an OWA change, the skill had no working way to compose a
mail on a standard corporate machine.**

- **OWA renamed the subject field and `--web` stopped working entirely.** The
  locator matched `aria-label` starting "add a subject"; OWA now labels that
  input `Subject` and uses "Add a subject" as the PLACEHOLDER, so the poll timed
  out on an element that was visible the whole time. Fields are now matched
  against several candidate names, on both label and placeholder, and the
  read-back uses the identical predicate -- it had the same bug, which would
  have made the read-back silently inspect nothing.
- **The recipient-chip query matched nothing, and silence looked like success.**
  A To field visibly holding three chips returned an empty list, and the count
  was printed only when the list was non-empty -- so an unreadable form and a
  clean run produced identical output. Three attempts at one mail left a draft
  addressed to the same person three times, and nothing said so. The selector is
  widened, and an empty result is now reported as **unverifiable** rather than as
  zero recipients: if the recipients cannot be read back, the run says so and
  tells you to check by eye. More chips than recipients raises a duplicate
  warning.
- **The "someone else typed in this window" guard fired on your own
  signature.** OWA puts the signature into every new compose, so a body is never
  empty to begin with. The body is now baselined at compose-open and only a
  change from that baseline stops the run -- keeping the real protection and
  losing the false positive. The message is also typed at the top (Control+Home)
  rather than wherever the signature left the cursor, and the run warns if the
  text that was there beforehand has gone.

## 1.3.0 — 2026-09-18

**The desktop path could not address a mail at all on a standard corporate
build, and said so with a stack trace.**

- **The Outlook Object Model Guard is now handled rather than hit.** Where
  policy denies address-book access -- `adminsecuritymode=3` with the prompts
  disabled, which appears to be the normal configuration -- `Recipients.Add`
  aborts. That surfaced as an unhandled `pywintypes.com_error` with no message
  and no guidance. It is now recognised, reported in plain words, and the mail
  is addressed from the string you supplied instead.
- **When an address is not known, the skill ASKS.** It never infers one: not
  from a name, not from the organisation's usual address pattern, not from
  another message. You either supply the address, which is used exactly as
  typed, or the recipient field is **left empty** for you to complete in
  Outlook. The second is a real choice, not a failure -- a draft with the right
  words and no recipient is safer than one addressed to a guess. Either way the
  output states that the recipient was not verified against the address book.
- **Reading a draft back cannot work under that policy, so it no longer
  pretends to.** The guard blocks reads as well as writes: the body and the
  recipients of a saved item both abort. The verification step used to raise
  AFTER the draft had been saved, reporting a failure that had not happened.
  It now separates "differs" from "could not be read", and says the draft is
  saved but unchecked rather than claiming a success it has not earned.
- **Hard-wrapped body files arrived squeezed.** Plain-text mail honours every
  newline, so a file wrapped at 80 columns -- which is how every editor and
  every assistant writes one -- reached the reader as a narrow ragged column
  that could not reflow. A real recipient's first comment was that it looked
  squeezed. Wrapped lines are now joined back into paragraphs, leaving list
  items, indented lines and quotes alone, and the run says how many it joined.
- **`connect()` documented a trap it did not avoid.** Late binding covers the
  Application object only; `GetNamespace('MAPI')` is wrapped through the gen_py
  cache regardless, so a half-written cache raised the very error the docstring
  claimed to prevent -- and the message blamed Outlook for being absent while it
  was running and reachable. The failure is now identified for what it is and
  the exact folder to remove is printed. The skill does not delete it: nothing
  in this library deletes anything on your machine.

## 1.2.1 — 2026-09-15

**The reply gate could accept an unrelated message.** Words of three letters
or fewer are dropped as carrying no identity, which is right -- but when that
left a single word, the gate stopped identifying anything. Asking to reply to
"TTC Line 2" collapsed to {line} and matched a mail titled "Line management
policy". A reply drafted against the wrong conversation is the failure this
gate exists to prevent.

When a request now reduces to one significant word, the whole phrase must
appear in the subject instead. "Timesheets" still finds "Missing timesheets for
August"; "TTC Line 2" no longer finds anything about line management.

Found by an independent audit.

**Fixed: every read-only run left a whole browser behind.** `browser.close()`
on a CDP connection only DETACHES -- measured, ten processes before the call
and eleven after. Eighteen accumulated in one evening. Because the automation
window shares the user's Edge taskbar entry, clicking Edge activated one of
them and showed the desktop, and a stale thumbnail persisted afterwards, so
Edge appeared broken when it was not. Reading scripts now quit the browser they
started; drafting scripts keep it open, because leaving an unsent draft on
screen is the point of them. `py scripts\srs_m365.py --close` also reported
"No automation browser was running" while closing eleven processes -- it counted
only the ones that needed force-killing.

**Fixed: the automation window is no longer parked off-screen.** It used to
launch at -2400,-2400 to stay out of the way. That is what made it invisible
and what hijacked the taskbar entry. It now opens maximised like any other
window, so you can watch what your assistant is doing.


## 1.2.0 — 2026-09-15

**Outlook desktop is now the default route; the browser is `--web`.** Asked why
the skill automated a web page to do something COM has done reliably for years,
there was no good answer. Over COM every value the skill sets is a property it
can read back off the saved draft, which turns two of the three defects below
into things that cannot happen rather than things that are handled.

Three defects, all from one real session.

- **Fixed: `draft_new.py` silently dropped the subject.** The subject step was
  `if spot:` after a 15-second poll. When the poll timed out it skipped the
  field and still printed a success summary, so a draft was created with an
  empty subject and reported as fine. The user found it afterwards by re-reading
  the field with a script of their own. On the desktop path the subject is now
  assigned and read back off the saved item; on the web path a missing field
  stops the run, and the field is read back after typing. **The lesson is wider
  than this script: typing into a field is not evidence that the value arrived,
  and a step that can be skipped must not share an exit code with one that
  succeeded.**
- **Fixed: `read_mail.py --thread N` could not open a collapsed conversation.**
  It clicked coordinates captured during the listing, which land on the
  conversation chevron for a collapsed row: the chevron expands, the reading
  pane never changes, and the run looked successful. `draft_reply.py` then
  correctly refused to type into a message that did not match — the gate
  working as intended — which is why the user fell back to composing a new mail
  and the reply went out unthreaded. The desktop path has no rows to click at
  all. The web path now re-finds the row by id at click time, aims at the
  subject rather than the row, and **verifies the reading pane is showing the
  message that was asked for** before reading anything.
- **Fixed: `SKILL.md` documented `draft_reply.py --thread`, which did not
  exist.** Now it does, and it means something better than it used to: it
  replies to item N of the last listing, starting from the message itself, so
  the reply stays in the conversation. A new gate check, `documented_flags`,
  now reconciles every flag shown in a SKILL.md against the argument parser of
  the script it is shown for, and blocks on a mismatch. Both files had been
  individually correct and only disagreed with each other, which is why nothing
  caught it.

## 1.1.0 — 2026-09-14

**Added a compose path.** `draft_new.py` writes a new mail from nothing —
recipients, Cc, subject, body — and leaves it as a draft. It still cannot send.

Reported by a user on first real use: the skill drafted replies, reply-alls and
forwards but had no way to start a new mail, and nothing said so. The
description was accurate, which made it a gap rather than a defect — but a gap
only discoverable by hitting it.

**Lesson applied, and worth applying elsewhere: when a skill lists what it does,
it should also name the nearest thing it does not do.** The absence of Send was
stated plainly and prominently; the absence of Compose was not stated at all,
and one is as surprising as the other. `SKILL.md` now carries a *What this skill
does NOT do* table.

Composing moves the risk. A reply is anchored to an open message that can be
checked; a new mail has no anchor, so the whole risk is the recipient:

- A resolved recipient chip shows only a **display name** — the address is
  nowhere in the page afterwards. So the address is verified while the
  suggestion is still on screen, and the element under the cursor is confirmed
  to still be that suggestion before it is clicked.
- A migrated colleague appears **twice** in the address book under one display
  name. The skill warns when more than one entry matched rather than assuming
  the first is right.
- The `to` field is matched on an exact aria-label. A loose pattern also
  matches Cc, Bcc and any address field the reading pane is showing.

**Fixed: the sender gate was open.** `header_matches` split the address on `@`
and kept the domain. Since everyone shares one company domain, *every* sender
matched every other sender — the check that stops a reply reaching the wrong
thread would have passed on any mail in the company. Now matched on the local
part only. Found by the self-test added the same day.

## 1.0.0 — 2026-09-13

First release.

Reads the signed-in user's own mailbox and prepares replies that the user sends
themselves.

**The package contains no send path.** Not a disabled one — an absent one.
There is no `--send` argument, no confirmation that unlocks sending and no
configuration entry, so there is nothing to switch on. That can be verified by
searching the package, which is a stronger assurance than a setting.

Also refuses, structurally: delete, move, archive, flag, categorise, mark read
or unread, open attachments, and read any mailbox other than the signed-in
user's own.

Design decisions worth recording:

- Drives the web client through a signed-in Edge profile rather than the Graph
  API. Conditional Access refuses client-credential flows on this tenant, so
  the browser is the only route that works — and it turns out to be the better
  security posture anyway, because the automation acts as the user, holds no
  credential of its own and cannot obtain one.
- Message bodies are collected only for a thread the user names. A listing
  answers most questions without putting two dozen Confidential bodies into a
  conversation with a model.
- `draft_reply.py` polls the open message header until it matches the subject
  or sender given on the command line, and aborts if it never does. The client
  repaints the previously open message for several seconds after routing, and a
  reply typed into the wrong thread is the failure that actually matters here.
- Refuses to overwrite text in a reply box that the skill did not write.
- Reports scope — how many messages were scanned, what was filtered, what was
  not collected — so a partial read is never presented as a complete answer.
- Distinguishes "nothing found" from "not signed in", which otherwise look
  identical and produce a confidently empty summary.
