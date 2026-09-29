import pandas as pd, numpy as np
a=pd.read_csv('Apartment_List_Rent_Estimates_2026_09.csv')
print(a.location_type.value_counts()); print(a.bed_size.value_counts())
c=a[(a.location_type=='City')&(a.bed_size=='overall')].copy()
print('cities overall:',len(c))
mc=[x for x in a.columns if x[:2]=='20' and '_' in x]
top=c.nlargest(100,'population')
print(top[['location_name','population']].head(5).to_string(), top.population.min())
v=top[mc].astype(float)
rows=[]
for i,m in enumerate(mc[12:],12):
    y=(v[m]/v[mc[i-12]]-1).dropna()
    rows.append(dict(month=m.replace('_','-'),n=len(y),neg=int((y<0).sum()),pct=100*(y<0).mean(),med=100*y.median()))
r=pd.DataFrame(rows); r.to_csv('al_top100city_neg_series.csv',index=False)
print(r.round(1).to_string(index=False))
