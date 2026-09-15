#!/usr/bin/env python3
"""L336 Part B — acceptance tests for wq_ledger B1 and B2.

Conditions: PROME/proposals/2026-09-11_L336-argus-redesign-ACCEPTANCE-CONDITIONS.md
PROPERTY tests (A8 discipline): B1 is asserted over EVERY semantic field rather than the one the audit named.
Fixtures are throwaway copies; nothing touches the live ledger.
"""
import contextlib, importlib.util, io, json, shutil, tempfile, unittest
from pathlib import Path
from unittest.mock import patch

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


class L335_SourceCoverage(unittest.TestCase):
    """Exercise primary source -> sync -> persisted history, not projected dicts alone."""

    def setUp(self):
        self.stack = contextlib.ExitStack()
        self.addCleanup(self.stack.close)
        td = Path(self.stack.enter_context(tempfile.TemporaryDirectory()))
        self.q = td / "WILL_QUEUE.md"
        shutil.copyfile(L.FIXTURE / "WILL_QUEUE.md", self.q)
        self.led = td / "ledger.tsv"
        self.stack.enter_context(patch.object(L, "now_stamp", return_value="2026-09-14 23:00"))
        self.stack.enter_context(contextlib.redirect_stdout(io.StringIO()))

    def edit_cell(self, column, value):
        lines = self.q.read_text().splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| 901 |"):
                cells = L.dd.cells(line)
                cells[column] = value
                lines[i] = "| " + " | ".join(cells) + " |"
                break
        else:
            self.fail("fixture WQ-901 missing")
        self.q.write_text("\n".join(lines) + "\n")

    def backfill(self):
        self.assertEqual(L.cmd_backfill(self.led, self.q, []), 0)

    def sync(self):
        before = L.read_rows(self.led)
        self.assertEqual(L.cmd_sync(self.led, self.q, []), 0)
        after = L.read_rows(self.led)
        self.assertEqual(L.cmd_check(self.led), 0)
        return after[len(before):]

    def assert_single_update(self, events):
        self.assertEqual([(r["wq"], r["event"]) for r in events], [("901", "UPDATED")])

    def test_notes_only_edit_is_retained_without_duplicate(self):
        self.backfill()
        self.edit_cell(6, "Evidence corrected; this is not Will's ruling.")
        events = self.sync()
        self.assert_single_update(events)
        self.assertEqual(json.loads(events[0]["record"])["notes"],
                         "Evidence corrected; this is not Will's ruling.")
        self.assertEqual(events[0]["verdict"], "—")
        self.assertEqual(events[0]["will_verbatim"], "")
        self.assertEqual(self.sync(), [])

    def test_item_body_change_preserving_bold_title_is_retained(self):
        self.backfill()
        self.q.write_text(self.q.read_text().replace("Some body text.", "Corrected evidence basis."))
        events = self.sync()
        self.assert_single_update(events)
        self.assertIn("Corrected evidence basis.", json.loads(events[0]["record"])["item"])

    def test_long_tail_changes_in_item_notes_and_recommendation(self):
        for column, key in ((1, "item"), (5, "rec"), (6, "notes")):
            with self.subTest(key=key):
                prefix = "**Same title.** " + "evidence " * 200
                self.edit_cell(column, prefix + "FIRST")
                if not self.led.exists():
                    self.backfill()
                else:
                    self.sync()
                self.edit_cell(column, prefix + "SECOND")
                events = self.sync()
                self.assert_single_update(events)
                self.assertEqual(json.loads(events[0]["record"])[key], prefix + "SECOND")

    def test_raw_deadline_text_change_with_same_date_is_retained(self):
        self.edit_cell(3, "2026-09-30 before release")
        self.backfill()
        self.edit_cell(3, "2026-09-30 after release")
        events = self.sync()
        self.assert_single_update(events)
        self.assertEqual(events[0]["needed_by"], "2026-09-30")
        self.assertEqual(json.loads(events[0]["record"])["by_raw"], "2026-09-30 after release")

    def test_link_target_change_without_label_change(self):
        self.edit_cell(6, "[source](https://example.test/first)")
        self.backfill()
        self.edit_cell(6, "[source](https://example.test/second)")
        events = self.sync()
        self.assert_single_update(events)
        self.assertIn("https://example.test/second", json.loads(events[0]["record"])["notes"])

    def test_unicode_quotes_backslashes_and_tabs_round_trip(self):
        self.backfill()
        note = '訂正 "quoted" \\path\tinternal-tab'
        self.edit_cell(6, note)
        events = self.sync()
        self.assert_single_update(events)
        self.assertEqual(json.loads(events[0]["record"])["notes"], note)

    def test_notes_deletion_and_oscillation_are_distinct(self):
        self.backfill()
        for note in ("A", "B", "A", ""):
            self.edit_cell(6, note)
            self.assert_single_update(self.sync())
            self.assertEqual(self.sync(), [])

    def test_padding_and_nonrow_prose_do_not_create_events(self):
        self.backfill()
        text = self.q.read_text().replace("| 901 |", "|  901  |")
        self.q.write_text("Unrelated introduction.\n\n" + text)
        self.assertEqual(self.sync(), [])

    def test_missing_notes_and_empty_notes_are_equivalent(self):
        self.edit_cell(6, "")
        self.backfill()
        lines = self.q.read_text().splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| 901 |"):
                lines[i] = "| " + " | ".join(L.dd.cells(line)[:6]) + " |"
        self.q.write_text("\n".join(lines) + "\n")
        self.assertEqual(self.sync(), [])

    def test_legacy_upgrade_appends_only_then_is_idempotent(self):
        states = L.live_state(self.q, [])
        for state in states.values():
            if state["status_after"] not in L.TERMINAL:
                state["record"] = ""  # actual pre-L335 OPEN projection
        L.append(self.led, [L.event_row("BACKFILL", s) for s in states.values()])
        before = self.led.read_bytes()
        events = self.sync()
        self.assertEqual({r["wq"] for r in events}, {"901", "902"})
        self.assertTrue(all(r["event"] == "UPDATED" for r in events))
        self.assertTrue(self.led.read_bytes().startswith(before))
        self.assertEqual(self.sync(), [])

    def test_live_open_overrides_older_terminal_without_becoming_decided(self):
        self.q.write_text(self.q.read_text() + '\n| **901 Old decision** | 9/1 | **RULED — old** |\n')
        self.backfill()
        self.assertEqual(L.last_state(L.read_rows(self.led))["901"]["status_after"], "OPEN")
        self.assertNotIn("901", {r["n"] for r in L.dd.parse_ledger_decided(self.led)})

    def test_terminal_transition_keeps_ruling_record_not_open_snapshot(self):
        self.backfill()
        original_decided = L.dd.parse_ledger_decided(self.led)
        self.edit_cell(6, "ordinary correction")
        self.sync()
        self.assertEqual(L.dd.parse_ledger_decided(self.led), original_decided)
        lines = [line for line in self.q.read_text().splitlines() if not line.startswith("| 901 |")]
        lines.append('| **901 Fixture open row** | 9/14 | **RULED — Will APPROVE, verbatim *"yes"*** |')
        self.q.write_text("\n".join(lines) + "\n")
        events = self.sync()
        self.assertEqual(events[0]["event"], "RULED")
        self.assertTrue(events[0]["record"].startswith("RULED"))
        self.assertEqual(events[0]["will_verbatim"], "yes")

    def test_broken_seal_refuses_snapshot_rollout_without_resealing(self):
        self.backfill()
        self.led.write_text(self.led.read_text().replace("Fixture", "Tampered", 1))
        before, seal = self.led.read_bytes(), L.crc_path(self.led).read_bytes()
        self.edit_cell(6, "corrected")
        self.assertEqual(L.cmd_sync(self.led, self.q, []), 1)
        self.assertEqual(self.led.read_bytes(), before)
        self.assertEqual(L.crc_path(self.led).read_bytes(), seal)

    def test_large_notes_remain_readable_and_csv_limit_is_restored(self):
        self.backfill()
        note = "x" * 140_000
        self.edit_cell(6, note)
        old_limit = L.csv.field_size_limit()
        events = self.sync()
        self.assert_single_update(events)
        self.assertEqual(json.loads(events[0]["record"])["notes"], note)
        self.assertEqual(self.sync(), [])
        self.assertEqual(L.csv.field_size_limit(), old_limit)


if __name__ == "__main__":
    unittest.main(verbosity=1)
