# Q3 Call Report run and frozen ranking test, Saturday 2026-11-07

**Desk:** REGINALD, laptop, PROME prome-bf's word Sat 09:07 ET. **Basis:** bank-level FFIEC Call Reports, quarter-end 6/30 and 9/30/2026, pulled fresh 09:07 to 09:13 ET unless labelled. **Nothing moved:** no score, band, threshold, gate or trade.

## 1. The answer first

The 8/20 risk score did not predict Q3. Banks it ranked riskier did not get worse by more in nonaccrual loans, and on charge-offs two far simpler measures beat it. Separately, the breadth test reads BROADER on its literal wording, but it gets there by a thin route: none of the five banks it tests passed the bad-loan test, and the count hangs on foreclosed-property rises at three of them, one just $0.9M and outside commercial real estate. Taken together this changes nothing on the regional-bank put thesis. It does not strengthen the tier-wide case, because commercial real estate bad loans fell across the 14. The population count that would actually test tier-wide stays UNKNOWN until the FDIC posts 9/30.

| Question | Result |
|---|---|
| Frozen ranking test (14 of 14) | **No skill shown.** S1 vs nonaccrual change −0.183, vs charge-offs −0.075. No distinguishable difference from the baselines on nonaccrual; **baselines better on charge-offs** (B1 +0.374, B2 +0.503) |
| Coverage point (S1 vs S2) | **No distinguishable difference** (0.005 and 0.032). S1 did not beat S2, so L801 stands |
| L180 breadth | **BROADER on the letter, c = 3, m = 0.** Bad-loan rate up >50%: **0 of 5**. Foreclosed property rising: WAL, SSB, BKU |
| Recognition exit rail, leg 2 | Not NOT BROADER, so the stand-down REVIEW cannot fire this cycle. Leg 1 met, leg 3 open |
| Cohort direction | Total-CRE bad-loan rate **2.23% → 2.13%**; multifamily 3.58% → 3.65% |
| FDIC 9/30 universe | **Not posted, 0 rows, 09:07 ET.** (a), (d), (e), (f) UNKNOWN |

⚠️ **The caveat that could change a decision.** L180 flips on one reading. The foreclosure limb was never given a size, so any rise counts (plan §2.0 ②, flagged 10/9). BKU's rise is $0.879M, all outside CRE. With CRE-only foreclosed property, shown beside and never substituted, c = 2 and the grade would be NOT BROADER. SSB and BKU are both still below their 3/31 levels. Only WAL is a build in any ordinary sense, and that is mostly one office property. A floor is Will's rule change. **My recommendation: do not change the rule after seeing the result. Keep BROADER as graded, read it as weak, and if Will wants a floor, register it before the Q4 run.**

⚠️ **Direction of that caveat.** The loose limb keeps the bear thesis alive by blocking a stand-down review. This desk benefits from that reading, so it should be discounted accordingly.

## 2. Completeness (plan §2.0 ④)

| Check | Result |
|---|---|
| Q3 Call Report in CDR | 14 of 14, side list 2 of 2. m = 0 |
| Amendment | 9/30 Last Update 10/27 to 10/30 at all 14, nothing since. 70 prior ledger rows byte-identical to the committed vintage |
| MI3 reproduction guard | 154 overlapping bank-quarters reproduce, 0 unexplained |
| Guard selftest | 11/11 |
| Protocol sha256 | `06e37edad2d58307…` matches |

## 3. Frozen ranking test

**Retrospective validation of frozen 8/20 scores, not a blind test.** Protocol `reports/2026-10-23_ranking-test_FROZEN_protocol.md`, script `scripts/ranking_test_20261107.py`, output `04_ranking.out`. Run 09:12 ET. n = 14 of 14. Positive means a higher score went with more deterioration.

| Ranking | Spearman, nonaccrual change (primary) | Spearman, Q3 charge-offs (secondary) | Top group vs other, primary | Top group vs other, secondary |
|---|---:|---:|---:|---:|
| S1, 8/20 score | **−0.183** | **−0.075** | n=3 +0.082 vs −0.058 | +0.282 vs +0.250 |
| S2, S1 less coverage point | −0.188 | −0.043 | n=3 +0.082 vs −0.058 | +0.282 vs +0.250 |
| B1, 6/30 nonaccrual ÷ loans | −0.062 | **+0.374** | n=3 +0.082 vs −0.058 | +0.282 vs +0.250 |
| B2, Q2 change in that ratio | −0.147 | **+0.503** | n=3 −0.047 vs −0.023 | +0.353 vs +0.230 |

| Comparison | Primary | Secondary | Reading (under 0.2 = no distinguishable difference) |
|---|---:|---:|---|
| S1 minus B1 | −0.122 | **−0.449** | Primary none; **secondary baseline ahead** |
| S1 minus B2 | −0.036 | **−0.578** | Primary none; **secondary baseline ahead** |
| S2 minus B1 | −0.126 | −0.417 | Same |
| S2 minus B2 | −0.041 | −0.546 | Same |
| S1 minus S2 | +0.005 | −0.032 | **None. The coverage point adds nothing distinguishable** |

| Bank | S1 | S2 | B1 | B2 | Primary, pp | Secondary, % |
|---|---:|---:|---:|---:|---:|---:|
| FLG | 6 | 5 | 4.88 | +0.152 | −0.069 | 0.477 |
| EGBN | 5 | 4 | 2.05 | −0.582 | **+0.681** | 0.253 |
| AMTB | 5 | 4 | 2.46 | −0.113 | −0.366 | 0.115 |
| VLY | 3 | 3 | 0.88 | +0.031 | +0.080 | 0.279 |
| OZK | 2 | 2 | 0.92 | +0.023 | −0.662 | 0.521 |
| WAL | 2 | 1 | 0.86 | +0.082 | −0.121 | 0.278 |
| SSB | 2 | 2 | 0.53 | −0.060 | +0.015 | 0.094 |
| BKU | 2 | 1 | 0.95 | −0.184 | +0.034 | 0.106 |
| SBCF | 2 | 2 | 0.66 | −0.093 | −0.118 | 0.159 |
| ZION | 1 | 1 | 0.47 | +0.013 | +0.030 | 0.018 |
| MTB | 1 | 1 | 0.84 | −0.042 | +0.049 | 0.349 |
| CUBI | 1 | 1 | 0.31 | +0.036 | −0.022 | 0.274 |
| CFG | 0 | 0 | 0.96 | −0.093 | +0.023 | 0.366 |
| HBAN | 0 | 0 | 0.84 | +0.128 | +0.049 | 0.304 |

**The +0.082 top-group mean is EGBN alone:** the other two top names, FLG and AMTB, fell. S1, S2 and B1 share one top three, so those columns match.

### Defects recorded, not repaired (protocol rule)

| Defect | Size | Changes a reading? |
|---|---|---|
| **Denominator mix at FFIEC 031 filers:** the frozen chain takes RCFD1403 over RCON2122 at CFG, AMTB, FLG, MTB, HBAN, VLY | Same-basis rerun, not the frozen test: primary S1 −0.172, S2 −0.172, B1 −0.062, B2 −0.174; secondary unchanged to 3 decimals | No |
| **Primary outcome counts foreclosure as improvement:** 1403 excludes foreclosed property | OZK nonaccrual −$211.3M with OREO +$127.9M; WAL −$76.4M with +$38.7M. Nonaccrual-plus-OREO rerun, not the frozen test: S1 −0.220, S2 −0.247, B1 −0.097, S1 minus B1 −0.123. B2 not rerun | No, S1 still no better |
| **Not blind:** Q3 releases for 13 of 14 read before the freeze; my 11/01 and 11/05 Q3 pulls came before this run | Scores were fixed 8/20 and not touched | No |
| **One quarter, n = 14, chosen banks** | One bank moves the primary S1: without EGBN −0.404, without OZK −0.197. Sign unchanged both ways | No significance claim is made |

**So what.** The score keeps no earned weight as a predictor of next-quarter deterioration. The frozen matrix stays as it is; the fresh ranking is the protocol's follow-on, frozen before the Q4 prints (~mid-January 2027). That new protocol should settle the foreclosure defect before it freezes.

**Matrix re-score (+OREO): NOT RUN.** The CALENDAR row says this run feeds it, but I found no registered letter for the method, and PROME's term is that no score moves except by one. It needs a letter first.

## 4. L180 breadth grade (plan §2.0)

Total-CRE bad-loan rate = nonaccrual + 90 days over construction + multifamily + non-owner-occupied. `oreo_total_k` = all foreclosed property, literal any-rise reading. Grader `grade_l180.py`, output `03_l180.out`.

| Bank | Rate 6/30 → 9/30 | Change | Up >50%? | Foreclosed property $M, 6/30 → 9/30 | Rise | CRE-only $M, shown beside | 3/31 level $M | Counts? |
|---|---:|---:|---|---:|---:|---:|---:|---|
| WAL | 2.71% → 1.69% | −37.6% | No | 126.1 → 164.7 | **+38.7, +30.7%** | 121.7 → 158.7 | 123.2 | **Yes** |
| VLY | 1.09% → 1.22% | +12.8% | No | 4.1 → 1.7 | −2.4, −58.1% | 4.1 → 1.7 | 5.2 | No |
| SSB | 0.24% → 0.30% | +25.3% | No | 12.4 → 15.2 | **+2.8, +22.8%** | 4.1 → 6.6 | 26.1 | **Yes** |
| BKU | 0.58% → 0.51% | −11.9% | No | 1.5 → 2.4 | **+0.9, +58.8%** | 1.5 → 1.5, flat | 4.2 | **Yes** |
| SBCF | 0.36% → 0.31% | −14.0% | No | 3.5 → 3.3 | −0.2, −6.0% | 3.4 → 3.0 | 4.3 | No |

**c = 3, m = 0, k = 3 → BROADER on the literal reading.** Q1 → Q2 dry run was c = 1.

| Multifamily sub-read, never counted | 6/30 | 9/30 | Foreclosed multifamily |
|---|---:|---:|---|
| WAL | 0.00% | 0.00% | 0 |
| VLY | 0.74% | 0.84% | 0 |
| SSB | **0.90%** | **1.83%** | 0 |
| BKU | 0.34% | 0.00% | 0 |
| SBCF | 0.10% | 0.00% | 0 |
| Cohort of 14 | 3.58% | 3.65% | |

**Individual-bank severity, not a spread (§2.0 ①):** EGBN is the only one of the 14 up >50% (2.86% → 4.75%, +66.1%; multifamily 4.45% → 11.93%). FLG 7.99% → 8.24%; multifamily 8.06% → 8.38%.

**Cohort of 14:** total nonaccrual $9,785M → $9,828M (+0.4%); foreclosed property $530.4M → $695.8M (+$165.4M), where OZK +$127.9M and WAL +$38.7M together exceed the whole rise.

**Other route to BROADER (cross-bank §D):** FDIC QBP ~late November, regional foreclosed CRE up a second quarter with `CREED-T-03`, reads separately.

## 5. CALENDAR 11/07 row

| Item | Result |
|---|---|
| (a) Friedberg 95 of 4,295 | **UNKNOWN.** No 9/30 universe at the FDIC; FFIEC bulk not tried under PROME's term. Primary statement still SEARCH-NOT-FOUND |
| (d), (e), (f) reserve-release counts | **UNKNOWN.** Runs when the FDIC posts, expected mid to late November (ESTIMATE). See note below |
| (c) HBAN step | **STILL OPEN, NOT DISCLOSED.** Q3 10-Q (acc 0000049196-26-000090, filed 10/27) compares only with 12/31, on an all-in basis including Cadence, and has no not-secured-by-real-estate line. Call Report: M3 $2,206.5M → $2,836.8M (+28.6%), loans +0.9%, 9.a $17.51B → $19.94B (+13.9%), so they grew together. New commitments stays INFERRED; relabel not ruled out |
| FLG step | M3 +54.1%, loans +1.5%, also STEP-CANDIDATE. Known since 11/01; funded plus unfunded +12.1% |
| MI3 rank citations | **Re-citable on 9/30 basis.** v1a: EGBN 11.78, MTB 10.56, WAL 8.53, OZK 4.77, CUBI 4.71, VLY 4.40, CFG 4.22, FLG 3.92, HBAN 3.75, BKU 3.40, ZION 1.98, SSB 0.79, SBCF 0, AMTB 0 (both reported zero). Largest dollars: MTB $5,413M. Name the basis every time |
| CUBI N | **MET.** Memo 10b+10c $3,595.6M → $4,037.5M, +12.3% vs >5%. Row stays **INCONCLUSIVE**: no F leg |
| WAL OREO | Nonfarm foreclosed property $95.6M → $132.5M (+$37.0M), tying to the 10-Q's $36M "primarily related to one office property" (WAL desk 10/30). Construction flat at $26.2M |
| WAL hotel | The Call Report has no hotel line. Non-owner-occupied 30-89 $6.5M → $5.8M, 90+ nil, nonaccrual $279.0M → $173.1M. Nothing here tests the 10-Q's $185M criticized figure |
| FLG $128M | **Resolved, my 11/06 wording corrected.** Not a blank line filled in: at 6/30 the balance sat on the C&I line. RC-C Memo 1: K163 C&I $123.8M → 0; K162 other nonfarm 0 → $128.5M. Total HK25 $337.0M → $409.2M. Line match is INFERRED; the 10-Q calling it CRE at 6/30 supports it |
| Combination watch, `bank-lending-to-private-credit` | **No third new name.** New at Q3: VLY $18.5M, EGBN $9.5M. Cohort NDFI nonaccrual fell, $223.3M → $215.3M. ⚠️ My 11/06 "third cohort bank" line was badly drawn: nine banks held some at both dates, WAL $122.5M largest and flat since 6/30 |
| `V1V3-ACCELERATE` | Not renamed. THRESHOLDS.tsv untouched; WALTER packet sent; review re-dated 11/20 |
| Exit rail | Leg 2 graded, table §1 |

**Note on (d), not an answer to it.** On the 14 chosen banks only, nonaccrual up and allowance down fit 6 at Q2 → Q3 (CFG, EGBN, FLG by $2K, HBAN, VLY, ZION) against 3 at Q1 → Q2 (FLG, OZK, ZION). Valley's shape is not unique in the cohort. These banks were picked for risk, so this says nothing about the population.

**Side list (WQ-624 A), beside the score, in no statistic:**

| $M | Preferred 6/30 → 9/30 | NexBank 6/30 → 9/30 |
|---|---:|---:|
| Multifamily 30-89 | 62.8 → 143.1 | 24.9 → 75.2 |
| Multifamily nonaccrual | 27.4 → 80.0 | 1.9 → 1.9 |
| Non-owner 30-89 | 19.2 → 33.4 | 0 → 5.0 |
| Non-owner nonaccrual | 62.0 → 71.0 | 33.4 → 35.5 |
| Total nonaccrual | 98.2 → 159.8 | 101.5 → 86.7 |
| Total loans | 6,279 → 6,267 | 9,339 → 8,682 |
| Foreclosed property | 3.0 → 11.5 | 40.9 → 11.4 |
| MI3 | 0 | 0 |

No new fact against the 11/05 scan. Preferred's 10-Q (REG-31) most likely Mon 11/9 at the FDIC.

## 6. Funding confirms, WQ-318, bank-level basis

`funding-Q3.tsv`. Reported beside the release grades; only CUBI N is newly graded.

| Bank | NIB 6/30 → 9/30 | FHLB advances | Uninsured share | Reading |
|---|---:|---:|---:|---|
| CUBI | +3.9% | +3.8% | 44.3% → 43.1% | F none |
| CFG | −1.7% | **+31.4%**, $6.36B → $8.36B | 47.5% → 47.8% | F3 confirmed, matches 10/16 |
| WAL | **−7.4%**, share 33.8% → 31.3% | −10.3% | 38.1% → 39.7% | F1 on this basis. Frame: inside the declared deposit program reads INCONCLUSIVE. WAL desk's |
| OZK | −0.2% | **$0 → $600M** | 32.5% → 32.3% | Any-FHLB limb met on this basis, OZK desk's |
| FLG | +5.6% | flat | 28.9% → 29.1% | None |
| EGBN | −0.9% | $100M → $0 | 27.7% → 26.6% | None |

⚠️ **Brokered deposits break at 9/30: do not compare the line across that date.** RCON2365 falls by about two-thirds at WAL, CFG, FLG and EGBN while RC-O G803 (brokered reciprocal) goes blank at all six banks. The falls land exactly where G803 was nonzero, so reciprocal deposits appear to have left the line (INFERRED; I did not read the FFIEC instruction or the rule behind it). Like-for-like, 6/30 net of G803: WAL +6.9%, CFG +29.4%, FLG +22.6%, OZK +19.9%, CUBI −8.0%, EGBN −32.4%. No F3 grade rests on this. Any fleet screen using 2365 inherits the break.

## 7. Regional-bank put thesis

**It changes nothing.** No score, gate, threshold or trade moves.

| Direction | Evidence |
|---|---|
| Against tier-wide | Cohort total-CRE bad-loan rate fell; no mid-pack bank passed the rate test; WAL's nonaccrual plus foreclosed property fell |
| For wider | c = 3 on the letter; multifamily rate up at SSB, doubled; EGBN severe; the shape in the note above; side-list late loans |
| Weakens this desk's tools | The matrix showed no skill, so "concentrated at FLG, EGBN, AMTB" rests on levels and named mechanisms, not on a tested ranking |
| Still open | (d) to (f) are the direct test of tier-wide vs name-specific and are UNKNOWN; FDIC QBP ~late November; REG-03 |

The live claim, severity concentrated not tier-wide, stands on Q3 levels. TRADE §2b records no candidate. TERRY constructs; Will decides.

## 8. Verified, inferred, unknown

- **VERIFIED:** every Call Report figure and statistic above, by command in this folder.
- **INFERRED:** the FLG line match; the reciprocal reading of the brokered break; HBAN new commitments.
- **UNKNOWN:** (a), (d), (e), (f) until the FDIC posts; Friedberg primary; HBAN step cause; WAL hotel loss content; the $99M WAL life-science loan's location (WAL desk).
- **Skipped:** matrix re-score, no letter. FFIEC bulk, PROME's term. **Three ledgers on the same 11/07 cadence not refreshed:** `NDFI_COHORT.tsv`, `RUNWAY_COHORT.tsv`, `ACL_ROLLFORWARD_COHORT.tsv`, all last refreshed 8/20 or thereabouts and flagged +79d by the staleness check; `scripts/` holds no NDFI builder. Q3 NDFI lines for the 14 sit in `05_extras.out`. Carried to a later session, not part of this run's brief.
- **Instrument fixes, own scripts, no value changed:** `mi3_cohort_screen.py` wrote CRLF into an LF ledger, now LF; `cre_rcn_cohort.py` stamped a hardcoded 9/26 refresh date, now today's. Both ledgers rewritten from the same day's cache.
