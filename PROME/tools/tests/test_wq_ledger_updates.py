"""Decision corrections must survive sync and remain valid events."""
import contextlib
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import wq_ledger as w

class LedgerUpdateTests(unittest.TestCase):
    def test_long_ruling_preserves_tail_condition(self):
        record = "RULED 2026-09-11 — " + "supporting context " * 30 + "CONDITION: no execution"
        with tempfile.TemporaryDirectory() as td:
            q = Path(td) / "queue.md"
            q.write_text("")
            with patch.object(w.dd, "parse_decided", return_value=[dict(n="901", name="Decision", record=record, done="2026-09-11", source="fixture")]):
                state = w.live_state(q, [])
            self.assertTrue(state["901"]["record"].endswith("CONDITION: no execution"))

    def state(self):
        return dict(wq="901", status_after="RULED", verdict="APPROVE", at="2026-09-11",
                    title="Decision", record="Approved subject to A", will_verbatim="yes",
                    type="", needed_by="", since="", rec="", source="fixture")

    def test_content_correction_is_recorded(self):
        prior = self.state()
        for key in ("record", "title", "rec", "type", "since"):
            with self.subTest(key=key):
                self.assertEqual(w.diff_state(prior, dict(prior, **{key: "corrected"})), "UPDATED")

    def test_same_day_updates_are_valid_and_retry_is_idempotent(self):
        with tempfile.TemporaryDirectory() as td, patch.object(w, "now_stamp", return_value="2026-09-11 14:00"), contextlib.redirect_stdout(io.StringIO()):
            ledger = Path(td) / "ledger.tsv"
            state = self.state()
            w.append(ledger, [w.event_row("BACKFILL", state)])
            for word in ("yes condition B", "yes condition C"):
                state = dict(state, will_verbatim=word)
                with patch.object(w, "live_state", return_value={"901": state}):
                    self.assertEqual(w.cmd_sync(ledger), 0)
                    n = len(w.read_rows(ledger))
                    self.assertEqual(w.cmd_sync(ledger), 0)
                    self.assertEqual(len(w.read_rows(ledger)), n)
            self.assertEqual(len(w.read_rows(ledger)), 3)
            self.assertEqual(w.cmd_check(ledger), 0)

    def test_truncated_sealed_ledger_is_not_new(self):
        with tempfile.TemporaryDirectory() as td:
            ledger = Path(td) / "ledger.tsv"
            w.append(ledger, [w.event_row("BACKFILL", self.state())])
            ledger.write_text("")
            self.assertFalse(w.seal_ok(ledger))

if __name__ == "__main__":
    unittest.main()
