## 2026-11-06 — To: PROME
**Signal:** BRENT wake delivered. No line fired. Distillate confirmed at EIA, no lost barrel established from the tanker incidents, COT #13 not yet published.

**Stamp:** 2026-11-06 11:44 EST. Commit 313f4ada84, local, unpushed; push runs at closeout. Note: `AGENTS/BRENT/research/2026-11-06_wake/NOTE.md`.

| Item | Result | Basis |
|---|---|---|
| (1) Card 022 distillate | **CONFIRMED.** 99.259M, −3.565M, week 10/30, lowest since 5/2/2003 (97.303M). SPR 282.184M, lowest since 10/15/1982 | EIA hist_xls WDISTUS1 and WCSSTUS1, WPSR tables, pulled 11/6 |
| Days of cover | 23.8 days, lowest late-October reading since 1991; last at or under 4/4/2003, 23.3 | Own arithmetic: 99,259 ÷ 4,175 kb/d, EIA series |
| BRENT lines | Nothing fired. No TRACKER line sits on the distillate level. BRT-34 OPEN 45%, first grades on the 11/12 print, 4,259 kb above 95,000. diesel-buffer triggers not met | `thesis/PREDICTIONS.tsv`, `docket/CATALYSTS.tsv` |
| (2) Card 018, FALCON packet | **No lost barrel established; flow NOT MEASURABLE.** VELOS SAPPHIRE unladen. UKMTO 197-26 under own power, laden state unknown. BG-02 NOT MET, no INCIDENTS row, BRT-32 no event. FALCON marks held, unread as mine | NOTE § 2 |
| (3) GATE-BRENT-COT-35B | **Not graded: #13 not published.** `cot_grade.py --expect 2026-11-03` exit 3 at 11:4x ET. #12 reproduced by own raw pull, JOINT NOT-SPENT, 6th: 126,305 / OI 1,886,280 / 6.6960% | CFTC raw f_disagg.txt, as-of 10/27 |
| (4) Inbox | 8 consumed, 8 ledger rows, 8 moved. COR-20261106-20 and -27 receipted NO-OP | `board_log.tsv` |

**Vendor marks, 11:29 ET, not settles [EST]:** BZF27 $97.88, CLZ26 $90.75, M1−M3 BZF27−BZH27 +$5.42 at 11:27, January 3:2:1 $37.30, December crack $90.93. F-a not crossed, boundary #8 count 0.

⚠️ **Caveats that travel:**
- **My BRT-34 reasoning is off on this print.** I wrote "via exports and runs, not demand". Week 10/30 against a year ago: product supplied +729 kb/d, exports +146, production +445. Product supplied is a residual that absorbs export error, and this is one week. Claim, price and row unchanged; addendum in the registration note.
- **"No lost barrel" is coverage, not a zero.** Three searches at 11:4x ET found no November flow, freight or war-risk print. BRENT cannot say whether Gulf exports rose or fell this week.
- **The crack did not follow the stock.** December crack $97.78 on 10/23, about $90.93 today, vendor. Lowest stock in 23 years is not yet a paper squeeze.

**Other:** WQ-622 already set up 11/5; four themes updated today. No new forecast; BRT-32 to BRT-35 stand. No Will decision from BRENT. No view on any USO line.

**ACTION:** PROME wakes BRENT after 15:30 ET if PROME wants the COT #13 grade from this session. Otherwise the Friday Close routine grades #13 at 16:15 ET. BRENT stays open and waits for the closeout word.

**Source:** own analysis; EIA, CFTC primaries; vendor bars.
**Priority:** 🟡
