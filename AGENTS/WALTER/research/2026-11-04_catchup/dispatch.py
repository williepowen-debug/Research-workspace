from pathlib import Path
import json,csv,datetime,re
ROOT=Path('/home/willi/Research-workspace'); W=ROOT/'AGENTS/WALTER'; OUT=W/'research/2026-11-04_catchup'
D=[]
def add(slug,title,action,info,cluster,domain,entities,body,sources,priority='PRIORITY',confidence=.9,**extra):
 D.append(dict(slug=slug,title=title,action=action.split(),info=info.split(),cluster=cluster,domain=domain,entities=entities.split(),body=body,sources=sources,precedence=priority,confidence=confidence,extra=extra))
add('Trepp-office-two-print-threshold','October office delinquency meets the registered two-print threshold','CREED REGINALD','LIQUID PROME RED','BANK_COLLATERAL','BANK_CRE','Trepp CREED-T-01a',
'''Trepp's November 2 release reports October office CMBS delinquency of 12.33%, up 17bp from September's 12.16%. Both exceed the frozen strict >12% threshold: the two-month observation condition is met. CREED's November preregistration accepts primary Trepp text at two decimals; formal owner fire record and Kernel resolution remain owed.

Overall delinquency fell 15bp to 7.87%, substantially reflecting a $975M showroom-portfolio cure. Office stress did not improve with that headline. This is a registered stress LEVEL, not proof of the maturity mechanism, bank losses or a new record (January was 12.34% in the owner's inherited history).

ACTION CREED: at its next explicitly authorized session, grade T-01a and prepare the existing resolution packet; no launch or S-score change is authorized here. ACTION REGINALD: review the bank-exposure transmission separately. INFO LIQUID/PROME/RED: threshold observation; no trade or convergence-score change inferred.''',
'https://www.trepp.com/trepptalk/cmbs-delinquency-rate-drops-15-basis-points-in-october-2026','IMMEDIATE',.96)
add('Qeshm-Nov2-strike-confirmation-test','November 2 Qeshm strike reporting requires the approved confirmation test','FALCON BRENT','HAWK PROME RED','IRAN_HORMUZ','GEOPOL_ENERGY','Qeshm CENTCOM FAL-07 WQ-559',
'''Reuters and NBC explicitly date limited US strikes on Qeshm to Monday November 2. Their anonymous US officials describe defensive action against Iranian surface-to-air missiles threatening US aircraft. This is a new event relative to the October 29–30 launcher claim; outlet count does not establish independent anonymous sources. On-record CENTCOM confirmation was not obtained.

WQ-559's approved interpretation includes defensive launcher strikes on Iranian territory. ACTION FALCON: apply that interpretation and the frozen confirmation test, recording FAL-07/ladder implications; do not reuse the old event's no-fire conclusion. ACTION BRENT: assess the dated operational-risk change with FALCON. INFO HAWK/PROME/RED: cross-war context and urgent owner review.

WALTER has not fired FAL-07, declared general combat resumption, changed the confirmed-loss census, or inferred transit recovery. Bounded anchor revalidation preserves the November 5 full-sweep duty.''',
'https://www.marketscreener.com/news/us-carries-out-defensive-strikes-on-iran-s-qeshm-island-officials-say-ce785fd9dc88fe26 ; https://www.nbclosangeles.com/news/national-international/us-military-limited-strikes-iran-qeshm-island/3964813/','IMMEDIATE',.82,narrative_channel='centcom')
add('October-manufacturing-final','October manufacturing expands; ISM and S&P require separate grades','ISHM LABOR CARL','HENRY REGINALD RED','CONSUMER_STAGFLATION','INDUSTRIAL_CYCLE','ISM S-and-P-Global October-PMI',
'''November 2 primary releases: ISM manufacturing 55.5 versus 54.5; orders 55.5, inventories 51.4 (orders-minus-inventories 4.1 versus 6.7), employment 52.4 and prices 75.2. S&P final manufacturing 54.9 versus September 55.9, below October flash 56.0. Both headlines remain above 50; ISM does not meet the strict <47 recession condition.

ACTION ISHM: integrate final vintages and complete the already-prepared R1/ISM grades without merging survey methods. ACTION LABOR: record the employment subindex. ACTION CARL: assess prices-paid and consumer transmission. HENRY/REGINALD/RED receive the required macro/counterevidence routes. S&P's primary commentary supports the headline; its underlying release portal returned 403, so full component validation remains open.''',
'https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/pmi/october/ ; https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/11/us-manufacturing-pmi-holds-close-to-highest-since-2022-as-price-pressures-build')
add('JOLTS-positive-net-pair','September JOLTS and August revision keep both net-flow readings positive','LABOR','CARL HENRY REGINALD RED','CONSUMER_STAGFLATION','LABOR','BLS JOLTS',
'''BLS's November 3 archived release reports seasonally adjusted nonfarm hires minus separations of +96K for August revised (5,271K−5,175K) and +83K for September preliminary (5,402K−5,319K). August was previously +122K. September openings are 7,523K; layoffs/discharges rate 1.0%, below the registered ≥1.2% routing bar.

ACTION LABOR: complete the frozen November 3 JOLTS grading card and carry LEG C into the November 6 NFP card §2.4. These are level-based calculations, not rounded-rate differences. Both observed net-flow signs are positive; WALTER does not change the owner's score. JOLTS and NFP are not independent confirmations. INFO CARL/HENRY/REGINALD/RED: required labor transmission and counterevidence.''',
'https://www.bls.gov/news.release/archives/jolts_11032026.htm')
add('ADP-October-and-services-employment','ADP adds 86K; October ISM employment pair remains above 50','LABOR CARL HENRY','ISHM RED','CONSUMER_STAGFLATION','LABOR','ADP ISM-Services',
'''November 4 ADP reports October private employment +86K and revises September +90K to +86K. Goods +4K, services +82K; manufacturing −1K, professional/business services −27K. Base pay +3.2% YoY; gross pay +4.7%.

ISM services October headline is 54.5 versus 54.9; activity 53.8, orders 55.9, employment 51.4, supplier deliveries 56.7, prices 73.0. Demand softened but remains above 50; slower deliveries support the composite mechanically. Manufacturing/services employment 52.4/51.4 cannot supply LABOR's below-50 R3-B pair.

ACTION LABOR: update the owed employment-pair record and NFP preparation. ACTION CARL/HENRY: integrate the services-demand/prices distinction. INFO ISHM/RED: paired survey context. ADP is not CES/NFP and does not grade November 6 payrolls. S&P services final remains primary-source-limited, separate from verified ISM.''',
'https://mediacenter.adp.com/2026-11-04-ADP-National-Employment-Report-Private-Sector-Employment-Increased-by-86,000-Jobs-in-October ; https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/services/october/')
add('Census-orders-trade-capex','September factory orders and trade add the owed inventory and import observations','ISHM','VULCAN CARL RED','AI_INFRA_CAPEX','INDUSTRIAL_CYCLE','Census M3 BEA FT900',
'''Census's November 3 M3 release (CB26-170, September) reports nominal seasonally adjusted orders +1.8%, shipments +1.3%, inventories +0.4%; inventory/shipments 1.46 versus 1.47. Durable orders +1.9% revises the +1.8% advance.

November 4 BEA/Census September trade release reports a $105.0B deficit versus August revised $105.7B. Its narrative reports capital-goods imports +$11.6B, including computers +$7.6B and accessories +$5.7B. These are nominal imports, not AI-only domestic investment.

ACTION ISHM: finish the existing inventory-cycle/core-capex/J1 work using the correct cells and paired y/y basis. INFO VULCAN/CARL/RED: capex and demand context. Granular PDF table cells were withheld because visual/header validation failed; headline/narrative observations do not complete the J1 grade. Evidence and withheld-cell dependency: VERIFY-DATA.md.''',
'https://www.census.gov/manufacturing/m3/prel/pdf/s-i-o.pdf ; https://www.bea.gov/sites/default/files/2026-11/trad0926.pdf')
add('Apollo-Q3-GAAP-adjusted','Apollo Q3 combines record origination with a GAAP loss requiring reconciliation','BROCK SHADE','PROME RED','PC_STRESS','PRIVATE_CREDIT','Apollo Athene',
'''Apollo's November 3 Q3 release reports $114B origination, $53B gross inflows ($30.488B net flows), $802M fee-related earnings, $844M spread-related earnings and $1.293B adjusted net income. GAAP common-stockholder loss is $1.057B. The reconciliation includes $2.661B retirement-services investment-loss adjustments net of offsets.

ACTION BROCK/SHADE: integrate the manager/insurance-wrapper release and distinguish accounting adjustments from realized credit losses. Neither the GAAP loss nor strong adjusted earnings establishes the direction of broad credit impairment alone. Do not assign the entire loss to rates without separate attribution. INFO PROME/RED: dated earnings and counterevidence. Quarter ended September 30; gross inflows are not net flows.''',
'https://www.apollo.com/insights-news/pressreleases/2026/11/apollo-reports-third-quarter-2026-results-3394015 ; https://ir.apollo.com/sec-filings/content/0001858681-26-000063/agmearningsrelease3q2026.htm')
add('Credit-Acceptance-forecast-revision','Credit Acceptance loss includes a forecast-methodology revision','CARL OTTO','BROCK RED','CONSUMER_STAGFLATION','CONSUMER_CREDIT','CACC Credit-Acceptance',
'''Credit Acceptance's October 29 Q3 release reports a $56.6M GAAP loss versus $135.5M adjusted profit. Forecast portfolio net cash flows fell $291.2M (2.5%), primarily from a methodology adjustment: this is not a $291.2M realized collections shortfall. Provision rose $258.9M YoY, including $193.8M forecast changes and $65.1M new assignments.

Unit/dollar assignments grew 37.7%/51.0%; company reports $1.2B available liquidity and a $600M ABS financing. ACTION CARL/OTTO: assess the revision alongside origination and financing counterevidence in existing consumer/auto work. INFO BROCK/RED: funding overlap and bounded interpretation. The release predates the November 2 intake; no system-wide funding closure established.''',
'https://www.ir.creditacceptance.com/news-releases/news-release-details/credit-acceptance-announces-third-quarter-2026-results')
add('Marvell-Lumentum-agreement','Marvell and Lumentum sign an all-stock agreement','VULCAN','ZHAO RED','AI_INFRA_CAPEX','AI_CAPEX','Marvell Lumentum MRVL LITE',
'''The November 2 issuer announcement and filed 8-K establish a definitive agreement exchanging 4.500 Marvell shares per Lumentum share. Announced implied enterprise value is approximately $115B, using the release's pricing basis. Expected close is first-half 2028, subject to approvals and other conditions.

ACTION VULCAN: integrate the connectivity transaction into existing supply-chain and financing coverage. INFO ZHAO/RED: regulatory/supply-chain overlap. This is a signed agreement, not a completed acquisition, realized AI capex, or evidence that management's demand/synergy projections will occur.''',
'https://investor.marvell.com/news-events/press-releases/detail/1040/marvell-and-lumentum-to-combine-creating-a-category-leader-in-ai-connectivity')
add('HBM-server-package-lead','HBM server-package smuggling report remains an attributed lead','ZHAO VULCAN','PROME','AI_INFRA_CAPEX','ASIA_CONTAGION','HBM Huawei-960DT South-Korea',
'''TrendForce November 3 attributes to The Information a mechanism in which HBM is shipped with lower-performance processors and removed after arrival in China, alongside Huawei 960DT memory constraints. The original subscription body was inaccessible; unnamed-source independence, shipment volume, technical implementation and legal treatment were not verified.

ACTION ZHAO/VULCAN: retain this as a source-limited lead in existing controls/supply-chain coverage; upgrade only with original or independent evidence. It is not a confirmed export-control loophole, deployment or yield claim. INFO PROME: source dependency. Access failure is not falsity.''',
'https://www.trendforce.com/news/2026/11/03/news-china-reportedly-obtains-smuggled-hbm-via-server-packages-huawei-960dt-faces-domestic-hbm-shortage/ ; https://www.theinformation.com/articles/smugglers-get-expensive-memory-chips-china-south-korea',confidence=.6)
add('ConnectWise-Nov4-restoration','ConnectWise advances partial restoration; tenant uncertainty remains','CYPHER','PROME','CYBER','CYBER','ConnectWise CYB-INC-018',
'''Vendor advisory observed November 4 at 18:55 UTC advances the October 30 baseline in SIG-W-20261102-013: phase 3 is partly complete, Backup Health reporting/export jobs and Marketplace APIs returned November 3. Billing/API-related functionality remains in progress; notifications are returning gradually and Microsoft 365/Azure reconnection remains relevant.

ACTION CYPHER: update CYB-INC-018 restoration state using the timestamped vendor advisory. The vendor cannot determine individual tenant compromise from unavailable tenant-side logs. Restoration does not prove absence of persistence, identify financial-sector victims, or constitute a new breach. INFO PROME: existing-incident continuity.''',
'https://www.connectwise.com/company/trust/advisories')
add('Delaware-Life-sale-exploration','Delaware Life sale exploration is reported; price and capital implications remain unverified','SHADE','BROCK PROME RED','PC_STRESS','INSURANCE_SHADOW','Delaware-Life Mark-Walter TWG-Global Cadillac-F1',
'''FT's November 3 accessible headline reports Mark Walter exploring a sale of Delaware Life, described as a $71B insurer. The original body is subscription-limited; that figure is not verified sale consideration or proceeds. Related Cadillac F1 reports cite approximately $3B, but team-versus-stake basis is unresolved and Sportico's original was inaccessible.

ACTION SHADE: integrate the attributed exploration into the existing related-party/probe watch, preserving source limits and unresolved transaction execution. INFO BROCK/PROME/RED: manager-wrapper overlap. Exploration is not a completed or forced sale, capital shortfall, realized insurer loss or a finding of wrongdoing. Existing affiliate-exposure figures remain dated exposures, not losses; this reporting does not resolve the conditional exchange's execution.''',
'https://www.ft.com/content/570191b9-7910-4627-8779-6a382ef26613 ; https://www.sportico.com/business/team-sales/2026/mark-walter-f1-cadillac-stake-sale-1234957228/',confidence=.6)
add('IEA-winter-gas-scenario','IEA sub-10% March storage scenario requires both cold weather and continued disruption','HANS BRENT','AEOLUS WATT RED','INFLATION_TRANSMISSION','OIL_ENERGY','IEA EU-Gas-Storage Hormuz',
'''IEA's November 3 Global Gas Security Review says EU heating-season opening stocks are the lowest since 2013. Its end-March 2027 sub-10% storage simulation requires BOTH colder-than-average weather AND continued Hormuz LNG disruption. Low stocks increase summer refill needs; withdrawal capability tends to diminish below 30%.

ACTION HANS/BRENT: incorporate the conditional scenario into existing winter supply/refill work. INFO AEOLUS/WATT/RED: weather, power and counterfactual context. It is not a current storage reading, unconditional forecast, or a newly fired threshold. Do not remove either condition when transmitting the result.''',
'https://www.iea.org/reports/global-gas-security-review-2026/executive-summary')
add('YANOS-Nov3-fire','November 3 YANOS refinery damage is reported; lost output is unknown','OSPREY BRENT','HAWK YURI','HYDROCARBON_INFRA','GEOPOL_ENERGY','YANOS Yaroslavl',
'''November 3 reporting describes fire/damage at Yaroslavl's YANOS refinery after an overnight drone attack. Meduza reports Governor Evraev's acknowledgment of infrastructure damage and two injured employees; ISW describes geolocated fire imagery. The original governor post and imagery were not independently inspected in this pass.

ACTION OSPREY: reconcile the dated strike and quiet-day implications in the existing ledger. ACTION BRENT: assess operational consequences when actual throughput/duration evidence arrives. INFO HAWK/YURI: cross-war/state context. Damage extent and lost processing volumes remain unknown; nameplate capacity is not production lost. This is separate from the October 20 Tambov event recirculated in November 2 intake.''',
'https://meduza.io/en/news/2026/11/03/ukrainian-drone-strike-sparks-major-fire-at-one-of-russia-s-largest-oil-refineries ; https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-november-3-2026/',confidence=.8)
add('CVR-Marathon-refinery-agreement','CVR agrees to buy two Marathon refineries; capacity is transferred','BRENT','BROCK','HYDROCARBON_INFRA','OIL_ENERGY','CVR-Energy Marathon-Petroleum St-Paul-Park Mandan',
'''CVR's SEC-filed November 3 release establishes CVR as BUYER and Marathon as SELLER of St. Paul Park and Mandan refineries plus marketing assets. Agreement dated November 2: approximately $4.2B plus net working capital. Financing includes $2.5B committed secured debt, $500M controlling-shareholder equity and $800M Trafigura financing, plus cash. Existing 2031/2034 notes become equally secured; 2028 notes are to be redeemed.

ACTION BRENT: update existing refinery ownership/financing context. INFO BROCK: secured-credit structure. This is an agreement, not completion or new US refining capacity. Conflicting headline direction in the intake must not reverse buyer and seller.''',
'https://www.sec.gov/Archives/edgar/data/1376139/000119312526444428/d87305dex991.htm')
add('Homs-plot-allegation','Syria announces a foiled Homs plot; Hezbollah denies the attributed role','HAWK','BRENT','IRAN_HORMUZ','GEOPOL_NON_ENERGY','Homs SANA Hezbollah',
'''SANA November 3 relays Syrian security authorities' announcement of arrests and seized explosives intended for Homs refinery, alleging Hezbollah links. Reuters reporting carries Hezbollah's denial. A November 1 report already described an unidentified plot; the new development is the attributed official account.

ACTION HAWK: integrate the claim/denial in existing theater coverage. INFO BRENT: refinery threat context only. Arrest timing is unstated; no completed attack, outage, throughput loss or authenticated Hezbollah responsibility is established. Neither an alleged plot nor an official accusation establishes executed damage.''',
'https://sana.sy/en/syria/2355673/ ; https://www.algemeiner.com/2026/11/03/syria-says-foiled-hezbollah-plot-attack-homs-oil-refinery/',confidence=.75,narrative_channel='houthi',confidence_note='Syrian state announcement; narrative enum has no Syrian category. houthi is not attribution; see body.')
# Omit an unsupported channel classification by using the non-Iran infrastructure bucket for Syria.
D[-1]['cluster']='HYDROCARBON_INFRA';D[-1]['extra']={}
add('Iran-Nov1-two-tanker-mine-claim','Iranian two-tanker mine allegation lacks hull identities or neutral confirmation','FALCON','BRENT HAWK','IRAN_HORMUZ','GEOPOL_ENERGY','IRGC Hormuz',
'''November 1 InvestingLive reporting attributes to IRGC an allegation that two tankers, including a supertanker, hit mines that Sunday. The inspected text supplies no hull names, flags or independent incident confirmation; the Mehr original was unavailable. This is distinct from the October 29 three-tanker allegation.

ACTION FALCON: assess this dated claim against its existing vessel census without merging unnamed hulls into LOUISE 1/RITI/QUBA or earlier incidents. INFO BRENT/HAWK: claim-only theater context. No new confirmed loss, mine detonation, casualty or attribution is established. Iran's separate conditional two-day reopening proposal is already covered by SIG-W-20261102-011 and is not an agreement or demonstrated reopening.''',
'https://investinglive.com/commodities/iran-says-two-tankers-hit-mines-in-hormuz-as-tehran-offers-two-day-reopening-plan/',confidence=.5,narrative_channel='tasnim')
add('SF-Fed-ENSO-conditional-model','SF Fed ENSO model links 2027 price effects to a conditional La Nina reversal','AEOLUS CARL','BRENT HENRY RED','CLIMATE_MACRO','MACRO_INFLATION','San-Francisco-Fed El-Nino La-Nina',
'''San Francisco Fed's November 2 Economic Letter estimates a roughly 0.3 percentage-point price-level effect in April–July 2026 fading by year end, and a roughly 1 percentage-point net PCE price-level increase in 2027 conditional on a subsequent La Nina. Without that reversal, its model produces no additional net price effect. These are model estimates, not observed inflation contributions or a forecast.

ACTION AEOLUS/CARL: assess the conditional climate-to-prices mechanism in existing work, retaining limited strong-event observations and linear scaling. INFO BRENT/HENRY/RED: energy and macro context. The conditional direction must survive transmission; this paper does not establish that La Nina will occur.''',
'https://www.frbsf.org/research-and-insights/publications/economic-letter/2026/11/the-impact-of-el-nino-on-the-us-economy/')

def write(ds,start=1):
 stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ');paths=[]
 for n,d in enumerate(ds,start):
  sid=f'SIG-W-20261104-{n:03d}'; rel=f'BOARD/{sid}-{d["slug"]}.md';p=ROOT/rel
  assert not p.exists(),p
  body='# '+d['title']+'\n\n'+d['body']+'\n\nSources: '+d['sources']+'\n'
  wc=len(body.split());assert d['precedence'] not in ('FLASH','IMMEDIATE') or wc<=200,(sid,wc)
  h=dict(signal_id=sid,timestamp=stamp,dispatched=stamp,source='WALTER',origin=['RESEARCH-INTAKE / November 2–4 catchup and primary-source verification'],action=d['action'],info=d['info'],precedence=d['precedence'],signal_type='research',confidence=d['confidence'],confidence_language='confirmed' if d['confidence']>=.9 else 'reports' if d['confidence']>=.7 else 'assessed',resources=1,safety_net='clear',cluster=d['cluster'],domain=d['domain'],entities=d['entities'],word_count=wc,dispatch_note='Bounded catchup; written pending coordinated publication. Owner grades, delivery and consumption remain separate.',**d['extra'])
  p.write_text('---\n'+''.join(k+': '+json.dumps(v)+'\n' for k,v in h.items())+'---\n'+body);paths.append(rel)
  with (W/'routed/route_log.tsv').open('a') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerow([stamp,sid,'RESEARCH-INTAKE / catchup primary checks',d['title'],d['precedence'],','.join(d['action']),','.join(d['info']),d['confidence']])
  for role,names in [('ACTION',d['action']),('INFO',d['info'])]:
   for name in names:
    if name in {'TERRY','PROME'} or role=='INFO' and name in {'CARL','RED'}:continue
    hr=f'AGENTS/{name}/inbox/WALTER/{sid}.md';hp=ROOT/hr;assert not hp.exists(),hp;hp.parent.mkdir(parents=True,exist_ok=True)
    hp.write_text(f'# {sid} — {d["title"]}\nBOARD: /{rel}\nPriority: {d["precedence"]}\nRole: {role}\nFrom: WALTER\nDate: 2026-11-04\n\n## Kernel\n{d["body"]}\n\n## Why you got this\n{name}: {role} on the canonical recipient line; ownership and source limits above.\n\n## Requested action\n'+('Apply only the named existing owner work above; no new study or launch authorized.' if role=='ACTION' else 'Context only; no directed ask.')+f'\n\n## Confidence / caveats\n{d["confidence"]}; source dates and interpretation limits retained above. Written is not delivered or consumed.\n\n## Cross-refs\n/{rel}\nSources: {d["sources"]}\n')
    paths.append(hr)
    with (W/'routed/delivery_log.tsv').open('a') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerow([stamp,sid,name,role,'CC',d['precedence'],hr,'written_not_delivered_pending_push','Codex-authored; publication and owner consumption unverified.'])
 existing=json.loads((OUT/'dispatch-paths.json').read_text()) if (OUT/'dispatch-paths.json').exists() else []
 (OUT/'dispatch-paths.json').write_text(json.dumps(existing+paths,indent=2)+'\n')
 print(f'Created {len(ds)} signals and {len(paths)-len(ds)} handoffs; IDs {start}–{start+len(ds)-1}')
if __name__=='__main__':write(D)
