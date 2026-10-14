"""Correct scalar serialization only; preserve BOARD bodies and recipient packets."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import subprocess

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
plan=json.loads((OUT/'dispatch-plan.json').read_text())
proof=[];paths=[]
for s in plan:
    p=ROOT/'BOARD'/Path(s['draft_path']).name
    old=p.read_text();head,body=old.split('\n---\n\n',1)
    source_commit=json.loads((OUT/'source-commit.json').read_text())['commit']
    original=subprocess.run(['git','show',source_commit+':'+str(p.relative_to(ROOT))],cwd=ROOT,capture_output=True,text=True,check=True).stdout
    newlines=[]
    for line in head.splitlines():
        if ': ' in line:
            key,value=line.split(': ',1)
            if key not in {'origin','dispatch_note','corrects','corrects_direction','dispatch_scope','erratum'}:
                try:
                    scalar=json.loads(value)
                    if isinstance(scalar,str):line=key+': '+scalar
                except ValueError:pass
        newlines.append(line)
    if not any(line.startswith('erratum:') for line in newlines):
        newlines.append('erratum: "2026-10-14 — scalar serialization corrected for legacy BOARD parsers; source claims and recipient packets unchanged."')
    new='\n'.join(newlines)+'\n---\n\n'+body
    assert new.split('\n---\n\n',1)[1]==body
    p.write_text(new)
    assert original.split('\n---\n\n',1)[1]==body
    proof.append({'path':str(p.relative_to(ROOT)),'old_sha256':hashlib.sha256(original.encode()).hexdigest(),'new_sha256':hashlib.sha256(new.encode()).hexdigest(),'body_sha256':hashlib.sha256(body.encode()).hexdigest(),'body_unchanged':True,'original_commit':source_commit})
    paths.append(str(p.relative_to(ROOT)))
r=subprocess.run(['python3','AGENTS/WALTER/tools/gen_board_index.py','--write','BOARD/INDEX.md','--cutover'],cwd=ROOT,capture_output=True,text=True)
assert r.returncode==0,(r.stdout,r.stderr)
paths.append('BOARD/INDEX.md')
r=subprocess.run(['python3','AGENTS/WALTER/tools/walter_doctor.py'],cwd=ROOT,capture_output=True,text=True)
(OUT/'doctor-after-repair.txt').write_text(r.stdout+r.stderr)
high=[line for line in (r.stdout+r.stderr).splitlines() if re.search(r'[⚠✗❌]\s+HIGH\b',line)]
assert not high,high
(OUT/'metadata-repair.json').write_text(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'proof':proof,'high_findings':high,'recipient_packets':'UNCHANGED'},indent=2))
paths += [str((OUT/'metadata-repair.json').relative_to(ROOT)),str((OUT/'doctor-after-repair.txt').relative_to(ROOT)),str(Path(__file__).relative_to(ROOT))]
msg=OUT/'repair-commit-message.txt';msg.write_text('WALTER: correct morning BOARD scalar serialization\n\nBodies conserved exactly; additive erratum records formatting correction. Recipient create-only packets untouched. Generated INDEX and doctor now reconcile.\n')
paths.append(str(msg.relative_to(ROOT)))
for cmd in [['git','add','--']+paths,['git','commit','-F',str(msg),'--']+paths]:
    r=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True);assert r.returncode==0,(r.stdout,r.stderr)
r=subprocess.run(['git','rev-parse','HEAD'],cwd=ROOT,capture_output=True,text=True)
(OUT/'metadata-repair-commit.json').write_text(json.dumps({'commit':r.stdout.strip(),'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2))
print('Metadata-only correction committed',r.stdout.strip(),'; bodies unchanged; doctor HIGH=0.')
