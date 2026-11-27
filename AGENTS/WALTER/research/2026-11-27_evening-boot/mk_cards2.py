import json
RO = "WALTER deep dive on Will's 11/27 bookmarks (Will 18:00 ET 'Lets look into these deeper'); five research helpers from about 18:00 ET; memo research/2026-11-27_evening-boot/DEEP-DIVE.md"
DD = "AGENTS/WALTER/research/2026-11-27_evening-boot/DEEP-DIVE.md"
def rec(ks):
    a=[];i=[]
    for k in ks:
        c=json.load(open(f"cards-{k}.json"))[0]
        for x in c["action"]+c["info"]:
            if x not in i: i.append(x)
    return i
union = rec(["004","005","007","008"])
cards={}
info010=[x for x in union if x not in ("FALCON","BRENT","BROCK","CARL")]
if "RED" not in info010: info010.append("RED")
cards["010"]=dict(
 id="SIG-W-20261127-010",
 slug="CORRECTION-of-20261127-004-005-007-008-Mokhber-quote-is-real-Ras-Tanura-loading-halt-reported-Nov-26-CoreWeave-six-of-seven-DDTLs-parent-guaranteed-per-10-Q-SoftBank-USD-CDS-516-535",
 safety_net="clear", event_window="open", route_origin=RO,
 origin=["Rule 9 deep-dive helpers 2026-11-27 from about 18:00 ET (pages read as named)", DD],
 signal_type="correction",
 title="CORRECTION of 20261127-004, -005, -007, -008 after reading primaries: the Mokhber quote is real (Reuters citing state media 11/27); 'zero hour' was said by IRGC commanders 11/27 (no missile exercise announced); Ras Tanura loadings were REPORTED halted Nov 26 after the Nov 25 attack (CNN via Newsquawk; unconfirmed by Aramco); CoreWeave's 10-Q shows six of seven DDTLs parent-guaranteed ($13.1B); SoftBank USD 5Y CDS 516 to 535 bp (the 542 is the yen contract); Brent-grade January item is undatable and immaterial; October imports led by capital goods, front-running unsourced",
 body="""# Correction of four 11/27 evening cards (deep dive, primaries read)

| Card, line | Was | Now | Direction |
|---|---|---|---|
| 004 item 4 (Mokhber) | 'exact quote not found', UNVERIFIED | **Reuters 11/27 citing Iranian state media:** 'Neither will the Strait of Hormuz be reopened, nor will we allow the blockade to remain in place.' WANA adds, asked when: 'It is happening right now.' Persian original not found | UPGRADED to REPORTED (Reuters) |
| 004 item 3 ('Zero Hour') | 'not found by search', UNVERIFIED | Nour News (SNSC-linked) about 11/22 to 24: zero hour 'approaching rapidly'. 11/27: IRGC Navy commander, Newsquawk 09:29 'zero hour ... imminent ... breaking the siege is an irreversible mission' (name unconfirmed); IRGC Aerospace's Majid Mousavi on X (TASS): breaking the blockade 'a settled matter'. Wire copy merges the two. **No missile exercise toward Hormuz announced** | Statements REPORTED; the exercise part stays unsupported |
| 004 item 7 (Ras Tanura) | 'Houthi Ras Tanura claims 10/27 to 10/30 unconfirmed'; single-account image | **Wrong referent.** The live event is the **Houthi attack of Wed 11/25** (card 20261125-008: four drones intercepted, fire near the terminal, MoD no damage), then **Newsquawk 26 Nov 14:05Z: 'Oil loadings have reportedly been halted at Saudi Arabia's Ras Tanura facility, following Wednesday's attack' (CNN, shipping source).** Nortilus 11/27: no force majeure or suspension announced. Aramco silent; resumption unknown. The halt report was never carded (no WALTER day session 11/26) | UPGRADED to a REPORTED loading halt, unconfirmed by the operator; ⛔ 'force majeure' is not established (ADD#25) |
| 004 item 1 (Pacific Archer) | identity not discussed | Probable IMO 9222510 (2001 Supramax), but Maritime Optima shows that hull at Fujairah anchorage since 11/22 23:48Z | Caveat ADDED: **identity unresolved** |
| 005 item 2 (Brent-grade January) | UNVERIFIED; 'decision-relevant to the Dated Brent basket if true' | Only copy is an undated Stocktwits post aged about 386 days (possibly a November 2025 item about January 2026). Brent stream about 23,000 b/d, about one cargo a month (Reuters 6/30/2026); Platts: benchmark robust to one grade at zero | DOWNGRADED: undatable and **immaterial to Dated Brent either way** |
| 005 item 3 (SOMO) | 'nothing current found', UNVERIFIED | **Bloomberg 11/27** (unnamed sources) via PiQ/OilPrice and Kemp: 20 to 30 million bbl of November cargoes delayed, some to load in the first 10 days of December; grades and cause not given | UPGRADED to REPORTED, single source |
| 005 item 5 (runs) | '17.6 mb/d not matched; EIA 16.9 w/e 11/13' | EIA w/e 11/20: **gross inputs 17,565 kb/d** (Kemp's 17.6), crude inputs 17,346, utilization 97.5% | CONFIRMED |
| 007 'So what' and title | 'reads as front-running or restocking ahead of tariff changes'; 'widest since March 2025 per relay' | Imports +$21.1B: **capital goods +$13.4B (64%), +80% y/y**; September's rise was led by computers and accessories (FT-900). USTR's Section 301 proposals came 11/25, after October; no tier-1 source ties October to front-running. On the BOP basis October would be about third behind Mar 2025 (-$159.5B) and Jan 2025 (-$152.8B); bases differ, FT-900 on 12/8 | REFRAMED: the mix fits AI hardware; front-running is unsourced |
| 008 item 2 (SoftBank CDS) | '542.255 on a Bloomberg chart; last print found 466 bp (11/6)' | **USD 5Y: 516 bp (Bloomberg 11/26, 6:30 Tokyo) and 534.6 bp (Reuters 11/26), highest since Oct 2022.** 542.255 is the **JPY-denominated** contract. 9.75% USD bond about 644 bp | Stress CONFIRMED; level 516 to 535 USD; do not mix the yen contract |
| 008 item 4 (CoreWeave DDTLs) | 'structure partly supported (DDTL 5.0)' | **Q3 10-Q Note 10 (read at EDGAR): DDTL 1.0, 2.0, 2.1, 3.0, 5.0, 5.5 parent-guaranteed, $13.1B; DDTL 4.0 (Meta-linked, $4.58B) non-recourse.** 'Six of seven' CONFIRMED. 'Worthless' stays an anonymous opinion | UPGRADED (structure); opinion unchanged |
| 008 'So what' (Meta loan) | 'at least $4B, Morgan Stanley and MUFG (Bloomberg 11/11)' | **$4.5B**, GPUs in escrow at Dalton GA, IG rating expected, price talk 7 to 7.5% (Bloomberg via Yahoo 11/25); not launched | UPDATED (cards 20261125-031, -035 carried it) |

- **Why the first pass missed these:** its helpers read search snippets only; this pass read Reuters relays, EDGAR, EIA, Census and Newsquawk pages. Card 004 item 7 also cited October claims without grepping the BOARD for the 11/25 Ras Tanura card (MEMORY finding 2).
- **Unchanged:** everything else on 004, 005, 007, 008, including the Ghazal recirculation verdict and the fourth-carrier verdict (still three).""",
 source=DD+"; Reuters via investing.com 5053767 and wanaen.com (Mokhber); Iran International 11/24, TASS, Newsquawk via stocknow.ai (zero hour); Newsquawk 2026-11-26 14:05Z and Nortilus 11/27 (Ras Tanura); maritimeoptima.com IMO 9222510; bairdmaritime Reuters reprint 2026-06-30; PiQ/OilPrice 11/27; ir.eia.gov WPSR tables; census.gov advance_report2610.pdf; bea.gov trad0926; The Economy 11/27 (Bloomberg relay), AI Stock Wire (Reuters relay); sec.gov CoreWeave 10-Q 2026-09-30; Yahoo/StockTwits 2026-11-25",
 action=["FALCON","BRENT","BROCK","CARL"], info=info010,
 precedence="PRIORITY", confidence=0.8,
 confidence_language="reports: primaries or tier-1 relays read; Bloomberg and centcom.mil refused automated access",
 cluster="MISC", domain="GEOPOL_ENERGY",
 entities=["Mokhber","IRGC","Nour News","Ras Tanura","Pacific Archer","Brent","SOMO","EIA","Census Bureau","SoftBank","CoreWeave","DDTL"],
 dispatch_note="PRIORITY correction (direction matters: the Ras Tanura halt and the Mokhber quote are upgrades). Recipients = union of 004, 005, 007, 008 plus RED; ACTION the four cards' lead owners. R1 COR-20261127-02 same commit; banners on all four. RED, PROME by BOARD diff.",
 route_summary="Correction of 004/005/007/008: Mokhber real, Ras Tanura halt reported, CoreWeave 6 of 7",
 extra_fm={"corrects":["SIG-W-20261127-004","SIG-W-20261127-005","SIG-W-20261127-007","SIG-W-20261127-008"],
  "corrects_direction":"004 items 3, 4, 7 UPGRADED (Zero Hour statements, Mokhber quote, Ras Tanura loading halt reported 11/26), item 1 identity caveat added; 005 item 2 DOWNGRADED (undatable, immaterial), item 3 UPGRADED (Bloomberg), item 5 CONFIRMED; 007 front-running framing WITHDRAWN (capital goods led); 008 item 2 level restated in USD 516 to 535 bp, item 4 CONFIRMED six of seven, Meta loan 4.5B",
  "kill_strings":["Houthi Ras Tanura claims 10/27 to 10/30 unconfirmed","exact quote not found","last print found 466 bp","structure partly supported","reads as front-running or restocking ahead of tariff changes","decision-relevant to the Dated Brent basket if true"]})
cards["011"]=dict(
 id="SIG-W-20261127-011",
 slug="Gulf-follow-up-Kun-Peng-Hong-Kong-tanker-hit-18-nm-E-of-Khasab-Nov-25-UKMTO-223-26-Iran-navy-chief-says-blockade-breakout-underway-with-escorts-convoy-walked-back-Amrita-Sen-China-stockpiling",
 safety_net="clear", event_window="open", route_origin=RO,
 origin=["Rule 9 deep-dive helpers 2026-11-27 (houseofsaud, Korea Times/AP, Iran International, Rigzone, EIA read)", DD],
 signal_type="context",
 title="Gulf follow-up: UKMTO 223-26 / JMIC 117/26, the Hong Kong-flag tanker Kun Peng (IMO 9272503) was hit 18 nm east of Khasab about 13:00Z Nov 25 (engine-room fire out; crew safe per UKMTO, one report says one badly hurt), not carded until now; Iran's navy chief Irani on state TV Nov 27: 'breaking through the enemy blockade is underway ... maritime escorts are taking place'; the Kharg convoy story was walked back Nov 22 to 23 (still staged, no date); Energy Aspects' Sen: China to lead global stockpiling over one to two years",
 body="""# Gulf and Hormuz follow-up (new to the BOARD)

| # | Item | Read | Verdict | Owner |
|---|---|---|---|---|
| 1 | **Kun Peng** (Hong Kong flag, IMO 9272503): struck about 1300Z Wed 11/25, 18 nm E of Khasab (UKMTO 223-26 / JMIC 117/26); engine-room fire extinguished; UKMTO crew safe, another report one severely injured | houseofsaud (secondary; ukmto.org refused automated access) | REPORTED hull hit inside the strait; not a sinking, GATE 2 untouched; FALCON census | FALCON |
| 2 | Other UKMTO-reported hits this week: 11/20 (214-26, 8 nm N of Khasab, outbound tanker, fire), 11/21 (two tankers, no position), 11/22 Chabahar ('incident with military forces'), 11/25 50 nm N of Madinat ash Shamal (weak secondary). None found dated 11/26 or 11/27 | UKMTO PDF snippet, houseofsaud, euronews | FALCON reconciles with its census (card 20261123-022 sweep) | FALCON |
| 3 | **Iran navy chief Shahram Irani (Artesh), state TV 11/27:** 'breaking through the enemy blockade is underway and our ports are active today'; 'maritime escorts are taking place' | AP via Korea Times | REPORTED statement; no escorted sailing confirmed by TankerTrackers, Kpler or CENTCOM | FALCON, BRENT |
| 4 | Kharg convoy ('Operation Fereydoun', Fars 11/18 or 19): 14 (Al-Monitor) to about 20 (Kpler) tankers, mostly loaded, stationary; walked back 11/22 to 23 by Tasnim, the Foreign Ministry and IRNA; TankerTrackers: 'Line Breaker' does not exist, 'Tania Star' spoofed | Iran International 11/20 to 25 | Repeat theme (cards 20261121-002, 20261123-015, -022): staged, no sailing date | FALCON |
| 5 | IRGC mine claims daily 11/23 to 27 (11/27: north of Ghavam Island, one of two tankers), none confirmed; JMIC called 11/24's unconfirmed | Bernama-Anadolu, houseofsaud | Claims only | FALCON |
| 6 | Energy Aspects (Amrita Sen): China to lead a global stockpiling push that could tighten markets 'over the coming year or two'; Nortilus: China importing about 11 mb/d; Dubai moved to a prompt premium | Bloomberg via Rigzone 11/27 | Forecast, attributed | BRENT, ZHAO |
| 7 | EIA w/e 11/20: utilization 97.5%, gasoline 217.7 mn bbl (+3.7% y/y), distillate 105.6 mn (-5.9% y/y), SPR 273.5 mn (-2.9) | ir.eia.gov tables read | CONFIRMED | BRENT |

- **What would mark real escalation (helper's list, for FALCON to judge):** a named laden tanker or group leaving Kharg past the blockade line under Iranian naval escort, confirmed by trackers or CENTCOM; a US strike on an Iranian escort or warship, or a confirmed Iranian strike on a US ship or aircraft; a fourth carrier ordered in, or an official statement naming power, water or energy targets.
- **Guards:** ADD#26 event-date discriminators applied (Kun Peng 11/25 is not the 11/27 Ghavam claim); 'force majeure' not established anywhere (ADD#25).""",
 source=DD+"; houseofsaud.com (UKMTO 223-26 relay); Korea Times/AP 2026-11-28 KST; Iran International 202611204994, 202611235703, 202611254651; Bernama-Anadolu 2640527; Rigzone 2026-11-27; ir.eia.gov wpsr table1, table2",
 action=["FALCON","BRENT"], info=["HAWK","SAM","ZHAO","HENRY","RED","PROME"],
 precedence="PRIORITY", confidence=0.7,
 confidence_language="reports: secondary relays of UKMTO and AP; EIA read",
 cluster="IRAN_HORMUZ", domain="GEOPOL_ENERGY",
 entities=["Kun Peng","UKMTO","JMIC","Khasab","Shahram Irani","Kharg","Operation Fereydoun","Ghavam Island","Energy Aspects","Amrita Sen","EIA"],
 dispatch_note="PRIORITY: a hull hit inside the strait not previously carded, plus Iran's navy saying breakout is underway. ACTION FALCON (census, ladder), BRENT (flows). Iran guards read this session. RED, PROME by BOARD diff.",
 route_summary="Gulf follow-up: Kun Peng hit 11/25; Irani says breakout underway")
cards["012"]=dict(
 id="SIG-W-20261127-012",
 slug="AI-credit-follow-up-SoftBank-S-and-P-LTV-above-30pct-vs-35pct-downgrade-trigger-CoreWeave-11.0B-principal-due-2027-notes-74-to-79-YTW-17pct-Mark-to-Swap-thesis-Goldman-Lynam-note",
 safety_net="clear", event_window="open", route_origin=RO,
 origin=["Rule 9 deep-dive helpers 2026-11-27 (Semafor read in full, EDGAR 10-Q and Oracle FWP read, groundbrkr.com read)", DD],
 signal_type="context",
 title="AI credit follow-up: S&P says SoftBank's loan-to-value is above 30% against a 35% downgrade trigger (BB+ at S&P and Fitch); SoftBank's July to September finance costs ¥461.9B, 2.6x; CoreWeave owes $11.0B of principal in 2027 on $47.5B gross debt, its notes at 73.9 to 79.2 (YTW about 17%) on 11/25; the 'Mark to Swap' piece Burry recommended argues debt capacity, not demand, binds the AI build; Goldman's line is Lynam's 'Two-Speed Junk Market' note",
 body="""# AI-credit follow-up (deep dive)

| # | Item | Read | Verdict | Owner |
|---|---|---|---|---|
| 1 | **SoftBank: S&P says loan-to-value (debt against holdings) is above 30% against a 35% downgrade trigger**; S&P and Fitch BB+; outlook stable since July; no downgrade found. Drivers (Bloomberg): $64.6B into OpenAI in total (incl. $30B extra in February, $10B borrowed in August against OpenAI shares, $10B paid in October), Arm-backed borrowing +$5B, July to September finance costs ¥461.9B (2.6x y/y); September ¥1T retail bond at 4.75% replaced 1.38% debt | The Economy 11/27 relaying Bloomberg (read); Bloomberg 403 | REPORTED; an Arm or OpenAI markdown is the path to the trigger | SAM, BROCK |
| 2 | **CoreWeave Q3 10-Q (9/30):** total debt $47.5B gross ($41.6B recourse, $5.27B non-recourse net); principal due $2.4B rest of 2026, **$11.0B in 2027**; senior notes $10.0B face, fair value $8.8B; converts $10.8B (1.75% 2031 and 2032, 2.875% 2033); OEM and software financing $6.9B; revolver $1.2B. Risk factors: October note prices fell 'significantly' | EDGAR 10-Q Note 10 read | CONFIRMED | BROCK, VULCAN |
| 3 | CoreWeave notes 11/25 (Bond Terminal): 9.25% 2030 79.206 (YTW 17.41%, +1,277 bp); 9.00% 2031 75.614 (17.45%); 9.75% 2031 74.791 (17.70%); 9.625% 2032 73.893 (16.99%, +1,231 bp). Bloomberg via snippets: 9% 2031 record low 76.6 on 11/24 | bondterminal.com read | REPORTED (vendor) | BROCK |
| 4 | **'Mark to Swap' (pseudonymous 'Groundbreaker', posted 11/20, 8,735 words; Burry 11/27: 'Must read. This is not me.'):** AI CDS are the 2007 ABX; rated lessees trade 4 to 7 notches below agency ratings on Moody's market-implied grid; lease collateral falls with tenant CDS; about 16% of value gone across 25 campuses ($207B), 24% with the 10Y; 40% of owner equity wiped (72% behind Oracle, 91% behind CoreWeave); four of six CoreWeave campuses worth less than their debt; debt capacity, not demand, binds (41% fewer GW behind Oracle, 63% behind CoreWeave). CDS cited undated: Oracle 316, CoreWeave 1,145, Meta 120, Nvidia 128 | groundbrkr.com read in full | A thesis, not data; its CDS levels are not a dated print | VULCAN, BROCK |
| 5 | Unsourced claims inside item 4: HSBC sold part of a Jupiter campus loan 'this month at about 85 cents'; banks marketed more than $56B of Oracle-lease construction loans in February | as above | UNVERIFIED claims for owners to check | GIBBS, BROCK |
| 6 | Goldman: 'three-speed', '$705B AI issuance', 'CCC past 1,200' trace to CryptoBriefing; nearest primary is Amanda Lynam, 'AI, Credit, and a Higher Cost of Capital' (heading 'Two-Speed Junk Market'), paywalled, undated | zerohedge headings read | The 1,200 cannot be ICE BofA CCC (1,417 on 11/25) | LIQUID |
| 7 | Oracle's 11/2 $10B FWP: 7.000% 2029 (+240, 7.062%), 7.450% 2031, 7.850% 2033, 8.000% 2037, 8.650% 2046 (+335, 8.667%). No dated '6.95%' source; a 11/26 report has 20 and 30-year yields near 9% (snippet) | sec.gov FWP read | Issue levels, not trading | VULCAN, BROCK |
| 8 | Semafor (read in full): beyond the lede, 'the risk isn't so much disappearing as moving somewhere harder to see'; AI issuance has 'crowded out Treasurys'; no loan types, sizes, buyers or prices | semafor.com read | CONFIRMED; seasonal window dressing noted by Semafor itself | GIBBS, BROCK |

- **So what:** the senior, contract-backed slice (Meta-backed $4.5B at 7 to 7.5%, IG expected) and the unsecured layer (about 17%) are 10 points apart on the same borrower; banks are moving AI exposure out by synthetic risk transfer. SoftBank is the name with a numbered rating trigger. No fresh dated CoreWeave 5Y CDS print was found (TERRY's CRWV card wants one).""",
 source=DD+"; The Economy 2026-11-27 (Bloomberg relay); sec.gov CoreWeave 10-Q 2026-09-30 and Oracle FWP 2026-11-02; bondterminal.com coreweave-inc (priced 11/25); groundbrkr.com 'Mark to Swap' 2026-11-20; semafor.com 2026-11-26; zerohedge Goldman headings; cryptobriefing 2026-11-27",
 action=["BROCK","VULCAN","SAM"], info=["GIBBS","LIQUID","SHADE","REGINALD","HENRY","RED","PROME"],
 precedence="PRIORITY", confidence=0.75,
 confidence_language="reports: EDGAR and Semafor read; SoftBank and bond prices via relays and a vendor",
 cluster="AI_INFRA_CAPEX", domain="PRIVATE_CREDIT",
 entities=["SoftBank","S&P","loan-to-value","OpenAI","Arm","CoreWeave","DDTL","Mark to Swap","Groundbreaker","Michael Burry","Goldman Sachs","Amanda Lynam","Oracle","Semafor","HSBC"],
 dispatch_note="PRIORITY: SoftBank's numbered rating trigger and CoreWeave's 2027 maturity wall, read at filings. ACTION BROCK (financing), VULCAN (AI capex substance), SAM (SoftBank). TERRY BOARD-only. RED, PROME by BOARD diff.",
 route_summary="AI credit: SoftBank LTV >30% vs 35% trigger; CoreWeave 11.0B due 2027")
cards["013"]=dict(
 id="SIG-W-20261127-013",
 slug="Data-follow-up-October-imports-led-by-capital-goods-plus-13.4B-of-21.1B-up-80pct-y-y-GDPNow-Q4-2.9-NY-Fed-2.99-St-Louis-Fed-loan-demand-minus-30-confirmed-lowest-since-Feb-2024",
 safety_net="clear", event_window="open", route_origin=RO,
 origin=["Rule 9 deep-dive helpers 2026-11-27 (census.gov PDF, bea.gov, atlantafed.org and newyorkfed.org xlsx, stlouisfed.org xlsx, dallasfed.org xls read)", DD],
 signal_type="indicator",
 title="Data follow-up: October's $21.1B import jump was led by capital goods (+$13.4B, 64%; +80% y/y; September's was computers and accessories), which fits AI hardware more than a tariff rush; GDPNow Q4 2.9% (11/25), NY Fed Nowcast 2.99% (11/27); St. Louis Fed Eighth District loan demand net -30 confirmed at the issuer's file, lowest since Feb 2024 and 41 points below what bankers expected",
 body="""# US data follow-up (issuer files read)

| # | Item | Read | Owner |
|---|---|---|---|
| 1 | **October imports by end use (Census, SA, nominal, $M):** total 365,297 (+21,100, +6.1%, +42.4% y/y); **capital goods 171,405 (+13,438, +8.5%, +80.0% y/y)**; industrial supplies 62,717 (+3,548); consumer goods 61,427 (+1,585); automotive 35,706 (+1,403); foods 18,597 (+459). Exports 215,819 (+6,704). September FT-900: capital goods +$11.6B led by computers (+$7.6B) and accessories (+$5.7B); pharma +$2.9B; gold -$2.7B. Product detail for October comes in the FT-900 on 12/8 | census.gov advance_report2610.pdf, bea.gov trad0926 | ISHM, CARL, VULCAN |
| 2 | Inventories: wholesale +0.9% (durables +1.6%, nondurables -0.3%); retail +0.8% (ex autos +0.6%, autos +1.3%); September revised up | census.gov | ISHM |
| 3 | **Nowcasts:** GDPNow Q4 2.9% SAAR (11/25, from 3.2% on 11/18): net exports -0.54 pp, inventories +0.58 pp, consumer +1.44; the 11/27 trade release is an internal update, first posted 12/1. NY Fed Staff Nowcast 2.99% (11/27, from 2.85%) | atlantafed.org GDPNow xlsx, newyorkfed.org xlsx | HENRY, CARL |
| 4 | **St. Louis Fed Economic Conditions Survey, banking (11/17 file):** loan demand -30 (prior quarter +11; expected for this quarter +11; next quarter -7), credit standards +13 (prior +6), delinquency +28 (prior +25); **lowest loan demand since Feb 2024 (-50)**; Eighth District only, no loan-category or respondent count | stlouisfed.org xlsx (Figure3_banking_bar, BankingTS) | REGINALD, CARL |
| 5 | Dallas Fed trimmed mean: October 2.83 (1-mo ann.), 2.39 (6-mo), 2.37 (12-mo); September 2.99. Core PCE y/y 3.3% (card 20261125-007) vs trimmed mean 2.4%: pressure in the tails | dallasfed.org pcehist | CARL, HENRY |
| 6 | Front-running: no tier-1 source; USTR's Section 301 proposals (China up to 20% / 10% Annex A, alternative 40%; comments 1/5/2027, hearings 1/25) were posted 11/25, after October (cards 20261125-005, -006) | ustr.gov read | ZHAO, ISHM |

- **So what:** imports of capital goods up 80% in a year is an AI-capex signature in the trade data (ISHM's borrowed-demand question: AI capex, not end demand). It is a GDP drag through net exports, partly offset by equipment investment and inventories; the net shows on 12/1. The Eighth District pattern (demand down, standards tighter, delinquency up) is a stress shape on one regional survey; REGINALD may want the national SLOOS and H.8 beside it.""",
 source=DD+"; census.gov/econ/indicators/2026/advance_report2610.pdf; bea.gov trad0926.pdf and time series xlsx; atlantafed.org GDPNow; newyorkfed.org Staff Nowcast xlsx; stlouisfed.org economic-conditions-survey xlsx; dallasfed.org pcehist; ustr.gov Section 301 China FRN",
 action=["ISHM","REGINALD","CARL"], info=["HENRY","VULCAN","LIQUID","ZHAO","GIBBS","RED","PROME"],
 precedence="PRIORITY", confidence=0.85,
 confidence_language="confirmed: issuer files read",
 cluster="INFLATION_TRANSMISSION", domain="INDUSTRIAL_CYCLE",
 entities=["Census Bureau","capital goods imports","FT-900","GDPNow","NY Fed Staff Nowcast","St. Louis Fed","Economic Conditions Survey","Dallas Fed","trimmed mean PCE","USTR","Section 301"],
 dispatch_note="PRIORITY: issuer-read detail behind card 007. ACTION ISHM (imports, inventories), REGINALD (8th District lending), CARL (inflation, trade). RED, PROME by BOARD diff.",
 route_summary="Data: Oct imports led by capital goods +80% y/y; 8th District loan demand -30")
cards["014"]=dict(
 id="SIG-W-20261127-014",
 slug="Cyber-follow-up-SAP-replaced-signing-keys-and-halted-build-workflows-has-not-said-whether-customers-must-act-official-no-coordination-statements-cover-only-Nov-12-to-17-outages",
 safety_net="clear", event_window="open", route_origin=RO,
 origin=["Rule 9 deep-dive helpers 2026-11-27 (heise, BleepingComputer, Reuters via Yahoo, LBC, Insurance Journal, TechXplore read)", DD],
 signal_type="context",
 title="Cyber follow-up: SAP says it has no evidence of downstream compromise of customer systems, but Handelsblatt reports it replaced its signing keys and halted automated build workflows, and SAP has not said whether customers must act (WiWo 17:29); Lloyds restored about 13:00 to 14:00 GMT, cause not given; the US officials' 'no coordinated attack' statements (11/18 House hearing) cover only the Nov 12 to 17 outages, not the later breaches (FinCEN, FBI NCIC, CIA/ODNI, SAP, Cloud One, DWP)",
 body="""# Cyber follow-up (deep dive)

| # | Victim | Finding | Read | Channel |
|---|---|---|---|---|
| 1 | SAP | Statement (dpa, via heise and BleepingComputer 11/27): 'suspicious activity' on its GitHub platform 'for developer productivity and software delivery'; 'no evidence of unauthorized access to customer business data'; evidence 'does not show downstream compromise of customer systems or data'. Handelsblatt: GitHub access restricted, **automated build workflows halted, signing keys replaced**. WiWo 11/27 17:29: whether customers must act, SAP 'left open'. No SAP security note found; BSI not reported involved. Shares about +0.8% at the Xetra close (snippet; job-cut news same day). Not the April 2026 npm 'Mini Shai-Hulud' event | heise, BleepingComputer, WiWo | **Supply-chain tail for SAP customers (banks, insurers): watch for an SAP security note or customer advisory** |
| 2 | US Air Force Cloud One | Reuters (Stone, Satter, 11/27 14:23Z, five anonymous sources): intrusion found within the past month; migrations paused, app updates blocked, admin rights revoked; Cyber Command called in (one source); control-plane access one source; actor and data unknown; Leidos prime since 2025 | Yahoo syndication read | defense; contractor exposure only |
| 3 | Lloyds Banking Group | from about 10:00 UTC 11/27, peak over 4,000 reports; restored about 13:00 to 14:00 GMT; no cause from the bank; Faster Payments itself not shown down; fifth glitch of 2026 per one outlet | The Register, Finexus | UK bank, operational |
| 4 | UK DWP | unusual activity first seen Thu 11/26; Universal Credit, PIP, state pension, job search, Tell Us Once online services offline; NCSC and the Government Cyber Coordination Centre; payments unaffected; no ransomware claim | LBC 11/27 | government services |
| 5 | Allstate | since Mon 11/23, no cause stated, ongoing 11/27; Oklahoma House Insurance Committee leaders urged policyholder protection; ALL about +2% on the week | Insurance Journal, Yahoo Finance | insurer, operational |
| 6 | Optimizely | cyberattack 11/17 affecting about 178 sites including HSBC and Equifax | Reuters via Wikipedia only | **weak source: CYPHER to confirm at Reuters** |

- **Cluster and the denials:** the 11/12 to 17 outages have stated non-cyber causes (Microsoft gateway defect, FAA telecom, JPMorgan 'software bug ... not cyber-related', Apple update, NSA patching). DNI Clayton, DHS Secretary Mullin and FBI Deputy Director Raia (House Homeland Security, 11/18) and Rubio said no indication of external or state actors. **Those statements predate the breaches since: FinCEN (card 20261124-020), FBI NCIC, CIA/ODNI, SAP, Cloud One, DWP.** No credible common-cause reporting found.
- Never list affected credit unions by name.""",
 source=DD+"; heise.de and bleepingcomputer.com 2026-11-27; wiwo.de 2026-11-27 17:29; Handelsblatt; Reuters via Yahoo 2026-11-27; The Register; Finexus; LBC 2026-11-27; Insurance Journal; TechXplore (AFP) 11/18 hearing",
 action=["CYPHER"], info=["GIBBS","REGINALD","SHADE","HANS","LIQUID","VULCAN","RED","PROME"],
 precedence="PRIORITY", confidence=0.75,
 confidence_language="reports: tier-1 and trade press read; SAP's own site had no statement",
 cluster="CYBER", domain="CYBER",
 entities=["SAP","GitHub","signing keys","US Air Force","Cloud One","Leidos","Lloyds Banking Group","DWP","NCSC","Allstate","Optimizely","FinCEN"],
 dispatch_note="PRIORITY under CYBER v0.49 (software supplier to banks and insurers). ACTION CYPHER. RED, PROME by BOARD diff.",
 route_summary="Cyber: SAP swapped signing keys, customer action unstated; denials predate breaches")
for k,c in cards.items():
    json.dump([c], open(f"cards-{k}.json","w"), indent=1, ensure_ascii=False)
print("ok")
