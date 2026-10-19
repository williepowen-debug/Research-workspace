"""Delivery B: real disposable Git repositories, no production state writes."""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import argus_scope as sc
import argus_contract as ac


class ContractTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.patch = patch.object(sc, 'ROOT', self.root)
        self.patch.start(); self.addCleanup(self.patch.stop)
        self.git('init', '-q', '-b', 'master')
        self.git('config', 'user.email', 'fixture@example.test')
        self.git('config', 'user.name', 'fixture')
        self.write('OWNER.md', 'OTTO owns the unrelated analysis and no PROME claim relies on it.\n')
        self.write('PROME/old', 'baseline')
        self.base = self.commit('OWNER.md', 'PROME/old')
        (self.root / 'PROME/state').mkdir()
        sc.record_baseline(self.base)
        self.write('PROME/result', 'reviewed result')
        self.plan = {'delivered': {'PROME/result': 'PROME authored this bounded repair'},
                     'evidence': [], 'observed': {}}

    def git(self, *args):
        return subprocess.run(['git', *args], cwd=self.root, check=True,
                              capture_output=True, text=True).stdout.strip()

    def write(self, path, value):
        target = self.root / path; target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(value)

    def commit(self, *paths):
        self.git('add', '--', *paths)
        self.git('commit', '-qm', 'fixture change', '--', *paths)
        return self.git('rev-parse', 'HEAD')

    def unrelated(self):
        return {'owner': 'OTTO', 'reason': 'Independent analysis, not used by delivery',
                'basis': {'path': 'OWNER.md', 'commit': self.base},
                'quote': 'OTTO owns the unrelated analysis', 'not_relied_on': True}

    def freeze(self):
        return ac.freeze(sc, self.plan)

    def manifest(self):
        return json.loads((self.root / sc.REVIEW_FILE).read_text())

    def save(self, d):
        (self.root / sc.REVIEW_FILE).write_text(json.dumps(d))

    def test_unrelated_pending_does_not_block_named_delivery_or_promotion(self):
        path = 'AGENTS/BROCK/inbox/foreign'
        self.write(path, 'unrelated')
        self.plan['observed'][path] = self.unrelated()
        d = self.freeze()
        self.assertIn(path, d['inventory'])
        self.assertEqual(sc.mark_reviewed('independent fixture verdict')[0], 0)
        a = self.commit('PROME/result')
        self.assertEqual(sc.verify_review(paths=['PROME/result'], ref=a)[0], 0)

    def test_unrelated_churn_is_explicit_and_preserves_review_contract(self):
        self.freeze(); self.assertEqual(sc.mark_reviewed()[0], 0)
        before = self.manifest()
        self.write('PROME/foreign', 'new unrelated packet')
        self.assertEqual(sc.verify_review()[0], 1)
        ac.observe(sc, {'PROME/foreign': self.unrelated()})
        self.assertEqual(sc.verify_review()[0], 0)
        self.write('PROME/foreign', 'changed packet')
        self.assertEqual(sc.verify_review()[0], 1)
        ac.observe(sc, {'PROME/foreign': self.unrelated()})
        after = self.manifest()
        self.assertEqual(before['contract_sha256'], after['contract_sha256'])
        self.assertEqual(after['verdict'], sc.REVIEWED)
        self.assertEqual(len(after['observed']['PROME/foreign']), 2)

    def test_new_nested_delivery_not_hidden_and_explicit_paths_do_not_hide_it(self):
        self.freeze()
        self.write('AGENTS/RED/inbox/data/prome', 'new delivery')
        self.assertEqual(sc.verify_review(paths=['PROME/result'])[0], 1)
        a = self.commit('PROME/result', 'AGENTS/RED/inbox/data/prome')
        self.assertEqual(sc.verify_review(paths=['PROME/result'], ref=a)[0], 1)

    def test_committed_and_pending_versions_and_deletion(self):
        earlier = self.commit('PROME/result')
        self.write('PROME/result', 'latest reviewed')
        (self.root / 'PROME/old').unlink()
        self.plan['delivered']['PROME/old'] = 'PROME intentionally retired this file'
        d = self.freeze()
        self.assertIn(earlier, d['contract']['delivered']['PROME/result']['versions'])
        self.assertIsNone(d['paths']['PROME/old'])
        a = self.commit('PROME/result', 'PROME/old')
        self.assertEqual(sc.verify_review(ref=a)[0], 0)

    def test_evidence_must_be_persisted_and_name_delivered_claim(self):
        self.write('PROME/source', 'not committed')
        self.plan['evidence'] = [{'path': 'PROME/source', 'commit': self.base, 'mode': 'current',
                                  'claims': {'PROME/result': 'supports result'}}]
        with self.assertRaises(ValueError): self.freeze()
        sha = self.commit('PROME/source')
        self.plan['evidence'][0]['commit'] = sha
        self.freeze()
        self.assertEqual(sc.verify_review()[0], 0)
        self.write('PROME/source', 'changed')
        self.assertEqual(sc.verify_review()[0], 1)

    def test_historical_evidence_survives_live_edit_but_current_does_not(self):
        self.plan['evidence'] = [{'path': 'OWNER.md', 'commit': self.base, 'mode': 'historical',
                                  'claims': {'PROME/result': 'dated quote only'}}]
        self.freeze()
        self.write('OWNER.md', 'new owner state')
        self.assertEqual(sc.verify_review()[0], 1)
        ac.observe(sc, {'OWNER.md': self.unrelated()})
        self.assertEqual(sc.verify_review()[0], 0)
        self.plan['evidence'][0]['mode'] = 'current'
        with self.assertRaises(ValueError): self.freeze()

    def test_delivery_and_evidence_both_enforced(self):
        sha = self.commit('PROME/result')
        self.plan['evidence'] = [{'path': 'PROME/result', 'commit': sha, 'mode': 'current',
                                  'claims': {'PROME/result': 'self-contained persisted evidence'}}]
        self.freeze()
        self.assertEqual(sc.verify_review()[0], 0)
        self.write('PROME/result', 'different')
        rc, lines = sc.verify_review()
        self.assertEqual(rc, 1); self.assertEqual(len(lines), 2)

    def test_empty_missing_malformed_and_role_tampering_fail_closed(self):
        self.freeze()
        self.assertEqual(sc.verify_review(paths=[])[0], 2)
        sc.mark_reviewed()
        original = self.manifest()
        d = copy.deepcopy(original)
        d['contract']['delivered']['PROME/result']['provenance'] = 'different roles'
        d['contract_sha256'] = ac.digest(d['contract'])
        self.save(d)
        self.assertEqual(sc.verify_review()[0], 2)
        self.save(original)
        (self.root / sc.BASELINE_FILE).unlink()
        self.assertEqual(sc.verify_review(paths=['PROME/result'])[0], 2)
        self.assertEqual(sc.mark_reviewed()[0], 2)

    def test_observed_cannot_replace_delivery_or_used_evidence(self):
        self.freeze()
        with self.assertRaises(ValueError): ac.observe(sc, {'PROME/result': self.unrelated()})
        self.write('AGENTS/OTTO/new', 'other')
        bad = self.unrelated(); bad['quote'] = 'absent quote'
        with self.assertRaises(ValueError): ac.observe(sc, {'AGENTS/OTTO/new': bad})
        bad = self.unrelated(); bad['owner'] = 'PROME'
        with self.assertRaises(ValueError): ac.observe(sc, {'AGENTS/OTTO/new': bad})

    def test_actual_commit_path_cannot_be_laundered_as_observed(self):
        self.write('PROME/foreign', 'unrelated')
        self.plan['observed']['PROME/foreign'] = self.unrelated()
        self.freeze()
        a = self.commit('PROME/result', 'PROME/foreign')
        ac.observe(sc, {'PROME/foreign': self.unrelated()})
        rc, lines = sc.verify_review(ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1)
        self.assertTrue(any('ACTUAL COMMIT' in s for s in lines))

    def test_named_delivery_and_later_snapshot_are_distinct(self):
        self.freeze(); sc.mark_reviewed()
        a = self.commit('PROME/result')
        self.write('PROME/foreign', 'concurrent owner')
        p = self.commit('PROME/foreign')
        ac.observe(sc, {'PROME/foreign': self.unrelated()})
        self.assertEqual(sc.verify_review(ref=a)[0], 0)
        self.assertEqual(sc.verify_review(ref=a, snapshot=p)[0], 0)
        self.write('PROME/result', 'changed after pre-push comparison')
        q = self.commit('PROME/result')
        self.assertEqual(sc.verify_review(ref=a)[0], 0)
        self.assertEqual(sc.verify_review(ref=a, snapshot=q)[0], 1)

    def test_named_ref_resolves_once(self):
        self.freeze(); a = self.commit('PROME/result')
        calls = []
        original = ac.resolve
        def capture(scope, ref):
            calls.append(ref)
            return original(scope, ref)
        self.git('tag', 'delivery', a)
        with patch.object(ac, 'resolve', side_effect=capture):
            self.assertEqual(sc.verify_review(ref='delivery')[0], 0)
        self.assertEqual(calls.count('delivery'), 1)

    def test_legacy_manifest_stays_strict(self):
        self.write('PROME/foreign', 'unrelated')
        sc.record_review(['PROME/result', 'PROME/foreign'])
        a = self.commit('PROME/result')
        self.assertEqual(sc.verify_review(paths=['PROME/result'], ref=a)[0], 1)

    def test_reader_ce1_historical_dependency_never_exempts_an_unclassified_version(self):
        self.plan['evidence'] = [{'path': 'OWNER.md', 'commit': self.base, 'mode': 'historical',
                                  'claims': {'PROME/result': 'dated quote'}}]
        self.write('OWNER.md', 'unknown replacement')
        with self.assertRaises(ValueError): self.freeze()
        self.plan['observed']['OWNER.md'] = self.unrelated()
        self.freeze()
        (self.root / 'OWNER.md').unlink()
        self.assertEqual(sc.verify_review()[0], 1)
        ac.observe(sc, {'OWNER.md': self.unrelated()})
        self.assertEqual(sc.verify_review()[0], 0)
        self.write('AGENTS/OTTO/moved-source', 'moved version')
        self.assertEqual(sc.verify_review()[0], 1)
        ac.observe(sc, {'AGENTS/OTTO/moved-source': self.unrelated()})
        self.assertEqual(sc.verify_review()[0], 0)

    def test_reader_ce2_remote_only_observation_cannot_skip_schema_and_attribution(self):
        self.freeze(); a = self.commit('PROME/result')
        self.git('switch', '-qc', 'remote-snapshot')
        path = 'AGENTS/OTTO/remote-only'
        self.write(path, 'remote bytes'); p = self.commit(path)
        self.git('switch', '-q', 'master')
        d = self.manifest()
        d['observed'][path] = [{'snapshot': {'commit_sha256': sc._committed_content_id(path, p)}}]
        self.save(d)
        self.assertEqual(sc.verify_review(ref=a, snapshot=p)[0], 2)
        d['observed'] = {}; self.save(d)
        ac.observe(sc, {path: self.unrelated()}, ref=p)
        self.assertEqual(sc.verify_review(ref=a, snapshot=p)[0], 0)


if __name__ == '__main__':
    unittest.main()
