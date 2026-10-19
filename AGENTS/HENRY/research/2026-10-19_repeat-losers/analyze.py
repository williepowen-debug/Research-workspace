import json,csv,pathlib,datetime,math
from zoneinfo import ZoneInfo
P=pathlib.Path(__file__).resolve().parent;NY=ZoneInfo('America/New_York');END='2026-10-19'
def read(s):
 try:
  d=json.loads((P/'raw'/('chart-'+s+'.json')).read_text())['chart']['result'][0];assert d['meta']['symbol']==s
  a=d['indicators']['adjclose'][0]['adjclose'];q=d['indicators']['quote'][0]
  return {datetime.datetime.fromtimestamp(t,NY).date().isoformat():dict(adj=ac,raw=c) for t,ac,c in zip(d['timestamp'],a,q['close']) if ac is not None and c is not None and ac>0 and c>0}
 except Exception:return {}
u=json.loads((P/'universe.json').read_text());stocks=[r['ticker'] for r in u['rows']];external={'BWXT':'XLI','RBA':'XLI','QSR':'XLY','NTR':'XLB','INGR':'XLP'};sectors={r['symbol']:r['sector'] for r in csv.DictReader((P/'sector-map.csv').open())};sectors.update(external);syms=list(dict.fromkeys(stocks+list(external)+['SPY','RSP','QQQ','QQEW','IWM']+list(set(sectors.values()))));data={s:read(s) for s in syms}
cal=sorted(d for d in data['SPY'] if d<=END);assert cal[-1]==END;dates={str(n):cal[-1-n] for n in [5,20,60]};assert len(cal[-61:])==61
metrics={};excluded=[];daily=[]
for s in stocks+list(external):
 sec=sectors.get(s);prices=data[s];reason=''
 if s=='SKYD':reason='October6acquisition/tickerhistory_unreconciled'
 elif not sec or sec not in data:reason='sector_UNKNOWN'
 elif any(day not in prices or day not in data[sec] for day in cal[-61:]):reason='missing_stock_or_sector_bar_in61sessiongrid'
 if reason:excluded.append(dict(symbol=s,reason=reason));continue
 m={'sector':sec,'formation_raw_close':prices[dates['20']]['raw'],'windows':{}}
 for n in [5,20,60]:
  grid=cal[-n-1:];start=grid[0];rows=[]
  for prev,day in zip(grid,grid[1:]):
   r={t:data[t][day]['adj']/data[t][prev]['adj']-1 for t in [s,'SPY',sec]};sr=r[s];ir=r['SPY'];cr=r[sec]
   row=dict(symbol=s,window=n,date=day,stock_return=sr,index_return=ir,sector_return=cr,index_up=ir>0,sector_up=cr>0,both_up=ir>0 and cr>0,stock_loss=sr<0,index_lag=sr<ir,sector_lag=sr<cr);rows.append(row);daily.append(row)
  ret=100*(prices[END]['adj']/prices[start]['adj']-1);iret=100*(data['SPY'][END]['adj']/data['SPY'][start]['adj']-1);cret=100*(data[sec][END]['adj']/data[sec][start]['adj']-1)
  w=dict(start=start,end=END,return_pct=ret,index_pct=iret,sector_pct=cret,index_relative_wealth_pct=100*((1+ret/100)/(1+iret/100)-1),sector_relative_wealth_pct=100*((1+ret/100)/(1+cret/100)-1))
  for cond in ['index_up','sector_up','both_up']:
   eligible=[r for r in rows if r[cond]];k=len(eligible);loss=sum(r['stock_loss'] for r in eligible)
   w[cond]=dict(eligible=k,losses=loss,loss_fraction=loss/k if k else None,index_lags=sum(r['index_lag'] for r in eligible),sector_lags=sum(r['sector_lag'] for r in eligible),stock_conditional_pct=100*(math.prod(1+r['stock_return'] for r in eligible)-1) if k else None,sector_conditional_pct=100*(math.prod(1+r['sector_return'] for r in eligible)-1) if k else None,index_conditional_pct=100*(math.prod(1+r['index_return'] for r in eligible)-1) if k else None)
  m['windows'][str(n)]=w
 a,b,c=[m['windows'][str(n)] for n in [5,20,60]]
 enough=b['both_up']['eligible']>=5 and c['both_up']['eligible']>=15
 persistent=enough and b['return_pct']<0 and c['return_pct']<0 and b['both_up']['loss_fraction']>.5 and c['both_up']['loss_fraction']>.5
 if not enough:m['label']='INSUFFICIENT'
 elif persistent:m['label']='RECOVERING' if a['return_pct']>=0 or a['both_up']['loss_fraction'] is None or a['both_up']['loss_fraction']<=.5 else 'CURRENTLY-PERSISTENT'
 elif b['return_pct']<0 and c['return_pct']>=0:m['label']='RECENT-ROTATION'
 else:m['label']='OTHER'
 m['persistent_history']=persistent;metrics[s]=m
ranked=sorted([s for s,m in metrics.items() if s in stocks and m['persistent_history']],key=lambda s:(-metrics[s]['windows']['20']['both_up']['loss_fraction'],metrics[s]['windows']['20']['sector_relative_wealth_pct'],s));shortlist=ranked[:8]
bench={s:{str(n):100*(data[s][END]['adj']/data[s][dates[str(n)]]['adj']-1) for n in [5,20,60]} for s in ['SPY','RSP','QQQ','QQEW','IWM']}
result=dict(endpoint=END,starts=dates,universe=len(stocks),covered=sum(s in metrics for s in stocks),excluded=excluded,labels={l:sum(metrics[s]['label']==l for s in stocks if s in metrics) for l in sorted({m['label'] for m in metrics.values()})},persistent_rank=ranked,shortlist=shortlist,benchmarks=bench)
for name,d in [('metrics.json',metrics),('summary.json',result)]: (P/name).write_text(json.dumps(d,indent=2)+'\n')
with (P/'daily-audit.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(daily[0]));w.writeheader();w.writerows(daily)
print(json.dumps(result,indent=2))
for s in shortlist+['SNDK','COHR','STX','WDC','MGM','MOS','DELL','SMCI']:
 if s in metrics:
  m=metrics[s];print(s,m['sector'],m['label'], [(n,round(m['windows'][n]['return_pct'],2),str(m['windows'][n]['both_up']['losses'])+'/'+str(m['windows'][n]['both_up']['eligible'])) for n in ['5','20','60']])
print('PASS exact61bargrid,fulluniversecounts,strictseparateindex/sector/bothconditions')
