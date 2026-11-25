import csv,sys,datetime as dt
D=sys.argv[1]
def load(s,col=None):
    out={}
    with open(f"{D}/cboe/{s}_History.csv") as f:
        r=csv.reader(f); h=next(r)
        for row in r:
            if not row or not row[0][0].isdigit(): continue
            d=dt.datetime.strptime(row[0],"%m/%d/%Y").date()
            try: v=float(row[-1])
            except: continue
            out[d]=v
    return out
vix=load("VIX"); v3=load("VIX3M")
days=sorted(set(vix)&set(v3))
print("overlap",days[0],days[-1],len(days))
# streaks of VIX3M/VIX<1
streaks=[];cur=[]
for d in days:
    if v3[d]/vix[d]<1.0: cur.append(d)
    else:
        if cur: streaks.append(cur)
        cur=[]
if cur: streaks.append(cur)
print("total inverted closes",sum(len(s) for s in streaks),"streaks",len(streaks))
from collections import Counter
c=Counter(len(s) for s in streaks)
print("length dist",sorted(c.items()))
idx={d:i for i,d in enumerate(days)}
vixdays=sorted(vix)
vi={d:i for i,d in enumerate(vixdays)}
def fwd(d,n):
    i=vi[d]+n
    return vix[vixdays[i]] if i<len(vixdays) else None
print("\nStreaks >=5:")
print("start end len | VIX@start VIX@day5 VIX@end maxVIXinStreak | minRatio | VIX +10td +20td +40td after end | max VIX next 20td after end | streak day5 date")
rows=[]
for s in streaks:
    if len(s)>=5:
        d5=s[4]; e=s[-1]
        mx=max(vix[d] for d in s); mr=min(v3[d]/vix[d] for d in s)
        f10,f20,f40=fwd(e,10),fwd(e,20),fwd(e,40)
        i=vi[e]; nxt=[vix[x] for x in vixdays[i+1:i+21]]
        # also forward from day 7 if reached
        d7=s[6] if len(s)>=7 else None
        nx7=None
        if d7:
            j=vi[d7]; nx7=(vix[d7], fwd(d7,10), max([vix[x] for x in vixdays[j+1:j+11]] or [float('nan')]), min([vix[x] for x in vixdays[j+1:j+11]] or [float('nan')]))
        rows.append((s[0],e,len(s),vix[s[0]],vix[d5],vix[e],mx,round(mr,4),f10,f20,f40,max(nxt) if nxt else None,d5,d7,nx7))
for r in rows: print(r)
