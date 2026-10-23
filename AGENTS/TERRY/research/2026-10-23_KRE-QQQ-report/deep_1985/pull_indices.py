"""Long daily histories for the deep study: ^NDX (1985), ^IXIC (1971), ^BKX (1993), ^TNX, plus KRE/QQQ
for the overlap check. Writes hist_idx.csv. Run: .venv/bin/python -I pull_indices.py
"""
import os, time
import yfinance as yf
HERE = os.path.dirname(os.path.abspath(__file__))
for i in range(4):
    try:
        df = yf.download(["^NDX", "^IXIC", "^BKX", "^TNX", "KRE", "QQQ"], start="1971-01-01", interval="1d",
                         auto_adjust=True, progress=False)["Close"]
        break
    except Exception:
        if i == 3:
            raise
        time.sleep(5 * (i + 1))
df.to_csv(os.path.join(HERE, "hist_idx.csv"))
print(df.shape); print(df.apply(lambda s: s.first_valid_index()).to_string()); print(df.count().to_string())
