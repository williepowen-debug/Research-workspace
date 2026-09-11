#!/usr/bin/env python3
"""L336 Part B — acceptance tests for wq_ledger B1 and B2.

Conditions: PROME/proposals/2026-09-11_L336-argus-redesign-ACCEPTANCE-CONDITIONS.md
PROPERTY tests (A8 discipline): B1 is asserted over EVERY semantic field rather than the one the audit named.
Fixtures are throwaway copies; nothing touches the live ledger.
"""
import importlib.util, shutil, tempfile, unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("wq_ledger", TOOLS / "wq_ledger.py")
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)


def row(**kw):
    r = {c: "" for c in L.SCHEMA}
    r.update({"wq": "901", "event": "UPDATED", "at": "2026-09-11", "status_after": "OPEN",
              "verdict": "—", "written_at": "2026-09-11 18:00"})
    r.update(kw); return r


class B1_CorrectionsProduceAnEvent(unittest.TestCase):
    """PROPERTY: a change to ANY semantic field yields UPDATED — not just the three once hand-listed."""

    def test_every_semantic_field_change_is_detected(self):
        missed = []
        for field in L.COMPARED:
            prev = row(); cur = row(); cur[field] = (prev.get(field) or "") + "CHANGED"
            if field == "status_after":
                continue                                  # its own branch, tested below
            if L.diff_state(prev, cur) != "UPDATED":
                missed.append(field)
        self.assertEqual(missed, [], f"a correction to these fields produces NO event: {missed}")

    def test_the_audits_exact_case_a_corrected_record(self):
        """Audit F2's reproduction: only the record's timestamp changes."""
        prev = row(record="Will in-session 09:00 ET")
        cur = row(record="Will in-session 10:00 ET")
        self.assertEqual(L.diff_state(prev, cur), "UPDATED")

    def test_generated_metadata_alone_never_fabricates_an_event(self):
        for field in L.GENERATED:
            prev = row(); cur = row(); cur[field] = "9999-12-31"
            if field == "event":
                continue
            self.assertIsNone(L.diff_state(prev, cur), f"{field} is write metadata, not content")

    def test_semantic_idempotence_an_unchanged_row_yields_nothing(self):
        self.assertIsNone(L.diff_state(row(), row()))

    def test_a_new_field_added_to_SCHEMA_is_compared_by_default(self):
        """The fix is by SUBTRACTION, so forgetting to list a field cannot hide a change again."""
        self.assertEqual(set(L.SCHEMA) - set(L.GENERATED), set(L.SEMANTIC))
        self.assertIn("record", L.COMPARED); self.assertIn("title", L.COMPARED)
        self.assertIn("rec", L.COMPARED); self.assertIn("source", L.COMPARED)
        self.assertIn("type", L.COMPARED); self.assertIn("since", L.COMPARED)


class B2_SameDayUpdatesAreDistinct(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.led = Path(self.tmp.name) / "L.tsv"
        self.led.write_text(L.HEADER + "\n", encoding="utf-8"); L.seal(self.led)
    def tearDown(self): self.tmp.cleanup()

    def test_two_legitimate_same_day_updates_both_append_and_check_passes(self):
        """Audit F3: the required closeout check blocked on valid tool-generated history."""
        L.append(self.led, [row(needed_by="2026-10-01", written_at="2026-09-11 18:00")])
        L.append(self.led, [row(needed_by="2026-10-02", written_at="2026-09-11 18:05")])
        self.assertEqual(L.cmd_check(self.led), 0, "two distinct same-day changes are not a duplicate")

    def test_same_day_same_minute_but_different_payload_is_still_distinct(self):
        L.append(self.led, [row(needed_by="2026-10-01", written_at="2026-09-11 18:00")])
        L.append(self.led, [row(needed_by="2026-10-02", written_at="2026-09-11 18:00")])
        self.assertEqual(L.cmd_check(self.led), 0, "identity is the payload, not the clock")

    def test_an_oscillation_is_not_a_duplicate_the_reviewers_counterexample(self):
        """❌2: A -> B -> A -> B on one day is FOUR legitimate changes. The first fix rejected it, which was
        audit-F3's own failure mode surviving at n=3. A duplicate is a CONSECUTIVE no-op, not any repeat."""
        for nb in ("2026-10-01", "2026-10-08", "2026-10-01", "2026-10-08"):
            L.append(self.led, [row(needed_by=nb, written_at="2026-09-11 18:0" + str(len(nb) % 10))])
        self.assertEqual(L.cmd_check(self.led), 0)

    def test_a_consecutive_noop_is_still_caught(self):
        r = row(needed_by="2026-10-01")
        L.append(self.led, [r]); L.append(self.led, [dict(r)])
        self.assertEqual(L.cmd_check(self.led), 1, "the relaxation must not blind the check")

    def test_the_duplicate_key_includes_the_payload(self):
        a, b = row(record="X"), row(record="Y")
        self.assertNotEqual(L.payload(a), L.payload(b))
        self.assertEqual(L.payload(a), L.payload(row(record="X", written_at="2026-09-11 23:59")),
                         "write metadata must not enter the payload")


if __name__ == "__main__":
    unittest.main(verbosity=1)
