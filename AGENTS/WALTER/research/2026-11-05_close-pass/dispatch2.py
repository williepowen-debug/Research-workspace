import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[
dict(n=57,slug='CORRECTION-VIX-finished-28.17-not-26.86-VVIX-135',
 title='CORRECTION to card 055: VIX finished about 28.17, not 26.86; VVIX 135.38; the 16:05 read predated the final prints',
 action=[],info=['REGINALD','LIQUID','RED','HENRY','VIOLET','VULCAN','BROCK','GIBBS','TERRY','NEXUS','MIDAS','PROME'],precedence='IMMEDIATE',signal_type='correction',confidence=0.8,lang='vendor post-close reads',
 cluster='POSITIONING_VALUATION',domain='MARKET_VOL',entities=['VIX','VIX9D','VIX3M','VVIX'],
 body='''Card 055 used a 16:05 ET vendor read. VIX-family indexes keep printing to about 16:15 ET, so it was stale. Vendor 16:22 ET: VIX 28.17 (+69.6%, +11.56 points), VIX9D 32.69, VIX3M 25.51, VVIX 135.38. Still not Cboe history, which had not posted at 21:23Z; certified on the morning pass.

Stocks unchanged: S&P 7,353.73 (−4.36%), QQQ 647.05, SMH −11.21%, KRE −2.47%. WAL 75.88. HYG 77.28 (−0.31%).

VIX is under 30 and the safety-net line; +5 was already FLASHed. Front of the curve is more inverted than 055 said: VIX9D/VIX3M about 1.28.

So the vol leg finished worse than 055 reported. Everything else in 055 stands. No ask.''',
 sources='AGENTS/WALTER/research/2026-11-05_close-pass/tape-1622.json',
 note='WALTER error of timing: read a live index before its final print.',
 extra=dict(corrects='SIG-W-20261105-055',corrects_direction='STRENGTHENS vol stress — VIX about 28.17 and VVIX 135.38 at the final print',kill_strings=['VIX 26.86'])),
dict(n=58,slug='Saudi-Yanbu-danger-alert-Houthi-missile-intercepted-toward-Medina',
 title='Saudi civil defense warns of danger at Yanbu; coalition intercepts Houthi missile toward Medina; no hit on oil facilities reported',
 action=['FALCON','BRENT'],info=['HAWK','SAM','HENRY','RED','TERRY','PROME'],precedence='IMMEDIATE',signal_type='context',confidence=0.7,
 cluster='IRAN_HORMUZ',domain='GEOPOL_ENERGY',entities=['Yanbu','Medina','Houthi','Saudi-Arabia','Sharurah'],
 body='''November 5, reports from about 09:44 GMT; collector headlines missed by the morning passes, surfaced in the evening intake. Search summaries of Reuters-relay pieces; bodies unread.

Saudi civil defense warned of potential danger near Yanbu, the kingdom's main Red Sea export hub. Minutes later coalition spokesman Turki al-Malki said a Houthi ballistic missile toward the Medina region was intercepted and destroyed. Alerts also went to Sharurah. Houthis called the Medina claim false and said "Our operations target only its oil facilities and military bases"; no claim of a Thursday attack on Saudi Arabia.

⛔ INTERCEPTED is not STRUCK. No damage, loading halt or shutdown reported. A warning is not a closure. Link between the two events is unclear.

Why it matters: Yanbu is the route Saudi crude uses to avoid Hormuz, so any real outage matters more than the Gulf claims. It was the FAL-05 route in September.

Brent January 98.44 (+4.04%), vendor, not a settle; no source read ties price to this.

ACTION FALCON, BRENT: check loadings; grade at your own letter.''',
 sources='https://houseofsaud.com/houthi-missile-medina-yanbu-nov5/ ; https://ca.news.yahoo.com/houthi-missiles-fired-medina-intercepted-110722626.html ; https://www.24newshd.tv/05-Nov-2026/saudi-coalition-intercepts-missile-fired-medina-warning-issued-yanbu ; Research-Intake data/2026-11-05/news.json',
 note='INTERCEPTED-to-STRUCK and date guards read. Sweep clock unchanged. Latency: same-day headlines sat behind the headline filter; routed about 12 hours late.',
 extra=dict(narrative_channel='houthi')),
dict(n=59,slug='Cable-One-Q3-431.8M-net-loss-impairments-covenant-language-MBI',
 title='Cable One Q3: $431.8M net loss on $358.0M impairments, revenue −11.7%, cash $674.8M, debt $3.55B; covenant warning tied to financing',
 action=['BROCK'],info=['LIQUID','RED','PROME'],precedence='PRIORITY',signal_type='research',confidence=0.95,lang='confirms',
 cluster='PC_STRESS',domain='PRIVATE_CREDIT',entities=['CABO','Cable-One','MBI','Mega-Broadband'],
 body='''8-K Exhibit 99.1, November 5, accepted 21:18Z, read at SEC. Revenue $332.2M (−11.7%), net loss $431.8M versus income $86.5M, adjusted EBITDA $159.8M (−20.8%), operating cash flow $92.6M (−40.8%). Charges: $358.0M asset impairments, $39.7M put option loss, $20.0M MBI equity impairment, all non-cash, net of tax.

Cash $674.8M; gross debt $3.55B.

MBI: the company says it has sufficient liquidity to pay the purchase price in full if the October 9 restraining order is dissolved, but intends to coordinate payment with financing that addresses some debt maturities, with "no assurances".

Covenants: compliant at September 30 and expects 12 more months, but "may not be able to maintain compliance if operating performance deteriorates or market conditions worsen, particularly if it does not consummate any financing". A breach without waiver could allow acceleration.

Management cites best residential data subscriber results in seven quarters.

ACTION BROCK: DOCKET L876 read; the 10-Q is due by November 9.''',
 sources='https://www.sec.gov/Archives/edgar/data/1632127/000163212726000036/a2026q3-pressrelease.htm',
 note='Primary, release only; no call or 10-Q read.'),
dict(n=60,slug='Evening-intake-Nano-Banc-order-ended-Russia-petrochemical-ban-memory-costs-Abrigo-held',
 title='Evening intake: Fed ends Nano Banc action; Russia bans petrochemical feedstock exports; memory costs hit Qualcomm and Arm; Abrigo held by CYPHER',
 action=['CREED','BRENT','VULCAN'],info=['REGINALD','GIBBS','OSPREY'],precedence='ROUTINE',signal_type='context',confidence=0.55,
 cluster='MISC',domain='OIL_ENERGY',entities=['Nano-Banc','Abrigo','Sageworks','QCOM','ARM'],
 body='''November 5 collector, headlines unless named.

CREED: Fed terminated its enforcement action with Allegiant United, Nano Financial and Nano Banc. Nano failed September 25; housekeeping, not news on recoveries.

BRENT: LIGA: after gasoline and diesel, Russia bans petrochemical feedstock exports. Energy Intelligence: Russia ramps up diesel exports to the US, denies glitches; date unread. WAM: diesel ban to late January 2027, already seen. StoneX: heating oil supply exposed to a single refinery outage.

VULCAN: Yahoo and TradingView: Qualcomm and Arm fell on memory pricing and supply hitting handset royalties. Same memory squeeze as card 045, from the buyer side.

Abrigo/Sageworks: 3-day outage October 30–November 2 and confirmed data incident, American Banker. CYPHER already holds it as CYB-INC-060 and briefed REGINALD, LIQUID, GIBBS, PROME. Recorded so the BOARD has it. Not tied to Arkéa's provider.

Microsoft 8-K: director Walmsley not standing for re-election; no signal.''',
 sources='Research-Intake data/2026-11-05/news.json ; https://www.sec.gov/Archives/edgar/data/789019/ ; AGENTS/CYPHER/STATUS.md',
 note='18 intake breaches dispositioned; Ueno and Boise alerts folded, nothing new. No link between Abrigo and Arkea established; the sentence states that.'),
]
print(send(CARDS,'WALTER close pass and evening intake')[0])
