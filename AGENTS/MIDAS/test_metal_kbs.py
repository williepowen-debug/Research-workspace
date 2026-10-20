"""Check lossless filtering and visible failure when derived KBs drift."""
import contextlib
import csv
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import boot
import refresh_metal_kbs as kb


class MetalKBTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'workbook').mkdir()
        self.rows = [dict.fromkeys(kb.FIELDS, '') for _ in range(3)]
        for row, key in zip(self.rows, ['gold-only', 'pair', 'desk']):
            row.update(id=key, fact='Quoted "fact"\twith newline\nand gold 金 ' * 300,
                       source='original/source', as_of='2026-10-19')
        self.tags = [dict(id=key, metals=metal, rationale='Reviewed subject')
                     for key, metal in [('gold-only', 'gold'),
                                        ('pair', 'platinum,palladium'),
                                        ('desk', 'shared')]]
        self.save_inputs()

    def save_inputs(self):
        for name, fields, rows in [('workbook/KB.tsv', kb.FIELDS, self.rows),
                                   ('KB_METALS.tsv', ('id', 'metals', 'rationale'), self.tags)]:
            with (self.root / name).open('w', newline='') as stream:
                writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t')
                writer.writeheader()
                writer.writerows(rows)

    def run_views(self, refresh=False):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return kb.run(self.root, refresh=refresh)

    def test_lossless_filtering_and_multi_metal_overlap(self):
        original = (self.root / 'workbook/KB.tsv').read_bytes()
        self.assertEqual(self.run_views(True), 0)
        expected = {'gold': self.rows[:1], 'silver': [], 'platinum': self.rows[1:2],
                    'palladium': self.rows[1:2], 'copper': [], 'shared': self.rows[1:]}
        for metal, rows in expected.items():
            with (self.root / metal / 'KB.tsv').open(newline='') as stream:
                self.assertEqual(list(csv.DictReader(stream, delimiter='\t')), rows)
        self.assertEqual((self.root / 'workbook/KB.tsv').read_bytes(), original)
        self.assertEqual(self.run_views(), 0)

    def test_missing_and_tampered_views_require_review_without_repair(self):
        self.assertEqual(self.run_views(), 1)
        self.assertFalse((self.root / 'gold').exists())
        self.run_views(True)
        path = self.root / 'gold/KB.tsv'
        path.write_text('tampered')
        self.assertEqual(self.run_views(), 1)
        self.assertEqual(path.read_text(), 'tampered')

    def test_new_unclassified_row_blocks_refresh_without_partial_updates(self):
        self.run_views(True)
        before = (self.root / 'gold/KB.tsv').read_bytes()
        self.rows.append(dict(self.rows[0], id='new'))
        self.save_inputs()
        self.assertEqual(self.run_views(True), 2)
        self.assertEqual((self.root / 'gold/KB.tsv').read_bytes(), before)

    def test_changed_canonical_fact_and_reclassification_are_detected(self):
        self.run_views(True)
        self.rows[0]['fact'] = 'Source correction'
        self.save_inputs()
        self.assertEqual(self.run_views(), 1)
        self.run_views(True)
        self.tags[0]['metals'] = 'silver'
        self.save_inputs()
        self.assertEqual(self.run_views(), 1)

    def test_invalid_assignments_and_duplicate_ids_fail(self):
        for change in ['unknown', 'gold,gold', 'shared,gold', '']:
            with self.subTest(tags=change):
                self.tags[0]['metals'] = change
                self.save_inputs()
                self.assertEqual(self.run_views(True), 2)
        self.tags[0]['metals'] = 'gold'
        self.tags.append(dict(self.tags[0]))
        self.save_inputs()
        self.assertEqual(self.run_views(True), 2)
        self.tags.pop()
        self.rows.append(dict(self.rows[0]))
        self.save_inputs()
        self.assertEqual(self.run_views(True), 2)

    def test_missing_input_fails(self):
        (self.root / 'KB_METALS.tsv').unlink()
        self.assertEqual(self.run_views(True), 2)

    def test_real_cli_is_cwd_independent(self):
        result = subprocess.run([sys.executable, str(kb.HERE / 'refresh_metal_kbs.py'),
                                 '--check'], cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def test_boot_reports_stale_and_invalid_kbs(self):
        for status in (1, 2):
            with self.subTest(status=status), \
                    patch.object(boot, 'run_marked', side_effect=lambda cmd: status if '--check' in cmd else 0), \
                    patch.object(boot, 'run_alert', return_value=0), \
                    patch.object(boot, 'predictions_due', return_value=(0, [])), \
                    patch.object(boot, 'cot_vintage_leg', return_value=(0, [])), \
                    patch.object(boot, 'cot_metals_vintage_leg', return_value=(0, [])):
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    self.assertEqual(boot.main(), status)
                self.assertIn('ledger staleness / metal KB views', output.getvalue().splitlines()[-1])


if __name__ == '__main__':
    unittest.main()
