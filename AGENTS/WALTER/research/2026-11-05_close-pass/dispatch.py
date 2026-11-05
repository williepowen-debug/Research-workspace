import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[
dict(n=55,slug='November-5-close-S&P-down-4.4-percent-VVIX-over-120-credit-ETFs-calm-WAL-under-78'.replace('&',''),
 title='Close read: S&P −4.4%, Nasdaq-100 −6.4%, worst into the bell; VVIX 131 over 120; credit ETFs still calm; WAL 75.89',
 action=['REGINALD','LIQUID','RED'],info=['HENRY','VIOLET','VULCAN','BROCK','GIBBS','TERRY','NEXUS','MIDAS','PROME'],precedence='IMMEDIATE',signal_type='context',confidence=0.8,lang='vendor post-close reads',
 cluster='POSITIONING_VALUATION',domain='MARKET_VOL',entities=['SPX','NDX','QQQ','SMH','VIX','VVIX','WAL','KRE','HYG','MU','AMD'],
 body='''Answers FLASH 016 and 017. Vendor read 16:05 ET, NOT official closes; Cboe history and FRED not yet posted.

S&P 7,353.73 (−4.36%), Nasdaq-100 −6.36%, QQQ 647.05 (−6.49%), SMH −11.21%, IWM −4.58%, RSP −2.89%. NVDA −9.26%, AMD −17.26%, MU −17.46%. S&P sits about 0.4% above HENRY's 200-day near 7,323. From 15:05 ET: QQQ −1.09%, SMH −2.2%; consistent with close-driven selling (054), not proof.

Vol: VIX 26.86, VIX9D 30.12, VIX3M 24.91, front inverted. VVIX 131.46 is over VIOLET's 120 line; VIOLET's session closed, its grade owed.

Did 016 and 017 hold? Equities and vol worsened. Banks confirmed: GS −6.44%, MS −5.93%, JPM −4.24%, KRE −2.47%. Credit proxies held calm: HYG −0.28%, JNK −0.28%, LQD +0.13%, BKLN −0.63%. Cash HY unknown until tomorrow.

ACTION REGINALD: WAL 75.89 under 78 is a re-entry; grade the close. LIQUID: Gate 069 L4, vendor IREN −16.95%, NBIS −14.94%, APLD −14.69%. RED: if VIXCLS ≥18, FT-06 exit run starts. HY ≥357 would trip +25 bp.''',
 sources='AGENTS/WALTER/research/2026-11-05_close-pass/tape-1604.json ; FRED and Cboe history not yet posted at 21:07Z',
 note='Closes read before certification on purpose, so owners have it tonight; certified follow-up on the November 6 morning pass. MIDAS info: S&P is below the 7,757.17 L819 level. Levered ETF read is arithmetic on vendor prints only.'),
dict(n=56,slug='Iranian-official-says-nuclear-proposal-sent-to-US-via-Qatar-seven-demands-first',
 title='Reuters: Iranian official says a nuclear proposal went to the US via Qatar, for discussion only after seven demands; no US confirmation',
 action=['FALCON'],info=['BRENT','HAWK','SAM','NEXUS','RED','PROME'],precedence='IMMEDIATE',signal_type='context',confidence=0.6,
 cluster='IRAN_HORMUZ',domain='GEOPOL_ENERGY',entities=['Iran','Qatar','Rezaei','Vance'],
 body='''Middle East Eye, November 5 20:17 GMT, citing Reuters: "Iran has sent the US a nuclear proposal via Qatar, which is to be discussed only after Washington meets its seven demands, a senior Iranian official told Reuters on Thursday." The official adds that Washington is reviewing it. Reuters body unread. Seven demands not listed. No US response found.

NYT, November 5, via search summary: Iran reviewing proposals from mediators on its nuclear program; Doha talks continue; Rezaei privately open to discussing the nuclear issue. Another report says Vance proposed direct talks in a letter; unverified.

Read it carefully. Anonymous Iranian official, one side, mediated, not bilateral. A precondition list is not an agreement. No signed text, date, reopening or US acceptance. The Iran anchor's dated-framework trigger is not met.

Brent January 98.57 (+4.17%), vendor, not a settle; "Oil rises over $2" and fresh tanker claims came the same day; no source ties price to this.

Held out, unverified: "Iran opens Hormuz to China and India" (OilPrice).

ACTION FALCON: grade against ladder item 5 at your own letter.''',
 sources='https://www.middleeasteye.net/live-blog/live-blog-update/iran-sent-nuclear-proposal-us-qatar-senior-iranian-official-tells ; https://www.jpost.com/middle-east/iran-news/article-914000 ; https://www.i24news.tv/en/news/middle-east/iran-eastern-states/artc-iran-weighs-nuclear-proposals-as-qatar-pushes-to-avert-renewed-us-strikes-report',
 note='Bounded check, sweep clock unchanged. Guards read for this dispatch: mediated-not-bilateral, POTUS channel, ceasefire kill word, negotiating-not-established. No US official voice found.',
 extra=dict(narrative_channel='mfa')),
]
print(send(CARDS,'WALTER close pass / vendor post-close / Rule 9 style bounded check')[0])
