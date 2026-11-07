import csv,re
R='AGENTS/REGINALD/workbook/'
rows=list(csv.DictReader([l for l in open(R+'CRE_RCN_COHORT.tsv') if not l.startswith('#')],delimiter='\t'))
D={(r['ticker'],r['quarter']):r for r in rows}
tks=sorted({r['ticker'] for r in rows})
n=lambda r,k:float(r[k])
def shape(q0,q1):
    out=[]
    for t in tks:
        a,b=D[(t,q0)],D[(t,q1)]
        if n(b,'nonaccrual_total_k')>n(a,'nonaccrual_total_k') and n(b,'acl_k')<n(a,'acl_k'):
            out.append(f"{t} NA {n(b,'nonaccrual_total_k')-n(a,'nonaccrual_total_k'):+,.0f} ACL {n(b,'acl_k')-n(a,'acl_k'):+,.0f}")
    return out
print('shape Q1>Q2',shape('3/31/2026','6/30/2026'));print('shape Q2>Q3',shape('6/30/2026','9/30/2026'))
print('sum NA',sum(n(D[(t,'6/30/2026')],'nonaccrual_total_k') for t in tks),sum(n(D[(t,'9/30/2026')],'nonaccrual_total_k') for t in tks))
print('sum OREO',sum(n(D[(t,'6/30/2026')],'oreo_total_k') for t in tks),sum(n(D[(t,'9/30/2026')],'oreo_total_k') for t in tks))
for q in ('3/31/2026','6/30/2026','9/30/2026'):
    print(q,'mid5 rate',[ (t,round(100*sum(n(D[(t,q)],k) for k in 'na_con_k na_mf_k na_noo_k pd90_con_k pd90_mf_k pd90_noo_k'.split())/sum(n(D[(t,q)],k) for k in 'bal_con_k bal_mf_k bal_noo_k'.split()),2),n(D[(t,q)],'oreo_total_k')) for t in ('WAL','VLY','SSB','BKU','SBCF')])
ndfi={'6/30':[25900,122456,0,9459,11556,130,25134,0,0,50,7000,21625,0,0],'9/30':[0,122497,9541,9429,7533,128,24968,0,0,0,7000,15701,18522,0]}
print('NDFI NA sum',{k:sum(v) for k,v in ndfi.items()},'holders',{k:sum(1 for x in v if x) for k,v in ndfi.items()})
print('CUBI 10b+10c',2858825+736743,3011076+1026454,round(100*((3011076+1026454)/(2858825+736743)-1),1))
hdr=None
for l in open(R+'MI3_COHORT.tsv'):
    if l.startswith('#'):continue
    f=l.rstrip('\n').split('\t')
    if hdr is None: hdr=f;continue
    r=dict(zip(hdr,f))
    if r.get('quarter')=='9/30/2026': print(r['ticker'],{k:r[k] for k in hdr if 'qoq' in k.lower() or 'step' in k.lower() or 'yoy' in k.lower()})
