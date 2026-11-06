import sys,os,json;sys.path.insert(0,os.path.dirname(__file__))
from lib import *
import statistics as st,bisect
S=load('WDISTUS1w');U=load('WDIUPUS2w')
ho={i:load(f'EER_EPD2F_PE{i}_Y35NY_DPGd') for i in (1,4)};cl={i:load(f'RCLC{i}d') for i in (1,4)}
d=sorted(U);cov={}
for i in range(3,len(d)):
    k=d[i]
    if k in S: cov[k]=S[k]/(sum(U[x] for x in d[i-3:i+1])/4)
def on(dct,day):
    while day not in dct:
        day-=dt.timedelta(days=1)
        if day<min(dct): return None
    return dct[day]
try:
    import yfinance as yf
    px={}
    for s in ['VLO','MPC','PSX','SPY']:
        h=yf.Ticker(s).history(period='max',interval='1d',auto_adjust=True)
        px[s]={i.date():float(x.Close) for i,x in h.iterrows()}
except Exception as e:
    px={};print('yf fail',e)
def stats(t):
    out={}
    out['stock']=S[t];out['cov']=round(cov[t],1)
    h0=on(ho[1],t);c0=on(cl[1],t);h4=on(ho[4],t);out['HO']=h0;out['crack']=round(h0*42-c0,1) if h0 and c0 else None;out['sp14']=round(h0-h4,3) if h4 else None
    for w in (4,8):
        f=t+dt.timedelta(weeks=w)
        if f>max(ho[1]): continue
        h=on(ho[1],f);c=on(cl[1],f)
        out[f'HO{w}%']=round((h/h0-1)*100,1);out[f'crk{w}']=round(h*42-c-(h0*42-c0),1)
        sw=min(S,key=lambda x:abs((x-f).days));out[f'st{w}']=round((S[sw]-S[t])/1000,1)
        if 'VLO' in px and t>=min(px['VLO']):
            v=on(px['VLO'],f)/on(px['VLO'],t)-1;s=on(px['SPY'],f)/on(px['SPY'],t)-1
            out[f'VLO{w}%']=round(v*100,1);out[f'VLOxSPY{w}']=round((v-s)*100,1)
    return out
# Rule: first week cover <= T with at least 26 weeks since previous qualifying week
for T in (26.0,27.0):
    ep=[];last=None
    for k in sorted(cov):
        if k>=dt.date(2026,1,1): break
        if cov[k]<=T:
            if last is None or (k-last).days>=182: ep.append(k)
            last=k
    print('RULE cover<=',T,'n',len(ep),[str(x) for x in ep])
    for e in ep: print('  ',e,stats(e))
# named dates
print('NAMED')
for t in [dt.date(2003,1,31),dt.date(2003,2,21),dt.date(2000,1,28),dt.date(2022,5,6),dt.date(2022,10,14),dt.date(2022,10,28),dt.date(2022,11,4)]:
    t=min(cov,key=lambda x:abs((x-t).days));print(t,stats(t))
# autumn set: Sep 15-Dec 15 first weeks that are the lowest cover for that week-of-year so far
print('SEASON low-cover list Oct 15-Nov 15, cover<=28.5')
for y in range(1991,2026):
    w=[k for k in cov if k.year==y and dt.date(y,10,20)<=k<=dt.date(y,11,10)]
    if w:
        k=min(w,key=lambda x:abs((x-dt.date(y,10,30)).days))
        if cov[k]<=28.5: print(y,k,stats(k))
# cover vs front spread: weeks with cover <=26, spread % distribution
sp={k:(ho[1][k]-ho[4][k])/ho[1][k]*100 for k in ho[1] if k in ho[4]}
lo=[on(sp,k) for k in cov if cov[k]<=26 and k<dt.date(2024,4,6) and k>=min(sp)]
lo=[x for x in lo if x is not None]
hi=[on(sp,k) for k in cov if 26<cov[k]<=32 and dt.date(1994,2,1)<=k<dt.date(2024,4,6)]
print('spread % when cover<=26 n',len(lo),'median',round(st.median(lo),1),'p25',round(sorted(lo)[len(lo)//4],1),'p75',round(sorted(lo)[3*len(lo)//4],1),'share below 6.67',round(sum(1 for x in lo if x<6.67)/len(lo)*100))
print('spread % cover 26-32 median',round(st.median(hi),1))
sd={k:ho[1][k]-ho[4][k] for k in sp}
ld=[on(sd,k) for k in cov if cov[k]<=26 and dt.date(1994,2,1)<=k<dt.date(2024,4,6)]
print('spread $ cover<=26 median',round(st.median(ld),3),'share below .2875',round(sum(1 for x in ld if x<.2875)/len(ld)*100))
# recent 2022 only weeks cover<=27
w=[k for k in cov if k.year==2022 and cov[k]<=27.5];print('2022 low weeks',[(str(k),round(cov[k],1),round(on(sd,k),2),round(on(sp,k),1)) for k in w])
# seasonal product supplied
wk=sorted(U)
ch=[]
for y in range(2013,2026):
    a=min(wk,key=lambda x:abs((x-dt.date(y,10,30)).days));i=wk.index(a)
    pre=st.mean(U[x] for x in wk[i-3:i+1]);post=st.mean(U[x] for x in wk[i+1:i+8]);ch.append((y,round(pre),round(post),round(post-pre)))
print('PS seasonal',ch,'mean',round(st.mean(c[3] for c in ch)))
j=json.load(open(os.path.dirname(__file__)+'/raw/curve_1106.json'))
print(j['HOZ26.NYM']['daily']);print(j['CLZ26.NYM']['daily'])
print('MEDIANS rule n=10')
ep=[dt.date(*x) for x in [(1994,2,4),(1996,2,16),(2000,2,4),(2001,3,30),(2003,2,7),(2004,2,6),(2005,2,11),(2008,4,4),(2022,3,4),(2022,10,14)]]
R=[stats(e) for e in ep]
for f in ['HO4%','HO8%','crk4','crk8','st4','st8','VLO4%','VLO8%','VLOxSPY4','VLOxSPY8']:
    x=[r[f] for r in R if f in r];print(f,'n',len(x),'median',round(st.median(x),1),'min',min(x),'max',max(x),'up',sum(1 for y in x if y>0))
print('MEDIANS rule n=17 (cover<=27, 2025-07-04 has no forward data)')
ep=[dt.date(*x) for x in [(1993,3,26),(1994,2,4),(1996,2,9),(1997,4,4),(2000,2,4),(2001,1,12),(2003,1,31),(2004,2,6),(2005,2,4),(2007,2,23),(2008,2,29),(2013,11,15),(2019,11,15),(2022,2,4),(2022,10,7),(2023,5,19)]]
R=[stats(e) for e in ep]
for f in ['HO4%','HO8%','crk4','crk8','st8','VLOxSPY4','VLOxSPY8']:
    x=[r[f] for r in R if f in r];print(f,'n',len(x),'median',round(st.median(x),1),'min',min(x),'max',max(x),'up',sum(1 for y in x if y>0))
