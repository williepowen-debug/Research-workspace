import yfinance as yf, pandas as pd
pd.set_option('display.width',200,'display.max_rows',80,'display.max_columns',30)
ET='America/New_York'
T={'ZQZ26.CBT':'ZQZ','ZQF27.CBT':'ZQF','ZQV27.CBT':'ZQV','ZN=F':'ZN','ZB=F':'ZB','ZT=F':'ZT','NQ=F':'NQ','ES=F':'ES'}
out={}
for t,n in T.items():
    h=yf.Ticker(t).history(period='3d',interval='15m',prepost=True,auto_adjust=False)
    h.index=h.index.tz_convert(ET); out[n]=h.Close; out[n+'_v']=h.Volume
d=pd.DataFrame(out).ffill()
w=d.loc['2026-11-05 15:45':'2026-11-06 09:00']
s=w.iloc[::4][['ZQZ','ZQZ_v','ZQF','ZQV','ZT','ZN','ZB','ES','NQ']]
print(s.round(3))
d.to_csv('raw/overnight_15m.csv')
