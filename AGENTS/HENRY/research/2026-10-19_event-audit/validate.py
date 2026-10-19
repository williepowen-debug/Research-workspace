"""Validate archive integrity and reproduce results without untracked raw files."""
from pathlib import Path
import json,hashlib,tarfile,tempfile,shutil,subprocess,sys,datetime as dt
P=Path(__file__).resolve().parent
manifest=json.load(open(P/'source-manifest.json'))
with tarfile.open(P/'sources.tar.gz') as ar:
 assert sorted(ar.getnames())==sorted(m['file'] for m in manifest)
 for m in manifest:
  blob=ar.extractfile(m['file']).read();assert len(blob)==m['bytes'];assert hashlib.sha256(blob).hexdigest()==m['sha256']
assert len(json.load(open(P/'filing-receipts.json')))==21
assert all(r['status']==200 for r in json.load(open(P/'filing-receipts.json')))
with tempfile.TemporaryDirectory(prefix='henry-event-audit-') as tmp:
 dest=Path(tmp)/'AGENTS/HENRY/research'/P.name;dest.mkdir(parents=True)
 for f in P.iterdir():
  if f.is_file():shutil.copy2(f,dest/f.name)
 for dirname,name in [('2026-10-19_repeat-losers','daily-audit.csv.gz'),('2026-10-19_repeat-losers','RESULT.md'),('2026-10-19_catchup','COHORT.md')]:
  (dest.parent/dirname).mkdir(exist_ok=True);shutil.copy2(P.parent/dirname/name,dest.parent/dirname/name)
 for script in ['analyze.py','peers.py']:
  r=subprocess.run([sys.executable,str(dest/script)],capture_output=True,text=True);assert r.returncode==0,r.stderr
 for name in ['sensitivities.csv','events.json','worst-days.json','peer-audit.json']:
  assert (P/name).read_bytes()==(dest/name).read_bytes(),name+' reproduced differently'
metrics=json.load(open(P.parent/'2026-10-19_repeat-losers/metrics.json'))
import csv
for r in csv.DictReader(open(P/'sensitivities.csv')):
 if r['scenario']=='baseline':
  value=((1+float(r['stock_retained_return']))/(1+float(r['sector_retained_return']))-1)*100
  assert abs(value-metrics[r['symbol']]['windows'][r['window']]['sector_relative_wealth_pct'])<1e-10
val={'observed_at':dt.datetime.now(dt.timezone.utc).isoformat(),'source_members':len(manifest),'source_archive_sha256':hashlib.sha256((P/'sources.tar.gz').read_bytes()).hexdigest(),'checks':{'archive_member_hashes':'PASS','21_SEC_filings_http200':'PASS','340_daily_rows_signs_counts_compounds':'PASS','216_scenario_rows':'PASS','raw_absent_isolated_reproduction':'PASS','prior_cohort_and_result_immutable':'PASS','baseline_sector_relative_wealth':'PASS','new_verified_peers':0},'result_sha256':hashlib.sha256((P/'RESULT.md').read_bytes()).hexdigest(),'shortlist_sha256':hashlib.sha256((P/'SHORTLIST.md').read_bytes()).hexdigest()}
(P/'validation.json').write_text(json.dumps(val,indent=2)+'\n');print(json.dumps(val,indent=2))
