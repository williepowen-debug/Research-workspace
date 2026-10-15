import sys, datetime as dt
import yfinance as yf
import numpy as np
from math import log, sqrt, erf
def N(x): return 0.5*(1+erf(x/sqrt(2)))
out = {}
for tk, spot, K, be, n in [("OZK",44.93,40.0,39.19,27),("WAL",72.22,65.0,63.29,46),("KRE",68.54,67.0,65.72,30)]:
    h = yf.Ticker(tk).history(start="2016-01-01", end="2026-10-15", auto_adjust=True)
    c = h["Close"].dropna()
    print(tk, "bars", len(c), "first", c.index[0].date(), "last", c.index[-1].date(), "last close", round(float(c.iloc[-1]),2))
    for label, start in [("5y", "2021-10-14"), ("10y", "2016-01-01")]:
        cc = c[c.index >= start].values
        r = cc[n:]/cc[:-n]-1
        strike_mv = K/spot-1; be_mv = be/spot-1
        p_strike = float(np.mean(r <= strike_mv)); p_be = float(np.mean(r <= be_mv))
        # ex-2023: drop windows whose start is in 2023
        idx = c[c.index >= start].index
        starts = idx[:-n]
        mask = np.array([d.year != 2023 for d in starts])
        p_strike_x = float(np.mean(r[mask] <= strike_mv)); p_be_x = float(np.mean(r[mask] <= be_mv))
        print(f"  {label}: windows={len(r)} n={n} | P(ret<= {strike_mv*100:.1f}% to strike)={p_strike*100:.1f}% (ex-2023 {p_strike_x*100:.1f}%) | P(ret<= {be_mv*100:.1f}% to breakeven)={p_be*100:.1f}% (ex-2023 {p_be_x*100:.1f}%)")
    # realized vol
    lr = np.diff(np.log(c.values))
    for w in (21, 63):
        print(f"  realized vol {w}d = {np.std(lr[-w:], ddof=1)*sqrt(252)*100:.1f}%")
