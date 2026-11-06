import sys,statistics as st
sys.path.insert(0,'FORGE/tools/market-data')
import fetch
def s(i,l=1100):
    return {r['date']:float(r['value']) for r in fetch.fred_fetch(i,limit=l)}
hy,bb,ccc,vix=s('BAMLH0A0HYM2'),s('BAMLH0A1HYBB'),s('BAMLH0A3HYC'),s('VIXCLS')
d=sorted(set(hy)&set(bb)&set(ccc))
print('obs',len(d),d[0],d[-1])
r={x:ccc[x]/bb[x] for x in d}
for x in d[-26:]:
    print(x,'HY',round(hy[x]*100),'BB',round(bb[x]*100),'CCC',round(ccc[x]*100),'CCC/BB',round(r[x],2),'VIX',vix.get(x))
# day-on-day
rows=[]
for a,b in zip(d,d[1:]):
    rows.append((b,round((hy[b]-hy[a])*100),r[b]-r[a]))
print('HY d/d +16 or wider, last 3y window n=',len(rows))
w=[x for x in rows if x[1]>=16]
print(len(w),'share',round(len(w)/len(rows)*100,1))
print('last 8:',[(x[0],x[1],round(x[2],2)) for x in w[-8:]])
up=[x for x in rows if x[1]>=10]
print('widening>=10bp days',len(up),'ratio rose on',sum(1 for x in up if x[2]>0),'ratio fell on',sum(1 for x in up if x[2]<0))
all_w=[x for x in rows if x[1]>0]
print('all widening days',len(all_w),'ratio rose on',sum(1 for x in all_w if x[2]>0),'fell',sum(1 for x in all_w if x[2]<0))
tight=[x for x in rows if x[1]<0]
print('tightening days',len(tight),'ratio rose on',sum(1 for x in tight if x[2]>0))
import math
xs=[x[1] for x in rows]; ys=[x[2] for x in rows]
mx,my=st.mean(xs),st.mean(ys)
c=sum((a-mx)*(b-my) for a,b in zip(xs,ys))/math.sqrt(sum((a-mx)**2 for a in xs)*sum((b-my)**2 for b in ys))
print('corr dHY,dRatio',round(c,3))
print('sd d/d HY bp last 250',round(st.pstdev(xs[-250:]),2),'mean',round(st.mean(xs[-250:]),2))
v=sorted(set(vix)); dv=[(b,vix[b]-vix[a]) for a,b in zip(v,v[1:])]
print('VIX obs',len(v),v[0],'top +d:',sorted(dv,key=lambda t:-t[1])[:5])
print('VIX days>=+3',sum(1 for _,x in dv if x>=3))
