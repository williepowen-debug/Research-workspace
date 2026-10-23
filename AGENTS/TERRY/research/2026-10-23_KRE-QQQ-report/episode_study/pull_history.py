"""Pull daily history for the episode study: KRE, QQQ, ^TNX, ^VIX from 2006-01-01 (KRE starts 2006-06).
Writes hist.csv (auto-adjusted closes; ^TNX in percent). Run: .venv/bin/python -I pull_history.py
"""
import os, time
import yfinance as yf

HERE = os.path.dirname(os.path.abspath(__file__))
for i in range(4):
    try:
        df = yf.download(["KRE", "QQQ", "^TNX", "^VIX"], start="2006-01-01", interval="1d",
                         auto_adjust=True, progress=False)["Close"]
        break
    except Exception:
        if i == 3:
            raise
        time.sleep(5 * (i + 1))
df.to_csv(os.path.join(HERE, "hist.csv"))
print(df.shape, df.index[0], df.index[-1])
print(df.count())
print(df.tail(3))
