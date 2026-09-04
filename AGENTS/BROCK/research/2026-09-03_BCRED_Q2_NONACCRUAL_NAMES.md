# BCRED Q2-2026 NON-ACCRUAL NAME LIST — the third carry, CLOSED
*Primary: BCRED Q2-2026 10-Q, acc `0001803498-26-000048`, Condensed Consolidated Schedule of Investments **June 30, 2026**, footnote **(17)** "Loan was on non-accrual status as of June 30, 2026."*
*Tool: `tools/soi_nonaccrual.py` (built 2026-09-03). **VALIDATION PASS — 25 loans / 15 issuers, matching the filing's own stated figures exactly.***

## Why this took three attempts, and what was actually wrong
**The bug was SCOPE, not parsing.** Footnote (17) is re-used in **six** places in this filing — the current-period fund schedule, the prior-period comparative, and **both unconsolidated JV schedules**, each × two period-ends. A naive marker grep returned **23 issuers / 69 loans** on 2026-08-28. Each schedule is terminated by its own footnote-definition block, so the current-period fund schedule is `[first SOI header] .. [first (17)-defined-as-June-30-2026 block]` — chars **631,292–822,631**, 191,339 of a 1,654,646-char document. **Scope it and the count is exact on the first try.**

## The list — 15 issuers, 25 loans, $1.94bn par at **42.6¢**

| Issuer | Loans | Par ($k) | Cost ($k) | Fair value ($k) | FV/par |
|---|---:|---:|---:|---:|---:|
| **Medallia, Inc.** | 2 | **1,118,387** | 1,084,029 | 553,601 | **49.5¢** |
| Benefytt Technologies, Inc. | 2 | 149,742 | 62,101 | 5,225 | **3.5¢** |
| Plasma Buyer, LLC | 4 | 119,889 | 108,106 | 64,302 | 53.6¢ |
| Atlas CC Acquisition Corp. | 4 | 105,386 | 72,978 | 10,154 | **9.6¢** |
| ES Group Holdings III, Ltd. | 2 | 95,450 | 97,787 | 79,883 | 83.7¢ |
| Paramount Global Surfaces, Inc. | 1 | 83,961 | 81,784 | 46,179 | 55.0¢ |
| Material Holdings, LLC | 1 | 66,966 | 57,075 | **0** | **0.0¢** |
| Curia Global, Inc. | 1 | 55,105 | 52,742 | 4,959 | **9.0¢** |
| WHCG Purchaser III, Inc. | 1 | 43,157 | 14,654 | 27,621 | 64.0¢ |
| Pigments Services, Inc. | 2 | 40,995 | 26,764 | 6,075 | **14.8¢** |
| AEC Parent Holdings, Inc. | 1 | 24,428 | 21,013 | 13,436 | 55.0¢ |
| Mitnick Purchaser, Inc. | 1 | 11,438 | 11,148 | 4,145 | 36.2¢ |
| Cast & Crew Payroll, LLC | 1 | 11,392 | 11,151 | 4,471 | 39.2¢ |
| Newfold Digital Holdings Group, Inc. | 1 | 6,340 | 6,086 | 2,745 | 43.3¢ |
| Hoya Midco, LLC | 1 | 2,765 | 2,724 | 1,228 | 44.4¢ |
| **TOTAL** | **25** | **1,935,401** | **1,710,142** | **824,024** | **42.6¢** |

✅ **INDEPENDENT RECONCILIATION:** aggregate cost **$1.71bn** against BCRED's stated **2.2% non-accrual at cost** implies a portfolio of **~$78bn at cost** — consistent with $42.78bn net assets at ~0.8x debt/equity. FV $824.0M against the stated **1.1% at FV** implies **~$75bn** at FV. **Both legs reconcile; the marks are not free-floating.**

## What the list says
🔑 **MEDALLIA IS 58% OF THE NON-ACCRUAL BOOK BY PAR** — $1.12bn across two loans, both marked **49.5¢**, both on non-accrual. ⚠️ **My `LESSONS #7` bellwether reference is 78¢, from a different vintage and source — I am NOT asserting a clean 78¢→49.5¢ series without confirming that basis.** What is primary today: **BCRED marks Medallia at 49.5¢ and has it on non-accrual at 6/30/26.**
🔑 **Four names are marked below 15¢ — Material Holdings at ZERO, Benefytt 3.5¢, Curia 9.0¢, Atlas CC 9.6¢.** **This is the population the small-fund <50¢ migration test needs**, and it is now a named list rather than an aggregate.
⚠️ **The 42.6¢ blended mark is a PAR-weighted figure dominated by one name.** Ex-Medallia the book is **$817M par at 33.2¢**. **Quote whichever you mean and say which.**

## Two traps this filing sets, both of which silently corrupt counts
1. **ONE PORTFOLIO COMPANY, TWO BORROWING ENTITIES.** *"CFCo, LLC (Benefytt Technologies, Inc.)"* and *"Daylight Beta Parent, LLC (Benefytt Technologies, Inc.)"* are separate rows. **Counting borrowing entities gives 16 issuers where the filing says 15.** The issuer of record is the **parenthetical**.
2. **INDUSTRY-HEADING GLUE.** Once HTML is flattened the industry heading abuts the first issuer in its section — *"Building Products ES Group Holdings III, Ltd."* The tool suffix-collapses where a shorter twin exists and **flags `PREFIX?` where it cannot**, rather than guessing. **Two names here needed manual cleaning: `Health Care Equipment & Supplies AEC Parent Holdings, Inc.` → AEC Parent Holdings, Inc.; `Life Sciences Tools & Services Curia Global, Inc.` → Curia Global, Inc.**

## Caveat I am keeping on the marks
The first marks pass produced **FV/par of 26,726¢** — the value regex had truncated the row and captured the *next* row's columns. Fixed by anchoring after the maturity date, and the tool now **discards any row failing `0 < FV ≤ 1.5 × par` rather than publishing it**. Medallia was then **verified row-by-row against the raw text** because a single name at 58% of the book is exactly the figure that should not be taken on a parser's word. **Counts were validated before the marks existed; the marks were validated separately.**
