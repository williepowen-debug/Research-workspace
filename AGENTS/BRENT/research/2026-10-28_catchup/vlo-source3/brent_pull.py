#!/usr/bin/env python3
"""Named Brent/RBOB contract window proxies (ESTIMATE, vendor 1m bars). ICE Brent settles 19:28-19:30 London;
London on GMT from 2026-10-25, New York EDT until 2026-11-01 => 15:28-15:30 ET this week. NYMEX RB 14:28-14:30 ET.
Context only; no registered count, grade or settlement substitution."""
import json,datetime as dt
from decimal import Decimal as D
from pathlib import Path
import yfinance as yf
R=Path(__file__).resolve().parent/'raw';out={}
win={'BZZ26.NYM':('15:28','15:29'),'BZF27.NYM':('15:28','15:29'),'BZG27.NYM':('15:28','15:29'),'RBZ26.NYM':('14:28','14:29')}
for s,w in win.items():
    t=yf.Ticker(s);h=t.history(period='5d',interval='1m',prepost=True)
    rows=[dict(label=i.tz_convert('America/New_York').isoformat(),close=float(r.Close),volume=int(r.Volume)) for i,r in h.iterrows()]
    json.dump(rows,open(R/f'{s}-1m.json','w'))
    exp=t.info.get('expireDate');out[s]={'expire_utc':dt.datetime.fromtimestamp(exp,dt.timezone.utc).date().isoformat() if exp else None,'days':{}}
    for d in ['2026-10-26','2026-10-27','2026-10-28']:
        b=[r for r in rows if r['label'][:10]==d and r['label'][11:16] in w]
        v=sum(r['volume'] for r in b)
        out[s]['days'][d]={'bars':[(r['label'][11:16],r['close'],r['volume']) for r in b],'vwap':round(sum(r['close']*r['volume'] for r in b)/v,4) if v>0 and len(b)==2 else None}
    out[s]['last']=rows[-1] if rows else None
json.dump(out,open(Path(__file__).resolve().parent/'brent_window.json','w'),indent=1)
for s,v in out.items(): print(s,v['expire_utc'],{d:x['vwap'] for d,x in v['days'].items()},v['last'])
