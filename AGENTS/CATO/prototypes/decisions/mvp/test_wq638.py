"""Option A counterexamples, entirely disposable Git repositories and local state."""
from datetime import datetime, timezone
import io
import json
import os
from pathlib import Path
from contextlib import redirect_stderr
from unittest.mock import patch
import unittest

import authorization
import delivery
import notification_hook
from notifications import Notifications, process_identity
import owner_receipt
from pilot_files import encoded, read_receipts
from test_desk import DeskTests

class OptionATests(unittest.TestCase):
    setUp=DeskTests.setUp
    git=DeskTests.git
    put=DeskTests.put
    commit=DeskTests.commit
    request=DeskTests.request
    install_options=DeskTests.install_options

    def source(self, mode='app', scope='reversible_internal', recommended='A'):
        path=self.install_options()
        self.options.update(schema_version='decisions-options/2', recommended_choice_id=recommended,
                            confirmation={'mode':mode,'scope':scope,'reason':'Owner-reviewed fixture scope.'})
        self.put(path,'```decisions-options\n'+json.dumps(self.options)+'\n```\n')
        self.commit(publish=True)
        self.display=self.store.display()
        return path

    def enable_app(self):
        import app
        self.put('PROME/reports/fixture-review.md','Fixture review only')
        self.commit(publish=True)
        acceptance=dict(schema_version='decisions-app-acceptance/1',queue_responses=True,
                        matching_chat_confirmation=True,confirmation_policy='explicit-reversible-internal/1',
                        app_only_enabled=True,app_only_since='2026-01-01T00:00:00+00:00',build_hashes=app.build_hashes(),
                        independent_review=dict(path='PROME/reports/fixture-review.md',commit=self.git('rev-parse','HEAD').strip()))
        self.put(app.ACCEPTANCE,json.dumps(acceptance));self.commit(publish=True)

    def receive(self,e):
        path=owner_receipt.write_received(self.repo,e)
        self.commit(publish=True)
        return path

    def answer(self):
        self.source()
        self.enable_app()
        event=self.store.save(self.request(action='choose',choice_id='A',note='Close it, but record the miss.\nKeep the caveat.'))
        delivery.deliver(self.repo,event)
        return event

    def ruling(self,event,**changes):
        proof=dict(schema_version='decisions-app-authorization/1',response_id=event['id'],response_sha256=event['sha256'],
                   scope='reversible_internal',conditions_within_scope=True,no_chat_conflict=True,
                   readback_at=datetime.now(timezone.utc).isoformat(),readback_text=authorization.readback_text(event))
        proof.update(changes)
        if not read_receipts(self.repo,event):self.receive(event)
        path='PROME/proposals/fixture-RULED.md'
        self.put(path,'Fixture ruling\n```decisions-app-authorization\n'+json.dumps(proof)+'\n```\n');self.commit(publish=True)
        return dict(path=path,commit=self.git('rev-parse','HEAD').strip())

    def test_app_only_exact_conditions_and_published_receipt(self):
        e=self.answer()
        self.assertFalse(self.display['requires_confirmation'])
        self.assertEqual(e['display']['record']['units'][0]['proposal']['recommendation']['option_id'],'A')
        self.assertIn('App-only eligible',delivery.packet_text(e))
        rec=owner_receipt.prepare(self.repo,e,'integrated',ruling=self.ruling(e),app_only=True)
        path=f"PROME/decisions/receipts/{e['id']}/{rec['id']}.json"
        self.put(path,encoded(rec)+'\n');self.commit(publish=True)
        self.assertEqual(read_receipts(self.repo,e)[-1]['authorization_basis'],'app')
        self.assertIsNone(rec['chat_confirmation'])

    def test_conflicting_chat_out_of_scope_conditions_and_missing_words_refuse(self):
        e=self.answer()
        for changes in [dict(no_chat_conflict=False),dict(conditions_within_scope=False),dict(readback_text='Approved'),dict(response_id='0'*32)]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                owner_receipt.prepare(self.repo,e,'integrated',ruling=self.ruling(e,**changes),app_only=True)

    def test_changed_policy_refuses(self):
        e=self.answer()
        self.options['confirmation']['mode']='chat'
        self.put(e['display']['options_source']['path'],'```decisions-options\n'+json.dumps(self.options)+'\n```\n')
        self.commit(publish=True)
        with self.assertRaisesRegex(ValueError,'changed'):
            owner_receipt.prepare(self.repo,e,'integrated',ruling=self.ruling(e),app_only=True)

    def test_superseded_answer_refuses(self):
        e=self.answer()
        newer=self.store.save(self.request(supersedes=e['id'],action='reply',note='Actually disapprove.'))
        delivery.deliver(self.repo,newer)
        with self.assertRaisesRegex(ValueError,'Superseded'):
            owner_receipt.prepare(self.repo,e,'integrated',ruling=self.ruling(e),app_only=True)

    def test_legacy_stays_chat_required(self):
        self.install_options()
        self.assertTrue(self.display['requires_confirmation'])
        e=self.store.save(self.request())
        self.assertIn('matching operator confirmation',delivery.packet_text(e))
        with self.assertRaisesRegex(ValueError,'matching chat'):
            authorization.validate_app_integration(self.repo,e,None,None)

    def test_all_protected_scopes_refuse_app_classification(self):
        for scope in authorization.SCOPES-{'reversible_internal'}:
            with self.subTest(scope=scope),self.assertRaises(ValueError):
                authorization.validate_policy(dict(mode='app',scope=scope,reason='test'))
        self.assertTrue(authorization.needs_chat({}))

    def test_invalid_recommendation_refuses_instead_of_guessing(self):
        with self.assertRaisesRegex(ValueError,'Recommendation'):
            self.source(recommended='C')

    def test_no_recommendation_is_explicit(self):
        self.source(recommended=None)
        self.assertIsNone(self.display['snapshot']['record']['units'][0]['proposal']['recommendation']['option_id'])

    def test_notify_only_published_idempotent_and_no_receipt(self):
        self.source();e=self.store.save(self.request())
        q=Notifications(Path(self.tmp.name)/'notify')
        with self.assertRaises(ValueError):q.enqueue(self.repo,e)
        delivery.deliver(self.repo,e)
        q.enqueue(self.repo,e);q.enqueue(self.repo,e)
        self.assertEqual(len(q.pending('session')),1)
        self.assertEqual(q.status()['state'],'unknown')
        self.assertEqual(read_receipts(self.repo,e),[])
        q.heartbeat('session',process_identity(os.getpid()),starting=True)
        self.assertEqual(q.status()['state'],'listening')
        q.end('session');self.assertFalse(q.heartbeat('session',process_identity(os.getpid())))
        self.assertEqual(q.status()['state'],'offline')

    def test_hook_emits_pointer_once_and_only_for_prome(self):
        e=self.answer();state=Path(self.tmp.name)/'notify';q=Notifications(state);q.enqueue(self.repo,e)
        payload=dict(cwd=str(self.root/'PROME'),session_id='fixture',hook_event_name='PostToolUse')
        out=io.StringIO()
        with redirect_stderr(out):
            result=notification_hook.run(payload,self.root,state,parent=process_identity(os.getpid()),lifetime=.05,poll=.01,interactive=True)
        self.assertEqual(result,2)
        self.assertIn(e['id'],out.getvalue());self.assertNotIn(e['request']['note'],out.getvalue())
        self.assertEqual(q.pending('fixture'),[]);self.assertEqual(len(q.pending('new-session')),1)
        self.assertEqual(read_receipts(self.repo,e),[])
        payload['cwd']=str(self.root/'AGENTS/CATO')
        self.assertEqual(notification_hook.run(payload,self.root,state),0)

if __name__=='__main__':unittest.main()

class RecoveryTests(OptionATests):
    def test_display_recovers_published_unnotified_answer(self):
        import app
        e=self.answer()
        desk=app.Desk(self.repo,Path(self.tmp.name)/'recovery',True)
        self.assertEqual(desk.notifications.pending('session'),[])
        with patch('app.accepted',return_value=(True,'')): desk.display()
        self.assertEqual([n['id'] for n in desk.notifications.pending('session')],[e['id']])
        with patch('app.accepted',return_value=(True,'')): desk.display()
        self.assertEqual(len(desk.notifications.pending('session')),1)

    def test_notification_db_failure_does_not_hide_delivered_answer(self):
        import app,sqlite3
        e=self.answer();desk=app.Desk(self.repo,Path(self.tmp.name)/'recovery',True)
        with patch('app.accepted',return_value=(True,'')),patch.object(desk.notifications,'connect',side_effect=sqlite3.OperationalError('locked')):
            state=desk.display()
        self.assertEqual(state['notification']['state'],'unknown')
        self.assertEqual(next(c for c in state['cards'] if c['wq_id']=='901')['delivery'],'delivered')
