#!/usr/bin/env python3
"""profile_clock_check.py — the CHEAP half of the profile-staleness trigger (wiring-sweep leg ㉕).

Every `profiles/<AGENT>.md` declares a Staleness trigger in prose. Almost all carry a DAY CLOCK
("> 45 days", ">30d", "hard floor 2026-09-15"). Nothing read those clocks between reviews —
PR#5 (2026-09-01) found ~22 of 35 profiles past their own named trigger. This check reads the
DAY-CLOCK leg only (content legs stay agent-judged) against the profile's last git commit date.

rc contract (CHECK_STANDARD §9):  0 = every dated clock inside its window
                                  1 = >=1 profile past its own day clock (names printed)
                                  2 = CANNOT-EVALUATE (git failed, no profiles dir)
Prints its PERIMETER on every run: N profiles read · M with a dated clock · K with none
(NO-DATED-CLOCK is a discovery line, never a pass). Read-only. cwd-proof (PAT-031).
"""
from __future__ import annotations
import re, subprocess, sys, datetime as dt
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent  # AGENTS/DAEDALUS
PROFILES = ROOT / "profiles"
DAY_RX = re.compile(r"(?:>|&gt;|over|past)\s*(\d{1,3})\s*(?:d\b|days?\b|-day)", re.I)
FLOOR_RX = re.compile(r"(?:hard\s+floor|floor)\s*[:=]?\s*(20\d\d-\d\d-\d\d)", re.I)
SKIP = {"_TEMPLATE"}

def last_commit_date(path: Path) -> dt.date | None:
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", str(path)],
                             capture_output=True, text=True, check=True, cwd=str(ROOT)).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return dt.date.fromisoformat(out) if out else None

DATE_RX = re.compile(r"\b(20\d\d-\d\d-\d\d)\b")
BANNER_MARKERS = ("STALE — TRIGGER FIRED", "NO DATED STALENESS TRIGGER")

def vintage_of(text: str, git_date: dt.date | None) -> tuple[dt.date | None, str]:
    """Content vintage = the LATEST date in the profile's header block (lines before the first '## ',
    max 15), skipping DAEDALUS banner lines — so a banner commit never resets the clock (a banner is a
    warning, not a fix). A Δ-block date counts: it IS a partial refresh (content legs stay agent-judged).
    Falls back to the git commit date when the header carries no date."""
    head = []
    for line in text.splitlines():
        if line.startswith("## "): break
        head.append(line)
        if len(head) >= 15: break
    dates = []
    for line in head:
        if any(m in line for m in BANNER_MARKERS): continue
        for m in DATE_RX.finditer(line):
            try: dates.append(dt.date.fromisoformat(m.group(1)))
            except ValueError: pass
    if dates: return max(dates), "header-date"
    return git_date, "git-date"

def clock_of(text: str) -> tuple[int | None, dt.date | None]:
    # only the trigger neighbourhood: lines mentioning staleness/trigger/refresh
    lines = [l for l in text.splitlines() if re.search(r"stalen|trigger|refresh", l, re.I)]
    hay = "\n".join(lines[:12])
    days = [int(m.group(1)) for m in DAY_RX.finditer(hay)]
    floors = [dt.date.fromisoformat(m.group(1)) for m in FLOOR_RX.finditer(hay)]
    return (min(days) if days else None), (min(floors) if floors else None)

def main(argv: list[str]) -> int:
    quiet = "--quiet" in argv
    today = dt.date.today()
    if not PROFILES.is_dir():
        print(f"PROFILE-CLOCK 2 CANNOT-EVALUATE: {PROFILES} missing"); return 2
    fired, ok, undated, cannot = [], [], [], []
    for p in sorted(PROFILES.glob("*.md")):
        name = p.stem
        if name in SKIP: continue
        text = p.read_text(encoding="utf-8", errors="replace")
        days, floor = clock_of(text)
        lc, basis = vintage_of(text, last_commit_date(p))
        if lc is None:
            cannot.append(name); continue
        age = (today - lc).days
        if days is None and floor is None:
            undated.append(f"{name}({age}d)"); continue
        hit = []
        if days is not None and age > days: hit.append(f"{age}d > {days}d")
        if floor is not None and today > floor: hit.append(f"floor {floor} passed")
        (fired if hit else ok).append(f"{name}: " + (", ".join(hit) if hit else f"{age}d ≤ {days if days is not None else 'floor '+str(floor)}") + f" [{basis} {lc}]")
    if cannot:
        print(f"PROFILE-CLOCK 2 CANNOT-EVALUATE: git date unreadable for {', '.join(cannot)}"); return 2
    n = len(fired) + len(ok) + len(undated)
    print(f"PROFILE-CLOCK perimeter: {n} profile(s) read · {len(fired)+len(ok)} with a DATED day-clock/floor · "
          f"{len(undated)} NO-DATED-CLOCK (content-only trigger, agent-judged, NOT certified here): {', '.join(undated) or '—'}")
    if fired:
        print(f"⏰ PROFILE-CLOCK 1: {len(fired)} profile(s) PAST their own day clock → refresh or banner (UPGRADE_PROTOCOL step 0):")
        for f in fired: print(f"   🔴 {f}")
        if not quiet:
            for o in ok: print(f"   ✅ {o}")
        return 1
    print(f"✅ PROFILE-CLOCK 0: every dated profile clock inside its window ({len(ok)} checked)")
    if not quiet:
        for o in ok: print(f"   ✅ {o}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
