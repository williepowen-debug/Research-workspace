import csv,datetime,collections,statistics as st,sys
W='AGENTS/REGINALD/workbook/'
def rows(f):
    L=[l.rstrip('\n') for l in open(W+f,newline='',encoding='utf-8')]
    B=[l for l in L if not l.startswith('#')]; c=B[0].split('\t'); return [dict(zip(c,b.split('\t'))) for b in B[1:]]
key=lambda q:datetime.datetime.strptime(q,'%m/%d/%Y')
a=rows('ACL_ROLLFORWARD_COHORT.tsv');r=rows('RUNWAY_COHORT.tsv');n=rows('NDFI_COHORT.tsv')
print('ACL rows',len(a),'9/30/26',sum(x['Quarter']=='9/30/2026' for x in a))
print('=== Q3 ACL rows')
for x in a:
    if x['Quarter']=='9/30/2026': print(x['Ticker'],x['ACL_begin_K'],x['recoveries_K'],x['provision_K'],x['chargeoffs_K'],x['ACL_end_K'],x['CO_over_prov'],x['identity_ties'],x['Notes'])
old=[x for x in a if x['Quarter']!='9/30/2026']
print('=== ties, 168 8/20 rows: as-built',sum(x['identity_ties']=='YES' for x in old),'of',len(old))
full=sum(1 for x in old if x['identity_ties']=='YES' or 'full_identity=YES' in x['Notes']);print('full identity',full,'of',len(old))
bad=[(x['Ticker'],x['Quarter'],x['Notes']) for x in old if 'full_identity=NO' in x['Notes']];print('still fail',bad)
wd=[x for x in old if x['identity_ties']=='NO' and 'writedowns_5523=0 ' not in x['Notes']];ad=[x for x in old if x['identity_ties']=='NO' and 'adj_C233=0 ' not in x['Notes']]
print('NO rows',sum(x['identity_ties']=='NO' for x in old),'with write-downs',len(wd),'with C233',len(ad))
for t in sorted({x['Ticker'] for x in a}):
    o=[x for x in old if x['Ticker']==t]
    print(t,'as-built',sum(x['identity_ties']=='YES' for x in o),'/12 full',sum(x['identity_ties']=='YES' or 'full_identity=YES' in x['Notes'] for x in o), 'NO:',[ (x['Quarter'],x['Notes'].split()[0].split('=')[1],x['Notes'].split()[1].split('=')[1]) for x in o if x['identity_ties']=='NO'])
print('=== all 182');
pos=[x for x in a if x['CO_over_prov'] not in('','UNDEFINED-prov<=0')]
v=sorted(float(x['CO_over_prov']) for x in pos)
print('n',len(v),'median',st.median(v),'p90',v[int(.9*len(v))],'>=10',[(x['Ticker'],x['Quarter'],x['CO_over_prov']) for x in pos if float(x['CO_over_prov'])>=10])
print('releases',[(x['Ticker'],x['Quarter'],x['provision_K']) for x in a if int(x['provision_K'])<=0])
print('=== runway latest vs prior')
for t in sorted({x['Ticker'] for x in r}):
    s=sorted([x for x in r if x['Ticker']==t],key=lambda x:key(x['Quarter']))
    print(t,s[-2]['runway_years'],'->',s[-1]['runway_years'],'ACL',s[-2]['ACL_K'],'->',s[-1]['ACL_K'],'perCO',s[-1]['per_chargeoffs_K'],'prov',s[-1]['per_provision_K'],'TTM',s[-1]['TTM_chargeoffs_K'],s[-1]['window_has_nontie'],s[-1]['quarter_ties'])
print('FLG series',[x['runway_years'] for x in sorted([y for y in r if y['Ticker']=='FLG'],key=lambda y:key(y['Quarter'])) if x['runway_years']])
rv=sorted(float(x['runway_years']) for x in r if x['runway_years'] and x['Quarter']=='9/30/2026')
allv=sorted(float(x['runway_years']) for x in r if x['runway_years']);print('n all',len(allv),'p10,p25,med,p75,p90',[allv[int(p*len(allv))] for p in(.1,.25,.5,.75,.9)])
print('win nontie',sum(x['window_has_nontie']=='YES' for x in r),'of',sum(x['window_has_nontie']!='' for x in r))
print('=== NDFI')
tk=[x['Ticker'] for x in n if x['Quarter']=='9/30/2026']
p={x['Ticker']:x for x in n if x['Quarter']=='6/30/2026'};c={x['Ticker']:x for x in n if x['Quarter']=='9/30/2026'}
for t in tk:
    a0,b0=p[t],c[t]
    print(t,'NDFI',a0['NDFI_total_K'],'->',b0['NDFI_total_K'],f"{(int(b0['NDFI_total_K'])/int(a0['NDFI_total_K'])-1)*100:+.1f}%",'pct',a0['NDFI_pct_loans'],b0['NDFI_pct_loans'],'PC',a0['PC_NDFI_K'],b0['PC_NDFI_K'],f"{(int(b0['PC_NDFI_K'])/max(int(a0['PC_NDFI_K']),1)-1)*100:+.1f}%",'PCpct',a0['PC_NDFI_pct_loans'],b0['PC_NDFI_pct_loans'],'unf',a0['Unfunded_NDFI_K'],b0['Unfunded_NDFI_K'],'NA',a0['NDFI_nonaccrual_K'],b0['NDFI_nonaccrual_K'],'3089',a0['NDFI_30_89_K'],b0['NDFI_30_89_K'],'90',a0['NDFI_90plus_K'],b0['NDFI_90plus_K'])
for lab,S in (('14',[t for t in tk if c[t]['Sample']=='MI3-cohort']),('26',tk)):
    print(lab,'NDFI',sum(int(p[t]['NDFI_total_K']) for t in S),sum(int(c[t]['NDFI_total_K']) for t in S),'PC',sum(int(p[t]['PC_NDFI_K']) for t in S),sum(int(c[t]['PC_NDFI_K']) for t in S),'NA',sum(int(p[t]['NDFI_nonaccrual_K']) for t in S),sum(int(c[t]['NDFI_nonaccrual_K']) for t in S),'3089',sum(int(p[t]['NDFI_30_89_K']) for t in S),sum(int(c[t]['NDFI_30_89_K']) for t in S))
print('NA rank',sorted([(int(c[t]['NDFI_nonaccrual_K']),t) for t in tk],reverse=True)[:6])
print('WAL mortgage share',int(c['WAL']['M10a_mortgage_K'])/int(c['WAL']['NDFI_total_K']))
