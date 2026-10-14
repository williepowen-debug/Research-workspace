"""Offline consumer tests for the October14 repair. All writes stay in /tmp.

Run: .venv/bin/python3 AGENTS/LIQUID/scripts/test_alert_srf_repair.py
No real timer/state/inbox/SIGNALS writes, market pulls, Git or external sends.
"""
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hy_oas_watch as watcher
import boot
import fetch
import sofr_dispersion

ROOT = Path(__file__).resolve().parents[3]
REPAIR = ROOT / 'AGENTS/LIQUID/research/2026-10-14_alert-SRF-repair'
FIXTURE_RECEIPTS = {}


@contextlib.contextmanager
def isolated_watcher():
    with tempfile.TemporaryDirectory(prefix='liquid-alert-repair-') as td:
        root = Path(td)
        alerts = root / 'AGENTS/LIQUID/alerts'
        alerts.mkdir(parents=True)
        inbox = root / 'PROME/inbox'
        inbox.mkdir(parents=True)
        signals = root / 'AGENTS/SIGNALS.md'
        signals.write_text('| date | owner | target | priority | description | source |\n'
                           '| 2026-10-01 | OTHER_OWNER | PROME | 🟡 | preserve this foreign row | fixture |\n')
        foreign = inbox / 'foreign-owner-packet.md'
        foreign.write_text('Preserve this foreign packet.\n')
        with mock.patch.multiple(watcher, WORKSPACE=root, ALERTDIR=alerts,
                                 ALOG=alerts/'HY_OAS_ALERTS.log', RLOG=alerts/'watch.log',
                                 STATE=alerts/'HY_OAS_STATE', PROME_INBOX=inbox, SIGNALS=signals):
            yield root


def run_watcher(latest, first, prev=None):
    if prev is not None:
        watcher.STATE.write_text(json.dumps(prev))
    with mock.patch.object(fetch, 'fred_fetch', return_value=latest), \
         mock.patch.object(fetch, '_retry_request', return_value=first), \
         mock.patch.object(fetch, 'FRED_API_KEY', 'SYNTHETIC-NO-NETWORK'), \
         mock.patch.object(sys, 'argv', ['hy_oas_watch.py']):
        return watcher.main()


def observations(*pairs):
    return [{'date': d, 'value': v} for d, v in pairs]


def capture(label):
    packets = {f.name: f.read_text() for f in watcher.PROME_INBOX.glob('*UNATTENDED*')}
    result = {'synthetic_fixture': True, 'packets': packets,
              'signals': watcher.SIGNALS.read_text(),
              'alert_log': watcher.ALOG.read_text() if watcher.ALOG.exists() else '',
              'watch_log': watcher.RLOG.read_text() if watcher.RLOG.exists() else '',
              'state': json.loads(watcher.STATE.read_text()) if watcher.STATE.exists() else {}}
    FIXTURE_RECEIPTS[label] = result
    return result


class WatcherConsumerTests(unittest.TestCase):
    def setUp(self):
        self.classify, self.hy = watcher._load_config()
        self.base = {'zone': 'green', 'sev': 0, 'obs_date': '2026-07-01'}

    def assert_kill_meaning(self, text):
        self.assertIn('NOT a kill', text)
        self.assertIn('tape-vs-substance guard', text)
        self.assertIn('do NOT retire the thesis', text)
        self.assertIn('If the arbiter is dark', text)
        self.assertNotIn('X1 CLOSED', text)

    def assert_widen_meaning(self, text):
        self.assertIn('LEVEL print, not a trigger', text)
        self.assertIn('strict `>280` SUSTAINED', text)
        self.assertIn("BROCK's wrapper-leads half", text)
        self.assertIn('Do not size off this packet', text)

    def test_ordinary_kill_actual_main_consumers_and_repeat(self):
        with isolated_watcher():
            latest = observations(('2026-07-03', '2.59'))
            first = {'observations': observations(('2026-07-01', '2.70'),
                                                 ('2026-07-02', '2.59'), ('2026-07-03', '2.59'))}
            self.assertEqual(run_watcher(latest, first, self.base), 0)
            out = capture('ordinary-kill')
            for text in [out['signals'], out['alert_log'], *out['packets'].values()]:
                self.assert_kill_meaning(text)
                self.assertIn('2026-07-03', text)
            self.assertEqual(out['state']['kill_met_on'], '2026-07-03')
            self.assertEqual(run_watcher(latest, first), 0)
            again = capture('ordinary-kill-repeat')
            for key in ('packets', 'signals', 'alert_log'):
                self.assertEqual(again[key], out[key])
            self.assertEqual(again['state']['delivered'], out['state']['delivered'])

    def test_escalation_actual_main_consumers_own_side(self):
        with isolated_watcher():
            self.assertEqual(run_watcher(observations(('2026-10-14', '2.90')),
                                       {'observations': observations(('2026-10-14', '2.90'))}, self.base), 0)
            out = capture('escalation-only')
            for text in [out['signals'], out['alert_log'], *out['packets'].values()]:
                self.assert_widen_meaning(text)
                self.assertNotIn('Kill-level fire:', text)
            self.assertIn('| 2026-10-14 | LIQUID | PROME | 🟠 |', out['signals'])

    def test_mixed_lost_state_all_consumers_original_event_date(self):
        with isolated_watcher():
            latest = observations(('2026-10-14', '2.90'))
            first = {'observations': observations(('2026-07-01', '2.59'),
                                                 ('2026-07-02', '2.58'), ('2026-10-14', '2.90'))}
            self.assertEqual(run_watcher(latest, first), 0)  # no state: recover terminal event
            out = capture('mixed-current-plus-historical')
            packet = next(iter(out['packets'].values()))
            self.assertIn('zone escalation [2026-10-14]', packet)
            self.assertIn('recovered historical kill-level event [2026-07-02]', packet)
            self.assertIn('**Current quote:** HY OAS 290bps [2026-10-14]', packet)
            self.assertNotIn('HY OAS 290bps — kill level met', packet)
            self.assertIn('| 2026-07-02 | LIQUID | ALL | 🔴 |', out['signals'])
            self.assertIn('| 2026-10-14 | LIQUID | PROME | 🟠 |', out['signals'])
            for text in [out['signals'], out['alert_log'], packet]:
                self.assert_kill_meaning(text)
                self.assert_widen_meaning(text)
                self.assertIn('2026-07-02', text)
            self.assertEqual(out['state']['kill_met_on'], '2026-07-02')
            self.assertEqual(run_watcher(latest, first), 0)
            again = capture('mixed-repeat')
            for key in ('packets', 'signals', 'alert_log'):
                self.assertEqual(again[key], out[key])

    def test_late_only_headline_and_log_preserve_history(self):
        with isolated_watcher():
            prev = {'zone': 'red', 'sev': 2, 'obs_date': '2026-10-13'}
            self.assertEqual(run_watcher(observations(('2026-10-14', '2.90')),
                              {'observations': observations(('2026-07-01', '2.59'),
                               ('2026-07-02', '2.58'), ('2026-10-14', '2.90'))}, prev), 0)
            out = capture('historical-only')
            packet = next(iter(out['packets'].values()))
            self.assertIn('recovered historical kill-level event [2026-07-02]', packet)
            self.assertNotIn('zone escalation [', packet)
            self.assertIn('| 2026-07-02 | LIQUID | ALL | 🔴 |', out['signals'])
            self.assert_kill_meaning(out['alert_log'])

    def test_first_published_value_distinct_from_latest_quote(self):
        with isolated_watcher():
            self.assertEqual(run_watcher(observations(('2026-07-03', '2.90')),
                              {'observations': observations(('2026-07-02', '2.59'),
                                                           ('2026-07-03', '2.58'))}, self.base), 0)
            out = capture('revision-latest-versus-first-published')
            self.assertIn('first-published HY OAS 258bps < 260', out['signals'])
            self.assertNotIn('HY OAS 290bps < 260', out['signals'])
            self.assertIn('**Current quote:** HY OAS 290bps', next(iter(out['packets'].values())))

    def test_first_published_frontier_behind_latest_keeps_original_date(self):
        with isolated_watcher():
            self.assertEqual(run_watcher(observations(('2026-07-06', '2.59')),
                              {'observations': observations(('2026-07-02', '2.59'),
                                                           ('2026-07-03', '2.58'))}, self.base), 0)
            out = capture('delayed-first-publication-frontier')
            self.assertEqual(out['state']['kill_met_on'], '2026-07-03')
            self.assertIn('| 2026-07-03 | LIQUID | ALL | 🔴 |', out['signals'])
            self.assertIn('recovered historical kill-level event [2026-07-03]',
                          next(iter(out['packets'].values())))

    def test_guard_not_truncated_and_pipe_safe(self):
        line = watcher.decide(259, '2026-07-03', self.base, self.hy, self.classify,
                              [('2026-07-03', 259), ('2026-07-02', 259)])['fired'][0]
        row = watcher._signals_row(line + ' | extra detail\nnext line', '2026-07-03')
        self.assert_kill_meaning(row)
        self.assertIn('/ extra detail next line', row)
        self.assertEqual(len(row.splitlines()), 1)
        self.assertEqual(row.count('|'), 7)
        self.assertGreater(len(row), 240)

    def test_legacy_dedup_keys_and_foreign_destinations_untouched(self):
        with isolated_watcher():
            fired = watcher.decide(290, '2026-10-14', self.base, self.hy, self.classify)['fired']
            before = capture('legacy-before')
            prev = {'delivered': [f'{line[:24]}|2026-10-14' for line in fired]}
            state = {}
            watcher._deliver(fired, 290, '2026-10-14', state, prev)
            after = capture('legacy-after')
            self.assertEqual(after['packets'], before['packets'])
            self.assertEqual(after['signals'], before['signals'])
            self.assertEqual(state['delivered'], prev['delivered'])
            self.assertEqual((watcher.PROME_INBOX/'foreign-owner-packet.md').read_text(),
                             'Preserve this foreign packet.\n')

    def test_append_preserves_foreign_rows_and_repeat_delivery(self):
        with isolated_watcher():
            fired = watcher.decide(290, '2026-10-14', self.base, self.hy, self.classify,
                                   late_kill='2026-07-02')['fired']
            prefix = watcher.SIGNALS.read_text()
            state = {}
            watcher._deliver(fired, 290, '2026-10-14', state, {})
            after = watcher.SIGNALS.read_text()
            self.assertTrue(after.startswith(prefix))
            self.assertEqual(len(after.splitlines()) - len(prefix.splitlines()), 2)
            watcher._deliver(fired, 290, '2026-10-14', {}, state)
            self.assertEqual(watcher.SIGNALS.read_text(), after)
            self.assertEqual((watcher.PROME_INBOX/'foreign-owner-packet.md').read_text(),
                             'Preserve this foreign packet.\n')

    def test_missing_historical_date_not_relabelled_today(self):
        line = '🚨 KILL-LEVEL MET (NOT a kill) — LATE ALERT: second date unavailable; do NOT retire the thesis.'
        row = watcher._signals_row(line, '2026-10-14')
        self.assertTrue(row.startswith('| UNKNOWN | LIQUID |'))
        self.assertIn('recovered historical kill-level event [UNKNOWN]',
                      watcher._packet_body([line], 290, '2026-10-14')[3])
        self.assertEqual(watcher._event_date(line.replace('second date unavailable',
                               'second dated 2026-99-99'), '2026-10-14'), 'UNKNOWN')

    def test_missing_first_publication_fails_closed(self):
        with isolated_watcher():
            self.assertEqual(run_watcher(observations(('2026-07-03', '2.59')),
                                         {'error': 'synthetic unavailable'}, self.base), 0)
            out = capture('vintage-unavailable')
            self.assertFalse(out['packets'])
            self.assertNotIn('kill_met_on', out['state'])
            self.assertIn('VINTAGE-FETCH-FAIL', out['watch_log'])

    def test_invalid_latest_quote_is_parse_failure_without_grade(self):
        for value in ('not a number', 'nan', 'inf'):
            with self.subTest(value=value), isolated_watcher():
                self.assertEqual(run_watcher(observations(('2026-07-03', value)),
                                  {'observations': []}, self.base), 3)
                out = capture('invalid-latest-'+value)
                self.assertEqual(out['state'], self.base)
                self.assertFalse(out['packets'])
                self.assertIn('PARSE-FAIL', out['watch_log'])

    def test_polling_gap_and_single_known_observation(self):
        with isolated_watcher():
            prev = dict(self.base, obs_date='2026-07-01', sub260=1)
            self.assertEqual(run_watcher(observations(('2026-07-03', '2.59')),
                       {'observations': observations(('2026-07-01', '2.59'),
                         ('2026-07-02', '2.70'), ('2026-07-03', '2.59'))}, prev), 0)
            out = capture('missed-poll-reset')
            self.assertEqual(out['state']['sub260'], 1)
            self.assertNotIn('kill_met_on', out['state'])
        r = watcher.decide(259, '2026-07-03', self.base, self.hy, self.classify)
        self.assertFalse(r['fired'])

    def test_published_boundary_normalization_actual_first_release_and_main(self):
        for value, run in [('2.59', 2), ('2.60', 0), ('2.61', 0),
                           ('2.5999999999999996', 0), ('2.6000000000000005', 0)]:
            with self.subTest(value=value), isolated_watcher():
                self.assertEqual(run_watcher(observations(('2026-07-03', value)),
                            {'observations': observations(('2026-07-02', '2.59'),
                                                          ('2026-07-03', value))}, self.base), 0)
                state = json.loads(watcher.STATE.read_text())
                self.assertEqual(state['bps'], round(float(value)*100))
                self.assertEqual(state['sub260'], run)
                self.assertEqual('kill_met_on' in state, run == 2)


class SRFTests(unittest.TestCase):
    def row(self, t, td, m, md, te=None, me=None):
        boot.RESULTS.clear()
        boot.add_srf_usage(t, td, te, m, md, me)
        self.assertEqual(len(boot.RESULTS), 1)
        return boot.RESULTS[0]

    def test_aligned_quiet_threshold_and_above(self):
        for t, m, marker, display in [(20, 20, '🟢', '$40.00B'),
                                      (25, 25, '🟢', '$50.00B'),
                                      (30, 30, '🔴', '$60.00B')]:
            with self.subTest(t=t, m=m):
                row = self.row(t, '2026-10-13', m, '2026-10-13')
                self.assertEqual((row['marker'], row['display'], row['asof']),
                                 (marker, display, '2026-10-13'))

    def test_mismatched_high_and_quiet_are_ungradeable_and_visible(self):
        for t, m in [(30, 30), (1, 1)]:
            row = self.row(t, '2026-10-12', m, '2026-10-13')
            self.assertEqual((row['display'], row['marker'], row['asof']), ('UNGRADEABLE', '⚪', ''))
            self.assertIn('2026-10-12', row['note'])
            self.assertIn('2026-10-13', row['note'])
            self.assertNotIn('no funding stress', row['note'])
            self.assertNotIn('ABOVE $50B', row['note'])
            with contextlib.redirect_stdout(io.StringIO()) as output:
                boot.render(False)
            self.assertIn('UNGRADEABLE', output.getvalue())

    def test_missing_dates_and_legs(self):
        for td, md in [(None, '2026-10-13'), ('2026-10-13', None), ('', ''),
                       ('UNKNOWN', 'UNKNOWN'), ('2026-99-99', '2026-99-99')]:
            row = self.row(30, td, 30, md)
            self.assertEqual(row['display'], 'UNGRADEABLE')
            self.assertFalse(row['asof'])
        for t, m, te, me in [(30, None, None, 'missing'), (None, 30, 'missing', None),
                              (None, None, 'missing', 'missing'), (30, None, None, None),
                              (float('nan'), 30, None, None), (30, float('inf'), None, None)]:
            row = self.row(t, '2026-10-13', m, '2026-10-13', te, me)
            self.assertEqual(row['display'], 'PARTIAL')
            self.assertIn('combined grade withheld', row['note'])
            self.assertFalse(row['asof'])

    def test_domestic_dashboard_calls_guard_without_network(self):
        def series(sid, n=6):
            if sid == 'RPONTSYD':
                return 30, '2026-10-12', [30], None
            if sid == 'RPONMBSD':
                return 30, '2026-10-13', [30], None
            return None, None, [], 'synthetic unavailable'
        boot.RESULTS.clear()
        with mock.patch.object(boot, 'fred_series', side_effect=series), \
             mock.patch.object(boot, 'fred_pairs', return_value=([], 'synthetic unavailable')), \
             mock.patch.object(boot, 'fred_fetch', return_value=[{'error': 'synthetic unavailable'}]), \
             mock.patch.object(sofr_dispersion, '_load', return_value=[]):
            boot.build_domestic()
        rows = [r for r in boot.RESULTS if r['label'] == 'SRF usage']
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['display'], 'UNGRADEABLE')


if __name__ == '__main__':
    result = unittest.main(verbosity=2, exit=False).result
    # Printed synthetic snapshots are captured in the command receipt, never
    # copied into real alert destinations or interpreted as market observations.
    print('\nSYNTHETIC CONSUMER SNAPSHOTS — not live market events')
    print(json.dumps(FIXTURE_RECEIPTS, indent=2, ensure_ascii=False))
    raise SystemExit(0 if result.wasSuccessful() else 1)
