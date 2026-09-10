"""Consumer regressions: amendments must outrank base prose and fail visibly."""
import copy
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import fleet_dashboard as fd
import heartbeat_projection as hp
import will_brief as wb
import will_handbook as wh

# Frozen 2026-09-08 (Am.#2) snapshot of HEARTBEAT.md + its projection companion. The two
# live-consumer regressions below pin what Am.#2 INVERTED (deploy question closed; FT-10 0/4),
# so they must read this fixture, never the live file — on 9/9 Am.#3 broke both while every
# amendment rule held (a snapshot assertion against a moving surface rots by construction).
FIXTURES = Path(__file__).resolve().parent / 'fixtures'
FIXTURE_FILES = {'HEARTBEAT.md': FIXTURES / 'HEARTBEAT_2026-09-08_am2.md',
                 'PROME/HEARTBEAT_DASHBOARD.md': FIXTURES / 'HEARTBEAT_DASHBOARD_2026-09-08_am2.md'}
_real_read = fd.read


def fixture_read(rel, *args, **kwargs):
    path = FIXTURE_FILES.get(rel)
    return path.read_text(encoding='utf-8') if path else _real_read(rel, *args, **kwargs)

BASE = {"one": "Old decision", "split": "Break 20 / Grind 47 / Unresolved 33",
        "channels": [{"name": "Energy", "headline": "Old headline", "body": "Old body", "cls": "crit"},
                     {"name": "Japan", "headline": "Unchanged", "body": "Dated evidence", "cls": "elev"}],
        "ticker": ["HY OAS 265 [old date]", "USD/JPY 154.29 [old date]"],
        "blocking": [], "base": "2026-09-07"}


def amendment(number, source, updates):
    prose = f"> **AMENDMENT #{number} — 2026-09-08** {source}"
    payload = {"amendment": number, "source_sha256": hashlib.sha256(prose.encode()).hexdigest(), "set": updates}
    return prose + "\n\n```dashboard-amendment\n" + json.dumps(payload) + "\n```\n"


class ProjectionTests(unittest.TestCase):
    def assert_withheld(self, text):
        h = hp.apply_amendments(text, BASE)
        self.assertTrue(h['errors'])
        for field in ('one', 'split', 'channels', 'ticker', 'blocking'):
            self.assertFalse(h[field], field)

    def test_latest_amendment_wins_without_mutating_base(self):
        before = copy.deepcopy(BASE)
        text = amendment(1, 'First ruling', {'one': 'First decision', 'channels': {'Energy': {'body': 'First body'}}})
        text += '\n' + amendment(2, 'Later evidence', {'one': 'Final decision', 'ticker': {'HY OAS': 'HY OAS 268 [new date]'}})
        h = hp.apply_amendments(text, BASE)
        self.assertEqual(h['one'], 'Final decision')
        self.assertEqual(h['channels'][0]['body'], 'First body')
        self.assertEqual(h['channels'][1], BASE['channels'][1])
        self.assertEqual(h['ticker'][1], BASE['ticker'][1])
        self.assertEqual(h['ticker'][0], 'HY OAS 268 [new date]')
        self.assertEqual(BASE, before)

    def test_missing_changed_malformed_and_orphan_projections_withhold(self):
        valid = amendment(1, 'New evidence', {'one': 'Current'})
        cases = [valid.split('```')[0], valid.replace('New evidence', 'Changed evidence'),
                 valid.replace('"set":', '"set"'), valid.rsplit('```', 1)[0],
                 valid + '\n' + amendment(2, 'Unprojected', {}).split('```')[0],
                 valid[valid.index('```'):], valid + '\n' + valid]
        for text in cases:
            with self.subTest(text=text):
                self.assert_withheld(text)

    def test_unsupported_or_ambiguous_targets_withhold(self):
        for updates in [{'unknown': 'value'}, {'channels': {'Unknown': {'body': 'new'}}},
                        {'channels': {'Energy': {'cls': 'guess'}}}, {'ticker': {'HYO': 'HYO 268'}},
                        {'ticker': {'HY OAS': 'DGS10 4.78'}}, {'one': ''}]:
            with self.subTest(updates=updates):
                self.assert_withheld(amendment(1, 'Evidence', updates))

    def test_duplicate_json_fields_rejected(self):
        text = amendment(1, 'Evidence', {'one': 'A'})
        self.assert_withheld(text.replace('"one": "A"', '"one": "A", "one": "B"'))

    def test_unamended_base_still_supported(self):
        h = hp.apply_amendments('No amendments', BASE)
        self.assertFalse(h['errors'])
        for key, value in BASE.items():
            self.assertEqual(h[key], value)


class LiveConsumerTests(unittest.TestCase):
    def test_missing_companion_withholds_amended_state(self):
        read = fd.read
        def missing(path):
            if path == 'PROME/HEARTBEAT_DASHBOARD.md':
                raise FileNotFoundError(path)
            return read(path)
        with patch.object(fd, 'read', side_effect=missing):
            h = fd.parse_heartbeat()
        self.assertTrue(h['errors'])
        self.assertFalse(h['one'])
        self.assertFalse(h['ticker'])

    def test_current_two_regressions_and_unaffected_channels(self):
        with patch.object(fd, 'read', side_effect=fixture_read):
            source = fd.read('HEARTBEAT.md')
            h = fd.parse_heartbeat()
        self.assertFalse(h['errors'])
        self.assertIn('STAND DOWN, NO DEPLOY', h['one'])
        self.assertIn('consumer 0/4, NOT FIRED', h['one'])
        self.assertNotIn('deploy question sits with Will', h['one'])
        self.assertNotIn('earliest fire the 9/9', h['one'])
        channels = {c['name']: c for c in h['channels']}
        self.assertIn('0/4', channels['Equity-vol']['headline'])
        self.assertIn('owner integration pending', channels['Equity-vol']['body'])
        self.assertIn('7 bp', channels['Rates']['body'])
        bare = hp.PROJECTIONS.sub('', hp.AMENDMENTS.sub('', source))
        with patch.object(fd, 'read', return_value=bare):
            old = fd.parse_heartbeat()
        old_channels = {c['name']: c for c in old['channels']}
        for name in ('Japan / carry', 'AI capex', 'Metals'):
            self.assertEqual(channels[name], old_channels[name])
        changed = ('HY OAS', 'DFII10', 'DGS10', '^SKEW', 'WAL', 'USO', 'XLE')
        unaffected = lambda tokens: [t for t in tokens if not any(hp.prefix_matches(t, p) for p in changed)]
        self.assertEqual(unaffected(h['ticker']), unaffected(old['ticker']))
        self.assertEqual(h['split'], old['split'])
        levels = {t['name']: t['val'] for t in fd.parse_tiles(h)}
        self.assertEqual(levels['HY OAS'], 268)
        self.assertEqual(levels['10Y Yield'], 4.78)

    def test_rendered_view_and_age_clock_without_global(self):
        with patch.object(fd, 'read', side_effect=fixture_read):
            page, snap = fd.build(dt.date(2026, 9, 9), '2026-09-09 test')
        self.assertIn('FT-10 consumer 0/4; NOT FIRED', page)
        self.assertIn('STAND DOWN, NO DEPLOY', page)
        self.assertIn('AMENDMENT #2', page)
        self.assertRegex(page, r'data-generated="\d{4}-\d\d-\d\dT.*Z"')
        self.assertFalse(snap['heartbeat_errors'])
        failed = hp.apply_amendments('> **AMENDMENT #1** missing', BASE)
        with patch.object(fd, 'parse_heartbeat', return_value=failed):
            bad_page, bad_snap = fd.build(dt.date(2026, 9, 9), '2026-09-09 test')
        self.assertIn('Current summary and levels withheld', bad_page)
        self.assertNotIn('Old decision', bad_page)
        self.assertTrue(bad_snap['heartbeat_errors'])

    def test_failed_render_does_not_advance_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            out, state = Path(directory) / 'view.html', Path(directory) / 'state.json'
            state.write_text('previous baseline')
            with patch.object(fd, 'STATE_PATH', str(state)), patch.object(fd, 'build', return_value=(
                'visible diagnostic', {'heartbeat_errors': ['bad amendment']})), patch.object(sys, 'argv', ['fleet_dashboard', '-o', str(out)]):
                self.assertEqual(fd.main(), 1)
            self.assertEqual(state.read_text(), 'previous baseline')

    def test_basis_points_respect_each_series_unit(self):
        h = {'ticker': ['HY OAS 268 bp [9/7]', 'CCC 1051 bps [9/3]',
                        'SOFR-IORB 5bp [9/3]']}
        tiles = {t['name']: t for t in fd.parse_tiles(h)}
        self.assertEqual(tiles['HY OAS']['val'], 268)
        self.assertEqual(tiles['HY OAS']['cls'], 'watch')
        self.assertEqual(tiles['CCC OAS']['val'], 1051)
        self.assertEqual(tiles['SOFR-IORB']['val'], 0.05)

    def test_book_header_survives_dated_execution_annotations(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'FORGE'
            path.mkdir()
            (path / 'STATUS.md').write_text('# FORGE\n' + ('Dated receipt explanation. ' * 220)
                + '\n**Updated:** 2026-09-03 | **Fidelity cash (money market):** $18,025.71 (47.11%)'
                + ' | **Fidelity account total:** $38,259.44\n\n## Positions\n')
            with patch.object(wb, 'ROOT', Path(directory)):
                money = wb.parse_money()
            self.assertEqual(money['total'], '38,259.44')
            self.assertEqual(money['cash_pct'], '47.11')

    def test_helm_excludes_closed_call_and_expired_rows(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'FORGE'
            path.mkdir()
            (path / 'STATUS.md').write_text('''## Fidelity — Longs
| Ticker | Type | Qty | Cost | Mark | Value | P&L |
|---|---|---|---|---|---|---|
| USO | Stock | 37 | $122.28 | $149 | $5513 | +20% |
| ~~USO~~ | $135C Oct-16 | 0 | $7.11 | — | $0 | CLOSED |
| ~~OZK~~ | $45P Aug-21 | 4 | $3.69 | $0 | $0 | EXPIRED |
''')
            with patch.object(wh, 'ROOT', Path(directory)):
                positions = wh.parse_positions([])
            self.assertEqual([(r['ticker'], r['pos'], r['qty']) for r in positions],
                             [('USO', 'Stock', '37')])


if __name__ == '__main__':
    unittest.main()
