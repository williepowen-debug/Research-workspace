#!/usr/bin/env python3
"""Offline regression: forward-calendar coverage (DOCKET L667 tooling rider, 2026-10-21).

An empty HIGH/MED forward window must exit 1 and leave ONE packet in the inbox
directory; a covered window exits 0 and writes nothing; an unreadable calendar or
an unparseable date is UNKNOWN (2), never a pass. The 9/30-10/09 shape (only a
LOW row ahead) is the reproduction.
"""
import contextlib
import io
from datetime import date
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import forward_calendar_check as fc

HEADER = "date\tevent\ttype\tagent_domain\texpected_vol_impact\tsource\tnotes\n"


class ForwardCalendarTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name)
        self.cal = self.dir / "CATALYSTS.tsv"
        self.inbox = self.dir / "inbox"

    def run_check(self, *extra):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = fc.main(["--as-of", "2026-09-30", "--catalysts-file", str(self.cal),
                          "--inbox-dir", str(self.inbox), *extra])
        return rc, buf.getvalue()

    def test_covered_window_passes_and_writes_nothing(self):
        self.cal.write_text(HEADER + "2026-10-14\tCPI\tDATA\tVIOLET\tHIGH\ts\tn\n")
        rc, out = self.run_check()
        self.assertEqual(rc, 0, out)
        self.assertFalse(self.inbox.exists())

    def test_low_only_window_is_empty_forward_and_packets_once(self):
        # the 9/30 shape: an Oct 7 LOW checkpoint, the next HIGH outside 14 days
        self.cal.write_text(HEADER + "2026-10-07\tcheckpoint\tCHECKPOINT\tVIOLET\tLOW\ts\tn\n"
                                     "2026-10-28\tFOMC\tFOMC\tVIOLET\tHIGH\ts\tn\n")
        rc, out = self.run_check()
        self.assertEqual(rc, 1, out)
        pkts = list(self.inbox.glob("2026-09-30_from-VIOLET_EMPTY-FORWARD-calendar.md"))
        self.assertEqual(len(pkts), 1)
        self.assertIn("ACTION (PROME)", pkts[0].read_text())
        rc2, out2 = self.run_check()
        self.assertEqual(rc2, 1)
        self.assertIn("already present", out2)
        self.assertEqual(len(list(self.inbox.iterdir())), 1)

    def test_row_dated_today_is_due_not_forward(self):
        self.cal.write_text(HEADER + "2026-09-30\tMU\tEARNINGS\tVIOLET\tMEDIUM\ts\tn\n")
        rc, _ = self.run_check("--no-packet")
        self.assertEqual(rc, 1)
        self.assertFalse(self.inbox.exists())

    def test_missing_calendar_and_bad_date_are_unknown(self):
        rc, _ = self.run_check()
        self.assertEqual(rc, 2)
        self.cal.write_text(HEADER + "Oct 14\tCPI\tDATA\tVIOLET\tHIGH\ts\tn\n")
        rc, out = self.run_check()
        self.assertEqual(rc, 2, out)


if __name__ == "__main__":
    unittest.main()
