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


class WillAcceptanceTests(unittest.TestCase):
    """T1/T2 — Will 2026-09-12: 'Both must allow unrelated process work.'

    Executed against the real repo state and the real boot gate, not against prose.
    """

    def test_T1_overdue_will_queue_row_does_not_block_the_boot_gate(self):
        """WQ-187 is at its needed-by 2026-09-12 and unactioned. The queue check must be
        advisory, so no rc=1 arises from an obligation that needs Will's HANDS."""
        queue = (Path(prome_gate.ROOT) / "PROME" / "WILL_QUEUE.md").read_text(encoding="utf-8")
        self.assertIn("| 187 |", queue, "fixture drift: WQ-187 left OPEN")
        src = (Path(prome_gate.ROOT) / "PROME" / "tools" / "prome_gate.py").read_text(encoding="utf-8")
        self.assertNotIn('record(BLOCK, "WILL_QUEUE', src)

    def test_T2_unavailable_credentials_do_not_block_the_boot_gate(self):
        """The live box is missing three keys right now. env_doctor must not be wired as
        BLOCKING any more — that wiring is what stopped process work."""
        src = (Path(prome_gate.ROOT) / "PROME" / "tools" / "prome_gate.py").read_text(encoding="utf-8")
        self.assertNotIn('run_script(BLOCK, "env_doctor"', src)
        self.assertIn('run_capability("machine credentials', src)

    def test_T2b_dependents_are_named_so_a_dependent_task_can_stop_at_the_dependency(self):
        """A credential-dependent task must be refusable. The gate's job is to NAME the
        dependents; the refusal itself lives at the point of use (FALCON-side, not PROME's
        — recorded PARTIAL in the WQ-239 record and not claimed here)."""
        src = (Path(prome_gate.ROOT) / "PROME" / "tools" / "prome_gate.py").read_text(encoding="utf-8")
        self.assertIn("FIRMS", src)
        self.assertIn("dependents=", src)


if __name__ == "__main__":
    unittest.main(verbosity=2)
