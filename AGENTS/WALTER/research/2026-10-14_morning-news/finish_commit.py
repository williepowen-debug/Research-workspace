"""Persist exact morning marker/receipt paths; no push or foreign-state edits."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import subprocess

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
DESK=ROOT/'AGENTS/WALTER'
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
last=DESK/'LAST_COMPLETION.md';s=last.read_text()
a='<!-- CLOSEOUT_RECEIPT_JSON\n';b='\nEND_CLOSEOUT_RECEIPT -->'
r=json.loads(s.split(a)[1].split(b)[0]);r['as_of']=now
r['manual_duties'].update({'11':'12 BOARD/44 create-only hands and one CLOSED19-ID batch; one FT08 history row and externalOrnnR1 row same source commit; two explicit kill dispositions. Metadata-only erratum12bodies hash-conserved, no recipient rewrites.','Tier1.breadcrumb':'One light-closeout/full-deferred breadcrumb saved; prior full history preserved.','root.consumer':'No registered threshold/baseline replaced; current observations retain their dates. External Ornn frame routed with R1; no new auto-memory or consumer scan condition selected.','root.orphans':'Exact own paths only; foreign TERRY/WAL/FORGE/PROME dirt listed in checks/orphans.txt, not staged or swept.','root.ledger_nudge':'Event ledgers refreshed; correctionsreceipt/doorbell/REGfire/deepresearch no new applicable receipt/DARK/fire/commission event, old clock retained rather than false refresh.','root.retirement':'Prior same-day full review of800 research/source paths retained,0eligible; all newly added research/source files datedtoday and in active evidence use,0new retirement moves.','15':'Live sections/owner duties and receipt updated; source/metadata published, marker/current receipt locally persisted by this scoped commit. Prior before-image conserved.','16':'Source8e2b066e6/metadata b77d7e41f on cachedorigin51c35cacc;44/44delivery reconciled. Exact source-backed745/0 marker/current receipt commit local; no self-push or actual owner-ack inference.'})
r['selected_checks']='Light runner6 checks:receipt,archives,weekdays,ledger nudge PASS;orphans ADVISORY;read-cap REVIEW(localCLAUDE70223B). Procedure and full market coverage remain PARTIAL. Receipt44/44cachedorigin proof;metadata/indexHIGH resolved. No fullbootexecution/recipientintegration inference.'
r['push']['note']='Source and metadata published by coordinated train at cached origin. Exact marker/current receipt commit locally persisted by this pass; its publication must be reconciled on next review, no self-push.'
s=s.replace('new mark/continuity persistence is the remaining commit duty.','marker/current continuity are locally persisted with the exact-path final commit; origin publication of that final state remains to reconcile.')
s=s.split(a)[0]+a+json.dumps(r,indent=2)+b+s.split(b)[1];last.write_text(s)
memo_text=f'# WALTER morning persistence receipt — {now}\n\nSource `8e2b066e699429f4780c0914af958d23131d0724` and metadata `b77d7e41f7d5159b2b8f759de0c1f32551f98bd9` are published at cached origin `51c35cacc2c2598bc74816a1ffae23a175a1a8ef`;44/44 handoffs reconciled. Actual owner integration UNKNOWN. Exact19 IDs marked after source commits;old726preserved,745processed/0staged. Three RULE9 helpers explicitly complete; no owner launch.\n\nNew metadata serialization error corrected additively;12 bodies hash-conserved and recipient packets untouched. Light receipt/archives/weekday/ledger checks pass;charter read-cap and source/coverage limits remain, so boot PARTIAL. Pending duties/design decisions live at `AGENTS/WALTER/LAST_COMPLETION.md`; source evidence `AGENTS/WALTER/research/2026-10-14_morning-news/REPORT.md`. Foreign dirty work excluded; no self-push. This marker/continuity commit needs next coordinated publication observation. No new research/trade decision.\n\n## COMPLETION — WALTER — 2026-10-14\nSTATUS: ⚠️ PARTIAL\nCHANGED:12 BOARD signals,44 handoffs,WALTER ledgers/state/source/marker receipts.\nRESULT:19 bookmarks fully dispositioned/exactly marked;FT08qualified,SKEW3/4;source44/44origin-proven.\nGAPS: Full boot/source coverage and actual owner integration unverified; final marker publication still to reconcile.\nWILL_NEEDS: No new decision; existing USO expiry rail stays TERRY/Will-owned.\nFOLLOW-UP: RED FT08 execution,FALCON census,today CBOE close,existing source duties/publication.\n'
own=DESK/'outbox/2026-10-14_morning-news-receipt.md'
shared=ROOT/'PROME/inbox/2026-10-14_from-WALTER_morning-news-receipt.md'
for path in (own,shared):
    with path.open('x') as f:f.write(memo_text)
paths=['AGENTS/WALTER/LAST_COMPLETION.md','AGENTS/WALTER/STATUS.md','AGENTS/WALTER/REGISTRY.tsv','AGENTS/WALTER/routed/delivery_log.tsv','AGENTS/WALTER/registry/x_bookmarks_pending.json','AGENTS/WALTER/registry/x_bookmarks_seen.json',str(own.relative_to(ROOT)),str(shared.relative_to(ROOT)),'AGENTS/WALTER/research/2026-10-14_morning-news/REPORT.md']
# All are this session's exact owned additions. Foreign untracked paths are excluded.
for path in OUT.rglob('*'):
    if path.is_file() and '__pycache__' not in path.parts:
        rel=str(path.relative_to(ROOT))
        test=subprocess.run(['git','ls-files','--error-unmatch','--',rel],cwd=ROOT,capture_output=True)
        if test.returncode:paths.append(rel)
paths=sorted(set(paths))
message=OUT/'final-commit-message.txt';message.write_text('WALTER: persist exact morning19 bookmark marker and publication receipt\n\n745 processed/0 staged;44 source handoffs origin-proven/reconciled. Light checks scoped, oversized charter/source gaps retained. Event-ledger clocks without new applicable events remain dated; no foreign state/index sweep or self-push.\n');paths.append(str(message.relative_to(ROOT)))
for cmd in [['git','add','--']+paths,['git','commit','-F',str(message),'--']+paths]:
    result=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True);assert result.returncode==0,(result.stdout,result.stderr)
sha=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
print('Final local marker/receipt commit',sha,'; no push;44 source handoffs already origin-proven.')
result=subprocess.run(['python3','AGENTS/WALTER/tools/closeout_check.py'],cwd=ROOT,capture_output=True,text=True)
print(result.stdout.strip());assert result.returncode==0,(result.stdout,result.stderr)
