# 2026-09-25 FORUM-7 BOND legs: FR2004 3-6Y / 6-7Y / long-end series pull (SBN2022+SBN2024). The F1/F2 percentiles were computed inline from its JSON output; method stated in analysis/2026-09-25_FORUM-7_BOND-legs-PREREG.md.
import sys, csv, datetime as dt, statistics as st
sys.path.insert(0,"monitors"); import fr2004_fetch as F
def pct(xs,q): xs=sorted(xs); return xs[min(len(xs)-1,int(q*len(xs)))]
ser={}
for k in ("PDPOSGSC-G3L6","PDPOSGSC-G6L7","PDPOSGSC-G7L11","PDPOSGSC-G11L21","PDPOSGSC-G21"):
    m={}
    for sb in ("SBN2022","SBN2024"):
        m.update(F.fetch(k,sb))
    ser[k]={ (d if isinstance(d,dt.date) else dt.date.fromisoformat(str(d))):float(v)/1000 if float(v)>1e4 else float(v) for d,v in m.items()}
dates=sorted(set.intersection(*[set(s) for s in ser.values()]))
print("as-of span",dates[0],dates[-1],"n",len(dates), "sample 9/16 G3L6:",ser["PDPOSGSC-G3L6"].get(dt.date(2026,9,16)))
LE=("PDPOSGSC-G7L11","PDPOSGSC-G11L21","PDPOSGSC-G21")
tot={d:sum(ser[k][d] for k in LE) for d in dates}
print("check long-end 9/16 =",round(tot.get(dt.date(2026,9,16),float('nan')),3))
auc=[]
for r in csv.DictReader(open("data/auction_history_v2_prome-spawned.csv")):
    auc.append(r)
print("cols:",list(auc[0].keys())[:12])
import json; json.dump({"dates":[d.isoformat() for d in dates],"g36":{d.isoformat():ser["PDPOSGSC-G3L6"][d] for d in dates},"g67":{d.isoformat():ser["PDPOSGSC-G6L7"][d] for d in dates},"tot":{d.isoformat():tot[d] for d in dates}},open(sys.argv[1],"w"))
