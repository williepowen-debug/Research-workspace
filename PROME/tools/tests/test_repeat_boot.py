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
        old=self.state.read_bytes()
        def racing_page(*args):
            result=reader.page(*args)
            (self.root/'CLAUDE.md').write_text('changed during read\n')
            return result
        with self.assertRaisesRegex(ValueError,'changed during read'):
            reuse.read_with_state(self.user,racing_page,self.state,'context-A',reuse=True)
        self.assertEqual(self.state.read_bytes(),old)

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
        (board/'SIG-W-20260921-001.md').write_text('---\naction: [OTHER]\n---\n# old\n')
        command=[sys.executable,'-B',str(script)]
        first=subprocess.run(command,cwd=self.root,capture_output=True,text=True)
        self.assertEqual(first.returncode,0)
        (board/'SIG-W-20260921-002.md').write_text('---\naction: [PROME]\n---\n# new action\n')
        second=subprocess.run(command,cwd=self.root,capture_output=True,text=True)
        self.assertEqual(second.returncode,1);self.assertIn('new action',second.stdout)
        self.assertEqual(cursor.read_text(),'SIG-W-20260921-001\n')


if __name__=='__main__': unittest.main()
