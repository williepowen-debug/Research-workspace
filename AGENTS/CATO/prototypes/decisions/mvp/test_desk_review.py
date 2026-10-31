"""Regressions from PROME's independent HOLD; writes stay in disposable Git fixtures."""
import json
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch

import app
import delivery
import owner_receipt
from pilot_files import encoded
from queue_store import QueueStore
import test_desk as fixtures


class ReviewTests(unittest.TestCase):
    setUp = fixtures.DeskTests.setUp
    git = fixtures.DeskTests.git
    put = fixtures.DeskTests.put
    commit = fixtures.DeskTests.commit
    request = fixtures.DeskTests.request
    install_options = fixtures.DeskTests.install_options

    def integrate(self, event, close=False):
        path = 'PROME/proposals/fixture-RULED.md'
        self.put(path, 'WQ-901: matching chat confirmation and ruling for this fixture.')
        self.git('add', '--', path); self.git('commit', '-qm', 'Fixture ruling', '--', path); self.git('push', '-q')
        ref = {'path': path, 'commit': self.git('rev-parse', 'HEAD').strip()}
        receipt = owner_receipt.prepare(self.repo, event, 'integrated', ref, ref)
        self.put(f"PROME/decisions/receipts/{event['id']}/{receipt['id']}.json", encoded(receipt)+'\n')
        if close:
            self.put('PROME/WILL_QUEUE.md', '\n'.join(l for l in self.text.splitlines() if not l.startswith('| 901')))
        receipt_path = f"PROME/decisions/receipts/{event['id']}/{receipt['id']}.json"
        paths = [receipt_path] + (['PROME/WILL_QUEUE.md'] if close else [])
        self.git('add', '--', *paths); self.git('commit', '-qm', 'Fixture receipt', '--', *paths); self.git('push', '-q')
        return receipt

    def test_recorded_answer_is_receipt_event_and_later_answer_cannot_send(self):
        a = self.store.save(self.request(note='Send digests'))
        delivery.deliver(self.repo, a)
        b = self.store.save(self.request(supersedes=a['id'], note='Do not send digests'))
        receipt = self.integrate(a)  # Must refuse even if the queue row remains open.
        card = self.store.display()
        self.assertEqual(card['last'], a)
        self.assertEqual(card['receipt'], receipt)
        self.assertIn(b, card['events'])
        self.assertEqual(delivery.delivery_state(self.repo,b),'saved')
        self.assertFalse(card['can_respond'])
        self.assertFalse(card['can_deliver'])
        before = self.git('rev-parse', 'HEAD')
        with self.assertRaisesRegex(ValueError, 'already recorded'):
            delivery.deliver(self.repo, b)
        self.assertEqual(self.git('rev-parse', 'HEAD'), before)
        self.assertFalse(self.repo.path(f"PROME/inbox/decisions-{b['id']}-from-CATO.md").exists())

    def test_changed_closed_blocked_and_unpublished_rows_refuse_saved_answer(self):
        event = self.store.save(self.request())
        variations = [self.text.replace('Exact caveat', 'Changed consequence'),
                      '\n'.join(l for l in self.text.splitlines() if not l.startswith('| 901')),
                      self.text.replace('Exact caveat', '⛔ waits: FALCON')]
        for text in variations:
            for published in (False, True):
                with self.subTest(text=text, published=published):
                    self.put('PROME/WILL_QUEUE.md', text)
                    if published: self.commit(publish=True)
                    with self.assertRaises(ValueError): delivery.deliver(self.repo, event)
                    card = self.store.display()
                    self.assertEqual(card['last'], event)
                    self.assertTrue(card['delivery_block'])
                    self.assertFalse(card['can_deliver'])
                    self.assertFalse((self.root/'PROME/inbox').exists())
            self.put('PROME/WILL_QUEUE.md', self.text); self.commit(publish=True)
        self.assertEqual(self.store.display()['last']['display'], event['display'])
        delivery.deliver(self.repo, event)  # Unrelated commit movement is allowed.

    def test_changed_options_refuse_saved_answer(self):
        path = self.install_options()
        event = self.store.save(self.request(action='choose', choice_id='A'))
        self.options['choices'][0]['meaning'] = 'An additional obligation'
        self.put(path, '```decisions-options\n'+json.dumps(self.options)+'\n```\n')
        self.commit(publish=True)
        with self.assertRaisesRegex(ValueError, 'Terms changed|Option terms changed'):
            delivery.deliver(self.repo, event)
        self.assertFalse(self.store.display()['can_deliver'])

    def test_send_fetches_remote_closure_without_manual_sync(self):
        event = self.store.save(self.request())
        other = Path(self.tmp.name)/'owner'
        subprocess.run(['git','clone','-q','-b','master',str(self.remote),str(other)], check=True)
        for args in [('config','user.name','Owner fixture'),('config','user.email','fixture@example.invalid')]:
            subprocess.run(['git',*args],cwd=other,check=True)
        (other/'PROME/WILL_QUEUE.md').write_text('\n'.join(l for l in self.text.splitlines() if not l.startswith('| 901')))
        for args in [('add','PROME/WILL_QUEUE.md'),('commit','-qm','Owner closes question'),('push','-q')]:
            subprocess.run(['git',*args],cwd=other,check=True)
        with self.assertRaisesRegex(ValueError, 'unavailable or changed'):
            delivery.deliver(self.repo,event)
        self.assertFalse((self.root/'PROME/inbox').exists())
        self.assertEqual(self.repo.path('PROME/WILL_QUEUE.md').read_text(),self.text)

    def test_source_change_during_check_stops_before_packet(self):
        event = self.store.save(self.request())
        run = subprocess.run
        def change(args, **kwargs):
            result=run(args,**kwargs)
            if args[:2]==['python3','scripts/claim_check.py']:
                self.put('PROME/WILL_QUEUE.md',self.text.replace('Exact caveat','New scope'))
            return result
        with patch('delivery.subprocess.run',side_effect=change):
            with self.assertRaises(ValueError): delivery.deliver(self.repo,event)
        self.assertFalse((self.root/'PROME/inbox').exists())

    def test_fork_preserves_both_answers_and_other_cards_remain_usable(self):
        desk=app.Desk(self.repo,Path(self.tmp.name)/'desktop',True)
        with patch('app.accepted',return_value=(True,'')):
            card=next(c for c in desk.display()['cards'] if c['wq_id']=='901')
            local=desk.save(self.request(display_hash=card['hash'],note='Local unsent answer'))
            laptop=QueueStore(Path(self.tmp.name)/'laptop.sqlite3',self.repo,'901',True)
            d=laptop.display()
            remote=laptop.save(self.request(display_hash=d['hash'],note='Other machine answer'))
            delivery.deliver(self.repo,remote)
            state=desk.display()
            conflict=next(c for c in state['cards'] if c['wq_id']=='901')
            other=next(c for c in state['cards'] if c['wq_id']=='902')
            self.assertEqual({e['id'] for e in conflict['events']},{local['id'],remote['id']})
            self.assertTrue(conflict['conflict'])
            self.assertFalse(conflict['can_respond'])
            self.assertFalse(conflict['can_deliver'])
            self.assertTrue(other['can_respond'])
            self.assertTrue(state['can_deliver'])
            with self.assertRaises(ValueError): desk.operate('/api/deliver',{'id':conflict['last']['id']})
            self.assertEqual({e['id'] for e in desk.queue_store('901',True).responses()['events']},{local['id'],remote['id']})

    def test_weekday_advice_is_reported_and_foreign_work_is_preserved(self):
        self.put('scripts/claim_check.py',"print('Advisory weekday mismatch in GATES'); raise SystemExit(1)\n")
        self.commit(publish=True)
        event=self.store.save(self.request())
        self.put('PROME/GATES.tsv','Another owner dirty weekday text\n')
        result=delivery.deliver(self.repo,event)
        self.assertIn('Advisory weekday mismatch',result['message'])
        self.assertEqual(result['checks'][0]['exit'],1)
        self.assertEqual(self.repo.path('PROME/GATES.tsv').read_text(),'Another owner dirty weekday text\n')
        self.assertEqual(delivery.delivery_state(self.repo,event),'delivered')

    def test_check_execution_failure_keeps_answer_without_inbox_packet(self):
        self.put('scripts/claim_check.py',"raise SystemExit(2)\n")
        self.commit(publish=True)
        event=self.store.save(self.request())
        with self.assertRaisesRegex(ValueError,'saved; not delivered: Weekday check failed'):
            delivery.deliver(self.repo,event)
        self.assertEqual(self.store.responses()['events'],[event])
        self.assertFalse((self.root/'PROME/inbox').exists())


if __name__=='__main__': unittest.main()
