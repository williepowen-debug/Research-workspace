import pandas as pd,numpy as np,io,urllib.request,yfinance as yf,datetime as dt
print("clock",dt.datetime.now().strftime("%H:%M"))
for t in ["^VIX","^VIX3M","^VVIX","^VIX9D","SPY","QQQ","HYG","RSP"]:
    h=yf.Ticker(t).history(period="1d",interval="1m"); print(t,round(h["Close"].iloc[-1],2),h.index[-1].strftime("%H:%M"))
def cboe(n):
    r=urllib.request.Request(f"https://cdn.cboe.com/api/global/us_indices/daily_prices/{n}_History.csv",headers={"User-Agent":"research-client"})
    d=pd.read_csv(io.BytesIO(urllib.request.urlopen(r,timeout=20).read())); d["DATE"]=pd.to_datetime(d["DATE"]); return d.set_index("DATE")
v=cboe("VIX")["CLOSE"]; m=cboe("VIX3M")["CLOSE"]
spx=yf.Ticker("^GSPC").history(start="1990-01-01",interval="1d")["Close"]; spx.index=spx.index.tz_localize(None).normalize()
d=pd.DataFrame({"v":v}); d["p"]=d.v.pct_change()*100; d["prev"]=d.v.shift(1); d["m"]=m
d=d.join(spx.rename("s"),how="left")
for name,mask in [("VIX +35%+, prior close<20",(d.p>=35)&(d.prev<20)),("VIX +25%+, prior <20",(d.p>=25)&(d.prev<20))]:
    idx=[i for i in np.where(mask)[0]]
    keep=[];last=-999
    for i in idx:
        if i-last>=20: keep.append(i); last=i
    rows=[]
    for i in keep:
        f=d.v.iloc[i+1:i+21]; 
        if len(f)<20: continue
        s0=d.s.iloc[i]; rows.append(dict(date=d.index[i].date(),prev=d.prev.iloc[i],close=d.v.iloc[i],pct=d.p.iloc[i],ratio=(d.m.iloc[i]/d.v.iloc[i]) if d.m.iloc[i]==d.m.iloc[i] else np.nan,
          v5=d.v.iloc[i+5],vmax20=f.max(),v20=d.v.iloc[i+20],spx5=(d.s.iloc[i+5]/s0-1)*100,spx20=(d.s.iloc[i+20]/s0-1)*100,spxmin20=(d.s.iloc[i+1:i+21].min()/s0-1)*100))
    x=pd.DataFrame(rows); print("\n",name,"episodes",len(x))
    if name.startswith("VIX +35"): print(x.round(2).to_string(index=False))
    print("median vmax20/close",round((x.vmax20/x.close).median(),3),"| new closing high within 20d:",int((x.vmax20>x.close).sum()),"of",len(x),"| VIX lower 5d later:",int((x.v5<x.close).sum()),"| VIX lower 20d later:",int((x.v20<x.close).sum()),"| median SPX 5d",round(x.spx5.median(),2),"20d",round(x.spx20.median(),2),"| SPX 20d down",int((x.spx20<0).sum()),"| median worst SPX 20d",round(x.spxmin20.median(),2))
    y=x[x.ratio<1]; 
    if len(y): print(" inverted subset n",len(y),"new high",int((y.vmax20>y.close).sum()),"lower 20d",int((y.v20<y.close).sum()),"median SPX20",round(y.spx20.median(),2))
c=pd.read_csv("AGENTS/VIOLET/workbook/IMPLIED_CORR.tsv",sep="\t",comment="#"); print(c.tail(6).iloc[:,:8].to_string(index=False))
c2=c.copy(); col=[k for k in c.columns if k.lower().startswith("cor1m")][0]
print("COR1M pctile of 9.53 / 18.03 in ledger:",round((c[col].astype(float)<9.53).mean()*100,1),round((c[col].astype(float)<18.03).mean()*100,1),"n",len(c))
