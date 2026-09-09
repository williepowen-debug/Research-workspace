"""Reproduce the catch-up's matched-clock arithmetic from saved inputs; no network."""
from pathlib import Path
import csv,json
import pandas as pd
P=Path(__file__).resolve().parent
R=P/'raw'
def series(name):
 d=pd.read_csv(R/name,index_col=0)
 d.index=pd.to_datetime(d.index,utc=True)
 return d['Close'].dropna()
out={}
for key in ['usdjpy','eurjpy','audjpy']:
 s=series(key+'-1h.csv'); w=s.loc['2026-09-02':'2026-09-08']; ch=w.pct_change(fill_method=None)*100
 t=ch.idxmin()
 out[key]={'sep2_22utc':float(s.loc['2026-09-02 22:00Z']),'sep8_22utc':float(s.loc['2026-09-08 22:00Z']),
 'return_pct':float((s.loc['2026-09-08 22:00Z']/s.loc['2026-09-02 22:00Z']-1)*100),
 'largest_hourly_fall_bar_utc':str(t),'largest_hourly_fall_pct':float(ch.loc[t])}
a=series('brent-nov-1h.csv');b=series('usdjpy-1h.csv')
t0='2026-09-04 19:00Z';t1='2026-09-08 19:00Z'
o0,o1=float(a.loc[t0]),float(a.loc[t1]);f0,f1=float(b.loc[t0]),float(b.loc[t1])
out['energy']={'bar_start_utc':[t0,t1],'brent_Nov_USD':[o0,o1],'USDJPY':[f0,f1],
 'JPY_per_barrel_proxy':[o0*f0,o1*f1], 'oil_return_pct':(o1/o0-1)*100,'fx_return_pct':(f1/f0-1)*100,
 'yen_oil_return_pct':(o1*f1/(o0*f0)-1)*100,'break_even_USDJPY':o0*f0/o1}
for fn in ['mof-month-lt.csv','mof-month-equity.csv']:
 rows=list(csv.reader((R/fn).read_text(encoding='cp932').splitlines()));year=''; found=[]
 for r in rows:
  if r and r[0].strip().isdigit():year=r[0].strip()
  if year=='2026' and len(r)>50 and r[2]=='Aug':
   found.append({name:float(r[col].replace(',',''))/10 for name,col in [('all',5),('banks_banking',20),('trust_banks_banking',23),('banks_trust_accounts',32),('financial_instruments_firms',41),('life_insurers',44),('investment_trusts',50)]})
 assert len(found)==1, (fn,found)
 out[fn+'_net_billion_yen']=found[0]
assert abs(out['energy']['yen_oil_return_pct']-1.36)<.01
(P/'calculations.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
