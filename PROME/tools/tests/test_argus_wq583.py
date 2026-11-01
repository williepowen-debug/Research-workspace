"""WQ-583 code half (DOCKET L912): candidate off the shared branch · byte-identical moves · exact-version reuse ·
derived delivery list. Acceptance: ACCEPTANCE_wq583_candidate_moves_reuse_2026-10-31.md. Disposable repos only."""
import io
import json
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_argus_contract import ContractFixture, PERIMETER, sc, ac  # noqa: E402


class WQ583Tests(ContractFixture):
    def setUp(self):
        # the same baseline as PerimeterPinTests: the REAL perimeter committed, so the advisory branches are live
        super().setUp()
        self.write(sc.PERIMETER_FILE, PERIMETER)
        self.write('memory/auto/MEMORY.md', 'idx\n')
        self.git('add', '--', sc.PERIMETER_FILE, 'memory/auto/MEMORY.md')
        self.git('commit', '-qm', 'baseline perimeter', '--', sc.PERIMETER_FILE, 'memory/auto/MEMORY.md')
        self.base = self.git('rev-parse', 'HEAD')
        sc.record_baseline(self.base)

    # ---- helpers
    def at(self, ref, path):
        return self.git('show', f'{ref}:{path}')

    def subject_commit(self, path, text, subject):
        self.write(path, text)
        self.git('add', '--', path); self.git('commit', '-qm', subject, '--', path)
        return self.git('rev-parse', 'HEAD')

    def msg(self, subject='PROME: closeout delivery'):
        f = self.root.parent / f'{self.root.name}-msg.txt'
        f.write_text(subject + '\n\nbody\n'); self.addCleanup(f.unlink, missing_ok=True)
        return f

    def reviewed(self):
        self.assertEqual(sc.mark_reviewed('fixture audit')[0], 0)

    def rebase_with(self, *paths_texts):
        """Commit files into the baseline so a later move has an origin present at the baseline."""
        for path, text in paths_texts:
            self.write(path, text)
        paths = [p for p, _ in paths_texts]
        self.git('add', '--', *paths); self.git('commit', '-qm', 'BROCK: baseline packets', '--', *paths)
        self.base = self.git('rev-parse', 'HEAD'); sc.record_baseline(self.base)

    # ---- AC1
    def test_ac1_candidate_is_an_immutable_commit_on_no_branch(self):
        head = self.git('rev-parse', 'HEAD'); status = self.git('status', '--porcelain')
        d = self.freeze(); k = d['candidate']['sha']
        self.assertEqual(self.git('rev-parse', ac.CANDIDATE_REF), k)
        self.assertEqual(self.git('for-each-ref', '--contains', k, 'refs/heads'), '')
        self.assertEqual(self.at(k, 'PROME/result'), 'reviewed result')
        self.assertEqual(self.git('rev-parse', k + '^'), head)
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)
        self.assertEqual(self.git('diff', '--cached', '--name-only'), '')
        self.assertEqual(self.git('status', '--porcelain').replace('\n?? PROME/state/argus_review.json', ''), status)

    def test_ac1_candidate_tamper_is_caught_by_validate(self):
        d = self.freeze()
        other = self.git('commit-tree', self.git('rev-parse', 'HEAD^{tree}'), '-p', 'HEAD', '-m', 'x')
        d['candidate']['sha'] = other; self.save(d)
        self.assertEqual(sc.verify_review()[0], 2)

    # ---- AC2
    def test_ac2_post_freeze_bookkeeping_does_not_break_mark_or_gate(self):
        self.freeze()
        self.write('PROME/result', 'reviewed result\nARGUS run-log row\n')
        self.assertEqual(sc.mark_reviewed('audit of the candidate')[0], 0)
        rc, lines = sc.verify_review()
        self.assertEqual(rc, 0, lines)
        self.assertTrue(lines[0].startswith('POST-FREEZE EDIT'), lines)

    def test_ac2_ref_form_stays_strict(self):
        self.freeze(); self.reviewed()
        self.write('PROME/result', 'edited after review'); b = self.commit('PROME/result')
        self.assertEqual(sc.verify_review(ref=b, paths=['PROME/result'])[0], 1)

    # ---- AC3
    def test_ac3_delivery_ships_candidate_bytes_and_carries_the_edit(self):
        self.freeze(); self.reviewed(); head = self.git('rev-parse', 'HEAD')
        self.write('PROME/result', 'reviewed result\nARGUS run-log row\n')
        with self.assertRaisesRegex(ValueError, 'post-freeze edits'):
            ac.deliver(sc, self.msg())
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)
        n, paths = ac.deliver(sc, self.msg(), carry=['PROME/result'])
        self.assertEqual(self.git('rev-parse', 'HEAD'), n)
        self.assertEqual(self.git('rev-parse', n + '^'), head)
        self.assertEqual(self.at(n, 'PROME/result'), 'reviewed result')
        self.assertEqual((self.root / 'PROME/result').read_text(), 'reviewed result\nARGUS run-log row\n')
        self.assertEqual(self.git('diff', '--cached', '--name-only'), '')
        self.assertEqual(self.git('diff', '--name-only'), 'PROME/result')   # unstaged: rides the bookkeeping commit
        self.assertEqual(sc.verify_review(ref=n, paths=paths)[0], 0)

    def test_ac3_delivery_keeps_another_desks_commit_since_the_freeze(self):
        self.freeze(); self.reviewed()
        desk = self.subject_commit('AGENTS/BROCK/note.md', 'desk\n', 'BROCK: desk note')
        n, paths = ac.deliver(sc, self.msg())
        self.assertEqual(self.git('rev-parse', n + '^'), desk)
        self.assertEqual(self.at(n, 'AGENTS/BROCK/note.md'), 'desk')
        self.assertEqual(paths, ['PROME/result'])
        rc, lines = sc.verify_review(ref=n, paths=paths)
        self.assertEqual(rc, 0, lines)

    def test_ac3_refuses_when_the_path_changed_on_master(self):
        self.freeze(); self.reviewed()
        self.subject_commit('PROME/result', 'someone else', 'BROCK: overwrote it')
        head = self.git('rev-parse', 'HEAD')
        with self.assertRaisesRegex(ValueError, 'changed on master since the freeze'):
            ac.deliver(sc, self.msg(), carry=['PROME/result'])
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)

    def test_ac3_refuses_unreviewed_candidate(self):
        self.freeze()
        with self.assertRaisesRegex(ValueError, 'not REVIEWED'):
            ac.deliver(sc, self.msg())

    def test_ac3_refuses_another_staged_version(self):
        self.freeze(); self.reviewed(); head = self.git('rev-parse', 'HEAD')
        self.write('PROME/result', 'staged by another session'); self.git('add', '--', 'PROME/result')
        with self.assertRaisesRegex(ValueError, 'shared index holds another version'):
            ac.deliver(sc, self.msg(), carry=['PROME/result'])
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)
        self.assertEqual(self.git('diff', '--cached', '--name-only'), 'PROME/result')

    def test_ac3_refuses_long_subject_and_stray_carry(self):
        self.freeze(); self.reviewed()
        with self.assertRaisesRegex(ValueError, '100'):
            ac.deliver(sc, self.msg('PROME: ' + 'x' * 100))
        with self.assertRaisesRegex(ValueError, 'no post-freeze edit'):
            ac.deliver(sc, self.msg(), carry=['PROME/result'])

    def test_ac3_master_moving_mid_delivery_writes_nothing(self):
        self.freeze(); self.reviewed(); real = ac._run
        def racing(scm, *args, **kw):
            out = real(scm, *args, **kw)
            if args and args[0] == 'commit-tree' and 'GIT_INDEX_FILE' not in (kw.get('env') or {}) and '-F' in args:
                self.subject_commit('AGENTS/BROCK/race.md', 'race\n', 'BROCK: raced')
            return out
        with patch.object(ac, '_run', racing):
            with self.assertRaises(Exception):
                ac.deliver(sc, self.msg())
        self.assertEqual(self.git('log', '-1', '--format=%s'), 'BROCK: raced')
        self.assertEqual(self.git('diff', '--cached', '--name-only'), '')

    # ---- AC4
    def test_ac4_prome_inbox_move_is_mechanical_and_ships_with_the_delivery(self):
        o, dst = 'PROME/inbox/2026-10-31_from-WALTER_x.md', 'PROME/inbox/processed/2026-10-31_from-WALTER_x.md'
        self.rebase_with((o, 'packet\n'))
        self.write('PROME/result', 'reviewed result')
        (self.root / 'PROME/inbox/processed').mkdir(parents=True, exist_ok=True)
        self.git('mv', o, dst)
        d = self.freeze()
        self.assertEqual(d['contract']['mechanical_moves'], {dst: {'origin': o, 'sha256': d['inventory'][dst]['working_sha256']}})
        self.assertNotIn(dst, d['contract']['delivered'])
        self.assertEqual(set(d['candidate']['paths']), {'PROME/result', o, dst})
        self.reviewed()
        n, paths = ac.deliver(sc, self.msg())
        self.assertEqual(self.at(n, dst), 'packet')
        self.assertNotIn(o, self.git('ls-tree', '-r', '--name-only', n).splitlines())
        rc, lines = sc.verify_review(ref=n, paths=paths)
        self.assertEqual(rc, 0, lines)
        self.assertEqual(self.git('status', '--porcelain', '--', 'PROME/inbox'), '')

    def test_ac4_desk_move_of_a_from_prome_packet_needs_no_entry_and_is_not_prome_s(self):
        o = 'AGENTS/GIBBS/inbox/2026-10-31_from-PROME_wake.md'
        dst = 'AGENTS/GIBBS/inbox/processed/2026-10-31_from-PROME_wake.md'
        self.rebase_with((o, 'wake\n'))
        self.write('PROME/result', 'reviewed result')
        (self.root / dst).parent.mkdir(parents=True, exist_ok=True); self.git('mv', o, dst)
        d = self.freeze()
        self.assertIn(dst, d['contract']['mechanical_moves'])
        self.assertEqual(set(d['candidate']['paths']), {'PROME/result'})
        self.assertEqual(sc.verify_review()[0], 0)

    def _gibbs_move(self, mutate=None, rename=False):
        o = 'AGENTS/GIBBS/inbox/2026-10-31_from-PROME_wake.md'
        dst = 'AGENTS/GIBBS/inbox/processed/' + ('renamed_from-PROME.md' if rename else '2026-10-31_from-PROME_wake.md')
        self.rebase_with((o, 'wake\n'))
        self.write('PROME/result', 'reviewed result')
        (self.root / dst).parent.mkdir(parents=True, exist_ok=True); self.git('mv', o, dst)
        if mutate:
            self.write(dst, mutate)
        return o, dst

    def test_ac4_changed_bytes_are_not_mechanical(self):
        self._gibbs_move(mutate='wake\nannotated\n')
        with self.assertRaisesRegex(ValueError, 'unclassified inventory'):
            self.freeze()

    def test_ac4_renamed_basename_is_not_mechanical(self):
        self._gibbs_move(rename=True)
        with self.assertRaisesRegex(ValueError, 'unclassified inventory'):
            self.freeze()

    def test_ac4_ambiguous_pairing_is_not_mechanical(self):
        a, b = 'AGENTS/GIBBS/inbox/x/2026_from-PROME_p.md', 'AGENTS/GIBBS/inbox/y/2026_from-PROME_p.md'
        self.rebase_with((a, 'same\n'), (b, 'same\n'))
        self.write('PROME/result', 'reviewed result')
        dst = 'AGENTS/GIBBS/inbox/processed/2026_from-PROME_p.md'
        (self.root / dst).parent.mkdir(parents=True, exist_ok=True); self.git('mv', a, dst); self.git('rm', '-q', b)
        with self.assertRaisesRegex(ValueError, 'unclassified inventory'):
            self.freeze()

    def test_ac4_ignore_file_move_is_never_mechanical(self):
        self.rebase_with(('PROME/x/.gitignore', 'tmp/\n'))
        self.write('PROME/result', 'reviewed result')
        (self.root / 'PROME/y').mkdir(parents=True, exist_ok=True); self.git('mv', 'PROME/x/.gitignore', 'PROME/y/.gitignore')
        with self.assertRaises(ValueError):
            self.freeze()

    def test_ac4_a_move_that_stops_holding_falls_back_to_strict(self):
        o, dst = self._gibbs_move()
        self.freeze()
        self.write(dst, 'wake\nedited after the freeze\n')
        rc, lines = sc.verify_review()
        self.assertEqual(rc, 1, lines)
        self.assertIn(f'UNCLASSIFIED: {dst} (new or changed observed version)', lines)

    def test_ac4_packet_sent_and_filed_inside_one_window_is_not_a_move_but_ships_unchanged(self):
        # reader 2026-10-31 ❌1: a version gained inside the window is new content, never a move
        o = 'AGENTS/WALTER/inbox/2026-10-31_from-PROME_note.md'
        dst = 'AGENTS/WALTER/inbox/processed/2026-10-31_from-PROME_note.md'
        self.subject_commit(o, 'note\n', 'PROME -> WALTER: note')
        (self.root / dst).parent.mkdir(parents=True, exist_ok=True)
        self.git('mv', o, dst); self.git('commit', '-qm', 'WALTER: file processed', '--', o, dst)
        d = ac.freeze(sc, {'auto_delivered': True})
        self.assertEqual(d['contract']['mechanical_moves'], {})
        self.assertIn(dst, d['contract']['delivered'])           # from-PROME name, committed-only: ships unchanged
        self.assertIn(o, d['contract']['delivered'])

    def test_ce01_in_window_edit_then_move_is_never_mechanical(self):
        self.rebase_with(('PROME/reports/a.md', 'old\n'))
        self.write('PROME/result', 'reviewed result')
        self.subject_commit('PROME/reports/a.md', 'NEW unreviewed text\n', 'PROME: intra-day edit')
        (self.root / 'PROME/archive').mkdir(parents=True, exist_ok=True)
        self.git('mv', 'PROME/reports/a.md', 'PROME/archive/a.md')
        d = ac.freeze(sc, {'auto_delivered': True})
        self.assertEqual(d['contract']['mechanical_moves'], {})
        self.assertIn('PROME/archive/a.md', d['contract']['delivered'])

    def test_ce06_forge_archive_move_is_prome_s_and_ships(self):
        self.rebase_with(('FORGE/LEDGER.tsv', 'rows\n'))
        self.write('PROME/result', 'reviewed result')
        (self.root / 'FORGE/_archive').mkdir(parents=True, exist_ok=True)
        self.git('mv', 'FORGE/LEDGER.tsv', 'FORGE/_archive/LEDGER.tsv')
        d = self.freeze()
        self.assertIn('FORGE/_archive/LEDGER.tsv', d['contract']['mechanical_moves'])
        self.assertIn('FORGE/_archive/LEDGER.tsv', d['candidate']['paths'])
        self.reviewed(); n, paths = ac.deliver(sc, self.msg())
        self.assertEqual(sc.verify_review(ref=n, paths=paths)[0], 0)

    def test_ce11_cross_side_move_is_not_mechanical(self):
        self.rebase_with(('AGENTS/BROCK/research/x.md', 'desk text\n'))
        self.write('PROME/result', 'reviewed result')
        (self.root / 'PROME/reports').mkdir(parents=True, exist_ok=True)
        self.git('mv', 'AGENTS/BROCK/research/x.md', 'PROME/reports/x.md')
        d = ac.freeze(sc, {'auto_delivered': True, 'delivered': {'AGENTS/BROCK/research/x.md': 'moved by PROME'}})
        self.assertEqual(d['contract']['mechanical_moves'], {})
        self.assertIn('PROME/reports/x.md', d['contract']['delivered'])

    # ---- AC5
    def test_ac5_reuse_from_a_reviewed_freeze_only_for_identical_bytes(self):
        self.freeze(); self.reviewed()
        self.write('PROME/second', 'new file')
        self.plan['delivered']['PROME/second'] = 'added after the review'
        d = self.freeze()
        self.assertEqual(set(d['contract']['reused']), {'PROME/result'})
        self.assertEqual(d['contract']['reused']['PROME/result']['source'], 'previous-review')
        self.reviewed()
        self.write('PROME/result', 'fixed after review')
        d = self.freeze()
        self.assertEqual(set(d['contract']['reused']), {'PROME/second'})

    def test_ac5_no_reuse_from_a_frozen_only_manifest(self):
        self.freeze()
        d = self.freeze()
        self.assertEqual(d['contract']['reused'], {})

    def test_wq584_declared_reviews_are_switched_off(self):
        # read #3 ⚠️3: a declared review was self-attested — only previous-review reuse counts now
        x = self.subject_commit('PROME/result', 'reviewed result', 'PROME: reviewed build')
        self.plan['reviewed'] = {'PROME/result': {'commit': x, 'receipt': 'OWNER.md'}}
        with self.assertRaisesRegex(ValueError, 'switched off'):
            self.freeze()

    def test_wq584_a_desks_pending_move_never_rides_a_prome_commit(self):
        o = 'AGENTS/RED/inbox/2026-10-31_from-WALTER_x.md'
        dst = 'AGENTS/RED/inbox/processed/2026-10-31_from-WALTER_x.md'
        self.rebase_with((o, 'packet\n'))
        self.write('PROME/result', 'reviewed result')
        (self.root / dst).parent.mkdir(parents=True, exist_ok=True); self.git('mv', o, dst)
        d = self.freeze()
        self.assertIn(dst, d['contract']['mechanical_moves'])
        self.git('add', '--', 'PROME/result')
        self.git('commit', '-qm', 'PROME: intra-day commit', '--', 'PROME/result', o, dst)   # sweeps RED's move
        a = self.git('rev-parse', 'HEAD')
        rc, lines = sc.verify_review(ref=a, paths=['PROME/result', o, dst])
        self.assertEqual(rc, 1, lines)
        self.assertIn(f'UNREVIEWED ACTUAL COMMIT PATH: {dst}', lines)

    def test_wq584_a_live_file_moved_into_prome_inbox_is_not_a_move(self):
        self.rebase_with(('PROME/tools/gate.py', 'print(1)\n'))
        self.write('PROME/result', 'reviewed result')
        (self.root / 'PROME/inbox').mkdir(parents=True, exist_ok=True)
        self.git('mv', 'PROME/tools/gate.py', 'PROME/inbox/gate.py')
        d = ac.freeze(sc, {'auto_delivered': True})
        self.assertEqual(d['contract']['mechanical_moves'], {})
        self.assertIn('PROME/tools/gate.py', d['contract']['delivered'])   # the removal is audited as PROME's

    # ---- AC6
    def test_ac6_auto_delivered_derives_prome_paths_and_leaves_foreign_alone(self):
        self.subject_commit('memory/2026-10-31.md', 'PROME account\n', 'PROME: daily account')
        self.subject_commit('memory/2026-10-30.md', 'desk note\n', 'BROCK: daily note')
        self.write('AGENTS/RED/inbox/2026-10-31_from-PROME_ask.md', 'ask\n')
        self.write('AGENTS/BROCK/work.md', 'desk pending\n')
        d = ac.freeze(sc, {'auto_delivered': True})
        got = set(d['contract']['delivered'])
        self.assertEqual(got, {'PROME/result', 'memory/2026-10-31.md', 'AGENTS/RED/inbox/2026-10-31_from-PROME_ask.md'})
        self.assertTrue(all(v['provenance'].startswith('auto (WQ-583 AC6') for v in d['contract']['delivered'].values()))
        self.assertIn('AGENTS/BROCK/work.md', d['foreign_at_freeze'])

    def test_ac6_explicit_entry_overrides_auto_provenance(self):
        d = ac.freeze(sc, {'auto_delivered': True, 'delivered': {'PROME/result': 'hand provenance'}})
        self.assertEqual(d['contract']['delivered']['PROME/result']['provenance'], 'hand provenance')

    def test_ce03_pending_edit_outside_prome_lane_is_never_auto_claimed(self):
        self.subject_commit('AGENTS/SIGNALS.md', 'PROME row\n', 'PROME: signal row')
        self.write('AGENTS/SIGNALS.md', 'PROME row\nBROCK uncommitted row\n')
        with self.assertRaisesRegex(ValueError, 'unclassified inventory'):
            ac.freeze(sc, {'auto_delivered': True})

    def test_ce04_via_prome_file_is_never_auto_claimed(self):
        # not claimed: the via-PROME name is evidence enough to demand a decision, never enough to claim it
        self.write('AGENTS/RED/inbox/2026-10-31_via-PROME_relay.md', 'desk-written relay\n')
        with self.assertRaisesRegex(ValueError, 'unclassified inventory.*via-PROME'):
            ac.freeze(sc, {'auto_delivered': True})

    def test_exclude_keeps_a_path_out_of_auto(self):
        self.write('PROME/other_desk_wrote_this', 'x\n')
        with self.assertRaisesRegex(ValueError, 'unclassified inventory'):
            ac.freeze(sc, {'auto_delivered': True, 'exclude': ['PROME/other_desk_wrote_this']})

    def test_ce02_repository_hooks_run_on_the_delivery(self):
        hooks = self.root / 'hooks'; hooks.mkdir()
        (hooks / 'pre-commit').write_text('#!/bin/sh\nif git diff --cached -U0 | grep -q SNEAK_MARKER_Q; then echo account guard >&2; exit 1; fi\n')
        (hooks / 'pre-commit').chmod(0o755)
        self.git('config', 'core.hooksPath', 'hooks')
        self.write('PROME/result', 'SNEAK_MARKER_Q')
        self.freeze(); self.reviewed(); head = self.git('rev-parse', 'HEAD')
        with self.assertRaisesRegex(ValueError, 'pre-commit hook refused'):
            ac.deliver(sc, self.msg())
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)

    def test_ce05_filemode_false_keeps_recorded_mode(self):
        self.git('config', 'core.fileMode', 'false')
        (self.root / 'PROME/result').chmod(0o755)
        d = self.freeze()
        self.assertEqual(ac.tree_entry(sc, d['candidate']['sha'], 'PROME/result')[0], '100644')

    def test_r2_1_desk_change_to_an_old_prome_packet_is_never_auto_claimed(self):
        self.rebase_with(('AGENTS/RED/inbox/2026-10-20_from-PROME_ask.md', 'ask\n'))
        self.write('AGENTS/RED/inbox/2026-10-20_from-PROME_ask.md', 'ask\nRED: DONE (desk text)\n')
        with self.assertRaisesRegex(ValueError, 'unclassified inventory'):
            ac.freeze(sc, {'auto_delivered': True})
        self.git('rm', '-q', '--cached', 'AGENTS/RED/inbox/2026-10-20_from-PROME_ask.md')
        (self.root / 'AGENTS/RED/inbox/2026-10-20_from-PROME_ask.md').unlink()
        with self.assertRaisesRegex(ValueError, 'unclassified inventory'):
            ac.freeze(sc, {'auto_delivered': True})

    def test_r2_2_excluded_inbox_bytes_never_move_into_an_owned_path(self):
        o = 'PROME/inbox/2026-10-31_from-DAEDALUS_skill/SKILL.md'
        self.rebase_with((o, 'desk-written skill\n'))
        self.write('PROME/result', 'reviewed result')
        (self.root / '.claude/skills/newskill').mkdir(parents=True, exist_ok=True)
        self.git('mv', o, '.claude/skills/newskill/SKILL.md')
        d = ac.freeze(sc, {'auto_delivered': True})
        self.assertEqual(d['contract']['mechanical_moves'], {})
        self.assertIn('.claude/skills/newskill/SKILL.md', d['contract']['delivered'])   # audited as PROME's

    def test_r2_9_a_move_never_carries_a_mode_change(self):
        self.rebase_with(('PROME/tools/x.sh', 'echo\n'))
        self.write('PROME/result', 'reviewed result')
        (self.root / 'PROME/archive').mkdir(parents=True, exist_ok=True)
        (self.root / 'PROME/tools/x.sh').rename(self.root / 'PROME/archive/x.sh')
        (self.root / 'PROME/archive/x.sh').chmod(0o755)
        d = ac.freeze(sc, {'auto_delivered': True})
        self.assertEqual(d['contract']['mechanical_moves'], {})

    def test_r2_4_a_hook_that_edits_the_index_refuses(self):
        hooks = self.root / 'hooks'; hooks.mkdir()
        (hooks / 'pre-commit').write_text('#!/bin/sh\necho extra > /dev/null; git update-index --add --cacheinfo 100644,$(echo x | git hash-object -w --stdin),PROME/sneak\n')
        (hooks / 'pre-commit').chmod(0o755)
        self.git('config', 'core.hooksPath', 'hooks')
        self.freeze(); self.reviewed(); head = self.git('rev-parse', 'HEAD')
        with self.assertRaisesRegex(ValueError, 'changed the index'):
            ac.deliver(sc, self.msg())
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)

    # ---- listing (what ARGUS reads)
    def test_listing_names_candidate_moves_and_reuse(self):
        o, dst = 'PROME/inbox/2026-10-31_from-WALTER_x.md', 'PROME/inbox/processed/2026-10-31_from-WALTER_x.md'
        self.rebase_with((o, 'packet\n'))
        self.write('PROME/result', 'reviewed result')
        (self.root / 'PROME/inbox/processed').mkdir(parents=True, exist_ok=True); self.git('mv', o, dst)
        d = self.freeze()
        buf = io.StringIO()
        with redirect_stdout(buf):
            sc.main(['--json'])
        j = json.loads(buf.getvalue())
        self.assertEqual(j['candidate'], d['candidate']['sha'][:9])
        self.assertIn(dst, j['mechanical_moves'])
        buf = io.StringIO()
        with redirect_stdout(buf):
            sc.main([])
        self.assertIn(f"..{d['candidate']['sha'][:9]} -- <path>", buf.getvalue())


if __name__ == '__main__':
    unittest.main()
