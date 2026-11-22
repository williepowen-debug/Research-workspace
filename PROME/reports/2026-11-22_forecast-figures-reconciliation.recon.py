import sys, collections, random
sys.path.insert(0,'PROME/tools')
import forecast_report as F
bucket=F.load_bucket(); rows,defects=F.read_all(bucket); rec=F.git_records(bucket)
dec=[r for r in rows if r["bucket"] in ("HIT","MISS")]; sc=[r for r in dec if r["p"] is not None]
T=[(r,F.timing(rec.get((r["desk"],r["id"]),[]),r["p"],r.get("resolved"),r["outcome"])) for r in sc]
print("scored",len(sc),"decided",len(dec))
print("class, whole population:",collections.Counter(t["cls"] for r,t in T))
fwd=[(r,t) for r,t in T if t["known"] is None or t["known"]>F.REPORT1_CUT]
print("closed pop",len(T)-len(fwd),collections.Counter(t["cls"] for r,t in T if not(t["known"] is None or t["known"]>F.REPORT1_CUT)))
def stats(S,label):
    n=len(S); hit=lambda r: r["bucket"]=="HIT"
    hr=sum(hit(r) for r,t in S)/n; ref=hr*(1-hr)
    b=sum((r["p"]-hit(r))**2 for r,t in S)/n
    b0=sum((t["p0"]-hit(r))**2 for r,t in S)/n
    rev=sum(1 for r,t in S if abs(t["p0"]-r["p"])>1e-9)
    print(f"{label}: n={n} hit={hr:.3f} ref={ref:.4f} brier={b:.4f} first={b0:.4f} gain={ref-b:+.4f} first-gain={ref-b0:+.4f} revised={rev}")
both=[(r,t) for r,t in T if t["p0"] is not None]
stats(both,"all")
nb=[(r,t) for r,t in both if t["cls"]!="BORN-DECIDED"]
stats(nb,"excluding born-decided")
stats([(r,t) for r,t in both if t["cls"]=="BEFORE"],"BEFORE only")
# bootstrap for first-logged gain, independent
rng=random.Random(619); d=[]
for _ in range(2000):
    bs=[both[rng.randrange(len(both))] for _ in both]
    h=sum(r["bucket"]=="HIT" for r,t in bs)/len(bs)
    d.append(h*(1-h)-sum((t["p0"]-(r["bucket"]=="HIT"))**2 for r,t in bs)/len(bs))
d.sort(); print("first-logged gain bootstrap 95%%: %+.3f to %+.3f"%(d[50],d[1949]))
# cluster bootstrap by desk for scored gain
bydesk=collections.defaultdict(list)
for r in sc: bydesk[r["desk"]].append(r)
desks=list(bydesk); d=[]
for _ in range(2000):
    bs=[r for k in (desks[rng.randrange(len(desks))] for _ in desks) for r in bydesk[k]]
    h=sum(r["bucket"]=="HIT" for r in bs)/len(bs)
    d.append(h*(1-h)-sum((r["p"]-(r["bucket"]=="HIT"))**2 for r in bs)/len(bs))
d.sort(); print("scored gain, resampling whole desks (%d desks): %+.3f to %+.3f"%(len(desks),d[50],d[1949]))
print("desks by n:",sorted(((len(v),k) for k,v in bydesk.items()),reverse=True)[:8])
