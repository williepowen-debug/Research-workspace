"""Acceptance cases for the news catch-up repair (WQ-676, Will 2026-11-11 14:16 ET).
Source: research/2026-11-11_intake-catchup/ACCEPTANCE.md, cases 1-9 (8 = existing suites)."""
import contextlib, hashlib, io, json, sys, tempfile, unittest
from pathlib import Path
from unittest import mock
import intake_scan as s


def item(title, cls, agents=('CYPHER',), hits=None):
    d = dict(title=title, classification=cls, agents=list(agents), entity='X', label='q')
    if hits:
        d['watch_hits'] = hits
    return d


def key_hit(t):
    return 'news:WATCH_HIT:' + hashlib.sha1(t.encode('utf-8')).hexdigest()[:12]


def key_dev(t):
    return 'news:DEVELOPMENT:' + hashlib.sha1(t.encode('utf-8')).hexdigest()[:12]


class CatchUp(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.lane = Path(self.tmp.name) / 'lane'
        self.days = {
            '2026-11-01': [item('D1 hit', 'NEW_WATCH_HIT', hits=[['CYPHER', 'x']])],
            '2026-11-02': [item('D2 hit', 'NEW_WATCH_HIT', hits=[['CYPHER', 'y']]), item('D2 dev', 'DEVELOPMENT'),
                           item('D2 alert', 'NEW_ALERT'), item('D2 plain', 'NEW')],
            '2026-11-03': [item('D3 hit', 'NEW_WATCH_HIT', hits=[['BROCK', 'z']]), item('D3 watch', 'NEW_WATCH')],
            '2026-11-04': [item('D4 hit', 'NEW_WATCH_HIT', hits=[['HENRY', 'w']]), item('D4 watch', 'NEW_WATCH')],
        }
        for d, items in self.days.items():
            (self.lane / 'data' / d).mkdir(parents=True)
            (self.lane / 'data' / d / 'news.json').write_text(json.dumps({'items': items}))
        self.live = {'jobs': {'newsweep': {'saved': 'data/2026-11-04/news.json',
                                           'by_class': {'NEW_WATCH_HIT': 1, 'NEW_WATCH': 1}}}}
        (self.lane / 'liveness.json').write_text(json.dumps(dict(self.live, last_run_utc='2026-11-04T21:00:00Z')))
        self.seen = Path(self.tmp.name) / 'intake_seen.json'
        self.p = [mock.patch.object(s, 'LANE', self.lane), mock.patch.object(s, 'SEEN', self.seen),
                  mock.patch.object(s, 'LIVENESS', self.lane / 'liveness.json')]
        for x in self.p: x.start()

    def tearDown(self):
        for x in self.p: x.stop()
        self.tmp.cleanup()

    def keys(self, last):
        return {r['key'] for r in s.collect_alerts(self.live, last)}

    def test_1_install_no_replay(self):
        k = self.keys(None)
        self.assertIn(key_hit('D4 hit'), k)
        self.assertIn('news:NEW_WATCH:data/2026-11-04/news.json', k)
        self.assertNotIn(key_hit('D3 hit'), k)
        self.assertNotIn(key_hit('D2 hit'), k)
        self.assertNotIn(key_hit('D1 hit'), k)

    def test_2_catch_up_reads_every_newer_batch(self):
        k = self.keys('data/2026-11-01/news.json')
        for want in (key_hit('D2 hit'), key_dev('D2 dev'), key_hit('D3 hit'), key_hit('D4 hit'),
                     'news:NEW_ALERT:data/2026-11-02/news.json', 'news:NEW_WATCH:data/2026-11-03/news.json',
                     'news:NEW_WATCH:data/2026-11-04/news.json'):
            self.assertIn(want, k)
        self.assertNotIn(key_hit('D1 hit'), k)

    def test_3_marked_batch_and_older_not_reread(self):
        k = self.keys('data/2026-11-02/news.json')
        self.assertIn(key_hit('D3 hit'), k)          # catch-up: absent under the old newest-only code
        self.assertIn(key_hit('D4 hit'), k)
        self.assertNotIn(key_hit('D1 hit'), k)
        self.assertNotIn(key_hit('D2 hit'), k)
        self.assertNotIn(key_dev('D2 dev'), k)

    def test_4_pointer_at_newest(self):
        self.assertEqual(s.news_batches('data/2026-11-04/news.json', 'data/2026-11-04/news.json'),
                         ['data/2026-11-04/news.json'])

    def test_5_mark_advances_pointer_and_reconciles(self):
        self.seen.write_text(json.dumps({'seen': {'news:WATCH_HIT:gone000000': 'x'}, 'updated': None,
                                         'last_marked_batch': 'data/2026-11-01/news.json'}))
        with mock.patch.object(sys, 'argv', ['intake_scan.py', '--mark']), contextlib.redirect_stdout(io.StringIO()):
            s.main()
        st = json.loads(self.seen.read_text())
        self.assertEqual(st['last_marked_batch'], 'data/2026-11-04/news.json')
        self.assertIn(key_hit('D2 hit'), st['seen'])
        self.assertNotIn('news:WATCH_HIT:gone000000', st['seen'])

    def test_6_unreadable_older_batch_fails_loud(self):
        (self.lane / 'data' / '2026-11-02' / 'news.json').write_text('{broken')
        k = self.keys('data/2026-11-01/news.json')
        self.assertIn('news:UNREADABLE:data/2026-11-02/news.json', k)
        self.assertIn(key_hit('D4 hit'), k)

    def test_7_bad_pointer_falls_back_and_warns(self):
        self.assertEqual(s.pointer_health('garbage')[0][0], 'MED')
        self.assertEqual(s.news_batches('data/2026-11-04/news.json', 'garbage'), ['data/2026-11-04/news.json'])
        # follow-up note 2: a parseable pointer whose file is gone still catches up BY DATE (no skip), LOW line
        self.assertEqual(s.news_batches('data/2026-11-04/news.json', 'data/2026-10-01/news.json'),
                         ['data/2026-11-01/news.json', 'data/2026-11-02/news.json', 'data/2026-11-03/news.json',
                          'data/2026-11-04/news.json'])
        self.assertEqual(s.pointer_health('data/2026-10-01/news.json', 'data/2026-11-04/news.json')[0][0], 'LOW')
        # follow-up note 3: an unrecognised newest path is loud
        self.assertEqual(s.pointer_health(None, 'weird/path.json')[0][0], 'MED')
        self.assertEqual(s.pointer_health(None), [])
        self.assertEqual(s.pointer_health('data/2026-11-01/news.json'), [])

    def test_9_report_states_range(self):
        self.seen.write_text(json.dumps({'seen': {}, 'updated': None, 'last_marked_batch': 'data/2026-11-01/news.json'}))
        out = io.StringIO()
        with mock.patch.object(sys, 'argv', ['intake_scan.py']), contextlib.redirect_stdout(out):
            s.main()
        self.assertIn('news batches scanned — 3: 2026-11-02..2026-11-04', out.getvalue())

    def mark(self, *extra):
        out = io.StringIO()
        with mock.patch.object(sys, 'argv', ['intake_scan.py', '--mark', *extra]), contextlib.redirect_stdout(out):
            rc = s.main()
        return rc, out.getvalue()

    def test_F1_mark_through_refused_if_lane_moved(self):
        before = json.dumps({'seen': {}, 'updated': None, 'last_marked_batch': 'data/2026-11-01/news.json'})
        self.seen.write_text(before)
        rc, out = self.mark('--through', 'data/2026-11-03/news.json')
        self.assertEqual(rc, 2)
        self.assertIn('REFUSED', out)
        self.assertEqual(self.seen.read_text(), before)
        rc, _ = self.mark('--through', 'data/2026-11-04/news.json')
        self.assertEqual(json.loads(self.seen.read_text())['last_marked_batch'], 'data/2026-11-04/news.json')

    def test_F3_mark_holds_before_unreadable_batch(self):
        (self.lane / 'data' / '2026-11-03' / 'news.json').write_text('{broken')
        self.seen.write_text(json.dumps({'seen': {}, 'updated': None, 'last_marked_batch': 'data/2026-11-01/news.json'}))
        self.mark('--through', 'data/2026-11-04/news.json')
        self.assertEqual(json.loads(self.seen.read_text())['last_marked_batch'], 'data/2026-11-02/news.json')

    def test_note1_valid_json_without_items_is_unreadable_in_scan_and_mark(self):
        (self.lane / 'data' / '2026-11-02' / 'news.json').write_text('[]')
        self.assertIn('news:UNREADABLE:data/2026-11-02/news.json', self.keys('data/2026-11-01/news.json'))
        self.seen.write_text(json.dumps({'seen': {}, 'updated': None, 'last_marked_batch': 'data/2026-11-01/news.json'}))
        self.mark('--through', 'data/2026-11-04/news.json')
        self.assertEqual(json.loads(self.seen.read_text())['last_marked_batch'], 'data/2026-11-01/news.json')

    def test_F4_pointer_ahead_warns_and_never_moves_back(self):
        (self.lane / 'data' / '2026-11-09').mkdir()
        (self.lane / 'data' / '2026-11-09' / 'news.json').write_text(json.dumps({'items': []}))
        self.assertEqual(s.pointer_health('data/2026-11-09/news.json', 'data/2026-11-04/news.json')[0][0], 'MED')
        self.seen.write_text(json.dumps({'seen': {}, 'updated': None, 'last_marked_batch': 'data/2026-11-09/news.json'}))
        self.mark()
        self.assertEqual(json.loads(self.seen.read_text())['last_marked_batch'], 'data/2026-11-09/news.json')

    def test_F5_missing_saved_keeps_counts(self):
        live = {'jobs': {'newsweep': {'by_class': {'NEW_ALERT': 2}}}}
        self.assertIn('news:NEW_ALERT:', {r['key'] for r in s.collect_alerts(live, None)})

    def test_F6_non_date_dirs_ignored(self):
        (self.lane / 'data' / '2026-11-02_rerun').mkdir()
        (self.lane / 'data' / '2026-11-02_rerun' / 'news.json').write_text(json.dumps({'items': [item('rerun hit', 'NEW_WATCH_HIT', hits=[['X', 'y']])]}))
        self.assertNotIn(key_hit('rerun hit'), self.keys('data/2026-11-01/news.json'))


if __name__ == '__main__':
    unittest.main()
