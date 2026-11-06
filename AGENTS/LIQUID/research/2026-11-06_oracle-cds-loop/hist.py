exec(open('ser.py').read().split("day=collections")[0].replace("print('NEWT'","(lambda *a:0)('NEWT'"))
# trade-event rows only, no novation prices; on-the-run 5Y
pts=[]
for r in N:
    if r['evt'] not in('TRAD',''): continue
    if r['pkg'].upper()=='TRUE' or r['nonstd'].upper()=='TRUE': continue
    d=dt.date.fromisoformat(r['ex'][:10])
    if r['exp']!=otr(d): continue
    n=num(r['notl']); 
    if not n or n<1e6: continue
    T=(dt.date.fromisoformat(r['exp'])-dt.date.fromisoformat(r['eff'])).days/365.25
    s=num(r['spr']) if r['spr'] else None; u=num(r['up']) if r['up'] and r['upt']=='UFRO' else None
    fx=num(r['fx']) if r['fx'] else None
    c=par(u/n,.01,T)*1e4 if u is not None and (fx in(.01,None)) else None
    pts.append(dict(d=d,ts=r['ex'][11:16],s=(s*1e4 if s and s>.005 else None),c=c,up=(u/n*100 if u is not None else None),plat=r['plat'],clr=r['clr']))
# drop conv outliers: >60bp from that day's median
by=collections.defaultdict(list)
for p in pts:
    if p['c']: by[p['d']].append(p['c'])
med={d:st.median(v) for d,v in by.items()}
for p in pts:
    if p['c'] and abs(p['c']-med[p['d']])>60: p['c']=None
ds=[p for p in pts if p['s']]
print('DISS max',sorted(((p['s'],p['d'],p['ts']) for p in ds),reverse=True)[:6])
print('CONV max',sorted(((round(p['c'],1),p['d'],p['ts']) for p in pts if p['c']),reverse=True)[:6])
g=[(p['c']-p['s']) for p in pts if p['s'] and p['c']]
print('pairs all',len(g),round(st.median(g),1))
g2=[(p['c']-p['s']) for p in pts if p['s'] and p['c'] and p['s']>=250]
print('pairs >=250',len(g2),round(st.median(g2),1) if g2 else '', round(min(g2),1) if g2 else '', round(max(g2),1) if g2 else '')
# monthly
m=collections.defaultdict(list); md=collections.defaultdict(list)
for d,v in sorted(med.items()): m[d.strftime('%Y-%m')].append((v,d))
for p in ds: md[p['d'].strftime('%Y-%m')].append((p['s'],p['d']))
print('month  days  conv_med_low  conv_med_high(date)  month_last | diss n, high(date)')
for k in sorted(m):
    v=m[k]; lo=min(v)[0]; hi=max(v); last=sorted(v,key=lambda x:x[1])[-1][0]
    dd=md.get(k,[]); print(k,len(v),round(lo),round(hi[0]),hi[1],round(last),'|',len(dd),(round(max(dd)[0],1),max(dd)[1]) if dd else '')
import json
json.dump({str(d):round(v,1) for d,v in sorted(med.items())},open('conv_med.json','w'))
# curve by maturity, last dates
print('--- curve, conv median by maturity')
for rng in [('2026-10-13','2026-10-13'),('2026-10-20','2026-10-20'),('2026-10-29','2026-10-30'),('2026-11-03','2026-11-05')]:
    c=collections.defaultdict(list)
    for r in N:
        if not(rng[0]<=r['ex'][:10]<=rng[1]) or r['evt'] not in('TRAD','') : continue
        n=num(r['notl']); u=num(r['up']) if r['up'] else None
        if not n or n<1e6 or u is None or r['fx']!='0.01': continue
        T=(dt.date.fromisoformat(r['exp'])-dt.date.fromisoformat(r['eff'])).days/365.25
        if T<.3: continue
        c[r['exp']].append(par(u/n,.01,T)*1e4)
    print(rng[0],{k:(round(st.median(v)),len(v)) for k,v in sorted(c.items())})
# clearing mix by period for on-the-run
print('--- clearing/plat')
for a,b in [('2026-07-01','2026-09-30'),('2026-10-01','2026-10-13'),('2026-10-14','2026-10-27'),('2026-10-28','2026-11-05')]:
    x=[r for r in N if a<=r['ex'][:10]<=b and r['evt']=='TRAD']
    days=len({r['ex'][:10] for r in x})
    print(a,b,'trades/day',round(len(x)/max(days,1),1),'clr',collections.Counter(r['clr'] for r in x).most_common(3),'plat',collections.Counter(r['plat'] for r in x).most_common(3),'pb',collections.Counter(r['pb'] for r in x).most_common(2),'blk',collections.Counter(r['blk'] for r in x).most_common(2))
