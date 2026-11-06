import pandas as pd, numpy as np
d=pd.read_csv('raw/intraday_5m.csv',index_col=0,parse_dates=True)
d.index=pd.to_datetime(d.index,utc=True).tz_convert('America/New_York')
print('last bars',d.index[-1])
cols=['^FVX','^TNX','^TYX','ZT=F','ZF=F','ZN=F','ZB=F','ZQZ26.CBT','ZQF27.CBT','ZQH27.CBT','ZQV27.CBT','TLT','HYG','LQD','KRE','SPY','DX-Y.NYB','GC=F']
stamps=['2026-11-05 15:55','2026-11-06 08:25','2026-11-06 08:30','2026-11-06 08:35','2026-11-06 08:45','2026-11-06 09:30','2026-11-06 10:00','2026-11-06 11:00','2026-11-06 12:00','2026-11-06 13:00','2026-11-06 14:00','2026-11-06 15:00']
rows=[]
for s in stamps:
    t=pd.Timestamp(s,tz='America/New_York')
    x=d.loc[:t,cols].ffill().iloc[-1]
    rows.append(x.rename(s[5:]))
r=pd.DataFrame(rows).T
pd.set_option('display.width',260,'display.max_columns',30)
print(r.round(3))
last=d[cols].ffill().iloc[-1]; print(last.round(3))
print(d['^TNX'].dropna().iloc[-3:])
