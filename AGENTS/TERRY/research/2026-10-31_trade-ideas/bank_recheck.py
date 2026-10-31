"""Bank-put re-check numbers (TERRY 2026-10-31). Read-only.
Lines and basis/marks transcribed from FORGE/STATUS.md (ANVIL reconcile of Will's
10/30 ~13:2x ET intraday Fidelity capture). Closes from yfinance 10/30 daily bars.
KRE frequencies: overlapping-window endpoint observations, NOT probabilities."""
import sys, json, datetime as dt
import pandas as pd, numpy as np, yfinance as yf

lines = [  # ticker, strike, expiry, qty, basis_usd, mark_1030_intraday
 ("KRE", 66.0, "2026-11-20", 3, 133.99, 0.26),
 ("KRE", 70.0, "2026-11-27", 2, 281.33, 1.02),
 ("KRE", 68.0, "2026-11-27", 10, 726.63, 0.50),
 ("KRE", 67.0, "2026-11-27", 4, 510.65, 0.37),
 ("KRE", 60.0, "2026-12-18", 5, 513.34+878.02, 0.27),
 ("KRE", 65.0, "2026-12-31", 2, 337.33, 0.75),
 ("OZK", 40.0, "2026-11-20", 4, 322.65, 0.10),
 ("WAL", 70.0, "2026-12-18", 2, 551.33, 1.15),
 ("WAL", 65.0, "2026-12-18", 4, 682.65, 0.55),
 ("ZION", 62.5, "2026-11-20", 2, 435.33, 0.40),
 ("VLY", 12.0, "2026-12-18", 1, 15.66, 0.05),
 ("FLG", 10.0, "2027-03-19", 1, 70.66, 0.55),
 ("APO", 95.0, "2026-12-18", 1, 1184.67, 0.65),
]
hol = {dt.date(2026,11,26), dt.date(2026,12,25), dt.date(2027,1,1), dt.date(2027,1,18), dt.date(2027,2,15)}
def sessions(after, to):
    d = pd.bdate_range(after + dt.timedelta(days=1), to)
    return sum(1 for x in d if x.date() not in hol)
asof = dt.date(2026,10,30)
tick = sorted({l[0] for l in lines})
closes = {}
for t in tick:
    h = yf.Ticker(t).history(start="2026-10-20", end="2026-10-31", auto_adjust=False)
    closes[t] = (float(h["Close"].iloc[-1]), str(h.index[-1].date()))
kre = yf.Ticker("KRE").history(start="2006-06-20", end="2026-10-31", auto_adjust=True)["Close"].dropna()
print(f"KRE adj-close bars: {len(kre)} ({kre.index[0].date()} .. {kre.index[-1].date()})")
tot_b = tot_v = 0.0
rows = []
for t,k,exp,q,b,m in lines:
    c, cd = closes[t]
    e = dt.date.fromisoformat(exp)
    n = sessions(asof, e)
    dist = (k/c - 1)*100
    val = m*q*100
    tot_b += b; tot_v += val
    freq = ""
    if t == "KRE":
        fwd = kre.shift(-n)/kre - 1
        fwd = fwd.dropna()
        hit = (fwd <= dist/100).mean()*100
        freq = f"{hit:.1f}% of {len(fwd)} windows"
    rows.append((t,k,exp,q,c,cd,dist,n,b,val,freq))
print(f"{'line':22} {'close[date]':18} {'to strike':>9} {'sess':>4} {'basis $':>9} {'value $':>8}  KRE endpoint freq (<= strike after N sessions, 2006+)")
for t,k,exp,q,c,cd,dist,n,b,val,freq in rows:
    print(f"{t} {k:g}P {exp} x{q:<3} {c:8.2f} [{cd}] {dist:+8.1f}% {n:4d} {b:9.2f} {val:8.2f}  {freq}")
print(f"TOTAL basis ${tot_b:,.2f} · value at 10/30 ~13:2x intraday marks ${tot_v:,.2f} · value/basis {tot_v/tot_b*100:.1f}%")
bank_b = sum(r[8] for r in rows if r[0]!="APO"); bank_v = sum(r[9] for r in rows if r[0]!="APO")
print(f"BANK ONLY (ex-APO): basis ${bank_b:,.2f} · value ${bank_v:,.2f} · contracts {sum(r[3] for r in rows if r[0]!='APO')}")
