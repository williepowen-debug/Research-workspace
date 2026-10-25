"""Independent raw-data arithmetic and loop-based count checks, not forecasting tests."""
from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal
import csv,json,hashlib
import pandas as pd

p=Path(__file__).resolve().parent; desk=p.parents[2]
out=json.loads((p/'summary.json').read_text())
x=pd.read_excel(p/'GLD_issuer_archive.xlsx',sheet_name='US GLD Historical Archive')
rows={pd.Timestamp(r['Date']).strftime('%Y-%m-%d'):r for r in x.to_dict('records')}
prices={k:Decimal(str(r['Closing Price'])) for k,r in rows.items()
        if pd.notna(pd.to_numeric(r['Closing Price'],errors='coerce'))}
def raw_market(symbol,key):
    raw=json.loads((p/(symbol+'.json')).read_text())['chart']['result'][0]
    values=raw['indicators']['adjclose'][0]['adjclose'] if key=='adjclose' else raw['indicators']['quote'][0][key]
    return {datetime.fromtimestamp(t,timezone.utc).strftime('%Y-%m-%d'):Decimal(str(v))
            for t,v in zip(raw['timestamp'],values) if v is not None}
y=raw_market('GLD','close'); spy=raw_market('SPY','adjclose'); dxy=raw_market('DX-Y.NYB','close')
assert abs(float(y['2026-10-23'])-366.61)<.0001
assert abs(float(100*(y['2026-10-23']/prices['2026-07-16']-1))-out['price']['above_july_low_pct'])<1e-9
assert y['2026-10-23']<prices['2026-10-14']
merged=prices|{k:v for k,v in y.items() if '2026-10-22'<k<='2026-10-23'}
for n in [20,60]:
    z=sorted(merged)[-n:]
    assert min(merged[k] for k in z)==merged['2026-10-23']
assert abs(float(rows['2026-10-22']['Tonnes of Gold'])-float(rows['2026-10-21']['Tonnes of Gold'])+11.98)<1e-9
assert abs(float(rows['2026-10-22']['Tonnes of Gold'])-float(rows['2026-10-15']['Tonnes of Gold'])+8.27)<1e-9
assert abs(float(100*(prices['2026-10-22']/prices['2026-10-09']-1))+4.051172707889117)<1e-9
yields={r[0]:float(r[2]) for r in list(csv.reader((p/'matched_financial_conditions.csv').open()))[1:]}
# Only need latest61 shared observations; this avoids treating earlier unmatched market starts as daily pairs.
dates=sorted(k for k in merged if k in spy and k in dxy)[-61:]
returns=[]
for a,b in zip(dates,dates[1:]):
    returns.append(dict(date=b,g=float(100*(merged[b]/merged[a]-1)),s=float(100*(spy[b]/spy[a]-1)),
       y=yields[b]-yields[a] if a in yields and b in yields else None,d=dxy[b]-dxy[a]))
for n in [20,60]:
    z=returns[-n:]
    cases=[('SPY_down',lambda r:r['s']<0),('SPY_down_at_least1pct',lambda r:r['s']<=-1)]
    for condition,fn in cases:
        a=[r for r in z if fn(r)]
        target=next(r for r in out['equity_response'] if r['window_sessions']==n and r['condition']==condition)
        assert len(a)==target['n'] and sum(r['g']>0 for r in a)==target['gold_up']
        assert abs(sum(r['g'] for r in a)/len(a)-target['mean_gold_pct'])<1e-10
    cases=[('real_yield_falls',lambda r:r['y'] is not None and r['y']<0),
           ('yield_and_dollar_fall',lambda r:r['y'] is not None and r['y']<0 and r['d']<0)]
    for condition,fn in cases:
        a=[r for r in z if fn(r)]
        target=next(r for r in out['conditional_financial_response'] if r['window_sessions']==n and r['condition']==condition)
        assert len(a)==target['n'] and sum(r['g']>0 for r in a)==target['gold_up']
        assert abs(sum(r['g'] for r in a)/len(a)-target['mean_gold_pct'])<1e-10

checks={'result':'PASS','checked':['Raw price near July low, broken October14 local low, latest20/60 minimum',
    'Raw issuer daily/five-observation bullion changes','Raw issuer fixed Oct9-22 return',
    'Independent raw-market adjacent-session equity/rate conditional counts and means'],'global_weekly_source':{}}
for name in ['sources/2026-10-20_news/wgc_weekly.pdf','sources/2026-10-20_GLD-review/wgc-weekly-flows-page13.png']:
    checks['global_weekly_source'][name]={'sha256':hashlib.sha256((desk/name).read_bytes()).hexdigest()}
checks['global_weekly_source']['visual_read']='Printed page13: week ended October16; net demand13.9t, flowsUSD1916.0mn; complete82/202 funds,74.8% of AUM; lagged partial snapshot.'
(p/'verification.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
