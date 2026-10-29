#!/usr/bin/env python3
"""WQ-420 source (2) acceptance check: vendor daily rows (yfinance 1d) for HOZ26/CLZ26 vs source (3).
Accept only a finalized session row with |C2-C3| <= 0.15; reject duplicated-volume/provisional rows. ESTIMATE context."""
import json
from decimal import Decimal as D
from pathlib import Path
import yfinance as yf
H=Path(__file__).resolve().parent
c3={o['date']:D(o['c3']) for o in json.load(open(H/'calculations.json'))['observations']}
rows={}
for s in ['HOZ26.NYM','CLZ26.NYM']:
    h=yf.Ticker(s).history(period='10d',interval='1d')
    rows[s]={i.date().isoformat():dict(close=float(r.Close),volume=int(r.Volume)) for i,r in h.iterrows()}
    json.dump(rows[s],open(H/'raw'/f'{s}-1d.json','w'),indent=1)
out={}
for d in ['2026-10-22','2026-10-23','2026-10-26','2026-10-27','2026-10-28']:
    ho=rows['HOZ26.NYM'].get(d);cl=rows['CLZ26.NYM'].get(d)
    if not ho or not cl: out[d]='missing'; continue
    c2=D(repr(ho['close'])).quantize(D('0.0001'))*42-D(repr(cl['close'])).quantize(D('0.01'))
    out[d]=dict(ho=ho,cl=cl,c2=str(c2),c3=str(c3[d]),abs_diff=str(abs(c2-c3[d])),within_015=abs(c2-c3[d])<=D('0.15'))
json.dump(out,open(H/'source2_check.json','w'),indent=1)
for d,v in out.items(): print(d,v)
