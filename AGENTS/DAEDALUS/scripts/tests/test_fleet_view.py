"""WQ-655 behavioral neighbours, with real temporary Git history."""
import datetime as dt
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location('fleet_view', Path(__file__).parents[1] / 'fleet_view.py')
fv = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(fv)
NOW = dt.datetime(2026, 11, 9, 20, tzinfo=dt.timezone.utc)


class FleetView(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.run_git('init', '-q')
        self.run_git('config', 'user.email', 'test@example.invalid')
        self.run_git('config', 'user.name', 'test')
        self.write('PROME/ROSTER.md', '## ACTIVE\n| Agent | Domain |\n| AAA | Test |\n## TIER-2\n## DORMANT\n## RETIRED\n## SPECIAL\n**PROME** — coordinator\n')
        self.write('PROME/DOCKET.tsv', '2026-11-09\tTask\tAAA\tPENDING\t\t\n')
        self.write('PROME/GATES.tsv', 'gate_id\tregistered\towner\tcondition\tconsequence_on_fire\tstate\tlast_checked\tsource\tconsumed_by\treview_by\nGATE-AAA-TEST\t2026-11-01\tAAA\ttest\ttest\tLIVE\t2026-11-09\ttest\t\t2026-11-09\n')
        self.write('PROME/state/ORCH_LOG.tsv', '\t'.join(fv.orch_log.COLS)+'\n')
        self.write('AGENTS/AAA/STATUS.md', 'test\n')
        self.write('AGENTS/AAA/inbox/README.md', '# Readme\n')
        self.write('PROME/inbox/.gitkeep', '')
        self.commit('AAA: fixture')

    def write(self, path, text):
        target = self.root/path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)

    def run_git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.root), *args], stderr=subprocess.STDOUT).decode()

    def commit(self, subject):
        self.run_git('add', '.')  # isolated fixture repo only
        self.run_git('commit', '-qm', subject)

    def collect(self, inv=None):
        return fv.collect(self.root, NOW, inv or (lambda: {'coverage': 'fixture only', 'observed_at': NOW.isoformat(), 'processes': [], 'error': 'unavailable'}))

    def test_scaffold_only_and_one_collection_two_views(self):
        self.write('AGENTS/AAA/inbox/PROTOCOL.md', '# Mail Processing Protocol\n')
        self.write('AGENTS/AAA/inbox/RECEIPT.md', '# Inbox Processing Receipt — today\n')
        data = self.collect()
        self.assertEqual([], data['desks']['AAA']['inbox'])
        self.assertEqual([], data['returns'])
        self.assertIn('No matches in checked inputs', fv.render(data))
        self.assertNotIn('Full roster', fv.render(data))
        self.assertIn('Full roster', fv.render(data, True))
        self.assertEqual(2, len(data['due']))

    def test_committed_return_remains_presence(self):
        self.write('PROME/inbox/2026-11-09_from-AAA_test.md', 'D:L1 result\n')
        self.commit('AAA: D:L1 return')
        data = self.collect()
        self.assertEqual(1, len(data['returns']))
        self.assertIn('RETURN FOUND', data['due'][0]['message'])
        self.assertIn('never completion', data['due'][0]['message'])

    def test_trim_preserves_details_and_unknowns(self):
        self.write('PROME/DOCKET.tsv',
                   '2026-11-09\tTask\tAAA\tPENDING (COVERED: test)\t\t\n'
                   'TBD\tUndated one\tAAA\tPENDING\t\t\n'
                   'TBD\tUndated two\tAAA\tPENDING\t\t\n')
        self.write('AGENTS/AAA/inbox/one.md', 'one')
        self.write('AGENTS/AAA/inbox/WALTER/two.md', 'two')
        data = self.collect()
        # Controlled ORCH records isolate display aggregation from ledger matching.
        for n in (2, 3):
            data['unknown'].append(dict(stamp=NOW.isoformat(),
                message=f'AAA: unreconciled ORCH in-flight claim, event 2026-11-09/{n}; actual activity UNKNOWN',
                source=f'PROME/state/ORCH_LOG.tsv:{n}'))
        data['due'].append(dict(stamp=NOW.isoformat(),
            message='D:L99 · AAA · covered=True · UNCHECKED (coverage incomplete: UNKNOWN)',
            source='PROME/DOCKET.tsv:99'))
        opening, full = fv.render(data), fv.render(data, True)
        self.assertIn('D:L99', opening)
        self.assertIn('coverage incomplete: UNKNOWN', opening)
        self.assertIn('2 AAA: inbox files present', opening)
        self.assertIn('1 covered due obligations', opening)
        self.assertIn('2 open undated obligations; due dates UNKNOWN', opening)
        self.assertIn('2 unreconciled current/future-day ORCH claims', opening)
        self.assertNotIn('inbox/one.md', opening)
        self.assertIn('inbox/one.md', full)
        self.assertIn('inbox/WALTER/two.md', full)
        self.assertIn('PROME/DOCKET.tsv:2', full)
        self.assertIn('PROME/state/ORCH_LOG.tsv:3', full)
        for r in fv.opening_rows(data, 'returns'):
            self.assertTrue(r['stamp'])
            self.assertEqual('AGENTS/AAA/inbox/', r['source'])
        for text in (opening, full):
            self.assertNotIn('pending consumption', text.lower())
            self.assertNotIn('pending candidates', text.lower())
            self.assertNotIn('unread', text.lower())
            self.assertNotIn('unconsumed', text.lower())
            self.assertNotIn('unfinished', text.lower())
            self.assertIn('Current turn activity UNKNOWN', text)

    def test_named_protocol_scaffolds_and_unknown_protocol(self):
        for name in ('CYPHER', 'FLG', 'GIBBS', 'ISHM'):
            path = self.root/f'AGENTS/{name}/inbox/PROTOCOL.md'
            self.write(str(path.relative_to(self.root)), f'# {name} — INBOX PROTOCOL\n')
            self.assertTrue(fv.scaffold(path))
        self.write('AGENTS/AAA/inbox/PROTOCOL.md', '# A new protocol request\n')
        self.assertFalse(fv.scaffold(self.root/'AGENTS/AAA/inbox/PROTOCOL.md'))

    def test_wrong_owner_prefix_never_becomes_owned_work(self):
        self.write('AGENTS/BBB/STATUS.md', 'other\n')
        self.commit('AAA: foreign only')
        history = fv.commits(self.root, 'HEAD')
        self.assertNotEqual(history[0]['sha'], fv.attribution('AAA', history)['sha'])
        self.assertIsNone(fv.attribution('BBB', history))

    def test_missing_and_malformed_are_unknown(self):
        (self.root/'PROME/GATES.tsv').unlink()
        (self.root/'AGENTS/AAA/inbox/README.md').unlink()
        (self.root/'AGENTS/AAA/inbox').rmdir()
        data = self.collect()
        text = fv.render(data)
        self.assertIn('GATES UNKNOWN', text)
        self.assertIn('AAA: inbox UNKNOWN', text)
        self.write('PROME/DOCKET.tsv', '2026-11-09\tbroken\n')
        self.assertIn('DOCKET UNKNOWN', fv.render(self.collect()))

    def test_real_packet_named_receipt_not_hidden(self):
        self.write('AGENTS/AAA/inbox/RECEIPT.md', '# A request from a colleague\n')
        self.assertEqual(1, len(self.collect()['returns']))

    def test_sessions_are_observation_not_activity_and_concurrency_visible(self):
        def inventory():
            self.write('PROME/DOCKET.tsv', '2026-11-10\tTask\tAAA\tPENDING\t\t\n')
            return {'coverage': 'visible processes only', 'observed_at': NOW.isoformat(), 'processes': [{'runtime': 'codex', 'cwd': str(self.root/'AGENTS/AAA')}]}
        data = self.collect(inventory)
        text = fv.render(data, True)
        self.assertIn('codex process observed', text)
        self.assertIn('current activity UNKNOWN', text)
        self.assertIn('Source changed during collection', text)

    def test_output_symlink_cannot_overwrite_ledger(self):
        output = self.root/'PROME/state/FLEET.md'
        ledger = self.root/'PROME/state/ORCH_LOG.tsv'
        before = ledger.read_bytes()
        output.symlink_to(ledger)
        with self.assertRaises(ValueError):
            fv.write_output(output, 'corruption', self.root)
        self.assertEqual(before, ledger.read_bytes())

    def test_foreign_only_citation_discloses_unknown_ownership(self):
        self.write('AGENTS/BBB/STATUS.md', 'foreign work')
        self.commit('AAA: D:L1 done')
        text = fv.render(self.collect())
        self.assertIn('RETURN FOUND; first-owner prefix-based citation; owned-work attribution UNKNOWN', text)

    def test_no_source_writes(self):
        before = {str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file() and '.git' not in p.parts}
        self.collect()
        after = {str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file() and '.git' not in p.parts}
        self.assertEqual(before, after)

    def test_foreign_inbox_rename_with_arrow_subject(self):
        self.write('AGENTS/BBB/inbox/packet.md', 'packet\n')
        self.commit('BBB: packet')
        (self.root/'AGENTS/BBB/inbox/processed').mkdir()
        self.run_git('mv', 'AGENTS/BBB/inbox/packet.md', 'AGENTS/BBB/inbox/processed/packet.md')
        self.commit('AAA -> BBB: swept rename')
        data = self.collect()
        self.assertTrue(any('AAA: foreign-desk rename' in r['message'] for r in data['conflicts']))


if __name__ == '__main__':
    unittest.main()
