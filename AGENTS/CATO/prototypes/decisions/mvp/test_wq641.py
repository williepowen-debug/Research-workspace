"""WQ-641 regressions in disposable repositories; never live operator answers."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import unittest
from unittest.mock import patch

import app
import authorization
import notification_hook
from notifications import Notifications, process_identity
import owner_receipt
from pilot_files import encoded, read_receipts
from queue_store import open_rows
import test_wq638 as fixtures

class ReturnTests(unittest.TestCase):
    def fixture(self):
        f=fixtures.OptionATests();f.setUp();self.addCleanup(f.doCleanups);return f

    def mutate(self,f,case):
        path='PROME/proposals/fixture-options.md'
        if case=='pointer':
            new='PROME/proposals/new-options.md';f.text=f.text.replace(path,new)
            f.options['confirmation'].update(mode='chat',scope='trade')
            f.options['queue_row_sha256']=hashlib.sha256(open_rows(f.text)['901']['row'].encode()).hexdigest()
            f.put(new,'```decisions-options\n'+json.dumps(f.options)+'\n```\n')
        elif case=='trade_row':
            f.text=f.text.replace('A: one task; B: no task.','Sell the held position.').replace(' <!-- decisions-options: '+path+' -->','')
        elif case=='closed':f.text='\n'.join(x for x in f.text.splitlines() if not x.startswith('| 901 |'))+'\n'
        elif case=='waiting':f.text=f.text.replace('Exact caveat','WAITING on Bob')
        elif case in {'policy_before','policy_after'}:
            f.options['confirmation'].update(mode='chat',scope='trade')
            f.put(path,'```decisions-options\n'+json.dumps(f.options)+'\n```\n')
        elif case=='recommendation':
            f.options['recommended_choice_id']='B'
            f.put(path,'```decisions-options\n'+json.dumps(f.options)+'\n```\n')
        f.put('PROME/WILL_QUEUE.md',f.text);f.commit(publish=True)

    def test_all_stale_cases_with_and_without_received_refuse(self):
        for received in (False,True):
            for case in ('pointer','trade_row','closed','policy_after','recommendation','waiting','policy_before'):
                with self.subTest(received=received,case=case):
                    f=self.fixture();e=f.answer()
                    if not received:f.receive=lambda event:None
                    if case in {'policy_after','recommendation','waiting'}:
                        ref=f.ruling(e);self.mutate(f,case)
                    else:
                        self.mutate(f,case);ref=f.ruling(e)
                    with self.assertRaises(ValueError):owner_receipt.prepare(f.repo,e,'integrated',ruling=ref,app_only=True)

    def test_prepare_refreshes_remote_before_current_check(self):
        f=self.fixture();e=f.answer();ref=f.ruling(e);old=f.git('rev-parse','origin/master').strip()
        self.mutate(f,'pointer');new=f.git('rev-parse','origin/master').strip()
        f.git('update-ref','refs/remotes/origin/master',old)
        with self.assertRaises(ValueError):owner_receipt.prepare(f.repo,e,'integrated',ruling=ref,app_only=True)
        self.assertEqual(f.git('rev-parse','origin/master').strip(),new)

    def test_historical_valid_receipt_survives_later_change_and_fallback(self):
        f=self.fixture();e=f.answer();ref=f.ruling(e)
        receipt=owner_receipt.prepare(f.repo,e,'integrated',ruling=ref,app_only=True)
        f.put(f"PROME/decisions/receipts/{e['id']}/{receipt['id']}.json",encoded(receipt)+'\n');f.commit(publish=True)
        self.mutate(f,'pointer')
        r=json.loads(f.repo.read(app.ACCEPTANCE));r['app_only_enabled']=False
        f.put(app.ACCEPTANCE,json.dumps(r));f.commit(publish=True)
        self.assertEqual([r['state'] for r in read_receipts(f.repo,e)],['received','integrated'])

    def test_received_must_be_published_for_both_confirmation_modes(self):
        f=self.fixture();e=f.answer();f.receive=lambda event:None;ref=f.ruling(e)
        for app_only in (False,True):
            with self.assertRaisesRegex(ValueError,'prior published received'):
                owner_receipt.prepare(f.repo,e,'integrated',ruling=ref,confirmation=None if app_only else ref,app_only=app_only)
        owner_receipt.write_received(f.repo,e)
        with self.assertRaisesRegex(ValueError,'prior published received'):
            owner_receipt.prepare(f.repo,e,'integrated',ruling=ref,app_only=True)

    def test_fallback_blocks_app_only_in_ui_intake_and_prepare(self):
        f=self.fixture();e=f.answer();ref=f.ruling(e)
        r=json.loads(f.repo.read(app.ACCEPTANCE));r['app_only_enabled']=False
        f.put(app.ACCEPTANCE,json.dumps(r));f.commit(publish=True)
        self.assertTrue(owner_receipt.inspect_event(f.repo,e)['requires_chat_confirmation'])
        desk=app.Desk(f.repo,Path(f.tmp.name)/'desk',True)
        self.assertTrue(next(c for c in desk.display()['cards'] if c['wq_id']=='901')['requires_confirmation'])
        with self.assertRaisesRegex(ValueError,'every answer'):
            owner_receipt.prepare(f.repo,e,'integrated',ruling=ref,app_only=True)
        # A later activation must not upgrade an answer made in fallback mode.
        r['app_only_enabled']=True;r['app_only_since']='2099-01-01T00:00:00+00:00'
        f.put(app.ACCEPTANCE,json.dumps(r));f.commit(publish=True)
        self.assertFalse(authorization.app_only_enabled(f.repo,e))

    def test_malformed_policy_is_local_and_good_card_can_be_answered(self):
        f=self.fixture();f.source();f.enable_app()
        desk=app.Desk(f.repo,Path(f.tmp.name)/'desk',True)
        for key,value in [('mode',[]),('scope',{}),('mode',False)]:
            with self.subTest(key=key,value=value):
                good=dict(f.options['confirmation']);f.options['confirmation'][key]=value
                f.put('PROME/proposals/fixture-options.md','```decisions-options\n'+json.dumps(f.options)+'\n```\n');f.commit(publish=True)
                state=desk.display();cards={c['wq_id']:c for c in state['cards']}
                self.assertEqual(state['errors'],[]);self.assertEqual(len(state['source_errors']),1)
                self.assertFalse(cards['901']['can_respond']);self.assertTrue(cards['902']['can_respond'])
                f.options['confirmation']=good
        c=cards['902'];r=f.request(unit_id='902.queue',display_hash=c['hash'],note='Fixture task response')
        self.assertEqual(desk.save(r)['request']['note'],'Fixture task response')

    def test_noninteractive_hook_returns_without_claiming_listener(self):
        f=self.fixture();state=Path(f.tmp.name)/'hook'
        payload=dict(cwd=str(f.root/'PROME'),session_id='headless',hook_event_name='SessionStart')
        with patch('notification_hook.interactive_parent',return_value=False):
            before=time.monotonic()
            self.assertEqual(notification_hook.run(payload,f.root,state,parent=process_identity(os.getpid())),0)
            self.assertLess(time.monotonic()-before,1)
        self.assertEqual(Notifications(state).status()['state'],'unknown')

    def test_print_mode_with_terminal_stdin_is_still_headless(self):
        import pty
        master,slave=pty.openpty()
        self.addCleanup(os.close,master);self.addCleanup(os.close,slave)
        code="import sys,os;sys.path.insert(0,sys.argv[1]);from notifications import interactive_parent,process_identity;print(interactive_parent(process_identity(os.getpid())))"
        result=subprocess.check_output([sys.executable,'-c',code,str(Path(__file__).parent),'--print'],stdin=slave,text=True,timeout=3)
        self.assertEqual(result.strip(),'False')

    def test_session_turnover_rearms_without_new_tool_and_old_end_is_harmless(self):
        f=self.fixture();state=Path(f.tmp.name)/'hook';q=Notifications(state);children=[]
        self.addCleanup(lambda:[p.terminate() for p in children if p.poll() is None])
        code='''import sys,json\nfrom pathlib import Path\nsys.path.insert(0,sys.argv[1])\nimport notification_hook\nraise SystemExit(notification_hook.run(json.loads(sys.argv[2]),Path(sys.argv[3]),Path(sys.argv[4]),parent=json.loads(sys.argv[5]),interactive=True,poll=float(sys.argv[6]),lifetime=8))'''
        def start(session,poll=.04):
            payload=dict(cwd=str(f.root/'PROME'),session_id=session,hook_event_name='SessionStart')
            p=subprocess.Popen([sys.executable,'-c',code,str(Path(__file__).parent),json.dumps(payload),str(f.root),str(state),json.dumps(process_identity(os.getpid())),str(poll)]);children.append(p);return p
        def wait_for(session):
            deadline=time.monotonic()+4
            while time.monotonic()<deadline:
                with q.connect() as db:r=db.execute('SELECT * FROM listener').fetchone()
                if r and r['session']==session and q.status()['state']=='listening':return
                time.sleep(.025)
            self.fail('New session did not acquire a live listener')
        a=start('old',1);wait_for('old')
        b=start('new');wait_for('new');q.end('old')
        self.assertEqual(q.status()['state'],'listening');self.assertEqual(a.wait(timeout=3),0)
        q.end('new');self.assertEqual(b.wait(timeout=3),0);self.assertEqual(q.status()['state'],'offline')

if __name__=='__main__':unittest.main()
