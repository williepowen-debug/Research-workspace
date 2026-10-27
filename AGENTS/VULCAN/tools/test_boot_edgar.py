#!/usr/bin/env python3
"""Offline boot wiring checks; temporary ledger, no network or production writes."""
import csv
import importlib.util
import io
from contextlib import redirect_stdout
from datetime import date, timedelta
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import sys

DESK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(DESK / 'tools'))
import edgar_watch as EW
spec = importlib.util.spec_from_file_location('vulcan_boot', DESK / 'boot.py')
boot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(boot)


class FilingBoot(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.ledger = Path(self.tmp.name) / 'seen.tsv'
        self.today = date.today()

    def write(self, series):
        with self.ledger.open('w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=['tick', 'form', 'filed', 'report_date', 'items', 'first_seen_utc'], delimiter='\t')
            w.writeheader()
            for tick, lags in series.items():
                for i, lag in enumerate(lags):
                    end = date(2025, 3, 31) + timedelta(days=91*i)
                    w.writerow(dict(tick=tick, form='10-Q', filed=end+timedelta(days=lag), report_date=end, items='', first_seen_utc=self.today.isoformat()+'T12:00:00Z'))

    def sweep(self, series, projected=None):
        self.write(series)
        with patch.object(boot, 'EDGAR_SEEN', self.ledger), patch.object(EW, 'earnings_cadence', return_value=None), patch.object(EW, 'next_window', return_value=projected) as project:
            rc, msg = boot.edgar_sweep()
        return rc, msg, project

    def test_early_filing_failure_survives_fresh_collection(self):
        rc, msg, project = self.sweep({'GOOGL': [24, 25, 26, 23]})
        self.assertEqual(rc, 2)
        self.assertIn('collection fresh', msg)
        self.assertIn('GOOGL 10-Q', msg)
        self.assertIn('FAIL', msg)
        self.assertIn('UNGRADEABLE', msg)
        self.assertIn('23d', msg)
        project.assert_not_called()

    def test_thin_history_is_named_without_false_model_failure(self):
        rc, msg, project = self.sweep({'THIN': [24, 25, 26]})
        self.assertEqual(rc, 1)
        self.assertIn('THIN 10-Q', msg)
        self.assertIn('n<4', msg)
        self.assertIn('UNGRADEABLE', msg)
        self.assertNotIn('backtest FAIL', msg)
        project.assert_not_called()

    def test_valid_history_and_no_window_remains_quiet(self):
        rc, msg, _ = self.sweep({'GOOD': [24, 25, 26, 27]})
        self.assertEqual(rc, 0)
        self.assertNotIn('UNGRADEABLE', msg)

    def test_failed_issuer_does_not_suppress_valid_issuer(self):
        nw = dict(earliest=self.today, latest=self.today, typical=self.today)
        rc, msg, project = self.sweep({'BAD': [24, 25, 26, 23], 'GOOD': [24, 25, 26, 27]}, nw)
        self.assertEqual(rc, 2)
        self.assertIn('BAD 10-Q', msg)
        self.assertIn('GOOD 10-Q WINDOW OPEN', msg)
        self.assertEqual(project.call_count, 1)

    def test_stale_projection_cannot_be_silent(self):
        rc, msg, _ = self.sweep({'GOOD': [24, 25, 26, 27]}, dict(stale=True, behind_days=500))
        self.assertEqual(rc, 1)
        self.assertIn('GOOD 10-Q', msg)
        self.assertIn('STALE', msg)
        self.assertIn('500', msg)

    def test_main_propagates_filing_failure(self):
        with patch.object(boot, 'run_alert', return_value=0), patch.object(boot, 'predictions_due', return_value=(0, [])), patch.object(boot, 's2_series_age', return_value=(0, 'ok')), patch.object(boot, 'mag7_series_age', return_value=(0, 'ok')), patch.object(boot, 's4_series_age', return_value=(0, 'ok')), patch.object(boot, 'catalyst_countdown', return_value=(0, 'ok')), patch.object(boot, 'workbook_schema', return_value=(0, 'ok')), patch.object(boot, 'edgar_sweep', return_value=(2, 'GOOGL 10-Q backtest FAIL')), patch.object(boot, 'corrections_leg', return_value=(0, 'ok')), patch.object(boot, 'push_leg', return_value=(0, 'ok')):
            out = io.StringIO()
            with redirect_stdout(out):
                rc = boot.main()
        self.assertEqual(rc, 2)
        self.assertIn('GOOGL 10-Q backtest FAIL', out.getvalue())
        self.assertNotIn('all quiet', out.getvalue())

    def test_google_retirement_keeps_failed_backtest_and_open_advisory(self):
        self.write({})
        with self.ledger.open('a', newline='') as f:
            w = csv.writer(f, delimiter='\t')
            for end, lag in [('2025-03-31', 24), ('2025-06-30', 25),
                             ('2025-09-30', 26), ('2026-03-31', 23)]:
                period = date.fromisoformat(end)
                w.writerow(['GOOGL', '10-Q', period+timedelta(days=lag), end, '',
                            self.today.isoformat()+'T12:00:00Z'])
            w.writerow(['GOOGL', '10-K', '2026-02-01', '2025-12-31', '',
                        self.today.isoformat()+'T12:00:00Z'])
        with patch.object(boot, 'EDGAR_SEEN', self.ledger), \
             patch.object(EW, 'earnings_cadence', return_value=None), \
             patch.object(EW, 'next_window') as project, \
             patch.object(boot, 'date') as clock:
            clock.today.return_value = date(2026, 7, 1)
            rc, msg = boot.edgar_sweep()
        self.assertEqual(rc, 1)
        self.assertIn('historical-min bound RETIRED', msg)
        self.assertIn('legacy backtest FAIL', msg)
        self.assertIn('Calendar watch OPEN from 2026-06-30', msg)
        self.assertIn('filing date UNGRADEABLE', msg)
        project.assert_not_called()


if __name__ == '__main__':
    unittest.main()
