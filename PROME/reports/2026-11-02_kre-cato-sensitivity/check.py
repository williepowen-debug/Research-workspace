"""Read-only audit of frozen KRE data; writes only this report's results."""
from pathlib import Path
import hashlib,json
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parents[3]
source=ROOT/'AGENTS/REGINALD/research/KRE/reports/2026-11-02_kre-etf-relationships/aligned_adjusted_closes.csv'
r=pd.read_csv(source,index_col=0,parse_dates=True).loc[:'2026-10-30'].pct_change(fill_method=None).dropna()
s=r.tail(63)
top=(s.KRE-s.KBWB).pow(2).nlargest(5).index
out={'source':str(source.relative_to(ROOT)),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'window_start':str(s.index[0].date()),'window_end':str(s.index[-1].date()),'regressions':{},'sensitivity':{}}
for x,reported in [('KBWB',.525),('IWM',.282),('SPY',.067)]:
 y=s.KRE.to_numpy();X=np.c_[np.ones(len(s)),s[x]]
 residual=y-X@np.linalg.lstsq(X,y,rcond=None)[0]
 rsq=1-float(residual@residual)/float(((y-y.mean())**2).sum())
 corr=float(s.KRE.corr(s[x]))
 assert abs(rsq-corr**2)<1e-12
 out['regressions'][x]={'n':len(s),'correlation':corr,'ols_with_intercept_R2':rsq,'external_report_R2':reported}
for label,dates in [('all',[]),('without_sep14',['2026-09-14']),('without_oct22',['2026-10-22']),('without_both',['2026-09-14','2026-10-22']),('without_top5',top)]:
 d=s.drop(pd.to_datetime(dates))
 out['sensitivity'][label]={'n':len(d),'KRE_KBWB':float(d.KRE.corr(d.KBWB)),'KRE_SPY':float(d.KRE.corr(d.SPY))}
g=(s.KRE-s.KBWB).pow(2)
out['top5_dates']=list(top.strftime('%Y-%m-%d'))
out['top5_squared_gap_share']=float(g.loc[top].sum()/g.sum())
base=[];trimmed=[]
for i in range(63,len(r)+1):
 d=r.iloc[i-63:i];base.append(d.KRE.corr(d.KBWB))
 d=d.drop((d.KRE-d.KBWB).abs().nlargest(5).index)
 trimmed.append(d.KRE.corr(d.KBWB))
for label,values in [('untrimmed_history',base),('symmetrically_trimmed_history',trimmed)]:
 a=np.array(values)
 out[label]={'overlapping_windows':len(a),'median':float(np.median(a)),'latest':float(a[-1]),'percentile_strictly_below':float(100*(a<a[-1]).mean())}
out['limits']=['Frozen same-vendor data; no independent vendor validation.','Delete return observations, not price rows; no bridging or backfill of omitted days.','Exceptional dates selected retrospectively; diagnostic only.','Historical windows overlap and percentile is not a p-value or independent episode count.','External regression implementation unavailable; discrepancy remains unreconciled.','No KBE series in this saved dataset; KBE claim not independently tested.','No causal identification, forecast, trade recommendation or owner-grade change.']
p=Path(__file__).with_name('results.json');p.write_text(json.dumps(out,indent=2)+'\n');print(p);print(json.dumps(out,indent=2))
