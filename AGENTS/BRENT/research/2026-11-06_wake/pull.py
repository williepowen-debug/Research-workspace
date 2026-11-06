#!/usr/bin/env python3
"""BRENT 11/6 intraday marks: named-contract vendor one-minute bars. ESTIMATE, not a settle. No window yet at run time."""
import json,datetime as dt
from pathlib import Path
import yfinance as yf
H=Path(__file__).resolve().parent;R=H/'raw'
syms=['BZF27.NYM','BZG27.NYM','BZH27.NYM','CLZ26.NYM','HOF27.NYM','RBF27.NYM','HOZ26.NYM']
D={}
for s in syms:
    t=yf.Ticker(s); h=t.history(period='3d',interval='1m',prepost=True)
    rows=[dict(label=i.tz_convert('America/New_York').isoformat(),close=float(r.Close),volume=int(r.Volume)) for i,r in h.iterrows()]
    json.dump(rows,open(R/f'{s}-1m.json','w')); D[s]={r['label'][:16]:r for r in rows}
    exp=None
    try:
        i=t.info; exp=dt.datetime.fromtimestamp(i['expireDate'],dt.timezone.utc).date().isoformat() if i.get('expireDate') else None
    except Exception as e: exp=str(e)[:40]
    today=[r for r in rows if r['label'][:10]=='2026-11-06']
    print(s,'exp',exp,'bars today',len(today),'vol>0',sum(1 for r in today if r['volume']>0),'last',today[-1]['label'][11:16] if today else None,today[-1]['close'] if today else None)
pairs=[(k,round(D['BZF27.NYM'][k]['close']-D['BZH27.NYM'][k]['close'],2)) for k in sorted(D['BZF27.NYM']) if k in D['BZH27.NYM'] and k[:10]=='2026-11-06' and D['BZF27.NYM'][k]['volume']>0 and D['BZH27.NYM'][k]['volume']>0]
print('M1-M3 same-minute pairs today',len(pairs),'min',min(p[1] for p in pairs) if pairs else None,'max',max(p[1] for p in pairs) if pairs else None,'last5',pairs[-5:])
def last(s):
    r=[x for k,x in sorted(D[s].items()) if k[:10]=='2026-11-06' and x['volume']>0]; return r[-1]['close'],r[-1]['label'][11:16]
b,bt=last('BZF27.NYM');c,ct=last('CLZ26.NYM');ho,ht=last('HOF27.NYM');rb,rt=last('RBF27.NYM');hz,hzt=last('HOZ26.NYM')
print('BZF27',b,bt,'CLZ26',c,ct,'HOF27',ho,ht,'RBF27',rb,rt,'HOZ26',hz,hzt)
print('Jan 3:2:1',round((2*rb+ho)*42/3-b,2),'Dec crack HOZ26x42-CLZ26',round(hz*42-c,2),'Jan HO crack vs BZF27',round(ho*42-b,2))
