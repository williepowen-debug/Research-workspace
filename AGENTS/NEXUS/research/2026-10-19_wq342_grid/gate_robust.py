import csv, os, sys
from decimal import Decimal
D0=os.path.join(os.path.dirname(os.path.abspath(__file__)),'gate')
def load(s): return {d:int(Decimal(v)*100) for d,v in csv.reader(open(os.path.join(D0,s+'.csv')))}
S=['BAMLH0A0HYM2','BAMLH0A2HYB','BAMLH0A3HYC','BAMLH0A1HYBB','BAMLC0A0CM']
ser={s:load(s) for s in S}
dates=sorted(set.intersection(*[set(v) for v in ser.values()]))
keep=[dates[0]]
for i in range(1,len(dates)):
    if not all(ser[s][dates[i]]==ser[s][dates[i-1]] for s in S): keep.append(dates[i])
dates=keep
ser['CCCmB']={d:ser['BAMLH0A3HYC'][d]-ser['BAMLH0A2HYB'][d] for d in dates}
ccc=[ser['BAMLH0A3HYC'][d] for d in dates]
def grade(x,i,W,D,k):
    L=x[i]; up=dn=0
    for j in range(i+1,i+1+W):
        up=up+1 if x[j]>=L+D else 0; dn=dn+1 if x[j]<=L-D else 0
        if up>=k: return 'UP'
        if dn>=k: return 'DN'
    return 'NV'
def rates(x,starts,W,D,k):
    st=[i for i in starts if i+W<len(x)]; n=len(st)
    if n==0: return "n=0"
    r={'UP':0,'DN':0,'NV':0}
    for i in st: r[grade(x,i,W,D,k)]+=1
    u,dn,nv=r['UP']/n,r['DN']/n,r['NV']/n
    ratio=(max(u,dn)/min(u,dn)) if min(u,dn)>0 else float('inf')
    ok=u>=.10 and dn>=.10 and ratio<=3 and nv<=.60
    return f"n={n:4d} UP {u*100:5.1f} DN {dn*100:5.1f} NV {nv*100:5.1f} ratio {ratio:4.2f} {'PASS' if ok else 'fail'}"
tgt,W,D,k=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
x=[ser[tgt][d] for d in dates]; N=len(x)
live=dates.index('2026-07-27')
allst=list(range(N)); reg=[i for i in allst if ccc[i]>=1000]
print(f"== {tgt} W={W} D=±{D}bp k={k}  (last cell {dates[-1]} = {x[-1]}bp)")
print(" unconditional           ", rates(x,allst,W,D,k))
print(" uncond non-overlapping  ", rates(x,allst[::W],W,D,k))
print(" regime CCC>=1000        ", rates(x,reg,W,D,k))
print(" regime ex-live-episode  ", rates(x,[i for i in reg if i<live],W,D,k))
print(" regime live episode only", rates(x,[i for i in reg if i>=live],W,D,k))
t=dates.index('2025-10-14') if '2025-10-14' in dates else next(i for i,d in enumerate(dates) if d>='2025-10-14')
print(" trailing year starts    ", rates(x,[i for i in allst if i>=t],W,D,k))
