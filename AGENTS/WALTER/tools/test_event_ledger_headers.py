"""Comment headers must survive batch writes and preserve overdue visibility."""
import csv
from datetime import timedelta
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import batch_manifest as batch
import walter_doctor as doctor


class EventHeaders(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.desk = Path(self.tmp.name)
        (self.desk / "registry").mkdir()

    def test_batch_headers_not_events_and_metadata_survives_next_write(self):
        path = self.desk / "registry/BATCH_MANIFEST.tsv"
        comments = "# Cadence: EVENT-DRIVEN\n# Last re-pull ATTEMPTED: 2026-10-12\n"
        header = "\t".join(batch.COLS) + "\n"
        fields = ["BM-20261012-01", "2026-10-12T00:00:00Z", "test", "1", "1",
                  "CLOSED", "1=NO-ACTION:test", "closed"]
        path.write_text(comments + header + header + "\t".join(fields) + "\n")
        with patch.object(batch, "LEDGER", path):
            rows = batch._read()
            self.assertEqual(len(rows), 1)
            batch._write(rows)
            self.assertEqual(batch._read(), rows)
        self.assertTrue(path.read_text().startswith(comments))

    def test_malformed_batch_is_still_refused(self):
        path = self.desk / "registry/BATCH_MANIFEST.tsv"
        path.write_text("# Cadence: EVENT-DRIVEN\n" + "\t".join(batch.COLS) + "\nBAD\n")
        with patch.object(batch, "LEDGER", path), self.assertRaises(SystemExit): batch._read()

    def test_deep_research_header_does_not_hide_overdue_request(self):
        path = self.desk / "registry/DEEP_RESEARCH_FLAGGED_LOG.tsv"
        header = ["flagged_date", "signal_id", "deadline", "disposition"]
        output = io.StringIO(); writer = csv.writer(output, delimiter="\t")
        writer.writerow(header)
        writer.writerow([str(doctor.TODAY - timedelta(days=10)), "REQ-TEST", str(doctor.TODAY - timedelta(days=1)), "QUEUED"])
        path.write_text("# Cadence: EVENT-DRIVEN\n# Last re-pull ATTEMPTED: 2026-10-12\n" + output.getvalue())
        with patch.object(doctor, "WALTER", self.desk):
            result = doctor.check_deep_research_pending_overdue()
        self.assertTrue(any(severity == doctor.MED and "REQ-TEST" in text for severity, text in result))


if __name__ == "__main__": unittest.main()
