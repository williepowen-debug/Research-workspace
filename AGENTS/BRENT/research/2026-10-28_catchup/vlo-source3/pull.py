#!/usr/bin/env python3
"""Pull vendor one-minute bars (yfinance) for HOZ26/CLZ26 (+HOF27 negative identity control, SPY bar-convention control).
Research only; vendor transport, never a settlement."""
import json,datetime as dt
from pathlib import Path
import yfinance as yf
R=Path(__file__).resolve().parent/'raw'
for s in ['HOZ26.NYM','CLZ26.NYM','HOF27.NYM','SPY']:
    t=yf.Ticker(s)
    h=t.history(period='8d',interval='1m',prepost=True)
    rows=[dict(label=i.tz_convert('America/New_York').isoformat(),open=float(r.Open),high=float(r.High),low=float(r.Low),close=float(r.Close),volume=int(r.Volume)) for i,r in h.iterrows()]
    json.dump(rows,open(R/f'{s}-1m.json','w'))
    info={k:t.info.get(k) for k in ['symbol','shortName','longName','exchange','quoteType','currency','expireDate','underlyingSymbol','exchangeTimezoneName']}
    json.dump(info,open(R/f'info-{s}.json','w'))
    print(s,len(rows),rows[0]['label'] if rows else None,rows[-1]['label'] if rows else None,info.get('shortName'),info.get('expireDate'))
print('pulled_at',dt.datetime.now(dt.timezone.utc).isoformat())
