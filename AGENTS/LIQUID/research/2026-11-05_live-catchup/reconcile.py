"""L4 on every HY-dated NYSE session since the letter's adoption: repaired read path vs exact oracle vs old 2dp line."""
import json,pathlib,importlib.util
from fractions import Fraction as Fr
from decimal import Decimal
p=pathlib.Path(__file__).parent
s=importlib.util.spec_from_file_location('g','AGENTS/LIQUID/scripts/gate069_legs.py'); g=importlib.util.module_from_spec(s); s.loader.exec_module(g)
raw=json.load(open(p/'raw_closes.json'))
hyr=json.load(open(p/'BAMLH0A0HYM2.json'))['rows']
hy={r['date']:round(float(r['value'])*100) for r in hyr}
four={t:{d:g.vendor_close(v) for d,v in raw[t].items() if d<='2026-11-04'} for t in g.TICK}
two={t:{d:round(float(v),2) for d,v in raw[t].items() if d<='2026-11-04'} for t in g.TICK}
print('closes per name',{t:len(four[t]) for t in g.TICK},'range',min(four['CRWV']),max(four['CRWV']))
odd=[(t,d,c) for t in g.TICK for d,c in sorted(four[t].items()) if Decimal(str(c))%Decimal('0.01')!=0]
def oracle(sess,prev,eq):
    hit=any(Fr(str(eq[t][sess]))<=Fr(str(eq[t][prev]))*Fr(85,100) for t in g.TICK)
    return 'FIRED' if hit and hy[sess]-hy[prev]>=5 else 'NOT FIRED'
rows=[];nyse=0
for sess in sorted(hy):
    if sess<'2026-09-02': continue
    if not g.is_session(sess): rows.append((sess,'NOT-NYSE')); continue
    prev=g.prev_session(sess)
    if prev not in hy: rows.append((sess,'NO-PRIOR-HY')); continue
    nyse+=1
    h={sess:hy[sess],prev:hy[prev]}
    a=g.grade_l4(h,{t:{d:v for d,v in four[t].items() if d<=sess} for t in g.TICK})
    b=g.grade_l4(h,{t:{d:v for d,v in two[t].items() if d<=sess} for t in g.TICK})
    worst=a.get('worst')
    rows.append((sess,a['state'],b['state'],oracle(sess,prev,four) if a['state']!='INSTRUMENT-FAULT' else 'FAULT',hy[sess]-hy[prev],worst[0] if worst else None,round(worst[1],3) if worst else None))
g_=[r for r in rows if len(r)>2]
print('closes total',sum(len(v) for v in four.values()),'non-cent',len(odd)); [print(' ',x) for x in odd]
print('NYSE sessions graded',nyse,'first',g_[0][0],'last',g_[-1][0])
print('other rows',[r for r in rows if len(r)==2])
print('repair != oracle',[r for r in g_ if r[1]!=r[3]])
print('repair != old-2dp',[r for r in g_ if r[1]!=r[2]])
print('fires',[r for r in g_ if r[1]=='FIRED'])
print('faults',[r for r in g_ if r[1]=='INSTRUMENT-FAULT'])
print('closest to -15',sorted(g_,key=lambda r:abs((r[6] or 0)+15))[:3])
print('last 4',g_[-4:])
