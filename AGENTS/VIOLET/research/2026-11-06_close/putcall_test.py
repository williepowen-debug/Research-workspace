import csv,datetime,json
def dd(s): return datetime.datetime.strptime(s,'%m/%d/%Y').date()
pc={}
for l in open('equitypc.csv'):
    p=[x.strip() for x in l.split(',')]
    try:
        d=dd(p[0]); pc[d]=float(p[4])
    except Exception: pass
for l in open('pc2.tsv'):
    a,b=l.split('\t'); pc[datetime.date.fromisoformat(a)]=float(b)
for r in csv.DictReader(open('pc.tsv'),delimiter='\t'):
    pc[datetime.date.fromisoformat(r['date'])]=float(r['equity'])
pc={k:v for k,v in pc.items() if v>0.05}
spx=[(dd(r['DATE']),float(r['SPX'])) for r in csv.DictReader(open('spx.csv'))]
ix={d:i for i,(d,_) in enumerate(spx)}
ds=[d for d in sorted(pc) if d in ix and d>=datetime.date(2012,6,11)]
print('sessions',len(ds),ds[0],ds[-1],'missing vs SPX',sum(1 for d,_ in spx if ds[0]<=d<=ds[-1] and d not in pc))
vals=[pc[d] for d in ds]
for v in (.89,.85,1.0,1.02): print('>=',v,sum(x>=v for x in vals))
print('rank .89 full', sum(x>=.89 for x in vals),'of',len(vals), 'pctile',round(100*sum(x<.89 for x in vals)/len(vals),1))
jumps=sorted(((pc[b]-pc[a],b,pc[a],pc[b]) for a,b in zip(ds,ds[1:])),reverse=True)[:12]
print('jumps',[(round(j,2),str(b),x,y) for j,b,x,y in jumps])
def stats(ev,label):
    out=[]
    for d in ev:
        i=ix[d]
        if i+20>=len(spx): out.append((d,pc[d],None)); continue
        c=spx[i][1]; f=[x for _,x in spx[i+1:i+21]]
        m=min(f); out.append((d,pc[d],round(100*(m/c-1),2),f.index(m)+1,round(100*(f[-1]/c-1),2),round(100*(f[4]/c-1),2)))
    done=[x for x in out if x[2] is not None]
    n=len(done)
    if n:
        lower=sum(1 for x in done if x[2]<-1)
        import statistics as s
        print(label,'n',n,'further close-low worse than -1% in 20s',lower,'median min%',s.median(x[2] for x in done),'median 20s ret',s.median(x[4] for x in done),'up20',sum(x[4]>0 for x in done),'median 5s',s.median(x[5] for x in done))
    return out
def episodes(th,gap=20):
    ev=[];last=None
    for k,d in enumerate(ds):
        if pc[d]>=th and (last is None or k-last>gap):
            ev.append(d); last=k
    return ev
for th in (1.0,.89,.85):
    o=stats(episodes(th),f'first>={th} gap20')
    if th>=.89:
        for x in o: print('  ',x)
base=[d for d in ds]
stats(base,'all sessions')
# 2024+ only for the >=.85 band, recent regime
