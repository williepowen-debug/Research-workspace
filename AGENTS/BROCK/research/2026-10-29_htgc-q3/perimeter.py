"""Constant-perimeter check for HTGC software (BROCK 2026-10-29).
HTGC re-cut its SOI industry labels at 9/30 (new Cybersecurity, Healthcare Technology & Digital Health,
Financial Technologies, Energy Technologies buckets). This holds the 6/30 Application+System Software
issuer set fixed and reads those issuers at 9/30 whatever their new label.
usage: python3 -I perimeter.py <6/30 HTGC_recs.json> <9/30 HTGC_recs.json>   (recs from ../2026-10-23_bdc-software-exposure/scripts/soi.py)
"""
import json,re,sys,collections
SOFT=re.compile(r"(Application|System) Software")
def load(p): return [r for r in json.load(open(p)) if "Total" not in r["id"] and "InvestmentOwnedAtFairValue" in r]
def co(i):
    i=i.replace("&amp;","&")
    if i.count(",")>=2: i=i.split(",",2)[2]
    n=re.split(r" senior| equity| warrant| junior| unsecured| first lien| second lien",i.split(" | ")[0].lower())[0]
    return re.sub(r"[^a-z0-9 ]","",n).strip()[:30]
a,b=load(sys.argv[1]),load(sys.argv[2])
A={co(r["id"]) for r in a if r["ind"] and SOFT.fullmatch(r["ind"])}
B={co(r["id"]) for r in b if r["ind"] and SOFT.fullmatch(r["ind"])}
def agg(R,K): return (sum(r["InvestmentOwnedAtFairValue"] for r in R if co(r["id"]) in K)/1e6, sum(r.get("InvestmentOwnedAtCost",0) for r in R if co(r["id"]) in K)/1e6)
for lab,R,K in [("6/30 issuers @6/30",a,A),("6/30 issuers @9/30",b,A),("9/30-label issuers @9/30",b,B)]:
    f,c=agg(R,K); print(f"{lab}: n={len(K)} FV {f:.1f} cost {c:.1f} FV/cost {f/c:.4f}")
ia={}
for r in a: ia.setdefault(co(r["id"]),r["ind"])
mv=collections.defaultdict(float)
for r in b:
    k=co(r["id"])
    if k in ia and ia[k]!=r["ind"] and SOFT.fullmatch(ia[k] or ""): mv[(ia[k],r["ind"])]+=r["InvestmentOwnedAtFairValue"]
for (x,y),v in sorted(mv.items(),key=lambda z:-z[1]): print(f"relabelled out of software: {x} -> {y}: FV {v/1e6:.1f}M")
