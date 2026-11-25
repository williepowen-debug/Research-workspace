import yfinance as yf, pandas as pd, numpy as np
s=yf.download('^GSPC',start='1989-01-01',end='2026-11-26',auto_adjust=False,progress=False)['Close'].squeeze()
v=yf.download('^VIX',start='1989-01-01',end='2026-11-26',auto_adjust=False,progress=False)['Close'].squeeze()
print('last',s.index[-1].date(),s.iloc[-1], 'vix',v.iloc[-1])
print('200d',round(s.iloc[-200:].mean(),2),'50d',round(s.iloc[-50:].mean(),2),'20d',round(s.iloc[-20:].mean(),2))
df=pd.concat([s.rename('s'),v.rename('v')],axis=1).dropna()
pk=df.s.cummax(); dd=df.s/pk-1
fut=pd.concat([df.s.shift(-k) for k in range(1,8)],axis=1).min(axis=1)/df.s-1
r5=df.s/df.s.shift(3)-1
def rate(mask,thr,name):
    m=mask & fut.notna()
    idx=np.where(m)[0]; keep=[];last=-99
    for i in idx:
        if i-last>=5: keep.append(i); last=i
    x=fut.iloc[keep]
    print(f'{name}: n={len(x)} P(min next7 <= {thr:.2%}) = {(x<=thr).mean():.0%}')
base=(df.v.between(23,30)) & (dd.between(-0.12,-0.06))
rate(base,-0.0228,'retest 7037 | VIX23-30 & dd 6-12%')
rate(base,-0.0696,'<=6700 | VIX23-30 & dd 6-12%')
b2=base & (r5>0.01)  # rebounding 3-session
rate(b2,-0.0228,'retest | same & 3-session change >+1%')
rate(b2,-0.0696,'<=6700 | same & 3-session >+1%')
