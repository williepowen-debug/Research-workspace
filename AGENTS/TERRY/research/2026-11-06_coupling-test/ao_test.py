import csv, datetime as dt, statistics as st, json
AO={}
for r in csv.DictReader(open('data/ao.csv')):
    if r['ao_index_cdas'].strip(): AO[dt.date(int(r['year']),int(r['month']),int(r['day']))]=float(r['ao_index_cdas'])
def run5(y,a,b,th=-1.0,n=5):
    d=dt.date(y,*a); e=dt.date(y,*b); c=best=0; first=None
    while d<=e:
        c=c+1 if AO.get(d,99)<=th else 0
        if c>best: best=c
        if c==n and first is None: first=d
        d+=dt.timedelta(1)
    return first,best
# Census Middle Atlantic NJ NY PA, East North Central IL IN MI OH WI (climdiv state codes)
ST={'028':'NJ','030':'NY','036':'PA','011':'IL','012':'IN','020':'MI','033':'OH','047':'WI'}
T={}
for l in open('data/tmpcst.txt'):
    p=l.split(); c=p[0][:3]; y=int(p[0][6:10]); e=p[0][3:6]
    if c in ST and p[0][3:6]!=None:
        T.setdefault(c,{})[y]=[float(x) for x in p[1:13]]
def dj(y):
    v=[]
    for c in ST:
        a=T[c].get(y); b=T[c].get(y+1)
        if not a or not b or a[11]<-90 or b[0]<-90: return None
        v.append((a[11]+b[0])/2)
    return sum(v)/len(v)
yrs=list(range(1950,2026))
X=[(y,dj(y)) for y in yrs if dj(y) is not None]
n=len(X); mx=sum(y for y,_ in X)/n; my=sum(t for _,t in X)/n
b=sum((y-mx)*(t-my) for y,t in X)/sum((y-mx)**2 for y,_ in X)
A={y:t-(my+b*(y-mx)) for y,t in X}
cut=sorted(A.values())[n//3-1]
print(f'Dec+Jan temp years {X[0][0]}-{X[-1][0]} n={n} mean {my:.1f}F trend {b*10:+.2f}F per decade; cold third cut {cut:+.2f}F')
for name,a,bb in [('AEO-14 window 11/07-12/04',(11,7),(12,4)),('card read 11/07-12/02',(11,7),(12,2)),('late 11/20-12/02',(11,20),(12,2))]:
    P=[y for y in yrs if run5(y,a,bb)[0]]; F=[y for y in yrs if not run5(y,a,bb)[0]]
    pa=[A[y] for y in P if y in A]; fa=[A[y] for y in F if y in A]
    pc=sum(v<=cut for v in pa); fc=sum(v<=cut for v in fa)
    print(f'{name}: pass {len(P)}/{len(yrs)} ({len(P)/len(yrs):.0%}). Pass: mean {st.mean(pa):+.2f}F, cold {pc}/{len(pa)} ({pc/len(pa):.0%}). Fail: mean {st.mean(fa):+.2f}F, cold {fc}/{len(fa)} ({fc/len(fa):.0%})')
P=[y for y in yrs if run5(y,(11,7),(12,2))[0]]
json.dump({'pass_card_read':P,'anom':{str(k):round(v,3) for k,v in A.items()},'cold_cut':cut},open('data/ao_pass.json','w'))
print('2025 Dec+Jan row present:',2025 in A,'; 2026 AO last',max(AO))
for th,k in [(-1.0,5),(-1.0,7),(-1.5,5),(-2.0,3),(-1.5,3)]:
    P=[y for y in yrs if run5(y,(11,7),(12,2),th,k)[0]]
    pa=[A[y] for y in P if y in A]; fa=[A[y] for y in yrs if y not in P and y in A]
    print(f' AO<={th} {k}d: pass {len(P)}/76 cold|pass {sum(v<=cut for v in pa)}/{len(pa)} cold|fail {sum(v<=cut for v in fa)}/{len(fa)}')
