"""Acceptance cases for WQ-694 option (a): versions replaced by a later same-day collector run are read
from the lane clone's git history. Source: research/2026-11-16_boot/WQ694-OPTION-A-ACCEPTANCE.md (A1-A8)."""
import contextlib, hashlib, io, json, os, subprocess, sys, tempfile, unittest
from pathlib import Path
from unittest import mock
import intake_scan as s

ENV = dict(os.environ, GIT_AUTHOR_NAME='t', GIT_AUTHOR_EMAIL='t@t', GIT_COMMITTER_NAME='t', GIT_COMMITTER_EMAIL='t@t')


def item(title, cls, hits=None, label='q', entity='X'):
    d = dict(title=title, classification=cls, agents=['CYPHER'], entity=entity, label=label)
    if hits:
        d['watch_hits'] = hits
    return d


def hit(t):
    return 'news:WATCH_HIT:' + hashlib.sha1(t.encode('utf-8')).hexdigest()[:12]


def P(day):
    return f'data/{day}/news.json'


class Versions(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.lane = Path(self.tmp.name) / 'lane'
        self.lane.mkdir()
        self.git('init', '-q')
        self.seen = Path(self.tmp.name) / 'intake_seen.json'
        self.p = [mock.patch.object(s, 'LANE', self.lane), mock.patch.object(s, 'SEEN', self.seen),
                  mock.patch.object(s, 'LIVENESS', self.lane / 'liveness.json'),
                  mock.patch.object(s, 'CRUISE_STATE', Path(self.tmp.name) / 'cruise.json'),
                  mock.patch.object(s, 'GPU_STATE', Path(self.tmp.name) / 'gpu.json'),
                  mock.patch.object(s, '_HIST', {}), mock.patch.object(s, '_BYTES', {}), mock.patch.object(s, '_VER', {})]
        for x in self.p: x.start()

    def tearDown(self):
        for x in self.p: x.stop()
        self.tmp.cleanup()

    def git(self, *a):
        return subprocess.run(['git', '-C', str(self.lane), *a], check=True, capture_output=True, env=ENV).stdout.decode()

    def run_collector(self, day, items):
        """One collector run: replaces data/<day>/news.json, updates liveness, commits (as the lane does)."""
        (self.lane / 'data' / day).mkdir(parents=True, exist_ok=True)
        (self.lane / P(day)).write_text(json.dumps({'items': items}))
        by = {}
        for it in items:
            by[it['classification']] = by.get(it['classification'], 0) + 1
        (self.lane / 'liveness.json').write_text(json.dumps(
            {'last_run_utc': f'{day}T20:00:00Z', 'jobs': {'newsweep': {'saved': P(day), 'by_class': by}}}))
        self.git('add', '-A')
        self.git('commit', '-q', '-m', f'collect {day}')
        s._HIST.clear()  # a new commit is a new process's history (scan and mark are separate processes)

    def scan(self):
        s._HIST.clear()
        out = io.StringIO()
        with mock.patch.object(sys, 'argv', ['intake_scan.py', '--json']), contextlib.redirect_stdout(out):
            s.main()
        return json.loads(out.getvalue())

    def mark(self, receipt=None, through=None):
        d = self.scan()
        out = io.StringIO()
        argv = ['intake_scan.py', '--mark', '--receipt', receipt or d['receipt']]
        if through:
            argv += ['--through', through]
        s._HIST.clear()
        with mock.patch.object(sys, 'argv', argv), contextlib.redirect_stdout(out):
            rc = s.main()
        return rc, out.getvalue()

    def new_keys(self, d):
        return {r['key'] for r in d['new']}

    def test_V1_two_runs_no_scan_between_reads_the_replaced_version(self):
        self.run_collector('2026-11-03', [item('D3', 'NEW')])
        self.assertEqual(self.mark()[0], 0)
        self.run_collector('2026-11-04', [item('overnight hit', 'NEW_WATCH_HIT', hits=[['CYPHER', 'a']]),
                                          item('overnight alert', 'NEW_ALERT')])
        v1 = s.batch_sha(P('2026-11-04'))
        self.run_collector('2026-11-04', [item('afternoon watch', 'NEW_WATCH')])
        d = self.scan()
        self.assertEqual(d['news_batches'], [f"{P('2026-11-04')}@{v1}", P('2026-11-04')])
        new = self.new_keys(d)
        self.assertIn(hit('overnight hit'), new)
        self.assertIn(f"news:NEW_ALERT:{P('2026-11-04')}@{v1}", new)
        self.assertIn(f"news:NEW_WATCH:{P('2026-11-04')}", new)
        self.assertTrue(any('replaced by a later same-day run, read from lane history' in h[1] for h in d['health']))

    def test_V2_after_mark_no_realert_and_no_reread(self):
        self.run_collector('2026-11-03', [item('D3', 'NEW')])
        self.mark()
        self.run_collector('2026-11-04', [item('overnight alert', 'NEW_ALERT')])
        self.run_collector('2026-11-04', [item('afternoon watch', 'NEW_WATCH')])
        self.assertEqual(self.mark(through=P('2026-11-04'))[0], 0)
        st = json.loads(self.seen.read_text())
        self.assertEqual((st['last_marked_batch'], st['last_marked_sha']), (P('2026-11-04'), s.batch_sha(P('2026-11-04'))))
        d = self.scan()
        self.assertEqual(d['news_batches'], [P('2026-11-04')])
        self.assertEqual(self.new_keys(d), set())

    def test_V3_marked_run1_then_runs_2_and_3(self):
        self.run_collector('2026-11-04', [item('run1', 'NEW_WATCH')])
        self.assertEqual(self.mark()[0], 0)  # install: newest only
        self.run_collector('2026-11-04', [item('run2 hit', 'NEW_WATCH_HIT', hits=[['BROCK', 'b']]), item('run2 alert', 'NEW_ALERT')])
        v2 = s.batch_sha(P('2026-11-04'))
        self.run_collector('2026-11-04', [item('run3 watch', 'NEW_WATCH')])
        v3 = s.batch_sha(P('2026-11-04'))
        d = self.scan()
        self.assertEqual(d['news_batches'], [f"{P('2026-11-04')}@{v2}", P('2026-11-04')])
        new = self.new_keys(d)
        self.assertIn(hit('run2 hit'), new)
        self.assertIn(f"news:NEW_ALERT:{P('2026-11-04')}@{v2}", new)
        self.assertIn(f"news:NEW_WATCH:{P('2026-11-04')}@{v3}", new)
        self.assertEqual(self.mark()[0], 0)
        d = self.scan()
        self.assertEqual(d['news_batches'], [P('2026-11-04')])
        self.assertEqual(self.new_keys(d), set())

    def test_V4_catch_up_across_days_oldest_first(self):
        self.run_collector('2026-11-02', [item('D2', 'NEW')])
        self.mark()
        self.run_collector('2026-11-03', [item('D3 a', 'NEW_WATCH')])
        a3 = s.batch_sha(P('2026-11-03'))
        self.run_collector('2026-11-03', [item('D3 b', 'NEW')])
        self.run_collector('2026-11-04', [item('D4 a', 'NEW')])
        a4 = s.batch_sha(P('2026-11-04'))
        self.run_collector('2026-11-04', [item('D4 b', 'NEW')])
        d = self.scan()
        self.assertEqual(d['news_batches'], [f"{P('2026-11-03')}@{a3}", P('2026-11-03'),
                                             f"{P('2026-11-04')}@{a4}", P('2026-11-04')])

    def test_V5_history_unknown_is_loud_and_changes_nothing_else(self):
        self.run_collector('2026-11-03', [item('D3', 'NEW')])
        self.mark()
        self.run_collector('2026-11-04', [item('D4', 'NEW_WATCH')])
        st = json.loads(self.seen.read_text())
        st['last_marked_sha'] = 'feedfacecafe'  # marked version not in history
        self.seen.write_text(json.dumps(st))
        d = self.scan()
        self.assertEqual(d['news_batches'], [P('2026-11-03'), P('2026-11-04')])  # rewritten marked + newest, as before
        self.assertTrue(any('not in lane history' in h[1] and 'UNKNOWN' in h[1] for h in d['health']))
        with mock.patch.object(s, '_git', side_effect=OSError('boom')):
            s._HIST.clear()
            batches, errs = s._version_plan(P('2026-11-04'), P('2026-11-03'), s.batch_sha(P('2026-11-03')))
        self.assertEqual(batches, [P('2026-11-04')])
        self.assertTrue(errs and 'lane history unreadable' in errs[0])

    def test_V6_receipt_binds_versions_and_pointer_can_stop_at_one(self):
        self.run_collector('2026-11-03', [item('D3', 'NEW')])
        self.mark()
        self.run_collector('2026-11-04', [item('v1 hit', 'NEW_WATCH_HIT', hits=[['CYPHER', 'c']])])
        v1 = s.batch_sha(P('2026-11-04'))
        self.run_collector('2026-11-04', [item('v2', 'NEW')])
        v2 = s.batch_sha(P('2026-11-04'))
        d = self.scan()
        self.assertIn(f"{P('2026-11-04')}@{v1}", d['news_batches'])
        self.assertEqual(self.mark(receipt='000000000000')[0], 2)  # stale receipt refused
        st0 = self.seen.read_text()
        self.assertEqual(json.loads(st0)['last_marked_sha'], s.batch_sha(P('2026-11-03')))  # nothing written
        (self.lane / P('2026-11-04')).write_text('{broken')       # a run commits an unreadable file:
        self.git('commit', '-qam', 'broken run')                  # the pointer must stop at v2, the last readable
        v3 = s.batch_sha(P('2026-11-04'))
        rc, out = self.mark()
        self.assertEqual(rc, 0, out)
        st = json.loads(self.seen.read_text())
        self.assertEqual((st['last_marked_batch'], st['last_marked_sha']), (P('2026-11-04'), v2))
        self.run_collector('2026-11-04', [item('v4', 'NEW')])     # a repair run
        d = self.scan()
        self.assertEqual(d['news_batches'], [f"{P('2026-11-04')}@{v3}", P('2026-11-04')])  # resumes after v2
        self.assertNotIn(hit('v1 hit'), self.new_keys(d))

    def test_V7_no_lane_write(self):
        self.run_collector('2026-11-03', [item('D3', 'NEW')])
        self.mark()
        self.run_collector('2026-11-04', [item('a', 'NEW_ALERT')])
        self.run_collector('2026-11-04', [item('b', 'NEW')])
        head, status = self.git('rev-parse', 'HEAD'), self.git('status', '--porcelain')
        self.assertEqual(self.mark()[0], 0)
        self.assertEqual((self.git('rev-parse', 'HEAD'), self.git('status', '--porcelain')), (head, status))

    def test_V8_cruise_queue_reads_replaced_versions(self):
        cand = dict(item('Royal Caribbean prices $1.5 billion senior notes offering', 'KNOWN', entity='Royal Caribbean'),
                    agents=['CRUISE'])
        self.assertTrue(s.is_cruise_capital_candidate(cand))      # the fixture really is a candidate
        self.run_collector('2026-11-04', [cand])
        v1 = s.batch_sha(P('2026-11-04'))
        self.run_collector('2026-11-04', [item('Other', 'NEW')])
        q, errors = s.cruise_capital_queue()
        self.assertEqual(errors, [])
        self.assertEqual([c['title'] for c in q], [cand['title']])
        self.assertEqual(q[0]['rows'][0]['version'], v1)

    def test_V9_gpu_queue_reads_replaced_versions_and_folds(self):
        self.run_collector('2026-11-12', [item('GPU loans wobble', 'NEW', label='gpu-obsolescence-1')])
        v1 = s.batch_sha(P('2026-11-12'))
        self.run_collector('2026-11-12', [item('GPU loans wobble', 'NEW', label='gpu-obsolescence-2')])
        q, errors = s.gpu_finance_queue()
        self.assertEqual(errors, [])
        self.assertEqual(len(q), 1)
        self.assertEqual([r.get('version') for r in q[0]['rows']], [v1, None])


if __name__ == '__main__':
    unittest.main()
