"""WQ-291 (Will 2026-09-26 15:04 ET): base rates behind BOND's EXACT proposed dealer-stock
leg for the September-4 paired kill on a 5Y I' fire. Reproducible; re-run to re-derive.

Population: every 5Y NOMINAL auction in the corpus with an FR2004 PRE and POST on the
trade-date window (WQ-290: PRE = last as-of STRICTLY BEFORE auction, POST = first as-of
ON OR AFTER). Buckets: 3-6Y (PDPOSGSC-G3L6), 6-7Y (G6L7), long-end TOTAL (7-11+11-21+>21).
Also: all-weeks 3-6Y w/w distribution (contrast), I'-fire subset, dealer-$ vs 3-6Y link.
Usage: ../../.venv/bin/python3 analysis/2026-09-26_WQ-291_kill-rule_base-rates.py
"""
import sys, datetime as dt, statistics as st
sys.path.insert(0, "monitors")
import fr2004_fetch as FR, fr2004_join as J

def pct(xs, q):  # same nearest-rank-floor rule as the FORUM-7 series script
    xs = sorted(xs); return xs[min(len(xs) - 1, int(q * len(xs)))]

def pooled(keyid):
    m = {}
    for sb, s, e in J.all_breaks():
        if e < J.BREAK_START: continue
        try: m.update(FR.fetch(keyid, sb))
        except SystemExit: pass
    return {dt.date.fromisoformat(str(k)): float(v) for k, v in m.items()}

fr, counts = J.fr2004_pooled()
g36, g67 = pooled("PDPOSGSC-G3L6"), pooled("PDPOSGSC-G6L7")
asofs = sorted(d for d in fr if d in g36 and d in g67)
print("FR2004 as-of span", asofs[0], "->", asofs[-1], "n", len(asofs), "breaks", counts)

aucs = [a for a in J.auctions_with_iprime() if a["term"].startswith("5-Year")]
import grade_auction as GA
recs = {r["cusip"] + r["date"]: r for r in GA.load()}
rows = []
for a in aucs:
    pre = [d for d in asofs if d < a["date"]]; post = [d for d in asofs if d >= a["date"]]
    if not pre or not post: continue
    p, q = pre[-1], post[0]
    rows.append(dict(date=a["date"], fired=a["fired"], old=a["old_fired"], dlr=a["dlr"],
        pre=p, post=q, d36=g36[q] - g36[p], d67=g67[q] - g67[p],
        dlong=fr[q]["LONG_END"] - fr[p]["LONG_END"]))
n = len(rows)
d36 = [r["d36"] for r in rows]; dl = [r["dlong"] for r in rows]
print(f"\n5Y auctions joined n={n}  span {rows[0]['date']} -> {rows[-1]['date']}")
print(f"3-6Y delta: median {st.median(d36):+.2f}  p75 {pct(d36,.75):+.2f}  p90 {pct(d36,.90):+.2f}  max {max(d36):+.2f}  min {min(d36):+.2f}")
print(f"  share >0 {sum(x>0 for x in d36)}/{n}  >1 {sum(x>1 for x in d36)}/{n}  >=8.6 {sum(x>=8.6 for x in d36)}/{n}")
print(f"LONG-END delta on 5Y weeks: median {st.median(dl):+.2f}  share >0 {sum(x>0 for x in dl)}/{n}  >1 {sum(x>1 for x in dl)}/{n}  >=6.4 {sum(x>=6.4 for x in dl)}/{n}")
# conflict table on 5Y weeks: 3-6Y STRESS vs long-end >1
for a36 in (True, False):
    for al in (True, False):
        k = sum(((r["d36"] >= 8.6) == a36) and ((r["dlong"] > 1) == al) for r in rows)
        print(f"  3-6Y>=8.6 {a36!s:5}  long>1 {al!s:5}: {k}")
# all-weeks 3-6Y w/w
ww = [g36[asofs[i]] - g36[asofs[i-1]] for i in range(1, len(asofs))]
print(f"\nALL weeks 3-6Y w/w n={len(ww)}: median {st.median(ww):+.2f} p90 {pct(ww,.9):+.2f}  share >=8.6 {sum(x>=8.6 for x in ww)}/{len(ww)}")
non5 = set(r["post"] for r in rows)
wn = [g36[asofs[i]] - g36[asofs[i-1]] for i in range(1, len(asofs)) if asofs[i] not in non5]
print(f"NON-5Y weeks 3-6Y w/w n={len(wn)}: median {st.median(wn):+.2f} p90 {pct(wn,.9):+.2f}  share >=8.6 {sum(x>=8.6 for x in wn)}/{len(wn)}")
# dealer take (pct of competitive) vs 3-6Y build: does the bucket see the award?
xs = [r["dlr"] for r in rows]; ys = d36
mx, my = st.mean(xs), st.mean(ys)
cov = sum((x-mx)*(y-my) for x, y in zip(xs, ys)); r_ = cov / (sum((x-mx)**2 for x in xs)**.5 * sum((y-my)**2 for y in ys)**.5)
print(f"\ncorr(dealer % of competitive, 3-6Y delta) over n={n}: r={r_:+.2f}")
top = sorted(rows, key=lambda r: -r["dlr"])[:9]
print("  top-quintile dealer-take auctions: 3-6Y median", f"{st.median([r['d36'] for r in top]):+.2f}", "vs rest", f"{st.median([r['d36'] for r in rows if r not in top]):+.2f}")
print("\nI' 5Y fires:", sum(r["fired"] for r in rows), " of which 3-6Y>=8.6:", sum(r["fired"] and r["d36"]>=8.6 for r in rows),
      " long>0:", sum(r["fired"] and r["dlong"]>0 for r in rows), " long>1:", sum(r["fired"] and r["dlong"]>1 for r in rows))
print("OLD-conjunctive 5Y fires:", [(str(r["date"]), round(r["d36"],2), round(r["dlong"],2)) for r in rows if r["old"]])
print("\nweekday of 5Y auctions:", {w: sum(r['date'].weekday()==w for r in rows) for w in range(5)})
print("last 6 rows:"); [print(" ", r["date"], r["pre"], r["post"], f"d36 {r['d36']:+.2f} d67 {r['d67']:+.2f} dlong {r['dlong']:+.2f} dlr {r['dlr']:.2f} fired {r['fired']}") for r in rows[-6:]]

# ---- extension (same run): dealer DOLLARS, full-corpus 5Y population, fire subsets
import csv
csvrows = {r["auction_date"]: r for r in csv.DictReader(open("data/auction_history_v2_prome-spawned.csv"))
           if r["tenor"] == "5Y" and r["is_tips"] in ("False", "false", "0", "")}
def dlr_bn(d):
    r = csvrows.get(d.isoformat()); return float(r["primary_dealer_accepted"]) / 1e9 if r else None
xs2 = [(dlr_bn(r["date"]), r["d36"]) for r in rows if dlr_bn(r["date"]) is not None]
mx, my = st.mean(x for x, _ in xs2), st.mean(y for _, y in xs2)
c = sum((x-mx)*(y-my) for x, y in xs2); rr = c / (sum((x-mx)**2 for x, _ in xs2)**.5 * sum((y-my)**2 for _, y in xs2)**.5)
print(f"\ncorr(dealer $B awarded, 3-6Y delta) n={len(xs2)}: r={rr:+.2f}; dealer $B median {st.median(x for x,_ in xs2):.1f}")
print("I' fires 3-6Y>0:", sum(r["fired"] and r["d36"]>0 for r in rows), "/", sum(r["fired"] for r in rows),
      "| I' fire rows:", [(str(r["date"]), round(r["d36"],1), round(r["dlong"],1)) for r in rows if r["fired"]])
# full-corpus 5Y population (no trailing-12 bench requirement) -> the FORUM-7 '44'
alld = sorted(dt.date.fromisoformat(d) for d in csvrows)
full = []
for d in alld:
    pre = [x for x in asofs if x < d]; post = [x for x in asofs if x >= d]
    if pre and post: full.append((d, g36[post[0]] - g36[pre[-1]], fr[post[0]]["LONG_END"] - fr[pre[-1]]["LONG_END"]))
f36 = [x[1] for x in full]; fl = [x[2] for x in full]
print(f"FULL-corpus 5Y n={len(full)} span {full[0][0]}->{full[-1][0]}: 3-6Y median {st.median(f36):+.2f} p90 {pct(f36,.9):+.2f} share>0 {sum(x>0 for x in f36)}/{len(full)} >=8.6 {sum(x>=8.6 for x in f36)}/{len(full)}")
print(f"  long-end on those weeks: >0 {sum(x>0 for x in fl)}/{len(full)} >1 {sum(x>1 for x in fl)}/{len(full)}")
print("  2x2 (3-6Y>=8.6, long>1):", {(a,b): sum(((x[1]>=8.6)==a) and ((x[2]>1)==b) for x in full) for a in (True,False) for b in (True,False)})
print("9/16 levels: 3-6Y", g36.get(dt.date(2026,9,16)), " 6-7Y", g67.get(dt.date(2026,9,16)), " long", round(fr[dt.date(2026,9,16)]["LONG_END"],2))
# weekday split on the full 44: a WEDNESDAY auction's POST is the award day itself (no distribution time)
for lab, sel in (("Wed", lambda d: d.weekday() == 2), ("Mon/Tue", lambda d: d.weekday() in (0, 1))):
    s = [x[1] for x in full if sel(x[0])]
    print(f"  {lab}: n={len(s)} 3-6Y median {st.median(s):+.2f} p90 {pct(s,.9):+.2f} >=8.6 {sum(v>=8.6 for v in s)}")
