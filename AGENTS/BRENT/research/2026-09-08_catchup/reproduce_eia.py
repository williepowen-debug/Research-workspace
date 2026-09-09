"""Reproduce the bounded BRT-29 evidence table from saved EIA workbooks.
Research calculation only; no prediction grading, network, registry or trade writes.
"""
from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parent
series = {}
for label, name in [('gas', 'gas-supplied.xls'), ('jet', 'jet-supplied.xls')]:
    df = pd.read_excel(ROOT / name, sheet_name='Data 1', header=2)
    assert len(df.columns) == 2, df.columns
    df.columns = ['date', 'value']
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').set_index('date')
    assert df.index.is_unique
    df['mean4'] = df.value.rolling(4).mean()
    # Explicit comparable-week join: same weekday, 364 days earlier.
    prior = df[['mean4']].rename(columns={'mean4': 'prior4'})
    prior.index = prior.index + pd.Timedelta(days=364)
    df = df.join(prior)
    df['yoy_pct'] = (df.mean4 / df.prior4 - 1) * 100
    for end in pd.date_range('2026-07-10', '2026-08-28', freq='W-FRI'):
        for anchor in [end, end - pd.Timedelta(days=364)]:
            expected = pd.date_range(anchor - pd.Timedelta(days=21), anchor, freq='W-FRI')
            values = df.reindex(expected).value
            assert values.notna().all(), (label, anchor, values)
            assert abs(values.mean() - df.loc[anchor, 'mean4']) < 1e-9
    series[label] = df[['mean4', 'prior4', 'yoy_pct']].add_prefix(label + '_')
comparison = series['gas'].join(series['jet'], how='inner').loc['2026-07-10':'2026-08-28'].copy()
assert len(comparison) == 8
assert comparison.notna().all().all()
comparison['jet_below_gas'] = comparison.jet_yoy_pct < comparison.gas_yoy_pct
comparison.to_csv(ROOT / 'brt29-eia-comparison.csv', float_format='%.5f', date_format='%Y-%m-%d')
postreg = comparison.loc['2026-07-24':]
clean = comparison.loc['2026-08-14':]
assert len(postreg) == 6 and int(postreg.jet_below_gas.sum()) == 2
assert len(clean) == 3 and int(clean.jet_below_gas.sum()) == 2
assert not bool(comparison.iloc[-1].jet_below_gas)
assert round(comparison.iloc[-1].gas_yoy_pct, 1) == -1.6  # Existing September 2 WPSR table.
result = {'gas_source': 'https://www.eia.gov/dnav/pet/hist_xls/WGFUPUS2w.xls',
          'jet_source': 'https://www.eia.gov/dnav/pet/hist_xls/WKJUPUS2w.xls',
          'retrieval_local_date': '2026-09-08', 'last_observation': '2026-08-28',
          'prior_comparison': '364 days earlier; four contiguous Friday observations on each leg',
          'post_registration_weeks': len(postreg), 'jet_below_gas_weeks': int(postreg.jet_below_gas.sum()),
          'mid_august_weeks': len(clean), 'mid_august_jet_below_gas_weeks': int(clean.jet_below_gas.sum()),
          'final_week_jet_below_gas': bool(comparison.iloc[-1].jet_below_gas),
          'scope': 'Retrospective as-retrieved history; not an as-published vintage or final prediction grade.'}
(ROOT / 'eia-validation.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
