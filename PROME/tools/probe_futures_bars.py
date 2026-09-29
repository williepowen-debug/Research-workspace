#!/usr/bin/env python3
"""probe_futures_bars.py — DOCKET L462 live probe of the vendor's futures bar labelling.

Run with the venv (yfinance): `.venv/bin/python3 PROME/tools/probe_futures_bars.py`.
Prints, per symbol: fast_info quote fields, the last daily bars, history_metadata
(regularMarketTime, timezone, currentTradingPeriod) and, for Brent, two days of hourly bars.
READ-ONLY at the vendor; writes nothing.

The owed check (ACCEPTANCE_fetch_evening_bar_L462_2026-09-29.md): re-run AFTER ~18:00 ET.
Expected if the detector's key holds: BZX26.NYM/BZZ26.NYM regularMarketTime >= 18:00 ET on
today's date, the last daily bar dated today (or already re-labelled tomorrow), and
`fetch.py price BZX26.NYM --json` reporting session = evening-next-session with change_pct
null. Paste the output into the acceptance file's live-leg section with the clock.
"""
import json, time, datetime, sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2] / "FORGE" / "tools" / "market-data"))
import yfinance as yf
now = time.time()
print("NOW", datetime.datetime.now(datetime.timezone.utc).isoformat(), "epoch", int(now))
for sym in ["BZX26.NYM", "BZZ26.NYM", "CLX26.NYM", "TLT", "^MOVE"]:
    tk = yf.Ticker(sym)
    fi = tk.fast_info
    print("=====", sym)
    for k in ["lastPrice","previousClose","regularMarketPreviousClose","open","dayHigh","dayLow","lastVolume","timezone","exchange"]:
        try: print("  fast_info", k, fi[k])
        except Exception as e: print("  fast_info", k, "ERR", type(e).__name__)
    h = tk.history(period="5d")
    print("  daily bars:")
    for ts, row in h.iterrows():
        print("   ", ts.isoformat(), "O", round(row["Open"],3), "C", round(row["Close"],3), "V", int(row["Volume"]))
    md = tk.history_metadata or {}
    keep = {k: md.get(k) for k in ["currency","symbol","exchangeName","fullExchangeName","exchangeTimezoneName","regularMarketTime","hasPrePostMarketData","gmtoffset","timezone","regularMarketPrice","previousClose","chartPreviousClose","priceHint","dataGranularity","range"]}
    print("  metadata:", json.dumps(keep, default=str))
    ctp = md.get("currentTradingPeriod")
    if ctp:
        for k, v in ctp.items():
            print("   ctp", k, {kk: (datetime.datetime.fromtimestamp(vv, datetime.timezone.utc).isoformat() if kk in ("start","end") else vv) for kk, vv in v.items()})
    tp = md.get("tradingPeriods")
    if tp is not None:
        print("   tradingPeriods type", type(tp).__name__, str(tp)[:300])
    if sym.startswith("BZX"):
        hh = tk.history(period="2d", interval="1h")
        print("  hourly bars (2d):")
        for ts, row in hh.iterrows():
            print("   ", ts.isoformat(), "C", round(row["Close"],3), "V", int(row["Volume"]))
