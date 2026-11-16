"""Acceptance cases for the news catch-up repair (WQ-676, Will 2026-11-11 14:16 ET).
Source: research/2026-11-11_intake-catchup/ACCEPTANCE.md, cases 1-9 (8 = existing suites)."""
import contextlib, hashlib, io, json, subprocess, sys, tempfile, unittest
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
        # a git clone with no commits = empty history (WQ-694 (a)); a lane that is not a clone now holds the pointer
        subprocess.run(['git', 'init', '-q', str(self.lane)], check=True)
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
        with mock.patch.object(sys, 'argv', ['intake_scan.py', '--mark', '--receipt', self.receipt()]), \
                contextlib.redirect_stdout(io.StringIO()):
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

    def receipt(self):
        """What the operator copies from the scan it read (CATO N14-1, 2026-11-14)."""
        out = io.StringIO()
        with mock.patch.object(sys, 'argv', ['intake_scan.py', '--json']), contextlib.redirect_stdout(out):
            s.main()
        return json.loads(out.getvalue())['receipt']

    def mark(self, *extra, receipt=None):
        out = io.StringIO()
        argv = ['intake_scan.py', '--mark', *extra, '--receipt', receipt or self.receipt()]
        with mock.patch.object(sys, 'argv', argv), contextlib.redirect_stdout(out):
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

    # 2026-11-14 (walter-72, Will 12:16 ET): the collector rewrites a day's news.json on every run.
    def rewrite(self, day, items):
        (self.lane / 'data' / day / 'news.json').write_text(json.dumps({'items': items}))

    def test_R1_marked_batch_rewritten_after_day_moved_on_is_rescanned(self):
        # 11/13 instance: marked 11/03 at 15:18Z; 21:08Z run replaced 11/03; next scan's newest is 11/04
        self.seen.write_text(json.dumps({'seen': {}, 'updated': None,
                                         'last_marked_batch': 'data/2026-11-03/news.json',
                                         'last_marked_sha': s.batch_sha('data/2026-11-03/news.json')}))
        self.rewrite('2026-11-03', [item('late hit', 'NEW_WATCH_HIT', hits=[['CYPHER', 'q']]),
                                    item('late alert', 'NEW_ALERT')])
        sha = s.batch_sha('data/2026-11-03/news.json')
        self.assertEqual(s.news_batches('data/2026-11-04/news.json', 'data/2026-11-03/news.json', 'stale'),
                         ['data/2026-11-03/news.json', 'data/2026-11-04/news.json'])
        k = {r['key'] for r in s.collect_alerts(self.live, 'data/2026-11-03/news.json',
                                                 json.loads(self.seen.read_text())['last_marked_sha'])}
        self.assertIn(key_hit('late hit'), k)
        self.assertIn(f'news:NEW_ALERT:data/2026-11-03/news.json@{sha}', k)

    def test_R2_same_day_rewrite_is_not_suppressed(self):
        # marked newest 11/04, then the collector rewrites 11/04 before the next scan
        rc, _ = self.mark()
        st = json.loads(self.seen.read_text())
        self.assertEqual(st['last_marked_sha'], s.batch_sha('data/2026-11-04/news.json'))
        self.rewrite('2026-11-04', [item('D4 later', 'NEW_WATCH')])
        out = io.StringIO()
        with mock.patch.object(sys, 'argv', ['intake_scan.py', '--json']), contextlib.redirect_stdout(out):
            s.main()
        new = {r['key'] for r in json.loads(out.getvalue())['new']}
        self.assertIn(f"news:NEW_WATCH:data/2026-11-04/news.json@{s.batch_sha('data/2026-11-04/news.json')}", new)

    def test_R3_unchanged_or_unfingerprinted_marked_batch_not_reread(self):
        self.assertEqual(s.news_batches('data/2026-11-04/news.json', 'data/2026-11-03/news.json',
                                        s.batch_sha('data/2026-11-03/news.json')), ['data/2026-11-04/news.json'])
        self.assertEqual(s.news_batches('data/2026-11-04/news.json', 'data/2026-11-03/news.json', None),
                         ['data/2026-11-04/news.json'])


    # 2026-11-14 (CATO N14-1, Will 14:28 ET): the acknowledgment binds to the bytes the scan presented.
    def test_R4_rewrite_between_scan_and_mark_is_refused_and_state_unmoved(self):
        self.seen.write_text(json.dumps({'seen': {}, 'updated': None, 'last_marked_batch': 'data/2026-11-03/news.json'}))
        before = self.seen.read_text()
        read = self.receipt()  # the operator reads this version
        self.rewrite('2026-11-04', [item('late ordinary headline', 'NEW')])
        rc, out = self.mark('--through', 'data/2026-11-04/news.json', receipt=read)
        self.assertEqual(rc, 2)
        self.assertIn('REFUSED', out)
        self.assertEqual(self.seen.read_text(), before)
        rc, _ = self.mark('--through', 'data/2026-11-04/news.json')  # re-scan, then mark what it printed
        self.assertEqual(rc, 0)
        self.assertEqual(json.loads(self.seen.read_text())['last_marked_sha'], s.batch_sha('data/2026-11-04/news.json'))

    def test_R5_mark_without_receipt_or_after_new_alert_key_is_refused(self):
        before = self.seen.read_text() if self.seen.exists() else None
        with mock.patch.object(sys, 'argv', ['intake_scan.py', '--mark', '--through', 'data/2026-11-04/news.json']), \
                contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(s.main(), 2)
        read = self.receipt()
        self.live['jobs']['newsweep']['by_class'] = {'NEW_WATCH_HIT': 1, 'NEW_WATCH': 1, 'NEW_ALERT': 1}
        (self.lane / 'liveness.json').write_text(json.dumps(dict(self.live, last_run_utc='2026-11-04T22:00:00Z')))
        self.rewrite('2026-11-04', self.days['2026-11-04'] + [item('D4 alert', 'NEW_ALERT')])
        rc, _ = self.mark('--through', 'data/2026-11-04/news.json', receipt=read)
        self.assertEqual(rc, 2)
        self.assertEqual(self.seen.read_text() if self.seen.exists() else None, before)


    # 2026-11-14 independent read 1 (PROME LEDGER_read1.md): L1 CX1, L10, L9.
    def test_R6_rewrite_inside_mark_is_not_stored_as_read(self):
        self.seen.write_text(json.dumps({'seen': {}, 'updated': None, 'last_marked_batch': 'data/2026-11-03/news.json'}))
        read = self.receipt()
        read_sha = s.batch_sha('data/2026-11-04/news.json')
        real = s.mark_pointer

        def racing(*a, **k):  # collector rewrite lands after the receipt check, before the state write
            self.rewrite('2026-11-04', [item('unread late headline', 'NEW')])
            return real(*a, **k)
        with mock.patch.object(s, 'mark_pointer', racing):
            rc, _ = self.mark('--through', 'data/2026-11-04/news.json', receipt=read)
        self.assertEqual(rc, 0)
        self.assertEqual(json.loads(self.seen.read_text())['last_marked_sha'], read_sha)
        st = json.loads(self.seen.read_text())
        self.assertIn('data/2026-11-04/news.json',
                      s.news_batches('data/2026-11-04/news.json', st['last_marked_batch'], st['last_marked_sha']))

    def test_R7_reading_change_under_same_key_is_refused(self):
        before = self.seen.read_text() if self.seen.exists() else None
        read = self.receipt()
        self.live['jobs']['newsweep']['by_class'] = {'NEW_WATCH_HIT': 1, 'NEW_WATCH': 2}
        (self.lane / 'liveness.json').write_text(json.dumps(dict(self.live, last_run_utc='2026-11-04T21:00:00Z')))
        rc, out = self.mark('--through', 'data/2026-11-04/news.json', receipt=read)
        self.assertEqual(rc, 2)
        self.assertEqual(self.seen.read_text() if self.seen.exists() else None, before)

    def test_R8_refusal_does_not_hand_over_the_current_receipt(self):
        read = self.receipt()
        self.rewrite('2026-11-04', [item('late', 'NEW')])
        now = self.receipt()
        rc, out = self.mark('--through', 'data/2026-11-04/news.json', receipt=read)
        self.assertEqual(rc, 2)
        self.assertNotIn(now, out)


    # 2026-11-14 independent read 2 (PROME LEDGER_read2.md) M1: readability inside --mark comes from the
    # receipt's own read, so a batch missing or unreadable at the scan cannot be passed by a repair in the gap.
    def race_mark(self, change, *extra):
        read = self.receipt()
        real = s.mark_pointer

        def racing(*a, **k):
            change()
            return real(*a, **k)
        with mock.patch.object(s, 'mark_pointer', racing):
            return self.mark(*extra, receipt=read)

    def test_R9_newest_missing_at_scan_appears_inside_mark_pointer_holds(self):
        self.seen.write_text(json.dumps({'seen': {}, 'updated': None, 'last_marked_batch': 'data/2026-11-03/news.json',
                                         'last_marked_sha': s.batch_sha('data/2026-11-03/news.json')}))
        (self.lane / 'data' / '2026-11-04' / 'news.json').unlink()
        rc, _ = self.race_mark(lambda: self.rewrite('2026-11-04', [item('hidden hit', 'NEW_WATCH_HIT', hits=[['CYPHER', 'h']])]),
                               '--through', 'data/2026-11-04/news.json')
        self.assertEqual(rc, 0)
        st = json.loads(self.seen.read_text())
        self.assertEqual(st['last_marked_batch'], 'data/2026-11-03/news.json')
        self.assertIsNotNone(st['last_marked_sha'])
        self.assertIn(key_hit('hidden hit'), self.keys(st['last_marked_batch']))

    def test_R10_unreadable_middle_repaired_inside_mark_pointer_holds(self):
        self.seen.write_text(json.dumps({'seen': {}, 'updated': None, 'last_marked_batch': 'data/2026-11-02/news.json'}))
        (self.lane / 'data' / '2026-11-03' / 'news.json').write_text('{broken')
        rc, _ = self.race_mark(lambda: self.rewrite('2026-11-03', [item('repaired hit', 'NEW_WATCH_HIT', hits=[['BROCK', 'r']])]),
                               '--through', 'data/2026-11-04/news.json')
        self.assertEqual(rc, 0)
        st = json.loads(self.seen.read_text())
        self.assertEqual(st['last_marked_batch'], 'data/2026-11-02/news.json')
        self.assertIn(key_hit('repaired hit'), self.keys(st['last_marked_batch']))


    # Follow-up 6 (WQ-694 A precondition, Will 2026-11-16 17:18 ET): a same-day second run must not re-alert.
    def scan_new(self):
        out = io.StringIO()
        with mock.patch.object(sys, 'argv', ['intake_scan.py', '--json']), contextlib.redirect_stdout(out):
            s.main()
        d = json.loads(out.getvalue())
        return {r['key'] for r in d['new']}, {r['key'] for r in d['suppressed']}

    def test_R11_marked_rewrite_does_not_realert_after_its_mark(self):
        b = 'data/2026-11-04/news.json'
        self.assertEqual(self.mark('--through', b)[0], 0)
        self.rewrite('2026-11-04', [item('D4 second run', 'NEW_WATCH'), item('D4 second alert', 'NEW_ALERT')])
        sha2 = s.batch_sha(b)
        new, _ = self.scan_new()
        self.assertIn(f'news:NEW_WATCH:{b}@{sha2}', new)        # the rewrite itself still alerts once
        self.assertEqual(self.mark('--through', b)[0], 0)
        st = json.loads(self.seen.read_text())
        self.assertEqual(st['last_marked_sha'], sha2)
        self.assertIn(f'news:NEW_WATCH:{b}', st['seen'])         # stored plain, the form the next scan computes
        self.assertNotIn(f'news:NEW_WATCH:{b}@{sha2}', st['seen'])
        new, sup = self.scan_new()
        self.assertFalse({k for k in new if k.startswith('news:NEW_')}, new)  # no false NEW on the unchanged batch
        self.assertIn(f'news:NEW_WATCH:{b}', sup)
        self.rewrite('2026-11-04', [item('D4 third run', 'NEW_WATCH')])     # a third run is new content again
        new, _ = self.scan_new()
        self.assertIn(f'news:NEW_WATCH:{b}@{s.batch_sha(b)}', new)

    def test_R12_settled_key_only_for_the_stored_sha(self):
        b = 'data/2026-11-04/news.json'
        self.assertEqual(s.settled_key(f'news:NEW_ALERT:{b}@abc', b, 'abc'), f'news:NEW_ALERT:{b}')
        self.assertEqual(s.settled_key(f'news:NEW_ALERT:{b}@abc', b, 'old'), f'news:NEW_ALERT:{b}@abc')
        self.assertEqual(s.settled_key(f'news:NEW_ALERT:{b}@abc', 'data/2026-11-05/news.json', 'abc'),
                         f'news:NEW_ALERT:{b}@abc')
        self.assertEqual(s.settled_key('news:WATCH_HIT:abc', b, 'abc'), 'news:WATCH_HIT:abc')


if __name__ == '__main__':
    unittest.main()
