"""L546 float-tie test for base_rate_review.flag() (S51 2026-10-09, DAEDALUS packet 10/8).

Run: python3 AGENTS/RED/scripts/test_base_rate_flag.py  (from repo root, under .venv).
DONE-WHEN (DAEDALUS): an exact-on-edge case lands on the side the threshold's own letter says.
"""
import importlib.util
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location("brr", Path(__file__).with_name("base_rate_review.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

CASES = [
    (33 / 120 * 100 / 55.0, "🔴"),   # 0.5000000000000001: letter `<= 0.5` -> 🔴 (mis-flagged pre-fix)
    (2 / 120 * 100 / 2.5, "🟠"),     # 0.6666666666666667: letter `<= 1/1.5` -> 🟠 (mis-flagged pre-fix)
    (2.0, "🔴"), (1.5, "🟠"), (1.0, "🟢"),
    (0.6667, "🟢"), (0.50001, "🟠"), (1.49999, "🟢"), (None, "  "),
]
bad = [(r, want, m.flag(r)) for r, want in CASES if m.flag(r) != want]
if bad:
    print("FAIL", bad)
    sys.exit(1)
print(f"PASS {len(CASES)}/{len(CASES)}")
