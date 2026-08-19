#!/usr/bin/env python3
"""BOND — boot-time recompute of LOAD-BEARING DERIVED statistics.

WHY THIS EXISTS
---------------
On 2026-08-18 BOND made six method errors in one day. **Every one was a
CARRIED figure; none was a fresh computation.** The existing boot protocol
already said "pull load-bearing figures LIVE" -- and BOND did. The gap was
that the instruction covered LEVELS (30Y, DFII10, HY OAS) and not DERIVED
statistics (runs, counts, percentiles, gate distances), which is where all
six errors lived.

It also encodes three specific lessons from that day:

  1. **Declare the aggregation, not just the series.** A run computed
     per-year and a run computed whole-series differ by 57% on the same
     data. Every line below prints its own method.
  2. **Refresh the RELEASE, not the series you happen to be grading.**
     DFII10 and DGS30 publish on the same H.15 cycle; BOND re-pulled one
     and left the other, leaving a live add-gate distance stale for hours.
     This pulls the whole set.
  3. **Bust the cache.** A 5-minute TTL is invisible to a reader and makes
     "I pulled it live" false without any error surfacing.

USAGE
-----
    python3 monitors/boot_recompute.py

Prints a stamped block for pasting/checking against STATUS. rc 0 always
(advisory); rc 2 on fetch failure, which is NOT a pass.
"""
from __future__ import annotations

import datetime as dt
import glob
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "FORGE" / "tools" / "market-data"))

# H.15 publishes these together -- always refresh as a SET.
H15_SET = ["DGS2", "DGS10", "DGS30", "DFII10", "T10YIE", "T5YIFR"]
CREDIT = ["BAMLH0A0HYM2", "BAMLH0A3HYC", "BAMLC0A0CM"]
GATES = {"DFII10": ("TLT add-gate", 2.50, "above"),
         "T5YIFR": ("inflation-unanchor red", 2.50, "above"),
         "DGS30": ("long-end level", 5.00, "above"),
         "DGS10": ("arm-#2 line", 4.50, "above")}


def bust_cache() -> int:
    n = 0
    for f in glob.glob(str(REPO / "FORGE/tools/market-data/.cache/fred_*.json")):
        try:
            os.remove(f); n += 1
        except OSError:
            pass
    return n


def main() -> int:
    import fetch  # noqa: E402
    print(f"[boot_recompute] cache entries busted: {bust_cache()}")
    print(f"[boot_recompute] run {dt.datetime.now():%Y-%m-%d %H:%M} local\n")

    series = {}
    try:
        for sid in H15_SET + CREDIT:
            raw = fetch.fred_fetch(sid, limit=20000)
            obs = sorted((o["date"], float(o["value"])) for o in raw if "error" not in o)
            if not obs:
                raise RuntimeError(f"{sid} returned no observations")
            series[sid] = obs
    except Exception as e:
        print(f"[boot_recompute] FETCH FAILURE: {e}", file=sys.stderr)
        print("[boot_recompute] rc=2 — NOT a pass.", file=sys.stderr)
        return 2

    print("== LEVELS (latest published) ==")
    for sid, obs in series.items():
        d, v = obs[-1]
        print(f"   {sid:14} {v:>8.2f}   [{d}]   n={len(obs):,}  span {obs[0][0]}→{obs[-1][0]}")

    print("\n== GATE DISTANCES (the numbers that drive decisions) ==")
    for sid, (label, thr, direction) in GATES.items():
        d, v = series[sid][-1]
        gap = (thr - v) if direction == "above" else (v - thr)
        state = "🔴 BREACHED" if gap <= 0 else f"{gap*100:>5.0f}bp away"
        print(f"   {sid:8} {v:>6.2f} vs {thr:>5.2f}  {label:24} {state}   [{d}]")

    print("\n== DERIVED: 30Y regime statistics ==")
    print("   method: DGS30 · session closes · threshold ≥5.00 · MAXIMAL run · WHOLE-SERIES scan")
    obs = series["DGS30"]
    y = dt.date.today().year
    cur = [x for x in obs if x[0].startswith(str(y))]
    days = sum(1 for _, v in cur if v >= 5.00)
    best = run = 0
    for _, v in obs:
        run = run + 1 if v >= 5.00 else 0
        best = max(best, run)
    live = 0
    for _, v in reversed(obs):
        if v >= 5.00:
            live += 1
        else:
            break
    print(f"   {y} days ≥5.00      : {days}   (of {len(cur)} sessions)")
    print(f"   current run         : {live} consecutive")
    print(f"   longest run, series : {best}")
    print(f"   {y} max             : {max(cur, key=lambda x: x[1])}")
    print(f"   series max          : {max(obs, key=lambda x: x[1])}")

    print("\n== DERIVED: percentiles (method: full-series rank of the latest close) ==")
    for sid in ("DGS30", "DGS10", "DFII10"):
        obs = series[sid]
        v = [x[1] for x in obs]
        cv = obs[-1][1]
        post = [x for d, x in obs if d >= "2010-01-01"]
        p_full = 100 * sum(1 for x in v if x < cv) / len(v)
        p_post = 100 * sum(1 for x in post if x < cv) / len(post) if post else float("nan")
        print(f"   {sid:8} {cv:>6.2f}  full {p_full:5.1f}th (n={len(v):,}, from {obs[0][0]})"
              f"   post-2010 {p_post:5.1f}th")

    print("\n⚠️  Paste-check these against STATUS. Any figure on a BOND surface that is NOT")
    print("    in this block, or disagrees with it, is a CARRIED figure — recompute or drop it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
