"""Bounded reproduction on the collection's frozen data; no network or owner updates."""
from pathlib import Path
import hashlib,json
import numpy as np
import pandas as pd
P=Path(__file__).resolve().parent
source=P.parent/'2026-11-02_kre-etf-relationships/aligned_adjusted_closes.csv'
r=pd.read_csv(source,index_col=0,parse_dates=True).loc[:'2026-10-30'].pct_change(fill_method=None).dropna();s=r.tail(63)
def partial(d):
 X=np.c_[np.ones(len(d)),d.SPY]
 residual=[d[x].values-X@np.linalg.lstsq(X,d[x].values,rcond=None)[0] for x in ['KRE','KBWB']]
 return float(np.corrcoef(*residual)[0,1])
result={'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'basis':'Saved Yahoo adjusted prices; not independent vendor validation; 3666 rather than report 3708 rolling 63-session windows.','market_beta':{x:float(s[x].cov(s.SPY)/s.SPY.var()) for x in ['KRE','KBWB']},'annualized_vol':{x:float(s[x].std()*np.sqrt(252)) for x in ['KRE','KBWB']},'annualized_gap_vol':float((s.KRE-s.KBWB).std()*np.sqrt(252)),'horizons':{},'blocks':[]}
for n in [21,42,63,126]:
 a=r.KRE.rolling(n).corr(r.KBWB).dropna()
 result['horizons'][str(n)]={'correlation':float(a.iloc[-1]),'windows':len(a),'percentile':float(100*(a<a.iloc[-1]).mean())}
for j in range(9,0,-1):
 d=r.iloc[-j*21:None if j==1 else -(j-1)*21]
 result['blocks'].append({'start':str(d.index[0].date()),'end':str(d.index[-1].date()),'correlation':float(d.KRE.corr(d.KBWB))})
a=[];trim=[]
for i in range(63,len(r)+1):
 d=r.iloc[i-63:i];a.append(partial(d));q=d.drop((d.KRE-d.KBWB).abs().nlargest(10).index);trim.append(q.KRE.corr(q.KBWB))
for label,values in [('SPY_partial',a),('trim10',trim)]:
 v=np.array(values);result[label]={'current':float(v[-1]),'median':float(np.median(v)),'percentile':float(100*(v<v[-1]).mean()),'overlapping_windows':len(v)}
c=r.KRE.rolling(63).corr(r.KBWB).dropna();d=pd.DataFrame({'current':c,'next':c.shift(-63)}).loc[:'2024-12-31'].dropna();z=d[d.current<.863]
result['persistence_check']={'threshold':.863,'conditioning_windows':len(z),'next_window_below':int((z.next<.863).sum()),'fraction':float((z.next<.863).mean()),'median_next':float(z.next.median()),'warning':'Conditioning dates overlap heavily; 175 windows are not 175 independent episodes, and historical fraction is not a forecast probability.'}
result['unverified']=['Issuer NAV replication','KBE/QABA/IAT histories and constituent baskets','Bootstrap interval','Full 3708-window baseline','Original R2 error provenance','Exact contribution attributed to volatility','Proposed forward test; no monitoring instruction adopted']
(P/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
