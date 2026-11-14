import sys,openpyxl,datetime as dt
from collections import defaultdict
SP=sys.argv[1]
SETTLE=dt.date(2026,11,13)  # T+1 from 11/12 marks
# Treasury par 11/12 (home.treasury.gov CSV): tenor years -> yield
CMT={1:4.65,2:4.86,3:4.90,5:4.95,7:5.02,10:5.10,20:5.48,30:5.43}
def cmt(t):
    ks=sorted(CMT)
    if t<=ks[0]: return CMT[ks[0]]
    for a,b in zip(ks,ks[1:]):
        if a<=t<=b: return CMT[a]+(CMT[b]-CMT[a])*(t-a)/(b-a)
    return CMT[ks[-1]]
def addm(d,m):
    y=d.year+(d.month-1+m)//12; mo=(d.month-1+m)%12+1
    import calendar; return dt.date(y,mo,min(d.day,calendar.monthrange(y,mo)[1]))
def flows(mat):
    ds=[mat]; 
    while True:
        p=addm(ds[-1],-6)
        if p<=SETTLE: return p,sorted(ds)
        ds.append(p)
def ytm(price_clean,cpn,mat):
    prev,ds=flows(mat)
    nxt=ds[0]; acc=cpn/2*((SETTLE-prev).days/(nxt-prev).days)
    dirty=price_clean+acc
    f=(nxt-SETTLE).days/(nxt-prev).days
    def pv(y):
        return sum((cpn/2+(100 if i==len(ds)-1 else 0))/(1+y/2)**(f+i) for i in range(len(ds)))
    lo,hi=-0.05,0.5
    for _ in range(100):
        m=(lo+hi)/2
        if pv(m)>dirty: lo=m
        else: hi=m
    return m*100,acc
TECH=['ORACLE','META PLATFORMS','ALPHABET','AMAZON','MICROSOFT','APPLE INC','BROADCOM','CISCO','INTEL','INTL BUSINESS','IBM','NVIDIA','SALESFORCE','QUALCOMM','MICRON','DELL','HP INC','HEWLETT','ADVANCED MICRO','TEXAS INSTR','KLA','APPLIED MATERIALS','LAM RESEARCH','ADOBE','INTUIT','ANALOG DEVICES','NXP','MARVELL','MOTOROLA','KYNDRYL','CDW','ROPER','ARROW','AVNET','FORTINET','WORKDAY','SYNOPSYS','CADENCE','KEYSIGHT','CORNING','JABIL','FLEX','AUTODESK','SERVICENOW','VMWARE','WESTERN DIGITAL','SEAGATE','NETAPP','MICROCHIP','ON SEMICONDUCTOR']
AIB=['ORACLE','META PLATFORMS','ALPHABET','AMAZON','MICROSOFT']
rows=[]
for fn in ['spib','spbo']:
    ws=openpyxl.load_workbook(f'{SP}/ssga/{fn}.xlsx',read_only=True).active
    for r in ws.iter_rows(min_row=6,values_only=True):
        if not r or not r[0] or r[5] in (None,0) or not r[8]: continue
        try: mat=dt.datetime.strptime(r[8],'%m/%d/%Y').date()
        except: continue
        if mat<=SETTLE+dt.timedelta(days=200): continue
        name=r[0].upper(); par=float(r[5]); mv=float(r[6]); cpn=float(r[4] or 0)
        if 'VAR' in name.split()[-1:] or cpn==0: continue
        px=mv/par*100
        t=(mat-SETTLE).days/365.25
        # two conventions: MV clean (as prior report) and MV dirty
        y_clean,acc=ytm(px,cpn,mat); y_dirty,_=ytm(px-acc,cpn,mat)
        iss=next((k for k in TECH if name.startswith(k) or (' '+k) in ' '+name[:30]),None)
        rows.append(dict(f=fn,name=r[0],id=r[1],cpn=cpn,mat=mat,t=t,px=px,mv=mv,acc=acc,s_clean=(y_clean-cmt(t))*100,s_dirty=(y_dirty-cmt(t))*100,y_clean=y_clean,y_dirty=y_dirty,iss=iss))
# dedupe by id (keep spib)
seen={};[seen.setdefault(x['id'],x) for x in rows]; rows=list(seen.values())
def wavg(rs,k): w=sum(x['mv'] for x in rs); return sum(x[k]*x['mv'] for x in rs)/w if w else float('nan')
groups={'All holdings':rows,'Tech basket':[x for x in rows if x['iss']],'AI builders (ORCL META GOOGL AMZN MSFT)':[x for x in rows if x['iss'] in AIB],'Other tech':[x for x in rows if x['iss'] and x['iss'] not in AIB],'Non-tech':[x for x in rows if not x['iss']]}
print('Group | n bonds | MV $B | wavg maturity yrs | yield clean-conv | yield dirty-conv | spread clean-conv | spread dirty-conv')
for g,rs in groups.items():
    print(f"{g} | {len(rs)} | {sum(x['mv'] for x in rs)/1e9:.2f} | {wavg(rs,'t'):.1f} | {wavg(rs,'y_clean'):.2f} | {wavg(rs,'y_dirty'):.2f} | {wavg(rs,'s_clean'):.0f} | {wavg(rs,'s_dirty'):.0f}")
print('\nBy issuer (tech)')
bi=defaultdict(list)
for x in rows:
    if x['iss']: bi[x['iss']].append(x)
for k,rs in sorted(bi.items(),key=lambda kv:-sum(x['mv'] for x in kv[1]))[:14]:
    print(f"{k} | {len(rs)} | {sum(x['mv'] for x in rs)/1e9:.2f} | {wavg(rs,'t'):.1f} | {wavg(rs,'s_clean'):.0f} | {wavg(rs,'s_dirty'):.0f}")
# maturity-bucket matched comparison: tech minus non-tech within buckets
print('\nBucket-matched spread, tech minus non-tech (clean / dirty conv)')
for a,b in [(1,3),(3,5),(5,7),(7,10),(10,20),(20,40)]:
    T=[x for x in groups['Tech basket'] if a<=x['t']<b]; N=[x for x in groups['Non-tech'] if a<=x['t']<b]; A=[x for x in groups['AI builders (ORCL META GOOGL AMZN MSFT)'] if a<=x['t']<b]
    if T and N: print(f"{a}-{b}y: tech {wavg(T,'s_clean'):.0f} vs non-tech {wavg(N,'s_clean'):.0f} => {wavg(T,'s_clean')-wavg(N,'s_clean'):+.0f} ; AI builders {wavg(A,'s_clean'):.0f} ({wavg(A,'s_clean')-wavg(N,'s_clean'):+.0f}) | dirty {wavg(T,'s_dirty')-wavg(N,'s_dirty'):+.0f} / AI {wavg(A,'s_dirty')-wavg(N,'s_dirty'):+.0f} | n {len(T)}/{len(A)}/{len(N)}")
print('\nOracle new notes (Nov 4 issue)')
REOFF={'2029':(99.835,240,100.535,228),'2031':(99.942,275,100.206,281),'2033':(99.995,305,100.894,298),'2046':(99.840,335,100.594,332)}
for x in rows:
    if x['iss']=='ORACLE' and x['mat'].month==11 and x['mat'].day==4 and x['mat'].year in (2029,2031,2033,2037,2046):
        r=REOFF.get(str(x['mat'].year))
        print(f"{x['name']} | mark {x['px']:.3f} | reoffer {r[0]} | Nov5 mark {r[2]} | spread clean-conv {x['s_clean']:.0f} dirty-conv {x['s_dirty']:.0f} | pricing spread {r[1]} | Nov5 {r[3]} | accrued {x['acc']:.3f} | y {x['y_clean']:.2f}")
print('\nBucket-matched, clean conv: AI builders ex-Oracle and Oracle alone, minus non-tech')
for a,b in [(1,3),(3,5),(5,7),(7,10),(10,20),(20,40)]:
    N=[x for x in groups['Non-tech'] if a<=x['t']<b]
    X=[x for x in rows if x['iss'] in AIB and x['iss']!='ORACLE' and a<=x['t']<b]
    O=[x for x in rows if x['iss']=='ORACLE' and a<=x['t']<b]
    print(f"{a}-{b}y: ex-ORCL builders {wavg(X,'s_clean')-wavg(N,'s_clean'):+.0f} (n {len(X)}) | ORCL {wavg(O,'s_clean')-wavg(N,'s_clean'):+.0f} (n {len(O)})")
X=[x for x in rows if x['iss'] in AIB and x['iss']!='ORACLE']
print('ex-ORCL builders all: spread',round(wavg(X,'s_clean')),'yield',round(wavg(X,'y_clean'),2),'mat',round(wavg(X,'t'),1))
