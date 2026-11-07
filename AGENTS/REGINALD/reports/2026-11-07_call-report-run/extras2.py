import sys, pathlib
sys.path.insert(0,'AGENTS/REGINALD/scripts')
import mi3_cohort_screen as m
import ranking_test_20261107 as rk
Q=['3-31-2026','6-30-2026','9-30-2026']
user,token=m.creds()
def load(rssd,q):
    p=pathlib.Path(f'/tmp/mi3/fac/{rssd}_{q}.sdf')
    if not p.exists():
        t=m.facsimile(user,token,rssd,q.replace('-','/'),use_cache=False)
    else: t=p.read_text(errors='replace')
    return m.parse(t),[l.split(';') for l in t.splitlines()[1:]]
fld=rk.field
print('== NDFI nonaccrual PV25 / 30-89 PV23 by quarter ($K)')
for row in list(m.COHORT):
    tk,rssd=row[0],row[1]
    o=[]
    for q in Q:
        d,_=load(rssd,q); o.append((fld(d,'PV25'),fld(d,'PV23'),fld(d,'PV24')))
    print(tk,o)
print('== FLG RC-C memo 1 all lines')
for q in Q:
    d,rows=load(694904,q)
    v={}
    for r in rows:
        if len(r)>7 and r[6].strip()=='RCCI':
            ln=r[7].strip()
            if ln.startswith('M1') and ln[2:3] in 'abcdefg' : v[ln]=(r[2],int(r[3]) if r[3] else None)
    print(q,sorted(v.items()))
print('== nonaccrual + OREO sensitivity (NOT the frozen test)')
T=[];pr={};D={}
for row in m.COHORT:
    tk,rssd=row[0],row[1]
    b,_=load(rssd,'6-30-2026');c,_=load(rssd,'9-30-2026')
    nb,nc,ob,oc,lb,lc=fld(b,'1403'),fld(c,'1403'),fld(b,'2150'),fld(c,'2150'),fld(b,'2122'),fld(c,'2122')
    pr[tk]=100*((nc+oc)/lc-(nb+ob)/lb);T.append(tk)
    print(f"{tk:5} NA {nb:>10,} -> {nc:>10,} ({nc-nb:+,}) OREO {ob:>8,} -> {oc:>8,} ({oc-ob:+,}) loans {lb:>12,} -> {lc:>12,} d(NA+OREO)/loans {pr[tk]:+.3f}; ACL {fld(b,'3123'):>9,} -> {fld(c,'3123'):>9,}")
oc=[pr[t] for t in T]
for k,i in (('S1',0),('S2',1),('B1',2)):
    print(k,round(rk.spearman([rk.FROZEN[t][i] for t in T],oc),3))
print('== side list')
for name,rssd in rk.SIDE_LIST:
    for q in ('6-30-2026','9-30-2026'):
        d,_=load(rssd,q)
        print(name,q,{c:fld(d,c) for c in ('2746','3499','F179','3501','F183','1403','2122','1460','F161','3123','2150','3500','F181')})
