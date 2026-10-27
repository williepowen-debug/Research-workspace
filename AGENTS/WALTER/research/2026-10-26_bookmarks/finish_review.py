"""Persist exact-ID, manually determined dispositions; no fetch or marking."""
from pathlib import Path
import json
import subprocess
from collections import Counter

ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).resolve().parent
FOLLOW='AGENTS/WALTER/research/2026-10-26_bookmarks/FOLLOW-UP.md'
# Post number, disposition, reading state, home, WALTER-written rationale.
ROWS=[
(1,'FOLD','partly_read','SIG-W-20261027-003','Bloomberg introduction rescued, full article still gated. Original S-1 selected risks and financial sections read. Growth-rate warning is prospective, not observed contraction.'),
(2,'FOLD','fully_read','SIG-W-20261026-004; SIG-W-20261026-012','Full TVC chart inspected: close 15.871%, change +2.939 percentage points; distinct from CDS, mortgages and matched closes. Existing Brazil event is better sourced; exact security identity remains unknown.'),
(3,'DISPATCH','partly_read','SIG-W-20261027-006','Image is a designed summary, not original memo. AWN full secondary body read; no realized-exit count. Merger savings are not a payroll/job-loss count.'),
(4,'FOLD','partly_read','SIG-W-20261027-006','Offer already exists in 1026-005; saved incremental severance terms not verified in public official text. No 60,000 completed layoffs.'),
(5,'DISPATCH','partly_read','SIG-W-20261027-009','Both full screenshots inspected; 38 individual profile claims retained/deduped. One radiology title uncertain, some regional/legal-entity scopes ambiguous. No confirmed breaches or incident dates.'),
(6,'DISPATCH','partly_read','SIG-W-20261027-005','Official research announcement ETH section read. Proof/formalization and external academic acceptance not reviewed; practical compute/crypto effects unestablished.'),
(7,'DISPATCH','partly_read','SIG-W-20261027-007','Full resale screenshot read. Property ZIP37219 differs from post ZIP37203. Closing/mortgage record and metro inventory baseline not independently recovered.'),
(8,'DISPATCH','fully_read','SIG-W-20261027-008','Full Intel primary confirms agreement, H1 2027 conditional closing and no disclosed price. Not a completed acquisition or quantified compute-demand change.'),
(9,'NO-ACTION','fully_read','REVIEW.md#norway','Reuters full body via Investing.com read: rally rhetoric; no indication of adopted immigration policy. No instrument, quantified labor-supply effect or fresh geopolitical action. Retained for an actual policy change.'),
(10,'DISPATCH','partly_read','SIG-W-20261027-003','Selected original S-1 sections distinguish fair-value carrying balance from principal and disclose IPO share conversion; no evidence of a $108B cash redemption or accounting fraud. Full bridge/terms incomplete.'),
(11,'DISPATCH','fully_read','SIG-W-20261027-004','Complete original filing paragraph confirms >one-month pre-training delay for security enhancements. It does not report actual weight theft or capex cancellation.'),
(12,'DISPATCH','partly_read','SIG-W-20261027-013','Conditional shortened timeline, not agreed or implemented. Full secondary short body read; original broadcast not recovered.'),
(13,'FOLD','fully_read','SIG-W-20261027-013','Original Israel Hayom full reporting body read. Offer/payment attributed to anonymous sources; official did not confirm a transfer. No ceasefire/throughput change inferred.'),
(14,'FOLD','partly_read','SIG-W-20261027-013','Same conditional state-TV timeline family as12. Two relay accounts are not independent confirmation; source broadcast unread.'),
(15,'DISPATCH','fully_read','SIG-W-20261027-015','Full Reuters via AOL read. Negotiations possible before November3 are not agreement, statutory tariff change or effective relief.'),
(16,'DISPATCH','fully_read','SIG-W-20261027-014','Full updated Reuters via JPost body read. Airstrike story is distinct from arrests; Jordan coordination assertion and Syrian casualty report separately attributed.'),
(17,'FOLD','partly_read','SIG-W-20261027-013','Saved post read; full i24 original not recovered. October25 unofficial strike-timing report does not replace October22 WH policy or establish an attack. Full guard corpus checked.'),
(18,'DISPATCH','partly_read','SIG-W-20261027-016','Full October26 issuer release read:110 safe/five unaccounted. Wire/post one-dead/four-missing retained separately. Video not authenticated/transcribed; cause/output unknown. Gabon, not Hormuz.'),
(19,'DISPATCH','fully_read','SIG-W-20261027-011','Full official Keystone article recovered via FX article blocks, including records, key scope, customer timing, shipping and deletion completion conditions.'),
(20,'FOLD','partly_read','SIG-W-20261027-007','Post read, original Goldman table not located.2.2%/25% historical comparison lacks matching denominator/vintage; potential counterevidence retained as unverified.'),
(21,'DUP','fully_read','SIG-W-20261026-005','Official Coleman image inspected in full; announcement, four countries and level<=70 already routed. Count and future-layoff extrapolation are not official realized exits.'),
(22,'DUP','fully_read','SIG-W-20261026-005','Same reported eligible60,000/27% count already qualified in005. No additional realized-exit observation.'),
(23,'DISPATCH','partly_read','SIG-W-20261027-018','Premium ZeroHedge and Bloomberg Law introductions read; full Bloomberg/UBS note and relative effect method remain inaccessible. Qualified lead, no causal/magnitude certification.'),
(24,'FOLD','partly_read','SIG-W-20261027-010','Full Reuters syndication read after direct redirect401. GMO duplicates CYB-INC-032; separate Park24 ¥3,000 event saved in supplemental batch02. Park24 issuer notice missing.'),
(25,'DUP','fully_read','SIG-W-20261022-016; SIG-W-20261023-019','Full chart inspected.18% CCC effective yield already verified18.01[Oct20]/17.82[Oct21];13.4% OAS matches1340[Oct22], superseded by owner1356[Oct23]. Same ICE basket, not two witnesses/new print.'),
(26,'DISPATCH','partly_read','SIG-W-20261027-012','Full THN body and vendor investigation update read; researcher current response, scope/summary read. Detailed reproduction/source diffs not audited. Vendor targetOct27 is not shipped patch.'),
(27,'DISPATCH','partly_read','SIG-W-20261027-017','Underlying news body read, department memo403. Proposed90-day resilience planning is not a dated war forecast or measured commissioning.'),
(28,'FOLD','partly_read','SIG-W-20261027-012','Full article/image read, same11-finding Tailworm report as26. Vendor update adds remediation status. No independent exploit reproduction/full technical audit.'),
(29,'FOLD','partly_read','SIG-W-20261027-017','Same Fox source family as27; underlying department memo unread, not a second witness.'),
(30,'NO-ACTION','fully_read','SIG-W-20261027-017','Full FX quoted post read. Anonymous bank-preparation hearsay supplies no institution, plan, event or financial observation; retained as unattributed context, not declared false.'),
(31,'DISPATCH','partly_read','SIG-W-20261027-019','Full saved smoke image and AP event body read; updated OPB summary available, full updated body not exposed. Officials say tanks stable/no nearby contamination; no ammonia-tank explosion established.'),
(32,'FOLD','partly_read','SIG-W-20261027-019','Full AP short event body read; source video not authenticated/transcribed. No injuries; cause/output/restart not known. Capacity is not measured lost production.'),
]

def main():
    mapping=json.loads((OUT/'item-map.json').read_text())
    review=json.loads((OUT/'review-stage32.json').read_text())
    assert len(mapping)==len(review['items'])==len(ROWS)==32
    by_id={x['id']:x for x in review['items']}
    report=['# Bookmark review — October 26 ET / October 27 UTC','',
            'Will-directed review of stage1ab5bbb3f5f34833bfc83fbdd384545b. Saved head was October27 00:33:16Z; no fresh head claim here. All32 IDs have an explicit disposition. Ten attached photos inspected; two source videos not authenticated/transcribed. Reading labels concern actual material read, not download success or factual truth.','',
            '18 new BOARD records include one urgent CYPHER incoming event outside the bookmarks. Publication, delivery and recipient incorporation remain separately evidenced. All material source gaps remain in [FOLLOW-UP](FOLLOW-UP.md). No trades, autonomous domain launches, studies or new collectors.','',
            '| Post | Saved ID | Disposition / home | Reading | Judgment |','|---|---|---|---|---|']
    manifest=[]
    for (n,disp,state,home,reason),m in zip(ROWS,mapping):
        assert n==m['n']
        x=by_id[m['id']];x.update(disposition=disp,read_state=state,
                                follow_up=FOLLOW if state!='fully_read' and disp in {'DISPATCH','FOLD'} else None,
                                ask_user=None)
        report.append(f'| {n} | {m["id"]} | {disp}: {home} | {state} | {reason} |')
        if n!=5:
            manifest.append({'item':len(manifest)+1,'post':n,'id':m['id'],'disposition':disp,'ref':home+'; '+reason})
    claims=json.loads((OUT/'gentlemen-38.json').read_text())
    for c in claims:
        manifest.append({'item':len(manifest)+1,'post':5,'claim':c['n'],'id':c['bookmark_id'],
                         'disposition':'DISPATCH','ref':'SIG-W-20261027-009; '+c['victim_as_read']+'; actor claim only, date2026-10-26; no duplicate found'})
    assert len(manifest)==69
    report+=['','## Norway','',
             'Reuters October25 rally report read via https://www.investing.com/news/economic-indicators/trump-adds-norway-to-vulgar-list-of-countries-citing-nobel-snub-4971339 . Rhetoric is not a policy instrument. No new immigration restriction asserted. Revisit on an actual administration instrument within MARCO/HAWK existing scope.','',
             '## Input accounting','',
             'BM-20261027-01:31 non-roundup posts +38 Gentlemen profiles =69 distinct content items. The two screenshots belong to one38-profile list. BM-20261027-02:one supplemental Park24 event, discovered inside the Reuters body before Park24 triage. Source post24 therefore receives an article-level FOLD, with separate named-event dispatch evidence.','',
             'Both financial-transmission and system-improvement lenses were applied: the ETH proof claim and security/prevention distinctions are retained with their validation limits. No automatic architecture/research commission.','',
             'Disposition counts (32 saved IDs): '+str(dict(Counter(x[1] for x in ROWS)))+'. Reading: '+str(dict(Counter(x[2] for x in ROWS)))+'. No source-access failure was labelled irrelevant or false.','',
             '## Batch boundary','',
             'New CYPHER urgent PHP2Shell packet verified independently at CISA and recorded as SIG-W-20261027-002; ConnectWise/Chrome dated owner clocks retained. Original14 regular/3 DEWEY packets remain pending, distinct from this bookmark work. Intake marks stay withheld pending those dispositions. WQ515 sample selection remains closed10/10; no added selection/grading. Full lifecycle adjudication and broader threshold/source gaps remain at LAST_COMPLETION.']
    (OUT/'REVIEW.md').write_text('\n'.join(report)+'\n')
    (OUT/'manifest-map69.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (OUT/'review-stage32.json').write_text(json.dumps(review,indent=2)+'\n')
    tool=ROOT/'AGENTS/WALTER/tools/batch_manifest.py'
    import sys
    for item in manifest:
        subprocess.run([sys.executable,str(tool),'--item','BM-20261027-01',str(item['item']),item['disposition'],item['ref']],cwd=ROOT,check=True,capture_output=True)
    subprocess.run([sys.executable,str(tool),'--item','BM-20261027-02','1','DISPATCH','SIG-W-20261027-010; Park24 ¥3,000 following personal-data breach; issuer notice missing; Reuters full body read'],cwd=ROOT,check=True,capture_output=True)
    for batch in ['BM-20261027-01','BM-20261027-02']:
        p=subprocess.run([sys.executable,str(tool),'--close',batch],cwd=ROOT,check=True,capture_output=True,text=True);print(p.stdout)
    print('Saved exact-ID review, source-gap map and69+1 item dispositions. No mark/fetch/commit/push.')

if __name__=='__main__':main()
