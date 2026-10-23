"""Rebuild the report datasets into ./data (TERRY 2026-10-23). Run: (cd repo root && .venv/bin/python -I AGENTS/TERRY/research/2026-10-23_KRE-QQQ-report/build_report_data.py).
kre_qqq_daily.csv and yearly_corr.csv were built separately (see README); px.csv is the frozen backtest price file."""
import sys, math, time, importlib.util, pandas as pd, numpy as np, yfinance as yf
import os
B=os.path.dirname(os.path.abspath(__file__)); R=B+'/data'
def dl(t,s,e):
    for k in range(5):
        x=yf.download(t,start=s,end=e,progress=False,auto_adjust=True)['Close']
        if all(x[c].count()>10 for c in x): return x
        time.sleep(3)
    raise SystemExit('download failed '+str(t))
T=dl(['KRE','QQQ','^TNX'],'2016-10-01','2026-10-23'); T=T[['KRE','QQQ','^TNX']]; T.columns=['KRE','QQQ','TNX']
ratio=T.KRE/T.QQQ
W=[('Post-election growth bet','2016-11-08','2016-12-09'),('Vaccine news, reopening','2020-11-06','2020-12-07'),('Reopening, rising rates','2020-12-31','2021-03-31'),('Reopening trade unwinds','2021-06-01','2021-07-08'),('Rate-cut hopes, small-cap rotation','2024-07-10','2024-07-31'),('Then: both fall together','2024-07-31','2024-08-05'),('Now: AI and chip sell-off','2026-10-06','2026-10-22')]
rows=[]
for lab,a,b in W:
    x=T.loc[a:b]; r=ratio.loc[a:b]; net=(r.iloc[-1]/r.iloc[0]-1)*100
    ctr=((r/r.cummax())-1).min()*100 if net>0 else ((r/r.cummin())-1).max()*100
    i=ratio.index.get_indexer([x.index[-1]])[0]
    trend=not lab.startswith('Then')
    nxt=round((ratio.iloc[i+20]/ratio.iloc[i]-1)*100,1) if (trend and i+20<len(ratio) and not lab.startswith('Now')) else None
    rows.append({'episode':lab,'start':x.index[0].strftime('%Y-%m-%d'),'end':x.index[-1].strftime('%Y-%m-%d'),
      'kre_pct':round((x.KRE.iloc[-1]/x.KRE.iloc[0]-1)*100,1),'qqq_pct':round((x.QQQ.iloc[-1]/x.QQQ.iloc[0]-1)*100,1),
      'ten_year_start':round(float(x.TNX.iloc[0]),2),'ten_year_end':round(float(x.TNX.iloc[-1]),2),
      'ratio_net_pct':round(net,1) if trend else None,'max_counter_pct':round(ctr,1) if trend else None,'sessions':len(x) if trend else None,'ratio_next20_pct':nxt})
pd.DataFrame(rows).to_csv(R+'/divergence_episodes_v2.csv',index=False)
d=dl(['KRE','QQQ'],'2024-01-01','2026-10-23'); r=(d.pct_change()*100).dropna()
bd=[]
for lab,a,b in [('Sep 25 – Oct 22, 2026','2026-09-25','2026-10-22'),('Jul – Sep 2026','2026-07-01','2026-09-24'),('Jan 2025 – Jun 2026','2025-01-01','2026-06-30'),('2024','2024-01-01','2024-12-31')]:
    x=r.loc[a:b]; dn=x[x.QQQ<=-1]; up=x[x.QQQ>=1]
    bd.append({'window':lab,'qqq_down_days':len(dn),'kre_avg_on_down':round(dn.KRE.mean(),2),'kre_up_share':int(round((dn.KRE>0).mean()*100)),'qqq_up_days':len(up),'kre_avg_on_up':round(up.KRE.mean(),2),'kre_down_share':int(round((up.KRE<0).mean()*100))})
pd.DataFrame(bd).to_csv(R+'/big_days.csv',index=False)
spec=importlib.util.spec_from_file_location('bt',B+'/seesaw_bt.py'); res={}
for tag,(ks,qs) in {'base':(1.35,0.88),'low':(1.1,0.75),'high':(1.6,1.0)}.items():
    sys.argv=['x',B+'/px.csv',str(ks),str(qs)]; bt=importlib.util.module_from_spec(spec); spec.loader.exec_module(bt)
    for s in ['2026-07-01','2026-08-24','2026-09-23','2026-10-06','2026-10-15']:
        u=bt.d.loc[s:]
        for m,lab in [('hold','Hold both'),('rebalance','Rebalance (sell–buy)'),('harvest','Harvest and park')]:
            o=bt.run(s,m); k=(s,m)
            res.setdefault(k,{'id':s+' '+m,'start':s,'strategy':lab,'kre_px_pct':round((u.KRE.iloc[-1]/u.KRE.iloc[0]-1)*100,1),'qqq_px_pct':round((u.QQQ.iloc[-1]/u.QQQ.iloc[0]-1)*100,1)})
            res[k]['pnl_'+tag]=o['pnl_pct']
            if tag=='base': res[k]['trades']=o['trades']; res[k]['friction_usd']=o['friction']
pd.DataFrame(res.values())[['id','start','strategy','kre_px_pct','qqq_px_pct','pnl_base','pnl_low','pnl_high','trades','friction_usd']].to_csv(R+'/strategy_backtest.csv',index=False)
dd=dl(['KRE','QQQ','^VIX','^VXN'],'2023-06-01','2026-10-23').dropna(subset=['KRE','QQQ']); dd[['^VIX','^VXN']]=dd[['^VIX','^VXN']].ffill()
N=lambda x:0.5*(1+math.erf(x/math.sqrt(2)))
def put(S,K,T,v,rr=0.04):
    if T<=0: return max(K-S,0)
    d1=(math.log(S/K)+(rr+v*v/2)*T)/(v*math.sqrt(T));d2=d1-v*math.sqrt(T);return K*math.exp(-rr*T)*N(-d2)-S*N(-d1)
legs={'QQQ':('^VXN',0.88,0.01),'KRE':('^VIX',1.35,0.05)}; H=20; out=[]; feats={}
for leg,(vx,sc,fr) in legs.items():
    px=dd[leg]; v=dd[vx]; ma=(px/px.rolling(20).mean()-1)*100; pct=v.rolling(120).apply(lambda x:(x<x[-1]).mean()*100,raw=True); feats[leg]=(ma,pct,v)
    rs=[]
    for i in range(len(dd)):
        if dd.index[i]<pd.Timestamp('2024-01-02') or i+H>=len(dd): continue
        S0=px.iloc[i];K=S0*0.97;p0=put(S0,K,60/365,sc*v.iloc[i]/100)*(1+fr);S1=px.iloc[i+H];p1=put(S1,K,32/365,sc*v.iloc[i+H]/100)*(1-fr)
        rs.append((ma.iloc[i],pct.iloc[i],p1/p0-1))
    Rr=pd.DataFrame(rs,columns=['ma','pct','ret']).dropna()
    for name,m in [('Any day',Rr.ret==Rr.ret),('Cheap insurance (vol ≤ 25th pct)',Rr.pct<=25),('Expensive insurance (vol ≥ 75th pct)',Rr.pct>=75),('Stretched up (≥ +2% vs 20-day avg)',Rr.ma>=2),('Stretched down (≤ −2% vs 20-day avg)',Rr.ma<=-2),('Cheap AND stretched up',(Rr.pct<=25)&(Rr.ma>=2)),('Expensive AND stretched down',(Rr.pct>=75)&(Rr.ma<=-2))]:
        s=Rr[m]; out.append({'id':leg+': '+name,'leg':leg,'condition':name,'n_days':len(s),'approx_episodes':int(round(len(s)/20)),'mean_pct':round(s.ret.mean()*100,1),'median_pct':round(s.ret.median()*100,1),'win_pct':int(round((s.ret>0).mean()*100))})
pd.DataFrame(out).to_csv(R+'/timing_signals.csv',index=False)
sc_rows=[]
for dt,lab in [('2026-07-01','Jul 1 start'),('2026-08-24','Aug 24 start'),('2026-09-23','Sep 23 start'),('2026-10-06','Oct 6 start'),('2026-10-22','Now (Oct 22 close)')]:
    qma,qp,qv=feats['QQQ']; kma,kp,kv=feats['KRE']; t=pd.Timestamp(dt)
    sc_rows.append({'moment':lab,'date':dt,'vxn':round(float(qv.loc[t]),2),'vxn_pctile':int(round(float(qp.loc[t]))),'qqq_vs_ma20_pct':round(float(qma.loc[t]),2),'vix':round(float(kv.loc[t]),2),'vix_pctile':int(round(float(kp.loc[t]))),'kre_vs_ma20_pct':round(float(kma.loc[t]),2),'hold_pnl_base':res.get((dt,'hold'),{}).get('pnl_base')})
pd.DataFrame(sc_rows).to_csv(R+'/start_conditions.csv',index=False)
asof='2026-10-22 11:01 ET (Fidelity IRA; Robinhood unverified)'
pd.DataFrame([
 {'group':'Bank and credit puts','contracts':29,'lines':11,'detail':'KRE 16 · WAL 6 · OZK 4 · ZION 2 · APO 1','expiries':'Nov 20 – Dec 31, 2026','mirror_asof':asof},
 {'group':'Tech (QQQ) puts','contracts':1,'lines':1,'detail':'QQQ $710 put','expiries':'Oct 26, 2026','mirror_asof':asof}]).to_csv(R+'/book_snapshot.csv',index=False)
pd.DataFrame([
 {'idea':'Flagstar slow-grind put','structure':'FLG Jul 16, 2027 $10 put ×3','max_loss_usd':256.95,'max_gain_usd':None,'breakeven':9.15,'level_needed':'Level 2 (single option)','trigger':'Green FLG day Oct 26 – Nov 20; skip if FLG under $10.00; pay no more than $0.90','status':'Idea only, not fired','quote_time':'Oct 23 09:55 ET screening'},
 {'idea':'Bank leg (rotation / harvest)','structure':'KRE Dec 18, 2026 $70 put ×1','max_loss_usd':197.65,'max_gain_usd':None,'breakeven':68.03,'level_needed':'Level 2 (single option)','trigger':'Timing checklist: VIX in bottom quarter of 6 months, KRE 2%+ above 20-day average, green KRE day','status':'Watch: VIX at 93rd percentile','quote_time':'Oct 23 10:46 ET screening'},
 {'idea':'Tech leg (rotation / harvest)','structure':'QQQ Dec 18, 2026 $700/$690 put spread ×1','max_loss_usd':374.30,'max_gain_usd':625.70,'breakeven':696.27,'level_needed':'Spreads (Level 3 at Fidelity, unverified)','trigger':'Timing checklist: VXN in bottom quarter of 6 months, QQQ 2%+ above 20-day average, green QQQ day','status':'Watch: VXN at 90th percentile; spread approval unverified','quote_time':'Oct 23 10:46 ET screening'},
 {'idea':'Snap-back / both-rally gap','structure':'QQQ Dec 18, 2026 $740/$750 call spread ×1','max_loss_usd':335.30,'max_gain_usd':664.70,'breakeven':743.34,'level_needed':'Spreads (Level 3 at Fidelity, unverified)','trigger':'KRE ÷ QQQ closes 3%+ below its peak, then a red QQQ day; skip if QQQ above $730','status':'Watch: no turn yet','quote_time':'Oct 23 11:02 ET screening'},
 {'idea':'Existing card: QQQ put wall','structure':'QQQ Nov 20, 2026 $690/$670 put spread ×1','max_loss_usd':492.30,'max_gain_usd':1507.70,'breakeven':685.09,'level_needed':'Spreads (Level 3 at Fidelity, unverified)','trigger':'S&P 500 cash close below 7,650, then a green QQQ day; entry window to Oct 30','status':'Not fired (Oct 22 close 7,663.43)','quote_time':'Card of Oct 22'}]).to_csv(R+'/trade_ideas.csv',index=False)
import os; print(sorted(os.listdir(R)))
