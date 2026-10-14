"""Save owned routing checkpoint; preserve previous handoff and carried duties."""
import csv
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
OWN=ROOT/'AGENTS/WALTER'
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
routes=json.loads((HERE/'prepared-routes.json').read_text())
last=OWN/'LAST_COMPLETION.md'
before=last.read_bytes()
archive=OWN/'archive/LAST_COMPLETION_2026-10-13_before-priority-routing.md'
if not archive.exists():archive.write_bytes(before)

# Source worklist has 18 grouped scanner keys but 27 flagged article items.
lane=json.loads(Path('/home/willi/Research-Intake/data/2026-10-13/news.json').read_text())
items=[r for r in lane['items'] if r.get('classification') in ('NEW_ALERT','NEW_WATCH','NEW_WATCH_HIT')]
assert len(items)==27
dispositions=[]
for n,r in enumerate(items,1):
    title=r['title']
    if 'life insurers increasingly rely' in title:
        disposition,ref='DISPATCH','SIG-W-20261013-003 primary-teaser-only;35pct baseline not adopted'
    elif 'senators' in title.lower() and 'diesel' in title.lower():
        disposition,ref='DISPATCH','SIG-W-20261013-004 same-letter-fold;12 primary signatories,not revocation'
    elif 'Yanbu Oil Loadings' in title:
        disposition,ref='DUP','September30 repost;September28 restart already in anchor;no current-operation regrade'
    elif 'Kansas Community Bank' in title or 'Junk Bonds to Your Investment' in title or 'DRAM Industry Revenue' in title:
        disposition,ref='NO-ACTION','Old publication date;no current-event route;not full-body-assessed'
    elif any(s in title for s in ['Russia - After Trump','Russian diesel exports could','Russia Eyes Higher','Oil prices fall as Russia diesel','global diesel exports will','diesel export capacity','Russia Lifts Diesel']):
        disposition,ref='FOLD','Existing permission/easing channel;new forecasts unadopted,no delivered increment;DEWEY86686cdb3/BRENTe40ea12fb reused'
    else:
        disposition,ref='NO-ACTION','Retained unmarked for ordinary intake;source-body review outside this bounded priority pass'
    dispositions.append({'item':n,**r,'disposition':disposition,'ref':ref})
    subprocess.run(['python3',str(OWN/'tools/batch_manifest.py'),'--item','BM-20261013-04',str(n),disposition,ref],check=True,capture_output=True)
subprocess.run(['python3',str(OWN/'tools/batch_manifest.py'),'--close','BM-20261013-04'],check=True,capture_output=True)
(HERE/'intake-dispositions.json').write_text(json.dumps(dispositions,indent=2)+'\n')

# The instruction basis has not changed; this records execution limits, not a new attestation.
boot={'as_of':stamp,'desk':'WALTER','runtime':'OpenAI Codex','model':'GPT-6 family; exact variant UNKNOWN','session':'/root; native session UUID unavailable',
      'repo':str(ROOT),'cwd':str(OWN),'root_instructions':['AGENTS.md','CLAUDE.md','USER.md'],
      'local_instructions':'CLAUDE.md explicitly read in chunks;local AGENTS.md absent',
      'handoff':'LAST_COMPLETION.md read and evaluated;predecessor bytes archived',
      'authority':'Will direct October13 boot/routing priorities;PROME October13 report reused',
      'state':'PARTIAL','pull':'main ff-only pull succeeded at boot;later foreign work prohibits pull/push',
      'intake':'October13 lane pulled;health current0missed;18 grouped keys/27 flagged articles;all dispositions recorded,not --mark because retained body gaps',
      'phone':'source directory absent;no item','dropzone':'0 content files','inbox':'0 top-level md at first pre-intake scan;late DEWEY checkpoint read whole',
      'X':'sandboxDNS retried with approval;refreshHTTP400;scan failed,nothingmarked;654 prior seen is historical,not today clearance',
      'registry':'45 rows;every existing STATUS first30 lines captured;not full-owner evidence',
      'readiness':'fleet listing/native transport unavailable;thread-local collaboration not fleet visibility;ORCH_INFLIGHT read whole;foreignBRENT/DEWEY/REGINALD/TERRY activity observed;0 dark inference/doorbells',
      'read_checks':'basis29 MATCH;declaredREADS/readcap REVIEW:localcharter70223B above32550B;no charter migration authority',
      'thresholds':'48 rows loaded/counted(RED12/REG8/CREED11/HANS17);currentpull partial;officialfutures13,UK/Bundcloses,TTFidentity,monthly/qualitative/compoundlegs remainungraded;no fullclearance',
      'helper':'RULE9 read-only refinery_verify;resultread;explicitcloseoutreceipt received;no domainownerlaunch or process-exit inference'}
(HERE/'BOOT_RECEIPT.json').write_text(json.dumps(boot,indent=2)+'\n')

# Update only actual changed registry rows; other header-derived vintages are conserved.
reg=OWN/'REGISTRY.tsv'
with reg.open() as f: rr=list(csv.DictReader(f,delimiter='\t')); fields=list(rr[0])
for r in rr:
    if r['Agent']=='WALTER':
        r.update(Updated='2026-10-13',Focus='Oct13 priority routing:6 sourced/qualified signals;bank/insurer/diesel owner assessments reused. BootPARTIAL/X400/source gaps. Canonical duties LAST_COMPLETION;no trade/owner grade.')
    if r['Agent']=='BRENT':
        r.update(Updated='2026-10-13',Focus='October13 committede40ea12fb report reused:energyWAITunchanged;France10M plan/October12CMEfinal recovered;OMROct14confirmed04:00EDT. Delivery/currentruns/earningsedge unknown.')
    if r['Agent']=='DEWEY':
        r.update(Updated='2026-10-13',Focus='October13 committed86686cdb3 checkpoint PARTIAL;3additionalcargo leads/0authenticateddeal increments in inspectedevidence. Signedimplementation/customs/ICEgaps;existingOct14deadline.')
with reg.open('w') as f:
    writer=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rr)

status=OWN/'STATUS.md'; s=status.read_text()
start=s.index('## DATED MARKET OBSERVATIONS');end=s.index('## MISSION',start)
replacement='''## DATED MARKET OBSERVATIONS — retrieved October13 23:08Z

| Object | Observation and limit |
|---|---|
| Credit | FRED MIRROR HY311bp/CCC1253bp [October12];HY9bp/2.8125% below strict>320,0/3;CCC fire banked,no repeat. October12 bond holiday may carry cash series,not a fresh independent witness. October13 credit print unavailable. |
| Volatility | FRED MIRROR VIXCLS15.21 [October12];banked state,exit>=18 not met. CBOE PRIMARY SKEW155.06 [October12] after154.34 [October9],2/4 at>=150;October13 publisher bar absent. Watch routed005;no fire. |
| Funding / rates | SOFR3.87−IORB3.90=-3bp [matchedOctober9];forwardIORB14 not substituted. DGS10/30 5.24/5.60 [October9],not October13. T5YIFR2.33 [October13]. |
| Labor | ICSA197K [weekendingOctober3,current revisedFRED mirror];no first-release recertification. |
| Banks | Vendor datedOctober13 KRE69.06,WAL73.73,OZK45.08;singlepull,not independent closecertification. WAL existing cycle2:no >=81.90 exit;no repeatfire. Issuer Q3workout outcomes remainpending. |
| Storage | AGSI gasdayOctober13 fill74.04%−same-source5yrnorm88.884%=-14.844pp;existingOPEN,exit>-12 notmet,0/5. Baselinecomposition/economicusefulness unvalidated. |
| Energy | Cushing24.745M bbl [weekOctober2];currentweek not yetpublished. October13 vendorfutures not formalsettles. BRENT/DEWEY recoveredOctober12 CMEfinal pairedinputs;no duplicated grade. Currentnamedsite run-rates/deliverednetdiesel UNKNOWN. |
| UK / HANS remainder | UK/Bund closes,TTF contractidentity,Italy/France matchedcloselegs notrefreshed in this pass;old observations are not currentclearance. Monthly/qualitative rows remain owner/source-limited. |
| Broker / Iran / freight | No newbroker or completeIranladder/freight survey;previous datedowner evidence retained. Brokertruth off-repo;no order/fill inferred. |

Evidence: `research/2026-10-13_priority-routing/observations.json` and `threshold-coverage.tsv`. Source dates govern. No full-market clearance.

'''
s=s[:start]+replacement+s[end:]
s=s.replace('**Updated:** 2026-10-13T14:24:38Z — Will-requested FULL closeout; handoff saved. Research coverage **PARTIAL**. BOARD **1367**; last routing day October12 **44 signals (1 FLASH,43 PRIORITY)**. This closeout:0 new signals, one MIDAS return CLOSED3/3 FOLD,3 helper closeout receipts. October12 cluster-mediating count0; no threshold alert generated.',f'**Updated:** {stamp} — Will-launched priority routing;boot/researchPARTIAL. BOARD **1373**;October13 **6 PRIORITY** signals,0FLASH/IMMEDIATE,0cluster-mediating,0newfires. Prior assessments reused;source limits travel with packets.')
b=s.index('## BOTTOM LINE'); e=s.index('## DATED MARKET',b)
s=s[:b]+'''## BOTTOM LINE

New WFC reserve/comparison inputs,finalEIOPA supervision,Moody's limitedRNF primaryteaser and Senate diesel-policy challenge reached WALTER's routing layer. A qualifiedWoodRiver FCC pointer retains unknown lostoutput/duration;CBOE October12 advances existingSKEW watch to2/4. No regional-bank fundingbreak,private-credit loss,delivered diesel increment or changed energyWAIT established. Evidence and next duties: LAST_COMPLETION.md.

'''+s[e:]
status.write_text(s)
session=OWN/'SESSION_LOG.md';old=session.read_text()
session.write_text(f'# {stamp} — light-closeout — full deferred\n6PRIORITY/22handoffs;WFC/EIOPA/RNF/Senate/SKEW/WoodRiver. DEWEY86686cdb3/BRENTe40ea12fb reused;WAIT unchanged. BootPARTIAL/Xrefresh400/intakeunmarked;no fullmarketclearance. Publication/consumption→LAST_COMPLETION.\n\n'+old)

# Update attempt clocks without inventing a new fire.
for name in ['FALSIFICATION_FIRED_LOG.tsv','REG_THRESHOLDS_FIRED_LOG.tsv','DEEP_RESEARCH_FLAGGED_LOG.tsv']:
    p=OWN/'registry'/name;t=p.read_text();t=t.replace('# Last re-pull ATTEMPTED: 2026-10-12', '# Last re-pull ATTEMPTED: 2026-10-13',1);p.write_text(t)
p=OWN/'registry/DEEP_RESEARCH_FLAGGED_LOG.tsv';t=p.read_text()
lines=t.splitlines()
for i,line in enumerate(lines):
    if '\tREQ-DEWEY-20261010-001\t' in line:
        cells=line.split('\t');cells[9]+=' || October13checkpoint86686cdb3 readwhole;delivery stubs verified. PARTIAL/October14deadline retained;CMEOctober12final gapclosed;FranceNovember-January10Mplan notadditive toIEA100M. Deliveredincrement/signedimplementation/US-law/ICEgaps retained.';lines[i]='\t'.join(cells)
p.write_text('\n'.join(lines)+'\n')

prior=before.decode();keep=prior[prior.index('## WILL_NEEDS'):prior.index('## CLOSEOUT RECEIPT')]
keep=keep.replace('No new decision is needed for this closeout. X authorization and the requested bookmark read are resolved.','No new research/trade decision. New launch-only X read failed refreshHTTP400;reauthorization would require Will’s browser. Nothing marked;prior48-item work stays complete.')
keep=keep.replace('Refresh eligible live-source observations before using dated near-trigger levels; no repeat48-bookmark scan/mark or repeated owner research.','October13 scoped marketpull and6source-qualified routes saved. Complete remaining source/owner checks before a grade;newXscan failed and intake remains unmarked. No repeated prior48-item work or owner research.')
keep=keep.replace('New closes not collected in this closeout.','October12 CBOE155.06 recovered;2/4,October13 bar absent;no earlyfire.')
keep=keep.replace('Existing packets/source upgrade consumed, broad research closure still requires missing evidence.','October13 checkpoint86686cdb3 read;CMEOctober12 final recovered,physical/signedannex/US-law/ICE gaps retained;PARTIAL and deadlines unchanged.')
evidence=[]
for rel in ['AGENTS/WALTER/research/2026-10-13_priority-routing/observations.json','AGENTS/WALTER/research/2026-10-13_priority-routing/refinery-verify.md','AGENTS/BRENT/research/2026-10-13_energy-wait/REPORT.md','AGENTS/DEWEY/output/2026-10-13_diesel-delivery-and-primary-document-checkpoint.md']:
    evidence.append({'path':rel,'sha256':hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),'note':'Source/owner evidence read;not inferred owner consumption of newWALTERpackets.'})
origin=subprocess.check_output(['git','rev-parse','origin/master'],cwd=ROOT,text=True).strip()
receipt={'schema':1,'as_of':stamp,'publication':[{'commit':origin,'state':'published'}],
         'delivery':{'signal_date':'20261013','total':22,'delivered':0,'note':'Newpacketswritten;localcommit/publicationreconciliationpending. Consumptionseparate.'},
         'push':{'all_walter_commits_on_origin':False,'note':'No self-authorizedPRIORITYpush;foreignworkingtreeobserved. Sourcecommitreceipt follows.'},
         'owner_review':{'scope':'manual evidence review; no automatic completion','evidence':evidence},
         'owed':['New routing persistence/publication and actualrecipientconsumption','Xbrowserreauth if resumed','Intakebody gaps/notmarked','48-row scanpartial;officialsettles13/HANSclosessourcegaps','ExistingSHADEL673ownerinputs andDEWEYOct14commission'],
         'next_review':'2026-10-14','procedure':{'tier':'light','scope':'Willpriorityrouting;notend-of-dayfullcloseout','claim':'Writtenrouteandmanualsourcechecks;bootPARTIAL;selectedchecksnotfullprocedure'},
         'manual_duties':{'11':'6BOARD/22createonlyhandoffs;INDEXgenerated;olddupsfolded;noR1correctiontoweownedsignal/figure','root.consumer':'Noownedthreshold/baseline supersession;newdatedsourceobservations only','root.memory':'Noauto-memory;Tier1 defers MEMORYtrim','root.retirement':'ExistingOct13 retirement assessment reused;no retirementmoves','helpers':'RULE9read-onlyresultread;explicitcloseoutreceipt;noownerlaunch/process-exitclaim'},
         'selected_checks':'Precommitweekday6clean;basis29MATCH;readcap/READS REVIEW;furtherlightchecksrecorded separately.'}
text=f'''# WALTER LAST_COMPLETION — October13 priority routing
Runtime: OpenAI Codex/GPT-6 family;exactvariant/nativeUUID UNKNOWN;thread /root. Updated {stamp}. Root/local instructions and priorhandoff read;localAGENTS.md absent.

## STATUS
Routing checkpoint saved;boot/research PARTIAL. Six PRIORITY signals and22 create-only handoffs;owner assessments reused. No full threshold/source clearance, new owner grade, trade or background-work promise.

## CHANGED
BOARD001–006/INDEX;route/deliverylogs;REGISTRYaffectedrows;STATUSdatedobservations;SESSION_LOGlightbreadcrumb;LAST_COMPLETIONpriorbytesarchived;BM04CLOSED27/27;datedsource/verification/receipt artifacts.

## RESULT
WFCnewQ3comparison/reserveinputs→BROCK/REGINALD;finalEIOPA→SHADE/HANS;primaryRNFteaser→SHADE;Senateletter andqualifiedWoodRiverlead→BRENT/HAWK;CBOEOctober12watch2/4→VIOLET. Sixroutes,22handoffs. Regionalworkout conclusions unaltered;energyWAITunchanged atBRENTe40ea12fb. DEWEY86686cdb3checkpointreadwhole;existingPARTIALcommission retained. WALcalendaralreadyowned,notrerouted.

## GAPS / OWED
- Publication/recipientconsumption unverified. Foreignwriteractivity prohibits pull/push;activeowner subtree packets require commit-window review. No native fleetmessage channel exposed;durablePROMEpacket pending creation.
- XrefreshHTTP400 afterapprovednetworkretry;0newitems marked. Prior654seen is historical,not currentclearance.
- Intake27contentitems all dispositioned;retained sourcebody gaps keep lane unmarked. Already-routed/oldsource items must reuse dispositions on nextscan.
- Current marketpass partial:HY311/CCC1253/VIX15.21 datedOctober12,SOFR/IORBdatedOctober9. SKEWOctober13barabsent;officialfuturesOctober13/HANScloses/monthlyqualitativecompound/sourcegaps ungraded. Charter70223B remains overreadbudget;basis29MATCHdoesnotcertifyexecution.
- WoodRiver originalwire/operator-event/onset/duration/outputunknown. FullMoodyRNFreport/measurementwindow/entitylossbaseunknown. EIOPAfinalOctober6doesnotestablishnamedUSloss/enforcement. SenateletterdoesnotrevokeGL135.
- Signeddieselimplementation/netdeliveredaddition/US-law/customs/ICEbasis missing. CMEOctober12final sourcegapclosed atDEWEY/BRENT,not aWALTERholdinggrade. SHADEL673freshLIQUIDcount/anchor and exactwindow remainowner-gated.
- PriorIranladder/OSPREYadoption/Rosner/paywall/freight/broker/Will-design duties retained below. No currentbroker/expiryorder inferred.

'''+keep+'## CLOSEOUT RECEIPT\n\nLight routing checkpoint;publication and consumption remain separate.\n\n<!-- CLOSEOUT_RECEIPT_JSON\n'+json.dumps(receipt,indent=2)+'\nEND_CLOSEOUT_RECEIPT -->\n'
last.write_text(text)
print('Saved owned checkpoint;27/27 batch dispositions,6routes/22handoffs;source/persistence gaps explicit.')
