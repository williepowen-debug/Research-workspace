"""Independent bounded calculations from the frozen Study 4 panel, no network."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
p=Path(__file__).resolve().parent
x=pd.read_csv(p/'source/data/panel.csv',index_col=0,parse_dates=True)
f=['MKT','SMB','HML','MOM']
for k in f:x[k]=x[k+'_ff'].fillna(x[k+'_p'])
fac=f+['dy10']
w=x.loc[:'2026-10-30'].tail(63)
def fit(y):
 a=np.column_stack([np.ones(len(w)),w[fac]])
 b=np.linalg.lstsq(a,y,rcond=None)[0];e=y-a@b
 return b,e,float(1-np.sum(e**2)/np.sum((y-y.mean())**2))
b,e,r2=fit(w.KRE-w.RF);bb,eb,br2=fit(w.KBWB-w.RF)
sector={}
for s in ['XLU','IYR','ITB','XLI','XLB','IYT','KIE','IWN','XLF','KBWB']:
 rolling=x[s].rolling(63).cov(x.SPY)/x.SPY.rolling(63).var();h=rolling.loc['2012-02-01':'2024-12-31'].dropna()
 sector[s]={'beta':float(rolling.iloc[-1]),'pct_pre2025':float((h<=rolling.iloc[-1]).mean())}
y=w.KRE-w.RF
bad=1-np.asarray(e).var()/y.var()
q=pd.read_csv(p/'source/out/q5_frozen_loading_test.csv');h=q[(q.asset=='KRE')&(q.to_end<'2025-01-01')]
result={'scope':'Independent calculations on supplied panel; not independent vendor verification','n':len(w),'corr_KRE_KBWB':float(w.KRE.corr(w.KBWB)),'KRE_beta_SPY':float(w.KRE.cov(w.SPY)/w.SPY.var()),'corr_SPY_RSP':float(w.SPY.corr(w.RSP)),'M3_loadings':dict(zip(fac,map(float,b[1:]))),'M3_R2_correct':r2,'q3b_mixed_ddof_R2':float(bad),'residual_corr':float(np.corrcoef(e,eb)[0,1]),'ten_comparators':sector,'q5_saved_output_calibration':{'n':len(h),'frozen_sd':float(h.err_frozen.std()),'naive_sd':float(h.err_naive.std())},'q5_limitation':'Frozen asset loadings are multiplied by realized NEXT-window factor betas; conditional attribution, not an unconditional ex-ante forecast.'}
(p/'key_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
