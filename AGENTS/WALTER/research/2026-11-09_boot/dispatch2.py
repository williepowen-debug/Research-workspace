import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-09_boot')
from dispatch_common import *
TAPE="Vendor intraday 10:51 ET November 9, not closes"
CARDS=[
dict(n=4,slug='Nvidia-down-about-4pct-while-QQQ-up-3pct-on-Huang-spy-report-follow-through-Citi-cuts-US-equities-and-tech-to-Neutral',
 title='Nvidia down about 4% while QQQ is up about 3% on the Jensen Huang spy-report story; Citi cuts US equities and global tech to Neutral',
 body=f"""{TAPE}: NVDA 179.40 (−3.88%), QQQ 676.62 (+3.13%), S&P 500 7,531.12 (+2.09%), CRWV 49.82 (+7.37%). Nvidia is lagging the index by about 7 points on a day the AI tape is up.

**The story (secondaries; WALTER did not read the NYT original):** the New York Times reported around October 29 to 30 that US intelligence suspected a Chinese businesswoman, Alice Huang (Huang Le), tied to Singapore data-centre firm Megaspeed, of being a Chinese asset who tried to cultivate Jensen Huang. Three House Republican committee chairs asked Huang for a closed-door briefing (UNI, November 6). Nvidia calls the Megaspeed contacts routine and says the chip-diversion allegations were investigated and dismissed; China calls the reports groundless. A Polymarket post (November 7) and a Kobeissi Letter post (November 9, "−5% premarket, −$225B") escalated it to a "romantic relationship"; that wording rests on unnamed sources and is unconfirmed. What changed over the weekend to move the stock today is not established.

**Citi (via DeItaone, November 9, note unread):** US equities, global tech and European tech cut to Neutral on weakening AI sentiment; Nasdaq could fall about 5% more before positioning turns decisively bearish; turns bullish on Europe.

Context, not a forecast: an @OddStats post says QQQ's November 5 −6% day is followed by deeper drawdowns historically if QQQ does not regain 683.65 by Tuesday's close; vendor QQQ is 676.62 now.

ACTION VULCAN: the Nvidia single-name read and any export-control or key-person channel. ACTION HENRY: the Citi call and the index tape. No new study.""",
 sources="X bookmarks 2119717185492775004 (@KobeissiLetter), 2118949821037912517 (@Polymarket), 2119763850325086357 (@DeItaone), 2119806908693627130 (@OddStats) ; https://www.scmp.com/tech/tech-war/article/3372743/china-dismisses-us-report-suspected-spy-targeting-nvidia-ceo-jensen-huang-groundless ; https://www.eenewseurope.com/en/jensen-huang-spy-plot-nvidia-china/ ; https://www.uniindia.com/world/us-gop-nvidia-ceo-china-spy-links/238184 ; https://www.wdbo.com/news/national/nvidia-denies-report-that-its-ceo-was-allegedly-targeted-chinese-spy-plot/UAKCTO3VIM7RZLMU5IY746T5VU/?outputType=amp ; WALTER vendor pull 15:51Z",
 action=['VULCAN','HENRY'],info=['VIOLET','ZHAO','RED','PROME'],precedence='PRIORITY',signal_type='context',confidence=0.6,lang='reports',
 cluster='AI_INFRA_CAPEX',domain='AI_CAPEX',entities=['Nvidia','Jensen Huang','Alice Huang','Megaspeed','Citi','QQQ','CoreWeave'],
 note="Will asked whether bookmarks were processed; X bookmark batch read 15:50Z. Prices from WALTER's vendor pull. NYT and Citi originals unread."),
dict(n=5,slug='SoftBank-down-4-2pct-in-Tokyo-before-results-Musk-claims-SoftBank-is-defaulting-on-turbine-orders-unverified',
 title='SoftBank down 4.2% in Tokyo on November 9, a day before results; Musk claims SoftBank is "defaulting" on turbine orders (November 6, unverified)',
 body="""SoftBank Group (9984.T) 3,400 yen, −4.2% on the November 9 Tokyo session (vendor). Results November 10, 15:30 JST (01:30 ET).

**Musk's claim, November 6 on X:** "SoftBank is defaulting on its turbine orders." No supplier, order, amount or project named; no confirmation from SoftBank or any turbine maker found. Secondaries report SoftBank shares fell 10.83% in Tokyo after the post and tie the turbines to SB Energy's roughly 9.2 GW Ohio gas plant; that link is reported, not confirmed. Musk runs xAI, a competitor for turbines and AI capacity, and has doubted SoftBank's Stargate funding since January 2025. Turbine orders are not debt: this is not a bond default claim.

Why it may matter: card 20261106-041 carries SAM's SoftBank leverage estimates (22.1% or 24.2% loan-to-value at the dated inputs); an equity fall moves loan-to-value against SoftBank, and a stranded turbine order would touch WATT's gas-for-AI lane alongside card 002's Anthropic deal.

ACTION SAM: read against the leverage estimate before tomorrow's results. No new study.""",
 sources="X bookmark 2119067457717412198 (@zerohedge) ; https://officechai.com/ai/softbank-is-defaulting-on-its-turbine-orders-claims-elon-musk/ ; https://beincrypto.com/elon-musk-softbank-defaulting-turbine-orders/ ; https://www.mitrade.com/insights/news/live-news/article-3-2238057-20261106 ; WALTER vendor pull 15:51Z",
 action=['SAM'],info=['VULCAN','WATT','NEXUS','LIQUID','HENRY'],precedence='PRIORITY',signal_type='context',confidence=0.5,lang='claims',
 cluster='AI_INFRA_CAPEX',domain='AI_CAPEX',entities=['SoftBank Group','Elon Musk','xAI','SB Energy','Stargate'],
 note="X bookmark; claim dated November 6 by three secondaries. Musk's post itself not read by WALTER. SoftBank 10.83% fall is a secondary's figure."),
dict(n=6,slug='US-demands-Iraq-close-Iran-border-crossings-Bessent-reportedly-presses-China-on-Tehran-Eisenkot-asked-to-form-Israeli-government',
 title='US reportedly demands Iraq close all but two Iran border crossings under Task Force Iron Gate; Bessent reportedly pressed China to lean on Tehran; Israel\'s president picks Eisenkot to form a government',
 body="""Weekend items from X bookmarks; WALTER did not read the originals. FALCON owns the theater, HAWK the scenarios.

- **Iraq border crossings, November 7:** Iraq's foreign minister told Al Jazeera the US formally demanded Iraq close all its border crossings with Iran except two, with an Iraqi official saying the US threatened sanctions (via @HormuzLetter). Follows Task Force Iron Gate (card 20261107-001). Not verified at Al Jazeera.
- **Bessent and China, November 8:** a US official told the Washington Post that Treasury Secretary Bessent formally pressed China to use its influence with Tehran to end the war, with Trump's backing (via @HormuzLetter). WALTER could not find the Post article; unverified. Bessent made similar public calls in May and August.
- **Israel, November 7 (AP):** President Herzog picked opposition candidate Gadi Eisenkot to form a new government, a setback for Netanyahu. Theater bearing is HAWK's and FALCON's call.
- **Jask and Qeshm, November 7:** an X account's "US jet struck SAM launchers" line conflicts with Iranian state TV saying the blasts were not confirmed strikes; FALCON graded it on card 20261108-002 as not a US strike day. No change here.

ACTION FALCON: the Iraq land-route item against the blockade and FAL rows. No new study.""",
 sources="X bookmarks 2119119041419714656, 2119476320652411214, 2119166955974262986 (@HormuzLetter), 2119157583533515245 (@AP), 2119161693674549308 (@DeItaone) ; https://apnews.com/article/israel-elections-75934bfce1f2f2e43e1823de3761b12d",
 action=['FALCON'],info=['HAWK','BRENT','ZHAO','RED','PROME'],precedence='PRIORITY',signal_type='context',confidence=0.55,lang='reports',
 cluster='IRAN_HORMUZ',domain='GEOPOL_ENERGY',entities=['Iraq','Task Force Iron Gate','Scott Bessent','China','Gadi Eisenkot','Washington Post','Al Jazeera'],
 note="Iran pre-dispatch guard: anchor sweep 11/05, next 11/12; mediated not bilateral. X relays only.",
 extra=dict(anchor_unverified_as_of='2026-11-08')),
dict(n=7,slug='Millennium-shuts-two-more-credit-pods-Binance-CFO-resigns-after-hack-private-credit-defaults-claim-unsourced',
 title='Millennium reportedly shuts two more credit trading pods (Abacove, Twin Lights); Binance CFO resigns after the hack; "private-credit defaults highest since 2008" is unsourced',
 body="""Small credit and plumbing items logged under WQ-622; nothing moves a score. X relays; originals unread.

| Item | Source, date | Note |
|---|---|---|
| Millennium closes credit pods Abacove and Twin Lights, days after pulling money from Axebrook; four named managers out | @junkbondanalyst, November 6, screenshot of a news report | Adds to card 20261106-008 hedge-fund item; multi-strategy de-risking in credit |
| Binance CFO resigns | @Nostre_damus, November 7, link only | Follows the $6.3B hack and Fed/OCC calls to banks (card 20261105-046); the "exchanges are going to collapse" line is commentary |
| "Private credit defaults hit the highest level since 2008, 40–50% tied to real estate" | @jonbrooks, November 8 | No index or source named; not usable as a figure |
| 10x-levered CLOs buying CoreWeave senior unsecured notes | @anchovycapital, November 6 | Same class as LIQUID's gate-069 and card 20261106-013; commentary |

ACTION LIQUID: Millennium and Binance against your plumbing lens. No new study.""",
 sources="X bookmarks 2118745842064703987, 2119204044564787517, 2117406534024253536, 2119414635053113810, 2118730605693370422",
 action=['LIQUID'],info=['BROCK','CYPHER','SHADE','HENRY'],precedence='ROUTINE',signal_type='context',confidence=0.4,lang='claims',
 cluster='PC_STRESS',domain='FUNDING_LIQUIDITY',entities=['Millennium','Abacove','Twin Lights','Axebrook','Binance','CoreWeave'],
 note="X bookmarks; relays only, not verified at a primary."),
dict(n=8,slug='Small-items-Japan-financial-cyber-shutdown-option-Berkshire-yen-bond-Union-Pacific-rate-threat-Jacksonville-300M-hole-El-Nino-jet',
 title='Small items: Japan may let financial firms shut systems for up to a month as a cyber defence (date unverified); Berkshire yen bond; Union Pacific CEO rate-hike threat; Jacksonville $300M budget hole; El Niño jet-stream outlook',
 body="""Logged under WQ-622; nothing moves a score. X relays; originals unread.

| Item | Source, date | Owner |
|---|---|---|
| Nikkei: Japanese financial services "may choose to shut down", a month-long halt "possible" as a cyber defence against AI-enabled attacks | @InterceptorNews, stamped November 9 | CYPHER, SAM. ⚠️ WALTER found the FSA and Bank of Japan draft on voluntary suspension reported in May 2026; a November Nikkei piece is not confirmed, so this may be a re-surfaced story |
| Berkshire Hathaway hires banks for its first yen bond since April | Bloomberg, November 9 | SAM |
| Union Pacific's CEO, in unsealed video, threatens customers with a 3–4% rate hike if they keep opposing the Norfolk Southern merger | @Breaking911, November 7 | ISHM |
| Jacksonville faces a $300M budget hole after Florida Amendment 3; police and fire off the table for cuts | Action News Jax, November 7 | CORAL; adds a city figure to card 20261105-036 |
| El Niño expected to fuel a record subtropical jet this winter, raising storm risk across the western, southern and eastern US | via Polymarket, November 7 | AEOLUS |

ACTION CYPHER: the Japan item, promote only on a primary. ACTION CORAL: the Jacksonville figure. No new study.""",
 sources="X bookmarks 2119649663582142556, 2119603414011174937, 2119201854257233944, 2118862304385142917, 2119085414124335308 ; https://threatcluster.io/cluster/japan-considers-financial-system-shutdowns-due-to-ai-cyber-r-21d4cf3c ; https://www.law360.com/mlex/artificial-intelligence/articles/2480955/japan-s-financial-sector-urged-to-prepare-for-ai-powered-cyberattacks",
 action=['CYPHER','CORAL'],info=['SAM','ISHM','AEOLUS','HOMER'],precedence='ROUTINE',signal_type='context',confidence=0.4,lang='claims',
 cluster='MISC',domain='CYBER',entities=['Japan FSA','Bank of Japan','Berkshire Hathaway','Union Pacific','Norfolk Southern','Jacksonville'],
 note="X bookmarks; Japan item's date unverified, may be the May 2026 draft re-surfaced."),
]
s,p=send(CARDS,'X bookmarks 2026-11-09 batch (35 items)')
print(s)
open('/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-WALTER/517172e0-69dd-46b8-8670-ebceccb432b5/scratchpad/paths2.txt','w').write('\n'.join(p)+'\n')
print(len(p))
