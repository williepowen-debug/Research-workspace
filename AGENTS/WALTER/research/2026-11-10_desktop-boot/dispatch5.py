import sys
sys.path.insert(0, '/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-10_desktop-boot')
from dispatch_common import *

CARDS = [
dict(n=10, slug='SoftBank-Q2-net-loss-1.12T-yen-597B-power-equipment-advance-payment-loss-Ohio-Intel-prepaid-forward-loss-322B',
 title='SoftBank fiscal Q2 net loss about ¥1.12 trillion ($7B): a ¥597.2B loss on advance payments for US data-center power equipment including Pike County, Ohio, and a ¥321.9B derivative loss on the Intel prepaid forwards',
 body="""SoftBank Group fiscal Q2 (July to September 2026), released November 10 (CNBC, AOL/Reuters, mlq.ai, Benzinga, read as search summaries; SoftBank's own release not read by WALTER):

| Item | Figure | Check |
|---|---|---|
| Q2 net loss | about ¥1.12T (about $7.0B to $7.1B by outlet FX); a year earlier about +¥2.5T; Bloomberg poll expected about +¥129B | CONFIRMED by several outlets |
| Power equipment | **¥597.2B (about $3.7B) loss on advance payments for power-generation equipment for US AI data centers, including Pike County, Ohio.** Reports describe the plans as revised; SoftBank says it may get rebates of up to $2.1B on future purchases | CONFIRMED amount; "defaults on turbines" (@rdd147) is CORRECTED framing: a written-off advance payment on revised plans, not a reported default |
| Intel | ¥321.9B derivative loss on Intel-backed prepaid forward contracts; ¥270.1B valuation loss on Intel shares | CONFIRMED amounts. Zero Hedge's $7.35B raised on the prepaid forwards and banks' "rights of use" over ¥1.1T of ¥1.65T pledged Intel shares: not verified |
| Financing cost | about ¥462B, more than double a year earlier | reports |
| Bridge takeout | Zero Hedge: the $40B OpenAI bridge was repaid by September 15 with an $11.87B two-year term loan, the Intel prepaid forwards, $5B more on the Arm margin loan (about $25B, 769M Arm shares, to 2028) and bond proceeds | Bridge repaid, $11.9B term loan and $25B Arm facility match SAM's grade lines 5 and 6; 769M shares and the bond share not verified |
| Ohio | SoftBank CFO (FirstSquawk headline 08:49Z): no discussion of reducing the size of the Ohio project | headline only |

**Not verified, from @rdd147:** the remaining $6.5B of the order was for Nvidia GPUs to be redirected to Oracle. No source found.

**Why SAM is on ACTION:** SAM's results grade (bbd8974416, line 55) says Musk's turbine claim (card 20261109-005) has "no route to SoftBank's leverage found in these documents". The reported ¥597.2B loss is on power equipment for the same Ohio campus. SAM to read SoftBank's own Q2 text on it and say whether the grade line, the 15.9% loan-to-value at September 30 or the roll changes. No new study.

Others: WATT (gas-for-AI turbine lane, card 20261109-005), VULCAN (AI capex; SoftBank and Oracle), LIQUID, NEXUS, HENRY context. SoftBank 9984.T closed ¥3,872, +13.88% on November 10 in Tokyo (vendor, before these figures were widely reported in the US).""",
 sources="https://www.cnbc.com/2026/11/10/softbank-2q-earnings-tech-selloff.html ; https://www.aol.com/articles/softbank-swings-7-billion-net-063725000.html ; https://mlq.ai/news/softbank-swings-to-a-7-billion-quarterly-loss-as-a-power-equipment-write-off-and-intel-hedges-hit-earnings/ ; https://www.benzinga.com/markets/earnings/26/11/63106347/softbanks-profit-reversal-highlights-growing-financial-strain-behind-ai-expansion ; X bookmarks 2120204471137403258, 2120205029433081965 (@zerohedge), 2120076492747272315 (@FirstSquawk), 2120094282186940749 (@rdd147), 2120195088773161024 (@PolymarketMoney) ; AGENTS/SAM/research/outputs/2026-11-06_softbank/2026-11-10_RESULTS_GRADE.md (bbd8974416) ; WALTER vendor pull 22:14Z",
 action=['SAM'], info=['VULCAN', 'WATT', 'NEXUS', 'LIQUID', 'HENRY', 'PROME'],
 precedence='PRIORITY', signal_type='event', confidence=0.85, lang='reports',
 cluster='AI_INFRA_CAPEX', domain='AI_CAPEX', entities=['SoftBank Group', 'SB Energy', 'Pike County Ohio', 'Intel', 'Arm', 'OpenAI', 'Oracle', 'Nvidia'],
 note="Batch BM-20261110-04, Will-originated bookmarks, items 5, 6, 7, 8, 12 folded into one card. Recipients follow card 20261109-005 (same thread), plus PROME. ACTION SAM because SAM's committed grade states no route from the turbine claim, and the confirmed ¥597.2B loss on Ohio power equipment is decision-changing content for that line; grep of SAM, WATT and VULCAN files for 597, advance payment, power generation equipment and 321.9: 0 hits; no SAM, WATT or VULCAN commit after 12:00 ET. PRIORITY, not IMMEDIATE: no RED, REGINALD, CREED or HANS row keys on a SoftBank P&L loss, and the leverage figure is not shown to cross 25%. Rule 9 bounded check by WALTER (web search, extended): loss, power-equipment and Intel figures CONFIRMED; the turbine-default framing CORRECTED; the GPU-to-Oracle claim and the collateral rights-of-use claim INDETERMINATE.",
 extra=dict(verify_result='CONFIRMED_WITH_CORRECTED_FRAMING', event_window='open', batch='BM-20261110-04 items 5, 6, 7, 8, 12')),

dict(n=11, slug='Small-items-bookmarks-Nov-10-evening-NVDA-168.89-down-5.5pct-CoreWeave-Q3-headline-10Y-4.98-Japan-spending-minus-6.8-COR1M-BofA-claim-unconfirmed',
 title='Small items from Will\'s bookmarks, November 10 evening: Nvidia $168.89 (−5.47%), CoreWeave Q3 headline figures, the 10-year at 4.98%, Japan household spending −6.8%, Cboe COR1M note, and a Bank of America claim WALTER could not confirm',
 body="""Third-party relays from Will's X bookmarks; WALTER verified only where stated.

| Item | Claim | Owner | Check |
|---|---|---|---|
| CoreWeave Q3 | EPS −$1.27 vs −$1.55 estimated; revenue $3.66B vs $3.54B estimated (@unusual_whales, November 10 21:12Z). August guide was $3.45B to $3.60B | VULCAN | headline relay, not verified; CoreWeave's release not read. CRWV $48.73, −0.51% on the regular session (vendor, 22:14Z) |
| Nvidia | Erased its 2026 gain, down 10% on the year and 31% from the October high of $243; down about 6% today (@unusual_whales, 19:24Z) | VULCAN, HENRY | NVDA $168.89, −5.47% on November 10 (vendor, 22:14Z); 31% from $243 is consistent with that price (WALTER arithmetic); year-start level not checked |
| Bank of America | Removed Nvidia and Micron from its top stock picks (@WatcherGuru, 12:03Z) | VULCAN | INDETERMINATE: WALTER's search found no report of a removal; coverage found still lists both. MU $725.11, −1.10% (vendor) |
| 10-year | High of day 4.98%, up 11 to 12bp (@MikeZaccardi, 14:39Z) | BOND, HENRY | ^TNX 4.98 on November 10 (vendor, 22:14Z) |
| Japan | September household spending −6.8% YoY vs −3% forecast, −3.1% prior (@financialjuice, November 9 23:30Z) | SAM | not verified; MIC release not read |
| Implied correlation | Cboe Macro Volatility Digest, November 9: implied vols fell across most asset classes last week; skew and convexity bid on the sell-off; COR1M peaked at about 22% on Thursday, "highly unusual" for that small a rise | VIOLET | VIOLET's ledger has COR1M 22.84 on November 5 and 12.35 on the November 10 print, consistent |
| VIX | Two straight days above 27, then back-to-back closes under 20: the third time in history (@OddStats, 21:36Z; second half of the thread not read) | VIOLET | not verified; small sample |

No directed ask; owners log.""",
 sources="X bookmarks 2120263362047287516, 2120236047791689993, 2120125152898003240, 2120164357740929436, 2119935736426242105, 2119896073560834060, 2120269470862082304 ; WALTER vendor pulls 22:14Z (FORGE fetch.py) ; BofA check: https://letsdatascience.com/news/bank-of-america-favors-nvidia-amd-on-ai-spending-a9c6d583 , https://www.webull.com/news/15669094052463616 ; CoreWeave guide: https://siliconangle.com/2026/08/11/coreweave-coasts-solid-earnings-beat-sending-stock-higher-hours/ ; AGENTS/VIOLET/STATUS.md COR1M rows",
 action=[], info=['VULCAN', 'HENRY', 'BOND', 'SAM', 'VIOLET', 'PROME'],
 precedence='ROUTINE', signal_type='context', confidence=0.6, lang='reports',
 cluster='AI_INFRA_CAPEX', domain='AI_CAPEX', entities=['CoreWeave', 'Nvidia', 'Micron', 'Bank of America', 'US 10-year', 'Japan household spending', 'COR1M', 'VIX'],
 note="Batch BM-20261110-04, Will-originated bookmarks (read in full). Rows by owner per REGISTRY Domain: AI_CAPEX VULCAN, index mechanics HENRY, rates BOND, Japan SAM, vol regime VIOLET. CoreWeave: VULCAN's own Q3 grade is the routing item carried in LAST_COMPLETION; this card relays the headline only and does not stand in for it. Bank of America: Rule 9 bounded check, INDETERMINATE. Prices are WALTER vendor pulls at 22:14Z, after the regular close.",
 extra=dict(event_window='open', batch='BM-20261110-04 items 1, 2, 3, 4, 9, 10, 11')),
]

stamp, paths = send(CARDS, "X bookmarks staged 2026-11-10T22:13:24Z, Will-added after the full closeout (BM-20261110-04)")
print(stamp)
print('\n'.join(paths))
