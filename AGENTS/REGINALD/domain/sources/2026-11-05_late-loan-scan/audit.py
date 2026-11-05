"""Coverage audit of scan.py (one-time). Reads the Call Reports already cached; no new rule. Near-misses and total-level moves are labelled NOT the rule."""
import json, sys
sys.path.insert(0, "AGENTS/REGINALD/scripts")
import mi3_cohort_screen as m
J = json.load(open(sys.argv[1] + "/scan_raw.json"))
CL = {"construction":(["F172","F173"],["F158","F159"]),"1-4 family":(["5398","C236","C238"],["1797","5367","5368"]),"multifamily":(["3499"],["1460"]),"owner CRE":(["F178"],["F160"]),"non-owner CRE":(["F179"],["F161"]),"C&I":(["1606"],["1763","1764"])}
def val(d,c):
    for p in ("RCON","RCFD"):
        if p+c in d: return d[p+c]
def tot(d,cs):
    v=[val(d,c) for c in cs]
    return None if all(x is None for x in v) else sum(x or 0 for x in v)
over=[];nobook={};cov=[];nm=[]
for r in J["rows"]:
    rs=r["rssd"]; c=m.parse((m.CACHE/f"{rs}_9-30-2026.sdf").read_text(errors="replace")); p=m.parse((m.CACHE/f"{rs}_6-30-2026.sdf").read_text(errors="replace"))
    s=0
    for k,(q,b) in CL.items():
        qc,qp,bv=tot(c,q),tot(p,q),tot(c,b)
        if qc is None or qp is None or not bv:
            if (qc or 0)>0: nobook.setdefault(k,[]).append(r["name"])
            continue
        s+=qc; d=qc-qp
        if d>=15000 and (qp==0 or d/qp>=0.3) and qc/bv>=0.01 and not (d>=25000 and (qp==0 or d/qp>=.5) and qc/bv>=.02):
            nm.append((d,r["name"][:30],k,qp,qc,round(qc/bv*100,1),r["assets_m"]))
    t=r["t3089_c"] or 0
    if s>t*1.01+1: over.append((r["name"],t,s))
    cov.append((s,t))
print("class sum > total (a real tie failure):",over[:8],len(over))
print("share of total 30-89 in the six classes: %.1f%%"%(100*sum(a for a,b in cov)/sum(b for a,b in cov)))
print("classes with late dollars but no book figure:",{k:v[:5] for k,v in nobook.items()})
print("NEAR MISSES (NOT the rule: +$15M, +30%, 1% of book):")
for x in sorted(nm,reverse=True)[:12]: print("  %s | %s | %.1f -> %.1f | %s%% | assets $%s M"%(x[1],x[2],x[3]/1e3,x[4]/1e3,x[5],f"{x[6]:,}"))
print("TOTAL 30-89 +50% and +$50M (NOT the rule):")
for r in sorted(J["rows"],key=lambda r:-((r["t3089_c"] or 0)-(r["t3089_p"] or 0))):
    a,b=r["t3089_p"] or 0,r["t3089_c"] or 0
    if b-a>=50000 and (a==0 or (b-a)/a>=.5): print("  %s %.1f -> %.1f assets $%s M%s"%(r["name"][:32],a/1e3,b/1e3,f"{r['assets_m']:,}"," ACQ" if r["acq"] else ""))
print("acquirers:",[r["name"][:22] for r in J["rows"] if r["acq"]])
