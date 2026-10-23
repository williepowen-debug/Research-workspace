"""Daily auto-adjusted closes for the financials comparison. Writes fin_px.csv.
ETFs: KRE regionals · KBE all banks (equal-wt) · KBWB large banks · ^BKX KBW Bank Index (1993+) · XLF broad financials ·
IAI brokers · KIE insurance · BIZD BDCs · IWM small caps · SPY · QQQ.
Single names (group composites): JPM BAC C WFC (money-center) · APO BX KKR ARES OWL (alt managers / private credit) ·
ARCC BXSL FSK GBDC HTGC (BDCs, DEWEY's software-heavy list) · WAL ZION OZK FLG (book regionals).
Run: .venv/bin/python -I pull_fin.py
"""
import os, time
import yfinance as yf
HERE = os.path.dirname(os.path.abspath(__file__))
T = ["KRE", "KBE", "KBWB", "^BKX", "XLF", "IAI", "KIE", "BIZD", "IWM", "SPY", "QQQ",
     "JPM", "BAC", "C", "WFC", "APO", "BX", "KKR", "ARES", "OWL", "ARCC", "BXSL", "FSK", "GBDC", "HTGC", "WAL", "ZION", "OZK", "FLG"]
for i in range(4):
    try:
        df = yf.download(T, start="2005-01-01", interval="1d", auto_adjust=True, progress=False)["Close"]; break
    except Exception:
        if i == 3: raise
        time.sleep(5 * (i + 1))
df.to_csv(os.path.join(HERE, "fin_px.csv"))
print(df.shape, df.index[-1]); print(df.apply(lambda s: s.first_valid_index().date()).to_string())
print("missing last row:", [c for c in df.columns if df[c].iloc[-1] != df[c].iloc[-1]])
