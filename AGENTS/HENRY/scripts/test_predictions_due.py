"""Due-scan integration with prediction ledger schemas; no market-data calls."""
import contextlib
import importlib.util
import io
from datetime import date
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("henry_boot_review", Path(__file__).with_name("boot.py"))
boot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(boot)

class PredictionSchemaTests(unittest.TestCase):
    def read(self, text):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "predictions.tsv"
            p.write_text(text)
            with patch.object(boot, "PREDICTIONS_TSV", p):
                return boot._read_rows()

    def test_seven_column_ledger_keeps_due_and_upcoming(self):
        rows = self.read("ID\tPrediction\tDate_Made\tConfidence\tStatus\tResolution_Date\tOutcome_Notes\n"
                         "HEN-44\tCPI\t2026-09-02\tUNSCORED-AS-MADE\tACTIVE\t2026-09-11\tFrozen\n"
                         "HEN-45\tFOMC\t2026-09-02\tUNSCORED-AS-MADE\tACTIVE\t2026-09-17\tFrozen\n")
        due, upcoming, _, _ = boot._classify(rows, date(2026, 9, 11))
        self.assertEqual([r[0] for r in due], ["HEN-44"])
        self.assertEqual([r[0] for r in upcoming], ["HEN-45"])

    def test_legacy_named_columns(self):
        rows = self.read("ID\tPrediction\tStatus\tResolution_Date\tOutcome_Notes\n"
                         "HEN-44\tCPI\tACTIVE\t2026-09-11\tFrozen\n")
        self.assertEqual(rows, [("HEN-44", "ACTIVE", "2026-09-11")])

    def test_unknown_schema_cannot_print_clean(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "predictions.tsv"
            p.write_text("ID\tUnknown\nHEN-44\tACTIVE\n")
            out = io.StringIO()
            with patch.object(boot, "PREDICTIONS_TSV", p), contextlib.redirect_stdout(out):
                boot.predictions_due(date(2026, 9, 11))
            self.assertIn("UNKNOWN", out.getvalue())
            self.assertNotIn("none overdue", out.getvalue())

if __name__ == "__main__":
    unittest.main()
