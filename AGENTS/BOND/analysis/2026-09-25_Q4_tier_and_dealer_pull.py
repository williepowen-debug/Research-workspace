# 2026-09-25 BOND, L477 Q4 (CCC isolated vs leading edge): ICE tier OAS on FRED (3-year window) + FR2004 dealer
# below-IG corporate inventory + DFII10. Run from AGENTS/BOND with the venv. Prints the tables used in
# analysis/2026-09-25_Q4_CCC-isolated-vs-leading-edge_BOND-side.md.
import sys, datetime as dt, statistics as st
sys.path.insert(0, "monitors"); sys.path.insert(0, "../../FORGE/tools/market-data")
import fetch, fr2004_fetch as F
def fred(s):
    return {dt.date.fromisoformat(o["date"]): float(o["value"]) for o in fetch.fred_fetch(s, limit=20000)
            if "error" not in o and o["value"] not in (".", "")}
T = {"CCC": "BAMLH0A3HYC", "B": "BAMLH0A2HYB", "BB": "BAMLH0A1HYBB", "HY": "BAMLH0A0HYM2", "BBB": "BAMLC0A4CBBB", "IG": "BAMLC0A0CM"}
X = {k: fred(v) for k, v in T.items()}
r = fred("DFII10")
D = sorted(set.intersection(*[set(x) for x in X.values()]))
last = D[-1]; print("ICE common span", D[0], "->", last, "n", len(D))
def prank(series, v): xs = sorted(series); return 100 * sum(x <= v for x in xs) / len(xs)
ref = [d for d in D if d <= dt.date(2026, 9, 10)][-1]
print(f"\n{'tier':5} {'level':>7} {'3y pct':>7} {'Δ since '+ref.isoformat():>18} {'2026 max':>9}")
for k in T:
    s = X[k]; v = s[last]*100
    print(f"{k:5} {v:7.0f} {prank([s[d] for d in D], s[last]):6.1f}% {100*(s[last]-s[ref]):+17.0f}bp {100*max(s[d] for d in D if d.year==2026):9.0f}")
for a, b in (("CCC", "B"), ("CCC", "BB"), ("B", "BB")):
    g = {d: 100*(X[a][d]-X[b][d]) for d in D}; gr = {d: X[a][d]/X[b][d] for d in D}
    print(f"{a}-{b}: gap {g[last]:.0f}bp (3y pct {prank(list(g.values()), g[last]):.1f}%, Δ since {ref} {g[last]-g[ref]:+.0f}bp) · ratio {gr[last]:.2f}x (3y pct {prank(list(gr.values()), gr[last]):.1f}%, was {gr[ref]:.2f}x)")
# beta of daily tier OAS changes to DFII10 changes: last 20 shared sessions vs the full 3y window
Dr = [d for d in D if d in r]
def beta(k, days):
    xs = [100*(r[days[i]]-r[days[i-1]]) for i in range(1, len(days))]; ys = [100*(X[k][days[i]]-X[k][days[i-1]]) for i in range(1, len(days))]
    mx, my = st.mean(xs), st.mean(ys); vx = sum((x-mx)**2 for x in xs)
    return sum((x-mx)*(y-my) for x, y in zip(xs, ys))/vx if vx else float("nan")
print(f"\nbeta of daily ΔOAS to daily ΔDFII10 (bp/bp): last 20 sessions to {Dr[-1]} vs full window")
for k in ("CCC", "B", "BB", "HY", "IG"):
    print(f"  {k:4} last20 {beta(k, Dr[-21:]):+.2f}   full {beta(k, Dr):+.2f}")
# dealer below-IG corporate inventory
keys = ["PDPOSCSBND-BELL13", "PDPOSCSBND-BELG13", "PDPOSCSBND-BELG5L10", "PDPOSCSBND-BELG10"]
ser = {}
for k in keys:
    m = {}
    for sb in ("SBN2022", "SBN2024"):
        try: m.update(F.fetch(k, sb))
        except Exception as e: print("  (no", k, sb, ")")
    ser[k] = {(d if isinstance(d, dt.date) else dt.date.fromisoformat(str(d))): float(v) for d, v in m.items()}
dd = sorted(set.intersection(*[set(s) for s in ser.values()]))
tot = {d: sum(ser[k][d] for k in keys) for d in dd}
unit = 1000.0 if max(abs(v) for v in tot.values()) > 1e4 else 1.0
print(f"\nFR2004 dealer BELOW-IG corporate inventory (net, $B), span {dd[0]} -> {dd[-1]}, n={len(dd)}")
for d in dd[-6:]:
    print(f"  as-of {d}: total {tot[d]/unit:6.2f}  " + "  ".join(f"{k.split('-')[1]} {ser[k][d]/unit:5.2f}" for k in keys))
lv = [tot[d]/unit for d in dd]; w4 = [(tot[dd[i]]-tot[dd[i-4]])/unit for i in range(4, len(dd))]
print(f"  level 3y-ish pct of latest: {prank(lv, lv[-1]):.1f}% (median {st.median(lv):.2f}, max {max(lv):.2f}) · 4-wk Δ latest {w4[-1]:+.2f} (pct {prank(w4, w4[-1]):.1f}%)")
# how unusual is the current 20-session beta? rolling 20-session beta distribution over the window
print("\nrolling 20-session beta to DFII10 — percentile of the latest window within all rolling windows")
for k in ("CCC", "B", "BB", "IG"):
    bs = [beta(k, Dr[i-20:i+1]) for i in range(20, len(Dr))]
    cur = bs[-1]
    print(f"  {k:4} latest {cur:+.2f}  pct {prank(bs, cur):5.1f}%  p10 {sorted(bs)[len(bs)//10]:+.2f}  p50 {st.median(bs):+.2f}  p90 {sorted(bs)[9*len(bs)//10]:+.2f}  n={len(bs)}")
