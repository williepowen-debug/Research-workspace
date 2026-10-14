from pathlib import Path
import sys,json,csv,base64,subprocess,concurrent.futures,hashlib,datetime
ROOT=Path(__file__).resolve().parents[5]; sys.path.insert(0,str(ROOT/'AGENTS/REGINALD/scripts'))
import mi3_cohort_screen as m
u,t=m.creds(); out=ROOT/'AGENTS/REGINALD/domain/sources/2026-10-13_bounded-securities-screen'; out.mkdir(parents=True,exist_ok=True)
raw=out/'raw';raw.mkdir(exist_ok=True)
periods=['3/31/2026','6/30/2026']
def fetch(item):
 tk,rssd,name,q=item; target=raw/f'{tk}_{q.replace("/","-")}.sdf'
 cmd=['curl','--max-time','45','-s','--fail-with-body','-H',f'UserID: {u}','-H',f'Authentication: Bearer {t}','-H','Content-Type: application/json','-H','dataSeries: Call','-H',f'reportingPeriodEndDate: {q}','-H','fiIDType: ID_RSSD','-H',f'fiID: {rssd}','-H','facsimileFormat: SDF',m.BASE+'/RetrieveFacsimile']
 r=subprocess.run(cmd,capture_output=True,text=True)
 rec={'ticker':tk,'rssd':rssd,'expected_name':name,'quarter':q,'curl_rc':r.returncode,'route':m.BASE+'/RetrieveFacsimile'}
 try:
  if r.returncode: raise ValueError('request-failed')
  txt=base64.b64decode(json.loads(r.stdout)).decode('utf8','replace'); rows=list(csv.reader(txt.splitlines(),delimiter=';'))
  assert 'MDRM' in rows[0][2]
  assert all(int(x[1])==rssd for x in rows[1:] if len(x)>3 and x[1])
  assert all(x[0] in [q,datetime.datetime.strptime(q,'%m/%d/%Y').strftime('%Y%m%d'),datetime.datetime.strptime(q,'%m/%d/%Y').strftime('%m/%d/%Y')] for x in rows[1:] if len(x)>3 and x[0])
  target.write_text(txt); rec.update(status='FRESH',sha256=hashlib.sha256(txt.encode()).hexdigest(),bytes=len(txt.encode()),source_path=str(target.relative_to(ROOT)))
 except Exception as e: rec.update(status='FAILED',reason=type(e).__name__)
 return rec
jobs=[(tk,rssd,name,q) for tk,rssd,name,_ in m.COHORT for q in periods]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 receipts=list(ex.map(fetch,jobs))
(out/'retrieval.json').write_text(json.dumps({'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'receipts':receipts},indent=2)+'\n')
for r in receipts:print(r['ticker'],r['quarter'],r['status'],r.get('bytes',''),r.get('reason',''))
