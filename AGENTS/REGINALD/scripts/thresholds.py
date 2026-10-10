#!/usr/bin/env python3
"""
REGINALD Threshold Monitor
Pulls live prices via yfinance and compares against thesis thresholds.
Prints breaches and near-miss warnings (within 5%).

Usage:
  .venv/bin/python3 AGENTS/REGINALD/scripts/thresholds.py
"""

import sys
from datetime import datetime

try:
    import yfinance as yf
except ImportError:
    print("  ERROR: yfinance not installed. Run: pip install yfinance")
    sys.exit(1)

# Thresholds: (ticker, direction, level, label)
# direction: "below" means breach when price < level, "above" means breach when price > level
THRESHOLDS = [
    # Bank stress
    ("KRE",   "below",  60.0,  "Acute regional stress"),
    ("WAL",   "below",  78.0,  "WAL price stress (REG-T-02); cause not pre-attributed"),
    ("OZK",   "below",  40.0,  "Crisis territory"),
    ("EGBN",  "below",  22.0,  "Capital raise territory"),
    # Macro
    ("BZ=F",  "above", 120.0,  "Stagflation — oil shock"),
    ("HYG",   "below",  75.0,  "HY credit stress"),
    # Also track key levels for context
    ("KRE",   "below",  65.0,  "KRE approaching prior low"),
    ("WAL",   "below",  70.0,  "WAL approaching crisis level"),
    ("WAL",   "below",  65.0,  "WAL at prior low"),
]

# Additional tickers to quote for context (no threshold, just display)
CONTEXT_TICKERS = ["SPY", "IWM", "^VIX", "^TNX", "TLT"]

WARN_PCT = 0.05  # 5% proximity warning


def get_prices(symbols):
    """Fetch current prices for a list of symbols. Returns dict of symbol -> price."""
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
    """Check all thresholds. Returns list of (ticker, level, label, status, price, distance_pct)."""
    results = []
    for ticker, direction, level, label in THRESHOLDS:
        p = prices.get(ticker)
        if not p:
            results.append((ticker, level, label, "NO DATA", None, None))
            continue

        price = p["price"]

        if direction == "below":
            if price < level:
                dist = (price - level) / level * 100
                results.append((ticker, level, label, "BREACHED", price, dist))
            elif price < level * (1 + WARN_PCT):
                dist = (price - level) / level * 100
                results.append((ticker, level, label, "WARNING", price, dist))
        elif direction == "above":
            if price > level:
                dist = (price - level) / level * 100
                results.append((ticker, level, label, "BREACHED", price, dist))
            elif price > level * (1 - WARN_PCT):
                dist = (price - level) / level * 100
                results.append((ticker, level, label, "WARNING", price, dist))

    return results


def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Collect all unique symbols
    threshold_syms = list(set(t[0] for t in THRESHOLDS))
    all_syms = list(set(threshold_syms + CONTEXT_TICKERS))

    print(f"\n{'='*70}")
    print(f"  REGINALD Threshold Monitor — {now}")
    print(f"{'='*70}")

    prices = get_prices(all_syms)

    if not prices:
        print("\n  ERROR: Could not fetch any prices. Check network.")
        return

    # Check thresholds
    alerts = check_thresholds(prices)

    breaches = [a for a in alerts if a[3] == "BREACHED"]
    warnings = [a for a in alerts if a[3] == "WARNING"]
    no_data = [a for a in alerts if a[3] == "NO DATA"]

    if breaches:
        print(f"\n  {'🔴 BREACHES':}")
        print(f"  {'-'*60}")
        for ticker, level, label, _, price, dist in breaches:
            print(f"  🔴 {ticker:<6} ${price:>8.2f}  (threshold ${level:.0f}, {dist:+.1f}%)  {label}")

    if warnings:
        print(f"\n  {'⚠️  NEAR THRESHOLD (within 5%)':}")
        print(f"  {'-'*60}")
        for ticker, level, label, _, price, dist in warnings:
            print(f"  ⚠️  {ticker:<6} ${price:>8.2f}  (threshold ${level:.0f}, {dist:+.1f}%)  {label}")

    if not breaches and not warnings:
        print(f"\n  ✅ No threshold breaches or warnings.")

    if no_data:
        for ticker, level, label, _, _, _ in no_data:
            print(f"  ⚪ {ticker:<6} — no data (threshold ${level:.0f}: {label})")

    # Context prices
    print(f"\n  {'CONTEXT':}")
    print(f"  {'-'*60}")
    for sym in CONTEXT_TICKERS:
        p = prices.get(sym)
        if p:
            arrow = "🟢" if p["chg"] >= 0 else "🔴"
            print(f"  {arrow} {sym:<8} ${p['price']:>10.2f}  ({p['chg']:+.2f}%)")
        else:
            print(f"  ⚪ {sym:<8} — no data")

    # Thesis tickers summary
    print(f"\n  {'THESIS TICKERS':}")
    print(f"  {'-'*60}")
    for sym in sorted(set(t[0] for t in THRESHOLDS)):
        p = prices.get(sym)
        if p:
            arrow = "🟢" if p["chg"] >= 0 else "🔴"
            print(f"  {arrow} {sym:<8} ${p['price']:>10.2f}  ({p['chg']:+.2f}%)")

    print()


if __name__ == "__main__":
    main()
