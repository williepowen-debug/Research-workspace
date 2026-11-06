import yfinance as yf, pandas as pd, numpy as np
pd.set_option('display.width',220,'display.max_rows',200,'display.max_columns',30)
ET='America/New_York'
# 1) ZQ bars with volume: did trades actually occur before and after 08:30?
for t in ['ZQZ26.CBT','ZQF27.CBT','ZQV27.CBT']:
    h=yf.Ticker(t).history(period='3d',interval='5m',prepost=True,auto_adjust=False)
    h.index=h.index.tz_convert(ET)
    h=h[['Open','High','Low','Close','Volume']]
    w=h.loc['2026-11-05 15:30':'2026-11-06 15:30']
    w=w[w.Volume>0]
    print(t,'bars with volume',len(w),'total vol',int(w.Volume.sum()))
    p=w.loc[:'2026-11-06 08:29']; q=w.loc['2026-11-06 08:30':]
    print(' last trade before 08:30',p.tail(3)[['Close','Volume']].to_string().replace('\n',' | '))
    print(' first after  08:30',q.head(4)[['Close','Volume']].to_string().replace('\n',' | '))
    print(' vol-weighted close, pre 11/06 00:00-08:29:', round((p.loc['2026-11-06 00:00':].Close*p.loc['2026-11-06 00:00':].Volume).sum()/max(1,p.loc['2026-11-06 00:00':].Volume.sum()),4),' post 08:30-15:30:',round((q.Close*q.Volume).sum()/max(1,q.Volume.sum()),4))
# 2) strip daily history
tk={'Nov26':'ZQX26.CBT','Dec26':'ZQZ26.CBT','Jan27':'ZQF27.CBT','Mar27':'ZQH27.CBT','Jun27':'ZQM27.CBT','Oct27':'ZQV27.CBT'}
d=yf.download(list(tk.values()),period='1mo',interval='1d',progress=False,auto_adjust=False)['Close'][list(tk.values())]
d.columns=list(tk); im=100-d
print(im.tail(9).round(3))
im2=im.copy(); im2['DecOdds%']=((im['Dec26']-3.88)*31/22/0.25*100).round(0)
print(im2[['Dec26','Jan27','Oct27','DecOdds%']].tail(9).round(3))
d.to_csv('raw/zq_daily.csv')
