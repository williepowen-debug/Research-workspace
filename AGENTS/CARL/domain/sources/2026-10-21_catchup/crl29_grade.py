# CRL-29 grade under C1-C5 (WQ-437). Exact decimal from USD fields; label-matched.
import re,sys,json
from decimal import Decimal as D, getcontext
getcontext().prec=40
S=sys.argv[1]
NUM=r'\$?\s?([\d,]+(?:\.\d+)?)'
def num(s): return D(s.replace(',',''))
def grab(t,pat,idx=0):
    m=re.search(pat,t)
    if not m: raise SystemExit(f'MISSING {pat}')
    return m.group(1+idx)
panel=[('AMCAR2023-2',['2025-10-31','2025-11-30','2025-12-31'],2023),
       ('AMCAR2024-1',['2026-06-30','2026-07-31','2026-08-31'],2024),
       ('EART2024-1',['2026-03-31','2026-04-30','2026-05-31'],2024)]
rows=[]
for deal,months,vint in panel:
    for i,mo in enumerate(months):
        t=open(f'{S}/{deal}_{mo}.txt').read()
        r={'deal':deal,'collection_end':mo,'age':26+i,'vintage':vint}
        r['tm']=grab(t,r'(?:Transaction Month|Collection Period Number|Collection Period No)[^\d]{0,5}(\d+)') if re.search(r'Transaction Month',t) else 'n/a'
        r['bop']=num(grab(t,r'\{\d+\} Beginning of period Aggregate Principal Balance \{\d+\} '+NUM))
        r['eop']=num(grab(t,r'End of period Aggregate Principal Balance \{\d+\} '+NUM))
        if deal.startswith('AMCAR'):
            m=re.search(r'Net Losses in Period \{\d+\} '+NUM+r' '+NUM+r' '+NUM,t)
            r['nl']=num(m.group(3))
            r['dq61']=num(grab(t,r'delinquent 61 days or more \{\d+\} '+NUM))
            r['dq61_pct_printed']=grab(t,r'delinquent 61 days or more \{\d+\} \$?\s?[\d,]+ ([\d.]+) ?%')
            r['dq31']=num(grab(t,r'\{\d+\} Total \{\d+\} [\d,]+ '+NUM))
        else:
            r['nl']=num(grab(t,r'Net losses during period \{\d+\} '+NUM))
            r['dq61']=num(grab(t,r'more than 60 days delinquent \{\d+\} '+NUM))
            r['dq61_pct_printed']=grab(t,r'Delinquency Rate as of the end of the Collection Period \{\d+\} ([\d.]+)%')
            r['dq31']=num(grab(t,r'\{\d+\} Total \{\d+\} [\d,]+ '+NUM))
        r['ext_prin']=num(grab(t,r'Principal Balance of Receivables extended during current period \{\d+\} '+NUM))
        r['ext_den']=num(grab(t,r'Beginning of Period Aggregate Principal Balance \{\d+\} '+NUM))
        r['ext_printed']=grab(t,r'Extension Rate[^%]{0,60}?\{\d+\} ([\d.]+) ?%')
        r['loss']=r['nl']/r['bop']*12*100
        r['ext']=r['ext_prin']/r['ext_den']*100
        r['stock']=r['dq61']/r['eop']*100
        r['stock31']=r['dq31']/r['eop']*100
        rows.append(r)
def band(ds,dl,de):
    if not ds<0: return 'NV: stock not down (premise absent)'
    if dl>=D('0.77') and de>=D('0.47'): return 'D'
    if dl>=D('0.77'): return 'A'
    if dl<D('0.77') and de>=D('0.47'): return 'B'
    return 'NV: stock down, loss %s, extension %s'%('up<0.77' if dl>=0 else 'down', 'up<0.47' if de>-D('0.47') else 'down>=0.47')
out={'rows':[],'changes':[],'trust':{}}
for deal,_,_ in panel:
    rr=[r for r in rows if r['deal']==deal]
    bands=[]
    for a,b in zip(rr,rr[1:]):
        ds=b['stock']-a['stock']; dl=b['loss']-a['loss']; de=b['ext']-a['ext']; ds31=b['stock31']-a['stock31']
        bd=band(ds,dl,de); bands.append(bd)
        out['changes'].append({'deal':deal,'ages':f"{a['age']}->{b['age']}",'d_stock61':f'{ds:.4f}','d_stock31':f'{ds31:.4f}','d_loss':f'{dl:.4f}','d_ext':f'{de:.4f}','band':bd})
    out['trust'][deal]=bands[0] if bands[0]==bands[1] and bands[0] in('A','B','D') else 'NO VERDICT ('+' | '.join(bands)+')'
for r in rows:
    out['rows'].append({k:(f'{v:.4f}' if isinstance(v,D) else v) for k,v in r.items()})
tb=out['trust']; vint={d:v for d,_,v in panel}
def panel_v():
    for X,opp in (('A','B'),('B','A')):
        ag=[d for d in tb if tb[d]==X]
        if len(ag)>=2 and len({vint[d] for d in ag})>=2 and not any(tb[d]==opp for d in tb): return X
    if sum(1 for d in tb if tb[d]=='D')>=2: return 'D'
    return 'NO VERDICT'
out['panel']=panel_v()
print(json.dumps(out,indent=1))
