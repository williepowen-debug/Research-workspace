"""Independent counterexamples for WQ-517 A (L796 ❌1). Fixtures are disposable repos under TMPDIR."""
import importlib.util, json, os, sys, unittest
from pathlib import Path
REPO = Path('/home/willi/Research-workspace')
sys.path.insert(0, str(REPO / 'PROME/tools'))
sys.path.insert(0, str(REPO / 'PROME/tools/tests'))
import argus_scope as sc
import argus_contract as ac
import test_argus_contract as T
spec = importlib.util.spec_from_file_location('ac_old', Path(__file__).parent / 'old/argus_contract_HEAD.py')
ac_old = importlib.util.module_from_spec(spec); spec.loader.exec_module(ac_old)
FP, UNC = T.FP, T.UNC

class CE(T.PerimeterPinTests):
    def show(self, name, rc, lines):
        print(f'\n[{name}] rc={rc}'); [print('   ', l) for l in lines]
    def both(self, name, **kw):
        rc, lines = sc.verify_review(**kw)
        self.show(name + ' NEW', rc, lines)
        d = self.manifest()
        orc, olines = ac_old.verify(sc, d, kw.get('paths'), kw.get('ref'), kw.get('snapshot'))
        self.show(name + ' PRE-REPAIR', orc, olines)
        return rc, lines, orc, olines

    # CE-A: HEAD advanced past the delivery; a foreign commit in delivery..HEAD (outside baseline..target), then pending edit
    def test_ceA_head_past_delivery_foreign_commit_then_pending(self):
        self.freeze(); a = self.commit('PROME/result')
        self.desk_commit('AGENTS/BROCK/y.md', 'v1\n')
        self.write('AGENTS/BROCK/y.md', 'v2 pending\n')
        rc, lines, *_ = self.both('CE-A', ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1); self.assertIn(UNC.format('AGENTS/BROCK/y.md'), lines)
    def test_ceA2_later_prome_commit_after_delivery(self):
        self.freeze(); a = self.commit('PROME/result')
        self.desk_commit('AGENTS/BROCK/z.md', 'PROME wrote\n', 'PROME -> BROCK: packet')
        rc, lines, *_ = self.both('CE-A2', ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1); self.assertIn(UNC.format('AGENTS/BROCK/z.md'), lines)
    def test_ceA3_later_prome_commit_then_foreign_pending_on_that_path(self):
        self.freeze(); a = self.commit('PROME/result')
        self.desk_commit('AGENTS/BROCK/z.md', 'PROME wrote\n', 'PROME -> BROCK: packet')
        self.write('AGENTS/BROCK/z.md', 'desk consumed and edited\n')
        rc, lines, *_ = self.both('CE-A3', ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1); self.assertEqual(self.foreign_lines(lines), [])

    # CE-B: pending DELETION
    def test_ceB_pending_deletion_foreign_tracked(self):
        self.write('AGENTS/BROCK/old.md', 'pre-baseline\n'); self.git('add', '--', 'AGENTS/BROCK/old.md')
        self.git('commit', '-qm', 'pre', '--', 'AGENTS/BROCK/old.md'); self.base = self.git('rev-parse', 'HEAD'); sc.record_baseline(self.base)
        self.freeze(); a = self.commit('PROME/result')
        (self.root / 'AGENTS/BROCK/old.md').unlink()
        rc, lines, *_ = self.both('CE-B foreign delete', ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 0); self.assertIn(FP.format('EXCLUDED', 'AGENTS/BROCK/old.md'), lines)
    def test_ceB2_pending_deletion_owned_and_perimeter(self):
        self.freeze(); a = self.commit('PROME/result')
        (self.root / 'PROME/old').unlink(); (self.root / sc.PERIMETER_FILE).unlink()
        rc, lines, *_ = self.both('CE-B2 owned+perimeter delete', ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1); self.assertEqual(self.foreign_lines(lines), [])

    # CE-C: staged RENAME out of the OWNED lane into an EXCLUDED lane
    def test_ceC_staged_rename_owned_to_excluded(self):
        self.freeze(); a = self.commit('PROME/result')
        (self.root / 'AGENTS/BROCK').mkdir(parents=True, exist_ok=True)
        self.git('mv', 'PROME/old', 'AGENTS/BROCK/old')
        print('\nporcelain:', sc.porcelain_entries())
        rc, lines, *_ = self.both('CE-C staged rename OWNED->EXCLUDED', ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1); self.assertIn(UNC.format('PROME/old'), lines)
    def test_ceC2_staged_rename_within_foreign_lane(self):
        self.write('AGENTS/BROCK/a.md', 'pre\n'); self.git('add', '--', 'AGENTS/BROCK/a.md')
        self.git('commit', '-qm', 'pre', '--', 'AGENTS/BROCK/a.md'); self.base = self.git('rev-parse', 'HEAD'); sc.record_baseline(self.base)
        self.freeze(); a = self.commit('PROME/result')
        self.git('mv', 'AGENTS/BROCK/a.md', 'AGENTS/BROCK/b.md')
        rc, lines, *_ = self.both('CE-C2 staged rename in foreign lane', ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 0)
    def test_ceC3_rename_to_prome_evidenced_name(self):
        self.write('AGENTS/BROCK/inbox/2026-10-24_from-PROME_x.md', 'pre\n'); self.git('add', '--', 'AGENTS/BROCK/inbox/2026-10-24_from-PROME_x.md')
        self.git('commit', '-qm', 'pre', '--', 'AGENTS/BROCK/inbox/2026-10-24_from-PROME_x.md'); self.base = self.git('rev-parse', 'HEAD'); sc.record_baseline(self.base)
        self.freeze(); a = self.commit('PROME/result')
        (self.root / 'AGENTS/BROCK/inbox/processed').mkdir(parents=True)
        self.git('mv', 'AGENTS/BROCK/inbox/2026-10-24_from-PROME_x.md', 'AGENTS/BROCK/inbox/processed/2026-10-24_from-PROME_x.md')
        rc, lines, *_ = self.both('CE-C3 desk consumes a PROME packet (pending move)', ref=a, paths=['PROME/result'])

    # CE-D: staged-only add; staged-then-reverted (working bytes == committed bytes)
    def test_ceD_staged_add_foreign(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('AGENTS/BROCK/s.md', 'staged\n'); self.git('add', '--', 'AGENTS/BROCK/s.md')
        rc, lines, *_ = self.both('CE-D staged add', ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 0)
    def test_ceD2_mode_only_and_staged_reverted(self):
        self.write('AGENTS/BROCK/m.md', 'pre\n'); self.write('OWNERX.md', 'pre\n'); self.git('add', '--', 'AGENTS/BROCK/m.md', 'OWNERX.md')
        self.git('commit', '-qm', 'pre', '--', 'AGENTS/BROCK/m.md', 'OWNERX.md'); self.base = self.git('rev-parse', 'HEAD'); sc.record_baseline(self.base)
        self.freeze(); a = self.commit('PROME/result')
        os.chmod(self.root / 'AGENTS/BROCK/m.md', 0o755)
        self.write('OWNERX.md', 'staged\n'); self.git('add', '--', 'OWNERX.md'); self.write('OWNERX.md', 'pre\n')
        os.chmod(self.root / 'PROME/old', 0o755)
        print('\nporcelain:', sc.porcelain_entries())
        rc, lines, *_ = self.both('CE-D2 mode-only + staged-reverted', ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1); self.assertIn(UNC.format('PROME/old'), lines)

    # CE-E: case / prefix lookalikes of the OWNED lane
    def test_ceE_case_and_prefix_lookalikes(self):
        self.freeze(); a = self.commit('PROME/result')
        for p in ('prome/state/x.md', 'PROMEX/state/x.md', 'Prome/state/x.md', 'PROME/inbox/x.md', 'forge/x.md'):
            self.write(p, 'x\n')
        rc, lines, *_ = self.both('CE-E lookalikes', ref=a, paths=['PROME/result'])

    # CE-F: never-advisory guard probes only the ignore file's own dir; the subtree holds OWNED / SHARED sublanes
    def test_ceF_claude_gitignore_hides_owned_skill(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('.claude/skills/newskill/SKILL.md', 'PROME skill written after the commit, never committed\n')
        rc0, l0 = sc.verify_review(ref=a, paths=['PROME/result']); self.show('CE-F control (no ignore file)', rc0, l0)
        self.write('.claude/.gitignore', 'skills/newskill/\n')
        rc, lines, orc, ol = self.both('CE-F .claude/.gitignore hides OWNED', ref=a, paths=['PROME/result'])
        print('   ignored?', self.git('status', '--porcelain', '-uall', '--ignored'))
    def test_ceF2_agents_gitignore_hides_prome_packet(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('AGENTS/BROCK/inbox/2026-10-24_from-PROME_x.md', 'PROME packet, uncommitted\n')
        self.write('AGENTS/.gitignore', '*/inbox/*from-PROME*\n')
        rc, lines, orc, ol = self.both('CE-F2 AGENTS/.gitignore hides PROME-evidenced', ref=a, paths=['PROME/result'])
    def test_ceF3_desk_lane_gitignore_hides_shared_inbox(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('AGENTS/BROCK/inbox/2026-10-24_from-PROME_y.md', 'PROME packet, uncommitted\n')
        self.write('AGENTS/BROCK/.gitignore', 'inbox/\n')
        rc, lines, orc, ol = self.both('CE-F3 AGENTS/BROCK/.gitignore hides SHARED inbox', ref=a, paths=['PROME/result'])
    def test_ceF4_same_at_working_tree_form(self):
        self.freeze()
        self.write('AGENTS/BROCK/inbox/2026-10-24_from-PROME_y.md', 'PROME packet, uncommitted\n')
        self.write('AGENTS/BROCK/.gitignore', 'inbox/\n')
        rc, lines = sc.verify_review(); self.show('CE-F4 working-tree form (step 8)', rc, lines)

    # CE-G: snapshot P not an ancestor of HEAD (side branch from the delivery), path pending-only locally
    def test_ceG_snapshot_not_ancestor_of_head(self):
        self.freeze(); a = self.commit('PROME/result')
        self.git('checkout', '-q', '-b', 'side')
        p = self.desk_commit('AGENTS/BROCK/z.md', 'remote v1\n', 'BROCK: z')
        self.git('checkout', '-q', 'master')
        self.write('AGENTS/BROCK/z.md', 'local pending\n')
        print('\nHEAD', self.git('rev-parse', 'HEAD')[:9], 'a', a[:9], 'p', p[:9])
        rc, lines, *_ = self.both('CE-G snapshot not ancestor of HEAD', ref=a, snapshot=p, paths=['PROME/result'])
        self.assertEqual(rc, 1); self.assertIn('UNCLASSIFIED SNAPSHOT PATH: AGENTS/BROCK/z.md', lines)
    def test_ceG2_head_behind_delivery(self):
        """HEAD reset below the delivery after it was made (delivery's own paths become staged pending)."""
        self.freeze(); self.write('AGENTS/BROCK/q.md', 'foreign'); a = self.commit('PROME/result')
        self.desk_commit('AGENTS/BROCK/q2.md', 'desk\n', 'BROCK: q2')
        b = self.git('rev-parse', 'HEAD')
        self.git('reset', '-q', '--soft', a + '~1')
        rc, lines, *_ = self.both('CE-G2 HEAD behind delivery, ref=delivery', ref=a, paths=['PROME/result'])
        rc, lines, *_ = self.both('CE-G2b HEAD behind, snapshot=b', ref=a, snapshot=b, paths=['PROME/result'])

    # CE-H: rc 0 with advisories only -> the push question; also an UNTRACKED pending-only file named like the delivery path's sibling
    def test_ceH_rc0_and_later_commits_still_checked(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('AGENTS/BROCK/new.md', 'x\n')
        rc, lines = sc.verify_review(ref=a, paths=['PROME/result']); self.show('CE-H rc0 advisory only', rc, lines)
        self.write('PROME/later', 'unreviewed PROME work'); self.commit('PROME/later')
        rc, lines = sc.verify_review(ref=a, paths=['PROME/result']); self.show('CE-H2 + later unreviewed PROME commit', rc, lines)
        self.assertEqual(rc, 1)

if __name__ == '__main__':
    unittest.main(verbosity=1)
