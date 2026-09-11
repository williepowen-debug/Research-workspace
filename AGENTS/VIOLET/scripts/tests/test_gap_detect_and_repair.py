#!/usr/bin/env python3
"""Regression test for the DETECT + REPAIR pair on a VX_DAILY trailing-edge gap.

WHY THIS EXISTS
---------------
Both halves of this pair shipped broken and were certified green by their own
output for weeks:

  `vx_daily_gapcheck.py`  ran the audit span to `hi = max(ledger)`, so a
  trailing-edge gap was unrepresentable — identical `rc=0 ... no gaps` at 416
  rows (three sessions missing) and 419 (repaired). The same broken reference
  also false-flagged the live intraday row as a PHANTOM. (KB-VIO-273)

  `backfill.py`  UPDATED rows and never CREATED them, so the repair the gapcheck
  printed could not actually run: a `--spot-only` pass over the hole touched 27
  rows, added 0, and reported "2,496 cells agreed."

⇒ Detection and repair must be tested TOGETHER. Fixing either alone leaves the
hole, and each one's own verdict looks clean while the other is broken.

FROZEN AND OFFLINE ON PURPOSE
-----------------------------
Fixture dates are synthetic (2030-01) and the CBOE publisher is a frozen dict,
not a live fetch. A test pinned to the live ledger's current values rots on the
next edit and a test that hits the network fails for reasons that are not the
code's. Nothing here changes when the real ledger does.

The frozen scenario:
    CBOE publishes VIX on   01-02 01-03 01-04 01-07 01-08 01-09 01-10
    companions present on   01-02 01-03 01-04       01-08 01-09 01-10
    => 01-07 is an ORPHAN VIX = holiday phantom, must never be created
    => publication frontier = 01-10
    ledger holds            01-02 01-03 01-04                   + 01-11 (live TICK)
    => 3 missing sessions; 01-11 is AHEAD of the frontier and is not a defect

Run: .venv/bin/python3 AGENTS/VIOLET/scripts/tests/test_gap_detect_and_repair.py
"""
from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = TESTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

import backfill                    # noqa: E402
import vx_daily_gapcheck as gc     # noqa: E402

VIX_DATES = ["2030-01-02", "2030-01-03", "2030-01-04",
             "2030-01-07", "2030-01-08", "2030-01-09", "2030-01-10"]
COMPANION_DATES = ["2030-01-02", "2030-01-03", "2030-01-04",
                   "2030-01-08", "2030-01-09", "2030-01-10"]
HOLIDAY = "2030-01-07"
FRONTIER = "2030-01-10"
LIVE_ROW = "2030-01-11"

_SPOT = {
    "2030-01-08": dict(vix=17.50, vix9d=16.10, vix3m=18.60, vix6m=19.30, vvix=93.00, skew=143.00),
    "2030-01-09": dict(vix=18.00, vix9d=16.60, vix3m=18.80, vix6m=19.40, vvix=95.00, skew=144.00),
    "2030-01-10": dict(vix=18.50, vix9d=17.10, vix3m=19.00, vix6m=19.50, vvix=97.00, skew=145.00),
    "2030-01-02": dict(vix=16.00, vix9d=15.00, vix3m=18.00, vix6m=19.00, vvix=90.00, skew=140.00),
    "2030-01-03": dict(vix=16.50, vix9d=15.40, vix3m=18.20, vix6m=19.10, vvix=91.00, skew=141.00),
    "2030-01-04": dict(vix=17.00, vix9d=15.80, vix3m=18.40, vix6m=19.20, vvix=92.00, skew=142.00),
}


def frozen_hist() -> dict[str, dict[str, float]]:
    """CBOE publisher of record, frozen. `vix` carries the holiday orphan; no
    companion does. No date beyond the frontier exists — the live session is
    genuinely unpublished, which is what makes 01-11 'ahead', not 'phantom'."""
    hist: dict[str, dict[str, float]] = {c: {} for c in backfill.CBOE_SERIES}
    for d, vals in _SPOT.items():
        for col, v in vals.items():
            hist[col][d] = v
    hist["vix"][HOLIDAY] = 17.25  # orphan: published by CBOE on a closed session
    return hist


class Result:
    def __init__(self) -> None:
        self.ok = True
        self.n = 0

    def check(self, label: str, cond: bool, detail: str = "") -> None:
        self.n += 1
        print(("  ✅ " if cond else "  ❌ ") + label + (f"  [{detail}]" if detail else ""))
        self.ok = self.ok and bool(cond)


def read_rows(p: Path) -> tuple[list[str], dict[str, list[str]]]:
    lines = p.read_text().splitlines()
    hdr = lines[0].split("\t")
    return hdr, {ln.split("\t")[0]: ln.split("\t") for ln in lines[1:] if ln.strip()}


def main() -> int:
    r = Result()
    hist = frozen_hist()
    gc.fetch_dates = lambda sym: (set(VIX_DATES) if sym == "VIX"
                                  else set(COMPANION_DATES))

    tmp = Path(tempfile.mkdtemp(prefix="violet_gap_"))
    work = tmp / "VX_DAILY.tsv"
    shutil.copy(TESTS_DIR / "fixtures" / "gap_ledger_BROKEN.tsv", work)
    backfill.DAILY_LOG = work

    print("\n--- 1. gapcheck DETECTS the trailing gap (and does not cry phantom) ---")
    rc = gc.main(["--ledger", str(work), "--quiet"])
    r.check("rc=1 on the broken ledger", rc == 1, f"rc={rc}")

    print("\n--- 2. backfill REPAIRS it ---")
    hdr, rows = backfill.load_existing()
    before = len(rows)
    stats = backfill.backfill_spot_cboe(rows, today=LIVE_ROW, hist=hist, failed=set())
    backfill.write_merged(hdr, rows)
    r.check("created exactly 3 rows", stats.get("created", 0) == 3,
            f"created={stats.get('created', '<key absent: pre-fix backfill>')}")
    r.check("row count 4 -> 7", (before, len(rows)) == (4, 7), f"{before}->{len(rows)}")

    print("\n--- 3. created rows are correct, and conventions held ---")
    cols, got = read_rows(work)
    cell = lambda d, c: got[d][cols.index(c)]
    r.check("01-10 vix == 18.5", cell(FRONTIER, "vix") == "18.5", cell(FRONTIER, "vix"))
    r.check("01-10 vvix == 97.0", cell(FRONTIER, "vvix") == "97.0", cell(FRONTIER, "vvix"))
    r.check("01-10 basis == SETTLE", cell(FRONTIER, "basis") == "SETTLE", cell(FRONTIER, "basis"))
    r.check("01-10 m1m2_adj_pct BLANK", cell(FRONTIER, "m1m2_adj_pct").strip() == "",
            repr(cell(FRONTIER, "m1m2_adj_pct")))
    r.check("01-10 regime computed", cell(FRONTIER, "regime") == "LOW_VOL", cell(FRONTIER, "regime"))

    print("\n--- 4. the two rows that must NOT be created ---")
    r.check("holiday orphan 01-07 absent", HOLIDAY not in got)
    r.check("unpublished 01-11 not invented", LIVE_ROW in got and len(got) == 7)

    print("\n--- 5. live TICK row survives the repair untouched ---")
    r.check("01-11 still basis=TICK", cell(LIVE_ROW, "basis") == "TICK", cell(LIVE_ROW, "basis"))

    print("\n--- 6. gapcheck now certifies the repaired ledger ---")
    rc2 = gc.main(["--ledger", str(work), "--quiet"])
    r.check("rc=0 after repair", rc2 == 0, f"rc={rc2}")

    print("\n--- 7. idempotent ---")
    hdr2, rows2 = backfill.load_existing()
    stats2 = backfill.backfill_spot_cboe(rows2, today=LIVE_ROW, hist=hist, failed=set())
    r.check("second run creates 0", stats2.get("created", 0) == 0,
            f"created={stats2.get('created', 0)}")

    shutil.rmtree(tmp, ignore_errors=True)
    print(f"\n{'ALL ' + str(r.n) + ' CHECKS PASSED' if r.ok else 'FAILED'}")
    return 0 if r.ok else 1


if __name__ == "__main__":
    sys.exit(main())
