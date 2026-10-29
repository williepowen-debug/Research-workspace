#!/usr/bin/env python3
"""
TEMPHELPS flag regression tests — labor_data.py assess() (BD-38, 2026-10-28).

Run:  .venv/bin/python3 AGENTS/LABOR/scripts/tests/test_temphelps_flag.py
Exit: 0 all pass, 1 any fail.

The flag used to be 🔴 on ANY monthly decline. The registered letters are
v14 `−20K ×2` and v16 `−6% YoY`; these cases pin the flag to those letters,
including the exact −20.0K and −6.0% boundaries and the real Sep-2026 print.
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import labor_data as L

FAILED = []


def series(latest3, base=2500.0):
    """Newest-first: three given values, then nine at `base`, then a 12-mo-ago `base`."""
    vals = list(latest3) + [base] * 10
    return [(f"obs{i}", v) for i, v in enumerate(vals)]


def check(name, obs, want):
    _, got = L.assess("TEMPHELPS", "level_mom", obs)
    ok = got == want
    print(f"{'PASS' if ok else 'FAIL'}  {name}: got {got!r} want {want!r}")
    if not ok:
        FAILED.append(name)


# Real Sep 2026 print: 2,486.8 vs Aug 2,497.7 (−10.9K), YoY base 2,471.6 => +0.6%.
real = [("s", 2486.8), ("a", 2497.7), ("j", 2500.0)] + [("x", 2480.0)] * 9 + [("y", 2471.6)]
check("Sep-2026 real print (−10.9K, +0.6% YoY) is not red", real, "🟢")
check("small decline is green", series([2495.0, 2500.0, 2500.0]), "🟢")
check("exactly −20.0K latest only = leg 1 of 2", series([2480.0, 2500.0, 2500.0]), "🟠")
check("−19.9K latest only = no leg", series([2480.1, 2500.0, 2500.0]), "🟢")
check("−20.0K twice = v14 met", series([2460.0, 2480.0, 2500.0]), "🔴")
check("−25K then −19.9K (older) = leg 1 only", series([2455.1, 2480.1, 2500.0]), "🟠")
check("older −20K, latest −10K = no leg (run must start at latest)", series([2470.0, 2480.0, 2500.0]), "🟢")
# YoY: base 2,500.0; −6.0% exactly = 2,350.0
yo = lambda v: [("a", v), ("b", v), ("c", v)] + [("x", v)] * 9 + [("y", 2500.0)]
check("YoY exactly −6.0% = v16 met", yo(2350.0), "🔴")
check("YoY −5.996% = not met", yo(2350.1), "🟢")
check("short history = cannot verify", series([2480.0, 2500.0, 2500.0])[:12], "⚠️")

print(f"\n{len(FAILED)} failure(s)")
sys.exit(1 if FAILED else 0)
