"""Author counterexamples for the prospective collector, in isolated Git repos."""
import copy
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('capture', Path(__file__).with_name('collect.py'))
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)
PATH = 'AGENTS/EXAMPLE/workbook/PREDICTIONS.tsv'
HEADER = 'ID\tPrediction\tConfidence\tStatus\n'


class CaptureTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        self.run_git('init', '-q', '-b', 'main')
        self.run_git('config', 'user.email', 'test@example.invalid')
        self.run_git('config', 'user.name', 'Test')
        self.source = self.repo / PATH
        self.source.parent.mkdir(parents=True)
        self.commit('old\tOld question\t70%\tOPEN\n')
        self.base = self.run_git('rev-parse', 'HEAD').strip()
        self.config = {'baseline_commit': self.base, 'baseline_keys': ['EXAMPLE/old'],
                       'paths': [PATH], 'limit': 20,
                       'enrollment_ends_utc': '2099-01-01T00:00:00+00:00'}

    def run_git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.repo), *args], text=True,
                                       stderr=subprocess.PIPE)

    def commit(self, body):
        self.source.write_text(HEADER + body)
        self.run_git('add', PATH)
        self.run_git('commit', '-qm', 'fixture')
        return self.run_git('rev-parse', 'HEAD').strip()

    def collect(self):
        return m.collect(self.repo, self.config, 'HEAD')

    def test_original_and_question_survive_remark_and_deletion(self):
        self.commit('old\tOld question\t20%\tMISS\nnew\tThreshold A\t65%\tOPEN\n')
        self.commit('old\tOld question\t20%\tMISS\nnew\tThreshold B\t30%\tMISS\n')
        self.commit('old\tOld question\t20%\tMISS\n')
        before = self.source.read_bytes()
        x = self.collect()
        self.assertEqual([r['key'] for r in x['selected']], ['EXAMPLE/new'])
        self.assertEqual(x['selected'][0]['p_original_candidate'], .65)
        self.assertEqual(x['selected'][0]['fields'][1], 'Threshold A')
        self.assertEqual(x['later_versions'][0]['fields'][1], 'Threshold B')
        self.assertTrue(x['later_versions'][1]['deleted_from_observed_path'])
        self.assertEqual(before, self.source.read_bytes())
        self.assertEqual(x, self.collect())

    def test_tie_order_and_cap(self):
        self.config['limit'] = 2
        self.commit('z\tQ\t80%\tOPEN\na\tQ\t20%\tOPEN\nb\tQ\t50%\tOPEN\n')
        self.assertEqual([r['key'] for r in self.collect()['selected']], ['EXAMPLE/a', 'EXAMPLE/b'])

    def test_tier_is_not_odds_or_later_backfill(self):
        self.commit('tier\tQ\tPROVISIONAL\tOPEN\n')
        self.commit('tier\tQ\t90%\tHIT\n')
        x = self.collect()
        self.assertEqual(x['selected'], [])
        self.assertEqual(len(x['nonnumeric_new_rows']), 1)

    def test_ambiguous_confidence_fails(self):
        self.commit('new\tQ\t70-80%\tOPEN\n')
        with self.assertRaisesRegex(ValueError, 'ambiguous numeric'):
            self.collect()

    def test_exact_interpretation_preserves_annotation_and_versions(self):
        commit = self.commit('new\tQ\t50% (carried mark)\tOPEN\n')
        decision = dict(key='EXAMPLE/new', commit=commit,
                        blob=self.run_git('rev-parse', commit + ':' + PATH).strip(),
                        confidence='50% (carried mark)', p=.5,
                        reason='Explicit original percentage', evidence='fixture original')
        self.commit('new\tChanged Q\t70%\tOPEN\n')
        result = m.collect(self.repo, self.config, 'HEAD', [decision])
        self.assertEqual(result['selected'][0]['fields'][2], decision['confidence'])
        self.assertEqual(result['selected'][0]['p_original_candidate'], .5)
        self.assertEqual(result['selected'][0]['probability_interpretation'], decision)
        self.assertEqual(result['later_versions'][0]['fields'][2], '70%')
        for field, value in [('key', 'OTHER/new'), ('commit', self.base),
                             ('blob', 'wrong'), ('confidence', '50% (other)'),
                             ('p', .7), ('evidence', ''), ('reason', '')]:
            with self.subTest(field=field):
                bad = {**decision, field: value}
                with self.assertRaises(ValueError):
                    m.collect(self.repo, self.config, 'HEAD', [bad])
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            m.collect(self.repo, self.config, 'HEAD', [decision, decision])

    def test_unreviewed_annotation_and_range_still_stop(self):
        self.commit('new\tQ\t50% (not reviewed)\tOPEN\n')
        with self.assertRaises(ValueError):
            self.collect()
        commit = self.commit('range\tQ\t50-60%\tOPEN\n')
        decision = dict(key='EXAMPLE/range', commit=commit,
                        blob=self.run_git('rev-parse', commit + ':' + PATH).strip(),
                        confidence='50-60%', p=.5, reason='Invalid choice', evidence='fixture')
        row = dict(key=decision['key'], commit=commit, blob=decision['blob'],
                   header=['confidence'], fields=['50-60%'])
        with self.assertRaises(ValueError):
            m.probability(row, [decision])

    def test_pct_requires_exact_review(self):
        commit = self.commit('new\tQ\t70pct\tOPEN\n')
        with self.assertRaises(ValueError):
            self.collect()
        decision = dict(key='EXAMPLE/new', commit=commit,
                        blob=self.run_git('rev-parse', commit + ':' + PATH).strip(),
                        confidence='70pct', p=.7, reason='pct means percent', evidence='fixture')
        result = m.collect(self.repo, self.config, 'HEAD', [decision])
        self.assertEqual(result['selected'][0]['p_original_candidate'], .7)

    def test_conditional_annotation_preserved_not_repriced(self):
        value = '40% [P(MET | fired); base MET 46 / NOT MET 32 / NV 22]'
        commit = self.commit('new\tConditional Q\t' + value + '\tOPEN\n')
        decision = dict(key='EXAMPLE/new', commit=commit,
                        blob=self.run_git('rev-parse', commit + ':' + PATH).strip(),
                        confidence=value, p=.4, reason='Explicit first mark', evidence='fixture')
        result = m.collect(self.repo, self.config, 'HEAD', [decision])
        self.assertEqual(result['selected'][0]['p_original_candidate'], .4)
        self.assertEqual(result['selected'][0]['fields'][2], value)
        self.assertNotIn('outcome', result['selected'][0])

    def test_malformed_candidate_fails_but_existing_defect_does_not_enroll(self):
        self.commit('old\tOld malformed\nnew\tQ\t60%\tOPEN\n')
        self.assertEqual(len(self.collect()['selected']), 1)
        self.commit('new\tQ\t60%\n')
        with self.assertRaisesRegex(ValueError, 'malformed'):
            self.collect()

    def test_duplicate_id_fails(self):
        self.commit('new\tQ\t60%\tOPEN\nnew\tQ\t40%\tOPEN\n')
        with self.assertRaisesRegex(ValueError, 'duplicate ID'):
            self.collect()

    def test_missing_ledger_fails(self):
        self.run_git('mv', PATH, 'AGENTS/EXAMPLE/workbook/MOVED.tsv')
        self.run_git('commit', '-qm', 'move')
        with self.assertRaises(subprocess.CalledProcessError):
            self.collect()

    def test_cutoff_no_backfilled_enrollment(self):
        self.config['enrollment_ends_utc'] = '2000-01-01T00:00:00+00:00'
        self.commit('new\tQ\t60%\tOPEN\n')
        self.assertEqual(self.collect()['selected'], [])

    def test_merge_fails(self):
        self.run_git('checkout', '-qb', 'side')
        self.commit('side\tQ\t60%\tOPEN\n')
        self.run_git('checkout', '-q', 'main')
        self.run_git('merge', '--no-ff', '-qm', 'merge', 'side')
        with self.assertRaisesRegex(ValueError, 'merge in pilot'):
            self.collect()

    def test_atomic_monotonic_write_and_concurrent_lock(self):
        self.commit('new\tQ\t60%\tOPEN\n')
        path = self.repo / 'capture.json'
        x = self.collect()
        m.write_capture(path, x, self.repo)
        original = path.read_bytes()
        bad = copy.deepcopy(x)
        bad['selected'][0]['p_original_candidate'] = .9
        with self.assertRaises(ValueError):
            m.write_capture(path, bad, self.repo)
        with self.assertRaises(subprocess.CalledProcessError):
            m.write_capture(path, m.collect(self.repo, self.config, self.base), self.repo)
        lock = os.open(self.repo, os.O_RDONLY)
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            with self.assertRaises(BlockingIOError):
                m.write_capture(path, x, self.repo)
        finally:
            os.close(lock)
        self.assertEqual(path.read_bytes(), original)


if __name__ == '__main__':
    unittest.main()
