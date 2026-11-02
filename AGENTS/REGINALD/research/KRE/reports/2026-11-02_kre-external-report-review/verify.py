"""Recheck descriptive claims; does not independently validate constituent prices."""
from pathlib import Path
import hashlib
import json
import pandas as pd

HERE = Path(__file__).resolve().parent
source = HERE / 'input_report.md'
lines = source.read_text().splitlines()
start = next(i for i, line in enumerate(lines) if '| name ' in line and 'CET1' in line and 'rally %' in line)
headers = [x.strip() for x in lines[start].strip('|').split('|')]
headers[0] = 'ticker'
rows = []
for line in lines[start + 2:]:
    if not line.startswith('|'):
        break
    rows.append([x.strip() for x in line.strip('|').split('|')])
table = pd.DataFrame(rows, columns=headers)
for col in ['wt %', '63d %', 'rally %', 'CET1']:
    table[col] = pd.to_numeric(table[col], errors='coerce')
prices = pd.read_csv(HERE.parent / '2026-11-02_kre-etf-relationships/aligned_adjusted_closes.csv', index_col='date', parse_dates=True)
returns = prices.pct_change(fill_method=None).dropna()
corr = returns.KRE.rolling(63).corr(returns.KBWB).dropna()
gap2 = (returns.KRE - returns.KBWB).tail(63).pow(2)
contribution = table['wt %'] * table['rally %'] / 100
result = {
    'input_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'constituents': len(table),
    'unique_tickers': table.ticker.nunique(),
    'weights_sum_pct': table['wt %'].sum(),
    'positive_63d_count': int((table['63d %'] > 0).sum()),
    'positive_rebound_count': int((table['rally %'] > 0).sum()),
    'median_rebound_pct': table['rally %'].median(),
    'top10_share_of_rounded_rebound_contributions_pct': contribution.nlargest(10).sum() / contribution.sum() * 100,
    'zero_CET1_tickers_needing_source_check': table.loc[table.CET1 == 0, 'ticker'].tolist(),
    'last_date': str(prices.index[-1].date()),
    'KRE_KBWB_63d_correlation': corr.iloc[-1],
    'rolling_window_count_our_baseline': len(corr),
    'correlation_percentile_our_baseline': (corr < corr.iloc[-1]).mean() * 100,
    'minimum_2026_correlation_date': str(corr.loc['2026'].idxmin().date()),
    'minimum_2026_correlation': corr.loc['2026'].min(),
    'top5_squared_daily_gap_share_pct': gap2.nlargest(5).sum() / gap2.sum() * 100,
    'top10_squared_daily_gap_share_pct': gap2.nlargest(10).sum() / gap2.sum() * 100,
    'limits': 'Appendix checks use published rounded figures, not independent stock histories. ETF calculations reuse our saved Yahoo data; independent calculation, same vendor. Historical baseline differs from supplied report.'
}
(HERE / 'verification.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
