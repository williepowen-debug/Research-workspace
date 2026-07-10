#!/usr/bin/env python3
"""
Market Data Fetch — Layer 1 (v2.1)
Pull live prices (yfinance) and economic data (FRED).

Changes from v2:
 - Tiered cache TTL (volatility-aware)
 - Delta threshold filtering (only emit on significant change)
 - Audit logging for debugging
 - Security fix: FRED_API_KEY required (no fallback)

Usage:
 python3 fetch.py price KRE APO WAL              # specific tickers
 python3 fetch.py price KRE APO --json           # JSON output for agents
 python3 fetch.py price KRE --history 30         # 30-day price history
 python3 fetch.py price KRE --delta 0.5          # only if change > 0.5%
 python3 fetch.py fred ICSA                      # single FRED series
 python3 fetch.py fred ICSA --periods 10         # with history
 python3 fetch.py all                            # everything Tier 1+2
 python3 fetch.py all --json                     # full snapshot as JSON
 python3 fetch.py prices                         # all tracked tickers
 python3 fetch.py econ                           # all tracked FRED series
 python3 fetch.py econ --json                    # econ data as JSON
 python3 fetch.py snapshot                       # compact one-liner per ticker
"""

import json
import os
import sys
import time
import urllib.request
import urllib.parse
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

def _load_dotenv():
    """Populate os.environ from a gitignored .env next to this file. Secrets
    (e.g. EIA_API_KEY) live there and are never committed. Existing env wins."""
    envp = Path(__file__).parent / ".env"
    if envp.exists():
        for line in envp.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


_load_dotenv()

FRED_API_KEY = os.environ.get("FRED_API_KEY", "")
if not FRED_API_KEY:
    print("WARN fetch.py: FRED_API_KEY not set (export it or add to FORGE/tools/market-data/.env) — FRED calls will fail",
          file=sys.stderr)

FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"

# EIA v2 API (weekly petroleum stocks, etc.). Key from gitignored .env / env var.
EIA_API_KEY = os.environ.get("EIA_API_KEY", "")
EIA_BASE = "https://api.eia.gov/v2"

CACHE_DIR = Path(__file__).parent / ".cache"
CACHE_TTL_VOLATILE = 30      # 30s for VIX, crypto
CACHE_TTL_STANDARD = 120     # 2min for oil, yields
CACHE_TTL_ECON = 300         # 5min for economic data
CACHE_TTL_HISTORICAL = 3600  # 1hr for historical

MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds, doubles each retry

AUDIT_LOG = Path(__file__).parent / "logs" / "market_data.log"

# --- Tier 1: Decision Drivers ---
TIER1_PRICES = {
    "BZ=F": "Brent Crude",
    "CL=F": "WTI Crude",
    "JPY=X": "USD/JPY",
}

TIER1_FRED = {
    "BAMLH0A0HYM2": "HY OAS",
    "BAMLC0A4CBBB": "BBB OAS",
    "ICSA": "Initial Claims",
    "CCSA": "Continuing Claims",
    "GASREGW": "Gas Price (wkly avg)",
    "DGS2": "2Y Treasury Yield",
    "DGS10": "10Y Treasury Yield",
    "T10Y2Y": "2s10s Spread",
    "T10YIE": "10Y Breakeven Inflation",
    "DCOILBRENTEU": "Brent (FRED, daily)",
}

# --- Tier 2: Position Monitoring ---
TIER2_PRICES = {
    "KRE": "Regional Banks ETF",
    "APO": "Apollo Global",
    "ARES": "Ares Management",
    "OZK": "Bank OZK",
    "WAL": "Western Alliance",
    "FXY": "Yen ETF",
    "TLT": "20Y+ Treasury ETF",
    "HYG": "HY Bond ETF",
    "IWM": "Russell 2000 ETF",
    "^VIX": "VIX",
    "^TNX": "10Y Treasury Yield",
    "SOFI": "SoFi Technologies",
}

ALL_PRICES = {**TIER1_PRICES, **TIER2_PRICES}
ALL_FRED = {**TIER1_FRED}

# Volatility tiers for cache TTL
VOLATILE_TICKERS = {"^VIX", "BTC-USD", "ETH-USD"}
STANDARD_TICKERS = {"BZ=F", "CL=F", "JPY=X", "^TNX"}


# ---------------------------------------------------------------------------
# Audit Logging
# ---------------------------------------------------------------------------

def _audit_log(action, details, latency_ms=None):
    """Append audit entry for debugging data freshness issues."""
    try:
        AUDIT_LOG.parent.mkdir(exist_ok=True)
        ts = datetime.now().isoformat()
        latency_str = f" latency={latency_ms:.0f}ms" if latency_ms else ""
        entry = f"{ts} {action}{latency_str} {json.dumps(details)}\n"
        with open(AUDIT_LOG, "a") as f:
            f.write(entry)
    except Exception:
        pass  # Audit logging is non-fatal


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _parse_flags(args):
    """Extract --json, --history N, --periods N, --delta PCT from args."""
    flags = {"json": False, "history": 0, "periods": 5, "delta": 0.0}
    clean = []
    skip_next = False
    for i, a in enumerate(args):
        if skip_next:
            skip_next = False
            continue
        if a == "--json":
            flags["json"] = True
        elif a == "--history" and i + 1 < len(args):
            flags["history"] = int(args[i + 1])
            skip_next = True
        elif a == "--periods" and i + 1 < len(args):
            flags["periods"] = int(args[i + 1])
            skip_next = True
        elif a == "--delta" and i + 1 < len(args):
            flags["delta"] = float(args[i + 1])
            skip_next = True
        else:
            clean.append(a)
    return clean, flags


def _retry_request(url, headers=None, timeout=15):
    """Make HTTP request with retry logic."""
    headers = headers or {"Accept": "application/json"}
    last_err = None
    for attempt in range(MAX_RETRIES):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read())
        except Exception as e:
            last_err = e
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_DELAY * (2 ** attempt))
    return {"error": str(last_err)}


# ---------------------------------------------------------------------------
# Cache (Tiered TTL)
# ---------------------------------------------------------------------------

def _cache_ttl(key):
    """Determine cache TTL based on data volatility."""
    # Check if it's a volatile ticker
    for ticker in VOLATILE_TICKERS:
        if ticker in key:
            return CACHE_TTL_VOLATILE
    # Check if it's a standard ticker
    for ticker in STANDARD_TICKERS:
        if ticker in key:
            return CACHE_TTL_STANDARD
    # Check if it's FRED / EIA economic data
    if "fred_" in key or "eia_" in key:
        return CACHE_TTL_ECON
    # Default for historical data
    if "history" in key:
        return CACHE_TTL_HISTORICAL
    return CACHE_TTL_STANDARD


def _cache_path(key):
    CACHE_DIR.mkdir(exist_ok=True)
    safe = key.replace("/", "_").replace("^", "_").replace("=", "_")
    return CACHE_DIR / f"{safe}.json"


def _cache_get(key):
    p = _cache_path(key)
    if not p.exists():
        return None
    try:
        data = json.loads(p.read_text())
    except (json.JSONDecodeError, OSError):
        return None
    ttl = _cache_ttl(key)
    if time.time() - data.get("ts", 0) > ttl:
        return None
    return data.get("val")


def _cache_set(key, val):
    p = _cache_path(key)
    try:
        p.write_text(json.dumps({"ts": time.time(), "val": val}))
    except OSError:
        pass  # non-fatal


# ---------------------------------------------------------------------------
# Delta Filtering
# ---------------------------------------------------------------------------

def _should_emit(ticker, new_data, delta_threshold):
    """Check if change exceeds delta threshold."""
    if delta_threshold <= 0:
        return True  # No filtering
    
    if "error" in new_data or "price" not in new_data:
        return True  # Always emit errors
    
    # Get previous value from cache
    cache_key = f"delta_check_{ticker}"
    prev_data = _cache_get(cache_key)
    
    if not prev_data or "price" not in prev_data:
        # First fetch or no previous data
        _cache_set(cache_key, new_data)
        return True
    
    prev_price = prev_data["price"]
    new_price = new_data["price"]
    
    if prev_price == 0:
        change_pct = 100 if new_price != 0 else 0
    else:
        change_pct = abs((new_price - prev_price) / prev_price * 100)
    
    if change_pct >= delta_threshold:
        _cache_set(cache_key, new_data)
        return True
    
    return False  # Change too small, skip


# ---------------------------------------------------------------------------
# FRED
# ---------------------------------------------------------------------------

def fred_fetch(series_id, limit=5):
    start_time = time.time()
    cached = _cache_get(f"fred_{series_id}_{limit}")
    if cached:
        _audit_log("FRED_CACHE_HIT", {"series": series_id, "limit": limit})
        return cached

    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "sort_order": "desc",
        "limit": limit,
    }
    url = f"{FRED_BASE}?{urllib.parse.urlencode(params)}"
    data = _retry_request(url)

    latency_ms = (time.time() - start_time) * 1000
    
    if "error" in data:
        _audit_log("FRED_ERROR", {"series": series_id, "error": data["error"]}, latency_ms)
        return [{"error": data["error"]}]

    obs = data.get("observations", [])
    result = [{"date": o["date"], "value": o["value"]} for o in obs if o["value"] != "."]
    _cache_set(f"fred_{series_id}_{limit}", result)
    _audit_log("FRED_FETCH", {"series": series_id, "observations": len(result)}, latency_ms)
    return result


# ---------------------------------------------------------------------------
# EIA (v2 API — weekly petroleum stocks etc.)
# ---------------------------------------------------------------------------

def eia_fetch(series_id, route="petroleum/stoc/wstk", limit=2):
    """Pull a weekly EIA v2 series (newest-first). Returns [{date, value}, ...]
    mirroring fred_fetch's shape so dashboard handling is identical.
    `route` is the EIA v2 dataset path; `series_id` is its `series` facet value."""
    start_time = time.time()
    cache_key = f"eia_{series_id}_{limit}"
    cached = _cache_get(cache_key)
    if cached:
        _audit_log("EIA_CACHE_HIT", {"series": series_id, "limit": limit})
        return cached

    if not EIA_API_KEY:
        return [{"error": "EIA_API_KEY not set (add to FORGE/tools/market-data/.env)"}]

    params = {
        "api_key": EIA_API_KEY,
        "frequency": "weekly",
        "data[0]": "value",
        "facets[series][]": series_id,
        "sort[0][column]": "period",
        "sort[0][direction]": "desc",
        "length": limit,
    }
    url = f"{EIA_BASE}/{route}/data/?{urllib.parse.urlencode(params)}"
    data = _retry_request(url)

    latency_ms = (time.time() - start_time) * 1000

    if "error" in data:
        _audit_log("EIA_ERROR", {"series": series_id, "error": data["error"]}, latency_ms)
        return [{"error": data["error"]}]

    rows = data.get("response", {}).get("data", [])
    result = [{"date": r["period"], "value": r["value"]} for r in rows if r.get("value") is not None]
    _cache_set(cache_key, result)
    _audit_log("EIA_FETCH", {"series": series_id, "observations": len(result)}, latency_ms)
    return result


# ---------------------------------------------------------------------------
# EIA electricity (v2 API — EIA-930 hourly demand + monthly retail prices)
# Added 2026-07-10 (DAEDALUS Step-1 power instrument layer — power-agent staged
# path; consumer: power_watch.py, HENRY-provisional). Non-breaking: petroleum
# callers use eia_fetch() above, which is untouched.
# ---------------------------------------------------------------------------

def eia_fetch_facets(route, facets, frequency="hourly", data_col="value",
                     limit=24, keep_fields=()):
    """Generic EIA v2 pull with arbitrary facets. eia_fetch() above is
    petroleum-shaped (weekly frequency + a `series` facet); this serves routes
    keyed on other facets — e.g. EIA-930 respondent/type, retail-sales
    stateid/sectorid. Verified live 2026-07-10 against both routes.

    facets: dict facet_id -> value or list of values.
    keep_fields: extra row fields to carry through (e.g. "sectorid").
    Returns newest-first [{date, value, <keep_fields...>}, ...] mirroring
    fred_fetch/eia_fetch shape, or [{"error": ...}] on failure."""
    start_time = time.time()
    facet_sig = "_".join(f"{k}-{'-'.join(map(str, v if isinstance(v, (list, tuple)) else [v]))}"
                         for k, v in sorted(facets.items()))
    cache_key = f"eia_{route}_{facet_sig}_{data_col}_{frequency}_{limit}"
    cached = _cache_get(cache_key)
    if cached:
        _audit_log("EIA_CACHE_HIT", {"route": route, "facets": facet_sig, "limit": limit})
        return cached

    if not EIA_API_KEY:
        return [{"error": "EIA_API_KEY not set (add to FORGE/tools/market-data/.env)"}]

    params = [
        ("api_key", EIA_API_KEY),
        ("frequency", frequency),
        ("data[0]", data_col),
        ("sort[0][column]", "period"),
        ("sort[0][direction]", "desc"),
        ("length", limit),
    ]
    for k, v in facets.items():
        for vv in (v if isinstance(v, (list, tuple)) else [v]):
            params.append((f"facets[{k}][]", vv))
    url = f"{EIA_BASE}/{route}/data/?{urllib.parse.urlencode(params)}"
    data = _retry_request(url)

    latency_ms = (time.time() - start_time) * 1000

    if "error" in data:
        _audit_log("EIA_ERROR", {"route": route, "facets": facet_sig, "error": data["error"]}, latency_ms)
        return [{"error": data["error"]}]

    rows = data.get("response", {}).get("data", [])
    result = []
    for r in rows:
        if r.get(data_col) is None:
            continue
        row = {"date": r["period"], "value": r[data_col]}
        for f in keep_fields:
            row[f] = r.get(f)
        result.append(row)
    _cache_set(cache_key, result)
    _audit_log("EIA_FETCH", {"route": route, "facets": facet_sig, "observations": len(result)}, latency_ms)
    return result


def eia_pjm_demand(hours=26):
    """EIA-930 hourly demand for the PJM balancing authority (route
    electricity/rto/region-data, respondent=PJM, type=D). Newest-first;
    period stamps are UTC hours ("YYYY-MM-DDTHH"); values are MWh for the
    hour (≈ average MW). Publication lags real time ~2-6 hours — stamp
    reads with the period hour, not "now". Default 26 rows = latest read
    + a full prior-24h peak window + slack."""
    return eia_fetch_facets("electricity/rto/region-data",
                            {"respondent": "PJM", "type": "D"},
                            frequency="hourly", data_col="value", limit=hours)


def eia_retail_power_price(sectors=("IND", "RES"), state="US", months=3):
    """Monthly average retail electricity price, cents/kWh (route
    electricity/retail-sales, forms EIA-826/861M). state="US" = U.S. total,
    served cleanly (verified live 2026-07-10; state codes e.g. "PA" also
    work). ~2-MONTH PUBLICATION LAG — the latest print is a backdrop, not a
    live price; always cite its month label. Rows carry `sectorid`
    ("IND"/"RES") so callers can split sectors."""
    return eia_fetch_facets("electricity/retail-sales",
                            {"stateid": state, "sectorid": list(sectors)},
                            frequency="monthly", data_col="price",
                            limit=months * max(len(sectors), 1),
                            keep_fields=("sectorid",))


# ---------------------------------------------------------------------------
# Prices (yfinance)
# ---------------------------------------------------------------------------

def price_fetch(tickers, delta_threshold=0.0):
    """Fetch current prices for a list of tickers with optional delta filtering."""
    import yfinance as yf
    
    cache_key = f"prices_{'_'.join(sorted(tickers))}"
    cached = _cache_get(cache_key)
    if cached:
        _audit_log("PRICE_CACHE_HIT", {"tickers": len(tickers)})
        # Still apply delta filtering even on cache hit
        if delta_threshold > 0:
            filtered = {}
            for t, d in cached.items():
                if _should_emit(t, d, delta_threshold):
                    filtered[t] = d
            return filtered
        return cached

    start_time = time.time()
    results = {}
    for t in tickers:
        try:
            tk = yf.Ticker(t)
            info = tk.fast_info
            curr = float(info["lastPrice"])
            prev = float(info.get("regularMarketPreviousClose") or info.get("previousClose") or 0)
            chg = ((curr - prev) / prev * 100) if prev else None
            results[t] = {
                "price": round(curr, 2),
                "prev": round(prev, 2) if prev else None,
                "change_pct": round(float(chg), 2) if chg is not None else None,
                "name": ALL_PRICES.get(t, t),
            }
        except Exception as e:
            results[t] = {"error": str(e), "name": ALL_PRICES.get(t, t)}

    latency_ms = (time.time() - start_time) * 1000
    _cache_set(cache_key, results)
    _audit_log("PRICE_FETCH", {"tickers": len(tickers), "errors": sum(1 for d in results.values() if "error" in d)}, latency_ms)
    
    # Apply delta filtering
    if delta_threshold > 0:
        filtered = {}
        for t, d in results.items():
            if _should_emit(t, d, delta_threshold):
                filtered[t] = d
        return filtered
    
    return results


def price_history(tickers, days=30):
    """Fetch daily close history for tickers. Returns dict of ticker -> [{date, close}]."""
    import yfinance as yf
    results = {}
    period = f"{days}d"
    for t in tickers:
        try:
            tk = yf.Ticker(t)
            hist = tk.history(period=period)
            if hist.empty:
                results[t] = {"error": "no data", "name": ALL_PRICES.get(t, t)}
                continue
            rows = []
            for date, row in hist.iterrows():
                rows.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "close": round(float(row["Close"]), 2),
                    "volume": int(row.get("Volume", 0)),
                })
            results[t] = {
                "name": ALL_PRICES.get(t, t),
                "days": len(rows),
                "history": rows,
                "high": round(float(hist["Close"].max()), 2),
                "low": round(float(hist["Close"].min()), 2),
                "start": rows[-1]["close"] if rows else None,
                "end": rows[0]["close"] if rows else None,
            }
            if results[t]["start"] and results[t]["end"]:
                pct = (results[t]["end"] - results[t]["start"]) / results[t]["start"] * 100
                results[t]["period_change_pct"] = round(pct, 2)
        except Exception as e:
            results[t] = {"error": str(e), "name": ALL_PRICES.get(t, t)}
    return results


# ---------------------------------------------------------------------------
# Display — Text
# ---------------------------------------------------------------------------

def display_prices(results, labels=None):
    print(f"\n {'Ticker':<10} {'Name':<22} {'Price':>10} {'Change':>10}")
    print(f" {'-'*54}")

    for t, d in results.items():
        if "error" in d:
            print(f" {t:<10} {d.get('name','')[:21]:<22} {'ERROR':>10} {str(d['error'])[:30]}")
            continue
        name = d.get("name", (labels or {}).get(t, ""))[:21]
        p = f"${d['price']:,.2f}" if d["price"] < 1000 else f"{d['price']:,.2f}"
        chg = f"{d['change_pct']:+.2f}%" if d.get("change_pct") is not None else "N/A"
        print(f" {t:<10} {name:<22} {p:>10} {chg:>10}")


def display_fred(series_id, label, obs):
    if obs and "error" in obs[0]:
        print(f" {label}: ERROR — {obs[0]['error']}")
        return

    latest = obs[0] if obs else None
    if not latest:
        print(f" {label}: NO DATA")
        return

    val = latest["value"]
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

    print(f" {label:<25} {formatted:>12} ({latest['date']})")

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
            print(f" {'':25} {v:>12} ({o['date']})")


def display_history(results):
    for t, d in results.items():
        if "error" in d:
            print(f"\n {t} ({d.get('name', '')}): ERROR — {d['error']}")
            continue
        chg = f"{d.get('period_change_pct', 0):+.2f}%" if d.get("period_change_pct") is not None else "N/A"
        print(f"\n {t} ({d['name']}) — {d['days']}d range: ${d['low']} – ${d['high']} Period: {chg}")
        print(f" {'Date':<14} {'Close':>10} {'Volume':>14}")
        print(f" {'-'*40}")
        # Show most recent 10 rows to keep output manageable
        for row in d["history"][:10]:
            vol = f"{row['volume']:,}" if row["volume"] else "—"
            print(f" {row['date']:<14} ${row['close']:>9,.2f} {vol:>14}")
        if d["days"] > 10:
            print(f" ... ({d['days'] - 10} more rows)")


def display_snapshot(price_results, fred_data):
    """One compact line per item — designed for quick agent consumption."""
    print(f"\n === MARKET SNAPSHOT ({time.strftime('%Y-%m-%d %H:%M ET')}) ===\n")
    for t, d in price_results.items():
        if "error" in d:
            print(f" {t:<10} {d.get('name',''):<20} ERROR")
            continue
        chg = f"{d['change_pct']:+.2f}%" if d.get("change_pct") is not None else ""
        print(f" {t:<10} {d.get('name',''):<20} ${d['price']:<10,.2f} {chg}")

    print()
    for sid, label in ALL_FRED.items():
        obs = fred_data.get(sid, [])
        if not obs or "error" in obs[0]:
            print(f" {label:<25} ERROR")
            continue
        val = obs[0]["value"]
        try:
            num = float(val)
            if num > 10000:
                val = f"{num:,.0f}"
            elif num > 100:
                val = f"{num:,.1f}"
        except ValueError:
            pass
        print(f" {label:<25} {val:>12} ({obs[0]['date']})")


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_price(tickers, flags):
    results = price_fetch(tickers, delta_threshold=flags["delta"])

    if flags["history"]:
        hist = price_history(tickers, flags["history"])
        if flags["json"]:
            print(json.dumps(hist, indent=2))
        else:
            display_history(hist)
        return

    if flags["json"]:
        print(json.dumps(results, indent=2))
    else:
        display_prices(results)


def cmd_fred(series_id, flags):
    label = ALL_FRED.get(series_id, series_id)
    obs = fred_fetch(series_id, limit=flags["periods"])

    if flags["json"]:
        print(json.dumps({"series": series_id, "label": label, "observations": obs}, indent=2))
    else:
        print()
        display_fred(series_id, label, obs)


def cmd_prices(flags):
    results = price_fetch(list(ALL_PRICES.keys()), delta_threshold=flags["delta"])
    if flags["json"]:
        print(json.dumps(results, indent=2))
    else:
        print("\n=== TRACKED PRICES ===")
        display_prices(results)


def cmd_econ(flags):
    all_data = {}
    for sid, label in ALL_FRED.items():
        obs = fred_fetch(sid, limit=flags["periods"])
        all_data[sid] = {"label": label, "observations": obs}

    if flags["json"]:
        print(json.dumps(all_data, indent=2))
    else:
        print("\n=== ECONOMIC DATA (FRED) ===\n")
        for sid, d in all_data.items():
            display_fred(sid, d["label"], d["observations"])


def cmd_all(flags):
    price_results = price_fetch(list(ALL_PRICES.keys()), delta_threshold=flags["delta"])
    fred_data = {}
    for sid in ALL_FRED:
        fred_data[sid] = fred_fetch(sid, limit=1)

    if flags["json"]:
        print(json.dumps({
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "prices": price_results,
            "fred": {sid: {"label": ALL_FRED[sid], "observations": obs} for sid, obs in fred_data.items()},
        }, indent=2))
    else:
        print("\n=== TRACKED PRICES ===")
        display_prices(price_results)
        print("\n=== ECONOMIC DATA (FRED) ===\n")
        for sid, obs in fred_data.items():
            display_fred(sid, ALL_FRED[sid], obs)
        print()


def cmd_snapshot(flags):
    price_results = price_fetch(list(ALL_PRICES.keys()), delta_threshold=flags["delta"])
    fred_data = {}
    for sid in ALL_FRED:
        fred_data[sid] = fred_fetch(sid, limit=1)

    if flags["json"]:
        # Flatten everything into a compact structure
        compact = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "prices": {}, "econ": {}}
        for t, d in price_results.items():
            if "error" not in d:
                compact["prices"][t] = {"p": d["price"], "chg": d.get("change_pct")}
            else:
                compact["prices"][t] = {"error": d["error"]}
        for sid, obs in fred_data.items():
            if obs and "error" not in obs[0]:
                compact["econ"][sid] = {"val": obs[0]["value"], "date": obs[0]["date"], "label": ALL_FRED[sid]}
            else:
                compact["econ"][sid] = {"error": "no data"}
        print(json.dumps(compact, indent=2))
    else:
        display_snapshot(price_results, fred_data)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args, flags = _parse_flags(sys.argv[1:])

    if not args or args[0] == "all":
        cmd_all(flags)
        return

    if args[0] == "prices":
        cmd_prices(flags)
        return

    if args[0] == "econ":
        cmd_econ(flags)
        return

    if args[0] == "snapshot":
        cmd_snapshot(flags)
        return

    if args[0] == "price":
        if len(args) < 2:
            print("Usage: fetch.py price TICKER [TICKER ...] [--json] [--history N] [--delta PCT]")
            return
        cmd_price(args[1:], flags)
        return

    if args[0] == "fred":
        if len(args) < 2:
            print("Usage: fetch.py fred SERIES_ID [--periods N] [--json]")
            return
        cmd_fred(args[1], flags)
        return

    # Fallback — treat args as tickers
    cmd_price(args, flags)


if __name__ == "__main__":
    main()
