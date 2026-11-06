import pandas as pd, numpy as np, sys
sp=sys.argv[1]
def s(n,col='CLOSE'):
    d=pd.read_csv(f'{sp}/cboe/{n}.csv'); d.columns=[c.strip().upper() for c in d.columns]
    d['DATE']=pd.to_datetime(d['DATE']); d=d.set_index('DATE')
    return d[col if col in d else d.columns[-1]].astype(float)
v=s('VIX');v3=s('VIX3M');vv=s('VVIX');sk=s('SKEW');o=s('OVX');c=s('COR1M')
print('n vix',len(v),v.index[-1].date())
r=v.pct_change().dropna()
print('rank +%',r.iloc[-1]*100,(r>=r.iloc[-1]).sum(),len(r)); print(r.sort_values().tail(4))
x=(v3/v).dropna(); print('ratio',round(x.iloc[-1],4),'n',len(x),'<=',(x<=x.iloc[-1]).sum()); 
print('prev inverted',x[x<1].index[-2].date(), 'prev lower', x[(x<=x.iloc[-1])].index[-2].date(), x[(x<=x.iloc[-1])].iloc[-2])
print('vvix>120 prev',vv[vv>120].index[-2].date(),vv[vv>120].iloc[-2],'vvix>=134.99 prev',vv[vv>=134.99].index[-2:], vv[vv>=134.99].iloc[-2:].values, 'd/d',(vv.iloc[-1]/vv.iloc[-2]-1)*100)
print('vix>=28.18 prev',v[v>=28.18].index[-2].date(),v[v>=28.18].iloc[-2])
print('skew',sk.tail(6).to_dict()); print('20d',round(sk.tail(20).mean(),2),'prior20',round(sk.iloc[-21:-1].mean(),2),'5dchg',sk.iloc[-1]-sk.iloc[-6],'pct all',round((sk<=sk.iloc[-1]).mean()*100,1),'pct1y',round((sk.tail(252)<=sk.iloc[-1]).mean()*100,1))
print('ovx',o.iloc[-1],'ratio',round(o.iloc[-1]/v.iloc[-1],3))
print('cor1m',c.iloc[-1],(c.iloc[-1]/c.iloc[-2]-1)*100)
hy=pd.read_csv('AGENTS/VIOLET/workbook/fred_cache/BAMLH0A0HYM2_2024-10-01.csv');hy.columns=['d','v'];hy['d']=pd.to_datetime(hy['d']);hy=hy.dropna().set_index('d')['v']*100
print(hy.tail(8).round(0).to_dict()); print('hy>=348 prev',hy[hy>=348].index[-2:] ,hy[hy>=348].iloc[-2:].values); dd=hy.diff(); print('1d>=16 prev',dd[dd>=15.5].tail(5).round(1).to_dict())
