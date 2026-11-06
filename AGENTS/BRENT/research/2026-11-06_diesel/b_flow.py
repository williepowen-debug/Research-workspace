import sys;sys.path.insert(0,__import__('os').path.dirname(__file__))
from lib import *
import statistics as st
S=load('WDISTUS1w');P=load('WDIRPUS2w');I=load('WDIIMUS2w');E=load('WDIEXUS2w');U=load('WDIUPUS2w')
G=load('WGIRIUS2w');UT=load('WPULEUS3w');CI=load('WCRRIUS2w')
wk=sorted(S)
def window(end,n):
    i=wk.index(end);return wk[i-n+1:i+1],wk[i-n]
def bal(end,n):
    w,b=window(end,n)
    d=dict(stock=S[end]-S[b],prod=sum(P[x] for x in w)*7/1000,imp=sum(I[x] for x in w)*7/1000,exp=sum(E[x] for x in w)*7/1000,ps=sum(U[x] for x in w)*7/1000)
    d['resid']=d['stock']/1000-(d['prod']+d['imp']-d['exp']-d['ps'])
    d['stock']/=1000
    return {k:round(v,1) for k,v in d.items()}
end=wk[-1]
def yago(end,y): 
    return min(wk,key=lambda x:abs((x-dt.date(end.year-y,end.month,end.day)).days))
for n in (4,8,13,26,39):
    a=bal(end,n);b=bal(yago(end,1),n)
    five=[bal(yago(end,y),n) for y in range(1,6)]
    f={k:round(st.mean(x[k] for x in five),1) for k in a}
    print(n,'wk 2026',a);print('   2025',b);print('   5yavg',f);print('   vs 2025',{k:round(a[k]-b[k],1) for k in a},' vs 5y',{k:round(a[k]-f[k],1) for k in a})
# since Jan 23 peak
pk=dt.date(2026,1,23);n=wk.index(end)-wk.index(pk);print('since peak weeks',n,bal(end,n),'same wks 2025',bal(yago(end,1),n))
print('refinery last 10: date gross crude util prod yield%')
for k in wk[-10:]:
    print(k,G.get(k),CI.get(k),UT.get(k),P[k],round(P[k]/G[k]*100,1) if k in G else None)
for y in (1,2,3,4,5):
    k=yago(end,y);print(k,G.get(k),UT.get(k),P[k],round(P[k]/G[k]*100,1))
# seasonal: util Sept-Oct vs 5y
for yr in range(2021,2027):
    w=[k for k in wk if k.year==yr and (k.month==10 or (k.month==9 and k.day>7))]
    print(yr,'Sep8-Oct util',round(st.mean(UT[k] for k in w if k in UT),1),'gross',round(st.mean(G[k] for k in w if k in G)),'prod',round(st.mean(P[k] for k in w)))
# seasonal path 10/30 to 12/18
rows=[]
for y in range(2006,2026):
    a=min(wk,key=lambda x:abs((x-dt.date(y,10,30)).days));b=wk[wk.index(a)+7];c=wk[wk.index(a)+1];
    pathmin=min(S[x] for x in wk[wk.index(a)+1:wk.index(a)+8])-S[a]
    rows.append((y,round(S[b]-S[a]),round(pathmin),round(S[c]-S[a]),round(st.mean(UT[x] for x in wk[wk.index(a)+1:wk.index(a)+8]),1)))
print('year,chg to 7wk,min in 7wk,next wk,util next7',rows)
print('mean chg 7wk',round(st.mean(r[1] for r in rows)),'median',st.median(r[1] for r in rows),'next wk mean',round(st.mean(r[3] for r in rows)))
print('last 10y mean',round(st.mean(r[1] for r in rows[-10:])))
# weekly vs monthly
mE=load('MDIEXUS2m');mU=load('MDIUPUS2m');mP=load('MDIRPUS2m');mS=load('MDISTUS1m')
print('monthly latest',max(mE),mE[max(mE)],max(mU),mU[max(mU)],max(mP),mP[max(mP)])
def wmean(d,y,m):
    v=[d[k] for k in d if k.year==y and k.month==m]; return st.mean(v) if v else None
print('month: monthlyExp weeklyExp gap | monthlyPS weeklyPS gap | monthlyProd weeklyProd')
gaps=[];gapu=[]
for k in sorted(mE)[-14:]:
    e=wmean(E,k.year,k.month);u=wmean(U,k.year,k.month);p=wmean(P,k.year,k.month)
    print(k.strftime('%Y-%m'),mE[k],round(e),round(mE[k]-e),'|',mU[k],round(u),round(mU[k]-u),'|',mP.get(k),round(p))
    gaps.append(mE[k]-e);gapu.append(mU[k]-u)
print('mean gap exports',round(st.mean(gaps)),'ps',round(st.mean(gapu)),'last 8 ex',round(st.mean(gaps[-8:])),'ps',round(st.mean(gapu[-8:])))
# PADD
from lib import load as L
names={1:'US',2:'PADD1',3:'1A',4:'1B',5:'1C',6:'PADD2',7:'PADD3',8:'PADD4',9:'PADD5'}
for c,nm in names.items():
    d=L('EPD0_stocks',1,c);e=max(d);ya=yago(e,1);five=st.mean(d[yago(e,y)] for y in range(1,6))
    wago=[d[x] for x in sorted(d)[-5:]]
    low=[x for x in sorted(d) if x<e and d[x]<=d[e]]
    print(nm,e,d[e],'yago',d[ya],round((d[e]/d[ya]-1)*100,1),'5y',round(five),round((d[e]/five-1)*100,1),'4wk chg',d[e]-wago[0],'last<=',low[-1] if low else None)
