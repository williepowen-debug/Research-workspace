import json
RO = "WALTER evening boot step 7h, Will's X bookmarks (71 fetched 2026-11-27T22:02:22Z), Will 17:05 ET 'lets do the full triage now'"
cards = {}
cards["004"] = dict(
 id="SIG-W-20261127-004",
 slug="Iran-blockade-CENTCOM-disabled-Palau-flagged-Pacific-Archer-Nov-26-after-Bandar-Abbas-departure-first-since-Tehran-vowed-to-break-blockade-Ghazal-Hormuz-hit-is-July-Red-Sea-recirculation-Zero-Hour-and-Mokhber-unverified",
 safety_net="clear", event_window="open", route_origin=RO,
 origin=["X bookmarks @HormuzReport, @UK_REPT, @HormuzLetter, @DeItaone, @BullTheoryio, @OilandEnergy, @CRUDEOIL231 (11/27)", "WebSearch 2026-11-27 22:0x to 22:10Z (CENTCOM release 4660484 via search; Iran International)", "Rule 9 helper verify (search summaries, houseofsaud 11/27 read)"],
 signal_type="context",
 title="Iran blockade, Nov 26 to 27: CENTCOM says a US aircraft disabled the Palau-flagged bulk carrier Pacific Archer in the Gulf of Oman on Nov 26 after it left Bandar Abbas (Iran International: first ship disabled since Tehran vowed to break the blockade); the 'Saudi supertanker Ghazal hit in Hormuz' post matches the July 28 Red Sea NCC Ghazal event, no Nov 27 hit found; IRGC 'Zero Hour', the Mokhber quote, a 'fourth carrier' and a Ras Tanura loading halt are unverified",
 body="""# Iran and Gulf items from Will's bookmarks, Nov 26 to 27

| # | Item | Read | Verdict | Owner |
|---|---|---|---|---|
| 1 | **CENTCOM: a US aircraft fired precision munitions at the stern of the Palau-flagged bulk carrier M/V Pacific Archer in the Gulf of Oman on Nov 26** after it left Bandar Abbas and ignored warnings; crew unharmed; CENTCOM totals 158 redirected, 6 disabled. Iran International: first ship disabled since Tehran vowed to break the blockade (prior: Huda, Nov 7). NSJ: Singapore-bound; Iran weighing a tanker convoy | CENTCOM release 4660484 and CENTCOM X post via search summary (a helper's fetch of centcom.mil returned 403, not retried) | CONFIRMED (event Nov 26, announced Nov 27) | FALCON |
| 2 | '@UK_REPT 17:51Z: missile strike on the Saudi-owned supertanker Ghazal amid explosions in Hormuz' | searches: NCC Ghazal (Bahri chemical/product tanker, not a supertanker) was a Houthi claim in the Red Sea on Jul 28, 2026. Nearest Nov 27 event: IRGC says a tanker hit a mine north of Ghavam Island Nov 27 morning, unnamed, unconfirmed by UKMTO, owners or CENTCOM (houseofsaud citing Anadolu, Fars) | **Name and date trap (guards ADD#26 Encelia class, ADD#13 name collision): carry as unconfirmed; not a new hull** | FALCON |
| 3 | IRGC 'Zero Hour' to break the blockade, 'irreversible mission', missile drills toward Hormuz (@HormuzReport citing IRGC statements and Ajel) | not found by search | UNVERIFIED claim | FALCON |
| 4 | Mokhber: 'neither will Hormuz be reopened, nor will we allow the blockade to remain' (@DeItaone 16:48Z) | exact quote not found; consistent in substance with a November Foreign Ministry line (blockade first) | UNVERIFIED quote | FALCON, HAWK |
| 5 | 'Netanyahu plans to destroy water, electricity and energy infrastructure for Iran's 90 million people if unable to defeat them, per Ynet' | no Ynet piece with that wording found; Ynet has reported Israel pressing the US to hit Iranian energy sites (anchor: Kan 10/29 single report) | UNVERIFIED wording | FALCON, HAWK |
| 6 | 'Trump sends a fourth aircraft carrier' (@OilandEnergy, question post) | USNI, ITV 11/16: Theodore Roosevelt arrived as the third carrier (with George H.W. Bush and George Washington), expected to relieve Washington; anchor 11/23 says carriers three to two | **Unsupported**; no fourth-carrier report found | FALCON |
| 7 | Ras Tanura / Ju'aymah: one account's satellite image stamped 2026/11/27 07:00 UTC shows the Ju'aymah SPMs empty, 'loadings still not resumed' (image opened) | no Aramco statement; Houthi Ras Tanura claims 10/27 to 10/30 unconfirmed; Aramco reported selling late-November fuel oil from Ras Tanura (Baird) | Single-account image; **guard: Ras Tanura = March 2, 2026 merge hazard; empty berths are not a halt** | FALCON, BRENT |

- **Guards read this session (IRAN_WAR_GUARDS):** 'INTERCEPTED' to 'STRUCK' retelling, 7/23 Ras Tanura date anchors, ADD#13 name collision, ADD#26 event-date discriminators. Item 1 is a US enforcement strike on a vessel, not on Iranian territory; FAL-07 is already RESOLVED (FALCON 11/04). A mine claim does not fire GATE 2 on relay.
- **So what:** blockade enforcement resumed after an 18-day gap and Iran's rhetoric is escalating, but no new hull hit, Gulf-ally production loss or loading outage is confirmed in this batch. OPEC+ meets Sun 11/29. Next full Iran sweep about 11/30.""",
 source="CENTCOM release 4660484 'U.S. Forces Disable Commercial Vessel During Blockade Enforcement Against Iran' and CENTCOM X 2126359352869065046 via search summaries 2026-11-27; Iran International 202611274132; NSJ; houseofsaud.com 11/27 (read by helper); USNI, ITV 2026-11-16; Investing.com 11/27; X bookmark texts and image",
 action=["FALCON"], info=["BRENT","HAWK","SAM","HENRY","RED","PROME"],
 precedence="PRIORITY", confidence=0.7,
 confidence_language="reports: item 1 CENTCOM via search summaries; items 2 to 7 unverified or recirculated",
 cluster="IRAN_HORMUZ", domain="GEOPOL_ENERGY",
 entities=["CENTCOM","Pacific Archer","Bandar Abbas","Gulf of Oman","IRGC","Mokhber","NCC Ghazal","Ghavam Island","Netanyahu","Theodore Roosevelt","Ras Tanura","Ju'aymah"],
 dispatch_note="PRIORITY: confirmed blockade enforcement strike plus a set of escalation claims, none of which fires a registered row. ACTION FALCON (grades all). Iran pre-dispatch guard read this session. RED, PROME by BOARD diff.",
 route_summary="Iran: CENTCOM disabled Pacific Archer 11/26; Ghazal is July recirculation")
cards["005"] = dict(
 id="SIG-W-20261127-005",
 slug="Oil-Nov-27-WTI-January-settled-83.08-down-0.72pct-Brent-Jan-95.44-secondary-unconfirmed-claims-no-Brent-grade-January-cargoes-SOMO-November-loadings-delayed-China-INE-bids-Kemp-crack-figure-unverified-Europe-diesel-item-is-2024",
 safety_net="clear", event_window="open", route_origin=RO,
 origin=["X bookmarks @FirstSquawk, @chigrl, @MarhelmData, @DarioCpx, @JKempEnergy, @business (11/25 to 11/27)", "Rule 9 helper verify (search summaries; EIA WPSR 11/18)"],
 signal_type="context",
 title="Oil, Nov 27: WTI January settled $83.08, down $0.60 (0.72%), Brent January $95.44, down 1.2% (one secondary report; settles not read at exchange); unconfirmed: no North Sea Brent-grade cargoes in January for low stock (Bloomberg notice via X), Iraq SOMO November loadings delayed 20 to 30 million barrels, China bidding on Shanghai INE crude; Kemp's 3-2-1 under $36 and 17.6 mb/d runs not matched; Bloomberg Europe diesel 'below Covid' item is August 2024",
 body="""# Oil items from Will's bookmarks, Nov 25 to 27

| # | Item | Read | Verdict | Owner |
|---|---|---|---|---|
| 1 | WTI January (CLF27) settled $83.08, -$0.60, -0.72% on Nov 27 (half day); Brent January $95.44, -1.2%; week: Brent about +3.1%, WTI about -1.1% | one secondary report via search summary; not read at CME or ICE. ⚠️ Brent card 20261126-008 had BZF27 settle 96.57 on 11/26 | CONFIRMED secondary | BRENT |
| 2 | **'No North Sea Brent-grade cargoes in January due to insufficient stock', per a notice seen by Bloomberg** (@chigrl 13:35Z) | no Bloomberg or Reuters item found by search; only a January 2026 Platts item (different year) | UNVERIFIED; decision-relevant to the Dated Brent basket if true | BRENT |
| 3 | Iraq SOMO pushed back November loadings, 20 to 30 million barrels delayed, some to load in the first 10 days of December (@MarhelmData) | nothing current found | UNVERIFIED | BRENT, FALCON |
| 4 | China bidding heavily on Shanghai INE crude futures 11/26 to 11/27; 'China to lead a global stockpiling drive over 1 to 2 years' (@DarioCpx, @MarhelmData; charts opened) | no source found for either; card 20261117-006 item 8 carried 'China resumes crude stockpiling' (investingLive 11/16) | UNVERIFIED; repeat theme | BRENT, ZHAO |
| 5 | Kemp: US 3-2-1 crack under $36 from a $72 late-September peak; refiners running almost 17.6 mb/d (charts opened) | Reuters/Kemp record 3-2-1 was $69.66 in July; no $72 or $36 found; EIA crude runs 16.9 mb/d w/e 11/13 (95.7%), w/e 11/20 not read; Kemp's figure may be gross inputs | UNMATCHED figures; WTI-basis crack, not Boundary #8 (Brent 3:2:1, NAMED January legs) | BRENT |
| 6 | Bloomberg 'Europe's diesel demand on course to be lower this year than during Covid' (tweet dated 11/25 with a 2026-11-25 URL) | helper found only the August 27, 2024 version (IEA OECD Europe); 2026 article page not read | Probable recirculation; open the 2026 URL before citing | BRENT, HANS |

- **So what:** only item 1 is a market fact, and it is secondary. Item 2 would matter (Dated Brent basket supply) and is unconfirmed: BRENT may want it checked at Bloomberg or a loading programme. Boundary rows #6 and #8 not graded here (named contracts not pulled).""",
 source="search summaries 2026-11-27 (oil settle report, Platts 2026-01, CME PVM note 11/10); EIA WPSR 2026-11-18 archive page; BNN Bloomberg 2024-08-27; X bookmark texts and images",
 action=["BRENT"], info=["FALCON","HAWK","ZHAO","HANS","CARL","HENRY","RED","PROME"],
 precedence="ROUTINE", confidence=0.55,
 confidence_language="unconfirmed: one secondary settle report; claims 2 to 4 not found at any primary",
 cluster="HYDROCARBON_INFRA", domain="OIL_ENERGY",
 entities=["WTI","CLF27","Brent","BZF27","SOMO","Iraq","INE","China","Kemp","EIA","Europe diesel"],
 dispatch_note="ROUTINE: market and supply claims, none confirmed beyond a secondary settle. ACTION BRENT. RED, PROME by BOARD diff.",
 route_summary="Oil: WTI Jan 83.08; unverified Brent-grade January and SOMO delay claims")
cards["006"] = dict(
 id="SIG-W-20261127-006",
 slug="Cyber-Nov-26-to-27-Reuters-hackers-breached-US-Air-Force-Cloud-One-SAP-confirms-suspicious-activity-in-its-GitHub-development-environment-UK-DWP-serious-cyber-incident-Lloyds-BoS-Halifax-app-outage-on-payday-Allstate-outage-day-5",
 safety_net="clear", event_window="open", route_origin=RO,
 origin=["X bookmarks @unusual_whales, @MTSlive, @HormuzLetter, @Polymarket, @BBCBreaking, @TheInsiderPaper, @Kalshi, @BillEvanina (11/27)", "Rule 9 helper verify (search summaries; Cyprus Mail read)"],
 signal_type="context",
 title="Cyber and outages, Nov 23 to 27: Reuters exclusive, hackers breached the US Air Force's Cloud One platform (found in the past month, Air Force declines comment; 'control plane' and NORAD details not corroborated); SAP confirms 'suspicious activity' in its GitHub development environment (Spiegel; AI use and code alteration unconfirmed; no customer data access reported); UK DWP takes public services offline after a 'serious cyber incident' (payments unaffected); Lloyds, Bank of Scotland, Halifax apps down on payday (cause not stated); Allstate outage day 5",
 body="""# Cyber and outage items from Will's bookmarks

| # | Victim | Claim / event | Read | Verdict | Channel |
|---|---|---|---|---|---|
| 1 | US Air Force Cloud One (Leidos-run) | Reuters exclusive Nov 27 (3 people): intrusion found 'in the past month or so' during an upgrade; app updates blocked, some admin rights revoked, migration paused; actor, scope, data theft unknown. NBC: a US official confirmed. Air Force: no comment on specific networks | Reuters via US News, CNBC, Military Times summaries | CONFIRMED core; 'control plane', NORAD radar, munitions tracking at 200+ sites NOT corroborated | government IT; pay apps reportedly hosted, no payment impact reported |
| 2 | SAP | Spiegel Nov 26 to 27: suspected attack on SAP's GitHub development environment, employee auth tokens stolen, code reportedly altered and copied; SAP confirms 'suspicious activity' and countermeasures ('Project Granite'), no indication of customer business-data access | ComputerBase, Handelsblatt, All About Security summaries; Spiegel not read | CORRECTED-FRAMING: a development-environment compromise; 'AI altered SAP's source code' unconfirmed | software supply chain (ERP used by banks, insurers) |
| 3 | UK Department for Work and Pensions | Pat McFadden: 'a serious cyber incident'; nearly all public-facing services down (Universal Credit portals, Pension Credit, Tell Us Once); NCSC investigating unusual activity from Thu Nov 26; benefit and pension payments unaffected | ITV, Yahoo summaries; BBC page not found | CONFIRMED; nature unconfirmed | government payment system touched, payments unaffected |
| 4 | Lloyds, Bank of Scotland, Halifax (Lloyds Banking Group) | apps and online banking failed from about 10:00 UTC Fri Nov 27 (payday), over 4,000 Downdetector reports; Lloyds: 'aware some customers are having difficulty accessing the app'; no cause or ETA by about 13:00. City AM alone links it to DWP | The Register summary | CONFIRMED outage; cyber NOT established; 'major UK banks' (Kalshi) beyond LBG not found | UK bank |
| 5 | Allstate | outage since Mon Nov 23 (login, policy, bill pay, claims submission, app roadside); claims by phone, no lapse or late fees; cause not stated | TechCrunch 11/25, CBS summaries | CORRECTED-FRAMING: day 5, still ongoing | US insurer |
| 6 | 'Past two weeks' outage list (@BillEvanina) | JPMorgan Chase and Wells Fargo outages were Nov 16 (with BofA, U.S. Bank, Capital One, Zelle); a source told NBC JPM's was a software bug, 'no evidence cyber'; FAA 11/14 router, Apple 11/17 'not a cyberattack', NSA 11/17 | Fortune, CBS, Cyprus Mail (read) | Mixed; officials see no coordinated attack | banks |

- **Per the v0.49 bank-supplier rule:** none of these is a named US core-banking or payment vendor; item 4 is a single UK banking group, one day. PRIORITY, not IMMEDIATE. Never list affected credit unions by name.
- **So what:** a dense cluster with no stated common cause: US banks Nov 16, Allstate from Nov 23, DWP Nov 26, Lloyds Nov 27, plus two confirmed intrusions (Air Force, SAP dev environment). The SAP item is the supply-chain one to watch for customer impact.""",
 source="Reuters exclusive 2026-11-27 via US News, CNBC, Military Times; ComputerBase, Handelsblatt, All About Security 11/26 to 27; ITV 2026-11-27; The Register 2026-11-27; TechCrunch 2026-11-25, CBS; Fortune 2026-11-16; Cyprus Mail 2026-11-18 (read); all others search summaries",
 action=["CYPHER"], info=["GIBBS","REGINALD","SHADE","HANS","LIQUID","VULCAN","RED","PROME"],
 precedence="PRIORITY", confidence=0.75,
 confidence_language="reports: tier-1 press via search summaries; no victim's own page read",
 cluster="CYBER", domain="CYBER",
 entities=["US Air Force","Cloud One","Leidos","SAP","GitHub","DWP","NCSC","Lloyds Banking Group","Bank of Scotland","Halifax","Allstate","JPMorgan Chase","Wells Fargo"],
 dispatch_note="PRIORITY under CYBER v0.49 bank-class minimum (Lloyds, Allstate). ACTION CYPHER. Info GIBBS (US large banks), REGINALD, SHADE (Allstate), HANS (UK), LIQUID (payments), VULCAN (SAP). RED, PROME by BOARD diff.",
 route_summary="Cyber: USAF Cloud One breach, SAP dev env, DWP, Lloyds outage, Allstate day 5")
cards["007"] = dict(
 id="SIG-W-20261127-007",
 slug="US-data-catch-up-Census-October-advance-goods-deficit-149.5B-from-135.1B-imports-365.3B-wholesale-inventories-up-0.9pct-Dallas-Fed-trimmed-mean-PCE-October-2.8-1-month-2.4-12-month-St-Louis-Fed-8th-District-banks-loan-demand-net-minus-30",
 safety_net="clear", event_window="open", route_origin=RO,
 origin=["census.gov advance_report2610.pdf (read by helper)", "dallasfed.org/research/pce (read by helper)", "X bookmarks @DeItaone, @PeterSchiff, @FirstSquawk, @KobeissiLetter (image opened), @spectatorindex, @unusual_whales, @Polymarket", "TIME 2026-11-27 (fetched by helper)", "INSEE IR263 (read by helper)"],
 signal_type="indicator",
 title="US data catch-up (missed by the 11/27 day calendar pass): Census October advance goods deficit $149.5B, widest since March 2025 per relay (Sept $135.1B; exports $215.8B, imports $365.3B, SA; released Fri 11/27 08:30 ET; wholesale inventories +0.9%, retail +0.8%); Dallas Fed trimmed mean PCE October 2.8% 1-month annualized, 2.4% 6-month and 12-month (11/25); St. Louis Fed 8th District bankers (11/17 edition): loan demand net -30% vs +11%, delinquency net +28%; France Q3 is -0.1% (flash), not -0.2% recession",
 body="""# US and other data from Will's bookmarks (calendar catch-up)

| # | Item | Read | Verdict | Owner |
|---|---|---|---|---|
| 1 | **Census Advance Economic Indicators, October 2026 (CB26-195), Fri 11/27 08:30 ET:** goods deficit **$149.5B**, +$14.4B from $135.1B; exports $215.8B (+$6.7B), imports $365.3B (+$21.1B); SA, not price-adjusted. Wholesale inventories $1,023.4B, +0.9% m/m (+8.5% y/y); retail $893.2B, +0.8% (+5.1% y/y); Sept revised retail to +0.7%, wholesale to +0.8%. Next 12/28. Relay (Schiff): largest October deficit on record, third-largest month after Jan and Mar 2025 | issuer PDF read (helper) | CONFIRMED | CARL (TARIFF_TRADE), ISHM |
| 2 | **Dallas Fed trimmed mean PCE, October:** 1-month annualized 2.8%, 6-month 2.4%, 12-month 2.4%; updated 11/25 (with BEA's October PCE), next 12/23 | dallasfed.org read (helper); the 'prior 3.0%' not verified | CONFIRMED | CARL |
| 3 | **St. Louis Fed Economic Conditions Survey (8th District), banking, 11/17 edition** (Kobeissi chart, opened): net % higher minus lower, current quarter: loan demand **-30%** (previous quarter +11%, expected next quarter -7%); delinquency **+28%** (prior +25%); credit standards +13% tighter (prior +6%) | chart attributed to St. Louis Fed; issuer figures sit in an xlsx not read | REPORTED; 11/17 edition, 10 days old | REGINALD, CARL |
| 4 | Trump (Truth Social 11/26, TIME 11/27): calls BEA's Q3 GDP revision to 4.3% annualized from 3.4% a 'massive, and purposeful, error' and 'fake Economic Numbers, just prior to the Election' | TIME page (helper) | CONFIRMED; the post is about the 11/25 second estimate and the Nov 3 midterms already held; no evidence offered | HENRY, CARL |
| 5 | 'France's economy shrinks 0.2% in Q3; plunges into recession' (@spectatorindex, @Polymarket) | INSEE first estimate (10/30): Q3 **-0.1%**, Q2 0.0%; Q1 was -0.2%; the 11/27 detailed estimate not retrieved | **CORRECTED-FRAMING: -0.2% and 'recession' unsupported by the flash**; card 20261127-002 carried France by title | HANS |
| 6 | BLS state unemployment, October (released 11/20): CT 5.1%, CA 5.0%, MI 5.0%; Florida 4.3% from 4.4% | BLS release summary | DUP for Florida (card 20261120-003, LABOR graded); other states not new | LABOR, CORAL |
| 7 | 'Banks to pay $400M in muni bond price-fixing trial' (@FirstSquawk 16:11Z) | search summaries: banks NEAR a settlement of more than $400M in the Philadelphia-led federal class action on variable-rate demand bond remarketing (JPMorgan, Morgan Stanley, Goldman named); no signed settlement found | CORRECTED-FRAMING: reported near-settlement | CARL (muni) |
| 8 | SOFR 5 bp above IORB (@gamesblazer06) | FRED: SOFR 3.95 [11/25], IORB 3.90 | CONFIRMED; REG-T-08 (>15 bp) not met | LIQUID |

- **Calendar:** items 1 and 2 were not in HENRY's ECON_CALENDAR or PROME's DOCKET; WALTER's 11/27 day pass recorded 'US none scheduled'. Logged as a miss in research/2026-11-27_evening-boot/CALENDAR-RECONCILIATION.tsv.
- **So what:** the import surge plus inventory build reads as front-running or restocking ahead of tariff changes (ISHM's real-demand-or-borrowed question); it subtracts from Q4 GDP tracking. The 8th District loan-demand swing is the sharpest in the chart and supports a credit-demand slowdown read, on one regional survey.""",
 source="census.gov/econ/indicators/2026/advance_report2610.pdf; dallasfed.org/research/pce; stlouisfed.org economic-conditions-survey-results (page, no figures) and Kobeissi chart; time.com 2026-11-27; insee.fr IR263; bls.gov laus.nr0; FRED SOFR, IORB 2026-11-27T21:58:41Z; search summaries for item 7",
 action=["CARL","ISHM","REGINALD"], info=["HENRY","LIQUID","LABOR","HANS","CORAL","RED","PROME"],
 precedence="PRIORITY", confidence=0.8,
 confidence_language="confirmed: items 1, 2 at the issuer; 3 a chart of the issuer's survey; 5 and 7 corrected framing",
 cluster="INFLATION_TRANSMISSION", domain="TARIFF_TRADE",
 entities=["Census Bureau","goods trade deficit","wholesale inventories","Dallas Fed","trimmed mean PCE","St. Louis Fed","Economic Conditions Survey","BEA","Q3 GDP","INSEE","France","SOFR","IORB","muni VRDO"],
 dispatch_note="PRIORITY rather than the data-day IMMEDIATE default: a late catch-up of a release with no registered trigger, read at the issuer; owners next read Mon 11/30. ACTION CARL (trade, inflation), ISHM (inventories, imports), REGINALD (8th District lending). RED, PROME by BOARD diff.",
 route_summary="Data catch-up: Oct goods deficit 149.5B; trimmed mean 2.8; 8th District loan demand -30")
cards["008"] = dict(
 id="SIG-W-20261127-008",
 slug="AI-credit-Semafor-Nov-26-Citi-and-JPMorgan-marketing-AI-loan-portfolios-some-via-synthetic-risk-transfer-SoftBank-5Y-CDS-542-on-a-Bloomberg-chart-retail-bond-spread-229-post-issuance-high-CoreWeave-DDTL-guarantee-claim-Nvidia-China-chips-story-not-matched",
 safety_net="clear", event_window="open", route_origin=RO,
 origin=["X bookmarks @BullTheoryio, @PolymarketMoney (Semafor image opened), @zerohedge (CDS chart opened), @puckrin (Bloomberg chart opened), @rdd147, @GlobalMktObserv, @DeItaone, @Polymarket, @LiveSquawk, @NoLimitGains, @zerohedge, @rickjeff78, @michaeljburry", "Rule 9 helper verify (search summaries)"],
 signal_type="context",
 title="AI credit, Nov 26 to 27: Semafor exclusive (11/26) says Citi and JPMorgan are marketing AI loan portfolios, some via synthetic risk transfer (no amounts); SoftBank 5Y CDS 542 bp on a Bloomberg screen chart (zerohedge; last verified print 466 bp on 11/6) and its retail bond spread at a post-issuance high near 229 bp (Bloomberg chart); CoreWeave 'senior bonds worthless' is one anonymous account (DDTL 5.0 parent guarantee per a filing summary); the 'Blackwell rack found as loan collateral' story is not matched",
 body="""# AI-credit items from Will's bookmarks

| # | Item | Read | Verdict | Owner |
|---|---|---|---|---|
| 1 | **Semafor exclusive, Nov 26 (Ellen DiMauro): 'Banks look to dump AI debt'**: Citi and JPMorgan marketing portfolios of AI loans, to manage risk or make room for more; some deals keep loans on balance sheet and pass loss risk to investors (synthetic risk transfer) | article screenshot opened; Semafor page via search summary; no amounts | CONFIRMED (lede); a recurring theme (FT, May 2026) | BROCK, GIBBS |
| 2 | **SoftBank 5Y CDS (JPY senior): 542.255 'last price'** on a Bloomberg screen chart posted by zerohedge 11/27 14:11Z ('+50 bp in 2 weeks, 25 from an 18-year high'); puckrin: 534.6 bp, shares about -68% from the June peak | charts opened; Bloomberg not read; last level found by search 466 bp (11/6, 4-year high) | REPORTED (chart only); the 18-year-high distance not checked | SAM, BROCK |
| 3 | SoftBank retail bond (¥1 trillion issue) spread about 229 bp, post-issuance high, 11/26 | Bloomberg chart via puckrin, opened | REPORTED (chart) | SAM |
| 4 | '@rdd147, being told: CoreWeave senior unsecured bonds considered worthless in bankruptcy because six of seven DDTL facilities are guaranteed by the parent' | filing summary: DDTL 5.0 ($3.1B) 'unconditionally guaranteed by the Parent' (May 2026 8-K); a blog says DDTL 1.0 to 5.0 parent-guaranteed; Q3 10-Q debt note not read | Structure partly supported; 'worthless' is an anonymous opinion | BROCK, VULCAN |
| 5 | CoreWeave shares -2.3% early 11/27 (@DeItaone); Nvidia's $2B January 2026 investment and residual-capacity purchase commitment through April 2032 (@GlobalMktObserv 'circular financing' framing) | Nvidia release Jan 26 via summary; capacity agreement size not found | CONFIRMED facts, framing is the poster's | VULCAN |
| 6 | 'Bloomberg: Nvidia Blackwell chips found at a Shanghai site tied to Alice Huang / Megaspeed; a Chinese firm listed a Blackwell rack as loan collateral, serial traced to a Gigabyte rack' | no 11/27 Bloomberg piece found; an earlier Bloomberg-sourced story has a Shanghai Longteng unit pledging 193 servers (Super Micro H100/H200, Gigabyte) as collateral, about ¥485M; Megaspeed denies wrongdoing; Commerce and DOJ investigating (card 20261117-006 carried Megaspeed) | UNMATCHED: chip generation and date unconfirmed | VULCAN, ZHAO |
| 7 | 'Oracle bonds trading at 6.95% this morning' (@rickjeff78) | no bond or source identified | UNVERIFIED | VULCAN, BROCK |
| 8 | Zerohedge: 'CCCs past 1,200 bp, AI debt $705B, Goldman: three-speed credit market' | FRED ICE BofA CCC and lower 1,417 bp [11/25]; the 1,200 index basis not identified; Goldman note not found | Basis UNKNOWN; do not set against FRED CCC | LIQUID |
| 9 | Burry posts 'must read, this is not me': Substack 'Mark to Swap: How the Market is Mispricing the AI Boom' (groundbreakerre) | not read | UNREAD | VULCAN |

- **So what:** item 1 is the new fact: two of the largest AI lenders are shedding exposure while CoreWeave's Meta-tied loan (at least $4B, Morgan Stanley and MUFG, Bloomberg 11/11) is in market. SoftBank's credit is the stress gauge on the chart (if 542 holds, it is up about 76 bp since 11/6). TERRY's CRWV card (NOT-FIRED, $48.00 trigger) already wants a fresh CoreWeave 5Y read before any entry.""",
 source="Semafor 2026-11-26 'Banks look to dump AI debt' (screenshot, search summary); Bloomberg charts via zerohedge and puckrin X posts 11/27; The Star 2026-11-06; Boardroom Alpha 8-K summary 2026-05-18; Nvidia newsroom 2026-01-26; letsdatascience and crypto.news summaries; FRED BAMLH0A3HYC",
 action=["BROCK","VULCAN"], info=["GIBBS","SAM","LIQUID","ZHAO","SHADE","REGINALD","RED","PROME"],
 precedence="PRIORITY", confidence=0.65,
 confidence_language="reports: item 1 confirmed at the article lede; CDS and spread from Bloomberg charts only; items 4, 6 to 9 unverified",
 cluster="AI_INFRA_CAPEX", domain="PRIVATE_CREDIT",
 entities=["Semafor","Citi","JPMorgan","SoftBank","CoreWeave","DDTL","Nvidia","Megaspeed","Shanghai Longteng","Oracle","Goldman Sachs","Michael Burry"],
 dispatch_note="PRIORITY: financing-leg news (PRIVATE_CREDIT per the AI-capex substance-vs-financing boundary) with VULCAN co-action on the substance items. TERRY BOARD-only, told by message (CRWV card). RED, PROME by BOARD diff.",
 route_summary="AI credit: Citi, JPM selling AI loans (Semafor); SoftBank CDS 542 chart")
cards["009"] = dict(
 id="SIG-W-20261127-009",
 slug="Small-items-Nov-27-bookmarks-Russia-December-military-pay-delay-is-the-Oct-30-Verstka-draft-combat-troops-exempt-Su-34-and-Dachne-claims-unmatched-Norse-Atlantic-suspended-flights-Nov-26-Korea-NPS-loss-is-a-won-valuation-SAP-cuts-repeat",
 safety_net="clear", event_window="open", route_origin=RO,
 origin=["X bookmarks @War_Radar2, @WarMonitor3, @Polymarket, @spectatorindex, @Reuters, @gamesblazer06", "Rule 9 helper verify (search summaries)"],
 signal_type="context",
 title="Small items, Nov 27 bookmarks: Russia's December military pay delay is the Oct 30 Verstka draft (pay to Jan 11 to 21, troops in the Ukraine group exempt; no final decision found); Su-34 'ten in three weeks' and a Dachne breakthrough not matched; Fujian landing drills and UK reservist story have no November source; Norse Atlantic suspended all flights Nov 26; Korea NPS '$151B Q3 loss' is a won valuation of listed stocks; SAP job cuts a repeat",
 body="""# Small items (WQ-622 log; logging is not scoring)

| # | Item | Read | Verdict | Tag |
|---|---|---|---|---|
| 1 | Russia's Defense Ministry proposes delaying December military pay to January, first in 18 years (@War_Radar2 11/27) | Meduza 10/30 (Verstka): draft order moves December pay to Jan 11 to 21 from the Dec 25 deadline; troops in the combined group fighting in Ukraine keep Dec 25; comment period to Nov 13; no final decision or Kremlin comment found | **Recirculated (Oct 30), framing drops the exemption** | combo:YURI/fiscal-strain |
| 2 | Musiienko: at least 10 Su-34s destroyed or damaged in three weeks, about 60% of annual output | Charter97 10/31: 8 hit in a month, 6 destroyed; Borisoglebsk 10/15 strike; output 14 to 18 a year (DIU) | Older and inflated count | combo:OSPREY/airframes |
| 3 | Ukrainian forces breach defences near Dachne, liberate the town | Dachne (Dnipropetrovsk) was Russia's last foothold there per a mid-August General Staff note; no November report found | UNVERIFIED | combo:OSPREY/front |
| 4 | China Fujian amphibious drills with civilian vessels and flotilla bridges (@WarMonitor3) | no November report or Eastern Theater announcement; the concept was documented in August 2025 | UNVERIFIED, likely old | combo:ZHAO/taiwan-strait |
| 5 | The Times: UK MoD could not locate 45,000 reservists in this week's call-up letters | no Times article found; April 2026 coverage of lost track of the recallable reserve; no call-up underway | UNVERIFIED | combo:none |
| 6 | Norse Atlantic suspended all flights (Thu Nov 26), may go bankrupt; lessors reportedly ended leases on all 12 787s Nov 27; $52M secured bonds | CNBC, Skift 11/26 summaries | CONFIRMED (date is 11/26) | combo:none |
| 7 | 'South Korea's national pension fund loses $151B in Q3' | NPS listed-stock holdings fell 182.4 trillion won (-35.3%) end-June to 10/15 (SK hynix -74.2T, Samsung -56.9T); no official Q3 loss reported by 10/28 | CORRECTED-FRAMING: a won valuation, not an official quarterly loss | combo:SAM/korea |
| 8 | SAP weighs at least 10,000 job cuts (Reuters citing Bloomberg) | SAP: no decisions made | REPEAT of 20261126-005 item 11 and 20261126-006 | combo:LABOR/layoffs |
| 9 | Commodity prices YTD: rice +95%, rubber +30%, canola +30%, cotton +29%, soybeans +20%, wheat +11% (@spectatorindex) | not checked | UNVERIFIED | combo:FERT/food-inputs |

- Absence is written 'not found by my search', not disproof.""",
 source="Meduza 2026-10-30; United24; Charter97 2026-10-31; Pravda 2026-10-29; United24 (Dachne); andrewerickson.com 2026-06-15; londonlovesbusiness (April 2026); CNBC, Skift 2026-11-26; Korea Herald, Capital.com, JoongAng summaries; CNBC 2026-11-27 (SAP); all search summaries",
 action=["YURI"], info=["OSPREY","HAWK","ZHAO","SAM","LABOR","FERT","HANS","RED","PROME"],
 precedence="ROUTINE", confidence=0.6,
 confidence_language="assessed: search summaries; most items recirculated or unmatched",
 cluster="MISC", domain="RU_STATE_ACTOR",
 entities=["Russia Defense Ministry","Verstka","Su-34","Dachne","Fujian","UK MoD","Norse Atlantic","National Pension Service","SAP"],
 dispatch_note="ROUTINE small-items card (step 10.6). ACTION YURI for item 1 only (a corrected recirculation in its lane). RED, PROME by BOARD diff.",
 route_summary="Small items: Russia pay delay is 10/30 draft; Norse; NPS; repeats")
for k,c in cards.items():
    json.dump([c], open(f"cards-{k}.json","w"), indent=1, ensure_ascii=False)
print("written", list(cards))
