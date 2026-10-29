#!/usr/bin/env python3
"""
CARL Threshold Monitor
Pulls live market prices (yfinance) and economic data (FRED) and compares
against CARL consumer-stress thesis thresholds.

Legacy diagnostic screens. Levels are not registered prediction/vector gates;
VX.tsv is frozen. A screen crossing cannot establish credit deterioration.

Color key:
  BREACHED  = legacy screen crossed; no registered thesis grade
  WARNING   = within 5% of threshold

Usage:
  .venv/bin/python3 AGENTS/CARL/scripts/thresholds.py
  .venv/bin/python3 AGENTS/CARL/scripts/thresholds.py --json
"""

import json
import os
import sys
import urllib.request
import urllib.parse
from datetime import datetime, timezone

try:
    import yfinance as yf
except ImportError:
    print("  ERROR: yfinance not installed.")
    sys.exit(1)

# ---------------------------------------------------------------------------
# FRED config (same key/pattern as FORGE/tools/market-data/fetch.py)
# ---------------------------------------------------------------------------

def _fred_key():
    """Env first, else the gitignored FORGE market-data .env (single per-machine home).
    Hardcoded copies scrubbed 2026-07-01 (public-prep) — never hardcode this key."""
    import pathlib, sys
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
FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"

# ---------------------------------------------------------------------------
# Market thresholds (yfinance)
# (ticker, direction, level, classification, label)
# direction: "above" = breach when price > level, "below" = breach when price < level
# classification: "risk" (bad for thesis), "thesis" (confirming), "stress" (structural)
# ---------------------------------------------------------------------------

MARKET_THRESHOLDS = [
    # Consumer credit canaries
    ("SYF",  "below",  25.0, "thesis",  "SYF legacy price screen below $25"),
    ("SYF",  "below",  30.0, "thesis",  "SYF legacy price screen — no NCO inference"),
    ("ALLY", "below",  25.0, "thesis",  "ALLY legacy price screen below $25"),
    ("ALLY", "below",  30.0, "thesis",  "ALLY legacy price screen below $30"),
    # DFS removed 2026-10-28: Discover was acquired by Capital One and no longer trades;
    # the dead ticker made every boot report INCOMPLETE DATA / FAIL. COF covers the book.
    ("COF",  "below", 120.0, "thesis",  "COF stress — subprime CC deterioration"),
    # Homebuilders (K-shape: LEN stressed, TOL resilient)
    ("LEN",  "below", 100.0, "thesis",  "LEN entry-level builder crisis"),
    ("LEN",  "below", 120.0, "thesis",  "LEN margin pressure accelerating"),
    ("DHI",  "below", 100.0, "thesis",  "DHI entry-level builder stress"),
    ("TOL",  "below", 100.0, "thesis",  "TOL upper-end stress — K-shape closing"),
    ("PHM",  "below", 100.0, "thesis",  "PHM builder stress — mid-market"),
    # Broad consumer / retail
    ("XLY",  "below", 170.0, "thesis",  "Consumer discretionary breakdown"),
    ("XRT",  "below",  65.0, "thesis",  "Retail ETF stress"),
    # Credit / spreads
    ("HYG",  "below",  75.0, "thesis",  "HY credit stress — spreads widening"),
    ("HYG",  "below",  72.0, "thesis",  "HY acute stress — dislocation"),
    # Cross-reference REGINALD
    ("KRE",  "below",  55.0, "thesis",  "Regional bank stress — consumer credit transmission"),
    ("KRE",  "below",  60.0, "thesis",  "KRE approaching prior stress level"),
    # Oil / energy (consumer squeeze)
    ("BZ=F", "above", 120.0, "risk",    "Brent >$120 — demand destruction accelerates"),
    ("BZ=F", "above", 100.0, "stress",  "Brent >$100 — gas squeeze active"),
    # Macro context
    ("SPY",  "below", 480.0, "thesis",  "SPX correction — reverse wealth effect activates"),
    ("SPY",  "below", 510.0, "thesis",  "SPX approaching correction territory"),
]

# Tickers quoted for context (no thresholds)
CONTEXT_TICKERS = ["^VIX", "^TNX", "TLT", "IWM"]

# ---------------------------------------------------------------------------
# FRED thresholds
# (series_id, label, direction, level, classification, threshold_label)
# ---------------------------------------------------------------------------

FRED_THRESHOLDS = [
    # Gas prices
    ("GASREGW",       "Gas Price (wkly EIA)",     "above",  4.50, "thesis",  "Gas >$4.50 — next behavioral breakpoint"),
    ("GASREGW",       "Gas Price (wkly EIA)",     "above",  4.00, "stress",  "Gas >$4 — behavioral breakpoint FIRED"),
    # Mortgage rates
    ("MORTGAGE30US",  "30yr Mortgage",            "above",  7.00, "thesis",  "Mortgage >7% — housing freeze"),
    ("MORTGAGE30US",  "30yr Mortgage",            "above",  6.50, "stress",  "Mortgage >6.5% — demand destruction"),
    # HY spreads
    ("BAMLH0A0HYM2", "HY OAS",                   "above",  4.50, "thesis",  "HY OAS >450bps — credit dislocation"),
    ("BAMLH0A0HYM2", "HY OAS",                   "above",  3.50, "stress",  "HY OAS >350bps — stress threshold"),
    ("BAMLH0A0HYM2", "HY OAS",                   "above",  3.00, "stress",  "HY OAS >300bps — elevated"),
    # Claims
    ("ICSA",          "Initial Claims (wkly)",    "above", 300000, "thesis", "Claims >300K — labor market breaking"),
    ("ICSA",          "Initial Claims (wkly)",    "above", 250000, "stress", "Claims >250K — deterioration"),
    ("CCSA",          "Continuing Claims",        "above", 2000000, "thesis","Cont. claims >2M — RED threshold"),
    ("CCSA",          "Continuing Claims",        "above", 1900000, "stress","Cont. claims >1.9M — YELLOW threshold"),
    # Savings rate
    ("PSAVERT",       "Personal Savings Rate",    "below",  3.00, "thesis",  "Savings <3% — RED, consumer buffer depleted"),
    ("PSAVERT",       "Personal Savings Rate",    "below",  4.00, "stress",  "Savings <4% — YELLOW, buffer thinning"),
    # Core PCE
    ("PCEPILFE",      "Core PCE (index)",         "above",  None, "stress",  "Core PCE — track direction (level is index, YoY computed)"),
    # Sentiment
    ("UMCSENT",       "UMich Sentiment",          "below", 55.0,  "thesis",  "UMich <55 — recessionary territory"),
    # Brent (FRED daily)
    ("DCOILBRENTEU",  "Brent Crude (FRED)",       "above", 120.0, "risk",    "Brent >$120 — oil shock"),
    ("DCOILBRENTEU",  "Brent Crude (FRED)",       "above", 100.0, "stress",  "Brent >$100 — gas squeeze"),
]

WARN_PCT = 0.05  # 5% proximity warning

# ---------------------------------------------------------------------------
# FRED fetcher (urllib, no fredapi dependency)
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
        req = urllib.request.Request(url, headers={"User-Agent": "CARL-Monitor/1.0"})
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
                current = info.get("regularMarketPrice")
                price = current or info.get("previousClose")
                prev = info.get("previousClose") or info.get("regularMarketPreviousClose")
                if price:
                    chg = ((price - prev) / prev * 100) if prev else 0
                    stamp = info.get("regularMarketTime") if current else None
                    prices[sym] = {
                        "price": price, "prev": prev, "chg": chg,
                        "basis": "regularMarketPrice" if current else "previousClose fallback",
                        "asof_utc": datetime.fromtimestamp(stamp, timezone.utc).isoformat() if stamp else None,
                    }
            except Exception:
                pass
    except Exception as e:
        print(f"  ERROR fetching prices: {e}")
    return prices


# ---------------------------------------------------------------------------
# Threshold checking
# ---------------------------------------------------------------------------

def check_market_thresholds(prices):
    """Check market thresholds. Breaches always reported; warnings: nearest per (ticker, direction)."""
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
        else:  # below
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
    """Check FRED thresholds. Returns list of alert dicts."""
    results = []
    warning_candidates = {}

    for series_id, label, direction, level, clas, thresh_label in FRED_THRESHOLDS:
        if level is None:  # direction-only tracking (e.g., PCE index)
            continue
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
        else:  # below
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
        return {"risk": "\U0001f534", "thesis": "\U0001f7e2", "stress": "\U0001f7e0"}[clas]
    else:
        return {"risk": "\u26a0\ufe0f ", "thesis": "\U0001f7e1", "stress": "\U0001f7e0"}[clas]


def fmt_value(value, series_id=None):
    """Format a numeric value contextually."""
    if series_id == "BAMLH0A0HYM2":
        return f"{value * 100:.1f}"  # FRED percentage points -> displayed bp
    if series_id and series_id in ("ICSA", "CCSA"):
        return f"{value:,.0f}"
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
        val_str = fmt_value(a["price"], a.get("ticker"))
        lev_str = fmt_value(a["level"], a.get("ticker"))
        src = f" ({a['date']})" if a.get("date") else ""
        print(f"  {e} {a['ticker']:<16} {val_str:>12}  (level {lev_str}, {a['dist']:+.1f}%){src}")
        print(f"              LEGACY SCREEN ONLY: {a['label']}; no registered grade")


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
        print(f"  CARL Threshold Monitor \u2014 {now}")
        print("  LEGACY DIAGNOSTIC — screens are not registered gates or thesis confirmations")
        print(f"{'='*72}")

    # --- Market data ---
    if not json_mode:
        print(f"\n  Fetching market data...", flush=True)
    prices = get_prices(all_syms)

    # --- FRED data ---
    if not json_mode:
        print(f"  Fetching FRED data...", flush=True)
    fred_series = list(set(t[0] for t in FRED_THRESHOLDS))
    fred_data = {}
    for sid in fred_series:
        fred_data[sid] = fred_fetch(sid, limit=3)

    # --- Check thresholds ---
    market_alerts = check_market_thresholds(prices)
    fred_alerts = check_fred_thresholds(fred_data)
    all_alerts = market_alerts + fred_alerts
    missing_market = sorted(set(all_syms) - prices.keys())
    missing_fred = sorted(s for s in fred_series
                          if not fred_data.get(s) or "error" in fred_data[s][0])
    incomplete = bool(missing_market or missing_fred)

    if json_mode:
        output = {
            "timestamp": now,
            "diagnostic_only": True,
            "coverage": {"missing_market": missing_market, "missing_fred": missing_fred},
            "alerts": all_alerts,
            "prices": {s: prices[s] for s in sorted(prices)},
            "fred": {s: fred_data[s] for s in sorted(fred_data)},
        }
        print(json.dumps(output, indent=2))
        return 1 if incomplete else 0

    # --- Display alerts ---
    breaches_thesis = [a for a in all_alerts if a["status"] == "BREACHED" and a["class"] == "thesis"]
    breaches_risk = [a for a in all_alerts if a["status"] == "BREACHED" and a["class"] == "risk"]
    breaches_stress = [a for a in all_alerts if a["status"] == "BREACHED" and a["class"] == "stress"]
    warnings = [a for a in all_alerts if a["status"] == "WARNING"]

    print_alerts(breaches_risk, "LEGACY RISK SCREENS — diagnostic only")
    print_alerts(breaches_thesis, "LEGACY PRICE/DATA SCREENS — not thesis confirmation")
    print_alerts(breaches_stress, "LEGACY CONTEXT SCREENS — diagnostic only")
    print_alerts(warnings, "\u26a0\ufe0f  NEAR THRESHOLDS (within 5%)")

    if not any([breaches_thesis, breaches_risk, breaches_stress, warnings]):
        print("\n  No screen crossings among available observations; missing inputs remain unassessed.")
    if incomplete:
        print(f"  WARNING: INCOMPLETE DATA — missing market: {', '.join(missing_market) or 'none'}; "
              f"missing FRED: {', '.join(missing_fred) or 'none'}")

    # --- Consumer credit canaries ---
    print(f"\n  CONSUMER CREDIT CANARIES")
    print(f"  {'-'*64}")
    canaries = ["SYF", "ALLY", "COF"]
    for sym in canaries:
        p = prices.get(sym)
        if p:
            arrow = "\U0001f7e2" if p["chg"] >= 0 else "\U0001f534"
            print(f"  {arrow} {sym:<8} ${p['price']:>10.2f}  ({p['chg']:+.2f}%) "
                  f"[{p.get('basis', 'UNKNOWN basis')}; asof {p.get('asof_utc') or 'UNKNOWN'}]")

    # --- Homebuilders (K-shape) ---
    print(f"\n  HOMEBUILDER K-SHAPE")
    print(f"  {'-'*64}")
    builders = ["LEN", "DHI", "PHM", "TOL"]
    for sym in builders:
        p = prices.get(sym)
        if p:
            arrow = "\U0001f7e2" if p["chg"] >= 0 else "\U0001f534"
            tag = ""
            if sym == "LEN":
                tag = " (entry-level; no live margin observation)"
            elif sym == "TOL":
                tag = " (luxury; no live margin observation)"
            print(f"  {arrow} {sym:<8} ${p['price']:>10.2f}  ({p['chg']:+.2f}%){tag} "
                  f"[{p.get('basis', 'UNKNOWN basis')}; asof {p.get('asof_utc') or 'UNKNOWN'}]")

    # --- FRED latest values ---
    print(f"\n  FRED LATEST VALUES")
    print(f"  {'-'*64}")
    display_order = [
        ("GASREGW", "Gas (wkly avg)"),
        ("MORTGAGE30US", "30yr Mortgage"),
        ("BAMLH0A0HYM2", "HY OAS (bps)"),
        ("ICSA", "Initial Claims"),
        ("CCSA", "Continuing Claims"),
        ("PSAVERT", "Savings Rate (%)"),
        ("UMCSENT", "UMich Sentiment"),
        ("DCOILBRENTEU", "Brent Crude"),
    ]
    for sid, label in display_order:
        obs = fred_data.get(sid, [])
        if obs and "error" not in obs[0]:
            val = obs[0]["value"]
            date = obs[0]["date"]
            try:
                num = float(val)
                formatted = fmt_value(num, sid)
            except ValueError:
                formatted = val
            # Show prior value if available
            prior_str = ""
            if len(obs) > 1:
                try:
                    prior = float(obs[1]["value"])
                    diff = num - prior
                    if sid in ("ICSA", "CCSA"):
                        prior_str = f"  (prior {fmt_value(prior, sid)}, {diff:+,.0f})"
                    elif sid == "BAMLH0A0HYM2":
                        prior_str = f"  (prior {fmt_value(prior, sid)}, {diff * 100:+.1f} bp)"
                    else:
                        prior_str = f"  (prior {fmt_value(prior, sid)}, {diff:+.2f})"
                except (ValueError, KeyError):
                    pass
            print(f"  {label:<22} {formatted:>12}  as of {date}{prior_str}")
        else:
            err = obs[0].get("error", "no data") if obs else "no data"
            print(f"  {label:<22} {'ERROR':>12}  {err[:50]}")

    # --- Context tickers ---
    print(f"\n  MACRO CONTEXT")
    print(f"  {'-'*64}")
    context_display = ["SPY", "IWM", "^VIX", "^TNX", "TLT", "BZ=F"]
    for sym in context_display:
        p = prices.get(sym)
        if p:
            arrow = "\U0001f7e2" if p["chg"] >= 0 else "\U0001f534"
            if sym.startswith("^"):
                print(f"  {arrow} {sym:<10} {p['price']:>10.2f}  ({p['chg']:+.2f}%) "
                      f"[{p.get('basis', 'UNKNOWN basis')}; asof {p.get('asof_utc') or 'UNKNOWN'}]")
            else:
                print(f"  {arrow} {sym:<10} ${p['price']:>9.2f}  ({p['chg']:+.2f}%) "
                      f"[{p.get('basis', 'UNKNOWN basis')}; asof {p.get('asof_utc') or 'UNKNOWN'}]")

    print()
    return 1 if incomplete else 0


if __name__ == "__main__":
    sys.exit(main())
