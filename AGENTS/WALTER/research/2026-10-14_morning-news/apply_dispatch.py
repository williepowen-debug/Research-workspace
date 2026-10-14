"""Apply exactly the reviewed morning plan; create-only fleet packets, scoped commit.

Requires filesystem permission beyond the WALTER desk. No push, pull, index reset,
recipient-state edit, owner launch or outbound messaging occurs.
"""
from pathlib import Path
import csv
import datetime
import hashlib
import json
import re
import subprocess
import sys

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
DESK = ROOT / 'AGENTS/WALTER'
PLAN = json.loads((OUT/'dispatch-plan.json').read_text())
EXEMPT = {'CARL','RED','PROME','TERRY'}
def run(args):
    r = subprocess.run(args,cwd=ROOT,capture_output=True,text=True)
    if r.returncode: raise RuntimeError(f'{args!r}: {r.stdout}\n{r.stderr}')
    return r.stdout.strip()
def write_new(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x') as f:f.write(text)
def append(path,rows):
    with path.open('a',newline='') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerows(rows)

if sys.argv[1:] != ['--apply']:
    print('Review dispatch-plan.json and drafts/ first; --apply writes the declared paths and creates one scoped local commit.')
    raise SystemExit()

destinations=[]
for s in PLAN:
    destinations.append(ROOT/'BOARD'/Path(s['draft_path']).name)
    for recipient in dict.fromkeys(s['action']+s['info']):
        if recipient=='TERRY' or (recipient in EXEMPT and recipient not in s['action']):continue
        destinations.append(ROOT/f'AGENTS/{recipient}/inbox/WALTER/{s["id"]}.md')
memo=ROOT/'PROME/inbox/2026-10-14_from-WALTER_morning-news-boot.md'
destinations.append(memo)
assert not any(p.exists() for p in destinations), 'Create-only collision: re-review the plan, never overwrite.'
old_ids=set(re.findall(r'^signal_id:\s*["\']?(SIG-W-\d{8}-\d{3})', '\n'.join(p.read_text()[:1000] for p in (ROOT/'BOARD').glob('SIG-W-20261014-*.md')),re.M))
assert not old_ids.intersection(s['id'] for s in PLAN), 'Signal-ID collision.'
route=[];delivery=[]
for s in PLAN:
    board=ROOT/'BOARD'/Path(s['draft_path']).name
    write_new(board,Path(s['draft_path']).read_text())
    route.append([s['stamp'],s['id'],'; '.join(x[0] for x in s['sources']),s['title'],s['precedence'],','.join(s['action']),','.join(s['info']),f"{s['confidence']:.2f}"])
    for recipient in dict.fromkeys(s['action']+s['info']):
        if recipient=='TERRY' or (recipient in EXEMPT and recipient not in s['action']):continue
        role='ACTION' if recipient in s['action'] else 'INFO'
        path=ROOT/f'AGENTS/{recipient}/inbox/WALTER/{s["id"]}.md'
        ask=s['ask'] if role=='ACTION' else 'Information only; no recipient-directed task or new research commission.'
        text=f'# WALTER handoff — {s["id"]}\n\n**BOARD:** `{board.relative_to(ROOT)}`\n**Priority:** {s["precedence"]}\n**Role:** {role}\n**From:** WALTER\n**Date:** {s["stamp"]}\n\n## Kernel\n\n{s["body"]}\n\n## Why you got this\n\n{recipient} is on the canonical {s["domain"]} routing line; actor, geography, property and sector axes checked.\n\n## Requested action\n\n{ask}\n\n## Confidence / caveats\n\nConfidence {s["confidence"]:.2f}; source/read/measurement limits are retained in the kernel and BOARD source section. Evidence at AGENTS/WALTER/research/2026-10-14_morning-news/. Owner integration is UNKNOWN. Only the recipient owner integrates and files this packet; a read-only helper must not consume or move it.\n\n## Cross references\n\n{board.relative_to(ROOT)}; WALTER LAST_COMPLETION.md.\n'
        write_new(path,text)
        delivery.append([s['stamp'],s['id'],recipient,role,'CLAUDE_CODE',s['precedence'],str(path.relative_to(ROOT)),'written_not_delivered_pending_push','Runtime-neutral create-only own packet; legacy platform schema token. Fleet liveness UNKNOWN; not DARK, no doorbell. Published/delivered/consumed remain distinct.'])
append(DESK/'routed/route_log.tsv',route)
append(DESK/'routed/delivery_log.tsv',delivery)
append(DESK/'registry/FALSIFICATION_FIRED_LOG.tsv',[['RED-FT-08','2026-10-14','3.2472160702','SIG-W-20261014-001','sustain1; Decimal TableA Jul0.2/Aug0.3/Sep0.3; S50 preregistered basis; owner score execution UNKNOWN']])
token=PLAN[9]
append(DESK/'registry/CORRECTIONS.tsv',[['COR-20261014-10','2026-10-14','WALTER','VULCAN,HENRY,RED,PROME',str((ROOT/'BOARD'/Path(token['draft_path']).name).relative_to(ROOT)),'2026-10-28','LIVE','EXTERNAL zerohedge said unrestricted Anthropic all-time-low; IS dated Ornn blended index with posted/executed primary method conflict; no nominal rate-cut or full-history conclusion','WEAKEN']])

dispositions=[('FOLD','SIG-W-20261014-001'),('FOLD','SIG-W-20261014-001; BLS real earnings used, cumulative chart is a separate basis'),('KILL','Unsupported anonymous unnamed-bank/forward-distress claim; credibility gate, not framing-false'),('DISPATCH','SIG-W-20261014-010'),('DISPATCH','SIG-W-20261014-011'),('FOLD','SIG-W-20261014-001'),('DUP','BM-20261014-02 item23 / BM-20261014-03 items2,5; same Bloomberg CFTC report, no manipulation finding'),('FOLD','SIG-W-20261014-001'),('NO-ACTION','Qualified Greenland interview pushback saved in verifier; no impending production established or existing supply figure replaced'),('DISPATCH','SIG-W-20261014-006'),('FOLD','SIG-W-20261014-001; consensus/historical rank not independently adopted'),('DUP','BM-20261014-03 items2,5; same CFTC report, no new investigative commission'),('DISPATCH','SIG-W-20261014-007'),('DISPATCH','SIG-W-20261014-009'),('DISPATCH','SIG-W-20261014-008'),('FOLD','SIG-W-20261014-001; rate-expectation causal claim not adopted'),('NO-ACTION','Demographic projection/opinion; source units/vintage/AI causal claim unresolved'),('KILL','Chart NH2% fails its own strict<1.5% confirmation criterion; no authenticated crash outcome'),('NO-ACTION','May2026 coding-process compilation; no financial-news delta or workflow change')]
captured=json.loads((OUT/'captured-ids.json').read_text())
mapping=[]
for i,(disposition,ref) in enumerate(dispositions,1):
    run(['python3','AGENTS/WALTER/tools/batch_manifest.py','--item','BM-20261014-05',str(i),disposition,ref])
    mapping.append({'item':i,'bookmark_id':captured[i-1],'disposition':disposition,'ref':ref})
run(['python3','AGENTS/WALTER/tools/batch_manifest.py','--close','BM-20261014-05'])
(OUT/'bookmark-dispositions.json').write_text(json.dumps(mapping,indent=2))
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
append(DESK/'filtered/kill_log.tsv',[[stamp,'X trackingcosts / 2110346655270645863','Anonymous mortgage>half/auto>2008 recession assertion','credibility',.2,'No bank/date/denominator/records; future about-to-be distress in numerator. INDETERMINATE UNSUPPORTED, not FALSE.'],[stamp,'X ClaytonCharts / 2110101127786324118','Confirmed Titanic label fails chart own NH threshold','credibility',.3,'NH2% datedOctober12 versus strict<1.5%; preliminary signal differs. No independently verified crash thesis.']])
for name in ['route_log.tsv','delivery_log.tsv']:
    path=DESK/'routed'/name
    text=path.read_text()
    if text.startswith('#') and 'Last re-pull ATTEMPTED:' in text:
        text=re.sub(r'^# Last re-pull ATTEMPTED:.*$',f'# Last re-pull ATTEMPTED: 2026-10-14 ({stamp}; scoped morning12 signals/44 hands, not full historic census)',text,count=1,flags=re.M);path.write_text(text)
run(['python3','AGENTS/WALTER/tools/gen_board_index.py','--write','BOARD/INDEX.md','--cutover'])

# These files were read in the parent turn; retain exact before-images and open duties.
for name in ['LAST_COMPLETION.md','STATUS.md','REGISTRY.tsv','SESSION_LOG.md']:
    backup=OUT/('before-'+name)
    if not backup.exists():backup.write_bytes((DESK/name).read_bytes())
status=(DESK/'STATUS.md').read_text()
status=status.replace('| Credit | FRED MIRROR HY311bp/CCC1253bp [October12];HY9bp/2.8125% below strict>320,0/3;CCC fire banked,no repeat. October12 bond holiday may carry cash series,not a fresh independent witness. October13 credit print unavailable. |','| Credit | FRED mirror HY316bp/CCC1267bp [October13], retrieved October14 16:12Z. HY4bp/1.25% below strict>320 on that dated print,0/3; +5bp versusOctober12, no+25bp bypass. CCC prior fire banked/no repeat. |')
status=status.replace('| Volatility | FRED MIRROR VIXCLS15.21 [October12];banked state,exit>=18 not met. CBOE PRIMARY SKEW155.06 [October12] after154.34 [October9],2/4 at>=150;October13 publisher bar absent. Watch routed005;no fire. |','| Volatility | FRED mirror VIXCLS15.27 [October13]; registered exit>=18 not met. CBOE PRIMARY SKEW154.74 [October13], after154.34/155.06 [October9/12]:3/4>=150, watch SIG-W-20261014-012; October14 official close absent/no early fire. Intraday VIX16.23 from16:12Z vendor pull is not a closing grade. |')
status=status.replace('SOFR3.87−IORB3.90=-3bp [matchedOctober9]','SOFR3.89−IORB3.90=-1bp [matchedOctober13]')
status=status.replace('## DATED MARKET OBSERVATIONS — retrieved October13 23:08Z','## DATED MARKET OBSERVATIONS — bounded refresh October14 16:12Z; unchanged rows retain prior dates')
status=status.replace('| Banks | Vendor datedOctober13 KRE69.06,WAL73.73,OZK45.08;singlepull,not independent closecertification. WAL existing cycle2:no >=81.90 exit;no repeatfire. Issuer Q3workout outcomes remainpending. |','| Banks | Vendor intraday October14 at16:12Z: KRE68.65/WAL72.14/OZK44.84; not closes. October13 vendor prior closes69.06/73.73/45.08 retain single-source limits; WAL existing cycle2/no exit/repeat. BAC/MS issuer Q3 counterevidence routed004; regional workout outcomes remain owner-gated. |')
status=status.replace('| Labor | ICSA197K [weekendingOctober3,current revisedFRED mirror];no first-release recertification. |','| Labor / inflation | ICSA197K [weekendingOctober3,FRED revised mirror];no first-release recertification. BLS September headline0.6/core0.3 m/m; TableA Jul0.2/Aug0.3/Sep0.3=>3.247216% annualized, qualifies RED-FT08. RED execution UNKNOWN. Real hourly earnings-0.5%m/m/-0.7%y/y; November composition resolver remains open. |')
(DESK/'STATUS.md').write_text(status)
continuity=(DESK/'LAST_COMPLETION.md').read_text()
continuity=re.sub(r'^# WALTER LAST_COMPLETION.*\nRuntime:.*\n',f'# WALTER LAST_COMPLETION — October14 morning catch-up\nRuntime: OpenAI Codex/GPT-6 family; exact variant/native UUID UNKNOWN; thread /root. Updated {stamp}. Will-launched11:55EDT; bounded morning routing/Tier1 persistence, no end-of-day closeout.\n',continuity,count=1)
def section(name,new):
    global continuity
    continuity=re.sub(r'(?ms)^## '+re.escape(name)+r'\n.*?(?=^## |\Z)','## '+name+'\n\n'+new+'\n\n',continuity,count=1)
section('STATUS','Boot PARTIAL: rules/state/registries loaded with scoped access limits; no full market clearance.12 morning signals/44 create-only hands,3 IMMEDIATE/9 PRIORITY; one FT08 qualification, one external Ornn correction;19 bookmark dispositions in CLOSED BM-20261014-05. Exact marking only after this source commit. Three RULE9 read-only helpers explicitly done; no owner launch. Prior72 batch stays complete.')
section('CHANGED','12 BOARD packets/generated INDEX, route/delivery/kill/fire/correction/batch ledgers; bounded STATUS market rows and LAST_COMPLETION;19-ID captured mapping and source receipts under research/2026-10-14_morning-news. REGISTRY headers reviewed; exact creates only in recipient lanes/PROME. No foreign state changes.')
section('RESULT','Official CPI qualifies RED-FT08 at3.247216% TableA annualized; RED owns integration/weight execution. Singapore MPA names GFS Pride sinking and GFS Giselle strike; mine mechanism and owner loss census unresolved. IEA crude/product split, BAC/MS counterevidence, ASML guidance, Redfin September/Florida, Netflix global cuts,2027 COLA, attributed StarShield and qualified Cato/Ornn inputs saved. CBOE October13 recovered, SKEW3/4/no early fire.19 bookmarks fully dispositioned; CFTC repeats fold into prior review.')
gaps='Source/local persistence and19-ID marking are separate from origin publication/actual recipient consumption. Foreign REGINALD/FORGE/PROME work observed; main-repo pull and self-push deferred under root protocol; exact source commit receipt follows. No verified native fleet transport or absence; UNKNOWN recipients never doorbelled.\n\nBoot/source scope: local CLAUDE70,223B exceeds budget/cap; basis29MATCH certifies declaration only. Four registry families48 rows loaded (RED12/REG8/CREED11/HANS17); daily/compound HANS closes, monthly/qualitative rows, fresh Cushing/official futures not comprehensively graded. FRED credit/VIX latestOctober13; H15 latestOctober9; fixed futures contract-month probe incomplete, no settlement grade. Iran full clock remainsOctober8; current MPA/Reuters leg does not reset it. ASML/Redfin/SSA/MPA some publisher bodies accessible only as extended indexed text; original Netflix memo/StarShield notice/Bloomberg full story remain unavailable.\n\nResearch-Intake clean ff-only pull already-up-to-date; snapshotOctober13,6 feedsOK/1 missed weekday run. Prior27 items remain dispositioned but body-gapped/unmarked; no silent bulk mark. Phone lane absent/no pending files, drop-zone0, top-level inbox0, REQ queue0; no active liaison. Existing physical-diesel/source/broker/Will-design duties below retained; DEWEY final complete/no new commission.'
section('GAPS / OWED',gaps)
old_will=continuity.split('## WILL_NEEDS\n',1)[1].split('## FOLLOW-UP',1)[0]
choices=next((p for p in old_will.split('\n\n') if 'WQ401' in p),'')
section('WILL_NEEDS','No new research/trade decision. '+choices+'\n\nTERRY October14 12:08EDT owner receipt now books QQQ744P closed and QQQ740P October15 reduced to3; these discharge the old QQQ744P carry. USO October14 150C x2 still carries today’s expiry rail in that dated receipt; current working orders/fill times UNKNOWN. VLO2total/original1 scope/secondUNKNOWN and other existing cards remain at TERRY. This is owner evidence, not a current broker snapshot or new WALTER trade recommendation.')
continuity=re.sub(r'(?ms)^\*\*Resume point:\*\*.*?(?=^1\.)','**Resume point:** inspect research/2026-10-14_morning-news/ source/commit/mark receipts and pending publication; read owner acknowledgment before claiming integration. FT08 owner execution, MPA identity/census and today’s eventual CBOE4th bar remain separate. Prior72/48 bookmark batches stay complete;19 captured morning IDs must never repeat after exact source-backed mark. Intake body gaps retain old dispositions; no new deep research or trade.\n\n',continuity,count=1)
continuity=continuity.replace('October12 CBOE155.06 recovered;2/4,October13 bar absent;no earlyfire.','October13 official154.74 recovered after155.06/154.34:3/4;SIG-W-20261014-012;no earlyfire beforeOctober14 publisher close.')
continuity=continuity.replace('This batch added exactly72 after source commit;verified726 processed/0 staged.','Prior batch added exactly72 after source commit,726 processed. Morning19 exact IDs are fully dispositioned; mark only after new source commit, expected745 processed/0 staged; verify actual result in mark-proof.json.')
receipt={'schema':1,'as_of':stamp,'publication':[],'delivery':{'signal_date':'20261014','total':len(delivery),'delivered':0,'note':'Written local/source commit pending; no origin or owner acknowledgment inferred.'},'push':{'all_walter_commits_on_origin':False,'note':'Foreign work; main pull/self-push deferred. Old receipt preserved in before-LAST_COMPLETION.md.'},'owner_review':{'scope':'Source and scoped owner evidence read; actual recipient integration UNKNOWN','evidence':[]},'owed':['Coordinated publication and recipient integration','RED FT08 execution; FALCON MPA identity/loss-census grade','CBOE October14 final close; source-limited remaining registry coverage','Existing intakebody/diesel/source/design duties retained in FOLLOW-UP'],'next_review':'2026-10-14','procedure':{'tier':'light','scope':'Morning routing persistence, no whole procedure/full market clearance','claim':'PARTIAL boot; bounded release/credit/vol coverage'},'manual_duties':{'helpers':'Three bounded read-only helpers explicitly complete; thread-local inventory is not fleet census','16':'Scoped local source commit; no foreign changes/push','15':'Before-image preserved; carried open choices/designs retained','Tier1':'Affected market observations/current duty strings refreshed; old dates retained elsewhere','root.memory':'No auto-memory edit','root.retirement':'Morning routing only; prior full-closeout retirement review retained, no move','root.ledger_nudge':'Route/delivery/kill/fire/correction/batch event rows updated; no invented historic/full census'}}
continuity=re.sub(r'(?s)<!-- CLOSEOUT_RECEIPT_JSON.*?END_CLOSEOUT_RECEIPT -->','<!-- CLOSEOUT_RECEIPT_JSON\n'+json.dumps(receipt,indent=2)+'\nEND_CLOSEOUT_RECEIPT -->',continuity,count=1)
(DESK/'LAST_COMPLETION.md').write_text(continuity)
session=(DESK/'SESSION_LOG.md').read_text();(DESK/'SESSION_LOG.md').write_text(f'# {stamp} — morning routing / light-closeout — full deferred\n12 signals/44 handoffs;19 bookmarks CLOSED/mark after source commit;FT08 qualified,SKEW3/4. BootPARTIAL/source clocks explicit;publication/owner consumption UNKNOWN. Evidence research/2026-10-14_morning-news;duties LAST_COMPLETION.\n\n'+session)

headers=json.loads((OUT/'owner-headers.json').read_text())
rows=list(csv.DictReader((DESK/'REGISTRY.tsv').open(),delimiter='\t'));fieldnames=list(rows[0])
for row in rows:
    name=row['Agent'];head=headers.get(name)
    if not head:continue
    lines=[line for line in head.splitlines() if re.search(r'Updated|Last real data refresh|CURRENT STATE|Closeout October13',line,re.I)]
    if not lines:continue
    first=lines[0];match=re.search(r'2026-\d{2}-\d{2}',first)
    if match and match.group(0)>=row['Updated']:
        row['Updated']=match.group(0);row['Focus']=f'Header-only morning review {stamp}; owner evidence: '+first[:500].replace('\t',' ')
with (DESK/'REGISTRY.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)

completion=f'## COMPLETION — WALTER — 2026-10-14\nSTATUS: ⚠️ PARTIAL\nCHANGED: BOARD twelve signals, WALTER route/delivery/fire/correction/kill/batch/state artifacts,44 recipient handoffs.\nRESULT:12 morning signals;19 captured bookmarks fully dispositioned;FT08 qualified at3.247216%,SKEW3/4,MPA named sinking.\nGAPS: Boot/source coverage partial; foreign work blocks pull/self-push; source commit/mark/publication and actual consumption separate.\nWILL_NEEDS: No new decision; existing USO expiry and cards remain TERRY/Will-owned.\nFOLLOW-UP: RED owner execution,FALCON census,official October14 SKEW close,coordinated publication and existing source duties.\n'
write_new(memo,'# WALTER morning news and boot — October14\n\nEvidence: `AGENTS/WALTER/research/2026-10-14_morning-news/`; live duties: `AGENTS/WALTER/LAST_COMPLETION.md`.\n\nNo owner launch; three RULE9 helpers explicitly complete. Native fleet transport unavailable/unverified; source packet does not establish acknowledgment. Desk state and recorded grades stay owner-held. The new MPA sinking is named flag-state evidence, not an authenticated mine mechanism or barrel count. RED preregistered core basis selects TableA; source qualification is not owner score execution.\n\n'+completion)
ownmemo=DESK/'outbox/2026-10-14_morning-news-boot.md';write_new(ownmemo,memo.read_text())

doctor=subprocess.run(['python3','AGENTS/WALTER/tools/walter_doctor.py'],cwd=ROOT,capture_output=True,text=True)
(OUT/'doctor-after.txt').write_text(doctor.stdout+doctor.stderr)
high=[line for line in (doctor.stdout+doctor.stderr).splitlines() if re.search(r'[⚠❌].*\bHIGH\b',line)]
if high:raise RuntimeError('Doctor HIGH findings require resolution before commit: '+repr(high))
# Every own path is explicitly recorded; preexisting foreign index entries remain untouched.
ownchanged=run(['git','status','--porcelain','--untracked-files=all','--','AGENTS/WALTER']).splitlines()
owned=[]
for line in ownchanged:
    path=line[3:]
    if '.cache/' in path or '__pycache__/' in path:continue
    if ' -> ' in path:raise RuntimeError('Unexpected owned rename requires archive review: '+line)
    if path.startswith('AGENTS/WALTER/'):owned.append(path)
paths=sorted(set(owned+[str(p.relative_to(ROOT)) for p in destinations]+['BOARD/INDEX.md']))
(OUT/'committed-paths.json').write_text(json.dumps(paths,indent=2))
paths.append(str((OUT/'committed-paths.json').relative_to(ROOT)))
(OUT/'source-packet-hashes.json').write_text(json.dumps({str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in destinations},indent=2));paths.append(str((OUT/'source-packet-hashes.json').relative_to(ROOT)))
message=OUT/'commit-message.txt';message.write_text('WALTER -> fleet: route October14 morning releases and19 bookmarks\n\n12 source-qualified signals/44 create-only handoffs; core TableA fire and dated SKEW watch. Source/owner caveats retained, no owner grade or trade. Event ledgers refreshed; wider monthly/qualitative/source coverage explicitly partial. Foreign work untouched; pull/self-push deferred.\n');paths.append(str(message.relative_to(ROOT)))
run(['git','add','--']+paths)
result=run(['git','commit','-F',str(message),'--']+paths)
sha=run(['git','rev-parse','HEAD'])
(OUT/'source-commit.json').write_text(json.dumps({'commit':sha,'result':result,'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'state':'LOCAL_COMMITTED; publication/consumption UNKNOWN','paths':paths},indent=2))
print(result)
print(f'Source commit {sha};12 signals/{len(delivery)} hands. Source-backed marking remains a separate next step. No push.')
