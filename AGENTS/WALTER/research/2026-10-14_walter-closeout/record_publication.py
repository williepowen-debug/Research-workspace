"""Record the verified closeout publication, commit own receipt, and safe-push it."""
from pathlib import Path
from datetime import datetime,timezone
import json,re,subprocess

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
REL='AGENTS/WALTER/research/2026-10-14_walter-closeout'
SOURCE='880c4d2ee2adb4202b9320e1d90123ff2fe52979'
def run(args):
    p=subprocess.run(args,cwd=ROOT,capture_output=True,text=True)
    if p.returncode:raise RuntimeError(str(args)+': '+p.stdout+'\n'+p.stderr)
    return p.stdout
origin=run(['git','rev-parse','origin/master']).strip()
run(['git','merge-base','--is-ancestor',SOURCE,origin])
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
assert not (OUT/'publication.json').exists(),'Receipt exists; inspect before retry, do not replay commit.'
lanes={}
for lane in ['inbox','inbox/DEWEY']:
    lanes[lane]=[str(p.relative_to(ROOT)) for p in (ROOT/'AGENTS/WALTER'/lane).glob('*') if p.is_file() and p.name not in {'README.md','.gitkeep','.gitignore'}]
publication={'observed_at':stamp,'closeout_commit':SOURCE,'origin':origin,'verified_source_ancestor':True,
             'safe_push_receipt':'Pushed. CONFIRMED: HEAD2262bcf2c is on origin/master (fresh fetch).',
             'push_train':['880c4d2ee WALTER closeout','2262bcf2c WAL public earnings-path consumption'],
             'delivery':{'total':51,'delivered':51,'integration':'Not inferred from publication'},
             'queues':lanes,'dewey':'Will reported running; no final return consumed',
             'excluded':'Pre-existing16-file October12 source cache; all foreign working files/staged changes',
             'limits':'This records source-closeout publication. The own receipt metadata commit is immediately safe-pushed next; final CLI receipt verifies it.'}
(OUT/'publication.json').write_text(json.dumps(publication,indent=2)+'\n')
last=ROOT/'AGENTS/WALTER/LAST_COMPLETION.md'
s=last.read_text()
s=s.replace('Current closeout commit/publication follows; source publication and actual recipient integration remain separate.',f'Closeout source commit {SOURCE} is published, freshly verified against origin {origin}. All51October14 hands are origin-proven; actual recipient integration remains separate. Dated publication receipt: {REL}/publication.json.')
m=re.search(r'<!-- CLOSEOUT_RECEIPT_JSON\n(.*?)\nEND_CLOSEOUT_RECEIPT -->',s,re.S)
r=json.loads(m[1]);r['as_of']=stamp
r['publication'].append({'commit':SOURCE,'state':'published'})
r['push']={'all_walter_commits_on_origin':True,'note':'All named source/closeout commits origin-proven at '+origin+' after fresh safe-push fetch; this dated own-receipt commit is immediately safe-pushed next. Actual owner integration not inferred.'}
r['manual_duties']['16']='Source closeout '+SOURCE+' committed and safe-pushed; fresh fetch confirms origin ancestry.51/51delivery reconciled. Own receipt persistence/safe-push follows, no pull/stash/rebase/foreignstage.'
r['owed']=[x for x in r['owed'] if x!='Current closeout exact-path commit and authorized publication/receipt reconciliation']
r['selected_checks']+=' Source closeout880c4d2ee now origin-proven; final current receipt check follows.'
s=s[:m.start(1)]+json.dumps(r,indent=2)+s[m.end(1):]
last.write_text(s)
receipt=run(['python3','AGENTS/WALTER/tools/closeout_check.py'])
assert json.loads(receipt)['status']=='PASS'
(OUT/'checks/receipt-after-push.txt').write_text(receipt)
(OUT/'final-receipt.md').write_text(f'# WALTER saved-session receipt — {stamp}\n\nCloseout source commit: {SOURCE}. Published and verified against freshly fetched origin{origin}. Morning/source/metadata/mark/access/three-thread commits are also origin-proven. All51October14handoffs reconcile; actual owner consumption is separate.\n\nContext preserved: updated STATUS/REGISTRY/MEMORY/SESSION_LOG/LAST_COMPLETION, backlog/intake receipts, DEWEY running acknowledgment and pending work. MEMORY96lines/22893bytes; earlier sessionnotes conserved. No owned authored work left unsaved by the source commit; the old16-file source cache stays excluded. Foreign working files were not staged.\n\nCurrent closeout receipt checkPASS51/51. Archive/weekday/version/local-memory checksPASS; doctor0HIGH/4inheritedMED. Oversizedcharter, USERboot-basis/READSattestation and explained no-event ledger nudge remain REVIEW. Source/market coverage PARTIAL. Two BOND/LIQUID owner returns remain queued; DEWEY final handoff not consumed.\n\nThis receipt and own metadata are committed and safe-pushed by record_publication.py; the final CLI fresh-fetch confirmation supplies the exact metadata commit receipt without writing another dirty file.\n')
paths=['AGENTS/WALTER/LAST_COMPLETION.md',REL+'/publication.json',REL+'/final-receipt.md',REL+'/checks/receipt-after-push.txt',REL+'/record_publication.py']
run(['git','diff','--check','--']+paths)
run(['git','add','--']+paths)
print(run(['git','commit','-m','WALTER: record verified closeout publication and restart receipt','--']+paths))
metadata=run(['git','rev-parse','HEAD']).strip()
p=subprocess.run(['bash','scripts/safe-push.sh'],cwd=ROOT,capture_output=True,text=True)
log=p.stdout+p.stderr
Path('/tmp/walter-final-closeout-push.txt').write_text(log)
print(log)
if p.returncode:raise SystemExit(p.returncode)
run(['git','merge-base','--is-ancestor',metadata,'origin/master'])
print('FINAL_METADATA_COMMIT '+metadata+' verified on origin/master.')
print(run(['python3','AGENTS/WALTER/tools/closeout_check.py']))
print(run(['git','status','--short','--','AGENTS/WALTER']))
