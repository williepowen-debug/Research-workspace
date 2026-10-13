# Cross-bank workout outcome bridge — bounded pre-Q3 build

**Authority:** Will directly asked REGINALD to do the first portion of the follow-up research after reviewing the October 12 regional-bank policy/CRE report, then directed REGINALD to continue with the available evidence. **As of:** October 12, 2026. **Artifact:** `workbook/WORKOUT_OUTCOME_BRIDGE.tsv`. **Receipt:** `domain/sources/2026-10-12_workout-outcome-bridge-receipt.json`.

## Result

The bridge contains **21 rows across OZK, EGBN, VLY and WAL**. It is intentionally not a cross-bank recovery total. Five rows reconcile a same-basis arithmetic bridge; WAL's three reported components also reconcile exactly to the parent classified-asset change. The others preserve a partial bridge, an unresolved named-loan baseline or a point-in-time stock transition. `UNKNOWN` means the issuer did not disclose the field; it never means zero. `N/A` means the field does not apply to the defined object.

The useful first conclusion is narrower than “extend and pretend” or “clean cure”:

- **Only RaDD supplies a named fresh-capital amount in this tranche:** 100.0 of sponsor/capital-partner money plus 21.3 of an existing reserve reduced funded principal to 579.1. Because the entire 121.3 may be readvanced and the 915.0 commitment remains, this is a real liquidity intervention but not certified permanent bank de-risking. The issuer's October 12 8-K is the governing primary; REGINALD consumed the complete owner report and its preserved filing.
- **OZK's other Q2 paths are economically different.** San Carlos exited with a 14.8 charge-off, but exact payoff cash/provider is absent. Three foreclosures recognized 34.5 of charge-offs and left 141.2 of OREO. Sullivan removed a 156.4 old nonaccrual and produced a pass-rated replacement loan whose new balance and cash support are undisclosed. A payoff, a foreclosure and a recapitalization cannot share one “cure” label.
- **EGBN shows the strongest completed portfolio cleanup, but carrying value is not cash.** The Q2 nonaccrual-HFI bridge exactly reconciles 128.761 + 36.038 inflows − 14.658 paydowns − 24.982 charge-offs − 14.035 HFS transfers = 111.124. The HFS bridge separately reconciles 55.702 + 155.486 inflows − 161.525 sale carrying value = 49.663. Exact gross/net cash proceeds and original-par recoveries are not disclosed. [EGBN's Q2 deck](https://www.sec.gov/Archives/edgar/data/1050441/000105044126000088/final-2q2026egbnearnings.htm) is the direct primary for both roll-forwards.
- **VLY and WAL rows are diagnostic baselines, not completed workout outcomes.** VLY disclosed 116.0 of Q2 CRE modifications, including 108.2 of significant payment delays, while multifamily 30–89-day past dues rose 9.4 to 101.5; the issuer does not identify cohort overlap. Of 1,457 of Q2 CRE maturities, 1,082 was retained by Valley, 341 paid off and left, and 33 was modified or otherwise handled; rounded components sum to 1,456. One 5.454 CRE term-extension loan modified in the prior 12 months had defaulted by June 30. WAL's bank-wide classified assets rose 1,070 to 1,128; the row is not CRE-only. [WAL's Q2 release](https://www.sec.gov/Archives/edgar/data/1212545/000162828026049001/pressrelease-6302026.htm) supplies the company table.

## Second-tranche findings

- **EGBN's full near-term named-loan set now has a baseline.** The bridge adds the 56.196 Montgomery storage facility (special mention, 72% LTV, 0.93 DSCR, August 10 maturity) and the 14.996 Anne Arundel storage facility (substandard, 77% LTV, 0.26 DSCR, September 30 maturity). Together with Prince George's and Fairfax, all four Q2 loans selected for post-maturity observation are encoded. No issuer disclosure reviewed through October 12 establishes a payoff, extension, HFS transfer, nonaccrual migration or OREO outcome, so all four remain `UNKNOWN`. A similar public project is not enough to identify a loan when the Q2 deck omits borrower and address.
- **VLY's 74.3% retention rate is lender behavior, not outside-market proof.** Valley retained 1,082 / 1,457 of Q2 maturities; 341 / 1,457, or 23.4%, paid off and left; 33 / 1,457, or 2.3%, was modified or otherwise handled. The slide footnote identifies a 25.8 office loan moved to nonaccrual and a 6.8 multifamily residential loan modified. The bridge therefore keeps “retained” separate from third-party exit proceeds.
- **VLY supplies one realized re-default observation.** Its June 30 10-Q reports 139.450 of CRE loans modified during the prior 12 months: 133.996 current and 5.454 at least 90 days past due. The same filing identifies the 5.454 as one term-extension loan that subsequently had a payment default, and its past-due table places that balance outside nonaccrual. This establishes failure to re-perform while still accruing, but not charge-off, recovery, cash support or ultimate disposition. The 250.109 year-earlier comparison is a changing trailing-window population, not cohort runoff.
- **WAL's parent change reconciles, but its economics do not.** Classified loans on accrual fell 15, nonaccrual loans rose 70, and repossessed assets rose 3; `-15 + 70 + 3 = +58`, exactly matching classified assets' rise from 1,070 to 1,128. Protective Cantor senior liens rose 51, arithmetically 87.9% of the parent change, but they are a subset within classified assets—not a fourth component—and the filing does not identify their bucket or establish new bank funding. The bridge marks that row `DO_NOT_SUM` and does not relabel Cantor as CRE.

## How to read the workbook

The accounting identity for a reconciled balance row is:

`opening + additions − reductions = ending`.

Every numeric term must use the row's stated measurement basis. Three controls prevent false precision:

1. **Measurement basis travels with the number.** Loan principal, HFS/OREO carrying value, property sale price, commitment and cash proceeds are not interchangeable.
2. **Residuals remain residuals.** San Carlos' 48.8 is the arithmetic remainder after the disclosed charge-off, not certified lender cash. VLY's 92.1 and WAL's 58.0 are endpoint stock changes, not cash flows.
3. **Overlap rows cannot be summed.** OZK's three named June foreclosures sit within the H1 bank-wide foreclosed-asset roll-forward. EGBN's HFI transfer-out and HFS inflow are cross-object views of related activity. The `Aggregation_Flag` and `Overlap_Group` columns make those constraints machine-visible.

`Outcome_Label` is descriptive, not a score:

- `CASH_DE_RISK` — sourced principal cash with no identified offsetting retained exposure on the defined object;
- `LOSS_RECOGNITION` — charge-off/write-down is the decisive observed event;
- `BUCKET_SHIFT` — exposure moved to HFS, OREO, a replacement loan or another classification;
- `BANK_FUNDED_CARRY` — lender supplied or capitalized additional exposure;
- `MIXED` — two or more of the above apply;
- `UNKNOWN` — the disclosed evidence cannot classify the economic outcome.

No row in this tranche is labeled `CASH_DE_RISK` on a standalone basis. That is not a bearish finding; it is a disclosure finding. San Carlos did extinguish the disclosed loan, EGBN did receive reported paydowns and sell HFS loans, and RaDD did receive fresh capital. The sources do not supply all fields needed to certify pure cash de-risking on a common basis.

## What the first tranche resolves—and does not

| Question | Current answer |
|---|---|
| Can falling problem-loan categories be treated as cash cures? | **No.** OZK and EGBN demonstrate charge-off, transfer, sale and replacement-loan paths. |
| Did RaDD receive real new capital? | **Yes, 100.0**, plus 21.3 existing reserve; the principal reduction is redrawable and the commitment unchanged. |
| Did EGBN execute real cleanup? | **Yes.** Paydowns, charges and completed HFS sales are observed. Exact loan-level cash recovery/original par remains unavailable. |
| Does VLY's modification cohort equal its multifamily past-due cohort? | **UNKNOWN.** The overlap is not disclosed. One 5.454 modified CRE loan did default, but it cannot be mapped to multifamily. |
| Does VLY's maturity disposition prove the external refinancing market is open? | **No.** Valley retained 74.3%; the 23.4% that paid off and left has no disclosed provider split. |
| Does WAL's aggregate bucket movement establish CRE deterioration? | **No.** The table is bank-wide. Its reported components reconcile, but Cantor is a subset and must not be summed or relabeled CRE. |

This work does **not** change REGINALD's frozen Q3 frame, bank scores, thresholds, predictions, calendar, trade posture or position records. It does not edit OZK, WAL or other peer-owned files.

## Best next fill

Use the already scheduled Q3 issuer materials to replace `UNKNOWN` fields, rather than opening a second monitoring rail:

1. **EGBN:** fill the Prince George's and Fairfax maturity outcomes; capture actual payoff, extension, HFS/nonaccrual/OREO movement and any attributable loss. These are the cleanest near-term loan-level tests.
2. **VLY:** test whether the 101.5 multifamily past-due stock cures or rolls, whether Q3 produces another large modification cohort, and whether the 5.5 re-default balance grows. Do not infer that a Q3 past-due cure resolves the eight-month deferral cohort.
3. **WAL:** decompose the 58.0 classified-asset increase by CRE versus LAM/Cantor and record cash/charge-off/retained-claim fields only where issuer disclosure permits.
4. **OZK:** use the owner desk's existing Q3 card for RaDD rating/accrual/redraw and for actual OREO sale cash or retained financing. Do not duplicate its live scoring surface.

The next material upgrade is not more rows; it is replacing the named-loan `UNKNOWN`s with same-basis cash, loss and retained-exposure fields.

## Source coverage and limits

The bridge consumes full or decisive-table primary work already completed on this desk and the OZK owner desk. The EGBN, VLY and WAL official sources were reopened on October 12. EGBN slide 16 directly reproduced both cited portfolio roll-forwards and slide 25 supplied the four named-loan baselines. VLY's full 10-Q and the official slide-32 image were retrieved from EDGAR and hashed in the receipt. The FDIC-hosted OZK PDF remained unavailable through the current web reader, so those rows rely on the pinned local full owner report and preserved-filing hash named in the receipt. No source silence is treated as a zero or a successful outcome.
