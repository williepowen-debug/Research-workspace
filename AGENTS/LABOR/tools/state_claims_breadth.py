#!/usr/bin/env python3
"""state_claims_breadth.py — LABOR L302 instrument (4): state initial-claims BREADTH from the ETA 539 primary.

Built 2026-09-17 (PROME commission DOCKET L302; promoted from the session scratchpad unchanged).
Input: ar539.csv from https://oui.doleta.gov/unemploy/csv/ar539.csv (13 MB; download first, path below).
Field c3 = state UI initial claims, NSA, by filing week (rptdate). Breadth = jurisdictions (50 + DC) whose
4-wk-avg NSA initial claims are UP vs the same 4 weeks a year earlier. DIAGNOSTIC ONLY -- not base-rated (BD-33).
Usage: cd "$(git rev-parse --show-toplevel)" && curl -sL -o /tmp/ar539.csv https://oui.doleta.gov/unemploy/csv/ar539.csv && .venv/bin/python3 AGENTS/LABOR/tools/state_claims_breadth.py /tmp/ar539.csv
"""
import sys
CSV = sys.argv[1] if len(sys.argv) > 1 else "ar539.csv"
import csv, collections, datetime as dt
rows=collections.defaultdict(dict)
with open(CSV) as f:
    r=csv.DictReader(f)
    for x in r:
        try: rows[x['st']][x['rptdate']]=int(x['c3'])
        except: pass
states=[s for s in rows if len(s)==2 and s not in ('PR','VI')]
latest='2026-09-05'
def wk(d,n): return (dt.date.fromisoformat(d)-dt.timedelta(weeks=n)).isoformat()
def avg4(s,end):
    v=[rows[s].get(wk(end,i)) for i in range(4)]
    return sum(v)/4 if all(x is not None for x in v) else None
yoy_end=wk(latest,52)
up4=up1=n=0; fl=None; tab=[]
for s in sorted(states):
    a=avg4(s,latest); b=avg4(s,yoy_end); l=rows[s].get(latest); ly=rows[s].get(yoy_end)
    if a is None or b is None or not l or not ly: continue
    n+=1
    yy4=(a/b-1)*100; yy1=(l/ly-1)*100
    up4+= yy4>0; up1+= yy1>0
    tab.append((s,l,ly,yy1,a,b,yy4))
print(f"states with data: {n}; latest week {latest}; yoy week {yoy_end}")
print(f"4wk-avg NSA IC UP YoY: {up4}/{n}   single-week UP YoY: {up1}/{n}")
tot=sum(t[1] for t in tab); toty=sum(t[2] for t in tab)
print(f"sum of states latest {tot:,} vs yr-ago {toty:,} => {(tot/toty-1)*100:+.1f}%")
print("\nWorst 10 by 4wk YoY:")
for t in sorted(tab,key=lambda t:-t[6])[:10]: print(f"  {t[0]} 4wk {t[4]:,.0f} vs {t[5]:,.0f} = {t[6]:+.1f}%  | wk {t[1]:,} vs {t[2]:,} = {t[3]:+.1f}%")
print("\nBest 10 (falling most):")
for t in sorted(tab,key=lambda t:t[6])[:10]: print(f"  {t[0]} 4wk {t[4]:,.0f} vs {t[5]:,.0f} = {t[6]:+.1f}%")
print("\nFL detail (NSA IC, last 8 weeks + yr-ago):")
for i in range(7,-1,-1):
    d=wk(latest,i); print(f"  {d}: {rows['FL'].get(d):,}  yr-ago {rows['FL'].get(wk(d,52)):,}")
for st in ['FL','TX','CA','NY','GA','WA']:
    t=[x for x in tab if x[0]==st][0]; print(f"  {st}: 4wk {t[4]:,.0f} vs {t[5]:,.0f} = {t[6]:+.1f}%")
# breadth history: for each of last 8 weeks, count states 4wk-avg up YoY
print("\nBreadth history (states 4wk-avg up YoY):")
for i in range(12,-1,-1):
    e=wk(latest,i); c=0;m=0
    for s in states:
        a=avg4(s,e); b=avg4(s,wk(e,52))
        if a and b: m+=1; c+= a>b
    print(f"  w/e {e}: {c}/{m}")
