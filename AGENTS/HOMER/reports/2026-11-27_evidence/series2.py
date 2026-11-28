import json,sys,os
base=sys.argv[1]
Ds=['20250930','20251231','20260331','20260630','20260930']
def v(r,k):
    x=r.get(k); return x if isinstance(x,(int,float)) else 0
for lab,cond in [('ex-UF ex-Flagstar',lambda r: r['CERT'] not in (29566,32541)),('ex-UF banks <$10B assets',lambda r: r['CERT']!=29566 and v(r,'ASSET')<10e6),('ex-UF banks >=$10B',lambda r: r['CERT']!=29566 and v(r,'ASSET')>=10e6)]:
    print('==',lab)
    for D in Ds:
        rows=[r['data'] for r in json.load(open(os.path.join(base,f'all_{D}.json')))['data']]
        g=[r for r in rows if cond(r)]
        L=sum(v(r,'LNREMULT') for r in g); p3=sum(v(r,'P3REMULT') for r in g); na=sum(v(r,'NAREMULT') for r in g); p9=sum(v(r,'P9REMULT') for r in g)
        print(D,f"MF {L/1e3:,.0f}  30-89 {100*p3/L:.3f}%  NA {100*na/L:.3f}%  PDNA {100*(p3+p9+na)/L:.3f}%")
