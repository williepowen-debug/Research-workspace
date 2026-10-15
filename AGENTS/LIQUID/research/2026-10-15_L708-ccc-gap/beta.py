import json, numpy as np, datetime as dt
P='/tmp/claude-1000/-home-willi-Research-workspace-PROME/16d245b5-0cb3-4174-b43d-e76c4903c384/scratchpad/l708/'
d=json.load(open(P+'fred.json'))
def ser(k):
    return {r['date']:round(float(r['value'])*100) for r in d[k] if r['value'] not in ('.','')}
BB,B,C,HY=ser('BAMLH0A1HYBB'),ser('BAMLH0A2HYB'),ser('BAMLH0A3HYC'),ser('BAMLH0A0HYM2')
# first-published check on window
for k,s in (('BAMLH0A2HYB',B),('BAMLH0A3HYC',C),('BAMLH0A0HYM2',HY),('BAMLH0A1HYBB',BB)):
    fp=d[k+'_fp']; rows=fp['rows']; mism=[r for r in rows if r['value'] not in('.','') and round(float(r['value'])*100)!=s.get(r['date'])]
    print('FP-check',k,'rows',len(rows),'first',rows[0]['date'] if rows else None,'last',rows[-1]['date'] if rows else None,'mismatches',len(mism),mism[:3], 'missing',fp.get('missing'))
dates=sorted(set(B)&set(C)&set(BB)&set(HY))
# carry-forward rows: all four unchanged vs prior
carry=set()
for i in range(1,len(dates)):
    a,b=dates[i-1],dates[i]
    if B[a]==B[b] and C[a]==C[b] and BB[a]==BB[b] and HY[a]==HY[b]: carry.add(b)
print('carry-forward rows (all 4 unchanged):',len(carry),sorted(carry)[-8:])
# build daily changes over non-carry rows: change vs previous non-carry row
eff=[x for x in dates if x not in carry]
rows=[]
for i in range(1,len(eff)):
    a,b=eff[i-1],eff[i]
    rows.append(dict(date=b,prev=a,dB=B[b]-B[a],dC=C[b]-C[a],dBB=BB[b]-BB[a],dHY=HY[b]-HY[a],gap=C[b]-B[b],dgap=(C[b]-B[b])-(C[a]-B[a]),
                     mturn=(b[:7]!=a[:7])))
fit=[r for r in rows if r['date']<='2026-09-23']
x=np.array([r['dB'] for r in fit],float); y=np.array([r['dC'] for r in fit],float)
b0=(x@y)/(x@x); res0=y-b0*x; sd0=res0.std(ddof=1)
X=np.c_[np.ones_like(x),x]; (a1,b1),*_=np.linalg.lstsq(X,y,rcond=None); res1=y-(a1+b1*x); sd1=res1.std(ddof=1)
r2_0=1-(res0@res0)/((y-y.mean())@(y-y.mean())); r2_1=1-(res1@res1)/((y-y.mean())@(y-y.mean()))
print(f'FIT n={len(fit)} {fit[0]["date"]}..{fit[-1]["date"]}  M0 no-int beta={b0:.3f} sd={sd0:.2f} R2={r2_0:.3f} | M1 a={a1:.3f} beta={b1:.3f} sd={sd1:.2f} R2={r2_1:.3f}')
# gap-change base rates
g=np.array([r['dgap'] for r in fit],float)
mt=np.array([r['mturn'] for r in fit]); 
print(f'dgap all: mean {g.mean():.2f} sd {g.std(ddof=1):.2f} n={len(g)} | P(dgap>0)={np.mean(g>0):.3f}')
print(f'dgap month-turn: n={mt.sum()} mean {g[mt].mean():.2f} sd {g[mt].std(ddof=1):.2f} median {np.median(g[mt]):.1f} P(>0)={np.mean(g[mt]>0):.3f} | non-turn mean {g[~mt].mean():.2f} sd {g[~mt].std(ddof=1):.2f}')
print('month-turn dgap list:',[ (r['date'],r['dgap'],r['dC'],r['dB']) for r in fit if r['mturn']])
# residual of month-turns
print(f'M0 resid month-turn mean {res0[mt].mean():.2f} sd {res0[mt].std(ddof=1):.2f} vs non-turn mean {res0[~mt].mean():.2f} sd {res0[~mt].std(ddof=1):.2f}')
def pct(v,arr): return 100*np.mean(arr<=v)
absr=np.abs(res0)
print('\nWINDOW (changes vs previous non-carry published obs; 10/12 carry-forward excluded)')
print('date       prev       dBB  dB  dC  dHY | gap  dgap | exp=b0*dB  excess  pct(signed) pct(|e|) | M1 excess')
win=[r for r in rows if '2026-09-24'<=r['date']<='2026-10-13']
out=[]
for r in win:
    e0=r['dC']-b0*r['dB']; e1=r['dC']-(a1+b1*r['dB'])
    out.append(dict(r,exp=round(b0*r['dB'],1),ex0=round(e0,1),ex1=round(e1,1),p_signed=round(pct(e0,res0)),p_abs=round(pct(abs(e0),absr)),gap_pctile=None))
    print(f"{r['date']} {r['prev']} {r['dBB']:+4d} {r['dB']:+4d} {r['dC']:+4d} {r['dHY']:+4d} | {r['gap']:4d} {r['dgap']:+4d} | {b0*r['dB']:+6.1f} {e0:+7.1f} {pct(e0,res0):6.0f} {pct(abs(e0),absr):6.0f} | {e1:+7.1f}{'  <- month-turn' if r['mturn'] else ''}")
prim=[o for o in out if '2026-10-02'<=o['date']<='2026-10-13']
sec=[o for o in out if '2026-09-25'<=o['date']<='2026-10-01']
for nm,s in (('PRIMARY 10/2-10/13',prim),('SECONDARY 9/25-10/1',sec)):
    print(nm,'n',len(s),'sum dgap',sum(o['dgap'] for o in s),'gap>0 sessions',sum(o['dgap']>0 for o in s),'sum dC',sum(o['dC'] for o in s),'sum dB',sum(o['dB'] for o in s),'sum beta-exp',round(sum(o['exp'] for o in s),1),'sum excess',round(sum(o['ex0'] for o in s),1),'excess>0',sum(o['ex0']>0 for o in s),'excess>=1sd',sum(o['ex0']>=sd0 for o in s))
tot=sum(o['dgap'] for o in out if o['date']>='2026-09-25')
r101=[o for o in out if o['date']=='2026-10-01'][0]
print('total dgap 9/25-10/13',tot,' 10/1 dgap',r101['dgap'],'share',round(100*r101['dgap']/tot,1),'%')
# base rate: excess positive on 7 of 7 consecutive? compute prob in fit history of k-session runs with all excess>0
ex=res0
runs=sum(1 for i in range(len(ex)-6) if all(ex[i:i+7]>0))
print('fit-history 7-session windows with excess>0 on all 7:',runs,'of',len(ex)-6)
gg=g
runs_g=sum(1 for i in range(len(gg)-6) if all(gg[i:i+7]>0))
print('fit-history 7-session windows with dgap>0 on all 7:',runs_g,'of',len(gg)-6)
runs_g12=sum(1 for i in range(len(gg)-11) if all(gg[i:i+12]>0))
print('fit-history 12-session windows with dgap>0 on all 12:',runs_g12,'of',len(gg)-11)
# 12-session gap change percentile
gap_series=[(r['date'],r['gap']) for r in rows]
ch12=[gap_series[i][1]-gap_series[i-12][1] for i in range(12,len(gap_series)) if gap_series[i][0]<='2026-09-23']
lastch=[g for dte,g in gap_series if dte=='2026-10-13'][0]-[g for dte,g in gap_series if dte=='2026-09-24'][0]
print('12-obs gap change 9/24->10/13:',lastch,'pct of fit-history 12-obs changes:',round(pct(lastch,np.array(ch12)),1),'max hist',max(ch12))
json.dump(dict(b0=b0,sd0=sd0,r2_0=r2_0,a1=a1,b1=b1,sd1=sd1,r2_1=r2_1,n=len(fit),win=out),open(P+'beta_out.json','w'),default=str)
