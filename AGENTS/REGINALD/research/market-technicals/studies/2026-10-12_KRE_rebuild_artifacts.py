from pathlib import Path
import json
import hashlib
import datetime as dt
import csv
import sys
import argparse
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser(description='Rebuild the dated KRE study artifacts from saved sources; no network requests.')
parser.add_argument('--plot-deps', type=Path, help='Optional temporary directory containing plotting dependencies')
args = parser.parse_args()
ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'domain/sources/2026-10-12_KRE_basket_study'
HUB = ROOT / 'research/market-technicals'
STUDIES = HUB / 'studies'
BASKET = pd.read_csv(SOURCE / 'basket-metrics.csv')
BENCH = pd.read_csv(SOURCE / 'benchmark-metrics.csv')
HISTORY = pd.read_csv(SOURCE / 'daily-history.csv.gz')
HOLDINGS = pd.read_csv(HUB / 'snapshots/2026-10-12/kre-holdings.csv')
FRED = pd.read_csv(SOURCE / 'dgs10.csv').set_index('observation_date')
RECEIPT = json.loads((SOURCE / 'fetch-receipt.json').read_text())
checks = {}
assert len(BASKET) == 167 and BASKET.symbol.nunique() == 167
assert BASKET.three_month_covered.all() and BASKET.four_week_covered.all()
assert (BASKET.last_available_date == '2026-10-09').all()
assert HISTORY.date.max() == '2026-10-09'
assert not HISTORY.duplicated(['symbol', 'date']).any()
assert all(r['identity']['symbol'] == r['symbol'] for r in RECEIPT['requests'])
assert hashlib.sha256((SOURCE / 'daily-history.csv.gz').read_bytes()).hexdigest() == RECEIPT['daily_history_sha256']
for first in ['2026-07-10', '2026-09-11']:
    assert HISTORY[HISTORY.date == first].symbol.nunique() == 175
checks['coverage'] = {'banks': 167, 'bank_published_weight_pct': float(BASKET.oct9_weight_pct.sum()),
                      'histories': 175, 'bars': len(HISTORY), 'missing_window_endpoints': 0,
                      'all_response_symbols_match': True,
                      'CBC_first_bar': HISTORY[HISTORY.symbol == 'CBC'].date.min(),
                      'shorter_CBC_history_covers_all_windows_and_moving_averages': True}
old = json.loads((ROOT / 'domain/sources/2026-10-12_KRE_top10_performance/performance.json').read_text())
diffs = []
for r in old:
    x = (BENCH if r['symbol'] == 'KRE' else BASKET).set_index('symbol').loc[r['symbol']]
    diffs.extend([abs(x.three_month_price_pct - r['three_month_price_pct']),
                  abs(x.four_week_price_pct - r['four_week_price_pct'])])
checks['previous_saved_top10_return_max_difference_pp'] = max(diffs)
assert max(diffs) < 1e-8
for label, start in [('three_month', '2026-07-10'), ('four_week', '2026-09-11')]:
    for r in BASKET.itertuples():
        x = HISTORY[HISTORY.symbol == r.symbol].set_index('date')
        assert abs(getattr(r, f'{label}_price_pct') - 100 * (x.loc['2026-10-09', 'Close'] / x.loc[start, 'Close'] - 1)) < 1e-8
    checks[f'{label}_adjusted_declining_banks'] = int((BASKET[f'{label}_adjusted_return_pct'] < 0).sum())
    checks[f'{label}_adjusted_declining_published_weight_pct'] = float(BASKET.loc[BASKET[f'{label}_adjusted_return_pct'] < 0, 'oct9_weight_pct'].sum())
checks['moving_average_rule'] = 'Arithmetic mean of last20/50 raw Close bars, all settled and endingOctober9'
checks['stock_splits'] = HISTORY.loc[HISTORY['Stock Splits'] != 0, ['symbol', 'date', 'Stock Splits']].to_dict('records')
checks['total_published_holdings_weight_pct'] = float(HOLDINGS.weight_pct.sum())
checks['cash_published_weight_pct'] = float(HOLDINGS.loc[HOLDINGS.ticker == '-', 'weight_pct'].sum())
checks['unallocated_published_weight_residual_pct'] = 100 - checks['total_published_holdings_weight_pct']
cross = pd.read_csv(SOURCE / 'issuer-weight-close-crosscheck.csv')
median_assets = float(cross.implied_nav_assets.median())
checks['issuer_weight_share_close_check'] = {
    'median_implied_common_denominator_usd': median_assets,
    'largest_deviation_from_common_denominator_pct': float((100 * (cross.implied_nav_assets / median_assets - 1)).abs().max()),
    'largest_deviation_from_published_rounded_NAV_AUM_pct': float(cross.difference_pct.abs().max()),
    'interpretation': 'Cross-sectional weights/shares/closes are consistent at a common denominator, but absolute implied denominator is about0.57% above published rounded NAV AUM. Gross/net/timing bridge unresolved; not an independent exact-close or NAV validation.'}
checks['historical_contribution'] = 'UNRESOLVED. June30 KRE NPORT verified, but July10/Sep11 weights, full membership bridge and September rebalance transactions not reconstructed. Current-weight scenarios are explicitly diagnostic only.'
(SOURCE / 'validation.json').write_text(json.dumps(checks, indent=2) + '\n')

for name, frame in [('2026-10-12_KRE_full_basket_metrics.csv', BASKET),
                    ('2026-10-12_KRE_benchmark_comparison.csv', BENCH[BENCH.symbol != '^TNX'])]:
    frame.to_csv(STUDIES / name, index=False)
close = HISTORY.pivot(index='date', columns='symbol', values='Close')
adj = HISTORY.pivot(index='date', columns='symbol', values='Adj Close')
bank_symbols = BASKET.symbol.tolist()
valid20 = close[bank_symbols].rolling(20, min_periods=20).mean()
valid50 = close[bank_symbols].rolling(50, min_periods=50).mean()
breadth = pd.DataFrame(index=close.index)
for n, ma in [(20, valid20), (50, valid50)]:
    valid = close[bank_symbols].notna() & ma.notna()
    below = (close[bank_symbols] < ma) & valid
    breadth[f'covered_sma{n}'] = valid.sum(axis=1)
    breadth[f'below_sma{n}_count'] = below.sum(axis=1)
    breadth[f'below_sma{n}_count_pct'] = 100 * below.sum(axis=1) / valid.sum(axis=1)
breadth = breadth.loc['2026-07-10':'2026-10-09']
breadth.to_csv(STUDIES / '2026-10-12_KRE_daily_breadth.csv', index_label='date')
diagnostic = BASKET.sort_values('four_week_current_weight_scenario_pp')[['symbol', 'name', 'oct9_weight_pct', 'four_week_price_pct', 'four_week_adjusted_return_pct', 'four_week_current_weight_scenario_pp', 'three_month_price_pct', 'three_month_current_weight_scenario_pp']].copy()
diagnostic['basis'] = 'October9 weights treated as fixed starting allocations; NOT historical fund contributions'
diagnostic.to_csv(STUDIES / '2026-10-12_KRE_weighted_decline_diagnostic.csv', index=False)
volume_symbols = ['KRE','FLG','BOH','RF','CFG','OZK','MTB','ZION','CCB','EGBN']
all_metrics = pd.concat([BASKET, BENCH], ignore_index=True).set_index('symbol')
volume = all_metrics.loc[volume_symbols, ['latest_volume', 'latest_volume_vs_prior20', 'last20_up_sessions', 'last20_down_sessions', 'last20_mean_down_vs_up_volume', 'last20_total_down_vs_up_volume']]
volume.to_csv(STUDIES / '2026-10-12_KRE_volume_comparison.csv', index_label='symbol')
rate_rows = []
for start in ['2026-07-10', '2026-09-11']:
    end = '2026-10-08'
    rate_rows.append({'start':start, 'end':end, 'DGS10_start_pct':FRED.loc[start,'DGS10'],
                      'DGS10_end_pct':FRED.loc[end,'DGS10'], 'DGS10_change_bp':100*(FRED.loc[end,'DGS10']-FRED.loc[start,'DGS10']),
                      'KRE_price_change_pct':100*(close.loc[end,'KRE']/close.loc[start,'KRE']-1),
                      'KRE_adjusted_return_pct':100*(adj.loc[end,'KRE']/adj.loc[start,'KRE']-1),
                      'source':'Federal Reserve H.15 DGS10 via FRED; latest availableOctober8; no forward fill toOctober9'})
pd.DataFrame(rate_rows).to_csv(STUDIES / '2026-10-12_KRE_rate_comparison.csv', index=False)
event_rows = []
for s in ['CCB','VLY']:
    for first,last in [('2026-07-10','2026-09-25'),('2026-09-25','2026-09-28'),('2026-09-28','2026-10-09')]:
        event_rows.append({'symbol':s,'start':first,'end':last,'price_change_pct':100*(close.loc[last,s]/close.loc[first,s]-1),
                           'context':'Existing KB188/189: VLY-Bluevine agreementSeptember27, issuer8-KSeptember28; association is not causal attribution'})
pd.DataFrame(event_rows).to_csv(STUDIES / '2026-10-12_KRE_BaaS_event_comparison.csv', index=False)

if args.plot_deps:
    sys.path.insert(0, str(args.plot_deps))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
plt.rcParams.update({'font.size':10, 'axes.spines.top':False, 'axes.spines.right':False,
                     'figure.facecolor':'white', 'axes.grid':True, 'grid.alpha':0.2})
fig, axes = plt.subplots(2,2, figsize=(14,10), constrained_layout=True)
period = adj.loc['2026-07-10':'2026-10-09']
for s,c in [('KRE','#b42318'),('KBE','#d97706'),('SPY','#15803d'),('IWM','#2563eb'),('XLF','#64748b')]:
    axes[0,0].plot(pd.to_datetime(period.index),100*period[s]/period[s].iloc[0], label=s, color=c, linewidth=2 if s=='KRE' else 1.3)
axes[0,0].set(title='Banks weakened while the broad market rose', ylabel='Dividend-adjusted index, July 10 = 100')
axes[0,0].legend(ncol=3, frameon=False)
for n,c in [(20,'#b42318'),(50,'#2563eb')]:
    axes[0,1].plot(pd.to_datetime(breadth.index),breadth[f'below_sma{n}_count_pct'],label=f'Below {n}-day average',color=c)
axes[0,1].set(title='Weakness reaches almost the entire current basket',ylabel='Percent of covered banks',ylim=(0,103))
axes[0,1].legend(frameon=False)
rates=FRED.dropna().loc['2026-07-10':'2026-10-08']
axes[1,0].plot(pd.to_datetime(rates.index),rates.DGS10,color='#7c3aed',linewidth=2)
axes[1,0].set(title='Long-term yields rose during the bank decline',ylabel='10-year constant-maturity yield, percent')
axes[1,0].text(.03,.95,'Federal Reserve DGS10 ends October 8\nNo October 9 observation carried forward',transform=axes[1,0].transAxes,va='top',fontsize=9)
worst=diagnostic.head(12).iloc[::-1]
axes[1,1].barh(worst.symbol,worst.four_week_current_weight_scenario_pp,color='#b42318')
axes[1,1].set(title='Largest weighted declines in a fixed-basket diagnostic',xlabel='Percentage-point effect; October 9 weights × adjusted returns\nSeptember 11–October 9; NOT actual historical fund attribution')
axes[1,1].grid(axis='x',alpha=.2)
for ax in [axes[0,0],axes[0,1],axes[1,0]]:
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
fig.suptitle('KRE whole-basket study — settled prices through October 9, 2026\n167 current bank holdings; source fetch October 12; historical membership limits apply',fontsize=15)
for ext in ['png','svg']:
    fig.savefig(STUDIES / f'2026-10-12_KRE_whole_basket_charts.{ext}',dpi=160)
print('Saved validated derived data and standalone PNG/SVG charts.')
print(json.dumps({'coverage':checks['coverage'],'rates':rate_rows,'weighted_worst':diagnostic.head(5).to_dict('records')},indent=2))
