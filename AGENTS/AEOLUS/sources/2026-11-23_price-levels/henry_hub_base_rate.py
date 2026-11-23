import csv,datetime as D,statistics as s
H={}
for y in range(1991,2027):
    L=[l.strip().split('|') for l in open(f'hdd/{y}.txt') if '|' in l]
    h=L[0] if L[0][0].lower().startswith('region') else None
    c=[l for l in L if l[0].strip()=='CONUS'][0][1:]
    ds=h[1:] if h else None
    for i,v in enumerate(c):
        d=D.datetime.strptime(ds[i].strip(),'%Y%m%d').date() if ds else D.date(y,1,1)+D.timedelta(i)
        try:H[d]=float(v)
        except:pass
print(len(H),min(H),max(H),'hdr',bool(ds))
def wk(d):
    v=[H.get(d-D.timedelta(i)) for i in range(7)]
    return sum(v) if None not in v else None
def dep(d):
    b=[]
    for y in range(1991,2021):
        try:x=wk(d.replace(year=y))
        except ValueError:x=None
        if x:b.append(x)
    x=wk(d);return round(100*(x/s.mean(b)-1),1) if x and b else None
R=[]
for r in csv.reader(open('hh.csv')):
    try:R.append((r[0],float(r[1])))
    except:pass
def win(d):
    y,m=d.year,d.month
    return f"{y-1}-{y}" if m<=3 else (f"{y}-{y+1}" if m>=11 else None)
for mult,n in((1.5,1),(1.5,3),(1.5,5),(1.75,3),(2,3)):
    run=0;ev={}
    for i in range(60,len(R)):
        d=D.date.fromisoformat(R[i][0]);p=R[i][1];med=s.median(x for _,x in R[i-60:i])
        run=run+1 if p>=mult*med else 0
        w=win(d)
        if run>=n and w:ev.setdefault(w,(str(d),p,round(p/med,2),max(x for x in (dep(d-D.timedelta(j)) for j in range(0,8)) if x is not None)))
    print(mult,n,len(ev));[print('  ',k,v) for k,v in ev.items()]
