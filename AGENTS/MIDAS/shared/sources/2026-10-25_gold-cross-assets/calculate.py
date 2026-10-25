"""Same-date cross-asset comparison. See METHOD.md; no network or state writes."""
from pathlib import Path
import hashlib,json
import numpy as np
import pandas as pd

HERE=Path(__file__).resolve().parent
DESK=HERE.parents[2]
gold_path=DESK/'gold/sources/2026-10-25_historical-comparison/gold_close_series.csv'
gold=pd.read_csv(gold_path,index_col=0,parse_dates=True).close.rename('GLD')
series={'GLD':gold}; raw={};audit={}
for ticker in ['SPY','IEF','TLT']:
 d=pd.read_csv(HERE/(ticker+'.csv'),index_col=0,parse_dates=True)
 assert d.index.is_unique and d.index.is_monotonic_increasing and (d[['Close','Adj Close']]>0).all().all()
 assert (d['Stock Splits']==0).all(),(ticker,'unexpected split: review basis')
 raw[ticker]=d;series[ticker]=d['Adj Close'].rename(ticker)
 ratio=d['Adj Close']/d.Close
 assert (ratio>0).all() and (ratio<=1.00001).all(),ticker
 audit[ticker]={'rows':len(d),'start':str(d.index[0].date()),'end':str(d.index[-1].date()),
  'adjustment_ratio_min':float(ratio.min()),'adjustment_ratio_max':float(ratio.max()),
  'dividend_rows':int((d.Dividends>0).sum()),'split_rows':int((d['Stock Splits']!=0).sum())}
o=pd.read_excel(HERE/'EIA_WTI_daily.xls',sheet_name='Data 1',header=2)
assert list(o.columns)==['Date','Cushing, OK WTI Spot Price FOB (Dollars per Barrel)']
o.columns=['Date','WTI'];o.Date=pd.to_datetime(o.Date,errors='raise');o.WTI=pd.to_numeric(o.WTI,errors='coerce')
oil=o.dropna().set_index('Date').WTI.sort_index();assert oil.index.is_unique
oil.to_csv(HERE/'EIA_WTI_extracted.csv')
series['WTI']=oil
universe=pd.concat(series.values(),axis=1,sort=True)
panel=universe.dropna().loc[gold.index[0]:gold.index[-1]]
assert panel.index.is_unique and len(panel)>5000
panel.to_csv(HERE/'all_asset_common_panel.csv')
funds=universe[['GLD','SPY','IEF','TLT']].dropna().loc[gold.index[0]:gold.index[-1]]
funds.to_csv(HERE/'funds_common_panel.csv')
last=panel.index[-1];last_fund=funds.index[-1]

def window(df,a,b,label):
 a=pd.Timestamp(a);b=pd.Timestamp(b)
 row={'window':label,'start':str(a.date()),'end':str(b.date()),'status':'OK'}
 if a not in df.index or b not in df.index:
  row['status']='UNAVAILABLE_EXACT_ENDPOINT';return row
 for t in df:
  if t=='WTI' and (df.loc[a,t]<=0 or df.loc[b,t]<=0):row[t]=None
  else:row[t]=float(100*(df.loc[b,t]/df.loc[a,t]-1))
 return row

recent=[]
for n in [5,21,63,126,252]:
 recent.append(window(panel,panel.index[-n-1],last,f'{n} common sessions to {last.date()}'))
recent.append(window(panel,panel.loc[:'2025-12-31'].index[-1],last,'2026 YTD, all-asset common endpoint'))
recent.append(window(panel,'2026-01-29',last,'Since January 29 gold peak, all-asset common endpoint'))
recent.append(window(panel,panel.loc[:'2022-12-31'].index[-1],last,'Since end-2022, all-asset common endpoint'))
pd.DataFrame(recent).to_csv(HERE/'recent_common_returns.csv',index=False)
fundrecent=[]
for n in [1,5,21,63,126,252]:
 fundrecent.append(window(funds,funds.index[-n-1],last_fund,f'{n} trading sessions to {last_fund.date()}'))
fundrecent.append(window(funds,funds.loc[:'2025-12-31'].index[-1],last_fund,'2026 YTD, fund endpoint'))
fundrecent.append(window(funds,'2026-01-29',last_fund,'Since January 29 gold peak, fund endpoint'))
fundrecent.append(window(funds,'2026-10-09','2026-10-22','October real-yield relief, funds only'))
fundrecent.append(window(funds,'2026-10-21','2026-10-22','October 22 liquidation day, funds only'))
pd.DataFrame(fundrecent).to_csv(HERE/'recent_fund_returns.csv',index=False)

# Same exact endpoints as the gold drawdowns; an oil lag is never filled.
episodes=pd.read_csv(DESK/'gold/sources/2026-10-25_historical-comparison/major_drawdowns.csv')
dd=[]
for _,e in episodes.iterrows():
 end=last if e.censored else pd.Timestamp(e.trough)
 r=window(panel,e.peak,end,f'Gold peak {e.peak} to '+('latest common date (ongoing)' if e.censored else 'gold trough'))
 r['censored']=bool(e.censored);dd.append(r)
pd.DataFrame(dd).to_csv(HERE/'gold_drawdown_cross_asset_returns.csv',index=False)

cases=[]
for label,a,b in [('2008 full year','2007-12-31','2008-12-31'),
 ('Initial pandemic cash liquidation','2020-03-09','2020-03-19'),
 ('2020 full year','2019-12-31','2020-12-31'),('2022 rate/inflation shock','2021-12-31','2022-12-30'),
 ('2023-2025 combined','2022-12-30','2025-12-31'),('2026 YTD common','2025-12-31',str(last.date()))]:
 cases.append(window(panel,a,b,label))
pd.DataFrame(cases).to_csv(HERE/'calendar_case_studies.csv',index=False)

# Last shared observed date each completed month; dates are retained explicitly.
completed=panel.loc[panel.index.to_period('M')<last.to_period('M')]
monthly_end=completed.groupby(completed.index.to_period('M')).tail(1)
monthly=monthly_end.pct_change(fill_method=None).dropna()*100
monthly_end.to_csv(HERE/'completed_month_end_common_levels.csv')
monthly.to_csv(HERE/'completed_monthly_returns.csv')
eras=[('All completed months','2004-11-18','2026-09-30'),('2004-2007','2004-11-18','2007-12-31'),
 ('2008-2012','2008-01-01','2012-12-31'),('2013-2019','2013-01-01','2019-12-31'),
 ('2020-2022','2020-01-01','2022-12-31'),('2023-2025','2023-01-01','2025-12-31'),
 ('2026 completed months','2026-01-01','2026-09-30')]
corr=[]
for label,a,b in eras:
 q=monthly.loc[a:b]
 row={'period':label,'n_months':len(q),'first':str(q.index[0].date()),'last':str(q.index[-1].date())}
 for t in ['SPY','IEF','TLT','WTI']:row['GLD_vs_'+t]=float(q.GLD.corr(q[t]))
 row['SPY_vs_IEF']=float(q.SPY.corr(q.IEF));row['SPY_vs_TLT']=float(q.SPY.corr(q.TLT))
 corr.append(row)
pd.DataFrame(corr).to_csv(HERE/'monthly_correlations_by_era.csv',index=False)
dailycorr=[];oil_ex=[]
for t in ['SPY','IEF','TLT','WTI']:
 q=universe[['GLD',t]].dropna().loc[gold.index[0]:gold.index[-1]]
 r=q.pct_change(fill_method=None)*100
 if t=='WTI':
  bad=(q.WTI<=0)|(q.WTI.shift(1)<=0)
  for dt in q.index[bad]:oil_ex.append({'date':str(dt.date()),'value':float(q.loc[dt,'WTI']),
                                      'previous':float(q.WTI.shift(1).loc[dt]),'reason':'nonpositive endpoint'})
  r=r.loc[~bad]
 r=r.dropna()
 for lab,w in [('All history',r),('Pre-2026',r.loc[:'2025-12-31']),('2026 YTD',r.loc['2026']),('Last120 observed pairs',r.tail(120))]:
  dailycorr.append({'asset':t,'period':lab,'n_pairs':len(w),'first':str(w.index[0].date()),
                    'last':str(w.index[-1].date()),'correlation':float(w.GLD.corr(w[t]))})
pd.DataFrame(dailycorr).to_csv(HERE/'daily_pairwise_correlations.csv',index=False)
pd.DataFrame(oil_ex).to_csv(HERE/'oil_daily_return_exclusions.csv',index=False)

r=funds.pct_change(fill_method=None).dropna()*100
cond=[]
for lab,a,b in [('Pre-2026','2004-11-18','2025-12-31'),('2026 YTD','2026-01-01','2026-10-23')]:
 q=r.loc[a:b]
 masks={'SPY down at least1pct':q.SPY<=-1,
        'SPY and IEF both negative':(q.SPY<0)&(q.IEF<0),
        'SPY and TLT both negative':(q.SPY<0)&(q.TLT<0),
        'SPY and IEF both down at least0.5pct':(q.SPY<=-.5)&(q.IEF<=-.5),
        'SPY and TLT both down at least0.5pct':(q.SPY<=-.5)&(q.TLT<=-.5)}
 for name,mask in masks.items():
  w=q.loc[mask];row={'period':lab,'condition':name,'n':len(w)}
  for t in ['GLD','SPY','IEF','TLT']:
   row[t+'_mean_pct']=float(w[t].mean()) if len(w) else None
   row[t+'_positive_fraction']=float((w[t]>0).mean()) if len(w) else None
  cond.append(row)
pd.DataFrame(cond).to_csv(HERE/'conditional_stress_returns.csv',index=False)
surges=[]
for lab,q in [('Pre-2026',monthly.loc[:'2025-12-31']),('2026 completed months',monthly.loc['2026'])]:
 w=q.loc[q.WTI>=10];row={'period':lab,'n_oil_up10_months':len(w),'dates':','.join(str(x.date()) for x in w.index)}
 for t in ['GLD','SPY','IEF','TLT','WTI']:
  row[t+'_mean_pct']=float(w[t].mean()) if len(w) else None
  row[t+'_positive_fraction']=float((w[t]>0).mean()) if len(w) else None
 surges.append(row)
pd.DataFrame(surges).to_csv(HERE/'oil_surge_months.csv',index=False)

# Reconcile vendor total-return proxies with captured issuer market-price disclosures.
verification=[]
official={'IEF':{2022:-15.16,2025:8.03},'TLT':{2022:-31.25,2025:4.25}}
for t,years in official.items():
 for y,value in years.items():
  v=series[t];measured=float(100*(v.loc[:f'{y}-12-31'].iloc[-1]/v.loc[:f'{y-1}-12-31'].iloc[-1]-1))
  delta=measured-value;assert abs(delta)<.04,(t,y,measured,value)
  verification.append({'asset':t,'period':str(y),'vendor_return_pct':measured,'issuer_market_return_pct':value,'difference_pp':delta})
v=series['SPY'];spy_ytd=float(100*(v.loc['2026-09-30']/v.loc[:'2025-12-31'].iloc[-1]-1))
verification.append({'asset':'SPY','period':'2026 through September30','vendor_return_pct':spy_ytd,
                     'issuer_market_return_pct':12.66,'difference_pp':spy_ytd-12.66})
assert abs(spy_ytd-12.66)<.1,spy_ytd
pd.DataFrame(verification).to_csv(HERE/'issuer_return_crosschecks.csv',index=False)

annual=[]
for y in range(2005,2027):
 q=panel.loc[str(y)];prev=panel.loc[:f'{y-1}-12-31']
 if len(q) and len(prev):annual.append(window(panel,prev.index[-1],q.index[-1],str(y)+(' partial' if y==2026 else '')))
pd.DataFrame(annual).to_csv(HERE/'annual_cross_asset_returns.csv',index=False)
growth=[]
for asset in ['GLD','SPY','IEF','TLT']:
 factor=float(panel[asset].iloc[-1]/panel[asset].iloc[0])
 growth.append({'asset':asset,'start':str(panel.index[0].date()),'end':str(last.date()),
                'usd100_growth':100*factor,'cumulative_return_pct':100*(factor-1)})
pd.DataFrame(growth).to_csv(HERE/'full_period_fund_growth.csv',index=False)
# Exploratory sensitivity after the prespecified comparisons, not a new signal.
q=funds.pct_change(fill_method=None).dropna().tail(120)
small=q.loc[q.GLD.abs().nsmallest(115).index]
robust={'pearson_last120':float(q.GLD.corr(q.SPY)),
        'rank_correlation_last120':float(q.GLD.rank().corr(q.SPY.rank())),
        'pearson_excluding5_largest_absolute_gold_returns':float(small.GLD.corr(small.SPY)),
        'basis':'exploratory robustness check; no forward performance or threshold claim'}
(HERE/'equity_correlation_sensitivity.json').write_text(json.dumps(robust,indent=2)+'\n')
summary={'gold_end':str(gold.index[-1].date()),'fund_end':str(last_fund.date()),'oil_end':str(oil.index[-1].date()),
 'common_start':str(panel.index[0].date()),'common_end':str(last.date()),'common_daily_levels':len(panel),
 'completed_month_return_n':len(monthly),'monthly_end':str(monthly.index[-1].date()),
 'latest_oil_usd_per_barrel':float(oil.iloc[-1]),'negative_oil_return_exclusions':oil_ex,'fund_adjustment_audit':audit,
 'gold_source_sha256':hashlib.sha256(gold_path.read_bytes()).hexdigest(),
 'limitations':['WTI spot price change is not an investment return','ETF adjusted market returns are not NAV returns',
  'oil daily percentage-return observations with nonpositive endpoints excluded','2026 monthly sample only9 months',
  'historical gold trough endpoints selected retrospectively; no prospective edge','different pairwise daily source frontiers'],
 'source_capture':'access.json'}
(HERE/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
for label,obj in [('SUMMARY',summary),('RECENT_ALL',recent),('RECENT_FUNDS',fundrecent),('CASES',cases),('GOLD_DRAWDOWNS',dd),('MONTH_CORR',corr),('DAILY_CORR',dailycorr),('CONDITIONAL',cond),('OIL_SURGE',surges),('ISSUER_CHECK',verification)]:
 print(label,json.dumps(obj,indent=2))
