#!/usr/bin/env python3
"""Floor-controlled Channel-1 transmission test (MARCO, 2026-07-31).

Spec + pre-committed thresholds: thesis/PREREG_2026-07-31_floor_controlled_channel1.md
DO NOT edit the strata or thresholds here — they are pre-registered. This script
only measures.

Design: restrict to federal-minimum ($7.25, no step) states so the statutory floor
cannot bind, then compute per state
    DID = YoY%d AHE(Leisure & Hospitality) - YoY%d AHE(Retail Trade)
and compare the high-immigrant-share stratum against the low-immigrant-share one.
Retail Trade is the floor-matched control sector.
"""
import json
import sys
import time
from pathlib import Path

import requests

API = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
OUT = Path(__file__).resolve().parents[1] / "research" / "floor_controlled_raw.json"

FIPS = {"AL": "01", "AZ": "04", "CA": "06", "FL": "12", "GA": "13", "IN": "18",
        "KS": "20", "KY": "21", "LA": "22", "MS": "28", "NC": "37", "OK": "40",
        "SC": "45", "TN": "47", "TX": "48", "UT": "49", "WV": "54"}

# Pre-registered strata (fixed 2026-07-31 before any pull)
HIGH_IMM_725 = ["TX", "GA", "NC", "UT", "OK", "KS"]
LOW_IMM_725 = ["TN", "AL", "MS", "KY", "SC", "WV", "IN", "LA"]
DIAGNOSTIC = ["FL", "CA", "AZ"]          # floor stepped in window — NOT scored

LH = "70000000"      # Leisure & Hospitality
RT = "40000000"      # Trade, Transportation & Utilities (primary control, Amendment 1)
EH = "65000000"      # Education & Health Services (robustness control, Amendment 1)
DT = "03"            # Average hourly earnings, all employees


def state_series(st, ind):
    return f"SMU{FIPS[st]}00000{ind}{DT}"


def fetch(series_ids, startyear="2024", endyear="2026"):
    """BLS v2 unregistered: <=25 series/request. Returns {series_id: {(yr,mo): value}}."""
    out = {}
    for i in range(0, len(series_ids), 25):
        batch = series_ids[i:i + 25]
        body = json.dumps({"seriesid": batch, "startyear": startyear, "endyear": endyear})
        r = requests.post(API, data=body,
                          headers={"Content-type": "application/json"}, timeout=120)
        r.raise_for_status()
        js = r.json()
        if js.get("status") != "REQUEST_SUCCEEDED":
            print(f"  ! BLS status={js.get('status')} msg={js.get('message')}")
        for s in js.get("Results", {}).get("series", []):
            vals = {}
            for d in s.get("data", []):
                if d.get("period", "").startswith("M") and d["period"] != "M13":
                    try:
                        vals[(int(d["year"]), int(d["period"][1:]))] = float(d["value"])
                    except ValueError:
                        pass
            out[s["seriesID"]] = vals
        time.sleep(1)
    return out


def yoy(vals, year=2026, month=6):
    """June-over-June percent change. None if either endpoint is missing."""
    cur = vals.get((year, month))
    pri = vals.get((year - 1, month))
    if cur is None or pri is None or pri == 0:
        return None
    return (cur / pri - 1.0) * 100.0


def main():
    states = HIGH_IMM_725 + LOW_IMM_725 + DIAGNOSTIC
    ids = [state_series(s, LH) for s in states] + [state_series(s, RT) for s in states]
    ids += [state_series(s, EH) for s in states]
    ids += ["CES7000000003", "CES4000000003", "CES6500000003"]

    print(f"Requesting {len(ids)} BLS series…")
    data = fetch(ids)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({k: {f"{y}-{m:02d}": v for (y, m), v in d.items()}
                               for k, d in data.items()}, indent=1))

    nat_lh = yoy(data.get("CES7000000003", {}))
    nat_rt = yoy(data.get("CES4000000003", {}))
    print(f"\nNATIONAL Jun26/Jun25: L&H {nat_lh:+.2f}%  Retail {nat_rt:+.2f}%  "
          f"DID {nat_lh - nat_rt:+.2f}pp\n" if nat_lh and nat_rt else "\nNATIONAL: missing\n")

    rows = {}
    print(f"{'St':<4}{'stratum':<10}{'L&H YoY':>9}{'TTU YoY':>12}{'DID(pp)':>10}{'DIDvsE&H':>11}")
    print("-" * 56)
    for st in states:
        strat = ("HIGH-imm" if st in HIGH_IMM_725 else
                 "low-imm" if st in LOW_IMM_725 else "DIAGnostic")
        lh = yoy(data.get(state_series(st, LH), {}))
        rt = yoy(data.get(state_series(st, RT), {}))
        did = (lh - rt) if (lh is not None and rt is not None) else None
        eh = yoy(data.get(state_series(st, EH), {}))
        did_eh = (lh - eh) if (lh is not None and eh is not None) else None
        rows[st] = {"stratum": strat, "lh": lh, "rt": rt, "did": did,
                    "eh": eh, "did_eh": did_eh}
        f = lambda v, s="%": f"{v:+.2f}{s}" if v is not None else "   n/a"
        print(f"{st:<4}{strat:<10}{f(lh):>9}{f(rt):>12}{f(did,'pp'):>10}{f(did_eh,'pp'):>11}")

    def summarize(group, label, key="did"):
        got = [rows[s][key] for s in group if rows[s][key] is not None]
        miss = [s for s in group if rows[s][key] is None]
        if not got:
            print(f"\n{label}: NO DATA ({len(miss)}/{len(group)} missing)")
            return None, 1.0
        mean = sum(got) / len(got)
        pos = sum(1 for d in got if d > 0)
        print(f"\n{label}: n={len(got)}/{len(group)}  mean DID {mean:+.2f}pp  "
              f"positive {pos}/{len(got)} ({pos/len(got)*100:.0f}%)"
              + (f"  MISSING: {','.join(miss)}" if miss else ""))
        return mean, len(miss) / len(group)

    print("\n" + "=" * 60)
    hi_mean, hi_missrate = summarize(HIGH_IMM_725, "HIGH-immigrant $7.25 stratum")
    lo_mean, _ = summarize(LOW_IMM_725, "LOW-immigrant $7.25 stratum")
    summarize(DIAGNOSTIC, "DIAGNOSTIC (floor stepped — NOT scored)")

    print("\n" + "=" * 60)
    print("PRE-REGISTERED SCORING")
    print("=" * 60)
    if hi_missrate > 0.40:
        print(f"DATA-QUALITY ABORT: {hi_missrate*100:.0f}% of high-immigrant stratum "
              f"missing Retail AHE (>40% threshold). Primary test NOT scored.")
        return 2
    tx = rows["TX"]["did"]
    gap = (hi_mean - lo_mean) if (hi_mean is not None and lo_mean is not None) else None
    got = [rows[s]["did"] for s in HIGH_IMM_725 if rows[s]["did"] is not None]
    pos_frac = sum(1 for d in got if d > 0) / len(got)

    c1 = hi_mean is not None and hi_mean >= 1.5
    c2 = pos_frac >= 0.70
    c3 = gap is not None and gap >= 1.5
    print(f"  CONFIRM c1 (hi mean >= +1.5pp):      {hi_mean:+.2f}pp   {'PASS' if c1 else 'FAIL'}")
    print(f"  CONFIRM c2 (>=70% positive):         {pos_frac*100:.0f}%      {'PASS' if c2 else 'FAIL'}")
    print(f"  CONFIRM c3 (hi-lo gap >= +1.5pp):    {gap:+.2f}pp   {'PASS' if c3 else 'FAIL'}"
          if gap is not None else "  CONFIRM c3: n/a")
    n1 = hi_mean is not None and hi_mean < 0.5
    n2 = gap is not None and gap < 0.5
    n3 = tx is not None and tx <= 0
    print(f"  NULL n1 (hi mean < +0.5pp):          {'TRIGGERED' if n1 else 'no'}")
    print(f"  NULL n2 (hi-lo gap < 0.5pp):         {'TRIGGERED' if n2 else 'no'}")
    print(f"  NULL n3 (TX DID <= 0):               {'TRIGGERED' if n3 else 'no'}"
          + (f"  [TX={tx:+.2f}pp]" if tx is not None else "  [TX n/a]"))

    verdict = ("CONFIRMED" if (c1 and c2 and c3) else
               "NULL / FALSIFIED" if (n1 or n2 or n3) else "AMBIGUOUS (= NOT CONFIRMED)")
    print(f"\n  >>> VERDICT: {verdict}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
