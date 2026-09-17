#!/usr/bin/env python3
"""Grader for BND-25 and BND-26 — FRED H.15 primary, cache-busted, AS FIRST PUBLISHED.

🔴 REBUILT 2026-09-17 ~16:0x ET, BEFORE the 9/16 cells published, after reading this
script against the registered letters in thesis/PREDICTIONS.tsv. v1 deviated from the
spec in FOUR ways, every one capable of producing a confident WRONG verdict:

  1. IT GRADED AN OUT-OF-UNIVERSE TENOR. v1 pulled ELEVEN series including DGS1MO.
     BND-25 registers TEN: DGS3MO, DGS6MO, DGS1, DGS2, DGS3, DGS5, DGS7, DGS10,
     DGS20, DGS30 ("20 observations: 10 tenors x 2 dates"). A DGS1MO argmax would
     have resolved the row FALSE on a series the letter does not contain.
  2. NO ALL-TEN-PUBLISHED REQUIREMENT. v1 silently dropped series missing a cell and
     computed the argmax over whatever remained. The letter resolves VOID-NOT-PUBLISHED
     unless BOTH dates exist for ALL TEN — a partial set must never yield a verdict.
  3. NO VOID-NO-MOVE BRANCH. The letter makes an all-ten-zero session the declared
     catch-all; v1 would have returned FALSE (every series ties the max at 0.0).
  4. NO VOID-INSUFFICIENT-PUBLICATION COUNT for BND-26. The letter voids the row if
     fewer than THREE sessions in the window are gradeable; v1 never counted.

Correct in v1 and preserved: the 2dp rounding happens AFTER the subtraction, and the
>= boundary means FALSE OWNS 4.95 exactly.
"""
import urllib.request, time, datetime as dt

# BND-25's registered universe. TEN series. DGS1MO is deliberately absent.
S25 = ['DGS3MO','DGS6MO','DGS1','DGS2','DGS3','DGS5','DGS7','DGS10','DGS20','DGS30']
BELLY = {'DGS2','DGS3','DGS5'}
D0, D1 = '2026-09-15', '2026-09-16'
WIN_LO, WIN_HI = '2026-09-16', '2026-09-23'

def pull(s):
    u = (f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={s}"
         f"&cosd=2026-09-01&_cb={int(time.time())}")
    rows = [l.split(',') for l in
            urllib.request.urlopen(u, timeout=60).read().decode().strip().split('\n')[1:]]
    return {d: (float(v) if v not in ('.', '') else None) for d, v in rows}

data = {s: pull(s) for s in sorted(set(S25) | {'DGS1', 'DGS2'})}
stamp = dt.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M %Z')
print(f"dated cache-busted pull: {stamp}")
print("frontier per series:",
      {s: max((d for d, v in data[s].items() if v is not None), default=None) for s in S25})

# ---------------------------------------------------------------- BND-25
print("\n=== BND-25 — belly-led argmax, STRICT, over the TEN registered tenors ===")
have = [s for s in S25 if data[s].get(D0) is not None and data[s].get(D1) is not None]
missing = [s for s in S25 if s not in have]
if missing:
    print(f"  {len(have)}/10 series have BOTH {D0} and {D1}; MISSING: {missing}")
    print("  ⇒ VOID-NOT-PUBLISHED (never FALSE) if still so at 2026-09-25 17:00 ET.")
    print("     NOT GRADEABLE NOW — a partial set must not yield a verdict.")
else:
    deltas = [(s, data[s][D1] - data[s][D0]) for s in S25]
    print("  Δ 9/15→9/16 (bp):", [(s, round(x * 100, 1)) for s, x in deltas])
    if all(abs(x) < 1e-12 for _, x in deltas):
        print("  ⇒ VOID-NO-MOVE — all ten changes exactly zero (declared catch-all).")
    else:
        mx = max(abs(x) for _, x in deltas)
        winners = [s for s, x in deltas if abs(abs(x) - mx) < 1e-9]
        verdict = 'TRUE' if all(w in BELLY for w in winners) else 'FALSE'
        print(f"  max |Δ| = {round(mx*100,1)}bp at {winners}")
        print(f"  ⇒ BND-25 = {verdict}  (TRUE iff EVERY argmax tenor ∈ {{DGS2,DGS3,DGS5}};"
              f" a tie STRADDLING belly and non-belly resolves FALSE)")

# ---------------------------------------------------------------- BND-26
print("\n=== BND-26 — 1y1y = (2×DGS2) − DGS1, 2dp AFTER subtraction; FALSE owns 4.95 ===")
sessions = sorted(d for d in set(data['DGS1']) | set(data['DGS2']) if WIN_LO <= d <= WIN_HI)
gradeable, breach = 0, None
for d in sessions:
    a, b = data['DGS1'].get(d), data['DGS2'].get(d)
    if a is None or b is None:
        print(f"  {d}: EXCLUDED — DGS1/DGS2 unpublished (never counted as a non-breach)")
        continue
    gradeable += 1
    f = round(2 * b - a, 2)
    hit = f >= 4.95
    if hit and breach is None:
        breach = (d, f)
    print(f"  {d}: 1y1y = 2×{b} − {a} = {f:.2f}" + ("   🔴 ≥4.95 ⇒ FALSE" if hit else "   ok (<4.95)"))
print(f"  gradeable sessions so far: {gradeable}")
if breach:
    print(f"  ⇒ BND-26 = FALSE — first breach {breach[0]} at {breach[1]:.2f}")
elif dt.date.today() < dt.date(2026, 9, 23):
    print("  ⇒ BND-26 still OPEN — window runs through 2026-09-23")
elif gradeable < 3:
    print("  ⇒ VOID-INSUFFICIENT-PUBLICATION — fewer than three gradeable sessions")
else:
    print("  ⇒ BND-26 = TRUE — no session in the window reached 4.95")
