"""WQ-246 (Will 2026-09-26 15:04 ET): base rates for the persistence count on THESIS gate (a)
'DFII10 >2.5 sustained'. Episodes = a published close >= L after a close < L; run = consecutive
published closes >= L (FRED skips non-publication dates; '.' cells dropped, never counted as a miss).
Reports, per level, how many crossings reach 3 and 5 consecutive, and P(>=5 | >=3).
Usage: python3 analysis/2026-09-26_WQ-246_dfii10_persistence.py
"""
import sys; sys.path.insert(0, "../../FORGE/tools/market-data")
import fetch
d = fetch.fred_fetch("DFII10", limit=20000)
obs = d["observations"] if isinstance(d, dict) and "observations" in d else d
rows = sorted((o["date"], float(o["value"])) for o in obs if o.get("value") not in (".", None, ""))
print("DFII10 n", len(rows), rows[0][0], "->", rows[-1][0], "last", rows[-1])
def episodes(L):
    eps, i = [], 1
    while i < len(rows):
        if rows[i][1] >= L and rows[i-1][1] < L:
            j = i
            while j < len(rows) and rows[j][1] >= L: j += 1
            eps.append((rows[i][0], j - i, j >= len(rows))); i = j
        else: i += 1
    return eps
for L in (2.00, 2.25, 2.50, 2.75):
    e = episodes(L); n = len(e)
    r3 = sum(x[1] >= 3 for x in e); r5 = sum(x[1] >= 5 for x in e); r1 = sum(x[1] == 1 for x in e)
    print(f"L={L:.2f}: crossings {n} | run==1 {r1} | >=3 {r3} | >=5 {r5} | P(>=5|>=3) {r5}/{r3}")
e = episodes(2.50)
print("2.50 episodes (start, run, still-open):", e)
since = [r for r in rows if r[0] >= "2026-09-10"]
print("since 2026-09-10:", len(since), "sessions; all >=2.50:", all(v >= 2.5 for _, v in since), "; 3rd:", since[2], " 5th:", since[4])
