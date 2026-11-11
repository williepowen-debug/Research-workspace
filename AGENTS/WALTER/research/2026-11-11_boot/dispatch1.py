import sys
sys.path.insert(0, '/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-11_boot')
from dispatch_common import *

CARDS = [
dict(n=1, slug='Saudi-tells-OPEC-October-crude-10.563-mbd-up-from-8.372-survey-9.2-conflicts-with-STEO-2.5-mbd-Middle-East-shut-ins',
 title='Saudi Arabia told OPEC it pumped 10.563 mb/d of crude in October, up from 8.372 mb/d in September (+26%, highest since February); Bloomberg\'s survey says 9.2 mb/d; this sits against EIA\'s November 10 STEO, which counted 2.5 mb/d of Middle East shut-ins in October',
 body="""**What was published.** OPEC's November Monthly Oil Market Report (November 11), direct communication table, relayed by @financialjuice at 13:01Z and by Bloomberg, Investing.com and Business Recorder the same morning:

| Series | September | October | Basis |
|---|---|---|---|
| Saudi crude, self-reported to OPEC | 8.372 mb/d | **10.563 mb/d** | direct communication; February 10.882 was the last higher month |
| Saudi crude, Bloomberg survey | about 8.23 (implied) | **9.2 mb/d (+0.97)** | independent survey |
| OPEC+ total, secondary sources | about 39.19 (implied) | **41.23 mb/d (+2.04)** | OPEC secondary sources |

**Why it matters.** Two readings of Saudi October output differ by about 1.36 mb/d. The self-reported figure is the larger. Either way Saudi output rose by roughly 1 to 2.2 mb/d in October. BRENT's grade of the November 10 STEO (9d2f187f38) carried "Middle East shut-ins 2.5 mb/d in October" and a Q4 world balance flipped to a 1.47 mb/d build on supply. BRENT also recorded a paper-physical gap: Dated Brent's newest print $107.03 (November 3), no measured build yet. This report is the second agency read BRENT named, ahead of the IEA report and the November 29 OPEC+ letter. Production is not exports: nothing here says how many barrels left through Yanbu or Hormuz.

**Limits.** WALTER did not open the OPEC report itself; figures come from the relay and three outlets that agree. OPEC's secondary-source estimate for Saudi Arabia was not read. The percent (+26%) is WALTER arithmetic on the two self-reported figures. Iran anchor last fully verified November 5; a full sweep is running now.

**Asks.** BRENT: grade against the STEO shut-in figure and your October supply path; say which Saudi series you use. TERRY: tradeability read. Will holds USO 30 shares (FORGE mirror, November 10 intraday). A reasoned NO CARD is a complete answer.""",
 sources="@financialjuice 2026-11-11T13:01:03Z (x.com status 2120502061553062010) ; Bloomberg 2026-11-11 'Saudis Tell OPEC Output Surged 26% to Highest Since War Began' https://www.bloomberg.com/news/articles/2026-11-11/saudis-tell-opec-output-they-surged-26-to-new-war-time-high [headline read] ; Investing.com https://www.investing.com/news/commodities-news/saudi-arabia-raises-oil-output-to-highest-level-since-february-93CH-5018855 ; Business Recorder https://www.brecorder.com/news/40448439/saudi-arabia-leads-further-jump-in-opec-oil-output-despite-war ; BRENT commit 9d2f187f38 (STEO grade) ; FORGE/STATUS.md USO row [11/10 intraday]",
 action=['BRENT', 'TERRY'], info=['FALCON', 'HAWK', 'RED', 'HENRY', 'PROME'],
 precedence='PRIORITY', signal_type='research', confidence=0.75, lang='reports',
 cluster='IRAN_HORMUZ', domain='OIL_ENERGY', entities=['Saudi Arabia', 'OPEC', 'OPEC MOMR November 2026', 'EIA STEO', 'USO'],
 note="OIL_ENERGY row: BRENT action, info HAWK and RED; FALCON added because the October recovery bears on the war-state supply read; TERRY ACTION under Will's 11/10 'always look for the trade' (USO held). Iran pre-dispatch guard: anchor_unverified_as_of 2026-11-05 (re-verify trigger met 11/10; full sweep helper running); guards checked: ADD#24 (a capacity or production figure is not a loss figure), two-track contradictions are not one side lying (self-report vs survey carried side by side). PRIORITY, not IMMEDIATE: no registered threshold; Brent boundaries 1 and 2 not near (BZF27 92.97 vendor 13:39Z). Precedence rises if BRENT finds the STEO shut-in figure overtaken.",
 extra=dict(anchor_unverified_as_of='2026-11-05', event_window='open')),

dict(n=2, slug='Siemens-Energy-FY2026-record-backlog-164B-Gas-Services-FY27-revenue-plus-24-26pct-Q4-orders-plus-5pct-9B-buyback-shares-up-about-9pct',
 title='Siemens Energy FY2026 (to September 30): record €164bn backlog, orders €68.1bn; FY2027 guide has Gas Services revenue +24% to 26% and Grid +22% to 24%; Q4 orders grew only 5.2%; up to €9bn more buyback; shares about +9% on November 11',
 body="""**From Siemens Energy's own release, November 11** (Rule 9 helper read the page):

| Item | Figure |
|---|---|
| FY2026 orders / revenue | €68.1bn (+18.8% comparable) / €44.2bn (+15.5%); book-to-bill 1.54 |
| Backlog, September 30 | €164bn, a record |
| FY2026 profit before special items | €5,486m (12.4% margin); net income €4,129m; free cash flow pre-tax €8,799m |
| Q4 (July to September) | orders €14.8bn, +5.2% comparable, "moderated" from the first three quarters; revenue €12.8bn, +21.5%, a record |
| FY2027 guide | group revenue +14% to 16%, margin 14% to 16%, net income about €5bn, FCF about €10bn |
| FY2027 Gas Services / Grid | revenue +24% to 26%, margin 18% to 20% / revenue +22% to 24%, margin 21% to 23% |
| 2030 target | revenue CAGR 12% to 14%, margin 20% to 22% |
| Capital return | dividend €2.30 (from €0.70); up to €9bn more buyback through FY2030 |

The release names data centres as a "new large consumer" of power: the AI build-out is "likely to lead to further investment in power generation capacity and grid infrastructure, especially in North America". It gives no gas-turbine unit or gigawatt count and no data-centre share of orders.

**For the capex question:** the turbine and grid supplier is guiding faster growth into FY2027. That is a supply-side read of continued AI power demand, not a hyperscaler capex figure. Q4 order growth slowed to 5.2%; one secondary report puts it under a €15.47bn consensus (not checked).

**Market (vendor, not a close):** ENR.DE €130.38, +8.80% at 13:40Z.

**Adjacent, not established as linked:** WSJ (November 11, headline only, paywalled): SoftBank "reserved enough gas turbines to generate the power of six Hoover Dams" at a cost of billions in losses. That ties to SoftBank's ¥597.2B power-equipment loss (cards 20261110-010, 012). The supplier is not named in what WALTER read.

**Ask, VULCAN:** log against your November 11 calendar row; grade only where a registered row keys on it.""",
 sources="Siemens Energy press release 2026-11-11 https://www.siemens-energy.com/global/en/home/press-releases/earnings-release-q4-fy-2026--siemens-energy-reports-a-record-yea.html (read by Rule 9 helper) ; RTTNews https://www.rttnews.com/3713160/siemens-energy-gains-on-strong-q4-positive-outlook-dividend-hike-9-bln-buyback.aspx [search summary only, consensus figure] ; vendor ENR.DE 2026-11-11T13:40:37Z ; WSJ via @WSJbusiness 2026-11-11T01:00:31Z https://on.wsj.com/4AkINFX [headline only]",
 action=['VULCAN'], info=['WATT', 'ISHM', 'HANS', 'SAM', 'HENRY', 'RED', 'PROME'],
 precedence='PRIORITY', signal_type='research', confidence=0.85, lang='confirmed',
 cluster='AI_INFRA_CAPEX', domain='AI_CAPEX', entities=['Siemens Energy', 'ENR.DE', 'SoftBank Group', 'Silver Bands 7'],
 note="Step 7i calendar catch-up: Siemens Energy FY2026 results are on VULCAN's catalyst ledger for 11/11; published, no owner record found, so normal triage. AI_CAPEX row: VULCAN action; WATT added (power equipment is WATT's channel per the INDUSTRIAL_CYCLE row), ISHM (capital goods), HANS (European issuer), SAM (SoftBank turbine headline). Figures from the issuer's release via a Rule 9 helper; WALTER did not read the PDF tables. PRIORITY: guidance, no capex cut.",
 extra=dict(event_window='closed')),

dict(n=3, slug='Commercial-Times-via-TrendForce-Nvidia-may-slow-chip-orders-amid-Huang-controversy-unquantified-same-report-says-orders-unchanged-for-now',
 title='Report, unquantified: Taiwan\'s Commercial Times, via TrendForce (November 10), says supply-chain sources suggest Nvidia "may slow chip orders" amid the Huang controversy, touching TSMC and ASE; the same article says orders and capacity "remain unchanged for now"',
 body="""**What the article says** (TrendForce news, November 10, read in full by a Rule 9 helper):

- "According to Commercial Times, supply chain sources suggest that NVIDIA may slow chip orders, potentially affecting upstream suppliers such as TSMC and ASE." No product, size or period is given.
- TrendForce's own inference, not a report: freed TSMC capacity "could benefit" AMD and ASIC designers (Broadcom, MediaTek, Alchip, GUC).
- **The same article cuts against it:** Commercial Times says some AI server orders face "renewed reviews" but "orders and production capacity remain unchanged for now"; Economic Daily News reports "no disruptions to orders or shipments" at Taiwanese chassis, rack and cooling suppliers.
- No Nvidia comment or denial is reported.

**Context already on the board:** Nvidia fell 5.47% to $168.89 on November 10 (vendor close; card 20261110-011). Huang's acknowledgement and the probe are on cards 20261109-004 and -011. The House briefing request for November 18 is reported by TrendForce, not checked by WALTER.

**Why route a weak claim:** an order slowdown at the largest AI-chip buyer is the class VULCAN's capex-cut gate watches. It decays quickly, so it goes now with its caveats rather than waiting. As worded it is a "may" from unnamed sources, contradicted in the same piece. Nothing here meets any VULCAN letter.

**Ask, VULCAN:** log it; say whether any row would key on a confirmed order cut, and what would confirm one.""",
 sources="TrendForce 2026-11-10 https://www.trendforce.com/news/2026/11/10/news-nvidia-order-cuts-reportedly-loom-amid-huang-controversy-amd-asic-rivals-may-gain-tsmc-capacity/ (read by Rule 9 helper; original Commercial Times not read) ; RESEARCH-INTAKE data/2026-11-10/news.json ; vendor NVDA close 2026-11-10",
 action=['VULCAN'], info=['HENRY', 'VIOLET', 'RED', 'ZHAO', 'PROME'],
 precedence='PRIORITY', signal_type='research', confidence=0.35, lang='claims',
 cluster='AI_INFRA_CAPEX', domain='AI_CAPEX', entities=['Nvidia', 'TSMC', 'ASE', 'AMD', 'Broadcom', 'MediaTek', 'Alchip', 'GUC', 'Commercial Times', 'TrendForce'],
 note="source: RESEARCH-INTAKE (VULCAN watch-level item). CHECKLIST 1.5 trigger (secondhand primary): Rule 9 helper read the TrendForce page; Commercial Times original not reached. Verdict INDETERMINATE: the claim is reported, not confirmed, and contradicted inside the same article. Routed by decay rate (MEMORY #9) at low confidence with the caveat written in. ZHAO info: Taiwan supply chain and the export-control angle of the Megaspeed story.",
 extra=dict(verify_research_verdict='INDETERMINATE', event_window='open')),

dict(n=4, slug='Small-items-Nov-11-VIX-near-18-RED-FT-06-exit-could-complete-today-SoftBank-Tokyo-closed-minus-0.44-SEC-penalties-lowest-since-2008-El-Nino-Florida',
 title='Small items, November 11: VIX near 18 on the day RED\'s FT-06 exit and RED-29 could complete; SoftBank closed −0.44% in Tokyo after opening −7.2%; SEC 2026 penalties $1.1B, lowest since 2008; Google TPU line-up; South Florida El Niño severe-weather odds; a TruStage claimant follow-up',
 body="""| Item | What it says | For | WALTER check |
|---|---|---|---|
| **VIX at the line** | VIX closed 19.46 on November 10 (VIOLET; vendor prior close agrees). RED-FT-06's exit needs VIXCLS of 18 or more on five sessions. RED had 3 of 5 through November 9; November 10 would make 4. RED-29 needs 18 or more on November 6, 9, 10 and 11. Today is a VIXCLS session (Veterans Day closes bonds, not stocks). | RED, VIOLET, HENRY | ^VIX 18.35 at 13:39Z, before the cash open: 0.35 above 18, inside 5%. Near-trigger watch, not a grade; RED grades after 10:30 ET November 12 |
| @OddStats | No VIX history since 1990 has two closes over 25 followed by three straight under 20; today would be the first | VIOLET | claim not checked; Cboe history is VIOLET's |
| SoftBank, first Tokyo session after results | opened −7.2%, low ¥3,465, closed ¥3,855 (−0.44%) on 82.7M shares; SAM's dated "wrong if" did not fire | VULCAN, LIQUID, RED | SAM's read (STATUS 08:5x ET); vendor 9984.T ¥3,855 −0.44% agrees |
| @rdd147 | Calls SoftBank's Ohio structure circular: its own developer (Portsmouth Landco LLC) builds for its own landlord (SB Energy); first building by 2030, rest by 2032; $60B+ build-out | SAM, VULCAN | opinion; entity names and dates not checked |
| SEC FY2026 enforcement | penalties ordered $1.1B, lowest since 2008 | BROCK | SEC press release 2026-113 linked; WALTER did not open it |
| Google TPU (TrendForce) | first year with four TPUs; 8i Max doubles HBM bandwidth | VULCAN | headline only |
| NWS Miami | strong El Niño winters bring about 3x more severe-weather reports in South Florida than neutral winters | CORAL, AEOLUS | NWS office post; chart not opened |
| @DRmetwatch | compares two Florida heavy-rain events three years apart | CORAL | images not opened |
| TruStage | Las Vegas family still waiting on a claim after the TruStage cyberattack (Yahoo, November 6) | CYPHER | consequence follow-up to cards 20261022-043, -044; no new incident fact |

No directed asks; owners log.""",
 sources="FRED VIXCLS (11/9 19.92) ; vendor ^VIX 2026-11-11T13:39:28Z ; VIOLET commit a6385331e2 (19.46) ; AGENTS/RED/registry/FALSIFICATION_TRIGGERS_SCAN.tsv RED-FT-06 ; PROME/DOCKET.tsv RED-29 row ; @OddStats 2026-11-11T12:55:00Z ; AGENTS/SAM/STATUS.md 2026-11-11 08:5x ET ; vendor 9984.T 13:40:37Z ; @rdd147 2026-11-10T19:17:03Z ; @davidamichaels 2026-11-10T19:37:37Z https://www.sec.gov/newsroom/press-releases/2026-113-sec-announces-enforcement-annual-results-fiscal-year-2026 ; TrendForce via RESEARCH-INTAKE 2026-11-10 ; @NWSMiami 2026-11-10T13:50:00Z ; @DRmetwatch 2026-11-11T03:09:51Z ; Yahoo via RESEARCH-INTAKE (TruStage, 2026-11-06)",
 action=[], info=['RED', 'VIOLET', 'HENRY', 'VULCAN', 'LIQUID', 'SAM', 'BROCK', 'CORAL', 'AEOLUS', 'CYPHER', 'PROME'],
 precedence='ROUTINE', signal_type='context', confidence=0.6, lang='reports',
 cluster='MISC', domain='MARKET_VOL', entities=['VIX', 'RED-FT-06', 'RED-29', 'SoftBank Group', 'Portsmouth Landco LLC', 'SEC', 'Google TPU', 'TruStage', 'El Nino'],
 note="Folded small items from bookmarks BM-20261111-02 and intake BM-20261111-01, logged per WQ-622 (small news recorded for combination). The VIX line is a near-trigger watch under THRESHOLD_SCAN step 7, routed because it is decision-relevant today (BOARD_CONSUMPTION_SPEC 3.5.3); RED owns the grade. RED is pull-complete: INFO by BOARD diff."),
]

stamp, paths = send(CARDS, "WALTER boot 2026-11-11 (walter-1e): step 7i calendar catch-up, step 7e intake, step 7h bookmarks")
print(stamp)
print('\n'.join(paths))
