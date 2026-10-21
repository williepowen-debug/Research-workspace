"""Contract and adversarial tests; temporary inputs only."""
import contextlib
import datetime as dt
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('coverage_check', Path(__file__).with_name('calendar_docket_coverage.py'))
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
DAY = dt.date(2026, 10, 20)


class Coverage(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.ledger = self.root / 'AGENTS/DAEDALUS/docket/CATALYSTS.tsv'
        self.docket = self.root / 'PROME/DOCKET.tsv'
        self.ledger.parent.mkdir(parents=True)
        self.docket.parent.mkdir(parents=True)
        self.ledger.write_text('date\tevent\n2026-10-20\tMETA Q3 earnings\n')
        self.docket.write_text('2026-10-20\tMETA Q3 results\tDAEDALUS\tPENDING\tx\ty\n')

    def run_check(self):
        return c.assess(self.root, self.docket, [self.ledger], DAY, 14)

    def test_clean(self):
        r = self.run_check()
        self.assertEqual(r['rc'], 0)
        self.assertEqual(r['records'][0]['matches'][0]['terms'], ['meta'])

    def test_missing(self):
        self.docket.write_text('2026-10-20\tMSFT Q3 results\tDAEDALUS\tPENDING\tx\ty\n')
        self.assertEqual(self.run_check()['rc'], 1)

    def test_wrong_owner_and_notes(self):
        for owner in ('VULCAN', 'VULCAN (DAEDALUS informed)'):
            with self.subTest(owner=owner):
                self.docket.write_text(f'2026-10-20\tMETA Q3 results\t{owner}\tPENDING\tx\tDAEDALUS\n')
                self.assertEqual(self.run_check()['rc'], 1)

    def test_history_does_not_match(self):
        self.docket.write_text('2026-10-20\tMSFT Q3 results\tDAEDALUS\tPENDING META\tx\tMETA earnings\n')
        self.assertEqual(self.run_check()['rc'], 1)

    def test_generic_only(self):
        self.ledger.write_text('date\tevent\n2026-10-20\tQ3 earnings review\n')
        self.assertEqual(self.run_check()['rc'], 2)

    def test_weekday_not_identity(self):
        for day in ('Wed', 'Wednesday', 'Thu', 'Thurs'):
            self.ledger.write_text(f'date\tevent\n2026-10-20\tMETA earnings ({day})\n')
            self.docket.write_text(f'2026-10-20\tMSFT earnings ({day})\tDAEDALUS\tPENDING\tx\ty\n')
            self.assertEqual(self.run_check()['rc'], 1)

    def test_multiple(self):
        self.docket.write_text(self.docket.read_text() * 2)
        self.assertEqual(self.run_check()['rc'], 2)

    def test_quarter_conflict(self):
        self.docket.write_text(self.docket.read_text().replace('Q3', 'Q2'))
        self.assertEqual(self.run_check()['rc'], 2)

    def test_window(self):
        self.ledger.write_text('date\tevent\n2026-10-19\tMETA\n2026-10-20\tMETA\n2026-11-03\tMETA\n2026-11-04\tMETA\n')
        r = self.run_check()
        self.assertEqual(r['counts']['OUTSIDE-WINDOW'], 2)
        self.assertEqual(r['counts']['MATCHED'], 1)
        self.assertEqual(r['counts']['UNMATCHED'], 1)

    def test_invalid_relative_dates(self):
        for date in ('2026-02-30', '~2026-10-20', 'Oct 20', 'next-session', '2026-10-20..2026-10-21', ''):
            with self.subTest(date=date):
                self.ledger.write_text(f'date\tevent\n{date}\tMETA\n')
                self.assertEqual(self.run_check()['rc'], 2)

    def test_unknown_dominates_missing(self):
        self.ledger.write_text('date\tevent\n2026-10-21\tAMD\ntomorrow\tMETA\n')
        r = self.run_check()
        self.assertEqual(r['rc'], 2)
        self.assertEqual(r['counts']['UNMATCHED'], 1)

    def test_empty_cases(self):
        for text in ('', 'date\tevent\n', 'date\tevent\n2027-10-20\tMETA\n'):
            self.ledger.write_text(text)
            self.assertEqual(self.run_check()['rc'], 2)
        self.assertEqual(c.assess(self.root, self.docket, [], DAY, 14)['rc'], 2)

    def test_bad_docket(self):
        for text in ('', '2026-10-20\tMETA\n', '2026-02-30\tMETA\tDAEDALUS\tPENDING\tx\ty\n'):
            self.docket.write_text(text)
            self.assertEqual(self.run_check()['rc'], 2)

    def test_ragged_tsv(self):
        self.ledger.write_text('date\tevent\n2026-10-20\tMETA\textra\n')
        self.assertEqual(self.run_check()['rc'], 2)

    def test_quoted_tsv(self):
        self.ledger.write_text('date\tevent\n2026-10-20\t"META\tQ3 earnings"\n')
        self.assertEqual(self.run_check()['rc'], 0)
        self.ledger.write_text('date\tevent\n2026-10-20\t"META\n')
        self.assertEqual(self.run_check()['rc'], 2)

    def test_markdown_multiple_tables(self):
        self.ledger = self.root / 'AGENTS/DAEDALUS/CALENDAR.md'
        self.ledger.write_text('| Date | Event |\n|---|---|\n| **2026-10-20** (Tue) | META Q3 \\| earnings |\n\n## More\n|When|What|\n|---|---|\n|2026-11-04|AMD|\n')
        r = self.run_check()
        self.assertEqual(r['rc'], 0)
        self.assertEqual(r['counts']['OUTSIDE-WINDOW'], 1)

    def test_exclusions(self):
        self.ledger.write_text('date\tevent\tStatus\n2026-10-20\tMETA\tPENDING\ntomorrow\tAMD\tRESOLVED\n')
        self.assertEqual(self.run_check()['rc'], 0)
        self.ledger.write_text('# FROZEN 2026-10-20\ndate\tevent\n2026-10-20\tMETA\n')
        r = self.run_check()
        self.assertEqual(r['rc'], 2)
        self.assertEqual(r['counts']['EXCLUDED'], 1)

    def test_history_section_does_not_leak(self):
        self.ledger = self.root / 'AGENTS/DAEDALUS/CALENDAR.md'
        self.ledger.write_text('## RESOLVED\n- Oct 20 closed.\n### Subsection\n- Oct 22 done.\n## ACTIVE\n|Date|Event|\n|---|---|\n|2026-10-20|META with resolved issue|\n')
        r = self.run_check()
        self.assertEqual(r['rc'], 0)
        self.assertEqual(r['counts']['EXCLUDED'], 2)

    def test_unsupported_md(self):
        self.ledger = self.root / 'AGENTS/DAEDALUS/CALENDAR.md'
        for text in ('- Oct 20 META\n', '|Date|Ticker|\n|---|---|\n|2026-10-20|META|\n', '|Date|Event|\n|---|---|\n|2026-10-20|META|extra|\n'):
            self.ledger.write_text(text)
            self.assertEqual(self.run_check()['rc'], 2)

    def test_live_headings_and_relative_prose(self):
        self.ledger = self.root / 'AGENTS/DAEDALUS/CALENDAR.md'
        control = '|Date|Event|\n|---|---|\n|2026-10-20|META earnings|\n\n'
        for tail in ('## 2026-10-21 AMD earnings\n', '- Tomorrow AMD earnings\n', '## Next-week review\n'):
            self.ledger.write_text(control + tail)
            r = self.run_check()
            self.assertEqual(r['rc'], 2)
            self.assertEqual(r['counts']['MATCHED'], 1)
            self.assertEqual(r['counts']['UNASSESSED'], 1)

    def test_docket_ranges(self):
        for span, rc in [('2026-10-19..2026-10-21', 2), ('~2026-10-20', 2), ('next-session', 2)]:
            self.docket.write_text(f'{span}\tMETA Q3\tDAEDALUS\tPENDING\tx\ty\n')
            self.assertEqual(self.run_check()['rc'], rc)

    def test_missing_file(self):
        self.ledger = self.ledger.with_name('missing.tsv')
        self.assertEqual(self.run_check()['rc'], 2)

    def test_change_during_read(self):
        original = Path.read_bytes
        calls = {}
        def read(p):
            calls[p] = calls.get(p, 0) + 1
            data = original(p)
            return data + b' ' if p == self.ledger and calls[p] == 2 else data
        with patch.object(Path, 'read_bytes', read):
            self.assertEqual(self.run_check()['rc'], 2)

    def test_cli_and_discovery(self):
        args = ['--root', str(self.root), '--as-of', DAY.isoformat()]
        with contextlib.redirect_stdout(io.StringIO()) as out:
            rc = c.main(args)
        self.assertEqual(rc, 0)
        self.assertIn('CLEAN:', out.getvalue())
        self.assertIn('DAEDALUS', out.getvalue())
        with contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(c.main(args + ['--json']), 0)
        self.assertEqual(len(json.loads(out.getvalue())['files']), 1)
        self.docket.write_text(self.docket.read_text().replace('META', 'MSFT'))
        with contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(c.main(args), 1)
        self.assertIn('UNMATCHED', out.getvalue())
        print('Watched capable flag:', [s for s in out.getvalue().splitlines() if s.startswith('UNMATCHED')][0])


if __name__ == '__main__':
    unittest.main()
