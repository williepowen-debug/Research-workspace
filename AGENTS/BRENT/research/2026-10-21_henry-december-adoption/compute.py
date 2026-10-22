#!/usr/bin/env python3
"""BRENT independent WQ-420 source-(3) December crack, HOZ26x42-CLZ26, from BRENT's own vendor pull.
Research only. Compares against HENRY f1-calculations.json. No threshold, holding grade or trade authority."""
import json,datetime as dt
from decimal import Decimal as D,getcontext
from pathlib import Path
getcontext().prec=40
H=Path(__file__).resolve().parent; RAW=H/'raw'
HEN=H.parents[2]/'HENRY/research/2026-10-19_catchup/f1-calculations.json'
def load(s): return json.load(open(RAW/f'{s}-1m.json'))
days=['2026-10-15','2026-10-16','2026-10-19','2026-10-20','2026-10-21']
ident={s:json.load(open(RAW/f'info-{s}.json')) for s in ['HOZ26.NYM','CLZ26.NYM','HOF27.NYM']}
expiry={s:dt.datetime.fromtimestamp(v['expireDate'],dt.timezone.utc).date().isoformat() for s,v in ident.items()}
assert expiry['HOZ26.NYM']=='2026-11-30' and expiry['CLZ26.NYM']=='2026-11-20' and expiry['HOF27.NYM']!=expiry['HOZ26.NYM']
spy=load('SPY');conv={}
for d in days:
    reg=[r['label'] for r in spy if r['label'][:10]==d and '09:30'<=r['label'][11:16]<='15:59']
    conv[d]=dict(count=len(reg),first=reg[0] if reg else None,last=reg[-1] if reg else None)
hen={o['date']:o for o in json.load(open(HEN))['observations']}
obs=[]
for d in days:
    legs={};ok=True;why=[]
    for s in ['HOZ26.NYM','CLZ26.NYM']:
        rows=[r for r in load(s) if r['label'][:10]==d and r['label'][11:16] in ('14:28','14:29')]
        labels=[r['label'][11:16] for r in rows]
        if labels!=['14:28','14:29']: ok=False;why.append(f'{s} bars {labels}')
        if any(r['volume']<=0 or r['close']<=0 for r in rows): ok=False;why.append(f'{s} nonpositive')
        v=sum(D(r['volume']) for r in rows)
        vw=sum(D(repr(r['close']))*D(r['volume']) for r in rows)/v if v>0 else None
        legs[s]=dict(rows=[{k:r[k] for k in ('label','close','volume')} for r in rows],close_volume_vwap=str(vw))
    c3=D(legs['HOZ26.NYM']['close_volume_vwap'])*42-D(legs['CLZ26.NYM']['close_volume_vwap']) if ok else None
    o=dict(date=d,legs=legs,valid=ok and conv[d]['count']==390,defects=why,c3=None if c3 is None else str(c3),
           below_95=None if c3 is None else c3<D(95),below_9016=None if c3 is None else c3<D('90.16'),
           distance_to_9016=None if c3 is None else str(c3-D('90.16')))
    if d in hen:
        hc=D(hen[d]['crack']);o['henry_c3']=str(hc);o['abs_diff_vs_henry']=str(abs(c3-hc)) if c3 is not None else None
        o['input_match']=all(
            [(r['label'][:16],str(D(repr(r['close']))),r['volume']) for r in legs[s]['rows']]==
            [(r['label'][:16],str(D(r['close'])),r['volume']) for r in hen[d]['legs'][s]['rows']]
            for s in legs)
    obs.append(o)
res=dict(basis='WQ-420 source (3): [14:28,14:30) ET two one-minute bars per leg, Close x Volume VWAP per leg, C3=42*P_HO-P_CL, ESTIMATE',
         contracts=dict(identity=ident,expiry_utc=expiry),bar_convention_control_SPY=conv,observations=obs)
json.dump(res,open(H/'calculations.json','w'),indent=1)
for o in obs: print(o['date'],o['valid'],o['c3'],o.get('henry_c3'),o.get('abs_diff_vs_henry'),o.get('input_match'),o['defects'],conv[o['date']])
