import csv,datetime as D,statistics as s
L={}
for r in csv.reader(open('gatun.csv')):
    try:L[D.date.fromisoformat(r[0][:10])]=float(r[1])
    except Exception:
        pass
print(len(L),min(L),max(L))
# effective Neopanamax max draft changes (date, ft, advisory); realised only (postponed steps dropped)
T="""2016-06-27 43 A-30-2016
2016-08-05 44 A-41-2016
2016-10-18 45 A-55-2016
2017-09-01 46 A-30-2017
2017-12-14 47 A-41-2017
2018-02-09 50 A-05-2018
2018-03-19 49 A-06-2018
2018-04-27 48 A-12-2018
2018-06-13 49 A-22-2018
2018-06-26 50 A-24-2018
2019-02-11 49 A-01-2019
2019-02-27 48 A-03-2019
2019-03-13 47 A-05-2019
2019-03-29 46 A-06-2019
2019-04-10 45 A-08-2019
2019-04-30 44 A-10-2019
2019-07-25 45 A-28-2019
2019-09-12 46 A-35-2019
2020-03-30 45.5 A-07-2020
2020-05-01 45 A-15-2020
2020-05-28 45.5 A-18-2020
2020-06-12 46 A-21-2020
2020-07-07 47 A-25-2020
2020-07-24 48 A-27-2020
2020-09-01 49 A-32-2020
2020-09-23 50 A-35-2020
2021-03-17 49.5 A-10-2021
2021-03-24 49 A-10-2021
2021-06-09 50 A-27-2021
2022-03-24 49.5 A-10-2022
2022-05-06 50 A-18-2022
2023-03-01 49.5 A-02-2023
2023-03-15 49 A-04-2023
2023-03-28 48.5 A-08-2023
2023-04-07 48 A-09-2023
2023-04-19 47.5 A-17-2023
2023-04-27 47 A-17-2023
2023-05-05 46.5 A-17-2023
2023-05-12 46 A-17-2023
2023-05-17 45 A-18-2023
2023-05-24 44.5 A-20-2023
2023-06-19 44 A-25-2023
2024-05-30 45 A-16-2024
2024-06-15 46 A-19-2024
2024-06-26 47 A-20-2024
2024-07-11 48 A-20-2024
2024-08-05 49 A-26-2024
2024-08-15 50 A-28-2024
2026-07-03 49.5 A-18-2026
2026-07-24 49 A-22-2026
2026-08-15 48.5 A-22-2026
2026-09-02 48 A-29-2026
2026-09-28 49 A-36-2026
2026-11-09 50 A-42-2026""".split('\n')
T=[(D.date.fromisoformat(a.split()[0]),float(a.split()[1]),a.split()[2]) for a in T]
pv=None
print('cuts: date draft lake gap(draft-lake)')
C=[]
for d,f,a in T:
    k='cut' if pv and f<pv else 'raise';print(d,k,f,a,L.get(d),round(L[d]-f,2) if d in L else None)
    if k=='cut':C.append((f,L[d]))
    pv=f
b={}
for f,l in C:b.setdefault(f,[]).append(l)
print({k:(sorted(v),round(s.mean(v),2)) for k,v in sorted(b.items())})
def draft(d):
    x=None
    for a,f,_ in T:
        if a<=d:x=f
    return x
print('season: draft 1Jan, min Jan-Apr; lake 22Nov,1Jan, minlake Jan-Apr')
for y in range(2017,2027):
    ds=[D.date(y,1,1)+D.timedelta(i) for i in range(120)]
    print(y,'nov22 draft',draft(D.date(y-1,11,22)),'min',min(draft(d) for d in ds),'lake nov22',L.get(D.date(y-1,11,22)),'1jan',L.get(D.date(y,1,1)),'30apr',L.get(D.date(y,4,30)),'min',min(L[d] for d in ds if d in L))
import json;json.dump({'T':[(str(a),b,c) for a,b,c in T]},open('T.json','w'))
# base rates of lake Nov22 -> fall to min by Apr 30
def mn(y,e=(4,30)):
    v=[L[d] for d in (D.date(y,1,1)+D.timedelta(i) for i in range(181)) if d in L and d<=D.date(y,*e)];return min(v)
R=[]
for y in range(1966,2027):
    d=D.date(y-1,11,22)
    if d in L:R.append((y,L[d],mn(y),round(L[d]-mn(y),2)))
def q(v):v=sorted(v);return [round(v[int(p*(len(v)-1))],2) for p in(.1,.25,.5,.75,.9)]
print('drop Nov22->min by Apr30 all n',len(R),q([r[3] for r in R]),'since2017',[(r[0],r[3]) for r in R if r[0]>=2017])
S=[1966,1973,1983,1992,1998,2016,2024]
print('strong EN',[r for r in R if r[0] in S])
for lv in (83.5,83,82.5,82,81.5,81):
    n=[r for r in R if r[2]<=lv];m=[r for r in R if r[3]>=86.58-lv];m2=[r for r in R if r[0]>=2017 and r[3]>=86.58-lv];m3=[r for r in R if r[0] in S and r[3]>=86.58-lv]
    print('lake<=',lv,'by Apr30: from 86.58 need drop',round(86.58-lv,2),'all yrs',len(m),'/',len(R),'since2017',len(m2),'/10','strongEN',len(m3),'/',len(S),[r[0] for r in m3])
