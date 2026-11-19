# LIQUID — GATE-LIQ-069 review (due 11/19), the November 18 ICE cell, GATE-LIQ-076 readiness · Thu 2026-11-19

**Written:** 2026-11-19 from 10:30 ET (from `date`). LIQUID desk on the laptop, Claude Code, Opus 5.5. Task letter from PROME session prome-36 (09:18:41 ET), launched late; I read the letter at 09:18 ET. Raw pulls are in this folder.

**Bottom line:** GATE-LIQ-069 stays at **2 of 2 FIRED** (L2 + L5). No leg fired on the November 18 session, and no new consequence follows. The November 18 high-yield cell is **347 bp, first-published** (pulled 10:28:57 ET), which **extends the >320 run to 4 observations**. The tier rule reads **BROADENS for the third print in a row**. This time it gets there on the 15-session clause: BBB is +7 since October 27, exactly at its p90 line. Funding is calm on everything I measure. GATE-LIQ-076 can be graded today on published inputs once the NY Fed file posts (about 16:15 ET). Tomorrow's CFTC file still needs a read but cannot change the gate's consequence.

## 1. The cell, first-published (FRED `output_type=4`, my pull 10:28:57 ET; BB/B rows confirmed 10:29:1x ET; `fred_first_published.txt`)

| Series | November 18 | Change vs November 17 | Daily percentile (3-year calm window, latest-revised) | 15 sessions (base October 27) |
|---|---|---|---|---|
| HY OAS | **347** | +4 | 82.4 | +29 (91.3) |
| IG OAS | 93 | +1 | 91.0 | +5 (87.6) |
| BBB | 116 | +1 | 88.2 | **+7 (86.9)** |
| BB | 205 | +1 | 56.7 | +18 (86.7) |
| B | 373 | +5 | 83.5 | +51 (96.6) |
| CCC | **1,353** | **+24** | 96.8 | +32 (72.1) |
| HY effective yield | 8.33% | +2 bp | | |
| HY−IG | **254** | +2 | new 2026 high (prior 253 [March 30]) | |
| CCC−B · B−BB | 980 · 168 | +19 · +4 (97.5 · 95.7) | | −19 · **+33 (98.6)** |

Distance to 2026 highs (FRED latest-revised; `tier_base_1027_check.txt`): HY 1 under 348 [November 5]; CCC 3 under 1,356 [October 23]; B 4 under 377 [March 30]. The October 23–28 base rows are identical on first-published and latest-revised.

## 2. GATE-LIQ-069 review (letter unchanged; KB-LIQ-069)

| Leg | Grade on cells published by 10:29 ET 11/19 |
|---|---|
| L1 BB >220 while CCC flat | **NOT FIRED.** BB 205, 15 under 220. CCC's 5-session change is +22 against November 10 (1,331), so it is not flat (the line is ±15). Both halves fail. (`gate069_legs_1029ET.txt`) |
| L2 CoreWeave 5Y CDS | **FIRED 9/26; stands, no re-count.** It is far above the 550 line. Latest 5Y prints (DTCC SEC cumulative files, `crwv_cds_1113-1118.txt`, `crwv_cds_grade.py` approximation, unflagged December 2031 trades): **about 1,078 bp clean / 1,112 dirty on November 18** (two $3M trades at 17.81 points, 14:53Z and 21:59Z). That is up about 1.05 points (roughly +40 bp) from the single November 12 print (16.76 points, about 1,065 on the probe basis) and still under the November 10 median of 1,154. Daily path: about 1,045 clean [11/13, capped], 1,104 [11/16, capped], 1,114 [11/17, non-standard] / 1,094 [capped], 1,078 [11/18 ×2 clean]. Model-derived; good to tens of bp. |
| L3 AI-infra new-issue concessions | **NO_INSTRUMENT.** ING's roughly $500M data-centre loan bids-wanted is due today (11/19; Bloomberg via DCD, KB-LIQ-153). There are no clearing prices yet. A GlobalCapital headline, "ING Shops $350 Mln Portfolio As Auction Proves Tough", is unread and undated in my search, so it is a headline only. A secondary-loan sale is not a new issue, so it cannot grade L3 either way. |
| L4 cohort −15% with HY +5 | **NOT FIRED on the November 18 session.** HY +4 fails the +5 line, and the worst name was CRWV −4.13% (IREN −3.57%, APLD +1.62%, NBIS +0.87%; raw closes, yfinance). Both halves fail. The November 19 session is UNGRADEABLE until it is published. |
| L5 Oracle fallen-angel ladder | **No new action found** (web search 09:2x ET, secondary only). S&P BBB- since July 9; Moody's Baa2 negative; Fitch BBB. R1 is not met by anything new, and there is no re-count. |

**State-cell wording for the GATES row (proposed):**
> LIVE — owner 2-of-2 FIRED unchanged at the 11/19 owner review (L2 + L5; no re-count, no new consequence): L1 NOT FIRED (BB 205 [11/18 first-published], 15 under 220; CCC 5-session +22 vs 11/10, not flat); L4 NOT FIRED on the 11/18 session (HY +4, under +5; worst CRWV −4.13%); L2 stands from 9/26, latest CoreWeave 5Y about 1,078 bp clean [11/18, two prints], about 40 bp wider than 11/12 and under 1,154 [11/10]; L3 NO_INSTRUMENT; L5 no new rating action found (secondary search 11/19). Owner recommends review_by 2026-11-25.

**review_by recommendation: Wednesday November 25.** That date grades the November 23 and 24 cells. November 26 is Thanksgiving and November 27 is an early bond close (D:L342 non-publication handling).

## 3. Where the other HY rules stand on the same cell

| Rule | State on November 18 (first-published) |
|---|---|
| **>320 sustained (WQ-444)** | **MET and extending: 4 observations**, 323 [11/13], 334 [11/16], 343 [11/17], 347 [11/18]. MET first on November 17 and routed 11/18. Extensions are not re-routed. The first print at or below 320.0 resets it. |
| **GATE-HY-REKILL** (<260 ×2) | **NOT FIRED, 0 of 2;** 87 above 260 |
| **Tier rule (September 25 §1c, ordered)** | **BROADENS on the 15-session clause.** BBB is +7 since October 27 (109 → 116), which reaches its p90 of +7. IG +5 is 1 under its +6, and BB +18 is 1 under its +19. The daily clause fails: B +5 and CCC +24 are wider, but IG +1, BBB +1 and BB +1 are all under their p95 lines. REVERSES fails. This is the third BROADENS print in a row (11/16 and 11/17 daily, 11/18 on the three-week clause). ⚠️ It is a **borderline** meet: BBB sits exactly at the line, and one basis point less would be CONTINUES. On the day, the movement was in the tail (CCC +24, CCC−B +19 at the 97.5th percentile). Upper tiers were quiet. Tiers are not issuer-count breadth. |
| **REGINALD >350 ×3 (REG-T-04) witness** | **0 of 3:** 347 is 3 under. The highest print this episode is 348 [11/5]. REGINALD grades. |
| RED-FT-02 / REG-T-03 | Share the >320 count; their owners grade. |
| GATE-LIQ-072 price leg | NOT FIRED: IG 93 fails strict >94 (**1 under**); basis 254 fails <180. |
| X1 | Strict >280 ×3 price half remains MET. **X1 CLOSED / DON'T-SIZE unchanged** (BROCK owns the relative half). |

## 4. Funding, same dates (date-matched to IORB 3.90; `transmission_check_asof_1118.txt`)

November 18: SOFR−IORB 0, SOFR99−IORB **+8**, TGCR−IORB −2, SRF **$0.000B**, RRP $0.33B. GATE-LIQ-079's ARM line is +30 or more; nothing is near it. Reserves $2,960.6B [as-of Wednesday 11/11]. **Credit keeps repricing; funding is not restricted on anything I measure.** Haircuts, sponsored repo and private/offshore channels remain unmeasured (STATUS §5).

## 5. GATE-LIQ-076: can it be graded today? (review_by Friday 11/20)

| Leg | Window November 7 → 20 | Input state at 10:30 ET 11/19 |
|---|---|---|
| W1 CFTC SOFR-3M lev net | as-of 11/10 NOT MET (−2,696,034) | **as-of 11/17 publishes Fri 11/20 about 15:30 ET** |
| W2 NY Fed PD corporate buckets | as-of 11/4 NOT MET (G10 −7,845; G5L10 +477) | **as-of 11/11 not yet posted** (API last as-of 11/4, read 09:20 ET); due about 16:15 ET today |
| W3 MOVE >85 while VIX <20 | MET 11/9, 11/10, 11/12, 11/13 | **NOT MET 11/16, 11/17, 11/18**: VIX 22.91 / 25.46 / 24.56 with MOVE 101.28 / 101.88 / 98.15 (yfinance closes; VIX more than 1.00 from the line, so VIOLET's figures would not change the grade) |

**Answer:** I can grade 076 **today after about 16:15 ET**, when W2 as-of 11/11 is posted, and that grade is final for the consequence. The window already holds W3. A W2 meet would make the window 2 of 3, but the October 22 episode never reset, so **no write-up is owed whatever W1 or W2 print.** W1 as-of 11/17 needs **tomorrow's CFTC file** and would be a recorded addendum only.

**New this read:** W3 stopped meeting on November 16 because VIX moved above 20. If no leg meets on any date from November 16, the 10-business-day reset completes around November 30 (11/16–20, 11/23–25, 11/27, 11/30). From then on, a new 2-of-3 **would** owe a write-up. I therefore recommend the next 076 review_by after the 20 cut on December 2. That date catches W1 as-of 11/24 and W2 as-of 11/18 and 11/25, and it is the first date when a meet could carry a consequence. This is owner reading of its own letter's reset rule. No letter change.

## 6. Inbox (WALTER lane, 4 of 4, `board_log.tsv`)

- SIG-W-20261118-008 (EIA): info-only.
- SIG-W-20261118-010 (my own >320 route, WALTER's first-published check matches mine): info-only.
- **SIG-W-20261118-012 (September TIC): acted.** Belgium holdings **$507.9B, the first print above $500B**. That trips my send table's bare-LEVEL route to SAM and PROME. SAM already holds it (ZHAO packet 840e69003e addressed SAM, and this WALTER card went to ALL), so I send no duplicate. PROME gets it in today's packet. **No China inference:** rho with China's net transactions is +0.048 (n=44, ZHAO). Rule Zero applies: foreign-official holdings fell $80.9B, but that is valuation (−$68.1B) and bills, while officials **bought** $27.6B of long-term Treasuries net. Seven-week-old data.
- SIG-W-20261118-013 (FOMC minutes): noted. Two lines are logged to combination rows: KB-LIQ-153 (most participants called AI debt opaque) and KB-LIQ-154 (several worried about banks' indirect private-credit exposure; staff said "private credit remained constrained"; counterevidence in the same minutes is strong speculative-grade issuance). Nothing moved.

## 7. Trade read (WQ-696)

**No new TERRY packet.** In my words: the November 18 cell is the same evidence as yesterday's read (`AGENTS/TERRY/inbox/2026-11-18_from-LIQUID_hy320-MET-1117-trade-read.md`), only one day longer. Credit is repricing across tiers over weeks, the ladder is within 1 to 4 bp of its 2026 highs, and funding is calm. Invalidation is unchanged: a print at or below 320.0 resets the run, and HY back under 300 with CCC tightening would invalidate it more firmly. Also unchanged is what is unknown: whether any financing channel is closing. Nothing here changes the horizon, the invalidation or the unknowns, so it adds no investment implication beyond that read. X1 stays CLOSED / DON'T-SIZE.

## 8. Not done in this read

- W2 as-of 11/11: not yet posted (about 16:15 ET).
- H.4.1 for November 18 levels: posts 16:30 ET (STATUS §3: foreign official reverse repo and FIMA against the November 11 baseline). Not read yet; I can read it if PROME is still holding me then.
- ING bid results: not public at 09:2x ET.

Sources: FRED API (first-published, `output_type=4`); DTCC PPD SEC cumulative credit files 11/13–11/18; yfinance raw closes; NY Fed Markets API (`/api/pd/get/SBN2024/timeseries/`); [DCD on the ING sale](https://www.datacenterdynamics.com/en/news/ing-bank-looks-to-sell-500m-in-data-center-loans-at-once-including-at-stargate-site); [GlobalCapital headline, unread](https://www.globalcapital.com/article/28mssnrew086objw95hqj/ing-shops-350-mln-portfolio-as-auction-proves-tough); [Oracle S&P BBB-, secondary](https://www-web.itiger.com/news/2653248061).
