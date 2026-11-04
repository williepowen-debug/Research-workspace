"""Bounded ISO-date/weekday emphasis regression tests (PR9 priority 5).

CLAIM_CHECK_SOURCE can name the original-source mutant for discrimination.
"""
import importlib.util
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
SOURCE = Path(os.environ.get('CLAIM_CHECK_SOURCE', ROOT / 'scripts/claim_check.py'))
spec = importlib.util.spec_from_file_location('claim_markdown_subject', SOURCE)
claim = importlib.util.module_from_spec(spec)
spec.loader.exec_module(claim)


class ClaimMarkdownTests(unittest.TestCase):
    def flags(self, line):
        return claim.weekday_flags('fixture.md', 7, line, 2026)

    def test_plain_contract(self):
        self.assertEqual(self.flags('2026-11-02 (Tue)'), [
            ('fixture.md', 7, 'weekday',
             '“2026-11-02 (Tue” — 2026-11-02 is a Monday, not Tue')])
        self.assertEqual(self.flags('2026-11-02 (Mon)'), [])

    def test_balanced_iso_and_day_wrappers(self):
        for marker in ('**', '__', '*', '_'):
            for line in (
                f'{marker}2026-11-02{marker} (Tue)',
                f'2026-11-02 ({marker}Tue{marker})',
                f'{marker}2026-11-02{marker} ({marker}Tue{marker})',
                f'{marker}Tue{marker} {marker}2026-11-02{marker}',
            ):
                with self.subTest(line=line):
                    self.assertEqual(len(self.flags(line)), 1)
                    self.assertEqual(self.flags(line.replace('Tue', 'Mon')), [])

    def test_production_shapes_and_wrong_day_mutants(self):
        # Exact date/weekday fragments of real production Markdown, plus labels
        # changed to wrong weekdays. No source evidence or market grade inferred.
        specimens = [
            ('| **2026-09-29** (Tue) 1:30 pm |', 'Tue', 'Wed'),
            ('| ~~**2026-10-28** (Wed) 11:00 am~~', 'Wed', 'Thu'),
            ('**2026-08-11** (Tuesday).', 'Tuesday', 'Wednesday'),
        ]
        for line, correct, wrong in specimens:
            with self.subTest(line=line):
                self.assertEqual(self.flags(line), [])
                self.assertEqual(len(self.flags(line.replace(correct, wrong))), 1)

    def test_scoped_formats_not_global_markdown_strip(self):
        for line in ('**11/02** (Tue)', '**Nov 2** (Tue)',
                     'Tue-Wed **2026-11-02**-03',
                     '**2026-11-02** Tue-Wed',
                     '**2026-11-02**-03 Tue-Wed'):
            with self.subTest(line=line):
                self.assertEqual(claim.normalize_iso_emphasis(line), line)
        self.assertEqual(self.flags('**11/02** (Tue)'), [])
        self.assertEqual(self.flags('**Nov 2** (Tue)'), [])

    def test_year_positions_unchanged(self):
        line = '**2026-11-02** (**Mon**) | Q2-2024 precedent = Tue 8/6'
        normalized = claim.normalize_iso_emphasis(line)
        self.assertEqual(len(line), len(normalized))
        self.assertEqual(line.index('2024'), normalized.index('2024'))
        self.assertEqual(line.index('8/6'), normalized.index('8/6'))
        self.assertEqual(self.flags(line), [])

    def test_adjacent_date_ownership(self):
        self.assertEqual(self.flags('**2026-11-01** — **Mon** **2026-11-02**'), [])
        self.assertEqual(len(self.flags('**2026-11-01** — **Tue** **2026-11-02**')), 1)

    def test_no_invalid_date_or_substring_invention(self):
        for line in ('**2026-02-30** (Tue)', '**2026-11-02** (Tuesdayish)',
                     '**2026-11-02** (Saturn)'):
            with self.subTest(line=line):
                self.assertEqual(self.flags(line), [])

    def test_other_checks_see_original_text(self):
        line = '**2026-11-02** (Tue) October25 gold $374'
        both = claim.check_text('fixture.md', line, {'weekday', 'units', 'glued'}, 2026)
        original = claim.check_text('fixture.md', line, {'units', 'glued'}, 2026)
        self.assertEqual([x for x in both if x[2] != 'weekday'], original)
        self.assertEqual(sorted(x[2] for x in both), ['glued', 'units', 'weekday'])

    def test_existing_weekday_cases(self):
        for line, expected in claim.SELFTEST:
            with self.subTest(line=line):
                self.assertEqual(len(self.flags(line)), expected)

    def test_cli_output_and_codes(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'case.md'
            p.write_text('**2026-11-02** (Tue)\n')
            args = ['python3', str(SOURCE), '--check', 'weekday', '--year', '2026', str(p)]
            bad = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
            self.assertEqual(bad.returncode, 1, bad.stdout)
            self.assertIn('[weekday]', bad.stdout)
            self.assertIn(f'{p}:1', bad.stdout)
            self.assertIn('Monday, not Tue', bad.stdout)
            p.write_text('**2026-11-02** (Mon)\n')
            good = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
            self.assertEqual(good.returncode, 0, good.stdout)
            self.assertIn('1 file(s) clean [weekday]', good.stdout)
            usage = subprocess.run(['python3', str(SOURCE), '--check', 'glud', str(p)],
                                   cwd=ROOT, text=True, capture_output=True)
            self.assertEqual(usage.returncode, 2)
            self.assertIn('nothing was checked', usage.stdout)


if __name__ == '__main__':
    unittest.main()
