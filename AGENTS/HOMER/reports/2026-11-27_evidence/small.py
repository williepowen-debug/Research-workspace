import json,sys,os
base=sys.argv[1]
def load(D): return {r['data']['CERT']:r['data'] for r in json.load(open(os.path.join(base,f'all_{D}.json')))['data']}
q3,q2=load('20260930'),load('20260630')
def v(r,k):
    x=r.get(k) if r else 0; return x if isinstance(x,(int,float)) else 0
g=[(c,r) for c,r in q3.items() if c!=29566 and v(r,'ASSET')<10e6 and c in q2]
def d(c,r,k): return v(r,k)-v(q2[c],k)
for k in ['P3REMULT','NAREMULT','P9REMULT']:
    tot=sum(d(c,r,k) for c,r in g)
    s=sorted(g,key=lambda x:-d(x[0],x[1],k))
    top5=sum(d(c,r,k) for c,r in s[:5])
    print(k,'same-bank <$10B net change $M',round(tot/1e3,1),' top5',round(top5/1e3,1),' rest',round((tot-top5)/1e3,1),' top5 names:',[(r['NAME'][:22],round(d(c,r,k)/1e3,1)) for c,r in s[:5]])
gg=[(c,r) for c,r in g if v(r,'LNREMULT')>=50000 and v(q2[c],'LNREMULT')>0]
def rate(r): return (v(r,'P3REMULT')+v(r,'P9REMULT')+v(r,'NAREMULT'))/v(r,'LNREMULT')
up=sum(1 for c,r in gg if rate(r)>rate(q2[c])+1e-12); dn=sum(1 for c,r in gg if rate(r)<rate(q2[c])-1e-12)
print(f'<$10B banks with MF>=$50M n={len(gg)}: PDNA ratio up {up}, down {dn}, flat {len(gg)-up-dn}')
