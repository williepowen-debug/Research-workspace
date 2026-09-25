# 2026-09-25 FORUM-7 BOND legs: ACM/KW share + gap base rates. Reads the ACM xls downloaded 01:06 ET 9/25 (frontier 9/23) from the session scratchpad path below; re-point S to a saved copy to reproduce.
import sys, datetime as dt, statistics as st, xlrd
sys.path.insert(0,"monitors"); sys.path.insert(0,"/home/willi/Research-workspace/FORGE/tools/market-data")
import fetch
S="/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-BOND/05a9513e-d3ce-4686-bf93-248e70ea3571/scratchpad"
# ---- ACM (file downloaded 01:06 ET; frontier 9/23 — 9/24 NOT in it)
sh=xlrd.open_workbook(S+"/acm.xls").sheet_by_name("ACM Daily"); h=sh.row_values(0); ci={x:i for i,x in enumerate(h)}
acm=[]
for r in range(1,sh.nrows):
    v=sh.row_values(r); d=dt.datetime.strptime(v[0],"%d-%b-%Y").date(); acm.append((d,v[ci["ACMTP10"]],v[ci["ACMY10"]]))
print("ACM frontier:",acm[-1][0])
kw={dt.date.fromisoformat(o["date"]):float(o["value"]) for o in fetch.fred_fetch("THREEFYTP10",limit=20000) if "error" not in o and o["value"] not in (".","")}
print("KW frontier:",max(kw))
def pct(xs,q): xs=sorted(xs); return xs[min(len(xs)-1,int(q*len(xs)))]
A={d:(tp,y) for d,tp,y in acm}
days=[d for d,_,_ in acm if d>=dt.date(2010,1,1)]
for k in (2,3):
    share=[]; gap=[]
    for i in range(len(days)-k):
        a,b=days[i],days[i+k]
        dy=(A[b][1]-A[a][1])*100; dtp=(A[b][0]-A[a][0])*100
        if dy>=15: share.append(dtp/dy)
        if a in kw and b in kw: gap.append(abs(dtp-(kw[b]-kw[a])*100))
    print(f"k={k}-session windows since 2010: ACM TP share of ΔY10 on windows with ΔY10>=+15bp: n={len(share)} median={st.median(share):.2f} p25={pct(share,.25):.2f} p75={pct(share,.75):.2f} p90={pct(share,.9):.2f}")
    print(f"   |ΔACM_TP-ΔKW_TP| n={len(gap)} median={st.median(gap):.2f} p75={pct(gap,.75):.2f} p90={pct(gap,.9):.2f} p95={pct(gap,.95):.2f}; share of windows > 6.9bp = {sum(g>6.9 for g in gap)/len(gap):.3f}")
# known leg 9/22->9/23
print("KNOWN 9/22->9/23 ACM: dTP=%.2f dY=%.2f share=%.2f"%((A[dt.date(2026,9,23)][0]-A[dt.date(2026,9,22)][0])*100,(A[dt.date(2026,9,23)][1]-A[dt.date(2026,9,22)][1])*100,(A[dt.date(2026,9,23)][0]-A[dt.date(2026,9,22)][0])/(A[dt.date(2026,9,23)][1]-A[dt.date(2026,9,22)][1])))
# ---- percentiles p05/p10 of ACM share, and KW share on DGS10 (par) moves
dg={dt.date.fromisoformat(o["date"]):float(o["value"]) for o in fetch.fred_fetch("DGS10",limit=20000) if "error" not in o and o["value"] not in (".","")}
share=[]
for i in range(len(days)-2):
    a,b=days[i],days[i+2]; dy=(A[b][1]-A[a][1])*100
    if dy>=15: share.append((A[b][0]-A[a][0])*100/dy)
print("ACM 2-sess share p05=%.2f p10=%.2f p25=%.2f"%(pct(share,.05),pct(share,.10),pct(share,.25)))
kd=sorted(d for d in kw if d>=dt.date(2010,1,1) and d in dg)
ks=[]
for i in range(len(kd)-2):
    a,b=kd[i],kd[i+2]; dy=(dg[b]-dg[a])*100
    if dy>=15: ks.append((kw[b]-kw[a])*100/dy)
print("KW 2-sess share (ΔKW/ΔDGS10, ΔDGS10>=15) n=%d p05=%.2f p10=%.2f p25=%.2f median=%.2f p75=%.2f"%(len(ks),pct(ks,.05),pct(ks,.1),pct(ks,.25),st.median(ks),pct(ks,.75)))
