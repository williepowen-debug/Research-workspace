import csv
lines=[l for l in open('AGENTS/REGINALD/workbook/CRE_RCN_COHORT.tsv') if not l.startswith('#')]
rows=list(csv.DictReader(lines,delimiter='\t'))
D={(r['ticker'],r['quarter']):r for r in rows}
def f(r,k):
    v=r[k]
    return None if v=='' else float(v)
def tot(r):
    num=[f(r,k) for k in 'na_con_k na_mf_k na_noo_k pd90_con_k pd90_mf_k pd90_noo_k'.split()]
    den=[f(r,k) for k in 'bal_con_k bal_mf_k bal_noo_k'.split()]
    if None in num or None in den: return None,None,None
    return sum(num),sum(den),100*sum(num)/sum(den)
def mf(r):
    n=[f(r,'na_mf_k'),f(r,'pd90_mf_k')];d=f(r,'bal_mf_k')
    if None in n or not d: return None
    return 100*sum(n)/d
tks=[]
for r in rows:
    if r['ticker'] not in tks: tks.append(r['ticker'])
Q0,Q1='6/30/2026','9/30/2026'
print('ticker  Q2rate Q3rate  chg%   | num Q2 $K -> Q3 $K | OREO Q2->Q3 ($K) rise | CREoreo Q2->Q3 | MF Q2 Q3 | oreo_mf Q2 Q3')
for t in tks:
    a,b=D[(t,Q0)],D[(t,Q1)]
    na,da,ra=tot(a); nb,db,rb=tot(b)
    ch=(rb/ra-1)*100 if ra else float('nan')
    oa,ob=f(a,'oreo_total_k'),f(b,'oreo_total_k')
    ca=sum(f(a,k) or 0 for k in ('oreo_con_k','oreo_mf_k','oreo_nfnr_k'));cb=sum(f(b,k) or 0 for k in ('oreo_con_k','oreo_mf_k','oreo_nfnr_k'))
    print(f"{t:5} {ra:6.2f} {rb:6.2f} {ch:+7.1f} | {na:>10,.0f} {nb:>10,.0f} den {da:>12,.0f} {db:>12,.0f}| {oa!s:>9} {ob!s:>9} {ob-oa:+9,.0f} ({((ob/oa-1)*100 if oa else float('nan')):+.1f}%) | {ca:>8,.0f} {cb:>8,.0f} | {mf(a) if mf(a) is None else round(mf(a),2)} {mf(b) if mf(b) is None else round(mf(b),2)} | {f(a,'oreo_mf_k')} {f(b,'oreo_mf_k')}")
print()
# cohort baselines
for q in ['6/30/2025','9/30/2025','12/31/2025','3/31/2026',Q0,Q1]:
    N=D_=M=Md=0
    for t in tks:
        r=D[(t,q)];n,d,_=tot(r);N+=n;D_+=d
        M+=f(r,'na_mf_k')+f(r,'pd90_mf_k');Md+=f(r,'bal_mf_k')
    print(q,'cohort total CRE',round(100*N/D_,2),'MF',round(100*M/Md,2))
print()
missing=[t for t in tks if tot(D[(t,Q1)])[2] is None or f(D[(t,Q1)],'oreo_total_k') is None]
print('missing',missing)
c=[]
for t in ['WAL','VLY','SSB','BKU','SBCF']:
    a,b=D[(t,Q0)],D[(t,Q1)]
    ra,rb=tot(a)[2],tot(b)[2]
    r50=(rb/ra-1)>0.5 if ra else None
    o=f(b,'oreo_total_k')>f(a,'oreo_total_k')
    print(t,'rate>50%',r50,'oreo rising',o)
    if r50 or o: c.append(t)
print('c',len(c),c)
