"""Bounded brief checks using PROME's actual November 6 producer record."""
from datetime import date
import hashlib
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import app
import briefs
import delivery
from pilot_files import record_block
from queue_store import open_rows
from store import reader
import test_desk as fixtures


class BriefTests(unittest.TestCase):
    git = fixtures.DeskTests.git
    put = fixtures.DeskTests.put
    commit = fixtures.DeskTests.commit
    request = fixtures.DeskTests.request

    def setUp(self):
        fixtures.DeskTests.setUp(self)
        clock = patch('briefs.today', return_value=date(2026, 11, 6))
        clock.start(); self.addCleanup(clock.stop)
        self.path = 'PROME/proposals/fixture-brief.md'
        original = (Path(__file__).resolve().parent.parent / 'releases/2026-11-06-briefs/wq632-producer.md').read_text()
        self.brief = record_block(original, 'decisions-brief')
        self.options = record_block(original, 'decisions-options')
        self.text = self.text.replace('Exact caveat |', 'Exact caveat <!-- decisions-options: '+self.path+' --> |')
        row_hash = hashlib.sha256(open_rows(self.text)['901']['row'].encode()).hexdigest()
        for block in (self.brief, self.options):
            block['wq_id'] = 901  # Preserve the real producer's integer dialect.
            block['queue_row_sha256'] = row_hash
        self.put('PROME/WILL_QUEUE.md', self.text)
        self.publish()
        self.display = self.store.display()

    def publish(self):
        self.put(self.path, '```decisions-brief\n'+json.dumps(self.brief)+'\n```\n\n'
                 +'```decisions-options\n'+json.dumps(self.options)+'\n```\n')
        self.commit(publish=True)

    def test_real_producer_wording_and_integer_choices_are_preserved(self):
        p = briefs.presentation(self.display['snapshot'])
        self.assertEqual(p['brief'], self.brief)
        self.assertEqual(self.display['unit']['proposal']['choices'], self.options['choices'])
        with patch('app.accepted', return_value=(True, '')):
            state = app.Desk(self.repo, Path(self.tmp.name)/'desktop', True).display()
        self.assertFalse(state['errors'])
        self.assertEqual(next(c for c in state['cards'] if c['wq_id']=='901')['brief'], self.brief)

    def test_answer_retains_explanation_and_source_edit_invalidates_pending_send(self):
        e = self.store.save(self.request(action='choose', choice_id='A'))
        self.assertEqual(briefs.presentation(e['display'])['brief'], self.brief)
        self.brief['conditions'].append('New material condition')
        self.publish()
        with self.assertRaisesRegex(ValueError, 'Option terms changed'):
            delivery.deliver(self.repo, e)
        self.assertNotIn('New material condition', e['display']['options_source']['text'])

    def test_delivery_and_restore_keep_original_explanation(self):
        e = self.store.save(self.request(action='choose', choice_id='B'))
        delivery.deliver(self.repo, e)
        self.assertEqual(delivery.delivery_state(self.repo, e), 'delivered')
        self.assertEqual(self.store.display()['events'][0], e)
        self.assertEqual(briefs.presentation(e['display'], historical=True)['brief'], self.brief)

    def test_expiry_reveals_full_terms_but_preserves_saved_explanation(self):
        snapshot = self.display['snapshot']
        with patch('briefs.today', return_value=date(2026, 11, 14)):
            result = briefs.presentation(snapshot)
            self.assertIsNone(result['brief'])
            self.assertIn('out of date', result['brief_notice'])
            self.assertEqual(briefs.presentation(snapshot, historical=True)['brief'], self.brief)

    def test_invalid_brief_isolated_from_choices_and_other_cards(self):
        for mutation in ({'conditions': 'wrong shape'}, {'queue_row_sha256': '0'*64},
                         {'wq_id': True}, {'supporting': [{'label':'bad', 'path':'../../secret'}]}):
            with self.subTest(mutation=mutation):
                old = dict(self.brief)
                self.brief.update(mutation); self.publish()
                with patch('app.accepted', return_value=(True, '')):
                    state = app.Desk(self.repo, Path(self.tmp.name)/'desktop', True).display()
                cards = {c['wq_id']:c for c in state['cards']}
                self.assertFalse(state['errors'])
                self.assertIsNone(cards['901']['brief'])
                self.assertTrue(cards['901']['brief_notice'])
                self.assertTrue(cards['902']['can_respond'])
                self.brief = old

    def test_unpublished_source_and_wrong_options_hash_cannot_enable_answers(self):
        self.put(self.path, 'unpublished replacement')
        with self.assertRaises(ValueError): self.store.display()
        self.options['queue_row_sha256'] = '0'*64
        self.publish()
        with self.assertRaises(ValueError): self.store.display()

    def test_closed_queue_does_not_resurrect_from_brief(self):
        self.put('PROME/WILL_QUEUE.md', self.text.replace(open_rows(self.text)['901']['row']+'\n', ''))
        self.commit(publish=True)
        with patch('app.accepted', return_value=(True, '')):
            state = app.Desk(self.repo, Path(self.tmp.name)/'desktop', True).display()
        self.assertNotIn('901', [c['wq_id'] for c in state['cards']])


if __name__ == '__main__': unittest.main()
