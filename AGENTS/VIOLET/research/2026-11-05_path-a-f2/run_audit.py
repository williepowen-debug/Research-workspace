"""Path A F2 audit. Definitions frozen in SPEC.md (cc62521ac). Usage: run_audit.py <dir holding archived HY txt>.
Raw ICE series stay outside the repo; this writes derived tables only."""
import io, json, re, sys, urllib.parse, urllib.request
import numpy as np, pandas as pd
SRC=sys.argv[1]; OUT="AGENTS/VIOLET/research/2026-11-05_path-a-f2/"
key=""
for l in open("FORGE/tools/market-data/.env"):
    m=re.match(r'\s*(?:export\s+)?FRED_API_KEY\s*=\s*"?([^"\s]+)',l)
    if m: key=m.group(1)
def fred(sid,start):
    u="https://api.stlouisfed.org/fred/series/observations?"+urllib.parse.urlencode(dict(series_id=sid,api_key=key,file_type="json",observation_start=start))
    o=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"research-client"}),timeout=60))["observations"]
    return pd.Series({pd.Timestamp(x["date"]):float(x["value"]) for x in o if x["value"]!="."})
arch={}
for l in open(SRC+"/hy_20231212182755.txt",encoding="utf-8",errors="replace"):
    m=re.match(r"\s*(\d{4}-\d{2}-\d{2})\s+(-?\d+\.\d+)\s*$",l)
    if m: arch[pd.Timestamp(m.group(1))]=float(m.group(2))
arch=pd.Series(arch); api=fred("BAMLH0A0HYM2","2023-11-06")
ov=arch.index.intersection(api.index); assert len(ov)>=20 and (arch[ov]-api[ov]).abs().max()<1e-9
hy=pd.concat([arch,api[api.index>arch.index[-1]]]).sort_index()
hybp=(hy*100).round().astype(int)
req=urllib.request.Request("https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv",headers={"User-Agent":"research-client"})
v=pd.read_csv(io.BytesIO(urllib.request.urlopen(req,timeout=40).read())); v["DATE"]=pd.to_datetime(v["DATE"]); vix=v.set_index("DATE")["CLOSE"].dropna()
curve=fred("T10Y2Y","1996-06-01")
df=pd.DataFrame({"hy":hybp,"vix":vix}).dropna(); df["curve"]=curve.reindex(df.index).ffill(limit=5); df=df.dropna()
df["hy"]=df.hy.astype(int)
print("aligned",len(df),df.index[0].date(),df.index[-1].date(),"splice",arch.index[-1].date(),"overlap",len(ov))
n=len(df); vals=df.vix.values
def fwdmax(a,b):
    o=np.full(n,np.nan)
    for i in range(n):
        if i+b<n: o[i]=vals[i+a:i+b+1].max()
    return o
W={"t10_30":fwdmax(10,30),"t1_30":fwdmax(1,30)}
def hits(window,kind):
    m=W[window]
    if kind=="pt10": return m>=vals+10
    return m>=30 if kind=="vix30" else m>=vals*(1.5 if kind=="p50" else 1.15)
def episodes(size,look,gate):
    h=df.hy.values; tmin=pd.Series(h).shift(1).rolling(look).min().values
    tr=np.full(n,-1)
    for i in range(look,n):
        tr[i]=i-look+int(np.argmin(h[i-look:i]))
    size_ok=(h-tmin)>=size
    if gate=="base": g=(df.vix.values<20)&(df.curve.values>=0)
    elif gate=="nocurve": g=df.vix.values<20
    elif gate=="trough":
        g=np.zeros(n,bool); ok=tr>=0; g[ok]=vals[tr[ok]]<20; g&=df.curve.values>=0
    q=np.where(size_ok&g&~np.isnan(tmin))[0]; ep=[]; last=-10**6
    for i in q:
        if i-last>=30: ep.append(i); last=i
    return ep,tr
def elig(gate):
    return (df.vix.values<20)&(df.curve.values>=0) if gate!="nocurve" else df.vix.values<20
ERA=pd.Timestamp("2018-01-01"); pre=df.index<ERA; rng=np.random.default_rng(7)
def cell(label,size,look,gate,window,kind):
    ep,_=episodes(size,look,gate); H=hits(window,kind); done=~np.isnan(W[window]); r={"cell":label}
    for nm,mask in (("pre",pre),("post",~pre),("all",np.ones(n,bool))):
        e=[i for i in ep if mask[i] and done[i]]; pool=np.where(elig(gate)&mask&done)[0]
        k=int(H[e].sum()); m=len(e); base=float(H[pool].mean()) if len(pool) else np.nan
        p=np.nan
        if m and len(pool)>=m:
            s=np.array([H[rng.choice(pool,m,replace=False)].sum() for _ in range(4000)]); p=float((s>=k).mean())
        r.update({f"{nm}_n":m,f"{nm}_hits":k,f"{nm}_rate":round(k/m*100,1) if m else None,f"{nm}_base":round(base*100,1),f"{nm}_lift":round(k/m/base,2) if m and base else None,f"{nm}_p":round(p,3) if p==p else None})
    r["incomplete"]=[str(df.index[i].date()) for i in ep if not done[i]]
    return r
C=[("PRIMARY 100bp/63d/gate/t10-30/+50%",100,63,"base","t10_30","p50"),("size 75",75,63,"base","t10_30","p50"),("size 50",50,63,"base","t10_30","p50"),
   ("look 42",100,42,"base","t10_30","p50"),("look 126",100,126,"base","t10_30","p50"),("no curve filter",100,63,"nocurve","t10_30","p50"),("VIX<20 at trough",100,63,"trough","t10_30","p50"),
   ("window t1-30",100,63,"base","t1_30","p50"),("hit +15%",100,63,"base","t10_30","p15"),("hit VIX>=30",100,63,"base","t10_30","vix30"),
   ("50bp hit +15%",50,63,"base","t10_30","p15"),("50bp hit VIX>=30",50,63,"base","t10_30","vix30"),("75bp hit +15%",75,63,"base","t10_30","p15"),("trough gate 50bp",50,63,"trough","t10_30","p50"),
   # POST-FREEZE, added after outcomes were seen: TRADE.md:185 states the claim as a spike of more than 10 points.
   ("POST-FREEZE hit +10pts",100,63,"base","t10_30","pt10"),("POST-FREEZE hit +10pts t1-30",100,63,"base","t1_30","pt10"),("POST-FREEZE 75bp hit +10pts",75,63,"base","t10_30","pt10"),("POST-FREEZE 50bp hit +10pts",50,63,"base","t10_30","pt10"),("POST-FREEZE no curve +10pts",100,63,"nocurve","t10_30","pt10")]
res=[cell(*c) for c in C]; R=pd.DataFrame(res)
cols=["cell","pre_n","pre_hits","pre_rate","pre_base","pre_lift","pre_p","post_n","post_hits","post_rate","post_base","post_lift","post_p","all_n","all_hits","all_rate","all_base","all_lift","all_p","incomplete"]
R[cols].to_csv(OUT+"cells.tsv",sep="\t",index=False); print(R[cols].drop(columns=["incomplete"]).to_string(index=False))
print("incomplete:",{r["cell"]:r["incomplete"] for r in res if r["incomplete"]})
rows=[]
for nm,s,g in (("100bp",100,"base"),("75bp",75,"base"),("50bp",50,"base"),("100bp-trough",100,"trough"),("100bp-nocurve",100,"nocurve")):
    ep,tr=episodes(s,63,g)
    for i in ep:
        w=vals[i+10:i+31] if i+30<n else None
        rows.append(dict(cell=nm,date=str(df.index[i].date()),trough=str(df.index[tr[i]].date()),hy_bp=int(df.hy.iloc[i]),trough_bp=int(df.hy.iloc[tr[i]]),vix=round(vals[i],2),vix_trough=round(vals[tr[i]],2),curve=round(df.curve.iloc[i],2),
             max_t10_30=None if w is None else round(float(w.max()),2),pct=None if w is None else round((w.max()/vals[i]-1)*100,1),max_t1_30=None if i+30>=n else round(float(vals[i+1:i+31].max()),2),hit=None if w is None else bool(w.max()>=vals[i]*1.5)))
E=pd.DataFrame(rows); E.to_csv(OUT+"episodes.tsv",sep="\t",index=False); print(E[E.cell.isin(["100bp","75bp","100bp-nocurve","100bp-trough"])].to_string(index=False))
