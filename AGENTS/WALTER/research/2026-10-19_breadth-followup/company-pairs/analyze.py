from pathlib import Path
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
import json,csv,statistics
D=Path(__file__).resolve().parent;NY=ZoneInfo('America/New_York');end='2026-10-16'
fund=json.loads((D/'exposures.json').read_text());assert all(x.get('filed',x.get('earnings_release','9999'))<'2026-09-18' for x in fund['companies'].values())
prices={};raw={};events={}
for s in list(fund['companies'])+['SPY']:
    z=json.loads((D/'raw'/(s+'.json')).read_text())['chart']['result'][0]
    assert z['meta']['dataGranularity']=='1d'
    ds=[datetime.fromtimestamp(t,NY).date().isoformat() for t in z['timestamp']]
    prices[s]={d:v for d,v in zip(ds,z['indicators']['adjclose'][0]['adjclose']) if v is not None and d<=end}
    raw[s]={d:v for d,v in zip(ds,z['indicators']['quote'][0]['close']) if v is not None and d<=end}
    events[s]=z.get('events',{})
sessions=sorted(prices['SPY']);assert sessions[-1]==end
rows=[]
for s,f in fund['companies'].items():
    r={'symbol':s,'financial_date':f['balance_date'],'rankable_refinancing':f['rankable_refinancing']}
    for n in [5,20,60]:
        start=sessions[-1-n];required=sessions[-1-n:]
        assert all(d in prices[s] for d in required),(s,n)
        r[f'{n}d_start']=start;r[f'{n}d_adj_return_pct']=100*(prices[s][end]/prices[s][start]-1)
        r[f'{n}d_raw_return_pct']=100*(raw[s][end]/raw[s][start]-1)
        if n==20 and f.get('shares'):
            r['rough_pre_window_size_billion']=f['shares']*raw[s][start]/1e9
    if f.get('interest_gross'):
        r['ytd_operating_income_over_recognized_interest']=f['operating_income_ytd']/f['interest_gross']
    rows.append(r)
lookup={r['symbol']:r for r in rows};pairs=[]
for a,b in [('DG','DLTR'),('HD','LOW'),('VZ','T'),('DUK','SO')]:
    r={'a':a,'b':b,'refinancing_exposure_order':'NOT_ESTABLISHED'}
    for n in [5,20,60]:r[f'{n}d_a_minus_b_pp']=lookup[a][f'{n}d_adj_return_pct']-lookup[b][f'{n}d_adj_return_pct']
    if all('rough_pre_window_size_billion' in lookup[s] for s in [a,b]):
        v=[lookup[s]['rough_pre_window_size_billion'] for s in [a,b]];r['rough_pre_window_size_ratio']=max(v)/min(v)
    pairs.append(r)
out={'asof':datetime.now(timezone.utc).isoformat(),'end':end,'rows':rows,'pairs':pairs,'events':events,
     'valid_pairs_for_maturity_exposure_hypothesis':0,
     'limits':['Four judgment-selected industry pairs, no market-wide representation or statistical causal estimate.',
               'Size estimates use pre-window known cover-page shares; intervening buybacks/issuance not fully reconciled.',
               'Comparable refinancing exposure not established, so no higher-risk-minus-lower-risk performance score.',
               'Adjusted-return vendor calculations, not official index returns; dividends/raw prices compared separately.']}
(D/'analysis.json').write_text(json.dumps(out,indent=2)+'\n')
with (D/'returns.csv').open('w') as f:
    fields=sorted(set().union(*(x.keys() for x in rows)));w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
print('RETURNS',[(r['symbol'],round(r['20d_adj_return_pct'],3),round(r['20d_raw_return_pct'],3),r.get('rough_pre_window_size_billion'),r.get('ytd_operating_income_over_recognized_interest')) for r in rows])
print('PAIRS',pairs)
