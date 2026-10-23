import json,re,collections
from metrics import name, CUT, SP
marks=collections.defaultdict(dict)
for t in CUT:
    R=json.load(open(f"{SP}/{t}_recs.json"))
    P=[r for r in R if r["ord"]<=CUT[t] and "InvestmentOwnedAtFairValue" in r and not re.search(r"\bTotal\b",r["id"])]
    if t=="FSK": P=[r for r in P if " | " in r["id"]]
    agg=collections.defaultdict(lambda:[0,0,False])
    for r in P:
        p=r.get("InvestmentOwnedBalancePrincipalAmount",0)
        if p and p>0 and r.get("par_unit")=="usd":
            k=name(t,r["id"]); a=agg[k]; a[0]+=p; a[1]+=r["InvestmentOwnedAtFairValue"]; a[2]=a[2] or r["soft"]
    for k,(p,f,s) in agg.items():
        if p>2e6: marks[k][t]=(f/p,p/1e6,s)
common={k:v for k,v in marks.items() if len(v)>=2 and any(x[2] for x in v.values())}
print("software names held by >=2 of 6:",len(common))
# pairwise: for each BDC, average (own mark - mean of others) on common software names, par-weighted
dev=collections.defaultdict(lambda:[0,0,0])
for k,v in common.items():
    for t,(m,p,s) in v.items():
        others=[x[0] for u,x in v.items() if u!=t]
        d=m-sum(others)/len(others)
        dev[t][0]+=d*p; dev[t][1]+=p; dev[t][2]+=1
for t,(a,b,n) in sorted(dev.items()):
    print(f"  {t}: par-wtd mark minus peers' mark on shared software names = {100*a/b:+.2f} pts (n={n} names, ${b:.0f}M par)")
low=[(min(x[0] for x in v.values()),k,{t:round(x[0],3) for t,x in v.items()}) for k,v in common.items()]
for m,k,d in sorted(low)[:14]:
    spread=max(d.values())-min(d.values())
    print(f"  {k}: {d} spread {100*spread:.1f}pts")
