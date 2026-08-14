#!/usr/bin/env python3
"""
MIDAS-07 grader — the FROZEN 4-branch frame, evaluated mechanically.

Written 2026-08-14 ~14:3x ET, BEFORE the 15:30 print, deliberately: a frame you
evaluate by eye after seeing the number is a frame you can talk yourself into.
Branch conditions are transcribed VERBATIM from workbook/PREDICTIONS.tsv row
MIDAS-07 (Will-registered 2026-08-07, frozen — zero re-tuning permitted).

  (a) FRAGILE            net > 225,000 AND net/OI > 56% AND OI > 400,000
  (b) ABSORBED           net/OI <= 53.2% AND gold >= $4,300
  (c) SQUEEZE-EXHAUSTION NC short < 20,000 AND OI <= 371,551
  (d) INDETERMINATE      anything else

KNOWN AMBIGUITY, recorded at registration and NOT silently repaired: (b) and (c)
are not mutually exclusive. If both fire, report the joint satisfaction and ask
Will to adjudicate precedence. This script prints BOTH rather than picking.

Usage: python3 grade_midas07.py --oi N --net N --short N --gold F
"""
import argparse

# Frozen boundaries — do not edit. Changing a number here changes a registered
# prediction after the fact, which is the whole thing the freeze exists to stop.
A_NET, A_RATIO, A_OI = 225_000, 56.0, 400_000
B_RATIO, B_GOLD = 53.2, 4_300.0
C_SHORT, C_OI = 20_000, 371_551

# Anchors as-of Tue 2026-08-04 (reproduced exactly from the raw CFTC file 8/14).
BASE = {"oi": 371_551, "net": 197_634, "short": 29_379, "ratio": 53.19}
JAN = {"oi": 527_455, "net": 251_238, "ratio": 47.6}   # 2026-01-13 blow-off peak

# Pre-registered MEASURED base rates (MIDAS forum dissent 2026-08-11, n=449
# weekly rows, CFTC legacy futures-only, exact market-name match).
PRIORS = {
    "a": "0.91% measured one-week transition rate (n=441); <=2% ceiling. "
         "P(dOI >= +28,449 | OI <= 400,000) = 0 of 19 observed (rule-of-three "
         "95% upper bound 15.8% -- do NOT quote 0-of-19 as a probability).",
    "b": "~6.8-8.3% (net/OI <= 51.47% at 8.3%, x price leg ~82%).",
    "c": "0.00% -- STRUCTURALLY UNREACHABLE. NC short < 20,000 has never "
         "occurred in 449 weeks. This branch can only ever say 'spent = FALSE'.",
    "d": "~92%+ on the full partition; 99.09% on the exhaustion axis where only "
         "(a) and (c) classify. INDETERMINATE was ALWAYS the modal outcome.",
}


def grade(oi, net, short, gold):
    ratio = 100.0 * net / oi
    legs = {
        "a": [("net > 225,000", net > A_NET, f"{net:,}"),
              ("net/OI > 56%", ratio > A_RATIO, f"{ratio:.2f}%"),
              ("OI > 400,000", oi > A_OI, f"{oi:,}")],
        "b": [("net/OI <= 53.2%", ratio <= B_RATIO, f"{ratio:.2f}%"),
              ("gold >= $4,300", gold >= B_GOLD, f"${gold:,.2f}")],
        "c": [("NC short < 20,000", short < C_SHORT, f"{short:,}"),
              ("OI <= 371,551", oi <= C_OI, f"{oi:,}")],
    }
    fired = [b for b, ls in legs.items() if all(ok for _, ok, _ in ls)]
    return ratio, legs, fired


def main():
    p = argparse.ArgumentParser()
    for f in ("oi", "net", "short"):
        p.add_argument(f"--{f}", type=int, required=True)
    p.add_argument("--gold", type=float, required=True, help="GC=F close, data-date")
    p.add_argument("--date", default="2026-08-11")
    a = p.parse_args()

    ratio, legs, fired = grade(a.oi, a.net, a.short, a.gold)
    names = {"a": "FRAGILE", "b": "ABSORBED", "c": "SQUEEZE-EXHAUSTION"}

    print("=" * 74)
    print(f"  MIDAS-07 GRADE — COT as-of {a.date} — FROZEN FRAME, VERBATIM")
    print("=" * 74)
    print(f"  PRINT : OI {a.oi:,} | net NC long {a.net:,} | NC short {a.short:,} "
          f"| net/OI {ratio:.2f}% | gold ${a.gold:,.2f}")
    print(f"  BASE  : OI {BASE['oi']:,} | net {BASE['net']:,} | short {BASE['short']:,} "
          f"| net/OI {BASE['ratio']:.2f}%   [as-of 2026-08-04]")
    print(f"  WoW   : OI {a.oi-BASE['oi']:+,} | net {a.net-BASE['net']:+,} | "
          f"short {a.short-BASE['short']:+,} | net/OI {ratio-BASE['ratio']:+.2f}pp")
    print(f"  vs JAN: OI {100*(a.oi/JAN['oi']-1):+.1f}% | net {100*(a.net/JAN['net']-1):+.1f}%"
          f" | net/OI {ratio-JAN['ratio']:+.1f}pp vs the 47.6% blow-off peak")
    print()
    for b, ls in legs.items():
        ok = all(x for _, x, _ in ls)
        print(f"  ({b}) {names[b]:<19} {'*** FIRES ***' if ok else 'no'}")
        for label, passed, val in ls:
            print(f"        [{'PASS' if passed else 'FAIL'}] {label:<22} actual {val}")
    print()
    print("-" * 74)
    if len(fired) == 1:
        print(f"  VERDICT: ({fired[0]}) {names[fired[0]]}")
    elif len(fired) == 0:
        print("  VERDICT: (d) INDETERMINATE — no branch satisfied. This is a REAL")
        print("           grade, not a failure to grade: it was the pre-registered")
        print("           modal outcome. Hold M1, no read.")
    else:
        print(f"  VERDICT: JOINT SATISFACTION — {', '.join(names[b] for b in fired)}")
        print("           The registration recorded (b)/(c) as non-exclusive and")
        print("           FROZE the overlap rather than repairing it. Report both;")
        print("           escalate to Will for precedence. Do NOT resolve alone.")
    print("-" * 74)
    print("  Pre-registered base rates (measured, n=449 — these TRAVEL with the grade):")
    for k in "abcd":
        print(f"    ({k}) {PRIORS[k]}")


if __name__ == "__main__":
    main()
