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
Exit 0 = clean · 1 = flags found (advisory) · 2 = usage/environment error.
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

# day-name immediately before a date: "Fri 2026-07-25", "Mon 7/28", "Tuesday 7/28"
RE_WEEKDAY = re.compile(
    r"\b(Mon|Tue|Tues|Wed|Thu|Thur|Thurs|Fri|Sat|Sun|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)"
    r"[\s,.\-–—]+(?:\*\*)?(\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}(?:/\d{2,4})?)\b", re.I)

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


def check_file(path, checks, year):
    rel = str(pathlib.Path(path))
    p = ROOT / path
    if not p.is_file() or p.suffix.lower() not in {".md", ".tsv", ".txt", ".py", ".sh", ".json"}:
        return []
    try:
        text = p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    flags = []
    for n, line in enumerate(text.splitlines(), 1):
        if "weekday" in checks:
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
            iso_year_spans = [mm.span(1) for mm in
                              re.finditer(r"\b(20\d{2})-\d{2}-\d{2}\b", line)]
            years = [(mm.start(), int(mm.group(1)))
                     for mm in re.finditer(r"\b(20\d{2})\b", line)
                     if not any(s <= mm.start(1) < e for s, e in iso_year_spans)]
            for m in RE_WEEKDAY.finditer(line):
                y = year
                if years and "-" not in m.group(2) and len(m.group(2).split("/")) < 3:
                    # ...and only borrow a year that is NEAR the date. "Nearest on the line"
                    # is unbounded, so on a long STATUS line ANY 4-digit number hijacks the
                    # date: measured 2026-08-03, an unbounded borrow produced 271 fleet flags
                    # of which most resolved to 2006/2022/2025 and flagged CORRECT text
                    # (BOND STATUS:96 "Fri 7/31" -> 2025 -> "Thursday, not Fri", when 7/31
                    # IS a Friday in 2026). A year that qualifies a date sits beside it —
                    # the DOCKET case this heuristic was built for, "Q2-2024 precedent =
                    # Tue 8/6", is 22 chars. Beyond the window, trust --year.
                    near = [t for t in years if abs(t[0] - m.start()) <= YEAR_PROXIMITY]
                    if near:
                        y = min(near, key=lambda t: abs(t[0] - m.start()))[1]
                d = parse_date(m.group(2), y)
                if not d:
                    continue
                want = DAYMAP.get(m.group(1).lower()[:3])
                if want is not None and d.weekday() != want:
                    flags.append((rel, n, "weekday",
                                  f"“{m.group(0).strip()}” — {d.isoformat()} is a "
                                  f"{DAYNAMES[d.weekday()]}, not {m.group(1)}"))
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
                if not (ROOT / t).exists() and not (p.parent / t).exists():
                    flags.append((rel, n, "pointer", f"`{t}` does not exist"))
    return flags


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--staged", action="store_true")
    ap.add_argument("--check", default="weekday,hash,units,pointer")
    ap.add_argument("--year", type=int, default=datetime.date.today().year,
                    help="year assumed for bare M/D dates")
    ap.add_argument("--quiet", action="store_true", help="print only flags")
    a = ap.parse_args()

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
