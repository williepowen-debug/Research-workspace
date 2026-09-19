#!/usr/bin/env python3
"""statcan_travel.py — Canadian-resident return trips from the US, AIR vs LAND-AUTO.

WHY THIS EXISTS
---------------
Built 2026-09-19 (session 27). MARCO had been reading these figures by hand off
StatCan's *Daily* releases; no table id, vector id or puller was ever recorded, so
`ID-01` — the registered identification condition for the tariff->sentiment channel —
could not be recomputed or audited. It now can.

THE SERIES (both are LEADING INDICATORS, daily frequency, ~2-week lag)
  AIR   PID 24-10-0056, coord 1.80.1.0.0.0.0.0.0.0  -> vector v1324883057
        "Canadian residents returning from the United States of America, air"
  LAND  PID 24-10-0057, coord 125.65.1.3.3.0.0.0.0.0 -> vector v1545883120
        Canada / all licence plates / Automobiles / Canadian resident visitors
        returning / Travellers

⚠️ These are the LEADING-INDICATOR cubes, NOT 24-10-0053 ("International travellers
entering or returning to Canada"). 24-10-0053 is the fuller table but lags ~3 months
(end 2026-06 when this was written) and its CSV is ~450 MB. 24-10-0005, which has
ideal category names, is TERMINATED at 2021-12 — do not reach for it.

⚠️ DAILY DATA. Months are summed, and a month is DROPPED unless every calendar day is
present — a partial month silently understates a monthly total, which is exactly the
kind of quietly-wrong aggregate that survives every structural check.

REPRODUCTION CHECK (why you can trust this): on the 2026-09-19 build these vectors
reproduced MARCO's four hand-carried ID-01 baseline figures to within 0.05pp —
Jun-26 auto -29.61 (carried -29.6) / air -25.03 (-25.0); Jul-26 auto -28.85 (-28.9) /
air -26.83 (-26.8). Re-run `--verify` to re-assert that before trusting a new pull.

Output: baselines/statcan_canadian_return.tsv — monthly levels, YoY, 2-yr stacks and
the auto-minus-air GAP that ID-01 is written on. Two-clock header dated by NEWEST
DATA MONTH.

Constraints: stdlib only. Fail loudly.
"""
import calendar
import collections
import datetime
import json
import pathlib
import sys
import urllib.request

OUT = pathlib.Path(__file__).resolve().parents[1] / "baselines" / "statcan_canadian_return.tsv"
WDS = "https://www150.statcan.gc.ca/t1/wds/rest/getDataFromCubePidCoordAndLatestNPeriods"

SERIES = [
    ("AIR",       24100056, "1.80.1.0.0.0.0.0.0.0"),
    ("LAND_AUTO", 24100057, "125.65.1.3.3.0.0.0.0.0"),
]

# Hand-carried figures this puller must reproduce (see module docstring).
BASELINE = {("2026-06", "LAND_AUTO"): -29.6, ("2026-06", "AIR"): -25.0,
            ("2026-07", "LAND_AUTO"): -28.9, ("2026-07", "AIR"): -26.8}


def pull(latest_n=1100):
    req = urllib.request.Request(
        WDS,
        data=json.dumps([{"productId": p, "coordinate": c, "latestN": latest_n}
                         for _, p, c in SERIES]).encode(),
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0 MARCO"})
    with urllib.request.urlopen(req, timeout=180) as r:
        js = json.load(r)
    if len(js) != len(SERIES):
        raise RuntimeError(f"WDS returned {len(js)} objects, expected {len(SERIES)}")
    daily = {}
    for (name, pid, _), o in zip(SERIES, js):
        if o.get("status") != "SUCCESS":
            raise RuntimeError(f"{name} (PID {pid}): {str(o)[:200]}")
        pts = o["object"]["vectorDataPoint"]
        if not pts:
            raise RuntimeError(f"{name}: zero data points")
        daily[name] = {p["refPer"]: float(p["value"]) for p in pts}
    return daily


def to_monthly(daily):
    monthly = collections.defaultdict(dict)
    counts = collections.defaultdict(lambda: collections.defaultdict(int))
    for leg, d in daily.items():
        agg = collections.defaultdict(float)
        for day, v in d.items():
            agg[day[:7]] += v
            counts[leg][day[:7]] += 1
        for mo, v in agg.items():
            monthly[mo][leg] = v
    dropped = []
    for leg in counts:
        for mo, n in counts[leg].items():
            y, m = int(mo[:4]), int(mo[5:7])
            if n != calendar.monthrange(y, m)[1]:
                monthly[mo].pop(leg, None)
                dropped.append(f"{leg}:{mo}({n}d)")
    complete = {mo: v for mo, v in monthly.items() if len(v) == len(SERIES)}
    return complete, sorted(set(dropped))


def pct(monthly, leg, mo, lag):
    y, m = int(mo[:4]), int(mo[5:7])
    prev = f"{y-lag}-{m:02d}"
    if prev not in monthly or leg not in monthly[prev]:
        return None
    return (monthly[mo][leg] / monthly[prev][leg] - 1) * 100


def main():
    monthly, dropped = to_monthly(pull())
    months = sorted(monthly)
    if not months:
        raise RuntimeError("no complete months with both legs")

    if "--verify" in sys.argv:
        bad = []
        for (mo, leg), want in BASELINE.items():
            got = pct(monthly, leg, mo, 2)
            if got is None or abs(got - want) > 0.1:
                bad.append(f"{mo}/{leg}: carried {want}, got {got}")
        print("REPRODUCTION: " + ("FAIL -> " + "; ".join(bad) if bad
                                  else f"OK, all {len(BASELINE)} carried figures within 0.1pp"))
        if bad:
            sys.exit(1)

    rows = []
    for mo in months:
        cells = [mo]
        for leg in ("AIR", "LAND_AUTO"):
            cells += [f"{monthly[mo][leg]:.0f}",
                      *(("" if v is None else f"{v:.2f}") for v in
                        (pct(monthly, leg, mo, 1), pct(monthly, leg, mo, 2)))]
        a, r = pct(monthly, "LAND_AUTO", mo, 2), pct(monthly, "AIR", mo, 2)
        cells.append("" if a is None or r is None else f"{a-r:.2f}")
        rows.append("\t".join(cells))

    newest = months[-1]
    hdr = [
        "# MARCO StatCan — Canadian-resident return trips from the US, AIR vs LAND-AUTO.",
        "# AIR  = PID 24-10-0056 coord 1.80.1.0.0.0.0.0.0.0 (v1324883057) — leading indicator, daily.",
        "# LAND_AUTO = PID 24-10-0057 coord 125.65.1.3.3.0.0.0.0.0 (v1545883120) — leading indicator, daily.",
        "# ⚠️ Daily data summed to months; a month with any missing day is DROPPED, not partially summed.",
        "# ⚠️ gap_auto_minus_air is the quantity ID-01 is written on. NEGATIVE = land worse than air.",
        "# ⚠️ Score on the 2-yr STACK, not YoY — YoY is base-effect-corrupted (VX-MARCO-1.01's own rule).",
        f"# Last real data refresh: {newest}-01   <- NEWEST DATA MONTH, not the pull date (PAT-044).",
        f"# pulled={datetime.date.today()} months={len(months)} newest={newest}"
        + (f" dropped_incomplete={','.join(dropped)}" if dropped else ""),
        "period\tair\tair_yoy\tair_stack2y\tland_auto\tland_auto_yoy\tland_auto_stack2y\tgap_auto_minus_air",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(hdr + rows) + "\n")
    print(f"Wrote {OUT} ({OUT.stat().st_size:,}B) — {len(months)} months, newest {newest}")
    if dropped:
        print(f"  dropped incomplete: {', '.join(dropped)}")


if __name__ == "__main__":
    main()
