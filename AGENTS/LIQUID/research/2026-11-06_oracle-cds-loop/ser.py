import collections,statistics as st,datetime as dt,math,sys
K=['file','id','orig','act','evt','evts','clr','ex','eff','exp','plat','pb','blk','notl','ccy','fx','spr','up','upt','pkg','red','name','fisn','upin','nonstd']
R=[]
for l in open('rows.tsv',encoding='utf-8'):
    p=l.rstrip('\n').split('\t')
    if len(p)==len(K) and p[1]!='__DAY__': R.append(dict(zip(K,p)))
def rpv(s,T,r=.04,Rc=.4):
    h=s/(1-Rc); return sum(.25*math.exp(-(r+h)*i/4) for i in range(1,int(round(T*4))+1))
def par(u,c,T):
    s=c+u/3.5
    for _ in range(60): s=c+u/rpv(s,T)
    return s
def num(x):
    try: return float(x.replace(',','').replace('+',''))
    except: return None
def otr(d):
    # 5Y on-the-run: rolls Mar 20 and Sep 20
    if d<dt.date(2026,3,20): return '2030-12-20'
    if d<dt.date(2026,9,21): return '2031-06-20'
    return '2031-12-20'
def clean(pred):
    O=[r for r in R if pred(r)]
    dead={r['orig'] for r in O if r['act']=='EROR' and r['orig']}
    corr={}
    for r in O:
        if r['act']=='CORR' and r['orig']: corr[r['orig']]=r
    out=[]
    for r in O:
        if r['act']!='NEWT' or r['id'] in dead: continue
        out.append(corr.get(r['id'],r) if r['id'] in corr and corr[r['id']]['act']=='CORR' else r)
    return O,dead,corr,out
isor=lambda r:r['red'].startswith('6EC42L') or 'ORACLE' in r['name'].upper() or r['name'].upper().startswith('ORCL') or r['upin'].startswith('ORACLE')
O,dead,corr,N=clean(isor)
print('NEWT',sum(1 for r in O if r['act']=='NEWT'),'cancelled',len(dead),'corr',len(corr),'dead matched',sum(1 for r in O if r['act']=='NEWT' and r['id'] in dead))
day=collections.defaultdict(lambda:{'d':[],'c':[],'n':0,'cap':0.0})
pairs=[]
for r in N:
    if r['ccy'] and r['ccy']!='USD': continue
    if r['pkg'].upper()=='TRUE' or r['nonstd'].upper()=='TRUE': continue
    d=dt.date.fromisoformat(r['ex'][:10])
    if r['exp']!=otr(d): continue
    n=num(r['notl'])
    if not n or n<1e5: continue
    T=(dt.date.fromisoformat(r['exp'])-dt.date.fromisoformat(r['eff'])).days/365.25
    s=num(r['spr']) if r['spr'] else None
    fx=num(r['fx']) if r['fx'] else None
    u=num(r['up']) if r['up'] and r['upt']=='UFRO' else None
    D=day[d]; D['n']+=1; D['cap']+=n
    if s and s>0.005: D['d'].append((r['ex'],s*1e4))
    if u is not None and (fx==.01):
        D['c'].append((r['ex'],par(u/n,.01,T)*1e4))
    if s and s>0.005 and u is not None:
        pairs.append((d,s*1e4,par(u/n,.01,T)*1e4,u/n*100))
import csv
with open('orcl_5y.tsv','w') as f:
    f.write('date\texp\tn\tcap_notl_mm\tdiss_n\tdiss_med\tdiss_last\tconv_n\tconv_med\tconv_last\n')
    for d in sorted(day):
        D=day[d]; ds=[x[1] for x in sorted(D['d'])]; cs=[x[1] for x in sorted(D['c'])]
        f.write(f"{d}\t{otr(d)}\t{D['n']}\t{D['cap']/1e6:.0f}\t{len(ds)}\t{st.median(ds) if ds else ''}\t{ds[-1] if ds else ''}\t{len(cs)}\t{round(st.median(cs),1) if cs else ''}\t{round(cs[-1],1) if cs else ''}\n")
print('days',len(day),'with diss',sum(1 for D in day.values() if D['d']))
if pairs:
    g=[p[2]-p[1] for p in pairs]; print('pairs',len(pairs),'conv-diss med',st.median(g),'min',min(g),'max',max(g))
    print(pairs[-8:])
