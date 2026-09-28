"""CATO independent offline review cases; no owner edits or network calls.

Run from repository root with .venv/bin/python <this-file>.
FAIL means an unmet review expectation, not a fixture execution failure.
"""
import contextlib
import datetime as dt
import importlib.util
import io
from pathlib import Path
import sys
import tempfile
import types
from unittest.mock import patch

import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("bond_rates_review", ROOT / "AGENTS/BOND/monitors/rates_context.py")
rc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rc)
TODAY = dt.date(2026, 9, 28)
results = []


def record(name, expectation, result, output):
    ok = expectation(result, output)
    results.append(ok)
    print(f"{'PASS' if ok else 'FAIL'} | {name} | findings={result}")
    for line in output.splitlines():
        if any(x in line for x in ('anchor EFFR', 'TERMINAL', 'next FOMC', 'NO FUTURE', 'not fired', 'TRIGGER', 'GAP')):
            print(' ', line.strip())


def fed_case(name, *, old_strip=False, old_effr=False, thin=False, missing_contract=False, missing_meeting=False, empty_docket=False):
    dates = pd.date_range('2026-09-21', periods=6, freq='B')
    if old_strip:
        dates = pd.date_range('2026-08-03', periods=6, freq='B')
    data = {}
    for i, (month, ticker) in enumerate(rc.zq_tickers(TODAY, 6)):
        rate = {'2026-11': 4.05, '2026-12': 4.10}.get(month, 3.88 + i * .08)
        data[ticker] = [100 - rate] * 6
        if thin and i > 0:
            data[ticker][-1] = float('nan')
        if missing_contract and month == '2026-11':
            data[ticker] = [float('nan')] * 6
    if missing_contract:
        data['ZQH27.CBT'] = [95.5] * 6  # still six nonempty raw contracts
    fake_yf = types.SimpleNamespace(download=lambda *a, **k: {'Close': pd.DataFrame(data, index=dates)})
    effr_date = '2026-08-07' if old_effr else '2026-09-25'
    with tempfile.TemporaryDirectory(prefix='cato-bond-case-') as td:
        home = Path(td)
        (home / 'docket').mkdir()
        rows = ['Date\tEvent']
        if not empty_docket:
            if not missing_meeting:
                rows.append('2026-10-28\tOCTOBER FOMC DECISION')
            rows.append('2026-12-09\tDECEMBER FOMC DECISION')
        (home / 'docket/CATALYSTS.tsv').write_text('\n'.join(rows))
        buf = io.StringIO()
        with patch.dict(sys.modules, {'yfinance': fake_yf}), patch.object(rc, 'BOND', home), \
             patch.object(rc, '_fred', return_value=[(effr_date, 3.88)]), \
             patch.object(rc, '_now_et', return_value=dt.datetime(2026, 9, 28, 17, 30)), \
             contextlib.redirect_stdout(buf):
            finding = rc.policy_path(TODAY)
    bad_input = any((old_strip, old_effr, thin, missing_contract, missing_meeting, empty_docket))
    expected = (lambda n, out: n > 0) if bad_input else (lambda n, out: n == 0 and '68%' in out)
    record(name, expected, finding, buf.getvalue())


def mortgage_case(name, mort, ust, expect_gap=False, expect_fire=False):
    buf = io.StringIO()
    with patch.object(rc, '_fred', side_effect=lambda sid, lim: mort if sid == 'MORTGAGE30US' else ust), contextlib.redirect_stdout(buf):
        finding = rc.mbs_rearm(TODAY)
    expected = (lambda n, out: n > 0) if expect_gap or expect_fire else (lambda n, out: n == 0 and 'not fired' in out)
    record(name, expected, finding, buf.getvalue())


fed_case('healthy October reading')
fed_case('whole strip six weeks stale', old_strip=True)
fed_case('EFFR anchor six weeks stale', old_effr=True)
fed_case('six raw contracts but only one current', thin=True)
fed_case('needed November contract absent', missing_contract=True)
fed_case('October missing but December remains', missing_meeting=True)
fed_case('no future meeting', empty_docket=True)
mortgage_case('healthy 185bp spread', [('2026-09-24', 7.03)], [('2026-09-24', 5.18)])
mortgage_case('231bp triggers review', [('2026-09-24', 7.31)], [('2026-09-24', 5.0)], expect_fire=True)
mortgage_case('six-week-old mortgage still reports no fire', [('2026-08-13', 7.03)], [('2026-08-13', 5.18)], expect_gap=True)
mortgage_case('current mortgage paired with six-week-old Treasury', [('2026-09-24', 7.03)], [('2026-08-13', 5.18)], expect_gap=True)

label = rc.bar_timing_label(dt.datetime(2026, 9, 28, 11, 0))
record('11am must not assert current vendor bar is a prior-session close',
       lambda n, out: 'prior session' not in out, None, label)
print('  actual label:', label)
print(f'\nTOTAL: {sum(results)} met / {len(results) - sum(results)} unmet / {len(results)} expectations')
sys.exit(0 if all(results) else 1)
