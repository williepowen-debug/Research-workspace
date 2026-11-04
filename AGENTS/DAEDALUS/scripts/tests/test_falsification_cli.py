"""Regression contract: real omitted bucket, CLI usage and unchanged row detection."""
import contextlib
import importlib.util
import io
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SOURCE = Path(os.environ.get('FALSIFICATION_SCAN_SOURCE', Path(__file__).parents[1] / 'falsification_scan.py'))
spec = importlib.util.spec_from_file_location('falsification_cli_subject', SOURCE)
scan = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scan)


class CLIContract(unittest.TestCase):
    def invoke(self, args):
        out, err = io.StringIO(), io.StringIO()
        with patch('sys.argv', ['falsification_scan.py', *args]), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                rc = scan.main()
            except SystemExit as exc:
                rc = exc.code
        return rc, out.getvalue(), err.getvalue()

    def test_real_market_candidate_both_modes(self):
        for mode in ([], ['--tsv']):
            with self.subTest(mode=mode):
                rc, out, _ = self.invoke(['--agent', 'BROCK', *mode])
                self.assertEqual(rc, 1)
                self.assertIn('BROCK', out)
                self.assertIn('MARKET', out)

    def test_real_meta_clean(self):
        rc, out, _ = self.invoke(['--agent', 'DAEDALUS'])
        self.assertEqual(rc, 0)
        self.assertIn('DAEDALUS', out)
        self.assertIn('non-Market', out)

    def test_help_does_not_load_or_scan(self):
        for arg in ['--help', '-h']:
            with self.subTest(arg=arg), patch.object(scan, 'groups', side_effect=AssertionError('help loaded directory')):
                rc, out, _ = self.invoke([arg])
                self.assertEqual(rc, 0)
                self.assertIn('usage:', out)
                self.assertIn('--agent', out)

    def test_invalid_arguments(self):
        for args in [['--typo'], ['--agent'], ['--agent', '--tsv'], ['--agent', 'NOT_A_DESK'], ['--agent', ''], ['--agent='], ['BROCK']]:
            with self.subTest(args=args):
                self.assertEqual(self.invoke(args)[0], 2)

    def test_current_stale_unstamped_rows_and_no_rail(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            desk = root / 'TEST'
            desk.mkdir()
            (desk / 'STATUS.md').write_text('Last Updated: 2026-10-30\n')
            thesis = desk / 'THESIS.md'
            thesis.write_text('Version v1.0\nLast updated: 2026-10-30\n')
            rail = desk / 'KILL.md'
            with patch.object(scan, 'AGENTS', root), patch.object(scan, 'groups', return_value={'TEST':'ACTIVE'}), patch.object(scan, 'agent_classes', return_value={'TEST':'Market'}):
                for content, expected, verdict in [('Last updated: 2026-10-30\n',0,'CURRENT'), ('Last updated: 2026-08-01\n',1,'STALE-FLAGGED'), ('No date\n',1,'UNSTAMPED')]:
                    rail.write_text(content)
                    rc, out, _ = self.invoke(['--agent','TEST','--tsv'])
                    self.assertEqual(rc, expected)
                    self.assertIn(verdict, out)
                rail.unlink()
                self.assertEqual(self.invoke(['--agent','TEST'])[0], 1)


if __name__ == '__main__':
    unittest.main()
