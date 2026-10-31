#!/usr/bin/env python3
"""L616 breadth — pull daily OHLC for the universe + ETF set (yfinance, free).
Run: .venv/bin/python3 -I <this> <research_dir> <cache_dir>
Writes <cache_dir>/px_const.pkl (constituents, 2024-01-02..2026-10-30, auto_adjust=False:
Close is split-adjusted only; Adj Close is split+dividend adjusted) and
<cache_dir>/px_etf.pkl (ETFs/indexes, long history for base rates).
Prints the failure list — a failed ticker is reported, never silently dropped.
"""
import sys, os, csv, time, pickle
import pandas as pd
import yfinance as yf

R, C = sys.argv[1], sys.argv[2]
uni = list(csv.DictReader(open(os.path.join(R, "universe.csv"))))
tick = [u["yf_ticker"] for u in uni]

def pull(tickers, start, end, chunk=150):
    frames = []
    for i in range(0, len(tickers), chunk):
        part = tickers[i:i + chunk]
        for attempt in range(3):
            try:
                df = yf.download(part, start=start, end=end, auto_adjust=False,
                                 progress=False, threads=True, group_by="column")
                frames.append(df)
                break
            except Exception as e:  # noqa: BLE001
                print("retry", i, type(e).__name__, e)
                time.sleep(5)
        print(f"  chunk {i}-{i+len(part)} done", flush=True)
    return pd.concat(frames, axis=1)

t0 = time.time()
px = pull(tick, "2024-01-01", "2026-10-31")
close = px["Close"]
bad = [t for t in tick if t not in close.columns or close[t].dropna().empty]
last = close.index.max()
stale = [t for t in tick if t in close.columns and not close[t].dropna().empty and close[t].dropna().index.max() < last]
print("constituents:", len(tick), "failed:", len(bad), bad)
print("last bar:", last, "| names whose last bar < last:", len(stale), stale[:30])
pickle.dump(px, open(os.path.join(C, "px_const.pkl"), "wb"))

ETF = ["SPY", "RSP", "QQQ", "QQEW", "IWM", "IJH", "MDY", "IJR", "OEF", "SOXX", "SMH",
       "XLK", "XLC", "XLY", "XLF", "XLV", "XLI", "XLE", "XLP", "XLU", "XLB", "XLRE",
       "^GSPC", "^NDX", "^RUT", "^SP400", "^SP600", "^VIX"]
pe = yf.download(ETF, start="2003-01-01", end="2026-10-31", auto_adjust=False,
                 progress=False, threads=True, group_by="column")
badE = [t for t in ETF if t not in pe["Close"].columns or pe["Close"][t].dropna().empty]
print("etf failed:", badE, "| etf last bar:", pe.index.max())
pickle.dump(pe, open(os.path.join(C, "px_etf.pkl"), "wb"))
print(f"done in {time.time()-t0:.0f}s")
