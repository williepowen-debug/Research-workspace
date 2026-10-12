from pathlib import Path
import json,zipfile,pandas as pd
p=Path(__file__).resolve().parent
with zipfile.ZipFile(p/'scf2025-extract.zip') as z: d=pd.read_csv(z.open('SCFP2025.csv'))
d.columns=d.columns.str.upper();w=d.WGT
for name in ['LATE','LATE60']:
 debt=d.HDEBT==1
 print(name,'all',100*(d[name]*w).sum()/w.sum(),'debtors',100*(d.loc[debt,name]*w[debt]).sum()/w[debt].sum())
for c,g in d.groupby('NINCCAT'):
 print('usual-income',c,100*(g.LATE*g.WGT).sum()/g.WGT.sum(),100*(g.LATE60*g.WGT).sum()/g.WGT.sum())
x=pd.read_excel(p/'census-benches26.xlsx',sheet_name='2026',header=None)
levels={k:[float(x.iloc[i,j]) for j in [7,8,9]] for k,i in [('total',71),('auto',78),('building',84),('gas',91),('restaurants',108),('nonstore',105)]}
levels['control']=[levels['total'][i]-sum(levels[k][i] for k in ['auto','building','gas','restaurants']) for i in range(3)]
for k,v in levels.items():print(k,v,'augMOM',100*(v[2]/v[1]-1))
slist=['RSDBS','CUSR0000SAF11','RSFSDP','CUSR0000SEFV','RSGMS','RSXFS','RSCCAS','CPIAPPSL']
data={s:{r['date']:float(r['value']) for r in json.loads((p/('fred-'+s+'.json')).read_text())['observations'] if r['value']!='.'} for s in slist}
for date in ['2026-07-01','2026-08-01']:
 year='2025'+date[4:]
 for s,price in [('RSDBS','CUSR0000SAF11'),('RSFSDP','CUSR0000SEFV'),('RSCCAS','CPIAPPSL')]:print(date,s,100*((data[s][date]/data[s][year])/(data[price][date]/data[price][year])-1))
 print('GMshare',100*data['RSGMS'][year]/data['RSXFS'][year],100*data['RSGMS'][date]/data['RSXFS'][date])
