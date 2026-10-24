"""Offline tests for edgar_doc.py `facts` (start/accn kept) and `compare` (DOCKET L834).

Run from the repository root:
  PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s AGENTS/DEWEY/scripts -p test_edgar_xbrl_compare.py -v

The first twelve tests are CATO's author tests (AGENTS/CATO/runs/2026-10-24_sec-comparison/
test_prepare.py, commit 38e1c2304) ported unchanged in substance, run against
edgar_doc.compare_build / compare_markdown. The rest cover PROME's acceptance
properties and the neighbours in ACCEPTANCE_edgar_xbrl_compare_2026-10-24.md.
No network: every source call is a fixture or a mock. Saves go to a temp dir.
"""

import contextlib
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
FIX = HERE / 'fixtures'
RESPONSE = FIX / 'sec-response_0000320193_NetIncomeLoss_2026-10-24.json'
CATO_PACKET = FIX / 'cato_comparison_0000320193_NetIncomeLoss_2026-10-24.json'
CATO_PROBE = FIX / 'cato_reader-probe_0000320193_NetIncomeLoss_2026-10-24.json'

spec = importlib.util.spec_from_file_location('edgar_doc', HERE / 'edgar_doc.py')
edgar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(edgar)
build, markdown = edgar.compare_build, edgar.compare_markdown

LIMITS_2D = [  # packet §2(d), verbatim
    'Filing cutoff is not a historical API snapshot.',
    'Same concept/unit and similar duration do not establish accounting comparability.',
    'Standard entity-level US-GAAP facts only; custom tags and segment facts need document work.',
    'Filing links identify sources; the source statements have not been independently reconciled.',
    'A fact appears in the SEC API only after the XBRL filing is processed; a press-release number is not in it.',
]
CLI = ['--cik', '0000320193', '--concept', 'NetIncomeLoss', '--unit', 'USD',
       '--prior', '2025-03-30', '2025-06-28', '--current', '2026-03-29', '2026-06-27',
       '--as-of', '2026-10-24']


class ComparisonTests(unittest.TestCase):
    """CATO's twelve, ported."""

    def setUp(self):
        self.raw = RESPONSE.read_bytes()
        self.data = json.loads(self.raw)
        self.args = dict(cik='0000320193', concept='NetIncomeLoss', unit='USD',
                         prior=['2025-03-30', '2025-06-28'],
                         current=['2026-03-29', '2026-06-27'], as_of='2026-10-24',
                         retrieved_at='2026-10-24T21:43:10.239847+00:00')

    def run_data(self, **args):
        return build(json.dumps(self.data).encode(), **(self.args | args))

    def current(self):
        return next(v for v in self.data['units']['USD'] if v.get('start') == '2026-03-29')

    def test_real_response_and_render(self):
        packet = build(self.raw, **self.args)
        self.assertEqual(packet['prior']['val'], 23434000000)
        self.assertEqual(packet['current']['val'], 29789000000)
        self.assertEqual(packet['calculation']['difference'], 6355000000)
        self.assertIn('2026-03-29 to 2026-06-27', markdown(packet))
        self.assertIn(packet['response_sha256'], markdown(packet))
        self.assertIn(packet['current']['filing_url'], markdown(packet))

    def test_quarter_vs_nine_months_rejected(self):
        with self.assertRaisesRegex(ValueError, 'mismatched durations'):
            self.run_data(current=['2025-09-28', '2026-06-27'])

    def test_missing_period_and_wrong_unit(self):
        for args in ({'unit': 'EUR'}, {'current': ['2026-03-28', '2026-06-26']}):
            with self.subTest(args=args), self.assertRaisesRegex(ValueError, 'Missing period'):
                self.run_data(**args)

    def test_wrong_issuer_or_concept(self):
        for args in ({'cik': '1'}, {'concept': 'Revenues'}):
            with self.subTest(args=args), self.assertRaisesRegex(ValueError, 'does not match'):
                self.run_data(**args)

    def test_missing_source_identity(self):
        del self.current()['accn']
        with self.assertRaisesRegex(ValueError, 'identity'):
            self.run_data()

    def test_conflicting_latest_record(self):
        other = copy.deepcopy(self.current())
        other['val'] += 1
        self.data['units']['USD'].append(other)
        with self.assertRaisesRegex(ValueError, 'Ambiguous'):
            self.run_data()

    def test_filing_cutoff_excludes_later_revision(self):
        other = copy.deepcopy(self.current())
        other.update(filed='2026-10-23', accn='0000320193-26-000099', val=1)
        self.data['units']['USD'].append(other)
        earlier = self.run_data(as_of='2026-08-01')
        later = self.run_data()
        self.assertEqual(earlier['current']['val'], 29789000000)
        self.assertEqual(later['current']['val'], 1)

    def test_cutoff_before_current_filing(self):
        with self.assertRaisesRegex(ValueError, 'No filing'):
            self.run_data(as_of='2026-07-01')

    def test_no_change(self):
        self.current()['val'] = 23434000000
        packet = self.run_data()
        self.assertEqual(packet['calculation']['difference'], 0)
        self.assertEqual(packet['calculation']['percent_change'], 0)

    def test_nonpositive_base_keeps_difference(self):
        for v in self.data['units']['USD']:
            if v.get('start') == '2025-03-30':
                v['val'] = 0
        packet = self.run_data()
        self.assertIsNone(packet['calculation']['percent_change'])
        self.assertEqual(packet['calculation']['difference'], 29789000000)

    def test_overlap_rejected(self):
        with self.assertRaisesRegex(ValueError, 'nonoverlapping'):
            self.run_data(prior=self.args['current'])

    def test_retrieval_requires_timezone(self):
        with self.assertRaisesRegex(ValueError, 'timezone'):
            self.run_data(retrieved_at='2026-10-24T21:43:10')


def run_cli(argv, get=None, save_root=None):
    """Run edgar_doc main() with argv; route compare saves to save_root."""
    out, err = io.StringIO(), io.StringIO()
    real = edgar._cmd_compare
    ctx = [patch.object(edgar.sys, 'argv', ['edgar_doc.py', *argv]),
           patch.object(edgar, '_cmd_compare', lambda a: real(a, save_root))]
    if get is not None:
        ctx.append(patch.object(edgar, '_get', get))
    with contextlib.ExitStack() as st:
        for c in ctx:
            st.enter_context(c)
        st.enter_context(contextlib.redirect_stdout(out))
        st.enter_context(contextlib.redirect_stderr(err))
        try:
            rc = edgar.main()
        except SystemExit as e:
            rc = e.code
    return rc, out.getvalue(), err.getvalue()


class AcceptanceTests(unittest.TestCase):
    """PROME §4 properties A1–A8 and the neighbours."""

    def setUp(self):
        self.raw = RESPONSE.read_bytes()
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    # A1 — facts is a superset; the probe pair is distinguishable
    def test_facts_superset_distinguishes_quarter_from_nine_months(self):
        probe = json.loads(CATO_PROBE.read_text())['producer_excerpt']
        rc, out, _ = run_cli(['facts', '--cik', '0000320193', '--concept', 'NetIncomeLoss'],
                             get=lambda url, h: json.dumps(probe).encode())
        self.assertIn(rc, (0, None))
        lines = [ln for ln in out.splitlines() if '2026-06-27' in ln]
        self.assertEqual(len(lines), 2)
        self.assertNotEqual(lines[0], lines[1])
        for ln in lines:  # prior columns still lead the line, in order
            self.assertRegex(ln, r'^  2026-06-27  Q3 2026  10-Q\s+USD  [\d,]+  start ')
            self.assertIn('filed 2026-07-31', ln)
            self.assertIn('0000320193-26-000020', ln)
        self.assertTrue(any('start 2025-09-28' in ln and '101,464,000,000' in ln for ln in lines))
        self.assertTrue(any('start 2026-03-29' in ln and '29,789,000,000' in ln for ln in lines))

    def test_xbrl_concept_rows_keep_start_accn_frame(self):
        probe = json.loads(CATO_PROBE.read_text())['producer_excerpt']
        with patch.object(edgar, '_get', return_value=json.dumps(probe).encode()):
            ent, label, rows = edgar.xbrl_concept('320193', 'NetIncomeLoss')
        self.assertEqual(ent, 'Apple Inc.')
        for r in rows:
            self.assertTrue({'unit', 'end', 'val', 'fy', 'fp', 'form', 'filed', 'start', 'accn', 'frame'} <= set(r))
        self.assertEqual({r['start'] for r in rows}, {'2025-09-28', '2026-03-29'})

    def test_facts_instant_row_marked(self):
        resp = {'entityName': 'X', 'label': 'Assets', 'units': {'USD': [
            {'end': '2026-06-30', 'val': 5, 'fy': 2026, 'fp': 'Q2', 'form': '10-Q', 'filed': '2026-07-30', 'accn': '0000000001-26-000001'}]}}
        rc, out, _ = run_cli(['facts', '--cik', '1', '--concept', 'Assets'], get=lambda u, h: json.dumps(resp).encode())
        self.assertIn('start - (instant)', out)

    # A2 — reproduces CATO's packet; A5 — limits verbatim
    def test_reproduces_cato_packet_and_limits_verbatim(self):
        cato = json.loads(CATO_PACKET.read_text())
        packet = build(self.raw, cik='0000320193', concept='NetIncomeLoss', unit='USD',
                       prior=['2025-03-30', '2025-06-28'], current=['2026-03-29', '2026-06-27'],
                       as_of='2026-10-24', retrieved_at='2026-10-24T21:43:10.239847+00:00')
        for k in cato:
            if k != 'limits':
                self.assertEqual(packet[k], cato[k], k)
        self.assertEqual(packet['response_sha256'],
                         '9b6ac23b024662c95dc7b4088a448bf60a31ff672e2f328161c5ceda6a8b9915')
        self.assertEqual(packet['limits'][:4], cato['limits'])
        self.assertEqual(packet['limits'], LIMITS_2D)
        self.assertEqual(set(packet) - set(cato), {'retrieval_basis', 'notes'})

    # A3 — Markdown rendered from the JSON record only
    def test_markdown_rendered_from_record(self):
        packet = build(self.raw, cik='0000320193', concept='NetIncomeLoss', unit='USD',
                       prior=['2025-03-30', '2025-06-28'], current=['2026-03-29', '2026-06-27'],
                       as_of='2026-10-24', retrieved_at='2026-10-24T21:43:10.239847+00:00')
        md = markdown(packet)
        for limit in LIMITS_2D:
            self.assertIn(f'- {limit}', md)
        packet['current']['val'] = 1
        self.assertIn('| 1 USD |', markdown(packet))
        self.assertNotEqual(md, markdown(packet))

    # A4 — CLI-level explicit failures, exit 2, cause named, no proxy value
    def test_cli_failures_name_cause(self):
        snap = ['--snapshot', str(RESPONSE)]
        cases = [
            (['compare', *CLI, *snap], '--snapshot requires --retrieved-at'),
            (['compare', *CLI, '--retrieved-at', '2026-10-24T21:43:10+00:00'], 'only for saved snapshots'),
            (['compare', *CLI[:1], 'abc', *CLI[2:], *snap, '--retrieved-at', '2026-10-24T21:43:10+00:00'], 'CIK must be'),
            (['compare', *CLI[:3], 'Net-Income', *CLI[4:], *snap, '--retrieved-at', '2026-10-24T21:43:10+00:00'], 'Invalid US-GAAP concept'),
            (['compare', *CLI[:-1], '2026-10-25', *snap, '--retrieved-at', '2026-10-24T21:43:10+00:00'], 'cutoff cannot be later'),
        ]
        for argv, cause in cases:
            with self.subTest(cause=cause):
                rc, out, err = run_cli(argv, get=lambda *a: self.fail('no fetch expected'), save_root=self.root)
                self.assertEqual(rc, 2)
                self.assertIn('Comparison unavailable', err)
                self.assertIn(cause, err)
                self.assertEqual(out, '')
        self.assertEqual(list(self.root.iterdir()), [])

    def test_instant_fact_named_as_cause(self):
        data = json.loads(self.raw)
        data['units']['USD'].append({'end': '2026-06-27', 'val': 7, 'accn': '0000320193-26-000020',
                                     'form': '10-Q', 'filed': '2026-07-31'})
        data['units']['USD'] = [v for v in data['units']['USD'] if v.get('start') != '2026-03-29']
        with self.assertRaisesRegex(ValueError, 'Missing period.*instant'):
            build(json.dumps(data).encode(), cik='320193', concept='NetIncomeLoss', unit='USD',
                  prior=['2025-03-30', '2025-06-28'], current=['2026-03-29', '2026-06-27'],
                  as_of='2026-10-24', retrieved_at='2026-10-24T21:43:10+00:00')

    # A6 — save: raw bytes hash to the record, JSON + MD beside it, path printed
    def test_save_writes_raw_json_md_and_prints_paths(self):
        rc, out, err = run_cli(['compare', *CLI, '--snapshot', str(RESPONSE),
                                '--retrieved-at', '2026-10-24T21:43:10.239847+00:00', '--save'],
                               save_root=self.root)
        self.assertEqual(rc, 0)
        packet = json.loads(out)
        folder = self.root / '2026-10-24_0000320193_NetIncomeLoss_USD'
        raw_path = folder / 'sec-response_9b6ac23b0246.json'
        self.assertEqual(hashlib.sha256(raw_path.read_bytes()).hexdigest(), packet['response_sha256'])
        self.assertEqual(raw_path.read_bytes(), self.raw)
        js = sorted(folder.glob('2025-03-30_*.json'))
        mds = sorted(folder.glob('2025-03-30_*.md'))
        self.assertEqual(len(js), 1)
        self.assertEqual(len(mds), 1)
        self.assertEqual(json.loads(js[0].read_text()), packet)
        self.assertEqual(mds[0].read_text(), markdown(packet))
        for p in (raw_path, js[0], mds[0]):
            self.assertIn(f'SAVED [written]: {p}', err)

    def test_save_never_overwrites(self):
        argv = ['compare', *CLI, '--snapshot', str(RESPONSE), '--save']
        run_cli([*argv, '--retrieved-at', '2026-10-24T21:43:10+00:00'], save_root=self.root)
        rc, _, err = run_cli([*argv, '--retrieved-at', '2026-10-24T22:00:00+00:00'], save_root=self.root)
        self.assertEqual(rc, 0)
        self.assertIn('already saved, identical', err)          # raw: content-addressed
        self.assertIn('earlier record KEPT', err)               # JSON differs by retrieved_at
        saved = json.loads(next(self.root.rglob('2025-03-30_*.json')).read_text())
        self.assertEqual(saved['retrieved_at'], '2026-10-24T21:43:10+00:00')

    def test_save_folder_uses_eastern_date(self):
        # 2026-10-25 01:00 UTC is 2026-10-24 21:00 EDT
        run_cli(['compare', *CLI, '--snapshot', str(RESPONSE), '--save',
                 '--retrieved-at', '2026-10-25T01:00:00+00:00'], save_root=self.root)
        self.assertTrue((self.root / '2026-10-24_0000320193_NetIncomeLoss_USD').is_dir())

    # A7 — retrieval basis recorded
    def test_retrieval_basis_snapshot_vs_live(self):
        rc, out, _ = run_cli(['compare', *CLI, '--snapshot', str(RESPONSE),
                              '--retrieved-at', '2026-10-24T21:43:10+00:00'])
        snap = json.loads(out)
        self.assertEqual(snap['retrieval_basis'], 'operator-snapshot')
        self.assertIn('not independently verified', snap['notes'][0])
        rc, out, _ = run_cli(['compare', *CLI], get=lambda url, h: self.raw)
        live = json.loads(out)
        self.assertEqual(live['retrieval_basis'], 'live-fetch')
        self.assertRegex(live['retrieved_at'], r'\+00:00$')

    # A8 — transport unchanged: CONCEPT URL, HJSON headers (declared-contact UA)
    def test_live_fetch_uses_existing_transport(self):
        seen = []
        rc, _, _ = run_cli(['compare', *CLI], get=lambda url, h: seen.append((url, h)) or self.raw)
        self.assertEqual(rc, 0)
        self.assertEqual(seen, [(edgar.CONCEPT.format(cik='0000320193', concept='NetIncomeLoss'), edgar.HJSON)])
        self.assertIn('williepowen@gmail.com', edgar.HJSON['User-Agent'])

    # Neighbour: overlap — two units for the same window
    def test_two_units_select_only_requested(self):
        data = json.loads(self.raw)
        shares = [dict(v, val=v['val'] // 1000) for v in data['units']['USD']
                  if v.get('start') in ('2025-03-30', '2026-03-29')]
        data['units']['shares'] = shares
        raw = json.dumps(data).encode()
        kw = dict(cik='320193', concept='NetIncomeLoss', prior=['2025-03-30', '2025-06-28'],
                  current=['2026-03-29', '2026-06-27'], as_of='2026-10-24',
                  retrieved_at='2026-10-24T21:43:10+00:00')
        usd = build(raw, unit='USD', **kw)
        sh = build(raw, unit='shares', **kw)
        self.assertEqual(usd['current']['val'], 29789000000)
        self.assertEqual(sh['current']['val'], 29789000)
        self.assertEqual(sh['current']['unit'], 'shares')
        with self.assertRaisesRegex(ValueError, 'Missing period.*units present: USD, shares'):
            build(raw, unit='EUR', **kw)

    def test_two_period_pairs_share_folder_distinct_files(self):
        base = ['compare', '--cik', '0000320193', '--concept', 'NetIncomeLoss', '--unit', 'USD',
                '--as-of', '2026-10-24', '--snapshot', str(RESPONSE),
                '--retrieved-at', '2026-10-24T21:43:10+00:00', '--save']
        run_cli([*base, '--prior', '2025-03-30', '2025-06-28', '--current', '2026-03-29', '2026-06-27'], save_root=self.root)
        rc, _, _ = run_cli([*base, '--prior', '2024-09-29', '2025-06-28', '--current', '2025-09-28', '2026-06-27'], save_root=self.root)
        self.assertEqual(rc, 0)
        folder = self.root / '2026-10-24_0000320193_NetIncomeLoss_USD'
        self.assertEqual(len(list(folder.glob('*.json'))), 3)   # one raw + two records
        self.assertEqual(len(list(folder.glob('*.md'))), 2)

    # Neighbours: wrong owner (404, unused tag) and missing information (403 / DNS)
    def test_transport_failures_are_explicit_and_save_nothing(self):
        for exc in (edgar.EdgarError('HTTP 404 for x\n  not found — verify the CIK/accession/concept exists'),
                    edgar.EdgarError('HTTP 403 for x'),
                    edgar.EdgarError('transport error for x: gaierror: [Errno -2] Name or service not known')):
            def boom(url, h, exc=exc):
                raise exc
            with self.subTest(exc=str(exc)[:20]):
                rc, out, err = run_cli(['compare', *CLI, '--save'], get=boom, save_root=self.root)
                self.assertEqual(rc, 2)
                self.assertEqual(out, '')
                self.assertIn('Comparison unavailable: ' + str(exc).split('\n')[0], err)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_failed_selection_saves_nothing(self):
        rc, out, err = run_cli(['compare', *CLI[:5], 'EUR', *CLI[6:], '--snapshot', str(RESPONSE),
                                '--retrieved-at', '2026-10-24T21:43:10+00:00', '--save'], save_root=self.root)
        self.assertEqual(rc, 2)
        self.assertIn('Missing period', err)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_save_refuses_raw_that_does_not_hash_to_record(self):
        packet = build(self.raw, cik='320193', concept='NetIncomeLoss', unit='USD',
                       prior=['2025-03-30', '2025-06-28'], current=['2026-03-29', '2026-06-27'],
                       as_of='2026-10-24', retrieved_at='2026-10-24T21:43:10+00:00')
        with self.assertRaisesRegex(ValueError, 'does not hash'):
            edgar.compare_save(self.raw + b' ', packet, markdown(packet), self.root)
        self.assertEqual(list(self.root.iterdir()), [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
