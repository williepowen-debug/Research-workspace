"""Delivery B: real disposable Git repositories, no production state writes."""
import copy
import hashlib
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


class ContractFixture(unittest.TestCase):
    """Disposable repo + helpers; no tests of its own. The baseline carries NO perimeter file, so every
    ContractTests case runs the strict path (reader 2026-10-24 ⚠️6)."""
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


class ContractTests(ContractFixture):
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


PERIMETER = (sc.ROOT / sc.PERIMETER_FILE).read_text()  # the REAL perimeter, read at import before ROOT is patched
FP = 'FOREIGN-PENDING (advisory, owner UNVERIFIED — {} lane, no PROME evidence): {}'
UNC = 'UNCLASSIFIED: {} (new or changed observed version)'


class PerimeterPinTests(ContractFixture):
    """DOCKET L796 ❌2 — the perimeter is PINNED at the freeze; the live file is never read at verify time.
    Acceptance: ACCEPTANCE_closeout_gate_perimeter_pin_2026-10-24.md (AC1–AC8). The baseline commits the REAL
    PROME/state/AUDIT_PERIMETER.tsv, so the advisory branch is live here (unlike ContractTests)."""
    def setUp(self):
        super().setUp()
        self.write(sc.PERIMETER_FILE, PERIMETER)
        self.write('memory/auto/MEMORY.md', 'idx\n')
        self.git('add', '--', sc.PERIMETER_FILE, 'memory/auto/MEMORY.md')
        self.git('commit', '-qm', 'baseline perimeter', '--', sc.PERIMETER_FILE, 'memory/auto/MEMORY.md')
        self.base = self.git('rev-parse', 'HEAD')
        sc.record_baseline(self.base)

    def perimeter_edit(self, old, new):
        f = self.root / sc.PERIMETER_FILE
        text = f.read_text()
        self.assertIn(old, text)
        f.write_text(text.replace(old, new, 1))

    def foreign_lines(self, lines):
        return [l for l in lines if l.startswith('FOREIGN-PENDING')]

    def test_ac1_freeze_pins_the_loaded_perimeter_outside_the_contract(self):
        self.freeze(); d = self.manifest()
        self.assertEqual([tuple(r) for r in d['perimeter']['rules']], sc.load_perimeter())
        self.assertEqual(d['perimeter']['sha256'],
                         hashlib.sha256((self.root / sc.PERIMETER_FILE).read_bytes()).hexdigest())
        self.assertNotIn('perimeter', d['contract'])
        self.assertEqual(d['contract_sha256'], ac.digest(d['contract']))

    def test_ac2_ce8b_self_exempting_perimeter_edit_blocks_both_paths(self):
        self.freeze()
        self.perimeter_edit('pattern\tclass\treason\n',
                            'pattern\tclass\treason\nPROME/state/AUDIT_PERIMETER.tsv\tEXCLUDED\tx\n'
                            'PROME/state/HANDOFF_X.md\tEXCLUDED\tx\n')
        self.write('PROME/state/HANDOFF_X.md', 'PROME owned post-freeze write\n')
        rc, lines = sc.verify_review()
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format(sc.PERIMETER_FILE), lines)
        self.assertIn(UNC.format('PROME/state/HANDOFF_X.md'), lines)
        self.assertEqual(self.foreign_lines(lines), [])

    def test_ac3_ce8_perimeter_edit_blocks_and_pinned_rules_still_classify(self):
        self.freeze()
        self.perimeter_edit('memory/auto/**\tSHARED', 'memory/auto/**\tEXCLUDED')
        self.write('memory/auto/x.md', 'x')
        rc, lines = sc.verify_review()
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format(sc.PERIMETER_FILE), lines)
        self.assertIn(FP.format('SHARED', 'memory/auto/x.md'), lines)

    def test_ac4_committed_side_is_attributed_by_the_pinned_rules_not_the_live_file(self):
        self.freeze()
        self.write('FORGE/x.md', 'desk wrote\n')
        self.git('add', '--', 'FORGE/x.md'); self.git('commit', '-qm', 'BRENT: forge note', '--', 'FORGE/x.md')
        self.perimeter_edit('FORGE/**\tOWNED', 'FORGE/**\tEXCLUDED')
        rc, lines = sc.verify_review()
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format('FORGE/x.md'), lines)

    def test_ac5a_manifest_without_a_pin_runs_strict(self):
        self.freeze(); d = self.manifest(); del d['perimeter']; self.save(d)
        self.write('AGENTS/BROCK/new.md', 'x')
        rc, lines = sc.verify_review()
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format('AGENTS/BROCK/new.md'), lines)
        self.assertEqual(self.foreign_lines(lines), [])

    def test_ac5b_tampered_pin_cannot_evaluate(self):
        self.freeze(); d = self.manifest(); d['perimeter']['rules'] = [['**', 'BOGUS', 'r']]; self.save(d)
        self.assertEqual(sc.verify_review()[0], 2)
        d['perimeter'] = {'sha256': 'nothex', 'rules': None}; self.save(d)
        self.assertEqual(sc.verify_review()[0], 2)

    def test_ac6_foreign_pending_arrival_stays_advisory_and_names_its_lane(self):
        self.freeze(); self.write('AGENTS/BROCK/new.md', 'x')
        rc, lines = sc.verify_review()
        self.assertEqual(rc, 0, lines)
        self.assertIn(FP.format('EXCLUDED', 'AGENTS/BROCK/new.md'), lines)

    def test_ac6b_ce7_corrupted_live_perimeter_blocks_on_the_perimeter_file_itself(self):
        self.freeze(); self.write('AGENTS/BROCK/new.md', 'x')
        (self.root / sc.PERIMETER_FILE).write_text('pattern\tclass\treason\nfoo\tBOGUS\tr\n')
        rc, lines = sc.verify_review()
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format(sc.PERIMETER_FILE), lines)
        self.assertIn(FP.format('EXCLUDED', 'AGENTS/BROCK/new.md'), lines)

    def test_ac7_ce5_rename_out_of_the_owned_lane_blocks(self):
        self.freeze()
        (self.root / 'AGENTS/ZED').mkdir(parents=True)
        self.git('mv', 'PROME/old', 'AGENTS/ZED/old')
        rc, lines = sc.verify_review()
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format('PROME/old'), lines)

    def test_ac8_ce2_prome_writes_in_other_lanes_are_advisory_and_labelled_by_lane(self):
        self.freeze()
        paths = {'memory/auto/finding_prome_new_lesson.md': 'SHARED',
                 'AGENTS/FALCON/inbox/data/2026-10-24_FIRMS.csv': 'SHARED',
                 'NEWROOTFILE.md': 'UNATTRIBUTED',
                 'PROME/inbox/processed/2026-10-24_from-WALTER_x.md': 'EXCLUDED'}
        for path in paths:
            self.write(path, 'PROME wrote this after the freeze\n')
        rc, lines = sc.verify_review()
        self.assertEqual(rc, 0, lines)
        self.assertEqual(sorted(self.foreign_lines(lines)), sorted(FP.format(l, p) for p, l in paths.items()))

    # --- reader 10/24 (second read, L796 ❌2 repair): ported counterexamples CE-C1 · CE-O · CE-G1 · CE-S10 ---

    def test_x1_ce_c1_perimeter_changed_before_the_freeze_must_be_delivered_never_attributed(self):
        self.perimeter_edit('pattern\tclass\treason\n',
                            'pattern\tclass\treason\nPROME/state/AUDIT_PERIMETER.tsv\tSHARED\tx\n')
        self.git('add', '--', sc.PERIMETER_FILE)
        self.git('commit', '-qm', 'BRENT: tidy', '--', sc.PERIMETER_FILE)   # a non-PROME subject, committed-only
        with self.assertRaises(ValueError) as cm:
            self.freeze()
        self.assertIn('deliver it', str(cm.exception))
        self.plan['delivered'][sc.PERIMETER_FILE] = 'PROME perimeter row'
        self.freeze(); d = self.manifest()
        self.assertEqual([tuple(r) for r in d['perimeter']['rules']], sc.load_perimeter())
        self.assertNotIn(sc.PERIMETER_FILE, d['attributed_by_commit'])

    def test_x1b_ce_o_perimeter_cannot_be_observed_only(self):
        self.perimeter_edit('pattern\tclass\treason\n',
                            'pattern\tclass\treason\nPROME/state/HANDOFF_X.md\tEXCLUDED\tx\n')
        self.plan['observed'][sc.PERIMETER_FILE] = self.unrelated()
        with self.assertRaises(ValueError) as cm:
            self.freeze()
        self.assertIn(sc.PERIMETER_FILE, str(cm.exception))  # either guard may fire first; both refuse the freeze

    def test_x2_ce_g1_gitignore_edit_after_the_freeze_blocks(self):
        self.freeze()
        self.write('.gitignore', 'PROME/state/HANDOFF_X.md\n')
        self.write('PROME/state/HANDOFF_X.md', 'hidden OWNED write\n')
        rc, lines = sc.verify_review()
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format('.gitignore'), lines)
        self.assertEqual(self.foreign_lines(lines), [])

    def test_x3_ce_s10_step_10_committed_side_uses_the_pin(self):
        self.freeze()
        self.write('FORGE/x.md', 'desk wrote\n')
        self.git('add', '--', 'FORGE/x.md'); self.git('commit', '-qm', 'BRENT: forge note', '--', 'FORGE/x.md')
        self.perimeter_edit('FORGE/**\tOWNED', 'FORGE/**\tEXCLUDED')
        a = self.commit('PROME/result')
        rc, lines = sc.verify_review(ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format('FORGE/x.md'), lines)
        self.assertIn(UNC.format(sc.PERIMETER_FILE), lines)
        self.assertEqual(self.foreign_lines(lines), [])

    # --- reader 10/24 read #2: ❌A committed ignore file · ❌B observe() door · ⚠️C nested desk ignore file ---

    def test_y1_committed_root_gitignore_under_a_desk_subject_is_never_attributed(self):
        self.freeze()
        self.write('.gitignore', 'PROME/state/HANDOFF_X.md\n')
        self.git('add', '--', '.gitignore'); self.git('commit', '-qm', 'BRENT: ignore scratch', '--', '.gitignore')
        self.write('PROME/state/HANDOFF_X.md', 'hidden OWNED write\n')
        rc, lines = sc.verify_review()
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format('.gitignore'), lines)
        a = self.commit('PROME/result')
        rc, lines = sc.verify_review(ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format('.gitignore'), lines)

    def test_y1b_pre_freeze_committed_root_gitignore_must_be_delivered(self):
        self.write('.gitignore', 'PROME/state/HANDOFF_X.md\n')
        self.git('add', '--', '.gitignore'); self.git('commit', '-qm', 'BRENT: ignore scratch', '--', '.gitignore')
        with self.assertRaises(ValueError) as cm:
            self.freeze()
        self.assertIn('.gitignore', str(cm.exception))
        self.plan['delivered']['.gitignore'] = 'PROME reviewed the ignore change'
        self.freeze()
        self.assertNotIn('.gitignore', self.manifest()['attributed_by_commit'])

    def test_y2_observe_refuses_the_perimeter_after_the_freeze(self):
        self.freeze()
        self.perimeter_edit('pattern\tclass\treason\n', 'pattern\tclass\treason\nPROME/state/HANDOFF_X.md\tEXCLUDED\tx\n')
        self.git('add', '--', sc.PERIMETER_FILE); self.git('commit', '-qm', 'BRENT: perimeter row', '--', sc.PERIMETER_FILE)
        with self.assertRaises(ValueError) as cm:
            ac.observe(sc, {sc.PERIMETER_FILE: self.unrelated()})
        self.assertIn('never observed-only', str(cm.exception))
        d = self.manifest()                      # a hand-inserted observed entry on the perimeter: CANNOT-EVALUATE
        d['observed'][sc.PERIMETER_FILE] = [{'owner': 'OTTO'}]; self.save(d)
        self.assertEqual(sc.verify_review()[0], 2)

    def test_y3_nested_ignore_file_in_an_excluded_lane_stays_advisory(self):
        self.freeze()
        self.write('AGENTS/BROCK/research/.gitignore', '*.csv\n')
        rc, lines = sc.verify_review()
        self.assertEqual(rc, 0, lines)
        self.assertIn(FP.format('EXCLUDED', 'AGENTS/BROCK/research/.gitignore'), lines)

    # --- WQ-517 A (Will 2026-10-24): pending-only foreign paths are advisory at the --ref / --snapshot forms too.
    # Acceptance: ACCEPTANCE_closeout_gate_ref_pending_only_2026-10-24.md (AC1–AC8) ---

    def desk_commit(self, path, text, subject='BROCK: desk note'):
        self.write(path, text)
        self.git('add', '--', path); self.git('commit', '-qm', subject, '--', path)
        return self.git('rev-parse', 'HEAD')

    def test_z1_ac1_pending_only_foreign_arrival_is_advisory_at_the_ref_form(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('AGENTS/BROCK/new.md', 'desk wrote after the delivery commit\n')
        rc, lines = sc.verify_review(ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 0, lines)
        self.assertEqual(self.foreign_lines(lines), [FP.format('EXCLUDED', 'AGENTS/BROCK/new.md')])
        self.assertNotIn(UNC.format('AGENTS/BROCK/new.md'), lines)

    def test_z2_ac2_committed_and_pending_foreign_path_stays_strict_at_the_ref_form(self):
        self.freeze(); a = self.commit('PROME/result')
        self.desk_commit('AGENTS/BROCK/new.md', 'v1\n')
        self.write('AGENTS/BROCK/new.md', 'v2 pending\n')
        rc, lines = sc.verify_review(ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format('AGENTS/BROCK/new.md'), lines)
        self.assertEqual(self.foreign_lines(lines), [])

    def test_z3_ac3_delivery_commit_paths_unchanged_either_way(self):
        self.freeze(); self.write('PROME/extra', 'rode along'); a = self.commit('PROME/result', 'PROME/extra')
        rc, lines = sc.verify_review(ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1, lines)
        self.assertIn('UNREVIEWED ACTUAL COMMIT PATH: PROME/extra', lines)
        self.assertEqual(self.foreign_lines(lines), [])

    def test_z3b_ac3_pending_edit_of_a_delivered_path_after_the_commit_verifies_committed_bytes(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('PROME/result', 'edited after the delivery commit\n')
        rc, lines = sc.verify_review(ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 0, lines)
        self.assertEqual(self.foreign_lines(lines), [])

    def test_z4_ac4_owned_lane_arrival_stays_strict_at_the_ref_form(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('PROME/state/x.md', 'someone wrote in the owned lane\n')
        rc, lines = sc.verify_review(ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format('PROME/state/x.md'), lines)
        self.assertEqual(self.foreign_lines(lines), [])

    def test_z5_ac5_prome_evidenced_arrival_stays_strict_at_the_ref_form(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('AGENTS/BROCK/inbox/2026-10-24_from-PROME_x.md', 'PROME packet, uncommitted\n')
        rc, lines = sc.verify_review(ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format('AGENTS/BROCK/inbox/2026-10-24_from-PROME_x.md'), lines)
        self.assertEqual(self.foreign_lines(lines), [])

    def test_z6_ac6_root_gitignore_edit_after_the_commit_stays_strict_at_the_ref_form(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('.gitignore', 'PROME/state/*.tmp\n')
        rc, lines = sc.verify_review(ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format('.gitignore'), lines)
        self.assertEqual(self.foreign_lines(lines), [])

    def test_z7_ac7_manifest_without_a_pin_runs_strict_at_the_ref_form(self):
        self.freeze(); d = self.manifest(); del d['perimeter']; self.save(d)
        a = self.commit('PROME/result')
        self.write('AGENTS/BROCK/new.md', 'x\n')
        rc, lines = sc.verify_review(ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format('AGENTS/BROCK/new.md'), lines)
        self.assertEqual(self.foreign_lines(lines), [])

    def test_z8_ac8_snapshot_history_stays_strict_while_pending_only_is_advisory(self):
        self.freeze(); a = self.commit('PROME/result')
        p = self.desk_commit('AGENTS/BROCK/other.md', 'v1\n', 'BROCK: other note')
        self.write('AGENTS/BROCK/other.md', 'v2 pending\n')
        self.write('AGENTS/BROCK/new.md', 'pending only\n')
        rc, lines = sc.verify_review(ref=a, snapshot=p, paths=['PROME/result'])
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format('AGENTS/BROCK/other.md'), lines)
        self.assertIn('UNCLASSIFIED SNAPSHOT PATH: AGENTS/BROCK/other.md', lines)
        self.assertEqual(self.foreign_lines(lines), [FP.format('EXCLUDED', 'AGENTS/BROCK/new.md')])

    # --- read #1 of the WQ-517 repair (Opus, 2026-10-24 19:4x ET) ❌1: nested ignore files at the --ref form ---

    def test_z9_ce_f_nested_ignore_file_above_an_owned_arrival_stays_strict_at_the_ref_form(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('.claude/skills/newskill/SKILL.md', 'owned arrival\n')
        self.write('.claude/.gitignore', 'skills/newskill/\n')
        rc, lines = sc.verify_review(ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format('.claude/.gitignore'), lines)
        self.assertEqual(self.foreign_lines(lines), [])

    def test_z9b_ce_f2_shared_lane_ignore_file_hiding_a_prome_packet_stays_strict_at_the_ref_form(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('AGENTS/BROCK/inbox/2026-10-24_from-PROME_x.md', 'PROME packet\n')
        self.write('AGENTS/.gitignore', '*/inbox/*from-PROME*\n')
        rc, lines = sc.verify_review(ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format('AGENTS/.gitignore'), lines)
        self.assertEqual(self.foreign_lines(lines), [])

    def test_z9c_ce_f3_desk_root_ignore_file_over_its_inbox_stays_strict_at_the_ref_form(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('AGENTS/BROCK/inbox/2026-10-24_from-PROME_y.md', 'PROME packet\n')
        self.write('AGENTS/BROCK/.gitignore', 'inbox/\n')
        rc, lines = sc.verify_review(ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1, lines)
        self.assertIn(UNC.format('AGENTS/BROCK/.gitignore'), lines)
        self.assertEqual(self.foreign_lines(lines), [])

    def test_y4_pin_digest_covers_the_bytes_the_rules_were_parsed_from(self):
        self.freeze(); d = self.manifest()
        self.assertEqual(d['perimeter']['sha256'], hashlib.sha256((self.root / sc.PERIMETER_FILE).read_bytes()).hexdigest())
        self.assertEqual([tuple(r) for r in d['perimeter']['rules']], sc.load_perimeter())


if __name__ == '__main__':
    unittest.main()
