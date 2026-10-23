"""Render REPORT.md from ./data (TERRY 2026-10-23). Every figure comes from the CSVs; prose is fixed text.
Run: python3 -I make_report_md.py   (from this folder)"""
import csv, os

H = os.path.dirname(os.path.abspath(__file__))
def rows(name): return list(csv.DictReader(open(os.path.join(H, 'data', name))))
def f1(x): return f"{float(x):+.1f}%" if x not in ('', None) else '—'
def f2(x): return f"{float(x):+.2f}%" if x not in ('', None) else '—'
def ordn(n):
    n = int(round(float(n))); return f"{n}{'th' if 11 <= n % 100 <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"
def table(head, body): return '\n'.join(['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)] + ['| ' + ' | '.join(r) + ' |' for r in body])

daily = rows('kre_qqq_daily.csv')
a = next(r for r in daily if r['date'] == '2026-10-06'); z = daily[-1]
kre = (float(z['kre']) / float(a['kre']) - 1) * 100; qqq = (float(z['qqq']) / float(a['qqq']) - 1) * 100
cs = sorted(float(r['corr20']) for r in daily); c = float(z['corr20'])
below = sum(1 for r in daily if float(r['corr20']) > c) / len(daily) * 100
yr = {r['year']: r for r in rows('yearly_corr.csv')}
ep = rows('divergence_episodes_v2.csv'); bd = rows('big_days.csv'); sb = {r['id']: r for r in rows('strategy_backtest.csv')}
ts = {r['id']: r for r in rows('timing_signals.csv')}; sc = rows('start_conditions.csv'); book = rows('book_snapshot.csv'); ideas = rows('trade_ideas.csv')
now = sc[-1]

out = [f"# KRE vs QQQ — divergence report (TERRY, data through {z['date']})",
"",
"Live pages: report https://claude.ai/artifact/GEqqMLyMMJieo4t2NpeJQq · map https://claude.ai/artifact/8JAPSUTSqPQL4nEGtSPc6h. Ideas only; nothing approved or placed. Strategy and timing results are MODEL prices (Black-Scholes from VIX/VXN), not fills.",
"",
"## Key findings",
f"1. **Rare divergence.** Since QQQ's Oct 6 peak close, KRE {kre:+.1f}% vs QQQ {qqq:+.1f}% (gap {kre-qqq:+.1f} pts). 20-day correlation {c:+.2f}, lower than {below:.1f}% of readings since 2024; 2026 YTD yearly correlation {float(yr['2026']['corr']):+.2f}, lowest since 2006.",
f"2. **One-sided see-saw.** On QQQ ≥1% down days since late September KRE averaged {f2(bd[0]['kre_avg_on_down'])}; Jan 2025–Jun 2026 it averaged {f2(bd[2]['kre_avg_on_down'])} on those days.",
"3. **Divergences trend, not oscillate.** See the episode table: weeks-long one-way moves with small pullbacks, then mostly flat; July 2024 ended in a joint fall.",
f"4. **Rebalancing (\"sell, buy\") lost to holding in the trend.** From Oct 6: rebalance {f1(sb['2026-10-06 rebalance']['pnl_base'])} vs hold {f1(sb['2026-10-06 hold']['pnl_base'])}. From Aug 24: harvest-and-park {f1(sb['2026-08-24 harvest']['pnl_base'])} vs hold {f1(sb['2026-08-24 hold']['pnl_base'])}.",
f"5. **Timing beats strategy.** KRE puts bought cheap-and-stretched-up averaged {f1(ts['KRE: Cheap AND stretched up']['mean_pct'])}; expensive-and-stretched-down {f1(ts['KRE: Expensive AND stretched down']['mean_pct'])}.",
f"6. **Now is a watch window.** VXN {ordn(now['vxn_pctile'])} percentile with QQQ {f2(now['qqq_vs_ma20_pct'])} vs 20-day avg; VIX {ordn(now['vix_pctile'])} percentile.",
f"7. **Book offsets during the see-saw.** {book[0]['contracts']} bank/credit put contracts vs {book[1]['contracts']} QQQ put (mirror {book[0]['mirror_asof']}). Nothing pays if both rally.",
"",
"## Past divergence episodes",
table(['Episode', 'From', 'To', 'KRE', 'QQQ', 'KRE÷QQQ', 'Biggest pullback', 'Sessions', 'Next 20', '10y start', '10y end'],
      [[r['episode'], r['start'], r['end'], f1(r['kre_pct']), f1(r['qqq_pct']), f1(r['ratio_net_pct']), f1(r['max_counter_pct']), (str(int(float(r['sessions']))) if r['sessions'] else '—'), f1(r['ratio_next20_pct']), r['ten_year_start'] + '%', r['ten_year_end'] + '%'] for r in ep]),
"",
"## KRE on QQQ's big days",
table(['Window', 'QQQ ≤−1% days', 'KRE avg', 'KRE rose', 'QQQ ≥+1% days', 'KRE avg', 'KRE fell'],
      [[r['window'], r['qqq_down_days'], f2(r['kre_avg_on_down']), r['kre_up_share'] + '%', r['qqq_up_days'], f2(r['kre_avg_on_up']), r['kre_down_share'] + '%'] for r in bd]),
"",
"## Strategy model test ($1,000; base / cheaper / pricier option assumptions)",
table(['Start', 'Strategy', 'KRE px', 'QQQ px', 'Base', 'Cheaper', 'Pricier', 'Trades', 'Costs'],
      [[r['start'], r['strategy'], f1(r['kre_px_pct']), f1(r['qqq_px_pct']), f1(r['pnl_base']), f1(r['pnl_low']), f1(r['pnl_high']), r['trades'], '$' + r['friction_usd']] for r in sb.values()]),
"",
"## Conditions at each start date",
table(['Moment', 'VXN', 'VXN pct', 'QQQ vs 20d', 'VIX', 'VIX pct', 'KRE vs 20d', 'Hold result'],
      [[r['moment'], r['vxn'], r['vxn_pctile'], f2(r['qqq_vs_ma20_pct']), r['vix'], r['vix_pctile'], f2(r['kre_vs_ma20_pct']), f1(r['hold_pnl_base'])] for r in sc]),
"",
"## Timing signals (put bought, sold 20 sessions later; Jan 2024 – Sep 2026)",
table(['Leg', 'Condition', 'Days', '≈Episodes', 'Average', 'Median', 'Made money'],
      [[r['leg'], r['condition'], r['n_days'], r['approx_episodes'], f1(r['mean_pct']), f1(r['median_pct']), r['win_pct'] + '%'] for r in ts.values()]),
"",
"**Checklist for any new put:** volatility index in the bottom quarter of its last six months · stock ≥2% above its 20-day average · green day for that stock (root rule #6) · a dated event before expiry · never after a drop with fear high.",
"",
"## Trade ideas on file",
table(['Idea', 'Structure', 'Max loss', 'Max gain', 'Breakeven', 'Level', 'Trigger', 'Status', 'Quoted'],
      [[r['idea'], r['structure'], '$' + r['max_loss_usd'], ('$' + r['max_gain_usd']) if r['max_gain_usd'] else '— (single put)', '$' + r['breakeven'], r['level_needed'], r['trigger'], r['status'], r['quote_time']] for r in ideas]),
"",
"**Rotation rules (if used):** KRE and QQQ only · ≥45 days out · recycle, never add · sell half a leg at +50% on its red day · park cash; redeploy to the other leg after KRE÷QQQ turns 3% from its extreme, on that leg's green day · ≤1 swap/week and only after a 3% line move · no recycling into a leg down 50% · stop rotating and hold both on the first joint ≥1% down day or 20-day correlation > +0.3.",
"",
"## Caveats",
"Model prices, not fills (VIX/VXN-scaled Black-Scholes, no skew). Five hand-picked episodes; overlapping test days (≈ days/20 independent cases). 2024–2026 mostly a rising market. Drivers are hypotheses (HENRY structure, NEXUS synthesis). yfinance closes, not exchange-official. Positions from the 10/22 11:01 ET Fidelity reconcile; Robinhood unverified. Fidelity options Level 2 (Will, 10/23); spread approval unverified.",
]
open(os.path.join(H, 'REPORT.md'), 'w').write('\n'.join(out) + '\n')
print('wrote REPORT.md', sum(len(x) for x in out), 'chars')
