"""Manifest-class neighbours; acceptance written before implementation."""
import contextlib
import io
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import table_check as tc


class ManifestClasses(unittest.TestCase):
    def run_case(self, rows, files=None, history=1):
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            for name, text in (files or {}).items():
                p = root / name
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(text)
            reads = root / 'reads.tsv'
            reads.write_text(rows)
            out = io.StringIO()
            with patch.object(tc, 'ROOT', root), patch.object(tc, 'READS', reads), \
                 patch.object(tc.read_cap_check, 'class_history', return_value=history), \
                 patch.object(sys, 'argv', ['table_check']), contextlib.redirect_stdout(out):
                rc = tc.main()
            return rc, out.getvalue()

    def test_class_scans_untracked_defective_member(self):
        rc, out = self.run_case('READ\tPROME\tinbox/*.md\twhole\n',
            {'inbox/a.md': '| a | b |\n|---|---|\n| 1 | 2 | lost |\n'})
        self.assertEqual(rc, 1)
        self.assertIn('lost', out)

    def test_empty_historical_class_is_explicit(self):
        rc, out = self.run_case('READ\tPROME\tinbox/*.md\twhole\n')
        self.assertEqual(rc, 0)
        self.assertIn('zero current files scanned', out)

    def test_typo_and_unavailable_history_are_unknown(self):
        for history in [0, None]:
            with self.subTest(history=history):
                rc, out = self.run_case('READ\tPROME\ttypo/*.md\twhole\n', history=history)
                self.assertEqual(rc, 2)
                self.assertIn('UNKNOWN', out)

    def test_concrete_missing_stays_unknown(self):
        self.assertEqual(self.run_case('READ\tPROME\tmissing.md\twhole\n')[0], 2)

    def test_other_reader_and_scoped_rows_do_not_enter(self):
        self.assertEqual(self.run_case('READ\tOTHER\tmissing.md\twhole\nREAD\tPROME\tmissing.md\tscoped\n')[0], 0)

    def test_concrete_and_class_overlap_preserves_finding(self):
        self.assertEqual(self.run_case('READ\tPROME\tinbox/a.md\twhole\nREAD\tPROME\tinbox/*.md\twhole\n',
            {'inbox/a.md': '| a |\n|---|\n| 1 | 2 |\n'})[0], 1)

    def test_deleted_after_expansion_is_unknown(self):
        with patch.object(tc.read_cap_check, '_class_members', return_value=['/nonexistent/table-check-deleted.md']):
            self.assertEqual(self.run_case('READ\tPROME\tinbox/*.md\twhole\n')[0], 2)


if __name__ == '__main__':
    unittest.main()
