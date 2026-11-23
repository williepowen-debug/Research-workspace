import csv,datetime as D
K={};U={}
for r in list(csv.reader(open('sources/2026-10-31_rhine-long-series/rhine_daily_means_2000-2026.csv')))[1:]:
    d=D.date.fromisoformat(r[0])
    try:
        if int(r[2])>=90:K[d]=float(r[1])
        if int(r[4])>=90:U[d]=float(r[3])
    except ValueError:pass
ds=sorted(set(K)&set(U));F=[ds[i] for i in range(2,len(ds)) if (ds[i]-ds[i-2]).days<=4 and all(K[ds[i-j]]<=40 and U[ds[i-j]]<=180 for j in range(3))]
# episodes: fires separated by >60 d
ep=[];
for f in F:
    if not ep or (f-ep[-1][-1]).days>60:ep.append([f])
    else:ep[-1].append(f)
print('episodes',[(e[0],e[-1],len(e)) for e in ep])
def complete(start,lv,n):
    r=0
    for k in sorted(x for x in K if x>start):
        r=r+1 if K[k]>=lv else 0
        if r==n:return k
for lv in(60,77,100,150):
    for n in(5,10,15):
        out=[]
        # A: every exit call made after any fire day inside an episode, checked for later refire within 60 d
        for e in ep:
            calls=[];i=0;last=e[0]
            while True:
                c=complete(last,lv,n)
                if not c or c.year>e[0].year+1:break
                nx=[f for f in F if f>c and (f-c).days<=60]
                calls.append((str(c),'REFIRE '+str(nx[0]) if nx else 'ok'))
                if not nx:break
                last=nx[0]
            out.append((e[0].year,calls))
        print(lv,n,out)
print('2018 detail: Sep 11 run before first fire?',[f for f in F if f.year==2018][:1])
print('2026 Kaub max between 10/22 and 11/02:',max((K[k],k) for k in K if D.date(2026,10,20)<=k<=D.date(2026,10,31)))
days=[sum(1 for k in K if k.year==y and K[k]<77) for y in range(2000,2026)];print('days <77 per yr mean',sum(days)/26,'median',sorted(days)[13])
