import csv, sys, os
from decimal import Decimal
D0=os.path.join(os.path.dirname(os.path.abspath(__file__)),'gate')
def load(s):
    out={}
    for d,v in csv.reader(open(os.path.join(D0,s+'.csv'))):
        out[d]=int(Decimal(v)*100)   # published decimal parsed exactly into bp
    return out
ser={s:load(s) for s in ['BAMLH0A0HYM2','BAMLH0A2HYB','BAMLH0A3HYC','BAMLH0A1HYBB','BAMLC0A0CM']}
dates=sorted(set.intersection(*[set(v) for v in ser.values()]))
# drop carry-forward cells: every series identical to prior cell (bond-holiday signature)
keep=[dates[0]]; dropped=[]
for i in range(1,len(dates)):
    if all(ser[s][dates[i]]==ser[s][dates[i-1]] for s in ser): dropped.append(dates[i])
    else: keep.append(dates[i])
print("sessions",len(dates),"carry-forward dropped",len(dropped),dropped[:12])
dates=keep
def grade(x,i,W,D,k):
    L=x[i]; up=dn=0
    for j in range(i+1,min(i+1+W,len(x))):
        up=up+1 if x[j]>=L+D else 0
        dn=dn+1 if x[j]<=L-D else 0
        if up>=k: return 'UP'
        if dn>=k: return 'DN'
    return 'NV'
def rates(x,starts,W,D,k):
    r={'UP':0,'DN':0,'NV':0}; n=0
    for i in starts:
        if i+W>=len(x): continue
        r[grade(x,i,W,D,k)]+=1; n+=1
    if n==0: return None
    u,dn,nv=r['UP']/n,r['DN']/n,r['NV']/n
    ratio=(max(u,dn)/min(u,dn)) if min(u,dn)>0 else float('inf')
    ok=(u>=.10 and dn>=.10 and ratio<=3 and nv<=.60)
    return n,u,dn,nv,ratio,ok
ccc=[ser['BAMLH0A3HYC'][d] for d in dates]
target=sys.argv[1]; k=int(sys.argv[2]) if len(sys.argv)>2 else 5
x=[ser[target][d] for d in dates]
Ws=[10,15,21,25,30]; Ds=[int(v) for v in (sys.argv[3].split(',') if len(sys.argv)>3 else '10,15,20,25,30,40,50'.split(','))]
allst=list(range(len(x))); reg=[i for i in allst if ccc[i]>=1000]
print(f"{target} k={k}  n_sessions={len(x)}  regime(CCC>=1000) starts={len(reg)}  last={dates[-1]} {x[-1]}bp")
print("W  D  | uncond n UP DN NV ratio ok | regime n UP DN NV ratio ok | BOTH")
for W in Ws:
    for D in Ds:
        a=rates(x,allst,W,D,k); b=rates(x,reg,W,D,k)
        if not a or not b: continue
        both=a[5] and b[5]
        print(f"{W:2d} {D:3d} | {a[0]:4d} {a[1]*100:5.1f} {a[2]*100:5.1f} {a[3]*100:5.1f} {a[4]:5.2f} {'Y' if a[5] else '-'} | {b[0]:4d} {b[1]*100:5.1f} {b[2]*100:5.1f} {b[3]*100:5.1f} {b[4]:5.2f} {'Y' if b[5] else '-'} | {'⭐' if both else ''}")
