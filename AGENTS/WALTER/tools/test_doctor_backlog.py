#!/usr/bin/env python3
"""Reproduction tests for the 2026-09-11 backlog-classifier defects (Codex-found).

Run: .venv/bin/python3 AGENTS/WALTER/tools/test_doctor_backlog.py   (exit 0 = pass)

⚠️ SCOPE, STATED SO A GREEN RUN IS NOT OVER-READ: these exercise `_handoff_role`, the
CLASSIFIER. The bucket routing that consumes it lives inside
`check_delivered_but_unconsumed` and walks the real filesystem; case 1 below asserts the
classification that the routing keys on, not the routing itself.
`[[finding_verification_zero_is_ambiguous]]`
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import walter_doctor as w

FAILS = []


def check(name, got, want):
    ok = got == want
    print(f"  {'PASS' if ok else 'FAIL'}  {name}: got {got!r}, want {want!r}")
    if not ok:
        FAILS.append(name)


roles = w._delivery_roles()
print("Reproductions of the defects fixed 2026-09-11:\n")

# 1. THE v0.26 HOLE. Before SPEC §3.5.8(a), WALTER wrote no handoff to a PULL_COMPLETE
#    desk, so the classifier sorted by DESK and called every such file archive residue.
#    v0.26 delivers ACTION asks to CARL/RED — an unanswered one must NOT be archive-class.
check("aged ACTION handoff to CARL (pull-complete) classifies ACTION",
      w._handoff_role("SIG-W-20260911-006", "CARL", "SIG-W-20260911-006.md", roles), "ACTION")

# 2. Unchanged behaviour: an INFO handoff to the same exempt desk is still archive-class.
check("INFO/note handoff to CARL stays INFO",
      w._handoff_role("2026-09-11-NOTE-x", "CARL", "2026-09-11-NOTE-cc-debt-chart-unsourced.md",
                      roles), "INFO")

# 3. NON-DISPATCH scope. `_bare_sig` returns the FULL STEM when no signal id is present,
#    so a truthiness guard never fires — the pattern must be tested. The DEWEY batch-2
#    queue manifest (54d) is owned by `deep_research_pending_overdue`, not this check;
#    counting it here pinned "oldest ACTION" to a file that is not a dispatch.
check("queue manifest is NON-DISPATCH, not ACTION",
      w._handoff_role(w._bare_sig("2026-07-02_BATCH-2_MANIFEST"), "DEWEY",
                      "2026-07-02_BATCH-2_MANIFEST.md", roles), "NON-DISPATCH")

# 4. FAIL-CLOSED. A real signal id with no delivery_log row and no BOARD row must come
#    back UNKNOWN (the caller counts UNKNOWN as ACTION), never INFO.
check("unresolvable SIG-shaped id fails closed to UNKNOWN",
      w._handoff_role("SIG-W-19990101-999", "ZHAO", "SIG-W-19990101-999.md", roles), "UNKNOWN")

# 5. A normal non-exempt ACTION recipient is unaffected by any of the above.
check("ACTION handoff to a normal desk still classifies ACTION",
      w._handoff_role("SIG-W-20260911-005", "REGINALD", "SIG-W-20260911-005.md", roles), "ACTION")


# ── Timestamp validation (Codex fixtures, 2026-09-11) ────────────────────────────────
# v1 of check_future_timestamps SEARCHED each field for a valid-looking substring with
# re.finditer, so a field matching nothing produced no finding and the check reported
# INFO "clean". Three of these four passed as clean before the repair.
import re as _re
_CANON = _re.compile(r"^(\d{4}-\d{2}-\d{2})T(\d{2}):(\d{2})(?::(\d{2}))?Z$")
_APPROX = _re.compile(r"^\d{4}-\d{2}-\d{2}T[\dx]{2}:[\dx]{2}(?::[\dx]{2})?Z$", _re.I)


def _classify(v):
    if not (v or "").strip():
        return "EMPTY"
    if _CANON.match(v):
        return "CANONICAL"
    if _APPROX.match(v) and "x" in v.lower().split("T", 1)[-1]:
        return "APPROX"
    return "FLAGGED"


print("\nTimestamp field validation (whole field, fail-closed):")
check("junk text is FLAGGED, not silently clean", _classify("NOT-A-TIMESTAMP"), "FLAGGED")
check("empty field is EMPTY, not skipped", _classify(""), "EMPTY")
check("non-canonical offset is FLAGGED (schema is ...Z)",
      _classify("2099-01-01T00:00:00+00:00"), "FLAGGED")
check("canonical future stamp parses (date test then catches it)",
      _classify("2099-01-01T00:00:00Z"), "CANONICAL")
# The approximate-minute convention must be RECOGNISED, not flagged as malformed — and
# the class must REQUIRE a literal x: `[\dx]` also matches digits, and a permissive
# version swallowed all 2,784 canonical stamps into the "convention" bucket.
check("approximate-minute convention is its own class", _classify("2026-08-15T02:3xZ"), "APPROX")
check("an ordinary canonical stamp is NOT mistaken for the convention",
      _classify("2026-09-11T22:05:00Z"), "CANONICAL")

print()
if FAILS:
    print(f"✗ {len(FAILS)} FAILED: {', '.join(FAILS)}")
    sys.exit(1)
print(f"✓ all 11 reproductions pass")
