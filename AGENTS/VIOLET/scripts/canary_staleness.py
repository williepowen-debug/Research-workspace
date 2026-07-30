#!/usr/bin/env python3
"""VIOLET CANARY_MAP staleness enforcement — the check the map has been asking for since v1.0.

`CANARY_MAP.md` § Staleness audit contract declares: *"A canary is DARK when its
last pull exceeds 2x its stated cadence (EOD instruments: >2 trading days; weekly
COT: >9 days)."* That contract was **UNENFORCED FROM v1.0 UNTIL 2026-07-28**, and
when it was finally audited by hand the file was **breaching it on five rows** —
COT 21d, JPY 11d, OVX 11d, cheap-tail 6d, and a Tier-3 GEX band 18d that sits
inside a registered VIOLET fire-condition.

The map names its own root cause: *"extend `ledger_staleness.py` coverage to this
file's Tier-1/2 pull dates = a future small ask"* had sat in the doc since v1.0 and
**was never built, so the only thing enforcing the contract was remembering to.**
The instrument the map exists to protect — a canary going dark unnoticed — went
dark inside the map's own text. (auto-memory `finding_mechanize_the_cap_not_the_ritual`.)

⚠️ WHY THIS LIVES IN `AGENTS/VIOLET/scripts/` AND NOT IN THE ROOT `ledger_staleness.py`:
the root script is a shared file VIOLET may not commit (root CLAUDE.md § Git
Protocol). The contract, the map and every backing ledger are VIOLET-owned, so the
enforcement belongs here. Wired into VIOLET's own `boot.py`.

METHOD — content vintage, never mtime. Each Tier-1 canary writes a dated row to a
workbook ledger; we read the MAX DATE in that ledger and compare it to the row's
stated cadence. ⚠️ mtime is corrupted by git sync (a pull restamps every file), so
an mtime-based freshness check fails FALSE-NEGATIVE — the failure direction that
lets a dark canary read as fresh (auto-memory `finding_mtime_is_corrupted_by_git_sync`).

Exit codes: 0 = all canaries within contract (or only un-ledgered rows flagged);
1 = at least one DARK canary, with --strict.

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/canary_staleness.py
  .venv/bin/python3 AGENTS/VIOLET/scripts/canary_staleness.py --quiet   # boot mode
"""
from __future__ import annotations

import argparse
import csv
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

VIOLET_DIR = Path(__file__).resolve().parents[1]
WB = VIOLET_DIR / "workbook"

# (canary, ledger, date column, cadence label, DARK threshold in CALENDAR days)
# Thresholds are 2x cadence per the contract, expressed in calendar days with
# weekend slack so a routine Fri-pull read on Monday does not false-fire.
CANARIES = [
    ("VIX3M/VIX inversion", "VX_DAILY.tsv",  "date",        "EOD daily", 4),
    ("VVIX",                "VX_DAILY.tsv",  "date",        "EOD daily", 4),
    ("SKEW + sustain",      "VX_DAILY.tsv",  "date",        "EOD daily", 4),
    ("JPY vol (carry)",     "JPY_VOL.tsv",   "date",        "EOD daily", 4),
    ("OVX/VIX ratio",       "OVX.tsv",       "date",        "EOD daily", 4),
    ("Cheap-tail window",   "CHEAP_TAIL.tsv","date",        "EOD daily", 4),
    ("COT VIX lev-money",   "COT_VIX.tsv",   "report_date", "weekly",    9),
]

# Rows with a registered threshold but NO backing ledger — they cannot be checked
# mechanically, which is itself worth surfacing rather than silently passing.
UNLEDGERED = [
    ("MOVE (rates vol)", "investing.com primary; yf ^MOVE unreliable as sole source"),
    ("CCC-BB dispersion + CCC OAS", "FRED via fred_fetch --summary (cache dir, not a dated ledger)"),
    ("Broad equity put/call", "WALTER-intake only — genuinely un-pullable, declared dark at v1.2"),
]


def max_date(path: Path, col: str) -> date | None:
    if not path.exists():
        return None
    best = None
    try:
        with path.open(newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                v = (row.get(col) or "").strip()
                if not v:
                    continue
                try:
                    d = datetime.fromisoformat(v).date()
                except ValueError:
                    continue
                if best is None or d > best:
                    best = d
    except OSError:
        return None
    return best


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--quiet", action="store_true", help="print only breaches (boot mode)")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any canary is DARK")
    a = ap.parse_args(argv)

    today = date.today()
    dark, rows = [], []
    for name, ledger, col, cadence, limit in CANARIES:
        d = max_date(WB / ledger, col)
        if d is None:
            rows.append((name, ledger, "NO DATA", "?", "🔴 DARK"))
            dark.append(f"{name}: no dated rows in {ledger}")
            continue
        age = (today - d).days
        state = "🔴 DARK" if age > limit else ("🟡 aging" if age > limit // 2 else "🟢 fresh")
        if age > limit:
            dark.append(f"{name}: {ledger} last row {d} = {age}d old (contract: DARK >{limit}d, {cadence})")
        rows.append((name, ledger, str(d), f"{age}d", state))

    if not a.quiet:
        print("CANARY_MAP staleness — contract: DARK when last pull > 2x cadence")
        print(f"{'canary':30s} {'ledger':16s} {'last row':12s} {'age':>5s}  state")
        print("-" * 78)
        for r in rows:
            print(f"{r[0]:30s} {r[1]:16s} {r[2]:12s} {r[3]:>5s}  {r[4]}")
        print()
        print("Un-ledgered rows (cannot be checked mechanically — verify by hand):")
        for n, why in UNLEDGERED:
            print(f"  · {n:32s} {why}")
        print()

    if dark:
        print(f"  🔴 CANARY_MAP CONTRACT BREACH — {len(dark)} DARK:")
        for d_ in dark:
            print(f"     {d_}")
        return 1 if a.strict else 0
    if not a.quiet:
        print("  ✓ all ledger-backed canaries within contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
