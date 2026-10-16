"""One-time reviewed dispatch writer. Create-only BOARD/handoffs; explicit paths."""
import csv,json
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[4]; W=ROOT/'AGENTS/WALTER'; HERE=Path(__file__).resolve().parent
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
S=[]
def add(n,slug,title,domain,cluster,action,info,confidence,body,ask,**extra):
 S.append(dict(n=n,slug=slug,title=title,domain=domain,cluster=cluster,action=action.split(','),info=info.split(','),confidence=confidence,body=body,ask=ask,extra=extra))
add(16,'china-september-ppi-upstream-pressure','China September PPI rises 5.0% year on year; downstream inflation and US bond implications remain separate','ASIA_CONTAGION','INFLATION_TRANSMISSION','ZHAO','CARL,HENRY,LIQUID,RED,PROME',.95,
'''NBS September2026 producer-price release, published October14: PPI +5.0% y/y and +1.2% m/m; producer purchasing prices +6.9%/+1.2%. Production goods +6.5% y/y versus consumer goods −0.1%; fuel/power input purchases +13.6% y/y. This is upstream pressure with uneven downstream transmission. NBS notes the January2026 base change has about0.08pp average influence on the annual PPI rate.

Primary: https://www.stats.gov.cn/sj/zxfbhjd/202610/t20261014_1965476.html . Recovered directly after the bookmark's CNBC link failed. Bookmark2110544165780295995 is October15; release date is October14. Its pandemic-scale inflation/TLT forecast is commentary, not established by Chinese PPI. China domestic prices are not US import prices or a calibrated Treasury forecast.''',
'ZHAO: assess upstream versus downstream transmission in the China macro read; no new tracking mandate or trade implied.')
add(17,'volta-bloomberg-sale-terms-evidence-upgrade','Bloomberg reports Volta loan sold at benchmark plus 650bp and 95 cents; exact final yield remains unknown','PRIVATE_CREDIT','AI_INFRA_CAPEX','VULCAN,LIQUID','BROCK,VIOLET,RED,PROME',.85,
'''Bloomberg's October15 19:25ET report (Laura Benitez/Jeannine Amodeo), now recovered in full via Yahoo, says the roughly$5B Volta financing sold Thursday at benchmark+650bp and95cents versus initial625–650/97–98. Yield is described only as above11%. Added terms include an early-repayment penalty and rating-dependent interest changes. Sources are unnamed people; banks/issuer did not certify closing documents.

This upgrades the sourcing of SIG-W-20261016-005 item1; its other credit/equity-listing observations retain their own dates and caveats. VULCAN's pre-stated comparator is formalOctober9 launch talk: +650 is below its≥800 margin leg; sold does not satisfy PULLED. ExactYTM for its≥13.25% alternative is UNKNOWN; discount95 cannot be translated without maturity/cashflows/fees. LIQUID's L3 is a separate letter. No owner grade changed.

Source: https://uk.finance.yahoo.com/news/jpmorgan-goldman-boost-yield-volta-232556640.html . Evidence: AGENTS/WALTER/research/2026-10-16_finish/verify-credit.md.''',
'VULCAN: adjudicate S5 using the stronger source and retain the exact-yield gap. LIQUID: evaluate the report under L3 on its own terms; no imported S5 grade.')
add(18,'jmic-cape-dao-status-conflict-container-clocks','JMIC publication disputes Cape Dao sinking; container incident dates reconcile across UTC and Singapore time','GEOPOL_ENERGY','IRAN_HORMUZ','FALCON','BRENT,HAWK,SAM,RED,PROME',.75,
'''UKMTO172/173 warnings datedOctober14 report events October13 16:40/17:00UTC. These are October14 00:40/01:00Singapore. MPA's October14 GFS GISELLE event therefore need not be a new attack. Keep hull, event/report clock, direction, mechanism and position distinct.

UKMTO-posted JMIC105 (cutoffOctober15 13:00UTC) provisionally maps172→GFS GISELLE and173→AL SAADIYAT. The posted PDF filename saysFINAL but pages carryDRAFT. It disputes Cape Dao's sinking, conflicting with the carried October14 IMO/FALCON finding. Publication status and source disagreement preclude silently deleting a loss. FALCON's five-loss census and approved B1/C14/D85 remain owner state, not regraded here.

Primary PDFs/MPA and precise retrieval limits: AGENTS/WALTER/research/2026-10-16_finish/verify-energy.md §2. JMIC link: https://t.co/sqhiqm9AeT . MPA: https://www.mpa.gov.sg/media-centre/details/two-singapore-registered-vessels-struck-in-strait-of-hormuz .

anchor_unverified_as_of: 2026-10-15. Bounded current check completed; full kinetic/diplomatic sweep not reset. This is a fresh source conflict requiring owner adjudication, not a certified new sinking, mine detonation or attack.''',
'FALCON: adjudicate Cape Dao against a clean final JMIC/IMO/navigation record; resolve the earlier003 clock/mapping question without double-counting.',narrative_channel='centcom',confidence_note='Confidence in identifying a published source conflict; sinking outcome and provisional mappings remain unresolved.')
add(19,'trepp-september-special-servicing-sector-flows','Trepp September special servicing reaches 11.49%; office eases while multifamily rises','BANK_CRE','BANK_COLLATERAL','CREED,HOMER','REGINALD,BROCK,CARL,RED,PROME',.95,
'''Trepp September full report (excerpt publishedOctober13), all-vintages Table1: overall special servicing11.49%, +7bp; office16.85%, −5bp; multifamily8.54%, +17bp; retail13.84%; lodging8.95%; mixed-use13.17%; industrial1.23%. Office remains below its registered>18 two-month bar. Multifamily belongs to HOMER, other national CRE to CREED.

Incoming transfers$2.65B/42wholeloans versus August$3.04B/29; exits$1.95B/48 versus$579.7M/32. Office represents57% of incoming balance. Reported exits mix returns to master servicing and zero balances, so they do not uniformly mean successful refinancing. August$3.04B is this report's comparison vintage, differing from the older owner$3.16B; reconcile rather than overwrite.

Named case: One SoHo Square, New York NY,$512.8M, transferAugust28 in the September report, current payments. Report simultaneously states imminent balloon/maturity default and maturityAugust6,2028; contradiction unresolved. No inferred acceleration or revised maturity.

Source: https://www.trepp.com/hubfs/Trepp%20CMBS%20Special%20Servicing%20Report%20September%202026.pdf . Full PDF/text and table verification: research/2026-10-16_finish/verify-credit.md. September officeDQ12.16 was already009-Oct-002; DQ and special servicing are different series.'''.replace('009-Oct-002','SIG-W-20261009-002'),
'CREED: grade the office print, reconcile comparison vintage and record the named case with the maturity conflict. HOMER: integrate the multifamily special-servicing print.',case=['One SoHo Square, New York NY'])
add(20,'liq07-publication-frontier-no-funding-accompaniment','LIQ-07 funding windows are observable; available data support no reserve-channel accompaniment','FUNDING_LIQUIDITY','BANK_COLLATERAL','LIQUID','RED,BOND,HENRY,REGINALD,PROME',.90,
'''Both named±10-session windows aroundSeptember30 have reached the publication frontier: SOFRSeptember16–October15; ICEsingle-BSeptember16–October14 includes the October12 non-SOFR holiday. Saved explicit date inventories preserve that mismatch.

October15 SOFR75−IORB +4bp;99−IORB +7bp; SRF$0.111B. Owner pure-function arithmetic gives robustz−0.337245 and slope+5.04bp/year. Across available matched funding observations in both windows, maximum eligiblez−0.224830, maximum99−IORB+9bp, maximumSRF$1.2B. None supplies the registered accompaniment. CandidateS2 means “no reserve-channel loop observed”, not no loop; collateral, redemptions, term-credit and offshore channels remain outside this test.

Latest-revised history is not first-publication reconstruction; missing holiday observation is not zero. NYFed publishes possible revisions around14:30ET, so vintage policy remains part of owner adjudication. Frozen credit trigger not regraded and predictionResolveByNovember10 unchanged.

Evidence and arithmetic: AGENTS/WALTER/research/2026-10-16_finish/verify-credit.md and credit-liq07-arithmetic.json. Sources: https://www.newyorkfed.org/markets/reference-rates/sofr and FRED series listed in credit-funding.json.''',
'LIQUID: adjudicate LIQ-07 on the registered calendar/vintage, retain the narrow channel meaning and record the owner verdict; this packet is evidence, not a grade.')
add(21,'eurostat-september-final-core-first-qualifying-month','Eurostat September final core inflation is 2.5%; first of two qualifying months, not a fire','EUROPE_MACRO','INFLATION_TRANSMISSION','HANS','BOND,LIQUID,CARL,RED,PROME',.95,
'''Eurostat published September FINAL HICP todayOctober16: core excluding energy,food,alcohol,tobacco2.5%y/y versus August2.4%; headline3.8%y/y and0.6%m/m; energy18.9%y/y and4.0%m/m. The energy flash18.8 is revised. HANS-T16≥2.5 for two consecutive finals has1/2, NOT a fire.

Release header schedules OctoberFLASH November4 and FINAL November18. Those replace approximateOctober17/October31 carry dates; a flash cannot complete the final-print sustain. German compositeSeptemberFINAL53.8 (October5 licensedTE display) also supersedes an August51.8 carry but remains above its<48 bar; originalS&P release was not recovered.

Primary: https://ec.europa.eu/eurostat/web/products-euro-indicators/w/2-16102026-ap . Direct publicGET succeeded while web rendering failed; substantive table retained in hans-eurostat-sep-final-extracted.txt. Full row/basis review: AGENTS/WALTER/research/2026-10-16_finish/verify-hans.md.''',
'HANS: update the final-print observation and calendar under the existing letter; retain1/2 and avoid an early fire.')
add(22,'korea-close-flow-direction-vintage-followup','Korea October16 close net buying is corroborated; exact primary total remains unavailable','JAPAN_BOJ','POSITIONING_VALUATION','SAM','HENRY,VULCAN,ZHAO,RED,PROME',.80,
'''Follow-up to SIG-W-20261016-006: the conflicting AJU net-selling observation was10:00KST, while KoreaTimes and Edaily close reports give KOSPI foreign net buying₩341B. An intraday sell reading can coexist with a net-buying close. Later AJU also reports buying but₩172.1B; its full body was unrecovered. Exact amount and primary finality remain unresolved.

Both direct KRX queries returned400LOGOUT, including a fresh public session. No KRX-confirmed figure is claimed. KOSDAQ foreign flow is a different market; KOSPI buying alone establishes neither a durable reversal of the prior streak nor a Japan carry-unwind verdict.

Sources: https://www.koreatimes.co.kr/amp/economy/20261016/samsung-sk-hynix-sell-off-excessive-as-memory-outlook-stays-strong-analysts ; https://en.edaily.co.kr/news/eda202610165501/ . Retrieval and conflicting laterAJU basis: AGENTS/WALTER/research/2026-10-16_finish/verify-hans.md §Korean foreign-flow conflict.''',
'SAM: narrow the direction-conflict carry to secondary close corroboration while retaining the exact-value/primary gap; preserve intraday versus close dates.')
add(23,'kobeissi-bullish-countercase-with-basis-limits','Kobeissi countercase: earnings resilience may support equities, but breadth and valuation comparisons remain unverified','MARKET_VOL','POSITIONING_VALUATION','HENRY','VULCAN,RED,PROME',.65,
'''Will-supplied PDF of The Kobeissi Letter argues that strong earnings and lower tech multiples could sustain equities or broaden gains if energy/inflation pressure eases. This is a bullish conditional countercase, not a war-end forecast, a proven harmless-concentration claim or a model-derived9,000 target.

Primary FactSet August28Q2 vintage confirms52% blended earnings growth at97% reporting. Excluding Alphabet and Amazon lowers growth to33.8%; their GAAP investment gains matter. That is removal of two companies, not removal of investment gains alone. The PDF earnings chart says47.4% while prose says52%, with different vintages unreconciled.

Breadth84% down≥10% from own highs/59%≥20%, and ten stocks contributing70% of the rally, remain Bloomberg/Nomura-attributed claims without original calculations. Individual all-time highs are different dates, not a common-period index bear market. The PDF NVIDIA chart says P/E27.98 rather than proving forward24; its Yardeni chart shows broad-index18.9 versus prose22. Matching consensus horizon/provider is missing.

Primary: https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_082826.pdf . PDF supplied at /mnt/c/Users/willi/Downloads/The Kobeissi Letter.pdf; full text and graph labels reviewed, publisher-host authentication unavailable. Verification: AGENTS/WALTER/research/2026-10-16_finish/verify-kobeissi.md.''',
'HENRY: consider the conditional bullish countercase against the current market read; distinguish recurring earnings/revisions and common-period breadth from the unverified statistics. No new model/tracking mandate.',signal_role='counter_evidence')
add(24,'tanker-weekly-vintage-separated','Tanker monitor separates strong older weekly averages from a mixed October15 route snapshot','OIL_ENERGY','HYDROCARBON_INFRA','BRENT','HAWK,FALCON,RED,PROME',.80,
'''Signal Group monitor publishedOctober16 labels Week41 but compares September28–October2 with October5–9: BDTI7,625,+32%; BCTI2,388,+2%; TD3CWS1,288,+12%. These are NOT changes for the week endingOctober16.

Its daily chart endsOctober14 (BDTI7,922 versusOctober13peak7,999). SeparateOctober15 snapshot: TD3C$1,356,523/day,−2.8% against that dashboard's prior-week reference; nine of16dirty routes declined, while Suezmax and westernAframax moved in opposite directions. Assessed route economics are not fleet realized profits or completed fixtures.

Publisher search-rendered body recovered: https://www.thesignalgroup.com/weekly-market-monitor/weekly-tanker-market-monitor-week-41-2026 . Direct body access failed. BalticOctober16Week42 tanker body remains unrecovered; a2025Week42 search result was rejected. No Worldscale boundary grade inferred from a differently specified route/report.

Evidence: AGENTS/WALTER/research/2026-10-16_finish/verify-energy.md §3. This updates available Friday evidence with explicit vintage limits, not a completed Baltic refresh.''',
'BRENT: incorporate the distinct observation periods in the freight read and retain the Baltic registered-source gap; no uniform current-week freight-up inference.')
add(25,'fhlb-q3-official-publication-calendar','FHLB Q3 calendar separates October30 highlights from November13 Combined Financial Report','BANK_CRE','BANK_COLLATERAL','REGINALD','LIQUID,RED,PROME',.95,
'''FHLB Office of Finance official calendar lists Q3 operating highlights October30 and Combined Financial Report November13, subject to change. This replaces the owner's approximateOctober29 carry as a publication expectation, without altering any threshold or grading basis.

REG-T06 names the Combined Financial Report system-wide period-end advances balance, all11banks, >$700B for three quarterly prints. Owner datedQ2$810.7B andQ1$734B supply2/3; the threshold is not completed by a calendar notice. Owner adjudication is needed before treating a highlights balance as an eligible substitute for the named report.

Primary calendar: https://www.fhlb-of.com/investor-resources/financial-reports/ . Evidence: AGENTS/WALTER/research/2026-10-16_finish/verify-red-reg.md. No new fire or owner method change.''',
'REGINALD: reconcile the Q3 observation date and whether an earlier highlights release is eligible under your existing source letter; do not silently change that letter.')

manifest=[]
for x in S:
 sid=f'SIG-W-20261016-{x["n"]:03d}'; path=ROOT/'BOARD'/f'{sid}-{x["slug"]}.md'
 header=dict(signal_id=sid,date='2026-10-16',timestamp=NOW,dispatched=NOW,source='WALTER',origin='Unfinished-work source verification; see body',domain=x['domain'],cluster=x['cluster'],entities={'16':['China-NBS','China-PPI'],'17':['Volta'],'18':['JMIC-105','CAPE-DAO','GFS-GISELLE','AL-SAADIYAT'],'19':['Trepp','One-SoHo-Square'],'20':['SOFR','IORB','LIQ-07'],'21':['Eurostat','HICP'],'22':['KRX','KOSPI'],'23':['Kobeissi','FactSet','NVDA'],'24':['Signal-Group','TD3C','BDTI'],'25':['FHLB-Office-of-Finance']}[str(x['n'])],precedence='PRIORITY',action=x['action'],to=x['action'],info=x['info'],confidence=x['confidence'],confidence_language='confirmed' if x['confidence']>=.9 else 'reports' if x['confidence']>=.75 else 'assessed',resources=1,signal_type='data-point',safety_net='clear',word_count=len((x['body']+' '+x['ask']).split()),dispatch_note='Scoped verification; no owner grade or consumption inferred. Native fleet tools unavailable; Will reports PROME/CATO/WALTER active. Concurrent foreign work gates push.')
 header.update(x['extra'])
 text='---\n'+'\n'.join(k+': '+(v if isinstance(v,str) and ': ' not in v and '\n' not in v else json.dumps(v,ensure_ascii=False)) for k,v in header.items())+'\n---\n\n# '+x['title']+'\n\n'+x['body']+'\n\n## Recipient action\n\n'+x['ask']+'\n'
 with path.open('x') as f:f.write(text)
 rel=str(path.relative_to(ROOT)); manifest.append(rel)
 with (W/'routed/route_log.tsv').open('a') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerow([NOW,sid,header['origin'],x['title'],'PRIORITY',','.join(x['action']),','.join(x['info']),x['confidence']])
 for role,agents in [('ACTION',x['action']),('INFO',x['info'])]:
  for agent in agents:
   if agent in ['PROME','TERRY'] or (role=='INFO' and agent in ['CARL','RED']):continue
   hpath=ROOT/'AGENTS'/agent/'inbox/WALTER'/f'{sid}.md';hpath.parent.mkdir(parents=True,exist_ok=True)
   handoff=f'# {sid} — {x["title"]}\nBOARD: /{rel}\nPriority: PRIORITY\nRole: {role}\nFrom: WALTER\nDate: 2026-10-16\n\n## Kernel\n\n{x["body"]}\n\n## Requested action\n\n'+(x['ask'] if role=='ACTION' else 'Information only; no recipient-directed request.')+'\n\n## Confidence / caveats\n\n'+str(x['confidence'])+'; source limitations above. Delivery is not owner consumption.\n'
   with hpath.open('x') as f:f.write(handoff)
   hp=str(hpath.relative_to(ROOT));manifest.append(hp)
   with (W/'routed/delivery_log.tsv').open('a') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerow([NOW,sid,agent,role,'UNKNOWN','PRIORITY',hp,'written_not_delivered_pending_push','Codex authored; current desk liveness not inferred from helper sessions; owner consumption UNKNOWN.'])
 for agent in x['action']:
  with (W/'registry/DOORBELL_LOG.tsv').open('a') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerow(['2026-10-16',agent,sid,'NONE','P0-UNKNOWN','NO','NA','NA','NA','','No native fleet visibility; Will named PROME/CATO/WALTER active; no cross-runtime relay tool. Foreign writes gate push.'])
(HERE/'dispatch-manifest.json').write_text(json.dumps({'as_of':NOW,'signals':len(S),'paths':manifest},indent=2)+'\n')
print(f'{len(S)} BOARD; {len(manifest)-len(S)} create-only handoffs')
