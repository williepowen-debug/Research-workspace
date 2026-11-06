import sys;sys.path.insert(0,__import__('os').path.dirname(__file__))
from lib import *
import bisect,statistics as st
ho={i:load(f'EER_EPD2F_PE{i}_Y35NY_DPGd') for i in (1,2,3,4)}
cl={i:load(f'RCLC{i}d') for i in (1,2,3,4)}
for i in (1,4): print('HO',i,min(ho[i]),max(ho[i]),ho[i][max(ho[i])],'CL',max(cl[i]),cl[i][max(cl[i])])
sp=load('EER_EPD2DXL0_PF4_Y35NY_DPGd');gc=load('EER_EPD2DXL0_PF4_RGC_DPGd');w=load('RWTCd');br=load('RBRTEd')
print('NYH ULSD spot',min(sp),max(sp),[(str(k),sp[k]) for k in sorted(sp)[-6:]]);print('USGC',[(str(k),gc[k]) for k in sorted(gc)[-3:]]);print('WTI spot',[(str(k),w[k]) for k in sorted(w)[-3:]]);print('Brent',[(str(k),br[k]) for k in sorted(br)[-3:]])
crack={k:ho[1][k]*42-cl[1][k] for k in ho[1] if k in cl[1]}
sprd={k:ho[1][k]-ho[4][k] for k in ho[1] if k in ho[4]}
pct={k:sprd[k]/ho[1][k]*100 for k in sprd}
cs={k:(ho[1][k]-ho[4][k])*42-(cl[1][k]-cl[4][k]) for k in sprd if k in cl[1] and k in cl[4]}
def rank(d,x):
    v=sorted(d.values());return round(bisect.bisect_left(v,x)/len(v)*100,1),len(v)
today=dict(crack=4.3105*42-90.45,sp=4.3105-4.0230,pc=(4.3105-4.0230)/4.3105*100,cs=(4.3105-4.0230)*42-(90.45-85.65))
print(today)
print('rank crack',rank(crack,today['crack']),'max',max(crack.items(),key=lambda x:x[1]))
print('rank spread $',rank(sprd,today['sp']),'max',max(sprd.items(),key=lambda x:x[1]))
print('rank spread %',rank(pct,today['pc']),'max',max(pct.items(),key=lambda x:x[1]))
print('rank crack slope',rank(cs,today['cs']),'max',max(cs.items(),key=lambda x:x[1]))
for a,b,l in [(dt.date(2003,2,10),dt.date(2003,3,21),'2003'),(dt.date(2022,4,20),dt.date(2022,5,31),'2022spr'),(dt.date(2022,10,10),dt.date(2022,11,10),'2022oct'),(dt.date(2008,6,1),dt.date(2008,7,15),'2008'),(dt.date(2000,1,15),dt.date(2000,2,15),'2000')]:
    k=[x for x in crack if a<=x<=b]
    if k: print(l,'crack mean',round(st.mean(crack[x] for x in k),2),'max',round(max(crack[x] for x in k),2),'spread1-4 mean',round(st.mean(sprd[x] for x in k if x in sprd),3),'max',round(max(sprd[x] for x in k if x in sprd),3),'% mean',round(st.mean(pct[x] for x in k if x in pct),1),'max',round(max(pct[x] for x in k if x in pct),1),'slope mean',round(st.mean(cs[x] for x in k if x in cs),1))
# spot crack over time including 2026
sc={k:sp[k]*42-w[k] for k in sp if k in w}
print('spot NYH-WTI latest',[(str(k),round(sc[k],2)) for k in sorted(sc)[-5:]],'rank',rank(sc,sc[max(sc)]),'max',max(sc.items(),key=lambda x:x[1]))
print('2026 monthly mean spot crack',{m:round(st.mean(v for k,v in sc.items() if k.year==2026 and k.month==m),1) for m in range(1,12) if any(k.year==2026 and k.month==m for k in sc)})
print('USGC minus NYH c/gal last',[(str(k),round((sp[k]-gc[k])*100,1)) for k in sorted(gc)[-5:] if k in sp])
print('10/30, 10/23 spot crack',[(str(k),round(sc[k],2)) for k in sorted(sc) if k>=dt.date(2026,10,14)])
