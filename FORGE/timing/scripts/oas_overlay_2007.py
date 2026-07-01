#!/usr/bin/env python3
"""
2007 vs 2026 HY OAS Overlay
Pulls daily HY OAS and CCC OAS from FRED, finds threshold crossings,
relief rallies, velocity, and credit→equity lag.
"""

import json
import urllib.request
from datetime import datetime, timedelta

import os
import sys


def _fred_key():
    """Env first, else the gitignored FORGE market-data .env (single per-machine home).
    Hardcoded copies scrubbed 2026-07-01 (public-prep) — never hardcode this key."""
    import pathlib
    k = os.environ.get("FRED_API_KEY", "")
    if k:
        return k
    p = pathlib.Path(__file__).resolve().parents[3] / "FORGE/tools/market-data/.env"
    if p.exists():
        for line in p.read_text().splitlines():
            if line.startswith("FRED_API_KEY="):
                return line.split("=", 1)[1].strip()
    print("WARN: FRED_API_KEY not found (env or FORGE/tools/market-data/.env) — FRED pulls will fail", file=sys.stderr)
    return ""


FRED_API_KEY = _fred_key()

def fred_daily(series_id, start, end):
    """Pull daily FRED series."""
    url = (
        f"https://api.stlouisfed.org/fred/series/observations"
        f"?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json"
        f"&observation_start={start}&observation_end={end}"
        f"&sort_order=asc"
    )
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    out = []
    for obs in data.get("observations", []):
        if obs["value"] != ".":
            out.append({"date": obs["date"], "value": float(obs["value"]) * 100})  # pct → bps
    return out


def find_crossings(data, thresholds, direction="up"):
    """Find first date each threshold is crossed."""
    crossings = {}
    for t in thresholds:
        for i, d in enumerate(data):
            if direction == "up" and d["value"] >= t:
                if t not in crossings:
                    crossings[t] = d["date"]
                    break
            elif direction == "down" and d["value"] <= t:
                if t not in crossings:
                    crossings[t] = d["date"]
                    break
    return crossings


def find_relief_rallies(data, min_compression=10):
    """Find tightening episodes within a widening trend."""
    rallies = []
    i = 0
    while i < len(data) - 1:
        # Look for local peaks (start of tightening)
        if i > 0 and data[i]["value"] > data[i-1]["value"] and data[i]["value"] > data[i+1]["value"]:
            peak_idx = i
            peak_val = data[i]["value"]
            # Find the trough
            trough_idx = i + 1
            trough_val = data[i+1]["value"]
            for j in range(i+1, min(i+60, len(data))):
                if data[j]["value"] < trough_val:
                    trough_val = data[j]["value"]
                    trough_idx = j
                elif data[j]["value"] > trough_val + 20:
                    # Widening resumed
                    break
            compression = peak_val - trough_val
            if compression >= min_compression:
                rallies.append({
                    "peak_date": data[peak_idx]["date"],
                    "peak_oas": peak_val,
                    "trough_date": data[trough_idx]["date"],
                    "trough_oas": trough_val,
                    "compression": round(compression, 1),
                    "days": (datetime.strptime(data[trough_idx]["date"], "%Y-%m-%d") -
                             datetime.strptime(data[peak_idx]["date"], "%Y-%m-%d")).days,
                })
                i = trough_idx
        i += 1
    return rallies


def monthly_velocity(data):
    """Average daily change by month."""
    months = {}
    for i in range(1, len(data)):
        month = data[i]["date"][:7]
        change = data[i]["value"] - data[i-1]["value"]
        if month not in months:
            months[month] = []
        months[month].append(change)
    
    result = []
    for month, changes in sorted(months.items()):
        avg = sum(changes) / len(changes)
        # Max 5-day moves
        result.append({
            "month": month,
            "avg_daily": round(avg, 2),
            "max_daily": round(max(changes), 1),
            "min_daily": round(min(changes), 1),
            "total": round(sum(changes), 1),
            "days": len(changes),
        })
    return result


def main():
    print("=" * 70)
    print("  2007 vs 2026 HY OAS OVERLAY")
    print("=" * 70)

    # --- Pull 2007 data ---
    print("\nFetching 2007 HY OAS (BAMLH0A0HYM2)...")
    hy_2007 = fred_daily("BAMLH0A0HYM2", "2007-01-01", "2008-06-30")
    print(f"  Got {len(hy_2007)} observations")

    print("Fetching 2007 CCC OAS (BAMLH0A3HYC)...")
    ccc_2007 = fred_daily("BAMLH0A3HYC", "2007-01-01", "2008-06-30")
    print(f"  Got {len(ccc_2007)} observations")

    # --- Pull 2026 data ---
    print("Fetching 2026 HY OAS...")
    hy_2026 = fred_daily("BAMLH0A0HYM2", "2026-01-01", "2026-12-31")
    print(f"  Got {len(hy_2026)} observations")

    print("Fetching 2026 CCC OAS (BAMLH0A3HYC)...")
    ccc_2026 = fred_daily("BAMLH0A3HYC", "2026-01-01", "2026-12-31")
    print(f"  Got {len(ccc_2026)} observations")

    # --- Pull SPX (use SP500 FRED series) ---
    # SPX not available on FRED pre-2013. Using NASDAQCOM as equity proxy.
    print("Fetching 2007 NASDAQ (NASDAQCOM) as equity proxy...")
    spx_2007 = fred_daily("NASDAQCOM", "2007-01-01", "2008-06-30")
    # NASDAQCOM is raw index, undo the *100 from fred_daily
    for d in spx_2007:
        d["value"] = d["value"] / 100
    print(f"  Got {len(spx_2007)} observations")

    # =====================================================================
    # TABLE 1: Threshold Crossings
    # =====================================================================
    thresholds_hy = [300, 320, 350, 400, 500, 600, 800]
    thresholds_ccc = [500, 600, 800, 1000, 1200, 1500]

    hy_cross_2007 = find_crossings(hy_2007, thresholds_hy)
    ccc_cross_2007 = find_crossings(ccc_2007, thresholds_ccc)
    hy_cross_2026 = find_crossings(hy_2026, thresholds_hy)
    ccc_cross_2026 = find_crossings(ccc_2026, thresholds_ccc)

    print("\n" + "=" * 70)
    print("  TABLE 1: HY OAS THRESHOLD CROSSINGS")
    print("=" * 70)
    print(f"  {'Threshold':>10} | {'2007 Date':>12} | {'2026 Date':>12} | {'2007→2026'}")
    print("  " + "-" * 60)

    ref_2007 = hy_cross_2007.get(300)
    ref_2026 = hy_cross_2026.get(300)

    for t in thresholds_hy:
        d07 = hy_cross_2007.get(t, "—")
        d26 = hy_cross_2026.get(t, "—")
        
        lag_info = ""
        if d07 != "—" and ref_2007:
            days_07 = (datetime.strptime(d07, "%Y-%m-%d") - datetime.strptime(ref_2007, "%Y-%m-%d")).days
            lag_info = f"{days_07}d from 300"
        if d26 != "—" and ref_2026:
            days_26 = (datetime.strptime(d26, "%Y-%m-%d") - datetime.strptime(ref_2026, "%Y-%m-%d")).days
            lag_info += f" | {days_26}d from 300"
        
        print(f"  {t:>10} | {d07:>12} | {d26:>12} | {lag_info}")

    print("\n" + "=" * 70)
    print("  TABLE 2: CCC OAS THRESHOLD CROSSINGS")
    print("=" * 70)
    print(f"  {'Threshold':>10} | {'2007 Date':>12} | {'2026 Date':>12}")
    print("  " + "-" * 45)
    for t in thresholds_ccc:
        d07 = ccc_cross_2007.get(t, "—")
        d26 = ccc_cross_2026.get(t, "—")
        print(f"  {t:>10} | {d07:>12} | {d26:>12}")

    # =====================================================================
    # CCC/HY Ratio
    # =====================================================================
    print("\n" + "=" * 70)
    print("  TABLE 3: CCC/HY RATIO (did CCC lead?)")
    print("=" * 70)
    
    # Match dates between HY and CCC for 2007
    hy_by_date = {d["date"]: d["value"] for d in hy_2007}
    ccc_by_date = {d["date"]: d["value"] for d in ccc_2007}
    
    # Sample key dates
    key_dates_07 = ["2007-01-02", "2007-03-01", "2007-06-01", "2007-06-15",
                     "2007-07-02", "2007-07-16", "2007-08-01", "2007-08-16",
                     "2007-09-04", "2007-10-01", "2007-11-01", "2007-12-03"]
    
    print(f"  {'Date':>12} | {'HY OAS':>8} | {'CCC OAS':>9} | {'Ratio':>6}")
    print("  " + "-" * 50)
    for d in key_dates_07:
        # Find nearest date
        hy_val = hy_by_date.get(d)
        ccc_val = ccc_by_date.get(d)
        if hy_val and ccc_val:
            ratio = round(ccc_val / hy_val, 2)
            print(f"  {d:>12} | {hy_val:>8.0f} | {ccc_val:>9.0f} | {ratio:>6.2f}")

    # Current 2026 ratio
    if hy_2026 and ccc_2026:
        last_hy = hy_2026[-1]
        last_ccc = ccc_2026[-1]
        ratio_26 = round(last_ccc["value"] / last_hy["value"], 2)
        print(f"\n  2026 current: HY {last_hy['value']:.0f} / CCC {last_ccc['value']:.0f} = ratio {ratio_26:.2f}")

    # =====================================================================
    # TABLE 4: Relief Rallies (2007)
    # =====================================================================
    # Focus on Jun-Dec 2007
    hy_jun_dec = [d for d in hy_2007 if d["date"] >= "2007-06-01"]
    rallies = find_relief_rallies(hy_jun_dec, min_compression=15)

    print("\n" + "=" * 70)
    print("  TABLE 4: RELIEF RALLIES IN CREDIT (2007, compression >15bps)")
    print("=" * 70)
    print(f"  {'Peak Date':>12} | {'Peak OAS':>9} | {'Trough Date':>12} | {'Trough OAS':>10} | {'Compress':>9} | {'Days':>5}")
    print("  " + "-" * 70)
    for r in rallies:
        print(f"  {r['peak_date']:>12} | {r['peak_oas']:>9.0f} | {r['trough_date']:>12} | {r['trough_oas']:>10.0f} | {r['compression']:>8.0f}bp | {r['days']:>5}")

    # =====================================================================
    # TABLE 5: Monthly Velocity (2007)
    # =====================================================================
    vel = monthly_velocity(hy_2007)
    
    print("\n" + "=" * 70)
    print("  TABLE 5: MONTHLY SPREAD VELOCITY (2007 HY OAS)")
    print("=" * 70)
    print(f"  {'Month':>8} | {'Avg Δ/day':>10} | {'Total Δ':>8} | {'Max Up':>7} | {'Max Down':>9}")
    print("  " + "-" * 55)
    for v in vel:
        print(f"  {v['month']:>8} | {v['avg_daily']:>9.2f}bp | {v['total']:>7.0f}bp | {v['max_daily']:>6.0f}bp | {v['min_daily']:>8.0f}bp")

    # =====================================================================
    # TABLE 6: Credit → Equity Lag
    # =====================================================================
    spx_by_date = {d["date"]: d["value"] for d in spx_2007}
    
    # SPX peak
    spx_peak = max(spx_2007, key=lambda x: x["value"])
    
    print("\n" + "=" * 70)
    print(f"  TABLE 6: CREDIT → EQUITY LAG (SPX peak: {spx_peak['date']} at {spx_peak['value']:.0f})")
    print("=" * 70)
    
    print(f"  {'HY Threshold':>13} | {'Date Crossed':>13} | {'SPX on Date':>12} | {'Days to SPX Peak':>17} | {'SPX vs Peak':>12}")
    print("  " + "-" * 75)
    
    for t in [300, 320, 350, 400, 500]:
        cross_date = hy_cross_2007.get(t)
        if cross_date:
            # Find nearest SPX
            spx_val = spx_by_date.get(cross_date)
            if not spx_val:
                # Try nearby dates
                for offset in range(1, 5):
                    d = datetime.strptime(cross_date, "%Y-%m-%d")
                    for delta in [offset, -offset]:
                        check = (d + timedelta(days=delta)).strftime("%Y-%m-%d")
                        if check in spx_by_date:
                            spx_val = spx_by_date[check]
                            break
                    if spx_val:
                        break
            
            days_to_peak = (datetime.strptime(spx_peak["date"], "%Y-%m-%d") -
                           datetime.strptime(cross_date, "%Y-%m-%d")).days
            
            pct = ""
            if spx_val:
                pct = f"{((spx_val / spx_peak['value']) - 1) * 100:+.1f}%"
                spx_str = f"{spx_val:.0f}"
            else:
                spx_str = "N/A"
            
            print(f"  {t:>13} | {cross_date:>13} | {spx_str:>12} | {days_to_peak:>17} | {pct:>12}")

    # =====================================================================
    # SUMMARY
    # =====================================================================
    print("\n" + "=" * 70)
    print("  SUMMARY & KEY FINDINGS")
    print("=" * 70)
    
    # Starting values
    if hy_2007:
        print(f"\n  2007 HY OAS started at: {hy_2007[0]['value']:.0f} ({hy_2007[0]['date']})")
        print(f"  2007 HY OAS ended at:   {hy_2007[-1]['value']:.0f} ({hy_2007[-1]['date']})")
    if hy_2026:
        print(f"  2026 HY OAS started at: {hy_2026[0]['value']:.0f} ({hy_2026[0]['date']})")
        print(f"  2026 HY OAS latest:     {hy_2026[-1]['value']:.0f} ({hy_2026[-1]['date']})")
    
    print()


if __name__ == "__main__":
    main()
