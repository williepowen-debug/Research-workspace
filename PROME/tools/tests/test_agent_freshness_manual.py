"""Manual-session output against a disposable roster and mocked activity."""
import contextlib
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import subprocess

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'PROME/tools'))

import agent_freshness as af

ROSTER = '''## ACTIVE
| BOND | domain |
## CLASSIFICATION PENDING — not a class, a deliberate hold (1)
- **CATO** — classification pending. Will-directed manual Codex/Astra reviewer. Excluded from automatic launch and signal routing.
## OTHER
'''


class ManualFreshness(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)
        (self.root / 'PROME').mkdir()
        (self.root / 'PROME/ROSTER.md').write_text(ROSTER)
        for name in ['CATO', 'BOND']:
            (self.root / 'AGENTS' / name).mkdir(parents=True)
        self.data = {n: dict(name=n, age_state='aged', age=50.0, inbox=[],
                            to_prome=[], dirty=[]) for n in ['CATO', 'BOND']}

    def run_cli(self, *args):
        out = io.StringIO()
        with patch.object(af, 'ROOT', self.root), patch.object(af, 'AGENTS', self.root/'AGENTS'), \
             patch.object(af, 'row', side_effect=lambda n: self.data[n]), \
             patch.object(sys, 'argv', ['agent_freshness.py', *args]), contextlib.redirect_stdout(out):
            rc = af.main()
        return rc, out.getvalue()

    def test_default_manual_mail_visible_without_launch_cues(self):
        self.data['CATO']['to_prome'] = ['packet']
        rc, out = self.run_cli()
        line = next(l for l in out.splitlines() if l.startswith('CATO'))
        self.assertIn('manual', line.lower())
        self.assertNotIn('DRAIN-FIRST', line)
        self.assertNotIn('STALE', line)
        self.assertEqual(rc, 0)

    def test_all_keeps_manual_never_and_dirty_information_without_fleet_flags(self):
        self.data['CATO'].update(age_state='never', age=None, dirty=[' M local'])
        _, out = self.run_cli('--all')
        line = next(l for l in out.splitlines() if l.startswith('CATO'))
        self.assertIn('never', line)
        self.assertIn('manual', line.lower())
        self.assertIn('uncommitted', line.lower())
        self.assertNotIn('NEVER-COMMITTED', line)
        self.assertNotIn('ORPHANED', line)

    def test_direct_clean_manual_query_is_not_launch_clearance(self):
        rc, out = self.run_cli('--agent', 'CATO')
        self.assertEqual(rc, 0)
        self.assertIn('manual', out.lower())
        self.assertNotIn('clear to brief', out)
        self.assertIn('no launch authorization', out.lower())

    def test_direct_manual_unknown_work_is_not_clean(self):
        self.data['CATO']['dirty'] = af.UNKNOWN
        rc, out = self.run_cli('--agent', 'CATO')
        self.assertEqual(rc, 1)
        self.assertIn('UNKNOWN', out)
        self.assertNotIn('clear to brief', out)

    def test_manual_mail_still_blocks_gate_for_inspection(self):
        self.data['CATO']['to_prome'] = ['packet']
        rc, out = self.run_cli('--gate')
        self.assertEqual(rc, 1)
        self.assertIn('CATO', out)
        self.assertIn('manual', out.lower())
        self.assertNotIn('briefing/spawning those agents', out)

    def test_mixed_gate_mail_separates_domain_and_manual(self):
        for name in self.data:
            self.data[name]['to_prome'] = ['packet']
        rc, out = self.run_cli('--gate')
        self.assertEqual(rc, 1)
        domain = next(l for l in out.splitlines() if 'briefing/spawning' in l)
        self.assertIn('BOND', domain)
        self.assertNotIn('CATO', domain)

    def test_domain_behavior_retains_clearance_and_flags(self):
        rc, out = self.run_cli('--agent', 'BOND')
        self.assertEqual(rc, 0)
        self.assertIn('clear to brief', out)
        self.data['BOND']['to_prome'] = ['packet']
        _, out = self.run_cli('--all')
        line = next(l for l in out.splitlines() if l.startswith('BOND'))
        self.assertIn('STALE', line)
        self.assertIn('DRAIN-FIRST', line)

    def test_missing_roster_never_returns_clearance(self):
        (self.root / 'PROME/ROSTER.md').unlink()
        rc, out = self.run_cli('--agent', 'BOND')
        self.assertEqual(rc, 2)
        self.assertIn('CANNOT-EVALUATE', out)
        self.assertNotIn('clear to brief', out)

    def test_missing_declaration_never_silently_classifies_as_domain(self):
        (self.root / 'PROME/ROSTER.md').write_text(ROSTER.replace('Excluded from automatic launch and signal routing.', ''))
        rc, out = self.run_cli('--agent', 'CATO')
        self.assertEqual(rc, 2)
        self.assertNotIn('clear to brief', out)

    def test_duplicate_entry_is_ambiguous(self):
        (self.root / 'PROME/ROSTER.md').write_text(ROSTER.replace('## OTHER', '- **CATO** — Excluded from automatic launch and signal routing.\n## OTHER'))
        self.assertEqual(self.run_cli('--gate')[0], 2)

    def test_declared_empty_section_and_missing_section_differ(self):
        p = self.root / 'PROME/ROSTER.md'
        p.write_text('## CLASSIFICATION PENDING (0)\n## OTHER\n')
        self.assertEqual(self.run_cli('--agent', 'BOND')[0], 0)
        p.write_text('## OTHER\n')
        self.assertEqual(self.run_cli('--agent', 'BOND')[0], 2)

    def test_zero_count_with_manual_row_is_not_empty(self):
        (self.root/'PROME/ROSTER.md').write_text(ROSTER.replace('(1)', '(0)'))
        self.assertEqual(self.run_cli('--agent', 'CATO')[0], 2)

    def test_duplicate_section_is_not_first_match_wins(self):
        (self.root/'PROME/ROSTER.md').write_text(ROSTER + '\n## CLASSIFICATION PENDING (0)\n')
        self.assertEqual(self.run_cli('--gate')[0], 2)

    def test_unsupported_bullets_cannot_hide_manual_rows_in_empty_section(self):
        for bullet in ['  - ', '\t- ', '* ', '+ ', '1. ', '1) ']:
            with self.subTest(bullet=bullet):
                (self.root/'PROME/ROSTER.md').write_text(
                    '## CLASSIFICATION PENDING (0)\n' + bullet +
                    '**CATO** — Excluded from automatic launch and signal routing.\n## OTHER\n')
                rc, out = self.run_cli('--agent', 'CATO')
                self.assertEqual(rc, 2)
                self.assertIn('CANNOT-EVALUATE', out)
                self.assertNotIn('clear to brief', out)

    def test_one_roster_snapshot_is_used_during_concurrent_change(self):
        def change_after_classification(name):
            (self.root/'PROME/ROSTER.md').write_text('## CLASSIFICATION PENDING (0)\n')
            return self.data[name]
        out = io.StringIO()
        with patch.object(af, 'ROOT', self.root), patch.object(af, 'AGENTS', self.root/'AGENTS'), \
             patch.object(af, 'row', side_effect=change_after_classification), \
             patch.object(sys, 'argv', ['agent_freshness.py', '--all']), contextlib.redirect_stdout(out):
            self.assertEqual(af.main(), 0)
        line = next(l for l in out.getvalue().splitlines() if l.startswith('CATO'))
        self.assertIn('manual', line.lower())


if __name__ == '__main__':
    unittest.main()
