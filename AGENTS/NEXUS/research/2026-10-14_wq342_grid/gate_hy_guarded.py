# HY W15/±10/k3 with a guarded DOWN branch: DOWN fires on the first cell that completes a 3-run <= L-10
# AND has CCC <= CCC at L. UP unchanged. Reports gate sets + robustness, and leg-2's own base rate (gate (e)).
import csv, os, sys
D0=os.path.join(os.path.dirname(os.path.abspath(__file__)),'gate')
def load(s): return {d:round(float(v)*100) for d,v in csv.reader(open(os.path.join(D0,s+'.csv')))}
S=['BAMLH0A0HYM2','BAMLH0A2HYB','BAMLH0A3HYC','BAMLH0A1HYBB','BAMLC0A0CM']
ser={s:load(s) for s in S}
dates=sorted(set.intersection(*[set(v) for v in ser.values()]))
keep=[dates[0]]
for i in range(1,len(dates)):
    if not all(ser[s][dates[i]]==ser[s][dates[i-1]] for s in S): keep.append(dates[i])
dates=keep
hy=[ser['BAMLH0A0HYM2'][d] for d in dates]; ccc=[ser['BAMLH0A3HYC'][d] for d in dates]
W,D,k=[int(a) for a in sys.argv[1:4]] if len(sys.argv)>3 else (15,10,3)
def grade(i):
    L=hy[i]; C0=ccc[i]; up=dn=0
    for j in range(i+1,i+1+W):
        up=up+1 if hy[j]>=L+D else 0; dn=dn+1 if hy[j]<=L-D else 0
        if up>=k: return 'UP'
        if dn>=k and ccc[j]<=C0: return 'DN'
    return 'NV'
def leg2(i):   # gate (e): leg 2 base rate = share of windows in which some cell has CCC <= CCC at L
    return any(ccc[j]<=ccc[i] for j in range(i+1,i+1+W))
def rates(st):
    st=[i for i in st if i+W<len(hy)]; n=len(st); r={'UP':0,'DN':0,'NV':0}
    for i in st: r[grade(i)]+=1
    u,d,nv=r['UP']/n,r['DN']/n,r['NV']/n; ratio=max(u,d)/min(u,d) if min(u,d)>0 else float('inf')
    ok=u>=.1 and d>=.1 and ratio<=3 and nv<=.6
    l2=sum(leg2(i) for i in st)/n
    return f"n={n:4d} UP {u*100:5.1f} DN {d*100:5.1f} NV {nv*100:5.1f} ratio {ratio:5.2f} {'PASS' if ok else 'fail'} | leg-2 alone {l2*100:5.1f}%"
live=dates.index('2026-07-27'); allst=list(range(len(hy))); reg=[i for i in allst if ccc[i]>=1000]
t=next(i for i,d in enumerate(dates) if d>='2025-10-14')
print(f"HY W{W} ±{D} k{k}, DOWN guarded by CCC<=CCC(L)")
for nm,st in [('unconditional',allst),('non-overlapping',allst[::W]),('regime CCC>=1000',reg),('regime ex-live',[i for i in reg if i<live]),('live only',[i for i in reg if i>=live]),('trailing year',[i for i in allst if i>=t])]:
    print(f" {nm:17s}", rates(st))
