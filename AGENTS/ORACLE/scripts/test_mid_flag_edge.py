#!/usr/bin/env python3
"""L546 float-tie edge test for kalshi.py fmt_row's wide-book ⚠mid marker.

DAEDALUS packet 2026-10-08 (DOCKET L546): `abs(yes - mid) >= 0.01` read
0.29-0.28 = 0.009999999999999981 as BELOW the edge, hiding the marker on exact
one-cent gaps. The letter is `>=`, so an exact one-cent gap must flag.

Needs the Kalshi cred dir present (kalshi.py loads its key at import).
Run: python3 AGENTS/ORACLE/scripts/test_mid_flag_edge.py   (exit 0 = all pass)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kalshi import fmt_row  # noqa: E402


def row(yes, mid, spread, status="active"):
    return {"yes": yes, "mid": mid, "spread": spread, "status": status,
            "thin": False, "days_left": None, "d_prev": None,
            "volume": 1000, "open_interest": 1000, "liquidity": None, "close": "2026-12-31"}


CASES = [
    # (label, yes, mid, spread, expect_flag)
    ("exact 1c gap 0.29 vs 0.28 (the float trap)", 0.29, 0.28, 0.04, True),
    ("exact 1c gap 0.57 vs 0.58", 0.57, 0.58, 0.04, True),
    ("half-cent gap 0.175 vs 0.17 (below edge)", 0.175, 0.17, 0.05, False),
    ("no gap", 0.40, 0.40, 0.04, False),
    ("spread exactly 3c is a usable book (0.31-0.28)", 0.31, 0.295, round(0.31 - 0.28, 10), True),
    ("spread 2c is too tight to flag", 0.30, 0.29, 0.02, False),
    ("finalized row never flags", 0.29, 0.28, 0.04, False, ),
]

fails = 0
for i, c in enumerate(CASES):
    label, yes, mid, sp, expect = c
    status = "finalized" if "finalized" in label else "active"
    # build the 3c spread from float subtraction too, so the _sp rounding is exercised
    if "exactly 3c" in label:
        sp = 0.31 - 0.28  # 0.030000000000000027 in binary float
    got = "⚠mid" in fmt_row("t", row(yes, mid, sp, status))
    ok = got == expect
    fails += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {label}: flag={got} expected={expect}")

print(f"{len(CASES) - fails}/{len(CASES)} pass")
sys.exit(1 if fails else 0)
