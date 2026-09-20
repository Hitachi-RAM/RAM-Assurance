"""Self-test: the target gate, which is what stops a reply reaching the wrong thread.

The browser path needs a signed-in session and cannot run unattended, so this
exercises the logic that decides WHETHER to type -- the part that carries the
risk. The typing itself is worthless if the gate is wrong.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import draft_reply as D  # noqa: E402
import outlook_com as O  # noqa: E402
import srs_m365 as M  # noqa: E402


def main() -> int:
    checks, failures = 0, []

    def check(label: str, condition: bool, detail: str = "") -> None:
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(f"{label}: {detail}" if detail else label)

    hdr = {"subject": "TTC Line 2 interface specification review",
           "sender": "EXAMPLE Alice <alice@example.com>"}

    check("matches on subject words",
          D.header_matches(hdr, "interface specification review", ""))
    check("matches on sender surname", D.header_matches(hdr, "", "alice"))
    check("rejects a different subject",
          not D.header_matches(hdr, "invoice payment terms schedule", ""))
    check("rejects a different sender",
          not D.header_matches(hdr, "", "bob.sample@example.com"))
    check("rejects an empty header",
          not D.header_matches({"subject": "", "sender": ""}, "interface", ""))

    # A half-match must not pass: one shared word out of four is a coincidence.
    check("rejects a single coincidental word",
          not D.header_matches(hdr, "quarterly financial review summary", ""))

    # Short words are dropped as carrying no identity. When that left only ONE
    # word, the gate stopped identifying a message: "TTC Line 2" collapsed to
    # {line} and matched a mail about line management.
    check("a request that collapses to one word does not match a stranger",
          not D.header_matches({"subject": "Line management policy",
                                "sender": ""}, "TTC Line 2", ""))
    check("and still matches the message it names",
          D.header_matches({"subject": "TTC Line 2 ATC contract review",
                            "sender": ""}, "TTC Line 2", ""))
    check("a genuinely single-word subject still works",
          D.header_matches({"subject": "Missing timesheets for August",
                            "sender": ""}, "Timesheets", ""))
    check("but not against an unrelated message",
          not D.header_matches({"subject": "Holiday calendar", "sender": ""},
                               "Timesheets", ""))

    check("no send path anywhere in the package",
          not any("send" in p.name.lower()
                  for p in (Path(__file__).resolve().parent.parent
                            / "scripts").glob("*.py")))

    scripts = Path(__file__).resolve().parent.parent / "scripts"
    compose = (scripts / "draft_new.py").read_text(encoding="utf-8")
    check("a compose path exists", (scripts / "draft_new.py").exists())
    check("recipient verified at click time", "elementFromPoint" in compose)
    check("warns when the address book matches more than once",
          "matches" in compose and "twice" in compose)
    check("to field matched exactly, not loosely", '"exact": True' in compose)
    check("suggestion list polled, never slept on", "M.poll" in compose)
    # The OPERATION, not the word: a file that documents "Send() appears
    # nowhere here" contains the word and is the best-behaved file in the set.
    check("compose never calls Send", ".Send(" not in compose)
    check("a subject is required", "A subject is required" in compose)

    # --- the three defects reported from real use on 2026-09-15 -------------
    # 1. The subject was set behind `if spot:` with no else, so a timed-out
    #    poll skipped the field and the run still reported success.
    reading = (scripts / "read_mail.py").read_text(encoding="utf-8")
    reply = (scripts / "draft_reply.py").read_text(encoding="utf-8")
    com = (scripts / "outlook_com.py").read_text(encoding="utf-8")

    import ast as _ast

    def guarded(source: str, needle: str) -> bool:
        """True if the statement that looks for `needle` is followed straight
        away by a branch that leaves the function."""
        for node in _ast.walk(_ast.parse(source)):
            body = getattr(node, "body", None)
            if not isinstance(body, list):
                continue
            for i, stmt in enumerate(body[:-1]):
                if needle not in _ast.unparse(stmt):
                    continue
                nxt = body[i + 1]
                if isinstance(nxt, _ast.If) and any(
                        isinstance(x, (_ast.Return, _ast.Raise))
                        for x in _ast.walk(nxt)):
                    return True
        return False

    check("the web subject step cannot be skipped silently",
          guarded(compose, "SUBJECT_NAMES"))
    check("the subject is read back after it is typed",
          "JS_FIELD_VALUE" in compose)
    check("the saved draft is re-read and compared",
          "verify_draft" in compose and "verify_draft" in com)

    # OWA renamed the subject box: aria-label became "Subject" and "Add a
    # subject" moved to the placeholder. One pinned string took the whole
    # browser path out, so the locator must carry alternatives and read both
    # attributes -- and the read-back must use the same predicate, or it
    # silently inspects nothing.
    check("the subject field has more than one candidate name",
          "SUBJECT_NAMES" in compose
          and compose.count('"subject"') + compose.count("'subject'") >= 1
          and "add a subject" in compose)
    check("fields are matched on placeholder as well as aria-label",
          "getAttribute('placeholder')" in compose)
    check("the read-back matches on placeholder too",
          compose.split("JS_FIELD_VALUE")[1].split('"""')[1].count("placeholder") >= 1
          if "JS_FIELD_VALUE" in compose else False,
          "a rename would make the read-back look at nothing")

    # An empty chip list must mean "I could not read them", never "there are
    # none": a To field holding three duplicates returned [] and printed nothing.
    check("an unreadable recipient list is reported, not passed over",
          "could NOT read the recipient chips" in compose,
          "silence here once hid a draft addressed to the same man three times")
    check("the chip query distinguishes absent from unreadable",
          "wells.length ? [] : null" in compose)
    check("duplicate chips raise a warning",
          "Check for duplicates" in compose)

    # OWA puts the signature in every new compose, so "is the body empty?" is
    # the wrong question.
    check("the body is baselined before typing, not required to be empty",
          "baseline" in compose)
    check("the message is typed at the top of the body",
          "Control+Home" in compose,
          "otherwise the mail reads signature-first")

    # 2. --thread clicked stale coordinates and never checked what opened.
    check("rows are re-found by id at click time, not by stored coordinates",
          "JS_OPEN_ROW" in reading and 'target["rect"]' not in reading)
    check("the reading pane is verified to show the message asked for",
          "JS_OPEN_SUBJECT" in reading)
    check("the chevron failure is named where it bites",
          "chevron" in reading.lower())

    # 3. SKILL.md documented a --thread flag draft_reply.py did not have.
    check("draft_reply accepts the --thread it is documented with",
          '"--thread"' in reply)
    check("replying starts from the message, so the thread is kept",
          ".Reply" in reply or "Reply()" in reply)

    # The desktop path must be as incapable of sending as the browser one.
    for name, text in (("outlook_com.py", com), ("draft_reply.py", reply),
                       ("draft_new.py", compose)):
        check(f"{name} never calls Send", ".Send(" not in text)
    check("Outlook is never quit from under the user", ".Quit(" not in com)
    check("late binding, so a stale gen_py cache cannot masquerade as a "
          "broken Outlook", "dynamic.Dispatch" in com)

    skill = (scripts.parent / "SKILL.md").read_text(encoding="utf-8")
    check("the skill states what it does NOT do",
          "What this skill does NOT do" in skill)

    source = (Path(__file__).resolve().parent.parent / "scripts"
              / "draft_reply.py").read_text(encoding="utf-8")
    check("banner is present so a leftover draft is identifiable",
          "BANNER" in source)
    check("refuses without a subject or sender",
          "--subject or --sender" in source)

    check("zero-width padding stripped", M.clean("hel\u200blo  world") == "hello world")
    check("private-use glyphs stripped", M.clean("\uf582 Open \ue486") == "Open")
    check("empty text is empty", M.clean(None) == "")

    check("forbidden actions include send", "send" in M.FORBIDDEN_ACTIONS)
    check("forbidden actions include delete", "delete" in M.FORBIDDEN_ACTIONS)

    # --- the body must reflow in the reader's window, not arrive as a column
    wrapped = ("This is a sentence that a text editor wrapped at about eighty\n"
               "columns, so it continues onto a second line and then a third\n"
               "line before it finishes.\n"
               "\n"
               "A second paragraph follows the blank line.\n"
               "\n"
               "- a list item that must keep its own line\n"
               "- a second list item\n"
               "    indented text that is structure, not prose\n")
    lines, joined = O.unwrap(wrapped)
    check("unwrap joins a hard-wrapped paragraph", joined == 2,
          f"joined {joined}, expected 2 (three lines make two joins)")
    check("unwrap produces one line per paragraph",
          lines[0].startswith("This is a sentence") and lines[0].endswith("finishes."))
    check("unwrap keeps a blank line between paragraphs", "" in lines)
    check("unwrap leaves list items alone",
          "- a list item that must keep its own line" in lines)
    check("unwrap leaves indented structure alone",
          any(ln.startswith("    indented") for ln in lines))
    check("unwrap of already-paragraphed text changes nothing",
          O.unwrap("One paragraph.\n\nAnother paragraph.\n")[1] == 0)

    # --- a policy block is not a resolution and must never look like one
    class _Guarded:
        """Stands in for Outlook where the Object Model Guard denies access."""
        @property
        def Recipients(self):
            raise RuntimeError("Operation aborted")

    report = O.resolve(_Guarded(), ["someone@example.com"], kind=1)
    check("a blocked address book yields one entry", len(report) == 1)
    check("a blocked address book is not reported as resolved",
          report[0]["resolved"] is False)
    check("a blocked address book is flagged as blocked",
          report[0]["blocked"] is True)
    check("a blocked address book invents no address",
          report[0]["address"] == "",
          "an address was produced without the address book")
    check("the requested address is carried through verbatim",
          report[0]["requested"] == "someone@example.com")
    check("the guard is recognised by its message",
          O.is_policy_block(RuntimeError("Operation aborted")))
    check("an ordinary error is NOT treated as a policy block",
          not O.is_policy_block(ValueError("something else")),
          "a real fault would be silently downgraded to a policy block")

    # --- SKILL.md must carry the rule, since the assistant reads it
    skill_md = (Path(__file__).resolve().parent.parent / "SKILL.md").read_text(
        encoding="utf-8")
    check("SKILL.md forbids inventing an address",
          "never invent an address" in skill_md.lower())
    check("SKILL.md offers leaving the recipient empty",
          "left empty" in skill_md.lower())

    print(f"ASSERTIONS: {checks}")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        return 1
    print(f"  {checks} assertion(s) passed. The browser path needs a signed-in "
          f"session and is not exercised here.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
