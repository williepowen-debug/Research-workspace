from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json,csv,statistics
D=Path(__file__).resolve().parent;NY=ZoneInfo('America/New_York');data={};rows=[]
for p in sorted(D.glob('chart-*.json')):
 j=json.loads(p.read_text());z=j['chart']['result'][0];sym=z['meta']['symbol'];m=z['meta'];q=z['indicators']['quote'][0];adj=z['indicators'].get('adjclose',[{}])[0].get('adjclose');bars={}
 for i,ts in enumerate(z['timestamp']):
  day=datetime.fromtimestamp(ts,NY).date().isoformat();raw=q['close'][i];a=adj[i] if adj else None
  if raw is not None:bars[day]={'close':raw,'adjusted':a}
 data[sym]={'meta':m,'bars':bars};ds=sorted(d for d in bars if d<='2026-10-16');end='2026-10-16';row={'symbol':sym,'last_complete':end,'quote_time':datetime.fromtimestamp(m['regularMarketTime'],NY).isoformat(),'intraday_date':datetime.fromtimestamp(m['regularMarketTime'],NY).date().isoformat(),'intraday_price':m['regularMarketPrice'],'intraday_ret_pct':100*(m['regularMarketPrice']/bars[end]['close']-1)}
 for n in [1,5,20,63]:
  if len(ds)>n:
   start=ds[-1-n];row[f'{n}d_start']=start;row[f'{n}d_price_ret_pct']=100*(bars[end]['close']/bars[start]['close']-1)
   if bars[end]['adjusted'] and bars[start]['adjusted']:row[f'{n}d_adj_ret_pct']=100*(bars[end]['adjusted']/bars[start]['adjusted']-1)
 rows.append(row)
lookup={r['symbol']:r for r in rows};pairs=[]
for eq,cap in [('RSP','SPY'),('QQEW','QQQ')]:
 x={'equal_weight':eq,'cap_weight':cap}
 for n in [5,20,63]:
  a=lookup[eq][f'{n}d_adj_ret_pct'];b=lookup[cap][f'{n}d_adj_ret_pct'];x[f'{n}d_arithmetic_gap_pp']=a-b;x[f'{n}d_relative_ratio_pct']=100*((1+a/100)/(1+b/100)-1);assert lookup[eq][f'{n}d_start']==lookup[cap][f'{n}d_start']
 x['intraday_gap_pp']=lookup[eq]['intraday_ret_pct']-lookup[cap]['intraday_ret_pct'];pairs.append(x)
sector=['XLK','XLC','XLY','XLF','XLV','XLI','XLP','XLE','XLU','XLRE','XLB'];secs=sorted([lookup[s] for s in sector],key=lambda x:x['intraday_ret_pct'],reverse=True)
snap=json.loads((D/'constituent-snapshot.json').read_text());u=json.loads((D/'universe.json').read_text());names={x['ticker']:x for x in u['rows']};out=[]
for s,x in snap.items():
 if x['quote_ret_pct'] is not None:out.append({'symbol':s,'name':names[s]['name'],'weight_pct_asof10_16':names[s]['weight_pct'],'intraday_ret_pct':x['quote_ret_pct'],'proxy_contribution_pp':names[s]['weight_pct']*x['quote_ret_pct']/100,'quote_time':x['quote_time']})
out.sort(key=lambda x:x['proxy_contribution_pp'],reverse=True)
# Data-derived validation: count partitions, age, prior-close/date matches and quote/bar discrepancies.
b=json.loads((D/'breadth-summary.json').read_text());assert b['up']+b['down']+b['unchanged']==b['usable_current_session']==503
now_dt=datetime.fromisoformat(b['finished']);ages=[(now_dt-datetime.fromisoformat(x['quote_time'])).total_seconds() for x in snap.values()]
bar_discrep=[{'symbol':s,'quote_return':x['quote_ret_pct'],'bar_return':x['bar_ret_pct']} for s,x in snap.items() if x['bar_ret_pct'] is not None and abs(x['bar_ret_pct']-x['quote_ret_pct'])>0.05]
# Recompute using today'schartbar instead ofmetaquote as a secondmethod, without claiming independentvendor.
returns=[x['bar_ret_pct'] for x in snap.values() if x['bar_ret_pct'] is not None]
validation={'coverage':503,'partition':'PASS','missing':b['missing'],'quote_age_seconds_min':min(ages),'quote_age_seconds_max':max(ages),'quote_bar_method_discrepancies_gt_005pp':bar_discrep,'bar_method_counts':{'up':sum(v>0 for v in returns),'down':sum(v<0 for v in returns),'flat':sum(v==0 for v in returns),'coverage':len(returns)},'independence':'metaquoteandchartbarshareYahoo;crosschecknotsourceindependence','issuer_weight_sum_note':'SPYfileallnumericweightssum100.218976%;tradableequity99.929217%. Do notcertifyindexcontributionsfromthisfile;weightedrankingisonlyapproximate.'}
res={'proxies':rows,'equal_vs_cap':pairs,'sector_snapshot':secs,'sector_positive':sum(x['intraday_ret_pct']>0 for x in secs),'sector_negative':sum(x['intraday_ret_pct']<0 for x in secs),'contribution_ranking_approx':out,'validation':validation};(D/'analysis.json').write_text(json.dumps(res,indent=2)+'\n')
with (D/'proxy-summary.csv').open('w') as f:
 fields=sorted(set().union(*(r.keys() for r in rows)));w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
print('Core proxies:')
for s in ['SPY','RSP','QQQ','QQEW','IWM','DIA','SMH','KRE']:
 x=lookup[s];print(s,'today',round(x['intraday_ret_pct'],3),'5d',round(x['5d_adj_ret_pct'],3),'20d',round(x['20d_adj_ret_pct'],3),'63d',round(x['63d_adj_ret_pct'],3),x['quote_time'])
print('Pairs',json.dumps(pairs));print('Sectors+',res['sector_positive'],'-',res['sector_negative'],[(x['symbol'],round(x['intraday_ret_pct'],2)) for x in secs]);print('Proxy contribution ranking',[(x['symbol'],round(x['intraday_ret_pct'],2),round(x['proxy_contribution_pp'],3)) for x in out[:12]])
print('Validation',json.dumps(validation))
print('Plot export deferred: no plotting library installed; standalone SVG generated separately.')
