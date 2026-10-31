#!/usr/bin/env python3
"""L616 breadth — retry tickers that failed in pull_prices.py, merge into px_const.pkl.
Run: .venv/bin/python3 -I <this> <research_dir> <cache_dir>
"""
import sys, os, csv, time, pickle
import pandas as pd
import yfinance as yf

R, C = sys.argv[1], sys.argv[2]
uni = list(csv.DictReader(open(os.path.join(R, "universe.csv"))))
tick = [u["yf_ticker"] for u in uni]
px = pickle.load(open(os.path.join(C, "px_const.pkl"), "rb"))
close = px["Close"]
bad = [t for t in tick if t not in close.columns or close[t].dropna().empty]
print("retrying", len(bad), bad)
got = {}
for t in bad:
    for attempt in range(3):
        try:
            df = yf.download(t, start="2024-01-01", end="2026-10-31", auto_adjust=False,
                             progress=False, threads=False)
            if df is not None and not df.empty:
                if isinstance(df.columns, pd.MultiIndex):
                    df.columns = df.columns.get_level_values(0)
                got[t] = df
                break
        except Exception as e:  # noqa: BLE001
            print("  err", t, type(e).__name__)
        time.sleep(2)
    time.sleep(0.5)
print("recovered", len(got), "still failed", [t for t in bad if t not in got])
for field in ["Open", "High", "Low", "Close", "Adj Close", "Volume"]:
    for t, df in got.items():
        px[(field, t)] = df[field].reindex(px.index)
px = px.sort_index(axis=1)
pickle.dump(px, open(os.path.join(C, "px_const.pkl"), "wb"))
close = px["Close"]
bad2 = [t for t in tick if t not in close.columns or close[t].dropna().empty]
print("after merge failed:", len(bad2), bad2)
