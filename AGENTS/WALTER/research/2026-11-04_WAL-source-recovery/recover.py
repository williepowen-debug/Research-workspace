"""Bounded retained-file recovery only; no network, credentials or cohort rerun."""
from pathlib import Path
import subprocess,json,hashlib,csv,datetime
R=Path('/home/willi/Research-workspace'); O=Path(__file__).resolve().parent
source=R/'AGENTS/WALTER/research/2026-10-31_call-report-read'
receipt=next(x for x in json.loads((source/'retrieval.json').read_text()) if x['bank']=='WAL' and x['report_date']=='20260930')
roots=[R,Path('/home/willi/Research-Intake'),Path('/tmp'),Path('/var/tmp'),Path('/home/willi/Downloads'),Path('/home/willi/.cache')]
candidates=[];scans=[]
for root in roots:
 if not root.exists():scans.append({'root':str(root),'state':'absent'});continue
 p=subprocess.run(['rg','--files','-uuu',str(root)],capture_output=True,text=True)
 files=p.stdout.splitlines();selected=[Path(x) for x in files if x.lower().endswith('.sdf') or ('3138146' in Path(x).name and Path(x).suffix.lower() in ['.txt','.csv','.json','.zip']) or ('wal' in Path(x).name.lower() and any(d in Path(x).name.lower() for d in ['20260930','2026-09-30','2026q3']) and Path(x).suffix.lower() in ['.txt','.csv','.json','.zip'])]
 scans.append({'root':str(root),'rg_rc':p.returncode,'listed_files':len(files),'candidate_files':len(selected),'errors':p.stderr.strip()})
 for f in selected:
  try: raw=f.read_bytes();h=hashlib.sha256(raw).hexdigest();candidates.append({'path':str(f),'bytes':len(raw),'sha256':h,'exact_match':h==receipt['sha256']})
  except OSError as e:candidates.append({'path':str(f),'error':str(e)})
# Search reachable Git history for original or renamed raw source paths, independent of working-tree retention.
p=subprocess.run(['git','log','--all','--format=','--name-only','--','*.sdf','*3138146*','*WAL*20260930*','*WAL*2026-09-30*'],cwd=R,capture_output=True,text=True)
history=sorted(set(x for x in p.stdout.splitlines() if x));hist_candidates=[x for x in history if 'wal' in Path(x).name.lower() or '3138146' in x]
hist=[]
for path in hist_candidates:
 revs=subprocess.check_output(['git','log','--all','--format=%H','--',path],cwd=R,text=True).splitlines()
 for rev in revs:
  v=subprocess.run(['git','show',rev+':'+path],cwd=R,capture_output=True)
  if v.returncode:continue
  h=hashlib.sha256(v.stdout).hexdigest();hist.append({'path':path,'commit':rev,'bytes':len(v.stdout),'sha256':h,'exact_match':h==receipt['sha256']})
matches=[x for x in candidates+hist if x.get('exact_match')]
remaining={}
for name in ['selected-primary-rows.tsv','bridge-primary-rows.tsv']:
 rows=list(csv.DictReader((source/name).open(),delimiter='\t'));chosen=[x for x in rows if x['bank']=='WAL' and x['period']=='20260930'];remaining[name]=chosen
result={'as_of':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':'RECOVERED' if matches else 'NOT RECOVERED','original_receipt':receipt,'exact_original_path_exists':Path(receipt['raw_path']).exists(),'scans':scans,'candidates':candidates,'git_history_candidates':hist,'matches':matches,'remaining_selected_evidence':remaining,'limits':'Local listed roots and reachable local Git refs only. No remote machine, deleted-file forensics, authenticated fresh retrieval or reconstructed original.'}
if matches:
 m=matches[0];raw=Path(m['path']).read_bytes() if 'commit' not in m else subprocess.check_output(['git','show',m['commit']+':'+m['path']],cwd=R)
 assert hashlib.sha256(raw).hexdigest()==receipt['sha256']
 rows=list(csv.reader(raw.decode().splitlines(),delimiter=';'))[1:];rows=[x for x in rows if len(x)>=8]
 assert len(rows)==receipt['rows'] and all(x[0]=='20260930' and x[1]=='3138146' for x in rows)
 (O/'WAL_20260930.sdf').write_bytes(raw);result['durable_copy']=str((O/'WAL_20260930.sdf').relative_to(R))
(O/'recovery.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['result']);print('original exists',result['exact_original_path_exists'],'file candidates',len(candidates),'historical versions',len(hist));print('surviving selected rows',{k:len(v) for k,v in remaining.items()});print('codes',{k:[x['MDRM'] for x in v] for k,v in remaining.items()});print('scan errors',[(x['root'],x.get('errors')) for x in scans if x.get('errors')])
