"""One-time join of existing, dated evidence; no retrieval or monitoring wiring."""
from pathlib import Path
import csv, hashlib, json

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
def rows(name):
    return list(csv.DictReader((l for l in (ROOT/name).read_text().splitlines() if l.strip() and not l.startswith('#')), delimiter='\t'))
paths = ['domain/sources/2026-10-13_bounded-securities-screen/screen.tsv', 'workbook/CRE_RCN_COHORT.tsv', 'workbook/NDFI_COHORT.tsv']
sec = {r['ticker']:r for r in rows(paths[0])}
cre = {r['ticker']:r for r in rows(paths[1]) if r['quarter']=='6/30/2026'}
ndfi = {r['Ticker']:r for r in rows(paths[2]) if r['Quarter']=='6/30/2026'}
assert len(sec)==len(cre)==14 and set(sec)==set(cre)
joined=[]
for t,s in sec.items():
    c,n=cre[t],ndfi[t]
    assert s['rssd']==c['rssd']==n['RSSD']
    def total(prefix, kinds): return sum(float(c[f'{prefix}_{k}_k']) for k in kinds)
    kinds=['con','mf','noo']
    bal=total('bal',kinds); bad=total('na',kinds)+total('pd90',kinds)
    na=float(c['nonaccrual_total_k']); eq=float(s['equity_k'])
    non_cre=na-total('na',kinds+['oo'])
    assert non_cre>=0 and eq>0 and na>0
    joined.append(dict(ticker=t,rssd=s['rssd'],as_of='2026-06-30',equity_k=eq,
        cre_balance_ex_owneroccupied_k=bal,cre_noncurrent_ex_owneroccupied_k=bad,
        cre_noncurrent_pct=100*bad/bal,nonaccrual_all_k=na,
        nonaccrual_pct_equity=100*na/eq,acl_k=float(c['acl_k']),acl_pct_nonaccrual=100*float(c['acl_k'])/na,
        noncre_nonaccrual_k=non_cre,oreo_all_k=float(c['oreo_total_k']),
        securities_fv_to_equity_x=s['securities_fv_to_equity_x'],
        assumed_60bp_D5_gross_pct_equity=s['incremental_gross_60bp_D5_pct_equity'],
        deposit_change_qoq_pct=s['deposit_change_qoq_pct'],fhlb_change_qoq_k=s['fhlb_change_qoq_k'],
        business_plus_PE_ndfi_k=n['PC_NDFI_K'],ndfi_total_nonaccrual_k=n['NDFI_nonaccrual_K'],
        unit_basis='USD thousands; percentages in percent; same BANK June30 total GAAP equity; CRE=construction+multifamily+nonowneroccupied',
        interpretation='Stocks are not losses; NDFI business+PE is a proxy, not pure private credit; missing AI/pension mapping is UNKNOWN, not zero'))
with (OUT/'cohort-join.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(joined[0]),delimiter='\t');w.writeheader();w.writerows(joined)
md=['| Bank | CRE noncurrent % | All nonaccrual / equity % | ACL / nonaccrual % | OREO $M | Securities / equity × | Deposits QoQ % | FHLB Δ $M |', '|---|---:|---:|---:|---:|---:|---:|---:|']
for r in joined:
    md.append(f"| {r['ticker']} | {r['cre_noncurrent_pct']:.2f} | {r['nonaccrual_pct_equity']:.1f} | {r['acl_pct_nonaccrual']:.1f} | {r['oreo_all_k']/1000:.1f} | {float(r['securities_fv_to_equity_x']):.2f} | {float(r['deposit_change_qoq_pct']):+.1f} | {float(r['fhlb_change_qoq_k'])/1000:+.1f} |")
(OUT/'table.md').write_text('\n'.join(md)+'\n')
receipt={'built_on':'2026-10-14','scope':'one-time existing14-bank synthesis; no new Call Report pull',
 'bank_as_of':'2026-06-30','inputs':[{ 'path':p,'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in paths],
 'checks':{'matched_rssd_rows':len(joined),'noncre_residual_nonnegative':True,'equity_positive':True},
 'bankruptcy':{'business_cases_12m_June2026':26941,'business_cases_12m_June2025':23043,'yoy_pct':100*(26941/23043-1),'basis':'cases with predominantly business debt, NOT small-business-only or unique firms'},
 'limits':['existing credit artifacts reused, not independently repulled','No joint loss forecast, current capital adequacy, or valuation edge established','Owner records read only; no peer launch or external send']}
(OUT/'join-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print('\n'.join(md))
