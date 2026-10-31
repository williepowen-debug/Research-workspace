"""Apply the FROZEN rule's universe + merger handling to the 10/31 FFIEC short-list pull (cache only, no network).
Frozen rule: reports/2026-10-28_borrowing-screen_FROZEN_rule.md (sha256 90e0a4a2...948a).
Universe = small commercial (dry-run TSV small==True, i.e. ex-25 largest by 6/30 assets). Probable acquirer = assets +>=20% in the quarter
-> excluded from flags and aggregate, listed separately. Flag = dbor >= $100M and (prior 0 or >=25%) and deposits down."""
import csv, os, sys
R0 = "/home/willi/Research-workspace"
sys.path.insert(0, R0 + "/AGENTS/REGINALD/scripts")
import mi3_cohort_screen as m, borrowing_screen as bs, borrowing_shortlist_ffiec as sl
R = list(csv.DictReader(open(sl.DRY), delimiter="\t")); F = lambda r, k: float(r[k])
by = {int(r["rssd"]): r for r in R if r["rssd"] not in ("", "None")}
small = [r for r in R if r["small"] == "True" and r["merger"] == "False"]
flagged = [r for r in small if F(r,"dbor") >= bs.FLAG_MIN_K and (F(r,"bor_p")==0 or F(r,"dbor")/F(r,"bor_p") >= bs.FLAG_MIN_PCT) and F(r,"ddep") < 0]
top20 = sorted((r for r in small if F(r,"dbor") > 0), key=lambda r: -F(r,"dbor"))[:20]
big100 = sorted(small, key=lambda r: -F(r,"asset"))[:100]
src = {}
for rs in bs.COHORT_RSSD: src.setdefault(rs, set()).add("cohort")
for g, t in ((flagged,"Q2-flag"),(top20,"Q2-top20"),(big100,"top100-assets")):
    for r in g: src.setdefault(int(r["rssd"]), set()).add(t)
rows = []; pend = []
for rs, tags in src.items():
    r = by[rs]; p = m.CACHE / f"{rs}_9-30-2026.sdf"
    if not p.exists(): pend.append((rs, r["name"])); continue
    x = sl.extract(m.parse(p.read_text(errors="replace")))
    bp = F(r,"bor_c"); dp = F(r,"dep_p")+F(r,"ddep"); ap = F(r,"asset")
    db = x["bor"]-bp; dd = x["dep"]-dp; ag = x["asset"]/ap-1
    acq = ag >= 0.20
    fl = db >= bs.FLAG_MIN_K and (bp==0 or db/bp >= bs.FLAG_MIN_PCT) and dd < 0
    rows.append(dict(rssd=rs, name=r["name"], st=r["state"], small=r["small"]=="True", cls=r["cls"], tags=",".join(sorted(tags)),
                     ap=ap, a=x["asset"], ag=ag, bp=bp, b=x["bor"], db=db, dd=dd, acq=acq, flag=fl and r["small"]=="True" and not acq,
                     fhlb=x["fhlb"], bro=x["bro"], brop=F(r,"dbro") if r["dbro"] not in ("","None") else None))
U = [r for r in rows if r["small"] and not r["acq"]]
A = [r for r in rows if r["small"] and r["acq"]]
L = [r for r in rows if not r["small"]]
f = lambda v: f"{v/1e6:+.2f}"
print(f"filed {len(rows)} pending {len(pend)}: {pend}")
print(f"SMALL ex-acquirers n={len(U)}: borrowings net {f(sum(r['db'] for r in U))} $B, gross up {f(sum(max(r['db'],0) for r in U))}, gross down {f(sum(min(r['db'],0) for r in U))}; deposits net {f(sum(r['dd'] for r in U))} $B")
ups = sorted((r['db'] for r in U if r['db']>0), reverse=True)
print(f"  top-10 share of gross increases within the LIST (not the frozen universe measure): {sum(ups[:10])/sum(ups)*100:.1f}% of {len(ups)} increasers")
print(f"PROBABLE ACQUIRERS (assets >=+20%) n={len(A)}:")
for r in A: print(f"  {r['name']} {r['st']} assets {r['ap']/1e6:.1f}->{r['a']/1e6:.1f} $B ({r['ag']*100:+.0f}%), bor {f(r['db'])}, dep {f(r['dd'])} $B, tags {r['tags']}")
print(f"LARGE (not in small universe; cohort context) n={len(L)}: borrowings net {f(sum(r['db'] for r in L))}, deposits net {f(sum(r['dd'] for r in L))}")
for r in L: print(f"  {r['name']} bor {r['bp']/1e6:.2f}->{r['b']/1e6:.2f} ({r['db']/1e3:+,.0f}M) dep {r['dd']/1e3:+,.0f}M assets {r['ag']*100:+.1f}% tags {r['tags']}")
print("FLAGS (small, ex-acquirers, frozen rule):")
for r in sorted(U, key=lambda r:-r['db']):
    if r['flag']: print(f"  {r['name']} {r['st']} rssd {r['rssd']} assets {r['a']/1e6:.1f}B ({r['ag']*100:+.1f}%), bor {r['bp']/1e6:.2f}->{r['b']/1e6:.2f} ({r['db']/1e3:+,.0f}M, {r['db']/r['bp']*100 if r['bp'] else float('inf'):+.0f}%), dep {r['dd']/1e3:+,.0f}M, FHLB {r['fhlb']/1e6:.2f}B, brokered 9/30 {(r['bro'] or 0)/1e6:.2f}B tags {r['tags']}")
print("COHORT (all 14):")
for r in rows:
    if "cohort" in r["tags"]: print(f"  {r['name']} small={r['small']} bor {r['bp']/1e6:.2f}->{r['b']/1e6:.2f} ({r['db']/1e3:+,.0f}M) dep {r['dd']/1e3:+,.0f}M FHLB {r['fhlb']/1e6:.2f} bro {(r['bro'] or 0)/1e6:.2f}")
# 10/28 subset comparison: the 28 banks filed by 10/28 (names from that file)
print("---- reconciliation & 10/28 comparison")
web = by[761806]; wb = F(web,"bor_c"); wd = F(web,"dep_p")+F(web,"ddep"); wa = F(web,"asset")
san = [r for r in rows if r["rssd"]==722777][0]
print(f"Santander+Webster pro forma: assets {(san['ap']+wa)/1e6:.1f}->{san['a']/1e6:.1f} ({(san['a']/(san['ap']+wa)-1)*100:+.1f}%), bor {(san['bp']+wb)/1e6:.2f}->{san['b']/1e6:.2f} ({(san['b']-san['bp']-wb)/1e6:+.2f}B), dep {(san['dd']-wd)/1e6:+.2f}B")
sm = [r for r in rows if r["small"]]
tot = sum(r["db"] for r in sm) - wb
print(f"List small incl acquirers, Webster prior netted: borrowings {tot/1e6:+.2f} $B (H.8 NSA small 7/1->9/30 +4.3B; list = 75% of Q2 small-bank borrowings)")
unf = [by[x] for x in (197478,413208,980661,782306)]
print("unfiled 6/30 borrowings:", {r['name']: round(F(r,'bor_c')/1e6,2) for r in unf})
import re
old = open(R0+"/AGENTS/REGINALD/domain/sources/2026-10-28_boot/borrowing_shortlist/borrowing_shortlist_Q3.md").read()
O = {}
for ln in old.splitlines():
    c = [x.strip() for x in ln.split("|")]
    if len(c) > 10 and c[1] not in ("Bank","---"):
        O[c[1]] = (int(c[6].replace(",","").replace("+","")), int(c[7].replace(",","").replace("+","")))
nm = {r["name"]: r for r in rows}
diff = [(k, v, (round(nm[k]["db"]/1e3), round(nm[k]["dd"]/1e3))) for k, v in O.items() if k in nm and (abs(v[0]-nm[k]["db"]/1e3)>1 or abs(v[1]-nm[k]["dd"]/1e3)>1)]
print(f"10/28 rows {len(O)}; matched now {sum(k in nm for k in O)}; changed {diff}")
s28 = sum(nm[k]["db"] for k in O if k in nm); r103 = [r for r in rows if r["name"] not in O]
print(f"same 28 now: bor {s28/1e6:+.2f}B; the 106 newly filed: bor {sum(r['db'] for r in r103)/1e6:+.2f}B dep {sum(r['dd'] for r in r103)/1e6:+.2f}B (raw, incl acquirers and 3 large cohort)")
