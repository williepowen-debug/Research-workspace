"""NOTE rows drop to INFO only when every (note_id, recipient) is classified; anything else stays MED."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import walter_doctor as doctor

DELIV = ("timestamp_routed\tsignal_id\trecipient\trole\trecipient_platform\tprecedence\thandoff_path\twritten_state\tnotes\n"
         "2026-09-14T17:55:42Z\tNOTE-2026-09-14-three-inflation-numbers\tRED\tinfo\tCC\tROUTINE\tx\tdelivered\tnote\n"
         "2026-09-14T17:55:42Z\tNOTE-2026-09-14-three-inflation-numbers\tCARL\tinfo\tCC\tROUTINE\tx\tdelivered\tnote\n")
HDR = "# c\nnote_id\trecipient\trole\tclassification\treview_date\tbasis\n"


def note_findings(ledger):
    with tempfile.TemporaryDirectory() as t:
        w = Path(t) / "WALTER"; b = Path(t) / "BOARD"
        (w / "routed").mkdir(parents=True); (w / "registry").mkdir(); b.mkdir()
        (w / "routed/delivery_log.tsv").write_text(DELIV)
        (w / "routed/route_log.tsv").write_text("Date\tSignal_ID\n")
        if ledger is not None:
            (w / "registry/NOTE_ROWS_REVIEWED.tsv").write_text(ledger)
        with patch.object(doctor, "WALTER", w), patch.object(doctor, "BOARD", b):
            return [(sev, msg) for sev, msg in doctor.check_log_reconcile() if "NOTE row" in msg]


class NoteRowReviewTests(unittest.TestCase):
    def test_all_reviewed_is_info(self):
        f = note_findings(HDR + "NOTE-2026-09-14-three-inflation-numbers\tRED\tinfo\tNOTE-CORRECT\t2026-10-23\tb\n"
                                "NOTE-2026-09-14-three-inflation-numbers\tCARL\tinfo\tNOTE-CORRECT\t2026-10-23\tb\n")
        self.assertEqual([s for s, _ in f], [doctor.INFO])

    def test_one_unreviewed_recipient_stays_med_and_names_it(self):
        f = note_findings(HDR + "NOTE-2026-09-14-three-inflation-numbers\tRED\tinfo\tNOTE-CORRECT\t2026-10-23\tb\n")
        self.assertEqual([s for s, _ in f], [doctor.MED])
        self.assertIn("→CARL", f[0][1])

    def test_missing_ledger_stays_med(self):
        f = note_findings(None)
        self.assertEqual([s for s, _ in f], [doctor.MED])
        self.assertIn("missing or unreadable", f[0][1])

    def test_blank_classification_does_not_count(self):
        f = note_findings(HDR + "NOTE-2026-09-14-three-inflation-numbers\tRED\tinfo\t\t2026-10-23\tb\n"
                                "NOTE-2026-09-14-three-inflation-numbers\tCARL\tinfo\tNOTE-CORRECT\t2026-10-23\tb\n")
        self.assertEqual([s for s, _ in f], [doctor.MED])


if __name__ == "__main__":
    unittest.main()
