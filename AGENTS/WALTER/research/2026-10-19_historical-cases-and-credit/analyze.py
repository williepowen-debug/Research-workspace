from pathlib import Path
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
import json,math,statistics,csv
D=Path(__file__).resolve().parent;NY=ZoneInfo('America/New_York');end='2026-10-16'
P=D/'history' if (D/'history').exists() else D.parent/'2026-10-19_breadth-followup'/'raw'
def load(p):
 z=json.loads(p.read_text())['chart']['result'][0];assert z['meta']['dataGranularity']=='1d'
 ds=[datetime.fromtimestamp(t,NY).date().isoformat() for t in z['timestamp']];assert len(ds)==len(set(ds))
 return ({d:v for d,v in zip(ds,z['indicators']['adjclose'][0]['adjclose']) if v is not None and d<=end},
         {d:v for d,v in zip(ds,z['indicators']['quote'][0]['close']) if v is not None and d<=end})
hist={s:load(P/f'chart-{s}.json')[0] for s in ['SPY','RSP']};ds=sorted(hist['SPY'])
cases=[('2007 breadth warning','2007-10-09'),('2015 deterioration','2015-08-06'),('2023 narrow advance','2023-06-06'),('2024 majority-down month','2024-06-28')]
case_rows=[]
for label,anchor in cases:
 i=ds.index(anchor);out={'label':label,'anchor':anchor,'outcomes':{}}
 for h in [21,63,126,252]:
  days=ds[i:i+h+1];assert len(days)==h+1
  v=[hist['SPY'][d] for d in days];peak=v[0];dd=0;dd_day=anchor;peak_day=anchor;peak_at_dd=anchor
  for day,p in zip(days,v):
   if p>peak:peak=p;peak_day=day
   if p/peak-1<dd:dd=p/peak-1;dd_day=day;peak_at_dd=peak_day
  spy=v[-1]/v[0]-1;rsp=hist['RSP'][days[-1]]/hist['RSP'][anchor]-1
  out['outcomes'][str(h)]={'end':days[-1],'spy_adj_return_pct':100*spy,'rsp_adj_return_pct':100*rsp,'rsp_spy_ratio_change_pct':100*((1+rsp)/(1+spy)-1),'max_closing_drawdown_pct':100*dd,'drawdown_trough_date':dd_day,'drawdown_peak_date':peak_at_dd,'worst_return_from_anchor_pct':100*(min(v)/v[0]-1)}
 case_rows.append(out)
px={};raw={}
for s in ['RCL','NCLH','CCL','CMCSA','CHTR','SPY','RSP','IWM','XLY','XLC']:px[s],raw[s]=load(D/'raw'/(s+'.json'))
sessions=sorted(px['SPY']);assert sessions[-1]==end;recent=[]
for s in px:
 r={'symbol':s}
 for n in [5,20,60]:
  start=sessions[-1-n];required=sessions[-1-n:];assert all(d in px[s] for d in required)
  r[f'{n}d_start']=start;r[f'{n}d_adj_return_pct']=100*(px[s][end]/px[s][start]-1);r[f'{n}d_raw_return_pct']=100*(raw[s][end]/raw[s][start]-1)
 recent.append(r)
f=json.loads((D/'cruise-exposures.json').read_text());ratios={}
for s in ['RCL','NCLH']:
 x=f[s];principal=x['gross_principal_including_finance_leases'];liq=x['cash']+x['available_general_revolver']
 ratios[s]={'balance_date':f['balance_date'],'liquidity_to_gross_principal_pct':100*liq/principal,'six_month_operating_income_to_gross_principal_pct':100*x['operating_income_6months']/principal,'liquidity_to_scheduled_principal_interest_through2027_pct':100*liq/x['debt_principal_interest_through2027'],'gross_principal':principal,'general_liquidity':liq}
assert all(ratios['NCLH'][k]<ratios['RCL'][k] for k in ['liquidity_to_gross_principal_pct','six_month_operating_income_to_gross_principal_pct'])

def solve(a,b):
 a=[list(r)+[v] for r,v in zip(a,b)];n=len(b)
 for k in range(n):
  pivot=max(range(k,n),key=lambda i:abs(a[i][k]));a[k],a[pivot]=a[pivot],a[k];assert abs(a[k][k])>1e-14
  v=a[k][k];a[k]=[x/v for x in a[k]]
  for i in range(n):
   if i!=k:
    q=a[i][k];a[i]=[x-q*y for x,y in zip(a[i],a[k])]
 return [r[-1] for r in a]
formation='2026-09-18';i=sessions.index(formation);train_i=list(range(i-125,i+1));test_i=list(range(i+1,len(sessions)))
assert len(train_i)==126 and len(test_i)==20
def lr(s,k):return math.log(px[s][sessions[k]]/px[s][sessions[k-1]])
models=[]
for s in ['RCL','NCLH','CCL','CMCSA','CHTR']:
 sector='XLC' if s in ['CMCSA','CHTR'] else 'XLY'
 for spec in ['market','market_size_sector']:
  def x(k):
   z=[1,lr('SPY',k)]
   return z+[lr('IWM',k)-lr('SPY',k),lr(sector,k)-lr('SPY',k)] if spec!='market' else z
  xx=[x(k) for k in train_i];yy=[lr(s,k) for k in train_i];n=len(xx[0]);mat=[[sum(r[a]*r[b] for r in xx) for b in range(n)] for a in range(n)];vec=[sum(r[a]*v for r,v in zip(xx,yy)) for a in range(n)];beta=solve(mat,vec)
  resid=[v-sum(a*b for a,b in zip(r,beta)) for r,v in zip(xx,yy)]
  assert max(abs(sum(r[a]*v for r,v in zip(xx,resid))) for a in range(n))<1e-8
  sums=sum(lr(s,k)-sum(a*b for a,b in zip(x(k),beta)) for k in test_i)
  models.append({'symbol':s,'spec':spec,'sector_proxy':sector,'training_start':sessions[train_i[0]-1],'training_end':formation,'training_returns':126,'outcome_start':formation,'outcome_end':end,'outcome_sessions':20,'beta':beta,'cumulative_residual_log_return':sums,'residual_return_proxy_pct':100*math.expm1(sums),'limits':'Exploratory126-session pre-window OLS; factor residual is not a causal credit effect or investable return.'})
result={'asof':datetime.now(timezone.utc).isoformat(),'historical_cases':case_rows,'financing_ratios':ratios,'recent_returns':recent,'factor_sensitivity':models,'limits':['Four hindsight-selected histories use different breadth definitions; no hit rate.','2024 measurement date is not verified publication date; cases are not executable signals.','RCL/NCLH June30 financial-cushion ordering, not September actual liquidity or rolling-maturity ordering.','RCL/NCLH size/businessmix differ; factor controls do not establish causal refinancing attribution.','CMCSA/CHTR acquisition/maturity clocks prevent clean exposure ordering; returns descriptive only.']}
(D/'analysis.json').write_text(json.dumps(result,indent=2)+'\n')
with (D/'returns.csv').open('w') as g:w=csv.DictWriter(g,fieldnames=list(recent[0]));w.writeheader();w.writerows(recent)
print('HISTORY')
for r in case_rows:print(r['label'],r['anchor'],[(h,round(x['spy_adj_return_pct'],2),round(x['max_closing_drawdown_pct'],2),x['drawdown_trough_date']) for h,x in r['outcomes'].items()])
print('RATIOS',ratios)
print('RECENT',[(r['symbol'],round(r['20d_adj_return_pct'],3),round(r['60d_adj_return_pct'],3)) for r in recent])
print('RESIDUALS',[(r['symbol'],r['spec'],round(r['residual_return_proxy_pct'],3)) for r in models])
