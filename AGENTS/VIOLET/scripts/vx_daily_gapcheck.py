#!/usr/bin/env python3
"""`VX_DAILY.tsv` session-completeness check — the OMISSION half of ledger integrity.

WHY THIS EXISTS
---------------
`VX_DAILY.tsv` is the ledger every `^SKEW` sustain claim is counted from, so a
missing session is not cosmetic: `RED-FT-10` counts consecutive CBOE bars ≥150,
and a hole in the ledger is indistinguishable from a bar that reset the chain.
On 2026-09-06 the ledger was missing 8/28 · 8/31 · 9/1 · 9/3 — four sessions,
inside the live FT-10 window — while every boot check ran green, because
`ledger_staleness.py` measures **VINTAGE, NOT GAPS**: a ledger whose newest row
is today is "fresh" no matter how many holes sit behind it.

This is deliberately the complement of `skew_integrity.py`, which compares
VALUES and is blind to a missing row; this compares the SET OF DATES and is
blind to a wrong value. Neither is sufficient alone. Run both.

⛔ THE TRAP THIS TOOL EXISTS TO NOT FALL INTO
---------------------------------------------
The obvious implementation — "every date in CBOE's `VIX_History.csv` must appear
in the ledger" — IS WRONG, and wrong in the direction that manufactures work.
**CBOE's own `VIX_History.csv` publishes a VIX close on days the US equity market
was CLOSED.** Measured 2026-09-06 over 2025-01-01 → 2026-09-04: 13 such dates,
every one a market holiday (MLK, Presidents', Memorial, Juneteenth, July 4th,
Labor Day, Thanksgiving, and 2025-01-09, the Carter day of mourning).

🔑 The phantom-holiday print is therefore **NOT a yfinance artifact**. VIOLET's
`MEMORY.md` DATA SOURCES entry attributes it to yfinance ("yfinance ^VIX
phantom-prints on US market holidays"); that attribution is incomplete. The
defect is UPSTREAM, in CBOE's published file, and yfinance inherits it. Anything
sourcing `^VIX` from anywhere inherits it.

The discriminator is the companion rule, and at CBOE it is exact: on all 13
dates `VIX` is published while `VIX3M` / `VIX6M` / `VVIX` / `SKEW` / `VIX9D` are
ALL absent. **13 of 13 caught, 0 false positives** over the same span. A real
session publishes companions; a phantom publishes an orphan VIX. That is the same
rule `backfill.py`'s spot path already applies to yfinance — it is applied here to
CBOE because the defect was never yfinance's to begin with.

⇒ A TRUE SESSION = a date where CBOE publishes VIX **and at least one companion**.
No holiday calendar is synthesized anywhere in this file. That is deliberate and
it is KB-VIO-243's rule, paid for three times: when a guard needs an external
schedule, derive it from observed history, never from a model of the schedule.

⛔ THE SECOND TRAP — THE ONE THIS FILE FELL INTO (fixed 2026-09-11)
-------------------------------------------------------------------
The span ran `lo = min(ledger)` → `hi = max(ledger)`. **The audit's upper bound
was the audited artifact's own last row**, so a trailing-edge gap could not exist
by construction: the ledger stopped at 9/7, CBOE had published through 9/10, and
9/8·9/9·9/10 fell OUTSIDE the window the check asked about. It printed the
identical `rc=0 … no gaps` verdict at 416 rows (three sessions missing) and at
419 (repaired). Found 2026-09-11; the docstring above was already boasting about
a different trap while this one ran.

The same broken reference fires in the OTHER direction intraday. Boot appends a
live TICK row for today; CBOE has not published today's bar until after settle;
so today's legitimate row was in the ledger, absent from `sessions`, and got
reported as a **PHANTOM**. One defect, two opposite symptoms — silent-green on a
real gap, loud-red on a correct row.

🔑 Both close with one change, and it is a change of REFERENCE, not of threshold:
**the upper bound is the PUBLISHER'S FRONTIER** — the newest date CBOE publishes
VIX with at least one companion — **never the ledger's own maximum.** A ledger
cannot be its own completeness reference. Zero free parameters: no grace window,
no holiday calendar, no "today" special case. Rows ahead of the frontier are the
unsettled live session; they are reported as ungraded, never as defects, and they
self-heal into the audited span as soon as CBOE publishes.

`extra` was also unbounded (`have - sessions`), charging the ledger for rows
outside the audited window whenever `--since` was passed. Now bounded both sides.

Exit codes: 0 = complete; 1 = missing session(s) or phantom row(s); 2 = could not
reach CBOE (fails CLOSED — an unreachable publisher is an unknown, not a pass).
"""
from __future__ import annotations

import argparse
import csv
import io
import sys
from pathlib import Path

import requests

SCRIPT_DIR = Path(__file__).resolve().parent
VIOLET_DIR = SCRIPT_DIR.parent
DAILY_LOG = VIOLET_DIR / "workbook" / "VX_DAILY.tsv"

CBOE_HISTORY_URL = "https://cdn.cboe.com/api/global/us_indices/daily_prices/{sym}_History.csv"
COMPANIONS = ("VIX3M", "VIX6M", "VVIX", "SKEW", "VIX9D")


def fetch_dates(sym: str) -> set[str] | None:
    """Dates on which CBOE publishes `sym`. None = endpoint unreachable (fail closed)."""
    try:
        r = requests.get(CBOE_HISTORY_URL.format(sym=sym), timeout=30,
                         headers={"User-Agent": "Mozilla/5.0"})
    except requests.RequestException as e:
        print(f"  ⚠ CBOE {sym}: {e}")
        return None
    if r.status_code != 200:
        print(f"  ⚠ CBOE {sym}: HTTP {r.status_code}")
        return None
    out = set()
    for row in csv.DictReader(io.StringIO(r.text)):
        d = row.get("DATE") or row.get("Date")
        if not d or "/" not in d:
            continue
        mm, dd, yy = d.split("/")
        out.add(f"{yy}-{mm}-{dd}")
    return out


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--quiet", action="store_true", help="one verdict line only")
    p.add_argument("--since", default=None, help="ISO date; default = ledger's own first row")
    p.add_argument("--ledger", default=None,
                   help="ledger path to audit (default: workbook/VX_DAILY.tsv). "
                        "Exists so this guard can be falsified against a FIXTURE "
                        "instead of by mutating the live ledger.")
    args = p.parse_args(argv)

    ledger = Path(args.ledger) if args.ledger else DAILY_LOG
    if not ledger.exists():
        print(f"🔴 GAPCHECK rc=2: {ledger} not found")
        return 2
    with open(ledger) as f:
        have = {r["date"] for r in csv.DictReader(f, delimiter="\t") if r.get("date")}
    if not have:
        print("🔴 GAPCHECK rc=2: ledger has no rows")
        return 2

    vix_dates = fetch_dates("VIX")
    if vix_dates is None:
        print("🔴 GAPCHECK rc=2 CANNOT-CERTIFY: CBOE VIX history unreachable — "
              "an unreachable publisher is an UNKNOWN, not a pass")
        return 2

    companion_dates: set[str] = set()
    reached = 0
    for sym in COMPANIONS:
        got = fetch_dates(sym)
        if got is not None:
            companion_dates |= got
            reached += 1
    if reached == 0:
        print("🔴 GAPCHECK rc=2 CANNOT-CERTIFY: no companion series reachable — "
              "cannot separate a real session from a holiday phantom")
        return 2

    lo = args.since or min(have)
    # 🔑 THE UPPER BOUND IS THE PUBLISHER'S FRONTIER, NEVER THE LEDGER'S OWN LAST
    # ROW. See "THE SECOND TRAP" in the docstring — `hi = max(have)` made a
    # trailing-edge gap unrepresentable AND false-flagged the live session.
    frontier = max((d for d in vix_dates if d in companion_dates), default=None)
    if frontier is None:
        print("🔴 GAPCHECK rc=2 CANNOT-CERTIFY: CBOE published no date carrying "
              "VIX *and* a companion — cannot establish a publication frontier")
        return 2
    hi = frontier
    # A TRUE session: CBOE publishes VIX *and* at least one companion. See docstring.
    sessions = {d for d in vix_dates if lo <= d <= hi and d in companion_dates}
    phantoms = {d for d in vix_dates if lo <= d <= hi and d not in companion_dates}

    missing = sorted(sessions - have)
    # `extra` is bounded to the audited span on BOTH sides. Unbounded, it charged
    # the ledger for rows outside the window it was asked about.
    extra = sorted(d for d in have if lo <= d <= hi and d not in sessions)
    # Rows ahead of the frontier are the LIVE session CBOE has not settled yet.
    # Not a defect and not certified either — reported so it is never silent.
    ahead = sorted(d for d in have if d > hi)

    if not args.quiet:
        print(f"  span {lo} → {hi}")
        print(f"  CBOE true sessions (VIX + ≥1 companion): {len(sessions)}")
        print(f"  holiday phantoms excluded (orphan VIX):  {len(phantoms)}")
        print(f"  ledger rows in span:                     "
              f"{len([d for d in have if lo <= d <= hi])}")
        if ahead:
            print(f"  ahead of publisher frontier (not graded): {len(ahead)} "
                  f"— {', '.join(ahead)}")

    if missing:
        print(f"  🔴 MISSING {len(missing)} session(s) CBOE published and the ledger lacks:")
        for d in missing:
            print(f"     {d}")
    if extra:
        print(f"  🔴 PHANTOM {len(extra)} ledger row(s) on a non-session:")
        for d in extra:
            print(f"     {d}")

    if missing or extra:
        print(f"🔴 VX_DAILY GAPCHECK rc=1 — {len(missing)} missing, {len(extra)} phantom. "
              f"Repair: backfill.py --spot-only")
        return 1
    print(f"✅ VX_DAILY GAPCHECK rc=0 — {len(sessions)} session(s) {lo}→{hi}, "
          f"no gaps, no phantoms ({len(phantoms)} holiday phantom(s) correctly absent)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
