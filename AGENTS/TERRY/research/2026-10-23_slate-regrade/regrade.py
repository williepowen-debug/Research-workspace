"""Re-grade the 10/20 slate (RSP / IEF / FXY) on completed closes through 10/23, on each card's own resolver.
RSP: close > 215.00 AND same-date RSP/SPY close ratio > max of the prior 20 aligned closes' ratio.
IEF: official Treasury 10Y (FRED DGS10) <= 5.00% on a completed date, then a LATER red IEF session with IEF >= 90.00.
FXY: close > max of the prior 20 closes, then a red FXY session with price >= 58.00.
Debit legs are broker checks (not graded here). yfinance daily closes (auto-adjusted for RSP/SPY; ETF splits none).
Run: .venv/bin/python -I regrade.py
"""
import os, time
import pandas as pd
import yfinance as yf
HERE = os.path.dirname(os.path.abspath(__file__))
for i in range(4):
    try:
        px = yf.download(["RSP", "SPY", "IEF", "FXY"], start="2026-08-15", interval="1d", auto_adjust=False, progress=False)["Close"]; break
    except Exception:
        if i == 3: raise
        time.sleep(5)
px = px.dropna(); px.to_csv(os.path.join(HERE, "closes.csv"))
dgs = pd.read_csv("/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-TERRY/2deef114-c99a-4664-858a-cf4630aeb422/scratchpad/dgs10.csv", index_col=0, parse_dates=True)["DGS10"]
dgs = pd.to_numeric(dgs, errors="coerce")
print(f"bars: {len(px)} ({px.index[0].date()} -> {px.index[-1].date()})\n")
ratio = px["RSP"] / px["SPY"]
print("RSP: date | close | >215 | ratio | prior-20 max | ratio leg | day chg")
for d in px.index[-5:]:
    i = px.index.get_loc(d); pm = ratio.iloc[i-20:i].max(); c = px["RSP"].iloc[i]; ch = c / px["RSP"].iloc[i-1] - 1
    print(f"  {d.date()} | {c:.2f} | {c>215} | {ratio.iloc[i]:.9f} | {pm:.9f} | {ratio.iloc[i]>pm} | {ch*100:+.2f}%")
print("\nIEF: date | DGS10 | <=5.00 | IEF close | day chg | red & >=90")
for d in px.index[-5:]:
    i = px.index.get_loc(d); c = px["IEF"].iloc[i]; ch = c / px["IEF"].iloc[i-1] - 1
    t = dgs.get(d, float('nan'))
    print(f"  {d.date()} | {t} | {t<=5.00 if t==t else 'not published'} | {c:.2f} | {ch*100:+.2f}% | {ch<0 and c>=90}")
print("\nFXY: date | close | prior-20 high | breakout | day chg | red & >=58")
for d in px.index[-5:]:
    i = px.index.get_loc(d); c = px["FXY"].iloc[i]; hi = px["FXY"].iloc[i-20:i].max(); ch = c / px["FXY"].iloc[i-1] - 1
    print(f"  {d.date()} | {c:.2f} | {hi:.2f} | {c>hi} | {ch*100:+.2f}% | {ch<0 and c>=58}")
