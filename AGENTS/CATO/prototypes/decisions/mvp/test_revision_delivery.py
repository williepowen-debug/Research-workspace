"""Final-review R1 regressions; only disposable repositories and local stores."""
import json
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch
import uuid

import app
import delivery
from pilot_files import Repo
from queue_store import QueueStore, REPLIES, immutable_export
from store import digest
import test_desk as fixtures


class RevisionDeliveryTests(unittest.TestCase):
    git = fixtures.DeskTests.git
    put = fixtures.DeskTests.put
    commit = fixtures.DeskTests.commit
    request = fixtures.DeskTests.request

    def setUp(self):
        fixtures.DeskTests.setUp(self)
        accepted = patch('app.accepted', return_value=(True, ''))
        accepted.start(); self.addCleanup(accepted.stop)
        self.desk = app.Desk(self.repo, Path(self.tmp.name)/'desktop', True)
        self.store = self.desk.queue_store('901', True)
        self.display = self.store.display()

    def send(self, event):
        return self.desk.operate('/api/deliver', {'id': event['id']})

    def publish(self, path):
        self.git('add','--',path)
        self.git('commit','-qm','Fixture source update','--',path)
        self.git('push','-q')

    def test_unsent_revisions_deliver_latest_only_and_restore_on_fresh_clone(self):
        a = self.desk.save(self.request(note='First private draft'))
        b = self.desk.save(self.request(supersedes=a['id'], note='Second private draft'))
        c = self.desk.save(self.request(supersedes=b['id'], note='Final response'))
        with self.assertRaisesRegex(ValueError, 'latest saved'): self.send(a)
        result = self.send(c)
        self.assertEqual(self.git('show','--format=','--name-only',result['commit']).splitlines(),
                         sorted([delivery.event_path(c),result['packet']]))
        for draft in (a,b):
            self.assertEqual(delivery.delivery_state(self.repo,draft),'saved')
            self.assertFalse(self.repo.path(f"PROME/inbox/decisions-{draft['id']}-from-CATO.md").exists())
        before = self.git('rev-parse','HEAD'); self.send(c)
        self.assertEqual(before,self.git('rev-parse','HEAD'))
        clone=Path(self.tmp.name)/'fresh'
        subprocess.run(['git','clone','-q','-b','master',str(self.remote),str(clone)],check=True)
        for k,v in [('user.name','Fixture'),('user.email','fixture@example.invalid')]:
            subprocess.run(['git','config',k,v],cwd=clone,check=True)
        restored=QueueStore(Path(self.tmp.name)/'fresh.sqlite3',Repo(clone),'901',True)
        card=restored.display()
        self.assertEqual(card['last'],c)
        self.assertTrue(card['history_notes'])
        self.assertTrue(card['can_respond'])
        self.assertEqual(card['events'],[c])
        d=restored.save(self.request(display_hash=card['hash'],supersedes=c['id'],note='Fresh-machine revision'))
        delivery.deliver(Repo(clone),d,local_events=lambda:restored.responses()['events'])
        self.assertEqual(delivery.delivery_state(Repo(clone),d),'delivered')

    def test_unsent_task_deferral_then_report_done_delivers(self):
        task=self.desk.queue_store('902',True); card=task.display()
        a=self.desk.save(self.request(unit_id='902.queue',display_hash=card['hash'],action='defer',note='Later',revisit='After the filing'))
        b=self.desk.save(self.request(unit_id='902.queue',display_hash=card['hash'],supersedes=a['id'],action='report_done',note='Uploaded corrected report'))
        self.send(b)
        self.assertEqual(delivery.delivery_state(self.repo,b),'delivered')
        self.assertEqual(delivery.delivery_state(self.repo,a),'saved')

    def test_stale_refusal_then_current_terms_replacement_delivers(self):
        a=self.desk.save(self.request())
        self.put('PROME/WILL_QUEUE.md',self.text.replace('Exact caveat','New caveat'))
        self.publish('PROME/WILL_QUEUE.md')
        with self.assertRaises(ValueError): self.send(a)
        card=self.store.display()
        b=self.desk.save(self.request(display_hash=card['hash'],supersedes=a['id'],note='Answer to new terms'))
        self.send(b)
        self.assertEqual(delivery.delivery_state(self.repo,a),'saved')
        self.assertEqual(delivery.delivery_state(self.repo,b),'delivered')

    def test_refused_commit_then_revised_answer_delivers_without_sweeping_old_stage(self):
        a=self.desk.save(self.request(note='Rejected fixture wording'))
        hook=self.put('scripts/githooks/pre-commit','#!/bin/sh\necho "Fixture refusal" >&2\nexit 1\n')
        hook.chmod(0o755)
        with self.assertRaises(subprocess.CalledProcessError): self.send(a)
        staged=self.git('diff','--cached','--name-only').splitlines()
        hook.write_text('#!/bin/sh\nexit 0\n')
        b=self.desk.save(self.request(supersedes=a['id'],note='Revised fixture wording'))
        self.send(b)
        self.assertEqual(self.git('diff','--cached','--name-only').splitlines(),staged)
        self.assertEqual(delivery.delivery_state(self.repo,a),'saved')
        self.assertEqual(delivery.delivery_state(self.repo,b),'delivered')

    def test_published_history_gap_does_not_silently_join_disconnected_segments(self):
        a=self.desk.save(self.request(note='First sent answer')); self.send(a)
        b=self.desk.save(self.request(supersedes=a['id'],note='Private intermediate'))
        c=self.desk.save(self.request(supersedes=b['id'],note='Latest sent answer')); self.send(c)
        restored=QueueStore(Path(self.tmp.name)/'without-private-draft.sqlite3',self.repo,'901',True)
        card=restored.display()
        self.assertEqual({e['id'] for e in card['events']},{a['id'],c['id']})
        self.assertTrue(card['history_notes'])
        self.assertTrue(card['conflict'])
        self.assertFalse(card['can_respond'])
        self.assertFalse(card['can_deliver'])

    def test_wrong_wq_and_tampered_local_history_refuse(self):
        a=self.desk.save(self.request())
        b=self.desk.save(self.request(supersedes=a['id']))
        other=self.desk.queue_store('902',True); d=other.display()
        wrong=other.save(self.request(unit_id='902.queue',display_hash=d['hash'],action='report_done'))
        with self.assertRaisesRegex(ValueError,'another queue item'):
            delivery.deliver(self.repo,b,local_events=lambda:[a,b,wrong])
        bad=json.loads(json.dumps(a));bad['request']['note']='Tampered history'
        with self.assertRaisesRegex(ValueError,'hash mismatch'):
            delivery.deliver(self.repo,b,local_events=lambda:[bad,b])
        self.assertFalse((self.root/'PROME/inbox').exists())

    def test_genuinely_missing_unpublished_predecessor_still_refuses(self):
        a=self.desk.save(self.request())
        bad=json.loads(json.dumps(a));bad['id']=uuid.uuid4().hex;bad['request']['id']=bad['id']
        bad['request']['supersedes']=uuid.uuid4().hex
        bad['sha256']=digest({k:v for k,v in bad.items() if k!='sha256'})
        immutable_export(self.repo,bad)
        with self.assertRaisesRegex(ValueError,'Missing predecessor'):
            delivery.deliver(self.repo,bad,local_events=lambda:[bad])
        self.assertFalse((self.root/'PROME/inbox').exists())

    def test_new_local_revision_during_checks_refuses_older_send(self):
        a=self.desk.save(self.request())
        b=self.desk.save(self.request(supersedes=a['id']))
        run=subprocess.run
        def revise(args,**kwargs):
            result=run(args,**kwargs)
            if args[:2]==['python3','scripts/claim_check.py']:
                self.store.save(self.request(supersedes=b['id'],note='Changed during checks'))
            return result
        with patch('delivery.subprocess.run',side_effect=revise):
            with self.assertRaisesRegex(ValueError,'latest saved'):self.send(b)
        self.assertFalse((self.root/'PROME/inbox').exists())


if __name__=='__main__':unittest.main()
