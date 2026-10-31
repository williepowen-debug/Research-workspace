"""Work-reduction batch counterexamples. All writes target disposable repositories."""
import hashlib
import json
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch
import uuid

import app
import delivery
import owner_receipt
from pilot_files import Repo, encoded
from queue_store import QueueStore, REPLIES
import test_desk as fixtures


class BatchTests(unittest.TestCase):
    git = fixtures.DeskTests.git
    put = fixtures.DeskTests.put
    commit = fixtures.DeskTests.commit
    request = fixtures.DeskTests.request

    def setUp(self):
        fixtures.DeskTests.setUp(self)

    def send(self, event):
        return delivery.deliver(self.repo, event, local_events=lambda: self.store.responses()['events'])

    def publish_file(self, path, text):
        self.put(path, text)
        self.git('add', '-f', '--', path)
        self.git('commit', '-qm', 'Fixture explicit publication', '--', path)
        self.git('push', '-q')

    def test_drafts_and_legacy_exports_are_ignored_and_never_swept(self):
        a = self.store.save(self.request(note='Private draft alpha'))
        b = self.store.save(self.request(supersedes=a['id'], note='Final beta'))
        self.assertFalse(self.repo.path(delivery.event_path(a)).exists())
        self.put(delivery.event_path(a), encoded(a)+'\n')  # Old-install export.
        self.assertTrue(self.git('check-ignore', delivery.event_path(a)).strip())
        self.assertNotIn('exports', self.git('status', '--porcelain', '--untracked-files=all'))
        self.assertNotIn(a['id'], self.git('status', '--porcelain', '--untracked-files=all'))
        self.send(b)
        self.assertFalse(delivery.published_packet(self.repo, a))
        with self.assertRaises(ValueError): self.repo.read(delivery.event_path(a), 'origin/master')
        self.assertEqual(self.repo.path(delivery.event_path(a)).read_text(), encoded(a)+'\n')

    def test_published_event_alone_requires_new_version_for_exact_pair(self):
        event = self.store.save(self.request())
        self.publish_file(delivery.event_path(event), encoded(event)+'\n')
        self.assertEqual(delivery.delivery_state(self.repo, event), 'published without inbox packet')
        report = owner_receipt.intake(self.repo, True)
        self.assertEqual(report['items'][0]['status'], 'needs_clarification')
        self.assertFalse(self.repo.path('PROME/decisions/receipts').exists())
        before=self.git('rev-parse','origin/master')
        with self.assertRaisesRegex(ValueError,'Incomplete earlier publication'): self.send(event)
        self.assertEqual(before,self.git('rev-parse','origin/master'))
        replacement=self.store.save(self.request(supersedes=event['id']))
        self.send(replacement)
        self.assertEqual(delivery.delivery_state(self.repo,replacement),'delivered')

    def test_processed_packet_still_proves_delivery(self):
        event = self.store.save(self.request()); result = self.send(event)
        self.git('mv', result['packet'], result['packet'].replace('/inbox/', '/inbox/processed/')) if self.repo.path('PROME/inbox/processed').exists() else None
        if not self.repo.path('PROME/inbox/processed').exists():
            self.repo.path('PROME/inbox/processed').mkdir()
            self.git('mv', result['packet'], result['packet'].replace('/inbox/', '/inbox/processed/'))
        self.git('commit', '-qm', 'Fixture owner files packet'); self.git('push', '-q')
        self.assertEqual(delivery.delivery_state(self.repo, event), 'delivered')
        before = self.git('rev-parse', 'HEAD'); self.send(event)
        self.assertEqual(before, self.git('rev-parse', 'HEAD'))

    def refusal_after_commit(self, mutate):
        event = self.store.save(self.request(note='Candidate that must not leak'))
        before = self.git('rev-parse', 'HEAD')
        self.put('foreign.txt', 'Another owner staged text'); self.git('add', 'foreign.txt')
        original = Repo.git
        def interleave(work, *args):
            result = original(work, *args)
            if args[0] == 'commit' and work.root != self.root:
                mutate(event)
            return result
        with patch.object(Repo, 'git', interleave):
            with self.assertRaises(ValueError): self.send(event)
        self.assertEqual(before, self.git('rev-parse', 'HEAD'))
        self.assertEqual(self.git('diff', '--cached', '--name-only').strip(), 'foreign.txt')
        self.assertFalse(self.repo.path(f"PROME/inbox/decisions-{event['id']}-from-CATO.md").exists())
        self.git('commit', '-qm', 'Unrelated owner closeout', '--', 'foreign.txt'); self.git('push', '-q')
        self.assertFalse(delivery.published_packet(self.repo, event))
        with self.assertRaises(ValueError): self.repo.read(delivery.event_path(event), 'origin/master')
        return event

    def test_new_local_answer_during_commit_never_reaches_shared_push(self):
        def revise(event):
            self.store.save(self.request(supersedes=event['id'], note='New local answer'))
        self.refusal_after_commit(revise)

    def test_changed_question_during_commit_never_reaches_shared_push(self):
        self.refusal_after_commit(lambda e: self.put('PROME/WILL_QUEUE.md', self.text.replace('Exact caveat', 'Different consequence')))

    def test_revoked_acceptance_after_commit_leaves_no_shared_commit(self):
        event=self.store.save(self.request()); before=self.git('rev-parse','HEAD'); active=[True]
        original=Repo.git
        def interleave(work,*args):
            result=original(work,*args)
            if args[0]=='commit' and work.root != self.root: active[0]=False
            return result
        def guard():
            if not active[0]: raise ValueError('Acceptance changed')
        with patch.object(Repo,'git',interleave):
            with self.assertRaisesRegex(ValueError,'Acceptance changed'):
                delivery.deliver(self.repo,event,guard=guard)
        self.assertEqual(before,self.git('rev-parse','HEAD'))
        self.assertEqual(delivery.delivery_state(self.repo,event),'saved')

    def test_remote_advance_at_push_is_refused_without_shared_commit(self):
        event=self.store.save(self.request()); run=subprocess.run
        def advance(args,**kwargs):
            if args==['bash','scripts/safe-push.sh']:
                self.publish_file('owner.txt','Owner remote update')
            return run(args,**kwargs)
        with patch('delivery.subprocess.run',side_effect=advance):
            with self.assertRaisesRegex(ValueError,'not published'): self.send(event)
        self.assertEqual(delivery.delivery_state(self.repo,event),'saved')
        self.assertFalse(delivery.published_packet(self.repo,event))
        self.send(event)
        self.assertEqual(delivery.delivery_state(self.repo,event),'delivered')

    def test_push_succeeds_then_times_out_is_confirmed_without_duplicate(self):
        event=self.store.save(self.request()); run=subprocess.run
        def ambiguous(args,**kwargs):
            result=run(args,**kwargs)
            if args==['bash','scripts/safe-push.sh']:
                self.assertEqual(result.returncode,0)
                raise subprocess.TimeoutExpired(args,120)
            return result
        with patch('delivery.subprocess.run',side_effect=ambiguous): self.send(event)
        before=self.git('rev-parse','origin/master'); self.send(event)
        self.assertEqual(before,self.git('rev-parse','origin/master'))

    def test_existing_unpublished_reply_commit_cannot_be_swept(self):
        a=self.store.save(self.request()); self.put(delivery.event_path(a),encoded(a)+'\n')
        self.git('add','-f',delivery.event_path(a)); self.git('commit','-qm','Fixture old refused send')
        b=self.store.save(self.request(supersedes=a['id'],note='Replacement'))
        with self.assertRaisesRegex(ValueError,'earlier unpublished reply'): self.send(b)
        self.assertEqual(delivery.delivery_state(self.repo,b),'saved')

    def test_intake_receives_once_and_never_rules(self):
        event=self.store.save(self.request()); self.send(event)
        preview=owner_receipt.intake(self.repo)
        self.assertEqual(preview['items'][0]['status'],'ready')
        first=owner_receipt.intake(self.repo,True); second=owner_receipt.intake(self.repo,True)
        self.assertEqual(first['items'][0]['receipt_path'],second['items'][0]['receipt_path'])
        files=list(self.repo.path('PROME/decisions/receipts').rglob('*.json'))
        self.assertEqual(len(files),1)
        receipt=json.loads(files[0].read_text()); self.assertEqual(receipt['state'],'received')
        self.assertIsNone(receipt['canonical_ruling']); self.assertIsNone(receipt['chat_confirmation'])
        self.assertEqual(self.repo.path('PROME/WILL_QUEUE.md').read_text(),self.text)
        self.assertTrue(first['requires_chat_confirmation'])
        self.assertEqual(self.git('diff','--cached','--name-only'),'')

    def test_intake_rejects_stale_terms_and_superseded_answer(self):
        a=self.store.save(self.request()); self.send(a)
        b=self.store.save(self.request(supersedes=a['id'],note='Replacement')); self.send(b)
        report=owner_receipt.intake(self.repo)
        rows={r['id']:r for r in report['items']}
        self.assertEqual(rows[a['id']]['status'],'superseded'); self.assertEqual(rows[b['id']]['status'],'ready')
        self.put('PROME/WILL_QUEUE.md',self.text.replace('Exact caveat','Changed terms'))
        report=owner_receipt.intake(self.repo,True)
        self.assertEqual(next(r for r in report['items'] if r['id']==b['id'])['status'],'needs_clarification')
        self.assertFalse(self.repo.path('PROME/decisions/receipts').exists())

    def test_intake_quarantines_malformed_event_without_losing_good_item(self):
        event=self.store.save(self.request()); self.send(event)
        bad=uuid.uuid4().hex; self.publish_file(f'{REPLIES}/{bad}.json','{broken')
        rows={r['id']:r for r in owner_receipt.intake(self.repo)['items']}
        self.assertEqual(rows[bad]['status'],'needs_clarification')
        self.assertEqual(rows[event['id']]['status'],'ready')

    def test_intake_ignores_unpublished_head_only_event(self):
        event=self.store.save(self.request()); self.put(delivery.event_path(event),encoded(event)+'\n')
        self.git('add','-f',delivery.event_path(event)); self.git('commit','-qm','Fixture unpublished response')
        self.assertEqual(owner_receipt.intake(self.repo)['items'],[])

    def test_intake_receipt_collision_preserves_original(self):
        event=self.store.save(self.request()); self.send(event)
        receipt=owner_receipt.prepare(self.repo,event,'received')
        receipt['id']=uuid.uuid5(uuid.NAMESPACE_URL,'decisions-received/1/'+event['sha256']).hex
        receipt['state']='rejected_stale'; path=owner_receipt.receipt_path(self.repo,receipt)
        path.parent.mkdir(parents=True); path.write_text(encoded(receipt)+'\n')
        row=owner_receipt.intake(self.repo,True)['items'][0]
        self.assertEqual(row['status'],'needs_clarification')
        self.assertEqual(json.loads(path.read_text())['state'],'rejected_stale')

    def test_intake_reuses_uncommitted_owner_prepared_received_receipt(self):
        event=self.store.save(self.request()); self.send(event)
        receipt=owner_receipt.prepare(self.repo,event,'received')
        path=owner_receipt.receipt_path(self.repo,receipt); path.parent.mkdir(parents=True)
        path.write_text(encoded(receipt)+'\n')
        row=owner_receipt.intake(self.repo,True)['items'][0]
        self.assertEqual(row['receipt_path'],str(path.relative_to(self.root)))
        self.assertEqual(len(list(path.parent.glob('*.json'))),1)

    def test_intake_refuses_response_with_wrong_filename(self):
        event=self.store.save(self.request()); self.send(event)
        wrong=uuid.uuid4().hex
        self.publish_file(f'{REPLIES}/{wrong}.json',encoded(event)+'\n')
        with self.assertRaisesRegex(ValueError,'filename'):
            owner_receipt.load_event(self.repo,wrong)

    def test_concurrent_intake_retries_write_one_received_receipt(self):
        from concurrent.futures import ThreadPoolExecutor
        event=self.store.save(self.request()); self.send(event)
        with ThreadPoolExecutor(max_workers=2) as pool:
            results=list(pool.map(lambda _: owner_receipt.intake(self.repo,True),range(2)))
        self.assertTrue(all(r['items'][0]['status']=='received' for r in results))
        self.assertEqual(len(list(self.repo.path('PROME/decisions/receipts').rglob('*.json'))),1)

    def test_intake_changed_options_refused(self):
        fixtures.DeskTests.install_options(self)
        event=self.store.save(self.request(action='choose',choice_id='A')); self.send(event)
        self.options['choices'][0]['meaning']='New obligation'
        path=event['display']['options_source']['path']
        self.publish_file(path,'```decisions-options\n'+json.dumps(self.options)+'\n```\n')
        row=owner_receipt.intake(self.repo,True)['items'][0]
        self.assertEqual(row['status'],'needs_clarification')
        self.assertFalse(self.repo.path('PROME/decisions/receipts').exists())

    def test_intake_disconnected_history_refuses_only_that_item(self):
        a=self.store.save(self.request()); self.send(a)
        b=self.store.save(self.request(supersedes=a['id'],note='Private middle'))
        c=self.store.save(self.request(supersedes=b['id'],note='Published last')); self.send(c)
        task=QueueStore(Path(self.tmp.name)/'task.sqlite3',self.repo,'902',True)
        d=task.display(); e=task.save(self.request(display_hash=d['hash'],unit_id='902.queue',action='report_done',note='Task report'))
        delivery.deliver(self.repo,e)
        rows={r['id']:r for r in owner_receipt.intake(self.repo,True)['items']}
        self.assertEqual(rows[c['id']]['status'],'needs_clarification')
        self.assertEqual(rows[e['id']]['status'],'received')
        self.assertFalse(self.repo.path('PROME/decisions/receipts/'+c['id']).exists())

    def test_intake_changed_source_inside_receipt_lock_refuses(self):
        event=self.store.save(self.request()); self.send(event)
        lock=owner_receipt.fcntl.flock
        def changed(*args):
            result=lock(*args)
            self.put('PROME/WILL_QUEUE.md',self.text.replace('Exact caveat','Different now'))
            return result
        with patch('owner_receipt.fcntl.flock',side_effect=changed):
            row=owner_receipt.intake(self.repo,True)['items'][0]
        self.assertEqual(row['status'],'needs_clarification')
        self.assertFalse(self.repo.path('PROME/decisions/receipts').exists())

    def test_fingerprint_repins_advice_and_keeps_parser_and_publication_guards(self):
        before=app.build_hashes()
        for name in ['scripts/claim_check.py','scripts/orphan_check.sh']:
            self.assertIn(name,before)
        for name in ['PROME/tools/willq_view.py','scripts/safe-push.sh','scripts/githooks/pre-push','scripts/account_guard.py','owner_receipt.py']:
            self.assertIn(name,before)
        read=Path.read_bytes
        def changed(p):
            data=read(p)
            if str(p).endswith('/scripts/claim_check.py'): return data+b'\n# advisory edit\n'
            return data
        with patch.object(Path,'read_bytes',changed): self.assertNotEqual(before,app.build_hashes())
        def critical(p):
            data=read(p)
            if str(p).endswith('/PROME/tools/willq_view.py'): return data+b'\n# parser edit\n'
            return data
        with patch.object(Path,'read_bytes',critical): self.assertNotEqual(before,app.build_hashes())


if __name__=='__main__': unittest.main()
