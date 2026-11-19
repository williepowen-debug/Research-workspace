#!/usr/bin/env python3
"""WQ-704 winter demand test (WATT, 2026-11-19). Reproducible from held files only.

Question: does the P1 letter's demand limb (EIA-930 PJM hour demand >= 97.0% of the
peak of the 24 hours before it, rounded to 1 dp -- power_watch.py / tape_scan.py rule)
carry information about price stress on its own?

Inputs (all in AGENTS/WATT/sources/, none fetched by this script):
  prices  DM2 rt_hrl_lmps PJM-RTO verified hourly: Sep 1-Oct 28 2025, Sep 1-Oct 28 2026,
          Nov 1-Dec 31 2025; DM2 5-min PJM-RTO Oct 23-Nov 14 11:00 EPT 2026 (verified
          where held, unverified otherwise).
  demand  EIA-930 respondent PJM type D, hourly, UTC stamps (pulled 2026-11-19).
Hour convention: EIA-930 stamps are ambiguous between hour-beginning and hour-ending
(tape_scan.py grades both); every table is computed under BOTH and reported.
Run from repo root:  python3 AGENTS/WATT/research/2026-11-19_winter_demand_test.py
"""
import json, sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from collections import defaultdict

S = "AGENTS/WATT/sources/"
EPT, UTC = ZoneInfo("America/New_York"), timezone.utc
MET = 97.0


def items(path):
    d = json.load(open(S + path))
    return d["items"] if isinstance(d, dict) else d


def ept_to_utc(rows, key="datetime_beginning_ept"):
    """EPT naive stamps -> UTC; the fall-back duplicate hour gets fold 0 then 1."""
    seen, out = defaultdict(int), {}
    for r in sorted(rows, key=lambda r: r[key]):
        k = r[key]
        naive = datetime.fromisoformat(k)
        u = naive.replace(tzinfo=EPT, fold=min(seen[k], 1)).astimezone(UTC)
        seen[k] += 1
        out[u] = float(r["total_lmp_rt"])
    return out


def demand(*paths):
    out = {}
    for p in paths:
        for r in items(p):
            if r.get("value") in (None, ""):
                continue
            out[datetime.strptime(r["period"][:13], "%Y-%m-%dT%H").replace(tzinfo=UTC)] = float(r["value"])
    return out


def pct(dm, h):
    if h not in dm:
        return None
    prior = [dm.get(h - timedelta(hours=k)) for k in range(1, 25)]
    prior = [p for p in prior if p is not None]
    if len(prior) < 20:
        return None
    return round(dm[h] / max(prior) * 100.0, 1)


def limb(dm, h_utc, conv):
    """conv 'HB': EIA stamp == price hour start (UTC); 'HE': EIA stamp == price hour end."""
    return pct(dm, h_utc if conv == "HB" else h_utc + timedelta(hours=1))


def table(name, prices, dm, thresholds=(200, 500, 1000)):
    res = {}
    for conv in ("HB", "HE"):
        rows = [(h, p, limb(dm, h, conv)) for h, p in prices.items()]
        rows = [(h, p, d) for h, p, d in rows if d is not None]
        n = len(rows)
        D = [r for r in rows if r[2] >= MET]
        nD = [r for r in rows if r[2] < MET]
        days = {h.astimezone(EPT).date() for h, _, _ in rows}
        days_D = {h.astimezone(EPT).date() for h, _, d in D}
        out = {"n": n, "D": len(D), "D_rate": len(D) / n if n else 0,
               "days": len(days), "days_with_D": len(days_D)}
        # hour-of-day profile of D hours (EPT hour beginning)
        hod = defaultdict(int)
        for h, _, _ in D:
            hod[h.astimezone(EPT).hour] += 1
        out["D_hours_by_ept_hour"] = dict(sorted(hod.items()))
        for t in thresholds:
            s = [r for r in rows if r[1] >= t]
            sD = [r for r in s if r[2] >= MET]
            pD = len(sD) / len(D) if D else 0
            pN = (len(s) - len(sD)) / len(nD) if nD else 0
            # absolute-load comparator at the SAME firing count as the limb
            k = len(D)
            ranked = sorted(rows, key=lambda r: dm_val(dm, r[0], conv), reverse=True)[:k]
            sA = sum(1 for r in ranked if r[1] >= t)
            out[f">={t}"] = {"spike_hours": len(s), "with_D": len(sD), "P_spike_given_D": pD,
                             "P_spike_given_notD": pN, "lift": (pD / pN) if pN else None,
                             "recall": len(sD) / len(s) if s else None,
                             "abs_load_topk_spikes": sA, "abs_load_topk_precision": sA / k if k else 0}
        res[conv] = out
    return {name: res}


def dm_val(dm, h, conv):
    return dm.get(h if conv == "HB" else h + timedelta(hours=1), 0)


def fivemin_runs(prices5):
    """Hours (UTC, floored) containing >=2 consecutive 5-min prints >= $1,000 (P1 price limb)."""
    ks = sorted(prices5)
    hits = set()
    for a, b in zip(ks, ks[1:]):
        if b - a == timedelta(minutes=5) and prices5[a] >= 1000 and prices5[b] >= 1000:
            for x in (a, b):
                hits.add(x.replace(minute=0))
    return hits


def main():
    dm = demand("2026-10-29/eia930-pjm-demand-0901-1028-2025.json",
                "2026-10-29/eia930-pjm-demand-0901-1028-2026.json",
                "2026-11-19/eia930-pjm-demand-1030-1231-2025.json",
                "2026-11-19/eia930-pjm-demand-1021-1119-2026.json",
                "2026-11-19/eia930-pjm-demand-dec2024-feb2025.json")
    out = {}
    out.update(table("autumn_2025_Sep1_Oct28_hourly", ept_to_utc(items("2026-10-29/dm2-rt-hrl-0901-1028-2025.json")), dm))
    out.update(table("autumn_2026_Sep1_Oct28_hourly", ept_to_utc(items("2026-10-29/dm2-rt-hrl-0901-1028-2026.json")), dm))
    out.update(table("winter_2025_Nov1_Dec31_hourly", ept_to_utc(items("2026-11-05/dm2-rt-hrl-1101-1231-2025.json")), dm))

    # 5-min Oct 23 - Nov 14 2026: verified first, unverified fills the rest
    p5 = {}
    for f in ["2026-11-05/dm2-fivemin-1029-1105.json", "2026-11-11/dm2-fivemin-1105-1111.json",
              "2026-11-14/dm2-fivemin-1111-1114.json", "2026-10-29/dm2-fivemin-1023-1029.json"]:
        p5.update(ept_to_utc(items(f)))
    for f in ["2026-11-05/dm2-fivemin-verified-1023-1027.json", "2026-11-05/dm2-fivemin-verified-1028-1105.json",
              "2026-11-11/dm2-fivemin-verified-1104-1111.json", "2026-11-14/dm2-fivemin-verified-1109-1114.json"]:
        p5.update(ept_to_utc(items(f)))
    run_hours = fivemin_runs(p5)
    hourly_max = defaultdict(float)
    for k, v in p5.items():
        hk = k.replace(minute=0)
        hourly_max[hk] = max(hourly_max.get(hk, -1e9), v)
    five = {}
    for conv in ("HB", "HE"):
        rows = [(h, m, limb(dm, h, conv)) for h, m in hourly_max.items()]
        rows = [r for r in rows if r[2] is not None]
        D = [r for r in rows if r[2] >= MET]
        nD = [r for r in rows if r[2] < MET]
        five[conv] = {"n_hours": len(rows), "D": len(D),
                      "price_limb_run_hours": sorted(h.astimezone(EPT).strftime("%m-%d %H:00") for h in run_hours),
                      "run_hours_with_D": sorted(h.astimezone(EPT).strftime("%m-%d %H:00 EPT") + f" {limb(dm, h, conv)}%" for h in run_hours if (limb(dm, h, conv) or 0) >= MET),
                      "run_hours_without_D": sorted(h.astimezone(EPT).strftime("%m-%d %H:00 EPT") + f" {limb(dm, h, conv)}%" for h in run_hours if (limb(dm, h, conv) or 0) < MET)}
        for t in (500, 1000):
            s = [r for r in rows if r[1] >= t]
            sD = [r for r in s if r[2] >= MET]
            five[conv][f"hourmax>={t}"] = {"hours": len(s), "with_D": len(sD),
                                           "P_given_D": len(sD) / len(D) if D else 0,
                                           "P_given_notD": (len(s) - len(sD)) / len(nD) if nD else 0}
    five["n_5min_prints"] = len(p5)
    five["span"] = [min(p5).astimezone(EPT).isoformat(), max(p5).astimezone(EPT).isoformat()]
    out["fivemin_2026_Oct23_Nov14"] = five

    # demand-only: how often the limb is met in a real winter (no prices held)
    for name, a, b in (("demand_only_Dec2024_Feb2025", "2024-12-02", "2025-03-01"),
                       ("demand_only_Nov1_Nov19_2026", "2026-11-01", "2026-11-19T15")):
        lo = datetime.fromisoformat(a).replace(tzinfo=UTC)
        hi = datetime.fromisoformat(b).replace(tzinfo=UTC)
        hrs = [h for h in dm if lo <= h < hi]
        ps = [(h, pct(dm, h)) for h in hrs]
        ps = [(h, p) for h, p in ps if p is not None]
        D = [(h, p) for h, p in ps if p >= MET]
        hod = defaultdict(int)
        for h, _ in D:
            hod[h.astimezone(EPT).hour] += 1
        days = {h.astimezone(EPT).date() for h, _ in ps}
        dD = {h.astimezone(EPT).date() for h, _ in D}
        top = sorted(ps, key=lambda x: dm[x[0]], reverse=True)[:5]
        out[name] = {"n": len(ps), "D": len(D), "D_rate": len(D) / len(ps) if ps else 0,
                     "days": len(days), "days_with_D": len(dD),
                     "D_by_ept_hour_of_stamp": dict(sorted(hod.items())),
                     "top5_load_hours": [(h.isoformat(), dm[h], p) for h, p in top]}
    json.dump(out, sys.stdout, indent=1, default=str)


if __name__ == "__main__" and "--conditional" not in sys.argv:
    main()


def conditional(prices, dm, t, conv="HB"):
    """Within peak hours (07-09 and 17-21 EPT) and within load terciles of those hours:
    spike rate with the limb met vs not met. Tests whether the limb adds anything
    once time of day and absolute load are held roughly fixed."""
    rows = []
    for h, p in prices.items():
        d = limb(dm, h, conv)
        hr = h.astimezone(EPT).hour
        if d is None or not (7 <= hr <= 9 or 17 <= hr <= 21):
            continue
        rows.append((h, p, d, dm_val(dm, h, conv)))
    rows.sort(key=lambda r: r[3])
    n = len(rows)
    out = {"peak_hours": n}
    for i, name in enumerate(("low", "mid", "high")):
        seg = rows[i * n // 3:(i + 1) * n // 3]
        D = [r for r in seg if r[2] >= MET]
        N = [r for r in seg if r[2] < MET]
        out[name] = {"load_range_MW": [seg[0][3], seg[-1][3]],
                     "D": len(D), "D_spikes": sum(r[1] >= t for r in D),
                     "notD": len(N), "notD_spikes": sum(r[1] >= t for r in N)}
    return out


if __name__ == "__main__" and "--conditional" in sys.argv:
    dm = demand("2026-10-29/eia930-pjm-demand-0901-1028-2025.json",
                "2026-10-29/eia930-pjm-demand-0901-1028-2026.json",
                "2026-11-19/eia930-pjm-demand-1030-1231-2025.json")
    res = {}
    for name, f, ts in (("autumn_2026", "2026-10-29/dm2-rt-hrl-0901-1028-2026.json", (200, 500, 1000)),
                        ("winter_2025", "2026-11-05/dm2-rt-hrl-1101-1231-2025.json", (100, 200)),
                        ("autumn_2025", "2026-10-29/dm2-rt-hrl-0901-1028-2025.json", (200,))):
        pr = ept_to_utc(items(f))
        for t in ts:
            for conv in ("HB", "HE"):
                res[f"{name} >=${t} {conv}"] = conditional(pr, dm, t, conv)
    json.dump(res, sys.stdout, indent=1, default=str)
