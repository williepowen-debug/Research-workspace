import warnings; warnings.filterwarnings('ignore')
import json, pandas as pd, numpy as np
from replicate import weights_prev, port_returns, BASE, END, TK, stock_tr, ROOT
D=ROOT+'/data/pxlong'
def ld(t):
    r=json.load(open(f'{D}/{t}.json'))['chart']['result'][0]
    idx=pd.to_datetime(r['timestamp'],unit='s').tz_localize('UTC').tz_convert('America/New_York').normalize().tz_localize(None)
    s=pd.Series(r['indicators']['adjclose'][0]['adjclose'],index=idx); s=s[~s.index.duplicated(keep='last')]
    return s[s.index<=END]
A=pd.DataFrame({t:ld(t) for t in TK+['KRE','KBWB','SPY']}).loc['2014-06-01':]
R=A.pct_change()
CM5=['JPM','BAC','GS','MS','C']; REST=[t for t in TK if t not in CM5]
W0=weights_prev(TK,start=pd.Timestamp('2026-07-31')).loc['2026-08-04']
wr=W0[REST]/W0[REST].sum(); wc=W0[CM5]/W0[CM5].sum()
R['exCM5_fixed']=(R[REST]*wr).sum(1,min_count=len(REST)); R['exCM5_EW']=R[REST].mean(1); R['CM5_fixed']=(R[CM5]*wc).sum(1,min_count=5)
# validate proxy in window vs holdings-based
Xh=port_returns(REST,start=pd.Timestamp('2026-07-31')); w=(Xh.index>BASE)
print('proxy vs holdings X corr in window', np.corrcoef(Xh[w], R['exCM5_fixed'].loc[Xh[w].index])[0,1])
R=R.loc['2015-01-01':]
out={}
for b in ['KBWB','exCM5_fixed','exCM5_EW','CM5_fixed','SPY']:
    rc=R['KRE'].rolling(63).corr(R[b]).dropna()
    cur=rc.iloc[-1]; pre=rc[rc.index<'2025-01-01']
    non=rc.iloc[::-63]  # non-overlapping ending 10/30
    out[b]=dict(current=round(cur,3),pct_all_since2015=round(100*(rc<cur).mean(),1),pct_pre2025=round(100*(pre<cur).mean(),1),median_pre2025=round(pre.median(),3),p10_pre2025=round(pre.quantile(.1),3),rank_nonoverlap=f"{int((non<cur).sum())+1}/{len(non)}")
    print(b,out[b])
pd.DataFrame(out).T.to_csv(ROOT+'/out/corr_history.csv')
# partial: what corr would KRE-KBWB be if CM5 behaved like the rest? -> in window, corr(KRE, exCM5) vs history
