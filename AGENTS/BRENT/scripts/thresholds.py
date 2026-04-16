#!/usr/bin/env python3
"""
BRENT Threshold Monitor
Pulls live oil/energy market prices (yfinance) and economic data (FRED) and
compares against BRENT's two-phase oil thesis thresholds.

Thresholds sourced from BRENT VX.tsv, STATUS.md, CLAUDE.md.

Color key:
  BREACHED  = threshold crossed
  WARNING   = within 5% of threshold

Classifications:
  risk    (🔴) = price moving bad for thesis (demand destruction, stop hit)
  thesis  (🟢) = price confirming thesis (squeeze intensifying)
  stress  (🟠) = structural stress level (not directional)

Usage:
  .venv/bin/python3 AGENTS/BRENT/scripts/thresholds.py
  .venv/bin/python3 AGENTS/BRENT/scripts/thresholds.py --json
"""

import json
import os
import sys
import urllib.request
import urllib.parse
from datetime import datetime

try:
    import yfinance as yf
except ImportError:
    print("  ERROR: yfinance not installed.")
    sys.exit(1)

# ---------------------------------------------------------------------------
# FRED config (same key as CARL)
# ---------------------------------------------------------------------------

FRED_API_KEY = os.environ.get("FRED_API_KEY", "8ce3f08db56f151f54221a0dd12b63de")
FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"

# ---------------------------------------------------------------------------
# Market thresholds (yfinance)
# (ticker, direction, level, classification, label)
# ---------------------------------------------------------------------------

MARKET_THRESHOLDS = [
    # ── Brent futures (BZ=F)
    ("BZ=F",  "above", 140.0, "stress",  "Brent >$140 — extreme dislocation (ATH intraweek)"),
    ("BZ=F",  "above", 120.0, "risk",    "Brent >$120 — demand destruction accelerates, Phase 2 approaches"),
    ("BZ=F",  "above", 100.0, "thesis",  "Brent >$100 — HAWK Scenario C confirmed, Phase 1 active"),
    ("BZ=F",  "below",  85.0, "risk",    "Brent <$85 — squeeze weakening, paper market front-running peace"),
    ("BZ=F",  "below",  75.0, "risk",    "Brent <$75 — THESIS BREAK, squeeze failed"),
    # ── WTI futures (CL=F)
    ("CL=F",  "above", 100.0, "thesis",  "WTI >$100 — Phase 1 broad"),
    ("CL=F",  "below",  70.0, "risk",    "WTI <$70 — US decoupling stress"),
    # ── USO (position)
    ("USO",   "below",  80.0, "risk",    "USO approaching drawdown watch"),
    ("USO",   "below",  75.0, "risk",    "USO stop territory"),
    # ── STNG (tanker position)
    ("STNG",  "below",  71.50, "risk",   "STNG STOP LEVEL — exit trigger"),
    ("STNG",  "above", 100.0, "thesis",  "STNG target zone — tanker super-cycle pricing in"),
    # ── LNG / Cheniere
    ("LNG",   "above", 255.0, "thesis",  "Cheniere in position zone (research BRT-10)"),
    ("LNG",   "above", 285.0, "thesis",  "Cheniere analyst PT range — LNG beat territory"),
    # ── Venture Global (VG — maximum leverage per BRT-10)
    ("VG",    "above",  15.0, "thesis",  "VG benefitting from spot LNG windfall"),
    # ── Energy ETFs (context)
    ("XLE",   "above", 100.0, "thesis",  "Energy sector leadership confirmed"),
    ("XOP",   "above", 150.0, "thesis",  "E&P sector broad strength"),
    # ── Refiners (crack-spread proxies)
    ("VLO",   "above", 160.0, "thesis",  "Refiner margins strong — crack spread wide"),
    ("MPC",   "above", 170.0, "thesis",  "MPC — crack spread beneficiary"),
    # ── Natgas (LNG spot cross-ref)
    ("NG=F",  "above",   4.0, "stress",  "Natgas >$4 — Atlantic basin competition"),
    ("NG=F",  "above",   5.0, "stress",  "Natgas >$5 — US gas market tight"),
]

# Context tickers (quoted but no thresholds)
CONTEXT_TICKERS = ["BZ=F", "CL=F", "USO", "STNG", "LNG", "VG", "XLE", "XOP", "VLO", "MPC",
                   "NG=F", "UNG", "FRO", "EURN", "DHT", "HAL", "SLB", "CVX", "XOM", "^VIX"]

# ---------------------------------------------------------------------------
# FRED thresholds
# (series_id, label, direction, level, classification, threshold_label)
# ---------------------------------------------------------------------------

FRED_THRESHOLDS = [
    # Dated Brent (physical)
    ("DCOILBRENTEU", "Dated Brent",        "above", 140.0, "stress",  "Dated Brent >$140 — extreme (ATH $144)"),
    ("DCOILBRENTEU", "Dated Brent",        "above", 120.0, "stress",  "Dated Brent >$120 — physical scarcity confirmed"),
    ("DCOILBRENTEU", "Dated Brent",        "below", 100.0, "risk",    "Dated Brent <$100 — physical squeeze resolving"),
    # WTI spot
    ("DCOILWTICO",   "WTI Spot",           "above", 100.0, "thesis",  "WTI >$100 — broad Phase 1"),
    # HY OAS — primary stress indicator (broad HY as energy proxy; no free energy-only series)
    ("BAMLH0A0HYM2", "HY Total OAS",       "above",   4.5, "risk",    "HY OAS >450bps — credit dislocation"),
    ("BAMLH0A0HYM2", "HY Total OAS",       "above",   3.5, "stress",  "HY OAS >350bps — stress threshold"),
    ("BAMLH0A0HYM2", "HY Total OAS",       "above",   3.0, "stress",  "HY OAS >300bps — elevated (currently)"),
    # Natural gas context
    ("DHHNGSP",      "Henry Hub Natgas",   "above",   4.0, "stress",  "Henry Hub >$4 — gas market tight"),
    # Retail gas (CARL owns primary, BRENT cross-ref)
    ("GASREGW",      "US Retail Gas",      "above",   4.50, "risk",   "Retail >$4.50 — next CARL breakpoint"),
    ("GASREGW",      "US Retail Gas",      "above",   4.00, "stress", "Retail >$4.00 — behavioral breakpoint (CONFIRMED)"),
]

# Context FRED series (display only)
CONTEXT_FRED = [
    ("DCOILBRENTEU", "Dated Brent"),
    ("DCOILWTICO",   "WTI Spot"),
    ("BAMLH0A0HYM2", "HY Total OAS (%)"),
    ("DHHNGSP",      "Henry Hub Gas"),
    ("GASREGW",      "US Retail Gas"),
]

WARN_PCT = 0.05  # 5% proximity warning

# ---------------------------------------------------------------------------
# FRED fetcher (urllib)
# ---------------------------------------------------------------------------

def fred_fetch(series_id, limit=3):
    """Fetch latest observations from FRED. Returns list of {date, value}."""
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "sort_order": "desc",
        "limit": limit,
    }
    url = f"{FRED_BASE}?{urllib.parse.urlencode(params)}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "BRENT-Monitor/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        obs = data.get("observations", [])
        return [{"date": o["date"], "value": o["value"]} for o in obs if o["value"] != "."]
    except Exception as e:
        return [{"error": str(e)}]


# ---------------------------------------------------------------------------
# Market price fetcher (yfinance)
# ---------------------------------------------------------------------------

def get_prices(symbols):
    """Fetch current prices. Returns dict symbol -> {price, prev, chg}."""
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


# ---------------------------------------------------------------------------
# Threshold checking
# ---------------------------------------------------------------------------

def check_market_thresholds(prices):
    results = []
    warning_candidates = {}

    for ticker, direction, level, clas, label in MARKET_THRESHOLDS:
        p = prices.get(ticker)
        if not p:
            continue
        price = p["price"]
        dist = (price - level) / level * 100

        if direction == "above":
            if price > level:
                results.append({"ticker": ticker, "level": level, "label": label,
                                "class": clas, "status": "BREACHED", "price": price,
                                "dist": dist, "direction": direction, "source": "market"})
            elif price > level * (1 - WARN_PCT):
                cand = {"ticker": ticker, "level": level, "label": label,
                        "class": clas, "status": "WARNING", "price": price,
                        "dist": dist, "direction": direction, "source": "market"}
                key = (ticker, direction)
                if key not in warning_candidates or abs(dist) < abs(warning_candidates[key]["dist"]):
                    warning_candidates[key] = cand
        else:
            if price < level:
                results.append({"ticker": ticker, "level": level, "label": label,
                                "class": clas, "status": "BREACHED", "price": price,
                                "dist": dist, "direction": direction, "source": "market"})
            elif price < level * (1 + WARN_PCT):
                cand = {"ticker": ticker, "level": level, "label": label,
                        "class": clas, "status": "WARNING", "price": price,
                        "dist": dist, "direction": direction, "source": "market"}
                key = (ticker, direction)
                if key not in warning_candidates or abs(dist) < abs(warning_candidates[key]["dist"]):
                    warning_candidates[key] = cand

    results.extend(warning_candidates.values())
    return results


def check_fred_thresholds(fred_data):
    results = []
    warning_candidates = {}

    for series_id, label, direction, level, clas, thresh_label in FRED_THRESHOLDS:
        obs = fred_data.get(series_id, [])
        if not obs or "error" in obs[0]:
            continue
        try:
            value = float(obs[0]["value"])
        except (ValueError, KeyError):
            continue

        dist = (value - level) / level * 100

        if direction == "above":
            if value > level:
                results.append({"ticker": series_id, "level": level, "label": thresh_label,
                                "class": clas, "status": "BREACHED", "price": value,
                                "dist": dist, "direction": direction, "source": "fred",
                                "date": obs[0]["date"], "series_label": label})
            elif value > level * (1 - WARN_PCT):
                cand = {"ticker": series_id, "level": level, "label": thresh_label,
                        "class": clas, "status": "WARNING", "price": value,
                        "dist": dist, "direction": direction, "source": "fred",
                        "date": obs[0]["date"], "series_label": label}
                key = (series_id, direction, level)
                if key not in warning_candidates or abs(dist) < abs(warning_candidates[key]["dist"]):
                    warning_candidates[key] = cand
        else:
            if value < level:
                results.append({"ticker": series_id, "level": level, "label": thresh_label,
                                "class": clas, "status": "BREACHED", "price": value,
                                "dist": dist, "direction": direction, "source": "fred",
                                "date": obs[0]["date"], "series_label": label})
            elif value < level * (1 + WARN_PCT):
                cand = {"ticker": series_id, "level": level, "label": thresh_label,
                        "class": clas, "status": "WARNING", "price": value,
                        "dist": dist, "direction": direction, "source": "fred",
                        "date": obs[0]["date"], "series_label": label}
                key = (series_id, direction, level)
                if key not in warning_candidates or abs(dist) < abs(warning_candidates[key]["dist"]):
                    warning_candidates[key] = cand

    results.extend(warning_candidates.values())
    return results


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------

def emoji_for(clas, status):
    if status == "BREACHED":
        return {"risk": "🔴", "thesis": "🟢", "stress": "🟠"}[clas]
    else:
        return {"risk": "⚠️ ", "thesis": "🟡", "stress": "🟠"}[clas]


def fmt_value(value):
    if abs(value) > 1000:
        return f"{value:,.0f}"
    if abs(value) > 10:
        return f"{value:.2f}"
    return f"{value:.3f}"


def print_alerts(alerts, header):
    if not alerts:
        return
    print(f"\n  {header}")
    print(f"  {'-'*64}")
    for a in alerts:
        e = emoji_for(a["class"], a["status"])
        val_str = fmt_value(a["price"])
        lev_str = fmt_value(a["level"])
        src = f" ({a['date']})" if a.get("date") else ""
        print(f"  {e} {a['ticker']:<16} {val_str:>12}  (level {lev_str}, {a['dist']:+.1f}%){src}")
        print(f"              {a['label']}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    json_mode = "--json" in sys.argv
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Collect all market symbols
    threshold_syms = list(set(t[0] for t in MARKET_THRESHOLDS))
    all_syms = list(set(threshold_syms + CONTEXT_TICKERS))

    if not json_mode:
        print(f"\n{'='*72}")
        print(f"  BRENT Threshold Monitor — {now}")
        print(f"{'='*72}")

    # Market
    if not json_mode:
        print(f"\n  Fetching market data...", flush=True)
    prices = get_prices(all_syms)

    # FRED
    if not json_mode:
        print(f"  Fetching FRED data...", flush=True)
    fred_series = list(set([t[0] for t in FRED_THRESHOLDS] + [s[0] for s in CONTEXT_FRED]))
    fred_data = {}
    for sid in fred_series:
        fred_data[sid] = fred_fetch(sid, limit=3)

    # Check thresholds
    market_alerts = check_market_thresholds(prices)
    fred_alerts = check_fred_thresholds(fred_data)
    all_alerts = market_alerts + fred_alerts

    if json_mode:
        output = {
            "timestamp": now,
            "alerts": all_alerts,
            "prices": {s: prices[s] for s in sorted(prices)},
            "fred": {s: fred_data[s] for s in sorted(fred_data)},
        }
        print(json.dumps(output, indent=2))
        return 0

    # Display alerts
    breaches_risk = [a for a in all_alerts if a["status"] == "BREACHED" and a["class"] == "risk"]
    breaches_thesis = [a for a in all_alerts if a["status"] == "BREACHED" and a["class"] == "thesis"]
    breaches_stress = [a for a in all_alerts if a["status"] == "BREACHED" and a["class"] == "stress"]
    warnings = [a for a in all_alerts if a["status"] == "WARNING"]

    print_alerts(breaches_risk,   "🔴 RISK BREACHES (bad for thesis)")
    print_alerts(breaches_thesis, "🟢 THESIS CONFIRMING BREACHES")
    print_alerts(breaches_stress, "🟠 STRUCTURAL STRESS BREACHES")
    print_alerts(warnings,        "⚠️  NEAR THRESHOLDS (within 5%)")

    if not any([breaches_thesis, breaches_risk, breaches_stress, warnings]):
        print(f"\n  ✅ No threshold breaches or warnings.")

    # Crude / futures snapshot
    print(f"\n  CRUDE & FUTURES")
    print(f"  {'-'*64}")
    crude_display = [
        ("BZ=F", "Brent futures"),
        ("CL=F", "WTI futures"),
        ("NG=F", "Natgas futures"),
    ]
    for sym, label in crude_display:
        p = prices.get(sym)
        if p:
            arrow = "🟢" if p["chg"] >= 0 else "🔴"
            print(f"  {arrow} {label:<22} ${p['price']:>8.2f}  ({p['chg']:+.2f}%)")

    # Positions
    print(f"\n  POSITIONS")
    print(f"  {'-'*64}")
    pos_display = [
        ("USO", "USO (oil long)"),
        ("STNG", "STNG (tanker)"),
        ("LNG", "Cheniere"),
        ("VG", "Venture Global"),
    ]
    for sym, label in pos_display:
        p = prices.get(sym)
        if p:
            arrow = "🟢" if p["chg"] >= 0 else "🔴"
            print(f"  {arrow} {label:<22} ${p['price']:>8.2f}  ({p['chg']:+.2f}%)")

    # Energy sector
    print(f"\n  ENERGY SECTOR")
    print(f"  {'-'*64}")
    energy_display = [
        ("XLE", "Energy ETF"),
        ("XOP", "E&P ETF"),
        ("XOM", "Exxon"),
        ("CVX", "Chevron"),
        ("HAL", "Halliburton"),
        ("SLB", "Schlumberger"),
        ("VLO", "Valero (refiner)"),
        ("MPC", "Marathon (refiner)"),
    ]
    for sym, label in energy_display:
        p = prices.get(sym)
        if p:
            arrow = "🟢" if p["chg"] >= 0 else "🔴"
            print(f"  {arrow} {label:<22} ${p['price']:>8.2f}  ({p['chg']:+.2f}%)")

    # Tanker universe
    print(f"\n  TANKERS (proxy for VLCC/LR2/MR rates)")
    print(f"  {'-'*64}")
    tanker_display = [
        ("FRO",  "Frontline (VLCC)"),
        ("EURN", "Euronav (VLCC/Suezmax)"),
        ("DHT",  "DHT (VLCC pure)"),
        ("STNG", "Scorpio (product)"),
    ]
    for sym, label in tanker_display:
        p = prices.get(sym)
        if p:
            arrow = "🟢" if p["chg"] >= 0 else "🔴"
            print(f"  {arrow} {label:<22} ${p['price']:>8.2f}  ({p['chg']:+.2f}%)")

    # FRED snapshot
    print(f"\n  FRED LATEST VALUES")
    print(f"  {'-'*64}")
    for sid, label in CONTEXT_FRED:
        obs = fred_data.get(sid, [])
        if obs and "error" not in obs[0]:
            val = obs[0]["value"]
            date = obs[0]["date"]
            try:
                num = float(val)
                formatted = fmt_value(num)
            except ValueError:
                formatted = val
            prior_str = ""
            if len(obs) > 1:
                try:
                    prior = float(obs[1]["value"])
                    diff = num - prior
                    prior_str = f"  (prior {fmt_value(prior)}, {diff:+.2f})"
                except (ValueError, KeyError):
                    pass
            print(f"  {label:<26} {formatted:>10}  as of {date}{prior_str}")
        else:
            err = obs[0].get("error", "no data") if obs else "no data"
            print(f"  {label:<26} {'ERROR':>10}  {err[:50]}")

    # Macro context
    print(f"\n  MACRO CONTEXT")
    print(f"  {'-'*64}")
    p = prices.get("^VIX")
    if p:
        arrow = "🔴" if p["chg"] >= 0 else "🟢"  # rising VIX = risk-off
        print(f"  {arrow} {'VIX':<10} {p['price']:>10.2f}  ({p['chg']:+.2f}%)")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
