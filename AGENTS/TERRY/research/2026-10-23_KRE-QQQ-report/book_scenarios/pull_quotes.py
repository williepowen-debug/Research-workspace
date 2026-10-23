"""Pull live option quotes for every line in positions.csv plus one year of daily closes
for the underlyings (for betas). Writes quotes.csv and px_1y.csv next to this file.
Vendor = yfinance; option quotes are SCREENING marks (no quote timestamp; durable finding 5b).
Run: .venv/bin/python -I pull_quotes.py
"""
import csv, os, time, datetime as dt
import yfinance as yf

HERE = os.path.dirname(os.path.abspath(__file__))

def retry(fn, tries=4):
    for i in range(tries):
        try:
            return fn()
        except Exception as e:  # network is flaky on this box
            if i == tries - 1:
                raise
            time.sleep(3 * (i + 1))

pos = list(csv.DictReader(open(os.path.join(HERE, "positions.csv"))))
tickers = sorted({p["ticker"] for p in pos})
pulled = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

spots = {}
for t in tickers:
    h = retry(lambda: yf.Ticker(t).history(period="1d", interval="1m"))
    spots[t] = (float(h["Close"].iloc[-1]), str(h.index[-1]))

chains = {}
rows = []
for p in pos:
    key = (p["ticker"], p["expiry"])
    if key not in chains:
        chains[key] = retry(lambda: yf.Ticker(p["ticker"]).option_chain(p["expiry"]).puts)
    df = chains[key]
    r = df[abs(df["strike"] - float(p["strike"])) < 1e-6]
    if r.empty:
        rows.append({**p, "spot": spots[p["ticker"]][0], "spot_asof": spots[p["ticker"]][1],
                     "bid": "", "ask": "", "iv": "", "last_trade": "", "pulled": pulled, "note": "STRIKE ABSENT"})
        continue
    r = r.iloc[0]
    rows.append({**p, "spot": spots[p["ticker"]][0], "spot_asof": spots[p["ticker"]][1],
                 "bid": float(r["bid"]), "ask": float(r["ask"]), "iv": float(r["impliedVolatility"]),
                 "last_trade": str(r["lastTradeDate"]), "pulled": pulled, "note": ""})

with open(os.path.join(HERE, "quotes.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)

px = retry(lambda: yf.download(tickers, period="1y", interval="1d", auto_adjust=True, progress=False)["Close"])
px.to_csv(os.path.join(HERE, "px_1y.csv"))
print(f"pulled {pulled}: {len(rows)} quote rows, px {px.shape[0]} bars x {px.shape[1]} tickers")
for r in rows:
    print(r["ticker"], r["strike"], r["expiry"], "bid", r["bid"], "ask", r["ask"], "iv", r["iv"], r["note"])
