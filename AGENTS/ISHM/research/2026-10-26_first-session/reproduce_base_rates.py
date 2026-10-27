from pathlib import Path
import pandas as pd,json
D=Path(__file__).resolve().parent/'sources'
O=D.parent

def fred(k):
 f=pd.read_csv(D/(k+'.csv'),index_col=0,parse_dates=True).iloc[:,0]
 return pd.to_numeric(f,errors='coerce').dropna()
cass=fred('FRGSHPUSM649NCIS');yoy=(cass/cass.shift(12)-1)*100
h=fred('BAMLH0A0HYM2').resample('MS').mean();h=h[h.index<'2026-10-01']
z=pd.DataFrame({'cass_yoy_pct':yoy,'hy_oas_pct':h}).dropna()
z['hy_change_3m_bp']=(h-h.shift(3))*100
z['hy_forward_3m_bp']=(h.shift(-3)-h)*100
z['freight_down']=z.cass_yoy_pct<0
z['three_down']=(yoy<0).rolling(3,min_periods=3).sum().reindex(z.index)==3
# Earliest HY month is partial. Remove it from month means and require three full lag months.
z=z[z.index>='2023-11-01']
z.loc[z.index<'2024-02-01','hy_change_3m_bp']=float('nan')
z.to_csv(O/'J2_monthly_sample.csv',float_format='%.9f')
report={'sample_start':str(z.index.min().date()),'sample_end':str(z.index.max().date()),'months':len(z),'freight_down_months':int(z.freight_down.sum()),'cass_history_start':str(cass.index.min().date()),'hy_daily_start':str(fred('BAMLH0A0HYM2').index.min().date()),'results':[],'distributions':{}}
for window in ['hy_change_3m_bp','hy_forward_3m_bp']:
 for freight in ['freight_down','three_down']:
  q=z[z[freight]].dropna(subset=[window])
  for bar in [0,25,50]:
   count=int((q[window]<=bar).sum())
   report['results'].append({'window':window,'freight':freight,'widening_cut_bp':bar,'no_widening_count':count,'denominator':len(q),'rate_pct':100*count/len(q) if len(q) else None})
for name,s in [('cass_yoy',yoy.dropna()),('core_capex_yoy',(fred('NEWORDER').pct_change(12)*100).dropna()),('rail_carloads_yoy',(fred('RAILFRTCARLOADSD11').pct_change(12)*100).dropna())]:
 report['distributions'][name]={'start':str(s.index.min().date()),'end':str(s.index.max().date()),'n':len(s),'p10':float(s.quantile(.1)),'p25':float(s.quantile(.25)),'p50':float(s.median()),'p75':float(s.quantile(.75)),'latest':float(s.iloc[-1]),'below0_n':int((s<0).sum()),'below_minus5_n':int((s<-5).sum())}
# Direct publisher XLSX reconciliation of FRED Cass mirror.
f=pd.read_excel(D/'cass_history.xlsx',sheet_name='Freight Index-Shipments',header=None)
p=f.iloc[7:,[1,2]].copy();p.columns=['date','publisher'];p['date']=pd.to_datetime(p.date,errors='coerce');p['publisher']=pd.to_numeric(p.publisher,errors='coerce');p=p.dropna().set_index('date').publisher
joint=pd.concat([cass.rename('fred'),p],axis=1).dropna();report['cass_publisher_reconcile']={'n':len(joint),'max_abs_gap':float((joint.fred-joint.publisher).abs().max())}
(O/'BASE_RATES.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
