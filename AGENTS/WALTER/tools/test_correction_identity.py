#!/usr/bin/env python3
"""Regression test — a CORRECTION must never be discharged by its ORIGINAL, or vice versa.

🔴 THE DEFECT (Codex finding 2, raised 2026-09-11, fixed 2026-09-14). Three coupled sites
made a correction and its original the SAME object:

  1. `_bare_sig("SIG-W-...-003-CORRECTION")` -> "SIG-W-...-003"  (by design, and correct
     for "which signal is this ABOUT" — wrong for "has THIS artifact been consumed").
  2. `_delivery_routed_dates` keys on (signal_id, recipient); delivery_log stores the BARE
     id for corrections too. Measured 2026-09-14: 0 of 2,800+ rows carry a -CORRECTION
     suffix, 33 (signal_id, recipient) keys appear twice, and ALL 33 pairs differ by
     handoff_path. Plain dict assignment => LAST row wins => one of every pair was aged
     off the other's timestamp.
  3. The consume cross-check was `sig in _recipient_board_log(recipient)` — a WHOLE-FILE
     SUBSTRING match on the bare id.

⚠️ Site 3 is the one that matters: a desk that consumed the ORIGINAL and never read the
CORRECTION had the correction marked CONSUMED. A correction going silent is the single
failure this desk exists to prevent.

⛔ FIXTURES ARE FROZEN, NOT READ FROM THE LIVE TREE.
`[[finding_regression_test_pinned_to_a_live_surface_rots_on_the_next_edit]]` — a test that
asserts against a live board_log certifies nothing past the next append.
"""
import pathlib, sys, importlib.util

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("wd", HERE / "walter_doctor.py")
wd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wd)

ORIG = "SIG-W-20260911-003"
CORR = "SIG-W-20260911-003-CORRECTION"

# --- frozen fixtures: three desks, three consumption states -------------------
FIXTURES = {
    "DESK_ORIG_ONLY": "timestamp_read\tsignal_id\tdisposition\tsource\tnotes\n"
                      "2026-09-12T13:00:00Z\tSIG-W-20260911-003.md\tacted\tINBOX_WALTER\t\n",
    "DESK_CORR_ONLY": "timestamp_read\tsignal_id\tdisposition\tsource\tnotes\n"
                      "2026-09-12T13:00:00Z\tSIG-W-20260911-003-CORRECTION.md\tacted\tINBOX_WALTER\t\n",
    "DESK_BOTH":      "timestamp_read\tsignal_id\tdisposition\tsource\tnotes\n"
                      "2026-09-12T13:00:00Z\tSIG-W-20260911-003.md\tacted\tINBOX_WALTER\t\n"
                      "2026-09-12T13:53:19Z\tSIG-W-20260911-003-CORRECTION.md\tacted\tINBOX_WALTER\t\n",
    "DESK_NEITHER":   "timestamp_read\tsignal_id\tdisposition\tsource\tnotes\n",
}
wd._BOARD_LOG_CACHE.update(FIXTURES)

fails = []
def check(label, got, want):
    ok = got == want
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: got {got}, want {want}")
    if not ok:
        fails.append(label)

print("=== _sig_variant splits identity from subject ===")
check("original -> no variant", wd._sig_variant(ORIG + "-some-slug"), (ORIG, ""))
check("correction -> CORRECTION", wd._sig_variant(CORR), (ORIG, "CORRECTION"))

print("\n=== DIRECTION 1 — consuming the ORIGINAL must NOT discharge the CORRECTION ===")
check("original reads consumed", wd._board_log_has("DESK_ORIG_ONLY", ORIG, ""), True)
check("CORRECTION reads NOT consumed", wd._board_log_has("DESK_ORIG_ONLY", ORIG, "CORRECTION"), False)

print("\n=== DIRECTION 2 — consuming the CORRECTION must NOT discharge the ORIGINAL ===")
check("correction reads consumed", wd._board_log_has("DESK_CORR_ONLY", ORIG, "CORRECTION"), True)
check("ORIGINAL reads NOT consumed", wd._board_log_has("DESK_CORR_ONLY", ORIG, ""), False)

print("\n=== control — both consumed, and neither consumed ===")
check("both: original", wd._board_log_has("DESK_BOTH", ORIG, ""), True)
check("both: correction", wd._board_log_has("DESK_BOTH", ORIG, "CORRECTION"), True)
check("neither: original", wd._board_log_has("DESK_NEITHER", ORIG, ""), False)
check("neither: correction", wd._board_log_has("DESK_NEITHER", ORIG, "CORRECTION"), False)

print("\n=== fail-closed: unknown desk / empty log is NEVER 'consumed' ===")
check("absent desk", wd._board_log_has("DESK_DOES_NOT_EXIST_XYZ", ORIG, ""), False)
check("empty sig", wd._board_log_has("DESK_BOTH", "", ""), False)

print()
if fails:
    print(f"FAILED {len(fails)}: {fails}")
    sys.exit(1)
print("ALL PASS — a correction and its original are distinct objects in both directions.")
