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
    sys.stderr.write("ERROR: yfinance not importable and no repo .venv found — run under .venv/bin/python3\n")
    sys.exit(2)

WATCHLIST = {
    "Positions": ["WAL", "OZK", "KRE", "ZION", "EGBN", "SSB", "IWM", "HYG", "TLT", "CF", "STNG", "AAL"],
    "Watchlist": ["LNG", "APO", "FLG", "CFG", "VLY", "USO"],
    "Benchmarks": ["SPY", "QQQ", "DX-Y.NYB", "CL=F", "BZ=F", "GC=F", "^TNX", "^VIX"],
}

def fmt(ticker, info):
    try:
        price = info.get("regularMarketPrice") or info.get("previousClose", 0)
        prev = info.get("previousClose") or info.get("regularMarketPreviousClose", 0)
        if price and prev:
            chg = ((price - prev) / prev) * 100
            arrow = "🟢" if chg >= 0 else "🔴"
            return f"  {arrow} {ticker:<8} ${price:>10.2f}  ({chg:+.2f}%)"
        return f"  ⚪ {ticker:<8} ${price:>10.2f}"
    except:
        return f"  ⚪ {ticker:<8} (no data)"

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
