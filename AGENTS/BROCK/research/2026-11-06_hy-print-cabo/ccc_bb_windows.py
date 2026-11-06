import sys
sys.path.insert(0,'FORGE/tools/market-data')
import fetch
def s(i,l=1100):
    return {r['date']:float(r['value']) for r in fetch.fred_fetch(i,limit=l)}
hy,bb,ccc,vix=s('BAMLH0A0HYM2'),s('BAMLH0A1HYBB'),s('BAMLH0A3HYC'),s('VIXCLS')
d=sorted(set(hy)&set(bb)&set(ccc)); r={x:ccc[x]/bb[x] for x in d}
print('ratio min/max',min(r.items(),key=lambda t:t[1]),max(r.items(),key=lambda t:t[1]))
print('obs <=5.93',sum(1 for v in r.values() if v<=5.93),'of',len(r))
last=[x for x in d if r[x]<=5.93][-6:]; print('last <=5.93',[(x,round(r[x],2),round(hy[x]*100)) for x in last])
# multi-session windows, non-overlapping and overlapping
for n in (5,10,15,20):
    ov=[(d[i],(hy[d[i]]-hy[d[i-n]])*100,r[d[i]]-r[d[i-n]]) for i in range(n,len(d))]
    w=[x for x in ov if x[1]>=25]
    no=[]; i=n
    while i<len(d):
        dh=(hy[d[i]]-hy[d[i-n]])*100
        if dh>=25:
            no.append((d[i],round(dh),round(r[d[i]]-r[d[i-n]],2))); i+=n
        else: i+=1
    print(n,'sessions, HY>=+25: overlap n',len(w),'ratio up',sum(1 for x in w if x[2]>0),'| nonoverlap n',len(no),'ratio up',sum(1 for x in no if x[2]>0),no[:12])
# row 10 base rate
dd=sorted(set(hy)&set(vix)); 
rows=[(b,vix[b]-vix[a],round((hy[b]-hy[a])*100)) for a,b in zip(dd,dd[1:])]
sp=[x for x in rows if x[1]>=3]
print('VIX>=+3 days in HY window',len(sp),'HY<=0 on',sum(1 for x in sp if x[2]<=0),'HY +1..+5',sum(1 for x in sp if 0<x[2]<=5),'HY>=+6',sum(1 for x in sp if x[2]>5),'median HY',sorted(x[2] for x in sp)[len(sp)//2])
print([ (x[0],round(x[1],2),x[2]) for x in sp if x[2]<=0])
print('5-session 10/29->11/05 HY',round((hy['2026-11-05']-hy['2026-10-29'])*100),'VIX',round(vix['2026-11-05']/vix['2026-10-29']-1,3))
print('ratio 10/28->11/05',round(r['2026-10-28'],3),round(r['2026-11-05'],3),'exact 11/4',round(r['2026-11-04'],3),'exact 11/5',round(r['2026-11-05'],3),'CCC-BB',round((ccc['2026-11-05']-bb['2026-11-05'])*100),round((ccc['2026-11-04']-bb['2026-11-04'])*100))
