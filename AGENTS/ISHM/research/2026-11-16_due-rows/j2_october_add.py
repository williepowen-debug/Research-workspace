"""J2 base-rate sample: add the October 2026 Cass month (2026-11-16).
Reads the 2026-11-13 sample unchanged; appends one row for October 2026 from the
Cass publisher XLSX (sources/cass_historical_1116.xlsx, Last-Modified 2026-11-13 22:20 GMT)
and the 2026-11-13 FRED HY OAS pull (October complete in it). No forward window
matures today: August's forward target (November 2026) is incomplete."""
from pathlib import Path
import pandas as pd, openpyxl, json
H=Path(__file__).resolve().parent
old=pd.read_csv(H.parent/'2026-11-13_due-rows/J2_monthly_sample_2026-11-13.csv',index_col=0,parse_dates=True)
hy=pd.to_numeric(pd.read_csv(H.parent/'2026-11-13_due-rows/sources/BAMLH0A0HYM2.csv',index_col=0,parse_dates=True).iloc[:,0],errors='coerce').dropna()
m=hy.resample('MS').mean()
ws=openpyxl.load_workbook(H/'sources/cass_historical_1116.xlsx',data_only=True)['Freight Index-Shipments']
cass={r[1]:r[2] for r in ws.iter_rows(values_only=True) if r[1] is not None and hasattr(r[1],'year')}
oct26,oct25=pd.Timestamp('2026-10-01'),pd.Timestamp('2025-10-01')
# revision check: every month already in the sample must match the new XLSX y/y
chk=[]
for d in old.index:
    a,b=cass.get(d.to_pydatetime()),cass.get((d-pd.DateOffset(years=1)).to_pydatetime())
    if a and b: chk.append(abs((a/b-1)*100-old.at[d,old.columns[0]]))
yoy=(cass[oct26.to_pydatetime()]/cass[oct25.to_pydatetime()]-1)*100
new=old.copy()
row={c:float('nan') for c in old.columns}
row[old.columns[0]]=yoy; row['hy_oas_pct']=m[oct26]
row['hy_change_3m_bp']=(m[oct26]-m[pd.Timestamp('2026-07-01')])*100
row['freight_down']=yoy<0
prev=[new.at[pd.Timestamp(x),old.columns[0]] for x in ['2026-08-01','2026-09-01']]
row['three_down']=all(v<0 for v in prev+[yoy])
new.loc[oct26]=row
new.to_csv(H/'J2_monthly_sample_2026-11-16.csv',float_format='%.9f')
res=[]
for w in ['hy_change_3m_bp','hy_forward_3m_bp']:
  for f in ['freight_down','three_down']:
    q=new[new[f].astype(str)=='True'].dropna(subset=[w])
    for bar in [0,25,50]:
      res.append({'window':w,'freight':f,'cut_bp':bar,'count':int((q[w]<=bar).sum()),'den':len(q)})
out={'added_month':'2026-10','cass_ship_oct26':cass[oct26.to_pydatetime()],'cass_ship_oct25':cass[oct25.to_pydatetime()],
     'cass_yoy_pct':yoy,'freight_down':bool(yoy<0),'hy_oct_mean_pct':float(m[oct26]),'hy_trailing_3m_bp':row['hy_change_3m_bp'],
     'cass_revision_check':{'months_compared':len(chk),'max_abs_yoy_diff_pp':float(max(chk))},
     'filled_forward_windows':[], 'results':res}
(H/'J2_BASE_RATES_2026-11-16.json').write_text(json.dumps(out,indent=2,default=str)); print(json.dumps(out,indent=1,default=str))
