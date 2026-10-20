"""Offline command-path guards for shipped BOND grader defects.
Run: root .venv/bin/python -m unittest discover -s AGENTS/BOND/monitors -p test_monitor_repairs.py -v
"""
import contextlib
import csv
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import grade_auction as g
import buyback_f2 as f2


class GraderPaths(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.snapshot = Path(self.tmp.name) / 'bars.json'
        self.snap = dict(cusip='TARGET', auction_date='2026-10-21', term='20-Year', tips=False,
                         frozen_on='2026-10-15', source='pre-print fixture', n=12,
                         ind_min=52.47, dlr_max=17.59, btc_min=2.36, p15=57.96, p15_reopen=64.24)
        self.rows = [g._fx(f'2025-{m:02d}-15', '20-Year', 56.3147+m,
                           reopening=True) for m in range(1, 13)]
        self.target = g._fx('2026-10-21', '20-Year', 57.96, cusip='TARGET', reopening=True)
        g.DEGENERATE.clear()
        self.addCleanup(g.DEGENERATE.clear)

    def run_grade(self, rows=None, pending=None, frozen=True, extra=None, date=False):
        self.snapshot.write_text(json.dumps(self.snap))
        argv = ['grade', '--date', '2026-10-21'] if date else ['grade', '--cusip', 'TARGET']
        if frozen:
            argv += ['--frozen-bars', str(self.snapshot)]
        argv += extra or []
        out = io.StringIO()
        with patch.object(g, 'load', return_value=self.rows + [self.target] if rows is None else rows), \
             patch.object(g, '_get', return_value=pending or []), patch('sys.argv', argv), \
             contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            rc = g.main()
        return rc, out.getvalue()

    def test_published_bar_boundaries_all_tenors(self):
        for raw in [54.8206, 58.8985, 59.424, 57.434, 65.0503, 57.9647, 63.894]:
            bar = g.published_bar(raw)
            self.snap['p15'] = bar
            for delta, expected in [(-0.0001, 'YES'), (0, 'NO'), (0.0001, 'NO')]:
                with self.subTest(raw=raw, delta=delta):
                    self.target['ind'] = bar + delta
                    rc, text = self.run_grade()
                    self.assertEqual(rc, 0)
                    line = next(x for x in text.splitlines() if "I' indirect below P15" in x)
                    self.assertIn('? ' + expected, line)

    def test_registered_snapshot_wins_over_different_rolling_pool(self):
        rc, text = self.run_grade()
        self.assertEqual(rc, 0)
        self.assertIn('57.96 vs 57.96', text)
        self.assertIn('RAW ROLLING AUDIT', text)
        self.assertIn('reopening-only alt: YES', text)

    def test_strict_old_and_cover_equality_then_breaches(self):
        self.target.update(ind=52.47, dlr=17.59, btc=2.36)
        rc, text = self.run_grade()
        self.assertEqual(rc, 0)
        for label in ['MIN ? NO', 'MAX ? NO']:
            self.assertIn(label, text)
        self.assertIn('CLEAN', text)  # OLD/cover clean, independent I-prime can fire
        self.target.update(ind=52.4699, dlr=17.5901, btc=2.3599)
        self.assertIn('COMPOSITION FAILURE', self.run_grade()[1])

    def test_no_snapshot_is_audit_only(self):
        rc, text = self.run_grade(frozen=False)
        self.assertEqual(rc, 0)
        self.assertIn('AUDIT ONLY', text)
        self.assertIn('NO GATE VERDICT', text)
        self.assertNotIn('Signal LIQUID', text)

    def test_bad_snapshots_fail_closed(self):
        for key, value in [('cusip', 'OTHER'), ('auction_date', '2026-10-22'), ('term', '5-Year'),
                           ('tips', True), ('tips', 0), ('p15', 57.9647), ('p15', float('nan')),
                           ('p15', True), ('p15', None), ('frozen_on', '2026-10-21'),
                           ('n', 5), ('source', '')]:
            with self.subTest(key=key, value=value):
                old = self.snap[key]
                self.snap[key] = value
                rc, text = self.run_grade()
                self.assertEqual(rc, 2)
                self.assertIn('GAP', text)
                self.snap[key] = old

    def test_non_object_snapshots_fail_as_gap(self):
        for snap in [[], None, 42]:
            old = self.snap
            self.snap = snap
            rc, text = self.run_grade()
            self.assertEqual(rc, 2)
            self.assertIn('GAP', text)
            self.snap = old

    def test_tips_grade_and_preprint_have_no_iprime(self):
        for row in self.rows + [self.target]:
            row['tips'] = True
        self.snap.update(tips=True, p15=None, p15_reopen=None)
        for pending in [[], [dict(cusip='TARGET', auctionDate='2026-10-21',
                                  securityTerm='20-Year', tips='Yes', reopening='Yes')]]:
            rc, text = self.run_grade(pending=pending)
            self.assertEqual(rc, 0)
            self.assertIn('NOT DEFINED FOR TIPS', text)
            self.assertNotIn("I' indirect below P15", text)
            self.assertNotIn('indirect < 57.96', text)

    def test_latest_degenerate_never_falls_back_to_original(self):
        g.DEGENERATE.append(('2026-10-21', 'TARGET', 'fixture', 'single leg'))
        original = dict(self.target, date='2026-09-15')
        rc, text = self.run_grade(rows=self.rows + [original])
        self.assertEqual(rc, 2)
        self.assertIn('GAP', text)
        self.assertNotIn('GRADE —', text)

    def test_bad_old_print_does_not_block_pending_reopening(self):
        g.DEGENERATE.append(('2026-09-15', 'TARGET', 'fixture', 'single leg'))
        pending = [dict(cusip='TARGET', auctionDate='2026-10-21', securityTerm='20-Year',
                        tips='No', reopening='Yes')]
        rc, text = self.run_grade(rows=self.rows, pending=pending)
        self.assertEqual(rc, 0)
        self.assertIn('PRE-PRINT', text)
        self.assertNotIn('GRADE —', text)

    def test_date_names_corrupt_neighbour_while_grading_clean(self):
        g.DEGENERATE.append(('2026-10-21', 'OTHER', 'fixture', 'single leg'))
        rc, text = self.run_grade(date=True)
        self.assertEqual(rc, 0)
        self.assertIn('OTHER', text)
        self.assertIn('GAP', text)
        self.assertIn('GRADE —', text)

    def test_thin_pool_prints_no_standalone_marker(self):
        rc, text = self.run_grade(rows=self.rows[:3] + [self.target], frozen=False)
        self.assertEqual(rc, 0)
        self.assertIn('NO GATE VERDICT', text)
        self.assertNotIn('STANDALONE MARKER', text)

    def test_both_loaders_exclude_and_report_bad_rows_each_load(self):
        fields = dict(auction_date='2026-09-15', cusip='BAD', tenor='20Y',
                      total_competitive_accepted='1100', primary_dealer_accepted='100',
                      direct_bidder_accepted='200', indirect_bidder_accepted='700', bid_to_cover_ratio='2.5')
        path = Path(self.tmp.name) / 'corpus.csv'
        with path.open('w') as out:
            writer = csv.DictWriter(out, fieldnames=list(fields))
            writer.writeheader(); writer.writerow(fields)
        ta = dict(securityType='Bond', cusip='BADTA', auctionDate='2026-09-16',
                  indirectBidderAccepted='700', directBidderAccepted='200', primaryDealerAccepted='100',
                  competitiveAccepted='1100')
        with patch.object(g, 'CORPUS', path), patch.object(g, 'frn_cusips', return_value={'FRN'}), \
             patch.object(g, '_get', return_value=[ta]):
            for _ in range(3):
                output = io.StringIO()
                with contextlib.redirect_stderr(output):
                    rows = g.load()
                self.assertEqual(rows, [])
                self.assertEqual(len(g.DEGENERATE), 2)
                self.assertIn('BADTA', output.getvalue())
                self.assertIn('BAD', output.getvalue())

    def test_frozen_snapshot_remains_authority_when_audit_missing_or_thin(self):
        self.target.update(ind=40, dlr=40, btc=2)
        for rows in [[self.target], self.rows[:1] + [self.target]]:
            rc, text = self.run_grade(rows=rows)
            self.assertEqual(rc, 0)
            self.assertIn('COMPOSITION FAILURE', text)
            self.assertIn("I' indirect below P15", text)
            self.assertIn('below trailing-12 MIN', text)
            self.assertNotIn('NO GATE VERDICT', text)

    def test_malformed_latest_rows_never_grade_stale_original(self):
        base = dict(securityType='Bond', cusip='TARGET', auctionDate='2026-10-21',
                    indirectBidderAccepted='60', directBidderAccepted='20', primaryDealerAccepted='20',
                    competitiveAccepted='100', bidToCoverRatio='2.5')
        mutations = [('indirectBidderAccepted', None), ('indirectBidderAccepted', 'inf'),
                     ('primaryDealerAccepted', 'nan'), ('competitiveAccepted', None),
                     ('competitiveAccepted', 'inf'), ('competitiveAccepted', 'nan'),
                     ('competitiveAccepted', '0'), ('competitiveAccepted', '-1'),
                     ('bidToCoverRatio', None), ('bidToCoverRatio', 'inf')]
        for key, value in mutations:
            with self.subTest(key=key, value=value):
                ta = dict(base, **{key: value})
                g.DEGENERATE.clear()
                with patch.object(g, '_get', return_value=[ta]):
                    self.assertEqual(g._from_ta_ws(), [])
                original = dict(self.target, date='2026-09-15')
                rc, text = self.run_grade(rows=self.rows + [original])
                self.assertEqual(rc, 2)
                self.assertNotIn('GRADE —', text)

    def test_tips_preprint_with_no_rolling_history(self):
        self.snap.update(tips=True, p15=None, p15_reopen=None)
        pending = [dict(cusip='TARGET', auctionDate='2026-10-21', securityTerm='20-Year',
                        tips='Yes', reopening='Yes')]
        rc, text = self.run_grade(rows=[], pending=pending)
        self.assertEqual(rc, 0)
        self.assertIn("I' NOT DEFINED FOR TIPS", text)
        self.assertNotIn("I' indirect below P15", text)

    def test_preprint_rejects_mismatched_snapshot(self):
        self.snap['cusip'] = 'OTHER'
        pending = [dict(cusip='TARGET', auctionDate='2026-10-21', securityTerm='20-Year',
                        tips='No', reopening='Yes')]
        rc, text = self.run_grade(rows=self.rows, pending=pending)
        self.assertEqual(rc, 2)
        self.assertIn('GAP', text)

    def test_degenerate_neighbours(self):
        self.assertIsNone(g.degenerate_reason(60, 0, 40, 100))
        self.assertEqual(g.degenerate_reason(None, 20, 80), 'missing')
        for legs in [(0, 0, 100), (float('nan'), 20, 80), (float('inf'), 20, 80), (1e308, 1e308, 1e308), (-1, 20, 81)]:
            self.assertTrue(g.degenerate_reason(*legs))


class PacketOutput(unittest.TestCase):
    def test_buyback_real_fixture_packet_uses_vintage_base_rate(self):
        fixture = json.loads(Path(f2.FIXTURE).read_text())
        vintage = json.loads(Path(f2.VINTAGE_FIXTURE).read_text())['vintage']
        metrics = f2.metrics(fixture['operation'], fixture['security_details'], vintage)
        packet = f2.render_packet(metrics)
        self.assertIn('base rate 1/53, 2024-06-05 through 2026-09-24', packet)
        self.assertNotIn('base rate 0/52', packet)
        self.assertTrue(metrics['verdict'].startswith('OFF'))


if __name__ == '__main__':
    unittest.main()
