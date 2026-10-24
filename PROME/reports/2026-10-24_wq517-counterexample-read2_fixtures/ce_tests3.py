"""Read #2 (WQ-517 fix pass 1): fresh counterexamples aimed at the IGNORE_FILES name test. Disposable repos under TMPDIR.
Each case runs NEW (live working-tree code), FIRSTCUT (live code with the fix-pass-1 name test removed) and PRE-REPAIR (HEAD)."""
import importlib.util, os, subprocess, sys, unittest
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from ce_tests import CE, sc, ac, ac_old, FP, UNC
spec = importlib.util.spec_from_file_location('ac_first', HERE / 'old/argus_contract_FIRSTCUT.py')
ac_first = importlib.util.module_from_spec(spec); spec.loader.exec_module(ac_first)

class CE3(CE):
    def three(self, name, **kw):
        out = {}
        for label, mod in (('NEW', ac), ('FIRSTCUT', ac_first), ('PRE-REPAIR', ac_old)):
            rc, lines = mod.verify(sc, self.manifest(), kw.get('paths'), kw.get('ref'), kw.get('snapshot'))
            self.show(f'{name} {label}', rc, lines); out[label] = (rc, lines)
        print('    porcelain:', sc.porcelain_entries())
        return out

    # CE-J: name variants git does NOT read as ignore files -> cannot hide; the arrival stays visible and strict
    def test_ceJ_uppercase_GITIGNORE_with_and_without_ignorecase(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('.claude/skills/newskill/SKILL.md', 'owned arrival\n')
        self.write('.claude/.GITIGNORE', 'skills/newskill/\n')
        o = self.three('CE-J .GITIGNORE', ref=a, paths=['PROME/result'])
        self.assertEqual(o['NEW'][0], 1); self.assertIn(UNC.format('.claude/skills/newskill/SKILL.md'), o['NEW'][1])
        self.git('config', 'core.ignorecase', 'true')
        o = self.three('CE-J core.ignorecase=true', ref=a, paths=['PROME/result'])
        self.assertEqual(o['NEW'][0], 1); self.assertIn(UNC.format('.claude/skills/newskill/SKILL.md'), o['NEW'][1])
    def test_ceJ2_suffix_and_space_variants(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('AGENTS/BROCK/inbox/2026-10-24_from-PROME_x.md', 'PROME packet\n')
        for n in ('.gitignore~', '.gitignore.bak', '.gitignore ', '.gitignore​'):
            self.write('AGENTS/BROCK/' + n, 'inbox/\n')
        o = self.three('CE-J2 suffix/space/zero-width variants', ref=a, paths=['PROME/result'])
        self.assertEqual(o['NEW'][0], 1); self.assertIn(UNC.format('AGENTS/BROCK/inbox/2026-10-24_from-PROME_x.md'), o['NEW'][1])
    def test_ceJ3_directory_named_gitignore(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('AGENTS/BROCK/inbox/2026-10-24_from-PROME_x.md', 'PROME packet\n')
        self.write('AGENTS/BROCK/.gitignore/inbox', 'inbox/\n')     # a DIRECTORY named .gitignore holding a file
        self.write('AGENTS/.gitignore/.gitignore', '*\n')         # a real ignore file inside that directory
        o = self.three('CE-J3 directory named .gitignore', ref=a, paths=['PROME/result'])
        self.assertEqual(o['NEW'][0], 1)

    # CE-K: inventory-hiders that are NOT ignore-file paths
    def test_ceK_git_info_exclude_hides_owned(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('.claude/skills/newskill/SKILL.md', 'owned arrival\n')
        with open(self.root / '.git/info/exclude', 'a') as f: f.write('.claude/skills/newskill/\n')
        self.three('CE-K .git/info/exclude', ref=a, paths=['PROME/result'])
        rc, l = sc.verify_review(); self.show('CE-K working-tree form', rc, l)
    def test_ceK2_nested_repo_collapses_a_prome_packet_into_a_directory_entry(self):
        self.freeze(); a = self.commit('PROME/result')
        d = self.root / 'AGENTS/BROCK/inbox/data'; d.mkdir(parents=True)
        subprocess.run(['git', 'init', '-q'], cwd=d, check=True)
        self.write('AGENTS/BROCK/inbox/data/2026-10-24_from-PROME_x.md', 'PROME packet body, uncommitted\n')
        o = self.three('CE-K2 nested repo in SHARED inbox lane', ref=a, paths=['PROME/result'])
        rc, l = sc.verify_review(); self.show('CE-K2 working-tree form', rc, l)
    def test_ceK3_nested_repo_gitfile_form(self):
        self.freeze(); a = self.commit('PROME/result')
        d = self.root / 'AGENTS/NEWDESK'; d.mkdir(parents=True)
        other = self.root.parent / (self.root.name + '_sidegit')
        subprocess.run(['git', 'init', '-q', '--separate-git-dir', str(other), str(d)], check=True)
        self.addCleanup(lambda: subprocess.run(['rm', '-rf', str(other)]))
        self.write('AGENTS/NEWDESK/inbox/2026-10-24_from-PROME_y.md', 'PROME packet body\n')
        self.three('CE-K3 nested repo via .git FILE (gitdir:)', ref=a, paths=['PROME/result'])
    def test_ceK4_nested_repo_over_owned_lane_lookup(self):
        """Does any EXCLUDED/SHARED untracked directory contain an OWNED subtree? .claude/ (EXCLUDED) holds .claude/skills/** (OWNED)."""
        self.freeze(); a = self.commit('PROME/result')
        d = self.root / '.claude'; d.mkdir(parents=True)
        subprocess.run(['git', 'init', '-q'], cwd=d, check=True)
        self.write('.claude/skills/newskill/SKILL.md', 'owned arrival\n')
        self.three('CE-K4 nested repo at .claude/ (untracked in fixture)', ref=a, paths=['PROME/result'])

    # CE-L: pending .gitattributes (export-ignore / filter) in an EXCLUDED folder
    def test_ceL_gitattributes_export_ignore_and_filter(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('AGENTS/BROCK/.gitattributes', '* export-ignore\n*.md filter=hide\n')
        o = self.three('CE-L nested .gitattributes', ref=a, paths=['PROME/result'])
        self.assertEqual(o['NEW'][0], 1); self.assertIn(UNC.format('AGENTS/BROCK/.gitattributes'), o['NEW'][1])

    # CE-M: an ignore file DELETED after the freeze (porcelain ' D'), and renames out of / into the name
    def _tracked_nested(self, path, text='inbox/\n'):
        self.write(path, text); self.git('add', '--', path); self.git('commit', '-qm', 'pre', '--', path)
        self.base = self.git('rev-parse', 'HEAD'); sc.record_baseline(self.base)
    def test_ceM_deleted_nested_ignore_file(self):
        self._tracked_nested('AGENTS/BROCK/.gitignore')
        self.freeze(); a = self.commit('PROME/result')
        (self.root / 'AGENTS/BROCK/.gitignore').unlink()
        self.three('CE-M nested ignore file deleted', ref=a, paths=['PROME/result'])
    def test_ceM2_rename_out_of_and_into_the_name(self):
        self._tracked_nested('AGENTS/BROCK/.gitignore')
        self.write('AGENTS/BROCK/notes', 'inbox/\n'); self.git('add', '--', 'AGENTS/BROCK/notes'); self.git('commit', '-qm', 'pre2', '--', 'AGENTS/BROCK/notes')
        self.base = self.git('rev-parse', 'HEAD'); sc.record_baseline(self.base)
        self.freeze(); a = self.commit('PROME/result')
        self.git('mv', 'AGENTS/BROCK/.gitignore', 'AGENTS/BROCK/gi.bak')
        self.git('mv', 'AGENTS/BROCK/notes', 'AGENTS/BROCK/sub/.gitignore') if False else None
        (self.root / 'AGENTS/BROCK/sub').mkdir(); self.git('mv', 'AGENTS/BROCK/notes', 'AGENTS/BROCK/sub/.gitignore')
        self.three('CE-M2 staged renames out of / into .gitignore', ref=a, paths=['PROME/result'])
    def test_ceM3_pending_edit_of_tracked_nested_ignore_file(self):
        self._tracked_nested('AGENTS/BROCK/research/.gitignore', '*.tmp\n')
        self.freeze(); a = self.commit('PROME/result')
        self.write('AGENTS/BROCK/research/.gitignore', '*.tmp\n*.log\n')
        self.three('CE-M3 routine desk edit of its own nested .gitignore', ref=a, paths=['PROME/result'])
        rc, l = sc.verify_review(); self.show('CE-M3 working-tree form', rc, l)

    # CE-N: ignore file COMMITTED by a desk after the delivery (then pending-edited / or not)
    def test_ceN_desk_commits_ignore_after_delivery_then_pending_edit(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('.claude/skills/newskill/SKILL.md', 'owned arrival\n')
        self.desk_commit('.claude/.gitignore', 'skills/newskill/\n', 'BROCK: harness ignore')
        self.write('.claude/.gitignore', 'skills/newskill/\n# edited\n')
        self.three('CE-N committed-after-delivery + pending edit', ref=a, paths=['PROME/result'])
    def test_ceN2_desk_commits_ignore_after_delivery_no_pending(self):
        self.freeze(); a = self.commit('PROME/result')
        self.write('.claude/skills/newskill/SKILL.md', 'owned arrival\n')
        self.desk_commit('.claude/.gitignore', 'skills/newskill/\n', 'BROCK: harness ignore')
        self.three('CE-N2 committed-only ignore file after delivery (WQ-485 A attribution)', ref=a, paths=['PROME/result'])
        rc, l = sc.verify_review(); self.show('CE-N2 working-tree form', rc, l)
    def test_ceN3_same_but_ignore_committed_BEFORE_freeze_then_owned_arrival(self):
        self.desk_commit('.claude/.gitignore', 'skills/newskill/\n', 'BROCK: harness ignore')
        self.freeze(); a = self.commit('PROME/result')
        self.write('.claude/skills/newskill/SKILL.md', 'owned arrival\n')
        self.three('CE-N3 committed (pre-freeze, post-baseline) ignore file', ref=a, paths=['PROME/result'])

if __name__ == '__main__':
    unittest.main(verbosity=1)
