#!/usr/bin/env python3
"""Market watchlist — quick quote + change for all positions."""

import os
import sys

try:
    import yfinance as yf
except ModuleNotFoundError:
    # yfinance lives only in the repo .venv — re-exec under it rather than
    # failing on the bare-python3 recipe (PAT-103; env guard prevents loops).
    if os.environ.get("_MARKET_VENV_REEXEC") != "1":
        _venv_py = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".venv", "bin", "python3")
        if os.path.exists(_venv_py):
            os.environ["_MARKET_VENV_REEXEC"] = "1"
            os.execv(_venv_py, [_venv_py] + sys.argv)
    if "--selftest" in sys.argv:
        yf = None  # --selftest drives fmt() over fixtures only; no yfinance, no network
    else:
        sys.stderr.write("ERROR: yfinance not importable and no repo .venv found — run under .venv/bin/python3\n")
        sys.exit(2)

import math
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

_NY = ZoneInfo("America/New_York")

WATCHLIST = {
    "Positions": ["WAL", "OZK", "KRE", "ZION", "EGBN", "SSB", "IWM", "HYG", "TLT", "CF", "STNG", "AAL"],
    "Watchlist": ["LNG", "APO", "FLG", "CFG", "VLY", "USO"],
    "Benchmarks": ["SPY", "QQQ", "DX-Y.NYB", "CL=F", "BZ=F", "GC=F", "^TNX", "^VIX"],
}

def _num(v):
    """A usable price: a finite, non-zero number. None / 0 / NaN / non-numeric -> None.
    (0 is treated as ABSENT: yfinance emits 0 for a missing live field; no watchlist
    instrument genuinely prints at 0.00. Negative prices are kept — CL=F printed -37.63 in 2020.)"""
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    if f == 0 or math.isnan(f) or math.isinf(f):
        return None
    return f


def _asof_tag(info, today=None):
    """As-of check on a LIVE row, keyed to regularMarketTime (epoch seconds) in America/New_York.
      same NY date as today -> ""                      (row format unchanged)
      earlier / other date  -> "  ⚠stale YYYY-MM-DD"
      field missing         -> "  ⚠no-asof"            (fail closed: yfinance supplies it on every
                                                         normal row, so absence is unverified, not fresh)
      unparseable           -> "  ⚠asof-unreadable"
    """
    t = info.get("regularMarketTime")
    if t is None:
        return "  ⚠no-asof"
    try:
        d = datetime.fromtimestamp(float(t), _NY).date()
    except (TypeError, ValueError, OverflowError, OSError):
        return "  ⚠asof-unreadable"
    if today is None:
        today = datetime.now(_NY).date()
    return "" if d == today else f"  ⚠stale {d.isoformat()}"


def fmt(ticker, info, today=None):
    """One watchlist row. Live rows keep the original format (+ an as-of tag only when the
    quote is not today's). When regularMarketPrice is absent/0/NaN, the previous close is
    printed LABELLED as such, with no change % and no colour arrow — a change computed from
    prev-close against itself is always +0.00% and would print a false 🟢 (DOCKET L409 D5)."""
    try:
        live = _num(info.get("regularMarketPrice"))
        prev = _num(info.get("previousClose")) or _num(info.get("regularMarketPreviousClose"))
        if live is None:
            if prev is None:
                return f"  ⚪ {ticker:<8} (no data)"
            return f"  ⚪ {ticker:<8} ${prev:>10.2f}  ⚠prev-close"
        tag = _asof_tag(info, today)
        if prev is not None:
            chg = ((live - prev) / prev) * 100
            arrow = "🟢" if chg >= 0 else "🔴"
            return f"  {arrow} {ticker:<8} ${live:>10.2f}  ({chg:+.2f}%){tag}"
        return f"  ⚪ {ticker:<8} ${live:>10.2f}{tag}"
    except Exception:
        return f"  ⚪ {ticker:<8} (no data)"


def _ny_epoch(y, m, d, hh=16, mm=0):
    return int(datetime(y, m, d, hh, mm, tzinfo=_NY).timestamp())


def selftest():
    """Drive fmt() over fixture dicts — no network. rc 0 all PASS, 1 any FAIL."""
    today = date(2026, 9, 24)
    now_t = _ny_epoch(2026, 9, 24, 16, 0)
    cases = [
        # (name, info, exact expected row)
        ("C3 live up, today (format unchanged)",
         {"regularMarketPrice": 76.26, "previousClose": 75.6, "regularMarketTime": now_t},
         "  🟢 WAL      $     76.26  (+0.87%)"),
        ("C3 live down, today (format unchanged)",
         {"regularMarketPrice": 45.0, "previousClose": 46.09, "regularMarketTime": now_t},
         "  🔴 WAL      $     45.00  (-2.36%)"),
        ("C1 regularMarketPrice absent -> prev-close, no %/arrow",
         {"previousClose": 75.6, "regularMarketTime": now_t},
         "  ⚪ WAL      $     75.60  ⚠prev-close"),
        ("C1 via regularMarketPreviousClose only",
         {"regularMarketPreviousClose": 75.6},
         "  ⚪ WAL      $     75.60  ⚠prev-close"),
        ("C2 stale: quote dated 2026-09-22",
         {"regularMarketPrice": 76.26, "previousClose": 75.6, "regularMarketTime": _ny_epoch(2026, 9, 22)},
         "  🟢 WAL      $     76.26  (+0.87%)  ⚠stale 2026-09-22"),
        ("C2 NY-tz boundary: 23:30 NY 9/23 (= 03:30 UTC 9/24) is stale",
         {"regularMarketPrice": 76.26, "previousClose": 75.6, "regularMarketTime": _ny_epoch(2026, 9, 23, 23, 30)},
         "  🟢 WAL      $     76.26  (+0.87%)  ⚠stale 2026-09-23"),
        ("C4 regularMarketPrice == 0 -> prev-close",
         {"regularMarketPrice": 0, "previousClose": 75.6, "regularMarketTime": now_t},
         "  ⚪ WAL      $     75.60  ⚠prev-close"),
        ("C4 regularMarketPrice NaN -> prev-close",
         {"regularMarketPrice": float("nan"), "previousClose": 75.6},
         "  ⚪ WAL      $     75.60  ⚠prev-close"),
        ("C4 regularMarketTime missing on live row -> no-asof",
         {"regularMarketPrice": 76.26, "previousClose": 75.6},
         "  🟢 WAL      $     76.26  (+0.87%)  ⚠no-asof"),
        ("C4 previousClose missing too -> (no data)",
         {"regularMarketTime": now_t},
         "  ⚪ WAL      (no data)"),
        ("C4 empty info -> (no data)",
         {},
         "  ⚪ WAL      (no data)"),
        ("C4 regularMarketTime unparseable",
         {"regularMarketPrice": 76.26, "previousClose": 75.6, "regularMarketTime": "garbage"},
         "  🟢 WAL      $     76.26  (+0.87%)  ⚠asof-unreadable"),
        ("C4 live price, previousClose missing (no %, as before)",
         {"regularMarketPrice": 76.26, "regularMarketTime": now_t},
         "  ⚪ WAL      $     76.26"),
        ("C4 negative live price kept (CL=F 2020)",
         {"regularMarketPrice": -37.63, "previousClose": 18.27, "regularMarketTime": now_t},
         "  🔴 WAL      $    -37.63  (-305.97%)"),
    ]
    fails = 0
    for name, info, want in cases:
        got = fmt("WAL", info, today=today)
        ok = got == want
        fails += not ok
        print(f"{'PASS' if ok else 'FAIL'}  {name}\n      {got}")
        if not ok:
            print(f"      want: {want}")
    print(f"\n{len(cases) - fails}/{len(cases)} PASS")
    return 0 if fails == 0 else 1

def options_chain(symbol, expiry=None):
    """Pull options chain for a symbol. If expiry is None, show available dates."""
    t = yf.Ticker(symbol)
    dates = t.options
    if not dates:
        print(f"No options data for {symbol}")
        return
    if expiry is None:
        more = f" (+{len(dates) - 10} more)" if len(dates) > 10 else ""
        print(f"\n{symbol} option expiries: {', '.join(dates[:10])}{more}")
        return
    chain = t.option_chain(expiry)
    print(f"\n=== {symbol} {expiry} CALLS (near ATM) ===")
    calls = chain.calls
    if len(calls) > 0:
        mid = len(calls) // 2
        start = max(0, mid - 5)
        end = min(len(calls), mid + 5)
        cols = ["strike", "lastPrice", "bid", "ask", "volume", "openInterest", "impliedVolatility"]
        avail = [c for c in cols if c in calls.columns]
        print(calls[avail].iloc[start:end].to_string(index=False))
    
    print(f"\n=== {symbol} {expiry} PUTS (near ATM) ===")
    puts = chain.puts
    if len(puts) > 0:
        mid = len(puts) // 2
        start = max(0, mid - 5)
        end = min(len(puts), mid + 5)
        avail = [c for c in cols if c in puts.columns]
        print(puts[avail].iloc[start:end].to_string(index=False))

def main():
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "--selftest":
            sys.exit(selftest())
        if cmd == "options" and len(sys.argv) >= 3:
            symbol = sys.argv[2].upper()
            expiry = sys.argv[3] if len(sys.argv) > 3 else None
            options_chain(symbol, expiry)
            return
        elif cmd == "quote":
            symbols = [s.upper() for s in sys.argv[2:]]
            tickers = yf.Tickers(" ".join(symbols))
            for sym in symbols:
                try:
                    info = tickers.tickers[sym].info
                    print(fmt(sym, info))
                except Exception as e:
                    print(f"  ⚪ {sym:<8} (error: {e})")
            return

    # Default: full watchlist
    all_symbols = []
    for group in WATCHLIST.values():
        all_symbols.extend(group)
    
    tickers = yf.Tickers(" ".join(all_symbols))
    
    for group_name, symbols in WATCHLIST.items():
        print(f"\n{'='*45}")
        print(f"  {group_name}")
        print(f"{'='*45}")
        for sym in symbols:
            try:
                info = tickers.tickers[sym].info
                print(fmt(sym, info))
            except Exception as e:
                print(f"  ⚪ {sym:<8} (error: {e})")

    # Crude oil label fix
    print(f"\n  Note: CL=F = WTI Crude, ^TNX = 10Y Yield, DXY=F = Dollar Index")

if __name__ == "__main__":
    main()
