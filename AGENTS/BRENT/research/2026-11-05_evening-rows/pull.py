#!/usr/bin/env python3
"""BRENT 11/5 evening: named-contract vendor one-minute bars and daily rows. ESTIMATE only; no settlement.
Window [14:28,14:30) ET (ICE Brent 19:28-19:30 London, both on standard time since 2026-11-01)."""
import json,datetime as dt
from pathlib import Path
import yfinance as yf
H=Path(__file__).resolve().parent;R=H/'raw'
syms=['BZF27.NYM','BZG27.NYM','BZH27.NYM','CLZ26.NYM','HOF27.NYM','RBF27.NYM','HOZ26.NYM','RBZ26.NYM']
out={}
for s in syms:
    t=yf.Ticker(s)
    h=t.history(period='5d',interval='1m',prepost=True)
    rows=[dict(label=i.tz_convert('America/New_York').isoformat(),close=float(r.Close),volume=int(r.Volume)) for i,r in h.iterrows()]
    json.dump(rows,open(R/f'{s}-1m.json','w'))
    d=t.history(period='10d',interval='1d',prepost=False)
    drows=[dict(date=i.tz_convert('America/New_York').date().isoformat(),close=float(r.Close),volume=int(r.Volume)) for i,r in d.iterrows()]
    json.dump(drows,open(R/f'{s}-1d.json','w'))
    b=[r for r in rows if r['label'][:10]=='2026-11-05' and r['label'][11:16] in('14:28','14:29')]
    v=sum(r['volume'] for r in b)
    out[s]=dict(bars=[(r['label'][11:16],r['close'],r['volume']) for r in b],vwap=round(sum(r['close']*r['volume'] for r in b)/v,4) if v>0 and len(b)==2 else None,daily=drows[-4:],rows_on_1105=len([r for r in rows if r['label'][:10]=='2026-11-05']),last=rows[-1] if rows else None)
    try:
        i=t.info; out[s]['expire']=dt.datetime.fromtimestamp(i['expireDate'],dt.timezone.utc).date().isoformat() if i.get('expireDate') else None
    except Exception as e: out[s]['expire']=str(e)
json.dump(out,open(H/'window.json','w'),indent=1)
for s,v in out.items(): print(s,v['expire'],'bars',v['bars'],'vwap',v['vwap'],'n1105',v['rows_on_1105']);print('   daily',v['daily'])
