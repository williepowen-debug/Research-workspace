#!/usr/bin/env python3
"""BRENT 11/5: BRT-31 week four inputs, and base rates for the new registrations. EIA v2 / FRED fallback via FORGE kit."""
import sys,json,datetime as dt,statistics as st,urllib.request,io,csv
sys.path.insert(0,'/home/willi/Research-workspace/FORGE/tools/market-data')
import fetch as F
def ser(sid,n=900):
    u=('https://api.eia.gov/v2/seriesid/PET.%s.W?api_key=%s&length=%d'%(sid,F.EIA_API_KEY,n))
    r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'research-client/1.0'}),timeout=40))
    return sorted((d['period'],float(d['value'])) for d in r['response']['data'] if d['value'] is not None)
g=ser('WGFUPUS2',900); print('WGFUPUS2 tail',g[-6:])
D=dict(g)
last=g[-1][0]; d0=dt.date.fromisoformat(last)
cur=[D[(d0-dt.timedelta(days=7*k)).isoformat()] for k in range(4)]
base=[D[(d0-dt.timedelta(days=364+7*k)).isoformat()] for k in range(4)]
print('week',last,'cur',cur,'base',base,'yoy%',(sum(cur)/sum(base)-1)*100)
dist=ser('WDISTUS1',1200); print('WDISTUS1 tail',dist[-3:])
DD={dt.date.fromisoformat(a):b for a,b in dist}
res=[]
for y in sorted({k.year for k in DD}):
    s=[k for k in DD if k.year==y and k.month==10 and k.day>=27 or (k.year==y and k.month==11 and k.day<=2)]
    if not s or y==2026: continue
    a=s[-1]; path=[DD.get(a+dt.timedelta(days=7*i)) for i in range(1,8)]
    if None in path: continue
    res.append((y,DD[a],round(min(path)-DD[a],3),round(path[-1]-DD[a],3)))
print('distillate y,start,min chg wk1-7,chg wk7'); [print(r) for r in res]
need=95.0-dist[-1][1]; print('need',need,'P(min<=need)',sum(r[2]<=need for r in res),len(res))
try:
    url='https://fred.stlouisfed.org/graph/fredgraph.csv?id=GASREGW'
    t=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'research-client/1.0'}),timeout=40).read().decode()
    rows=[(dt.date.fromisoformat(r['observation_date'] if 'observation_date' in r else r['DATE']),float(r['GASREGW'])) for r in csv.DictReader(io.StringIO(t)) if r['GASREGW'] not in('.','')]
    G=dict(rows); print('GASREGW tail',rows[-3:])
    out=[]
    for y in range(2000,2026):
        s=[k for k in G if k.year==y and k.month==11 and k.day<=7]
        if not s: continue
        a=s[0]; path=[G.get(a+dt.timedelta(days=7*i)) for i in range(1,7)]
        if None in path: continue
        out.append((y,G[a],round(min(path)/G[a]-1,4)))
    print('gas y,start,min pct wk1-6',out)
    print('need pct',4.0/rows[-1][1]-1,'count',sum(o[2]<=4.0/rows[-1][1]-1 for o in out),len(out))
except Exception as e: print('FRED fail',e)
