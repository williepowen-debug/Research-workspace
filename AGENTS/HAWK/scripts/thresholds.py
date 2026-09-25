#!/usr/bin/env python3
# ⛔ FROZEN 2026-07-09 (legacy suite; see boot.py lines 1-16) — NOT run by HAWK's boot
# protocol and invoked by nothing live (grep 2026-09-25: only frozen boot.py calls it).
# DECLARED 2026-09-25 per PROME L429/L441 census (packet 2026-09-23):
#   - L429: every level below is keyed on the GENERIC continuation BZ=F, which rolls to
#     the next contract month; a level can move by the calendar spread with zero change
#     in the world (live instance: WALTER SIG-W-20260925-008, BZ=F Nov->Dec roll printed
#     'Brent -7.8%' on 9/25). The Brent-WTI line mixes two continuations with different
#     expiries (mode iii).
#   - L441: BRENT_PEAK = 116.38 is a FROZEN yardstick, vintage 'Apr 2026' as written,
#     source not recorded, never recomputed. Re-check date: NONE while frozen — any
#     revival must first recompute it from a named dated source and move the ladder to
#     a named dated contract month, per boot.py's live-data-audit condition.
#   - The scenario bands (D-EXTREME/C/B...) are July-era thesis labels, not current marks.
# Do not cite any output of this script. Prices come from FORGE/tools/market-data/fetch.py.
"""
HAWK Threshold Monitor — Brent Price & Scenario Triggers

Pulls live Brent crude price via yfinance and checks against HAWK thesis
scenario thresholds ($80, $100, $120). Outputs current price, scenario
zone, and alert status.

Usage:
  .venv/bin/python3 AGENTS/HAWK/scripts/thresholds.py
  .venv/bin/python3 AGENTS/HAWK/scripts/thresholds.py --save    # write to workbook
"""

import sys
import argparse
from datetime import datetime
from pathlib import Path

try:
    import yfinance as yf
except ImportError:
    print("  ERROR: yfinance not installed. Run: pip install yfinance")
    sys.exit(1)

HAWK_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = HAWK_DIR / "workbook"
WORKBOOK.mkdir(exist_ok=True)

# Scenario thresholds for Brent (BZ=F)
# Format: (level, scenario_zone, description)
THRESHOLDS = [
    (150.0, "D-EXTREME", "Kharg strike or Hormuz closure — extreme supply shock"),
    (120.0, "D-SEVERE",  "Multi-facility strikes — severe escalation confirmed"),
    (100.0, "D-RISK",    "Escalation signal — ceasefire collapse likely"),
    (80.0,  "C",         "Controlled burns framework threshold"),
    (60.0,  "B",         "Deal/stand-down confirmed — supply normalization"),
]

BRENT_PEAK = 116.38  # Post-strike peak (Apr 2026)

def get_brent_price():
    """Fetch current Brent price via yfinance."""
    try:
        ticker = yf.Ticker("BZ=F")
        info = ticker.info
        price = info.get("regularMarketPrice") or info.get("previousClose")
        prev = info.get("previousClose") or info.get("regularMarketPreviousClose")
        if price and prev:
            chg_pct = ((price - prev) / prev) * 100
            return {
                "price": price,
                "prev": prev,
                "chg_pct": chg_pct,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    except Exception as e:
        print(f"  ERROR fetching Brent price: {e}")
    return None


def get_wti_price():
    """Fetch current WTI price for spread analysis."""
    try:
        ticker = yf.Ticker("CL=F")
        info = ticker.info
        price = info.get("regularMarketPrice")
        return price
    except Exception:
        return None


def determine_scenario(price):
    """Determine scenario zone based on Brent price."""
    for level, zone, desc in THRESHOLDS:
        if price >= level:
            return zone, desc, level
    return "B-CONFIRMED", "Below B threshold — full normalization", 60.0


def check_proximity(price):
    """Check if price is within 10% of any threshold."""
    warnings = []
    for level, zone, desc in THRESHOLDS:
        dist_pct = abs(price - level) / level * 100
        if dist_pct <= 10:
            direction = "above" if price > level else "below"
            warnings.append({
                "level": level,
                "zone": zone,
                "dist_pct": dist_pct,
                "direction": direction,
                "desc": desc
            })
    return sorted(warnings, key=lambda x: x["dist_pct"])


def save_breach(price, scenario, zone_level):
    """Log price to PRICE_BREACHES.tsv."""
    tsv_path = WORKBOOK / "PRICE_BREACHES.tsv"
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Create file with header if doesn't exist
    if not tsv_path.exists():
        with open(tsv_path, "w") as f:
            f.write("date\tprice\tscenario\tzone_level\tpeak_distance_pct\n")
    
    # Check if already logged today
    already_logged = False
    with open(tsv_path) as f:
        next(f, None)  # skip header
        for line in f:
            parts = line.strip().split("\t")
            if parts and parts[0] == today:
                already_logged = True
                break
    
    if not already_logged:
        peak_dist = ((price - BRENT_PEAK) / BRENT_PEAK) * 100 if BRENT_PEAK else 0
        with open(tsv_path, "a") as f:
            f.write(f"{today}\t{price:.2f}\t{scenario}\t{zone_level}\t{peak_dist:.1f}\n")


def get_cached_price():
    """Get cached/last known price from workbook."""
    cache_path = WORKBOOK / "PRICE_BREACHES.tsv"
    if cache_path.exists():
        try:
            with open(cache_path) as f:
                lines = f.readlines()
                if len(lines) > 1:
                    # Get last line (most recent entry)
                    last_line = lines[-1].strip()
                    parts = last_line.split("\t")
                    if len(parts) >= 2:
                        price = float(parts[1])
                        date = parts[0]
                        return {
                            "price": price,
                            "prev": price,
                            "chg_pct": 0.0,
                            "timestamp": f"{date} (cached)",
                            "cached": True
                        }
        except Exception as e:
            print(f"  WARNING: Could not read cached price: {e}")
    return None


def main():
    parser = argparse.ArgumentParser(description="HAWK Brent threshold monitor")
    parser.add_argument("--save", action="store_true", help="Save to workbook")
    parser.add_argument("--quick", action="store_true", help="Use cached price (skip live fetch)")
    args = parser.parse_args()
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M ET")
    
    print(f"\n{'='*70}")
    print(f"  HAWK Threshold Monitor — {now}")
    print(f"{'='*70}")
    
    # Fetch prices (live or cached)
    if args.quick:
        print("\n  [QUICK MODE: Using cached price]")
        brent = get_cached_price()
        if not brent:
            print("  WARNING: No cached price found, attempting live fetch...")
            brent = get_brent_price()
        wti = None
    else:
        brent = get_brent_price()
        wti = get_wti_price()
    
    if not brent:
        print("\n  ERROR: Could not fetch Brent price. Check network.")
        return 1
    
    price = brent["price"]
    peak_dist = ((price - BRENT_PEAK) / BRENT_PEAK) * 100 if BRENT_PEAK else 0
    
    # Determine scenario
    scenario, desc, zone_level = determine_scenario(price)
    
    # Output header
    print(f"\n  BRENT CRUDE: ${price:.2f}  ({brent['chg_pct']:+.2f}%)")
    if wti:
        spread = price - wti
        print(f"  WTI:         ${wti:.2f}  (Brent-WTI spread: ${spread:.2f})")
    print(f"  vs Peak:     {peak_dist:+.1f}%  (peak: ${BRENT_PEAK:.2f})")
    
    # Scenario zone
    print(f"\n  SCENARIO ZONE: {scenario}")
    print(f"  {'-'*60}")
    
    if scenario.startswith("D"):
        print(f"  🔴 ESCALATION — {desc}")
    elif scenario == "C":
        print(f"  🟡 CONTROLLED — {desc}")
    elif scenario.startswith("B"):
        print(f"  🟢 NORMALIZED — {desc}")
    
    # Threshold status table
    print(f"\n  THRESHOLD STATUS")
    print(f"  {'-'*60}")
    print(f"  {'Level':<10} {'Status':<15} {'Distance':<12} Description")
    print(f"  {'-'*60}")
    
    for level, zone, description in THRESHOLDS:
        if price >= level:
            status = "🔴 BREACHED"
            dist_str = f"+{((price-level)/level)*100:.1f}%"
        else:
            status = "🟢 Clear"
            dist_str = f"-{((level-price)/level)*100:.1f}%"
        print(f"  ${level:<9.0f} {status:<15} {dist_str:<12} {description[:35]}")
    
    # Proximity warnings
    warnings = check_proximity(price)
    if warnings:
        print(f"\n  ⚠️  PROXIMITY WARNINGS (within 10% of threshold)")
        print(f"  {'-'*60}")
        for w in warnings[:2]:  # Show closest 2
            emoji = "🔴" if w["zone"].startswith("D") else "🟡" if w["zone"] == "C" else "🟢"
            print(f"  {emoji} ${w['level']:.0f} ({w['zone']}): {w['dist_pct']:.1f}% {w['direction']}")
    
    # Save if requested
    if args.save:
        save_breach(price, scenario, zone_level)
        print(f"\n  💾 Logged to workbook/PRICE_BREACHES.tsv")
    
    # Alert summary
    print(f"\n  ALERT STATUS")
    print(f"  {'-'*60}")
    if scenario.startswith("D") and price >= 100:
        print(f"  🔴 ALERT: Brent in escalation zone — reassess scenarios")
    elif scenario.startswith("D") and price >= 120:
        print(f"  🔴🔴 CRITICAL: Severe escalation confirmed — D → 95%+")
    elif price < 60:
        print(f"  🟢 B scenario threshold — check physical restart progress")
    else:
        print(f"  ✅ No active alerts")
    
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
