"""Prepare/review first; apply two create-only source packets and an exact-path commit.

No DEWEY launch/queue file, push, pull, owner-state edit or external send.
"""
from pathlib import Path
import csv
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess
import sys

OUT = Path(__file__).resolve().parent
DESK = OUT.parents[1]
ROOT = DESK.parents[1]
REL = 'AGENTS/WALTER/research/2026-10-14_three-thread-verification'
def run(argv):
    p = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
    if p.returncode:
        raise RuntimeError(f'{argv!r}: {p.stdout}\n{p.stderr}')
    return p.stdout
def create(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x') as f:
        f.write(content)
def append(path, rows):
    with path.open('a', newline='') as f:
        csv.writer(f, delimiter='\t', lineterminator='\n').writerows(rows)

if sys.argv[1:] == ['--prepare']:
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    signals = [
        dict(id='SIG-W-20261014-013', slug='ports-pike-study-rights-cost-allocation-gates',
             title='PORTS-Pike filing separates proposed capacity, payment commitments and connection rights',
             domain='POWER_GRID', cluster='AI_INFRA_CAPEX', entities=['PJM','PORTS-Pike','SB-Energy','AEP-Ohio','OpenAI','PUCO','FERC'],
             action=['WATT','VULCAN'], info=['HENRY','RED','PROME'], confidence=.88, language='reports',
             body="PJM's October13 ER27-126-000 filing describes PORTS-Pike's initial800MW separately from proposed additional9,570MW load/10,170MW gross generation through2032. These are planned populations, not IT MW, contracted capacity or delivered generation. The filing represents SB Energy infrastructure-payment commitments independent of usage, with actual allocation/recovery subject to PUCO/FERC proceedings. The study grants no construction/interconnection rights. Its120-day PUCO-action condition follows the Final System Upgrade Report and can be extended; no calendar deadline/start is established here. Proposed generation and developer payments are counterevidence to assuming all costs fall on other ratepayers. No named loss, delay outcome or net spare capacity is established. Project/phase context is already VULCAN-owned; the filing is the new document-level lead.",
             sources=[['PJM ER27-126-000, October13; extracted PDF pp8-10/13-14, scoped read','https://www.pjm.com/pjmfiles/directory/etariff/FercDockets/9925/20261013-er27-126-000.pdf']],
             ask='WATT/VULCAN: assess the filing within existing project/power work; distinguish proposed load/gross generation, payment commitments and granted connection rights. Contract/approval bridge is a prepared DEWEY candidate, not an accepted commission or owner launch.',
             read='Helper recovered linked PDF extraction; parent independently read critical extracted passages. Direct PDF opening inconsistent; no full44-page/raw-PDF authentication. Existing DOE/DR findings fold into SIG-W-20261013-007.', candidate=True),
        dict(id='SIG-W-20261014-014', slug='diesel-retail-relief-fedex-surcharge-pass-through',
             title='Diesel retail relief reaches published FedEx ground surcharge; margin losses remain unmeasured',
             domain='OIL_ENERGY', cluster='INFLATION_TRANSMISSION', entities=['EIA','FedEx','US-on-highway-diesel'],
             action=['BRENT','CARL'], info=['HENRY','LIQUID','RED','PROME'], confidence=.93, language='confirmed',
             body="EIA's October14 posting observes October12 US on-highway diesel$6.179/gallon,−$0.020w/w,+$2.514y/y; September28/October5 were$6.382/$6.199. FedEx's October12–18 ground/home/international-ground/pickup surcharge is28.75%, versus29.25% October5–11, using October5 versus September28 diesel. The published mechanism transmits costs with a lag; individual customer agreements control. Other package/air services use jet fuel. Falling prices/surcharges and carrier recovery challenge uninterrupted acceleration and automatic carrier-margin-loss claims. This is a price/invoicing channel, not measured current invoices, net margins, diesel-to-core CPI causality or proof of Russian delivered additions. August PPI is already SIG-W-20260910-005; September PPI remains scheduled October15 08:30ET. No repeat cargo study or automatic monitoring commissioned.",
             sources=[['EIA posting October14; observations October12','https://www.eia.gov/petroleum/gasdiesel/'],['FedEx current October12–18 weekly schedule and contract caveat','https://www.fedex.com/en-us/shipping/fuel-surcharge.html'],['BLS August PPI release September10; next September print October15','https://www.bls.gov/news.release/ppi.nr0.htm']],
             ask='BRENT/CARL: integrate dated retail relief and the surcharge transmission mechanism into existing energy/consumer work. Preserve payer, contract-lag and margin-perimeter distinctions; no company-specific loss or new study presumed.',
             read='Parent independently opened EIA/FedEx bodies and the BLS next-release line. Public schedules are observed; actual contract/invoice/margin outcomes remain unknown.', candidate=False),
    ]
    for s in signals:
        s['stamp'] = stamp
        s['precedence'] = 'PRIORITY'
        s['filename'] = s['id']+'-'+s['slug']+'.md'
        fields = {'signal_id':s['id'],'date':'2026-10-14','timestamp':stamp,'dispatched':stamp,'source':'WALTER',
                  'origin':[x[0] for x in s['sources']], 'domain':s['domain'],'cluster':s['cluster'],'entities':s['entities'],
                  'precedence':'PRIORITY','action':s['action'],'to':s['action'],'info':s['info'],'confidence':s['confidence'],
                  'confidence_language':s['language'],'resources':1,'signal_type':'research','safety_net':'clear','event_window':'closed',
                  'word_count':len(s['body'].split()),'dispatch_note':'Will-authorized three-thread framing verification; three read-only helpers complete. No owner or DEWEY launch; publication and consumption separate.'}
        if s['candidate']:
            fields['dispatch_note'] += ' deep_research_candidate: T5 — executed rights, payment security and delay cost bearers.'
            fields['confidence_note'] = 'Filing representation confirmed at extracted primary body; no independent operating/cost outcome or complete agreement/raw-PDF read.'
        else:
            fields['cluster_secondary'] = 'HYDROCARBON_INFRA'
            fields['consumer_transmission'] = 'pump_pass_through'
        # Legacy parsers require unquoted scalar timestamp/cluster strings.
        plain={'signal_id','date','timestamp','dispatched','source','domain','cluster','precedence','confidence_language','signal_type','safety_net','event_window','cluster_secondary','consumer_transmission'}
        header='---\n'+'\n'.join(k+': '+(v if isinstance(v,str) and k in plain else json.dumps(v,ensure_ascii=False)) for k,v in fields.items())+'\n---\n'
        source_lines='\n'.join('- ['+label+']('+url+')' for label,url in s['sources'])
        text=header+'\n# '+s['title']+'\n\n'+s['body']+'\n\n## Source and read scope\n\n'+source_lines+'\n\n'+s['read']+'\n\n## Requested action\n\n'+s['ask']+'\n'
        if s['candidate']:
            text+='\n## 🔬 Deep-research prompt (candidate)\n\n'+(OUT/'DEWEY-power-candidate.md').read_text()
        create(OUT/s['filename'],text)
    create(OUT/'dispatch-plan.json',json.dumps(signals,indent=2,ensure_ascii=False)+'\n')
    print('Prepared two drafts, seven recipient handoffs, one DEWEY candidate; no fleet writes or commission launch.')
    raise SystemExit()

if sys.argv[1:] != ['--apply']:
    raise SystemExit('Use --prepare, review drafts/plan, then --apply with required filesystem/Git permission.')
signals=json.loads((OUT/'dispatch-plan.json').read_text())
exempt={'CARL','RED','PROME','TERRY'}
dest=[]
for s in signals:
    dest.append(ROOT/'BOARD'/s['filename'])
    for recipient in dict.fromkeys(s['action']+s['info']):
        if recipient=='TERRY' or (recipient in exempt and recipient not in s['action']):
            continue
        dest.append(ROOT/f'AGENTS/{recipient}/inbox/WALTER/{s["id"]}.md')
memo=ROOT/'PROME/inbox/2026-10-14_from-WALTER_three-thread-verification.md'
dest.append(memo)
assert not any(p.exists() for p in dest), 'Create-only collision; re-review, never overwrite.'
existing='\n'.join(p.read_text()[:1000] for p in (ROOT/'BOARD').glob('SIG-W-20261014-*.md'))
assert all(not re.search(r'^signal_id:\s*'+re.escape(s['id'])+r'\s*$',existing,re.M) for s in signals)
assert 'REQ-DEWEY-20261014-001' not in (DESK/'registry/DEEP_RESEARCH_FLAGGED_LOG.tsv').read_text()
staged_before=run(['git','diff','--cached','--name-only']).splitlines()
# Root Git protocol uses explicit pathspec commits to preserve unrelated index work.
# Stop only for overlap; never unstage or sweep another desk's staged changes.
assert not [p for p in staged_before if p.startswith('AGENTS/WALTER/') or p=='BOARD/INDEX.md' or p in {str(x.relative_to(ROOT)) for x in dest}], 'Staged overlap: review before writing.'
create(OUT/'preexisting-staged.txt','\n'.join(staged_before)+'\n')
for name in ['LAST_COMPLETION.md','SESSION_LOG.md']:
    create(OUT/('before-'+name),(DESK/name).read_text())
routes=[]
delivery=[]
for s in signals:
    create(ROOT/'BOARD'/s['filename'],(OUT/s['filename']).read_text())
    routes.append([s['stamp'],s['id'],'; '.join(x[0] for x in s['sources']),s['title'],s['precedence'],','.join(s['action']),','.join(s['info']),f'{s["confidence"]:.2f}'])
    for recipient in dict.fromkeys(s['action']+s['info']):
        if recipient=='TERRY' or (recipient in exempt and recipient not in s['action']):
            continue
        role='ACTION' if recipient in s['action'] else 'INFO'
        path=ROOT/f'AGENTS/{recipient}/inbox/WALTER/{s["id"]}.md'
        ask=s['ask'] if role=='ACTION' else 'Information only; no directed task, priority change or research commission.'
        create(path,f'# WALTER handoff — {s["id"]}\n\nBOARD: BOARD/{s["filename"]}\nDate: {s["stamp"]}\nRole: {role}\nPriority: PRIORITY\n\n{s["body"]}\n\n## Requested action\n\n{ask}\n\n## Evidence and limits\n\n{s["read"]}\n\nEvidence: {REL}/REPORT.md. Recipient owns integration and filing. Read-only helpers must not consume/move this packet. Actual owner integration UNKNOWN; source publication and delivery separate.\n')
        delivery.append([s['stamp'],s['id'],recipient,role,'CLAUDE_CODE','PRIORITY',str(path.relative_to(ROOT)),'written_not_delivered_pending_push','Codex runtime; legacy schema token. Create-only; no recipient state edits. Fleet liveness UNKNOWN, no DARK/doorbell inference.'])
append(DESK/'routed/route_log.tsv',routes)
append(DESK/'routed/delivery_log.tsv',delivery)
append(DESK/'registry/DEEP_RESEARCH_FLAGGED_LOG.tsv',[[
    '2026-10-14','REQ-DEWEY-20261014-001','T5 verify-left-material-uncertainty; T3 load-bearing contract evidence','AI_INFRA_CAPEX',
    'PORTS-Pike: which connection rights/payment obligations are executed, which approvals pending, and who bears delay/underutilization costs?',
    'WATT/VULCAN connection-readiness and project-cost assessment; no preset loss/weight change',
    'BOARD/'+signals[0]['filename'],'open','PENDING','Prepared candidate only; no DEWEY accepted commission or launch','DEWEY',
    'Will authorized three-thread investigation and asked division of work; source verification complete, specific deep commission remains proposed. '+REL+'/DEWEY-power-candidate.md','']])
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
pickup=f'## CURRENT PICKUP — {stamp} — three-thread verification\n\nWill authorized looking into power/AI, diesel/cost transmission and insurer/private-credit funding; this supersedes earlier no-new-research wording only for this bounded pass. Three read-only helpers returned and explicitly closed. Evidence: {REL}/REPORT.md. Two PRIORITY source packets013/014, seven create-only hands; one prepared DEWEY power-contract candidate REQ-DEWEY-20261014-001, not an accepted commission/launch. Existing diesel commission remains closed. Insurer evidence/acquisition stays SHADE/WQ422; no gated statutory dig or owner grade. All three underlying economic questions retain explicit gaps.\n\nPublication/delivery/consumption of this new source set remain pending until separately evidenced. No native fleet presence/transport or recipient acknowledgment claimed. No new Will permission question; a DEWEY owner session has not been opened. Existing unrelated source/design obligations and all prior receipts below remain retained with their dates. No positions involved.\n\n'
p=DESK/'LAST_COMPLETION.md'
old=p.read_text()
pos=old.index('## STATUS')
p.write_text(old[:pos]+pickup+old[pos:])
p=DESK/'SESSION_LOG.md'
p.write_text(f'# {stamp} — three-thread source verification / light closeout, full deferred\nTwo source packets013/014, seven handoffs; three read-only helpers closed. One prepared DEWEY power-contract candidate; no commission/owner launch. Insurer WQ422 source dependency, diesel margin/cargo uncertainty retained. Evidence {REL}/REPORT.md; source publication/consumption pending.\n\n'+p.read_text())
memo_text=f'# WALTER — three-thread verification\n\nWill authorized the investigation. Bounded source verification produced two source packets, one prepared DEWEY contract-bridge candidate, and no owner launch. Diesel supply commission remains closed; insurer acquisition remains existing SHADE/WQ422, not a new broad study.\n\nEvidence: {REL}/REPORT.md. Candidate: {REL}/DEWEY-power-candidate.md. Existing full boot/read-cap/market limits retain their dated receipts; this pass makes no full-clearance claim.\n\n## COMPLETION — WALTER — 2026-10-14\nSTATUS: ⚠️ PARTIAL\nCHANGED: Two BOARD packets, seven recipient handoffs, route/delivery/deep-candidate ledgers, own continuity/evidence.\nRESULT: Three bounded verification legs complete; source deltas are PORTS-Pike rights/cost gates and dated diesel/surcharge relief.\nGAPS: Raw/full power agreement and executed rights/cost outcomes, named unrecovered fuel costs, insurer statements remain unresolved; source publication/owner consumption separate.\nWILL_NEEDS: None for the completed verification; DEWEY assignment is a prepared candidate, not launched.\nFOLLOW-UP: Existing owners assess source packets; proposed focused DEWEY rights/payment bridge; preserve SHADE acquisition/gates and prior diesel closeout.\n'
create(memo,memo_text)
create(DESK/'outbox/2026-10-14_three-thread-verification.md',memo_text)
run(['python3','AGENTS/WALTER/tools/gen_board_index.py','--write','BOARD/INDEX.md','--cutover'])
doctor_process=subprocess.run(['python3','AGENTS/WALTER/tools/walter_doctor.py'],cwd=ROOT,capture_output=True,text=True)
doctor=doctor_process.stdout+doctor_process.stderr
create(OUT/'doctor-after.txt',doctor)
levels=re.findall(r'^\s*[✗⚠]\s+(HIGH|MED)\s+',doctor,re.M)
assert doctor_process.returncode==len(levels) and 'check raised ' not in doctor, 'Doctor failed to execute normally.'
assert 'HIGH' not in levels, 'Doctor HIGH: inspect before committing.'
own_files=['REPORT.md','DEWEY-power-candidate.md','apply_packets.py','power-er27-evidence.json','dispatch-plan.json','helper-closeout.json',
           'before-LAST_COMPLETION.md','before-SESSION_LOG.md','doctor-after.txt','preexisting-staged.txt']+[s['filename'] for s in signals]
paths=[REL+'/'+name for name in own_files]+[str(p.relative_to(ROOT)) for p in dest]+[
    'BOARD/INDEX.md','AGENTS/WALTER/routed/route_log.tsv','AGENTS/WALTER/routed/delivery_log.tsv',
    'AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv','AGENTS/WALTER/LAST_COMPLETION.md','AGENTS/WALTER/SESSION_LOG.md',
    'AGENTS/WALTER/outbox/2026-10-14_three-thread-verification.md']
manifest={'paths':paths,'destinations':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in dest},
          'hands':len(delivery),'publication':'UNKNOWN','integration':'UNKNOWN','dewey':'CANDIDATE_ONLY; not launched'}
create(OUT/'persistence-manifest.json',json.dumps(manifest,indent=2)+'\n')
paths.append(REL+'/persistence-manifest.json')
run(['git','add','--']+paths)
result=run(['git','commit','-m','WALTER -> WATT VULCAN BRENT CARL HENRY LIQUID: verify three research threads','--']+paths)
sha=run(['git','rev-parse','HEAD']).strip()
print(result)
print('SOURCE_COMMIT '+sha+'; 2 signals / '+str(len(delivery))+' hands; no push or DEWEY launch.')
