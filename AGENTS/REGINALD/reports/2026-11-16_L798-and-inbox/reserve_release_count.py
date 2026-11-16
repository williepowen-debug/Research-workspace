"""Carried count (d) from CALENDAR 11/07 row (PROME packet 11/02, DOCKET L180 scope add):
banks with total nonaccrual (1403 / FDIC NALNLS) UP and loan allowance (3123 / LNATRES) DOWN,
quarter over quarter, count + share of banks + share of total loans; prior quarter beside it.
Inputs are DEWEY's saved primary files (read-only): FFIEC 9/30 rows, FDIC BankFind 6/30 and 3/31.
Units $thousands. A bank missing either cell at either date is excluded and counted as excluded.
Run from repo root: python3 -I AGENTS/REGINALD/reports/2026-11-16_L798-and-inbox/reserve_release_count.py
"""
import csv, json, sys
B = "AGENTS/DEWEY/research/2026-11-11_003R-population/"

def fdic(path):
    out = {}
    for r in json.load(open(path))["data"]:
        x = r["data"]
        out[int(x["CERT"])] = (x.get("NALNLS"), x.get("LNATRES"), x.get("LNLSGR"), x.get("NAME"))
    return out

def ffiec(path):
    out = {}
    for r in csv.DictReader(open(path), delimiter="\t"):
        f = lambda k: None if r[k] in ("", "None") else float(r[k])
        out[int(r["CERT"])] = (f("NALNLS"), f("LNATRES"), f("LNLSGR"), r["NAME"])
    return out

def count(prev, cur, label):
    common = set(prev) & set(cur)
    ok = [c for c in common if None not in prev[c][:3] and None not in cur[c][:3]]
    hit = [c for c in ok if cur[c][0] > prev[c][0] and cur[c][1] < prev[c][1]]
    tl = sum(cur[c][2] for c in ok); hl = sum(cur[c][2] for c in hit)
    print(f"{label}: common={len(common)} usable={len(ok)} excluded={len(common)-len(ok)} "
          f"hit={len(hit)} ({len(hit)/len(ok):.1%} of banks) loans {hl/1e6:,.1f}B of {tl/1e6:,.1f}B ({hl/tl:.1%})")
    big = sorted(hit, key=lambda c: -cur[c][2])[:10]
    for c in big:
        print(f"   {cur[c][3][:40]:40s} cert {c}: NA {prev[c][0]/1e3:,.1f}M -> {cur[c][0]/1e3:,.1f}M, ALLL {prev[c][1]/1e3:,.1f}M -> {cur[c][1]/1e3:,.1f}M, loans {cur[c][2]/1e6:,.1f}B")
    return hit

q1 = fdic(B + "fdic-20260331.json"); q2 = fdic(B + "fdic-20260630.json"); q3 = ffiec(B + "current-bank-rows.tsv")
count(q1, q2, "3/31 -> 6/30 (FDIC both)")
count(q2, q3, "6/30 (FDIC) -> 9/30 (FFIEC)")

# Sensitivity (diagnostic only, not the registered letter): both moves at least 1% of the prior level.
def count_material(prev, cur, label, m=0.01):
    ok = [c for c in set(prev) & set(cur) if None not in prev[c][:3] and None not in cur[c][:3]]
    hit = [c for c in ok if prev[c][0] > 0 and prev[c][1] > 0 and cur[c][0] >= prev[c][0]*(1+m) and cur[c][1] <= prev[c][1]*(1-m)]
    tl = sum(cur[c][2] for c in ok); hl = sum(cur[c][2] for c in hit)
    print(f"{label} [both moves >=1%]: hit={len(hit)} ({len(hit)/len(ok):.1%} of banks) loans {hl/tl:.1%}")
count_material(q1, q2, "3/31 -> 6/30")
count_material(q2, q3, "6/30 -> 9/30")
