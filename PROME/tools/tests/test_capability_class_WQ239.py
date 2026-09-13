#!/usr/bin/env python3
"""WQ-239 — the CAPABILITY class: a missing machine capability must never gate work
that does not use it, must stay reported until restored, and must distinguish
UNKNOWN from UNAVAILABLE (Will 2026-09-12 20:49: "a crash, unreadable configuration,
or unrecognized result must report UNKNOWN").

ACCEPTANCE CONDITIONS these tests come from (written before the edit, WQ-229) —
 B1 unrelated work proceeds in EVERY state · B4 never gets quieter (reported until
 restored; no silencing path) · B5 a follow-up deadline drives escalation urgency
 ONLY · UNKNOWN preserved as a third state · AVAILABLE means PRESENT, not AUTHENTICATED.

Neighbour categories (PROME/tools/tests/README.md): ordinary ✓ · overlap ✓ (tracker
row present AND capability healthy) · wrong owner ✓ (tracker id that names no row) ·
missing information ✓ (this is the UNKNOWN block — the whole point) · concurrent
activity — N/A with reason: run_capability holds no shared state across processes;
it writes one log under a per-run LOG_DIR and returns a value.

Run: python3 -m unittest PROME.tools.tests.test_capability_class_WQ239   (from repo root)
  or python3 PROME/tools/tests/test_capability_class_WQ239.py
"""
import datetime as dt
import sys
import subprocess
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import prome_gate  # noqa: E402

PY = sys.executable


def probe(body):
    """A throwaway python probe with a chosen exit code / output."""
    return [PY, "-c", body]


class CapabilityStates(unittest.TestCase):
    def setUp(self):
        prome_gate.results.clear()
        prome_gate.capabilities.clear()
        prome_gate.LOG_DIR = Path(tempfile.mkdtemp(prefix="cap-test-"))

    def state(self, body, **kw):
        return prome_gate.run_capability("probe", probe(body), "owner.md", "dependent work", **kw)

    # ---------------------------------------------------------------- ordinary
    def test_rc0_is_available(self):
        self.assertEqual(self.state("raise SystemExit(0)"), prome_gate.CAP_AVAILABLE)

    def test_rc1_is_unavailable(self):
        self.assertEqual(self.state("print('X ✗ KEY missing'); raise SystemExit(1)"),
                         prome_gate.CAP_UNAVAILABLE)

    def test_available_is_labelled_presence_not_authentication(self):
        """Will 2026-09-12: 'Credential presence also does not prove authentication succeeds.'"""
        self.state("raise SystemExit(0)")
        detail = prome_gate.capabilities[0][2]
        self.assertIn("NOT authenticated", detail)

    def test_unavailable_detail_names_what_is_missing_not_that_a_check_ran(self):
        """Regression: the first implementation filtered with startswith('✗') while
        env_doctor prints 'ENV-DOCTOR ✗ KEY missing…', so it surfaced the perimeter
        summary — it reported that a check ran, not what it found."""
        self.state("print('TOOL perimeter — checked: a · b'); print('TOOL ✗ KEY_ONE missing');"
                   " raise SystemExit(1)")
        self.assertIn("KEY_ONE", prome_gate.capabilities[0][2])

    # ------------------------------------------------- missing information (4)
    def test_unrecognised_rc_is_unknown_not_unavailable(self):
        self.assertEqual(self.state("raise SystemExit(2)"), prome_gate.CAP_UNKNOWN)

    def test_crash_is_unknown(self):
        st = prome_gate.run_capability("probe", ["/nonexistent/binary/xyz"], "o.md", "d")
        self.assertEqual(st, prome_gate.CAP_UNKNOWN)

    def test_unknown_is_not_silently_read_as_available(self):
        for body in ("raise SystemExit(2)", "raise SystemExit(7)"):
            self.assertNotEqual(self.state(body), prome_gate.CAP_AVAILABLE)

    def test_unknown_says_it_established_nothing(self):
        self.state("raise SystemExit(3)")
        self.assertIn("established nothing", prome_gate.capabilities[0][2])

    # -------------------------------------------- B1: never gates unrelated work
    def test_no_capability_state_contributes_to_rc(self):
        """The core property. BLOCK's contract is 'disposition before proceeding' for ALL
        work; CAPABILITY has no such contract in any state."""
        for body in ("raise SystemExit(0)", "raise SystemExit(1)", "raise SystemExit(2)"):
            prome_gate.capabilities.clear()
            self.state(body)
            blocking = [r for r in prome_gate.results if r[0] == prome_gate.BLOCK and not r[2]]
            self.assertEqual(blocking, [], "a capability state reached the blocking bucket")

    def test_capability_never_enters_the_results_list_at_all(self):
        self.state("raise SystemExit(1)")
        self.assertEqual(prome_gate.results, [])
        self.assertEqual(len(prome_gate.capabilities), 1)

    # ------------------------------------ B4: reported until restored, no silencing
    def test_every_run_records_the_capability_regardless_of_state(self):
        for body in ("raise SystemExit(0)", "raise SystemExit(1)", "raise SystemExit(2)"):
            self.state(body)
        self.assertEqual(len(prome_gate.capabilities), 3)


class TrackerUrgency(unittest.TestCase):
    """B5 — a follow-up deadline drives ESCALATION URGENCY ONLY, never gating."""

    def test_overdue_tracker_reads_overdue(self):
        self.assertTrue(prome_gate._tracker_overdue("238", dt.date(2026, 9, 20)))

    def test_tracker_inside_its_date_is_not_urgent(self):
        self.assertFalse(prome_gate._tracker_overdue("238", dt.date(2026, 9, 18)))

    def test_wrong_owner_unknown_row_id_never_manufactures_urgency(self):
        self.assertFalse(prome_gate._tracker_overdue("999999", dt.date(2030, 1, 1)))

    def test_no_tracker_is_not_urgent(self):
        self.assertFalse(prome_gate._tracker_overdue(None, dt.date(2030, 1, 1)))

    def test_overlap_healthy_capability_with_a_tracker_row_is_not_urgent(self):
        """Overlap: the row exists AND the capability is fine. Urgency is rendered only
        for non-AVAILABLE states, so a stale tracker cannot shout about a working key."""
        prome_gate.capabilities.clear()
        prome_gate.LOG_DIR = Path(tempfile.mkdtemp(prefix="cap-test-"))
        st = prome_gate.run_capability("probe", probe("raise SystemExit(0)"), "o.md", "d",
                                       tracker="238")
        self.assertEqual(st, prome_gate.CAP_AVAILABLE)


class ProbeFailureVsConfirmedGap(unittest.TestCase):
    """Regressions for two failures reproduced by external review against 81e7da15e.

    Both exited rc=1 and were read as UNAVAILABLE. rc alone CANNOT distinguish
    'the probe confirmed a gap' from 'the probe could not evaluate' — an unreadable
    config and three missing keys are both rc=1 from env_doctor. The output decides.
    ⛔ The original crash test used a NONEXISTENT EXECUTABLE, which fails in the PARENT
    (subprocess.run raises) — it never exercised a child that starts and then dies."""

    def setUp(self):
        prome_gate.results.clear()
        prome_gate.capabilities.clear()
        prome_gate.LOG_DIR = Path(tempfile.mkdtemp(prefix="cap-test-"))

    def test_in_child_exception_is_unknown_not_unavailable(self):
        """REPORTED FAILURE 1: a Python child crashing with RuntimeError exits 1."""
        st = prome_gate.run_capability("p", probe("raise RuntimeError('boom')"), "o", "d")
        self.assertEqual(st, prome_gate.CAP_UNKNOWN)

    def test_real_env_doctor_with_unreadable_config_is_unknown(self):
        """REPORTED FAILURE 2: the ACTUAL probe against an unreadable target. Runs the
        real scripts/env_doctor.py; chmod is restored in finally, including on failure."""
        env = Path(prome_gate.ROOT) / "FORGE" / "tools" / "market-data" / ".env"
        if not env.exists():
            self.skipTest("no .env on this box")
        mode = env.stat().st_mode
        try:
            env.chmod(0o000)
            st = prome_gate.run_capability(
                "env", [PY, "scripts/env_doctor.py", "--quiet"], "o", "d")
        finally:
            env.chmod(mode)
        self.assertEqual(st, prome_gate.CAP_UNKNOWN)

    def test_nonzero_with_no_readable_finding_is_unknown(self):
        st = prome_gate.run_capability("p", probe("print('weird'); raise SystemExit(1)"), "o", "d")
        self.assertEqual(st, prome_gate.CAP_UNKNOWN)

    def test_nonzero_with_a_real_finding_is_still_unavailable(self):
        """The repair must not swing the other way and call every failure UNKNOWN."""
        st = prome_gate.run_capability(
            "p", probe("print('T ✗ FIRMS_MAP_KEY missing'); raise SystemExit(1)"), "o", "d")
        self.assertEqual(st, prome_gate.CAP_UNAVAILABLE)

    def test_overlap_findings_present_AND_a_traceback_is_unknown(self):
        """Overlap: the probe emitted a real finding and THEN crashed, so its verdict is
        partial. A partial verdict is not a verdict."""
        st = prome_gate.run_capability("p", probe(
            "print('T ✗ FIRMS_MAP_KEY missing'); raise RuntimeError('died after')"), "o", "d")
        self.assertEqual(st, prome_gate.CAP_UNKNOWN)


class DependentScoping(unittest.TestCase):
    """Reported limitation: any environment failure printed the union of every
    dependent workflow, including FRED/EIA when only FFIEC or NASA keys were missing."""

    def setUp(self):
        prome_gate.capabilities.clear()
        prome_gate.LOG_DIR = Path(tempfile.mkdtemp(prefix="cap-test-"))

    def dependents_for(self, line):
        prome_gate.run_capability("p", probe(f"print({line!r}); raise SystemExit(1)"),
                                  "o", "DECLARED-SUPERSET")
        return prome_gate.capabilities[-1][4]

    def test_only_the_named_keys_dependents_are_reported(self):
        dep = self.dependents_for("T ✗ FIRMS_MAP_KEY missing")
        self.assertIn("FIRMS", dep)
        self.assertNotIn("FRED", dep)
        self.assertNotIn("EIA", dep)

    def test_ffiec_gap_does_not_withhold_fred(self):
        dep = self.dependents_for("T ✗ FFIEC_CDR_TOKEN missing")
        self.assertIn("FFIEC", dep)
        self.assertNotIn("FRED", dep)

    def test_unrecognised_key_keeps_the_declared_superset(self):
        """Category 4: never silently narrow to nothing when the attribute is absent."""
        self.assertEqual(self.dependents_for("T ✗ SOMETHING_NEW missing"), "DECLARED-SUPERSET")


class AggregateGateBehaviour(unittest.TestCase):
    """T1/T2 executed through the gate's real rc function with isolated fixtures.

    ⛔ The previous versions of these tests asserted on SOURCE STRINGS — they established
    wiring, never behaviour (external review 2026-09-12)."""

    OK_BLOCK = (prome_gate.BLOCK, "some blocking check", True, "", "owner")
    BAD_BLOCK = (prome_gate.BLOCK, "some blocking check", False, "", "owner")

    def cap(self, state):
        return ("machine credentials", state, "d", "o", "deps", "238")

    def test_T1_overdue_tracker_plus_unavailable_capability_still_rc0(self):
        """Will's T1/T2: both must allow unrelated process work."""
        for state in (prome_gate.CAP_UNAVAILABLE, prome_gate.CAP_UNKNOWN,
                      prome_gate.CAP_AVAILABLE):
            self.assertEqual(
                prome_gate.aggregate_rc([self.OK_BLOCK], [self.cap(state)]), 0,
                f"capability state {state} reached rc")

    def test_T2_overdue_tracker_raises_urgency_not_rc(self):
        with tempfile.TemporaryDirectory() as d:
            q = Path(d) / "WILL_QUEUE.md"
            q.write_text("| 238 | item | ACTION | 2026-09-19 | 9/12 | rec | notes |\n",
                         encoding="utf-8")
            self.assertTrue(prome_gate._tracker_overdue("238", dt.date(2026, 9, 20), q))
            self.assertFalse(prome_gate._tracker_overdue("238", dt.date(2026, 9, 18), q))
        self.assertEqual(
            prome_gate.aggregate_rc([self.OK_BLOCK],
                                    [self.cap(prome_gate.CAP_UNAVAILABLE)]), 0)

    def test_the_rc_function_can_still_fail(self):
        """Control: a test that only ever sees 0 proves nothing."""
        self.assertEqual(prome_gate.aggregate_rc([self.BAD_BLOCK], []), 1)

    def test_end_to_end_boot_gate_passes_with_a_real_unavailable_capability(self):
        """The live box is missing keys right now: run the WHOLE gate as a subprocess."""
        p = subprocess.run([PY, "PROME/tools/prome_gate.py", "boot"],
                           cwd=prome_gate.ROOT, capture_output=True, text=True, timeout=300)
        self.assertIn("CAPABILITIES", p.stdout)
        self.assertRegex(p.stdout, r"\[(UNAVAILABLE|UNKNOWN|AVAILABLE)\s*\]")
        if "[UNAVAILABLE" in p.stdout or "[UNKNOWN" in p.stdout:
            self.assertEqual(p.returncode, 0,
                             "a non-AVAILABLE capability gated the whole boot gate")


if __name__ == "__main__":
    unittest.main(verbosity=2)
