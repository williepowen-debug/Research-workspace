import sys, pandas as pd, numpy as np
sys.path.insert(0,'/home/willi/Research-workspace/FORGE/tools/market-data')
import fetch
def ser(sid,n=3000):
    r=fetch.fred_fetch(sid,limit=n); return pd.Series({pd.Timestamp(x['date']):float(x['value']) for x in r if 'date' in x}).sort_index()
sofr,iorb=ser('SOFR'),ser('IORB')
sp=(sofr-iorb).dropna()*100
w=sp.resample('W-WED').mean()
df=pd.read_pickle('df.pkl'); pc=pd.read_pickle('pc.pkl')
x=pd.DataFrame({'spread':w,'bor':df.b,'pc':pc}).dropna()
x=x.loc['2022-01-01':]
print('weeks',len(x), x.index[0].date(), x.index[-1].date())
print('SOFR-IORB weekly avg, recent:', [(i.date().isoformat(), round(v,1)) for i,v in w.loc['2026-08-26':].items()])
print('corr(level spread, primary credit) since 2024:', round(x.loc['2024':].spread.corr(x.loc['2024':].pc),2))
print('corr(spread change 6w, borrowing % change 6w) since 2024:', round(x.loc['2024':].spread.diff(6).corr(x.loc['2024':].bor.pct_change(6)),2))
print('SOFR-IORB pctile of latest week since 2022:', round((x.spread<x.spread.iloc[-1]).mean()*100))
