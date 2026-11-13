"""J2 base-rate sample: add matured windows only (2026-11-13).
Frozen first-session sample is read unchanged; only cells whose window has now
completed are filled from a fresh FRED HY OAS pull (sources/BAMLH0A0HYM2.csv).
No new freight month is added unless a Cass month exists in sources/."""
from pathlib import Path
import pandas as pd, json
H=Path(__file__).resolve().parent
old=pd.read_csv(H.parent/'2026-10-26_first-session/J2_monthly_sample.csv',index_col=0,parse_dates=True)
hy=pd.to_numeric(pd.read_csv(H/'sources/BAMLH0A0HYM2.csv',index_col=0,parse_dates=True).iloc[:,0],errors='coerce').dropna()
frozen=pd.to_numeric(pd.read_csv(H.parent/'2026-10-26_first-session/sources/BAMLH0A0HYM2.csv',index_col=0,parse_dates=True).iloc[:,0],errors='coerce').dropna()
j=pd.concat([frozen.rename('o'),hy.rename('n')],axis=1).dropna()
rev={'overlap_days':len(j),'max_abs_diff_pct':float((j.o-j.n).abs().max())}
m=hy.resample('MS').mean()
last_complete=pd.Timestamp('2026-10-01')  # October 2026 complete; November partial at pull
new=old.copy(); filled=[]
for d in new.index:
    tgt=d+pd.DateOffset(months=3)
    if pd.isna(new.at[d,'hy_forward_3m_bp']) and tgt<=last_complete:
        new.at[d,'hy_forward_3m_bp']=(m[tgt]-new.at[d,'hy_oas_pct'])*100; filled.append(str(d.date()))
new.to_csv(H/'J2_monthly_sample_2026-11-13.csv',float_format='%.9f')
res=[]
for w in ['hy_change_3m_bp','hy_forward_3m_bp']:
  for f in ['freight_down','three_down']:
    q=new[new[f].astype(str)=='True'].dropna(subset=[w])
    for bar in [0,25,50]:
      res.append({'window':w,'freight':f,'cut_bp':bar,'count':int((q[w]<=bar).sum()),'den':len(q)})
out={'filled_forward_windows':filled,'oct_2026_hy_mean_pct':float(m[last_complete]),'oct_days':int(len(hy['2026-10'])),
     'hy_pull_range':[str(hy.index.min().date()),str(hy.index.max().date())],'revision_check':rev,'results':res,
     'new_freight_months_added':0}
(H/'J2_BASE_RATES_2026-11-13.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=1))
