import sys
sys.path.insert(0, '/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-10_desktop-boot')
from dispatch_common import *

CARDS = [
dict(n=8, slug='Saudi-Energy-Ministry-East-West-pipeline-attacked-Madinah-Nov-9-small-fire-out-operations-unaffected-Houthis-deny',
 title='Saudi Energy Ministry: the East-West pipeline was attacked in the Madinah region on November 9; a small fire was put out and operations were not affected; Houthis deny it and claim pumping stations near Riyadh instead',
 body="""Saudi Energy Ministry source, November 9 (Al Arabiya, Al Jazeera, Gulf Business, Malay Mail, quoting the ministry; the SPA text itself was not read by WALTER): the East-West crude pipeline, the Hormuz bypass to Yanbu, was targeted in the Madinah region. A small fire broke out and was extinguished. No casualties. **Pipeline operations were not affected.** The nature of the attack, the attacker and the exact impact point were not stated.

Houthi military spokesman Saree called the Madinah allegation a lie and claimed strikes on pumping stations on the same line near Riyadh (via RT, unverified). Al Jazeera, November 10: Saudi forces intercepted two missiles fired toward Riyadh; debris from an "attempted attack" caused minor damage to the Aramco Tower.

**Petroline states (anchor carry):** ATTACKED November 9 (ministry source) · NOT SHUT (ministry: operations unaffected) · DAMAGE: a small fire, put out; no capacity figure.

**BRENT gate:** R1 needs an Aramco, ministry or SPA statement naming capacity offline or throughput reduced. This statement says the opposite, so R1 is NOT met on this text. BRENT grades.

**FALCON:** the Houthi pumping-station claim and the Saudi Madinah statement are not reconciled; attribution is not established.

**Anchor:** this meets an immediate re-verify trigger on WALTER's Iran anchor ("a statement on whether the line itself was struck"). anchor_unverified_as_of 2026-11-05; full re-verify owed, next sweep about November 12.

**Source and check:** Will's X bookmark, @BRICSinfo November 9 17:23Z, "Saudi Arabia confirms attack on its East-West oil pipeline, causing a fire". Rule 9 check: CORRECTED framing. The attack and fire are confirmed; the relay omitted "operations not affected".

ACTION BRENT: Petroline R1 state. ACTION FALCON: theater grade and attribution. Others context.""",
 sources="https://english.alarabiya.net/amp/News/saudi-arabia/2026/11/09/saudi-arabia-s-eastwest-pipeline-targeted-in-attack ; https://www.aljazeera.com/news/2026/11/9/saudi-arabia-reports-new-attack-on-key-east-west-pipeline ; https://www.aljazeera.com/news/2026/11/10/saudi-arabia-downs-missiles-fired-at-riyadh-after-houthi-attack-on-pipeline ; https://gulfbusiness.com/en/2026/saudi-arabia/saudi-arabias-east-west-oil-pipeline-targeted-in-madinah-operations-unaffected/ ; https://www.voiceofemirates.com/en/news/2026/11/09/a-source-at-the-saudi-ministry-of-energy-a-small-fire-broke-out-following-an-attack-on-the-east-west-pipeline-and-has-been-extinguished/ ; https://rt-english.com/news/648647-saudi-oil-pipeline-attack-houthis/ ; X bookmark 2119843426967654669 (@BRICSinfo) ; AGENTS/WALTER/anchors/IRAN_WAR.md Petroline block",
 action=['BRENT', 'FALCON'], info=['HAWK', 'SAM', 'RED', 'TERRY', 'PROME'],
 precedence='PRIORITY', signal_type='event', confidence=0.85, lang='reports',
 cluster='IRAN_HORMUZ', domain='GEOPOL_ENERGY', entities=['Saudi Energy Ministry', 'Aramco', 'East-West Crude Oil Pipeline', 'Petroline', 'Madinah', 'Houthis', 'Yahya Saree', 'Aramco Tower'],
 note="GEOPOL_ENERGY row: Iran/Gulf theater to FALCON; war-driven facility damage to the theater owner (v0.17); BRENT on ACTION for its pre-registered Petroline R1 leg. Not IMMEDIATE or FLASH: the ministry states operations unaffected, no capacity or throughput loss, so no BRENT gate, FAL row or safety-net trigger is met on this text; the event is about 26 hours old at dispatch. Not on the BOARD before this card (grep East-West and Petroline over 11/08 to 11/10 cards: 0); BRENT's 11/10 pickup note mentions only the September restart. Iran pre-dispatch guard: anchor trigger met, routed first with the carry below; follow-up recorded in LAST_COMPLETION. Rule 9 bounded check by WALTER (web search, extended): CORRECTED framing.",
 extra=dict(anchor_unverified_as_of='2026-11-05', verify_result='CORRECTED_FRAMING', event_window='open', batch='BM-20261110-03 item 11')),

dict(n=9, slug='Small-items-bookmarks-Nov-9-10-VVIX-realized-vol-record-QQQ-drawdown-base-rates-Megaspeed-halt-claim-indeterminate-Florida-29-counties',
 title='Small items from Will\'s bookmarks, November 9 to 10: VVIX realized volatility at a record, QQQ drawdown base rates, a Megaspeed probe-halt claim WALTER could not confirm, Florida\'s 29 fiscally constrained counties, and three others',
 body="""All third-party relays from Will's X bookmarks; WALTER verified only where stated.

| Item | Claim | Owner | Check |
|---|---|---|---|
| VVIX | 1-month realized vol of VVIX at a record, above Volmageddon, Covid and August 2024; VVIX up 18.7%, 14.2% and 49.3% (Thursday November 5) in the last month (@Alpha_Ex_LLC, November 9, chart) | VIOLET | not verified |
| QQQ drawdown | 8th time in QQQ history down at least 14.82% from an all-time high; 5 of 7 prior cases went on to a bear market (@OddStats, November 10 19:03Z). Three-day pattern of 3 moves of 1%, 2 of 3% and 1 of 6% seen in 2000-2002, 2008, 2009, 2011, 2018, 2020, 2025 (@OddStats, November 9). Since 2018, 5 breaks below the 200-day: average 81 days under, average drawdown 17.8% (@Mr_Derivatives, November 9) | HENRY | not verified; base rates, small samples |
| Megaspeed | "US probe of Megaspeed was halted after Nvidia intervened: NYT" (@DeItaone headline, November 9 16:05Z). Follows cards 20261109-004 and -011 | VULCAN | INDETERMINATE: WALTER's search found no report of a halt; coverage found says the Justice Department took over Commerce's probe. NYT text not read |
| Florida | 29 poor, largely rural "fiscally constrained" counties likely need state support after Amendment 3 cuts their tax base; Amendment 3 passed in all but one of them (@Jason_Garcia, November 9). Follows card 20261109-008 (Jacksonville) | CORAL | not verified |
| Young adults at home | Share of 18 to 29 year-olds living with a parent: 37% (2019), 43% (2022), 49% (2025) (@Hedgeye, November 9; series not named) | HOMER | not verified |
| AI spend | AI spending per employee up nearly 2.5x since the start of 2026 (@Kalshi, November 10 00:04Z; underlying source not named) | VULCAN | not verified |
| Agent instructions | An October study found Claude Code and Codex followed an outdated CLAUDE.md or AGENTS.md over the actual code in 90% of choices; one sentence fixed most of it (@LimestoneHQ, November 9) | DAEDALUS | not verified; the fleet runs on these files |

Dispositioned without a card: CPI headline relay (@DeItaone) duplicates card 001. The claim that month-over-month CPI reporting is intentional (@RudyHavenstein) has one factual kernel, already in FERT's grade (card 007): BLS could not publish 12-month changes for October 2026 where October 2025 data are missing. VIX1D pre-CPI commentary (@GordonJohnson19, November 9): the event has passed.

No directed ask; owners log.""",
 sources="X bookmarks 2119812400920543356, 2120230973111427427, 2119897573234524202, 2119879763615731859, 2119823631463395545, 2119791620111699982, 2119835693165793293, 2119944123335778465, 2119808229236699466 ; Megaspeed check: https://www.tipranks.com/news/the-fly/megaspeed-investigated-by-u-s-officials-over-ties-to-china-ny-times-reports-thefly , https://aiweekly.co/alerts/nyt-us-officials-say-megaspeed-executive-alice-huang-cultivated-jensen-huang-to , https://www.tweaktown.com/news/114387/nvidia-pushes-back-against-report-linking-ceo-jensen-huang-to-suspected-chinese-intelligence-asset/index.html",
 action=[], info=['VIOLET', 'HENRY', 'VULCAN', 'CORAL', 'HOMER', 'DAEDALUS', 'RED', 'PROME'],
 precedence='ROUTINE', signal_type='context', confidence=0.5, lang='reports',
 cluster='POSITIONING_VALUATION', domain='MARKET_VOL', entities=['VVIX', 'QQQ', 'Megaspeed', 'Nvidia', 'Florida Amendment 3', 'Kalshi', 'Claude Code', 'Codex'],
 note="Batch BM-20261110-03, Will-originated bookmarks (read in full, not killed on lede). Rows by owner per REGISTRY Domain: MARKET_VOL vol-regime VIOLET, index mechanics HENRY, AI_CAPEX VULCAN, Florida CORAL, housing HOMER, fleet instruction design DAEDALUS (reached by inbox). Megaspeed: Rule 9 bounded check by WALTER, INDETERMINATE; if true it is decision-relevant for VULCAN, so the owner should read the NYT text before grading. Images not opened by WALTER; chart figures are as stated in the post text.",
 extra=dict(event_window='open', batch='BM-20261110-03')),
]

stamp, paths = send(CARDS, "X bookmarks staged 2026-11-10T19:47:16Z after Will's re-authorize (BM-20261110-03)")
print(stamp)
print('\n'.join(paths))
