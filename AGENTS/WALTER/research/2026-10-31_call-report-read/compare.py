"""One-time requested bank comparison; not a monitor or owner grading writer.
Fresh March/June FFIEC primary pulls, September files from this session's verified availability pull.
All amount fields $000; ratios as published percent. Raw source files retained outside git.
"""
from pathlib import Path
import sys,json,base64,csv,io,subprocess,tempfile,hashlib,datetime,concurrent.futures
from decimal import Decimal as D
ROOT=Path(__file__).resolve().parents[4]; HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'AGENTS/REGINALD/scripts'))
import mi3_cohort_screen as m
COHORT=[('OZK',107244),('WAL',3138146),('EGBN',2652092),('ZION',276579),('SSB',1929247),('CFG',3303298),('BKU',3938186),('SBCF',34537),('AMTB',83638),('FLG',694904),('MTB',501105),('HBAN',12311),('VLY',229801),('CUBI',2354985)]
Q3=Path('/tmp/walter-call-report-availability-6guvqyx_'); RAW=Path(tempfile.mkdtemp(prefix='walter-call-report-comparison-'))
user,token=m.creds()
def pull(arg):
 bank,rssd,period=arg
 headers='\n'.join([f'UserID: {user}',f'Authentication: Bearer {token}','Content-Type: application/json','dataSeries: Call',f'reportingPeriodEndDate: {period}','fiIDType: ID_RSSD',f'fiID: {rssd}','facsimileFormat: SDF'])+'\n'
 p=subprocess.run(['curl','-sS','--max-time','40','--header','@-','--write-out','\n%{http_code}',m.BASE+'/RetrieveFacsimile'],input=headers,text=True,capture_output=True)
 body,_,http=p.stdout.rpartition('\n')
 if http!='200':raise ValueError(f'{bank} {period} HTTP {http}')
 raw=base64.b64decode(json.loads(body)); date={'3/31/2026':'20260331','6/30/2026':'20260630'}[period]; path=RAW/f'{bank}_{date}.sdf';path.write_bytes(raw);return (bank,date,path)
jobs=[(bank,rssd,q) for bank,rssd in COHORT for q in ['3/31/2026','6/30/2026']]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: paths=list(pool.map(pull,jobs))
paths += [(bank,'20260930',Q3/f'{bank}_20260930.sdf') for bank,rssd in COHORT]
fields={'asset':['RCFD2170','RCON2170'],'equity':['RCFD3210','RCON3210'],'aoci':['RCFDB530','RCONB530'],'afs_cost':['RCFD1772','RCON1772'],'afs_fv':['RCFD1773','RCON1773'],'htm_cost':['RCFD1754','RCON1754'],'htm_fv':['RCFD1771','RCON1771'],'dom_dep':['RCON2200'],'foreign_dep':['RCFN2200'],'nib_dom':['RCON6631'],'brokered':['RCON2365'],'uninsured_dom':['RCON5597'],'loans':['RCFD2122','RCON2122'],'allowance':['RCFD3123','RCON3123'],'nal':['RCFD1403','RCON1403'],'past90':['RCFD1407','RCON1407'],'past30':['RCFD1406','RCON1406'],'ni_ytd':['RIAD4340'],'co_ytd':['RIAD4635'],'rec_ytd':['RIAD4605'],'loan_prov_ytd':['RIAD4230'],'other_bor':['RCFD3190','RCON3190'],'fedfunds':['RCONB993','RCFDB993'],'repos':['RCFDB995','RCONB995'],'cet1ratio':['RCFAP793','RCOAP793','RCFDP793','RCONP793'],'cet1':['RCFAP859','RCOAP859','RCFDP859','RCONP859'],'mi3':['RCFD2746','RCON2746'],'ndfi':['RCFDJ454','RCONJ454']}
data={}; evidence=[];receipts=[]
for bank,date,path in paths:
 raw=path.read_bytes();rows=list(csv.reader(io.StringIO(raw.decode('utf-8')),delimiter=';')); rows=[r for r in rows[1:] if len(r)>=8];rssd=dict(COHORT)[bank]
 assert rows and all(r[0]==date and r[1]==str(rssd) for r in rows),(bank,date,'identity')
 by={r[2]:r for r in rows};d={}
 for field,codes in fields.items():
  code=next((c for c in codes if c in by),None)
  if code:
   r=by[code];v=r[3].replace(',','').replace('%','');d[field]=D(v) if v not in ['', 'NR','NA'] else None;evidence.append([bank,date,field]+r)
  else:d[field]=None
 # Foreign deposits absent on domestic-only form, not other arbitrary missing values.
 d['deposits']=d['dom_dep']+(d['foreign_dep'] or D(0)) if d['dom_dep'] is not None else None
 d['borrowings']=sum(d[k] for k in ['other_bor','fedfunds','repos']) if all(d[k] is not None for k in ['other_bor','fedfunds','repos']) else None
 for typ in ['afs','htm']:d[typ+'_gap']=d[typ+'_cost']-d[typ+'_fv'] if d[typ+'_cost'] is not None and d[typ+'_fv'] is not None else None
 d['nco_ytd']=d['co_ytd']-d['rec_ytd'] if d['co_ytd'] is not None and d['rec_ytd'] is not None else None
 data[(bank,date)]=d;receipts.append({'bank':bank,'rssd':rssd,'report_date':date,'sha256':hashlib.sha256(raw).hexdigest(),'raw_path':str(path),'rows':len(rows),'source':m.BASE+'/RetrieveFacsimile','retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat() if date!='20260930' else '2026-11-01T02:18:33.515051+00:00'})
def diff(b,a):return b-a if b is not None and a is not None else None
def pct(a,b):return a/b*100 if a is not None and b not in [None,0] else None
summary=[]
for bank,rssd in COHORT:
 a,b,c=[data[(bank,date)] for date in ['20260331','20260630','20260930']]
 z={'bank':bank,'rssd':rssd,'q2':b,'q3':c,'change':{k:diff(c[k],b[k]) for k in b}}
 z.update(equity_pct=pct(diff(c['equity'],b['equity']),b['equity']),aoci_drag_pct_q2_equity=pct(diff(b['aoci'],c['aoci']),b['equity']),deposit_pct=pct(diff(c['deposits'],b['deposits']),b['deposits']),q2_nal_pct=pct(b['nal'],b['loans']),q3_nal_pct=pct(c['nal'],c['loans']),q2_acl_nal_pct=pct(b['allowance'],b['nal']),q3_acl_nal_pct=pct(c['allowance'],c['nal']),q2_income=diff(b['ni_ytd'],a['ni_ytd']),q3_income=diff(c['ni_ytd'],b['ni_ytd']),q2_nco=diff(b['nco_ytd'],a['nco_ytd']),q3_nco=diff(c['nco_ytd'],b['nco_ytd']),q2_loan_prov=diff(b['loan_prov_ytd'],a['loan_prov_ytd']),q3_loan_prov=diff(c['loan_prov_ytd'],b['loan_prov_ytd']))
 summary.append(z)
(HERE/'comparison.json').write_text(json.dumps(summary,default=str,indent=2)+'\n');(HERE/'retrieval.json').write_text(json.dumps(receipts,indent=2)+'\n')
with (HERE/'selected-primary-rows.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['bank','period','field','Call Date','Bank RSSD','MDRM','Value','Last Update','Short Definition','Schedule','Line']);w.writerows(evidence)
print('bank eq% AOCI-drag% deps% CET1 Q2->Q3 NAL Q2->Q3 $M NCO Q2->Q3 $M income Q2->Q3 $M')
for z in summary:
 def f(v,scale=1):return 'NA' if v is None else f'{v/D(scale):.2f}'
 print(z['bank'],f(z['equity_pct']),f(z['aoci_drag_pct_q2_equity']),f(z['deposit_pct']),f(z['q2']['cet1ratio'])+'->'+f(z['q3']['cet1ratio']),f(z['q2']['nal'],1000)+'->'+f(z['q3']['nal'],1000),f(z['q2_nco'],1000)+'->'+f(z['q3_nco'],1000),f(z['q2_income'],1000)+'->'+f(z['q3_income'],1000))
print('Raw primary cache:',RAW)
