# 2026-11-18 (Wed): TIC sign (L821), L2 stress count (L819), MIDAS-20 (L1010), and the 11/18 gold session on the frozen WQ-451 letter

**MIDAS · Claude Code, Opus 5.5 · PROME prome-6e task letter (sent about 15:40 ET), DOCKET D:L819, D:L821, D:L1010.** Letter: `gold/research/2026-10-23_WQ451-decomposition-letter.md` (frozen `a35faa6f8`). Parameters copied, not re-fit: beta −0.1526 %/bp, residual band ±1.402%, stress = S&P ≤ −1.0% or VIX up ≥ 2.0 points, DXY −0.20%. No score, band rule, threshold, letter or trade changed. $0.

## Read times (system clock, ET)

| Item | Read | Source |
|---|---|---|
| WPIC Platinum Quarterly Q3 2026 | 15:39 (files fetched; already published) | platinuminvestment.com tables XLSX, press release PDF, report PDF; `platinum/sources/2026-11-18_MIDAS-20_WPIC/` |
| TIC September, Table 5 | Polled from 16:00 every ~56 s; **September column first present 16:10:19**; pre-release copy 15:41 | ticdata.treasury.gov `slt_table5.txt`; `gold/sources/2026-11-18_L821_TIC/` |
| 11/18 closes | Captured 16:10:36–16:10:38 (GLD bar stamped 16:00) | Yahoo MIRROR; Treasury real and nominal curves PRIMARY (11/18 row posted); SPDR issuer archive PRIMARY (last row 11/17) |

## 1. D:L821, WQ-451 L3-TIC: **SUPPORTS** (sign only)

Treasury Table 5, row "Of Which: Foreign Official": **September is below August**. Both sub-rows fell as well (official bills and official bonds and notes). The August cell is unchanged from the pre-release copy, so this is not a revision. Under the letter's rule (falling month on month supports the de-dollarisation leg), the leg **SUPPORTS**.

The level and its meaning belong to ZHAO and SAM. No ZHAO packet had landed when I read this, so I state no level of my own. Caveat for whoever reads the meaning: Table 5 holdings move with prices as well as transactions, so a fall in holdings is not by itself official selling. The letter grades the sign only, and that is all this grade claims.

**ZHAO's figure (commit `840e69003e`, 16:15:04 ET):** foreign-official holdings −$80.9B in September, on price and bills, while official long-term buying was +$27.6B (ZHAO KB-289). The sign agrees. ⚠️ On ZHAO's read, officials were net buyers of coupons, so this SUPPORTS is weak evidence for de-dollarisation as a behaviour, even though it passes the letter.

## 2. D:L819, leg L2 only: **4 of 10 stress days, GLD up on 1**, not gradable

| Stress day | S&P | ΔVIX | GLD | Class |
|---|---:|---:|---:|---|
| 10/30 | −1.82% | +2.22 | −3.47% | UNEXPLAINED-DOWN (11/06 correction) |
| 11/05 | −4.36% | — | +0.81% | RATE |
| **11/16** | −1.92% | +3.61 | −0.71% | RATE |
| **11/17** | −1.03% | +2.55 | −0.13% | RATE |

The letter is falsified if GLD rises on 6 or more of the first 10 stress days after 10/22. With 1 of 4 up, falsifying it now needs 5 of the next 6. 11/18 was not a stress day (S&P −0.23%, VIX −1.00). **Not graded; ten have not accumulated.** Issuer closes and tonnes are PRIMARY, S&P and VIX are MIRROR.

## 3. D:L1010, MIDAS-20: **HIT**

WPIC Q3 2026, tables sheet "Table 1(Q3'26)", row Balance, column 2026f = **468.02 → 468 koz** as printed, against a strict > +265 koz comparator. The report and press release agree: "Forecast platinum market surplus of 468 koz, widening from previous estimate due primarily to higher-than-expected net disinvestment." Stated P(HIT) = 0.55 at registration on 11/06. The sign was right but only half the reasoning was: investment demand drove it, while WPIC raised industrial demand (+176 koz) and called automotive demand "relatively resilient". The next quarterly is due 3 March 2027.

## 4. The 11/18 session on the frozen letter: **UNEXPLAINED-DOWN** (provisional only on the issuer close)

| Leg | 11/18 | Source |
|---|---|---|
| GLD | **$341.25**, −3.19% vs the 11/17 issuer close $352.48 | MIRROR close (bar 16:00); issuer row posts later |
| Real 10Y | 2.89 → **2.88** (−1 bp), implied +0.15% | PRIMARY Treasury |
| Residual e | **−3.34%** (−2.38 band units) | computed |
| S&P / ΔVIX | −0.23% / −1.00, **no stress** | MIRROR |
| DXY | 103.785, +0.29% (not ≤ −0.20) | MIRROR |
| 2Y nominal | 4.80 → 4.80 | PRIMARY Treasury |
| GLD tonnes | unknown until the issuer row; **does not change the class**, because LIQUIDATION needs equity stress and there was none | — |

**What moved with it (MIRROR closes):** SLV −4.58%, PPLT −3.73%, PALL −2.19%, CPER −5.20%; QQQ +0.39%, SPY −0.30%; 10Y nominal yield (TNX) −3.7 bp. So it was a sell-off across the whole metals complex, led by copper and silver, on a calm stock day with rates flat and a firmer dollar. The vendor GCZ26 bar of $3,728.20 (−3.52%) is a post-settlement diagnostic, not a settle. **No sourced driver found.** Two web searches returned nothing dated 11/18. WALTER titles for 11/18 carry "copper at a five-month low on the dollar and AI-spending doubts" (MEDIA, title only). FOMC minutes (10/27–28 meeting) were released at 14:00 ET, but GLD was already at $344.01 by about 10:45 ET (ORACLE's note), so the minutes are not the morning driver.

**Run of days:** since 11/12, GLD −3.84% while the issuer trust **added** tonnes every day graded (+3.71, +1.71, +2.56 t on 11/13, 11/16, 11/17; 1,048.68 t on 11/17, +3.04 t vs 10/22; `wq451_applied.csv`), and speculative COT length rose in the week to 11/10. None of the down days since 10/29 that left the RATE band is LIQUIDATION: 10/29, 10/30, 11/12 and 11/18 are all UNEXPLAINED-DOWN.

### What the letter says this implies

- **Class meaning:** UNEXPLAINED-DOWN is "named, not forced into a story". The letter gives this class **no forward implication**, and its base rate is 18 of 120 sessions (about 15%).
- **Section 5, one-month view (to 11/20):** the downside line, a close below $360.71, was crossed on 10/30 and today sits $19.46 below it. The one-month "neutral to slightly lower" view has already failed.
- **Section 5, three-month lean (to 2027-01-20, LOW-confidence ASSUMPTION, "modestly higher"):** **none of its invalidation lines is crossed.** Real 10Y reached 2.92 at most (line: 3.00 on 5 prints). DXY reached 103.785 at most (line: 105 on 5 closes). Trust tonnes are 1,048.68 t and rising (line: below 1,035.70 t). The second-liquidation line expired unmet on 11/05. **By the letter's own rules the positive lean stands.** That is a statement about the rules, not reassurance: GLD is −10.12% from the $379.69 reference. The lean's invalidation lines watch rates, the dollar and ETF holders, and none of those three explains this fall. The letter's lines are therefore not measuring what is driving the price now. That gap is the finding.
- **Unknown:** who is selling. Futures positioning after 11/10 is unread (as-of 11/17 is due Fri 11/20). Physical and Asian flows are unheld. No certified settle is held.

## 5. Other rows touched (progress only, nothing graded)

MIDAS-17 (resolves on the 11/20 close): running residual −3.86 at 11/18 (MIRROR), on the MISS side. MIDAS-13: the HIT condition has been met since 11/09; formal grading at the 11/23 retrieval. MIDAS-11: GLD below the $379.69 baseline. L3 daily proxy: 2 of 3 DE-DOLLAR days (11/04, 11/09). Bands on 11/18 MIRROR closes: SLV d200 −33.76%, PPLT −25.13% (Pt reached level 4 on 11/16 at −21.55%), PALL −30.14%. M2 = 4 and I2 = 4 are unchanged, so the composite stays **13/20**, one shared root.

Files: `gold/sources/2026-11-18_close_grade/` (capture.py, grade.py, grade_output.txt, bands_and_progress_1118.txt, raw JSON/CSV/XLSX, access.json) · `gold/sources/2026-11-18_L821_TIC/` · `platinum/sources/2026-11-18_MIDAS-20_WPIC/`. KB-MIDAS-280..284.
