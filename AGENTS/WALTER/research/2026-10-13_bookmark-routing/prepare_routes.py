"""One-session reviewed packet preparation. No network, landing, Git or marking."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PLAN = []

def add(slug, title, items, domain, cluster, action, info, confidence, entities, body, sources, refs, ask, **extra):
    PLAN.append(dict(slug=slug, title=title, items=items, domain=domain, cluster=cluster,
                     action=action, info=info, confidence=confidence, entities=entities,
                     body=body, sources=sources, refs=refs, ask=ask, **extra))

energy = 'AGENTS/WALTER/research/2026-10-13_bookmark-routing/energy-verify.md'
ai = 'AGENTS/WALTER/research/2026-10-13_bookmark-routing/ai-credit-verify.md'
funding = 'AGENTS/WALTER/research/2026-10-13_bookmark-routing/funding-verify.md'
extra_funding = 'AGENTS/WALTER/research/2026-10-13_bookmark-routing/funding-extra-verify.md'
q3 = 'AGENTS/BROCK/research/2026-10-09_BRK-31_bank-Q3_frame_FROZEN.md'

add('pjm-issued-order-and-demand-response-not-diesel-shortage',
    'PJM received the October13–16 DOE order and called demand response; diesel-shortage framing unsupported',
    [30,44], 'POWER_GRID','AI_INFRA_CAPEX',['WATT'],['VULCAN','HENRY','BRENT','CARL','RED','PROME'],.95,
    ['PJM','DOE','Order-202-26-50'],
    'DOE202-26-50 was issued October12, effective October13–16. It cites electricity demand, generation maintenance and transmission constraints; it does not declare a diesel-supply emergency. PJM’s October13 primary update confirms the combined order and a demand-response action; posting105561 runs14:00–21:00EPT. Posting105564 identifies October14 need for specified resources, not a maximum-output directive. PJM says large-load backup generation has not been used to date.\n\nCHANGE: closes the issuance gap in WATT’s October12 request-only assessment. The order’s900MW is a forecast distance to reserve margin, not observed spare generation. Authority, paid load reduction and actual backup operation are separate. No blackout, measured diesel burn, economic loss or new trigger grade is established.',
    [('2026-10-12; effective October13–16','https://www.energy.gov/documents/doe-order-no-202-26-50','DOE order; full extracted text and supplied cover read'),('2026-10-13','https://insidelines.pjm.com/operations-update-extends-maximum-generation-alert-calls-on-demand-response/','PJM operational statement'),('2026-10-13','https://emergencyprocedures.pjm.com/ep/pages/viewposting.jsf?id=105561','Demand-response action, product requirements')],
    [energy,'AGENTS/WATT/reports/2026-10-12_DOCKET-L654_PJM-advisory-IRAS-grade.md'],
    'WATT: integrate issued-order and operating-action evidence in the existing PJM assessment. Preserve the utilization gap; any episode or threshold grade remains yours.')

add('dhahran-administrative-building-fire-output-unmeasured',
    'Dhahran fire report narrows to an administrative building; oil-output loss remains unmeasured',
    [17,18,49],'GEOPOL_ENERGY','IRAN_HORMUZ',['FALCON','BRENT'],['HAWK','RED','PROME'],.80,
    ['Saudi-Aramco','Dhahran','Sanaa'],
    'An October13 Reuters screenshot reports booms, evacuation and an uncertain direct-impact-versus-debris mechanism. A later Reuters update, syndicated October14 Saudi local with an October13 dateline, relays the Saudi Energy Ministry’s limited administrative-building fire and no injuries. The same update covers the coalition’s Sanaa oil-depot warning/operation. Direct Ministry/operator confirmation was not independently recovered. The video thumbnail is unauthenticated.\n\nCHANGE: a new dated administrative-site event after earlier generic threats. No crude or diesel output loss, sustained processing-unit outage or company-wide9.1Mb/d removal is established. Attribution and escalation synthesis remain with theater owners. This packet pairs with the new receiving-tonnage and time-late incident packets through the shipping/energy-risk channel; do not double-count them as measured lost barrels.',
    [('2026-10-13 Reuters report; syndicated update October14 Saudi local','https://www.internazionale.it/ultime-notizie-reuters/2026/10/14/saudi-led-coalition-orders-evacuation-of-yemen-oil-facility-in-sanaa-ahead-of-operation','Reuters original-wire syndication; primary Ministry body not recovered'),('2026-10-13','https://x.com/RyanRozbiani/status/2110091523559932296','Reuters screenshot visually read; early report, not independent wire')],
    [energy,'AGENTS/FALCON/workbook/KB.tsv'],
    'FALCON: integrate the dated event with direct/debris and attribution limits. BRENT: retain output UNKNOWN in the existing supply assessment. No new study or holding grade requested.')

add('df-peak-oct12-boarding-not-diesel-cargo-confiscation',
    'DF Peak boarding reported October12 south of Réunion; cargo and confiscation outcome unverified',
    [19,39],'GEOPOL_ENERGY','IRAN_HORMUZ',['HAWK','OSPREY'],['YURI','BRENT','RED','PROME'],.75,
    ['DF-Peak','France','Reunion'],
    'October12 NavalNews and Euronews reporting, attributed to Macron/French military statements, identifies DFPeak boarded more than450 nautical miles south of Réunion under false-flag/illegal-fuel suspicions. October13 reposts do not establish an October13 boarding. The directly authenticated Macron/EMA body and final judicial/cargo outcome were not recovered.\n\nCHANGE: a named sanctions-enforcement lead, not a demonstrated diesel-deal delivery loss. Cargo grade/origin/quantity/destination, permanent confiscation and links to the US diesel agreement remain UNKNOWN. Russia’s legal objection is not a legality ruling. HAWK owns enforcement synthesis; OSPREY owns the Russian-energy shipping implication; YURI receives state-response context.',
    [('2026-10-12','https://www.navalnews.com/naval-news/2026/10/french-navy-intercepts-and-boards-shadow-fleet-tanker-df-peak-south-of-reunion/','Named official-statement relay, boarding'),('2026-10-12','https://www.euronews.com/2026/10/12/french-navy-intercepts-and-boards-shadow-fleet-ship-macron-says','Official-statement relay; shared provenance possible')],
    [energy,'AGENTS/DEWEY/output/2026-10-13_diesel-commission-final.md'],
    'HAWK/OSPREY: incorporate the qualified named boarding in existing enforcement/shipping work; preserve cargo and outcome gaps. No new cargo monitor or legal grade requested.')

add('fujairah-empty-vlcc-retreat-receiving-tonnage',
    'Reported empty-VLCC retreat challenges resilient Gulf transfer receiving-tonnage assumptions',
    [27],'GEOPOL_ENERGY','IRAN_HORMUZ',['FALCON','BRENT'],['HAWK','RED','PROME'],.85,
    ['Fujairah','VLCC','Suezmax','Bloomberg'],
    'Bloomberg’s October13 original reporting, syndicated at gCaptain, describes at least10 emptyVLCCs and severalSuezmax stopping or reversing as they approached Fujairah in recent days; other ships continued. The underlying vessel-level track data and exact observation window are not independently reproduced. This is one wire, not multiple independent witnesses.\n\nCHANGE: reported withdrawal of receiving tonnage is a concrete contrary input to the existing resilient ship-to-ship bypass/operator-willingness frame. It does not measure export loss or establish the bypass-gauge fire. Fujairah indicated destinations can proxy offshore transfer intentions, not final discharge. Pair with the dated incident and Dhahran packets, while keeping their event identities and unmeasured barrels separate.',
    [('2026-10-13','https://gcaptain.com/supertankers-turn-from-gulf-oil-transfer-hub-amid-irans-attacks/','Bloomberg original-wire syndication; compiled tracking observation')],
    [energy,'AGENTS/HAWK/workbook/FLOW.tsv','AGENTS/FALCON/domain/GCC_INPORT_HULL_WATCH.md'],
    'FALCON: incorporate receiving-tonnage withdrawal in the existing bypass assessment. BRENT: preserve the observation/volume distinction in current supply work; no export-loss calculation or trigger grade requested.')

add('ukmto-time-late-notices-tally-and-identity-guards',
    'Time-late UKMTO notices add reported October11 incidents; six-ship tally and attribution remain qualified',
    [1,41,68],'GEOPOL_ENERGY','IRAN_HORMUZ',['FALCON','BRENT'],['HAWK','RED','PROME'],.75,
    ['UKMTO','JMIC','Hormuz','Sohar'],
    'gCaptain’s October12 wire summary groups164–169 as six vessels including five tankers and a container ship, with four time-late notices. Directly inspected primary168 dates an outbound products-tanker strike October11 by an unknown projectile; JMIC104 corroborates164 damage, crew safe and onward sailing. The complete six-incident primary series was not reconstructed.\n\nCHANGE: qualified time-late reporting beyond the already-routed162/164/Sohar set; preserve original event dates and reconcile hull identities with FALCON. The chart’s25 is a trailing14-day MiddleEast maritime-region total, not25 daily Hormuz attacks. Highest-ever and blanket Iranian attribution are not independently certified. The unnamed IRGC Monday claim is claim-only and must not become a seventh hull, sinking or lost cargo. Pair with the receiving-tonnage and Dhahran packets; no new casualty or output sum.',
    [('2026-10-12; events October11','https://gcaptain.com/new-reports-reveal-five-more-ships-hit-near-hormuz/','Reported grouping/time-late notice interpretation'),('2026-10-11','https://www.ukmto.org/-/media/ukmto/products/update-104-jmic-advisory-note-11-october-1.pdf?rev=ff03f3af21364e44a4e9413136d44456','JMIC104 primary inspected'),('2026-10-11 incident; late notice','https://t.co/uZYr0SsNZ8','Primary168 PDF retrieved by helper; other late PDFs access-limited')],
    [energy,'BOARD/SIG-W-20261011-007-sohar-oman-MT-petro-dolphin-drone-hit-at-anchorage-2-indian-crew-missing-plus-valthera-named-hormuz-hit-10-11-FALCON-BRENT.md'],
    'FALCON: reconcile the late notices within existing hull/event evidence before changing counts. BRENT: retain physical-output UNKNOWN. No new loss/attribution or trigger grade requested.')

add('neso-transmission-delay-assistance-secure-supply',
    'NESO requested up to1,200MW French assistance after a transmission-return delay; supplies stayed secure',
    [51],'POWER_GRID','MISC',['WATT','HANS'],['RED','PROME'],.95,
    ['NESO','National-Grid-Electricity-Transmission','France','Great-Britain'],
    'The authenticated complete NESO five-post October12 thread says a delayed NationalGrid transmission-asset return reduced afternoon network capability. NESO reports EmergencyAssistance at16:52 (source timezone unspecified) and requests for700MW followed by500MW of extra French-interconnector imports, up to1,200MW support. It expressly reports secure supplies and no customer interruption.\n\nCHANGE: direct operator evidence closes the earlier thread-access gap and replaces the third-party-only status of the1,200MW claim. Assistance requests are not independently metered delivered flow. Duration and price remain unmeasured; no blackout, demand-surge, diesel-shortage or European funding consequence established.',
    [('2026-10-12,17:07:06–09Z','https://x.com/neso_energy/status/2109692347365658789','Complete authenticated operator thread, five posts read')],
    [energy,'AGENTS/WATT/STATUS.md'],
    'WATT/HANS: integrate this bounded operator event in existing power/European-energy context. Preserve request-versus-delivered-flow and continuity distinctions; no new score or monitoring scope requested.')

add('volta-underwriting-order-not-cleared-financing',
    'Volta financing reports shift underwriting risk; Apollo’s order is not an insurer exposure or closed allocation',
    [5,67],'PRIVATE_CREDIT','AI_INFRA_CAPEX',['BROCK','LIQUID'],['VULCAN','SHADE','RED','PROME'],.80,
    ['Volta-Infrastructure','JPMorgan','Goldman-Sachs','Apollo','Anthropic'],
    'Bloomberg’s October13 original-reporting excerpt attributes$1.3bn bank underwriting versus$3.7bn GPU financing excluded from that underwriting to people familiar. Semafor’s complete October13 article reports expected pricing later this week at least11%, an Apollo$1.5bn order and allocations still being discussed. Rate relief is reportedly conditional on Anthropic attaining investment-grade status. Company/loan-document confirmation is absent.\n\nCHANGE: new named financing-risk allocation and placement lead in the existing AI-credit frame. Excluded underwriting does not establish unfunded debt, failed syndication or banks selling funded positions. The Apollo order is not a closed allocation, Athene holding or insurer loss. LIQUID’s prior CDS leg and VULCAN’s October9 Firmus-equity trigger remain already fired; this does not re-fire them or commission a broader study.',
    [('2026-10-13','https://news.bloomberglaw.com/banking-law/jpmorgan-goldman-curb-exposure-on-5-billion-volta-ai-loan-1','Original-reporting excerpt; remainder paywalled'),('2026-10-13','https://www.semafor.com/article/10/13/2026/voltas-5-billion-debt-deal-is-a-pulse-check-on-the-ai-financing-boom','Full publisher body plus screenshot read; expected terms, not cleared pricing')],
    [ai,q3,'AGENTS/VULCAN/workbook/VX.tsv'],
    'BROCK/LIQUID: incorporate the named underwriting/placement lead in existing financing work, retaining final terms and holder identity UNKNOWN. SHADE is information-only; no insurer transmission or new study asserted.')

add('ai-credit-quote-leads-instrument-and-cohort-unverified',
    'AI-credit screenshots and thread claims lack matched instruments and named cohort confirmation',
    [9,29],'FUNDING_LIQUIDITY','AI_INFRA_CAPEX',['LIQUID'],['BROCK','VULCAN','RED','PROME'],.45,
    ['CoreWeave','CRWV','Oracle','SMCI'],
    'The CoreWeave-attributed CDS image shows CZ037664Curncy998.7228 without borrower, tenor, quote/trade basis or terminal timezone; its printed prior high1001.460 is July29. The bond image shows15.110%YTM with AllTime selected, without identified bond or dated endpoint. These cannot establish a one-day blowout or bankruptcy. The full author thread additionally alleges OracleCDS>260bp, unnamed GPU-hoster LTV/cash-flow breaches and forced SMCI revolver tightening. Those contract/quote claims remain independently unconfirmed.\n\nCHANGE: source-specific quote and contract-change pointers with explicit gaps, not a matched-basis new CDS fire or demonstrated spreading cohort. Existing LIQUID instrument distinctions and BROCK’s CoreWeave-versus-generic-GPU collateral limits survive. SMCI’s June30 compliance in its August31 10-K does not clear an October allegation, and no verified October amendment was recovered in the bounded check.',
    [('2026-10-13','https://x.com/INArteCarloDoss/status/2110088719059595551','Full authenticated author thread plus screenshot read; claim-grade'),('2026-10-13 repost','https://x.com/rdd147/status/2110004402232975761','Unidentified YTM screenshot visually read'),('2026-08-31; June30 reporting date','https://www.sec.gov/Archives/edgar/data/1375365/000137536526000022/smci-20260630.htm','Note8 baseline compliance/amendment terms, not October clearance')],
    [ai,'AGENTS/WALTER/research/2026-10-13_bookmark-routing/ai-credit-thread-verify.md','AGENTS/LIQUID/analysis/2026-09-28_L510-isda-benchmark.md'],
    'LIQUID: keep these source-specific pointers separate from the existing identified instrument and cohort conclusions. No independent current spread, bankruptcy probability, new fire or broad financing study established.')

add('bac-penalty-crediting-not-regional-credit-loss',
    'BAC’s$1.2bn FinCEN penalty credits the OCC$750M; separate OFAC settlement is much smaller',
    [21,22],'BANK_CRE','BANK_COLLATERAL',['REGINALD'],['BROCK','RED','PROME'],.95,
    ['Bank-of-America','BAC','FinCEN','OCC','OFAC'],
    'October13 regulator releases confirm FinCEN’s$1.2bn AML penalty credits the OCC’s$750M assessment. They must not be added as separate incremental charges. OFAC separately settles475 apparent violations for$11,662,930 and describes the matter as non-egregious. Issuer charge timing, tax treatment and Q3 financial effect were not retrieved at primary.\n\nCHANGE: named regulatory-expense context, not borrower credit deterioration, private-credit loss or regional-bank funding strain. BAC is a large-bank comparator; this does not expand REGINALD’s regional cohort. The posts’ headline figure should not become a cross-bank credit-loss total.',
    [('2026-10-13','https://www.fincen.gov/news/news-releases/fincen-assesses-12-billion-penalty-against-bank-america','FinCEN primary penalty/crediting'),('2026-10-13','https://www.occ.gov/news-issuances/news-releases/2026/nr-occ-2026-89.html','OCC primary'),('2026-10-13','https://ofac.treasury.gov/recent-actions/20261013_33','OFAC primary settlement')],
    [funding,'AGENTS/REGINALD/reports/2026-10-09_Q3_earnings_read_plan.md'],
    'REGINALD: retain regulatory expense separately from credit-loss/funding evidence in existing bank comparisons. No regional-cohort addition or credit grade requested.')

add('CORRECTION-external-tga-average-versus-wednesday',
    'CORRECTION: TGA$880.253bn is the weekly average; October7 Wednesday balance is$885.783bn',
    [26],'FUNDING_LIQUIDITY','FED_FRAMEWORK',['LIQUID'],['BOND','RED','PROME'],.95,
    ['Treasury-General-Account','Federal-Reserve','LHMacro'],
    'H.4.1 October8 Table1 identifies TGA$880,253M as the weekly average and$885,783M as the Wednesday October7 point balance. The bookmarked chart labels its$880bn figure Wednesday; LIQUID’s current STATUS carries$880.3B[10/7] without the average qualification. The earlier WALTER signal049 explicitly framed reserve balances as weekly averages and did not establish this chart’s Wednesday claim.\n\nCHANGE: correct the measurement label where a point cash balance was intended; do not replace a valid weekly-average series with a point series. If the unverified$7.16T trailing-outlay denominator is assumed, derived coverage is44.87 versus45.16days; both round45. The denominator,80th percentile,31-day median and reduced-bill-supply inference remain unverified. Funding grade and unnamed-borrower limits survive. External correction only; no other desk’s canonical file edited.',
    [('2026-10-08; week/point October7','https://www.federalreserve.gov/releases/h41/20261008/','Table1 TGA weekly-average versus Wednesday columns'),('2026-10-13','https://x.com/LHMacro/status/2109991996752535793','Source chart label reviewed; historic percentile not reproduced')],
    [funding,'AGENTS/LIQUID/STATUS.md','BOARD/SIG-W-20261008-049-fed-discount-window-9-965B-wed-10-07-highest-since-jan-2024-amex-350M-occ-aml-penalty-no-asset-cap-car-mart-sixth-lender-bridge-to-10-15-LIQUID-OTTO.md'],
    'LIQUID: reconcile the average/point label in your existing funding surface. Preserve both source series and the45-day conditional rounding; no bill-supply or funding-state grade requested.',
    signal_type='correction', corrects='EXTERNAL: LHMacro October13 TGA chart Wednesday label; AGENTS/LIQUID/STATUS.md TGA measurement label',
    kill_strings=['TGA $880.3B [10/7]'], corrects_direction='HOLDS conditional45-day rounding; point-balance label changes, funding consequence ungraded')

add('chile-pension-rate-swaps-not-quantified-treasury-selling',
    'Chile pension losses concern rate derivatives; forced Treasury cash selling is not established',
    [24],'FUNDING_LIQUIDITY','FED_FRAMEWORK',['BOND','LIQUID'],['RED','PROME'],.65,
    ['Chile','AFP','interest-rate-swaps','Bloomberg'],
    'Bloomberg’s October13 original-reporting teaser describes derivative bets at seven Chilean AFP pension managers with$229bn assets. Its attached BloombergAI summary relays$1.4bn gain becoming$7.7bn September market-value loss and closing positions. The full article, underlying regulator table and referenced new rule were not retrieved. AI summary and publisher teaser are one provenance chain.\n\nCHANGE: a qualified rates-derivatives and position-unwind lead for existing bond/funding work. The teaser does not establish US Treasury cash liquidation, measured forced-sale volume, counterparty loss or a margin cascade. Do not translate marked derivative losses into cash outflows or import the US-LDI mechanism without evidence. Previous clean-auction findings retain their dated scope.',
    [('2026-10-13,18:15Z','https://news.bloomberglaw.com/securities-law/us-swaps-bets-backfire-wiping-out-billions-from-funds-in-chile','Original-reporting teaser; rest paywalled'),('Retrieved October13 EDT','https://www.siid.cl/fondos-de-pensiones','Regulator monitor identified, underlying current table unretrieved')],
    [funding,'AGENTS/BOND/STATUS.md'],
    'BOND/LIQUID: retain this qualified derivative-unwind lead in existing rates/funding context. Cash selling, margin/counterparty loss and rule details remain UNKNOWN; no new study or grade requested.')

add('yandex-payment-access-compensation-not-bank-run',
    'Yandex payment-access outage and reported temporary compensation do not establish a bank run',
    [35],'GEOPOL_ENERGY','HYDROCARBON_INFRA',['OSPREY'],['RED','PROME'],.75,
    ['Yandex','Yandex-Pay','Yandex-Bank','Vladimir'],
    'Yandex’s October11 statement confirms disrupted account access after infrastructure damage and says replicated records remain intact. Kommersant October13 reports staged recovery and20% annualized compensation for October11–17 only; the linked companyTelegram body was inaccessible. That reported temporary compensation is not a permanent no-strings deposit offer.\n\nCHANGE: payment-access/compensation context beyond existing signal013’s infrastructure outage. No deposit-outflow quantity, insolvency, top-ten retail-deposit rank or systemic domino effect was independently established. The headline’s bank-collapse mechanism remains INDETERMINATE, not disproved merely by missing evidence. OSPREY owns the existing Russian infrastructure consequence; no new Russian state-decision event or regional-US-bank inference.',
    [('2026-10-11','https://yandex.ru/company/news/11-10-2026-01','Company outage/replication statement'),('2026-10-13,04:29 publisher time','https://www.kommersant.ru/doc/9025087','Recovery/temporary-compensation relay; companyTelegram inaccessible')],
    [funding,'BOARD/SIG-W-20261012-013-yandex-vladimir-third-site-outage-http-bots-not-social-accounts.md'],
    'OSPREY: integrate the payment-access/temporary-compensation delta in existing Yandex infrastructure evidence. Preserve outflow and solvency UNKNOWN; no new banking study requested.')

add('jpm-q3-reported-managed-and-return-bases',
    'JPM Q3 issuer data separates reported/managed revenue and ROE/ROTCE; consensus miss is unverified',
    [42],'BANK_CRE','BANK_COLLATERAL',['BROCK','REGINALD'],['RED','PROME'],.95,
    ['JPMorgan','JPM'],
    'JPM’s October13 SECEx99.1 reports EPS$5.57 and adjusted$5.75; adjustment removes$498M after-tax securities losses. Reported revenue is$50.2B versus$50.9B managed. ROE is17%, while ROTCE is20% and adjusted21%. The post’s$5.90/$51.22B consensus and comparison basis were not issuer-primary authenticated.\n\nCHANGE: release-day inputs to the existing frozen BRK-31/Q3 read, with numerator/denominator discipline. Aggregate$2.7B credit provision/$539M reserve build is not attributable private-credit/NDFI loss or a regional funding event. Call/Q&A and final10-Q are outside this bounded release read. No issuer-wide miss, owner trigger, regional-cohort expansion or new credit grade is asserted.',
    [('2026-10-13','https://www.sec.gov/Archives/edgar/data/19617/000162828026065582/a3q26erfexhibit991narrative.htm','Issuer release and adjustment footnote2d')],
    [funding,q3,'AGENTS/REGINALD/reports/2026-10-09_Q3_earnings_read_plan.md'],
    'BROCK/REGINALD: use these matched-basis issuer inputs in the already authorized Q3 read. Keep PC attribution, consensus, call and10-Q gaps explicit; no new score or cohort requested.')

add('japan-cgpi-september-actual-prior-not-consensus',
    'Japan September producer inflation6.8% follows August7.6%; a consensus miss is not established',
    [70],'JAPAN_BOJ','ASIA_CHINA',['SAM'],['LIQUID','RED','PROME'],.95,
    ['Bank-of-Japan','Japan','CGPI'],
    'BOJ’s October13 SeptemberCGPI preliminary release, pp1/6, reports domestic producer prices+6.8%YoY and−0.3%MoM. August7.6% is a prior-month actual. The supplied images do not establish7.6% as a forecast; the alleged0.8pp consensus miss remains unverified.\n\nCHANGE: a new dated producer-price actual for the existing Japan inflation/carry context, not a BOJ decision or re-armed carry trigger. The separate BloombergJapan bookmark forecasts an October14 market rebound; it is a forward view, not a completed October14 outcome. Contract, currency and funding grades remain SAM’s.',
    [('2026-10-13; September preliminary','https://www.boj.or.jp/en/statistics/pi/cgpi_release/cgpi2609.pdf','BOJ pp1/6 current and prior actual')],
    [funding,'AGENTS/SAM/STATUS.md'],
    'SAM: integrate the dated CGPI actual with prior-month/forecast distinctions in existing inflation context. No consensus-miss or BOJ/carry-state grade requested.')

add('volsignals-year-end-put-model-and-conditional-vanna',
    'VolSignals reports growing December31 put hedges; positions and futures estimates are modeled',
    [10,11,12],'MARKET_VOL','POSITIONING_VALUATION',['HENRY'],['VIOLET','LIQUID','RED','PROME'],.65,
    ['VolSignals','VS3D','SPX','ES','December-31'],
    'Complete October12/13 VolSignals threads and images attribute all positions to VS3D. The publisher’s customerDecember31 total grows from32,742 October9 to51,224 October13, versus a13,476 October2 image header; prose calls October2 flat, a conditional baseline ambiguity if customer perimeters match. Around40K dealer shorts on three strikes are a different participant/perimeter and must not be forced to sum to51.2K.\n\nCHANGE: dated model-origin year-end hedge positioning, not verified dealer executions or a market-wide flow total. At7800, the publisher’s+3vol scenario is about2,500ES; given rounded strike positions/deltas, independent arithmetic gives2,466.688. About1,700 belongs to the+2vol aggregate or the7250 strike’s+3vol contribution, not all strikes at+3. Whole-book netting, execution and timing remain unverified. No inevitable sell wave, new vol fire or trade construction follows.',
    [('2026-10-12','https://x.com/VolSignals/status/2109741286093676792','Complete author thread and image read; proprietary model'),('2026-10-13','https://x.com/VolSignals/status/2110142224457494748','Complete author thread and images; position definitions and conditional scenarios')],
    [extra_funding,'AGENTS/HENRY/STATUS.md','AGENTS/VIOLET/CANARY_MAP.md'],
    'HENRY: integrate this dated model-origin positioning lead within existing dealer mechanics. Preserve participant/perimeter and conditional-versus-executed distinctions; no new flow grade or trade requested.')

add('maine-residential-heating-oil-observation-not-futures',
    'Maine residential heating oil$5.974/gal October5 supplies a dated household-cost observation',
    [56],'OIL_ENERGY','INFLATION_TRANSMISSION',['BRENT'],['CARL','RED','PROME'],.95,
    ['Maine','EIA','heating-oil'],
    'EIA’s W_EPD2F_PRS_SME_DPG primary history reports Maine residentialNo2heating oil$5.974/gal October5. This is a state retail/residential observation, not NYHarbor futures or wholesaleULSD. The post’s approximately80%YoY, September record and household-share comparisons were not independently reproduced on matched survey bases.\n\nCHANGE: a source-identified household heating-cost print for existing fuel pass-through work. If the post’s approximate$3.30 prior price is assumed, a275-gallon fill costs an additional$735.35 using5.974, not its$675 claim; the prior basis itself is unverified. Do not adopt a synthetic YoY statistic. No new diesel supply, futures settle, refinery margin or nationwide loss is established.',
    [('2026-10-05 observation; retrieved October13 EDT','https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?f=W&n=PET&s=W_EPD2F_PRS_SME_DPG','State residential price history, exact series')],
    ['AGENTS/BRENT/research/2026-10-13_energy-wait/REPORT.md'],
    'BRENT: retain the dated residential benchmark in existing fuel-cost transmission work. CARL information-only; comparative/statutory/futures implications remain ungraded.')

add('picklr-corporate-filing-lease-guarantor-unverified',
    'Picklr’s October9 corporate Chapter11 filing is confirmed; personal40-lease guarantee claim is not',
    [54],'BANK_CRE','BANK_COLLATERAL',['CREED'],['REGINALD','RED','PROME'],.85,
    ['Picklr','Picklr-Clubs','Northern-District-of-Texas'],
    'The retained case administrator identifies PicklrInc’s October9 Chapter11 case26-34687 and related PicklrClubs proceedings. The website’s related-case numbers/dates contain inconsistent cells, so adopt only the main debtor identity/date supported by its petition locator. The post attributes guarantees on40 facility leases to the founder/CEO personally; supplied media is a club photograph and does not establish that liability. Reports elsewhere distinguish corporate guarantees.\n\nCHANGE: a named tenant/corporate-restructuring lead for existing CRE market context. No specific property/CRE loan, rent shortfall, bank creditor, personal guarantee instrument or facility closure was authenticated here. This is not a named-property case feed and does not establish landlord loss or system-wide club shutdown. October13 repost is not the main petition date.',
    [('2026-10-09 petition','https://cases.omniagentsolutions.com/?clientId=3812','Retained case administrator main-debtor table; related-case cells conflict'),('2026-10-09','https://casedocs.omniagentsolutions.com/cmsvol2/pub_47622/d129edce-2d22-4c71-8561-5380cbe7b46e_1_Redacted.pdf','Main-debtor petition indexed filing stamp; full guarantee schedule not reviewed')],
    ['AGENTS/WALTER/research/2026-10-13_bookmark-routing/root-source-review.md'],
    'CREED: note the named corporate tenant-restructuring lead in existing CRE context, with property/guarantor/loss UNKNOWN. No named-property ledger addition, owner launch or new case study requested.')

add('korea-oct13-close-and-program-sell-sidecar',
    'Korea October13 closes sharply lower; five-minute sidecar suspended program sell orders',
    [57,62,64,66,69],'ASIA_CONTAGION','ASIA_CHINA',['VULCAN','HENRY'],['VIOLET','ZHAO','LIQUID','RED','PROME'],.85,
    ['KOSPI','KOSPI-200-futures','SK-hynix','KRX'],
    'Dated original wires report October13 KOSPI6035.35 close,−5.46%; AjuPress reports5911.11/−7.41% intraday. Yonhap reports SKhynix−10.09% close, versus the post’s−10.3% intraday relay. Newsis identifies09:47KST sidecar when KOSPI200 futures955.02/−5.08%; it suspended program sell orders for five minutes, not all exchange trading. KRX primary notice was not retrieved.\n\nCHANGE: a fresh dated realization of the already-owned Korea/semiconductor mechanism, not its first fire. Item64’s−7.05% is KOSPI200FUTURES; item62’s−15.13% is a multi-session spot move from October2 to an intraday endpoint. The40%June-peak claim and buyback-causality story remain unverified. HockTan/JPM commentary and19GW powered-shell forecast do not establish measured capex or power losses. Owner price/contract tests remain separate.',
    [('2026-10-13,16:36KST','https://en.yna.co.kr/view/AEN20261013007552320','Yonhap original close report'),('2026-10-13,18:03KST update','https://m.ajupress.com/amp/20261013171446394','AjuPress close/intraday report'),('2026-10-13,09:53KST','https://www.newsis.com/view/NISX20261013_0003823402','Indexed original morning sidecar report; direct opening timed out')],
    ['AGENTS/WALTER/research/2026-10-13_bookmark-routing/korea-verify.md','AGENTS/VIOLET/CANARY_MAP.md','AGENTS/VULCAN/workbook/VX.tsv'],
    'VULCAN/HENRY: integrate the dated selloff/mechanics with the existing semiconductor transmission frame. No first-fire, market-wide halt, buyback-causality or owner score asserted.',
    cluster_secondary=['AI_INFRA_CAPEX','POSITIONING_VALUATION'])

add('las-vegas-august-inventory-not-october-clearing-loss',
    'LasVegas listings report is an August stock observation; first above10,000 since2014, not since2009',
    [55],'BANK_CRE','BANK_COLLATERAL',['HOMER'],['REGINALD','CARL','RED','PROME'],.75,
    ['Las-Vegas','Brownell-Analytics','Las-Vegas-Realtors'],
    'The October5 ReviewJournal body, updatedOctober8, relays August inventory10,344 from BrownellAnalytics and10,304 all-property listings from LasVegasRealtors; these are not independently reconciled populations. It says first above10,000 since2014, with2009 an earlier historical comparison. Its named source says contracts/new escrows declined five months while median single-family price$485,000 was flat MoM/YoY.\n\nCHANGE: an older-observation/newly examined local supply-demand divergence lead, not current October stock, forced-sale clearing mark or bank recovery loss. The map itself cannot prove inventory count. Original vendor/realtor tables were not directly recovered. Keep this August relay separate from already-routed September Redfin figures and its source-column conflict; no universal price-collapse inference.',
    [('2026-10-05,updated October8; August observation','https://www.reviewjournal.com/business/housing/las-vegas-area-home-listings-top-10000-for-first-time-in-more-than-a-decade-3895884/','Full named data-provider relay; original tables unretrieved')],
    ['BOARD/SIG-W-20261012-035-September-Redfin-demand-Parcl-between-cuts-SHED-vintage-qualified.md','AGENTS/WALTER/research/2026-10-13_bookmark-routing/root-source-review.md'],
    'HOMER: retain the period/population-qualified local observation in existing housing context. No current October stock, named distress event or bank-loss grade requested.')

add('ual-fare-filed-increase-unverified-demand-counterlead',
    'United fare-increase relay is a qualified pricing counterlead; booked revenue and rival adoption unverified',
    [72],'OIL_ENERGY','CONSUMER_STAGFLATION',['BRENT'],['CARL','RED','PROME'],.50,
    ['United-Airlines','UAL','JPMorgan'],
    'FirstSquawk’s October12 lateUTC post attributes a$10 each-way increase across nearly all US domestic fare listings to JPMorgan and says rivals have not followed. The original analyst fare-file dataset/company confirmation was not recovered in the bounded search. Two million listings, if valid, are fare records, not two million tickets sold or a measured revenue increment.\n\nCHANGE: a qualified pricing-power counterlead within BRENT’s existing airline fuel-demand comparison. It does not establish industry-wide fares, realized yields, booking volumes or fuel pass-through. The post’s confidence-in-demand interpretation remains inference; a filed fare can be discounted or abandoned. No new airline study, current earnings grade or cruise-sector extrapolation follows.',
    [('2026-10-12,23:57:51Z','https://x.com/FirstSquawk/status/2109795714733854776','Attributed headline relay only; analyst/company confirmation unretrieved')],
    ['AGENTS/BRENT/demand_destruction/TRACKER.md','AGENTS/WALTER/research/2026-10-13_bookmark-routing/root-source-review.md'],
    'BRENT: retain the qualified pricing counterlead in existing demand/fuel context, with realized uptake UNKNOWN. No paid source acquisition or new study requested.')

add('anthropic-internal-coding-output-not-paid-inference-roi',
    'Anthropic reports rapid internal code growth and source-control efficiency; paid inference economics remain unmeasured',
    [31],'AI_CAPEX','AI_INFRA_CAPEX',['VULCAN'],['HENRY','RED','PROME'],.85,
    ['Anthropic','Scion','Antique'],
    'Anthropic’s complete October13 engineering post reports approximately2,500 merged code changes daily in May versus more than30,000 in September, a five-month internal source-control migration, and a25% CI CPU-capacity saving. It describes internal agent-heavy work and a bottleneck moving into development infrastructure. These are company-reported operating observations, not independently benchmarked economy-wide productivity.\n\nCHANGE: a concrete issuer-authored internal-use/efficiency counterweight to blanket adoption-collapse commentary. Code changes are not accepted economic deliverables, paid API traffic, revenue, profitable inference or GPU capex. The reported infrastructure savings concern the described source-control/CI system, not all AI training/inference electricity. No S1/S3/S5 score or public-company earnings effect established.',
    [('2026-10-13; May/September observations','https://www.anthropic.com/engineering/redesigning-source-control','Full company engineering post read; self-reported operating case')],
    ['AGENTS/WALTER/research/2026-10-13_bookmark-routing/root-source-review.md','AGENTS/VULCAN/STATUS.md'],
    'VULCAN: retain the issuer-reported internal-use/efficiency counterevidence in existing adoption economics, preserving the usage/output-versus-paid-return distinction. No new benchmark study or score requested.')

if __name__ == '__main__':
    existing = list((ROOT/'BOARD').glob('SIG-W-20261013-*.md'))
    high = max(int(p.name.split('-')[3]) for p in existing)
    if high != 6:
        raise SystemExit(f'REFUSE: expected October13 next ID007, found high{high}; recheck allocation')
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    stage = HERE/'.cache/packets'
    files = []
    for n,r in enumerate(PLAN,7):
        r['signal_id']=f'SIG-W-20261013-{n:03d}'
        r['board_path']=f'BOARD/{r["signal_id"]}-{r["slug"]}.md'
    paired=[PLAN[i] for i in [1,3,4]]
    for r in paired:
        r['title']='Paired energy/shipping risk: '+r['title']
        r['pair_note']='Pairs '+', '.join(x['signal_id'] for x in paired if x is not r)+' on the same shipping/energy-risk channel; separate event identities and unmeasured volumes.'
        r['refs'].extend(x['board_path'] for x in paired if x is not r)
    for n,r in enumerate(PLAN,7):
        sid=f'SIG-W-20261013-{n:03d}'
        path=f'BOARD/{sid}-{r["slug"]}.md'
        source_text='\n'.join(f'- [{date}: {basis}]({url})' for date,url,basis in r['sources'])
        body=f'# {r["title"]}\n\nSource lane: x-bookmark; snapshot items {r["items"]}.\n\n{r["body"]}\n\n## Source / read scope\n\n{source_text}\n\nRead-state: full bookmarked text and attached photos read; video thumbnails only. Retrieved/verified {stamp}. Source-specific body/primary access limits above remain.\n\n## Requested action\n\n{r["ask"]}\n\n## Existing assessments / verification\n\n'+'\n'.join('- '+p for p in r['refs'])+'\n'
        head={'signal_id':sid,'date':'2026-10-13','timestamp':stamp,'time_dispatched':stamp,
              'source':'WALTER','origin':f'Will-authorized x-bookmark snapshot, items{r["items"]}; dated sources below',
              'domain':r['domain'],'cluster':r['cluster'],'entities':r['entities'],'precedence':'PRIORITY',
              'action':r['action'],'to':r['action'],'info':r['info'],'confidence':r['confidence'],
              'confidence_language':'confirmed' if r['confidence']>=.9 else 'reports' if r['confidence']>=.75 else 'assessed' if r['confidence']>=.5 else 'unconfirmed',
              'signal_type':r.get('signal_type','research'),'resources':1,'safety_net':'clear','event_window':'closed',
              'word_count':len(body.split()),'dispatch_note':'Sourced bounded evidence; source-lane x-bookmark. Existing owner judgments/grades retained. No owner launch, new study, unattended run or trade. Fleet visibility UNKNOWN; written/published/consumed separate.'}
        if r.get('pair_note'):head['dispatch_note']+=' '+r['pair_note']
        for k in ['corrects','kill_strings','corrects_direction','cluster_secondary']:
            if k in r:head[k]=r[k]
        def scalar(v):
            if isinstance(v,str) and v and all(c.isalnum() or c in '_-.:TZ' for c in v):return v
            return json.dumps(v,ensure_ascii=False)
        text='---\n'+'\n'.join(k+': '+scalar(v) for k,v in head.items())+'\n---\n\n'+body
        p=stage/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
        files.append({'path':path,'sha256':hashlib.sha256(text.encode()).hexdigest()})
        for role,names in [('ACTION',r['action']),('INFO',r['info'])]:
            for name in names:
                if name in ['PROME','RED','TERRY'] or name=='CARL' and role=='INFO':continue
                target=f'AGENTS/{name}/inbox/WALTER/{sid}.md'
                hand=f'# {sid} — {r["title"]}\n\nBOARD: /{path}\nFrom: WALTER\nPriority: PRIORITY\nRole: {role}\nSignal date: 2026-10-13 EDT\nRetrieved: {stamp}\nSource lane: x-bookmark\n\n## Kernel\n\n{r["body"]}\n\n## Why you received this\n\n{name}: '+('Existing domain-owner evidence integration; no new research/grade commissioned.' if role=='ACTION' else 'Information only; no recipient-directed work requested.')+'\n\n## Requested action\n\n'+(r['ask'] if role=='ACTION' else 'Information only; no action requested.')+f'\n\n## Confidence and limits\n\n{r["confidence"]}. Source/measurement gaps above travel with this packet. Written pending commit/publication; actual consumption unknown.\n\n## Source\n\n{source_text}\n\n## Existing assessments\n\n'+'\n'.join('- '+p for p in r['refs'])+'\n'
                p=stage/target;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(hand)
                files.append({'path':target,'sha256':hashlib.sha256(hand.encode()).hexdigest()})
        r.update(signal_id=sid,board_path=path,timestamp=stamp)
    (HERE/'prepared-routes.json').write_text(json.dumps(PLAN,ensure_ascii=False,indent=2)+'\n')
    (HERE/'packet-manifest.json').write_text(json.dumps({'prepared_at':stamp,'files':files},indent=2)+'\n')
    print(f'Prepared {len(PLAN)} signals, {len(files)-len(PLAN)} create-only handoffs; not landed or marked.')
