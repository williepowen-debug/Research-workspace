import csv,datetime as D,json,statistics as s,sys
K={};U={}
for r in list(csv.reader(open('sources/2026-10-31_rhine-long-series/rhine_daily_means_2000-2026.csv')))[1:]:
    try:
        d=D.date.fromisoformat(r[0])
        if int(r[2])>=90:K[d]=float(r[1])
        if int(r[4])>=90:U[d]=float(r[3])
    except ValueError:pass
ds=sorted(set(K)&set(U));fire=[ds[i] for i in range(2,len(ds)) if all(K[ds[i-j]]<=40 and U[ds[i-j]]<=180 for j in range(3))]
import itertools
def runs(y):
    f=[d for d in fire if d.year==y]
    kd=sorted(k for k in K if f and k>=f[0])
    n=0;done=None
    for k in kd:
        n=n+1 if K[k]>=77 else 0
        if n==10:done=k;break
    after=[d for d in fire if done and done<d<=done+D.timedelta(60)]
    return f[0],f[-1],done,len(after),after[:1]
for y in(2003,2018,2022):print(y,runs(y))
# how often 10 complete days >=77 followed within 60 d by 3-day 40/180 fire, all autumns
n=0;bad=0;r=0;last=None
for k in sorted(K):
    if k.year>2025:break
    r=r+1 if K[k]>=77 else 0
    if r==10 and k.month in(8,9,10,11,12) and (last is None or (k-last).days>30):
        n+=1;last=k
        if any(k<f<=k+D.timedelta(60) for f in fire):bad+=1;print('  refire after',k)
print('Aug-Dec first 10-day runs',n,'refire within 60d',bad)
J=sorted((x['date'][:10],float(x['rate'])) for x in json.load(open(sys.argv[1])) if x.get('rate'))
B={}
for d,v in J:
    dt=D.date.fromisoformat(d);B[(dt.isocalendar()[0],dt.isocalendar()[1])]=v
R={}
for (y,w),v in B.items():
    p=[B[(y-i,w)] for i in range(1,6) if (y-i,w) in B]
    if len(p)==5 and 35<=w<=49:R[(y,w)]=v/s.mean(p)
v=sorted(R.values());print('n autumn weeks',len(v),'q50,75,90',[round(v[int(len(v)*q)],2) for q in(.5,.75,.9)],'now',[(k,round(R[k],2)) for k in sorted(R)[-3:]])
for th in(1.25,1.5,2.0):
    print('ratio>=',th,'years with 3+ straight wks',[y for y in sorted({k[0] for k in R}) if any(all(R.get((y,w+j),0)>=th for j in range(3)) for w in range(35,48))])
