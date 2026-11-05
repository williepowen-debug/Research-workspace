import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
HY='332'
CARDS=[
dict(n=9,slug='HY-332-CCC-1297-November-4-VIXCLS-resets-FT-06-exit-run',
 title='HY 332 and CCC 1,297 on November 4, both tighter; VIXCLS 16.61 resets the RED-FT-06 exit run',
 action=['RED'],info=['LIQUID','VIOLET'],precedence='PRIORITY',signal_type='context',confidence=0.9,lang='confirms',
 cluster='BANK_COLLATERAL',domain='FUNDING_LIQUIDITY',entities=['RED-FT-02','RED-FT-06','RED-FT-07','RED-FT-10','REG-T-03','REG-T-04','BAMLH0A0HYM2','BAMLH0A3HYC','VIXCLS'],
 body="""FRED, November 4 observations, read 15:08Z, first-published read in the tool for HY: HY OAS 332 bp, −8 from 340; CCC 1,297 bp, −19 from 1,316. These are pre-today prints: they do not include this morning's AI selling.

RED-FT-02 and REG-T-03: fired state retained, no re-fire; four closes 344, 343, 340, 332; exits <300 ×3 and <=300 ×5 at 0. REG-T-04 strict >350 ×3 at 0/3, 18 bp away, now outside the 5% watch band. RED-FT-07: state unchanged, exit <930 ×3 not met.

VIXCLS 16.61 [November 4] is below 18, so the RED-FT-06 exit run goes 3/5 to 0/5 on WALTER's read; FIRED-BANKED retained; not a new fire, since the fire leg is <16 ×5. Cboe SKEW 150.90 [November 4]: RED-FT-10 fired, exit 0. SOFR−IORB +4 bp [November 4]; REG-T-08 no.

ACTION RED: grade FT-06 at your next session; your next wake is November 6 unless PROME moves it.""",
 sources='FRED BAMLH0A0HYM2, BAMLH0A3HYC, VIXCLS, SOFR, IORB read 2026-11-05 ; https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv ; research/2026-11-05_morning/THRESHOLD-SCAN.md',
 note='Closes batch BM-20261105-01 item 8. Scope: November 4 close only. WALTER executes the count; RED owns the grade.'),
dict(n=10,slug='CoreWeave-bonds-15-to-16-percent-no-default-on-EDGAR',
 title='CoreWeave secured notes trade at 15–16% yield; EDGAR shows no bankruptcy or acceleration filing',
 action=['VULCAN','BROCK'],info=['LIQUID','RED','PROME'],precedence='PRIORITY',signal_type='research',confidence=0.75,
 cluster='AI_INFRA_CAPEX',domain='PRIVATE_CREDIT',entities=['CRWV','CoreWeave'],
 body='''Bookmark screenshot, Ed Zitron, November 4, terminal table, vendor unseen, not independently priced: 9.25% June 2030 83.43, 15.53%; 9.00% February 2031 80.86, 15.33%; 9.75% October 2031 79.48, 15.97%; 9.625% July 2032 78.94, 15.32%; 8.50% July 2032 75.56, 15.04%. Converts 8.88–10.18%. Bloomberg, Yahoo and TipRanks November 4 headlines say bonds hit new lows on Texas data-center risk; bodies unread.

LIQUID [November 4]: model-derived 5-year CDS 1,103–1,211 bp, flat-hazard, not executable; reads this as one-cohort repricing, not funding stress. Vendor CRWV 44.14, −8.84% at 10:08 ET.

KILL: "no longer has access to bond markets… Bankrupt" (X, @rdd147). EDGAR read 15:0xZ: latest 8-K September 22 (items 1.01, 3.02, 8.01); no item 1.03 or 2.04; prospectus supplement September 17. Access to markets at these yields is a live question; bankruptcy is not an established fact. 2027 obligations NOT read.

ACTION VULCAN: weak-link read with Q3 about November 9. ACTION BROCK: DDTL and lender exposure.''',
 sources='https://pbs.twimg.com/media/HWS8LwYX0AAg6o5.jpg ; X 2118025416174669925 ; X 2118054715619766712 ; https://data.sec.gov/submissions/CIK0001769628.json ; AGENTS/LIQUID/STATUS.md',
 note='Bookmarks 11 and 14. Financing leg, so PRIVATE_CREDIT with VULCAN on action per the substance-versus-financing boundary. Screenshot figures unverified at a pricing source.',
 extra={'kill_note':'CoreWeave bankrupt claim: no EDGAR item 1.03 or 2.04 through November 5'}),
dict(n=11,slug='Citrini-calls-peak-AI-capex-growth-free-section-read',
 title='Citrini calls peak AI capex growth and higher US data-center costs; opinion, paid body unread',
 action=['VULCAN'],info=['WATT','HENRY'],precedence='PRIORITY',signal_type='thesis-frame',confidence=0.6,
 cluster='AI_INFRA_CAPEX',domain='AI_CAPEX',entities=['Citrini','hyperscalers','Texas','Ohio','Georgia'],
 body='''Citrini Research, "State of the Themes", November 4; free section read, paid body not. Named view, not data. Claims "peak capex growth"; asymmetric risk now to the downside; hyperscaler annualized capex "about to hit $1 trillion"; ecosystem ARR at least $200 billion; demand for issuance "starting to wane"; quarterly RPO growth lowest in years; governors in Texas, Ohio and Georgia unlikely to stop building but cost "almost certainly" higher. Terminal headlines add a late-cycle stagflation tilt; not seen in the free text. None of these figures were checked.

Why it matters: a widely followed thematic book turning the same day data-center stocks fell. That is a positioning fact, whatever the capex truth. It may have added to the selling; not established. Card 005 holds the tape.

ACTION VULCAN: compare the capex and RPO claims with your own series; S1 needs a hyperscaler capex cut year on year, and this is not one.''',
 sources='https://www.citriniresearch.com/p/state-of-the-themes-556 ; X 2118112949675999562 ; X 2118079004863610885',
 note='Bookmarks 5 and 6. thesis-frame stays PRIORITY. Copy list trimmed under WQ-556 C.'),
dict(n=12,slug='Fannie-Freddie-common-falls-after-Ackman-rally-cause-unread',
 title='Fannie and Freddie common fell as much as 24% November 4 and fall again today; cause not established',
 action=['HOMER'],info=['LIQUID','RED'],precedence='PRIORITY',signal_type='context',confidence=0.7,
 cluster='BANK_COLLATERAL',domain='BANK_CRE',entities=['FNMA','FMCC','Ackman','FHFA'],
 body='''Quote screenshots, November 4: FNMA low 4.08 versus prior close 5.56, about 4.20 at one point (−24.46%), FMCC 3.77 (−24.60%); 4.87 at 13:36 ET. Vendor November 4 closes FNMA 4.80, FMCC 4.36; 10:08 ET today FNMA 4.38 (−8.75%), FMCC 3.95 (−9.40%), not closes.

Headlines, bodies unread: shares rose 9% and 7% on Election Day on Ackman's conservatorship-exit push; National Mortgage News November 4, investors risk "zero earnings" through 2033. The link from the Democratic sweep to these moves is a reasonable reading, not an established cause. This is common equity in conservatorship, not agency-debt or MBS stress; no funding read here.

Bookmark claims, unverified, one dated October 5: capital about 2.5% of $4.6 trillion; 1.5% serious delinquency wipes quarterly profit. "FHA delinquency pushing 12%" sits beside HOMER's 11.79% Q2 row, RED above 12%; Q3 MBA not read. "Housing about to crash" is the poster's framing.

ACTION HOMER: read the cause; check the FHA line at the next MBA print.''',
 sources='https://pbs.twimg.com/media/HWSlfAobEAAHKVR.jpg ; https://pbs.twimg.com/media/HWTXCrWb0AAZEXB.jpg ; X 2117999683067162677 ; X 2118054171362677138 ; X 2107243654503162164 ; vendor tape 15:08Z',
 note='Bookmarks 7, 12, 13. No BOARD card held the GSE move. HOMER STATUS dated October 29.'),
dict(n=13,slug='Ueno-Paraguay-update-central-bank-chief-out-impeachment-move',
 title='Ueno update: Paraguay central bank chief resigned, lawmakers move to impeach; no US exposure established',
 action=['LIQUID'],info=['REGINALD','BROCK','RED','PROME'],precedence='PRIORITY',signal_type='research',confidence=0.7,
 cluster='BANK_COLLATERAL',domain='FUNDING_LIQUIDITY',entities=['Ueno-Bank','Banco-Central-del-Paraguay','Pena','Carvallo'],
 body='''Update to card 20261104-069, which holds the BCP primaries. Headlines, bodies unread unless named. Reuters November 3: central bank chief resigns at the president's request. Reuters November 4: lawmakers call to impeach the president. Bloomberg November 4: accounts vanished before dawn; card payments and rent disrupted. Latin Times November 4: $380 million of public pension money at risk. FT and LA Times: bank has ties to President Peña.

Superintendency notice in the bookmark image, November 3: Resolution 0015/2026 suspends redemptions, cash distributions and subscriptions at 13 funds from five managers: CADIEM, Puente, ueno, BNB Asset Management and Basa. Matches 069.

UNVERIFIED, one X thread: eight executives ordered arrested; two of three big-store card payments; the $1,700 cap; 14 banks asked for solvency reports in October; Itaipú money stuck. Euronews says "liquidation"; BCP says resolution: carry BCP's word. "60% of adults" and "half of savings" differ across outlets; no denominator read.

No US exposure, regional contagion or asset-loss total established. ACTION LIQUID: integrate the fund and political facts; say whether any channel reaches your book.''',
 sources='BOARD/SIG-W-20261104-069-Ueno-bank-fund-transmission.md ; https://pbs.twimg.com/media/HWR_YMPasAAqsmg.jpg ; X 2118016700767453361 ; X 2117957799183528340 ; X 2118108238163886528 ; Google News titles November 3–5 saved in research/2026-11-05_bookmarks/src',
 note='Bookmarks 2, 3, 4. Bloomberg, Reuters and Economist bodies not read; Bright Data CLI absent on this box. Will bookmarked three, so routed as an update, not folded silently.'),
dict(n=14,slug='QQQ-below-its-200-day-after-Wednesday-survived-post-SOXL-short-volume',
 title='QQQ now trades below the 200-day average a Wednesday post said it had survived; SOXL short volume at April 2025 scale',
 action=['HENRY'],info=['VIOLET'],precedence='PRIORITY',signal_type='context',confidence=0.7,
 cluster='POSITIONING_VALUATION',domain='MARKET_VOL',entities=['QQQ','SOXL'],
 body='''Barchart chart November 4, 13:33 ET: QQQ 200-day average 680.57, QQQ 694.92. Vendor 10:08 ET today: QQQ 664.83 (−3.92%), so about 2.3% under that level; intraday, not a close, and the average moves daily.

SOXL chart, @BenKizemchuk: FINRA short-sale volume about 49.2 million for the current partial week versus a 10-week average 28.6 million, the highest since the April 2025 spike the poster marks as a low. This is FINRA short-sale volume, not short interest; on a 3x fund much of it can be market-maker hedging. The "prior low" alignment is one case.

Opinion charts, read, not routed as evidence: Dow head-and-shoulders count against large-cap momentum, and a WTI channel count pointing to 104+.

ACTION HENRY: index mechanics on a close below the 200-day. VIX 20.12, +3.51 at 10:08 ET; the +5 intraday safety line is 21.61.''',
 sources='https://pbs.twimg.com/media/HWTSeNyW4AA00Ud.jpg ; https://pbs.twimg.com/media/HWUsn-iX0AAkkJ2.jpg ; X 2118049301385670896 ; X 2118148507374874639 ; vendor tape 15:08Z',
 note='Bookmarks 1, 9; 8 and 10 read and disposed NO-ACTION. Short-volume caveat is WALTER context, not an owner read.'),
]
print(send(CARDS,'WALTER November 5 X bookmarks, Will-curated, 15 IDs')[0])
