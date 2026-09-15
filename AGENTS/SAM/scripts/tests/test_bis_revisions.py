"""Ensure revised same-quarter data cannot hide behind an unchanged period label."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('bis_gli', Path(__file__).parents[1] / 'bis_gli.py')
bis = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bis)

class RevisionTests(unittest.TestCase):
    def row(self, quarter, value, stamp):
        return [quarter, 'series', 'label', value, '1', '3P', 'loans', 'BIS', 'stock', stamp]

    def test_revision_replaces_key_and_preserves_other_quarter(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'data.tsv'
            bis.upsert_observations(p, [self.row('2025-Q4', '60', 'old'), self.row('2026-Q1', '65.83', 'old')])
            self.assertEqual(bis.upsert_observations(p, [self.row('2026-Q1', '65.91', 'new')]), 1)
            self.assertEqual(len(p.read_text().splitlines()), 3)
            self.assertIn('2025-Q4', p.read_text())
            self.assertIn('65.91', p.read_text())
            self.assertNotIn('65.83', p.read_text())
            prior = p.read_bytes()
            self.assertEqual(bis.upsert_observations(p, [self.row('2026-Q1', '65.91', 'later')]), 0)
            self.assertEqual(p.read_bytes(), prior)

    def test_duplicate_input_does_not_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'data.tsv'
            row = self.row('2026-Q1', '65.91', 'new')
            with self.assertRaises(ValueError):
                bis.upsert_observations(p, [row, row])
            self.assertFalse(p.exists())

if __name__ == '__main__':
    unittest.main()
