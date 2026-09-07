#!/usr/bin/env python3
"""
LABOR regression tests — predictions_due.parse_timeframe().

Run:  .venv/bin/python3 AGENTS/LABOR/scripts/tests/test_prediction_deadlines.py

WHY THIS FILE EXISTS
--------------------
LAB-18 and LAB-19 register as "Sep-Nov 2026 obs (prints Oct 2 / Nov 6 / Dec 4)".
The month-range branch read only the OBSERVATION label and returned 2026-11-30 --
four days BEFORE the final registered release. Simulating Dec 1 printed
"OVERDUE -- resolve this session" for two rows that could not yet be resolved.

The unparsed bucket cannot catch this: the string parses FINE, just to the wrong
object. Confusing an observation month with a publication date is the same class
as grading a revisable series without naming its vintage (WQ-175 clause 2).
Found by CODEX, 2026-09-07.
"""
import sys, pathlib
from datetime import date

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import predictions_due as P

CASES = [
    # (timeframe, expected due-by, note)
    ("Sep-Nov 2026 obs (prints Oct 2 / Nov 6 / Dec 4)", date(2026, 12, 4),
     "LAB-18/LAB-19 - the reported defect: last RELEASE, not last obs month"),
    ("Nov-Dec 2026 obs (prints Dec 4 / Jan 8)", date(2027, 1, 8),
     "year rollover - a print month before the obs window is NEXT year"),
    ("Sep 2026 obs resolve-by 2026-12-04", date(2026, 12, 4),
     "explicit resolve-by overrides every label heuristic"),
    # --- year handling: an EXPLICIT release year must never be inferred over ----
    # Regression introduced 2026-09-07 by the publication-clause parser itself and
    # caught by CODEX: it read month/day and discarded a year the row stated.
    ("Dec 2026 obs (prints Jan 8 2027)", date(2027, 1, 8),
     "explicit release year wins over inference"),
    ("Q4 2026 (prints Jan 8 2027)", date(2027, 1, 8),
     "explicit release year, quarter label"),
    ("Dec 2026 obs (prints Jan 8)", date(2027, 1, 8),
     "single-month window still rolls over - obs_start must not need a dash"),
    ("Sep-Nov 2026 obs (prints Oct 2 / Nov 6 / Dec 4 2026)", date(2026, 12, 4),
     "mixed: explicit year on the last release, inferred on the rest"),
    # --- rows that must NOT move -------------------------------------------
    ("Q2-Q3 2026", date(2026, 9, 30), "LAB-03 unchanged"),
    ("Q3-Q4 2026", date(2026, 12, 31), "LAB-11 / LAB-12 unchanged"),
    ("Q1-2027", date(2027, 3, 31), "LAB-08 unchanged"),
    ("Through 2026", date(2026, 12, 31), "ongoing unchanged"),
    ("Jun 6 2026", date(2026, 6, 6), "exact date unchanged"),
]

failed = 0
for tf, want, note in CASES:
    got, basis = P.parse_timeframe(tf)
    ok = got == want
    failed += not ok
    print(f"  [{'pass' if ok else 'FAIL'}] {note}")
    if not ok:
        print(f"         {tf!r} -> {got} ({basis}), want {want}")

# The live ledger must never flag a row overdue before its last registered release.
_header, rows = P.load_predictions()
open_rows = [r for r in rows if (r.get("Status") or "").strip().upper() == "OPEN"]
for r in open_rows:
    due, basis = P.parse_timeframe(r.get("Timeframe", ""))
    pid = (r.get("Pred_ID") or "").strip()
    if not pid:
        print("  [FAIL] a row has no Pred_ID — the per-row assertions below cannot bind")
        failed += 1
        continue
    if due is None:
        print(f"  [FAIL] {pid} unparseable: {basis}")
        failed += 1
    elif pid in ("LAB-18", "LAB-19") and due < date(2026, 12, 4):
        print(f"  [FAIL] {pid} due {due} precedes its final release 2026-12-04")
        failed += 1
    else:
        print(f"  [pass] live {pid} -> {due} ({basis})")

seen = {(r.get("Pred_ID") or "").strip() for r in open_rows}
for must in ("LAB-18", "LAB-19"):
    if must not in seen:
        print(f"  [FAIL] {must} not found among OPEN rows — the assertion guarding the "
              f"reported defect did not bind. A test that cannot reach its case is not a test.")
        failed += 1
    else:
        print(f"  [pass] {must} present, assertion bound")

print()
print(f"{failed} FAILED" if failed else "ALL PASS")
sys.exit(1 if failed else 0)
