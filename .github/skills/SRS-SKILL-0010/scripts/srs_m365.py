# ---------------------------------------------------------------
# Shared module from the SRS skill library. Do not edit here:
# edit the library copy so every skill gets the fix.
# ---------------------------------------------------------------
"""Shared Microsoft 365 browser foundation for the SRS skill library.

Every M365 skill in this library (Outlook, Teams, SharePoint, Copilot,
Calendar, Transcripts) drives the *web* surface through one signed-in Edge
profile rather than calling the Graph API. That is not a preference: app
registration and client-credential flows are refused by Conditional Access on
this tenant, so the only route that works is the one the user already has.

Consequences of that choice, which the skills depend on:

* The automation acts **as the signed-in user** and can see exactly what they
  can see. It holds no credential of its own and cannot obtain one.
* Sign-in happens once, interactively, in a real window. Nothing in this
  library ever handles a password, and no password is stored anywhere.
* One profile single-signs-on into Outlook web, Teams, SharePoint and
  m365.cloud.microsoft, so six skills share one sign-in.

The profile is SINGLE-WRITER. A browser left running from an earlier run makes
the next launch fail; `close_profile_edge()` closes only the processes holding
*this* profile and never touches the user's own Edge windows.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

try:
    from playwright.sync_api import sync_playwright
except ImportError:  # pragma: no cover - reported by the caller, not here
    sync_playwright = None  # type: ignore[assignment]

# --------------------------------------------------------------------------
# Profile location. Configurable because this ships to other people's machines.
# --------------------------------------------------------------------------

DEFAULT_PROFILE_DIR = ".m365_profile"
DEFAULT_PORT = 9333

ZERO_WIDTH = re.compile(r"[\u200b-\u200f\ufeff]")
PRIVATE_USE = re.compile(r"[\uE000-\uF8FF]")

URLS = {
    "mail": "https://outlook.office.com/mail/",
    "calendar": "https://outlook.office.com/calendar/view/workweek",
    "teams": "https://teams.microsoft.com/v2/",
    "copilot": "https://m365.cloud.microsoft/chat/",
}


def profile_path() -> Path:
    """Where the signed-in Edge profile lives.

    Deliberately OUTSIDE the skill package. It used to sit in a folder beside
    the scripts, which was convenient and wrong three ways: it broke reinstall
    while a browser held the lock, it put files in an installed package that
    its own manifest does not list, and -- the one that matters -- it left live
    session cookies inside a folder people copy and zip to hand a skill to a
    colleague. A profile is credentials, so it belongs with the user's other
    credentials, not with the code.

    One location for every M365 skill, so signing in once covers mail, Teams,
    SharePoint, calendar and Copilot. The env var lets a site point elsewhere.
    """
    env = os.environ.get("SRS_M365_PROFILE")
    if env:
        return Path(env).expanduser()
    base = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~")
    return Path(base) / "SRS-Skills" / "m365-profile"


def debug_port() -> int:
    return int(os.environ.get("SRS_M365_PORT", DEFAULT_PORT))


# --------------------------------------------------------------------------
# Edge process management
# --------------------------------------------------------------------------

EDGE_CANDIDATES = [
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
]

_PS_LIST = ("Get-CimInstance Win32_Process -Filter \"Name='msedge.exe'\" | "
            "Select-Object ProcessId, CommandLine | ConvertTo-Json -Depth 3 -Compress")


def edge_exe() -> Path:
    for p in EDGE_CANDIDATES:
        if p.exists():
            return p
    raise SystemExit("msedge.exe not found in either Program Files location.")


def _profile_procs() -> list[dict]:
    """Edge processes holding OUR profile, and only ours.

    Matching on the profile directory is what makes this safe. The user
    routinely has a dozen Edge processes of their own; none of them carry
    this path on the command line.
    """
    out = subprocess.run(["powershell", "-NoProfile", "-Command", _PS_LIST],
                         capture_output=True, text=True).stdout.strip()
    try:
        procs = json.loads(out) if out else []
    except json.JSONDecodeError:
        return []
    if isinstance(procs, dict):
        procs = [procs]
    key = str(profile_path()).lower()
    return [p for p in procs if key in (p.get("CommandLine") or "").lower()]


def close_profile_edge(*, graceful_pages: bool = True) -> int:
    """Close the automation browser. Never force-kills the user's Edge.

    Force-killing makes Edge offer to restore pages on the next launch, and a
    user who accepts that gets stale drafts reopened. So close tabs over the
    debugging port first where possible and only kill what survives.

    Returns how many processes were closed ALTOGETHER. It used to return only
    the force-killed survivors, so a clean graceful shutdown of eleven
    processes reported "No automation browser was running" -- in the one
    command people run to check exactly that.
    """
    before = _profile_procs()
    if graceful_pages and _port_live() and sync_playwright is not None:
        try:
            with sync_playwright() as pw:
                browser = pw.chromium.connect_over_cdp(
                    f"http://127.0.0.1:{debug_port()}")
                for ctx in browser.contexts:
                    for page in list(ctx.pages):
                        try:
                            page.close()
                        except Exception:
                            pass
                browser.close()
            time.sleep(2)
        except Exception:
            pass
    survivors = _profile_procs()
    for p in survivors:
        subprocess.run(["taskkill", "/PID", str(p["ProcessId"]), "/T", "/F"],
                       capture_output=True, text=True)
    if survivors:
        time.sleep(3)
    return len(before)


def _port_live() -> bool:
    import urllib.error
    import urllib.request
    try:
        with urllib.request.urlopen(
                f"http://127.0.0.1:{debug_port()}/json/version", timeout=2):
            return True
    except (urllib.error.URLError, OSError):
        return False

_STARTED_HERE = False


def start_edge(url: str, *, offscreen: bool = False) -> None:
    """Start Edge on the skill profile with a debugging port, unless already up.

    Edge is started as an ordinary process rather than through
    `launch_persistent_context`, because Playwright closes the browser it
    launched when the script exits -- which would discard an unsent draft.
    """
    global _STARTED_HERE
    if _port_live():
        return
    _STARTED_HERE = True
    if _profile_procs():
        close_profile_edge(graceful_pages=False)
    profile = profile_path()
    profile.mkdir(parents=True, exist_ok=True)
    args = [
        str(edge_exe()),
        f"--user-data-dir={profile}",
        f"--remote-debugging-port={debug_port()}",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-session-crashed-bubble",
        "--hide-crash-restore-bubble",
        "--restore-last-session=false",
    ]
    # The window is always visible. It used to be parked at -2400,-2400 when a
    # caller asked for `offscreen`, which was a bad trade: the automation window
    # shares the user's Edge taskbar entry, so clicking Edge while a skill ran
    # activated an invisible window and showed the desktop, and a stale
    # thumbnail of it persisted afterwards. Being able to watch what your
    # assistant is doing is worth more than keeping it out of the way.
    args.append("--start-maximized")
    args.append(url)
    subprocess.Popen(args)
    for _ in range(60):
        if _port_live():
            return
        time.sleep(1)
    raise SystemExit(f"Edge did not open the debugging port {debug_port()}.")


def attach(pw, url: str, *, offscreen: bool = False):
    """Return (browser, page) on the page that is actually showing `url`.

    The caller must NOT close the browser. `browser.close()` on a CDP
    connection only detaches, but being explicit here has saved a draft more
    than once.

    Picking `contexts[0].pages[0]` is what the obvious version does, and it is
    wrong: Edge frequently holds a stray about:blank tab first, so the skill
    drives a blank page and then reports that the site's controls are missing.
    Observed 2026-09-14 as "Could not find Researcher in the rail" -- an
    absence reported when nothing had been looked at.
    """
    start_edge(url, offscreen=offscreen)
    browser = pw.chromium.connect_over_cdp(f"http://127.0.0.1:{debug_port()}")
    host = urlparse(url).netloc

    page = next((p for p in all_pages(browser) if urlparse(p.url).netloc == host),
                None)
    if page is None:
        ctx = browser.contexts[0]
        page = next((p for p in ctx.pages if p.url not in ("about:blank", "")),
                    None) or ctx.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=90000)
    page.bring_to_front()
    return browser, page


def release(browser, *, keep_open: bool = False) -> None:
    """Finish with the browser: detach, or quit it if this run started it.

    `browser.close()` on a CDP connection only DETACHES -- measured, ten
    processes before and eleven after. So a read-only script that ran and
    exited left a whole Edge behind, off-screen, every single time. Eighteen of
    them accumulated in one evening, and because Windows activates an existing
    off-screen window when you click the taskbar, Edge looked broken.

    Closes the pages through the handle the caller already has. Calling
    close_profile_edge() here instead opened a SECOND sync_playwright context
    inside the one still running, which is not re-entrant and took the whole
    process down with an access violation and no traceback.

    A drafting script must pass keep_open=True: its whole point is to leave an
    unsent draft on screen. A reading script should not.
    """
    if not keep_open and _STARTED_HERE:
        try:
            for ctx in browser.contexts:
                for page in list(ctx.pages):
                    try:
                        page.close()
                    except Exception:
                        pass
        except Exception:
            pass
    try:
        browser.close()
    except Exception:
        pass
    if keep_open or not _STARTED_HERE:
        return
    time.sleep(2)
    close_profile_edge(graceful_pages=False)   # taskkill only: no new context


def all_pages(browser) -> list:
    """Every page in every context.

    A popped-out Outlook window arrives as a NEW CDP context, so
    `contexts[0].pages` silently misses it.
    """
    return [p for c in browser.contexts for p in c.pages]


# --------------------------------------------------------------------------
# Page helpers. Locators are avoided on purpose.
# --------------------------------------------------------------------------

def js(page, script: str, arg=None, *, tries: int = 3):
    """Read the DOM through evaluate() and get a plain dict back.

    Playwright locators (`count()`, `is_visible()`, `inner_text()`) block
    indefinitely on some Teams SPA states. evaluate() has no actionability
    wait, so it cannot hang the same way.

    Retries on "Execution context was destroyed". A Teams deep link redirects
    two or three times before the app settles, and a probe that lands mid
    redirect raises rather than returning nothing -- which reads to the caller
    like the page is broken when it is merely still arriving.
    """
    for attempt in range(tries):
        try:
            return page.evaluate(script, arg) if arg is not None \
                else page.evaluate(script)
        except Exception as exc:
            navigating = "context was destroyed" in str(exc) \
                or "Execution context" in str(exc)
            if not navigating or attempt == tries - 1:
                raise
            try:
                page.wait_for_load_state("domcontentloaded", timeout=15000)
            except Exception:
                pass
            page.wait_for_timeout(1500)


def clean(text: str | None) -> str:
    """Strip the invisible padding these surfaces add to their own text.

    The Copilot composer pads with zero-width characters, so a strict length
    compare fails (301 against 299); Outlook menu labels are wrapped in
    private-use glyphs.
    """
    if not text:
        return ""
    text = ZERO_WIDTH.sub("", text)
    text = PRIVATE_USE.sub("", text)
    return re.sub(r"\s+", " ", text).strip()


JS_DISMISS = r"""
() => {
  // Outlook lays a Copilot promotion over a prepared compose window, and it
  // appears AFTER the page settles, so it must be dismissed late and again
  // partway through anything slow.
  const out = [];
  for (const d of document.querySelectorAll('[role="dialog"]')) {
    const t = (d.innerText || '');
    if (/reminder/i.test(t)) continue;            // the user's own reminders
    for (const b of d.querySelectorAll('button')) {
      const label = (b.innerText || '').trim();
      if (/^(Not now|Dismiss|Maybe later|No thanks|Got it|Close)$/i.test(label)) {
        b.click(); out.push(label); break;
      }
    }
  }
  // Teams offers its desktop app before it will show the web client.
  for (const el of document.querySelectorAll('a,button,span,div')) {
    const label = (el.innerText || '').trim();
    if (/^(Use the web app instead|Continue on this browser)$/i.test(label)) {
      el.click(); out.push(label); break;
    }
  }
  return out;
}
"""


def dismiss_prompts(page) -> list[str]:
    try:
        return page.evaluate(JS_DISMISS) or []
    except Exception:
        return []


def poll(fn, *, seconds: float = 30, interval: float = 1.0):
    """Poll until fn() is truthy. Returns the value, or None on timeout.

    Fixed sleeps fail intermittently on every one of these surfaces -- a six
    second wait for the address-book list failed once in five.
    """
    deadline = time.time() + seconds
    while time.time() < deadline:
        try:
            value = fn()
        except Exception:
            value = None
        if value:
            return value
        time.sleep(interval)
    return None


def signed_in(page) -> bool:
    """True once the tenant has actually let us in.

    A sign-in page is a perfectly healthy-looking page; without this check a
    skill reports 'no items found' when the truth is 'not signed in'.
    """
    url = page.url or ""
    return not any(s in url for s in ("login.microsoftonline.com",
                                      "login.live.com", "/oauth2/"))


def require_sign_in(page, *, seconds: float = 300) -> None:
    if signed_in(page):
        return
    print("  Sign in in the browser window that just opened. Waiting...")
    if not poll(lambda: signed_in(page), seconds=seconds, interval=2):
        raise SystemExit("Still on the sign-in page. Nothing was read or written.")


# --------------------------------------------------------------------------
# The library-wide safety posture
# --------------------------------------------------------------------------

#: Words that must never appear in an action this library performs on the
#: user's behalf without them doing it themselves.
FORBIDDEN_ACTIONS = ("send", "delete", "cancel", "decline", "accept",
                     "remove", "purge", "empty", "discard")


def refuse(action: str, alternative: str) -> None:
    """Stop, and say what the skill will do instead.

    Raising rather than warning matters: a warning in a log is not a control.
    """
    raise SystemExit(
        f"Refused: this skill does not {action}.\n"
        f"  What it will do instead: {alternative}\n"
        f"  If you want it {action}ed, do it yourself in the window that is open.")


def confirm(question: str) -> bool:
    """Ask the person at the keyboard. Absent a keyboard, the answer is no."""
    if not sys.stdin.isatty():
        print(f"  {question} -> no keyboard to ask, so: no.")
        return False
    return input(f"  {question} [y/N] ").strip().lower() in ("y", "yes")


def main_close() -> None:
    """`py srs_m365.py --close` -- shared by every skill in the M365 block."""
    n = close_profile_edge()
    print(f"Closed {n} automation process(es) holding {profile_path()}."
          if n else "No automation browser was running.")


if __name__ == "__main__":
    if "--close" in sys.argv:
        main_close()
    elif "--profile" in sys.argv:
        print(profile_path())
    else:
        print(__doc__)
        print(f"\nProfile: {profile_path()}\nPort:    {debug_port()}")
        print("\n  --close    close the automation browser")
        print("  --profile  print the profile path")
