from pathlib import Path
import csv,json,re,datetime,hashlib,collections
W=Path('/home/willi/Research-workspace/AGENTS/WALTER'); R=W.parents[1]; O=W/'research/2026-11-04_catchup';now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
p=W/'REGISTRY.tsv';rows=list(csv.DictReader(p.open(),delimiter='\t'));updates={
'REGINALD':('2026-11-03','November 3 owner KRE redemption review: price/share-count divergence is historical, not a standalone bank-credit signal. Existing grades unchanged.'),
'NEXUS':('2026-11-04','November 4 working owner catch-up header: L16 UP and M-07 DOWN graded; delta-annotated, not a full matrix re-sweep. No independent WALTER acceptance of the full review.'),
'DAEDALUS':('2026-11-04','November 4 header records startup/recovery only; maintenance not established by the header. Other dirty authored files do not prove a completed review.'),
'WALTER':('2026-11-04','Authorized bounded catch-up: 68 source-qualified cards; 464 intake records and 49 bookmarks dispositioned. Current duties, approvals and publication limits: LAST_COMPLETION.md.')}
for row in rows:
 if row['Agent'] in updates:row['Updated'],row['Focus']=updates[row['Agent']]
with p.open('w') as f:w=csv.DictWriter(f,fieldnames=rows[0],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
review={'as_of':now,'rows':len(rows),'available_status_headers':44,'updated':updates,'counts':dict(collections.Counter(x['Status'] for x in rows)),'scope':'Owner lead-header comparison only. No automatic lifecycle, research completion, classification or grade inference.'}
(O/'registry-review.json').write_text(json.dumps(review,indent=2)+'\n')
p=W/'STATUS.md';s=p.read_text();s=re.sub(r'\*\*Updated:\*\*[^\n]+',f'**Updated:** {now} — authorized November 4 catch-up; FULL closeout. Operational coverage PARTIAL. Duties: LAST_COMPLETION.md.',s,count=1)
start=s.index('## BOTTOM LINE');end=s.index('## DATED MARKET OBSERVATIONS')
s=s[:start]+'''## BOTTOM LINE

November 4 catch-up: 68 source-qualified cards, zero kill-log rows, three verification helpers completing nine bounded passes. All 464 intake records and 57 bookmark content units dispositioned. Trepp office two-print stress condition met; Qeshm and UKMTO 188 require FALCON grading. UNG sampled analyzed winds remain positive. Source and owner limits survive in LAST_COMPLETION.md and research/2026-11-04_catchup/REVIEW.md.

BALANCED baseline retained; labor intake LOOSE within 72 hours of November 6 payrolls. Zero day cluster_mediating flags. Historical observations below retain their dates; no whole-market clearance.

'''+s[end:]
insert='| November 4 catch-up | FRED November 3: HY 340 bp, CCC 1,316 bp, VIXCLS 20.83, SOFR minus IORB +7 bp, T5YIFR 2.21%; Cboe SKEW 150.01. Cushing 27.250M barrels [week October 30]. WAL 76.77 / KRE 72.88 / UNG 9.13 [November 3 unadjusted closes]. HY >350 x3 not met; 10 bp watch. VIX exit run 3/5, owner grade retained. GFS November 4 12Z analyzed vortex mean +1.092857 m/s, no sampled reversal. Futures returns withheld by tool; official settlements and compound/source gaps remain. Evidence: research/2026-11-04_catchup/THRESHOLD-SCAN.md. |\n'
s=s.replace('|---|---|\n','|---|---|\n'+insert,1)
a=s.index('## NETWORK AWARENESS');b=s.index('## Active LIAISON channels',a)
s=s[:a]+f'''## NETWORK AWARENESS

REGISTRY refreshed first at {now}: {len(rows)} rows, 44 available owner STATUS headers compared; REGINALD, NEXUS, DAEDALUS and WALTER mirrors updated. Colors and classes retained. Header evidence is scoped to its dated activity. Working NEXUS grades are owner-authored evidence, not independent acceptance. Snapshot: research/2026-11-04_catchup/registry-review.json.

Complete cross-runtime lifecycle visibility remains UNKNOWN; no DARK or launch inference. Three bounded verification helpers completed nine passes; no active helper remains. Source coverage and central reattestation limits are in LAST_COMPLETION.md.

'''+s[b:]
s=s.replace('**Current: BALANCED baseline. Passed bank-Q3 and CPI windows do not independently sustain LOOSE posture; upcoming catalysts require their own dated scope.**','**Current: BALANCED baseline, with labor intake LOOSE through the November 6 payroll release window (within 72 hours as of November 4). Passed bank-Q3 and CPI windows do not sustain other LOOSE domains.**')
s=s.replace('Current closeout evidence: `research/2026-11-02_intake-inbox/closeout/`','Current closeout evidence: `research/2026-11-04_catchup/closeout/`')
# Rotate only the oldest contiguous complete table rows verbatim; conserve them in the same commit.
a=s.index('| Object |');b=s.index('\n\nEvidence:',a);block=s[a:b];lines=block.splitlines(True);rot=[]
while len(s.encode())>22785:
 line=lines.pop();rot.insert(0,line);s=s[:a]+''.join(lines).rstrip('\n')+s[b:];b=s.index('\n\nEvidence:',a)
p.write_text(s)
entry=f'''# FULL CLOSEOUT — {now} — authorized November 4 catch-up

68 BOARD cards, 187 required handoffs, zero kill-log rows; three bounded verification helpers completed nine passes. Intake 464/464 and bookmark content 57/57 CLOSED; exact 49 bookmark IDs marked. Source leads are explicitly unverified. Threshold registry accounts for 48 IDs; no whole-registry all-clear. Owed DEWEY requests overlap completed owner work and remain for reconciliation. No domain launch, trade or new study. Registry refreshed before NETWORK; MEMORY session note and current duty/approval list refreshed. Full closeout has no LIGHT narrative debt. Publication and source limitations remain solely in LAST_COMPLETION.md. Review: research/2026-11-04_catchup/REVIEW.md.

'''
if rot:entry+=f'## Verbatim STATUS rotation — {now}\n\nOldest contiguous {len(rot)} observation rows; moved without rewriting.\n\n| Object | Observation and limit |\n|---|---|\n'+''.join(rot)+'\n\n'
p=W/'SESSION_LOG.md';p.write_text(entry+p.read_text())
p=W/'MEMORY.md';s=p.read_text();s=s[:s.index('## Session Notes')]+'''## Session Notes

November 4 authorized catch-up completed at the stated source scopes; FULL continuity refreshed. Current duties, conditional approvals, unresolved sources and publication limits are solely in LAST_COMPLETION. Three verification helpers finished; no ongoing WALTER study or order. November 5 calendar/MEMORY review remains due.
''';p.write_text(s)
print('STATUS',len((W/'STATUS.md').read_bytes()),'rotated',len(rot),'registry',len(rows))
