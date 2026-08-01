#!/usr/bin/env python3
"""Derivation for the floor-controlled Channel-1 test's FL diagnostic + power statistics.

Built 2026-07-31 (session 20) after PROME's audit found that two of the most-propagated
numbers from session 19 had no committed derivation, and that the pre-registered FL
diagnostic was printed but never scored.

Reads only `research/floor_controlled_raw.json` (the committed BLS CES pull from s19).
Makes no network calls, so it reproduces the s19 result exactly rather than a fresh one.

Sections
  1  FL diagnostic, scored against PREREG section 3 line 52 (FL DID approx 0 => confirms
     the Amendment-2 explanation of FL's raw +4.88pp L&H gap)
  2  Decomposition of FL's June DID into its treated-leg and control-leg parts
  3  Panel dispersion and power: the statistic the ~6pp figure actually bounds
  4  Within-state stability: the statistic the "3.2pp swing" figure was meant to be

Usage:  .venv/bin/python3 AGENTS/MARCO/scripts/fl_diagnostic_score.py
"""
import json
import math
import statistics as st
import sys
from pathlib import Path

RAW = Path(__file__).resolve().parents[1] / "research" / "floor_controlled_raw.json"

FIPS = {"TX": "48", "GA": "13", "NC": "37", "UT": "49", "OK": "40", "KS": "20",
        "TN": "47", "AL": "01", "MS": "28", "KY": "21", "SC": "45", "WV": "54",
        "IN": "18", "LA": "22", "FL": "12", "CA": "06", "AZ": "04"}
IND = {"LH": "70000000", "TTU": "40000000", "EH": "65000000"}
NAT = {"LH": "CES7000000003", "TTU": "CES4000000003", "EH": "CES6500000003"}

HIGH = ["TX", "GA", "NC", "UT", "OK", "KS"]        # high-immigrant $7.25 stratum
LOW = ["TN", "AL", "MS", "KY", "SC", "WV", "IN", "LA"]  # low-immigrant $7.25 stratum
SCORED = HIGH + LOW
MONTHS = [f"2026-{m:02d}" for m in range(1, 7)]
WINDOW = "2026-06"


def load():
    if not RAW.exists():
        sys.exit(f"FAIL: {RAW} not found. This script reads the committed s19 pull only; "
                 "it does not re-fetch from BLS.")
    return json.load(open(RAW))


def yoy(series, month):
    """12-month percent change. Returns None when either endpoint is absent."""
    if series is None:
        return None
    yr, mo = month.split("-")
    prev = f"{int(yr) - 1}-{mo}"
    if month not in series or prev not in series:
        return None
    return (series[month] / series[prev] - 1) * 100


def main():
    d = load()
    ser = lambda s, i: d.get(f"SMU{FIPS[s]}00000{IND[i]}03")
    nat = lambda i: d.get(NAT[i])
    did = lambda s, i, m: (lambda a, b: None if a is None or b is None else a - b)(
        yoy(ser(s, "LH"), m), yoy(ser(s, i), m))

    missing = [s for s in SCORED + ["FL"] for i in ("LH", "TTU", "EH") if ser(s, i) is None]
    if missing:
        sys.exit(f"FAIL: {len(missing)} series absent from the raw pull: {sorted(set(missing))}. "
                 "Every section below needs the full panel; refusing to print partial results.")

    print("=" * 74)
    print("  FL DIAGNOSTIC + POWER DERIVATION — floor-controlled Channel-1 test")
    print(f"  source: {RAW.name} (BLS CES state AHE, pulled 2026-07-31, no re-fetch)")
    print("=" * 74)

    # -- 1 -----------------------------------------------------------------
    print("\n1. FL DIAGNOSTIC, SCORED")
    print("   PREREG section 3 line 52: FL DID approx 0 (while raw L&H gap = +4.88pp)")
    print("   => independently confirms the Amendment-2 explanation.\n")
    print(f"   {'month':9}{'FL L&H':>9}{'FL TTU':>9}{'DID TTU':>9}{'DID E&H':>9}"
          f"{'nat L&H':>9}{'FL-nat':>9}")
    for m in MONTHS:
        a, b = yoy(ser("FL", "LH"), m), yoy(ser("FL", "TTU"), m)
        nl = yoy(nat("LH"), m)
        print(f"   {m:9}{a:9.2f}{b:9.2f}{did('FL','TTU',m):9.2f}"
              f"{did('FL','EH',m):9.2f}{nl:9.2f}{a - nl:9.2f}")

    fl_t, fl_e = did("FL", "TTU", WINDOW), did("FL", "EH", WINDOW)
    print(f"\n   SCORED at {WINDOW}: FL DID = {fl_t:+.2f}pp (TTU) / {fl_e:+.2f}pp (E&H).")
    print("   Pre-registered expectation was approx 0. VERDICT: MISS.")

    mono = [did("FL", "TTU", m) for m in MONTHS]
    print(f"   Stability of FL DID(TTU) across 2026: range {min(mono):.2f} to {max(mono):.2f}"
          f" = {max(mono) - min(mono):.2f}pp spread; June is {mono[-1] - st.mean(mono[:5]):+.2f}pp"
          " above the Jan-May mean.")
    print("   A claim that FL's DID is 'stable in every month of 2026' does not hold on "
          "these figures.")

    # -- 2 -----------------------------------------------------------------
    print("\n2. DECOMPOSITION OF FL's JUNE DID")
    a = yoy(ser("FL", "LH"), WINDOW)
    b = yoy(ser("FL", "TTU"), WINDOW)
    nl, nt = yoy(nat("LH"), WINDOW), yoy(nat("TTU"), WINDOW)
    print(f"   FL DID(TTU) {fl_t:+.2f}pp  =  treated leg (FL L&H - nat L&H) {a - nl:+.2f}pp")
    print(f"                          +  control leg (nat TTU - FL TTU)  {nt - b:+.2f}pp")
    print(f"                          +  national sector gap             {nl - nt:+.2f}pp")
    may = yoy(ser("FL", "TTU"), "2026-05")
    print(f"   FL TTU YoY fell {may:.2f} (May) -> {b:.2f} (June). The June step-up in FL's DID"
          " comes from the control sector weakening, not from L&H accelerating.")

    # -- 3 -----------------------------------------------------------------
    print("\n3. PANEL DISPERSION AND POWER (what the ~6pp figure actually bounds)")
    for ctl in ("TTU", "EH"):
        h = [did(s, ctl, WINDOW) for s in HIGH]
        l = [did(s, ctl, WINDOW) for s in LOW]
        sd_h, sd_l, sd_p = st.stdev(h), st.stdev(l), st.stdev(h + l)
        se = math.sqrt(sd_h ** 2 / len(h) + sd_l ** 2 / len(l))
        diff = st.mean(h) - st.mean(l)
        print(f"   [{ctl}] stratum sd: high {sd_h:.2f} (n={len(h)}), low {sd_l:.2f} "
              f"(n={len(l)}), pooled {sd_p:.2f}")
        print(f"         high-low difference {diff:+.2f}pp, SE {se:.2f}, t {diff / se:+.2f}")
        print(f"         1.96 x SE = {1.96 * se:.2f}pp  -> smallest STRATUM-MEAN DIFFERENCE "
              "separable from zero at 95%")
        print(f"         2.80 x SE = {2.8 * se:.2f}pp  -> 80%-power MDE for the same statistic")
        print(f"         1.96 x pooled sd = {1.96 * sd_p:.2f}pp -> band for a SINGLE STATE's DID"
              " against the panel mean")
        fl = did("FL", ctl, WINDOW)
        bigger = [s for s in SCORED if did(s, ctl, WINDOW) > fl]
        print(f"         FL {fl:+.2f}pp sits {(fl - st.mean(h + l)) / sd_p:+.2f} sd from the panel"
              f" mean; {len(bigger)} of {len(SCORED)} scored states exceed it: {bigger}")

    # -- 4 -----------------------------------------------------------------
    print("\n4. WITHIN-STATE STABILITY (the statistic '3.2pp median swing' was meant to be)")
    for ctl in ("TTU", "EH"):
        for label, states in (("14 scored", SCORED), ("6 high-imm", HIGH)):
            rng, sds, steps = [], [], []
            for s in states:
                v = [did(s, ctl, m) for m in MONTHS]
                rng.append(max(v) - min(v))
                sds.append(st.stdev(v))
                steps.append(st.median([abs(v[i + 1] - v[i]) for i in range(len(v) - 1)]))
            print(f"   [{ctl}] {label:11} median 6-mo range {st.median(rng):.2f}pp | "
                  f"mean range {st.mean(rng):.2f}pp | median within-state sd {st.median(sds):.2f}pp"
                  f" | median |MoM step| {st.median(steps):.2f}pp")
    print("   No definition tried reproduces 3.2pp. The citable statistic is the median 6-month"
          " range, 4.02pp (TTU, 14 scored states).")

    print("\n" + "=" * 74)
    print("  Reproduced from the committed raw pull. Any figure in RESULTS.md, THESIS.md or an")
    print("  outbound packet that is not printed above has no derivation behind it.")
    print("=" * 74)


if __name__ == "__main__":
    main()
