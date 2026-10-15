import json, sys, math
import numpy as np
data=json.load(open(sys.argv[1]))
spy=data["SPY"]; cal=sorted(spy)
gov=["KSS","NWL","NCLH","AMC","JBLU"]; sens=["HTZ","WOOF","HLF","BALY"]
def prevday(d): i=cal.index(d); return cal[i-1]
# completeness vs SPY calendar
for t in gov+sens:
    miss=[d for d in cal if d not in data[t]]
    print("missing",t,miss)
def ret(t,d0,d1): return data[t][d1]/data[t][d0]-1
fit=[d for d in cal if "2026-03-02"<=d<="2026-09-23"]
res={}
for t in gov+sens:
    r=np.array([ret(t,prevday(d),d) for d in fit]); m=np.array([ret("SPY",prevday(d),d) for d in fit])
    beta=np.cov(r,m,ddof=1)[0,1]/np.var(m,ddof=1)
    e=r-beta*m; sig=e.std(ddof=1)
    res[t]=dict(beta=beta,sigma=sig,n=len(fit))
prim=["2026-10-02","2026-10-05","2026-10-06","2026-10-07","2026-10-08","2026-10-09","2026-10-13"]
sec=["2026-09-25","2026-09-28","2026-09-29","2026-09-30","2026-10-01"]
def z(t,d,two=False):
    if two and d=="2026-10-13":
        d0="2026-10-09"; k=math.sqrt(2)
    else:
        d0=prevday(d); k=1.0
    r=ret(t,d0,d); m=ret("SPY",d0,d)
    return r, m, (r-res[t]["beta"]*m)/(res[t]["sigma"]*k)
out={"fit":{t:{k:float(v) for k,v in res[t].items()} for t in res},"primary":{},"secondary":{},"oneday_1013":{}}
print("\nfit n=",len(fit), "window",fit[0],fit[-1])
for t in gov+sens: print(f"{t:5s} beta {res[t]['beta']:.3f} sigma {res[t]['sigma']*100:.3f}%")
for label,sess,two in (("primary",prim,True),("secondary",sec,False)):
    print(f"\n{label}: z (return, SPY)")
    for t in gov+sens:
        row=[]
        for d in sess:
            r,m,zz=z(t,d,two); row.append(zz); out[label].setdefault(t,{})[d]=dict(r=r,spy=m,z=zz)
        nw=sum(1 for x in row if x<=-1.0); nn=sum(1 for x in row if abs(x)<=0.3)
        print(f"{t:5s} "+" ".join(f"{x:+.2f}" for x in row)+f" | z<=-1: {nw}/{len(sess)}  |z|<=0.3: {nn}/{len(sess)}")
print("\n10/13 one-day alternative:")
for t in gov+sens:
    r,m,zz=z(t,"2026-10-13",False); out["oneday_1013"][t]=dict(r=r,spy=m,z=zz)
    r2,m2,z2=z(t,"2026-10-13",True)
    print(f"{t:5s} 1-day z {zz:+.2f} (r {r*100:+.2f}%)   2-day governing z {z2:+.2f} (r {r2*100:+.2f}%)")
print("SPY returns primary:", [round(ret('SPY',('2026-10-09' if d=='2026-10-13' else prevday(d)),d)*100,2) for d in prim])
json.dump(out,open(sys.argv[2],"w"),indent=1)
