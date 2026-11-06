# BKU Q3 10-Q grade: FL frame cells, REG-32, FL aggregate FINAL

**Graded:** 2026-11-06 11:21 ET. **Owner:** REGINALD. **Task:** PROME doorbell 11/06 11:14 ET; CORAL packet `41475cdd6` (ungraded cell read). **Frame:** `reports/2026-09-24_FL_bank_rail_Q3_FROZEN_frame.md` with Amendments A1–A3, unedited.

## 1. Result

| Item | Grade |
|---|---|
| BKU CRE 30-89 accruing (primary) | **TRANSMITS** |
| BKU CRE 90+ | HOLDS |
| BKU CRE criticized QoQ | HOLDS |
| BKU class (A2.3: P transmits alone, T = 1) | **MIXED, FINAL** (all three cells read, A2.4) |
| REG-32 (72%, "both cells hold") | **FALSE** ("FALSE if either cell TRANSMITS") |
| FL aggregate (A3: H = 3, T = 0, m = 0) | **NO TRANSMISSION, FINAL** |
| Recognition lane leg (1), STATUS line 98 | Met, now final; legs (2) L180 11/07 and (3) REG-03 stay open |

CORAL's class (MIXED) and aggregate are confirmed. CORAL's limit 1 is closed by a source its packet did not use. Its limit 2 is confirmed and sharpened. Its limit 3 is narrowed. A frame defect is disclosed in §3.

## 2. Cells, read at primary

Filings read by me at SEC 11/06: 10-Q 9/30/26 acc 0001504008-26-000091 (`bku-20260930.htm`), Q2 10-Q acc 0001504008-26-000079 (`bku-20260630.htm`). Call Reports: BankUnited, N.A. (RSSD 3938186), FFIEC CDR facsimile, fresh pull 11/06, `use_cache=False`.

| Cell | 6/30/26 | 9/30/26 | Bar | Result | Locator |
|---|---:|---:|---|---|---|
| CRE 30-59 | $0 | $0 | | | Note 4, Past Due and Non-Accrual Loans, aging table, row CRE, both 10-Qs |
| CRE 60-89 | $0 | **$21,321K** | > $0 | met | same |
| CRE 30-89 | $0 | **$21,321K** | ≥ $15.6M | met | same |
| CRE 90+ | $6,084K | $6,018K | ≥ $12.2M | not met | same |
| CRE criticized | $481.290M | $427.390M | rises | fell $53.9M | MD&A risk-rating table: SM 33,868 + sub accruing 411,167 + sub non-accruing 36,255 vs 0 + 391,714 + 35,676 |

## 3. The "accruing" word, tested at the Call Report, and a frame defect

The 10-Q aging row is not split by accrual status. CORAL's packet inferred "most is accruing" from flat non-accrual. **That inference does not hold on its own:** a loan already on non-accrual and paying could go late without moving the non-accrual total, and CRE non-accrual of ~$29M sat in the Current column at 6/30.

**RC-N column A is defined as past due 30–89 days and still accruing, so it answers directly:**

| Date | RCONF179 other nonfarm nonres, 30-89 accruing | RCONF183 same, nonaccrual | RCON3499 multifamily 30-89 | RCONF173 other construction 30-89 |
|---|---:|---:|---:|---:|
| 9/30/25 | $0 | $102,891K | $0 | F173 $10,000K |
| 12/31/25 | $7,818K | $62,751K | $0 | F173 $0 |
| 3/31/26 | **$23,203K** | $59,194K | not pulled | not pulled |
| 6/30/26 | $0 | $36,256K | $0 | $0 |
| 9/30/26 | **$21,321K** | $35,676K | $0 | $0 |

**$21,321K ties to the 10-Q to the thousand, in the accruing column.** Limit 1 is closed: the cell is met on its literal word, and the loan(s) are non-owner-occupied nonfarm nonresidential. **Not multifamily, not construction or land.** Office, hotel, retail and industrial remain possible; the Call Report does not separate them.

Independent 10-Q cross-check: CRE non-accrual $35.676M ≈ non-owner-occupied $29.424M + SBA ~$6.25M (CRE 90+ $6.018M is about the $6M guaranteed SBA portion). The $29.424M equals the nine-month "Term Extension and Other than Insignificant Payment Delays" row, and at 6/30 both were $29.922M. That Q2 modification carried 2.0 years of payment deferral, so the one non-accrual loan group that could have sat in the late bucket had its payments deferred. Consistent with the RC-N reading.

**⚠️ FRAME DEFECT, DISCLOSED (frame header rule), not re-tuned.** The cell is labelled "accruing", but the $15.6M bar and the "Q4-25 level" came from the unsplit 10-Q aging row ($751K + $14,867K). On the accruing basis the Q4-25 figure was $7.818M. So the frozen bar is higher than the label's own basis implies. Effect on this grade: none, because $21.321M clears $15.6M on both bases. **Effect on the Q2 base-rate wording: the REG-32 note's "$15.6M [12/31/25], a Q1 spike" understates Q1 on the accruing basis ($23.2M at 3/31).** The Q1 10-Q aging row was not re-read here.

## 4. What the $21.3M is

- **Size:** 0.30% of CRE ($7,073.4M, 9/30). About 36% of the CRE allowance ($60.049M, 9/30; $58.571M, 6/30). 22.3% of CRE modified in the prior 12 months ($95.604M).
- **All of it sits in loans already modified for borrowers in financial difficulty** (modified-loan aging table: CRE 60-89 $21,321K of $95,604K; at 6/30, CRE $91,013K all current). The Q3 modified-and-defaulted table has no CRE row, so it is not a default by the filing's definition.
- **The pattern, new here:** this same accruing line read $23.2M at 3/31, $0 at 6/30, $21.3M at 9/30. Q2 carried $35.431M of CRE term extensions (weighted 0.4 year), and the 6/30 modified table was all current. **INFERENCE, not disclosed:** a loan late at 3/31, extended in Q2, late again by 9/30. If true, this is one credit that a short extension did not fix, which is seasoning, not a fresh default wave. The filing does not identify the loan(s), and I cannot prove it is the same borrower.
- **The 10-Q narrative does not discuss it.** MD&A says the special mention and substandard accruing tables are "All … performing". I did not read the Q3 call for this figure.
- **Location, UNKNOWN.** CRE is 46% Florida by collateral [9/30], and among the property types still possible: office 54%, hotel 75%, industrial 42%, retail 38% (10-Q MD&A CRE table). Nothing ties this balance to Florida. Multifamily is excluded, which removes the New York rent-regulated reading from this balance; it does not by itself settle any condo question.

**CONFIRMED / REFUTED / UNKNOWN (research standard):** my working expectation, REG-32 "both cells hold" at 72%, is **REFUTED** on the primary cell. No separate dated BKU expectation exists in `reports/2026-10-13_review-response_forward-judgments.md`. Forecast error, not missing disclosure. Incremental recognition: the CRE allowance rose $1.5M; no charge-off is tied to this balance; nothing here is a loss figure. Retained risk: the balance rolls to 90+ or non-accrual at 12/31.

**What changes the read.** Worse: the balance is 90+, non-accrual or charged off at the 12/31 Call Report (RCONF179 falls while F181 or F183 rises by a like amount) or a second CRE balance appears in the 30-89 line. Better: it clears with no matching rise in F181 or F183 and no charge-off. A cure via another modification is not a clean bill: log it as extended, not healed. No standing monitor is created; the existing Q4 Call Report read covers it.

## 5. Other items in the filing

- **Loans 90+ still accruing $28.885M [9/30] vs $0 [6/30]:** this is **C&I, not CRE.** RCON1607 (C&I 90+ accruing) $28,886K vs $0, CRE lines F181 $0. It drives non-performing loans to $263.8M (1.11%) from $223.9M (0.94%). Not a frame cell.
- **C&I non-accrual $140.0M vs $116.4M** (NPA table, non-SBA). Not a frame cell. Logged because the total bank's credit picture is worse than the frame's CRE-only lens shows.
- **Total criticized and classified fell $10M; CRE criticized fell $53.9M, so non-CRE rose.** C&I substandard accruing $235.8M vs $169.2M.

### FL-resi sub-read (§3, never enters the aggregate)
BKU 1-4 single family: non-accrual $23.673M vs $26.034M; 60-89 $5.757M vs $7.189M; 90+ $17.005M vs $18.630M; 30-59 $42.472M vs $39.911M. Non-accrual, 60-89 and 90+ fell; 30-59 rose. Florida is 7.2% of the residential book at 9/30 on the MD&A state table. **Handed to CORAL's leg. No condo-association book disclosed.**

## 6. Aggregate

| Name | Class | Final |
|---|---|---|
| AMTB | HOLDS | yes (10-Q read 11/05, acc 0001734342-26-000088) |
| SSB | HOLDS | yes, 11/05 |
| SBCF | HOLDS | yes, 11/05 |
| BKU | **MIXED** | yes, 11/06 |

A3: H = 3, T = 0, m = 0, so T + m < 2 and H ≥ 3: **NO TRANSMISSION, FINAL.** §5's "all four 10-Qs read" is met. No TRANSMISSION CONFIRMED packet trips. CORAL owns the combined L227 verdict.

**Do not over-read FINAL.** It says FL credit stress did not reach bank books at breadth in Q3 on four names. It is a four-name count in which BKU's primary cell did transmit, on one credit.

## 7. Trade route

No candidate, TRADE.md §2b. One modified credit at 0.30% of CRE; class MIXED; aggregate NO TRANSMISSION; BKU not on the book per POSITIONS. No score, threshold, gate or trade changed. Matrix scores re-read at the existing run, not here.

## 8. Verification scope

Read: both 10-Q HTML documents' loan note, MD&A CRE, risk-rating and NPA sections, as text extraction. Pulled: RC-N line items for five dates, values as printed above, with the 3/31 row limited to the lines shown. Not read: BKU Q3 call transcript, Q1 10-Q aging row, property-type charts (images; `(1)` footnotes only). Frame unedited. CORAL's Q2 and Q3 figures all reproduced.
