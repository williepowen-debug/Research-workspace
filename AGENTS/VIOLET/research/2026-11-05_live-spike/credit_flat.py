import pandas as pd,numpy as np,io,urllib.request,sys,re
f=sys.argv[1]
rows=[l.split() for l in open(f,errors="ignore") if re.match(r"\d{4}-\d{2}-\d{2}\s+\d+\.\d+\s*$",l)]
a=pd.Series({pd.Timestamp(x):float(y)*100 for x,y in rows})
c=pd.read_csv("AGENTS/VIOLET/workbook/fred_cache/BAMLH0A0HYM2_2024-10-01.csv"); c.columns=["d","v"]; c=c[pd.to_numeric(c.v,errors="coerce").notna()]
b=pd.Series(c.v.astype(float).values*100,index=pd.to_datetime(c.d))
hy=pd.concat([a,b[b.index>a.index[-1]]]).sort_index()
r=urllib.request.Request("https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv",headers={"User-Agent":"research-client"})
v=pd.read_csv(io.BytesIO(urllib.request.urlopen(r,timeout=20).read())); v["DATE"]=pd.to_datetime(v["DATE"]); v=v.set_index("DATE")["CLOSE"]
d=pd.DataFrame({"v":v,"h":hy}).dropna(); d["v5"]=d.v.pct_change(5)*100; d["h5"]=d.h.diff(5)
print("rows",len(d),d.index[0].date(),d.index[-1].date())
print("all days 5d HY change abs pctiles",d.h5.abs().quantile([.5,.75,.9]).round(1).to_dict())
e=d[d.v5>=30]; keep=[];last=None
for t in e.index:
    if last is None or (d.index.get_loc(t)-d.index.get_loc(last))>=20: keep.append(t); last=t
x=d.loc[keep]; print("episodes VIX+30% in 5d",len(x)); print("HY 5d change median",x.h5.median(),"quartiles",x.h5.quantile([.25,.75]).round(1).to_dict())
for k in (10,15,25): print("share within <=",k,"bp wider:",round((x.h5<=k).mean()*100,1),"n",int((x.h5<=k).sum()))
fw=[]
for t in keep:
    i=d.index.get_loc(t); 
    if i+20<len(d): fw.append((d.h5.iloc[i],d.h.iloc[i+20]-d.h.iloc[i],d.v.iloc[i+1:i+21].max()/d.v.iloc[i]))
f=pd.DataFrame(fw,columns=["h5","hf","vm"])
for name,m in [("<=+10",f.h5<=10),("+10 to +25",(f.h5>10)&(f.h5<=25)),(">+25",f.h5>25)]:
    y=f[m]; print(name,"n",len(y),"median HY next20",round(y.hf.median(),1),"median VIX max ratio",round(y.vm.median(),3),"HY +50bp next20",int((y.hf>=50).sum()))
