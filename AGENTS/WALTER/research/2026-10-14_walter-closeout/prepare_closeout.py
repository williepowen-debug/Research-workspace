"""Own-desk closeout write-back; no pull, push, foreign writes or owner grading."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import csv,hashlib,json,re,subprocess

OUT=Path(__file__).resolve().parent
DESK=OUT.parents[1]
ROOT=DESK.parents[1]
REL='AGENTS/WALTER/research/2026-10-14_walter-closeout'
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
before={name:(OUT/('before-'+name)).read_text() for name in ['LAST_COMPLETION.md','STATUS.md','MEMORY.md','REGISTRY.tsv','SESSION_LOG.md']}

# Step13 precedes the derived STATUS/network subsection. Status bands stay owner-held.
rows=list(csv.DictReader(before['REGISTRY.tsv'].splitlines(),delimiter='\t'))
headers={};missing=[]
for row in rows:
    p=(ROOT/'PROME/STATUS.md') if row['Agent']=='PROME' else ROOT/'AGENTS'/row['Agent']/'STATUS.md'
    if not p.exists():
        missing.append(row['Agent']);continue
    head='\n'.join(p.read_text().splitlines()[:30])+'\n'
    headers[row['Agent']]=head
    claims=[line for line in head.splitlines() if re.search(r'updated|closeout|last real data refresh',line,re.I)]
    if not claims:continue
    claim=claims[0]
    date=re.search(r'2026-\d{2}-\d{2}',claim)
    if date and row['Updated']<=date[0]<='2026-10-14':
        row['Updated']=date[0]
    row['Focus']='Header-only closeout review '+stamp+'; '+claim[:520].replace('\t',' ')
for row in rows:
    if row['Agent']=='WALTER':
        row['Updated']='2026-10-14'
        row['Focus']='Will-requested full context/persistence closeout;14 source packets today,19bookmark dispositions; no fresh closing-market grade. Duties LAST_COMPLETION.'
with (DESK/'REGISTRY.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
(OUT/'owner-headers.json').write_text(json.dumps({'observed_at':stamp,'scope':'First30lines only; source dates preserved; no fleet presence inference','headers':headers,'missing':missing},indent=2)+'\n')
stale=[f"{r['Agent']} {r['Updated']} ({r['Status']})" for r in rows if r['Updated']<'2026-10-01']
count=len(list((ROOT/'BOARD').glob('SIG-W-*.md')))
status=before['STATUS.md']
status=re.sub(r'^\*\*Updated:\*\*.*$',f'**Updated:** {stamp} — Will-requested FULL context/persistence closeout. BOARD **{count}**; October14 source set14 (3IMMEDIATE/11PRIORITY),19bookmark dispositions,6 bounded read-only verification helpers across the morning and three-thread passes. Source/boot market coverage remains PARTIAL. Current obligations and publication evidence: LAST_COMPLETION.md.',status,count=1,flags=re.M)
bottom='Morning CPI, shipping, energy, bank/AI/housing inputs and the later power-contract/diesel-surcharge findings have source-backed records. Bookmark access works; the745-ID ledger and prior dispositions are preserved. DEWEY is now running the approved power-contract question per Will; its final return is not yet consumed. Two later BOND/LIQUID owner-routing returns remain in the inbox. Research gaps, source clocks and current work belong to LAST_COMPLETION.md; this closeout does not certify current market conditions.'
status=re.sub(r'(?ms)^## BOTTOM LINE\n.*?(?=^## )','## BOTTOM LINE\n\n'+bottom+'\n\n',status,count=1)
status=status.replace('- Closeout evidence/manual duty outcomes: `research/2026-10-13_session-closeout/`.','- Closeout evidence/manual duty outcomes: `research/2026-10-14_walter-closeout/`.')
status=re.sub(r'(?m)^- X transport restored .*$', '- X access rechecked October14 16:54Z (HTTP200); read-only backlog check17:36Z found0unprocessed on the standard newest-first boundary.745processed/0staged; no token refresh or additional mark. Morning19 IDs remain source-backed; prior72/48 batch evidence remains historical. Sources: `research/2026-10-14_morning-news/`.',status,count=1)
network=f'REGISTRY reviewed at{stamp} before this derived subsection: {len(rows)}rows/{len(headers)}available STATUS headers at first30-line scope; {len(missing)}missing ({", ".join(missing)}). PROME resolved at the repository root. Owner dates/bands retained; header inspection is not complete owner evidence or fleet presence. Older dates: '+ '; '.join(stale)+'.\n\nOctober14 source set14:3IMMEDIATE/11PRIORITY;0cluster-mediating; one existing FT08 qualification, no additional owner grade. New BOND/LIQUID returns are queued for source routing. Six read-only verification helpers explicitly closed across two passes; Will reports DEWEY running independently. No WALTER owner launch or new doorbell.'
status=re.sub(r'(?ms)^## NETWORK AWARENESS\n.*?(?=^## )','## NETWORK AWARENESS\n\n'+network+'\n\n',status,count=1)
status=status.replace('scoped LOOSE for imminent CPI and bank-Q3 information','scoped LOOSE for the existing bank-Q3 catalyst window; CPI release is now past')
(DESK/'STATUS.md').write_text(status)

# Step14: preserve old session notes verbatim in SESSION_LOG; no durable lesson rewrite.
memory=before['MEMORY.md']; oldnotes=memory.split('## Session Notes\n',1)[1]
newnotes=f'**CHANGES SINCE — {stamp}, Will-requested full context/persistence closeout:** October14 source set14 signals/51owner packets,19bookmark dispositions;745processed/0staged. X and other intake health checks saved; six bounded verification helpers explicitly closed.\n**NEXT SESSION:** read LAST_COMPLETION.md; pick up BOND/LIQUID routing returns and DEWEY final handoff when delivered. Reuse prior source/mark evidence; retain dated market/source limitations and Will\'s scope correction.\nWill confirms DEWEY running; prior diesel commission remains closed. No new trade, monitor or unattended authority. Old session notes conserved verbatim in SESSION_LOG; existing October15 size trigger retained.\n'
(DESK/'MEMORY.md').write_text(memory.split('## Session Notes\n',1)[0]+'## Session Notes\n\n'+newnotes)
entry=f'# {stamp} — Will-requested FULL CLOSEOUT / context persistence and restart handoff\n\nOctober14 source set14signals/51hands;19captured bookmarks dispositioned,745processed/0staged. Fresh origin proof covers all prior WALTER source/metadata/mark/access/three-thread commits; current closeout commit follows. Seven delivery flags reconciled after fresh fetch. Registry refreshed before derived STATUS; MEMORY notes rewritten and prior notes conserved below. No new market grade; boot/source coverage remains PARTIAL. Two BOND/LIQUID owner-routing returns queued; Will reports DEWEY running, final handoff not consumed.\n\n## Prior MEMORY session notes — verbatim conservation\n\n'+oldnotes+'\n\n'
(DESK/'SESSION_LOG.md').write_text(entry+before['SESSION_LOG.md'])

# Specific pending commission now has direct operator start evidence, not completion.
p=DESK/'registry/DEEP_RESEARCH_FLAGGED_LOG.tsv'
lines=p.read_text().splitlines(); changed=0
for i,line in enumerate(lines):
    f=line.split('\t')
    if len(f)>1 and f[1]=='REQ-DEWEY-20261014-001':
        assert len(f)==13 and f[8]=='PENDING'
        f[9]='Will directly confirms DEWEY up and running on the approved PORTS-Pike assignment; final owner deliverable/handoff not yet consumed'
        f[11]+=' | '+stamp+': Will reports launch after receiving CodexSol command. Exact DEWEY session/model verification remains owner-held; no duplicate launch or source-resolution claim.'
        lines[i]='\t'.join(f);changed+=1
assert changed==1
p.write_text('\n'.join(lines)+'\n')

# Reuse today's verified no-age-candidate retirement result; all new paths dated today.
prior=json.loads((DESK/'research/2026-10-14_session-closeout/retirement-review.json').read_text())
(OUT/'retirement-review.json').write_text(json.dumps({'observed_at':stamp,'prior_full_review':prior,'new_work':'All session source/receipt additions datedOctober14, active and referenced. No candidate reached60days within this day. Existing16-file October12 cache remains unstaged/untouched; no archive/deletion performed.','disposition':'No retirement move justified; prior no-age-candidate result reused'},indent=2)+'\n')
owner=json.loads((OUT/'owner-review.json').read_text())
publication=json.loads((OUT/'publication-before.json').read_text())
design=before['LAST_COMPLETION.md'].split('## OPEN DESIGN DECISIONS\n',1)[1].split('## CLOSEOUT RECEIPT',1)[0]
evidence=[{'path':REL+'/owner-headers.json','sha256':hashlib.sha256((OUT/'owner-headers.json').read_bytes()).hexdigest(),'note':'Header-only registry context, not recipient integration.'}]+owner['evidence']
receipt={'schema':1,'as_of':stamp,'publication':publication['publication'],'delivery':{'signal_date':'20261014','total':51,'delivered':51,'note':'Freshly fetched origin proves all51; seven new rows reconciled. Actual owner integration separate.'},'push':{'all_walter_commits_on_origin':False,'note':'Prior source/mark/access/metadata commits origin-proven; current closeout/check receipt commit and authorized safe-push follow.'},'owner_review':{'scope':'manual evidence review; no automatic completion','evidence':evidence},'owed':['Two committed BOND/LIQUID owner-return routing packets remain in inbox; no silent consumption','DEWEY final power-contract handoff and then ledger/delivery audit','RED FT08 owner execution; FALCON loss-census grade; official October14 SKEW close and existing source-limited coverage','Existing intakebody/diesel/insurer/design duties retained below','Current closeout exact-path commit and authorized publication/receipt reconciliation'],'next_review':'2026-10-15','procedure':{'tier':'full','scope':'Full context/persistence write-back steps13,12,14,15,16; market boot/source coverage partial','claim':'Selected checks and final publication receipt follow; no full market-clearance claim'},'manual_duties':{'11':'Existing14 source packets/51hands and CLOSED19bookmark batch conserved;0newsignals in closeout. Two new owner returns read but remain queued/unfiled.','13':'46registry rows reviewed using41headers/5missing, before12b; bands and source dates owner-held.','12(a,b)':'BOARD count refreshed fromfiles; derived network regenerated afterregistry; no owner presence inference.','12(c)':'BALANCED unchanged; expired imminentCPI wording removed, existingbankcatalystposture retained.','12(d,e)':'New FULL session entry; BOTTOMLINErecut; older lightbreadcrumbs conserved as history.','12(f)':'Read-cap checker to run; oversized charter unresolved and outside this closeout scope.','14':'MEMORY sessionnotes rewritten; durable feedback retained; oldnotes conservedverbatim; line/byte counts saved below. No promotion/newauto-memory.','15':'Current obligation list overwritten, beforeimage saved; source/owner limitations retained.','16':'Will explicitly requested commit/push; freshsafe-push dryrun alreadyprovedpriorHEADonorigin. Exactownpaths only, no pull/rebase/stash/foreignstage; finalpushaftercommit.','root.retirement':'Prior same-day800trackedfile no-age-candidate census reused; allnewfiles datedtoday;0moves.','root.consumer':'No threshold/canonical figure supersession, no consumer scan condition selected.','root.orphans':'Rootadvisorycheck to run; oldcacheexcluded and allforeignworkuntouched.','helpers':'Six read-only helpers across two completedpasses; no newhelper/ownerlaunch. DEWEY nowrunning perWill.','mark':'745processed/0staged; read-only probes did not alter ledger.'},'selected_checks':'Full runner pending; inherited oversized-charter read-cap REVIEW expected; no full-procedure or market-clearance shortcut.'}
follow='''1. **New owner returns:** inbox/2026-10-14_from-LIQUID_ROUTE-credit-broadening-and-mixed-etf-redemptions.md requests dated IG/BBB/ETF context to REGINALD/BROCK/HENRY. BOND post-CPI return is also queued. Reports read and hash-pinned here; packets remain in place and are not claimed routed/consumed. Source figures retain October13/intraday cutoffs; no new threshold grade.
2. **DEWEY power:** REQ-DEWEY-20261014-001 is PENDING execution/return, now approved and running per Will. Do not duplicate its launch or consume its in-progress output. Await actual final handoff, inspect full returned report, verify direct recipient stubs, close audit row only on delivered evidence. Prior REQ-DEWEY-20261010-001 diesel study stays final/closed, underlying delivered supply/signed allocation/cargo/customs/ICE UNKNOWN. CARL-DR-1 remains PARTIAL/dueNov13, Q3pending.
3. **Source and research:** retain morning FT08 owner execution and FALCON MPA loss-census ownership; RED-FT10 October13 SKEW3/4, no earlyOctober14 close fire. Next existing Iran full targetOct15 (fullclockOct8); gas/refining OUT classification and FALCON clock not reset by partial source improvements. Intake27articles remain assessed/body-gapped/unmarked; source-access failures are not absence. Named diesel margins/actual deliveries and insurer SHADE/WQ422 documents remain unresolved under existing gates.
4. **Completed work:** do not repeat morning19, prior72/48 bookmark batches or oldDEWEY studies. Xprobe16:54ZHTTP200 and backlogprobe17:36Z0new retain their times; intakehealth17:43Z is not a continuing monitor. Latest collector snapshotOct13, sixjobsOK/one missedweekdayrun; phone delivery and Telegram access remain unverified.
5. **Existing owner returns/design:** retain LIQUID-1007, BRENT-1008/-003, VULCAN/BROCK-1009, FALCON gas/theater/UKMTO, OSPREY deal/1272 correction, YURI signedterms, BOND/ZHAO-004, HENRY/VULCAN-006, CORAL PembrokeLakes-1008-040, CREED Trepp-1009-002, SHADE Guggenheim, MARCO harness and VULCAN useful-life decisions. CARL SCF numerator already resolved KB504/529; TERRY/OZK prior integration observed, no universal reply obligation.
6. **Process:** XpilotreviewOct17 retains renewal/timeouts/WSL scope and no unattendedauthority. StalenesssweepOct24; MEMORYsizecalendarOct15 remains. WQ255/WQ388/WQ401 and existing Telegram/visibility/acceptance duties stay open at their owners. No GateC/scheduling activation. Oldposition/expiry carries removed from WALTER's live duties under Will's direct scope correction; exact prior text preserved in the beforeimage.
7. **Dated owner clocks:** existing WPSROct15noon/VLO basis/LIQ07Oct15–16, MTB/CFG/H8/tankerweeklyOct16, WALOct19–20, OZKOct20–21, FOMCOct27–28/UKBudgetOct28/ECBOct29, BZZ26LTD/boundary8 switches and TreasuryNov2/4 are prior owner-source pointers, not independently reverified calendar advice. No new WALTER position-management duty.
'''
last=f'''# WALTER LAST_COMPLETION — October14 full context/persistence closeout
Runtime: OpenAI Codex/GPT-6 family; exact variant/native session UUID UNKNOWN; task/root. Updated {stamp}. Will explicitly requested committing and pushing WALTER after a long session. Source/market boot coverage remains PARTIAL.

## STATUS

Current source set14signals/51create-only owner hands (3IMMEDIATE/11PRIORITY); morning19bookmarks dispositioned and source-backed marks complete,745processed/0staged. Six bounded verification helpers explicitly closed across two passes. Full continuity write-back now replaces earlier light summaries; existing market/source gaps remain. Will confirms DEWEY running the approved power-contract assignment; no final return consumed.

## CHANGED

REGISTRY refreshed before derived STATUS/network; STATUS lead/bottomline and source pointers, MEMORY sessionnotes, SESSION_LOG, currentcompletion, deep-research execution note and seven delivery flags. Previously uncommitted read-only bookmark/intake receipts included in exact own-path persistence. Beforeimages, ownerreview and checks under {REL}. No new signals, owner state edits, source-ledger marks or foreign stages.

## RESULT

Fresh origin fetch proves all six named prior WALTER source/metadata/mark/access/three-thread commits and51/51October14handoffs. Two later owner returns remain queued. Source findings retained: CPI and realearnings, named MPA shipping loss, IEA crude/product split, bank/AI/housing counterevidence, PORTS-Pike rights/cost gates and dated diesel/surcharge relief. No new owner grade or market refresh in closeout.

## GAPS / OWED

Current closeout commit/publication follows; source publication and actual recipient integration remain separate. Two BOND/LIQUID routing packets require the next source-routing pass. DEWEY report is in progress under its own writer; no premature return or resolution claim.

Localcharter70,223B still exceeds read-cap budget; no charter migration approved here. Full daily/compound HANS closes, monthly/qualitative registry coverage, Cushing/official named-month settlements, complete Iran/freight survey and several publisher bodies remain source-limited at their actual dates. No full market clearance. Phone lane has no input folder and live delivery unverified; Telegram tools unavailable. Old16-file source cache is intentionally unstaged/untouched, not unsaved authored work. Foreign desks' work remains theirs; no mainrepo pull or stash/rebase.

## WILL_NEEDS

None newly required for this closeout. Will authorized commit/push and confirmed DEWEY running. Existing unactivated charter/design checkpoints, WQ401/WQ388, optional subscription/step7h choices remain at their owners; no renewed ask. WALTER scope remains news/source routing; position expiry management/reminders stay with Will/TERRY. No trade or unattended permission inferred.

## FOLLOW-UP

{follow}
## OPEN DESIGN DECISIONS
{design}
## CLOSEOUT RECEIPT

Full context/persistence write-back; selected checks, publication, recipient integration and market coverage remain separate.

<!-- CLOSEOUT_RECEIPT_JSON
{json.dumps(receipt,indent=2)}
END_CLOSEOUT_RECEIPT -->
'''
(DESK/'LAST_COMPLETION.md').write_text(last)
proof={'as_of':stamp,'registry_before_status':True,'rows':len(rows),'headers':len(headers),'missing':missing,'memory_lines':len((DESK/'MEMORY.md').read_text().splitlines()),'memory_bytes':(DESK/'MEMORY.md').stat().st_size,'memory_note_conservation':oldnotes in (DESK/'SESSION_LOG.md').read_text(),'board_count':count,'queued_owner_returns':2,'dewey':'Will confirmsrunning; finalreturnnotconsumed','source_publication':publication['publication'],'delivery':{'total':51,'delivered':51}}
assert proof['memory_lines']<=100 and proof['memory_note_conservation']
(OUT/'writeback-proof.json').write_text(json.dumps(proof,indent=2)+'\n')
print(json.dumps(proof,indent=2))
