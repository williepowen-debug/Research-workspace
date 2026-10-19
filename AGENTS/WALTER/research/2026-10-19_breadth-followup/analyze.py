"""Exploratory analysis; frozen definitions in PLAN.md. Stdlib only."""
from pathlib import Path
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import csv, json, statistics, hashlib

D = Path(__file__).resolve().parent
OLD = D.parent / '2026-10-19_breadth'
NY = ZoneInfo('America/New_York')
END = '2026-10-16'
prices, raw_prices = {}, {}
for f in sorted((D / 'raw').glob('chart-*.json')):
    z = json.loads(f.read_text())['chart']['result'][0]
    assert z['meta']['dataGranularity'] == '1d', f
    dates = [datetime.fromtimestamp(t, NY).date().isoformat() for t in z['timestamp']]
    assert len(dates) == len(set(dates)), f
    adj = z['indicators']['adjclose'][0]['adjclose']
    close = z['indicators']['quote'][0]['close']
    s = z['meta']['symbol']
    prices[s] = {d: v for d, v in zip(dates, adj) if v is not None and d <= END}
    raw_prices[s] = {d: v for d, v in zip(dates, close) if v is not None and d <= END}
    assert all(v > 0 for v in prices[s].values()), s
sessions = sorted(prices['SPY'])
assert sessions[-1] == END
credit = {}
for f in sorted((D / 'raw').glob('BAML*.csv')):
    rows = list(csv.DictReader(f.read_text().splitlines()))
    credit[f.stem] = {r['observation_date']: float(r[f.stem]) * 100 for r in rows
                      if r[f.stem] not in ['', '.'] and r['observation_date'] <= END}
assert all(credit.values()), 'Credit download incomplete'

recent = []
for n in [1, 5, 20, 60, 63]:
    start = sessions[-1-n]
    r = {'sessions': n, 'start': start, 'end': END, 'etf_adj_returns_pct': {}, 'oas_changes_bp': {}}
    for s, p in prices.items():
        if start in p and END in p:
            r['etf_adj_returns_pct'][s] = 100 * (p[END] / p[start] - 1)
    for s, p in credit.items():
        if start in p and END in p:
            r['oas_changes_bp'][s] = p[END] - p[start]
    r['rsp_spy_ratio_change_pct'] = 100 * ((prices['RSP'][END] / prices['RSP'][start]) /
                                           (prices['SPY'][END] / prices['SPY'][start]) - 1)
    recent.append(r)

snap = json.loads((OLD / 'constituent-snapshot.json').read_text())
daily = []
big_moves = []
for i in range(len(sessions)-60, len(sessions)):
    day, prev = sessions[i], sessions[i-1]
    rr = []
    for s, x in snap.items():
        p = x['bars']
        if day in p and prev in p and p[prev] > 0:
            ret = p[day] / p[prev] - 1
            rr.append(ret)
            if abs(ret) > .30:
                big_moves.append({'date': day, 'symbol': s, 'return_pct': ret*100})
    spy = prices['SPY'][day] / prices['SPY'][prev] - 1
    rsp = prices['RSP'][day] / prices['RSP'][prev] - 1
    daily.append({'date': day, 'prior_session': prev, 'coverage': len(rr),
                  'up': sum(v > 0 for v in rr), 'down': sum(v < 0 for v in rr),
                  'flat': sum(v == 0 for v in rr), 'mean_raw_return_pct': statistics.mean(rr)*100,
                  'median_raw_return_pct': statistics.median(rr)*100,
                  'spy_adj_return_pct': spy*100, 'rsp_adj_return_pct': rsp*100,
                  'index_up_majority_down': spy > 0 and sum(v < 0 for v in rr) > len(rr)/2})
ma = {}
for n in [50, 200]:
    ds = sessions[-n:]
    valid = [(s, x['bars']) for s, x in snap.items() if all(d in x['bars'] for d in ds)]
    above = sum(p[END] > statistics.mean(p[d] for d in ds) for s, p in valid)
    ma[str(n)] = {'covered': len(valid), 'above': above,
                  'percent': 100*above/len(valid) if valid else None}
window_breadth = []
for n in [5,20,60]:
    ds = sessions[-1-n:]
    stable = [(s, x['bars']) for s, x in snap.items() if all(d in x['bars'] for d in ds)]
    out = {'sessions': n, 'stable_cohort': len(stable), 'start': ds[0], 'end': ds[-1]}
    rr = [p[ds[-1]]/p[ds[0]]-1 for s,p in stable]
    out.update(up=sum(v>0 for v in rr),down=sum(v<0 for v in rr),
               median_raw_return_pct=100*statistics.median(rr))
    window_breadth.append(out)

def outcome(i, h):
    ds = sessions[i:i+h+1]
    v = [prices['SPY'][d] for d in ds]
    assert len(v) == h+1
    peak, dd = v[0], 0
    for x in v:
        peak = max(peak, x)
        dd = min(dd, x/peak-1)
    return {'return_pct': 100*(v[-1]/v[0]-1),
            'min_return_from_entry_pct': 100*(min(v)/v[0]-1),
            'max_closing_drawdown_pct': 100*dd}

def summarize(events):
    out = {'n': len(events), 'dates': [e['date'] for e in events], 'horizons': {}}
    for h in [21,63,126]:
        v = [e['outcomes'][str(h)] for e in events]
        if v:
            out['horizons'][str(h)] = {'n': len(v), 'mean_return_pct': statistics.mean(x['return_pct'] for x in v),
                'median_return_pct': statistics.median(x['return_pct'] for x in v),
                'positive_count': sum(x['return_pct']>0 for x in v),
                'closing_drawdown_ge10pct_count': sum(x['max_closing_drawdown_pct']<=-10 for x in v),
                'worst_return_pct': min(x['return_pct'] for x in v),
                'worst_closing_drawdown_pct': min(x['max_closing_drawdown_pct'] for x in v)}
    return out

def study(formation, credit_only=False, floor=0):
    # Every arm has its own chronologically greedy spacing; dates across arms may overlap.
    conditions = ['unconditional','index_up','index_up_narrow','index_up_broad',
                  'index_up_narrow_credit_widen','index_up_narrow_credit_not_widen']
    arms = {s: [] for s in conditions}
    next_i = {s: 0 for s in conditions}
    candidates = {s: 0 for s in conditions}
    first = None
    hy = credit['BAMLH0A0HYM2']
    for i in range(formation, len(sessions)-126):
        day, start = sessions[i], sessions[i-formation]
        if not all(d in prices['RSP'] for d in sessions[i-formation:i+1]):
            continue
        credit_ok = day in hy and start in hy
        if credit_only and not credit_ok:
            continue
        if first is None:
            first = day
        cap = prices['SPY'][day]/prices['SPY'][start]-1
        rel = (prices['RSP'][day]/prices['RSP'][start])/(1+cap)-1
        delta = hy[day]-hy[start] if credit_ok else None
        tests = {'unconditional': True, 'index_up': cap>0, 'index_up_narrow':cap>0 and rel<0,
                 'index_up_broad': cap>0 and rel>=0,
                 'index_up_narrow_credit_widen':cap>0 and rel<0 and delta is not None and
                     (delta>0 if floor==0 else delta>=floor-1e-9),
                 'index_up_narrow_credit_not_widen':cap>0 and rel<0 and delta is not None and delta<=0}
        for key, ok in tests.items():
            if not ok:
                continue
            candidates[key] += 1
            if i < next_i[key]:
                continue
            arms[key].append({'date': day, 'formation_start':start, 'session_index':i,
                             'spy_formation_return_pct':100*cap, 'relative_ratio_pct':100*rel,
                             'hy_change_bp':delta, 'outcomes':{str(h):outcome(i,h) for h in [21,63,126]}})
            next_i[key] = i+126
    for events in arms.values():
        assert all(b['session_index']-a['session_index']>=126 for a,b in zip(events,events[1:]))
    return {'formation_sessions':formation, 'credit_matched_perimeter':credit_only,
            'credit_widening_floor_bp':floor, 'credit_operator':'positive' if floor==0 else 'at least', 'first_eligible': first,
            'last_mature': sessions[-127], 'candidate_dependent_days':candidates,
            'summary':{s:summarize(v) for s,v in arms.items()}, 'events':arms}

studies = {'full20':study(20), 'full60':study(60), 'credit20':study(20,True),
           'credit60':study(60,True), 'credit20_20bp':study(20,True,20)}
# Compare recovered same-vintage overlapping recent bars from both retrievals.
crosscheck = {}
for s in ['SPY','RSP','QQQ','QQEW','IWM']:
    z = json.loads((OLD/f'chart-{s}.json').read_text())['chart']['result'][0]
    p = {datetime.fromtimestamp(t,NY).date().isoformat():v for t,v in zip(z['timestamp'],z['indicators']['adjclose'][0]['adjclose']) if v is not None}
    common = sorted(set(p)&set(prices[s]))[-64:]
    crosscheck[s] = {'common':len(common), 'maximum_relative_difference':max(abs(p[d]/prices[s][d]-1) for d in common)}
limits = ['RSP/SPY is a size/style/sector-exposed ETF proxy, not historical constituent A/D.',
          'Stock breadth uses October16 current holdings and raw prices; survivorship, membership, corporate-action and coverage limits.',
          'OAS dates are retrospective observation dates, not verified availability timestamps; no executable backtest.',
          'All arms spaced126sessions internally, but arms share dates/outcomes; not independent experiment groups.',
          'Greedy spacing depends on first date; small counts and threshold sensitivity are material.',
          'No causal refinancing attribution or validated crash probability.']
result = {'as_of':datetime.now(timezone.utc).isoformat(), 'end':END,
          'prices_perimeter':{s:{'first':min(p),'last':max(p),'n':len(p)} for s,p in prices.items()},
          'credit_perimeter':{s:{'first':min(p),'last':max(p),'n':len(p)} for s,p in credit.items()},
          'recent':recent, 'breadth_daily':daily, 'breadth_windows':window_breadth,
          'moving_averages':ma, 'raw_stock_moves_over30pct':big_moves,
          'studies':studies, 'same_vendor_retrieval_crosscheck':crosscheck, 'limits':limits}
(D/'analysis.json').write_text(json.dumps(result,indent=2)+'\n')
with (D/'breadth-60sessions.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(daily[0]));w.writeheader();w.writerows(daily)
for s in ['full20','full60','credit20','credit60','credit20_20bp']:
    print(s)
    for arm,v in studies[s]['summary'].items():
        print(arm,v['n'],v['horizons'].get('63'),flush=True)
print('RECENT',json.dumps(recent))
print('BREADTH',window_breadth,'MA',ma,'BIG',big_moves)
print('DIVERGENT DAYS', [x['date'] for x in daily if x['index_up_majority_down']])
print('CROSSCHECK',crosscheck)
