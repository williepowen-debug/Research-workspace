"""Prepare reviewable packets locally; no writes outside WALTER."""
from pathlib import Path
import json
import datetime

OUT = Path(__file__).resolve().parent
STAMP = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
signals = []
def add(n, slug, title, domain, cluster, action, info, body, sources, ask, precedence='PRIORITY', confidence=.9, kind='research', extra=None):
    signals.append(dict(n=n, id=f'SIG-W-20261014-{n:03}', slug=slug, title=title, domain=domain, cluster=cluster, action=action, info=info, body=body, sources=sources, ask=ask, precedence=precedence, confidence=confidence, kind=kind, extra=extra or {}, stamp=STAMP))

add(1,'september-cpi-core-trigger-real-wage-squeeze','September CPI: registered core inflation line crossed; real hourly earnings fall',
    'MACRO_INFLATION','INFLATION_TRANSMISSION',['RED','CARL'],['HENRY','LIQUID','LABOR','BRENT','PROME'],
    'BLS October14 release: September CPI +0.6% m/m SA, +3.7% y/y NSA; gasoline +9.1% explains over half the headline monthly increase. Core +0.3% m/m, +2.6% y/y. Published July/August/September core 0.2/0.3/0.3 compounded exactly in Decimal gives 3.247216% annualized, 3.2% at the registered 1dp grid: RED-FT-08 >=3.0 is met, sustain1. RED’s October1 pre-data ruling explicitly selects TableA and calls a published0.3 FIRE; the older0.4 confirmation note must not veto that ruling. RED owns score execution; no changed owner weights claimed. Its oil-to-core composition test still needs November10. The trigger is not rare: RED measured8/19 months since2025. BLS real hourly earnings -0.5% m/m and -0.7% y/y; weekly -0.5%/-0.1%. These are different from the cumulative January2025 chart and are not a matched-worker wage panel.',
    [('BLS CPI, October14 08:30ET','https://www.bls.gov/news.release/cpi.nr0.htm'),('BLS real earnings, same release time','https://www.bls.gov/news.release/realer.nr0.htm')],
    'RED: integrate the qualified FT-08 fire against the existing pre-written decision tree and record owner execution; retain November composition resolver. CARL: integrate the official inflation/real-income release within existing tests.',
    'IMMEDIATE',.98,'threshold-crossed',{'falsification_trigger':'RED-FT-08','consumer_transmission':'pump_pass_through','consumer_lens':'mixed','cluster_secondary':'CONSUMER_STAGFLATION'})

add(2,'gfs-pride-sinking-gfs-giselle-strike','Flag-state authority confirms GFS Pride sinking; GFS Giselle reaches safe anchorage',
    'GEOPOL_ENERGY','IRAN_HORMUZ',['FALCON','BRENT'],['HAWK','SAM','RED','PROME'],
    'Singapore MPA October14 primary says GFS PRIDE was struck October13 Singapore Time by an unknown projectile, suffered damage/fire and subsequently sank;21 crew evacuated without injuries. GFS GISELLE was struck October14 Singapore Time, suffered hull damage and reached safe anchorage under own power;22 crew safe. MPA’s complete substantive indexed text was read; direct opening failed. No UTC event time, coordinates, cargo quantity or quantified barrel loss recovered. The unnamed Iranian mine/2,500-container claim is separate: mechanism and identity match are unverified. Do not add that claim as another hull or count. Reuters October14 reports changed Iranian tactics/election objective from two unnamed Iranian officials and small-boat spotters from an unnamed US official; this is attributed reporting, not authenticated intent or closure. AP executive-floor damage at Dhahran is anonymous-source specificity beyond yesterday’s administrative-fire packet, not measured oil-output loss. FALCON owns census/gate eligibility and marks; existing3-loss owner count is not silently replaced.',
    [('Singapore MPA October14','https://www.mpa.gov.sg/media-centre/details/two-singapore-registered-vessels-struck-in-strait-of-hormuz'),('Reuters October14 full-body syndication','https://www.internazionale.it/ultime-notizie-reuters/2026/10/14/iran-shifting-tactics-to-step-up-attacks-on-shipping-before-us-vote-officials-say')],
    'FALCON: reconcile exact vessel/event identities and existing loss census before any grade. BRENT: integrate the confirmed shipping loss and source limits in existing transport work; no barrel conversion or new study.',
    'IMMEDIATE',.9,'catalyst',{'narrative_channel':'tasnim','anchor_unverified_as_of':'2026-10-08','dispatch_scope':'narrative_channel tags only the separately attributed Iranian mine claim; MPA is independent flag-state evidence, not an Iranian endorsement'})

add(3,'iea-october-crude-product-recovery-split','October IEA report: crude recovery outpaces products; diesel balance remains constrained',
    'OIL_ENERGY','HYDROCARBON_INFRA',['BRENT'],['CARL','HENRY','LIQUID','HANS','OSPREY','FALCON','RED','PROME'],
    'IEA’s October14 public OMR estimates September Gulf crude exports13.9Mb/d, +4.4Mb/d m/m, over75% of prewar; product shipments1.9Mb/d versus4.7Mb/d prewar. September global diesel exports were700kb/d below a year earlier. The agency forecasts global oil demand -2.6Mb/d in2026 and constrained product balances into2027. Observed on-land inventories fell113Mb in September while oil on water rose103Mb: the net10Mb decline must not erase location/delivery differences. These are institutional estimates/forecasts, chiefly September and some older stock observations, not live cargo measurements or confirmed supplemental diesel deliveries. BRENT’s12:08EDT public-body assessment already holds the source; reuse it rather than repeating research. Its operating-refiner/expectations WAIT survives. IEA’s G7 acceleration language refers to the existing March collective action. No new release volume, current site outage, price target or held-VLO grade inferred.',
    [('IEA public OMR, October14; browser full public body read','https://www.iea.org/reports/oil-market-report-october-2026')],
    'BRENT: reuse the existing October14 owner assessment for any routing integration; retain quantities’ source dates, delivery uncertainty and existing holding gates.','PRIORITY',.93,
    extra={'cluster_secondary':'INFLATION_TRANSMISSION','consumer_transmission':'pump_pass_through','consumer_lens':'mixed'})

add(4,'bac-ms-q3-counterevidence','Big-bank Q3: BAC settlement charge lowers earnings while charge-offs improve; MS revenue grows',
    'BANK_CRE','BANK_COLLATERAL',['REGINALD'],['CARL','BROCK','LIQUID','RED','PROME'],
    'October14 issuer releases: Bank of America Q3 net income$6.933B/EPS$0.91 includes a$1.2B regulatory settlement charge in noninterest expense. Adjusted$8.1B/EPS$1.08 are non-GAAP, not reported GAAP profit. Net charge-offs$1.349B versus$1.412B Q2; annualized ratio0.44% versus0.47%. Card charge-off ratio3.22% versus3.55% Q2; early/late card delinquencies improved year-on-year for six consecutive quarters. Provision$1.269B and net reserve release$80M qualify the credit read. Morgan Stanley revenue$20.338B versus$18.224B a year earlier; net income$4.909B versus$4.610B, EPS$3.03. Large-bank figures counter a claim of broad borrower-loss acceleration; they do not clear regional CRE or named NDFI borrowers. A regulatory expense is not a credit loss. BAC full release and MS PDF read locally; no live share-price reaction or consensus grade inferred.',
    [('BAC Q3 issuer release, October14','https://investor.bankofamerica.com/regulatory-and-other-filings/select-sec-filings/content/0000070858-26-000481/bac09302026ex991.htm'),('MS Q3 issuer PDF, October14','https://www.morganstanley.com/about-us-ir/shareholder/3q2026.pdf')],
    'REGINALD: integrate issuer counterevidence within existing Q3 framework; keep settlement, provision and borrower losses separate.',
    'IMMEDIATE',.97,'catalyst',{'signal_role':'counter_evidence'})

add(5,'asml-q3-sales-guidance','ASML Q3 sales and full-year guidance supply AI-capex counterevidence',
    'AI_CAPEX','AI_INFRA_CAPEX',['VULCAN'],['VIOLET','HENRY','WATT','RED','PROME'],
    'ASML October14 issuer release reports Q3 sales€11.662B, gross margin57.5%, net income€5.0B; Q4 sales guidance€14.2–15.2B and FY2026€44–45B, gross margin around56%. Indexed issuer body was read; direct issuer opens/pull failed, so this is not a claimed successful full earnings-package read. Reported results and guidance are separate from committed future orders, delivered system capacity and customer returns. This supplies equipment-demand counterevidence to a broad AI-capex collapse; it does not refute financing, model-price or depreciation concerns. No stock-price reaction, USD conversion, bookings surprise, owner score or trade inferred.',
    [('ASML October14 issuer release, indexed primary body','https://www.investor.asml.com/news-releases/news-release-details/asml-reports-eu11.7-billion-total-net-sales-and-eu5.0-billion-net-income-q3-2026')],
    'VULCAN: integrate current issuer results/guidance with the existing capex tests; preserve package-access and demand-versus-return limits.',confidence=.85,extra={'signal_role':'counter_evidence'})

add(6,'redfin-september-seller-buyer-gap-miami','Redfin September estimate: seller surplus62.6%; Miami158.9%',
    'HOUSING','BANK_COLLATERAL',['HOMER','CORAL'],['CARL','REGINALD','HENRY','RED','PROME'],
    'Redfin October14 report estimates928,892 buyers and1,510,784 sellers in September, a62.6% seller surplus, record within its2013-onward history.41 of50 large metros are buyer markets; Miami158.9%, Nashville152.3%, Houston134.6%. Buyer numbers are modelled from search/matching, sellers active listings; both seasonally adjusted and revisable. Buyer-market definition requires >10% seller surplus. Current report’s August comparator56.9% differs from the earlier published58% that owners hold; preserve source vintage, do not silently restack it. This is a new September monthly delta, distinct from pending/closed sales and August LasVegas signals. It does not establish forced selling, price-collapse magnitude or bank recovery losses. Extended indexed primary body/methodology read; direct current release open failed.',
    [('Redfin October14 primary report','https://www.redfin.com/news/buyers-vs-sellers-september-2026/')],
    'HOMER: integrate the national monthly model on its stated basis. CORAL: integrate the Florida metro observations and reconcile the current report’s vintage with existing housing evidence.',confidence=.87,extra={'consumer_transmission':'wealth_effect','consumer_lens':'mixed'})

add(7,'netflix-global-job-cuts','Netflix reports about1,000 global job cuts, approximately6% of staff',
    'LABOR','CONSUMER_STAGFLATION',['LABOR'],['CARL','HENRY','RED','PROME'],
    'October14 Reuters memo reporting and TechCrunch direct company confirmation put Netflix’s cuts at roughly6% of global staff/about1,000 jobs. The original employee memo was not independently retrieved; evidence is dated reporter text, not an official WARN census. Do not convert the global count into U.S. layoffs, a net employment print, or a market-wide recession. It is a company event for the existing white-collar/labor supply work, not a new tracking commission; geography/timing of departures remains unresolved.',
    [('TechCrunch October14 direct company confirmation, indexed body','https://techcrunch.com/2026/10/14/netflix-to-lay-off-1000-staff-amid-intensifying-competition-for-user-attention/'),('Reuters October14 memo report','https://www.investing.com/news/stock-market-news/netflix-cuts-about-6-of-jobs-wsj-reports-4949456')],
    'LABOR: triage the reported global company event within existing labor work, retaining jurisdiction and memo-access limits.',confidence=.8)

add(8,'ssa-2027-cola-income-counterevidence','SSA announces3.6% benefit adjustment for2027',
    'MACRO_INFLATION','CONSUMER_STAGFLATION',['CARL'],['LABOR','HENRY','RED','PROME'],
    'SSA October14 announcement sets2027 Social Security COLA at3.6%; Social Security changes begin January2027 and SSI December31,2026. Its stated average retirement benefit rise is about$75/month. Nominal annual adjustment, not a current October cash transfer or proof of purchasing-power restoration. Beneficiary groups overlap and must not be summed as distinct people. This counterweights real-income squeeze for that cohort on a delayed calendar. Official indexed announcement/fact-sheet text read; direct current page access was limited.',
    [('SSA official October14 announcement','https://www.ssa.gov/blog/en/posts/2026-10-14.html')],
    'CARL: integrate the announced nominal income adjustment and effective dates in existing consumer income work.',confidence=.9,extra={'consumer_transmission':'policy_pass_through','consumer_lens':'tier_stratified'})

add(9,'ukraine-starshield-motion-restriction-report','Ukrainian adviser reports moving-terminal restriction disrupted drone missions',
    'GEOPOL_ENERGY','HYDROCARBON_INFRA',['OSPREY'],['HAWK','RED','PROME'],
    'Interfax October14 09:37 report quotes presidential adviser Serhiy Beskrestnov saying a100mph moving-terminal limit applied overnight to the StarShield military service without warning, disrupting several missions. Original adviser social post and SpaceX/provider notice were not recovered. This is an attributed operational constraint, not an authenticated universal Starlink shutdown, all-drone failure, political motive or observed refinery-output effect. Preserve military-service scope and reported speed units; no theater grade changed.',
    [('Interfax October14 indexed report','https://en.interfax.com.ua/news/general/1219719.html')],
    'OSPREY: triage the attributed operational report within existing theater work; preserve original/provider authentication and energy-impact unknowns.',confidence=.65)

add(10,'CORRECTION-ornn-anthropic-blended-price-method','Anthropic blended-price index falls; nominal rate cut and all-time claim remain unproved',
    'AI_CAPEX','AI_INFRA_CAPEX',['VULCAN'],['HENRY','RED','PROME'],
    'Ornn October13 Anthropic settle is$0.84 per million tokens, down29.4% over7days and47.2% over30days; tied low within the visible July14-onward window. The bookmarked chart was visually inspected. Primary methodology is internally inconsistent: docs describe activity/provider-weighted posted prices; FAQ describes executed realized prices with caching, routing and model mix. A constant-basket nominal cut, issuer margin compression and full-history all-time low are therefore unproved; history has an April4–June3 coverage break. This is a different index from the August19 LLMTK source; it does not silently replace that old basket. Correct the wrapper’s unrestricted all-time/nominal-price implication; route the bounded dated index observation.',
    [('Ornn index','https://data.ornn.com/markets/tokens/anthropic'),('Ornn method','https://data.ornn.com/docs/token-price-index'),('Ornn FAQ','https://data.ornn.com/faq')],
    'VULCAN: retain the bounded index observation and primary method disagreement in existing price/capex work; do not treat it as an authenticated nominal rate cut.',confidence=.72,kind='correction',extra={'corrects':'EXTERNAL: @zerohedge October14 Anthropic all-time-low price framing; constant-basket/nominal implication unverified','corrects_direction':'WEAKENS unrestricted historical and nominal-price inference'})

add(11,'cato-government-announced-equity-compilation','Cato compilation shows35 announced federal company equity positions sinceJune2025',
    'TARIFF_TRADE','FED_FRAMEWORK',['CARL'],['HAWK','VULCAN','MIDAS','ZHAO','RED','PROME'],
    'Cato’s October13 dashboard screenshot shows35 announced company equity positions over June2025–October2026:11 semiconductors,9 quantum,11 minerals, plus remaining sectors. Its definition includes announced/conditional interests and nonmonetary golden shares; these are not35 completed cash investments or deals since June2026. October2 explanatory text counted34 and included company-only Hertha announcement and the USSteel golden share. Current site narrative endsSeptember while screenshot extendsOctober: preserve source-version mismatch. This is Cato’s compilation, not an independently audited government dataset. Route as qualified policy/capital-allocation context, not a new ownership-program thesis or deployment.',
    [('Cato dashboard','https://www.cato.org/restoring-free-enterprise/government-ownership-dashboard'),('Cato October2 explanation','https://www.cato.org/blog/trump-administrations-equity-portfolio-reaches-34-deals')],
    'CARL: triage the qualified policy compilation in existing policy-transmission work; financing/semiconductor/minerals recipients receive context only.',confidence=.72)

add(12,'skew-third-qualifying-close-watch','Official SKEW October13 closes154.74; three of four qualifying sessions, no early fire',
    'MARKET_VOL','POSITIONING_VALUATION',['VIOLET'],['HENRY','LIQUID','RED','PROME'],
    'Cboe SKEW_History.csv retrieved October14 shows154.34[October9],155.06[October12],154.74[October13] after149.19[October8]. Under RED-FT-10 >=150 on4 consecutive published sessions, this is3/4, not a fire. October12 was an equity trading session; the bond holiday must not bridge it out of this series. October14’s final official observation is absent at the midday pull; if it qualifies, it can complete the run only after publication. This recovers the previously unavailableOctober13 bar and advances the existing watch, not a new trigger registration. Separate FRED mirrors October13: HY316bp, CCC1267bp, VIX cash15.27; HY remains below strict>320 and has no3-close run. VIX intraday16.23 is not its registered closing exit. No same-day official-close grade or consensus vol prediction.',
    [('Cboe official daily CSV','https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv')],
    'VIOLET: integrate the recovered third official qualifying bar and evaluate today’s publisher close under the existing row; no early fire.',confidence=.98,kind='pattern-match')

# No archive or recipient write occurs here. The source packets are reviewable.
draft = OUT / 'drafts'
draft.mkdir(exist_ok=True)
for s in signals:
    s['entities'] = {'1':['BLS','RED','CPI-U'], '2':['GFS-PRIDE','GFS-GISELLE','Singapore-MPA','Saudi-Aramco'], '3':['IEA','Gulf','Russia'], '4':['Bank-of-America','BAC','Morgan-Stanley','MS'], '5':['ASML'], '6':['Redfin','Miami','Nashville','Houston'], '7':['Netflix','NFLX'], '8':['Social-Security-Administration'], '9':['StarShield','SpaceX','Ukraine','Serhiy-Beskrestnov'], '10':['Ornn','Anthropic'], '11':['Cato-Institute','Hertha','US-Steel'], '12':['Cboe','SKEW','RED-FT-10']}[str(s['n'])]
    source_text='\n'.join(f'- [{name}]({url})' for name,url in s['sources'])
    body=f"# {s['title']}\n\n{s['body']}\n\n## Source / read scope\n\n{source_text}\n\nEvidence: AGENTS/WALTER/research/2026-10-14_morning-news/. Source date governs, not dispatch time.\n\n## Requested action\n\n{s['ask']}\n"
    s['word_count']=len(body.split())
    header=dict(signal_id=s['id'],date='2026-10-14',timestamp=s['stamp'],dispatched=s['stamp'],source='WALTER',origin=[x[0] for x in s['sources']],domain=s['domain'],cluster=s['cluster'],entities=s['entities'],precedence=s['precedence'],action=s['action'],to=s['action'],info=s['info'],confidence=s['confidence'],confidence_language='confirmed' if s['confidence']>=.9 else 'reports',resources=1,signal_type=s['kind'],safety_net='clear',event_window='closed',word_count=s['word_count'],dispatch_note='Source-qualified morning catch-up; owner state/grades unchanged except WALTER-qualified FT08 fire history. Actual owner integration UNKNOWN. Native fleet visibility UNKNOWN; no DARK inference or owner spawn. Three bounded read-only RULE9 helpers explicitly complete.')
    header.update(s['extra'])
    # Push tearline is separately counted; source/recipient sections are retained.
    s['push_word_count']=len(s['body'].split())
    if s['precedence']=='IMMEDIATE':
        assert s['push_word_count'] <=200, (s['id'],s['push_word_count'])
        header['word_count']=s['push_word_count']
    text='---\n'+'\n'.join(f'{k}: {json.dumps(v,ensure_ascii=False)}' for k,v in header.items())+'\n---\n\n'+body
    s['draft_path']=str(draft / f"{s['id']}-{s['slug']}.md")
    Path(s['draft_path']).write_text(text)
(OUT/'dispatch-plan.json').write_text(json.dumps(signals,indent=2,ensure_ascii=False))
print(f'Prepared {len(signals)} packets at {draft}; IMMEDIATE tearline counts:',[(s['id'],s['push_word_count']) for s in signals if s['precedence']=='IMMEDIATE'])
