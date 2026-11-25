"""Servicer unsecured bonds in the iShares HYG holdings file: 2026-10-21 vs 2026-11-24.
Marks are BlackRock's evaluated prices, not TRACE trades. Spread = yield to worst minus
Treasury par curve interpolated at the file's own modified duration (approximate, not OAS)."""
import re,csv,sys,gzip,statistics as st
def load(p):
    t=(gzip.open if p.endswith('.gz') else open)(p,'rt',encoding='utf-8-sig',errors='replace').read()
    R=[[x.replace('&amp;','&') for x in re.findall(r'<ss:Data[^>]*>(.*?)</ss:Data>',r,re.S)] for r in re.findall(r'<ss:Row[^>]*>(.*?)</ss:Row>',t,re.S)]
    i=next(k for k,r in enumerate(R) if r[:1]==['Name'] and 'Yield to Worst (%)' in r)
    H=R[i]; out={}
    for r in R[i+1:]:
        if len(r)!=len(H): break
        d=dict(zip(H,r))
        if d['Asset Class']!='Fixed Income': continue
        try: v=(float(d['Price']),float(d['Yield to Worst (%)']),float(d['Mod. Duration']))
        except ValueError: continue
        k=(d['Name'].replace(' 144A','').replace(' RegS',''),d['Coupon (%)'],d['Maturity'])
        out[k]=v+(d['Sector'],float(d['Par Value'].replace(',','')))
    return out
T={'1 Mo':1/12,'3 Mo':.25,'6 Mo':.5,'1 Yr':1,'2 Yr':2,'3 Yr':3,'5 Yr':5,'7 Yr':7,'10 Yr':10}
def curve(p,date):
    for r in csv.DictReader(open(p)):
        if r['Date']==date: return sorted((T[k],float(r[k])) for k in T)
    raise SystemExit('no curve '+date)
def itp(c,x):
    if x<=c[0][0]: return c[0][1]
    for (a,ya),(b,yb) in zip(c,c[1:]):
        if a<=x<=b: return ya+(yb-ya)*(x-a)/(b-a)
    return c[-1][1]
dl=sys.argv[1] if len(sys.argv)>1 else '.'
A=load('../2026-10-22_after-close/hyg-download.xls'); B=load('hyg-download.xls.gz')
ca=curve(dl+'/ust_202610.csv','10/21/2026'); cb=curve(dl+'/ust_202611.csv','11/24/2026')
print('bonds',len(A),len(B),'UST 10/21',ca,'11/24',cb)
sp=lambda v,c:100*(v[1]-itp(c,v[2]))
KEY=('PENNYMAC','FREEDOM MORT','UWM','UNITED WHOLESALE','ROCKET COMP','ROCKET MORT','NATIONSTAR','RITHM','PLANET','LOANDEPOT','PROVIDENT FUND','PHH','ONITY','CROSSCOUNTRY')
g={}
print('| Bond | Price 10/21 | Price 11/24 | YTW 10/21 | YTW 11/24 | Spread 10/21 | Spread 11/24 | Chg |')
for k in sorted(set(A)|set(B)):
    if not k[0].startswith(KEY): continue
    a,b=A.get(k),B.get(k); n=f'{k[0]} {k[1]}% {k[2]}'
    if a and b:
        x,y=sp(a,ca),sp(b,cb); g.setdefault(k[0].split()[0],[]).append((b[1],y,y-x,b[0]-a[0]))
        print(f'| {n} | {a[0]} | {b[0]} | {a[1]} | {b[1]} | {x:.0f} | {y:.0f} | {y-x:+.0f} |')
    else: print(f'| {n} | {a and a[0]} | {b and b[0]} | {a and a[1]} | {b and b[1]} | only one file |')
for k,v in g.items(): print(k,len(v),'median YTW %.2f spread %.0f chg %+.0f price %+.2f'%tuple(st.median(z[i] for z in v) for i in range(4)))
com=[k for k in set(A)&set(B) if 1<=B[k][2]<=7 and A[k][1]<25 and B[k][1]<25]
al=[sp(B[k],cb)-sp(A[k],ca) for k in com]; q=sorted(al); n=len(q)
print('ALL HYG common n',n,'spread chg median %.0f p25 %.0f p75 %.0f p90 %.0f'%(q[n//2],q[n//4],q[3*n//4],q[9*n//10]),'YTW median %.2f'%st.median(B[k][1] for k in com))
ys=sorted(B[k][1] for k in B); print('rank of 10.00%% among %d HYG YTW: %.0f pct'%(len(ys),100*sum(y<10 for y in ys)/len(ys)))
for k in ('Finance Companies',):
    c=[sp(B[x],cb)-sp(A[x],ca) for x in com if B[x][3]==k and not x[0].startswith(KEY)]; print(k,'ex-servicers n',len(c),'median chg %.0f'%st.median(c))
# price band at BB-: nearest duration bond set 3.5-5
print('10 pct note present:',[k for k in B if k[0].startswith('FREEDOM') and k[1].startswith('10')])
print('new coupons (accrual Nov)',[k for k in B if k not in A and float(k[1])>=9][:15])
# control: bonds starting at a similar spread and duration, ex the mortgage names
SERV=lambda k:k[0].startswith(KEY)
def ctl(lo,hi):
    v=sorted(sp(B[k],cb)-sp(A[k],ca) for k in com if not SERV(k) and lo<=sp(A[k],ca)<=hi and 2<=A[k][2]<=5)
    return v
for lo,hi,tag in ((300,450,'Freedom'),(310,480,'PennyMac'),(120,200,'Rocket'),(550,650,'UWM')):
    v=ctl(lo,hi); n=len(v); print(f'CONTROL {tag} start {lo}-{hi}: n {n} p25 {v[n//4]:.0f} median {v[n//2]:.0f} p75 {v[3*n//4]:.0f} p90 {v[9*n//10]:.0f}')
v=ctl(300,450); fr=[sp(B[k],cb)-sp(A[k],ca) for k in com if k[0].startswith('FREEDOM')]
print('Freedom pctile vs control',[round(100*sum(x<f for x in v)/len(v)) for f in fr])
pm=[sp(B[k],cb)-sp(A[k],ca) for k in com if k[0].startswith('PENNYMAC')]; v=ctl(310,480)
print('PennyMac pctile vs control',[round(100*sum(x<f for x in v)/len(v)) for f in pm])
print('10pct 2032 spread at 10.00/10.07: %.0f / %.0f'%(1000-100*itp(cb,3.96),1007-100*itp(cb,3.96)))
