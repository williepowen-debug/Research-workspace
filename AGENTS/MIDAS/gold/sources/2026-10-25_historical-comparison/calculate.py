"""Descriptive gold history; fixed method in METHOD.md. No network or forecasts."""
from pathlib import Path
import hashlib, json
import numpy as np
import pandas as pd

HERE=Path(__file__).resolve().parent
DESK=HERE.parents[2]
inputs={
 'issuer':DESK/'shared/sources/2026-10-25_boot/GLD_issuer_archive.xlsx',
 'recent':DESK/'shared/sources/2026-10-25_boot/GLD.csv',
 'yield_history':DESK/'sources/2026-10-12_m1-expanded/DFII10_latest.json',
 'yield_newer':DESK/'sources/2026-10-20_GLD-review/DFII10.json',
 'treasury':DESK/'shared/sources/2026-10-23_catch-up/treasury_real_curve_2026.csv',
 'stress_panel':DESK/'gold/sources/2026-10-23_wq451/panel.csv',
}
raw=pd.read_excel(inputs['issuer'],sheet_name='US GLD Historical Archive')
raw['Date']=pd.to_datetime(raw.Date,format='%d-%b-%Y',errors='raise')
raw['close']=pd.to_numeric(raw['Closing Price'],errors='coerce')
assert not raw.Date.duplicated().any()
raw.loc[raw.close.isna(),['Date','Closing Price']].to_csv(HERE/'excluded_issuer_rows.csv',index=False)
d=raw.dropna(subset=['close']).set_index('Date').sort_index()
assert (d.close>0).all()
s=d.close.copy()
v=pd.read_csv(inputs['recent'],index_col=0,parse_dates=True).Close
v.index=pd.to_datetime(v.index).tz_localize(None).normalize()
overlap=s.index.intersection(v.index)
err=float((s.loc[overlap]-v.loc[overlap]).abs().max())
assert err<.0001,err
append=v.loc[(v.index>s.index[-1])&(v.index<=pd.Timestamp('2026-10-23'))]
s=pd.concat([s,append]);assert s.index.is_unique and str(s.index[-1].date())=='2026-10-23'
pd.DataFrame({'close':s,'source':['PRIMARY issuer' if t<=d.index[-1] else 'MIRROR Yahoo' for t in s.index]}).to_csv(HERE/'gold_close_series.csv')
dd=100*(s/s.cummax()-1)
pd.DataFrame({'close':s,'drawdown_pct':dd}).to_csv(HERE/'drawdown_series.csv')
recent=[]
for n in [1,5,21,63,126,252,504,756]:
 r=100*(s/s.shift(n)-1)
 ref=r.loc[:'2025-12-31'].dropna()
 recent.append({'sessions':n,'start':str(s.index[-n-1].date()),'end':str(s.index[-1].date()),
  'return_pct':float(r.iloc[-1]),'pre2026_percentile':float(100*(ref<=r.iloc[-1]).mean()),
  'reference_n_overlapping':len(ref),'reference_median_pct':float(ref.median())})
pd.DataFrame(recent).to_csv(HERE/'recent_returns.csv',index=False)

# Every running-high episode, including small declines, then filter by realized depth.
episodes=[]; peak=s.index[0]; high=float(s.iloc[0]);active=None
for dt,px in s.items():
 px=float(px)
 if px>=high:
  if active:
   active['recovery']=str(dt.date());episodes.append(active);active=None
  high=px;peak=dt
 else:
  depth=100*(px/high-1)
  if active is None:
   active={'peak':str(peak.date()),'peak_price':high,'trough':str(dt.date()),'trough_price':px,
    'depth_pct':depth,'first20':None,'first25':None,'recovery':None}
  if depth<active['depth_pct']:
   active.update(trough=str(dt.date()),trough_price=px,depth_pct=depth)
  for level in [20,25]:
   if depth<=-level and active[f'first{level}'] is None:active[f'first{level}']=str(dt.date())
if active:episodes.append(active)
major=[e.copy() for e in episodes if e['depth_pct']<=-20]
for e in major:
 end=pd.Timestamp(e['recovery'] or s.index[-1]);pk=pd.Timestamp(e['peak'])
 e['days_to_trough']=(pd.Timestamp(e['trough'])-pk).days
 e['underwater_calendar_days']=(end-pk).days
 e['censored']=e['recovery'] is None
pd.DataFrame(major).to_csv(HERE/'major_drawdowns.csv',index=False)
forward=[]
for e in major:
 if e['censored']:continue
 for level in [20,25]:
  date=e[f'first{level}']
  if date is None:continue
  i=s.index.get_loc(pd.Timestamp(date))
  row={'peak':e['peak'],'crossing_pct':-level,'date':date,'close':float(s.iloc[i])}
  for n in [21,63,126,252]:
   row[f'fwd{n}_pct']=float(100*(s.iloc[i+n]/s.iloc[i]-1)) if i+n<len(s) else None
  forward.append(row)
pd.DataFrame(forward).to_csv(HERE/'historical_crossing_forward_returns.csv',index=False)

# Same-date observed endpoint pairs, no fill; newer captures supersede older points.
y={}
for label in ['yield_history','yield_newer']:
 for row in json.loads(inputs[label].read_text()):
  try:y[pd.Timestamp(row['date'])]=float(row['value'])
  except ValueError:pass
t=pd.read_csv(inputs['treasury']);t.Date=pd.to_datetime(t.Date)
for _,row in t.iterrows():
 if pd.notna(row['10 YR']):y[row.Date]=float(row['10 YR'])
ys=pd.Series(y).sort_index(); ys.name='real10y'
pairs=pd.concat([s.rename('GLD'),ys],axis=1,join='inner').dropna()
pairs['gld_return_pct']=pairs.GLD.pct_change(fill_method=None)*100
pairs['yield_change_bp']=pairs.real10y.diff()*100
pairs.to_csv(HERE/'same_endpoint_rate_pairs.csv')
rate=[]
for label,a,b in [('2010-2015','2010-01-01','2015-12-31'),('2016-2019','2016-01-01','2019-12-31'),
 ('2020-2022','2020-01-01','2022-12-31'),('2023-2025','2023-01-01','2025-12-31'),
 ('2026 YTD','2026-01-01','2026-10-22')]:
 q=pairs.loc[a:b,['gld_return_pct','yield_change_bp']].dropna()
 beta=float(q.cov().iloc[0,1]/q.yield_change_bp.var()); corr=float(q.corr().iloc[0,1])
 rate.append({'period':label,'n_pairs':len(q),'beta_pct_per_bp':beta,'correlation':corr,'r_squared':corr*corr})
q=pairs[['gld_return_pct','yield_change_bp']].dropna().tail(120)
beta=float(q.cov().iloc[0,1]/q.yield_change_bp.var());corr=float(q.corr().iloc[0,1])
rate.append({'period':f'last120 through {q.index[-1].date()}','n_pairs':len(q),
 'beta_pct_per_bp':beta,'correlation':corr,'r_squared':corr*corr})
pd.DataFrame(rate).to_csv(HERE/'rate_relationship_by_era.csv',index=False)
relief=pairs.loc['2026-10-09':'2026-10-22']
relief_stats={'start':str(relief.index[0].date()),'end':str(relief.index[-1].date()),
 'gld_return_pct':float(100*(relief.GLD.iloc[-1]/relief.GLD.iloc[0]-1)),
 'real_yield_change_bp':float(100*(relief.real10y.iloc[-1]-relief.real10y.iloc[0]))}
annual=s.resample('YE').last();annual_table=100*annual.pct_change(fill_method=None)
annual_table.index=annual_table.index.year
annual_table.to_csv(HERE/'annual_returns.csv',header=['return_pct'])
anchor={}
for year in [2022,2023,2024,2025]:
 a=s.loc[f'{year}-01-01':f'{year}-12-31']
 anchor[f'since_{year}_lastclose_pct']=float(100*(s.iloc[-1]/a.iloc[-1]-1))
holdings=[]
for label,a,b in [('2008','2008-03-17','2008-11-12'),('2011–2015','2011-08-22','2015-12-17'),
                  ('2020–2022','2020-08-06','2022-09-26'),('2026 ongoing','2026-01-29','2026-10-22')]:
 start=float(d.loc[a,'Tonnes of Gold']);end=float(d.loc[b,'Tonnes of Gold'])
 holdings.append(dict(episode=label,start=a,end=b,tonnes_start=start,tonnes_end=end,
                      change_tonnes=end-start,change_pct=100*(end/start-1)))
pd.DataFrame(holdings).to_csv(HERE/'issuer_holdings_context.csv',index=False)
supplementary={}
for a,b in [('2020-03-09','2020-03-19'),('2025-12-31','2026-01-29'),('2026-08-31','2026-10-23')]:
 supplementary[a+' to '+b]=float(100*(s.loc[b]/s.loc[a]-1))
supplementary['now_vs_july16_low_pct']=float(100*(s.iloc[-1]/s.loc['2026-07-16']-1))
supplementary['oct22_vs_july16_tonnes']=float(d.loc['2026-10-22','Tonnes of Gold'])-float(d.loc['2026-07-16','Tonnes of Gold'])
low22=s.loc['2022'].idxmin();peakdt=s.idxmax()
summary={'endpoint':str(s.index[-1].date()),'close':float(s.iloc[-1]),'issuer_endpoint':str(d.index[-1].date()),
 'primary_rows':len(d),'excluded_holidays_or_missing':int(raw.close.isna().sum()),
 'appended_mirror_rows':len(append),'overlap_n':len(overlap),'overlap_max_error':err,
 'peak':str(peakdt.date()),'peak_price':float(s.max()),'current_drawdown_pct':float(dd.iloc[-1]),
 'recovery_required_pct':float(100*(s.max()/s.iloc[-1]-1)),
 'pre2026_underwater_deeper_fraction_pct':float(100*(dd.loc[:'2025-12-31']<=dd.iloc[-1]).mean()),
 'low2022_date':str(low22.date()),'low2022_price':float(s.loc[low22]),
 'low2022_to_peak_pct':float(100*(s.max()/s.loc[low22]-1)),
 'low2022_to_now_pct':float(100*(s.iloc[-1]/s.loc[low22]-1)),
 'cagr_full_history_pct':float(100*((s.iloc[-1]/s.iloc[0])**(365.25/(s.index[-1]-s.index[0]).days)-1)),
 'drawdown_episode_count20':len(major),'completed_episode_count20':sum(not e['censored'] for e in major),
 'relief_window':relief_stats,'calendar_anchors':anchor,'supplementary_descriptive_context':supplementary,
 'sources':{k:{'path':str(v.relative_to(DESK)),'sha256':hashlib.sha256(v.read_bytes()).hexdigest()} for k,v in inputs.items()}}
(HERE/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
for label,obj in [('SUMMARY',summary),('RECENT',recent),('EPISODES',major),('FORWARD',forward),('RATES',rate)]:
 print(label,json.dumps(obj,indent=2))
