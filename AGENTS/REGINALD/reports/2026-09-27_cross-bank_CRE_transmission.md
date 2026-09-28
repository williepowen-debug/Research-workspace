# CRE → regional-bank losses: cross-bank comparison (REGINALD leg, 2026-09-27)

**Asked by:** PROME task, relaying Will 17:24 ET (`PROME/plans/2026-09-27_cre-to-bank-loss-transmission-PLAN.md`, e614dee5e). **Research only.** No score, threshold, tool or trade changes; nothing here is a proposal.
**Reuses:** matrix v2.0 (`BANK_EXPOSURE_MATRIX.md`, 8/20) · 9/26 loss bridge as corrected (`reports/2026-09-26_CRE_top3_loss_bridge.md`, b93e3ac58 + this session) · `workbook/CRE_RCN_COHORT.tsv` (FFIEC Call Reports, 14 banks × 5 quarters, pulled 9/26) · Nano forensics (`reports/2026-09-27_nano-banc-failure-forensics.md`) · `thesis/CHANGELOG.md` 8/13 entry.
**New work this session:** none pulled. Two cohort aggregates (§A3) were computed from the existing 9/26 ledger. The recipe is in §E.

## The answer first

- **Bank losses from commercial real estate (CRE) are concentrated, not tier-wide.** That is on the evidence I can see: 14 named banks through 6/30/26, plus one national four-ratio screen.
- Across the cohort, CRE problem loans and CRE net charge-offs both **fell** year on year. Only **OZK** had a sharp new rise.
- **The property market is broader than the bank losses so far.** Multifamily delinquency is rising, the Washington DC/Northern Virginia office cluster is under stress, and regional banks are foreclosing more. Those reach bank losses with a lag of one to several quarters. My instruments measure closed quarters, so **"concentrated" is a statement about 6/30, not about Q3.**
- **The three rankings disagree on names because they measure different things, not because the evidence conflicts.** EGBN appears in all three. The one conclusion all three share is **"not tier-wide."**
- **Nano Banc does not change this.** Its capital was destroyed mostly by legal costs. Nationally, no other bank matched its profile on the four ratios (none met even three). Its one lesson for the cohort is **reserve coverage collapsing while bad loans rose**, and on that measure FLG, AMTB and EGBN are the banks below 100%.

---

## A. OBSERVED (primary, dated, cited)

### A1. Three rankings, three instruments

| Ranking | Date | What it measures | Names at the top | What it cannot see |
|---|---|---|---|---|
| **Thesis-retirement verdict** | 8/13 (`thesis/CHANGELOG.md` L118) | **Qualitative synthesis** of five desk tests (Q1 cohort NCO split 6/8; CRE delinquency by bank size 6/20; EGBN Q2 7/25; FL small-bank watch-card 4-of-4 revert 8/10; benign large-cap Q2) | **OZK / EGBN**, "not tier-wide" | No uniform instrument. The names reflect where the desk's work was, not a cross-bank measure. |
| **Matrix v2.0** | 8/20, 6/30/26 Call Reports | **Two instrumented channels only:** ① SR 07-1 CRE concentration (construction + multifamily + non-owner-occupied ÷ total capital, 300% line) ② **bank-wide** nonaccrual % + a point if reserves < nonaccrual | **FLG 6 · EGBN 5 · AMTB 5**; OZK and WAL both 2 | Not CRE-specific (AMTB's credit points are mostly non-CRE: $50M of $169M nonaccrual). **Blind to foreclosed property**, so OZK's $288.1M looks like 154% reserve coverage but is 78% with the foreclosed property counted (matrix §3d). Point-in-time. 14 names chosen under earlier priors. The six other channels are held by their owners (§6). |
| **9/26 loss bridge** | 9/26, Q2-26 10-Qs | **Scenario loss on named CRE pools**, net of reserves, as a multiple of one year of pre-provision revenue (PPNR) and as a hit to CET1 capital | FLG **8.4–10.5×** PPNR · EGBN **1.6–2.3×** · OZK **0.6×** | Only 3 banks. The loss rates are **my assumptions** (§B). It measures earnings capacity against a scenario, not an observed loss. |

**Reconciliation:**
- **(a) → (b):** when the verdict was instrumented on 8/20, it held ("3 of 14 elevated, 8 score ≤2") but **moved names**: FLG in, OZK out. STATUS has carried FLG/EGBN/AMTB since 8/20. ⚠️ PROME's brief cites the 8/13 OZK/EGBN wording; **the live STATUS claim is the 8/20 one.**
- **(b) → (c):** on 9/26 I cut the matrix to CRE. AMTB came out (non-CRE credit). OZK went back in, because its foreclosed CRE is invisible to the matrix. **So OZK's 8/13 inclusion was right for a reason the 8/20 instrument could not see.**
- **FLG ranks 1st on (b) and (c) for different reasons.** On (b) it is concentration 327.5% + nonaccrual 4.88% + reserves covering 29% of nonaccrual. On (c) the 8–11× is driven as much by **thin earnings** (TTM PPNR $143M, 10-Q) as by loss size, and its CRE loss rates have **no market anchor** (bridge §3, "ASSUMPTION ONLY").

### A2. Where each top name's CRE loss comes from (each has a named, bank-specific mechanism)

| Bank | Mechanism (from filings) | Source |
|---|---|---|
| **FLG** | NYC rent-regulated multifamily: cash flow squeezed (debt-service coverage 1.01×) and rate resets. 20.45% of the original balance of rent-regulated nonaccruals is already recognised ((351 + 76) / 2,088). The $133M gap between the two charge-off schedules is **structural, and its location cannot be determined** (FLG KB-FLG-061/066). | Deck s16 (8-K acc 0000910073-26-000065); 10-Q acc -26-000068 |
| **EGBN** | DC office largely cleaned up (criticized $287M → $77M), but most remaining office values rest on pre-6/30/25 appraisals, and its own re-appraisals ran −14% to −29%. Multifamily: 4 criticized loans ($155.8M) mature Aug–Dec 2026 with debt-service coverage of 0.15–0.89×. **Basis (D5, re-verified at the deck 9/27):** EGBN Q2-26 earnings deck (8-K acc 0001050441-26-000088) special-mention and substandard >$10M tables, as of 6/30/26, maturities 8/1–12/31/2026. The 4 multifamily loans are apartments in Prince George's $56.0M (SS, 0.63×), DC $42.9M (SM, 0.67×), Other US $36.4M (SM, 0.89×) and DC $20.5M (SS, 0.15×), totalling **$155.8M**. The **"7 loans / $249M"** figure is ALL property types with coverage <1.0×. It adds 2 storage loans ($56.2M, $15.0M) and the Fairfax office ($22.1M), which makes it a whole-window criticized figure, **not a multifamily one**. The full window is 9 loans, $287.6M. | Q2-26 10-Q acc 0001050441-26-000096; deck acc -000088 |
| **OZK** | Construction/lab loans that failed to refinance, then foreclosure. Foreclosed property **$150M → $288.1M in one quarter**, carried at 86–100% of appraisal. Its own vacant Seattle office sold at **58% of appraisal**. | Call Report 6/30/26; OZK desk |

### A3. Breadth across the 14-bank cohort (FFIEC Call Reports, 6/30/25 → 6/30/26; CRE = construction + multifamily + non-owner-occupied; "bad" = nonaccrual + 90 days past due)

| Measure | 6/30/25 | 6/30/26 | Banks rising |
|---|---:|---:|---|
| CRE bad-loan rate, cohort | 2.46% | **2.23%** | **7 of 14** (OZK, WAL, SBCF, AMTB, FLG, VLY, CUBI) |
| … excluding FLG | 1.37% | **1.20%** | |
| Rose >50% **and** above 1% | | | **only OZK** (0.04% → 1.34%) |
| H1 CRE net charge-offs, cohort | $528M | **$452M** | **6 of 14**; notable: WAL $26.6M → $58.8M, OZK $15.8M → $47.2M |
| … excluding FLG | $338M | **$291M** | |
| Foreclosed property (all types) | $507M | **$530M** | OZK +$129M; WAL −$92M |

⇒ **In aggregate the cohort's CRE credit improved. The deterioration is at named banks, and OZK is the only new one.** WAL's charge-offs doubled but are single-credit (Cantor; the WAL desk owns that call).

### A4. Nano Banc (failed 9/25), the national check
- Four-ratio screen on **all 4,313 filers at 6/30/26** (FDIC API): noncurrent >10% · uninsured deposits >50% · equity/assets <6% · CRE concentration >300%.
  - **Only Nano met all four; no other bank met three.**
  - In my cohort, **none met two.** One ratio each: BKU (uninsured deposits 58%), FLG (CRE 328%), VLY (CRE 320%).
  - (Forensics §4.) ⚠️ This is a **lagging** screen: it would have scored Nano at 1 leg at 12/31/23.
- **Cause of failure:** mostly legal costs (2025 legal expense $46.3M, the largest charge in a −$75.3M loss). **The FDIC's loss is on the CRE assets**: ≈$120M ≈ 17% of $690.9M on the 9/22 books (DFPI Exh. A). That is my scenario figure; the FDIC's own is $114M on 6/30 assets.
- **The one transferable lesson:** reserves fell from 109% of noncurrent loans (12/23) to **10%** (12/25) while noncurrent rose. Nano would have flagged at 33% on my matrix's reserve leg five quarters before it failed. **In my cohort, three banks are below 100% today: FLG 29% · AMTB 51% · EGBN 88%** (6/30/26).

### A5. Market side (consumed from owners, not re-derived)
- **Multifamily:** Freddie multifamily delinquency **0.64% [Aug]**, the 4th rise in a row from 0.42% in February. Fannie **0.61% [Jul]**. CMBS multifamily 7.69% [Aug], flat. (HOMER, issuer primary, 9/26.)
- **CRE distress:** CREED's 9/26 map finds 2026 distress is mostly failure to refinance, with **multifamily the one type where cash-flow stress is rising**. The DC/Northern Virginia office cluster is the densest new CMBS cluster.
- **FDIC Q2 Quarterly Banking Profile (QBP):** at regional banks ($10–250B), foreclosed CRE rose **$723.9M → $915.3M (+26.4%)** while their noncurrent rate fell 1.39 → 1.22%. **Regionals foreclosing, the largest banks charging off.** This is an accounting-scale comparison, not an attribution. CREED's `CREED-T-03` (the FDIC's non-owner-occupied CRE noncurrent measure) has **not** fired.

---

## B. SCENARIO ASSUMPTIONS (mine unless named)

| Assumption | Where it bites | Basis |
|---|---|---|
| Pool loss rates (FLG nonaccrual multifamily 8% / 20%; FLG CRE pools 10% / 25% etc.) | The FLG 8.4–10.5× multiple | **FLG CRE pools: assumption only, no market anchor.** The multifamily stress is cross-checked against BCB's NJ/NY problem-pool sale at ≤79% of face (8-K 9/25), a small bank's self-selected pool. |
| OZK lab (RaDD) loss **65%** | OZK $656M stress | **Top of the OZK desk's band, 50–65% ($275–360M on $555M funded)**, adopted 9/26 *(label corrected 9/27 per OZK packet 2b4c996f4: OZK's band is 50–65% = $275–360M on $555M funded; 65% is its top)* |
| EGBN non-office haircut **13.3%** | EGBN multifamily | EGBN's own H1-26 exit haircut |
| General reserve allocated pro-rata by pool | High end of each reserve-credit range | Banks do not disclose it by grade; **my allocation** |
| PPNR = trailing four quarters, no forward growth; losses land with no earnings offset | The multiples and CET1 figures | Simplification. Read as multiples, never as a yes/no. |
| Nano ≈$120M loss / 17% | Nano's own loss only. **NOT a mark for any cohort pool** (no type or lien match; CREED §B4) | Equity + estimated FDIC loss on 9/22 books; a **zero-adjustment scenario** until the FDIC–Sunwest purchase agreement (P&A) posts |

---

## C. UNKNOWNS

1. **Q3.** Every bank-level figure here is as of 6/30. The rate level (10-year 5.18% [9/25], the highest since 2007) and the multifamily delinquency rise are post-quarter and not yet in any bank print.
2. **The population.** The cohort is 14 names picked under earlier (MI3-era) priors. The four-ratio national screen covers everyone but only ratios that lag. **No national CRE-specific leading screen exists.** The MI3 / reserve-collapse markers at Nano are n=1 and not adopted.
3. **Office is not separable** in the Call Report (it sits inside owner- and non-owner-occupied).
4. **Unsecured CRE finance booked as C&I (MI3)** is reported but unscored. Rank citations are on hold until the 11/07 re-run.
5. **FLG's $133M gap:** location not determinable. Neither loss-at-exit nor accruing-loan appraisal write-downs leads (KB-FLG-066).
6. **Values on OZK's foreclosed property:** $288M carried at 86–100% of appraisal against one comparable sale at 58%.
7. **Nano:** P&A terms, the claims bar date, and who holds its liens senior to WAL now (DEWEY is checking the recorders).
8. **The six channels owned by other desks** (NDFI, private credit, funding, etc.) are not in this comparison.

---

## D. What would change the conclusion, and which way

| Observation | Date | Moves toward |
|---|---|---|
| **Q3 CRE nonaccrual / charge-offs at the mid-pack names** (WAL, VLY 320% concentration, SSB, BKU, SBCF): ≥3 of them with CRE bad-loan rate up >50% QoQ or a new foreclosure build | Earnings ~10/20–28 (estimates); Call Reports → my run **11/07** | **BROADER** |
| **FDIC Q3 QBP:** a second consecutive rise in regional foreclosed CRE **and** `CREED-T-03` firing | ~late Nov | **BROADER** |
| **Nano P&A / FDIC loss estimate** revised up materially from $114M | check-by **Fri 10/9**; the Fed OIG loss review ~3/2027 | **Evidence about small-bank Southern California CRE values only. By itself it moves no bank's scenario rate.** At most it is weak directional evidence, pool by pool, and only where a type-and-lien match is shown. ~~Harsher market marks on small-bank CRE → raises every scenario rate, not the ranking~~ *(amended 9/27 on CATO's review via Will/PROME, and CREED transfer test §B4 cd4674c5e: Nano's pool is neighbourhood retail, medical office, small multifamily and several second liens, and it matches no FLG, EGBN or OZK pool on type or lien)* |
| **EGBN's 4 criticized multifamily loans ($155.8M, Aug–Dec maturities)** pay off or extend at par; FLG multifamily special mention ≤ $2,757M | EGBN Q3 10-Q ~early Nov; FLG Q3 | **CONCENTRATED holds, and the scenarios overstate.** If they go to held-for-sale at a haircut, EGBN/FLG severity rises, but still concentrated. |
| **OZK foreclosed-property sale** priced near 58% rather than 86–100% of appraisal | Any OZK 8-K / Q3 | OZK severity **up** (concentrated) |
| Freddie multifamily delinquency through ~0.75% while the cohort's multifamily bad-loan rate stays flat | Monthly | The **lag widens**. Transmission is pending, not absent. |

**The one to watch first:** the Q3 prints at the **mid-pack** banks, not the top three. The top three are already named. Breadth shows up, or doesn't, in banks nobody is watching.

---

## E. Reproduce §A3
From `workbook/CRE_RCN_COHORT.tsv`, per bank:
- **Balance** = `bal_con + bal_mf + bal_noo`.
- **Bad** = `na_{con,mf,noo} + pd90_{con,mf,noo}`.
- **H1 net charge-offs** = Σ(`co_ytd_*` − `rec_ytd_*`) over con/mf/noo at the 6/30 year-to-date rows.
- **Foreclosed** = `oreo_total_k`.

Owner-occupied CRE is excluded, per SR 07-1. Computed 2026-09-27 by an inline script; no new pull.

---

## F. Q2-26 WORKOUT CHECK: how problem CRE got resolved (WQ-312, one-time; Will-approved 20:25 ET)

**Scope:** a one-time integration of Q2-26 (H1 where only half-year is disclosed) problem-CRE resolutions at FLG · OZK · WAL · EGBN · VLY.
- The four fields are kept separate so no dollar counts twice: **F1** what happened · **F2** where the cash came from · **F3** exposure retained · **F4** loss already recognised.
- **Not a standing ledger.** Existing filings and desk reports only. No score, tool or trade.
- **UNDISCLOSED funding is a limit, not a signal.** Successes and failures are tested the same way.

**Row sources (each desk owns its rows; not restated here beyond the totals):**
- **OZK:** `AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md` (68fd0f4d5)
- **FLG:** `AGENTS/FLG/reports/2026-09-27_WQ312_Q2_workout_rows.md` (485507d09)
- **WAL:** `AGENTS/WAL/research/2026-09-27_WQ312-WAL-Q2-workout-rows.md` (171338055). ⚠️ W-2 Cantor and W-4 LAM are **fraud / C&I, not CRE**, so they are excluded from the CRE totals.
- **EGBN + VLY (REGINALD-filled):** §F.1 below
- **Observability:** CREED `AGENTS/CREED/analysis/2026-09-27_WQ312_workout-funding-observability.md` (38f5e3c7a)

### F.1 EGBN and VLY rows (REGINALD; no desk owns them)
### EGBN — Q2-26 (REGINALD-filled; no desk owns EGBN)
Sources:
- **[Q]** 10-Q Q2-26, acc 0001050441-26-000096 (Note 4, Note 11)
- **[D]** Q2 deck, acc 0001050441-26-000088 (slides 16, 19, 24, 25)
- **[D1]** Q1 deck
- Derivations in `reports/2026-09-26_CRE_top3_dossiers/{dossier_EGBN,q2_EGBN}.md`

| id | balance $M | qtr | F1 what happened | F2 cash source | F3 retained | F4 loss recognised | later | source |
|---|---:|---|---|---|---|---|---|---|
| E1 **AGGREGATE**: HFS pipeline, 10 loans sold | carrying **161.5** sold; transfers in at FV **126.7** | Q2 | partial charge-off at transfer → to HFS → **sold** | buyer: **UNDISCLOSED** (buyer equity vs any EGBN financing not stated) | none disclosed; **$49.7M still in HFS at 6/30, 100% "under executed contracts"** | **CO on transfer $25.1M**; sale **gain $2.2M** over carrying (~101–103% of post-mark carrying) | n/a | [D s16]; [Q] Note 4; H1 − Q1 DERIVED |
| E2 **AGGREGATE**: nonaccrual paydowns | **14.7** | Q2 | paid off / paid down | **UNDISCLOSED** | none on these | N/D | n/a | deck NAL roll [D s24] |
| E3 **AGGREGATE**: nonaccrual charge-offs, retained book | **25.0** | Q2 | partial charge-off (retained) | none | residual balances stay in nonaccrual ($111.1M total at 6/30) | **$25.0M CO**; up to ~80% consumed Q1 specific reserves (specific ACL 38.4 → 18.5) | nonaccrual | [D s24]; [Q] ACL |
| E3a ↳ DC office NAL (loan-level, inside E3) | 36.5 → **19.2** | Q2 | partial charge-off, retained | none | **residual $19.2M nonaccrual** | **~$17.3M CO** against its Q1 specific; collateral value $44.6M → $38.5M (−13.7%) | nonaccrual | [D1 s27] vs [D s24–25] |
| E4 **AGGREGATE**: nonaccrual → HFS | **14.0** | Q2 | to HFS (feeds E1) | — | — | inside E1's $25.1M | — | [D s24] |
| E5 Fairfax apartment (Q1 substandard, 61% LTV) | 48.7 | Q2 | **left the >$10M criticized list; route UNDISCLOSED** (payoff / upgrade / HFS all possible) | UNDISCLOSED | UNDISCLOSED | N/D | unknown | [D1] vs [D] s25 |
| E6 Prince George's apartment (substandard, 88% LTV, DSCR 0.63) | 56.0 | Q2 | **renewed/extended** 4/21 → 8/21/26 | none (extension) | **renewed loan $56.0M** | N/D (accruing; no specific disclosed) | **matured again 8/21/26, outcome UNDISCLOSED** | [D s25] |
| *(out of window)* DC apartment (substandard) | 35.4 | **Q3** | paid off in full after 6/30 (deck footnote 5) | UNDISCLOSED | none | none shown | — | [D s25 fn 5]; **not counted** |

**EGBN coverage (Q2):**
- **Denominator:** nonaccrual outflow **$53.7M** (paydowns 14.7 + CO 25.0 + to HFS 14.0; roll 128.8 + 36.0 in − 53.7 = 111.1), **plus** HFS sold (carrying $161.5M).
- **Loan-identified rows** (E3a $17.3M written off, E5 $48.7M, E6 $56.0M) cover **~$122M**. **Everything else is aggregate.**
- **F2 funding source is UNDISCLOSED for 100% of the dollars that left.**

### VLY — Q2-26 (REGINALD-filled; no desk owns VLY)
Sources:
- **[ER]** release, 8-K EX-99.1, acc 0000714310-26-000036
- **[DK]** deck, same accession (slides 25, 32)
- **[10Q]** acc 0000714310-26-000041
- Detail in `reports/2026-09-27_VLY_CRE_transmission.md`

| id | balance $M | qtr | F1 what happened | F2 cash source | F3 retained | F4 loss recognised | later | source |
|---|---:|---|---|---|---|---|---|---|
| V1 **AGGREGATE**, **all maturing CRE (NOT problem-specific)** | **1,082** of 1,457 | Q2 | **renewed/retained by VLY** | none (VLY renewal) | **renewed loans $1,082M** | N/D | N/D | [DK s32] |
| V2 **AGGREGATE**, all maturing CRE | **341** | Q2 | paid off and left | **UNDISCLOSED** (borrower funds vs third-party refinancing not split) | none | N/D | n/a | [DK s32] |
| V3 office loan at maturity | 25.8 | Q2 | **moved to nonaccrual** (a failure, not a resolution) | none | **$25.8M nonaccrual** | N/D | nonaccrual | [DK s32 fn 1] |
| V4 multifamily loan at maturity | 6.8 | Q2 | modified | none | modified loan $6.8M | N/D | unknown | [DK s32 fn 1] |
| V5 **AGGREGATE**: CRE modifications to borrowers in financial difficulty | **116.0** | Q2 | **modified: payment delay $108.2M (wtd 8-month deferral)** + term extension $7.7M + rate cut $0.07M | none | **modified loans $116.0M** | N/D | **unknown for the Q2 cohort.** Of the 12-month stock ($139.5M), $5.5M re-defaulted. | [10Q] modification tables |
| V6 **AGGREGATE**: criticized CRE decline | **~200** (3.3B → 3.1B) | Q2 | "upgrades and payoffs" (**split UNDISCLOSED**) | UNDISCLOSED | UNDISCLOSED | N/D | n/a | [DK s25] |
| V7 **AGGREGATE**: CRE net charge-offs | **~11.7** | Q2 | partial charge-offs of non-performing CRE | none | residual in nonaccrual ($256.1M CRE NA at 6/30) | **~$11.7M** (Call Report YTD differences) | nonaccrual | [ER]; Call Report |
| V8 non-performing CRE relationship | 9.1 | **Q1** (H1) | to HFS (Q4-25) → **sold** | buyer: UNDISCLOSED | none | Q4-25 write-down at transfer N/D; **sale gain $0.77M** over HFS carrying | n/a | [10Q] Loan Portfolio Sales |

**VLY coverage (Q2):**
- **Denominators:** CRE maturities **$1,457M** (V1 + V2 + V3 + V4 = 100% of that line, but only $32.6M is loan-identified) · criticized CRE decline **~$0.2B** (V6, 0% loan-identified) · nonaccrual outflow **NOT DISCLOSED** (VLY publishes no nonaccrual roll-forward).
- **Loan-identified rows** (V3, V4, V8) cover **$41.7M**. **Everything else is aggregate.**
- **F2 funding source is UNDISCLOSED** for V2 and V6. V1 and V5 are VLY's own renewal or modification, with no new cash.

⚠️ **Possible overlap inside VLY:** the $6.8M multifamily loan "modified" at maturity (V4) may sit inside the $116.0M of Q2 modifications (V5). It is not disclosed, so it is not added twice in the totals below.

### F.2 Totals by field ($M, Q2-26 unless marked; press-grade marked **P-G**)

**F1: what happened** (problem-CRE only; the all-maturity and all-repayment aggregates are listed separately)

| Outcome | FLG | OZK | EGBN | VLY | WAL |
|---|---:|---:|---:|---:|---:|
| Paid off / sold / paid down, **mix unsplit** | 190 (nonaccrual payoffs + dispositions) | — | 14.7 paydowns | — | "six-credit" path: 2 closed by the Q2 call, **$ UNDISCLOSED** |
| Sold (via HFS) | inside 190 | 6.9 OREO sales (H1) | **161.5** carrying sold (10 loans) | 9.1 (Q1) | |
| Paid off **with a loss** | — | 63.6 (San Carlos) | — | — | |
| Paid off via third-party refi | 80.5 (**P-G**, performing loan) | — | — | — | |
| Cured / recapitalised to pass | 6 (cures) | **156.4** (Sullivan: new sponsor equity) | — | — | $99M life-science loan **brought current end-June, still nonaccrual** (not a cure; borrower funding UNDISCLOSED) |
| **Modified / deferred / extended (retained)** | **382** (MF 259 + CRE 123) | 37 extensions ($ N/D; **booked as $0 hardship modifications**) | 56.0 (Prince George's extension) | **116.0** (108.2 payment delay) | |
| Partial charge-off, loan retained | 60 | inside foreclosures | 25.0 | ~11.7 | |
| **Foreclosed → OREO/REO** | 2 | **175.7** pre-charge-off (Seattle ×2, Atlanta) | — | — | **+7 properties, "primarily office"**. OREO **$123.2M → $126.1M** (+$2.9M, Call Report), so the adds were small or offset by undisclosed sales |
| Moved to nonaccrual at maturity (failure) | — | — | — | 25.8 (office) | |
| Route UNDISCLOSED | — | — | 48.7 (Fairfax apartment exited the criticized list) | ~200 (criticized decline, "upgrades and payoffs") | |
| *Aggregate, not problem-specific* | ~1,100 "par payoffs" (~39% substandard) | 2,920 RESG repayments | — | 1,082 renewed + 341 paid off (all maturing CRE) | — |
| *Exposure ADDED as a workout tactic (not a resolution)* | Pinnacle buyer loan 338.5 (Q1, **P-G**) | — | — | — | **+$51M senior-lien purchases** (to $64M; Cantor collateral, WAL's own cash) |

**F2: where the cash came from.** Stated per bank, not summed, because the perimeters differ.

| Source | Evidence |
|---|---|
| **Third-party refinance** | **One named case: FLG R8, $80.5M** (Zions → Barclays CMBS), **P-G**, performing loan, 6% discount. **No filing names a third-party takeout at any bank.** |
| **New sponsor equity** | OZK Sullivan $156.4M (amount of equity UNDISCLOSED); OZK The Jack pending |
| **Buyer financed by the selling bank** | **FLG Pinnacle (Q1, P-G): FLG lent the buyer $338.5M of the $451.3M price (75%).** Undisclosed at every other bank. |
| **The bank's own cash, buying senior liens ahead of itself** | **WAL: +$51M in Q2 (to $64M)** of non-performing senior liens on Cantor collateral. Exposure **added**, not resolved. |
| None (charge-off, foreclosure, modification, extension) | Every retained-loan row |
| **UNDISCLOSED** | **FLG $190M + ~$1.1B · OZK $63.6M + $2.92B · EGBN $161.5M + $14.7M + $48.7M · VLY $341M + ~$200M · WAL six-credit closings ($ N/D) + the $99M borrower's cure funding.** **This is where most of the dollars sit.** |

**F3: exposure retained**
- **Modified or extended loans kept:** FLG $382M · VLY $116M · EGBN $56M · OZK 37 extensions (balances N/D).
- **New OREO:** OZK $141.2M (carried at 95–100% of appraisal, **untested by sale**) · FLG REO $8M total.
- **New loan to a buyer:** FLG $338.5M (P-G, Q1).
- **WAL:** $99M life-science loan retained in nonaccrual · +7 OREO properties · +$51M purchased senior liens.
- **Recapitalised loan:** OZK Sullivan (size N/D).
- **Still in HFS under contract:** EGBN $49.7M.

**F4: loss already recognised, where the severity is measurable**

| Exit type | Severity | Basis |
|---|---:|---|
| OZK foreclosures (3 loans) | **19.6%** (range 7–28%) | charge-off ÷ pre-charge-off balance, $34.5M / $175.7M |
| OZK San Carlos payoff | **23.3%** | $14.8M / $63.6M |
| EGBN HFS transfers | **16.5%** Q2 (13.3% H1) | charge-off at transfer ÷ (FV + charge-off); then sold at ~101–103% of the marked value |
| FLG Pinnacle sale | price ≈ **80% of debt** (P-G) | $451.3M vs >$564M debt; FLG carrying value UNDISCLOSED |
| FLG R8 performing refi | **6.0%** (P-G) | $4.8M / $80.5M |

- **Recognised charge-offs, Q2:** FLG $60M (schedule line; ACL MF $81M + CRE $13M) · EGBN $25.1M at transfer + $25.0M retained · OZK $49.3M on named loans · VLY ~$11.7M CRE · **WAL $0 on its named CRE** ($99M loan, OREO valuation losses zero). WAL's large H1 charge-offs were fraud / C&I.
- ⇒ **Problem-CRE exits that are measurable cluster at ~13–28% of balance. The one performing exit was 6%.** For scale, my bridge's multifamily nonaccrual scenario is 8% base / 20% stress on top of what is already recognised.

### F.3 Coverage per bank (what share of the period's resolution activity the rows can see)

| Bank | Denominator (named) | F1 known | F2 + F3 known | Loan-level |
|---|---|---|---|---|
| **FLG** | Q2 nonaccrual outflow **$258M** | 100% (aggregate) | **26%** ($68M: cures, REO, charge-offs) | **$0** |
| **OZK** | Q2 RESG repayments **$2.92B** | credit-level **14%** ($402M) | for the $402M only | ~33% of the 3/31 classified + criticized book |
| **EGBN** | Q2 nonaccrual outflow **$53.7M** + HFS sold **$161.5M** | 100% (aggregate) | **0% of cash exits** (F2 UNDISCLOSED) | ~$122M (E3a / E5 / E6) |
| **VLY** | Q2 CRE maturities **$1,457M**; criticized decline ~$0.2B; **no nonaccrual roll-forward published** | 100% of maturities (aggregate) | **0% of the $341M payoffs** | $41.7M |
| **WAL** | H1 net charge-offs **$263.5M**; **no resolution-dollar denominator exists** (six-credit path and OREO are count / guidance only) | 58% of H1 NCO is **fraud / C&I** (LAM $126.4M + Cantor $26.1M), not CRE | CRE: **$0** recognised on the $99M loan and the +7 OREO | $99M (W-1) |

### F.4 What it establishes, and what it does not

**1. "Successful" resolutions: outcomes are visible, the takeout funding is not.**
- Every bank discloses that problem loans **left**: FLG $190M nonaccrual payoffs, EGBN $161.5M sold at or above its marks, OZK $2.92B repayments.
- **The cash behind them is UNDISCLOSED for essentially every dollar.** CREED confirms it is **not observable in aggregate** without loan identifiers.
- **The only named outside-cash exits are press-grade, and each carries a caveat:** FLG R8 was refinanced out **at a 6% loss**. FLG's one large named exit, Pinnacle, was **75% financed by FLG itself**.
- ⇒ **"Par payoffs show the refinancing market is open" is an INFERENCE, not an observation** (CREED).
- The only clean primary successes are **OZK Sullivan** (new sponsor equity, cured to pass; loan retained) and **EGBN's sales at or above their post-write-down marks** (so the marks held; the price as a share of par is UNDISCLOSED).

**2. Retained risk is large, and it is where the failure evidence is.**
- **FLG:** modifications $382M in Q2. **47% of MF loans modified in the prior 12 months were past due at 6/30, and $286M of MF modifications re-defaulted in H1** (primary, KB-FLG-069). **That is the strongest failure signal in the set.**
- **VLY:** $108M of 8-month payment deferrals. Untested until ~Q1-27.
- **OZK:** $141M of new OREO, carried at 95–100% of appraisal and not yet sold. Its one vacant-office comparable sold at 58% of appraisal (OZK desk).
- **EGBN:** extended a substandard 88%-LTV loan, and it matured again 8/21 with an undisclosed outcome.
- **WAL:** the $99M life-science walk-away loan is **$0 charged off, appraisal pending**. +7 office-led OREO properties carry **zero** valuation loss. **Loss deferred, not absent** (WAL's own read).
- ⚠️ **The hardship-modification tables are not comparable across banks.** OZK booked **$0 CRE** hardship modifications against **37 RESG extensions** in the same quarter. VLY and FLG booked $116M and $382M. **The difference is a classification practice, not necessarily credit.** A cross-bank "modification rate" read off these tables would be wrong.

**3. Recognised losses are real where they can be measured, and consistent with severe-but-not-catastrophic.**
- Measurable problem-exit severities are **13–28%**, with **OZK's foreclosures carried at 95–100% of appraisal untested**.
- **WAL and OZK recognise the least loss at foreclosure** (WAL zero OREO valuation loss; OZK 95–100% of appraisal). EGBN takes its loss at transfer and then proves it by sale. **Recognition timing differs by bank, so the same economic loss shows up in different quarters.**
- EGBN's marks were **validated by sales** (sold at ~101–103% of marked value). OZK's OREO marks and FLG's modification book are **not yet validated**.

**4. What remains unknown.**
- (a) **Takeout funding** for ~all aggregate payoffs.
- (b) Whether any bank **financed buyers** other than FLG on Pinnacle.
- (c) **Sale price as % of par** anywhere (only % of carrying value is disclosed).
- (d) Whether OZK's OREO marks hold on sale.
- (e) How VLY's deferrals and FLG's Q2 modification cohort perform.
- (f) **The named sample is biased toward failures** (CREED): regulators and issuers name problem loans, not clean payoffs. So the observable set over-weights what went wrong. **Do not read the failure share of named rows as a failure rate.**

**Next observation:**
- Q3 prints (~10/20–10/23; all dates estimates) and Q3 10-Qs (~early–mid Nov).
- **FLG's modification re-defaults** in the Q3 hardship-modification tables.
- **The first sales of OZK's OREO** (price vs 95–100% carrying value).
- **VLY's Q2 multifamily past-due cohort.**
- Any disclosure of **bank-financed buyers**.
- Rising re-defaults or financed exits → the workouts are **keeping** the risk. Disclosed third-party takeouts at or near carrying value → the exits are **removing** it.
