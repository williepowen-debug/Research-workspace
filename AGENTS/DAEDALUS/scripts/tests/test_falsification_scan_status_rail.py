#!/usr/bin/env python3
"""Acceptance tests for the in-STATUS kill-rail reader (design/2026-10-30_FALSIFICATION_SCAN_STATUS_RAIL.md)."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('falsification_scan', HERE.parent/'falsification_scan.py')
fs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fs)


def status(rail_line, updated='2026-09-30', pad=0):
    lines = ['# X STATUS', '', f'**Last Updated: {updated}**', '']
    lines += [f'filler {i}' for i in range(pad)]
    lines += ['## EXIT RULES', rail_line, '| rule | state |']
    return '\n'.join(lines) + '\n'


class StatusRailTests(unittest.TestCase):
    def rails(self, text, group='ACTIVE'):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            (d/'STATUS.md').write_text(text)
            return fs.status_rails('X', group, d, fs.status_date(d), None, False)

    def test_ac2_stale_rail_flags(self):
        rows = self.rails(status('*Kill rail re-derived: 2026-08-17.*'))
        self.assertEqual([r['verdict'] for r in rows], ['STALE-FLAGGED'])
        self.assertEqual(rows[0]['age'], 44)

    def test_clean_rail_reads_current(self):
        rows = self.rails(status('**Kill rail re-derived: 2026-09-22** (re-checked 9/28)'))
        self.assertEqual([r['verdict'] for r in rows], ['CURRENT'])
        self.assertEqual(rows[0]['cls'], 'kill rail (in-STATUS)')

    def test_ac3_prose_is_not_a_rail(self):
        rows = self.rails(status('The kill rail was re-derived last month after the print.'))
        self.assertEqual(rows, [])

    def test_ac4_deep_line_found_with_line_number(self):
        rows = self.rails(status('*Kill rail re-derived: 2026-09-22*', pad=80))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['surface'], 'STATUS.md:86')

    def test_ac6_dormant_skips(self):
        rows = self.rails(status('*Kill rail re-derived: 2026-08-17.*'), group='DORMANT')
        self.assertEqual([r['verdict'] for r in rows], ['DORMANT-SKIP'])

    def test_no_status_file_yields_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(fs.status_rails('X', 'ACTIVE', Path(tmp), None, None, False), [])


if __name__ == '__main__':
    unittest.main()
