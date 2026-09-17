#!/usr/bin/env python3
"""indeed_lead_test.py — LABOR L302 instrument (1) audit helper: Indeed postings YoY + the postings->JOLTS-hires LEAD TEST.

Built 2026-09-17 (promoted from the session scratchpad unchanged). Reads the two Indeed Hiring Lab CSVs from SP and JTSHIL/IHLIDXUS
via FORGE/tools/market-data/fetch.py. Result on 2026-09-17: total postings lead hires by +1 month at r=+0.31 (n=54, r^2=0.096); new postings show no lead.
Run from repo root; set SP to a dir holding indeed_us.csv (US/aggregate_job_postings_US.csv) and indeed_state.csv (US/state_job_postings_us.csv).
"""
import csv, sys, datetime as dt, statistics as st
sys.path.insert(0,'FORGE/tools/market-data'); import fetch
SP='/tmp/claude-1000/-home-willi-Research-workspace-PROME/dfdba42f-a266-4b11-be6a-5412cd418b80/scratchpad'
nat={}
with open(f'{SP}/indeed_us.csv') as f:
    hdr=None
    for r in csv.DictReader(f):
        nat.setdefault(r['variable'],{})[r['date']]=float(r['indeed_job_postings_index_SA'])
print("variables:", list(nat))
for v in nat:
    d=sorted(nat[v]); last=d[-1]; ya=(dt.date.fromisoformat(last)-dt.timedelta(days=364)).isoformat()
    print(f"{v}: {last} = {nat[v][last]:.2f} | yr-ago {ya} = {nat[v].get(ya)} | YoY {(nat[v][last]/nat[v][ya]-1)*100:+.2f}% | first obs {d[0]} n={len(d)}")
# FL
fl={}
with open(f'{SP}/indeed_state.csv') as f:
    for r in csv.DictReader(f):
        if r.get('state')=='FL' or r.get('geo')=='FL' or r.get('state_code')=='FL':
            fl[r['date']]=float(r['indeed_job_postings_index'])
if fl:
    d=sorted(fl); last=d[-1]; ya=(dt.date.fromisoformat(last)-dt.timedelta(days=364)).isoformat()
    print(f"FL: {last}={fl[last]:.2f} yr-ago {ya}={fl.get(ya)} YoY {(fl[last]/fl[ya]-1)*100:+.2f}%")
else:
    with open(f'{SP}/indeed_state.csv') as f: print("state cols:", next(csv.reader(f)))
# FRED IHLIDXUS vs repo
o=fetch.fred_fetch('IHLIDXUS',3); print("FRED IHLIDXUS:", o[:3])
# LEAD TEST: monthly avg of total postings vs JOLTS hires (JTSHIL), 2022-01..latest, 3-mo log changes, cross-corr at leads
tp=nat['total postings'] if 'total postings' in nat else nat[list(nat)[0]]
mon={}
for d,v in tp.items():
    m=d[:7]; mon.setdefault(m,[]).append(v)
mon={m:st.mean(v) for m,v in mon.items()}
h=fetch.fred_fetch('JTSHIL',80); hires={x['date'][:7]:float(x['value']) for x in h}
import math
months=sorted(m for m in mon if m>='2022-01' and m in hires)
def d3(series,m,k=3):
    y,mo=map(int,m.split('-')); mo2=mo-k; y2=y
    while mo2<1: mo2+=12; y2-=1
    p=f"{y2:04d}-{mo2:02d}"
    return math.log(series[m]/series[p]) if p in series and m in series else None
P={m:d3(mon,m) for m in months}; H={m:d3(hires,m) for m in months}
def shift(m,k):
    y,mo=map(int,m.split('-')); mo2=mo+k; y2=y
    while mo2>12: mo2-=12; y2+=1
    while mo2<1: mo2+=12; y2-=1
    return f"{y2:04d}-{mo2:02d}"
def corr(a,b):
    n=len(a); ma=st.mean(a); mb=st.mean(b)
    sa=math.sqrt(sum((x-ma)**2 for x in a)); sb=math.sqrt(sum((x-mb)**2 for x in b))
    return sum((x-ma)*(y-mb) for x,y in zip(a,b))/(sa*sb) if sa and sb else float('nan')
print(f"\nLEAD TEST (3-mo log-change, monthly-avg Indeed TOTAL postings vs JOLTS hires JTSHIL), sample {months[0]}..{months[-1]}:")
for k in range(-3,4):
    pairs=[(P[m],H[shift(m,k)]) for m in months if P.get(m) is not None and shift(m,k) in H and H[shift(m,k)] is not None]
    if len(pairs)>10: print(f"  postings lead hires by {k:+d} mo: r={corr([p for p,_ in pairs],[q for _,q in pairs]):+.2f}  n={len(pairs)}")
# same for NEW postings
if 'new postings' in nat:
    np_={}
    for d,v in nat['new postings'].items(): np_.setdefault(d[:7],[]).append(v)
    np_={m:st.mean(v) for m,v in np_.items()}
    PN={m:d3(np_,m) for m in months}
    print("NEW postings vs hires:")
    for k in range(-3,4):
        pairs=[(PN[m],H[shift(m,k)]) for m in months if PN.get(m) is not None and shift(m,k) in H and H[shift(m,k)] is not None]
        if len(pairs)>10: print(f"  new postings lead hires by {k:+d} mo: r={corr([p for p,_ in pairs],[q for _,q in pairs]):+.2f}  n={len(pairs)}")
print("\nlast 6 months monthly avg total postings:", [(m,round(mon[m],2)) for m in sorted(mon)[-6:]])
print("last 6 JOLTS hires:", [(m,hires[m]) for m in sorted(hires)[-6:]])
