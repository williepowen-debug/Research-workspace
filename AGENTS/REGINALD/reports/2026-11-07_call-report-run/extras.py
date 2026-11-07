import sys, pathlib, collections
sys.path.insert(0,'AGENTS/REGINALD/scripts')
import mi3_cohort_screen as m
import ranking_test_20261107 as rk
Q=['3-31-2026','6-30-2026','9-30-2026']
def load(rssd,q):
    p=pathlib.Path(f'/tmp/mi3/fac/{rssd}_{q}.sdf')
    if not p.exists(): return None,[]
    t=p.read_text(errors='replace'); rows=[l.split(';') for l in t.splitlines()[1:]]
    return m.parse(t),rows
print('== filing Last Update, 9/30 (mode, max) and any 6/30 update after 2026-08-15')
for row in m.COHORT:
    tk,rssd=row[0],row[1]
    d,rows=load(rssd,'9-30-2026')
    lu=collections.Counter(r[4] for r in rows if len(r)>4 and r[4])
    d2,rows2=load(rssd,'6-30-2026')
    lu2=[r[4] for r in rows2 if len(r)>4 and r[4]]
    print(tk,'9/30 latest',max(lu),'mode',lu.most_common(1)[0][0],'| 6/30 latest',max(lu2))
print('== NDFI: RC-N M9 and all RCN rows naming nondepository, plus 9.a and Memo 10')
for row in m.COHORT+[('Preferred',1918344),('NexBank',652874)]:
    tk,rssd=row[0],row[1]
    d,rows=load(rssd,'9-30-2026')
    seen={}
    for r in rows:
        if len(r)>7 and 'nondepository' in r[5].lower() and r[6].strip()=='RCN':
            seen[r[7].strip()+' '+r[2][4:]]=r[3]
    print(tk,seen)
print('== Memo 10 at 6/30, 9/30 (bal)')
for row in m.COHORT:
    tk,rssd=row[0],row[1]
    out=[]
    for q in ['6-30-2026','9-30-2026']:
        d,rows=load(rssd,q)
        vals={}
        for r in rows:
            if len(r)>7 and r[6].strip()=='RCCI' and r[7].strip() in('9a','M10a','M10b','M10c','M10d','M10e'):
                vals[r[7].strip()]=vals.get(r[7].strip()) or r[3]
        out.append(vals)
    print(tk,out)
print('== same-basis sensitivity: 1403 over matching-prefix 2122')
def fld(d,c):
    for p in ('RCON','RCFD','RIAD'):
        if p+c in d:return d[p+c]
def same(d):
    if 'RCFD1403' in d and 'RCFD2122' in d: return d['RCFD1403'],d['RCFD2122']
    return fld(d,'1403'),fld(d,'2122')
pr={};sec={};b2={};pf={};sf={};bf={}
for row in m.COHORT:
    tk,rssd=row[0],row[1]
    a,_=load(rssd,'3-31-2026');b,_=load(rssd,'6-30-2026');c,_=load(rssd,'9-30-2026')
    na,la=same(a);nb,lb=same(b);nc,lc=same(c)
    pr[tk]=100*(nc/lc-nb/lb);b2[tk]=100*(nb/lb-na/la)
    co=(fld(c,'4635') or 0)-(fld(c,'4605') or 0);cob=(fld(b,'4635') or 0)-(fld(b,'4605') or 0)
    sec[tk]=100*(co-cob)/lc*4
    fl=fld(c,'2122');pf[tk]=(fld(c,'1403')/fl-fld(b,'1403')/fld(b,'2122'))*100
    print(tk,'RCFD2122' , 'RCFD2122' in c, f"primary same {pr[tk]:+.3f} frozen {pf[tk]:+.3f}; secondary same {sec[tk]:.3f}; 6/30 ratio same {100*nb/lb:.3f}")
T=list(pr)
for name,o in (('primary',pr),('secondary',sec)):
    oc=[o[t] for t in T]
    for k,i in (('S1',0),('S2',1),('B1',2)):
        print(name,k,round(rk.spearman([rk.FROZEN[t][i] for t in T],oc),3))
    print(name,'B2',round(rk.spearman([b2[t] for t in T],oc),3))
print('== leave-out: primary S1, without EGBN; without OZK')
fr={'OZK':-.662,'WAL':-.121,'EGBN':.681,'ZION':.030,'SSB':.015,'CFG':.023,'BKU':.034,'SBCF':-.118,'AMTB':-.366,'FLG':-.069,'MTB':.049,'HBAN':.049,'VLY':.080,'CUBI':-.022}
for drop in ('OZK','EGBN'):
    t=[x for x in T if x!=drop]
    print(drop,'primary S1',round(rk.spearman([rk.FROZEN[x][0] for x in t],[pf[x] for x in t]),3),'B1',round(rk.spearman([rk.FROZEN[x][2] for x in t],[pf[x] for x in t]),3))
print('== FLG memo 1 rows RC-C')
for q in Q:
    d,rows=load(694904,q)
    print(q,[ (r[2],r[3],r[7].strip(),r[5][:50]) for r in rows if len(r)>7 and r[6].strip()=='RCCI' and r[7].strip().startswith('M1') and not r[7].strip().startswith('M10') and not r[7].strip().startswith('M1 ') and r[2].startswith('RCFD')][:20])
print('== side list q/q')
for name,rssd in rk.SIDE_LIST: print(name,rssd)
