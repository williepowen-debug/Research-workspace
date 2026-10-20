from pathlib import Path
import json,math,hashlib
import pandas as pd,numpy as np
from openpyxl import load_workbook
out=Path(__file__).resolve().parent

def history(name):
 f=pd.read_csv(out/name,index_col=0)
 f.index=pd.to_datetime(f.index,utc=True).tz_convert('America/New_York').tz_localize(None).normalize()
 assert f.index.is_unique and f.index.is_monotonic_increasing
 return f.loc[:'2026-10-19']
gdf=history('GLD.csv'); g=gdf.Close
assert not gdf[['Dividends','Stock Splits','Capital Gains']].fillna(0).to_numpy().any()
dxy=history('DXY.csv').Close

def fred(name):
 data=json.loads((out/(name+'.json')).read_text());assert not any('error' in r for r in data)
 s=pd.Series({pd.Timestamp(r['date']):float(r['value']) for r in data}).sort_index()
 assert s.index.is_unique
 return s

y=fred('DFII10');usd=fred('DTWEXBGS')
gp=pd.Series(g.index,index=g.index).shift(); yp=pd.Series(y.index,index=y.index).shift()
pairs=pd.DataFrame({'ret':g.pct_change(fill_method=None)*100,'dy_bp':(y.diff()*100).round(8),'gld_prior_date':gp,'yield_prior_date':yp}).dropna()
pairs.index.name='date';pairs.to_csv(out/'pairs.csv')
def fit(f):
 x=f.dy_bp.to_numpy();r=f.ret.to_numpy();n=len(x);xc=x-x.mean();rc=r-r.mean();den=xc@xc
 assert den>0
 b=float(xc@rc/den);a=float(r.mean()-b*x.mean());res=r-(a+b*x);sse=float(res@res);sst=float(rc@rc)
 se=math.sqrt(sse/(n-2)/den)
 return {'n':n,'first':str(f.index[0].date()),'last':str(f.index[-1].date()),'intercept_pct':a,'beta_pct_per_bp':b,'se_ordinary':se,'t_ordinary':b/se,'r2':1-sse/sst,'mismatched_start_dates':int((f.gld_prior_date!=f.yield_prior_date).sum())}
fits={str(n):fit(pairs.tail(n)) for n in (20,60,120)}
repro=fit(pairs.loc[:'2026-10-08'].tail(120));assert abs(repro['beta_pct_per_bp']-(-.16322189))<1e-7
same=pairs.loc[pairs.gld_prior_date==pairs.yield_prior_date]
# Compare the identical fixed120-pair perimeter with mismatches excluded, not a selected new horizon.
current120=pairs.tail(120);fit_same=fit(current120.loc[current120.gld_prior_date==current120.yield_prior_date])
common=pairs.index[-1];common_g=g.loc[:common]
windows=[]
for n in (5,20,60):
 start=common_g.index[-n-1];end=common_g.index[-1]
 # Both dates must be observed, with no forward filled yields/dollars.
 if start not in y.index or start not in usd.index:raise ValueError(str(start))
 windows.append({'gld_sessions':n,'start':str(start.date()),'end':str(end.date()),'gld_start':float(g[start]),'gld_end':float(g[end]),'gld_pct':float((g[end]/g[start]-1)*100),'dfii10_start':float(y[start]),'dfii10_end':float(y[end]),'dy_bp':round(float((y[end]-y[start])*100),8),'broad_usd_start':float(usd[start]),'broad_usd_end':float(usd[end]),'broad_usd_pct':float((usd[end]/usd[start]-1)*100),'dxy_start':float(dxy[start]),'dxy_end':float(dxy[end]),'dxy_pct':float((dxy[end]/dxy[start]-1)*100)})
wb=load_workbook(out/'spdr_archive.xlsx',read_only=True,data_only=True)
rows=list(wb['US GLD Historical Archive'].values);a=pd.DataFrame(rows[1:],columns=rows[0]);a['date']=pd.to_datetime(a.Date,format='%d-%b-%Y');a=a.set_index('date').sort_index()
for c in ['Closing Price','Ounces of Gold per Share','Total Ounces of Gold in the Trust','Tonnes of Gold','Total Net Asset Value in the Trust']:a[c]=pd.to_numeric(a[c],errors='coerce')
a=a.dropna(subset=['Tonnes of Gold','Closing Price']);a=a.loc[:'2026-10-19']
comparisons=[]
for date in ['2026-08-31','2026-09-30','2026-10-09','2026-10-16','2026-10-19']:
 r=a.loc[date];comparisons.append({'date':date,'close':float(r['Closing Price']),'tonnes':float(r['Tonnes of Gold']),'ounces':float(r['Total Ounces of Gold in the Trust']),'ounces_per_share':float(r['Ounces of Gold per Share']),'nav_usd':float(r['Total Net Asset Value in the Trust'])})
last=a.iloc[-1];changes=[]
for date in ['2026-08-31','2026-09-30','2026-10-09','2026-10-16']:
 r=a.loc[date];changes.append({'from':date,'through':str(a.index[-1].date()),'tonnes_change':float(last['Tonnes of Gold']-r['Tonnes of Gold']),'close_pct':float((last['Closing Price']/r['Closing Price']-1)*100),'nav_pct':float((last['Total Net Asset Value in the Trust']/r['Total Net Asset Value in the Trust']-1)*100),'metal_per_share_pct':float((last['Ounces of Gold per Share']/r['Ounces of Gold per Share']-1)*100)})
# Ounce-to-tonne reconciliation tolerates published2dp tonnes; no share count inferred.
recent=a.loc['2026-08-31':].copy();err=(recent['Total Ounces of Gold in the Trust']*31.1034768/1e6-recent['Tonnes of Gold']).abs().max();assert math.isfinite(err)
recent.to_csv(out/'issuer_recent.csv')
v=a[['Closing Price']].join(g.rename('vendor_close'),how='inner').loc['2026-08-31':]; maxprice=float((v['Closing Price']-v.vendor_close).abs().max());assert maxprice<.0001
b=fits['120']['beta_pct_per_bp'];anchor=float(last['Closing Price'])
shocks=[{'yield_shock_bp':bp,'associated_gld_pct':b*bp,'illustrative_gld_price':anchor*(1+b*bp/100)} for bp in [-25,-10,10,25]]
# Purely descriptive trading context, no optimized signal threshold.
trend={'close_date':str(g.index[-1].date()),'close':float(g.iloc[-1]),'ma20':float(g.tail(20).mean()),'ma50':float(g.tail(50).mean()),'ma200':float(g.tail(200).mean()),'daily_sigma120_pct':float(pairs.ret.tail(120).std()),'observed_recent20_low_close':float(g.tail(20).min()),'observed_recent20_high_close':float(g.tail(20).max())}
summary={'fit':fits,'reproduce_Oct8':repro,'same_start_in_current120':fit_same,'common_windows':windows,'issuer_points':comparisons,'issuer_changes_to_latest':changes,'issuer_ounce_tonne_max_error_t':float(err),'issuer_ounce_tonne_initial_0_011t_tolerance_pass':bool(err<.011),'issuer_unit_caveat':'Issuer ounces converted at exact troy factor exceed published tonnes by up to0.01325t; initial identity tolerance FAILED, not certified. Preserve both, use reported tonne changes with ounce-derived delta crosscheck; no rounding cause assumed.','issuer_vendor_recent_max_price_error_usd':maxprice,'illustrative_shocks_not_forecasts':shocks,'trend_context_not_new_bands':trend,'asof_common':str(common.date()),'input_hashes':{n:hashlib.sha256((out/n).read_bytes()).hexdigest() for n in ['METHOD.md','GLD.csv','DXY.csv','DFII10.json','DTWEXBGS.json','spdr_archive.xlsx']}}
(out/'summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
