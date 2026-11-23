import csv,datetime as D,sys,math
sys.path.insert(0,'../pyl');import numpy as np
L={}
for r in csv.reader(open('gatun.csv')):
    try:L[D.date.fromisoformat(r[0][:10])]=float(r[1])
    except:pass
O={}
for l in open('oni.txt'):
    p=l.split()
    if p and p[0]=='DJF':O[int(p[1])]=float(p[3])
X=[];Y=[];yr=[]
for y in range(1966,2027):
    a=L.get(D.date(y-1,11,22));
    if a is None or y not in O:continue
    mn=min(L[D.date(y,1,1)+D.timedelta(i)] for i in range(120) if D.date(y,1,1)+D.timedelta(i) in L)
    X.append([1,O[y],a,1 if y>=2017 else 0]);Y.append(a-mn);yr.append(y)
X=np.array(X);Y=np.array(Y);print(len(Y),'corr drop-ONI',round(np.corrcoef(X[:,1],Y)[0,1],3),'drop-start',round(np.corrcoef(X[:,2],Y)[0,1],3))
from math import erf
def fit(X,Y,x0,lab):
    b,_,_,_=np.linalg.lstsq(X,Y,rcond=None);r=Y-X@b;n,k=X.shape;s=math.sqrt(r@r/(n-k));se=s*math.sqrt(1+x0@np.linalg.inv(X.T@X)@x0);m=x0@b
    print(lab,'b',b.round(2),'s',round(s,2),'pred drop',round(m,2),'pred min lake',round(86.58-m,2),{lv:round(.5*(1-erf(((86.58-lv)-m)/se/math.sqrt(2))),2) for lv in(83.5,83.18,83,82.66,82.14)})
for o in(2.0,2.5):
    fit(X,Y,np.array([1,o,86.58,1]),f'ONI {o} +start+post')
m=[i for i in range(len(yr)) if 1]
fit(X[:,:3],Y,np.array([1,2.5,86.58]),'ONI2.5 +start')
near=[(yr[i],X[i,2],round(86.58-0-0+0,0) and round(Y[i],2),X[i,1]) for i in range(len(yr)) if abs(X[i,2]-86.58)<=.75]
print('near starts',near)
print('near starts count drop>=3.58',sum(a[2]>=3.58 for a in near),'of',len(near))
print('ONI>=1.0',[(yr[i],X[i,1],X[i,2],round(Y[i],2)) for i in range(len(yr)) if X[i,1]>=1.0])
