#!/usr/bin/env python3
"""
Market Data Fetch — Layer 1
Pull live prices (yfinance) and economic data (FRED).

Usage:
  python3 fetch.py price KRE APO WAL           # specific tickers
  python3 fetch.py fred ICSA                    # single FRED series
  python3 fetch.py fred ICSA --periods 10       # with history
  python3 fetch.py all                          # everything Tier 1+2
  python3 fetch.py prices                       # all tracked tickers
  python3 fetch.py econ                         # all tracked FRED series
"""

import json, os, sys, time, urllib.request, urllib.parse
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

FRED_API_KEY = "8ce3f08db56f151f54221a0dd12b63de"
FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"

CACHE_DIR = Path(__file__).parent / ".cache"
CACHE_TTL = 300  # 5 minutes

# --- Tier 1: Decision Drivers ---
TIER1_PRICES = {
    "BZ=F":   "Brent Crude",
    "JPY=X":  "USD/JPY",
}

TIER1_FRED = {
    "BAMLH0A0HYM2": "HY OAS",
    "ICSA":          "Initial Claims",
    "CCSA":          "Continuing Claims",
    "GASREGW":       "Gas Price (wkly avg)",
}

# --- Tier 2: Position Monitoring ---
TIER2_PRICES = {
    "KRE":    "Regional Banks ETF",
    "APO":    "Apollo Global",
    "ARES":   "Ares Management",
    "OZK":    "Bank OZK",
    "WAL":    "Western Alliance",
    "FXY":    "Yen ETF",
    "TLT":    "20Y+ Treasury ETF",
    "^VIX":   "VIX",
}

ALL_PRICES = {**TIER1_PRICES, **TIER2_PRICES}
ALL_FRED = {**TIER1_FRED}

# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------

def _cache_path(key):
    CACHE_DIR.mkdir(exist_ok=True)
    safe = key.replace("/", "_").replace("^", "_").replace("=", "_")
    return CACHE_DIR / f"{safe}.json"

def _cache_get(key):
    p = _cache_path(key)
    if not p.exists():
        return None
    data = json.loads(p.read_text())
    if time.time() - data.get("ts", 0) > CACHE_TTL:
        return None
    return data.get("val")

def _cache_set(key, val):
    p = _cache_path(key)
    p.write_text(json.dumps({"ts": time.time(), "val": val}))

# ---------------------------------------------------------------------------
# FRED
# ---------------------------------------------------------------------------

def fred_fetch(series_id, limit=5):
    cached = _cache_get(f"fred_{series_id}_{limit}")
    if cached:
        return cached

    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "sort_order": "desc",
        "limit": limit,
    }
    url = f"{FRED_BASE}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        obs = data.get("observations", [])
        result = [{"date": o["date"], "value": o["value"]} for o in obs if o["value"] != "."]
        _cache_set(f"fred_{series_id}_{limit}", result)
        return result
    except Exception as e:
        return [{"error": str(e)}]

# ---------------------------------------------------------------------------
# Prices (yfinance)
# ---------------------------------------------------------------------------

def price_fetch(tickers):
    """Fetch current prices for a list of tickers. Returns dict of ticker -> {price, change, prev}."""
    cache_key = f"prices_{'_'.join(sorted(tickers))}"
    cached = _cache_get(cache_key)
    if cached:
        return cached

    try:
        import yfinance as yf
        data = yf.download(tickers, period="2d", progress=False, threads=True)

        if data.empty:
            return {"error": "No data returned"}

        results = {}
        close = data["Close"]

        for t in tickers:
            try:
                if len(tickers) == 1:
                    curr = close.iloc[-1]
                    prev = close.iloc[-2] if len(close) > 1 else None
                else:
                    curr = close[t].iloc[-1]
                    prev = close[t].iloc[-2] if len(close) > 1 else None

                chg = ((curr - prev) / prev * 100) if prev else None
                results[t] = {
                    "price": round(float(curr), 2),
                    "prev": round(float(prev), 2) if prev else None,
                    "change": round(float(chg), 2) if chg is not None else None,
                }
            except Exception:
                results[t] = {"error": f"Failed to parse {t}"}

        _cache_set(cache_key, results)
        return results
    except Exception as e:
        return {"error": str(e)}

# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------

def display_prices(results, labels=None):
    if "error" in results:
        print(f"  ERROR: {results['error']}")
        return

    print(f"\n  {'Ticker':<10} {'Name':<22} {'Price':>10} {'Change':>10}")
    print(f"  {'-'*54}")

    for t, d in results.items():
        if "error" in d:
            print(f"  {t:<10} {'':22} {'ERROR':>10}")
            continue
        name = (labels or {}).get(t, "")[:21]
        p = f"${d['price']:,.2f}" if d["price"] < 1000 else f"{d['price']:,.2f}"
        chg = f"{d['change']:+.2f}%" if d["change"] is not None else "N/A"
        print(f"  {t:<10} {name:<22} {p:>10} {chg:>10}")

def display_fred(series_id, label, obs):
    if obs and "error" in obs[0]:
        print(f"  {label}: ERROR — {obs[0]['error']}")
        return

    latest = obs[0] if obs else None
    if not latest:
        print(f"  {label}: NO DATA")
        return

    val = latest["value"]
    # Format large numbers with commas
    try:
        num = float(val)
        if num > 10000:
            formatted = f"{num:,.0f}"
        elif num > 100:
            formatted = f"{num:,.1f}"
        else:
            formatted = f"{num}"
    except ValueError:
        formatted = val

    print(f"  {label:<25} {formatted:>12}   ({latest['date']})")

    if len(obs) > 1:
        for o in obs[1:]:
            v = o["value"]
            try:
                n = float(v)
                if n > 10000:
                    v = f"{n:,.0f}"
                elif n > 100:
                    v = f"{n:,.1f}"
            except ValueError:
                pass
            print(f"  {'':25} {v:>12}   ({o['date']})")

# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_price(tickers):
    labels = {**ALL_PRICES}
    results = price_fetch(tickers)
    display_prices(results, labels)

def cmd_fred(series_id, periods=5):
    label = ALL_FRED.get(series_id, series_id)
    obs = fred_fetch(series_id, limit=periods)
    print()
    display_fred(series_id, label, obs)

def cmd_prices():
    print("\n=== TRACKED PRICES ===")
    results = price_fetch(list(ALL_PRICES.keys()))
    display_prices(results, ALL_PRICES)

def cmd_econ():
    print("\n=== ECONOMIC DATA (FRED) ===\n")
    for sid, label in ALL_FRED.items():
        obs = fred_fetch(sid, limit=1)
        display_fred(sid, label, obs)

def cmd_all():
    cmd_prices()
    cmd_econ()
    print()

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = sys.argv[1:]

    if not args or args[0] == "all":
        cmd_all()
        return

    if args[0] == "prices":
        cmd_prices()
        return

    if args[0] == "econ":
        cmd_econ()
        return

    if args[0] == "price":
        if len(args) < 2:
            print("Usage: fetch.py price TICKER [TICKER ...]")
            return
        cmd_price(args[1:])
        return

    if args[0] == "fred":
        if len(args) < 2:
            print("Usage: fetch.py fred SERIES_ID [--periods N]")
            return
        periods = 5
        for i, a in enumerate(args):
            if a == "--periods" and i + 1 < len(args):
                periods = int(args[i + 1])
        cmd_fred(args[1], periods)
        return

    # Fallback — treat args as tickers
    cmd_price(args)

if __name__ == "__main__":
    main()
