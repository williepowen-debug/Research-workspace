#!/usr/bin/env python3
"""claim_check — mechanical checks for error classes that memory alone does not catch.

WHY THIS EXISTS (2026-07-27, Will-directed). A measurement pass that day found the
fleet's ~8 mechanical detectors (firetime/orphan/env_doctor/spine_audit/...) fire
reliably, while memory-based lessons do not: **two errors shipped that session were
in classes already written down in the author's own auto-memory index** —
`feedback_behavior_language_over_hash_pinning` (a commit hash cited as provenance,
routed to 3 agents, already rebased away) and `feedback_verify_etf_vs_fx` (gold
quoted at the GLD ticker's price). A lesson that requires you to *remember to
remember*, at the moment you are confident and moving fast, is not a control.
This converts the high-frequency ones into something that runs.

Advisory by design: it flags, it never blocks and never edits. False positives are
cheap; a missed predicate error costs a routed packet or a mis-stamped level.

CHECKS
  weekday  a day-name asserted next to a date that is not that weekday.
           n=3 in-repo before this was built (WALTER "Fri 2026-07-25" = a Saturday,
           which produced a false 🔴 outage alarm; HEARTBEAT "Mon 7/28" = a Tuesday;
           WALTER log "6/20 is a SATURDAY, docs mislabeled Sun").
  hash     a git hash cited as provenance that is NOT an ancestor of origin/master
           — i.e. rebased away, or from a branch a reader cannot reach. A hash is
           not the artifact; cite a durable path.
  units    a named instrument quoted at a magnitude that belongs to its tracking
           ETF (or vice versa) — "gold $374" is GLD, not gold.
  pointer  a backtick-quoted repo path that does not exist (dead cross-reference).

USAGE
    python3 scripts/claim_check.py                 # files changed vs HEAD (pre-commit)
    python3 scripts/claim_check.py PATH [PATH...]  # explicit files
    python3 scripts/claim_check.py --staged        # only staged files
    python3 scripts/claim_check.py --check weekday,hash
    python3 scripts/claim_check.py --selftest     # shipped falsification set (CHECK_STANDARD §3/§14)
Exit 0 = clean · 1 = flags found (advisory) · 2 = usage/environment error.
--selftest: exit 0 = every case behaved · 1 = a case failed (the tool is NOT trustworthy).
"""
import argparse
import datetime
import functools
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(
    subprocess.run(["git", "rev-parse", "--show-toplevel"],
                   capture_output=True, text=True).stdout.strip() or ".")

DAYS = {d.lower(): i for i, d in enumerate(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])}
ABBR = {d[:3].lower(): i for d, i in zip(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], range(7))}
DAYMAP = {**DAYS, **ABBR}
DAYNAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Exact day tokens (for validating the LEADING half of a "Tue-Wed" pair — a
# prefix-word like "Satellite-" must not read as Sat via the [:3] shortcut).
DAYTOKENS = set(DAYS) | {"mon", "tue", "tues", "wed", "thu", "thur", "thurs", "fri", "sat", "sun"}

# day-name immediately before a date: "Fri 2026-07-25", "Mon 7/28", "Tuesday 7/28"
_DAY_ALT = r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|Mon|Tues|Tue|Wed|Thurs|Thur|Thu|Fri|Sat|Sun)"
_NUM_DATE = r"(\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}(?:/\d{2,4})?)"
RE_WEEKDAY = re.compile(
    r"\b" + _DAY_ALT + r"[\s,.\-–—]+(?:\*\*)?" + _NUM_DATE + r"\b", re.I)
# ORDER-BLIND FORMS (2026-09-03, PROME defect report off a TERRY find): the regex above
# matched weekday-BEFORE-date ONLY, so "9/6 Sat", "9/6 (Saturday)" and "Sep 6 (Sat)" all
# read CLEAN — a root-closeout gate (step 1e) silently certifying files for every desk;
# TERRY's STATUS shipped a wrong weekday through a clean run the same day
# (finding_scan_keyed_on_naming_reads_local_form_as_absence). Three more forms:
#   AFTER   — "9/6 Sat" · "2026-09-06 (Sat)" · "9/5-6 Sat-Sun" (range: lead vs start, trail vs end)
#   MONTH   — "Sep 6 (Sat)" · "Sept 6, 2026 Sat"  (month-name date, weekday after)
#   MONTH<  — "Sat Sep 6" · "Saturday, September 6, 2026"  (month-name date, weekday before)
# Word-boundary guard on the weekday token is (?![A-Za-z]) so "Sat" inside "Saturn" /
# "satisfaction" stays silent. Month names are matched CASE-SENSITIVELY capitalized so
# the verb "may" cannot seed a date. A weekday that is itself immediately FOLLOWED by a
# date ("9/6 — Mon 9/8") belongs to that next date and is skipped in the AFTER forms.
_DAY_CI = r"(?P<day>(?i:" + _DAY_ALT[1:-1] + r"))"          # named, case-insensitive
_TRAIL_DAY = r"(?i:" + _DAY_ALT + r")"                         # unnamed, for trailing-pair lookups
_MON = r"(?P<mon>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Sep|Oct|Nov|Dec)[a-z]*\.?"
_MON_DAY = r"\s+(?P<dd>\d{1,2})(?![\d/])(?P<rng>[-–—]\d{1,2}(?!\d))?(?:,?\s+(?P<yy>20\d{2}))?"
RE_WEEKDAY_AFTER = re.compile(
    r"(?<![\w/])(?P<date>" + _NUM_DATE[1:-1] + r")(?P<rng>[-–—]\d{1,2}(?:/\d{1,2})?)?"
    r"(?:[\s,.\-–—]+\(?|\s*\()" + _DAY_CI + r"\)?(?![A-Za-z])")
RE_WEEKDAY_MONTH_AFTER = re.compile(
    r"\b" + _MON + _MON_DAY + r"(?:[\s,.\-–—]+\(?|\s*\()" + _DAY_CI + r"\)?(?![A-Za-z])")
RE_WEEKDAY_MONTH_BEFORE = re.compile(
    r"\b" + _DAY_CI + r"[\s,.\-–—]+(?:\*\*)?" + _MON + _MON_DAY + r"\b")
MONTHS = {m: i + 1 for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}
MONTHS["Sept"] = 9

RE_HASH = re.compile(r"(?<![0-9a-zA-Z/])([0-9a-f]{7,40})(?![0-9a-zA-Z])")
# Only real PATHS (must contain "/"). A bare basename in prose — `fetch.py`,
# `orphan_check.sh` — is a conversational reference, not a cross-reference, and
# flagging those was pure noise on the first live run.
RE_PTR = re.compile(r"`([A-Za-z0-9_][A-Za-z0-9_.\-]*(?:/[A-Za-z0-9_.\-]+)+\.(?:md|tsv|py|sh|json|js|csv))`")

# label, name-regex, plausible band for the UNDERLYING, band for its tracking ETF, ETF ticker
UNITS = [
    ("gold",      re.compile(r"\bgold\b", re.I),            (1000, 20000), (50, 999),   "GLD"),
    ("S&P 500",   re.compile(r"\bS&P ?500\b|\bSPX\b"),      (2000, 20000), (200, 1999), "SPY"),
    ("Nasdaq",    re.compile(r"\bnasdaq\b|\bNDX\b", re.I),  (8000, 60000), (150, 1999), "QQQ"),
    ("Dow",       re.compile(r"\bdow\b|\bDJIA\b", re.I),    (15000, 90000), (150, 1999), "DIA"),
]
RE_MONEY = re.compile(r"\$\s?([0-9][0-9,]*(?:\.[0-9]+)?)")
PROXIMITY = 40   # chars between an instrument name and a price to attribute them

SKIP_DIRS = {".git", "node_modules", ".venv", "__pycache__"}
# Text surfaces a directory-expanded run will read (binaries/caches are pointless to scan).
TEXT_SUFFIXES = {".md", ".tsv", ".csv", ".txt", ".py", ".sh", ".json", ".yml", ".yaml"}
# How close a 4-digit year must sit to a bare M/D to be read as qualifying it.
YEAR_PROXIMITY = 30


def sh(args):
    return subprocess.run(args, capture_output=True, text=True, cwd=ROOT)


@functools.lru_cache(maxsize=None)
def hash_state(h):
    """'missing' | 'unreachable' | 'ok'"""
    if sh(["git", "cat-file", "-e", h + "^{commit}"]).returncode != 0:
        return "missing"
    if sh(["git", "merge-base", "--is-ancestor", h, "origin/master"]).returncode == 0:
        return "ok"
    return "unreachable"


def parse_date(tok, fallback_year):
    try:
        if "-" in tok:
            return datetime.date.fromisoformat(tok)
        p = tok.split("/")
        mo, da = int(p[0]), int(p[1])
        yr = fallback_year
        if len(p) == 3:
            yr = int(p[2]);  yr += 2000 if yr < 100 else 0
        return datetime.date(yr, mo, da)
    except (ValueError, IndexError):
        return None


def changed_files(staged_only=False):
    cmd = ["git", "diff", "--name-only", "--diff-filter=ACMR"]
    out = sh(cmd + (["--cached"] if staged_only else ["HEAD"])).stdout.split()
    if not staged_only:
        out += sh(["git", "ls-files", "--others", "--exclude-standard"]).stdout.split()
    return sorted(set(out))


def borrow_year(line, years, tok, pos, default):
    """Year for a bare M/D token at `pos`: the nearest 4-digit year within
    YEAR_PROXIMITY that is not part of a complete ISO date; else `default`."""
    if years and "-" not in tok and len(tok.split("/")) < 3:
        near = [t for t in years if abs(t[0] - pos) <= YEAR_PROXIMITY]
        if near:
            return min(near, key=lambda t: abs(t[0] - pos))[1]
    return default


def line_years(line):
    """4-digit years on the line that are NOT the year of a complete ISO date."""
    iso_year_spans = [mm.span(1) for mm in re.finditer(r"\b(20\d{2})-\d{2}-\d{2}\b", line)]
    return [(mm.start(), int(mm.group(1)))
            for mm in re.finditer(r"\b(20\d{2})\b", line)
            if not any(s <= mm.start(1) < e for s, e in iso_year_spans)]


def weekday_flags(rel, n, line, year):
    """All four weekday forms for ONE line. Returns [(rel, n, 'weekday', msg)]."""
    flags = []
    # A bare "8/6" inherits the year from the NEAREST 4-digit year named on
    # the same line, not from today. Caught on the first live run: DOCKET's
    # "Q2-2024 precedent = Tue 8/6" is CORRECT (2024-08-06 was a Tuesday) and
    # assuming 2026 made it look wrong. Nearly find-replaced a right answer.
    # ...but a year that is PART OF A COMPLETE DATE is already spoken for: it
    # describes that date, not a bare M/D elsewhere on the line. Without this
    # exclusion the heuristic inverts CORRECT text — live instance 2026-08-03,
    # CARL packet line 15: "...ELIMINATED Mon 8/3 (FHFA refused the delay; 15%
    # reserve req 2027-01-04)". The nearest year was 2027, so 8/3 resolved to
    # 2027-08-03 (a Tuesday) and "Mon 8/3" — which is right in 2026 — was
    # flagged as wrong. Same class as the DOCKET case above, opposite direction:
    # there the fix was to STOP assuming today's year, here it is to stop
    # borrowing a year that belongs to another date. (DAEDALUS, scripts/ break-fix)
    # ...and only borrow a year that is NEAR the date. "Nearest on the line"
    # is unbounded, so on a long STATUS line ANY 4-digit number hijacks the
    # date: measured 2026-08-03, an unbounded borrow produced 271 fleet flags
    # of which most resolved to 2006/2022/2025 and flagged CORRECT text
    # (BOND STATUS:96 "Fri 7/31" -> 2025 -> "Thursday, not Fri", when 7/31
    # IS a Friday in 2026). A year that qualifies a date sits beside it —
    # the DOCKET case this heuristic was built for, "Q2-2024 precedent =
    # Tue 8/6", is 22 chars. Beyond the window, trust --year.
    years = line_years(line)
    claimed = []   # date spans already graded by the BEFORE form

    def flag(label, d, want_name):
        flags.append((rel, n, "weekday",
                      f"\u201c{label}\u201d \u2014 {d.isoformat()} is a "
                      f"{DAYNAMES[d.weekday()]}, not {want_name}"))

    # ---- form 1: weekday BEFORE numeric date ("Fri 2026-07-25", "Mon 7/28") ----
    for m in RE_WEEKDAY.finditer(line):
        d = parse_date(m.group(2), borrow_year(line, years, m.group(2), m.start(), year))
        if not d:
            continue
        claimed.append(m.span(2))
        want = DAYMAP.get(m.group(1).lower()[:3])
        if want is None:
            continue
        # Two-day-range label guard (RED 8/7, ML-RED-143): "Tue-Wed 9/15-16"
        # pairs the SECOND weekday with the FIRST date — a correct,
        # primary-verified label flagged wrong, and the cheapest edit that
        # silences it damages the label. When this weekday is the trailing
        # half of a Day-Day pair: grade the LEADING day against the start
        # date, and grade THIS day against the END of a D/D-D range if one
        # is written (keeps power: "Tue-Thu 9/15-16" still flags on Thu vs
        # 9/16=Wed); with no range end, the trailing half is ungradeable —
        # skip it, never grade it against the start.
        pre = re.search(r"([A-Za-z]{3,9})[-\u2013\u2014]$", line[: m.start()])
        lead_want = (DAYMAP.get(pre.group(1).lower()[:3])
                     if pre and pre.group(1).lower() in DAYTOKENS else None)
        if lead_want is not None:
            if d.weekday() != lead_want:
                flags.append((rel, n, "weekday",
                              f"\u201c{pre.group(1)}-{m.group(0).strip()}\u201d \u2014 range start "
                              f"{d.isoformat()} is a {DAYNAMES[d.weekday()]}, "
                              f"not {pre.group(1)}"))
            endm = re.match(r"[-\u2013\u2014](\d{1,2}(?:/\d{1,2})?)(?!\d)", line[m.end():])
            if endm:
                ed = range_end(d, endm.group(1))
                if ed and ed.weekday() != want:
                    flags.append((rel, n, "weekday",
                                  f"\u201c{m.group(0).strip()}-{endm.group(1)}\u201d \u2014 range end "
                                  f"{ed.isoformat()} is a {DAYNAMES[ed.weekday()]}, "
                                  f"not {m.group(1)}"))
            continue
        if d.weekday() != want:
            flag(m.group(0).strip(), d, m.group(1))

    # ---- form 2: numeric date, weekday AFTER ("9/6 Sat", "2026-09-06 (Sat)", "9/5-6 Sat-Sun") ----
    for m in RE_WEEKDAY_AFTER.finditer(line):
        dspan = m.span("date")
        if any(a <= dspan[0] < b for a, b in claimed):
            continue                       # date already graded by form 1
        if RE_WEEKDAY.match(line, m.start("day")):
            continue                       # "9/6 \u2014 Mon 9/8": Mon belongs to 9/8
        d = parse_date(m.group("date"), borrow_year(line, years, m.group("date"), m.start(), year))
        if not d:
            continue
        want = DAYMAP.get(m.group("day").lower()[:3])
        if want is None:
            continue
        label = m.group(0).strip().rstrip(")")
        if d.weekday() != want:
            flag(label, d, m.group("day"))
        # trailing half of a Day-Day pair grades against the range END, if written
        trail = re.match(r"[-\u2013\u2014]" + _TRAIL_DAY + r"(?![A-Za-z])", line[m.end():])
        if trail and m.group("rng"):
            ed = range_end(d, m.group("rng")[1:])
            tw = DAYMAP.get(trail.group(1).lower()[:3])
            if ed and tw is not None and ed.weekday() != tw:
                flags.append((rel, n, "weekday",
                              f"\u201c{label}{trail.group(0)}\u201d \u2014 range end "
                              f"{ed.isoformat()} is a {DAYNAMES[ed.weekday()]}, not {trail.group(1)}"))

    # ---- form 3/4: month-name date, weekday AFTER or BEFORE ("Sep 6 (Sat)", "Sat Sep 6") ----
    # Day-Day pair guard applies here too: the FIRST fleet run of this form flagged
    # BRENT "Wed–Thu Aug 12-13" and SAM "Tue-Wed Sep 15-16" — both CORRECT labels —
    # because the trailing weekday was graded against the range START. Same RED 8/7
    # rule as form 1: lead vs start, trailing vs END, never trailing vs start.
    for rx, order in ((RE_WEEKDAY_MONTH_AFTER, "after"), (RE_WEEKDAY_MONTH_BEFORE, "before")):
        for m in rx.finditer(line):
            mon, dd, yy, day = m.group("mon"), m.group("dd"), m.group("yy"), m.group("day")
            day_pos = m.start("day")
            if order == "after" and RE_WEEKDAY.match(line, day_pos):
                continue
            mo = MONTHS.get(mon[:4] if mon.startswith("Sept") else mon[:3])
            if mo is None:
                continue
            y = int(yy) if yy else borrow_year(line, years, f"{mo}/{dd}", m.start(), year)
            try:
                d = datetime.date(y, mo, int(dd))
            except ValueError:
                continue
            want = DAYMAP.get(day.lower()[:3])
            if want is None:
                continue
            rng = m.group("rng")
            label = m.group(0).strip().rstrip(")")
            if order == "before":
                pre = re.search(r"([A-Za-z]{3,9})[-\u2013\u2014]$", line[:day_pos])
                lead_want = (DAYMAP.get(pre.group(1).lower()[:3])
                             if pre and pre.group(1).lower() in DAYTOKENS else None)
                if lead_want is not None:          # this weekday is the TRAILING half
                    if d.weekday() != lead_want:
                        flags.append((rel, n, "weekday",
                                      f"\u201c{pre.group(1)}-{label}\u201d \u2014 range start "
                                      f"{d.isoformat()} is a {DAYNAMES[d.weekday()]}, not {pre.group(1)}"))
                    if rng:
                        ed = range_end(d, rng[1:])
                        if ed and ed.weekday() != want:
                            flags.append((rel, n, "weekday",
                                          f"\u201c{label}\u201d \u2014 range end {ed.isoformat()} is a "
                                          f"{DAYNAMES[ed.weekday()]}, not {day}"))
                    continue
            if d.weekday() != want:
                flag(label, d, day)
            if order == "after" and rng:            # "Aug 12-13 Wed-Thu": trailing vs end
                trail = re.match(r"[-\u2013\u2014]" + _TRAIL_DAY + r"(?![A-Za-z])", line[m.end():])
                if trail:
                    ed = range_end(d, rng[1:])
                    tw = DAYMAP.get(trail.group(1).lower()[:3])
                    if ed and tw is not None and ed.weekday() != tw:
                        flags.append((rel, n, "weekday",
                                      f"\u201c{label}{trail.group(0)}\u201d \u2014 range end "
                                      f"{ed.isoformat()} is a {DAYNAMES[ed.weekday()]}, not {trail.group(1)}"))
    return flags


def range_end(d, tok):
    """End date of a "D/D-D" or "D/D-D/D" range given its start and the tail token."""
    try:
        return (datetime.date(d.year, *map(int, tok.split("/")))
                if "/" in tok else d.replace(day=int(tok)))
    except ValueError:
        return None


def check_file(path, checks, year):
    rel = str(pathlib.Path(path))
    p = ROOT / path
    if not p.is_file() or p.suffix.lower() not in {".md", ".tsv", ".txt", ".py", ".sh", ".json"}:
        return []
    try:
        text = p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    return check_text(rel, text, checks, year, p)


def check_text(rel, text, checks, year, p=None):
    flags = []
    for n, line in enumerate(text.splitlines(), 1):
        if "weekday" in checks:
            flags += weekday_flags(rel, n, line, year)
        if "hash" in checks:
            for m in RE_HASH.finditer(line):
                h = m.group(1)
                if not (re.search(r"[a-f]", h) and re.search(r"[0-9]", h)):
                    continue          # all-digit / all-alpha: not a hash
                st = hash_state(h)
                if st == "unreachable":
                    flags.append((rel, n, "hash",
                                  f"`{h}` is a real commit but NOT an ancestor of "
                                  f"origin/master — a reader cannot reach it. Cite a path."))
                elif st == "missing":
                    flags.append((rel, n, "hash",
                                  f"`{h}` resolves to no commit in this repo "
                                  f"(rebased away, GC'd, or foreign). Cite a path."))
        if "units" in checks:
            for label, rx, good, etf_band, etf in UNITS:
                if not rx.search(line):
                    continue
                # If the line names the ETF explicitly it is quoting BOTH on purpose
                # ("gold $4,078.30 · GLD $373.78") — that is correct writing, not a
                # conflation. Only an unaccompanied ETF-magnitude number is suspect.
                if re.search(rf"\b{etf}\b", line):
                    continue
                # Proximity, not whole-line. The HEARTBEAT stress dashboard is ONE
                # ~2,000-char line holding ~40 instruments; whole-line matching made
                # every name collide with every price. A price must sit within
                # PROXIMITY chars of the name to be attributed to it.
                spans = [m.span() for m in rx.finditer(line)]
                for m in RE_MONEY.finditer(line):
                    if not any(min(abs(m.start() - e), abs(s - m.end())) <= PROXIMITY
                               for s, e in spans):
                        continue
                    try:
                        v = float(m.group(1).replace(",", ""))
                    except ValueError:
                        continue
                    if etf_band[0] <= v <= etf_band[1] and not (good[0] <= v <= good[1]):
                        flags.append((rel, n, "units",
                                      f"“{label}” quoted at ${m.group(1)} — that is "
                                      f"{etf}'s magnitude, not the underlying "
                                      f"(expected {good[0]:,}–{good[1]:,}). ETF≠underlying."))
        if "pointer" in checks:
            for m in RE_PTR.finditer(line):
                t = m.group(1)
                if t.startswith(("http", "~")) or " " in t:
                    continue
                if not (ROOT / t).exists() and not (p is not None and (p.parent / t).exists()):
                    flags.append((rel, n, "pointer", f"`{t}` does not exist"))
    return flags


# Shipped falsification set (2026-09-03, PROME ask #2 — measure.py precedent). Each case is
# (line, expected weekday-flag count). The year is PINNED to 2026 so the set never drifts
# with the calendar. Three cases are PROME's reproduced false-cleans; three are the forms
# that always flagged (must keep flagging); the rest are negative controls and the three
# documented live regressions (DOCKET 2024 borrow · CARL 2027 non-borrow · RED range pair).
SELFTEST = [
    # PROME 9/3 table — 2026-09-06 is a SUNDAY
    ("x Sat 2026-09-06 y", 1),          # flagged before, must still
    ("x Sat 9/6 y", 1),                  # flagged before, must still
    ("x 9/6 Sat y", 1),                  # was CLEAN — weekday AFTER date
    ("x 9/6 (Saturday) y", 1),           # was CLEAN — parenthetical
    ("x Sep 6 (Sat) y", 1),              # was CLEAN — month-name form
    ("x Saturday 9/6 y", 1),             # flagged before, must still
    # negative controls — word-boundary guards
    ("x satisfaction 9/6 y", 0),
    ("x 9/6 satisfaction y", 0),
    ("x Saturn 9/6 y", 0),
    ("x 9/6 Saturn y", 0),
    ("x we may 6 (Sat) y", 0),           # lowercase 'may' is not a month
    # correct labels must stay CLEAN (2026-09-06 Sun, 2026-09-05 Sat, 2026-09-08 Tue)
    ("x 9/6 Sun y", 0),
    ("x 9/6 (Sunday) y", 0),
    ("x Sep 6 (Sun) y", 0),
    ("x Sun, September 6, 2026 y", 0),
    ("x 2026-09-06 (Sun) y", 0),
    ("x 9/5-6 Sat-Sun y", 0),            # after-form range: lead vs start, trail vs end
    ("x 9/5-6 Sat-Mon y", 1),            # ...and the trailing half is still graded
    ("x 9/6 \u2014 Tue 9/8 y", 0),        # the Tue belongs to 9/8, not to 9/6
    ("x Sat 9/5, Sunday 9/6 y", 0),      # two before-form labels, both right
    # documented live regressions
    ("Q2-2024 precedent = Tue 8/6", 0),                                   # borrow 2024
    ("ELIMINATED Mon 8/3 (FHFA refused; 15% reserve req 2027-01-04)", 0), # do NOT borrow 2027
    ("Tue-Wed 9/15-16", 0),                                               # RED range pair
    ("Tue-Thu 9/15-16", 1),                                               # ...keeps power
    # month-name range pairs — the first fleet run's two FALSE positives (BRENT L109, SAM L147)
    ("| **Wed\u2013Thu Aug 12-13** | COALITION WINDOW", 0),
    ("| Tue-Wed **Sep 15-16** | FOMC (SEP)", 0),
    ("| Tue-Thu **Sep 15-16** | FOMC (SEP)", 1),                           # ...keeps power
    ("Aug 12-13 Wed-Thu", 0),
    ("Aug 12-13 Wed-Fri", 1),
]


def selftest():
    fails = 0
    for line, want in SELFTEST:
        got = len(check_text("<selftest>", line, {"weekday"}, 2026))
        ok = got == want
        fails += not ok
        print(f"  {'\u2713' if ok else '\u2717'} expect {want} got {got}  {line!r}")
    if fails:
        print(f"CLAIM-CHECK SELFTEST \u2717 {fails}/{len(SELFTEST)} case(s) FAILED \u2014 do not trust the weekday check")
        return 1
    print(f"CLAIM-CHECK SELFTEST \u2713 {len(SELFTEST)}/{len(SELFTEST)} cases behaved [weekday]")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--staged", action="store_true")
    ap.add_argument("--check", default="weekday,hash,units,pointer")
    ap.add_argument("--year", type=int, default=datetime.date.today().year,
                    help="year assumed for bare M/D dates")
    ap.add_argument("--quiet", action="store_true", help="print only flags")
    ap.add_argument("--selftest", action="store_true",
                    help="run the shipped falsification set; exit 1 if any case misbehaves")
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    checks = {c.strip() for c in a.check.split(",") if c.strip()}
    files = a.paths or changed_files(a.staged)
    # Expand directory arguments. Without this, `claim_check.py AGENTS PROME` read the two
    # DIRECTORY names as files, failed silently on OSError, and printed
    # "✓ 2 file(s) clean" — a whole-fleet pass claimed off zero bytes read. PAT-074: a check
    # must be audited by what its PASS means. (DAEDALUS, scripts/ break-fix 2026-08-03)
    expanded = []
    for f in files:
        p = pathlib.Path(f)
        if p.is_dir():
            expanded += [str(q) for q in sorted(p.rglob("*"))
                         if q.is_file() and q.suffix.lower() in TEXT_SUFFIXES]
        else:
            expanded.append(f)
    files = expanded
    files = [f for f in files if not any(s in pathlib.Path(f).parts for s in SKIP_DIRS)]
    if not files:
        if not a.quiet:
            print("CLAIM-CHECK ✓ nothing to check")
        return 0

    all_flags = []
    for f in files:
        all_flags += check_file(f, checks, a.year)

    if not all_flags:
        if not a.quiet:
            print(f"CLAIM-CHECK ✓ {len(files)} file(s) clean [{','.join(sorted(checks))}]")
        return 0

    by_kind = {}
    for rel, n, kind, msg in all_flags:
        by_kind.setdefault(kind, []).append((rel, n, msg))
    print(f"CLAIM-CHECK ⚠️  {len(all_flags)} flag(s) across {len(files)} file(s)")
    for kind in sorted(by_kind):
        print(f"\n[{kind}]")
        for rel, n, msg in by_kind[kind]:
            print(f"  {rel}:{n}\n      {msg}")
    print("\nAdvisory — nothing blocked, nothing edited. A flag is a prompt to LOOK, "
          "not an instruction to find-replace.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
