# WQ-312 — Flagstar Q2-26 problem-CRE workout rows (written 2026-09-27 20:27 ET, from `date`)

**Commissioned by:** PROME (WQ-312, approved by Will 20:25 ET), a one-time check. **Integrator:** REGINALD. **Author:** FLG.
**Bounds:** existing filings and FLG reports only; no tools, scores or trades. **UNDISCLOSED funding is a limit, not a signal.** Successes and failures are tested the same way.
**Entity:** Flagstar Bank, N.A. (CIK 0000910073), one legal entity since Oct-2025.
**Primaries:** 10-Q Q2-26 (acc 0000910073-26-000068: non-accrual roll-forward; modifications to borrowers experiencing financial difficulty (FDM) tables; ACL roll-forward) · Q2 earnings release and deck (8-K acc 0000910073-26-000065) · 10-Q Q1-26 (acc …-26-000047). FLG ledger `workbook/NONACCRUAL_FLOW.tsv` (Q-derived rows, identity ties). Press only where marked **PRESS-GRADE**.

**Anti-double-count rule used here:** rows **R1–R4** are the four legs of the **Q2 non-accrual roll-forward** and sum to its outflow. **R5** (modifications) and **R6** (par payoffs) are **separate issuer series that can overlap R1–R4** and are **not added** to the coverage line. **R7** (Pinnacle) and **R8** (discounted payoff) are named events, and the note on each row says which series it sits inside.

---

## Rows

| id | Balance ($M) | Quarter | F1 WHAT HAPPENED | F2 CASH SOURCE | F3 EXPOSURE RETAINED | F4 LOSS ALREADY RECOGNISED | Later performance | Cite |
|---|---:|---|---|---|---|---|---|---|
| **R1** Non-accrual → payoffs, incl. dispositions and principal paydowns | **190** | Q2-26 | Paid off / sold / paid down. **The mix is not split** | **UNDISCLOSED** (borrower, third-party refi or buyer; whether FLG financed any buyer is not disclosed) | **UNDISCLOSED** (no disclosure of new FLG loans to buyers) | Not disclosed per loan. Charge-offs at exit may sit here rather than in R2 (KB-FLG-061/066: undetermined) | n/a | 10-Q Q2-26 roll-forward; NONACCRUAL_FLOW Q2-derived |
| **R2** Non-accrual → charge-offs | **60** | Q2-26 | Partial / full charge-off | none | Residual stays in non-accrual unless exited via R1 | **$60M** (schedule line). Q2 ACL gross charge-offs: **MF $81M, CRE $13M**. The ACL figure exceeds the schedule line (perimeter gap, KB-061) | n/a | 10-Q Q2-26 roll-forward + Note 6 |
| **R3** Non-accrual → restored to performing (cure) | **6** | Q2-26 | Returned to accrual | Borrower (implied by cure) | Full loan retained, now accruing | Not disclosed per loan | Not disclosed | 10-Q roll-forward |
| **R4** Non-accrual → transferred to other assets (foreclosure / REO) | **2** | Q2-26 | Foreclosed → repossessed asset | none | **REO**. Repossessed assets **$8M** at 6/30/26 ($11M at 12/31/25) | Recorded at fair value less cost to sell; later declines go through expense | Not disclosed | 10-Q roll-forward + NPA table |
| **R5** Modifications to borrowers in difficulty — **MF** | **259** (H1: 364) | Q2-26 | **Modified.** Q2 split: rate reduction $134M · term extension $85M · both $40M. Weighted average **7.68% → 5.17%**, **+1.2 years** | none | **Full modified loan retained** ($259M) | Not disclosed per loan | 🔴 **FAILURE SIGNAL.** MF loans modified in the prior 12 months, at 6/30/26: **$375M**, of which **current $199M · 30–89 DPD $23M · 90+ DPD $153M ⇒ 47% past due**. MF modifications that **re-defaulted within 12 months: $286M in H1-26** ($29M in Q2). ⚠️ The past-due stock includes H2-25 vintages; it cannot be matched to the Q2 cohort | 10-Q Q2-26 FDM tables |
| **R5b** Modifications — **CRE** | **123** (H1: 159) | Q2-26 | Modified: rate reduction $110M · extension $4M · both $9M. **8.63% → 6.57%**, **+0.9 years** | none | Full modified loan retained ($123M) | Not disclosed | CRE modified in the prior 12 months: **$160M**, current $128M · 30–89 $19M · 90+ $13M ⇒ **20% past due**. Re-defaulted within 12 months: **$69M in H1-26** ($39M in Q2) | 10-Q Q2-26 FDM tables |
| **R6** MF + CRE **par payoffs** (aggregate issuer series) | **~1,100** (39% substandard ⇒ ~$429M derived) | Q2-26 | Paid off at par (company label) | **UNDISCLOSED** (borrower vs third-party refi; whether any refi was by FLG itself is not disclosed) | **UNDISCLOSED** | "Par" = no loss on the payoff amount. **Prior charge-offs on these loans not disclosed** | n/a | Q2 release headline and CRE section ("unchanged compared to first quarter") |
| **R7** **Pinnacle Group** — the Q1 "single borrower relationship undergoing bankruptcy" — **PRESS-GRADE; identity not confirmed by the issuer** | Debt **>$564M** (press; FLG carrying value **UNDISCLOSED**) | **Q1-26** (closed 2026-03-31) | Foreclosure started → **Chapter 11** (May 2025) → court-approved sale (1/19/26) → **sold** to Summit Properties for **$451.3M** | **Buyer equity ~$113M + buyer financed by FLG $338.5M (~75%)** | **New loan $338.5M** to the buyer (grade and terms **UNDISCLOSED**) | **UNDISCLOSED** for the relationship. 10-Q: H1 MF+CRE gross charge-offs $193M were "primarily driven by appraisals … and the resolution of a single borrower relationship undergoing bankruptcy." Not separable | New loan: **not disclosed** | KB-FLG-067 (Multifamily Dive 2026-01-20; TRD 2026-03-31); 10-Q Q2-26 text. **Sits inside Q1's R1-equivalent ($646M)** |
| **R8** Discounted payoff, performing NYC rent-stabilized loan — **PRESS-GRADE** | **80.5** | Q2-26 (reported 4/27/26) | Paid off at a **$4.8M discount** (~6.0%) via refinance | **Third-party refi** (Zions $83M; note into a Barclays CMBS) | none | **$4.8M** loss at payoff | n/a | KB-FLG-065 (Bisnow 2026-04-27). **Performing loan, so outside the non-accrual schedule and outside "par" payoffs** |

**Context, not counted (net change or multi-period, not Q2 resolutions):** NYC rent-regulated MF **−$338M QoQ** in Q2 (net balance change, deck) · NYC rent-regulated payoffs since 2024 **$2.0B, 56% from substandard** (cumulative, deck) · classified loans **$9.7B → $8.5B** in H1 (10-Q).

---

## COVERAGE LINE

**Denominator: Q2-26 non-accrual outflow = $258M** (payoffs/dispositions 190 + charge-offs 60 + cures 6 + to other assets 2; NONACCRUAL_FLOW Q2-derived, identity ties).
- **What happened (F1):** covered for **$258M / $258M = 100%**, at the aggregate level only (R1–R4).
- **Cash source and exposure retained (F2 + F3):** known for **$6M (cures) + $2M (REO) + $60M (charge-offs, no cash) = $68M / $258M = 26%**. **The $190M payoff/disposition leg (74%) is UNDISCLOSED on both** — a limit, not a signal.
- **Named, loan-level Q2 resolutions inside this denominator: $0 / $258M.** The one named Q2 event (R8, $80.5M) was a performing loan and sits outside it.
- **H1 view, for reference:** H1 outflow **$955M**. Pinnacle (R7) is the only named resolution. Its **carrying** amount in the roll-forward is undisclosed; against its **>$564M debt** it would be **≤~59%** of H1 outflow, press-grade.
- **Not in the denominator** (separate series, would double-count): R5/R5b modifications ($382M in Q2), which retain the loan, and R6 par payoffs (~$1.1B), which mix pass and substandard loans and are partly accruing.

---

## OBSERVED / SCENARIO ASSUMPTIONS / UNKNOWNS

**OBSERVED:** all figures in R1–R6 are primary (10-Q or Q2 release/deck). R7 and R8 are press-grade and marked.

**SCENARIO ASSUMPTIONS:** R7 = Pinnacle rests on timing, bankruptcy, a single relationship and Flagstar as lender (KB-067). The issuer does not name the borrower.

**UNKNOWNS:**
1. The split of R1's $190M between borrower payoff, third-party refi, note sale and buyer-financed sale.
2. Whether FLG financed buyers on any exit other than Pinnacle.
3. Prior charge-offs on the R6 par-payoff loans.
4. The R5 cohort match (Q2 modifications vs the 12-month past-due stock).
5. The grade and performance of the $338.5M Summit loan.

**Successes and failures on the same test:**
- **Success-side evidence:** R6 par payoffs (F2 undisclosed) · R3 cures ($6M, small) · R8 third-party refi (at a 6% loss).
- **Failure-side evidence:** R5/R5b re-defaults and past-dues (primary, material: 47% of 12-month MF modifications past due) · R2 charge-offs · R7 exit below debt with 75% retained exposure (press-grade).

## Next observation that would change this read
**Q3-26 10-Q (~11/9):**
- the Q3 FDM tables: do MF modification re-defaults keep accumulating?
- the roll-forward's payoff leg
- any disclosure of loans to buyers of FLG-held collateral

**Q3 call (~10/23):** whether management quantifies buyer-financing on dispositions.
**Direction:** re-defaults rising, or buyer-financing disclosed as material ⇒ workouts are **retaining** risk. Payoffs holding with F2 disclosed as third-party ⇒ exits are **removing** it.

— FLG
