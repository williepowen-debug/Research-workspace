"""L757 production-shaped regression and retained-alert controls.

Run from repository root. FIRETIME_MODULE may select the original implementation
for the mutation check; never mutate production input documents.
"""
import datetime as dt
import importlib.util
import os
import subprocess
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    'firetime_l757', os.environ.get('FIRETIME_MODULE', ROOT / 'scripts/firetime_check.py'))
f = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(f)
f.REPO = str(ROOT)
TODAY = dt.date(2026, 10, 21)
ROWS = [{'start': dt.date(2026, 12, 31), 'end': dt.date(2026, 12, 31),
         'catalyst': 'control deadline'}]


class L757(unittest.TestCase):
    def flags(self, text):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / 'sample.md'
            path.write_text(text)
            with patch.object(f, 'git_time', return_value=None):
                return f.check_artifact(str(path), ROWS, set(), TODAY)[0]

    def dates(self, text):
        return [x for x in self.flags(text) if x.startswith('DATE DRIFT:')]

    def test_explicit_historical_year_not_truncated(self):
        for token in ['1/18/2022', '01/01/2025', '1/13/2023', '1/19/26']:
            with self.subTest(token=token):
                self.assertEqual([], self.dates('Event ' + token))

    def test_explicit_future_year_preserved(self):
        self.assertTrue(any('2027-01-18' in x for x in self.dates('Due 1/18/2027')))

    def test_far_future_year_not_truncated(self):
        self.assertEqual([], self.dates('Due 1/18/2028'))

    def test_fraction_of_and_size(self):
        for text in ['~1/6 of FLG’s book', '**~1/16 the size**',
                     '**1/16 of FLG’s $8.9B**']:
            with self.subTest(text=text):
                self.assertEqual([], self.dates(text))

    def test_score_and_ratio(self):
        for text in ['V3 score = 1/5', 'V3 was cut **2/5 → 1/5**',
                     '**brief-gap rate = 1/17.**', 'Hit rate = 12/24']:
            with self.subTest(text=text):
                self.assertEqual([], self.dates(text))

    def test_quantity_does_not_suppress_other_date(self):
        self.assertTrue(self.dates('Hit rate 12/24; next due 1/5.'))

    def test_ambiguous_periods_not_silently_suppressed(self):
        self.assertTrue(self.dates('$601M [12/25]'))
        self.assertTrue(self.dates('$10.9M (12/24 → 6/26)'))

    def test_ambiguous_dates_still_flag(self):
        for text in ['Due 12/24', 'Due Dec-25', 'at 12/23', 'V3 1/5']:
            with self.subTest(text=text):
                self.assertTrue(self.dates(text))

    def test_templates_not_paths(self):
        self.assertEqual([], self.flags('Daily detail `memory/YYYY-MM-DD.md`.'))

    def test_concrete_missing_path_retained(self):
        self.assertTrue(any('DEAD POINTER' in x for x in self.flags(
            'Daily detail `memory/2099-12-31-L757-absent.md`.')))

    def test_local_negation_does_not_hide_other_path(self):
        flags = self.flags('Use `PROME/inbox/`, NOT `AGENTS/PROME/inbox/`; '
                           'read `scripts/L757-absent.py`.')
        self.assertFalse(any('AGENTS/PROME' in x for x in flags))
        self.assertTrue(any('scripts/L757-absent.py' in x for x in flags))

    def test_git_object_artifact(self):
        flags, infos = f.check_artifact(
            '778ef6a38:PROME/inbox/2026-10-12_from-MIDAS_news-sweep.md',
            ROWS, set(), TODAY)
        self.assertFalse(any(x.startswith('UNREADABLE') for x in flags))
        self.assertTrue(any('pinned Git blob' in x for x in infos))

    def test_historical_pointer_uses_tree_not_working_file(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            def git(*args, data=None):
                return subprocess.run(['git', '-C', d, *args], input=data,
                                      capture_output=True, text=True, check=True).stdout.strip()
            git('init', '-q')
            blob = git('hash-object', '-w', '--stdin', data='Historical file.\n')
            source = git('hash-object', '-w', '--stdin',
                         data='Read `scripts/old.py` and `scripts/new.py`.\n')
            subtree = git('mktree', data=f'100644 blob {blob}\told.py\n')
            tree = git('mktree', data=f'100644 blob {source}\tsource.md\n'
                                    f'040000 tree {subtree}\tscripts\n')
            (repo / 'scripts').mkdir()
            (repo / 'scripts/new.py').write_text('Only exists in working tree.\n')
            with patch.object(f, 'REPO', d):
                flags, _ = f.check_artifact(tree + ':source.md', ROWS, set(), TODAY)
            self.assertTrue(any('scripts/new.py' in x for x in flags))
            self.assertFalse(any('scripts/old.py' in x for x in flags))

    def test_review_repeated_relative_pointer(self):
        flags = self.flags('NOT `workbook/L757-absent.tsv`; read `workbook/L757-absent.tsv`.')
        self.assertTrue(any('workbook/L757-absent.tsv' in x for x in flags))

    def test_review_rate_date_not_assignment(self):
        self.assertTrue(self.dates('Review rate 1/17'))

    def test_review_pinned_blob_still_has_date_claims(self):
        with tempfile.TemporaryDirectory() as d:
            def git(*args, data=None):
                return subprocess.run(['git', '-C', d, *args], input=data,
                                      capture_output=True, text=True, check=True).stdout.strip()
            git('init', '-q')
            blob = git('hash-object', '-w', '--stdin', data='Operative deadline 2027-01-17.\n')
            tree = git('mktree', data=f'100644 blob {blob}\tletter.md\n')
            with patch.object(f, 'REPO', d):
                flags, _ = f.check_artifact(tree + ':letter.md', ROWS, set(), TODAY)
            self.assertTrue(any('DATE DRIFT' in x for x in flags))

    def test_missing_git_object_not_clean(self):
        flags, _ = f.check_artifact('778ef6a38:scripts/L757-absent.md', ROWS, set(), TODAY)
        self.assertTrue(any(x.startswith('UNREADABLE') for x in flags))


if __name__ == '__main__':
    unittest.main()
