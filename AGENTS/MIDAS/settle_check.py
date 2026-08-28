#!/usr/bin/env python3
"""
MIDAS -- settle-time metals check. WRITTEN 2026-08-28 ~11:2x ET, BEFORE the 13:30 ET COMEX settle.

WHY THIS EXISTS
  Three things have to happen at 13:30 and each one has already been done wrong on this desk:

  1. PRINT BOTH BASES (L-19). The frozen letter names `GC=F`. Today GC=F's DAILY HISTORY is stitched
     to the DYING contract while its LIVE bar is GCZ26 -- three different values for 2026-08-27
     ($4,609.70 / $4,664.00 / $4,631.40, a 1.18% spread). KB-080, L-40.
  2. IDENTIFY THE CONTRACT BY VOLUME, NOT PRICE (L-40). A ~1,000-lot day on the world's most liquid
     gold future is not the front month. This is the cheapest contract-identity test there is and it
     needs no contract codes.
  3. LABEL PRE-SETTLE vs SETTLED (L-37/N5 ii-b). A bar pulled before 13:30 -- or after 18:00 ET -- is
     in-flight. On 2026-08-20 this desk published a mislabelled in-flight bar TO WILL. On 2026-08-27
     four of six provisional legs were wrong, every one HIGH.

  The PGM betas are hardcoded from the canonical report so the I2 residual cannot be re-fit at
  13:31 while looking at the number. They reproduce the report EXACTLY:
  Pt 8/4 = 3.11 sigma, Pd 8/4 = 2.69 sigma, Pt 8/19 = 0.59 sigma.

WHAT THIS DOES NOT DO
  It does not grade MIDAS-06 (the DFII10 leg publishes Mon 8/31), it does not fire I2, and it moves
  no score, band or threshold. It prints figures with correct labels. A human grades.

USAGE
  python3 settle_check.py                 # label from the clock
  python3 settle_check.py --assume-settled  # only after 13:30 ET AND a T+1 re-pull is still owed
"""
import argparse
import datetime
import sys

# ---- PRE-REGISTERED, from reports/2026-08-27_pgm-surge-attribution.md (n=665, 2024-01-03 -> 2026-08-26) ----
PGM = {"PA=F": dict(beta=1.1095, icept=-0.0703, sigma=2.494, name="Palladium"),
       "PL=F": dict(beta=1.1492, icept=-0.0225, sigma=2.012, name="Platinum")}
I2_TRIGGER_SIGMA = 2.5     # re-open condition (b): Pt or Pd residual >2.5 sigma vs gold, Pd LEADING
MIDAS06_A = 4340.70        # branch (a) gold leg
MIDAS06_B = 4050.00        # branch (b) gold leg
# Confirmed 8/27 settles, T+1 re-pulled 2026-08-28 10:38 ET (KB-079)
PRIOR = {"GC=F": 4609.70, "GCZ26.CMX": 4664.00, "PA=F": 1337.60, "PL=F": 1845.30,
         "SI=F": 69.429, "HG=F": 6.5870, "GLD": 422.60}
# Instruments whose real front-month daily volume should be five figures or more.
LIQUID_FLOOR = {"GC=F": 50000, "GCZ26.CMX": 50000, "SI=F": 10000, "HG=F": 10000}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--assume-settled", action="store_true")
    a = ap.parse_args()
    try:
        import yfinance as yf
    except ImportError:
        print("FATAL: yfinance missing -- run under the repo .venv.")
        return 2

    now = datetime.datetime.now()
    settled = a.assume_settled or (now.hour, now.minute) >= (13, 30)
    label = "SETTLED (13:30 ET struck)" if settled else "*** PRE-SETTLE -- IN-FLIGHT BAR, NOT A CLOSE ***"

    print("=" * 78)
    print("  MIDAS SETTLE CHECK   %s" % now.strftime("%Y-%m-%d %H:%M %Z"))
    print("  label: %s" % label)
    if settled and not a.assume_settled:
        print("  >>> 13:30 has passed, but L-37 says a T+1 RE-PULL IS STILL OWED before these are")
        print("      quoted as final. The 8/27 bars were wrong in 4 of 6 legs, every one HIGH.")
    print("=" * 78)

    tick = {}
    print("\n  --- LIVE / LAST, with the VOLUME contract-identity test (L-40) ---")
    for t in ["GC=F", "GCZ26.CMX", "SI=F", "HG=F", "PL=F", "PA=F", "GLD"]:
        try:
            h = yf.Ticker(t).history(period="5d", interval="1d")
            last = float(h["Close"].iloc[-1])
            vol = int(h["Volume"].iloc[-1] or 0)
            bar = str(h.index[-1].date())
            tick[t] = last
            flag = ""
            if t in LIQUID_FLOOR and 0 < vol < LIQUID_FLOOR[t]:
                flag = "  <<< VOLUME TOO LOW FOR A FRONT MONTH -- likely the DYING contract (L-40)"
            o, hi, lo = (float(h["Open"].iloc[-1]), float(h["High"].iloc[-1]), float(h["Low"].iloc[-1]))
            if o == hi == lo == last:
                flag += "  <<< FLAT O=H=L=C: dying-contract tell, not a quiet session"
            print("    %-11s bar %s  close %10.4f  vol %9s%s" % (t, bar, last, format(vol, ","), flag))
        except Exception as e:
            print("    %-11s ERROR %s" % (t, str(e)[:50]))

    if "GC=F" in tick and "GCZ26.CMX" in tick:
        gap = tick["GCZ26.CMX"] - tick["GC=F"]
        print("\n  --- BASIS (L-19: print BOTH, always) ---")
        print("    GC=F %10.4f   GCZ26.CMX %10.4f   gap %+.2f (%+.3f%%)"
              % (tick["GC=F"], tick["GCZ26.CMX"], gap, 100 * gap / tick["GC=F"]))
        print("    %s" % ("IDENTICAL -- GC=F's current bar IS GCZ26." if abs(gap) < 1e-6
                          else "DIVERGENT -- name the basis on every figure you quote."))

    print("\n  --- MIDAS-06 GOLD LEG (branch b settles TODAY; branch a's yield leg is Mon 8/31) ---")
    for t in ["GC=F", "GCZ26.CMX"]:
        if t in tick:
            print("    %-11s %10.4f   vs $%.2f: %+.2f%%   vs $%.2f: %+.2f%%   -> (a) %s | (b) %s"
                  % (t, tick[t], MIDAS06_A, 100 * (tick[t] / MIDAS06_A - 1),
                     MIDAS06_B, 100 * (tick[t] / MIDAS06_B - 1),
                     "PASS" if tick[t] >= MIDAS06_A else "FAIL",
                     "PASS" if tick[t] < MIDAS06_B else "FAIL"))
    print("    REMINDER: (d) INDETERMINATE is Will-ruled legitimate (row 68). Do not patch the spec.")

    print("\n  --- I2 PGM RESIDUAL, every candidate basis pair (KB-081; gold denominator is forked) ---")
    pairs = [("A  GCZ26 both ends (internally consistent)", "GCZ26.CMX", PRIOR["GCZ26.CMX"]),
             ("B  GC=F history basis (CROSS-ROLL, bound only)", "GC=F", PRIOR["GC=F"])]
    fired = []
    for pname, gt, g0 in pairs:
        if gt not in tick:
            continue
        g = 100 * (tick[gt] / g0 - 1)
        line = "    %-46s gold %+6.2f%% |" % (pname, g)
        for pt in ["PA=F", "PL=F"]:
            if pt not in tick:
                continue
            c = PGM[pt]
            chg = 100 * (tick[pt] / PRIOR[pt] - 1)
            resid = chg - (c["beta"] * g + c["icept"])
            sig = resid / c["sigma"]
            line += "  %s %+6.2f%% = %+5.2fsd" % (pt, chg, sig)
            if abs(sig) >= I2_TRIGGER_SIGMA:
                fired.append((pname, pt, sig))
        print(line)

    pd_lead = ("PA=F" in tick and "PL=F" in tick
               and (tick["PA=F"] / PRIOR["PA=F"]) > (tick["PL=F"] / PRIOR["PL=F"]))
    print("\n    Pd leads Pt: %s" % ("YES" if pd_lead else "NO"))
    if fired and pd_lead:
        print("    >>> I2 RE-OPEN CONDITION (b) LEGS ARE MET on %d basis pair(s): %s"
              % (len(fired), ", ".join("%s %s %+.2fsd" % f for f in fired)))
        print("    >>> That is n=3 (after 2026-08-04). The report's Sec.7: n=3 DEMANDS A MECHANISM,")
        print("        not another filing. Route to HAWK and escalate to PROME.")
        print("    >>> STILL NOT A FIRING unless these are SETTLED closes -- and per L-37 a T+1")
        print("        re-pull is owed even then. NO score moves from this script.")
    else:
        print("    >>> Condition (b) NOT met on this pull. Absence of a firing, not evidence for anything.")

    print("\n  ⛔ NOTHING GRADED, NOTHING FIRED, NO SCORE MOVED. A human reads this and decides.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
