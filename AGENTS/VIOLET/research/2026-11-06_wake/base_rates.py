import pandas as pd, numpy as np, sys
sp=sys.argv[1]
def s(n):
    d=pd.read_csv(f'{sp}/cboe/{n}.csv'); d.columns=[c.strip().upper() for c in d.columns]
    d['DATE']=pd.to_datetime(d['DATE']); d=d.set_index('DATE')
    return d['CLOSE' if 'CLOSE' in d else d.columns[-1]].astype(float)
v=s('VIX');v3=s('VIX3M');vv=s('VVIX');sk=s('SKEW')
df=pd.concat({'v':v,'m':v3},axis=1).dropna(); df['r']=df.m/df.v; inv=df.r<1
# A inversion exit: first inverted close after >=20 non-inverted closes, excl 11/05
idx=[i for i in range(20,len(df)-1) if inv.iloc[i] and not inv.iloc[i-20:i].any()]
print('A episodes (first inverted after 20 clean)',len(idx))
rows=[]
for i in idx:
    fut=df.r.iloc[i+1:i+61]
    ex=np.argmax((fut>=1).values)+1 if (fut>=1).any() else 99
    rows.append((df.index[i].date(),round(df.r.iloc[i],4),round(df.v.iloc[i],2),round(df.v.iloc[i]/df.v.iloc[i-1]-1,3),ex,round(df.r.iloc[i+1],4)))
a=pd.DataFrame(rows,columns='d r vix chg exit next_r'.split()); print(a.to_string())
for lbl,sub in [('all',a),('r<=0.95',a[a.r<=.95]),('r<=0.93',a[a.r<=.93]),('next_r<1',a[a.next_r<1]),('next_r<1 & r<=.95',a[(a.next_r<1)&(a.r<=.95)])]:
    print(lbl,len(sub),'exit<=6 (d+1..d+6)',(sub.exit<=6).sum(),'exit<=11',(sub.exit<=11).sum(),'median',sub.exit.median())
# B VIX >=1.0646x within sessions 1..11 of first inverted close, plus conditional on next-day drop
rows=[]
for i in idx:
    fut=df.v.iloc[i+1:i+12]; 
    rows.append((df.index[i].date(),df.v.iloc[i],df.v.iloc[i+1]/df.v.iloc[i]-1,fut.max()/df.v.iloc[i]-1,(fut.max()/df.v.iloc[i+1]-1)))
b=pd.DataFrame(rows,columns='d vix d1 mx mx_from_d1'.split())
print('B all',len(b),'max>=+6.46%',(b.mx>=.0646).sum())
s2=b[(b.vix>=20)&(b.vix<=38)]; print('vix20-38',len(s2),(s2.mx>=.0646).sum())
s3=b[b.d1<=-.05]; print('d1<=-5%',len(s3),(s3.mx>=.0646).sum()); print(s3.round(3).to_string())
# B2 large spike set: VIX +35%+ 1-day? use 5-day +30% from <20 with inverted close
v5=df.v/df.v.shift(5)-1
big=[i for i in idx if v5.iloc[i]>=.3]; print('inverted first & +30% 5d',len(big),[str(df.index[i].date()) for i in big])
print(' reach',sum(df.v.iloc[i+1:i+12].max()/df.v.iloc[i]-1>=.0646 for i in big))
# C SKEW<140 within 38 sessions, conditional
sd=sk.to_frame('s'); sd['m20']=sd.s.rolling(20).mean(); sd['fmin']=sd.s[::-1].rolling(38).min()[::-1].shift(-1)
c=sd[(sd.s>=145)&(sd.s<=155)&(sd.m20>=150)].dropna()
c0=c[c.index>='2013-01-01']; print('C days',len(c),'hit',(c.fmin<140).mean().round(3),'since2013',len(c0),(c0.fmin<140).mean().round(3))
gap=c0.index.to_series().diff().dt.days>30; ep=c0[gap|(c0.index==c0.index[0])]; print('C episodes',len(ep),(ep.fmin<140).sum()); print(ep[['s','m20','fmin']].round(2).to_string())
print('skew last <140', sk[sk<140].tail(3).to_dict(), 'skew min last 60',sk.tail(60).min(),sk.tail(60).idxmin())
# D VVIX <100 within 11 sessions after first VVIX>=125 close with VVIX<=100 in prior 5
vd=vv.to_frame('x'); 
ix=[i for i in range(30,len(vd)-12) if vd.x.iloc[i]>=125 and vd.x.iloc[i-5:i].min()<=100 and (vd.x.iloc[i-20:i]<125).all()]
rows=[(vd.index[i].date(),vd.x.iloc[i],vd.x.iloc[i+1],vd.x.iloc[i+1:i+12].min(),vd.x.iloc[i+1:i+12].lt(100).any(),vd.x.iloc[i+1:i+20].lt(100).any()) for i in ix]
d=pd.DataFrame(rows,columns='d x next min11 hit11 hit19'.split()); print(d.round(2).to_string()); print('D',len(d),d.hit11.sum(),d.hit19.sum())
