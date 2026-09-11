#!/usr/bin/env python3
"""Regression test for `skew_bar_continuity.py`.

WHY THIS EXISTS (KB-VIO-285)
-----------------------------
On 2026-09-11 the VX_DAILY row for 9/11 existed, carried VIX/VIX9D/VIX3M/VVIX, and
had a BLANK `skew` cell — and **every blocking closeout contract passed green**.
`vx_daily_gapcheck.py` asks whether the ROW exists; a present row with a missing
cell is invisible to it. The blank was a suppressed real close of 154.49, a value
above the 150 line on RED's SUSTAIN-4 FT-10 counter.

⚠️ THE PROPERTY UNDER TEST
---------------------------
Not "it reports green today." Three things that must hold together:
  · a BLANK CELL on a published session FAILS          (A — the actual 9/11 regression)
  · a row AHEAD of the publisher frontier is NOT FLAGGED (C — else the live
    unsettled session goes red every evening and the guard gets waved through,
    which is the n=4 CANARY_MAP failure)
  · an unreachable publisher is UNKNOWN, never a pass   (D — fail closed)

And (F) the ablation: the session-presence logic alone does NOT catch (A). If that
ever starts catching it, this file is redundant and should be retired deliberately
rather than left as decoration.

FROZEN AND OFFLINE: the publisher and the ledger are both fixtures. No network.

Run: .venv/bin/python3 AGENTS/VIOLET/scripts/tests/test_skew_bar_continuity.py
"""
from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPTS_DIR))

import skew_bar_continuity as sbc  # noqa: E402

COLS = ["date", "vix", "vix3m", "vix6m", "vvix", "skew", "basis"]
PUB = {"2026-09-08", "2026-09-09", "2026-09-10"}          # publisher frontier = 09-10
LIVE = "2026-09-11"                                        # ahead of the frontier


class R:
    def __init__(self) -> None:
        self.ok, self.n = True, 0

    def check(self, label: str, got, want) -> None:
        self.n += 1
        good = got == want
        print(("  ✅ " if good else "  ❌ ") + f"{label}  [got {got}, want {want}]")
        self.ok = self.ok and good


def write(tmp: Path, rows: list[dict]) -> None:
    p = tmp / "VX_DAILY.tsv"
    with p.open("w", encoding="utf-8", newline="") as fh:
        fh.write("\t".join(COLS) + "\n")
        for r in rows:
            fh.write("\t".join(str(r.get(c, "")) for c in COLS) + "\n")
    sbc.DAILY_LOG = p


def row(d: str, skew: str = "147.02") -> dict:
    return {"date": d, "vix": "17.84", "vix3m": "19.73", "vix6m": "21.17",
            "vvix": "102.66", "skew": skew, "basis": "SETTLE"}


def main() -> int:
    r = R()
    tmp = Path(tempfile.mkdtemp(prefix="violet_sbc_"))
    real_fetch, real_log = sbc.fetch_dates, sbc.DAILY_LOG
    sbc.fetch_dates = lambda sym: set(PUB)

    full = [row("2026-09-08"), row("2026-09-09"), row("2026-09-10")]

    print("\n--- A. BLANK cell on a published session -> must FAIL (the 9/11 regression) ---")
    write(tmp, [row("2026-09-08"), row("2026-09-09"), row("2026-09-10", skew="")])
    r.check("blank skew cell is caught", sbc.main(["--quiet"]), 1)

    print("\n--- B. published session with NO row -> must FAIL ---")
    write(tmp, [row("2026-09-08"), row("2026-09-10")])
    r.check("missing row is caught", sbc.main(["--quiet"]), 1)

    print("\n--- C. row AHEAD of the frontier with a blank -> must NOT be flagged ---")
    write(tmp, full + [row(LIVE, skew="")])
    r.check("live unsettled session is not graded", sbc.main(["--quiet"]), 0)

    print("\n--- D. publisher unreachable -> UNKNOWN (2), never a pass ---")
    write(tmp, full)
    sbc.fetch_dates = lambda sym: None
    r.check("unreachable publisher fails CLOSED", sbc.main(["--quiet"]), 2)
    sbc.fetch_dates = lambda sym: set(PUB)

    print("\n--- E. every published session carries a value -> PASS ---")
    write(tmp, full)
    r.check("clean ledger passes", sbc.main(["--quiet"]), 0)

    print("\n--- F. ABLATION: session-PRESENCE alone does not catch a blank cell ---")
    # This is the gapcheck's question, reproduced: do the row DATES match the
    # publisher? On fixture A they match exactly -- which is why 9/11 shipped green.
    ledger_dates = {"2026-09-08", "2026-09-09", "2026-09-10"}
    r.check("presence check sees no gap on the blank-cell ledger",
            sorted(PUB - ledger_dates), [])
    write(tmp, [row("2026-09-08"), row("2026-09-09"), row("2026-09-10", skew="")])
    r.check("...while THIS check fails it", sbc.main(["--quiet"]), 1)

    sbc.fetch_dates, sbc.DAILY_LOG = real_fetch, real_log
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"\n{'ALL ' + str(r.n) + ' CHECKS PASSED' if r.ok else 'FAILED'}")
    return 0 if r.ok else 1


if __name__ == "__main__":
    sys.exit(main())
