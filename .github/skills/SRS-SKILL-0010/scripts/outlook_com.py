"""Outlook via COM, for the machines that have it.

Why this exists alongside the browser path: the browser is the only option on a
machine with no Outlook desktop, but for everything it CAN do, COM is better in
the one way that matters here -- what you set is a property you can read back.

  * A subject typed into a web field is confirmed only by the field appearing.
    A subject assigned over COM can be re-read off the saved item and compared.
  * A recipient chip in the web client shows a display name and hides the
    address. A COM recipient resolves against the address book and exposes the
    SMTP address, so "is this the right person" stops being a judgement call.
  * A reply built by clicking a conversation row depends on the row being where
    it was a moment ago. ``MailItem.Reply()`` keeps the conversation without any
    of that, because it starts from the message itself.

Safety, deliberately narrow:
  * ``Send`` is never called anywhere in this module, and the gate checks that.
  * Outlook is one instance per session, so this ATTACHES to the user's running
    copy. It never calls ``Quit`` and never closes a window it did not open.
  * Nothing is deleted, moved, flagged, or marked read. Reading ``.Body`` over
    COM does not mark a message read -- unlike opening it in the client.
"""
from __future__ import annotations

import datetime as _dt
import re
from pathlib import Path

OL_MAIL_ITEM = 0
OL_FOLDER_INBOX = 6
OL_FOLDER_SENT = 5
OL_FOLDER_DRAFTS = 16

FOLDERS = {"inbox": OL_FOLDER_INBOX, "sent": OL_FOLDER_SENT,
           "drafts": OL_FOLDER_DRAFTS}

_NUMBERED = re.compile(r"\d+[.)]\s")


class OutlookUnavailable(RuntimeError):
    """Outlook desktop could not be reached. The caller offers the web path."""


class AddressBookBlocked(RuntimeError):
    """Policy denies address-book access. The mail can still be drafted."""


# The Outlook Object Model Guard returns these when a policy denies access to
# the address book. Measured on a standard corporate build: adminsecuritymode=3
# with promptoomaddressbookaccess=0 means deny, and do not even prompt.
_GUARD_CODES = (-2147467260, -2147467259)


def is_policy_block(exc: Exception) -> bool:
    """True if this exception is the Object Model Guard rather than a real fault."""
    for attr in ("hresult", "args"):
        value = getattr(exc, attr, None)
        if isinstance(value, int) and value in _GUARD_CODES:
            return True
        if isinstance(value, tuple):
            for part in value:
                if isinstance(part, int) and part in _GUARD_CODES:
                    return True
    return "operation aborted" in str(exc).lower()


def connect():
    """Attach to the running Outlook, late-bound.

    Late binding is used for the Application object, but it does NOT avoid the
    generated cache: the object returned by ``GetNamespace('MAPI')`` is wrapped
    through gen_py regardless, so a half-written cache still raises
    ``AttributeError: ... has no attribute 'CLSIDToClassMap'`` from inside the
    namespace call. An earlier docstring claimed otherwise and the resulting
    message blamed Outlook for being absent while it was running and reachable.
    A stale cache is therefore named, so you can remove it yourself. This skill
    deletes nothing: the folder sits under your profile and the path is printed
    rather than acted on.
    """
    try:
        from win32com.client import dynamic
    except ImportError as exc:
        raise OutlookUnavailable(
            "pywin32 is not installed, so the Outlook desktop path is not "
            "available.  py -m pip install pywin32") from exc

    try:
        app = dynamic.Dispatch("Outlook.Application")
        return app, app.GetNamespace("MAPI")
    except AttributeError as exc:
        raise OutlookUnavailable(
            f"Outlook is running and reachable, but its generated type cache is "
            f"unusable ({exc}). This is not a problem with Outlook or with your "
            f"mail.\n  Delete this folder and run it again -- pywin32 rebuilds "
            f"it automatically:\n    {_gen_py_path()}\n  Or use --web for the "
            f"browser path.") from exc
    except Exception as exc:
        raise OutlookUnavailable(
            f"Outlook desktop did not respond ({type(exc).__name__}). If it "
            f"is not installed or not running, use --web for the browser "
            f"path.") from exc


def _gen_py_path() -> str:
    """Where pywin32 keeps its generated cache, for the user to clear by hand."""
    try:
        import win32com.client.gencache as gencache
        return str(Path(gencache.GetGeneratePath()))
    except Exception:
        return r"%LOCALAPPDATA%\Temp\gen_py"


def safe(obj, name: str, default=""):
    """Property reads on late-bound items raise more often than they should."""
    try:
        value = getattr(obj, name)
        return default if value is None else value
    except Exception:
        return default


def folder(ns, name: str):
    key = (name or "inbox").strip().lower()
    if key in FOLDERS:
        return ns.GetDefaultFolder(FOLDERS[key])
    inbox = ns.GetDefaultFolder(OL_FOLDER_INBOX)
    for i in range(1, safe(inbox.Folders, "Count", 0) + 1):
        sub = inbox.Folders.Item(i)
        if str(safe(sub, "Name")).lower() == key:
            return sub
    raise OutlookUnavailable(
        f"No folder named {name!r}. Known: inbox, sent, drafts, or a folder "
        f"directly under the inbox.")


def recent(ns, folder_name="inbox", count=25, days=0, sender="", search=""):
    """Newest first. Returns dicts, not COM objects: the caller should not be
    holding live references while the user works in Outlook."""
    items = folder(ns, folder_name).Items
    items.Sort("[ReceivedTime]", True)
    if days:
        cutoff = _dt.datetime.now() - _dt.timedelta(days=days)
        items = items.Restrict(
            "[ReceivedTime] >= '" + cutoff.strftime("%m/%d/%Y %I:%M %p") + "'")
        items.Sort("[ReceivedTime]", True)

    want_sender, want_text = sender.lower().strip(), search.lower().strip()
    out = []
    total = safe(items, "Count", 0)
    for i in range(1, total + 1):
        if len(out) >= count:
            break
        try:
            it = items.Item(i)
        except Exception:
            continue
        if str(safe(it, "Class", 0)) != "43":        # olMail only
            if safe(it, "MessageClass", "") and not str(
                    safe(it, "MessageClass")).startswith("IPM.Note"):
                continue
        frm = str(safe(it, "SenderName"))
        addr = str(safe(it, "SenderEmailAddress"))
        subject = str(safe(it, "Subject"))
        if want_sender and want_sender not in (frm + " " + addr).lower():
            continue
        if want_text and want_text not in (subject + " " +
                                           str(safe(it, "Body"))[:2000]).lower():
            continue
        received = safe(it, "ReceivedTime", None)
        out.append({
            "entry_id": str(safe(it, "EntryID")),
            "sender": frm,
            "sender_address": addr,
            "subject": subject,
            "when": str(received)[:19] if received else "",
            "unread": bool(safe(it, "UnRead", False)),
            "attachments": int(safe(safe(it, "Attachments"), "Count", 0) or 0),
            "preview": " ".join(str(safe(it, "Body"))[:400].split()),
        })
    return out


def by_entry_id(ns, entry_id: str):
    try:
        return ns.GetItemFromID(entry_id)
    except Exception as exc:
        raise OutlookUnavailable(
            "That message is no longer in the mailbox at the recorded id. "
            "Re-run the listing and try again.") from exc


def resolve(item, addresses, kind=1) -> list:
    """Add recipients and resolve them against the address book.

    kind: 1 To, 2 Cc. Returns one dict per address. ``resolved`` False means
    the address book did not recognise it -- the caller must stop, because an
    unresolved recipient is the failure that sends mail to the wrong person.

    Where policy denies address-book access the dict carries ``blocked`` True
    instead. That is not an error and not a resolution: the caller may still
    address the mail from a string the USER supplied, and must say that the
    recipient was never checked.
    """
    report = []
    for address in addresses:
        entry = {"requested": address, "resolved": False, "blocked": False,
                 "name": "", "address": "", "kind": "cc" if kind == 2 else "to"}
        try:
            rcp = item.Recipients.Add(address)
            rcp.Type = kind
            entry["resolved"] = bool(rcp.Resolve())
        except Exception as exc:
            if not is_policy_block(exc):
                raise
            entry["blocked"] = True
            report.append(entry)
            continue
        if entry["resolved"]:
            try:
                ae = rcp.AddressEntry
                entry["address"] = str(
                    safe(ae, "GetExchangeUser")
                    and safe(ae.GetExchangeUser(), "PrimarySmtpAddress")
                    or safe(ae, "Address"))
            except Exception:
                entry["address"] = str(safe(rcp, "Address"))
        entry["name"] = str(safe(rcp, "Name"))
        report.append(entry)
    return report


def address_plainly(item, to: list, cc: list) -> None:
    """Write addresses as strings, the one path policy still allows.

    Setting .To is not address-book access, so it survives the Object Model
    Guard. Nothing is resolved and nothing is verified; only addresses the user
    supplied verbatim should ever reach this.
    """
    if to:
        item.To = "; ".join(to)
    if cc:
        item.CC = "; ".join(cc)


def drafts_count(ns) -> int:
    return int(safe(ns.GetDefaultFolder(OL_FOLDER_DRAFTS).Items, "Count", 0) or 0)


def unwrap(text: str) -> tuple:
    """Join hard-wrapped lines back into paragraphs. Returns (lines, n_joined).

    Outlook's plain-text body honours every newline, so a file wrapped at 72 or
    80 columns -- which is how every editor and every assistant writes one --
    arrives as a narrow ragged column that cannot reflow to the reader's
    window. A real recipient's first comment was that it looked squeezed.

    A blank line ends a paragraph. Lines that carry their own structure are
    left exactly as they are: list items, indented lines, quotes and headings.
    """
    def structural(line: str) -> bool:
        stripped = line.lstrip()
        return (line[:1].isspace()
                or stripped.startswith(("-", "*", ">", "#", "|"))
                or bool(_NUMBERED.match(stripped)))

    out, para, joined = [], [], 0
    def flush():
        nonlocal joined
        if para:
            joined += len(para) - 1
            out.append(" ".join(para))
            para.clear()

    for line in text.splitlines():
        if not line.strip():
            flush()
            out.append("")
        elif structural(line):
            flush()
            out.append(line)
        else:
            para.append(line.strip())
    flush()
    while out and not out[-1]:
        out.pop()
    return out, joined


def _read(obj, name):
    """Return (value, readable). Policy blocks reads as well as writes."""
    try:
        value = getattr(obj, name)
        return ("" if value is None else value), True
    except Exception:
        return "", False


def verify_draft(ns, entry_id: str, subject: str, body: str) -> tuple:
    """Re-open the SAVED item and compare it with what was asked for.

    Returns (problems, unchecked). A property the Object Model Guard refuses to
    read is reported as UNCHECKED, never as a discrepancy and never as a pass.
    On a policy-restricted machine the body and the recipients cannot be read
    back at all, so an earlier version raised after the draft had already been
    saved -- reporting a failure that had not happened, for a draft that was
    sitting correctly in Drafts.
    """
    item = by_entry_id(ns, entry_id)
    problems, unchecked = [], []

    actual_subject, ok = _read(item, "Subject")
    if not ok:
        unchecked.append("subject")
    elif str(actual_subject).strip() != subject.strip():
        problems.append(f"subject is {str(actual_subject)!r}, expected {subject!r}")

    actual_body, ok = _read(item, "Body")
    if not ok:
        unchecked.append("body")
    else:
        probe = " ".join(body.split())[:60]
        if probe and probe not in " ".join(str(actual_body).split()):
            problems.append("the body text is not in the saved draft")

    to, ok_to = _read(item, "To")
    cc, ok_cc = _read(item, "CC")
    if not (ok_to or ok_cc):
        unchecked.append("recipients")
    elif not str(to).strip() and not str(cc).strip():
        problems.append("the saved draft has no recipients")

    return problems, unchecked
