# Stylized: put the Jan-15 10/12C at each year's Dec-4 with spot scaled to S0, walk UNG's real daily path to Jan-8.
# Black-Scholes, flat IV 70/76 (card screening vols near 72.6 on the long leg), r 4%. Marks, not fills. Not a track record.
import csv, json, datetime as dt, math, statistics as st, re, glob, sys
from math import log,sqrt,erf,exp
from cpc_test import read, MA, EN
N=lambda x:.5*(1+erf(x/sqrt(2)))
def c(S,K,T,v,r=.04):
    if T<=0: return max(S-K,0)
    d1=(log(S/K)+(r+v*v/2)*T)/(v*sqrt(T)); return S*N(d1)-K*exp(-r*T)*N(d1-v*sqrt(T))
sp=lambda S,T:c(S,10,T,.70)-c(S,12,T,.76)
rows=list(csv.reader(open('data/gas_closes.csv')))
hdr=rows[0]; ui=hdr.index('UNG')
px=[(dt.date.fromisoformat(r[0][:10]),float(r[ui])) for r in rows[1:] if r[ui] not in('',)]
A=json.load(open('data/ao_pass.json')); ao=set(A['pass_card_read'])
# last CPC issue on or before Dec 3
last={}
for p in sorted(glob.glob('data/cpc/*.zip')):
    d=re.search(r'(\d{8})',p).group(1)
    if d!='20261105': last[int(d[:4])]=d
lastp={y:read(f'data/cpc/814temp_{d}.zip') for y,d in last.items()}
lv=lambda o:(sum(o[c_][0]=='B' for c_ in MA)>=2 and sum(o[c_][0]=='B' for c_ in EN)>=2)
print('last issue <=12/3 v2 pass:',{y:lv(o) for y,o in lastp.items()})
an={int(k):v for k,v in A['anom'].items()}; cut=A['cold_cut']
P=[y for y in lastp if lv(lastp[y])]; F=[y for y in lastp if not lv(lastp[y])]
print(' pass',len(P),'/',len(lastp),'mean',round(st.mean(an[y] for y in P),2),'cold',sum(an[y]<=cut for y in P),'| fail mean',round(st.mean(an[y] for y in F),2),'cold',sum(an[y]<=cut for y in F),'/',len(F))
print(' last issue pass AND AO run:',[y for y in P if y in ao])
for S0 in (8.5,9.4,10.0):
    out={}
    for y in range(2007,2026):
        path=[(d,p) for d,p in px if dt.date(y,12,4)<=d<=dt.date(y+1,1,8)]
        if len(path)<15 or path[0][0]>dt.date(y,12,9): continue
        b=path[0][1]; exp_d=dt.date(y+1,1,15); v0=sp(S0,(exp_d-path[0][0]).days/365); v=None
        for d,p in path:
            m=sp(S0*p/b,(exp_d-d).days/365)
            if m>=1.00: v=m; break   # harvest at $1.00
        if v is None: v=m           # time stop Jan 8
        out[y]=(v0,v)
    d=[v-v0 for v0,v in out.values()]
    print(f'S0 {S0}: n={len(out)} sell at 12/4 value ${500*st.mean(v0 for v0,_ in out.values()):.0f} x5; hold mean ${500*st.mean(v for _,v in out.values()):.0f}, median ${500*st.median(v for _,v in out.values()):.0f}; hold beat sell {sum(x>0 for x in d)}/{len(d)}; harvested {sum(v>=1 for _,v in out.values())}')
    for nm,Y in (('AO pass',[y for y in out if y in ao]),('AO fail',[y for y in out if y not in ao])):
        print(f'   {nm} n={len(Y)} hold-minus-sell mean ${500*st.mean(out[y][1]-out[y][0] for y in Y):+.0f}')
    if S0==9.4: print('   by year hold-sell $',{y:round(500*(out[y][1]-out[y][0])) for y in out})
