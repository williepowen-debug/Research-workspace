import json,sys,collections
d=[r['data'] for r in json.load(open(sys.argv[1]))['data']]
A={'Brevard','Seminole','Volusia','Lake','Putnam','Flagler'}
N={'Orange','Osceola','St. Johns','Clay','Marion'}
B={'Palm Beach','Broward','Miami-Dade','Martin','St. Lucie','Indian River'}
cnty=collections.Counter(r['CNTYNAMB'] for r in d)
missing=[c for c in A|N|B if c not in cnty]
print('missing county names',missing)
agg=collections.defaultdict(lambda: collections.Counter())
info={}
for r in d:
    c=r['CERT']; info[c]=(r['NAMEFULL'],r['NAMEHCR'],r['STALP'],r['ASSET'])
    v=r['DEPSUMBR'] or 0
    agg[c]['FL']+=v; agg[c]['FLn']+=1
    if r['CNTYNAMB'] in A: agg[c]['A']+=v; agg[c]['An']+=1
    if r['CNTYNAMB'] in N: agg[c]['N']+=v; agg[c]['Nn']+=1
    if r['CNTYNAMB'] in B: agg[c]['B']+=v; agg[c]['Bn']+=1
    if r['CNTYNAMB'] in ('Palm Beach','Broward','Miami-Dade'): agg[c]['SE3']+=v
    if r['CNTYNAMB'] in ('Martin','St. Lucie','Indian River'): agg[c]['TC']+=v
tot=collections.Counter()
for c,a in agg.items():
    for k in a: tot[k]+=a[k]
print('FL total $B',tot['FL']/1e6,'A',tot['A']/1e6,'N',tot['N']/1e6,'B',tot['B']/1e6, 'branches FL',tot['FLn'],'A',tot['An'],'B',tot['Bn'])
json.dump({str(c):[info[c],dict(a)] for c,a in agg.items()},open('agg.json','w'))
rows=sorted(agg.items(),key=lambda x:-(x[1]['A']+x[1]['B']))[:45]
for c,a in rows:
    n=info[c]
    print(f"{c}\t{n[0][:34]:34}\t{n[2]}\tasset${n[3]/1e6:.1f}B\tFL${a['FL']/1e6:.2f}B\tA${a['A']/1e6:.2f}B({a['An']})\tN${a['N']/1e6:.2f}B\tB${a['B']/1e6:.2f}B({a['Bn']})\tSE3${a['SE3']/1e6:.2f}\tTC${a['TC']/1e6:.2f}")
