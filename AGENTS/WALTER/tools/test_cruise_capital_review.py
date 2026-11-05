#!/usr/bin/env python3
"""Acceptance cases for the CRUISE_CAPITAL_REVIEW queue (WQ-598 A, Will 2026-11-04).

Source: research/2026-11-04_maintenance/CRUISE-COVERAGE.md § Acceptance cases.
Run: python3 AGENTS/WALTER/tools/test_cruise_capital_review.py
"""
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import intake_scan as s


def row(title, entity='Royal Caribbean', cls='KNOWN', agents=('CRUISE',), date='Tue, 03 Nov 2026 12:00:00 GMT'):
    return {'title': title, 'entity': entity, 'classification': cls, 'agents': list(agents),
            'date': date, 'link': f'https://example.test/{abs(hash(title))}'}


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.lane = Path(self.tmp.name) / 'lane'
        self.state = Path(self.tmp.name) / 'state.json'
        patches = [mock.patch.object(s, 'LANE', self.lane), mock.patch.object(s, 'CRUISE_STATE', self.state)]
        for p in patches:
            p.start()
            self.addCleanup(p.stop)
        self.addCleanup(self.tmp.cleanup)

    def day(self, name, items, edgar=None):
        d = self.lane / 'data' / name
        d.mkdir(parents=True)
        (d / 'news.json').write_text(json.dumps({'items': items}))
        if edgar is not None:
            (d / 'edgar_8k.json').write_text(json.dumps({'filings': edgar}))

    def queue(self):
        return s.cruise_capital_queue()


class Selection(Base):
    def test_capital_titles_are_candidates(self):
        for title, ent in [('Norwegian Cruise prices $950 million notes offering', 'Norwegian Cruise'),
                           ('Royal Caribbean buys stake in Sandals', 'Royal Caribbean'),
                           ('Morgan Stanley syndicating loan for Royal Caribbean', 'Royal Caribbean'),
                           ('Carnival Corp upsizes commercial paper programme', 'Carnival Corp')]:
            self.assertTrue(s.is_cruise_capital_candidate(row(title, ent)), title)

    def test_rejections(self):
        for item in [row('Royal Caribbean new Bahamas itinerary promotion'),
                     row('Norwegian Cruise NHL sponsorship', 'Norwegian Cruise'),
                     row('Analyst raises Carnival price target', 'Carnival Corp'),
                     row('CCL Industries bond offering', 'CCL Industries'),
                     row('Debt financing for cruise operator', None, agents=('CRUISE',)),
                     row('Royal Caribbean bond offering', agents=('BROCK',)),
                     row('Royal Caribbean bond offering', cls='NEW_WATCH_HIT'),
                     row('Carnival guidance on conference call', 'Carnival Corp', cls='NEW_WATCH_HIT')]:
            self.assertFalse(s.is_cruise_capital_candidate(item), item['title'])

    def test_institutional_stake_trade_stays_a_human_call(self):
        self.assertTrue(s.is_cruise_capital_candidate(row('Vanguard trims stake in Carnival Corp', 'Carnival Corp')))


class Queue(Base):
    def test_relays_fold_and_keep_every_row(self):
        t = 'Morgan Stanley syndicating loan for Royal Caribbean'
        self.day('2026-11-03', [row(t), row(t.upper())])
        self.day('2026-11-04', [row(t)])
        q, errors = self.queue()
        self.assertEqual(errors, [])
        self.assertEqual(len(q), 1)
        self.assertEqual(len(q[0]['rows']), 3)
        self.assertEqual(q[0]['precedence'], 'ROUTINE')

    def test_new_term_is_not_folded_into_an_older_title(self):
        self.day('2026-11-03', [row('Royal Caribbean Sandals stake acquisition')])
        self.day('2026-11-04', [row('Royal Caribbean Sandals joint venture loan upsized')])
        self.assertEqual(len(self.queue()[0]), 2)

    def test_no_archive_replay_before_baseline(self):
        self.day('2026-10-07', [row('Royal Caribbean syndicating loan')])
        self.day(s.CRUISE_BASELINE_DAY, [])
        self.assertEqual(self.queue()[0], [])

    def test_missed_days_after_baseline_are_all_read(self):
        for n, d in enumerate(['2026-11-04', '2026-11-05', '2026-11-06']):
            self.day(d, [row(f'Royal Caribbean loan number {n}')])
        self.assertEqual(len(self.queue()[0]), 3)

    def test_edgar_overlap_is_shown_so_no_second_dispatch(self):
        self.day('2026-11-04', [row('Carnival Corp commercial paper capacity', 'Carnival Corp')],
                 edgar=[{'ticker': 'CCL', 'date': '2026-11-04', 'items': ['1.01', '2.03', '9.01']},
                        {'ticker': 'RCL', 'date': '2026-11-02', 'items': ['8.01']}])
        c = self.queue()[0][0]
        self.assertEqual(len(c['edgar_overlap']), 1)
        self.assertIn('CCL 2026-11-04', c['edgar_overlap'][0])

    def test_printed_overlap_does_not_claim_a_filing_is_the_same_event(self):
        self.day('2026-11-03', [row('Royal Caribbean and Sandals announce joint venture')],
                 edgar=[{'ticker': 'RCL', 'date': '2026-10-27', 'items': ['2.02', '9.01']}])
        live = {'jobs': {}, 'last_run_utc': '2026-11-04T21:01:17Z', 'status': 'ok'}
        out = io.StringIO()
        with mock.patch.object(s, 'SEEN', Path(self.tmp.name) / 'seen.json'), \
                mock.patch.object(s, 'load_liveness', return_value=(live, None)), \
                mock.patch.object(sys, 'argv', ['intake_scan.py']), redirect_stdout(out):
            s.main()
        self.assertIn('if this is the same event', out.getvalue())
        self.assertNotIn('same-day', out.getvalue())

    def test_corrupt_or_missing_file_is_explicit_and_consumes_nothing(self):
        self.day('2026-11-03', [row('Royal Caribbean revolver extended')])
        bad = self.lane / 'data' / '2026-11-04'
        bad.mkdir(parents=True)
        (bad / 'news.json').write_text('{not json')
        (self.lane / 'data' / '2026-11-05').mkdir()
        q, errors = self.queue()
        self.assertEqual(len(q), 1)
        self.assertEqual(len(errors), 2)
        self.assertFalse(self.state.exists())

    def test_corrupt_state_fails_closed(self):
        self.day('2026-11-03', [row('Royal Caribbean revolver extended')])
        self.state.write_text('{broken')
        q, errors = self.queue()
        self.assertEqual(q, [])
        self.assertTrue(errors)
        self.assertEqual(self.state.read_text(), '{broken')


class Disposition(Base):
    def test_only_the_named_item_is_consumed_and_it_stays_consumed(self):
        self.day('2026-11-03', [row('Royal Caribbean Sandals loan'), row('Royal Caribbean revolver extended')])
        q, _ = self.queue()
        with redirect_stdout(io.StringIO()):
            self.assertEqual(s.cruise_disposition(q[0]['key'], 'FOLD', 'SIG-W-20261014-028'), 0)
        rest, _ = self.queue()
        self.assertEqual([c['key'] for c in rest], [q[1]['key']])
        rec = json.loads(self.state.read_text())['consumed'][q[0]['key']]
        self.assertEqual((rec['disposition'], rec['ref']), ('FOLD', 'SIG-W-20261014-028'))

    def test_unseen_key_bad_token_and_blank_ref_are_refused(self):
        self.day('2026-11-03', [row('Royal Caribbean Sandals loan')])
        key = self.queue()[0][0]['key']
        with redirect_stdout(io.StringIO()):
            self.assertNotEqual(s.cruise_disposition('cruise:000000000000', 'DUP', 'x'), 0)
            self.assertNotEqual(s.cruise_disposition(key, 'CLOSED', 'x'), 0)
            self.assertNotEqual(s.cruise_disposition(key, 'DUP', ' '), 0)
        self.assertFalse(self.state.exists())

    def test_ordinary_mark_never_consumes_the_queue(self):
        self.day('2026-11-03', [row('Royal Caribbean Sandals loan')])
        seen = Path(self.tmp.name) / 'seen.json'
        live = {'jobs': {}, 'last_run_utc': '2026-11-04T21:01:17Z', 'status': 'ok'}
        with mock.patch.object(s, 'SEEN', seen), mock.patch.object(s, 'load_liveness', return_value=(live, None)), \
                mock.patch.object(sys, 'argv', ['intake_scan.py', '--mark']), redirect_stdout(io.StringIO()):
            s.main()
        self.assertTrue(seen.exists())
        self.assertFalse(self.state.exists())
        self.assertEqual(len(self.queue()[0]), 1)


class SavedReplay(unittest.TestCase):
    """The purposive sample from the design: 6 rows on the real saved files, if present."""

    @unittest.skipUnless(Path('/home/willi/Research-Intake/data/2026-10-07/news.json').exists(), 'lane absent')
    def test_design_sample_counts(self):
        n = 0
        for day in ['2026-10-01', '2026-10-05', '2026-10-06', '2026-10-07', '2026-11-02', '2026-11-03', '2026-11-04']:
            items = json.loads(Path(f'/home/willi/Research-Intake/data/{day}/news.json').read_text())['items']
            n += sum(s.is_cruise_capital_candidate(i) for i in items)
        self.assertEqual(n, 6)


if __name__ == '__main__':
    unittest.main()
