import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_bookmarks3')
from dispatch_common import *
CARDS=[
dict(n=29,slug='Microsoft-ends-older-Oracle-rental-and-delays-IREN-for-network-upgrade-ORCL-recovered-the-drop',
 title='Microsoft lets a 2023 Oracle rental lapse and asks IREN for a network upgrade; ORCL recovered the drop; the "deals falling apart" post overreaches',
 action=['VULCAN','LIQUID'],info=['BROCK','HENRY','RED','PROME'],precedence='PRIORITY',signal_type='context',confidence=0.8,lang='reports',
 cluster='AI_INFRA_CAPEX',domain='AI_CAPEX',entities=['Microsoft','Oracle-Corp','ORCL','IREN','Tencent'],
 body='''Two reports, same customer.

Oracle: Bloomberg November 6, read through Investing.com and a Reuters brief; Bloomberg's page refused the fetch, full text unread. Microsoft declined to renew a contract announced in 2023 for Bing AI capacity on older Nvidia chips, and has been turning that capacity off in recent months. Value could not be determined. Microsoft declined to comment. Oracle says demand stays strong, including for earlier-generation GPUs; in September it said it renews four-year-old GPUs at a 20% premium. No page read ties this to OpenAI.

Tape: ORCL low $109.21, then $115.29 at 14:05 ET, +0.1% on the November 5 close of $115.16. Yahoo, intraday, not a close. The −4% and −5% posts describe the first drop. Still under the $116 offering price.

BullTheory post, checked:
- Tencent $7B cancelled: FT November 4, two people, after US officials raised concerns. No public confirmation from either company in what was read. "Trump administration" is other outlets' wording.
- 11% discount: holds, $116 against $130.67 on October 30, −11.2%.
- 8.65%: top coupon, card 021.
- "Used up its funding limit through 2030": the October 28 cap is $20B for fiscal 2027–2030, excluding refinancing. It was spent as planned, not forced past a limit.
- −26% in 7 sessions: only high to low, $148.48 to $109.21. October 28 close to 14:05 is −20.2%.
- −68% from the high: −66.1% now on Yahoo's adjusted $340.56.
- CDS record 3.25%: not found. BOARD has 288 bp on October 15; one undated report says 315 bp.
- "Biggest deals falling apart": not supported. The Microsoft contract's size is unknown.

IREN: CNBC November 5, read whole; call unread. Over $4B of annual recurring revenue projected for 2026 moves to at least January, payment possibly February, on "a customer-requested change and supplier timing". Co-CEO Daniel Roberts named Microsoft, which asked to reconfigure and upgrade network infrastructure so 200 MW can serve latest-generation frontier models. IREN says the target stays fully contracted and funded. That is weeks of delay on a run-rate, not $4B lost. Capex $15B for the rest of the fiscal year: $9B cash and committed, $6B target financing "subject to market conditions". IREN $21.62 at 14:05 ET, +19.9% on $18.03. This gives the company's account beside card 047's satellite-delay claim.

WALTER's framing, not a finding: older capacity dropped, newer spec demanded. That bears on older GPU life and sits against Oracle's 20% renewal claim.

ACTION VULCAN: read both at your sources and decide whether either moves a score. ACTION LIQUID: read the $6B target financing and Oracle's position under its offering price.''',
 sources='https://ca.investing.com/news/stock-market-news/oracle-falls-4-as-microsoft-reportedly-winds-down-ai-cloud-capacity-deal-4939940 ; https://live.euronext.com/en/financial-news/microsoft-winding-down-oracle-deal-rent-ai-cloud-capacity-bloomberg-news-reports ; https://www.bloomberg.com/news/articles/2026-11-06/microsoft-is-winding-down-oracle-deal-to-rent-ai-cloud-capacity (unread) ; https://www.investing.com/news/stock-market-news/oracle-cancels-7-bln-chip-leasing-deal-with-tencent-ft-reports-4997349 ; https://www.cnbc.com/2026/11/05/iren-earnings-report-q1-2027-.html ; https://investinglive.com/stocks/icymi-oracle-jumps-around-11-on-225bn-2030-revenue-goal-and-20bn-cap-on-new-funding/',
 note='Bookmarks 2, 3, 6, 7, 8, 11, 13. Rule 9 fetch helpers read CNBC and three of four Oracle pages. No Oracle row in the four threshold registries. Prices are intraday.',
 extra=dict(kill_strings=['Oracle\'s AI deals are falling apart one by one'])),
dict(n=30,slug='OpenAI-round-shrinks-SoftBank-hundreds-of-millions-after-65B-Friar-1.25-trillion-misstatement',
 title='OpenAI round cut by at least a third; SoftBank in talks for hundreds of millions after about $65B; Friar\'s "$1.25 billion" is a slip',
 action=['VULCAN','SAM'],info=['LIQUID','BROCK','ZHAO','HENRY','RED','PROME'],precedence='PRIORITY',signal_type='context',confidence=0.75,lang='reports',
 cluster='AI_INFRA_CAPEX',domain='AI_CAPEX',entities=['OpenAI','SoftBank','MGX','Coatue','Arm'],
 body='''NYT DealBook, November 6, two excerpts read in images, whole piece unread, anonymous people. OpenAI cut its round by at least a third from up to $30B at up to $1.5T in September, and now raises at $1.25T. It seeks up to $20B in two parts; today is the first part's deadline and it expects to close in coming weeks. An Emirati group including MGX is expected to lead with single-digit billions. SoftBank is in talks for hundreds of millions, against roughly $65B so far. Coatue discussed hundreds of millions.

The news is the marginal funder: SoftBank's check is a small fraction of its last $30B.

CFO Sarah Friar, CNBC November 6, excerpts: "almost a 50% lift" from March. $1.25T on $852B is +46.7%, so that holds. The transcript has her saying $1.25 billion; coverage treats it as a slip. Do not quote the billion. She said OpenAI keeps investing despite midterm opposition to data centers, and still looks at a 2027 listing.

Zitron post: "has not closed" fits the NYT. His "$11bn" is not in the excerpts, which say up to $20B; not found elsewhere. His Anthropic $1.1T listing claim was not checked and is not routed as fact.

SoftBank post, DeItaone, no source named: −59% since early June holds, ¥8,624 on June 2 to ¥3,549 November 6, −58.8%, Yahoo. Arm −51% since June 30 holds, $354.57 to $173.68 intraday. Debt added $40.4B, OpenAI $64B and leverage 13% against a 25% limit are unchecked; NYT says roughly $65B. Adds to card 003.

ACTION VULCAN: integrate the round terms. ACTION SAM: read SoftBank's reduced check beside card 003 at your sources. No grade moved here.''',
 sources='NYT DealBook November 6 (images in Will bookmark 2118740290936709157) ; https://www.cnbc.com/2026/11/06/cnbc-exclusive-transcript-openai-cfo-sarah-friar-speaks-with-cnbcs-sara-eisen-on-squawk-on-the-street-today.html ; https://www.cnbc.com/2026/11/06/open-ai-data-centers-election.html ; https://fourweekmba.com/ai-openai-cfo-puts-raise-talks-at-1-25t-47-above-march/',
 note='Bookmarks 5, 15, 20, 23. Friar text from search extracts; transcript page not opened whole.'),
dict(n=31,slug='ECB-supervisors-weigh-review-of-bank-data-center-lending-not-final',
 title='ECB supervisors weigh a review of bank data-center lending, possibly on-site; not final',
 action=['HANS'],info=['VULCAN','BROCK','LIQUID','REGINALD','RED','PROME'],precedence='PRIORITY',signal_type='context',confidence=0.7,lang='reports',
 cluster='AI_INFRA_CAPEX',domain='EUROPE_MACRO',entities=['ECB','European-banks','data-centers'],
 body='''Bloomberg, November 6, people familiar; read through search extracts and relays, full text unread, no ECB statement found. Senior ECB supervisors have raised a review of data-center lending internally and with lenders they oversee, to gauge risk from swings in AI sentiment and valuations. It could take the form of on-site inspections on how banks assess future cash flows, collateral values and default provisions. One source says the scope would be narrower than the earlier leveraged-finance review. The approach is not final.

Delta: in February the ECB asked a small number of lenders for more detail (Bloomberg, February 23). This would be a step up in form, if it happens.

ACTION HANS: read it at your sources and decide whether any row applies. HANS-T-14 is the nearest by subject, and it concerns bank links to private credit, so WALTER does not read this as a fire and does not grade it. No lender is named in what was read.''',
 sources='https://www.bloomberg.com/news/articles/2026-11-06/ecb-considers-review-of-banks-data-center-lending-as-fears-rise (unread) ; https://in.investing.com/news/stock-market-news/ecb-mulls-review-of-bank-lending-tied-to-data-centers--bloomberg-93CH-5687535 ; https://www.bloomberg.com/news/articles/2026-02-23/ecb-steps-up-scrutiny-of-european-banks-ai-industry-exposure',
 note='Bookmark 14. First search returned only February; a second found the November 6 report.'),
dict(n=32,slug='BROCK-MFIC-Q3-non-accruals-7.9-percent-at-cost-six-new-names',
 title='BROCK: MFIC Q3 non-accruals 7.9% at cost from 4.6%, NAV as pre-announced',
 action=[],info=['OTTO','CARL','LIQUID','RED','PROME'],precedence='ROUTINE',signal_type='context',confidence=0.9,lang='confirms',source='BROCK',
 cluster='PC_STRESS',domain='PRIVATE_CREDIT',entities=['MFIC','ARCC','LendingPoint','Thomas-Scientific','Heniff','Magnate','Kauffman-Engineering','CSC','US-Auto'],
 body='''BROCK, November 6. MFIC, Apollo-managed and being bought by ARCC: final September 30 NAV $12.86 equals the preliminary, −3.81% on the quarter. BROCK's ladder row 6 did not fire.

New since the October 27 deal: non-accruals 7.9% of total investments at cost, from 4.6% on June 30; 5.7% at fair value, from 2.9%. Six new names, $132.9M at cost: LendingPoint, Thomas Scientific, Heniff, Magnate, Kauffman Engineering, CSC.

For OTTO: the US Auto pool went from 0.40 to 0.11 of cost, and LendingPoint is on non-accrual. BROCK says this may interest you; no ask.

Limits: call not read. The issuer's sentence says debt portfolio, while 7.9% reproduces only on total investments, so quote the denominator. No score moved.''',
 sources='MFIC 10-Q 0001193125-26-447829 ; 8-K 0001193125-26-448373 ; AGENTS/BROCK/research/2026-11-06_mfic-q3/REPORT.md ; KB-BRK-453, 454, 455',
 note='BROCK packet SIG-BROCK-WALTER-20261106-003. WALTER checked NAV and non-accrual table in BROCK REPORT.md, not the filing.'),
dict(n=33,slug='Small-items-Apple-20-percent-unsupported-put-call-1.05-France-diesel-Cybertruck-DraftKings-month-old',
 title='Small items: Apple 20% claim unsupported; put/call 1.05; France 3.6M barrels unconfirmed; Cybertruck ends; DraftKings suit is a month old',
 action=[],info=['VULCAN','HENRY','VIOLET','RED','LABOR','FERT','BRENT','HANS','OTTO','ORACLE','CORAL','SAM','CYPHER'],precedence='ROUTINE',signal_type='context',confidence=0.65,lang='reports',
 cluster='POSITIONING_VALUATION',domain='MARKET_VOL',entities=['Apple','CPCE','VIX','SAGESS','Cybertruck','DraftKings','Seminole-Tribe','EFS','Coolworld'],
 body='''Each line is for its owner; no asks.

- VULCAN: ⛔ Kalshi, 18:09Z, "Apple cuts AI infrastructure spending by 20%". Not found in two searches about an hour later. That is a negative, not proof it is false. Reported instead: Bloomberg November 4, some engineers' daily AI tool caps cut from $300 to $200; secondary reports of fiscal 2026 capex −29% to $9.0B and R&D +32% to $45.8B.
- HENRY, VIOLET, RED: StockCharts equity put/call 1.05 on November 5, chart read, the top of its 2024–26 range. S&P 7,353.73, −4.36%, 200-day 7,322.74. "Spikes come near lows" is an unverified pattern claim. Bloomberg, November 5, "Crowded Hedge Fund Trades Are Unwinding Fast After Ugly October", excerpts only; forced-cut quote is an opinion. Its chart shows SOX near −9.5% on November 5; Yahoo closes give −12.2%. Reconcile before quoting.
- RED: VIX fell 4.22 to 16.61, rose 11.57 to 28.18, and was 24.53 at 12:50 ET, Yahoo, not a close. The OddStats pattern needs a −4 close, 24.18 or lower. No registry meaning.
- LABOR: a post says long-term share 28.7% unadjusted. Card 001 has 27.6% adjusted. WALTER could not read that table's columns; unchecked.
- FERT: Health Ranger, a food seller, says all US organic corn is sold out to June 2027. One anecdote. Argus says 2026-27 began with no carryover, so tight is supported, sold out is not. His fertilizer link is his inference.
- BRENT, HANS: Kalshi says France sold 3.6M barrels of diesel. Not found. Official program is 10M barrels, November 1 to January 31, at cost. Whether 3.6M is sales to date is unknown.
- OTTO: Reuters via NBC, read whole. Musk on X: Cybertruck production winds down around mid-2027 to raise Cybercab output. 2025 US sales 20,237, −48%, Kelley Blue Book.
- ORACLE desk, CORAL: "BREAKING" DraftKings post. The Seminole Tribe sued DraftKings and CEO Robins in Broward County on October 8, including a Florida RICO claim. No November development found.
- SAM: Takaichi, November 6, says AI and chip selloff may or may not persist; monitoring, no measure. Headlines only.
- CYPHER: adds to card 050. Contractor Coolworld hit, night of November 1–2; 110°C was a setpoint, not necessarily reached; EFS says samples unaltered. Site count disputed.''',
 sources='https://techcrunch.com/2026/11/04/apple-is-reportedly-cutting-budgets-for-its-internal-ai-usage/ ; https://www.cfodive.com/news/apples-ai-investment-bucks-big-tech-spending-trend/873541/ ; https://www.argusmedia.com/en/news-and-insights/latest-market-news/2885886-tight-us-organic-corn-supplies-hinge-on-harvest ; https://presse.economie.gouv.fr/liberation-des-stocks-strategiques-baisse-des-prix-a-la-pompe/ ; https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817 ; https://www.covers.com/industry/seminole-tribe-sues-draftkings-florida-sports-betting-oct-8-2026 ; https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/cyberattaques-des-frigos-pirates-les-stocks-de-l-etablissement-francais-du-sang-vises_8268404.html',
 note='Bookmarks 1, 4, 9, 10, 12, 16, 18, 19, 21, 22, 24, 25. Item 17 is a duplicate of card 024. Logged under Will\'s November 5 rule on subthreshold news. Apple line to be rechecked at the close pass.',
 extra=dict(kill_strings=['Apple cuts AI infrastructure spending by 20%'])),
]
s,p=send(CARDS,'x-bookmark BM-20261106-03')
print(s);print(len(p));open('/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_bookmarks3/paths.txt','w').write('\n'.join(p)+'\n')
