#!/usr/bin/env python3
"""Follow-up checks on REPORT.md section 3-4 after Will's reviewer (CATO) read, 2026-11-17 afternoon.

Usage: review_checks.py <dir_q2> <dir_q3>   (same unzipped FFIEC bulk folders as universe_counts.py)

1. Matched banks: the 6/30 -> 9/30 comparison on exactly the same institutions.
2. AFS versus HTM: available-for-sale marks already reduce GAAP equity through AOCI; held-to-maturity
   marks are disclosed fair-value differences, not in book equity. Split the measure accordingly.
3. Aggregate dollars: did the system's unrealized loss in dollars double, or only the ratio?
4. Rough rate attribution: duration-proxy loss (DUR buckets) x the Q3 yield move vs the actual change.
5. Measures B and D on 6/30 (the Friedberg claim's quarter), which the first run did not test.
Values in $ thousands as filed; RCFD where present, else RCON; POR filers only.
"""
import os, statistics, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # our own code folder, not the data folder
from universe_counts import load, num, measures, count_ge, DUR  # noqa: E402

TAX = 0.79


def split(rec):
    m = measures(rec)
    if m is None or m["eq"] is None or m["eq"] <= 0:
        return None
    ac, af = num(rec, "1772"), num(rec, "1773")
    hc, hf = num(rec, "1754"), num(rec, "1771")
    m["afs"] = (ac - af) if None not in (ac, af) else None
    m["htm"] = (hc - hf) if None not in (hc, hf) else None
    return m


def main():
    q2, q3 = load(sys.argv[1]), load(sys.argv[2])
    S2 = {r: split(v) for r, v in q2.items()}
    S3 = {r: split(v) for r, v in q3.items()}
    both = [r for r in S3 if r in S2 and S2[r] and S3[r] and S2[r]["ul"] is not None and S3[r]["ul"] is not None]
    print(f"matched banks with positive equity and securities lines both quarters: {len(both)}")

    print("\n1. Matched-bank comparison (same institutions)")
    for k, S in (("6/30", S2), ("9/30", S3)):
        g = [S[r]["ul"] / S[r]["eq"] for r in both]
        at = [S[r]["ul"] * TAX / S[r]["eq"] for r in both]
        print(f"  {k}: median pretax {statistics.median(g):.1%}; >=20% after tax {count_ge(at, .20)} ({count_ge(at, .20)/len(both):.1%}); "
              f">=20% pretax {count_ge(g, .20)}")
    g2 = {r: S2[r]["ul"] * TAX / S2[r]["eq"] for r in both}
    g3 = {r: S3[r]["ul"] * TAX / S3[r]["eq"] for r in both}
    up = sum(1 for r in both if g3[r] > g2[r])
    print(f"  banks whose ratio rose: {up} of {len(both)} ({up/len(both):.1%}); entered >=20%: "
          f"{sum(1 for r in both if g3[r] >= .2 > g2[r])}; left: {sum(1 for r in both if g2[r] >= .2 > g3[r])}")

    print("\n2. AFS versus HTM (matched banks; after-tax share of GAAP equity 3210)")
    for k, S in (("6/30", S2), ("9/30", S3)):
        a = [(S[r]["afs"] or 0) * TAX / S[r]["eq"] for r in both]
        h = [(S[r]["htm"] or 0) * TAX / S[r]["eq"] for r in both]
        tot = [S[r]["ul"] * TAX / S[r]["eq"] for r in both]
        hits = [r for r, t in zip(both, tot) if t >= .2]
        afs_alone = sum(1 for r in hits if (S[r]["afs"] or 0) * TAX / S[r]["eq"] >= .2)
        htm_alone = sum(1 for r in hits if (S[r]["htm"] or 0) * TAX / S[r]["eq"] >= .2)
        has_htm = sum(1 for r in both if S[r]["htm"] and abs(S[r]["htm"]) > 0)
        A = sum(S[r]["afs"] or 0 for r in both); H = sum(S[r]["htm"] or 0 for r in both)
        print(f"  {k}: median AFS {statistics.median(a):.1%}, median HTM {statistics.median(h):.1%}; banks reporting any HTM mark {has_htm}; "
              f"of {len(hits)} at >=20% total: AFS alone >=20% {afs_alone}, HTM alone >=20% {htm_alone}, need both {len(hits)-sum(1 for r in hits if (S[r]['afs'] or 0)*TAX/S[r]['eq']>=.2 or (S[r]['htm'] or 0)*TAX/S[r]['eq']>=.2)}; "
              f"system pretax AFS ${A/1e6:,.1f}B, HTM ${H/1e6:,.1f}B (HTM share {H/(A+H):.0%})")
    # equity before the AFS mark: add back after-tax AFS loss, to see the ratio on a basis that does not already net it
    for k, S in (("6/30", S2), ("9/30", S3)):
        x = [S[r]["ul"] * TAX / (S[r]["eq"] + (S[r]["afs"] or 0) * TAX) for r in both if S[r]["eq"] + (S[r]["afs"] or 0) * TAX > 0]
        print(f"  {k}: total after tax / (equity + after-tax AFS loss added back): median {statistics.median(x):.1%}; >=20% {count_ge(x, .2)} of {len(x)}")

    print("\n3. Aggregate dollars (matched banks, pretax)")
    for k, S in (("6/30", S2), ("9/30", S3)):
        print(f"  {k}: unrealized loss ${sum(S[r]['ul'] for r in both)/1e6:,.1f}B; equity ${sum(S[r]['eq'] for r in both)/1e6:,.1f}B; "
              f"aggregate ratio {sum(S[r]['ul'] for r in both)/sum(S[r]['eq'] for r in both):.1%}")
    small = [r for r in both if S3[r]["assets"] and S3[r]["assets"] < 10e6]
    for k, S in (("6/30", S2), ("9/30", S3)):
        print(f"  {k} banks under $10B assets (n={len(small)}): loss ${sum(S[r]['ul'] for r in small)/1e6:,.1f}B, "
              f"ratio {sum(S[r]['ul'] for r in small)/sum(S[r]['eq'] for r in small):.1%}")

    print("\n4. Rough rate attribution (duration PROXY, stated buckets; hedges, spreads, purchases and sales not modelled)")
    dv2 = sum(S2[r]["dv"] for r in both)
    d_ul = sum(S3[r]["ul"] for r in both) - sum(S2[r]["ul"] for r in both)
    for bp, lab in ((85, "10Y +85bp"), (90, "5Y +90bp")):
        print(f"  6/30 book x {lab}: predicted ${dv2*bp/1e4/1e6:,.1f}B vs actual change ${d_ul/1e6:,.1f}B ({d_ul/(dv2*bp/1e4):.0%} of the proxy)")

    print("\n5. Measures B and D on 6/30 (all 6/30 filers, as in the first run)")
    rows2 = [m for m in S2.values() if m]
    for bp in (100, 200, 300):
        g = [m["dv"] * bp / 1e4 / m["eq"] for m in rows2]
        print(f"  B 6/30 +{bp}bp shock loss alone >=20% of equity: {count_ge(g, .2)} of {len(rows2)}")
    rows = [m for m in rows2 if m["ul"] is not None and m["cet1"] and m["cet1"] > 0]
    g = [m["ul"] * TAX / m["cet1"] for m in rows]
    hit = [m for m, x in zip(rows, g) if x >= .2]
    print(f"  D 6/30 after-tax loss >=20% of CET1: {len(hit)} of {len(rows)}; of those AOCI opt-out = 1: {sum(1 for m in hit if m['optout'] == '1')}")


if __name__ == "__main__":
    main()
