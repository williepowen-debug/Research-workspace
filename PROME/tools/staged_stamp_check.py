#!/usr/bin/env python3
"""staged_stamp_check.py — flag a clock stamp in STAGED ADDED lines that is ahead of the clock.

WQ-713 (Will 2026-11-17), DOCKET L1188 item 1. Called by scripts/githooks/pre-commit.
Acceptance: PROME/tools/tests/ACCEPTANCE_staged_stamp_ahead_2026-11-20.md.

ADVISORY ONLY: prints to stdout, ALWAYS exits 0. A stamp is read only in its full form, an ISO
date directly followed by a clock time and its zone: `2026-11-20 13:45 ET` (EST, EDT) or
`2026-11-20T18:45Z` (seconds optional). It is flagged when its instant is more than 2 minutes
and at most 24 hours after now. Anything else (partial, approximate, zoneless) is not read.

  --now  YYYY-MM-DDTHH:MM:SSZ   the clock to compare against (tests); default the system clock
  --diff-file PATH              read a unified diff from PATH instead of the index (tests)
"""
import argparse
import datetime as dt
import re
import subprocess
import sys

LOW = dt.timedelta(minutes=2)
HIGH = dt.timedelta(hours=24)
_ET = re.compile(r"(?<!\d)(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}) (ET|EST|EDT)\b")
_Z = re.compile(r"(?<!\d)(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})(?::(\d{2}))?Z\b")
MAX_PRINT = 10


def _eastern(naive: dt.datetime, zone: str) -> dt.datetime:
    """The UTC instant of an Eastern wall-clock time. EST and EDT are taken at their word;
    plain ET uses the zone database, and the US rule if the database is absent."""
    if zone == "EST":
        return (naive + dt.timedelta(hours=5)).replace(tzinfo=dt.timezone.utc)
    if zone == "EDT":
        return (naive + dt.timedelta(hours=4)).replace(tzinfo=dt.timezone.utc)
    try:
        from zoneinfo import ZoneInfo
        return naive.replace(tzinfo=ZoneInfo("America/New_York")).astimezone(dt.timezone.utc)
    except Exception:
        y = naive.year
        start = dt.datetime(y, 3, 8) + dt.timedelta(days=(6 - dt.datetime(y, 3, 8).weekday()) % 7, hours=2)
        end = dt.datetime(y, 11, 1) + dt.timedelta(days=(6 - dt.datetime(y, 11, 1).weekday()) % 7, hours=2)
        off = 4 if start <= naive < end else 5
        return (naive + dt.timedelta(hours=off)).replace(tzinfo=dt.timezone.utc)


def stamps(line: str):
    """[(text, utc instant)] for every full stamp on the line; an impossible date is skipped."""
    out = []
    for m in _ET.finditer(line):
        try:
            naive = dt.datetime(*(int(m.group(i)) for i in range(1, 6)))
        except ValueError:
            continue
        out.append((m.group(0), _eastern(naive, m.group(6))))
    for m in _Z.finditer(line):
        try:
            when = dt.datetime(*(int(m.group(i)) for i in range(1, 6)), int(m.group(6) or 0),
                               tzinfo=dt.timezone.utc)
        except ValueError:
            continue
        out.append((m.group(0), when))
    return out


def ahead(diff_text: str, now: dt.datetime):
    """[(file, stamp text, minutes ahead)] over ADDED lines of a unified diff."""
    found, path, in_hunk = [], "?", False
    for line in diff_text.split("\n"):
        if line.startswith("diff --git "):      # a new file's headers follow; hunk lines never start this way
            in_hunk = False
            continue
        if line.startswith("@@"):
            in_hunk = True
            continue
        if not in_hunk:                         # `+++ b/path` is a header only before the file's first hunk
            if line.startswith("+++ "):
                path = line[6:] if line.startswith("+++ b/") else line[4:]
            continue
        if not line.startswith("+"):
            continue
        for text, when in stamps(line[1:]):
            gap = when - now
            if LOW < gap <= HIGH:
                found.append((path, text, int(gap.total_seconds() // 60)))
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--now")
    ap.add_argument("--diff-file")
    a = ap.parse_args()
    now = (dt.datetime.strptime(a.now, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
           if a.now else dt.datetime.now(dt.timezone.utc))
    if a.diff_file:
        with open(a.diff_file, "rb") as fh:
            raw = fh.read()
    else:
        raw = subprocess.run(["git", "diff", "--cached", "-U0", "--no-color", "--no-ext-diff"],
                             capture_output=True, timeout=20).stdout
    hits = ahead(raw.decode("utf-8", errors="replace"), now)
    if hits:
        print(f"stamp check: {len(hits)} staged clock stamp(s) are AHEAD of the clock "
              "(a scheduled time may be ignored; a record of something done takes its time from `date`):")
        for path, text, mins in hits[:MAX_PRINT]:
            print(f"  {path}: {text} is {mins} min ahead")
        if len(hits) > MAX_PRINT:
            print(f"  and {len(hits) - MAX_PRINT} more")
    return 0


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except BaseException as e:   # advisory: never a traceback, never a non-zero exit
        print(f"stamp check: could not run ({type(e).__name__}); commit not affected")
    sys.exit(0)
