#!/usr/bin/env python3
"""BRENT WQ-420 source-(3) December crack observations, C3 = 42*P_HO - P_CL over [14:28,14:30) ET,
Close x Volume VWAP per leg, native-tick normalized (HO 0.0001, CL 0.01) per the WQ-420 approved insert.
Adapted from research/2026-10-21_henry-december-adoption/{compute,normalize}.py. ESTIMATE only.
Research only; TERRY owns holding grades; no threshold, grade or trade authority."""
import json,datetime as dt,numpy as np
from decimal import Decimal as D,getcontext
from pathlib import Path
getcontext().prec=40
H=Path(__file__).resolve().parent;RAW=H/'raw'
load=lambda s: json.load(open(RAW/f'{s}-1m.json'))
days=['2026-10-22','2026-10-23','2026-10-26','2026-10-27','2026-10-28']
ident={s:json.load(open(RAW/f'info-{s}.json')) for s in ['HOZ26.NYM','CLZ26.NYM','HOF27.NYM']}
expiry={s:dt.datetime.fromtimestamp(v['expireDate'],dt.timezone.utc).date().isoformat() for s,v in ident.items()}
assert expiry['HOZ26.NYM']=='2026-11-30' and expiry['CLZ26.NYM']=='2026-11-20' and expiry['HOF27.NYM']!=expiry['HOZ26.NYM']
TICK={'HOZ26.NYM':D('0.0001'),'CLZ26.NYM':D('0.01')}
def norm(x,tick):
    f=np.float32(x);n=(D(repr(float(x)))/tick).to_integral_value()*tick
    rt=lambda v: np.float32(float(v))==f
    return n,rt(n) and not rt(n-tick) and not rt(n+tick)
spy=load('SPY');hof=load('HOF27.NYM')
CME_1023=D('97.7840')  # source (1), CME FINAL bulletin 205 (10/23), research/2026-10-26_energy-review
obs=[]
for d in days:
    reg=[r['label'] for r in spy if r['label'][:10]==d and '09:30'<=r['label'][11:16]<='15:59']
    conv=dict(count=len(reg),first=reg[0][11:16] if reg else None,last=reg[-1][11:16] if reg else None)
    legs={};ok=True;why=[]
    for s in ['HOZ26.NYM','CLZ26.NYM']:
        rows=[r for r in load(s) if r['label'][:10]==d and r['label'][11:16] in ('14:28','14:29')]
        labels=[r['label'][11:16] for r in rows]
        if labels!=['14:28','14:29']: ok=False;why.append(f'{s} bars {labels}')
        if any(r['close']<=0 for r in rows): ok=False;why.append(f'{s} nonpositive price')
        nrows=[]
        for r in rows:
            n,good=norm(r['close'],TICK[s])
            if not good: ok=False;why.append(f'{s} {r["label"][11:16]} tick roundtrip not unique')
            nrows.append(dict(label=r['label'],transport=r['close'],native=str(n),volume=r['volume']))
        vol=sum(D(r['volume']) for r in nrows)
        if vol<=0: ok=False;why.append(f'{s} zero total volume')
        legs[s]=dict(rows=nrows,vwap=None if vol<=0 else str(sum(D(r['native'])*D(r['volume']) for r in nrows)/vol))
    c=D(legs['HOZ26.NYM']['vwap'])*42-D(legs['CLZ26.NYM']['vwap']) if ok else None
    hz=[r['close'] for r in load('HOZ26.NYM') if r['label'][:10]==d and r['label'][11:16] in ('14:28','14:29')]
    hf=[r['close'] for r in hof if r['label'][:10]==d and r['label'][11:16] in ('14:28','14:29')]
    o=dict(date=d,valid=ok and conv['count']==390,defects=why,bar_convention_SPY=conv,
        negative_control_HOF27_differs=(hz!=hf) if hf else 'HOF27 bars missing',
        c3=None if c is None else str(c),below_95=None if c is None else c<D(95),below_9016=None if c is None else c<D('90.16'),
        margin_vs_95=None if c is None else str(c-D(95)),margin_vs_9016=None if c is None else str(c-D('90.16')),
        within_015_of_9016=None if c is None else abs(c-D('90.16'))<=D('0.15'),legs=legs)
    if d=='2026-10-23' and c is not None: o['positive_control_vs_CME_source1']=dict(cme_c1=str(CME_1023),abs_diff=str(abs(c-CME_1023)))
    obs.append(o)
json.dump(dict(rule='WQ-420 source (3), native-tick normalized, ESTIMATE',contracts=dict(identity=ident,expiry_utc=expiry),observations=obs),open(H/'calculations.json','w'),indent=1)
for o in obs: print(o['date'],'valid',o['valid'],'C3',o['c3'][:10] if o['c3'] else None,'<95',o['below_95'],'<90.16',o['below_9016'],'band9016',o['within_015_of_9016'],'SPY',o['bar_convention_SPY']['count'],'negctl',o['negative_control_HOF27_differs'],o.get('positive_control_vs_CME_source1',''),o['defects'])
