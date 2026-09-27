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
