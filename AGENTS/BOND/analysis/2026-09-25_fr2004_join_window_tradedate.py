# 2026-09-25 BOND: trade-date window variant (PRE<auction<=POST) of analysis/2026-09-25_fr2004_join_window_sensitivity.py; generated from it by string substitution. Output recorded in analysis/2026-09-25_rates-move-TP-columns_and_FR2004-timing-RESOLVED.md
import sys, copy, random, statistics as st, io, contextlib
sys.path.insert(0,"monitors"); sys.path.insert(0,"/home/willi/Research-workspace/FORGE/tools/market-data")
import fr2004_join as J
def join_strict(aucs, fr):
    asofs = sorted(fr)
    for a in aucs:
        pre=[d for d in asofs if d < a["date"]]; post=[d for d in asofs if d >= a["date"]]
        a["pre"]=pre[-1] if pre else None; a["post"]=post[0] if post else None
        if a["pre"] is None or a["post"] is None: a["d_long"]=a["d_1121"]=a["d_21"]=None; continue
        p,q=fr[a["pre"]],fr[a["post"]]
        a["d_long"]=q["LONG_END"]-p["LONG_END"]; a["d_1121"]=q["11-21Y"]-p["11-21Y"]; a["d_21"]=q[">21Y"]-p[">21Y"]
    return [a for a in aucs if a.get("d_long") is not None]
with contextlib.redirect_stdout(io.StringIO()):
    fr,_=J.fr2004_pooled(); aucs=J.auctions_with_iprime()
s=J.dgs30_series(); idx={d:i for i,(d,_) in enumerate(s)}
def fwd(ds,k):
    i=idx.get(ds); 
    return None if i is None or i+k>=len(s) else 100*(s[i+k][1]-s[i][1])
legs={"TOTAL>0":lambda a:a["d_long"]>0,"TOTAL>1B":lambda a:a["d_long"]>1.0,"11-21Y>0":lambda a:a["d_1121"]>0,">21Y>0":lambda a:a["d_21"]>0}
def perm(x,y,n=20000,seed=20260917):
    rng=random.Random(seed); obs=st.median(x)-st.median(y); pool=x+y; k=len(x); c=0
    for _ in range(n):
        rng.shuffle(pool)
        if abs(st.median(pool[:k])-st.median(pool[k:]))>=abs(obs)-1e-12: c+=1
    return obs,(c+1)/(n+1)
for name,jf in (("TRADE-DATE PRE<auction<=POST",join_strict),):
    j=jf(copy.deepcopy(aucs),fr)
    print(f"== {name}  n={len(j)}")
    for ln,leg in legs.items():
        P=[fwd(a["date"].isoformat(),5) for a in j if a["fired"] and leg(a)]
        U=[fwd(a["date"].isoformat(),5) for a in j if a["fired"] and not leg(a)]
        N=[fwd(a["date"].isoformat(),5) for a in j if not a["fired"]]
        P=[v for v in P if v is not None];U=[v for v in U if v is not None];N=[v for v in N if v is not None]
        d1,p1=perm(P,U); d2,p2=perm(P,N)
        print(f"   {ln:9} paired n={len(P):2} med {st.median(P):+5.1f} | unpaired n={len(U):2} med {st.median(U):+5.1f} | P-U {d1:+5.1f}bp p={p1:.3f} | P-nofire {d2:+5.1f}bp p={p2:.3f}")
