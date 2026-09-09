"""Regression checks for advisory reporting and both incident quantity representations."""
import contextlib
import csv
import importlib.util
import io
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / (name + '.py'))
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


boot = module('boot')
instrument = module('instrument_check')


class Reporting(unittest.TestCase):
    def run_child(self, rc, stdout, stderr=''):
        result = subprocess.CompletedProcess([], rc, stdout, stderr)
        with patch.object(boot.subprocess, 'run', return_value=result):
            return boot.run_script(SCRIPTS / 'instrument_check.py', [])

    def test_advisory_is_visible_without_blocking(self):
        self.assertEqual(self.run_child(0, 'BRENT_INSTRUMENT_SUMMARY: WARNINGS; stale_active=2')[0], 'WARNINGS')

    def test_generic_caution_does_not_make_clean_run_warning(self):
        self.assertEqual(self.run_child(0, '⚠️ This checks instruments, not levels.\nBRENT_INSTRUMENT_SUMMARY: OK')[0], 'OK')

    def test_warning_never_downgrades_failure_or_findings(self):
        for rc, expected in ((1, 'FAIL'), (2, 'FINDINGS')):
            self.assertEqual(self.run_child(rc, 'BRENT_INSTRUMENT_SUMMARY: WARNINGS')[0], expected)

    def test_missing_script_and_timeout_fail(self):
        self.assertEqual(boot.run_script(SCRIPTS / 'does-not-exist.py', [])[0], 'FAIL')
        with patch.object(boot.subprocess, 'run', side_effect=subprocess.TimeoutExpired([], 1)):
            self.assertEqual(boot.run_script(SCRIPTS / 'instrument_check.py', [])[0], 'FAIL')

    def test_summary_exit_codes_and_no_false_clean_body(self):
        for state, expected in (('OK', 0), ('WARNINGS', 0), ('FINDINGS', 2), ('FAIL', 1)):
            with self.subTest(state=state):
                buf = io.StringIO()
                with patch.object(boot, 'BOOT_SEQUENCE', [('fixture', 'instrument_check.py', [], False)]), \
                     patch.object(boot, 'run_script', return_value=(state, 'plain diagnostic', 0)), \
                     patch.object(boot.sys, 'argv', ['boot.py']), contextlib.redirect_stdout(buf):
                    self.assertEqual(boot.main(), expected)
                output = buf.getvalue()
                if state != 'OK':
                    self.assertNotIn('ran cleanly', output)
                    self.assertNotIn('All scripts completed successfully', output)
                if state == 'WARNINGS':
                    self.assertIn('ADVISORY WARNINGS', output)


class IncidentQuantity(unittest.TestCase):
    def check(self, **overrides):
        row = dict(id='RF-TEST', facility='Fixture', status='PARTIAL_RESTART',
                   capacity_unit='BPD', offline_unit='BPD', capacity_bpd='380000',
                   bpd_offline_est='47000', capacity_qty='380000', offline_qty='47000')
        row.update(overrides)
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'incidents.tsv'
            with p.open('w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=list(row), delimiter='\t')
                writer.writeheader(); writer.writerow(row)
            with patch.object(instrument, 'INCIDENTS', p):
                return instrument.check_incident_impossible()

    def test_typed_impossible_even_when_legacy_repaired(self):
        self.assertEqual(self.check(offline_qty='415000')[0][2:4], (380000, 415000))

    def test_legacy_impossible_even_when_typed_repaired(self):
        self.assertEqual(len(self.check(bpd_offline_est='415000')), 1)

    def test_no_double_report_and_no_wrong_unit_comparison(self):
        self.assertEqual(len(self.check(bpd_offline_est='415000', offline_qty='415000')), 1)
        self.assertEqual(self.check(offline_unit='BCFD', offline_qty='415000'), [])
        self.assertEqual(self.check(offline_qty='', bpd_offline_est=''), [])
        self.assertEqual(self.check(), [])


if __name__ == '__main__':
    unittest.main()
