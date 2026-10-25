"""Descriptive diagnostics only. Read METHOD.md; no network or state mutation."""
from pathlib import Path
from io import StringIO
import sys, json, hashlib
import numpy as np
import pandas as pd

P=Path(__file__).resolve().parent
D=P.parents[2]
sys.path.insert(0,str(D))
from cot_gold import extract_gold
END=pd.Timestamp('2026-10-23')

market={}
for symbol in ['GLD','SPY','DX-Y.NYB']:
    raw=json.loads((P/(symbol+'.json')).read_text())['chart']['result'][0]
    dates=pd.to_datetime(raw['timestamp'],unit='s',utc=True).tz_convert('America/New_York').tz_localize(None).normalize()
    q=pd.DataFrame(raw['indicators']['quote'][0],index=dates)
    q['adjclose']=raw['indicators']['adjclose'][0]['adjclose']
    q=q.loc[:END].dropna(subset=['close'])
    assert q.index.is_unique and q.index[-1]==END
    q.to_csv(P/(symbol+'_extracted.csv'))
    market[symbol]=q

issuer=pd.read_excel(P/'GLD_issuer_archive.xlsx',sheet_name='US GLD Historical Archive')
issuer.Date=pd.to_datetime(issuer.Date,format='%d-%b-%Y')
for c in issuer.columns[1:]:issuer[c]=pd.to_numeric(issuer[c],errors='coerce')
issuer=issuer.set_index('Date').sort_index().loc[:END]
assert issuer.index.is_unique
i=issuer.dropna(subset=['Closing Price','Tonnes of Gold'])
g=i['Closing Price'].copy()
v=market['GLD']['close']
common=g.index.intersection(v.index)
maxerr=float((g.loc[common]-v.loc[common]).abs().max())
assert maxerr<.0001,maxerr
g=pd.concat([g,v.loc[v.index>g.index[-1]]])
assert g.index[-1]==END and g.index.is_unique
g.rename('GLD').to_csv(P/'gold_close_series.csv')

price={'date':str(END.date()),'close':float(g.iloc[-1]),'issuer_date':str(i.index[-1].date()),
       'issuer_vendor_overlap_n':len(common),'issuer_vendor_max_error':maxerr,
       'july_low_date':'2026-07-16','july_low':float(g.loc['2026-07-16']),
       'above_july_low_pct':float(100*(g.iloc[-1]/g.loc['2026-07-16']-1))}
for n in [20,50,200]:
    ma=float(g.tail(n).mean())
    price[f'mean{n}']=ma;price[f'vs_mean{n}_pct']=float(100*(g.iloc[-1]/ma-1))
for n in [20,60]:
    a=g.tail(n)
    price[f'low{n}']=float(a.min());price[f'low{n}_date']=str(a.idxmin().date())
    price[f'return{n}_pct']=float(100*(g.iloc[-1]/g.iloc[-n-1]-1))
extrema=[]
for j in range(2,len(g)-2):
    q=g.iloc[j-2:j+3]
    if (q==q.iloc[2]).sum()!=1:continue
    kind='peak' if q.iloc[2]==q.max() else 'trough' if q.iloc[2]==q.min() else None
    if kind and g.index[j]>=pd.Timestamp('2026-07-01'):
        extrema.append({'date':str(g.index[j].date()),'close':float(q.iloc[2]),'type':kind,
                        'confirmed_after':str(g.index[j+2].date())})
pd.DataFrame(extrema).to_csv(P/'confirmed_local_extrema.csv',index=False)
price['recent_local_extrema']=extrema[-8:]

hold=i[['Closing Price','Tonnes of Gold','Total Ounces of Gold in the Trust','Ounces of Gold per Share']].copy()
hold['tonnes_change']=hold['Tonnes of Gold'].diff()
hold['implied_shares_not_issuer_reported']=hold['Total Ounces of Gold in the Trust']/hold['Ounces of Gold per Share']
hold.tail(35).to_csv(P/'issuer_recent_holdings.csv')
holding={'date':str(hold.index[-1].date()),'tonnes':float(hold['Tonnes of Gold'].iloc[-1]),
         'last_day_tonnes_change':float(hold.tonnes_change.iloc[-1]),
         'since_sep30_tonnes':float(hold['Tonnes of Gold'].iloc[-1]-hold.loc['2026-09-30','Tonnes of Gold']),
         'since_july16_tonnes':float(hold['Tonnes of Gold'].iloc[-1]-hold.loc['2026-07-16','Tonnes of Gold'])}
for n in [5,21]:
    holding[f'change{n}_tonnes']=float(hold['Tonnes of Gold'].iloc[-1]-hold['Tonnes of Gold'].iloc[-n-1])
    holding[f'change{n}_start']=str(hold.index[-n-1].date())

# Stored observed history supplies older dates; refreshed Fed H.15 independently checks latest primary values.
prior_path=D/'gold/sources/2026-10-25_historical-comparison/same_endpoint_rate_pairs.csv'
prior=pd.read_csv(prior_path,index_col=0,parse_dates=True)
ys=prior.real10y.copy()
h15=pd.read_html(StringIO((P/'fed_h15.html').read_text()))[0]
labels=h15.iloc[:,0].astype(str)
start=labels[labels.str.contains('Inflation indexed',case=False)].index[0]
end=labels[labels.str.contains('Inflation-indexed long-term',case=False)].index[0]
part=h15.loc[start:end]
row=part[part.iloc[:,0].astype(str).str.fullmatch('10-year')].iloc[0]
fed=[]
for col in h15.columns[1:]:
    dt=pd.to_datetime(col,format='%Y %b %d')
    val=float(row[col]);fed.append({'date':str(dt.date()),'real10y':val})
    if dt in ys.index:assert abs(ys.loc[dt]-val)<1e-9
    ys.loc[dt]=val
ys=ys.sort_index().loc[:END]
pd.DataFrame(fed).to_csv(P/'fed_real10y_extracted.csv',index=False)
full=pd.concat([g,ys.rename('real10y'),market['DX-Y.NYB']['close'].rename('DXY')],axis=1,sort=True)
full.columns=['GLD','real10y','DXY']
matched=full.dropna()
matched.to_csv(P/'matched_financial_conditions.csv')
windows=[]
for name,a,b in [('Oct9_to_latest','2026-10-09',str(matched.index[-1].date()))]+[
    (f'last{n}_matched',str(matched.index[-n-1].date()),str(matched.index[-1].date())) for n in [5,21]]:
    x,y=matched.loc[a],matched.loc[b]
    windows.append({'window':name,'start':a,'end':b,'GLD_pct':float(100*(y.GLD/x.GLD-1)),
                    'real10y_start':float(x.real10y),'real10y_end':float(y.real10y),
                    'real10y_change_bp':float(100*(y.real10y-x.real10y)),
                    'DXY_pct':float(100*(y.DXY/x.DXY-1))})
pd.DataFrame(windows).to_csv(P/'financial_condition_windows.csv',index=False)

# Daily changes only on consecutive actual GLD observations. Missing yield observations stay missing.
daily=full.reindex(g.index)
daily['GLD_return_pct']=daily.GLD.pct_change(fill_method=None)*100
daily['yield_change_bp']=daily.real10y.diff()*100
daily['DXY_return_pct']=daily.DXY.pct_change(fill_method=None)*100
cond=[]
for n in [20,60]:
    q=daily.tail(n)
    for name,mask in [('real_yield_falls',q.yield_change_bp<0),
                      ('yield_and_dollar_fall',(q.yield_change_bp<0)&(q.DXY_return_pct<0))]:
        z=q.loc[mask].dropna(subset=['GLD_return_pct','yield_change_bp','DXY_return_pct'])
        cond.append({'window_sessions':n,'window_start':str(q.index[0].date()),'window_end':str(q.index[-1].date()),
          'condition':name,'n':len(z),'gold_up':int((z.GLD_return_pct>0).sum()),
          'mean_gold_pct':float(z.GLD_return_pct.mean()),'median_gold_pct':float(z.GLD_return_pct.median())})
daily.tail(65).to_csv(P/'daily_financial_responses.csv')
pd.DataFrame(cond).to_csv(P/'conditional_financial_responses.csv',index=False)

cot=extract_gold((P/'cftc_legacy.txt').read_text())
assert cot['report_date']=='2026-10-20',cot
consumed=pd.read_csv(D/'sources/cot_vintages_consumed.tsv',sep='\t',comment='#')
cot['already_consumed']=cot['report_date'] in consumed.iloc[:,0].astype(str).tolist()
cot['previous_nc_long']=245300;cot['previous_nc_short']=37421;cot['previous_oi']=396345
cot['long_change']=cot['nc_long']-cot['previous_nc_long'];cot['short_change']=cot['nc_short']-cot['previous_nc_short']
(P/'cot_verified.json').write_text(json.dumps(cot,indent=2)+'\n')

equity=pd.concat([g.rename('GLD'),market['SPY']['adjclose'].rename('SPY')],axis=1,join='inner').dropna()
er=equity.pct_change(fill_method=None)*100
eq=[]
for n in [20,60]:
    q=er.tail(n)
    for name,mask in [('SPY_down',q.SPY<0),('SPY_down_at_least1pct',q.SPY<=-1)]:
        z=q.loc[mask]
        eq.append({'window_sessions':n,'start':str(q.index[0].date()),'end':str(q.index[-1].date()),
                   'condition':name,'n':len(z),'gold_up':int((z.GLD>0).sum()),
                   'mean_gold_pct':float(z.GLD.mean()),'median_gold_pct':float(z.GLD.median())})
er.tail(65).to_csv(P/'daily_equity_responses.csv')
pd.DataFrame(eq).to_csv(P/'conditional_equity_responses.csv',index=False)

summary={'price':price,'holdings':holding,'financial_windows':windows,'conditional_financial_response':cond,
         'latest_primary_rate_date':max(x['date'] for x in fed),'cot':cot,'equity_response':eq,
         'limitations':['Descriptive unvalidated diagnostics, no calibrated bottom probability.',
         'Latest issuer holdings and refreshed Fed rates end October22; no Friday flow/rate claim.',
         'GLD is one fund; WGC global week ending October16 is lagged and partially reported.',
         'Recent equity and rate subsets are small and overlapping; no causal attribution or option-book P&L.',
         'Implied shares divide two rounded issuer quantities and are not a reported share-count or exact flow.'],
         'dependency':{'path':str(prior_path.relative_to(D)),'sha256':hashlib.sha256(prior_path.read_bytes()).hexdigest()}}
(P/'summary.json').write_text(json.dumps(summary,indent=2,allow_nan=False)+'\n')
print(json.dumps(summary,indent=2,allow_nan=False))
