"""Phase 4 acceptance: isolated read receipts and non-advancing repeat checks."""
import contextlib
import datetime as dt
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
REPO = TOOLS.parents[1]


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, TOOLS / filename)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


reader = load('repeat_reader', 'boot_read.py')
reuse = load('repeat_reuse', 'boot_reuse.py')
session = load('repeat_session', 'boot_session.py')
gate = load('repeat_gate', 'prome_gate.py')


class Fixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='repeat-boot-')
        self.addCleanup(self.tmp.cleanup)
        self.area = Path(self.tmp.name)
        self.root = self.area / 'repo'
        self.root.mkdir()
        self.state = self.area / 'reads.json'
        self.user = self.root / 'USER.md'
        for name in reuse.BASIS:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('fixture ' + name + '\n')
        self.user.write_text('α🧭 retained instructions\n' * 600)
        for name in ('boot_read.py', 'boot_reuse.py', 'boot_session.py'):
            shutil.copyfile(TOOLS / name, self.root / 'PROME/tools' / name)
        for module in (reuse, session, gate):
            self.enterContext(patch.object(module, 'ROOT', self.root))
        self.enterContext(patch.object(reuse, 'today', return_value='2026-09-21'))

    def call(self, path=None, **kwargs):
        return reuse.read_with_state(path or self.user, reader.page, self.state,
                                     kwargs.pop('context_id', 'context-A'), **kwargs)

    def consume(self, path=None):
        offset, digest, output = 0, None, []
        while True:
            result = self.call(path, offset=offset, expected_sha=digest)
            output.append(result['text'])
            if result['eof']:
                return result['sha256'], ''.join(output)
            offset, digest = result['next_offset'], result['sha256']

    def acknowledged(self, path=None):
        digest, text = self.consume(path)
        self.assertEqual(self.call(path, acknowledge=True, expected_sha=digest)['read_kind'], 'ACKNOWLEDGED')
        return digest, text

    def complete_boot(self, rc=0):
        run = self.area / 'boot'
        run.mkdir()
        common = {'repository': str(self.root), 'mode':'boot'}
        (run/'attempt.json').write_text(json.dumps({**common,'attempted_at':'2020-01-01T00:00:00+00:00'}))
        (run/'completed.json').write_text(json.dumps({**common,'returncode':rc,'incomplete':rc==2}))
        (run/'gate.txt').write_text('historical mechanical output\n')
        return run

    def quiet(self, fn, *args, **kwargs):
        out=io.StringIO()
        with contextlib.redirect_stdout(out):
            rc=fn(*args, **kwargs)
        return rc,out.getvalue()


class ReadReceipts(Fixture):
    def test_acknowledged_full_read_reuses_only_retained_context(self):
        digest, text=self.acknowledged()
        self.assertEqual(text,self.user.read_text())
        result=self.call(reuse=True)
        self.assertEqual(result['read_kind'],'REUSED_IN_CONTEXT')
        self.assertEqual(result['sha256'],digest)
        self.assertEqual(result['text'],'')
        self.assertIn('fresh boot checks',result['limit'])
        self.assertEqual(self.call(reuse=True,context_id='new-context')['read_kind'],'FULL')

    def test_eof_emission_without_acknowledgement_is_not_reusable(self):
        self.consume()
        self.assertEqual(self.call(reuse=True)['read_kind'],'FULL')

    def test_partial_last_page_seek_and_missing_digest_cannot_acknowledge(self):
        first=self.call()
        with self.assertRaises(ValueError):
            self.call(acknowledge=True,expected_sha=first['sha256'])
        end=reader.page(self.user)['sha256']
        self.call(offset=len(self.user.read_text())-2,expected_sha=end)
        with self.assertRaises(ValueError):
            self.call(acknowledge=True,expected_sha=end)
        self.consume()
        with self.assertRaises(ValueError):
            self.call(acknowledge=True)

    def test_each_document_requires_its_own_acknowledgement(self):
        self.acknowledged()
        boot=self.root/'PROME/BOOT.md'
        self.assertEqual(self.call(boot,reuse=True)['read_kind'],'FULL')
        self.assertEqual(self.call(reuse=True)['read_kind'],'REUSED_IN_CONTEXT')

    def test_changed_instruction_or_policy_invalidates_unchanged_document(self):
        for changed in ('PROME/BOOT.md','CLAUDE.md','PROME/registry/READS.tsv',
                        'PROME/tools/boot_read.py','PROME/tools/boot_reuse.py'):
            with self.subTest(changed=changed):
                self.acknowledged()
                path=self.root/changed
                path.write_text(path.read_text()+'amendment\n')
                self.assertEqual(self.call(reuse=True)['read_kind'],'FULL')

    def test_same_day_live_rulings_and_other_files_always_emit_current_text(self):
        self.acknowledged()
        for name in ('PROME/WILL_QUEUE.md','PROME/SCRATCH.md','HEARTBEAT.md',
                     'PROME/ACTIVE_DECISIONS.md','PROME/STATUS.md','PROME/HANDOFF.md'):
            path=self.root/name
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text('unconsumed ruling / action 1\n')
            self.assertEqual(self.call(path,reuse=True)['text'],path.read_text())
            path.write_text('new same-day ruling / action 2\n')
            self.assertEqual(self.call(path,reuse=True)['text'],path.read_text())

    def test_date_advance_forces_full_read_without_file_change(self):
        self.acknowledged()
        before=self.user.read_bytes()
        with patch.object(reuse,'today',return_value='2026-09-22'):
            self.assertEqual(self.call(reuse=True)['read_kind'],'FULL')
        self.assertEqual(self.user.read_bytes(),before)

    def test_missing_corrupt_wrong_repo_and_schema_baselines_fall_back(self):
        for bad in (None,'broken','[]','{}'):
            with self.subTest(bad=bad):
                self.acknowledged()
                if bad is None: self.state.unlink()
                else: self.state.write_text(bad)
                self.assertEqual(self.call(reuse=True)['read_kind'],'FULL')
        for field,value in [('repository','/other'),('version',99),('version',True),('context_id','other')]:
            self.acknowledged()
            data=json.loads(self.state.read_text());data[field]=value
            self.state.write_text(json.dumps(data))
            self.assertEqual(self.call(reuse=True)['read_kind'],'FULL')

    def test_missing_basis_and_missing_source_never_reuse(self):
        self.acknowledged()
        (self.root/'CLAUDE.md').unlink()
        self.assertEqual(self.call(reuse=True)['read_kind'],'FULL')
        self.user.unlink()
        with self.assertRaises(OSError): self.call(reuse=True)

    def test_symlink_alias_and_inside_repo_state_never_reuse(self):
        self.acknowledged()
        alias=self.area/'alias.md';alias.symlink_to(self.user)
        self.assertEqual(self.call(alias,reuse=True)['read_kind'],'FULL')
        with patch.object(self,'state',self.root/'state.json'):
            self.assertEqual(self.call(reuse=True)['read_kind'],'FULL')
        self.assertFalse((self.root/'state.json').exists())
        other=self.area/'other.md';other.write_text('new policy\n')
        self.user.unlink();self.user.symlink_to(other)
        self.assertEqual(self.call(reuse=True)['read_kind'],'FULL')

    def test_source_and_policy_mutation_during_read_refuse_receipt(self):
        self.acknowledged()
        def racing_page(*args):
            result=reader.page(*args)
            (self.root/'CLAUDE.md').write_text('changed during read\n')
            return result
        with self.assertRaisesRegex(ValueError,'changed during read'):
            reuse.read_with_state(self.user,racing_page,self.state,'context-A',reuse=True)
        state=json.loads(self.state.read_text())
        self.assertEqual(state['pending_policy_reads'],['CLAUDE.md'])
        self.assertEqual(state['reads'],{})

    def test_competing_state_writer_falls_back_without_modifying_receipt(self):
        self.acknowledged()
        old=self.state.read_bytes()
        with self.state.with_suffix('.json.lock').open('a') as lock:
            reuse.fcntl.flock(lock,reuse.fcntl.LOCK_EX|reuse.fcntl.LOCK_NB)
            result=self.call(reuse=True)
            self.assertEqual(result['read_kind'],'FULL')
            self.assertIn('busy',result['reuse_reason'])
        self.assertEqual(self.state.read_bytes(),old)

    def test_write_failure_cannot_acknowledge_and_missing_context_errors(self):
        digest,_=self.consume()
        with patch.object(reuse,'save_state',side_effect=OSError('fixture write failed')):
            with self.assertRaises(ValueError): self.call(acknowledge=True,expected_sha=digest)
        self.assertFalse(json.loads(self.state.read_text())['reads']['USER.md']['acknowledged'])
        with self.assertRaises(ValueError): self.call(context_id='')

    def test_cli_full_pages_acknowledgement_and_reuse(self):
        # Child derives ROOT from the copied tool path, never the live repo.
        command=[sys.executable,'-B',str(self.root/'PROME/tools/boot_read.py'),str(self.user),
                 '--read-state',str(self.state),'--context-id','cli-context']
        offset,digest=0,None
        while True:
            args=[] if not offset else ['--offset',str(offset),'--sha256',digest]
            p=subprocess.run(command+args,capture_output=True,text=True,check=True)
            row=json.loads(p.stdout)
            if row['eof']: break
            offset,digest=row['next_offset'],row['sha256']
        p=subprocess.run(command+['--ack-read','--sha256',row['sha256']],capture_output=True,text=True,check=True)
        self.assertEqual(json.loads(p.stdout)['read_kind'],'ACKNOWLEDGED')
        p=subprocess.run(command+['--reuse'],capture_output=True,text=True,check=True)
        self.assertEqual(json.loads(p.stdout)['read_kind'],'REUSED_IN_CONTEXT')


class PolicyRecovery(Fixture):
    def change(self, name, text='new instruction\n'):
        path = self.root / name
        path.write_text(path.read_text() + text)
        return path

    def test_changed_claude_is_delivered_and_user_ack_alone_cannot_restore_reuse(self):
        self.acknowledged()
        claude = self.change('CLAUDE.md')
        blocked = self.call(reuse=True)
        self.assertEqual(blocked['pending_policy_reads'], ['CLAUDE.md'])
        self.assertIn('Reuse blocked', blocked['recovery'])
        self.acknowledged()
        self.assertEqual(self.call(reuse=True)['read_kind'], 'FULL')
        self.acknowledged(self.root / 'PROME/BOOT.md')
        self.assertEqual(self.call(self.root / 'PROME/BOOT.md', reuse=True)['read_kind'], 'FULL')
        digest, text = self.consume(claude)
        self.assertEqual(text, claude.read_text())
        self.assertEqual(self.call(reuse=True)['pending_policy_reads'], ['CLAUDE.md'])
        ack = self.call(claude, acknowledge=True, expected_sha=digest)
        self.assertEqual(ack['pending_policy_reads'], [])
        self.acknowledged()
        self.assertEqual(self.call(reuse=True)['read_kind'], 'REUSED_IN_CONTEXT')
        # Policy recovery never turns CLAUDE itself into a reusable document.
        self.assertEqual(self.call(claude, reuse=True)['text'], claude.read_text())

    def test_changes_accumulate_across_date_and_reversion(self):
        self.acknowledged()
        claude = self.root / 'CLAUDE.md'
        original = claude.read_text()
        self.change('CLAUDE.md')
        self.call(reuse=True)
        self.change('AGENTS.md')
        claude.write_text(original)
        with patch.object(reuse, 'today', return_value='2026-09-22'):
            self.assertEqual(self.call(reuse=True)['pending_policy_reads'], ['AGENTS.md', 'CLAUDE.md'])
            self.acknowledged()
            self.acknowledged(claude)
            self.assertEqual(self.call(reuse=True)['pending_policy_reads'], ['AGENTS.md'])
            self.acknowledged(self.root / 'AGENTS.md')
            self.acknowledged()
            self.assertEqual(self.call(reuse=True)['read_kind'], 'REUSED_IN_CONTEXT')

    def test_every_basis_change_requires_its_own_read_and_ack(self):
        self.acknowledged()
        for name in reuse.BASIS:
            with self.subTest(name=name):
                path = self.change(name)
                self.assertEqual(self.call(reuse=True)['pending_policy_reads'], [name])
                self.acknowledged(path)
                self.acknowledged()
                self.assertEqual(self.call(reuse=True)['read_kind'], 'REUSED_IN_CONTEXT')
                if name not in reuse.ELIGIBLE:
                    self.assertEqual(self.call(path, reuse=True)['read_kind'], 'FULL')

    def test_pending_policy_requires_contiguous_pages_and_correct_digest(self):
        self.acknowledged()
        claude = self.change('CLAUDE.md', 'unread rule\n' * 1800)
        self.call(reuse=True)
        first = self.call(claude)
        self.assertFalse(first['eof'])
        with self.assertRaises(ValueError):
            self.call(claude, acknowledge=True, expected_sha=first['sha256'])
        self.call(claude, offset=len(claude.read_text())-1, expected_sha=first['sha256'])
        with self.assertRaises(ValueError):
            self.call(claude, acknowledge=True, expected_sha=first['sha256'])
        digest, _ = self.consume(claude)
        for wrong in (None, '0' * 64):
            with self.assertRaises(ValueError):
                self.call(claude, acknowledge=True, expected_sha=wrong)
        self.assertEqual(json.loads(self.state.read_text())['pending_policy_reads'], ['CLAUDE.md'])
        self.assertEqual(self.call(claude, acknowledge=True, expected_sha=digest)['pending_policy_reads'], [])

    def test_legacy_and_corrupt_receipts_require_full_basis_recovery(self):
        for kind in ('legacy', 'corrupt', 'empty', 'missing-hash', 'bad-pending'):
            with self.subTest(kind=kind):
                self.acknowledged()
                old = json.loads(self.state.read_text())
                if kind == 'legacy':
                    old = {k: old[k] for k in ('repository', 'context_id', 'date', 'reads')}
                    old.update(version=1, policy_sha256='0' * 64)
                elif kind == 'empty': old = {}
                elif kind == 'missing-hash': old['policy_hashes'].pop('CLAUDE.md')
                elif kind == 'bad-pending': old['pending_policy_reads'] = [None]
                self.state.write_text('broken' if kind == 'corrupt' else json.dumps(old))
                self.assertEqual(set(self.call(reuse=True)['pending_policy_reads']), set(reuse.BASIS))
                self.acknowledged()
                self.assertIn('CLAUDE.md', self.call(reuse=True)['pending_policy_reads'])
                for name in reuse.BASIS:
                    self.acknowledged(self.root / name)
                self.assertEqual(self.call(reuse=True)['read_kind'], 'REUSED_IN_CONTEXT')

    def test_wrong_context_and_external_alias_cannot_acknowledge_pending_path(self):
        self.acknowledged()
        claude = self.change('CLAUDE.md')
        digest, _ = self.consume(claude)
        before = self.state.read_bytes()
        alias = self.area / 'CLAUDE.md'
        alias.symlink_to(claude)
        for path, kwargs in ((alias, {}), (claude, {'context_id': 'different-context'})):
            with self.assertRaises(ValueError):
                self.call(path, acknowledge=True, expected_sha=digest, **kwargs)
            self.assertEqual(self.state.read_bytes(), before)

    def test_missing_policy_and_failed_ack_write_preserve_pending(self):
        self.acknowledged()
        claude = self.change('CLAUDE.md')
        digest, _ = self.consume(claude)
        before = self.state.read_bytes()
        with patch.object(reuse, 'save_state', side_effect=OSError('fixture failure')):
            with self.assertRaises(ValueError):
                self.call(claude, acknowledge=True, expected_sha=digest)
        self.assertEqual(self.state.read_bytes(), before)
        claude.unlink()
        self.assertEqual(self.call(reuse=True)['read_kind'], 'FULL')
        self.assertEqual(self.state.read_bytes(), before)
        with self.assertRaises(ValueError):
            self.call(claude, acknowledge=True, expected_sha=digest)

    def test_policy_race_during_ack_accumulates_new_debt_on_retry(self):
        self.acknowledged()
        claude = self.change('CLAUDE.md')
        digest, _ = self.consume(claude)
        agents = self.root / 'AGENTS.md'
        original = agents.read_text()
        def race(*args):
            result = reader.page(*args)
            self.change('AGENTS.md')
            return result
        with self.assertRaisesRegex(ValueError, 'changed during read'):
            reuse.read_with_state(claude, race, self.state, 'context-A',
                                  acknowledge=True, expected_sha=digest)
        self.assertEqual(json.loads(self.state.read_text())['pending_policy_reads'], ['AGENTS.md', 'CLAUDE.md'])
        agents.write_text(original)
        self.assertEqual(self.call(reuse=True)['pending_policy_reads'], ['AGENTS.md', 'CLAUDE.md'])
        self.acknowledged(claude)
        self.acknowledged()
        self.assertEqual(self.call(reuse=True)['pending_policy_reads'], ['AGENTS.md'])

    def test_failed_ack_or_page_cannot_erase_detected_policy_change_after_reversion(self):
        for failure in ('ack', 'digest', 'offset'):
            with self.subTest(failure=failure):
                digest, _ = self.acknowledged()
                claude = self.root / 'CLAUDE.md'
                original = claude.read_text()
                self.change('CLAUDE.md')
                kwargs = {'acknowledge': True, 'expected_sha': digest} if failure == 'ack' else (
                    {'expected_sha': '0' * 64} if failure == 'digest' else {'offset': 1})
                with self.assertRaises(ValueError): self.call(**kwargs)
                self.assertEqual(json.loads(self.state.read_text())['pending_policy_reads'], ['CLAUDE.md'])
                claude.write_text(original)
                self.acknowledged()
                self.assertEqual(self.call(reuse=True)['pending_policy_reads'], ['CLAUDE.md'])
                self.acknowledged(claude)

    def test_policy_change_during_failed_page_is_preserved_and_save_failure_refuses(self):
        self.acknowledged()
        claude = self.root / 'CLAUDE.md'
        original = claude.read_text()
        def race(*args):
            self.change('CLAUDE.md')
            raise ValueError('fixture page refused')
        with self.assertRaisesRegex(ValueError, 'changed during read'):
            reuse.read_with_state(self.user, race, self.state, 'context-A')
        claude.write_text(original)
        with patch.object(reuse, 'save_state', side_effect=OSError('fixture failure')):
            with self.assertRaisesRegex(ValueError, 'recovery not saved'):
                self.call(reuse=True)
        self.acknowledged()
        self.assertEqual(self.call(reuse=True)['pending_policy_reads'], ['CLAUDE.md'])


class Refresh(Fixture):
    def test_interrupted_first_attempt_never_launches_advancing_child_twice(self):
        run=self.area/'first-boot'
        with patch.object(session.subprocess,'run',return_value=subprocess.CompletedProcess([], -9)) as spy:
            self.assertEqual(self.quiet(session.run_once,run)[0],2)
            self.assertEqual(self.quiet(session.run_once,run)[0],2)
            self.assertEqual(self.quiet(session.run_refresh,run)[0],2)
            self.assertEqual(spy.call_count,1)
        self.assertFalse((run/'completed.json').exists())

    def test_cli_refresh_dispatch_keeps_boot_checks_nonadvancing(self):
        with patch.object(sys,'argv',['prome_gate.py','refresh','--log-dir',str(self.area/'logs')]), \
             patch.object(gate,'mode_boot') as boot,patch.object(gate,'mode_closeout') as closeout:
            self.assertEqual(self.quiet(gate.main)[0],0)
            boot.assert_called_once_with(advance_board=False)
            closeout.assert_not_called()

    def test_completed_original_refresh_preserves_receipt_and_uses_refresh_mode(self):
        run=self.complete_boot()
        before={p.name:p.read_bytes() for p in run.iterdir()}
        def child(cmd,**kwargs):
            self.assertEqual(cmd[2],'refresh')
            self.assertNotIn('--advance',cmd)
            kwargs['stdout'].write('fresh check output\n')
            return subprocess.CompletedProcess(cmd,0)
        with patch.object(session.subprocess,'run',side_effect=child) as spy:
            rc,out=self.quiet(session.run_refresh,run)
            self.assertEqual(rc,0)
            self.assertEqual(spy.call_count,1)
        for name,content in before.items(): self.assertEqual((run/name).read_bytes(),content)
        refreshes=list(run.glob('refresh-*'))
        report=json.loads((refreshes[0]/'completed.json').read_text())
        self.assertFalse(report['board_advance'])
        self.assertIn('Manual/private steps still required',out)

    def test_incomplete_missing_malformed_wrong_owner_never_launch(self):
        run=self.complete_boot(rc=2)
        originals=(run/'attempt.json').read_text(),(run/'completed.json').read_text()
        variants=[('completed.json',None),('completed.json','[]'),('completed.json',originals[1]),
                  ('attempt.json','{}'),('attempt.json','broken')]
        for name,content in variants:
            (run/'attempt.json').write_text(originals[0]);(run/'completed.json').write_text(originals[1])
            if content is None: (run/name).unlink()
            else: (run/name).write_text(content)
            with patch.object(session.subprocess,'run') as spy:
                rc,out=self.quiet(session.run_refresh,run)
                self.assertEqual(rc,2);spy.assert_not_called()
            self.assertFalse(list(run.glob('refresh-*')))
        with patch.object(session.subprocess,'run') as spy:
            self.assertEqual(self.quiet(session.run_refresh,self.area/'absent')[0],2)
            spy.assert_not_called()

    def test_plain_retry_still_never_advances_again(self):
        run=self.complete_boot()
        with patch.object(session.subprocess,'run') as spy:
            self.assertEqual(self.quiet(session.run_once,run)[0],0)
            spy.assert_not_called()
        (run/'completed.json').unlink()
        with patch.object(session.subprocess,'run') as spy:
            self.assertEqual(self.quiet(session.run_once,run)[0],2)
            spy.assert_not_called()

    def test_interrupted_refresh_does_not_rewrite_original_or_complete_it(self):
        run=self.complete_boot();before=(run/'completed.json').read_bytes()
        with patch.object(session.subprocess,'run',return_value=subprocess.CompletedProcess([], -9)):
            self.assertEqual(self.quiet(session.run_refresh,run)[0],2)
        self.assertEqual((run/'completed.json').read_bytes(),before)
        self.assertFalse(any(p.exists() for p in run.glob('refresh-*/completed.json')))

    def test_refresh_check_inventory_matches_boot_except_board_advance(self):
        def capture(advance):
            calls=[]
            with patch.object(gate,'run_script',side_effect=lambda *a,**k:calls.append(('script',a,k))), \
                 patch.object(gate,'run_capability',side_effect=lambda *a,**k:calls.append(('cap',a,k))), \
                 patch.object(gate,'guard',side_effect=lambda *a,**k:calls.append(('guard',a,k))), \
                 patch.object(gate,'SESSION_JSON',None):
                gate.mode_boot(advance_board=advance)
            return calls
        normal,fresh=capture(True),capture(False)
        self.assertEqual(len(normal),len(fresh))
        differences=[]
        for a,b in zip(normal,fresh):
            if a!=b: differences.append((a,b))
        self.assertEqual(len(differences),1)
        a,b=differences[0]
        self.assertEqual(a[1][1],'board_scan')
        self.assertEqual(a[1][2][:-1],b[1][2]);self.assertEqual(a[1][2][-1],'--advance')
        self.assertTrue(any('corrections_boot_check.py' in str(call) for call in fresh))

    def test_unchanged_gate_crossing_date_is_reassessed_by_refresh(self):
        path=self.root/'PROME/GATES.tsv'
        row=['GATE-X','fixture','fixture','fixture','fixture','LIVE','2026-09-21',
             'fixture','NONE','INSTRUMENT','fixture','2026-09-21']
        path.write_text('\t'.join(row)+'\n');before=path.read_bytes()
        def only_gate(fn,*args):
            if fn is gate.check_gates_tsv: fn(*args)
        for day,want in [('2026-09-21',0),('2026-09-22',1)]:
            class ClockDate(dt.date):
                @classmethod
                def today(cls): return cls.fromisoformat(day)
            with patch.object(gate.dt,'date',ClockDate),patch.object(gate,'results',[]), \
                 patch.object(gate,'guard',side_effect=only_gate), \
                 patch.object(gate,'run_script'),patch.object(gate,'run_capability'):
                gate.mode_boot(advance_board=False)
                self.assertEqual(gate.aggregate_rc(gate.results,[]),want)
        self.assertEqual(path.read_bytes(),before)

    def test_new_same_day_board_action_is_read_without_cursor_advance(self):
        script=self.root/'PROME/tools/board_scan.py'
        shutil.copyfile(TOOLS/'board_scan.py',script)
        subprocess.run(['git','init','-q',str(self.root)],check=True)
        board=self.root/'BOARD';board.mkdir()
        cursor=self.root/'PROME/state/board_cursor.txt';cursor.parent.mkdir();cursor.write_text('SIG-W-20260921-001\n')
        # 2026-09-30 (CATO RC1): the scanner reads only PUBLISHED signals — committed, with complete
        # stamped metadata — so the fixture publishes each file the way WALTER does.
        def publish(num,action,head):
            sid=f'SIG-W-20260921-{num:03d}'
            (board/f'{sid}.md').write_text(f'---\nsignal_id: {sid}\ntime_dispatched: 2026-09-21T12:00:00Z\naction: [{action}]\ninfo: []\n---\n# {head}\n')
            subprocess.run(['git','-C',str(self.root),'add',f'BOARD/{sid}.md'],check=True)
            subprocess.run(['git','-C',str(self.root),'-c','user.email=f@example.invalid','-c','user.name=f','commit','-q','-m',sid],check=True)
        publish(1,'OTHER','old')
        command=[sys.executable,'-B',str(script)]
        # the consumed ledger is never rebuilt implicitly: the fixture runs the one-time migration
        seed=subprocess.run(command+['--seed-from-cursor'],cwd=self.root,capture_output=True,text=True)
        self.assertEqual(seed.returncode,0,seed.stderr)
        first=subprocess.run(command,cwd=self.root,capture_output=True,text=True)
        self.assertEqual(first.returncode,0)
        publish(2,'PROME','new action')
        second=subprocess.run(command,cwd=self.root,capture_output=True,text=True)
        self.assertEqual(second.returncode,1);self.assertIn('new action',second.stdout)
        self.assertEqual(cursor.read_text(),'SIG-W-20260921-001\n')


if __name__=='__main__': unittest.main()
