import json,sys,os
base=sys.argv[1]
def load(D): return {r['data']['CERT']:r['data'] for r in json.load(open(os.path.join(base,f'all_{D}.json')))['data']}
q3,q2,q3p=load('20260930'),load('20260630'),load('20250930')
def v(r,k):
    x=r.get(k) if r else 0; return x if isinstance(x,(int,float)) else 0
def pdna(r): return v(r,'P3REMULT')+v(r,'P9REMULT')+v(r,'NAREMULT')
UF=29566
rows=[]
for c,r in q3.items():
    p=q2.get(c); 
    rows.append((c,r['NAME'][:38],v(r,'ASSET'),v(r,'LNREMULT'),pdna(r),pdna(p),v(r,'NTREMULT')-v(p,'NTREMULT'),v(r,'NAREMULT')-v(p,'NAREMULT')))
tot_d=sum(x[4]-x[5] for x in rows)
print('total dPDNA Q2->Q3 $M',tot_d/1e3, ' (banks present in Q3 only; acquired/failed banks drop out)')
rows.sort(key=lambda x:-(x[4]-x[5]))
print('TOP 12 increases dPDNA ($M): cert name assets$B MFloans$M PDNA_Q3 PDNA_Q2 d  NCO_Q3')
for x in rows[:12]: print(x[0],x[1],f"{x[2]/1e6:.1f}",f"{x[3]/1e3:,.0f}",f"{x[4]/1e3:,.1f}",f"{x[5]/1e3:,.1f}",f"{(x[4]-x[5])/1e3:+,.1f}",f"{x[6]/1e3:,.1f}")
print('TOP 8 decreases')
for x in rows[-8:]: print(x[0],x[1],f"{x[2]/1e6:.1f}",f"{x[3]/1e3:,.0f}",f"{x[4]/1e3:,.1f}",f"{x[5]/1e3:,.1f}",f"{(x[4]-x[5])/1e3:+,.1f}")
ex=[x for x in rows if x[0]!=UF]
inc=sum(x[4]-x[5] for x in ex if x[4]>x[5]); dec=sum(x[4]-x[5] for x in ex if x[4]<x[5])
print('ex-UF gross increases',inc/1e3,'gross decreases',dec/1e3,'net',(inc+dec)/1e3)
top5=sum(x[4]-x[5] for x in ex[:5]); print('ex-UF top5 increases sum',top5/1e3, ' ex-UF ex-top5 net', (inc+dec-top5)/1e3)
# breadth: banks with MF>=$100M
big=[x for x in ex if x[3]>=100000 and q2.get(x[0]) and v(q2[x[0]],'LNREMULT')>0]
up=sum(1 for x in big if x[4]/x[3] > pdna(q2[x[0]])/v(q2[x[0]],'LNREMULT')+1e-12)
dn=sum(1 for x in big if x[4]/x[3] < pdna(q2[x[0]])/v(q2[x[0]],'LNREMULT')-1e-12)
L_up=sum(x[3] for x in big if x[4]/x[3] > pdna(q2[x[0]])/v(q2[x[0]],'LNREMULT')+1e-12)
print(f'breadth (ex-UF banks with MF loans >= $100M, n={len(big)}): PDNA ratio up {up}, down {dn}, flat {len(big)-up-dn}; MF loans at banks up {L_up/sum(x[3] for x in big):.1%}')
# same, YoY
bigy=[x for x in ex if x[3]>=100000 and q3p.get(x[0]) and v(q3p[x[0]],'LNREMULT')>0]
upy=sum(1 for x in bigy if x[4]/x[3] > pdna(q3p[x[0]])/v(q3p[x[0]],'LNREMULT')+1e-12)
dny=sum(1 for x in bigy if x[4]/x[3] < pdna(q3p[x[0]])/v(q3p[x[0]],'LNREMULT')-1e-12)
print(f'breadth YoY (n={len(bigy)}): up {upy}, down {dny}')
# NCO Q3 concentration ex-UF
nco=sorted(ex,key=lambda x:-x[6]); tn=sum(x[6] for x in ex)
print('ex-UF Q3 NCO total',tn/1e3)
for x in nco[:8]: print('  NCO',x[0],x[1],f"{x[6]/1e3:,.1f}")
# size buckets
for lab,lo,hi in [('>=$250B',250e6,1e12),('$100-250B',100e6,250e6),('$10-100B',10e6,100e6),('$1-10B',1e6,10e6),('<$1B',0,1e6)]:
    g=[x for x in ex if lo<=x[2]<hi]
    L=sum(x[3] for x in g); a=sum(x[4] for x in g); b=sum(x[5] for x in g)
    Lp=sum(v(q2.get(x[0]),'LNREMULT') for x in g)
    if L: print(f'{lab}: MF loans {L/1e3:,.0f}  PDNA Q3 {100*a/L:.3f}%  Q2 (same banks) {100*b/Lp:.3f}%  NCO_Q3 {sum(x[6] for x in g)/1e3:,.1f}')
