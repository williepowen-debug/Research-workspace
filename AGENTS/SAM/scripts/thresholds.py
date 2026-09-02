#!/usr/bin/env python3
"""
SAM Threshold Monitor
Pulls live FX/oil prices via yfinance and compares against SAM thesis thresholds.
Prints breaches and near-miss warnings (within 5%).

Thresholds are color-coded by thesis direction:
  🔴 = risk / stop zone (price moving wrong way for thesis)
  🟢 = thesis confirming (price moving right way)
  🟠 = structural stress level (not directional)

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/thresholds.py
"""

import os
import sys
from datetime import datetime

try:
    import yfinance as yf
except ImportError:
    print("  ERROR: yfinance not installed.")
    sys.exit(1)

# Thresholds: (ticker, direction, level, classification, label)
# direction: "above" = breach when price > level, "below" = breach when price < level
# classification: "risk" (🔴), "thesis" (🟢), "stress" (🟠)
THRESHOLDS = [
    # ── USD/JPY risk zone (yen weakening = bad for FXY long)
    ("USDJPY=X", "above", 167.0, "risk",   "STOP — thesis may be broken, no MOF response"),
    ("USDJPY=X", "above", 165.0, "risk",   "Approaching stop — yen weakness accelerating"),
    ("USDJPY=X", "above", 162.0, "risk",   "Re-anchored mkt intervention line (ING 6/26); playbook 3rd-strike zone 162-163; AMBUSH regime = unsignalled"),
    ("USDJPY=X", "above", 160.0, "risk",   "Historic strike zone (Apr30/May6 2026 ops); CH-011: MOF fires on disorder/speed, NOT level"),
    # ── USD/JPY thesis zone (yen strengthening = thesis working)
    ("USDJPY=X", "below", 155.0, "thesis", "Phase 2 carry unwind onset"),
    ("USDJPY=X", "below", 150.0, "thesis", "Deep carry unwind — FXY target zone approaching"),
    ("USDJPY=X", "below", 147.0, "thesis", "Forced carry unwind zone"),
    ("USDJPY=X", "below", 145.0, "thesis", "Unhedged positions underwater → mechanical selling"),
    ("USDJPY=X", "below", 135.0, "thesis", "Life insurer forced systematic selling (avg entry rate)"),
    # ── FXY position levels
    ("FXY",      "below",  55.05, "risk",   "Former stop level (FLAT since 6/29) — watch/re-entry reference only"),
    ("FXY",      "above",  60.00, "thesis", "FXY target zone entry ($60-62)"),
    ("FXY",      "above",  62.00, "thesis", "FXY target zone upper bound — consider partial profits"),
    # ── Brent oil
    ("BZ=F",     "above", 120.0, "risk",   "Kharg scenario — oil shock dominates, Phase 1 extends"),
    ("BZ=F",     "below",  90.0, "thesis", "Oil headwind resolved — rate differential takes over"),
    ("BZ=F",     "below",  80.0, "thesis", "Full oil de-escalation — BOJ hike comfortable"),
]

# Context tickers (quoted but no thresholds)
CONTEXT_TICKERS = ["EURJPY=X", "GBPJPY=X", "AUDJPY=X"]

# JGB thresholds are NOT evaluated in this script. They are fetched and graded by
# jgb_yields.py, which runs in the same boot. DAEDALUS 8/28 (confirmed by SAM 9/1)
# found that printing them here as "⚪ MANUAL CHECK ... check manually via web", in the
# SAME visual form as the live USDJPY/FXY/Brent rows, makes a reader believe the KEY
# THRESHOLDS table is being monitored inline when nothing is fetched or compared.
# Verdict: SUBSTITUTED. Fix = render them in a visibly different form that names the
# owner, and echo the last stored close so the pointer is checkable rather than bare.
JGB_DELEGATED = [
    ("JGB 10Y", "10Y", 2.40, "Stress crossover"),
    ("JGB 30Y", "30Y", 4.00, "Severe insurer stress"),
    ("JGB 40Y", "40Y", 4.00, "Extreme long-end stress"),
]
JGB_TSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "workbook", "JGB_YIELDS.tsv")


def _last_jgb_row():
    """Last stored MOF close, or None. Read-only echo — jgb_yields.py owns the grade."""
    try:
        with open(JGB_TSV, encoding="utf-8") as fh:
            rows = [ln.rstrip("\n").split("\t") for ln in fh if ln.strip()]
        hdr, last = rows[0], rows[-1]
        return dict(zip(hdr, last))
    except Exception:
        return None

WARN_PCT = 0.05  # 5% proximity warning


def get_prices(symbols):
    """Fetch current prices for symbols. Returns dict symbol -> {price, prev, chg}."""
    prices = {}
    try:
        tickers = yf.Tickers(" ".join(symbols))
        for sym in symbols:
            try:
                info = tickers.tickers[sym].info
                price = info.get("regularMarketPrice") or info.get("previousClose")
                prev = info.get("previousClose") or info.get("regularMarketPreviousClose")
                if price:
                    chg = ((price - prev) / prev * 100) if prev else 0
                    prices[sym] = {"price": price, "prev": prev, "chg": chg}
            except Exception:
                pass
    except Exception as e:
        print(f"  ERROR fetching prices: {e}")
    return prices


def check_thresholds(prices):
    """
    Check all thresholds. Returns list of dicts.
    Rules:
      - BREACHED: always reported (no deduping — every active breach matters).
      - WARNING: only the NEAREST un-breached level per (ticker, direction) is reported,
        to avoid noise when SAM has clustered thresholds (e.g., USDJPY at 160/162/165/167).
    """
    results = []
    warning_candidates = {}  # (ticker, direction) -> closest warning dict

    for ticker, direction, level, clas, label in THRESHOLDS:
        p = prices.get(ticker)
        if not p:
            continue

        price = p["price"]
        dist = (price - level) / level * 100

        if direction == "above":
            if price > level:
                results.append({"ticker": ticker, "level": level, "label": label,
                                "class": clas, "status": "BREACHED", "price": price,
                                "dist": dist, "direction": direction})
            elif price > level * (1 - WARN_PCT):
                cand = {"ticker": ticker, "level": level, "label": label,
                        "class": clas, "status": "WARNING", "price": price,
                        "dist": dist, "direction": direction}
                key = (ticker, direction)
                # Keep the one closest to breach (smallest positive distance to level)
                if key not in warning_candidates or abs(dist) < abs(warning_candidates[key]["dist"]):
                    warning_candidates[key] = cand
        else:  # below
            if price < level:
                results.append({"ticker": ticker, "level": level, "label": label,
                                "class": clas, "status": "BREACHED", "price": price,
                                "dist": dist, "direction": direction})
            elif price < level * (1 + WARN_PCT):
                cand = {"ticker": ticker, "level": level, "label": label,
                        "class": clas, "status": "WARNING", "price": price,
                        "dist": dist, "direction": direction}
                key = (ticker, direction)
                if key not in warning_candidates or abs(dist) < abs(warning_candidates[key]["dist"]):
                    warning_candidates[key] = cand

    results.extend(warning_candidates.values())
    return results


def emoji_for(clas, status):
    """Emoji for classification + status combination."""
    if status == "BREACHED":
        if clas == "risk":
            return "🔴"
        elif clas == "thesis":
            return "🟢"
        else:
            return "🟠"
    else:  # WARNING
        if clas == "risk":
            return "⚠️ "
        elif clas == "thesis":
            return "🟡"
        else:
            return "🟠"


def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Collect symbols
    threshold_syms = list(set(t[0] for t in THRESHOLDS))
    all_syms = list(set(threshold_syms + CONTEXT_TICKERS))

    print(f"\n{'='*70}")
    print(f"  SAM Threshold Monitor — {now}")
    print(f"{'='*70}")

    prices = get_prices(all_syms)

    if not prices:
        print("\n  ERROR: Could not fetch any prices. Check network.")
        return 1

    alerts = check_thresholds(prices)

    risk_breaches = [a for a in alerts if a["status"] == "BREACHED" and a["class"] == "risk"]
    thesis_breaches = [a for a in alerts if a["status"] == "BREACHED" and a["class"] == "thesis"]
    warnings = [a for a in alerts if a["status"] == "WARNING"]

    if risk_breaches:
        print(f"\n  🔴 RISK BREACHES")
        print(f"  {'-'*60}")
        for a in risk_breaches:
            price_str = f"{a['price']:.2f}" if a["ticker"].endswith("=X") else f"${a['price']:.2f}"
            level_str = f"{a['level']:.2f}"
            print(f"  🔴 {a['ticker']:<10} {price_str:>10}  (level {level_str}, {a['dist']:+.1f}%)")
            print(f"              {a['label']}")

    if thesis_breaches:
        print(f"\n  🟢 THESIS CONFIRMING BREACHES")
        print(f"  {'-'*60}")
        for a in thesis_breaches:
            price_str = f"{a['price']:.2f}" if a["ticker"].endswith("=X") else f"${a['price']:.2f}"
            level_str = f"{a['level']:.2f}"
            print(f"  🟢 {a['ticker']:<10} {price_str:>10}  (level {level_str}, {a['dist']:+.1f}%)")
            print(f"              {a['label']}")

    if warnings:
        print(f"\n  ⚠️  NEAR THRESHOLDS (within 5%)")
        print(f"  {'-'*60}")
        for a in warnings:
            emoji = emoji_for(a["class"], "WARNING")
            price_str = f"{a['price']:.2f}" if a["ticker"].endswith("=X") else f"${a['price']:.2f}"
            level_str = f"{a['level']:.2f}"
            print(f"  {emoji} {a['ticker']:<10} {price_str:>10}  (level {level_str}, {a['dist']:+.1f}%)")
            print(f"              {a['label']}")

    if not risk_breaches and not thesis_breaches and not warnings:
        print(f"\n  ✅ No threshold breaches or near-warnings.")

    # Current levels snapshot
    print(f"\n  CURRENT LEVELS")
    print(f"  {'-'*60}")
    display_order = ["FXY", "USDJPY=X", "EURJPY=X", "GBPJPY=X", "AUDJPY=X", "BZ=F"]
    for sym in display_order:
        p = prices.get(sym)
        if p:
            arrow = "🟢" if p["chg"] >= 0 else "🔴"
            price_str = f"{p['price']:>9.2f}" if sym.endswith("=X") else f"${p['price']:>8.2f}"
            print(f"  {arrow} {sym:<12} {price_str}  ({p['chg']:+.2f}%)")

    # JGB thresholds are owned by jgb_yields.py — deliberately rendered differently
    # from the live rows above so this block cannot be mistaken for inline monitoring.
    row = _last_jgb_row()
    stamp = f"last stored MOF close {row['Date']}" if row else "NO STORED DATA"
    print(f"\n  ┌─ JGB thresholds: NOT EVALUATED HERE ─ owned by jgb_yields.py (same boot)")
    print(f"  │  This block fetches and compares NOTHING. Read its verdict there.")
    print(f"  │  Echo only, {stamp}:")
    for name, col, level, note in JGB_DELEGATED:
        val = row.get(col) if row else None
        shown = f"{float(val):.3f}%" if val else "  n/a "
        print(f"  │    {name:<8} {shown:>8}  vs {level:.2f}%  ({note})")
    print(f"  └─ ⚠️  echo may be stale; jgb_yields.py is the grade of record")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
