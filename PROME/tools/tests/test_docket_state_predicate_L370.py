#!/usr/bin/env python3
"""L370 ⊕ L450 — the DOCKET state predicate in prome_gate.py must read through the canonical
reader (scripts/docket_view.py:state_kind), never an exact-match test. Fixture-free: it imports
the predicate and the reader and compares them on the neighbour cases named in
ACCEPTANCE_docket_state_predicate_L370_2026-10-29.md. Run from the repo root:
    python3 PROME/tools/tests/test_docket_state_predicate_L370.py
"""
import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "PROME/tools"))
sys.path.insert(0, str(ROOT / "scripts"))

gate = importlib.import_module("prome_gate")
dv = importlib.import_module("docket_view")

CASES = {
    # cell → expected inspected?
    "PENDING": True,                                                   # AC1 ordinary
    "PENDING — registered 2026-10-22 11:3x ET (PROME)": True,          # AC1 em-dash annotation
    "PENDING · RE-DATED 2026-10-29 → 2026-11-05 (ESTIMATE)": True,    # AC1 middot annotation
    "PENDING(OVERDUE-annotated 2026-09-23 by prome-7a)": True,        # overlap: legacy paren form
    "PENDING: COVERED HANS": True,                                     # AC1 colon
    "  pending — lower case after strip  ": True,                      # AC2 case/strip parity
    "★ CORAL thesis re-test CONVERGENCE": True,                        # AC2 star lead
    "RE-DATED 2026-10-05→2026-10-09 by PROME": True,                   # AC2 re-dated lead
    "SLID to 2026-11-03": True,                                        # AC2 slid lead
    "RESOLVED 2026-10-29 (was PENDING since 10/22)": False,            # AC3 buried token
    "⛔ DATE CONTESTED — still PENDING at the owner": False,            # AC3 prefixed narrative
    "TOMBSTONE 2026-10-28 (WQ-530 A)": False,                          # terminal
    "": False,                                                         # missing information (schema check owns it)
}


def main() -> int:
    fails = []
    for cell, expected in CASES.items():
        got = gate._docket_pending(cell)
        canon = dv.state_kind(cell) == "PENDING"
        if got != expected:
            fails.append(f"predicate: {cell!r} → {got}, expected {expected}")
        if got != canon:
            fails.append(f"parity: {cell!r} → predicate {got}, canonical reader {canon}")
    # AC4: the inline fallback must agree with the canonical reader on every case
    for cell, expected in CASES.items():
        fb = gate._docket_pending_fallback(cell)
        if fb != expected:
            fails.append(f"fallback: {cell!r} → {fb}, expected {expected}")
    # the old exact-match test must NOT be what the predicate does (the defect itself)
    if gate._docket_pending("PENDING — registered") is False:
        fails.append("predicate still behaves like the exact-match test")
    # The dated-OVERDUE annotation cases (❌1, reader 2026-10-29) retired 2026-10-31 with the check they tested —
    # DOCKET overdue-unannotated (WQ-578 batch 2, #17); the predicate cases above still bind check_docket_today.
    if fails:
        print("❌ L370 predicate test: " + str(len(fails)) + " failure(s)")
        for f in fails:
            print("   - " + f)
        return 1
    print(f"✅ L370 predicate test: {len(CASES)} cases × predicate/parity/fallback agree with the canonical reader")
    return 0


if __name__ == "__main__":
    sys.exit(main())
