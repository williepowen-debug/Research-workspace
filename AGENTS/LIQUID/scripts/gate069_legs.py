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
from fetch import fred_fetch

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
    # ⚠️ DATE-MATCH REPAIR 2026-09-29 (KB-LIQ-126 class; owed since the 9/25 L4 re-read).
    # The prior version paired the latest HY obs (T+1, e.g. Fri) with the LATEST equity
    # session (e.g. Mon): a cross-date pair that could fire or clear L4 on two different
    # days. The letter is ONE session ("-15%/session w/ credit underperforming"), so the
    # equity change is now taken on the HY obs date itself, raw unadjusted closes, and
    # fails CLOSED if that bar (or the prior session's) is missing (the 9/22 dropped-bar case).
    worst = None; faults = []
    prev = d[-2]
    try:
        import yfinance as yf, warnings; warnings.filterwarnings("ignore")
        px = yf.download(tick, start=prev, end=None, auto_adjust=False, progress=False)["Close"]
        px.index = [i.strftime("%Y-%m-%d") for i in px.index]
    except Exception as e:
        px = None; faults.append(f"fetch failed: {type(e).__name__}")
    if px is not None:
        extra = [k for k in px.columns if k not in tick]
        if extra: faults.append(f"UNREQUESTED tickers returned {extra} — identity mismatch")
        for t in tick:
            if t not in px.columns:
                faults.append(f"{t} missing"); print(f"      {t:<6} 🔴 no series"); continue
            c = px[t].dropna()
            if last not in c.index or prev not in c.index:
                faults.append(f"{t} bar missing for {prev if prev not in c.index else last}")
                print(f"      {t:<6} 🔴 bar missing (need {prev} and {last})"); continue
            chg = (c[last] / c[prev] - 1) * 100
            print(f"      {t:<6} {c[last]:>10.2f}  {chg:+.2f}%   [session {last} vs {prev}, raw close]")
            if worst is None or chg < worst[1]: worst = (t, chg)
        newer = sorted(i for i in px.index if i > last)
        if newer:
            print(f"      ⏳ equity sessions after the latest HY obs {newer}: UNGRADEABLE-PENDING-PUBLICATION (not graded)")
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
