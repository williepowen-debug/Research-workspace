import pandas as pd, numpy as np
from load import *; from holdings import *
close,div,spl,adj=panel()
u8,v8,na8=nport(); u10,v10,na10=invesco()
BASE=pd.Timestamp('2026-08-03'); END=pd.Timestamp('2026-10-30'); SW=pd.Timestamp('2026-09-18')
P=close[TK]; Dv=div[TK]
def units_for(dates, switch=SW, pre=None, post=None):
    pre=u8 if pre is None else pre; post=u10 if post is None else post
    # units held at close of t-1 determine return on t
    U=pd.DataFrame([ (pre if d<=switch else post) for d in dates], index=dates)
    return U
def port_returns(names, switch=SW, start=None, end=END, pre=None, post=None):
    idx=P.index; dates=idx[(idx>=(start or idx[0]))&(idx<=end)]
    U=units_for(dates,switch,pre,post)[names]
    mv_prev=(U.shift(0)*P.loc[dates,names]).sum(1)   # value at close d with units held at close d
    out={}
    for k in range(1,len(dates)):
        d0,d1=dates[k-1],dates[k]; u=U.loc[d0]
        out[d1]=(u*(P.loc[d1,names]+Dv.loc[d1,names])).sum()/(u*P.loc[d0,names]).sum()-1
    return pd.Series(out)
def weights_prev(names, switch=SW, start=None, end=END):
    idx=P.index; dates=idx[(idx>=(start or idx[0]))&(idx<=end)]
    U=units_for(dates,switch)[names]
    W=(U*P.loc[dates,names]); W=W.div(W.sum(1),axis=0)
    return W.shift(1).iloc[1:]   # weight at close t-1 applying to return t
def stock_tr():
    return ((P+Dv)/P.shift(1)-1)
def cum(r,a=None,b=None):
    r=r.loc[(r.index>(a or r.index[0]-pd.Timedelta(days=1)))&(r.index<=(b or r.index[-1]))]
    return (1+r).prod()-1
