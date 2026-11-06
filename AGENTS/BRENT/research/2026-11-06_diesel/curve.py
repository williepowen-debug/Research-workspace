#!/usr/bin/env python3
"""BRENT 11/6 diesel curve from named vendor contracts. ESTIMATE, intraday, not settlements. Contract identity read from expireDate."""
import json,datetime as dt
from pathlib import Path
import yfinance as yf
R=Path(__file__).resolve().parent/'raw'
mon=['Z26','F27','G27','H27','J27','K27','M27','N27','Q27','U27','Z27']
out={}
for root in ['HO','CL','RB']:
    for m in mon:
        s=f'{root}{m}.NYM'
        try:
            t=yf.Ticker(s);h=t.history(period='3d',interval='1m',prepost=False)
            r=[(i.tz_convert('America/New_York').isoformat()[:16],float(x.Close),int(x.Volume)) for i,x in h.iterrows() if x.Volume>0 and i.tz_convert('America/New_York').date()==dt.date(2026,11,6)]
            exp=None
            try:
                i=t.info;exp=dt.datetime.fromtimestamp(i['expireDate'],dt.timezone.utc).date().isoformat() if i.get('expireDate') else None
            except Exception: pass
            d=t.history(period='10d',interval='1d')
            out[s]=dict(exp=exp,last=r[-1] if r else None,n=len(r),vol=sum(x[2] for x in r),daily=[(str(i.date()),round(float(x.Close),4),int(x.Volume)) for i,x in d.iterrows()][-6:])
        except Exception as e: out[s]=dict(err=str(e)[:80])
json.dump(out,open(R/'curve_1106.json','w'),indent=1)
for m in mon:
    h,c=out.get(f'HO{m}.NYM',{}),out.get(f'CL{m}.NYM',{})
    if h.get('last') and c.get('last'):
        print(m,'HO',round(h['last'][1],4),h['last'][0][11:],'exp',h['exp'],'n',h['n'],'| CL',round(c['last'][1],2),c['last'][0][11:],'exp',c['exp'],'| crack',round(h['last'][1]*42-c['last'][1],2))
    else: print(m,'missing',h.get('n'),c.get('n'))
