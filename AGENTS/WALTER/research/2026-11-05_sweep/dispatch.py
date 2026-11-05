import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
O='WALTER news sweep November 5 / 1,690 headlines, 32 queries'
CARDS=[
dict(n=44,slug='KBRA-private-credit-defaults-largest-quarterly-jump-112-borrowers',
 title='KBRA: private credit defaults post their largest quarterly jump, 112 borrowers, up 22%; concentrated in smaller companies',
 action=['BROCK'],info=['LIQUID','SHADE','RED','PROME'],precedence='PRIORITY',signal_type='research',confidence=0.65,
 cluster='PC_STRESS',domain='PRIVATE_CREDIT',entities=['KBRA','direct-lending'],
 body='''Bloomberg, November 5, body refused retrieval; figures come from a search summary of it. KBRA's report: 112 borrowers defaulted on private debt, up 22% from the prior quarter, the largest single-quarter rise on record. Sample: more than 3,000 middle-market companies with over $1.4T of direct-lending debt, 12 months through September. Pressure sits in smaller borrowers.

Not the same series as Fitch's 6.3% (card 039); do not merge counts or rates. KBRA's rate for this period was not read, and "largest jump" is a change, not a level.

Why it matters: this arrives beside Fitch's Q3 count, BCRED's 49.9% fill (032) and the Fed survey showing banks tighter on nonbank lenders (031, 043). Same direction, separate instruments; WALTER grades none of it.

ACTION BROCK: read KBRA's own report and place it against your default line.''',
 sources='https://www.bloomberg.com/news/articles/2026-11-05/private-credit-defaults-record-largest-quarterly-jump-kbra-says (refused) ; Google News title 2026-11-05',
 note='Search-summary figures, labelled. Stated as new against BOARD 1104-026 KBRA mention.'),
dict(n=45,slug='Micron-pauses-Taoyuan-plant-labor-dispute-unconfirmed-by-company',
 title='Bloomberg: Micron all but halts its $3–4.5B Taoyuan plant over a labor dispute; Micron has not confirmed, existing output continues',
 action=['VULCAN'],info=['HAWK','HENRY','RED'],precedence='PRIORITY',signal_type='context',confidence=0.75,
 cluster='AI_INFRA_CAPEX',domain='AI_CAPEX',entities=['MU','Micron','Taoyuan','Fab-11E'],
 body='''Taipei Times reprint of Bloomberg, read: Micron "has all but halted construction" of its Taoyuan memory plant, Fab 11E, budgeted US$3–4.5B, due 2028, per people familiar. Taoyuan's government says it has not been notified. Micron: "our operations today continue as normal", not addressing the complex.

Secondaries: the union wants clearer profit-sharing; 24-hour strike October 22; talks resume November 6. The Taiwanese labor authority's role and that date rest on secondaries. Taichung's union settled October 21. Taiwan is 50–60% of Micron's output, a secondary figure.

Why it matters: a rare labor stoppage at a memory leader while memory shortages are the bull case. MU fell about 12–13% today, within a broad chip rout; no source isolates this cause.

Separate from today's AI selling, not a demand signal. A supply delay, if it stands, tightens memory further.

ACTION VULCAN: place against your memory read.''',
 sources='https://www.taipeitimes.com/News/biz/archives/2026/11/06/2003867231 ; https://www.bloomberg.com/news/articles/2026-11-05/micron-pauses-work-on-4-5-billion-taiwan-plant-after-labor-spat ; Google News titles 2026-11-05',
 note='HAWK as Taiwan chokepoint. Anonymous sourcing retained.'),
dict(n=46,slug='Fed-OCC-called-banks-after-Binance-hack-Reuters-sources',
 title='Reuters sources: Fed and OCC supervisors called banks after the $6.3B Binance hack; no disruption found, no guidance issued',
 action=['CYPHER'],info=['GIBBS','REGINALD','LIQUID','RED','PROME'],precedence='PRIORITY',signal_type='context',confidence=0.7,
 cluster='CYBER',domain='CYBER',entities=['Binance','Federal-Reserve','OCC','TraderTraitor'],
 body='''Update to CYPHER's Binance thread (card 20261104-061). Reuters via Investing.com, summary read: supervisors began calling banks November 2, asking about unusual activity or disruptions. Fed and OCC declined comment. Anonymous sources. One report says banks found no disruption. No new guidance announced.

Why it matters: this is the first sign of US bank supervisors treating a crypto theft as a possible bank risk. It is outreach, not a finding.

⛔ Crypto outlets call it a "probe" raising "Wall Street contagion fears". Relay neither word; nothing reports a bank affected.

FBI attribution to TraderTraitor, October 31. Recovery figures conflict (90–95% versus 98%), and stablecoin freezes $2.4B versus about $3B; these measure different things.

ACTION CYPHER: add to the thread. GIBBS: context only.''',
 sources='https://investing.com/news/economy-news/binance-hack-prompted-us-regulators-to-check-in-on-bank-systems-sources-say-5002832 ; https://cryptobriefing.com/us-regulators-check-banks-binance-hack/ ; https://www.cryptopolitan.com/fed-occ-phone-banks-after-binance-hack/',
 note='PROME on the line for the crypto no-owner class history. Search summaries; bodies unread.'),
dict(n=47,slug='AI-financing-leads-SpaceX-sell-down-Partners-Group-gates-Microsoft-Oracle-delays',
 title='AI financing leads: Goldman and Apollo marketing SpaceX\'s $40B; Partners Group gates again; IREN, Nebius and Oracle site-delay claims',
 action=['VULCAN','BROCK'],info=['WATT','LIQUID','RED'],precedence='PRIORITY',signal_type='context',confidence=0.5,
 cluster='AI_INFRA_CAPEX',domain='AI_CAPEX',entities=['SpaceX','Apollo','Goldman-Sachs','Partners-Group','IREN','NBIS','ORCL','Project-Jupiter'],
 body='''Headlines November 5, bodies unread.

Bloomberg: "Goldman, Apollo in Talks to Sell SpaceX's $40 Billion AI Deal." Background: binding commitment disclosed October 26, reported about $10B bank loans and $30B investment-grade debt, close by year-end. Whether demand holds in this tape is the question; unread.

Citywire: Partners Group investors "continue hitting redemption gates in October". October figures unread. BROCK: wrapper read.

BigGo, weak source: Microsoft's $5B capex gap, satellite images point to delays at IREN and Nebius sites. WALTER found no corroboration; a search found only an older FT/SynMax 40% estimate and Microsoft's capex miss in one secondary. Treat as a claim. IREN fell about 17% and Nebius 16% today, tape.

Stocktwits: Oracle's OpenAI-linked New Mexico site faces a fresh power permit delay. Project Jupiter's air permit decision was reported due by November 23; current status unclear.

ACTION VULCAN, BROCK: read at your sources.''',
 sources='Google News titles 2026-11-05 ; https://techcrunch.com/2026/10/26/spacex-locks-in-40b-gpu-financing-deal-with-apollo/ ; https://www.tomshardware.com/tech-industry/artificial-intelligence/analytics-group-signals-possible-delays-at-40-percent-of-ai-data-center-construction-sites-companies-deny-schedule-holdups-but-satellite-imagery-indicates-otherwise ; https://www.abqjournal.com/business/new-mexico-supreme-court-lifts-stays-on-project-jupiter-dealing-setback-to-opponents/3124024',
 note='Lead card, low confidence by design.'),
dict(n=48,slug='35-West-Wacker-236M-foreclosure-suit-Chicago-Loop',
 title='Lender sues to foreclose on $236M loan tied to 35 West Wacker, Chicago; headlines only',
 action=['CREED'],info=['REGINALD','LIQUID'],precedence='PRIORITY',signal_type='context',confidence=0.6,
 cluster='BANK_COLLATERAL',domain='BANK_CRE',entities=['35-West-Wacker','Chicago'],
 body='''The Real Deal and Crain's Chicago Business, November 5, headlines: lender sues to foreclose on a $236M loan tied to 35 West Wacker; "Wacker Drive tower landlord hit with $236M foreclosure lawsuit". Bodies refused retrieval. Lender, borrower, loan type, occupancy and filing date unread. A search found no other coverage.

⛔ Not Société Générale's $237M 161 North Clark suit (2023), a near-identical number.

ACTION CREED: case entry and read at the source. No WALTER grade.''',
 sources='Google News titles 2026-11-05 (The Real Deal, Crain\'s Chicago Business) ; https://therealdeal.com/chicago/2023/10/04/societe-generale-foreclosing-on-237m-loop-office-debt',
 note='Named property distress, so case field and CREED line. Illinois Center sale November 12 is separate.',
 extra=dict(case=['35 West Wacker, Chicago IL'])),
dict(n=49,slug='Layoff-headlines-before-payrolls-Amazon-Block-Comcast-manufacturing',
 title='Layoff headlines before payrolls: Amazon and Alaska in Washington, Block, Google, Comcast; 6,000+ manufacturing cuts in October',
 action=['LABOR'],info=['CARL','HENRY','ISHM'],precedence='PRIORITY',signal_type='context',confidence=0.55,
 cluster='CONSUMER_STAGFLATION',domain='LABOR',entities=['AMZN','ALK','XYZ','GOOGL','CMCSA','ServiceNow'],
 body='''Headlines November 4–5, bodies unread; labor intake is LOOSE into Friday's payrolls.

OPB: Amazon and Alaska Airlines cut jobs in Washington state. Business Insider: Block's second round this year. Yahoo: "Google Joins The Surge Of Tech Layoffs"; Comcast broad layoffs, narrative piece. Manufacturing Dive: over 6,000 manufacturing layoffs announced in October. NowBen, weak source, says "Exclusive": more ServiceNow layoffs.

Set against: claims 189,000 and October Challenger cuts lowest for the month since 2023 (card 002). Reuters calls claims a 57-year low.

Why it matters: these are announcements, not counted exits, and most fall after October's survey week, so they cannot move Friday's print. They bear on November onward.

ACTION LABOR: note for the November read; do not grade Friday against them.''',
 sources='Google News titles 2026-11-05',
 note='Survey-week inference is WALTER\'s; LABOR owns it. Folded per desk.'),
dict(n=50,slug='Sweep-roundup-Lagarde-Argentina-Russian-refineries-French-OT-attack-yttrium',
 title='Sweep roundup: Lagarde on December, Argentina peso-debt bonds, Russian refinery count, French blood-bank OT attack, yttrium to Japan',
 action=['HANS','SAM','OSPREY','CYPHER','ZHAO'],info=['BRENT','LIQUID','RED'],precedence='ROUTINE',signal_type='context',confidence=0.5,
 cluster='MISC',domain='GEOPOL_NON_ENERGY',entities=['ECB','Lagarde','Argentina','Rosneft','Ryazan','yttrium'],
 body='''Headlines November 5, bodies unread; each for its owner.

HANS: Reuters: Lagarde says data will tell if a December hike is needed. Bloomberg's "unanimously hikes" on the BoE means all nine backed a rise; BoE's primary vote is still 8–1, one for more.

SAM: Bloomberg: Argentina bonds drop as market flags intervention in peso debt. Content unread.

OSPREY, BRENT info: RBC-Ukraine and UNITED24: 15 of 38 major Russian refineries halted. Ukrainian outlets; a search found FT's 16 "targeted" since August 2025, a different measure. Meduza: Ryazan refinery fire. Straits Times: strikes deplete Russian diesel supply.

CYPHER: France 24, SecurityWeek: hackers reached a French blood bank's cooling controls, attempted heating to 110°C; no products compromised. Central Oregon Daily: US warns of "ongoing cyber threat" to industrial refrigeration; agency unread.

ZHAO: BigGo, weak source: yttrium oxide exports to Japan down 98%.

Check before relaying.''',
 sources='Google News titles 2026-11-05 ; AGENTS/WALTER/research/2026-11-05_sweep/headlines.json',
 note='Thin items folded. Two Iran headlines held out of this card, see SWEEP-REVIEW.md.'),
]
print(send(CARDS,O)[0])
