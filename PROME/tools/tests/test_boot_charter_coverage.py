"""Runtime charter coverage; all mutable inputs live in disposable directories."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[3]

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, REPO / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

readcap = load('charter_readcap', 'scripts/read_cap_check.py')
gate = load('charter_gate', 'PROME/tools/prome_gate.py')
session = load('charter_session', 'PROME/tools/boot_session.py')

class CharterCoverage(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix='charter-coverage-')
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        (self.root / 'PROME').mkdir()
        (self.root / 'CLAUDE.md').write_text('root instructions')
        (self.root / 'PROME/CLAUDE.md').write_text('local instructions')
        (self.root / 'PROME/BOOT.md').write_text('boot instructions')
        self.enterContext(patch.object(readcap, 'ROOT', str(self.root)))
        self.enterContext(patch.object(readcap, 'READS_TSV', str(self.root / 'reads.tsv')))
        self.enterContext(patch.object(session, 'ROOT', self.root))
        self.manifest()

    def manifest(self, paths=('PROME/BOOT.md',), attested=True):
        rows = ['ATTESTATION\tPROME\t.\tmanifest-complete\ts\tPROME\t2026-10-04\tfixture'] if attested else []
        rows += [f'READ\tPROME\t{p}\twhole\ts\tPROME\t2026-10-04\tfixture' for p in paths]
        (self.root / 'reads.tsv').write_text(readcap.HDR + '\n' + '\n'.join(rows) + '\n')

    def capture(self, fn, *args, **kwargs):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = fn(*args, **kwargs)
        return rc, out.getvalue()

    def check(self, mode=None):
        args = ['read_cap_check.py', '--agent', 'PROME', '--require-manifest']
        if mode is not None:
            args += ['--charter-mode', mode]
        return self.capture(readcap.main, args)

    def test_explicit_charter_breach_cannot_hide_behind_injection_assumption(self):
        (self.root / 'PROME/CLAUDE.md').write_text('x' * (readcap.BUDGET_BYTES + 1))
        for mode, expected_rc, count in [('explicit', 1, 3), ('injected', 0, 1), (None, 0, 1)]:
            with self.subTest(mode=mode):
                rc, out = self.check(mode)
                self.assertEqual(rc, expected_rc)
                self.assertIn(f'reads={count}', out.splitlines()[-1])
                self.assertIn(f'charter_mode={mode or "unspecified"}', out)
                if mode is None:
                    self.assertIn('injection UNCONFIRMED', out)
                else:
                    self.assertEqual(gate.summarize_read_cap(out, rc, mode)[0], mode == 'injected')

    def test_root_charter_assessed_and_overlap_counted_once(self):
        self.manifest(('PROME/BOOT.md', 'PROME/CLAUDE.md', 'CLAUDE.md'))
        (self.root / 'CLAUDE.md').write_text('x' * (readcap.CAP_BYTES + 1))
        rc, out = self.check('explicit')
        self.assertEqual(rc, 1)
        line = out.splitlines()[-1]
        self.assertIn('reads=3 ', line)
        self.assertIn('over_cap=1 ', line)
        self.assertIn('charter_reads=2 ', line)

    def test_runtime_overlay_promotes_scoped_charter_without_contradictory_exclusion(self):
        self.manifest(('PROME/BOOT.md', 'PROME/CLAUDE.md'))
        manifest = self.root / 'reads.tsv'
        manifest.write_text(manifest.read_text().replace('PROME/CLAUDE.md\twhole', 'PROME/CLAUDE.md\tscoped'))
        rc, out = self.check('explicit')
        self.assertEqual(rc, 0)
        self.assertIn('reads=3 ', out.splitlines()[-1])
        self.assertNotIn('declared `scoped` — not cap-bearing', out)

    def test_charter_path_aliases_count_once_in_whole_and_scoped_overlaps(self):
        for mode in ('whole', 'scoped'):
            with self.subTest(mode=mode):
                self.manifest(('./PROME/CLAUDE.md', 'PROME/../CLAUDE.md', 'PROME/CLAUDE.md'))
                manifest = self.root / 'reads.tsv'
                manifest.write_text(manifest.read_text().replace('\twhole\t', f'\t{mode}\t'))
                rc, out = self.check('explicit')
                self.assertEqual(rc, 0)
                self.assertIn('reads=2 ', out.splitlines()[-1])
                self.assertIn('charter_reads=2 ', out.splitlines()[-1])
                self.assertNotIn('not cap-bearing, not counted', out)

    def test_absent_and_unreadable_charter_with_successful_stat_are_unknown(self):
        local = self.root / 'PROME/CLAUDE.md'
        local.unlink()
        self.assertEqual(self.check('explicit')[0], 2)
        local.write_text('exists')
        original = open
        def deny(path, *args, **kwargs):
            if Path(path) == local:
                raise PermissionError('fixture read denied despite stat')
            return original(path, *args, **kwargs)
        with patch('builtins.open', side_effect=deny):
            rc, out = self.check('explicit')
        self.assertEqual(rc, 2)
        self.assertIn('assessed=0', out)
        self.assertFalse(gate.summarize_read_cap(out, rc, 'explicit')[0])

    def test_manifest_defects_and_missing_attestation_are_not_overridden(self):
        self.manifest(('PROME/BOOT.md', 'absent.md'))
        rc, out = self.check('explicit')
        self.assertEqual(rc, 1)
        self.assertIn('manifest_defects=1', out)
        self.manifest(attested=False)
        self.assertEqual(self.check('explicit')[0], 2)

    def test_default_other_desk_grade_is_unchanged_and_explicit_is_owner_scoped(self):
        desk = self.root / 'AGENTS/ALPHA'
        desk.mkdir(parents=True)
        (desk / 'CLAUDE.md').write_text('x' * (readcap.BUDGET_BYTES + 1))
        (self.root / 'reads.tsv').write_text((self.root / 'reads.tsv').read_text().replace('PROME', 'ALPHA').replace('ALPHA/BOOT.md', 'PROME/BOOT.md'))
        for mode, rc in [('unspecified', 0), ('injected', 0), ('explicit', 1)]:
            result, _ = self.capture(readcap.check_agent, 'ALPHA', charter_mode=mode)
            self.assertEqual(result[0], rc)

    def test_invalid_modes_and_gate_coverage_mismatch_fail_closed(self):
        for args in (['--agent', 'PROME', '--charter-mode'],
                     ['--agent', 'PROME', '--charter-mode', 'maybe'],
                     ['--agent', 'PROME', '--charter-mode', 'injected', '--charter-mode', 'explicit'],
                     ['--fleet', '--charter-mode', 'explicit']):
            self.assertEqual(self.capture(readcap.main, ['check'] + args)[0], 2)
        rc, out = self.check('explicit')
        for bad in (out.replace('charter_mode=explicit', 'charter_mode=injected'),
                    out.replace('charter_reads=2', 'charter_reads=0'),
                    out.replace('charter_mode=explicit', '')):
            with self.assertRaises(ValueError):
                gate.summarize_read_cap(bad, rc, 'explicit')
        with patch.object(gate, 'run_script') as run, patch.object(gate, 'guard'):
            gate.check_byte_budgets()
            self.assertEqual(run.call_args.args[2][-2:], ['--charter-mode', 'explicit'])

    def test_runner_records_modes_retry_does_not_regrade_and_refresh_is_separate(self):
        run = self.root / 'run'
        child = subprocess.CompletedProcess([], 0)
        with patch.object(session.subprocess, 'run', return_value=child) as execute:
            self.assertEqual(self.capture(session.run_once, run, charter_mode='injected')[0], 0)
            self.assertEqual(execute.call_args.args[0][-2:], ['--charter-mode', 'injected'])
        saved = (run / 'completed.json').read_bytes()
        with patch.object(session.subprocess, 'run') as execute:
            rc, out = self.capture(session.run_once, run, charter_mode='explicit')
            self.assertEqual(rc, 0)
            execute.assert_not_called()
            self.assertIn('charter_mode=injected', out)
            self.assertIn('requested explicit', out)
        with patch.object(session.subprocess, 'run', return_value=child) as execute:
            self.assertEqual(self.capture(session.run_refresh, run)[0], 0)
            self.assertEqual(execute.call_args.args[0][-2:], ['--charter-mode', 'explicit'])
        self.assertEqual((run / 'completed.json').read_bytes(), saved)
        fresh = next(run.glob('refresh-*/completed.json'))
        receipt = json.loads(fresh.read_text())
        self.assertEqual(receipt['charter_mode'], 'explicit')
        self.assertFalse(receipt['board_advance'])

    def test_old_receipt_coverage_is_unknown_without_rerun(self):
        run = self.root / 'old'
        with patch.object(session.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0)):
            self.capture(session.run_once, run)
        p = run / 'completed.json'
        receipt = json.loads(p.read_text()); receipt.pop('charter_mode'); p.write_text(json.dumps(receipt))
        with patch.object(session.subprocess, 'run') as execute:
            rc, out = self.capture(session.run_once, run)
            execute.assert_not_called()
        self.assertEqual(rc, 0)
        self.assertIn('charter_mode=UNKNOWN', out)

if __name__ == '__main__':
    unittest.main()
