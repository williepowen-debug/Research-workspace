"""L334 predictive leg. Does a desk's unconsumed INFO backlog at the start of a week predict a correction in the next 14 days?
Unit: desk-week, Mondays 2026-09-14 to 2026-10-19. Backlog: INFO handoffs delivered at least 2 days before the Monday, not yet removed from
AGENTS/<desk>/inbox/WALTER/ top level by git history at that Monday. Pull-complete desks excluded (no INFO handoffs).
Outcomes in the following 14 days, CORRECTIONS.tsv rows only, ALL rows excluded:
 Y1 desk named in targets (exposure). Y2 desk is corrector (its own figure corrected). Y3 Y1 with direction WEAKEN or FLIP.
Test: within-desk (each desk's weeks demeaned) correlation, permutation of weeks within desk, 10,000 draws."""
import csv,re,subprocess,json,random,statistics as st,collections,datetime as dt
ROOT='/home/willi/Research-workspace'
rows=list(csv.DictReader(open(f'{ROOT}/AGENTS/WALTER/routed/delivery_log.tsv',encoding='utf-8'),delimiter='\t'))
info=[r for r in rows if r['role']=='INFO' and r['timestamp_routed']>='2026-08-20' and r['timestamp_routed']<='2026-10-20T00:00:00Z' and '/inbox/WALTER/' in r.get('handoff_path','')]
out=subprocess.run(['git','log','--since=2026-08-15','--until=2026-11-06','--format=C %ct','--name-status','-M','--diff-filter=DR','--','AGENTS/*/inbox/WALTER/*.md','AGENTS/*/inbox/WALTER/**'],cwd=ROOT,capture_output=True,text=True).stdout
removed={};ct=None
for l in out.splitlines():
    if l.startswith('C '): ct=int(l[2:]);continue
    p=l.split('\t')
    if len(p)>=2 and p[0][:1] in 'DR':
        o=p[1]
        if re.match(r'AGENTS/[A-Z]+/inbox/WALTER/[^/]+$',o): removed[o]=min(ct,removed.get(o,ct)) if False else ct if o not in removed or ct<removed[o] else removed[o]
def ts(s): return dt.datetime.fromisoformat(s.replace('Z','+00:00'))
mons=[dt.datetime(2026,9,14,tzinfo=dt.timezone.utc)+dt.timedelta(days=7*i) for i in range(6)]
cor=[]
for l in open(f'{ROOT}/AGENTS/WALTER/registry/CORRECTIONS.tsv',encoding='utf-8'):
    if l.startswith('#') or l.startswith('correction_id'): continue
    c=l.rstrip('\n').split('\t')
    if len(c)>=9: cor.append(dict(id=c[0],date=c[1],corrector=c[2],targets=c[3],direction=c[8]))
desks=sorted({r['recipient'] for r in info}-{'CARL','RED','PROME','TERRY'})
panel=[]
for d in desks:
    for m in mons:
        back=[];cut=m-dt.timedelta(days=2)
        for r in info:
            if r['recipient']!=d: continue
            t=ts(r['timestamp_routed'])
            if t>cut: continue
            rm=removed.get(r['handoff_path'])
            if rm is None or rm>m.timestamp(): back.append((m-t).days)
        end=(m+dt.timedelta(days=14)).date().isoformat();st_=m.date().isoformat()
        w=[c for c in cor if st_<=c['date']<end]
        t1=[c for c in w if c['targets']!='ALL' and d in c['targets'].split(',')]
        panel.append(dict(desk=d,week=st_,n=len(back),age=(st.mean(back) if back else 0),y1=len(t1),y2=sum(c['corrector']==d for c in w),y3=sum(c['direction'] in('WEAKEN','FLIP') for c in t1)))
def corr(x,y):
    if len(x)<3 or st.pstdev(x)==0 or st.pstdev(y)==0: return None
    return st.correlation(x,y)
def within(xk,yk,draws=10000,seed=7):
    by=collections.defaultdict(list)
    for p in panel: by[p['desk']].append(p)
    by={k:v for k,v in by.items() if max(q[xk] for q in v)>0}
    def stat(xs):
        X=[];Y=[]
        for k,v in by.items():
            mx=st.mean(a for a in xs[k]);my=st.mean(q[yk] for q in v)
            X+=[a-mx for a in xs[k]];Y+=[q[yk]-my for q in v]
        return corr(X,Y)
    xs={k:[q[xk] for q in v] for k,v in by.items()}
    obs=stat(xs); rnd=random.Random(seed);g=0;n=0
    for _ in range(draws):
        ys={k:rnd.sample(a,len(a)) for k,a in xs.items()}
        s=stat(ys)
        if s is None: continue
        n+=1;g+=abs(s)>=abs(obs)
    return dict(r=obs and round(obs,3),p=round(g/n,4) if n else None,desks=len(by),n=sum(len(v) for v in by.values()))
res={'desk_weeks':len(panel),'desks':len(desks),'mondays':[m.date().isoformat() for m in mons],'corrections_in_scope':sum('2026-09-14'<=c['date']<'2026-11-02' for c in cor),'removed_paths':len(removed),'info_rows':len(info),
 'mean_backlog':round(st.mean(p['n'] for p in panel),1),'max_backlog':max(p['n'] for p in panel)}
for x in('n','age'):
    for y in('y1','y2','y3'):
        res[f'{x}->{y}']=within(x,y)
q=sorted(p['n'] for p in panel);hi=q[int(.75*len(q))];lo=q[int(.25*len(q))]
for y in('y1','y2','y3'):
    res[f'top_vs_bottom_{y}']=dict(hi_cut=hi,lo_cut=lo,hi=round(st.mean(p[y] for p in panel if p['n']>=hi),3),lo=round(st.mean(p[y] for p in panel if p['n']<=lo),3),hi_share=round(st.mean(p[y]>0 for p in panel if p['n']>=hi),3),lo_share=round(st.mean(p[y]>0 for p in panel if p['n']<=lo),3))
N=res['n->y1']['n']; res['detectable_r_80pct_power_alpha05']=round(2.8/((N-res['n->y1']['desks'])**.5),3)
json.dump(res,open(f'{ROOT}/AGENTS/WALTER/research/2026-11-05_L334/results.json','w'),indent=1)
csv.DictWriter(open(f'{ROOT}/AGENTS/WALTER/research/2026-11-05_L334/panel.tsv','w'),fieldnames=list(panel[0]),delimiter='\t').writeheader()
w=csv.DictWriter(open(f'{ROOT}/AGENTS/WALTER/research/2026-11-05_L334/panel.tsv','a'),fieldnames=list(panel[0]),delimiter='\t');w.writerows(panel)
print(json.dumps(res,indent=0)); 
ag=collections.defaultdict(list)
for p in panel: ag[p['desk']].append(p['n'])
print(sorted(((k,max(v),round(st.mean(v),1)) for k,v in ag.items()),key=lambda x:-x[2])[:12])
