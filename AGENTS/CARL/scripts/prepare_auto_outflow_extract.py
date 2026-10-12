#!/usr/bin/env python3
"""Offline source extraction for CRL-29 preparation. Does not calculate a verdict.
Run from any cwd after fetching the retained source manifest/documents.
Labels/Current-column selection govern; field numbers are captured, not assumed.
"""
from pathlib import Path
import re,html,json,csv,datetime,hashlib,sys
b=Path(__file__).resolve().parent.parent/'domain/sources/2026-10-12_followup'
def flat(raw):return html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',raw)))
def number(s):return float(s.replace(',',''))
def req(pattern,t,label):
 m=re.search(pattern,t,re.I)
 if not m:raise ValueError(label+' missing')
 return m
num=r'([\d,]+(?:\.\d+)?)'
def single(label,t):return number(req(re.escape(label)+r'\s*\{\d+\}\s*\$?\s*'+num,t,label).group(1))
def percent(label,t):return float(req(re.escape(label)+r'[\s\S]{0,190}?([\d.]+)\s*%',t,label).group(1))
def am_loss(t):
 m=req(r'\{(\d+)\}\s*Net Losses in Period\s*\{\1\}([^{}]+)',t,'AMCAR net losses row')
 vals=re.findall(num,m.group(2));assert len(vals)==3,(m.group(0),vals)
 return number(vals[-1]),int(m.group(1)),[number(v) for v in vals]
def dq(label,t):
 m=req(re.escape(label)+r'\s*\{\d+\}([^{}]+)',t,label)
 vals=re.findall(num,m.group(1));assert len(vals)==3,(label,vals)
 return number(vals[1]),number(vals[2])
def date_field(label,t):return datetime.datetime.strptime(req(label+r':?\s*(\d{2}/\d{2}/\d{4})',t,label).group(1),'%m/%d/%Y').date()
def build(r):
 source=(b/r['raw_path']).read_bytes()
 assert hashlib.sha256(source).hexdigest()==r['sha256'], 'source hash mismatch'
 raw=source.decode('utf8');t=flat(raw);deal=r['deal'];am=deal.startswith('AMCAR')
 begin=date_field('Monthly Period Beginning' if am else 'Collection Period Beginning',t)
 end=date_field('Monthly Period Ending' if am else 'Collection Period Ending',t)
 assert r['reportDate'].split()[0]==end.isoformat(),(deal,'report/collection mismatch')
 assert ('AmeriCredit Automobile Receivables Trust '+deal.replace('AMCAR','') if am else 'Exeter Automobile Receivables Trust '+deal.replace('EART','')) in t,(deal,'identity missing')
 cutoff=datetime.date(2024,4,14) if deal=='AMCAR2024-1' else datetime.date(2023,8,3) if deal=='AMCAR2023-2' else None
 if cutoff is None:
  m=req(r'Initial Purchase\s+[\d,]+\s*(\d{2}/\d{2}/\d{4})',t,'Exeter cutoff');cutoff=datetime.datetime.strptime(m.group(1),'%m/%d/%Y').date()
 age=(end.year-cutoff.year)*12+end.month-cutoff.month-int(end.day<cutoff.day)
 bop=single('Beginning of period Aggregate Principal Balance',t)
 eop=single('End of period Pool Balance of the Receivables',t) if not am else single('Ending Pool Balance',t)
 ext=percent('Extension Rate',t)
 if am:nl,lossref,losscols=am_loss(t)
 else:nl=single('Net losses during period',t);lossref=int(req(r'\{(\d+)\}\s*Net losses during period',t,'lossref').group(1));losscols=[nl]
 dollars61,pct61=dq('61-90 days',t);dollars91,pct91=dq('91-120 days',t)
 pubmonth=int(req(('Transaction Month' if am else 'Months Seasoned')+r':?\s*(\d+)',t,'issuer age').group(1))
 out={'deal':deal,'cik':r['cik'],'filing_date':r['filingDate'],'accession':r['accession'],'collection_begin':begin.isoformat(),'collection_end':end.isoformat(),'cutoff_date':cutoff.isoformat(),'age_months_from_cutoff':age,'issuer_month_label':pubmonth,'bop_pool_usd':bop,'eop_pool_usd':eop,'net_losses_current_usd':nl,'net_loss_field_ref':lossref,'loss_row_values_original_previous_current':','.join(map(str,losscols)),'annualized_loss_pct':nl/bop*12*100,'extension_rate_pct':ext,'dq61_90_usd':dollars61,'dq61_90_published_pct':pct61,'dq91_120_usd':dollars91,'dq91_120_published_pct':pct91,'dq_percentage_denominator':'BEGINNING_POOL' if am else 'ENDING_POOL','source_url':r['exhibit_url'],'source_sha256':r['sha256'],'state':'EXTRACTED_NOT_GRADED'}
 # Observed reporting denominator is tested, not presumed across issuers.
 denom=bop if am else eop
 assert abs(dollars61/denom*100-pct61)<.011,(deal,'61-90 denominator mismatch')
 assert abs(dollars91/denom*100-pct91)<.011,(deal,'91-120 denominator mismatch')
 # Complete source excerpt to preserve object/column identity.
 anchors=['Monthly Period Beginning' if am else 'Collection Period Beginning','Initial Purchase','Beginning of period Aggregate Principal Balance','Net Losses in Period' if am else 'Net losses during period','61-90 days','91-120 days','Extension Rate']
 snippets=[]
 for label in anchors:
  m=req(re.escape(label),t,label);snippets.append(t[max(0,m.start()-30):m.start()+380])
 (b/(deal+'_'+end.isoformat()+'-fields.txt')).write_text('\n\n'.join(snippets)+'\n')
 return out
if '--selftest' in sys.argv:
 # Source-backed checks catch the known dangerous column/identity failure modes.
 a=flat((b/'AMCAR2024-1_2026-08-31.html').read_text())
 c=flat((b/'AMCAR2023-2_2025-10-31.html').read_text())
 assert am_loss(a)==(4185064.0,115,[0.0,3883159.0,4185064.0])
 assert am_loss(c)[1]==113 and percent('Extension Rate',c)==4.04
 malformed=re.sub(r'(Net Losses in Period\s*\{115\})([^{}]+)',r'\1 $0 $3883159',a,count=1)
 try:am_loss(malformed)
 except AssertionError:pass
 else:raise AssertionError('missing Current column accepted')
 manifest=json.loads((b/'auto-access.json').read_text())
 first=next(r for r in manifest if r['deal']=='AMCAR2024-1')
 for change in [{'reportDate':'1999-01-31'},{'sha256':'wrong-hash'}]:
  try:build(dict(first,**change))
  except AssertionError:pass
  else:raise AssertionError('invalid source identity/period accepted')
 print('Source-backed selftest PASS: Current-column selection, vintage field drift, missing-column refusal, period/hash refusal.')
 raise SystemExit(0)
rows=[];fail=[]
for r in json.loads((b/'auto-access.json').read_text()):
 if r['deal']=='FROZEN_OTTO_CONTROL':continue
 try:rows.append(build(r))
 except Exception as e:fail.append({'deal':r['deal'],'reportDate':r['reportDate'],'error':str(e)})
control=flat((b/'frozen-control.html').read_text());cnl=percent('Cumulative net loss ratio',control)
assert abs(cnl-27.58)<.001,('frozen control',cnl)
(b/'auto-extraction-failures.json').write_text(json.dumps(fail,indent=2)+'\n')
if rows:
 with (b/'auto-extracted.tsv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('Frozen control CNL:',cnl,'PASS; rows',len(rows),'failures',len(fail))
for r in rows:print(r['deal'],r['collection_end'],'age',r['age_months_from_cutoff'],'issuer-age',r['issuer_month_label'],'loss',round(r['annualized_loss_pct'],4),'ext',r['extension_rate_pct'],'DQ61',r['dq61_90_published_pct'])
for f in fail:print('FAIL',f)
if fail:raise SystemExit(1)
