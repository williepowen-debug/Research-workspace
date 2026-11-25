import yfinance as yf, sys, pandas as pd
syms=["^VIX","^VIX9D","^VIX3M","^VIX6M","^VVIX","^GSPC"]
out={}
for s in syms:
    try:
        h=yf.Ticker(s).history(period="2d",interval="1m",prepost=True)
        if h.empty: out[s]=h; continue
        h.index=h.index.tz_convert("America/New_York")
        h=h[h.index.date==pd.Timestamp.now(tz="America/New_York").date()]
        out[s]=h
    except Exception as e: print(s,"ERR",e)
for s,h in out.items():
    if h.empty: print(s,"no bars"); continue
    print(f"{s}: bars {h.index[0]:%H:%M}..{h.index[-1]:%H:%M} n={len(h)} last={h['Close'].iloc[-1]:.2f} hi={h['High'].max():.2f}@{h['High'].idxmax():%H:%M} lo={h['Low'].min():.2f}@{h['Low'].idxmin():%H:%M}")
marks=sys.argv[1:] or ["09:25","09:30","09:31","09:35","09:40","09:45","09:50","09:55","10:00"]
v=out.get("^VIX")
rows=[]
for m in marks:
    r=[m]
    for s in syms:
        h=out.get(s)
        if h is None or h.empty: r.append(None); continue
        sel=h[h.index.strftime("%H:%M")<=m]
        r.append(round(float(sel['Close'].iloc[-1]),2) if len(sel) and sel.index[-1].strftime("%H:%M")>=("09:30" if s!="^VIX" else "00:00") else None)
    rows.append(r)
df=pd.DataFrame(rows,columns=["ET"]+syms)
df["9D/VIX"]=(df["^VIX9D"]/df["^VIX"]).round(4); df["3M/VIX"]=(df["^VIX3M"]/df["^VIX"]).round(4)
print(df.to_string(index=False))
