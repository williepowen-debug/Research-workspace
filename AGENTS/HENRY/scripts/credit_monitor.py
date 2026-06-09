#!/usr/bin/env python3
"""
HENRY Credit Early-Warning Monitor
===================================
Tracks the two signals that lead the HY OAS headline (which gaps, not grinds):

  1. CCC/HY DISPERSION  — the distressed tail (CCC) vs the index (HY). When CCC
     refuses to compress with HY, dispersion widens *underneath* a calm headline.
     This is the "trap loading" gauge. Source: FRED (live, no key needed).

  2. HY FUND-FLOW PROXY — HY ETF (HYG/JNK) price + volume + relative-to-IG (LQD).
     True flow data (ICI/Lipper/EPFR) isn't free/API-able; the robust public
     proxies are: ETF total-return turning negative, down-moves on volume surges
     (redemption pressure), and HY underperforming IG (HYG/LQD falling = the
     income bid stepping back). Source: yfinance.

Why these and not HY OAS itself: the income bid keeps HY pinned tight until it
suddenly breaks, so the headline is the LAST thing to move. Dispersion + flows
crack first. See HENRY STATUS "BOTTOM LINE" + MEMORY (2026-06-09).

Usage:
  python3 scripts/credit_monitor.py            # human-readable block
  python3 scripts/credit_monitor.py --json     # JSON for agents
  python3 scripts/credit_monitor.py --days 60  # longer FRED lookback

Run from anywhere; paths are resolved relative to the script.
Requires: yfinance (in repo .venv), internet for FRED + yfinance.
"""

import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone

# --- FRED series (OAS, in percent; multiply by 100 for bps) ---
FRED_SERIES = {
    "HY":  "BAMLH0A0HYM2",   # US High Yield index OAS (blended — BB/B dominate, masks the tail)
    "BB":  "BAMLH0A1HYBB",   # BB OAS (quality junk — the healthy top of HY)
    "CCC": "BAMLH0A3HYC",    # US CCC & lower OAS (the distressed tail)
}
# Primary bifurcation gauge = CCC - BB (distressed vs quality, NO overlap).
# CCC-HY dilutes the signal because HY *contains* CCC. See Will 2026-06-09 catch:
# blended HY tightened -52bps/yr while CCC WIDENED +27bps — a 9-month K-shaped split
# the index hid. Track the CCC-BB gap + ratio trajectory, not just the headline.

# --- ETF proxies ---
HY_ETFS = ["HYG", "JNK"]     # high-yield bond ETFs
IG_ETF = "LQD"               # investment-grade ETF (relative benchmark)

# --- Thresholds (calibratable; see THRESHOLDS note at bottom) ---
HY_OAS_YELLOW = 320          # bps — range-break above the tight band -> confirms bid giving way
DISPERSION_5D_WIDEN = 25     # bps — CCC-BB gap widening this much over 5d = acute tail stress
DISPERSION_63D_WIDEN = 40    # bps — CCC-BB gap widening this much over ~3mo = sustained bifurcation
                             # (ran ~+21bps/quarter through early 2026; +40 = a clear acceleration)
HYG_5D_DROP = -1.5           # % — HYG 5-day return below this = price stress
VOL_SURGE = 1.3              # x — latest volume vs 20d avg above this = flow/redemption pressure
HYG_LQD_5D_DROP = -0.75      # % — HY underperforming IG by this over 5d = credit-quality risk-off


def fetch_fred_series(series_id, days):
    """Pull a FRED series as [(date, value_float)] via the public CSV endpoint (no API key).

    Shells out to curl — this environment's urllib times out on FRED while curl
    works reliably (validated 2026-06-09)."""
    cosd = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}&cosd={cosd}"
    proc = subprocess.run(["curl", "-s", "--max-time", "30", url],
                          capture_output=True, text=True)
    text = proc.stdout
    rows = []
    for line in text.strip().splitlines()[1:]:  # skip header
        parts = line.split(",")
        if len(parts) != 2:
            continue
        date, val = parts[0].strip(), parts[1].strip()
        if val in ("", "."):
            continue
        try:
            rows.append((date, float(val)))
        except ValueError:
            continue
    return rows


def n_ago(rows, n):
    """Value n observations before the last (0 = latest). Returns (date, val) or None."""
    if len(rows) > n:
        return rows[-1 - n]
    return None


def build_dispersion(days):
    """Compute the credit bifurcation gauge from live FRED data.

    PRIMARY = CCC - BB (distressed vs quality junk). SECONDARY = CCC - HY (legacy).
    Trajectory is multi-month (5d/20d/63d) because the bifurcation is a quarters-long
    trend, not a daily wiggle — a 5d-only read misses it entirely (Will 6/9 catch)."""
    hy = fetch_fred_series(FRED_SERIES["HY"], days)
    bb = fetch_fred_series(FRED_SERIES["BB"], days)
    ccc = fetch_fred_series(FRED_SERIES["CCC"], days)
    if not hy or not bb or not ccc:
        return {"error": "FRED returned no data"}

    def bps(rows, n=0):
        v = n_ago(rows, n)
        return round(v[1] * 100) if v else None

    hy_bps, bb_bps, ccc_bps = bps(hy), bps(bb), bps(ccc)
    gap_bb = ccc_bps - bb_bps              # PRIMARY bifurcation gauge
    gap_hy = ccc_bps - hy_bps              # legacy (diluted — HY contains CCC)
    ratio_bb = round(ccc_bps / bb_bps, 2) if bb_bps else None
    ratio_hy = round(ccc_bps / hy_bps, 2) if hy_bps else None

    def gap_bb_at(n):
        c, b = bps(ccc, n), bps(bb, n)
        return (c - b) if (c is not None and b is not None) else None

    g5, g20, g63 = gap_bb_at(5), gap_bb_at(20), gap_bb_at(63)
    chg5 = (gap_bb - g5) if g5 is not None else None
    chg20 = (gap_bb - g20) if g20 is not None else None
    chg63 = (gap_bb - g63) if g63 is not None else None
    ccc_63 = (ccc_bps - bps(ccc, 63)) if bps(ccc, 63) is not None else None
    bb_63 = (bb_bps - bps(bb, 63)) if bps(bb, 63) is not None else None

    flags = []
    if hy_bps > HY_OAS_YELLOW:
        flags.append(f"HY OAS {hy_bps} > {HY_OAS_YELLOW} YELLOW — range break, bid giving way")
    if chg5 is not None and chg5 >= DISPERSION_5D_WIDEN:
        flags.append(f"CCC-BB gap +{chg5}bps over 5d — acute tail stress")
    if chg63 is not None and chg63 >= DISPERSION_63D_WIDEN:
        flags.append(f"BIFURCATION: CCC-BB gap +{chg63}bps over ~3mo — sustained K-shaped widening")
    if ccc_63 is not None and bb_63 is not None and ccc_63 > 0 and bb_63 <= 0:
        flags.append(f"CCC widening (+{ccc_63}/3mo) while BB flat/tighter ({bb_63:+d}) — bifurcation signature")

    return {
        "hy_oas_bps": hy_bps, "bb_oas_bps": bb_bps, "ccc_oas_bps": ccc_bps,
        "hy_date": hy[-1][0], "ccc_date": ccc[-1][0],
        "gap_bb": gap_bb, "ratio_bb": ratio_bb,         # PRIMARY
        "gap_hy": gap_hy, "ratio_hy": ratio_hy,         # legacy
        "gap_bb_5d_chg": chg5, "gap_bb_20d_chg": chg20, "gap_bb_63d_chg": chg63,
        "ccc_63d_chg": ccc_63, "bb_63d_chg": bb_63,
        "flags": flags,
    }


def build_flows():
    """Compute the HY fund-flow proxy from ETF price/volume/relative action."""
    import yfinance as yf

    def etf_stats(ticker):
        hist = yf.Ticker(ticker).history(period="30d")
        if hist.empty:
            return {"error": "no data"}
        closes = hist["Close"]
        vols = hist["Volume"]
        last = float(closes.iloc[-1])
        d1 = round((last / float(closes.iloc[-2]) - 1) * 100, 2) if len(closes) > 1 else None
        d5 = round((last / float(closes.iloc[-6]) - 1) * 100, 2) if len(closes) > 5 else None
        vol_last = float(vols.iloc[-1])
        vol_avg20 = float(vols.tail(20).mean())
        vol_x = round(vol_last / vol_avg20, 2) if vol_avg20 else None
        return {"price": round(last, 2), "d1_pct": d1, "d5_pct": d5,
                "vol_x_20d": vol_x, "closes": closes}

    out = {}
    for t in HY_ETFS:
        out[t] = etf_stats(t)
    out[IG_ETF] = etf_stats(IG_ETF)

    # HY-vs-IG relative: HYG/LQD ratio 5d change (HY underperforming = credit risk-off)
    rel_5d = None
    hyg, lqd = out.get("HYG"), out.get(IG_ETF)
    if hyg and lqd and "closes" in hyg and "closes" in lqd:
        hc, lc = hyg["closes"], lqd["closes"]
        if len(hc) > 5 and len(lc) > 5:
            r_now = float(hc.iloc[-1]) / float(lc.iloc[-1])
            r_5d = float(hc.iloc[-6]) / float(lc.iloc[-6])
            rel_5d = round((r_now / r_5d - 1) * 100, 2)

    flags = []
    for t in HY_ETFS:
        s = out[t]
        if s.get("d5_pct") is not None and s["d5_pct"] <= HYG_5D_DROP:
            flags.append(f"{t} 5d {s['d5_pct']}% <= {HYG_5D_DROP}% — price stress")
        if (s.get("vol_x_20d") is not None and s["vol_x_20d"] >= VOL_SURGE
                and s.get("d1_pct") is not None and s["d1_pct"] < 0):
            flags.append(f"{t} volume {s['vol_x_20d']}x 20d avg on a down day — redemption-pressure proxy")
    if rel_5d is not None and rel_5d <= HYG_LQD_5D_DROP:
        flags.append(f"HYG/LQD {rel_5d}% over 5d — HY underperforming IG, income bid stepping back")

    # strip the raw series before returning
    for t in out:
        out[t].pop("closes", None)
    return {"etfs": out, "hyg_lqd_5d_pct": rel_5d, "flags": flags}


def run(days=140):  # ≈95 trading obs — enough for the 63-obs (~3mo) bifurcation lookback
    disp = build_dispersion(days)
    flows = build_flows()
    all_flags = disp.get("flags", []) + flows.get("flags", [])
    return {
        "as_of": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "dispersion": disp,
        "flows": flows,
        "alert": bool(all_flags),
        "flags": all_flags,
    }


def fmt(report):
    d = report["dispersion"]
    f = report["flows"]
    L = []
    L.append("=" * 60)
    L.append(f"  HENRY CREDIT EARLY-WARNING MONITOR  ·  {report['as_of']}")
    L.append("=" * 60)
    if "error" in d:
        L.append(f"  DISPERSION: ERROR — {d['error']}")
    else:
        L.append("  CREDIT BIFURCATION (quality BB vs distressed CCC — the K-shape)")
        L.append(f"    BB  {d['bb_oas_bps']}bps   B-tier quality junk (healthy top)")
        L.append(f"    HY  {d['hy_oas_bps']}bps   blended index [{d['hy_date']}] (masks the tail)")
        L.append(f"    CCC {d['ccc_oas_bps']}bps   distressed tail [{d['ccc_date']}]")
        traj = ""
        if d['gap_bb_5d_chg'] is not None:
            traj = (f"   Δgap 5d {d['gap_bb_5d_chg']:+}  20d {d['gap_bb_20d_chg']:+}"
                    + (f"  ~3mo {d['gap_bb_63d_chg']:+}" if d['gap_bb_63d_chg'] is not None else ""))
        L.append(f"    → GAP (CCC-BB) {d['gap_bb']}bps   ratio {d['ratio_bb']}x{traj}")
        if d.get('ccc_63d_chg') is not None and d.get('bb_63d_chg') is not None:
            L.append(f"    → 3mo trend: CCC {d['ccc_63d_chg']:+}bps  vs  BB {d['bb_63d_chg']:+}bps"
                     + ("   ← diverging (bifurcation)" if d['ccc_63d_chg'] > 0 >= d['bb_63d_chg'] else ""))
    L.append("")
    L.append("  HY FUND-FLOW PROXY (ETF price / volume / vs IG)")
    for t in HY_ETFS + [IG_ETF]:
        s = f["etfs"].get(t, {})
        if "error" in s:
            L.append(f"    {t:4} ERROR — {s['error']}")
        else:
            L.append(f"    {t:4} ${s['price']}   1d {s['d1_pct']:+}%   5d {s['d5_pct']:+}%   vol {s['vol_x_20d']}x20d")
    if f["hyg_lqd_5d_pct"] is not None:
        L.append(f"    HYG/LQD (HY vs IG) 5d: {f['hyg_lqd_5d_pct']:+}%")
    L.append("")
    if report["flags"]:
        L.append("  ⚠ FLAGS:")
        for fl in report["flags"]:
            L.append(f"    → {fl}")
    else:
        L.append("  ✓ No flags — credit calm, dispersion stable, income bid intact.")
    L.append("=" * 60)
    return "\n".join(L)


def main():
    args = sys.argv[1:]
    days = 140  # ≈100 trading obs — covers the 63-obs (~3mo) bifurcation lookback
    if "--days" in args:
        days = int(args[args.index("--days") + 1])
    report = run(days)
    if "--json" in args:
        print(json.dumps(report, indent=2))
    else:
        print(fmt(report))


if __name__ == "__main__":
    main()
