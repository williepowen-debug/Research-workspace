import yfinance as yf,pandas as pd,datetime as dt
tk={'Dec26':'ZQZ26.CBT','Jan27':'ZQF27.CBT','Feb27':'ZQG27.CBT','Oct27':'ZQV27.CBT'}
d=100-yf.download(list(tk.values()),period='1mo',interval='1d',progress=False,auto_adjust=False)['Close'][list(tk.values())]; d.columns=list(tk)
E=3.88
o=pd.DataFrame({'Dec_bp':(d.Dec26-E)*100*31/22}); o['Dec_%']=o.Dec_bp/25*100; o['Oct27_bp']=(d.Oct27-E)*100; o['beyond_Dec_bp']=o.Oct27_bp-o.Dec_bp; o['Jan_bp']=(d.Jan27-E)*100
print(dt.datetime.now().strftime('%H:%M')); print(o.tail(9).round(1)); o.to_csv('raw/strip_table.csv')
