# EGBN — the Q4-2026 maturity wall (Will-directed deep dive, 2026-10-22 ~11:25 ET)

**Sources:**
- Eagle Bancorp Q3 8-K acc 0001050441-26-000110 (accepted 2026-10-22T00:26Z): deck slides 13, 16, 18, 19, 20, 21, each read as an image by REGINALD. Slides are saved in `domain/sources/2026-10-22_catchup/`.
- Q2 comparator: the Q2 deck text at `domain/sources/2026-10-20_EGBN_cash-outcome/Q2-deck.txt` (slide 25 criticized table) and `reports/2026-09-26_CRE_top3_dossiers/q2_EGBN.md`.
- Loan matching uses county + type + balance + maturity; Eagle publishes no loan IDs.
- The 10/22 10:00 ET call has **not** been heard. Scope: existing EGBN thread (CRE top-3, L35, L694 question); no new monitor, prediction or trade.

## 1. Bottom line
- **The wall is bigger than the multifamily chart suggests, and its risk is mostly refinancing and recognition timing, not loss size.**
  - About **$525M of identified loans mature between 10/27 and 12/30** (~8% of the $6.5B book): $146.9M criticized plus $378.6M pass-rated large loans.
  - On Eagle's own appraisals, plausible losses on the criticized part are **~$0–8M** if values hold and **~$20–31M** if values are 20–35% below appraisal. That is roughly ≤1.3 quarters of pre-provision revenue ($23.8M Q3) and **≤ $1.02 of the $38.00 TBV per share** before tax benefit and before any reserve already held.
- **Eagle's Q3 behaviour is extend, not exit.**
  - Of the four large criticized loans whose maturities fell in Q3, the two that can still be identified were **extended**: Prince George's apartments 8/21 → 12/21/26, now nonaccrual; Montgomery storage 8/10/26 → 2/10/27.
  - The other two (the Fairfax office loan and Anne Arundel storage) left the over-$10M list with **no disclosed destination**. Their absence is not a payoff.
- **The first test is in five days.** On **Tue 10/27**, a $42.7M DC apartment loan (special mention, DSCR 0.63) and a $27.7M Montgomery mixed-use loan (special mention, appraisal dated **10/18/2021**) mature.
- **⚠️ A disclosure discrepancy to put to the company.** The $20.5M DC apartment loan maturing 12/30 shows **LTV 84% on a $24.5M appraisal dated 6/13/2026 in the Q2 deck**, and **LTV 152% on a $13.5M appraisal with the same 6/13/2026 date in the Q3 deck**. The loan is still **accruing**, at DSCR 0.24.
  - Both rows are internally consistent (20.521/24.5 = 84%; 20.474/13.5 = 152%).
  - A likely explanation is a switch from a prospective ("as-stabilized") value to the "as-is" value in the same appraisal report. That is **INFERENCE**; the deck does not say.
  - This is the second appraisal-table inconsistency at Eagle this year: the Q1 deck printed the Prince George's appraisal as both $62.2M and $63.7M.
  - **Why it matters:** if other printed LTVs also rest on prospective values, they overstate the cushion.

## 2. The four criticized loans maturing in Q4 (deck s20, 9/30/26)
| Maturity | Loan | Balance | Rating / accrual | LTV · appraisal (date) | DSCR | Q2 → Q3 change |
|---|---|---:|---|---|---:|---|
| **Tue 10/27** | DC apartment | $42.685M | Special mention, accruing | 61% · $70.0M (**8/17/2026**) | 0.63 | New appraisal **−5.4%** ($74.0M 9/30/25 → $70.0M); DSCR 0.67 → 0.63; maturity unchanged |
| **Tue 10/27** | Montgomery mixed-use (mostly commercial) | $27.722M | Special mention, accruing | 53% · $52.6M (**10/18/2021**) | 0.75 | Unchanged; the appraisal is five years old |
| **Mon 12/21** | Prince George's apartments | $56.000M | Substandard, **nonaccrual** (#1 NAL, 33.7% of NALs) | 88% · $63.7M (3/9/2026) | 0.74 | Maturity re-extended 8/21 → 12/21; no principal paid; moved to nonaccrual (76.0% of Q3 NPL inflows, s19) |
| **Wed 12/30** | DC apartment | $20.474M | Substandard, **accruing** | **152%** · $13.5M (6/13/2026) | 0.24 | Q2 printed 84% · $24.5M (6/13/2026) · DSCR 0.15 — see §1 ⚠️ |
| | **Total** | **$146.9M** | | | | |

The Q2 list of nine criticized loans maturing Aug–Dec 2026 ($287.6M), traced to Q3:

| Q2 loan (maturity) | Q3 outcome |
|---|---|
| Montgomery storage $56.2M (8/10) | **Extended to 2/10/27**, still special mention, balance −$0.13M. The July call (SECONDARY transcript) reportedly targeted a year-end payoff; the new maturity sits past year-end. |
| Prince George's apartments $56.0M (8/21) | **Extended to 12/21; nonaccrual** |
| Fairfax office $22.1M (9/25) | **Off the over-$10M list; destination not disclosed.** HFS inflows were $0, so it was not moved to held-for-sale. Payoffs (−$107.8M) and upgrades (−$40.7M) are the other exits in the s13 waterfall. |
| Anne Arundel storage $15.0M (9/30, DSCR 0.26) | **Off the over-$10M list; destination not disclosed** |
| DC apartment $42.9M (10/27) | Still due 10/27 (above) |
| Montgomery mixed-use $27.7M (10/27) | Still due 10/27 (above) |
| DC office $10.8M (11/10) | **Off the special-mention over-$10M list; not disclosed** |
| "Other US" apartment $36.4M (11/30) | **Off both over-$10M lists; not disclosed** (too small for the top-25, whose floor is $48.9M) |
| DC apartment $20.5M (12/30) | Still due 12/30; appraisal value printed 45% lower (above) |

The desk's original four-apartment set ($155.8M: Prince George's, DC $42.9M, Other US $36.4M, DC $20.5M) now reads:
- **one** extended and nonaccrual
- **two** still due 10/27 and 12/30
- **one** with its outcome not disclosed.

**Genuine contrary evidence:**
- One criticized DC apartment loan ($35.4M) **was paid off in full** after 6/30 (Q2 footnote 5).
- The criticized book fell $759.6M → $648.4M, mostly through payoffs (−$107.8M, s13).

## 3. The pass-rated part of the wall (deck s21, top-25 loans)
| Maturity | Loan | Balance | Appraisal (date) · LTV |
|---|---|---:|---|
| Mon 11/30 | Montgomery apartment + retail, **construction** | $88.5M | $151.0M (5/9/2023) · 59% |
| Mon 11/30 | Prince William industrial, **construction** | $53.0M | $115.2M (9/15/2022) · 46% |
| Wed 12/23 | Montgomery apartment + retail, **construction** | $94.0M | $168.0M (11/14/2022) · 56% |
| Wed 12/23 | Falls Church apartments, income-producing | $88.1M | $185.6M (11/14/2022) · 47% |
| Tue 12/29 | DC assisted-living (CCRC) | $55.0M | $85.0M (8/17/2026) · 65% |
| | **Total** | **$378.6M** | |

- **Loss risk here is low.** Values would have to fall ~36–49% below the printed appraisals before these loans lose money (8% sale-cost assumption; break-even = 1 − LTV/0.92).
- **What this wall does carry:**
  - **Construction takeout risk.** Two Montgomery projects ($182.5M, which equals Montgomery's multifamily construction total on s29) need permanent financing at today's rates.
  - **Appraisal refresh.** Eagle's stated policy is that "appraisals refresh on upcoming maturity or modification" (s18), so most of these values date from 2022–23 and get re-tested now.
  - Eagle's own 2026 re-appraisals point both ways:

| Loan | Old appraisal | New appraisal | Change |
|---|---|---|---|
| DC apartment | $74.0M | $70.0M | −5% |
| DC apartment | $31.0M | $26.7M | −14% |
| Fairfax office | $24.3M | $26.6M | +9% |
| Q2 dossier range | — | — | −14% to −29% |

- **Valuation anchor:** the income-producing multifamily book shows debt yield 6.5% × LTV 62% ⇒ an implied appraisal cap rate of **~4.0%** (DERIVED, s16). If buyers price at 5.0–5.5% (an assumption; CREED owns market cap rates), values sit ~20–27% below appraisal. That is the "−20%" column below.
- The likeliest outcome is **migration** (pass → watch → criticized), which raises provisions and criticized totals before it produces losses.

## 4. Loss sizing on the criticized four (gross of reserves already held; 8% sale costs; $M)
| Value vs printed appraisal | DC $42.7M | Mont. $27.7M | Prince George's $56.0M | DC $20.5M on $13.5M (Q3) | DC $20.5M on $24.5M (Q2) | **Total (Q3 basis)** | TBV/share, no tax benefit |
|---|---:|---:|---:|---:|---:|---:|---:|
| Holds | 0 | 0 | 0 | 8.1 | 0 | **8.1** | $0.27 |
| −20% | 0 | 0 | 9.1 | 10.5 | 2.4 | **19.6** | $0.64 |
| −35% | 0.8 | 0 | 17.9 | 12.4 | 5.8 | **31.1** | $1.02 |

- Shares outstanding: 30,480,480 (R-p12). TBV $38.00.
- Buffers at 9/30: total ACL $120.8M; ACL/NPLs **72.75%** (was 109.01%); Q3 pre-provision revenue $23.8M; CET1 14.99%.
- **Specific reserves are not disclosed loan by loan.** Eagle says they "increased" (R-p2). Part of these losses may already be reserved. The Q3 10-Q (individually-assessed loans, MF allowance) should narrow this.
- **What this does not capture:**
  - A sale at a deeper discount than −35%. (Eagle's H1-26 non-office exit haircut was 13.3%; the office-era haircut was 39.6%.)
  - Losses on the unidentified ~$58M of Q4 multifamily maturities. The $265.7M on s16 less the $207.2M identified income-producing multifamily above leaves ~$58.5M of smaller or pass loans.
  - Rate or NIM effects.

## 5. What to watch, dated
| When | Event | What would change the read |
|---|---|---|
| ASAP | 10/22 call transcript | Prince George's plan (restructure vs sale); the DC $20.5M appraisal basis; the 10/27 refinancing status |
| Tue 10/27 | DC apt $42.7M + Montgomery mixed-use $27.7M mature | Outcome is visible only at the Q4 release (~late Jan 2027), unless an 8-K or the 10-Q subsequent-events note discloses it |
| ~early Nov | Q3 10-Q | Individually-assessed loans and specific reserves; MF criticized table; whether the Fairfax office, Anne Arundel, DC office $10.8M and Other-US apartment loans **paid off or were upgraded** |
| 11/30 · 12/21 · 12/23 · 12/29 · 12/30 | Remaining wall (§2, §3) | Extensions with new appraisals are the base case |
| ~late Jan 2027 | Q4 release | Grades the expectations below |

**Desk expectations, recorded 2026-10-22 before any Q4 outcome.** These are **unscored**; making any of them a REG row needs Will's word.
- **X1.** At least two of the four criticized Q4 maturities ($146.9M) are **still bank-held at 12/31/26** (extended, modified, nonaccrual or OREO) rather than repaid by outside cash. Basis: 2 of 2 identifiable Q3 maturities were extended. **Falsified** if three or more are repaid by outside cash by 12/31.
- **X2.** Q4 net charge-offs plus specific-reserve build attributable to these four loans total **≤ $31M** (the −35% row). **Falsified** above that, which would mean values sit more than 35% below the printed appraisals.
- **X3.** At least $100M of the $378.6M pass wall shows up as **extended** in Q4 disclosure, rather than refinanced away. Low confidence: construction takeouts can close cleanly.

## 6. Prior expectations — outcomes appended, priors not rewritten
- **10/13 forward judgment** (`reports/2026-10-13_review-response_forward-judgments.md`): "at least one of the four near-term maturity-baseline loans remains bank-held at September 30 after an extension…". **Outcome 10/22: TRUE.** Two were extended and are still held (Prince George's, Montgomery storage); two are undisclosed.
- **10/20 expectation** (`reports/2026-10-20_EGBN_cash-recovery_investigation.md`): "an extension alone would follow [the reported July] plan… not a positive cash cure or an unexpected new default." **Outcome 10/22:** the extension happened, **plus a move to nonaccrual**. That goes further than "extension alone", though still short of a recognized loss on the loan. Montgomery storage's maturity now sits past the reported year-end payoff objective; that is an observation, not a refutation.

## 7. What this does not change
- The EGBN matrix score stays 5 until the 11/07 re-score.
- The concentration thesis is unchanged.
- The EGBN PASS (no trade case; reasons: unproved mispricing, liquidity/horizon) stands. EGBN traded ~$31.49 at 11:03 ET (vendor quote, +10.4% on the print; ~0.83× TBV). That reaction says the market is reading the low provision and capital build, not the Q4 wall.
- RED grades CHG-027 (L35). TERRY constructs any trade, and Will decides.
