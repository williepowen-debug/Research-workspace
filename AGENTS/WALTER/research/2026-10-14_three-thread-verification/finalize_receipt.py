"""Pin the already-created source commit; exact own-path metadata commit only."""
from pathlib import Path
from datetime import datetime,timezone
import json,re,subprocess
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
SOURCE='d540a59b844f506fd3924a165478cf2d7456ce7a'
subprocess.run(['git','cat-file','-e',SOURCE+'^{commit}'],cwd=ROOT,check=True)
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
last=ROOT/'AGENTS/WALTER/LAST_COMPLETION.md'
s=last.read_text()
s=s.replace('Publication/delivery/consumption of this new source set remain pending until separately evidenced.','Source packets committed locally at '+SOURCE+'. Publication/delivery/consumption remain pending until separately evidenced.',1)
m=re.search(r'<!-- CLOSEOUT_RECEIPT_JSON\n(.*?)\nEND_CLOSEOUT_RECEIPT -->',s,re.S)
r=json.loads(m[1]);r['as_of']=stamp
r['publication'].append({'commit':SOURCE,'state':'pending'})
r['delivery']['note']='Morning44 hands origin-proven. New013/014 seven hands source-committed locally at '+SOURCE+'; publication and integration UNKNOWN.'
r['push']['note']='Three-thread source committed locally; coordinated origin publication unverified. No WALTER self-push; owner integration separate.'
r['manual_duties']['16']='Source '+SOURCE+' local; seven new hands pending publication. Morning44 proof retained; no self-push.'
r['selected_checks']='Receipt PASS44/51; archives/weekdays PASS; orphans ADVISORY. Read-cap REVIEW inherited oversized charter. Doctor0HIGH/4inheritedMED. Two source packets/seven hands committed locally; underlying economic/source outcomes PARTIAL.'
s=s[:m.start(1)]+json.dumps(r,indent=2)+s[m.end(1):]
last.write_text(s)
receipt=OUT/'RECEIPT.md'
assert not receipt.exists()
receipt.write_text(f'# Three-thread source receipt — {stamp}\n\nSource commit: {SOURCE}. Two BOARD source packets013/014, seven create-only owner handoffs. Three read-only helpers returned and explicitly closed. Prepared DEWEY power-contract candidate; no accepted commission or launch.\n\nValidation: both YAML headers parse; exact packet hashes and single route/ledger rows checked; doctor0HIGH/4inheritedMED; receipt44/51PASS, archives/weekdaysPASS; inherited read-capREVIEW and orphansADVISORY. Source commit preserved unrelated staged work through exact pathspecs.\n\nPublication of this source set and actual owner integration remain UNKNOWN; seven new hands are not claimed delivered. WALTER no self-push. Existing insurer access/owner gates and completed prior diesel commission preserved. Full economics and full boot remain PARTIAL.\n')
paths=['AGENTS/WALTER/LAST_COMPLETION.md',str(receipt.relative_to(ROOT)),str(Path(__file__).resolve().relative_to(ROOT))]
subprocess.run(['git','add','--']+paths,cwd=ROOT,check=True)
subprocess.run(['git','commit','-m','WALTER: pin three-thread source persistence and remaining research gaps','--']+paths,cwd=ROOT,check=True)
