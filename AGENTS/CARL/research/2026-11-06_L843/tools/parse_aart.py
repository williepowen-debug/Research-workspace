#!/usr/bin/env python3
"""Parse AART monthly certificates: deal, collection end, monthly period, CNL, pool stats. Run from research/2026-11-06_L843."""
import json,re,html,csv,sys
def text(f):
    t=open(f,encoding='utf8',errors='ignore').read()
    t=re.sub(r'</(tr|p|div|table)>','\n',t); t=re.sub(r'</t[dh]>','\t',t); t=re.sub(r'<[^>]+>','',t); t=html.unescape(t); t=re.sub(r'[ \xa0]+',' ',t); t=re.sub(r'\t[\t ]*','\t',t); t=re.sub(r'\n\s*\n+','\n',t)
    return t
man=json.load(open('sources/aart/manifest.json'))
rows=[]
for m in man:
    t=text(m['file']); L=t.split('\n')
    r=dict(deal=m['deal'],period_end=m['period'],filed=m['filed'],accession=m['accession'],exhibit=m['exhibit'],form=m['form'])
    bad=[]
    # CNL row: first 'Current' after the Net Charge-Offs header
    i=next((k for k,l in enumerate(L) if 'Cumulative Net Charge-Offs' in l and 'Period' not in l),None)
    if i is None: bad.append('nohdr')
    else:
        cur=next((l for l in L[i:i+6] if l.startswith('Current')),None)
        c=cur.strip('\t').split('\t') if cur else []
        c=[x.strip() for x in c if x.strip()!='']
        if len(c)>=9:
            r['month_ncos']=float(c[3].replace(',','').replace('(','-').replace(')',''))
            r['month_loss_rate_pct']=float(c[5].rstrip('%').replace('(','-').replace(')',''))
            r['agg_fin']=float(c[6].replace(',',''))
            r['cum_nco']=float(c[7].replace(',','').replace('(','-').replace(')',''))
            r['cnl_pct']=float(c[8].rstrip('%').replace('(','-').replace(')',''))
        else: bad.append('cnlrow:'+str(c))
    # older layout: section 6 B, 'Totals' row; inception weighted averages on 'Deal Totals' row
    if 'cnl_pct' not in r:
        i=next((k for k,l in enumerate(L) if l.strip().startswith('B. Cumulative')),None)
        if i is not None:
            tl=next((l for l in L[i:i+6] if l.startswith('Totals')),None)
            if tl:
                c=[x.strip() for x in tl.split('\t') if x.strip()]
                r['agg_fin']=float(c[1].replace(',','')); r['cum_nco']=float(c[2].replace(',','').replace('(','-').replace(')',''))
                r['cnl_pct']=float(c[3].replace('%','').replace('(','-').replace(')','').strip()); bad=[x for x in bad if x!='nohdr']
        i=next((k for k,l in enumerate(L) if l.strip()=='A. Current'),None)
        if i is not None:
            cur=next((l for l in L[i:i+6] if l.startswith('Current')),None)
            if cur:
                c=[x.strip() for x in cur.split('\t') if x.strip()]
                r['month_ncos']=float(c[3].replace(',','').replace('(','-').replace(')',''))
                r['month_loss_rate_pct']=float(c[5].replace('%','').replace('(','-').replace(')','').strip())
        dt=[l for l in L if l.startswith('Deal Totals') and 'Number of Receivables' not in l]
        for l in dt:
            c=[x.strip().rstrip('%') for x in l.split('\t')[1:] if x.strip()]
            if len(c)>=9:
                r['coupon_init'],r['coupon_beg'],r['coupon_end'],r['orig_mat_init'],r['orig_mat_beg'],r['orig_mat_end'],r['rem_mat_init'],r['rem_mat_beg'],r['rem_mat_end']=[float(x) for x in c[:9]]
                break
    m3=re.search(r'Number of Receivables extended during the current Collection Period\t([\d,]+)',t)
    if m3: r['extended_n']=int(m3.group(1).replace(',',''))
    mcut=next((l for l in L if 'Accounts over 60' in l),None)
    k=next((j for j,l in enumerate(L) if l.startswith('Monthly Period') or 'Prepayment Percentage' in l),None)
    if k is not None:
        for l in L[k:k+4]:
            if re.fullmatch(r'\s*\d{1,3}\s*\t?\s*',l): r['monthly_period']=int(l.strip()); break
    for key,pat in [('coupon',r'^Weighted Averages\tCoupon\t'),('orig_mat',r'^Original Maturity\t'),('rem_mat',r'^Remaining Maturity\t')]:
        l=next((x for x in L if re.search(pat,x)),None)
        if l:
            p=[x.strip().rstrip('%') for x in l.strip('\t').split('\t')][-3:]
            r[key+'_init'],r[key+'_beg'],r[key+'_end']=[float(x) for x in p]
    l=next((x for x in L if x.startswith('Number of Receivables') or 'Number of Receivables' in x),None)
    if l: r['n_init']=int(l.strip('\t').split('\t')[-3].replace(',',''))
    if not r.get('monthly_period'):
        tr=[l for l in L if re.search(r'^\t?\d{1,2}\t\d\.\d\d%\t\d\.\d\d%\tPass',l) or re.search(r'Period\tTrigger\tDelinquencies',l)]
        m2=re.search(r'\n(?:\t)?(\d{1,3})\t(\d\.\d\d)%\t(\d+\.\d\d)%\t(Pass|Fail)',t)
        if m2: r['monthly_period']=int(m2.group(1))
    if bad: r['bad']=';'.join(bad)
    rows.append(r)
rows.sort(key=lambda x:(x['deal'],x['period_end']))
def ym(s): return int(s[:4])*12+int(s[5:7])
CUT={'2023-1':'2023-05','2024-1':'2024-01','2024-2':'2024-07','2025-1':'2025-08','2026-1':'2026-01'}
for r in rows:
    parsed=r.get('monthly_period')
    r['parsed_period']=parsed if parsed else ''
    r['monthly_period']=ym(r['period_end'])-ym(CUT[r['deal']])
keys=sorted({k for r in rows for k in r})
with open('AART_PANEL.tsv','w',newline='') as f:
    w=csv.DictWriter(f,keys,delimiter='\t',lineterminator='\n'); w.writeheader(); w.writerows(rows)
print(len(rows),'rows; bad:',[ (r['deal'],r['period_end'],r['bad'][:60]) for r in rows if 'bad' in r][:6])
for d in sorted({r['deal'] for r in rows}):
    R=[r for r in rows if r['deal']==d]
    a=R[0]
    print(d,'n',len(R),'periods',[r.get('monthly_period') for r in R][:3],'..',R[-1].get('monthly_period'),'agg',a.get('agg_fin'),'coupon',a.get('coupon_init'),'orig',a.get('orig_mat_init'),'rem',a.get('rem_mat_init'),'age',round(a.get('orig_mat_init',0)-a.get('rem_mat_init',0),1),'n_init',a.get('n_init'),'lastCNL',R[-1].get('cnl_pct'))
