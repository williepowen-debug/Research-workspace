import sys,io,contextlib,statistics as st,collections,datetime as dt
sys.path.insert(0,'.')
import grade_auction as g
with contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):
    recs=g.load()
rows=[x for x in recs if not x['tips']]
def pct_bar(term,date):
    b=g.bench(recs,term,False,date,12)
    return b
out=[]
for x in rows:
    if x['term'] not in('3Y','10Y','30Y','3-Year','10-Year','30-Year'): continue
print(sorted({x['term'] for x in rows}))
T=('3-Year','10-Year','30-Year')
by=collections.defaultdict(dict)
for x in rows:
    if x['term'] in T and not x['reopening']:
        k=x['date'][:7]
        b=g.bench(recs,x['term'],False,x['date'],12)
        if not b or b.get('n',0)<12 or b.get('ind_p15') is None and b.get('p15') is None: continue
        bar=b.get('ind_p15',b.get('p15'))
        by[k][x['term']]=(x['date'],round(x['ind'],2),round(bar,2),x['ind']<bar)
tri={k:v for k,v in by.items() if len(v)==3 and any(s in k for s in('-02','-05','-08','-11'))}
print(len(tri))
for k in sorted(tri): print(k,{t[:2]:(v[1],v[2],'FIRE' if v[3] else '') for t,v in tri[k].items()})
n=len(tri); f=sum(any(v[3] for v in q.values()) for q in tri.values()); print('triads',n,'with >=1 fire',f)
for t in T:
    a=[q[t][3] for q in tri.values()]; print(t,sum(a),'of',len(a))
# all prints incl. reopenings at refunding tenors
al=collections.Counter(); fi=collections.Counter()
for x in rows:
    if x['term'] in T:
        b=g.bench(recs,x['term'],False,x['date'],12)
        if b and b.get('n',0)>=12:
            bar=b.get('ind_p15',b.get('p15'))
            if bar is None: continue
            al[(x['term'],x['reopening'])]+=1; fi[(x['term'],x['reopening'])]+= x['ind']<bar
for k in sorted(al): print(k,fi[k],'of',al[k])
