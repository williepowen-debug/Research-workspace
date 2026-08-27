import json,subprocess,sys,datetime as dt,statistics as st
from pathlib import Path
ROOT=Path("/home/willi/Research-workspace"); FETCH=ROOT/"FORGE/tools/market-data/fetch.py"
def hist(t):
    out=subprocess.run([sys.executable,str(FETCH),"price",t,"--history","200","--json"],capture_output=True,text=True,timeout=240,cwd=ROOT).stdout
    d=json.loads(out)
    def f(o):
        if isinstance(o,dict):
            for k,v in o.items():
                if k=="history" and isinstance(v,list): return v
                r=f(v)
                if r is not None: return r
        if isinstance(o,list):
            for v in o:
                r=f(v)
                if r is not None: return r
    return {r["date"]:r["close"] for r in f(d)}
names=["VLO","CVI","MPC","DINO","PSX"]; D={t:hist(t) for t in names+["XLE"]}
X=D["XLE"]; ds=sorted(set(X)&set.intersection(*[set(D[t]) for t in names]))
WAR="2026-02-27"
def spread_cal30(t):
    out=[]
    for i,d1 in enumerate(ds):
        tgt=(dt.date.fromisoformat(d1)-dt.timedelta(days=30)).isoformat()
        prior=[d for d in ds[:i+1] if d>=tgt]
        if not prior or prior[0]==d1: continue
        d0=prior[0]
        out.append((d1,(D[t][d1]/D[t][d0]-1)*100-(X[d1]/X[d0]-1)*100))
    return out
print("BASIS = 30 CALENDAR DAYS (matches BRENT's table)\n")
res={}
for t in names:
    s=[(d,v) for d,v in spread_cal30(t) if d>=WAR]
    v=[x for _,x in s]; cur=s[-1]; q=sorted(v)
    pc=lambda p:q[max(0,min(len(q)-1,int(round(p/100*(len(q)-1)))))]
    below=sum(1 for x in v if x<=cur[1])/len(v)*100
    res[t]=(cur[1],below)
    print(f"{t}: n={len(v)} ({s[0][0]}..{s[-1][0]})  mean {st.mean(v):+6.2f}  median {st.median(v):+6.2f}  sd {st.pstdev(v):5.2f}")
    print(f"    p05 {pc(5):+6.2f} p25 {pc(25):+6.2f} p50 {pc(50):+6.2f} p75 {pc(75):+6.2f} p95 {pc(95):+6.2f}   min {min(v):+6.2f} max {max(v):+6.2f}")
    print(f"    TODAY {cur[1]:+6.2f}pp  ->  percentile {below:5.1f}%\n")
SUB=[("2/27-3/31","2026-02-27","2026-03-31"),("4/01-5/31","2026-04-01","2026-05-31"),
     ("6/01-7/15","2026-06-01","2026-07-15"),("7/16-8/17","2026-07-16","2026-08-17"),
     ("8/18-now","2026-08-18","2026-12-31")]
print("SUB-REGIME OVERLAY (VLO, cal-30d):")
s=spread_cal30("VLO")
for lab,a,b in SUB:
    v=[x for d,x in s if a<=d<=b]
    if v: print(f"  {lab}: n={len(v):3d}  mean {st.mean(v):+6.2f}  median {st.median(v):+6.2f}  min {min(v):+6.2f}  max {max(v):+6.2f}")
