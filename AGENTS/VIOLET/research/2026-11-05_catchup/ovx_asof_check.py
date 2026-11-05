# As-of reconstruction check for OVX.tsv rows (ratio ladder vs tool). Read-only.
import pandas as pd, sys, yfinance as yf, io, urllib.request
def cboe(sym,col):
    req=urllib.request.Request(f"https://cdn.cboe.com/api/global/us_indices/daily_prices/{sym}_History.csv",headers={"User-Agent":"research-client"})
    d=pd.read_csv(io.BytesIO(urllib.request.urlopen(req,timeout=30).read()))
    d["DATE"]=pd.to_datetime(d["DATE"]); return d.set_index("DATE")[col].dropna()
co=cboe("OVX","OVX"); cv=cboe("VIX","CLOSE")
yo=yf.Ticker("^OVX").history(period="max",auto_adjust=False)["Close"].dropna(); yv=yf.Ticker("^VIX").history(period="max",auto_adjust=False)["Close"].dropna()
yo.index=yo.index.tz_localize(None).normalize(); yv.index=yv.index.tz_localize(None).normalize()
print("cboe OVX start",co.index[0].date(),len(co),"yf OVX start",yo.index[0].date(),len(yo))
for name,o,v in (("cboe",co,cv),("yf",yo,yv)):
    for dt in ["2026-10-28","2026-10-29","2026-10-30","2026-11-02","2026-11-03","2026-11-04"]:
        t=pd.Timestamp(dt); df=pd.DataFrame({"o":o,"v":v}).dropna(); df=df[df.index<=t]
        if t not in df.index: print(name,dt,"absent"); continue
        df["r"]=df.o/df.v; df["g"]=df.o-df.v; l=df.iloc[-1]
        print(name,dt,len(df),round(l.o,2),round(l.v,2),"ratio",round(l.r,2),"pr",round((df.r<=l.r).mean()*100,1),"p90",round(df.r.quantile(.9),2),"p95",round(df.r.quantile(.95),2),"lvlp",round((df.o<=l.o).mean()*100,1),"p75lvl",round(df.o.quantile(.75),2),"p90lvl",round(df.o.quantile(.9),2),"gp",round((df.g<=l.g).mean()*100,1))
