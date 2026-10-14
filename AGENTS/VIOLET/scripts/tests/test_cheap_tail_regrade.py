#!/usr/bin/env python3
"""Offline regression: stale source dates cannot write or request construction.

L667 ride-along: explicit dated regrades must preserve operator disposition;
missing calendar coverage must be visible without changing the four market lines.
"""
import contextlib
import csv
from datetime import date, timedelta
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import cheap_tail as ct
import backfill


class RegradeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "calendar.tsv"
        self.path.write_text("date\tevent\ttype\tagent\timpact\n2026-10-14\tCPI\tDATA\tVIOLET\tHIGH\n")
        self.data = dict(asof="2026-10-13", vix=15.27, vvix=85.38,
                         skew=154.74, vix_pctile=1, vvix_pctile=1,
                         skew_pctile=1, provisional=[], source="CBOE")

    def test_dated_calendar(self):
        self.assertEqual(ct.nearest_catalyst(date(2026, 10, 13), self.path), (1, "CPI"))
        self.assertEqual(ct.nearest_catalyst(date(2026, 10, 15), self.path), (None, "-"))

    def test_stale_new_row_withheld(self):
        path = Path(self.temp.name) / "log.tsv"
        data = {**self.data, "asof": "2000-01-01"}
        with patch.object(ct, "DAILY_LOG", path):
            self.assertIn("WITHHELD", ct.append_log(data, 1, "CPI", 4, "OPEN", "test"))
        self.assertFalse(path.exists())

    def test_explicit_regrade_preserves_disposition(self):
        path = Path(self.temp.name) / "log.tsv"
        with patch.object(ct, "DAILY_LOG", path):
            ct.append_log(self.data, 1, "CPI", 4, "OPEN", "DISPOSITION: PASSED WQ-418", regrade_date=date(2026, 10, 13))
            ct.append_log(self.data, 1, "CPI", 4, "OPEN", "regraded", regrade_date=date(2026, 10, 13))
        with path.open() as f:
            rows = list(csv.DictReader(f, delimiter="\t"))
        self.assertEqual(len(rows), 1)
        self.assertIn("DISPOSITION: PASSED WQ-418", rows[0]["note"])
        self.assertEqual(rows[0]["cat_days"], "1")

    def test_future_or_provisional_regrade_refused(self):
        future = date.today() + timedelta(days=2)
        with self.assertRaises(ValueError):
            ct.append_log({**self.data, "asof": str(future)}, 1, "CPI", 4, "OPEN", "", regrade_date=future)
        with self.assertRaises(ValueError):
            ct.append_log({**self.data, "provisional": ["skew"]}, 1, "CPI", 4, "OPEN", "", regrade_date=date(2026, 10, 13))

    def test_missing_bar_no_nearest_date(self):
        history = {str(date(2024, 1, 1) + timedelta(days=i)): 15.0 for i in range(501)}
        history.update({"2026-10-12": 15.0, "2026-10-14": 17.0})
        with patch.object(backfill, "fetch_cboe_history", return_value=(history, True)):
            with self.assertRaisesRegex(RuntimeError, "no complete CBOE observation"):
                ct.pull(date(2026, 10, 13))

    def test_historical_cboe_outage_no_mirror(self):
        with patch.object(backfill, "fetch_cboe_history", return_value=({}, False)):
            with self.assertRaisesRegex(RuntimeError, "requires CBOE"):
                ct.pull(date(2026, 10, 13))

    def test_empty_calendar_warns_and_stale_open_no_menu(self):
        self.path.write_text("date\tevent\ttype\tagent\timpact\n")
        output = io.StringIO()
        with patch.object(ct, "pull", return_value=self.data), patch.object(ct, "CATALYSTS", self.path), patch.object(sys, "argv", ["cheap_tail", "--no-log"]), contextlib.redirect_stdout(output):
            self.assertEqual(ct.main(), 0)
        self.assertIn("CALENDAR GAP", output.getvalue())
        self.assertIn("HISTORICAL ONLY", output.getvalue())
        self.assertNotIn("Vehicle discipline", output.getvalue())
        with patch.object(ct, "pull", return_value=self.data), patch.object(ct, "nearest_catalyst", return_value=(1, "CPI")), patch.object(sys, "argv", ["cheap_tail", "--no-log"]), contextlib.redirect_stdout(output):
            ct.main()
        self.assertNotIn("Vehicle discipline", output.getvalue())


if __name__ == "__main__":
    unittest.main()
