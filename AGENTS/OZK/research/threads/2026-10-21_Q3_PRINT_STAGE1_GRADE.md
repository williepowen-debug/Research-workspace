# OZK Q3-2026 print — Stage-1 grade (written materials) · DOCKET D:L520 · WQ-313 item ③

**Written:** 2026-10-21 (Wed), session start 08:55 ET (`date`), OZK desk spawned by PROME (Tier-1 WQ-184 due-row wake, WQ-465 A).
**Primary:** FDIC FLNG **12022** attachment 1, "Bank OZK Q32026 Form 8K - Earnings Release, Management Comments & Financial Supplement.pdf", filed 2026-10-20 (release 3:05 p.m. CT). Saved `raw/Q3_2026_8K_bundle.pdf`, sha256 `81ba170dad2095bde8fe9af5243fd8713a5ceec33f15d409b6039b94cffb1293`. `flng_watch.py` 2026-10-21 08:55 ET: 2 filings after id 11981 (12019 = the 10/12 8-K, 12022 = this bundle).
**Stage-2 (the 10/21 08:30 ET call) is PENDING:** at 09:01 ET no transcript existed (web search; Quartr MCP needs re-authentication). Under the pre-print card ("release read first, full call second; no absence-based resolution before both") nothing below resolves by absence.
**Pre-registered letters graded against:** `workbook/Q3_2026_SCORING_CARD.md` (committed 961218af6 / aea8a07a7, 2026-10-12, before the print) and the "Next observations" table of `research/threads/2026-09-27_CRE_LOSS_TRANSMISSION_OZK_LEG.md`. Nothing in either was edited; results are appended.

Tokens: **VERIFIED** = read at the primary page · **DERIVED** = arithmetic on primary figures · **INFERRED** · **UNKNOWN** · **PENDING** (call/10-Q/Call Report).

## 1. Headline numbers (Q3-26 vs Q2-26)

| Metric | Q2-26 | Q3-26 | Source / token |
|---|---|---|---|
| Net income to common / diluted EPS | $163.3M / $1.49 | **$164.3M / $1.50** | 99.1 p.1 · VERIFIED |
| PPNR | $259.4M | **$261.4M** | MC App. reconciliation · VERIFIED |
| Provision / net charge-offs | $45.6M / $56.3M | **$47.8M / $44.5M** | MC p.22 · VERIFIED |
| Annualized NCO ratio | 0.69% | **0.53%** (9M **0.59%**) | MC p.20 · VERIFIED |
| ACL (ALL + unfunded reserve) | $617.8M | **$621.1M** ($469.9M ALL = 1.38% of loans; $151.3M unfunded) | MC p.22 · VERIFIED; 617.8 − 44.5 + 47.8 = 621.1 DERIVED ties |
| Special mention | $616M | **$303M** | MC Fig 22 p.23 · VERIFIED |
| Substandard accrual | $73M | **$182M** | Fig 22 · VERIFIED |
| Substandard non-accrual | $300M | **$89M** | Fig 22 · VERIFIED |
| Foreclosed assets (OREO) | $293M | **$420M** (+43%) | Fig 22 · VERIFIED |
| **Total classified + criticized** | **$1,282M** | **$995M** (−$287M, −22.4%) | Fig 22 · VERIFIED / DERIVED |
| Loans past due | $298M / 0.92% | **$88M / 0.26%** | Fig 22 · VERIFIED |
| Nonperforming assets | $593M / 1.42% | **$510M / 1.18%** | Fig 22 · VERIFIED |
| RESG total commitments | $25.7B | **$25.4B** | MC p.12 · VERIFIED |
| RESG repayments & other | $2.92B | **$1.65B** (4Q $9.16B; Oct 1–19 ≈$0.69B) | MC p.12 Fig 12 · VERIFIED |
| Expenses on nonperforming assets (insurance/taxes/other + OREO write-downs) | $5.57M + $2.65M | **$9.80M + $4.27M = $14.07M** | MC non-interest expense table · VERIFIED / DERIVED |
| CET1 | 11.80% | **11.44%** (preliminary) | MC p.35 Fig 34 · VERIFIED |
| TBV / share | $48.41 | **$47.50** (−$0.91, attributed by issuer to AOCI/securities) | MC p.35–36 · VERIFIED |
| Buyback | none in Q2 (prior program expired) | **0.65M sh, $31.4M @ $48.21**; Oct 1–19 0.52M sh, $23.8M @ $45.85 | MC p.34 · VERIFIED |
| Sub notes ($350M) | 2.75% fixed | reset 10/1 to 3M Term SOFR + 209bp; **6.14% for Q4-26**; Q4 NIM drag 3bp; Tier 2 −20% | MC p.35 · VERIFIED — **supersedes the desk's ≈6.19% estimate** (drag ≈$12.0M/yr Act/360, was ≈$12.3M) |

## 2. Pre-registered "next observations" (thread 9/27) — graded

| Pre-registered observation | Branch the print took | Grade |
|---|---|---|
| **RaDD "~92-day" report-back** (toward stress = specific reserve, downgrade, or extension without paydown/new equity; against = executed extension **with** curtailment or new cash equity) | Executed 10/9 to **December 2029** with **$100M new capital** from sponsor + mezzanine lender; $4.3M fees accreted; original variable rate kept; 45-day bridge preceded it; a negotiated agreement now governs future capital contributions; sponsor + partners have invested ≈**$1.23B** in total. No reserve, downgrade or charge-off disclosed. New appraisal (Fig 26: Life Science, $915M commitment) LTV **50.3% → 68.4%** | **AGAINST-STRESS branch** ✅ (MC p.28–29, VERIFIED). Report-back delivered on time |
| Foreclosed-property sale prices vs carrying (8150 Sunset, Seattle, Atlanta) | **No OREO sale priced in Q3.** LA land LOI became a sales contract that **did not close**; Santa Monica carrying cut **$4.0M** to $40.8M (95% of Sept appraisal); Seattle ×2, Atlanta, Chicago carrying unchanged | **INSUFFICIENT** — per WQ-313's own fallback: *the delayed-loss hypothesis stays a hypothesis, neither confirmed nor retired* |
| **Boston 10 Prospect** ($169.3M, $0 reserve): sale closes, or OZK takes title | **Sale failed; OZK took title** after a **$37.3M charge-off**; OREO **$132.0M = 80% of the Sept-2026 as-is appraisal** (appraisal ≈$165M, DERIVED) | **TOWARD-STRESS branch** fired. Size **$37.3M**, below the $85M bridge-stress figure the thread carried |
| Special mention $616M: reversal or migration | **One named migration:** Boston, MA **land** $105.9M (77% as-is LTV, Dec-25 appraisal, matures Dec-26) SM → substandard accrual. SM net **−$313M**; the remaining ≈−$207M flow (upgrade / payoff / other) is not itemized in writing | **MIXED** — one migration toward stress; net fall against. Credit-level flow **PENDING** (call/10-Q) |
| Q3 NCO vs the ≤55bps kill line; buyback | NCO **0.53%** ≤ 55bps; buyback $31.4M executed | Kill-§2 **re-opens honestly but does NOT fire**: its letter is "sustained sub-50bps through Q2–Q3"; Q2 was 0.69% and Q3 0.53% is above 50bps. The 50/55 wording gap is not reconciled here (card instruction) |
| Q3 Call Report RIAD5409 / RIAD5415 | — | **PENDING** ~Nov 1–10 (FFIEC JWT expires 11/5 — Will action) |

## 3. Q3 card rows R1–R6 (RaDD) and W1–W14 (workouts)

| Row | Observation (9/30 unless stated) | Interpretation | Status |
|---|---|---|---|
| R1 recognition | No RaDD charge-off, reserve or loss named. Q3 bank-wide NCO $44.5M, of which Boston $37.3M ⇒ ≤$7.2M net unattributed to a named credit. Pooled-reserve share UNKNOWN | Charge-off leg ≈ nil by every written source; reserve leg undisclosed (pooled ACL) | **OZK-09 OPEN / STUCK** (attribution guard) — leans FALSE |
| R2 rating | Not in Fig 23 substandard list or OREO list; each classified bucket (SM $303M, sub-accrual $182M, nonaccrual $89M) is smaller than RaDD's balance (post-paydown $579.1M) | **Pass-rated at 9/30 by elimination** | INFERRED-HIGH |
| R3 draw budget | Agreement "to govern the terms of future additional capital contributions, if needed"; readvance of $121.3M paydown not addressed | Weakens on sponsor-commitment side; readvance risk unchanged | UNKNOWN on budget |
| R4 capital providers | "sponsor and mezzanine lender" contributed $100M; prior contributions $87.1M (6/24), $8.7M (9/24), $9.3M (11/24), $82.0M (1/25) | Named funded support | VERIFIED (legal form UNKNOWN) |
| R5 funding reconciliation | Not disclosed | — | UNKNOWN / PENDING 10-Q |
| R6 leasing | None disclosed; LTV 68.4% on new appraisal (basis per 10/12 8-K: as-stabilized) | Collateral value fell 18.1 LTV points | No lease evidence |
| W1 Sullivan | No Q3 mention | — | PENDING |
| W3/W4 Seattle U-District OREO | $56.1M / $48.5M, carrying unchanged | No sale | Unresolved |
| W5 Atlanta OREO | $36.6M; "meaningful leasing interest" | Intent only | Unresolved |
| W6 OREO sales | **No OREO sale priced in Q3**; OREO write-downs $4.27M; stock $292.7M → $420.4M | Pile growing, untested by sales | Unresolved |
| W7 The Jack (Seattle Pioneer Square office, $25.9M nonaccrual) | Recapitalized "as expected" by sponsor + new capital partner → **new pass-rated loan** | WEAKENS stress (debt-on-debt credit cured to pass); any Q3 loss inside the ≤$7.2M residual | VERIFIED outcome |
| W8 Wauwatosa hotel ($16.7M nonaccrual) | **Paid off from the property sale**, "negligible recovery" | WEAKENS — cash payoff at carrying | VERIFIED |
| W9 Boston 10 Prospect | Failed sale → title, $37.3M c/o, OREO $132.0M | **STRENGTHENS** — largest named loss; now recognized | VERIFIED |
| W10 Baltimore land ($40.0M, 303 DPD) | Note under sale contract; close Q4-26/Q1-27; "net proceeds substantially equal" to balance; else title | Contract, not cash | Unresolved |
| W11 8150 Sunset (LA land OREO $54.5M) | Contract did not close; new counterparty | Mild strengthen (failed close), no price | Unresolved |
| W12 RaDD | see R1–R6 | | |
| W13 RESG activity | Repayments $1.65B; commitments $25.4B | Runoff continues | — |
| W14 modifications | 50 in Q3; 711 over 17 quarters; $1.5B extra sponsor equity ($956M reserves + $581M paydowns) | Issuer frame; not a cure proof | — |

**Q2 adverse-selection conjunction (OZK-07, Q2 TRUE) did NOT repeat in Q3:** classified + criticized fell 22.4% while RESG commitments fell 1.2% — both falling is the card's contrary case. OZK-07 itself is not re-graded.

## 4. Registered predictions and kill rails — Q3 collection only (no terminal grade)

| Letter | Q3 input | Note |
|---|---|---|
| OZK-02 (≥32% problem-category share by Q4) | Not collected this pass (property-type commitment table) | GAP — collect at Q4 |
| OZK-03 (FY RESG NCO ≥60bps) | Bank-wide 9M NCO 0.59%; no RESG NCO line printed | P-OZK-5 scope gap stands |
| OZK-04 (RESG roster ≥3.8% by Q4; ≤3.0% invalidates) | Roster basis RESG substandard + RESG OREO: 40.0 + 105.9 + 23.6 + 416.0 = **$585.5M / $25.4B = 2.31%** (Q2 same basis $569.4M / $25.7B = 2.22%) | DERIVED, basis INFERRED (Q1 $719M baseline roster differed); diagnostic only |
| OZK-09 | R1 above | OPEN/STUCK; 45% scoring prior unchanged |
| Kill §1 | Past due $88M | Already FIRED-LITERAL (Q2); unchanged |
| Kill §2 | Q3 0.53% | Not fired (§2 above) |
| Kill §3 | Fresh capital observed 10/9 | Letter's pre-maturity window unchanged |

## 5. Earnings and capital burden

PPNR $261.4M covers provision $47.8M **5.5×**; the $14.1M of nonperforming-asset expense is already inside PPNR. Net income flat QoQ. CET1 −36bp to 11.44% alongside +$1.57B loan growth and $31.4M buyback — credit is not the disclosed driver. **Credit costs are an earnings drag, not a capital event, on Q3 evidence** (same conclusion as the 9/27 thread).

## 6. Net read for the thesis

Q3 is **predominantly contrary** to RESERVOIR's stress-accumulation claim: aggregate classified/criticized, past-due, nonaccrual and NPA all fell; the quarter's NCO ratio dropped under the kill line; RaDD was extended with cash; two named problem credits (Jack, Wauwatosa) resolved without disclosed loss. **What confirms** the mechanism: the Boston failed sale → title → $37.3M loss; a new $105.9M Boston land substandard; OREO up 43% to $420M with **zero priced sales** — so the "marks untested by sales" question is still open and OREO carrying costs are rising ($14.1M/qtr). The largest named loss candidate has now been recognized at $37.3M.

## 7. Position exposure (figures only; TERRY owns the card, Will the order)

Will's OZK Nov-20 $40P ×4 (broker basis $322.66, 10/7 capture). Pulls 2026-10-21 09:01 ET, before the open: OZK last **$46.16** (10/20 close, set before the 4:05 p.m. ET release; no post-release trade observed by the tool) — strike **$6.16 / 13.3% below**. Put last **$0.20** (10/20 15:58 ET); bid/ask 0/0 pre-open ⇒ ≈**$80** marked across 4 contracts. P/TBV at $46.16 vs $47.50 = **0.97×**. To finish in the money OZK must fall more than 13.3% in the 30 days to 11/20; this print names no remaining near-term loss event of that scale.
