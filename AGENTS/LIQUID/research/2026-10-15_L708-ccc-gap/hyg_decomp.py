import json, collections
P='/tmp/claude-1000/-home-willi-Research-workspace-PROME/16d245b5-0cb3-4174-b43d-e76c4903c384/scratchpad/l708/'
d=json.load(open(P+'hyg_holdings.json'))
def key(r): return (r['Name'],r['Maturity'],r['Coupon (%)'])
f=lambda x: float(x.replace(',','')) if x not in ('--','') else None
a={key(r):r for r in d['h13'] if r['Asset Class']=='Fixed Income'}; b={key(r):r for r in d['h14'] if r['Asset Class']=='Fixed Income'}
rows=[]
for k in a:
    if k not in b: continue
    p0,p1,w,y0=f(a[k]['Price']),f(b[k]['Price']),f(a[k]['Weight (%)']),f(a[k]['Yield to Worst (%)'])
    if None in (p0,p1,w,y0) or not p0: continue
    rows.append(dict(name=k[0],mat=k[1],cpn=k[2],sector=a[k]['Sector'],w=w,p0=p0,p1=p1,r=(p1/p0-1)*100,y0=y0,y1=f(b[k]['Yield to Worst (%)'])))
tw=sum(r['w'] for r in rows); tot=sum(r['w']*r['r'] for r in rows)/100
print(f'n={len(rows)} weight {tw:.2f}%  price-only contribution {tot:.4f}% of fund (excl. accrual)')
for lab,cond in (('YTW>=12% sleeve (distressed proxy)',lambda r:r['y0']>=12),('YTW 9-12%',lambda r:9<=r['y0']<12),('YTW<9%',lambda r:r['y0']<9)):
    s=[r for r in rows if cond(r)]; sw=sum(r['w'] for r in s); c=sum(r['w']*r['r'] for r in s)/100
    print(f'{lab}: n={len(s)} weight {sw:.2f}% contribution {c:.4f}%  ({100*c/tot:.0f}% of total) wavg ret {100*c/sw:.2f}%')
s=[r for r in rows if r['y0']>=12]
sec=collections.defaultdict(lambda:[0,0,0])
for r in s: sec[r['sector']][0]+=r['w']; sec[r['sector']][1]+=r['w']*r['r']/100; sec[r['sector']][2]+=1
c12=sum(v[1] for v in sec.values())
print('YTW>=12% sleeve by sector (contribution, share of sleeve loss):')
for k,v in sorted(sec.items(), key=lambda kv: kv[1][1]):
    print(f'  {k:28s} n={v[2]:3d} w={v[0]:.2f}% contrib={v[1]:+.4f}% share={100*v[1]/c12:5.0f}% wavg ret={100*v[1]/v[0]:+.2f}%')
iss=collections.defaultdict(lambda:[0,0])
for r in s: iss[r['name']][0]+=r['w']; iss[r['name']][1]+=r['w']*r['r']/100
top=sorted(iss.items(), key=lambda kv: kv[1][1])[:8]
print('YTW>=12% sleeve top issuers by loss contribution:')
cum=0
for k,v in top:
    cum+=v[1]; print(f'  {k:40s} w={v[0]:.3f}% contrib={v[1]:+.4f}% share={100*v[1]/c12:4.0f}% cum={100*cum/c12:4.0f}%')
