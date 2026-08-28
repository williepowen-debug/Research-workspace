#!/usr/bin/env python3
"""
LIQUID — GATE-LIQ-069 (AI-HY cohort re-arm) leg instrumentation.

Registry letter: "ANY ONE of 5 legs: BB>220-while-CCC-flat · CoreWeave 5Y CDS re-widen
>100bp · AI-infra HY new-issue concessions widening · cohort equity (CRWV,IREN,APLD,NBIS)
-15%/session w/ credit underperforming · ORCL fallen-angel ladder."

Instruments L1 and L4 ONLY. L2/L3 are terminal-gated (NO_INSTRUMENT); L5 is ratings
(JUDGEMENT). See the returned letter for the disposition of each.

⚠️ L1 and L4 each contain an UNNAMED sub-threshold in the registry text -- "CCC flat" and
"credit underperforming". This tool applies EXPLICIT PROPOSED definitions, printed on every
run so the reader can see what was assumed. They are PROPOSALS, not adopted spec.
"""
import sys, argparse
sys.path.insert(0, "FORGE/tools/market-data")
from fetch import fred_fetch, price_fetch

# PROPOSED definitions for the unnamed sub-thresholds (NOT adopted spec)
CCC_FLAT_BP = 15      # |CCC 5-session change| <= 15bp  == "flat"
CRED_UNDER_BP = 5     # HY OAS widened >= 5bp on the session == "credit underperforming"

def ser(sid, n=30):
    out = {}
    for x in fred_fetch(sid, limit=n):
        v = x.get("value")
        if v in (".", "", None): continue
        out[x["date"]] = float(v) * 100
    return out

def main():
    ap = argparse.ArgumentParser(); ap.parse_args()
    print("=" * 96)
    print("  GATE-LIQ-069 — instrumented legs L1 / L4   (L2, L3 = NO_INSTRUMENT; L5 = JUDGEMENT)")
    print(f"  PROPOSED defs, NOT adopted spec:  'CCC flat' = |5-sess CCC delta| <= {CCC_FLAT_BP}bp")
    print(f"                                    'credit underperforming' = HY OAS +{CRED_UNDER_BP}bp or more on the session")
    print("=" * 96)

    bb, ccc, hy = ser("BAMLH0A1HYBB"), ser("BAMLH0A3HYC"), ser("BAMLH0A0HYM2")
    d = sorted(set(bb) & set(ccc) & set(hy))
    if len(d) < 6:
        print("  🔴 INSTRUMENT-FAULT — fewer than 6 common observations; cannot evaluate L1."); return
    last = d[-1]
    ccc_chg = ccc[last] - ccc[d[-6]]
    l1_bb = bb[last] > 220
    l1_flat = abs(ccc_chg) <= CCC_FLAT_BP
    print(f"\n  L1  BB>220 while CCC flat            [obs {last}]")
    print(f"      BB {bb[last]:.0f}bps  -> BB>220? {'YES' if l1_bb else 'NO'}   ({220 - bb[last]:+.0f}bp to the line)")
    print(f"      CCC {ccc[last]:.0f}bps, 5-sess change {ccc_chg:+.0f}bp -> flat? {'YES' if l1_flat else 'NO'}")
    print(f"      => L1 {'🔴 FIRED' if (l1_bb and l1_flat) else '🟢 NOT FIRED'}   (conjunctive; BB is the binding half)")

    tick = ["CRWV", "IREN", "APLD", "NBIS"]
    print(f"\n  L4  cohort equity -15%/session with credit underperforming")
    # ⚠️ F1 IDENTITY GUARD (KB-LIQ-117). price_fetch takes a LIST. Passing the bare string
    # "CRWV" iterates it into "C","R","W","V" and returns CITIGROUP / R / W / VISA -- real
    # prices for unrelated companies, under keys that look like a partial answer. Caught
    # 2026-08-28 while writing this file, hours after the same class (KB-LIQ-116) nearly
    # fired GATE-LIQ-076 off a different exchange's contract. ALWAYS pass a list, and
    # ALWAYS verify the returned keys are the tickers you asked for.
    worst = None; faults = []
    try:
        quotes = price_fetch(tick)
    except Exception as e:
        quotes = {}; faults.append(f"fetch failed: {type(e).__name__}")
    missing = [t for t in tick if t not in quotes]
    extra = [k for k in quotes if k not in tick]
    if missing: faults.append(f"missing tickers {missing}")
    if extra:   faults.append(f"UNREQUESTED tickers returned {extra} — identity mismatch")
    for t in tick:
        q = quotes.get(t)
        if not q:
            print(f"      {t:<6} 🔴 no quote"); continue
        chg = q.get("change_pct")
        if chg is None:
            faults.append(f"{t} has no change_pct"); print(f"      {t:<6} {q.get('price')}  change UNAVAILABLE"); continue
        print(f"      {t:<6} {q.get('price'):>10}  {float(chg):+.2f}%   [{q.get('asof')}]")
        if worst is None or float(chg) < worst[1]: worst = (t, float(chg))
    hy_chg = hy[last] - hy[d[-2]]
    l4_cr = hy_chg >= CRED_UNDER_BP
    print(f"      HY OAS session change {hy_chg:+.0f}bp [obs {last}] -> credit underperforming? {'YES' if l4_cr else 'NO'}")
    if faults:
        # ⛔ NEVER report NOT FIRED off an unmeasured leg — that is the dead-quiet failure.
        print(f"      => L4 🔴 INSTRUMENT-FAULT — {'; '.join(faults)}")
        print(f"         NOT graded. An unmeasured leg is UNMEASURED, never NOT FIRED.")
    else:
        l4_eq = worst is not None and worst[1] <= -15
        print(f"      worst name: {worst[0]} {worst[1]:+.2f}%  -> <=-15%? {'YES' if l4_eq else 'NO'}")
        print(f"      => L4 {'🔴 FIRED' if (l4_eq and l4_cr) else '🟢 NOT FIRED'}   (conjunctive)")
    print(f"\n  ⛔ L2 CoreWeave 5Y CDS  — NO_INSTRUMENT (single-name CDS, terminal-gated)")
    print(f"  ⛔ L3 AI-infra new-issue concessions — NO_INSTRUMENT (dealer/terminal primary)")
    print(f"  ⚠️  L5 ORCL fallen-angel ladder — JUDGEMENT (ratings; primary re-verification owed)")
    print("=" * 96)

if __name__ == "__main__":
    main()
