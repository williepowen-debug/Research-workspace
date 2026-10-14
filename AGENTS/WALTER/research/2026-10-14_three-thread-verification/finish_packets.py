"""Resume persistence after the completed create-only packet phase; never replay it."""
from pathlib import Path
import csv
import hashlib
import json
import re
import subprocess

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
REL='AGENTS/WALTER/research/2026-10-14_three-thread-verification'
def run(argv):
    p=subprocess.run(argv,cwd=ROOT,capture_output=True,text=True)
    if p.returncode:
        raise RuntimeError(f'{argv!r}: {p.stdout}\n{p.stderr}')
    return p.stdout
plan=json.loads((OUT/'dispatch-plan.json').read_text())
dest=[]
for s in plan:
    board=ROOT/'BOARD'/s['filename']
    assert board.read_bytes()==(OUT/s['filename']).read_bytes()
    dest.append(board)
    for recipient in dict.fromkeys(s['action']+s['info']):
        if recipient=='TERRY' or (recipient in {'CARL','RED','PROME','TERRY'} and recipient not in s['action']):
            continue
        p=ROOT/f'AGENTS/{recipient}/inbox/WALTER/{s["id"]}.md'
        assert p.is_file()
        dest.append(p)
    for ledger in ['AGENTS/WALTER/routed/route_log.tsv','AGENTS/WALTER/routed/delivery_log.tsv']:
        rows=(ROOT/ledger).read_text().splitlines()
        expected=1 if 'route_log' in ledger else sum(1 for p in dest if p.name==s['id']+'.md')
        assert sum(s['id'] in line for line in rows)==expected,(ledger,s['id'],expected)
memo=ROOT/'PROME/inbox/2026-10-14_from-WALTER_three-thread-verification.md'
assert memo.is_file()
dest.append(memo)
p=subprocess.run(['python3','AGENTS/WALTER/tools/walter_doctor.py'],cwd=ROOT,capture_output=True,text=True)
doctor=p.stdout+p.stderr
(OUT/'doctor-after.txt').write_text(doctor)
levels=re.findall(r'^\s*[✗⚠]\s+(HIGH|MED)\s+',doctor,re.M)
# Doctor returns its finding count, not a boolean status (four inherited MED).
assert p.returncode==len(levels) and 'check raised ' not in doctor
assert 'HIGH' not in levels
names=['REPORT.md','DEWEY-power-candidate.md','apply_packets.py','finish_packets.py','power-er27-evidence.json','dispatch-plan.json','helper-closeout.json',
       'before-LAST_COMPLETION.md','before-SESSION_LOG.md','doctor-after.txt','preexisting-staged.txt']+[s['filename'] for s in plan]
names+=['checks/'+p.name for p in (OUT/'checks').iterdir() if p.is_file()]
paths=[REL+'/'+name for name in names]+[str(p.relative_to(ROOT)) for p in dest]+[
    'BOARD/INDEX.md','AGENTS/WALTER/routed/route_log.tsv','AGENTS/WALTER/routed/delivery_log.tsv',
    'AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv','AGENTS/WALTER/LAST_COMPLETION.md','AGENTS/WALTER/SESSION_LOG.md',
    'AGENTS/WALTER/outbox/2026-10-14_three-thread-verification.md']
manifest={'paths':paths,'destinations':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in dest},
          'signals':2,'hands':7,'publication':'UNKNOWN','integration':'UNKNOWN','dewey':'CANDIDATE_ONLY; not launched',
          'checks':'Doctor0HIGH/4inheritedMED; selected light checks retain read-cap REVIEW, not full procedure completion',
          'resume':'Create-only phase completed once; original persistence stopped on inherited doctor MED exit; no replay/duplicate ledger rows.'}
(OUT/'persistence-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
paths.append(REL+'/persistence-manifest.json')
# The 13-column deep ledger requires an empty impact cell until owner consumption.
# Its terminal tab is a schema delimiter, not accidental prose whitespace.
flag_path='AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv'
flag_rows=list(csv.reader((ROOT/flag_path).open(),delimiter='\t'))
flag=[row for row in flag_rows if len(row)>1 and row[1]=='REQ-DEWEY-20261014-001']
assert len(flag)==1 and len(flag[0])==13 and flag[0][-1]==''
run(['git','diff','--check','--']+[p for p in paths if p!=flag_path])
run(['git','add','--']+paths)
print(run(['git','commit','-m','WALTER -> WATT VULCAN BRENT CARL HENRY LIQUID: verify three research threads','--']+paths))
print('SOURCE_COMMIT '+run(['git','rev-parse','HEAD']).strip()+'; two signals/seven handoffs; no push/DEWEY launch.')
