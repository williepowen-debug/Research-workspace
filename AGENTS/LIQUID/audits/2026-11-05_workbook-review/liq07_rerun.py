"""LIQ-07 trigger legs on every published obs, 9/24..11/4, plus funding legs around the late-October run. Read-only; no re-grade."""
import sys
sys.path.insert(0,'FORGE/tools/market-data')
from fetch import fred_fetch
def s(i,n=70): return {r['date']:round(float(r['value'])*100) for r in fred_fetch(i,limit=n) if r.get('value') not in('.','',None)}
B,C,BB,BBB,IG=[s(x) for x in ['BAMLH0A2HYB','BAMLH0A3HYC','BAMLH0A1HYBB','BAMLC0A4CBBB','BAMLC0A0CM']]
ds=sorted(set(B)&set(C)&set(BB)&set(BBB)&set(IG))
rows=[]
for i,d in enumerate(ds):
    if i<15 or d<'2026-09-24': continue
    p=ds[i-15]
    rows.append((d,B[d]-B[p],C[d]-C[p],BB[d]-BB[p],BBB[d]-BBB[p],IG[d]-IG[p]))
run=0
print('date       B15 CCC15 BB15 BBB15 IG15 trig run')
for r in rows:
    hit=r[1]>=28 and r[2]>=0
    run=run+1 if hit else 0
    print(r[0],f'{r[1]:>4}{r[2]:>6}{r[3]:>5}{r[4]:>6}{r[5]:>5}','Y' if hit else '.',f'{run:>3}')
