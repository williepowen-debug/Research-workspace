"""Path-B successor base rates (BRENT, 2026-09-30). Reproduces every figure in NOTE.md.
Inputs (saved beside this file): EIA WPSR psw01.xls 'Data 2' product supplied (WGFUPUS2 etc.,
retrieved 2026-09-30 10:57 ET) and FRED GASREGW keyless CSV (retrieved 2026-09-30 ~11:3x ET).
Metric: gasoline product supplied 4-wk avg vs the 4 weeks 52 weeks earlier (reproduces EIA's
published 4-wk YoY: wk-9/11 -1.0119%, wk-9/18 -0.7798%, wk-9/25 +0.2587% ~ EIA prose '+0.3%').
Regime filter: GASREGW YoY >= +20% in EVERY one of the prior 12 weeks. Excluded: 2020-03..2021-12
(COVID) and all of 2026 (the period under test). Window = the 8 prints after a start week."""
import json, csv, datetime as dt, os
H=os.path.dirname(os.path.abspath(__file__))
d=json.load(open(os.path.join(H,"eia_product_supplied_through_2026-09-25.json")))
G={dt.date.fromisoformat(a):v for a,v in d["WGFUPUS2"]}
P={}
for row in csv.DictReader(open(os.path.join(H,"GASREGW_fred_2026-09-30.csv"))):
    try: P[dt.date.fromisoformat(row["observation_date"])]=float(row["GASREGW"])
    except ValueError: pass
def near(day,tol=6):
    for k in range(tol+1):
        for s in (-1,1):
            x=day+dt.timedelta(days=s*k)
            if x in P: return P[x]
weeks=sorted(G)
def yoy4(i):
    if i<55 or abs((weeks[i]-weeks[i-52]).days-364)>3: return None
    return (sum(G[weeks[j]] for j in range(i-3,i+1))/sum(G[weeks[j]] for j in range(i-55,i-51))-1)*100
rows=[]
for i,w in enumerate(weeks):
    if w.year<1993 or dt.date(2020,3,1)<=w<=dt.date(2021,12,31) or w>=dt.date(2026,1,1): continue
    y=yoy4(i)
    pys=[near(w+dt.timedelta(days=3-7*k))/near(w+dt.timedelta(days=3-7*k-364))-1 for k in range(12)
         if near(w+dt.timedelta(days=3-7*k)) and near(w+dt.timedelta(days=3-7*k-364))]
    if y is None or len(pys)<10: continue
    rows.append((w,y,min(pys)*100))
def classify(filt,T,NV,K=2,L=8):
    res={"MET":0,"NOT_MET":0,"NO_VERDICT":0}; eps=set()
    for i,(w,y,py) in enumerate(rows):
        if not filt(y,py): continue
        win=rows[i+1:i+1+L]
        if len(win)<L or (win[-1][0]-w).days>7*L+3: continue
        xs=[x[1] for x in win]
        c=("MET" if any(all(x<=T for x in xs[k:k+K]) for k in range(L-K+1))
           else "NOT_MET" if all(x>NV for x in xs) else "NO_VERDICT")
        res[c]+=1; eps.add(w.year)
    n=sum(res.values()); return n,{k:round(100*v/n) for k,v in res.items()},sorted(eps)
print(f"weeks in sample: {len(rows)}  ({rows[0][0]} .. {rows[-1][0]})")
for lab,f in [("HIGH-PRICE & start>=-0.5",lambda y,py:py>=20 and y>=-0.5),("ALL & start>=-0.5",lambda y,py:y>=-0.5),
              ("HIGH-PRICE any start",lambda y,py:py>=20),("ALL any start",lambda y,py:True)]:
    for T in (-2.5,-3.0):
        n,p,e=classify(f,T,-1.0)
        print(f"{lab:26s} T<={T} x2 consec, NOT-MET all>-1.0: n={n:3d} {p}  episodes={e if lab.startswith('HIGH') else '...'}")

print("\nGRID (start>=-0.5; K consecutive; NOT-MET = every print > -1.0):")
for T in (-1.5,-2.0,-2.5):
    for K in (2,):
        a=classify(lambda y,py:py>=20 and y>=-0.5,T,-1.0,K); b=classify(lambda y,py:y>=-0.5,T,-1.0,K)
        print(f"  T<={T} K={K}: HIGH-PRICE n={a[0]} {a[1]} | ALL n={b[0]} {b[1]}")
