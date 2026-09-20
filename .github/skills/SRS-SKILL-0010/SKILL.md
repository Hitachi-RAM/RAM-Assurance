---
id: SRS-SKILL-0010
name: srs-outlook-interaction
title: Outlook Interaction
version: 1.3.1
released: 2026-09-18
status: released
classification: Confidential
owner: Frederick Bourgoin
support_contact: frederick.bourgoin@hitachirail.com
certificate: SRS-CERT-0010-1.2.1
install_target: .github/skills
site_config: external
check_after: 2026-12-12
supersedes: null
superseded_by: null
shared_modules: [srs_m365.py]
requires:
  python: ">=3.9"
  packages: ["playwright"]
description: >
  OUTLOOK MAIL SKILL. Reads your mailbox and prepares mail you send yourself.
  USE WHEN: someone asks what is in their inbox, what they have missed, what is
  still waiting on a reply, or to summarise a long thread; when they want a
  reply, a chase-up, a forward or a NEW mail written for them; when they need to
  find the mail where something was agreed.
  DO NOT USE FOR: sending. This skill cannot send, delete, move, archive, flag
  or mark anything read, and cannot open attachments. Every mail it writes --
  reply or new -- is left as a draft for the person to read, change and send
  themselves. DO NOT USE to read anybody else's mailbox, including a shared or
  delegated one.
---

# SRS-SKILL-0010 — Outlook Interaction

Reads your mail and writes your replies. **You send them.**

The skill stops one step before the Send button, every time, for everyone. That
is not a setting that can be turned off — there is no code in this package that
clicks Send.

---

## Why it stops there

A mail that goes out under your name is your statement, and you are answerable
for it. An assistant that drafts well and sends nothing leaves you in exactly
the position you were always in: you decide what your colleagues and customers
hear from you. An assistant that sends removes that, and adds nothing you
wanted.

It also fails safe. A skill that drafts the wrong reply costs you ten seconds
reading it. A skill that sends the wrong reply costs a relationship.

---

## What it can and cannot do

| It will | It will not |
|---|---|
| List and read your inbox and folders | Send anything, ever |
| Search by sender, subject, date, text | Delete, archive or move a message |
| Summarise a long thread | Mark read or unread, flag or categorise |
| Draft a reply, a reply-all or a forward | Empty Deleted Items or Junk |
| Leave the draft open for you to check | Open a shared or delegated mailbox |
| Tell you what it did not read | Download or open attachments |

There is no `--send` argument, no confirmation prompt that unlocks sending, and
no configuration file entry. The absence is the control.

---

## It acts as you, and holds nothing

Sign-in happens once, in a real browser window, with your own credentials typed
by you. The skill never sees your password and cannot store one. Afterwards it
reuses the signed-in profile.

It therefore sees exactly what you see — no more. It cannot reach a mailbox you
cannot reach, and if your access is removed the skill loses it at the same
moment.

**Your mail is Confidential and often personal.** Read the section at the end of
this file on what leaves your machine before using this on anything sensitive.

---

## Run it

```powershell
py scripts\read_mail.py --folder Inbox --count 25          # what is in there
py scripts\read_mail.py --from "alice" --days 30          # from one person
py scripts\read_mail.py --search "TTC Line 2" --days 90    # find the mail
py scripts\read_mail.py --thread 3 --full                  # read one properly
py scripts\draft_reply.py --thread 3 --subject "..." --body reply.md
py scripts\draft_new.py --to "someone@example.com" --subject "..." --body note.md
py scripts\srs_m365.py --close                             # shut the browser
```

These use **Outlook desktop**, which needs no sign-in and marks nothing read.
Add `--web` to any of the first three to use the browser instead, on a machine
with no Outlook desktop; the first browser run opens a window and asks you to
sign in, and later runs do not.

---

## What this skill does NOT do

Stated here because the absence of Send is obvious and the other absences are
not, and a gap you only discover by hitting it is worse than one you were told
about.

| Not available | What to do instead |
|---|---|
| **Send** anything | Read the draft and press Send yourself |
| Delete, move, archive, flag, mark read | Do it in Outlook |
| Open or read an attachment | Open it yourself if you need it |
| Read a shared or delegated mailbox | Ask the owner to run it |
| Reply to a message you have not named | Give `--subject` or `--sender` |
| Recall, resend, or edit a sent message | Nothing here touches Sent Items |
| Rules, signatures, out-of-office | Outlook settings |

Both drafting paths exist: **`draft_reply.py`** replies to a message you name
from the last listing, and **`draft_new.py`** composes from nothing. Neither
sends.

---

## Reading

`read_mail.py` writes `mail_data.json` and prints a summary. The JSON is what
the assistant reads; the summary is what you read.

Each item carries sender, subject, received time, whether it is unread, whether
it has attachments, the preview line, and — with `--full` — the body text.

**Bodies are not collected unless you ask.** A listing of 25 subjects tells the
assistant enough to answer "what is waiting on me" without putting 25 message
bodies into a conversation. Ask for the body of the thread you actually care
about.

### What it deliberately does not read

- Attachments. It reports that they exist and their file names. Opening a
  document is a different decision, and a spreadsheet full of salaries should
  not be pulled into a chat because someone asked what was in their inbox.
- Other people's mailboxes, including ones you have delegate rights to. The
  skill checks the mailbox it landed in and stops if it is not yours.
- Anything in a folder you did not name.

---

## Drafting

Two routes to the mailbox, and the default is the better one.

**Outlook desktop (default).** Everything the skill sets is a property it can
read back off the saved draft: the subject, the body, and the resolved SMTP
address behind every recipient. After saving, the draft is re-opened from
Outlook and compared against what was asked for, and any difference stops the
run. This matters more than it sounds. In the browser the subject is typed into
a field, and an earlier version treated the field appearing as proof the
subject had arrived: when the wait timed out it skipped the field and still
reported success, and a draft went out for review with no subject at all.

**`draft_reply.py --thread N`** replies to item N of the last `read_mail.py`
listing. It starts from the message itself, so the reply stays in the
conversation, and no conversation row has to be found and clicked. It still
checks the message against the `--subject` or `--sender` you named and refuses
if they disagree. With `--web` it instead replies to whatever is open in the
browser, polling the open header until it matches, because the web client
paints the previously-open message for several seconds after routing.

**`draft_new.py`** composes from nothing, so there is no open message to check
against and the whole risk moves to the recipient. On the desktop path an
unresolved recipient stops the run before anything is saved. In the browser
(`--web`) it is harder: a resolved recipient chip shows only a **display name** — the
address is nowhere in the page afterwards — so the only moment an address can be
verified is while the suggestion is still on screen. And a migrated colleague
appears **twice** in the address book under one display name, so "exactly one
suggestion" is never safe. The skill confirms the element under the cursor is
still the intended suggestion before clicking, warns when more than one entry
matched, and reads the subject field back after typing into it.

If the reply box already contains text that the skill did not write, it stops.
That text is yours.

### When the address book cannot be reached

Most corporate builds run the Outlook Object Model Guard, which denies
programmatic access to the address book without even prompting. The skill can
still write the mail; it simply cannot check who the recipient is.

**It must never invent an address.** Not from a name, not from your
organisation's usual `first.last@` pattern, not from an address seen in another
message. A plausible address belonging to the wrong person is precisely the
failure this skill exists to prevent, and it is worse than doing nothing
because it looks right.

So when an address is not known, the assistant **asks**, and takes neither
option without an answer:

1. **you supply the address**, which is then used exactly as you typed it; or
2. **the recipient field is left empty**, and the draft says so, for you to
   complete in Outlook.

The second is a real choice, not a failure. A draft with the right words and no
recipient is useful, and far safer than one addressed to a guess.

Either way the output states that the recipient was **not verified against the
address book** — because that verification is the reason the desktop path
exists, and if it did not happen you are entitled to know.

The same applies to reading a draft back. Where policy blocks it, the skill
says the draft is saved but could not be checked, rather than reporting success
it has not earned.

### Write the body in paragraphs

The body file should have one line per **paragraph**, with blank lines between
them. Plain-text mail honours every newline, so a file hard-wrapped at 80
columns arrives as a narrow ragged column. The skill now joins wrapped lines
back into paragraphs and tells you when it has, leaving list items, indented
lines and quotes alone.

The draft opens with a line saying it was prepared by an assistant. Delete that
line before you send if you like — but decide deliberately, because your
recipient is entitled to know whether they are reading you.

---

## What the assistant should tell you

When it has read your mail, it should say what it read: which folder, how many
items, over what period, and what it skipped. "You have three things waiting"
is not useful if it looked at 25 of 400 messages and did not say so.

If it could not read something — a protected message, a folder it could not
open — it should say that too, rather than producing a tidy summary of the part
that happened to work.

---

## Mail is Confidential, and some of it is personal

Anything the assistant reads becomes part of the conversation, and that
conversation goes to the model. Before you point this at a mailbox:

- Personal data in mail — health, performance, grievance, recruitment, pay —
  should not be summarised by an assistant without a reason you could defend.
- Customer and contract correspondence is Confidential and sometimes carries
  obligations about where it may be processed.
- A thread you did not originate may contain other people's confidences.

Narrow the read. `--search` and `--from` with a date window exist so you can
answer a question without opening the whole mailbox.

---

## Troubleshooting

**"Still on the sign-in page."** Conditional Access wants a fresh
authentication. Sign in in the window; nothing was read.

**The browser will not start.** A previous run left one holding the profile.
`py scripts\srs_m365.py --close`. It closes only the automation browser, matched
on the profile folder — your own Edge windows are untouched.

**It found the wrong message.** The header gate should have stopped it. Report
that, because it means the gate is wrong, and it is the only thing standing
between a draft and the wrong recipient.

**Nothing at all was found.** Check you were signed in. An empty result and a
locked door look identical unless the skill says which it was — this one does.

---

## Limitations, and where responsibility sits

This skill is deliberately limited. The limits are not gaps waiting to be
filled: they are what keeps it inside Hitachi Rail governance.

- **It acts as you.** It can reach only what your own access already allows, and
  it holds no credentials of its own. It cannot see anything you could not
  already open yourself.
- **It does not send, delete or destroy.** Where it produces something that
  would leave your machine, it prepares a draft and stops. You read it and you
  send it.
- **It is classified Confidential.** Share it on that basis.

### If you change it

**Modifying this skill so that it exceeds those limits is your decision and your
responsibility, not the maintainer's.** Two things follow, and both are facts
rather than cautions:

1. **The certificate covers these files exactly.** `CERTIFICATE.json` records
   the SHA-256 of every file in the package and states that it is void if any of
   them differs. A modified copy is therefore uncertified by construction —
   nothing has checked it, and nothing can.
2. **Governance applies to the action, not to the tool.** The Acceptable Use and
   AI policies govern what is done and by whom. Removing a safety gate does not
   remove the obligation it was there to meet; it removes the evidence that you
   met it.

### If it will not do something you need

Ask. The answer is often yes, and then it can be done once, checked, and given
to everybody rather than solved privately in a copy nobody can verify.

Contact: frederick.bourgoin@hitachirail.com

