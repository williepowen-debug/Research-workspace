import csv,sys,datetime as dt
D=sys.argv[1]
def load(s):
    out={}
    for row in csv.reader(open(f"{D}/cboe/{s}_History.csv")):
        if not row or not row[0][:1].isdigit(): continue
        try: out[dt.datetime.strptime(row[0],"%m/%d/%Y").date()]=float(row[-1])
        except: pass
    return out
vix=load("VIX"); v3=load("VIX3M")
days=sorted(set(vix)&set(v3))
streaks=[];cur=[]
for d in days:
    if v3[d]/vix[d]<1: cur.append(d)
    else:
        if cur: streaks.append(cur); cur=[]
if cur: streaks.append(cur)
print("first VIX3M date",min(v3),"first VIX date",min(vix))
print("day7 | len | VIX@d7 | next10 closes>25 count | min next10 | max next10 | VIX +20 sessions after d7 | streak ended within next10?")
n=0;held=0
for s in streaks:
    if len(s)>=7:
        d7=s[6]; i=days.index(d7); nx=[vix[x] for x in days[i+1:i+11]]
        f20=vix[days[i+20]] if i+20<len(days) else None
        ok=all(v>25 for v in nx); n+=1; held+=ok
        print(d7,len(s),vix[d7],sum(v>25 for v in nx),min(nx),max(nx),f20,len(s)<17, "HELD" if ok else "")
print("held all 10 >25:",held,"of",n)
# what happened day6->? all streaks reaching 6
r6=[s for s in streaks if len(s)>=6 and s[-1]!=days[-1]]
print("completed streaks reaching 6:",len(r6),"reaching 7:",sum(len(s)>=7 for s in r6))
r5=[s for s in streaks if len(s)>=5 and s[-1]!=days[-1]]
print("completed streaks reaching 5:",len(r5),"reaching 7:",sum(len(s)>=7 for s in r5))
# median length, peak timing: was max VIX of episode before or after day 7?
for s in streaks:
    if len(s)>=7:
        d7=s[6]; i=days.index(d7)
        win=days[max(0,days.index(s[0])-5):i+21]
        pk=max(win,key=lambda x:vix[x])
        print(s[0],"peak close in [start-5, d7+20]:",pk,vix[pk],"before/at d7" if pk<=d7 else "AFTER d7")
