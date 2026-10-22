#!/usr/bin/env python3
"""WQ-420 precision step: normalize each vendor float transport value to its CME native tick
(HO 0.0001 USD/gal, rule 150102.C; CL 0.01 USD/bbl, rule 200102.C, as verified by TERRY 10/19 at primary).
Accept only if the tick value round-trips EXACTLY to the float32 transport value and both adjacent ticks do not.
Research only; no threshold, holding grade or trade authority."""
import json,numpy as np
from decimal import Decimal as D,getcontext
from pathlib import Path
getcontext().prec=40
H=Path(__file__).resolve().parent
calc=json.load(open(H/'calculations.json'))
TICK={'HOZ26.NYM':D('0.0001'),'CLZ26.NYM':D('0.01')}
def norm(x,tick):
    f=np.float32(x); n=(D(repr(float(x)))/tick).to_integral_value()*tick
    rt=lambda v: np.float32(float(v))==f
    return n, rt(n) and not rt(n-tick) and not rt(n+tick)
out=[]
for o in calc['observations']:
    legs={};ok=True
    for s,v in o['legs'].items():
        rows=[]
        for r in v['rows']:
            n,good=norm(r['close'],TICK[s]); ok&=good
            rows.append(dict(label=r['label'],transport=r['close'],native=str(n),roundtrip_unique=good,volume=r['volume']))
        vol=sum(D(r['volume']) for r in rows)
        legs[s]=dict(rows=rows,vwap=str(sum(D(r['native'])*D(r['volume']) for r in rows)/vol))
    c=D(legs['HOZ26.NYM']['vwap'])*42-D(legs['CLZ26.NYM']['vwap'])
    out.append(dict(date=o['date'],precision_verified=ok,c3=str(c),below_95=c<D(95),below_9016=c<D('90.16'),
        margin_vs_95=str(c-D(95)),margin_vs_9016=str(c-D('90.16')),within_015_of_9016=abs(c-D('90.16'))<=D('0.15'),
        within_015_of_95=abs(c-D(95))<=D('0.15'),transport_c3=o['c3'],legs=legs))
json.dump(dict(rule='WQ-420 source (3), native-tick normalized',observations=out),open(H/'normalized.json','w'),indent=1)
for x in out: print(x['date'],x['precision_verified'],x['c3'][:14],'<95',x['below_95'],'<90.16',x['below_9016'],'m95',x['margin_vs_95'][:9],'band95',x['within_015_of_95'],'band9016',x['within_015_of_9016'])
