#!/usr/bin/env python3
"""Reproduce every figure in research/2026-09-30_CASE_LEDGER_PATTERNS.md from Will's workbook v3 (read-only).

Comparable PRICE set: Event Type in {Property sale, Property sale / CMBS liquidation}; numeric disposition AND benchmark;
USD; not a duplicate or excluded summary. 'Sourced' = has Source URL 1. 'Verified benchmark' = Benchmark Type exactly
'Prior purchase' (the workbook's own label; '(unverified)' rows excluded). Discount = the workbook's cached column F
(1 - price / benchmark): a PRICE change versus an earlier mark, never a loan loss.
Run: .venv/bin/python3 AGENTS/CREED/scripts/workbook_patterns.py
"""
import math, pathlib, statistics as st
import openpyxl

SRC = pathlib.Path(__file__).resolve().parents[1] / "cases" / "sources" / "2026-09-30_will_CRE_Loss_Sales_v3.xlsx"
wb = openpyxl.load_workbook(SRC, data_only=True)
R = list(wb["CRE Distress Sales"].iter_rows(values_only=True))
H = R[0]
X = [dict(zip(H, r)) for r in R[1:] if any(r)]
num = lambda v: v if isinstance(v, (int, float)) and not isinstance(v, bool) else None
P = [x for x in X if num(x["Disposition Amount ($M)"]) and num(x["Benchmark Amount ($M)"])
     and x["Event Type"] in ("Property sale", "Property sale / CMBS liquidation")
     and "uplicate" not in str(x["Event Status"]) and "xcluded" not in str(x["Event Status"]) and x["Currency"] == "USD"]
d = lambda x: x["Discount to Benchmark (%)"]
src = lambda x: bool(x["Source URL 1"])


def med(L):
    return f"{round(st.median(L) * 100)}% (n={len(L)})" if L else "n=0"


def rank(a):
    s = sorted(a)
    return [s.index(v) + (s.count(v) - 1) / 2 for v in a]


def spearman(a, b):
    ra, rb = rank(a), rank(b)
    ma, mb = st.mean(ra), st.mean(rb)
    return sum((x - ma) * (y - mb) for x, y in zip(ra, rb)) / math.sqrt(sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb))


print(f"workbook rows {len(X)} | comparable price set {len(P)} | sourced {sum(map(src, P))} | median drop all {med([d(x) for x in P])}, sourced {med([d(x) for x in P if src(x)])}")
print("\n[P1] purchase year (prior-purchase benchmarks only)")
PP = [x for x in P if str(x["Benchmark Type"]).startswith("Prior purchase") and isinstance(x["Benchmark Year"], int)]
print(f"  Spearman(benchmark year, drop) n={len(PP)}: {spearman([x['Benchmark Year'] for x in PP], [d(x) for x in PP]):.2f}")
for lab, lo, hi in [("<=2010", 0, 2010), ("2011-2016", 2011, 2016), ("2017-2020", 2017, 2020), ("2021+", 2021, 2100)]:
    L = [x for x in PP if lo <= x["Benchmark Year"] <= hi]
    print(f"  {lab:9} all {med([d(x) for x in L]):14} verified-benchmark {med([d(x) for x in L if x['Benchmark Type'] == 'Prior purchase'])}")
print("\n[P2] failed buildings: price vs prior value")
for lab, L in [("all", P), ("drop >=80%", [x for x in P if d(x) >= 0.8]), ("drop <80%", [x for x in P if d(x) < 0.8])]:
    a, b = [x["Benchmark Amount ($M)"] for x in L], [x["Disposition Amount ($M)"] for x in L]
    print(f"  {lab:11} n={len(L):2} Spearman(price, prior) {spearman(a, b):.2f} | price ${min(b)}-{max(b)}M | prior ${min(a)}-{max(a)}M | sourced {sum(map(src, L))}")
small = [x for x in P if x["Disposition Amount ($M)"] < 15]
print(f"  sub-$15M sales n={len(small)} (sourced {sum(map(src, small))}): price ${min(x['Disposition Amount ($M)'] for x in small)}-{max(x['Disposition Amount ($M)'] for x in small)}M vs prior ${min(x['Benchmark Amount ($M)'] for x in small)}-{max(x['Benchmark Amount ($M)'] for x in small)}M")
conv = [x for x in P if "onver" in str(x["Property Type"])]
print(f"  conversion-labelled {med([d(x) for x in conv])} (sourced {sum(map(src, conv))}) vs other {med([d(x) for x in P if x not in conv])}")
print("  occupancy known:", "; ".join(f"{str(x['Property Name / Address'])[:22]} occ {x['Occupancy at Event']} drop {round(d(x) * 100)}%{' [sourced]' if src(x) else ''}" for x in P if x["Occupancy at Event"]))
print("\n[P3] lender loss vs price (rows with loan, price and loss/severity)")
for x in X:
    L_, loss, pr, rec = num(x["Loan Balance ($M)"]), num(x["Realized Credit Loss ($M)"]), num(x["Disposition Amount ($M)"]), num(x["Net Principal Recovery ($M)"])
    if L_ and (loss or "severity" in str(x["Credit Loss Status"])):
        sev = loss / L_ if loss else 1.01
        line = f"  {str(x['Property Name / Address'])[:26]:26} loan ${L_}M loss {'$' + str(loss) + 'M' if loss else '~101% (reported)'} severity {round(sev * 100)}%"
        if pr:
            line += f" | price {round(pr / L_ * 100)}% of loan ({x['Disposition Amount Type']}) | loss beyond price {round((sev - (1 - pr / L_)) * 100)}pp"
        print(line + f" | {x['Verification Status']}")
print("\n[P6] metro medians (n>=2):")
by = {}
for x in P:
    by.setdefault(str(x["Location"])[:-3].strip(), []).append(d(x))
print("  " + "; ".join(f"{k} {round(st.median(v) * 100)}% n={len(v)}" for k, v in sorted(by.items(), key=lambda kv: -len(kv[1])) if len(v) >= 2))
print("[P7] price gains:", "; ".join(f"{str(x['Property Name / Address'])[:24]} ${x['Benchmark Amount ($M)']}M ({x['Benchmark Year']}) -> ${x['Disposition Amount ($M)']}M ({x['Sale / Status Year']})" for x in P if d(x) < 0))

# ---- added after the 2026-09-30 cold read: the workbook's OWN comparable filter, sourced-only figures, a null test ----
import random
print("\n[FILTER] workbook methodology: Include=Yes + verified benchmark ('Prior purchase') + same type")
V = [x for x in P if x["Include in Sale Analysis"] == "Yes" and x["Benchmark Type"] == "Prior purchase" and isinstance(x["Benchmark Year"], int)]
print(f"  compliant rows n={len(V)}: " + "; ".join(f"{str(x['Property Name / Address'])[:20]} {x['Benchmark Year']}->{x['Sale / Status Year']} {round(d(x) * 100)}%" for x in sorted(V, key=lambda x: x['Benchmark Year'])))
print(f"  Spearman(year, drop) compliant {spearman([x['Benchmark Year'] for x in V], [d(x) for x in V]):.2f} (n={len(V)}); "
      f"excluding the 410 Townsend 2024 resale {spearman([x['Benchmark Year'] for x in V if x['Benchmark Year'] != 2024], [d(x) for x in V if x['Benchmark Year'] != 2024]):.2f} (n={len(V) - 1})")
U = [x for x in PP if x["Benchmark Type"] != "Prior purchase"]
print(f"  unverified prior-purchase rows: Spearman {spearman([x['Benchmark Year'] for x in U], [d(x) for x in U]):.2f} (n={len(U)})")
print(f"  benchmark types in the 46: {dict((t, sum(1 for x in P if x['Benchmark Type'] == t)) for t in sorted({str(x['Benchmark Type']) for x in P}))}")
print(f"  Include flag in the 46: {dict((t, sum(1 for x in P if x['Include in Sale Analysis'] == t)) for t in sorted({str(x['Include in Sale Analysis']) for x in P}))}")
print("\n[P2-check] sourced-only, prior-purchase-only, and a shuffle null for the 80% split")
for lab, L in [("sourced >=80%", [x for x in P if src(x) and d(x) >= 0.8]), ("sourced <80%", [x for x in P if src(x) and d(x) < 0.8]),
               ("prior-purchase >=80%", [x for x in PP if d(x) >= 0.8]), ("prior-purchase <80%", [x for x in PP if d(x) < 0.8])]:
    print(f"  {lab:21} n={len(L):2} Spearman(price, prior) {spearman([x['Benchmark Amount ($M)'] for x in L], [x['Disposition Amount ($M)'] for x in L]):.2f}")
random.seed(7)
pri = [x["Benchmark Amount ($M)"] for x in P]
ratio = [x["Disposition Amount ($M)"] / x["Benchmark Amount ($M)"] for x in P]
lo_hi = []
for _ in range(2000):
    r = ratio[:]
    random.shuffle(r)
    deep = [(p, p * q) for p, q in zip(pri, r) if q <= 0.2]
    rest = [(p, p * q) for p, q in zip(pri, r) if q > 0.2]
    if len(deep) > 3 and len(rest) > 3:
        lo_hi.append((spearman(*zip(*deep)), spearman(*zip(*rest))))
lo_hi.sort()
print(f"  null (ratio shuffled, independent of prior), 2000 draws: median deep {st.median(a for a, _ in lo_hi):.2f} vs rest {st.median(b for _, b in lo_hi):.2f}; "
      f"share of draws with deep <= 0.53: {sum(1 for a, _ in lo_hi if a <= 0.53) / len(lo_hi):.1%}")
print("\n[COUNTS] office labels:", sum(1 for x in X if "office" in str(x["Property Type"]).lower()), "contain 'office' |",
      sum(1 for x in X if str(x["Property Type"]).startswith("Office")), "start with 'Office' |", sum(1 for x in X if x["Property Type"] == "Office"), "exactly 'Office'")
for x in X:
    if x["Event ID"] == "EVT-0071-01":
        print("[OCC] One City Centre raw text:", {k: x[k] for k in ("Raw Recent Price Text", "Raw Prior Price Text", "Raw Decline Text", "Review Notes", "Credit Loss Status")})
