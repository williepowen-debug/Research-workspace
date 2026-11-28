import json,sys,os
base=sys.argv[1]
Ds=['20250630','20250930','20251231','20260331','20260630','20260930']
data={}
for D in Ds:
    rows=[r['data'] for r in json.load(open(os.path.join(base,f'all_{D}.json')))['data']]
    data[D]={r['CERT']:r for r in rows}
def v(r,k): 
    x=r.get(k); return x if isinstance(x,(int,float)) else 0
UF=29566
def tot(D,excl=()):
    s=dict(L=0,P3=0,P9=0,NA=0,NT=0,DR=0,CR=0,n=0)
    for c,r in data[D].items():
        if c in excl: continue
        s['L']+=v(r,'LNREMULT');s['P3']+=v(r,'P3REMULT');s['P9']+=v(r,'P9REMULT');s['NA']+=v(r,'NAREMULT')
        s['NT']+=v(r,'NTREMULT');s['DR']+=v(r,'DRREMULT');s['CR']+=v(r,'CRREMULT')
        if v(r,'LNREMULT')>0: s['n']+=1
    return s
print('$ millions; rates % of MF loans')
for lab,ex in [('ALL',()),('EX-UF',(UF,))]:
    print('==',lab)
    prevYTD=None
    for D in Ds:
        s=tot(D,ex)
        pd=s['P3']+s['P9']+s['NA']
        ytd=s['NT']
        q = ytd if D[4:6]=='03' or prevYTD is None else ytd-prevYTD
        if D[4:6]=='03': q=ytd
        print(D, f"loans {s['L']/1e3:,.0f}  30-89 {s['P3']/1e3:,.0f} ({100*s['P3']/s['L']:.3f})  90+ {s['P9']/1e3:,.0f}  NA {s['NA']/1e3:,.0f} ({100*s['NA']/s['L']:.3f})  PDNA {pd/1e3:,.0f} ({100*pd/s['L']:.3f})  NCO_YTD {ytd/1e3:,.1f}  NCO_Q {q/1e3 if D!='20250630' else float('nan'):,.1f}  banksMF {s['n']}")
        prevYTD=ytd if D[4:6]!='12' else None
