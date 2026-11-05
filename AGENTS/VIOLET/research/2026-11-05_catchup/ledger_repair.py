# Catch-up 2026-11-05: dated rows from Cboe files. Observations only; no threshold or logic change.
import csv, io, math, urllib.request, datetime as dt, pandas as pd, yfinance as yf
W="AGENTS/VIOLET/workbook/"; R="AGENTS/VIOLET/research/2026-11-05_catchup/"
STAMP=dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
def rd(p):
    t=open(p,newline="",encoding="utf-8").read().split("\n"); 
    if t[-1]=="": t=t[:-1]
    return [l.split("\t") for l in t]
def wr(p,rows): open(p,"w",newline="",encoding="utf-8").write("\n".join("\t".join(r) for r in rows)+"\n")
def cboe(sym):
    req=urllib.request.Request(f"https://cdn.cboe.com/api/global/us_indices/daily_prices/{sym}_History.csv",headers={"User-Agent":"research-client"})
    d=pd.read_csv(io.BytesIO(urllib.request.urlopen(req,timeout=30).read())); d["DATE"]=pd.to_datetime(d["DATE"])
    return d.set_index("DATE")["CLOSE" if "CLOSE" in d.columns else sym].dropna()
# 1. VX_DAILY m1m2 on 11/02-11/04, same-day settle WITH its stamp
rows=rd(W+"VX_DAILY.tsv"); h=rows[0]; ix={c:i for i,c in enumerate(h)}
for d in ["2026-11-02","2026-11-03","2026-11-04"]:
    s={}
    for line in open(R+f"settle/{d}.csv",encoding="utf-8"):
        p=line.strip().split(",")
        if len(p)>=4 and p[1] in("VX/X6","VX/Z6"): s[p[1]]=float(p[3])
    v=round((s["VX/Z6"]-s["VX/X6"])/s["VX/X6"]*100,3)
    r=[x for x in rows if x[0]==d][0]; assert r[ix["m1m2_adj_pct"]]==""
    r[ix["m1m2_strict_pct"]]=r[ix["m1m2_adj_pct"]]=str(v); r[ix["m1_symbol"]]="VX/X6"; r[ix["m2_symbol"]]="VX/Z6"; r[ix["m1m2_settle_date"]]=d
    print("VX",d,s,v)
wr(W+"VX_DAILY.tsv",rows)
# 2. OVX rows on the tool basis (yfinance max window trimmed to as-of; values equal Cboe closes)
yo=yf.Ticker("^OVX").history(period="max",auto_adjust=False)["Close"].dropna(); yv=yf.Ticker("^VIX").history(period="max",auto_adjust=False)["Close"].dropna()
yo.index=yo.index.tz_localize(None).normalize(); yv.index=yv.index.tz_localize(None).normalize()
co,cv=cboe("OVX"),cboe("VIX")
rows=rd(W+"OVX.tsv"); h=rows[0]
for d in ["2026-10-29","2026-11-02","2026-11-03"]:
    t=pd.Timestamp(d); df=pd.DataFrame({"o":yo,"v":yv}).dropna(); df=df[df.index<=t]; df["r"]=df.o/df.v; df["g"]=df.o-df.v; l=df.iloc[-1]
    assert abs(l.o-co[t])<0.011 and abs(l.v-cv[t])<0.011, (d,l.o,co[t],l.v,cv[t])
    ratio=round(l.r,2); p90=round(df.r.quantile(.9),2); p95=round(df.r.quantile(.95),2); p75l=round(df.o.quantile(.75),2); p90l=round(df.o.quantile(.9),2); o=round(l.o,2)
    state="FIRE" if ratio>=p95 and o>=p75l else "WATCH" if ratio>=p90 and o>=p75l else "CALM"
    note=("BACKFILL 11/05 from official closes (values agree Cboe OVX/VIX_History), ovx.py ladder window trimmed to as-of, no later data"
          + (" REPLACES 10/29 TICK row 56.32/16.97 per KB-VIO-365" if d=="2026-10-29" else " WATCH by 0.01 on the tool window; Cboe-only window from 2009 has p90 3.01 and reads CALM"))
    new=[d,str(o),str(round(l.v,2)),str(round(l.g,2)),str(ratio),str(round((df.o<=l.o).mean()*100,1)),str(round((df.r<=l.r).mean()*100,1)),str(round((df.g<=l.g).mean()*100,1)),str(p90),str(p95),str(p75l),str(p90l),state,note,STAMP]
    assert len(new)==len(h)
    rows=[r for r in rows if r[0]!=d]; rows.append(new); print("OVX",new[:13])
rows=[rows[0]]+sorted(rows[1:],key=lambda r:r[0]); wr(W+"OVX.tsv",rows)
# 3. IMPLIED_CORR dated closes
c1,c3,c30=cboe("COR1M"),cboe("COR3M"),cboe("COR30D")
rows=rd(W+"IMPLIED_CORR.tsv"); h=rows[0]; ix={c:i for i,c in enumerate(h)}
print("check 10/30 row", [r for r in rows if r[0]=="2026-10-30"][0][:4], c1[pd.Timestamp("2026-10-30")], c3[pd.Timestamp("2026-10-30")], c30[pd.Timestamp("2026-10-30")])
sess=list(c1.index); 
for d in ["2026-10-29","2026-11-02","2026-11-03","2026-11-04"]:
    t=pd.Timestamp(d); p=sess[sess.index(t)-1]; vix=round(float(cv[t]),2); c=round(float(c1[t]),2)
    note="constituent_vol_est is DERIVED VIX/sqrt(rho), first-order, DIRECTION-ONLY; BACKFILL 11/05 from Cboe COR*/VIX_History"+(" REPLACES 10/29 TICK row 9.52/13.43 per KB-VIO-365" if d=="2026-10-29" else "")
    new=[d,str(c),str(round(float(c3[t]),2)),str(round(float(c30[t]),2)),str(vix),str(round(vix/math.sqrt(c/100),1)),str(round(float(c1[p]),2)),"SETTLE",STAMP,note]
    assert len(new)==len(h)
    rows=[r for r in rows if r[0]!=d]; rows.append(new); print("COR",new[:8])
rows=[rows[0]]+sorted(rows[1:],key=lambda r:r[0]); wr(W+"IMPLIED_CORR.tsv",rows)
