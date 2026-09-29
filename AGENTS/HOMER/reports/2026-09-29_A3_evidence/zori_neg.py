import pandas as pd, numpy as np
d=pd.read_csv('zori.csv')
d=d[d.RegionType!='country'].copy()
dc=[c for c in d.columns if c[:2]=='20']
v=d[dc].astype(float)
yoy=v.T.pct_change(12, fill_method=None).T   # per-metro yoy
# require both endpoints valid
mask=v.notna() & v.shift(12,axis=1).notna()
yoy=yoy.where(mask)
top=d.index.isin(d.nsmallest(100,"SizeRank").index)
print("top100 SizeRank range:",d[top].SizeRank.min(),d[top].SizeRank.max())
assert top.sum()==100, top.sum()
rows=[]
for c in dc[12:]:
    a=yoy[c].dropna(); t=yoy.loc[top,c].dropna()
    rows.append(dict(month=c[:7], n_all=len(a), pct_all=100*(a<0).mean() if len(a) else np.nan,
                     n_top=len(t), neg_top=int((t<0).sum()), pct_top=100*(t<0).mean() if len(t) else np.nan,
                     med_top=100*t.median(), us=None))
r=pd.DataFrame(rows)
us=pd.read_csv('zori.csv'); us=us[us.RegionType=='country'][dc].astype(float).iloc[0]
usy=(us/us.shift(12)-1)*100
r['us_yoy']=[usy[c] for c in dc[12:]]
r.to_csv('zori_neg_series.csv',index=False)
pd.set_option('display.width',200); pd.set_option('display.max_rows',500)
print(r.round(1).to_string(index=False))
# top100 metros missing data
miss=d.loc[top,['SizeRank','RegionName']][v.loc[top,dc[0]].isna()]
print('top100 lacking 2015-01 value:',len(miss)); print(miss.to_string(index=False))
