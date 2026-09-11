#!/usr/bin/env python3
"""Every `^SKEW` session CBOE has published must carry a VALUE in VX_DAILY.

WHY THIS EXISTS (KB-VIO-283/285, built 2026-09-11 evening)
-----------------------------------------------------------
`vx_daily_gapcheck.py` asks whether the ROW exists. It does not ask whether the
`skew` CELL in that row is filled. **On 2026-09-11 the 9/11 row existed, carried
VIX/VIX9D/VIX3M/VVIX, and had a BLANK skew — and every blocking contract passed
green.** The stale-column guard had suppressed a real 154.49 close (its witness
was a 5-minute intraday feed against an EOD-only series), and nothing downstream
noticed, because a present row with a missing cell is invisible to a
session-presence check.

🔑 **THE CONSEQUENCE IS SPECIFIC TO THIS SERIES.** `^SKEW` is the grading source
for RED's **FT-10, a SUSTAIN-4 counter**. A sustain counter **cannot be
reconstructed after the fact from a ledger that skipped sessions** — a missing bar
is not a gap you can backfill an opinion into, it is a run you can no longer grade.
And the omission is silent in the safe-looking direction: the counter simply reads
0-of-N forever and every completeness check passes.

⚠️ **AND IT IS A STANDING OBLIGATION, NOT SESSION STATE.** As long as RED is dark
(dark since 2026-09-10; my acute bar packet was item 7 of NINE unconsumed in its
inbox), **nobody else is counting FT-10**, so this desk must keep the dated bars
existing for whenever RED does boot. That obligation first lived only in
`SCRATCH.md` — **the one file defined to be overwritten every session.** PROME
flagged it: *an obligation recorded only in the file designed to be overwritten is
the ledger-with-gaps failure one level up — the thing that PREVENTS the gap is
itself gap-prone.* **This file is the durable form of that commitment**, because a
ritual a session must remember is a ritual a session will eventually skip
(`[[finding_mechanize_the_cap_not_the_ritual]]`).

THE REFERENCE IS THE PUBLISHER, NEVER THE LEDGER
------------------------------------------------
The set of sessions that SHOULD have a value comes from CBOE's own
`SKEW_History.csv`, bounded below by where the ledger starts and above by the
publisher's frontier. **A ledger cannot be its own completeness reference**
(KB-VIO-277, the defect that made `hi = max(ledger)` report silent-green on a
trailing gap). Rows ahead of the frontier are the live session CBOE has not
settled yet and are NOT graded.

Fails CLOSED: an unreachable endpoint is UNKNOWN, not a pass.

Run: .venv/bin/python3 AGENTS/VIOLET/scripts/skew_bar_continuity.py [--quiet]
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from vx_daily_gapcheck import fetch_dates  # noqa: E402  (one source of truth)

DAILY_LOG = SCRIPT_DIR.parent / "workbook" / "VX_DAILY.tsv"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="^SKEW bar continuity in VX_DAILY.")
    ap.add_argument("--quiet", action="store_true", help="only print on failure")
    a = ap.parse_args(argv)

    if not DAILY_LOG.exists():
        print(f"  🔴 CANNOT CERTIFY — {DAILY_LOG} is missing. Absent is UNKNOWN, not a pass.")
        return 2
    with DAILY_LOG.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    if not rows:
        print("  🔴 CANNOT CERTIFY — VX_DAILY has no rows.")
        return 2

    published = fetch_dates("SKEW")
    if published is None:
        print("  🔴 CANNOT CERTIFY — CBOE SKEW_History.csv unreachable. "
              "An unverifiable reference is UNKNOWN, not a pass.")
        return 2

    have = {r["date"]: (r.get("skew") or "").strip() for r in rows if r.get("date")}
    lo, frontier = min(have), max(published)
    # Graded window: published sessions inside the ledger's own span, never past
    # the publisher's frontier (rows ahead of it are the unsettled live session).
    graded = sorted(d for d in published if lo <= d <= frontier)

    missing_row = [d for d in graded if d not in have]
    blank_cell = [d for d in graded if d in have and not have[d]]

    if not a.quiet:
        print(f"  span {lo} → {frontier}  ·  CBOE-published ^SKEW sessions: {len(graded)}")
        ahead = sorted(d for d in have if d > frontier)
        if ahead:
            print(f"  ahead of publisher frontier (not graded): {len(ahead)} — {', '.join(ahead)}")

    if missing_row or blank_cell:
        if blank_cell:
            print(f"  🔴 {len(blank_cell)} published ^SKEW session(s) present in VX_DAILY with a BLANK "
                  f"skew cell: {', '.join(blank_cell[-12:])}")
            print("     A present row with a missing cell is INVISIBLE to the session-presence check.")
            print("     Repair: .venv/bin/python3 AGENTS/VIOLET/scripts/backfill.py --spot-only")
        if missing_row:
            print(f"  🔴 {len(missing_row)} published ^SKEW session(s) have NO row: "
                  f"{', '.join(missing_row[-12:])}")
        print("  ⚠️  FT-10 is SUSTAIN-4 on this series. A skipped bar cannot be reconstructed "
              "after the fact — the run becomes ungradeable, silently, reading 0-of-N.")
        return 1

    if not a.quiet:
        print(f"  ✅ SKEW BAR CONTINUITY rc=0 — all {len(graded)} published session(s) "
              f"carry a value; no blank cells, no missing rows.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
