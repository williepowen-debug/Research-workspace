"""Create the reviewed self-authored coordinator memo and exact-path closeout commit."""
from pathlib import Path
import csv,json,subprocess
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
REL='AGENTS/WALTER/research/2026-10-14_walter-closeout'
memo=ROOT/'PROME/inbox/2026-10-14_from-WALTER_context-persistence-closeout.md'
assert not memo.exists(),'Create-only collision; review rather than overwrite.'
checks=json.loads((OUT/'checks/checks.json').read_text())
assert next(x for x in checks['checks'] if x['check']=='receipt')['state']=='PASS'
assert not any(' HIGH ' in x for x in (OUT/'checks/doctor.txt').read_text().splitlines())
flag='AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv'
flagrows=list(csv.reader((ROOT/flag).open(),delimiter='\t'))
row=[r for r in flagrows if len(r)>1 and r[1]=='REQ-DEWEY-20261014-001']
assert len(row)==1 and len(row[0])==13 and row[0][-1]==''
def run(args):
    p=subprocess.run(args,cwd=ROOT,capture_output=True,text=True)
    if p.returncode:raise RuntimeError(str(args)+': '+p.stdout+'\n'+p.stderr)
    return p.stdout
with memo.open('x') as f:f.write((OUT/'PROME-memo-draft.md').read_text())
ownmemo=ROOT/'AGENTS/WALTER/outbox/2026-10-14_context-persistence-closeout.md'
assert not ownmemo.exists()
with ownmemo.open('x') as f:f.write(memo.read_text())
names=['prepare_closeout.py','commit_closeout.py','REPORT.md','PROME-memo-draft.md','publication-before.json','owner-review.json','owner-headers.json','retirement-review.json','writeback-proof.json']
names+=['before-'+n for n in ['LAST_COMPLETION.md','STATUS.md','MEMORY.md','REGISTRY.tsv','SESSION_LOG.md']]
names+=['checks/'+n for n in ['checks.json','draft.md','receipt.txt','read-cap.txt','archives.txt','orphans.txt','weekdays.txt','ledger-nudge.txt','basis.txt','reads.txt','doctor.txt','versions.txt']]
paths=[REL+'/'+n for n in names]+['AGENTS/WALTER/'+n for n in ['LAST_COMPLETION.md','STATUS.md','MEMORY.md','REGISTRY.tsv','SESSION_LOG.md','routed/delivery_log.tsv']]+[flag,str(memo.relative_to(ROOT)),str(ownmemo.relative_to(ROOT))]
paths+=['AGENTS/WALTER/research/2026-10-14_intake-health/'+n for n in ['health.json','phone.txt','corrections.txt','intake-after-sync.txt','dropzone.txt','intake.txt']]
paths+=['AGENTS/WALTER/research/2026-10-14_morning-news/bookmark-unprocessed-probe.json']
assert all((ROOT/p).is_file() for p in paths)
(OUT/'commit-paths.json').write_text(json.dumps(paths,indent=2)+'\n');paths.append(REL+'/commit-paths.json')
staged=run(['git','diff','--cached','--name-only']).splitlines()
assert not set(staged).intersection(paths),'Staged overlap must be reviewed.'
run(['git','diff','--check','--']+[p for p in paths if p!=flag])
print(run(['git','diff','--stat','--']+paths))
run(['git','add','--']+paths)
message='WALTER -> PROME: save October14 context, intake receipts and DEWEY handoff\n\nFull manual write-back;14source signals/51origin-proven hands,745processed/0staged. Preserve queued owner returns, DEWEY start, source/market gaps and USER/basis/READS review. No new kill/correction/fire/doorbell/batch event: event ledger clocks deliberately unchanged. Exact authored paths only; old cache and foreign work excluded. Will explicitly requested commit/push; no pull, stash or foreign staging.\n'
print(run(['git','commit','-m',message,'--']+paths))
print('CLOSEOUT_COMMIT '+run(['git','rev-parse','HEAD']).strip())
