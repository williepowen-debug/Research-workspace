from pathlib import Path
from datetime import datetime,timezone
import json,csv
R=Path('/home/willi/Research-workspace');W=R/'AGENTS/WALTER';D=W/'research/2026-10-21_boot';now=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
rows=[(4,'russian-diesel-two-destination-signals','Russian diesel tankers signal Turkey and Brazil; deliveries and restored export scale unproved','OIL_ENERGY','HYDROCARBON_INFRA',['BRENT'],['OSPREY','HAWK','HENRY','RED','PROME'],['Russia','Leruo','Dolunay'],'''Reuters October20 reports Kpler/LSEG destination signals: Leruo left Primorsk October16 for Manaus, Brazil; Dolunay left October14 with diesel for Alanya, Turkey. These departures indicate renewed commercial routing after the ban change; destinations are not confirmed arrivals, delivered supply or restored export scale. Kpler/LSEG are reported vendor observations, not WALTER's own tracker pulls. Five lane outlets recycle the same Reuters report, not five independent witnesses.

BRENT ACTION: integrate this shipping follow-through into existing diesel-supply assessment. OSPREY/HAWK/HENRY/RED/PROME INFO. No new Russian-state decision or Iran-state assertion, no price/threshold/holding grade. The actor-policy leg remains separately owned.

Source RESEARCH-INTAKE October20 batch; complete accessible Reuters syndication read, datedOctober20: https://energynow.com/2026/10/russian-diesel-returns-to-familiar-destinations-following-export-ban-lift-shipping-data-shows/ . Direct shipping records and full cargo/delivery census uninspected. Novelty check found no Leruo/Dolunay in BRENT or OSPREY live analytical records; existing October20 proposal/IEA announcement is a different object.'''),
(5,'dram-newsroom-forecast-not-official-research-revision','DRAM newsroom reports roughly 20% Q4 price growth; official forecast comparability unresolved','AI_CAPEX','AI_INFRA_CAPEX',['VULCAN'],['HENRY','VIOLET','WATT','RED','PROME'],['DRAM','TrendForce','CXMT'],'''TrendForce's independently operated newsroom on October20 relays Commercial Times expectations of roughly20% quarter-over-quarter Q4 DRAM contract-price growth. This is an attributed forecast, not an observed settlement or an established revision to TrendForce research's September30 conventional-DRAM +10–15% range, still carried in VULCAN. Product perimeter and original analyst-method comparability remain unresolved; do not splice the figures as a measured acceleration.

The same body treats CXMT commercialization/yield questions and NVIDIA HBM changes conditionally; WALTER establishes no mass-production breakthrough or executed design switch. This additional reporting challenges overconfident near-term memory-glut framing without changing an owner score.

VULCAN ACTION: assess the new attributed forecast against the existing S2 contract-price basis, preserving the newsroom/research distinction and product-scope uncertainty. Other recipients INFO. No new study, threshold or grade commissioned.

Source RESEARCH-INTAKE; complete October20 newsroom article read: https://www.trendforce.com/news/2026/10/20/news-dram-prices-seen-rising-20-qoq-in-4q26-despite-slower-gains-ai-demand-tight-supply-support-outlook/ . Underlying Commercial Times body not independently inspected.'''),
(6,'dutch-storage-lowered-target-not-eu-gap-exit','Dutch storage exceeds a reduced national target; this does not clear the EU storage-gap trigger','EUROPE_MACRO','HYDROCARBON_INFRA',['HANS'],['BRENT','HENRY','LIQUID','RED','PROME'],['Netherlands','EBN','AGSI'],'''ANP via NL Times October20 reports Dutch gas storage65.5%, above a revised64% target after EBN's filling assignment; the prior target was74%. Nearly€1B was allocated, not established here as spent. Hitting a lowered national target is distinct from closing the EU aggregate gap to its own five-year norm. The underlying ministry/EBN records were not independently read; retain attributed reporting.

WALTER's direct AGSI pull on October21 returns gasdayOctober19 EU74.62%, with AGSI-native same-day five-year mean89.236%: signed gap−14.616 percentage points. This remains outside HANS-T-08's registered exit >−12pp for5consecutive gasdays; latest computable day contributes no exit. Baseline-composition sensitivity and economic usefulness remain unvalidated; no broad supply all-clear follows.

HANS ACTION: integrate the country-target outcome into existing European storage assessment without substituting it for the registered EU instrument. Other recipients INFO. Existing fired state is not re-fired; no new band or owner grade.

Sources RESEARCH-INTAKE; full https://nltimes.nl/2026/10/20/netherlands-meets-eu-gas-storage-target-government-intervention read; direct AGSI evidence research/2026-10-21_boot/hans-observations.json.''')]
paths=[]
for n,slug,title,domain,cluster,actions,infos,entities,body in rows:
 sid=f'SIG-W-20261021-{n:03d}';bp=f'BOARD/{sid}-{slug}.md';h={'signal_id':sid,'date':'2026-10-21','timestamp':now,'dispatched':now,'source':'RESEARCH-INTAKE','origin':'October20 lane; dated source bodies independently read October21','domain':domain,'cluster':cluster,'action':actions,'info':infos,'precedence':'PRIORITY','signal_type':'research','confidence':0.8,'confidence_language':'reports','resources':1,'safety_net':'clear','word_count':len(body.split()),'entities':entities,'event_window':'closed','dispatch_note':'Full accessible article body read; named primary/vendor access limits retained; no owner grade or new research commission.'}
 with (R/bp).open('x') as f:f.write('---\n'+'\n'.join(k+': '+json.dumps(v) for k,v in h.items())+'\n---\n\n# '+title+'\n\n'+body+'\n')
 paths.append(bp)
 with (W/'routed/route_log.tsv').open('a') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerow([now,sid,'RESEARCH-INTAKE',title,'PRIORITY',','.join(actions),','.join(infos),'0.8'])
 for who in actions+infos:
  role='ACTION' if who in actions else 'INFO'
  if who in ['PROME','TERRY'] or who in ['CARL','RED'] and role=='INFO':continue
  hp=f'AGENTS/{who}/inbox/WALTER/{sid}.md';(R/hp).parent.mkdir(parents=True,exist_ok=True)
  with (R/hp).open('x') as f:f.write(f'# {sid} — {title}\nBOARD: /{bp}\nPriority: PRIORITY\nRole: {role}\nFrom: WALTER\nDate: 2026-10-21\n\n## Kernel\n'+body+'\n\n## Why you got this\nExisting domain source update.\n\n## Requested action\n'+('Assess in the existing domain work as specified above; no new research direction.' if role=='ACTION' else 'INFO only; no directed ask.')+'\n\n## Confidence / caveats\n0.80 reports; source and basis limits in the kernel are material. No universal verification, delivery or consumption claim.\n\n## Cross-refs\n'+bp+'\n')
  with (W/'routed/delivery_log.tsv').open('a') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerow([now,sid,who,role,'CLAUDE_CODE','PRIORITY',hp,'written_not_delivered_pending_push','Create-only intake relay; publication deferred for foreign dirty work'])
  paths.append(hp)
(D/'intake-route-paths.json').write_text(json.dumps(paths,indent=2)+'\n');print('Three further signals created; lane remains unmarked until all NEW dispositions complete.')
