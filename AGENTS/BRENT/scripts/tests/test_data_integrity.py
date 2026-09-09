"""Behavioral regressions for the September 9 audit defects (offline inputs)."""
import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))


def module(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / (name + '.py'))
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


quotes = module('thresholds')
eia = module('eia_weekly')
pred = module('predictions_due')
countdown = module('catalyst_countdown')
ratios = module('refiner_ratios')
cot = module('cot_grade')
composites = module('composites')
instruments = module('instrument_check')
NOW = datetime(2026, 9, 9, 16, 0, tzinfo=timezone.utc)
WEEK = date(2026, 9, 4)


class QuoteIntegrity(unittest.TestCase):
    def quote(self, **changes):
        data = dict(regularMarketPrice=110, regularMarketPreviousClose=100,
                    regularMarketTime=(NOW - timedelta(minutes=15)).timestamp())
        data.update(changes)
        return quotes.quote_record(data, now=NOW)

    def grade(self, quote):
        with patch.object(quotes, 'MARKET_THRESHOLDS', [('USO', 'above', 105, 'risk', 'fixture')]):
            return quotes.check_market_thresholds({'USO': quote})

    def test_previous_close_does_not_become_current_quote(self):
        q = self.quote(regularMarketPrice=None, previousClose=150)
        self.assertIsNone(q['price'])
        self.assertEqual(q['state'], 'UNGRADED')
        self.assertEqual(len(self.grade(q)[1]), 1)

    def test_missing_stale_future_nonfinite_quotes_do_not_grade(self):
        for changes in [dict(regularMarketTime=None), dict(regularMarketTime=946684800),
                        dict(regularMarketTime=(NOW + timedelta(seconds=1)).timestamp()),
                        dict(regularMarketPrice=float('nan')), dict(regularMarketPrice=float('inf'))]:
            with self.subTest(changes=changes):
                alerts, ungraded = self.grade(self.quote(**changes))
                self.assertEqual(alerts, [])
                self.assertEqual(len(ungraded), 1)

    def test_recent_quote_preserves_timestamp_and_breach(self):
        q = self.quote()
        alerts, ungraded = self.grade(q)
        self.assertEqual(ungraded, [])
        self.assertEqual(alerts[0]['status'], 'BREACHED')
        self.assertEqual(alerts[0]['date'], q['date'])
        self.assertAlmostEqual(q['chg'], 10)

    def test_unavailable_previous_close_is_not_zero_change(self):
        self.assertIsNone(self.quote(regularMarketPreviousClose=None)['chg'])

    def test_stale_context_is_labeled_in_display(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            quotes.print_quote('USO', 'USO', {'USO': self.quote(regularMarketTime=946684800)})
        self.assertIn('UNGRADED', out.getvalue())
        self.assertIn('2000-', out.getvalue())


class EIAIntegrity(unittest.TestCase):
    def api(self, sid, route=None, limit=None):
        if sid == eia.GAS_SUPPLIED_SERIES[0]:
            return [{'date': (WEEK - timedelta(weeks=i)).isoformat(), 'value': 100 if i < 4 else 80}
                    for i in range(60)]
        return [{'date': WEEK.isoformat(), 'value': 1000},
                {'date': (WEEK - timedelta(weeks=1)).isoformat(), 'value': 900}]

    def fetch(self, reader=None):
        fake = SimpleNamespace(EIA_API_KEY='fixture', eia_fetch=reader or self.api)
        with patch.object(eia, 'HAVE_FORGE', True), patch.object(eia, '_forge', fake):
            return eia.fetch_live_metrics()

    def test_complete_dated_api_result_and_four_week_comparison(self):
        m = self.fetch()
        self.assertEqual(eia.coverage(m, today=NOW.date()), [])
        self.assertAlmostEqual(m['gas_yoy_latest'], 25)
        self.assertAlmostEqual(m['cushing_wow'], .1)

    def test_partial_api_is_findings_not_full_success(self):
        def only_util(sid, **kwargs):
            return self.api(sid, **kwargs) if sid == 'WPULEUS3' else []
        m = self.fetch(only_util)
        self.assertIn('missing cushing', eia.coverage(m, today=NOW.date()))
        with patch.object(eia, 'fetch_live_metrics', return_value=m), patch.object(sys, 'argv', ['eia_weekly.py', '--live']):
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(eia.main(), 2)
        self.assertNotIn('not fired', out.getvalue())
        self.assertIn('gas_yoy_latest: UNKNOWN', out.getvalue())

    def test_null_week_is_not_removed_from_yoy_window(self):
        values = eia.dated_values(self.api(eia.GAS_SUPPLIED_SERIES[0]))
        for missing in [WEEK - timedelta(weeks=1), WEEK - timedelta(weeks=53)]:
            with self.subTest(missing=missing):
                gappy = dict(values); gappy[missing] = None
                self.assertIsNone(eia.gas_comparison(gappy, WEEK))

    def test_date_join_is_order_independent(self):
        rows = self.api(eia.GAS_SUPPLIED_SERIES[0])
        self.assertEqual(eia.gas_comparison(eia.dated_values(rows[::-1]), WEEK), 25)

    def test_wow_requires_adjacent_week_and_does_not_backfill_latest_null(self):
        def gap(sid, **kwargs):
            rows = self.api(sid, **kwargs)
            if sid == 'WCSSTUS1':
                rows[1]['date'] = (WEEK - timedelta(weeks=2)).isoformat()
            if sid == 'W_EPC0_SAX_YCUOK_MBBL':
                rows[0]['value'] = None
            return rows
        m = self.fetch(gap)
        self.assertNotIn('spr_wow', m)
        self.assertNotIn('cushing', m)

    def test_mixed_metric_weeks_and_future_dates_are_findings(self):
        m = self.fetch()
        m['dates']['util'] = (WEEK - timedelta(weeks=1)).isoformat()
        self.assertIn('mixed observation weeks; no synchronized report', eia.coverage(m, today=NOW.date()))
        m['dates']['util'] = '2026-10-01'
        self.assertIn('util: future observation', eia.coverage(m, today=NOW.date()))

    def test_current_saved_report_values_and_notice_fallback(self):
        report = (eia.EIA_DATA_DIR / 'eia_2026-09-02.md').read_text()
        m = eia.extract_metrics(report)
        self.assertEqual(m['week_ending'], '2026-08-28')
        self.assertEqual(m['report_date'], '2026-09-02')
        self.assertEqual(m['cushing'], 22.508)
        self.assertEqual(m['gas_yoy_latest'], -1.6)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'eia_2026-09-02.md').write_text(report)
            (root / 'eia_2026-09-09.md').write_text('# Publication notice: NO NEW REPORT\n')
            with patch.object(eia, 'EIA_DATA_DIR', root):
                self.assertEqual(eia.find_latest_eia_file().name, 'eia_2026-09-02.md')

    def test_conflicting_duplicates_remain_unusable(self):
        rows = [{'date': WEEK.isoformat(), 'value': v} for v in (1, 2, 1)]
        self.assertIsNone(eia.dated_values(rows)[WEEK])

    def test_copy_mtime_cannot_refresh_old_local_data(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / 'eia_2026-04-15.md'
            p.write_text('# EIA Weekly Petroleum Status Report — Week Ending 2026-04-10\n'
                         '**Released:** 2026-04-15\n| **Refinery utilization** | **98.0%** | 97% | +1pp |\n')
            with patch.object(eia, 'EIA_DATA_DIR', p.parent), patch.object(sys, 'argv', ['eia_weekly.py', '--local']):
                with contextlib.redirect_stdout(io.StringIO()) as out:
                    self.assertEqual(eia.main(), 2)
            self.assertIn('LOCAL', out.getvalue())
            self.assertIn('STALE observation 2026-04-10', out.getvalue())
            self.assertNotIn('LIVE pull', out.getvalue())

    def test_retired_trigger_and_universal_floor_do_not_reappear(self):
        self.assertIn('record only', eia.status_for_gas_yoy(-10)[1])
        self.assertNotIn('separate and live', eia.status_for_spr(250)[1])


class DeadlineAndRetirement(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        p = Path(self.folder.name) / 'predictions.tsv'
        p.write_text('BRT-07\t2026-03-06\tfixture claim\t50%\tWithin 7 days of reopening\tOPEN — OUTER BOUND 2027-03-06\t\t\t\t\n'
                     'BRT-29\t2026-07-21\t(M) carriers announce by Aug-31; (T) later\t55%\tBy 2026-09-30\tOPEN\t\t\t\tM unresolved\n')
        patcher = patch.object(pred, 'PRED', p)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_outer_bound_becomes_due_without_inventing_event(self):
        due, _, _, _ = pred.scan(today=date(2027, 3, 7))
        row = next(row for row in due if row[0] == 'BRT-07')
        self.assertEqual(row[2], date(2027, 3, 6))
        self.assertIn('precondition not inferred', row[1])

    def test_conditional_without_outer_bound_does_not_crash(self):
        with patch.object(pred, 'scan', return_value=([], [], [], [('TEST', 'Within 7 days of reopening', 'OPEN')])), patch.object(pred, 'sub_obligations', return_value=[]):
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(pred.main(), 0)

    def test_M_deadline_is_separate_from_final_prediction(self):
        rows = pred.sub_obligations(today=NOW.date())
        self.assertEqual(rows[0][2], date(2026, 8, 31))
        self.assertNotIn('BRT-29', [r[0] for r in pred.scan(today=NOW.date())[0]])

    def test_countdown_is_explicitly_weekdays_not_trading_sessions(self):
        self.assertEqual(countdown.weekdays_between(date(2026, 9, 4), date(2026, 9, 8)), 2)
        with contextlib.redirect_stdout(io.StringIO()) as out, patch.object(sys, 'argv', ['countdown.py']):
            countdown.main()
        self.assertIn('holidays are included', out.getvalue())
        self.assertNotIn('d trd', out.getvalue())

    def test_retired_cli_neither_fetches_nor_appends(self):
        with patch.object(ratios, 'fetch_history') as fetch, patch.object(ratios, 'append_tsv') as append:
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(ratios.main(), 0)
        fetch.assert_not_called(); append.assert_not_called()

    def test_cot_frozen_deadband_stays_correct(self):
        self.assertEqual([cot.leg_a(v) for v in [109164, 109165, 113745, 118325, 118326]],
                         ['SPENT', 'NO-VERDICT', 'NO-VERDICT', 'NO-VERDICT', 'NOT-SPENT'])


class CompositeIntegrity(unittest.TestCase):
    def prices(self, values, when=None):
        now = when or datetime(2026, 9, 9, 18, 30, tzinfo=timezone.utc)
        return {symbol: quotes.quote_record(dict(symbol=symbol, currency='USD', regularMarketPrice=value,
                    regularMarketPreviousClose=100, regularMarketTime=(now - timedelta(minutes=1)).timestamp()), now=now)
                for symbol, value in values.items()}

    def test_tanker_all_three_names_and_sign_discarded(self):
        p = self.prices(dict(STNG=99, FRO=104, DHT=98))
        r = composites.tanker_snapshot(p, now=datetime(2026, 9, 9, 18, 30, tzinfo=timezone.utc))
        self.assertEqual(r['problems'], [])
        self.assertAlmostEqual(r['max_absolute_percent'], 4)
        self.assertTrue(r['window_open'])
        self.assertNotIn('grade', r)
        del p['DHT']
        self.assertIsNone(composites.tanker_snapshot(p)['max_absolute_percent'])

    def test_tanker_delayed_pre1400_print_cannot_open_window(self):
        now = datetime(2026, 9, 9, 18, 5, tzinfo=timezone.utc)
        p = self.prices(dict(STNG=99, FRO=104, DHT=98), when=now - timedelta(minutes=10))
        self.assertFalse(composites.tanker_snapshot(p, now=now)['window_open'])

    def test_large_leg_time_skew_is_ungraded(self):
        p = self.prices(dict(STNG=99, FRO=104, DHT=98))
        p['DHT']['date'] = '2026-09-09T18:20:00+00:00'
        self.assertIn('quote legs differ by more than five minutes', composites.tanker_snapshot(p)['problems'])

    def test_explicit_futures_units_and_orientation(self):
        p = self.prices({'CLX26.NYM': 95, 'BZX26.NYM': 100, 'HOX26.NYM': 4})
        r = composites.futures_snapshot(p, 'CLX26.NYM', 'BZX26.NYM', 'HOX26.NYM')
        self.assertEqual(r['spreads_usd_per_bbl'], {'WTI_minus_Brent': -5, 'ULSD_minus_Brent': 68, 'ULSD_minus_WTI': 73})

    def test_mismatched_maturities_continuous_and_wrong_currency_rejected(self):
        for symbols in [('CLV26.NYM', 'BZX26.NYM', 'HOX26.NYM'), ('CL=F', 'BZ=F', 'HO=F')]:
            p = self.prices(dict(zip(symbols, [95, 100, 4])))
            self.assertIsNone(composites.futures_snapshot(p, *symbols)['spreads_usd_per_bbl'])
        p = self.prices({'CLX26.NYM': 95, 'BZX26.NYM': 100, 'HOX26.NYM': 4})
        p['HOX26.NYM']['currency'] = 'GBP'
        self.assertIsNone(composites.futures_snapshot(p, 'CLX26.NYM', 'BZX26.NYM', 'HOX26.NYM')['spreads_usd_per_bbl'])


class CompositeRegistryRouting(unittest.TestCase):
    def setUp(self):
        instruments._PROBE_CACHE.clear()
        self.row = dict(probe='basket:STNG,FRO,DHT', probe_scope='all_components',
                        max_stale_days='-1')

    def test_complete_basket_still_requires_owner_grade(self):
        with patch.object(instruments, 'probe_tanker_basket', return_value=(True, NOW, 'all three')):
            findings, probed, detail = instruments.evaluate(self.row)
        codes = {f['code'] for f in findings}
        self.assertTrue(probed)
        self.assertIn('REACHABLE', codes)
        self.assertIn('OWNER_GRADE_REQUIRED', codes)
        self.assertNotIn('PARTIAL_COVERAGE', codes)

    def test_missing_leg_cannot_pass_probe(self):
        with patch.object(instruments, 'probe_tanker_basket', return_value=(False, None, 'DHT absent')):
            findings, _, _ = instruments.evaluate(self.row)
        self.assertIn('DEAD', {f['code'] for f in findings})

    def test_single_leg_cannot_claim_all_components(self):
        self.row['probe'] = 'yf:STNG'
        findings, _, _ = instruments.evaluate(self.row, quick=True)
        self.assertIn('UNKNOWN_PROBE_SCOPE', {f['code'] for f in findings})


if __name__ == '__main__':
    unittest.main()
