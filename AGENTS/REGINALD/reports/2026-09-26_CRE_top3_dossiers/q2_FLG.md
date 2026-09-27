# FLG: the $133M charge-off gap, and loss-bridge inputs (6/30/2026)

Read-only pass, 2026-09-26. All figures $M.

**Sources.** All documents are under `https://www.sec.gov/Archives/edgar/data/910073/`.
- **[10Q]** Q2-26 10-Q, acc 0000910073-26-000068, `.../000091007326000068/fbc-20260630.htm`
- **[10Q1]** Q1-26 10-Q, acc -26-000047
- **[10K]** FY25 10-K, acc -26-000025
- **[Q325] / [Q225] / [Q125]** 2025 10-Qs, accs -25-000181 / -25-000110 / -25-000076
- **[ER2]** Q2-26 earnings release, 8-K acc -26-000065, `a2q2026earningsrelease.htm`
- **[DECK s#]** slide # of the earnings deck in the same 8-K. Slides 13–18 and 25 were read as images.
- **[ER1] / [ER4] / [ER3]** Q1-26 / Q4-25 / Q3-25 releases, accs -26-000035 / -26-000017 / -25-000172

⚠️ **The scratchpad is shared.** My first extract, `scratchpad/q.txt`, was overwritten mid-run by an **Eagle Bancorp (EGBN)** 10-Q. Every figure here comes from `scratchpad/flgq2/`, whose registrant is verified as Flagstar. Any sibling agent that read `q.txt` should check which registrant it got.

---

## TASK 1: RESOLVING THE $133M

### 1a. The two schedules, verbatim

**Nonaccrual roll-forward, held for investment (HFI).** Source: [10Q] MD&A, "changes in non-accrual loans for the six months ended June 30, 2026". The Q1 column comes from the same table in [10Q1].

| Line (verbatim) | Q1-26 | H1-26 | Q2-26 (DERIVED: H1 − Q1) |
|---|---:|---:|---:|
| Balance at December 31, 2025 | 2,975 | 2,975 | 2,675 |
| New non-accrual loans | 397 | 780 | 383 |
| **Charge-offs** | **(40)** | **(100)** | **(60)** |
| Transferred to Other assets | (2) | (4) | (2) |
| Loan payoffs, including dispositions and principal pay-downs | (646) | (836) | (190) |
| Restored to performing status | (9) | (15) | (6) |
| Balance at period end | 2,675 | 2,800 | 2,800 |

- **Scope: all HFI segments.** The $2,975M opening balance = MF 2,261 + CRE 489 + 1-4 family 64 + C&I 130 + Other 31 [10Q non-accrual table].
- **Held-for-sale (HFS) loans are excluded:** $5M of HFS nonaccrual at 6/30/26 and $30M at 12/31/25 [10Q fn 1].

**ACL roll-forward.** Source: [10Q] Note 6. The Q1 row is from [10Q1] Note 6.

| Line | MF | CRE | 1-4 | C&I | Other | Total |
|---|---:|---:|---:|---:|---:|---:|
| Q1-26 charge-offs | (81) | (18) | (1) | (5) | (8) | **(113)** |
| Q2-26 charge-offs | (81) | (13) | (1) | (18) | (7) | **(120)** |
| H1 beginning balance | 549 | 229 | 35 | 150 | 67 | 1,030 |
| **H1 charge-offs** | **(162)** | **(31)** | (2) | (23) | (15) | **(233)** |
| H1 recoveries | 10 | 22 | – | 18 | 5 | 55 |
| H1 provision | 42 | (67) | 2 | 32 | 8 | 17 |
| H1 ending balance | 439 | 153 | 35 | 177 | 65 | 869 |

- **Call Report.** The FFIEC RI-B year-to-date charge-offs at 6/30/26 are MF $161,926K, non-owner-occupied CRE $31,737K, owner-occupied $0, construction $0, total $232,410K (`AGENTS/REGINALD/workbook/CRE_RCN_COHORT.tsv:53`). That is the ACL basis again, so the Call Report cannot split nonaccrual from accruing loans.
- **The 10-Q's own attribution** [10Q MD&A]: "Gross charge-offs of $193 million were recorded on multi-family and CRE loans ... primarily driven by appraisals received on those loans and the resolution of a single borrower relationship undergoing bankruptcy proceedings during the three months ended March 31, 2026."

### 1b. The gap recurs every quarter

All figures are DERIVED as differences between year-to-date disclosures in each filing's two schedules.

| Qtr | ACL gross charge-offs | Roll-forward charge-offs | **Gap** | MF+CRE gross charge-offs | MF+CRE outside the roll-forward (floor) | New nonaccrual | Payoffs / dispositions | Transfers to HFS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Q1-25 | 124 | 43 | 81 | 82 | 39 | 842 | 102 | 25 |
| Q2-25 | 140 | 100 | 40 | 125 | 25 | 486 | 370 | 0 |
| Q3-25 | 92 | 19 | 73 | 72 | 53 | 360 | 235 | 38 |
| Q4-25 | 93 | 23 | 70 | 47 | 24 | 306 | 508 | 32 |
| Q1-26 | 113 | 40 | 73 | 99 | 59 | 397 | 646 | 0 |
| Q2-26 | 120 | 60 | 60 | 94 | 34 | 383 | 190 | 0 |
| **H1-26** | **233** | **100** | **133** | **193** | **93** | 780 | 836 | 0 |
| FY25 | 449 | 185 | 264 | 326 | 141 | 1,994 | 1,215 | 95 |

### 1c. Verdict on each candidate

| # | Candidate | Verdict | Evidence |
|---|---|---|---|
| (a) | Loans written down when they enter nonaccrual, with the "New non-accrual" line recorded net of the write-down; or loans that enter and leave nonaccrual within the period | **CANNOT DETERMINE. Leading candidate.** | FLG's policy fits: "All substandard loans, including non-accrual loans, are appraised at the time of downgrade" [10Q], and collateral-dependent loans are "written down to their current appraised values less costs to sell" [10K]. MF collateral-dependent loans ($2,130M, [10Q] Note 5) ≈ MF nonaccrual ($2,132M). **Floor:** MF charge-offs alone ($162M) exceed the roll-forward's entire charge-offs line ($100M). The gap does not move with new-nonaccrual volume (842 → 81; 306 → 70). No charge-off split by grade or by roll-forward line is disclosed. |
| (b) | Charge-offs on **accruing** loans | **REFUTED as material for MF. CANNOT DETERMINE for CRE.** | Since 1/2024, cumulative net charge-offs on the accruing special-mention + substandard part of NYC ≥50% RR are **$2M (0.07%)**, against **$351M** on its nonaccrual loans [DECK s16]. MF collateral-dependent ≈ MF nonaccrual. CRE collateral-dependent is $346M against $471M nonaccrual. H1 modifications included **no principal forgiveness** [10Q modification table: rate / term / combination only]. The $51M of loans 90+ days past due and still accruing has no segment breakdown. |
| (c) | Losses on payoffs or dispositions booked inside the "payoffs, including dispositions" line | **CANNOT DETERMINE. Partial support in Q1-26 only.** | In Q1 the bankruptcy relationship was sold. The 10-K said FLG "expect[s] to close on the sale of these loans during the three months ending March 31, 2026" [10K]. Q1 net charge-offs rose $34M QoQ, "primarily related to the one borrower relationship that was in bankruptcy" [10Q1]. **Against (c) as the steady-state cause:** the gap does not scale with payoffs. Q2-26 had $190M of payoffs and a $60M gap; Q2-25 had $370M and $40M. Net gain on loan sales & securitizations was +$9M in H1-26 [10Q income statement]; losses on HFI sales go through the ACL instead, so that line is no test. |
| (d) | Held-for-sale transfers | **REFUTED for 2026** | The cash-flow line "Transfer of loans from held for investment to held for sale" is "–" for H1-26 (255 in H1-25) [10Q]. The roll-forward has no HFS line in 2026. Q1-26's gap was $73M with zero HFS transfers. |
| (e) | Non-CRE charge-offs outside the schedule | **REFUTED as a scope explanation. Up to $40M CANNOT DETERMINE.** | The roll-forward covers all segments. Non-MF/CRE charge-offs total 2 + 23 + 15 = **$40M**. Consumer loans can be charged off at 120/180 days past due, or at bankruptcy notice + 60 days [10K Note 2], possibly without first being placed on nonaccrual. |
| (f) | Period or basis mismatch | **REFUTED** | Both schedules are six-month year-to-date, HFI. The roll-forward's 100 matches neither gross (233) nor net (178). Matching Q2's net charge-offs of $100M is coincidence: Q1's roll-forward shows 40, against Q1 gross of 113 and net of 78. |

### 1d. Where the $233M sits

| Bucket | $M | Status |
|---|---:|---|
| (1) Charge-offs shown in the nonaccrual roll-forward | **100** | DISCLOSED; segment mix NOT DISCLOSED |
| (2a) HFS transfers / (2b) period-basis mismatch | 0 / 0 | REFUTED |
| (2c) Accruing MF loans | ≈0 | Deck evidence under (b) |
| (2d) Non-MF/CRE charge-offs that bypass the roll-forward | 0–40 | CANNOT DETERMINE |
| (3) **MF+CRE charge-offs on nonaccrual / collateral-dependent loans, outside the roll-forward's charge-offs line** | **93–133** | Floor DERIVED 193 − 100. Mechanism = (a) netting at entry and/or (c) the Q1 bankruptcy disposition. **The split between them is NOT DISCLOSED.** |
| **Residual with no identified home** | **0** | But 93–133 remains unallocated between (a) and (c) |

**Were the "par payoffs" not at par? No evidence either way; it cannot be excluded.**
- The par-payoff disclosures are MF **$1.7B** in H1, 42% of it substandard [10Q MD&A], and CRE $1.1B in each of Q1 and Q2 [DECK s13]. These are mostly accruing substandard loans, and those carry ≈$0 cumulative net charge-offs.
- The one identified non-par exit is the Q1 bankruptcy note sale. That was a **disposition** of nonaccrual loans, not a "par payoff".
- **Hypothetical upper bound (DERIVED):** if the whole $133M were hidden discounts on the $2.2B of "par" payoffs, the discount would be 6.0% (133 / 2,200). The gap not tracking payoff volume argues against this.

---

## TASK 2: BRIDGE INPUTS AT 6/30/2026, ON THE 10-Q AMORTIZED-COST BASIS

### 2a. Risk-grade pools

Source: [10Q] Note 5, credit-quality tables by risk category. Balances are net of prior charge-offs.

| Grade | MF | CRE |
|---|---:|---:|
| Pass | 17,860 | 6,406 |
| Special mention | 2,757 | 376 |
| Substandard (accruing) | 4,182 | 991 |
| Nonaccrual | 2,132 | 471 |
| **Total** | **26,931** | **8,244** |
| H1 gross charge-offs | 162 | 31 |

### 2b. Reserve held against each pool

| Item | MF | CRE | Source |
|---|---:|---:|---|
| Segment ACL | 439 | 153 | [10Q] Note 6 |
| **Specific allowance** (allowance tied to individual nonaccrual loans) | **83** | **30** | [10Q] Note 6 nonaccrual table (all-segment total 163; 222 at 12/31/25) |
| Nonaccrual with no allowance / with an allowance | 1,143 / 989 | 354 / 117 | same |
| **Collective ACL** (segment ACL minus specific) | **356** | **123** | DERIVED |
| Collective ACL ÷ (pass + SM + SS) | 1.44% (356 / 24,799) | 1.58% (123 / 7,773) | DERIVED |
| **Collective ACL by risk grade** | **NOT DISCLOSED** | **NOT DISCLOSED** | |
| NYC ≥50% RR subset only (a partial grade split) | Pass ≈48 (DERIVED: 4,089 × 1.18%) · SM+SS **134** (5.03%) · nonaccrual **76** (4.38%) · total 258 = 3.04% × 8,490 | — | [DECK s16] |
| Collateral-dependent loans | 2,130 | 346 | [10Q] Note 5 |
| Impaired loans at fair value, nonrecurring (Level 3), all segments | 2,621 | | [10Q] Note 15 |

⚠️ **The deck's segment ACL is on a different basis:** CRE 148 and C&I 182 vs the 10-Q's 153 and 177, because the deck moves owner-occupied office into C&I [DECK s17]. Use the 10-Q figures.

### 2c. Losses already taken, capital, earnings

| Item | Value | As of | Source |
|---|---|---|---|
| NYC ≥50% RR nonaccrual: pre-charge-off balance / net charge-offs / book | **2,088 / 351 (16.80%) / 1,737** | 6/30/26; net charge-offs since 1/2024 on loans still held | [DECK s16; s25 notes 5–6] |
| NYC ≥50% RR special mention + substandard: pre-charge-off / net charge-offs / book | 2,667 / 2 / 2,665 | same | [DECK s16] |
| MF net charge-offs since 1/2024, including resolved loans | 689 | 6/30/26 | [DECK s14] |
| Cumulative charge-offs on the whole $2,800M nonaccrual pool | NOT DISCLOSED | | |
| Reserve for unfunded commitments | **56** (55 at 12/31/25) | 6/30/26 | [10Q] Note 17 fn; [DECK s17] |
| CET1 capital | **$7,937M / 13.16%** | 6/30/26 | [10Q] MD&A regulatory-capital table |
| Tier 1 / total capital | 8,441 / 10,003 (16.58%) | 6/30/26 | same |
| Risk-weighted assets | **≈60,312** (7,937 / 0.1316). Cross-check from the minimum line: 2,715 / 4.5% = 60,333 | 6/30/26 | DERIVED; the dollar figure is not printed |
| CET1 target | "low end of target CET1 range of **10.5%**"; excess capital **$1.6B**. DERIVED check: (13.16% − 10.5%) × 60,312 = 1,604 | 6/30/26 | [ER2] |
| PPNR (pre-provision net revenue) | Q3-25 **−3** · Q4-25 **48** · Q1-26 **32** · Q2-26 **66** → TTM **143** (DERIVED). Adjusted: 15 · 60 · 41 · 62 → **178** | | [ER3] / [ER4] / [ER1] PPNR text; [ER2] PPNR table |
| Common dividends | $0.01 per share per quarter; **$9M cash in H1-26** | | [ER2]; [10Q] cash flow |
| Preferred dividends | $8M per quarter; $16M in H1 | | same |
| Buyback authorization | **$250M, authorized July 2026, 12 months.** "We had no active share repurchase programs as of June 30, 2026" | | [10Q] Note 16, Part II Item 2; 8-K EX-99.3 |
| Buyback executed so far | **NOT DISCLOSED.** No 8-K since 7/24; the Q3 10-Q is due ~11/6. Q2 repurchases were only shares withheld for tax (18,609 @ $14.13; 4,262 @ $13.53) | | [10Q] Part II Item 2 |

### 2d. How the deck's $4.4B criticized pool overlaps the 10-Q grade tables

The deck's **$4,401M "Criticized + Classified"** pool is a **subset** of the 10-Q MF grades, not an addition to them [DECK s15/16]. It is nonaccrual **1,737** plus special mention + substandard **2,665**. The two sources share a basis: the deck's NYC total of 13,388 equals the 10-Q MF geography table's "Total New York City" of 13,388, and that table sums to 26,931 at amortized cost.

**Mutually exclusive MF pools (DERIVED; they sum to 26,931):**

| Pool | NYC ≥50% RR | All other MF |
|---|---:|---:|
| Nonaccrual | 1,737 | **395** |
| Special mention + substandard | 2,665 (split NOT DISCLOSED) | **4,274** |
| Pass | 4,089 | **13,771** |

**Rules for using these pools:**
1. Stress either the NYC RR pool or the 10-Q grade rows, never both. Doing both double-counts up to $4,401M.
2. About $76M of the $83M MF specific allowance sits on NYC RR nonaccrual loans. That leaves ≈$7M (DERIVED) for the other $395M of MF nonaccrual. This assumes the deck's nonaccrual ACL is all specific allowance, which the deck does not state.
3. The deck's 281 at 2.87% is a different perimeter from its NYC 3.04% line. 281 / 2.87% ≈ $9.8B, which includes non-NYC rent-regulated loans.
4. The deck's "criticized + classified" includes nonaccrual loans, even though footnote 4 reads "special mention or substandard".

---

## BOTTOM LINE
1. The $133M gap is structural, not a one-off: it runs $40–81M every quarter for 6 quarters and was $264M in FY25. It comes from how the nonaccrual roll-forward is presented, **not** from hidden losses in another pool. ⛔ *(9/27: the FLG desk grades the location NOT DETERMINABLE; its leading reading is loss taken at exit, so "par payoffs" may not have been par. See `reports/2026-09-26_CRE_top3_loss_bridge.md` §4 ①.)*
2. At least **$93M** (193 − 100) is MF/CRE charge-offs on nonaccrual or collateral-dependent loans that bypass the roll-forward's "Charge-offs" line. The likely routes are write-downs netted into "New non-accrual" and the Q1 bankruptcy sale booked inside "dispositions"; the split between them is NOT DISCLOSED. Up to $40M may be non-CRE.
3. Refuted: held-for-sale transfers (zero in 2026), a period or basis mismatch, a scope mismatch, and material charge-offs on accruing MF loans ($2M cumulative).
4. There is no evidence that "par payoffs" were below par: the gap does not track payoff volume.
5. For the bridge, use the 10-Q basis and treat the deck's $4.4B as a subset. Collective ACL is MF 356 / CRE 123, with no split by grade. Other inputs: CET1 $7,937M on ≈$60.3B RWA; TTM PPNR $143M; $1.6B above the 10.5% target; no buyback execution disclosed.
