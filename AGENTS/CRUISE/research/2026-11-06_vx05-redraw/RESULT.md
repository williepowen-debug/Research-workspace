# VX-CRU-05 redraw, draft cells for Will's ruling — 2026-11-06

**State of this draft: PROPOSED. It does not count until Will rules. `VX-CRU-05` holds RED(4) and `workbook/VX.tsv` is unchanged.** Ruling that ordered it: WQ-627 A, Will 2026-11-06 about 14:05 ET, `PROME/proposals/2026-11-06_wq627-628-629-634-RULED.md`.

**Verdict: on the 9/30/26 prints the draft reads ORANGE(3), one step below today's RED(4). On this desk's arithmetic it returns to RED(4) at the next print, because leverage is set to pass 6.0x as the strong Q4 2025 quarter leaves the trailing year.** Working model, not truth.

Primary: NCLH earnings Ex-99.1 and 10-Q / 10-K filings, 2023-02-28 to 2026-10-29, pulled from sec.gov 2026-11-06. Arithmetic: `calc.py`, `calculations.json`. Filings are not committed; `pull.py` and `pull2.py` re-fetch them. USD millions unless marked.

## The draft cells

**Proposed `Vector` label:** NCLH leverage and deposits against capacity.

| Cell | Leverage leg | Deposit leg |
|---|---|---|
| **GREEN (1)** | ≤ 4.9x | ≥ 0.00pp |
| **YELLOW (2)** | 5.0x to 5.4x | −0.01pp to −3.00pp |
| **ORANGE (3)** | 5.5x to 5.9x | −3.01pp to −8.00pp |
| **RED (4)** | ≥ 6.0x | ≤ −8.01pp |

**Row score = (leverage leg score + deposit leg score) ÷ 2, rounded up.** This covers all 16 combinations, so no reading falls outside a cell. That gap was the defect in the old row. Score 5 is not used, the same as `VX-CRU-01`.

| Spec | Leverage leg | Deposit leg |
|---|---|---|
| **Level** | Cells above | Cells above |
| **Instrument** | "Net Leverage" as the company prints it in the quarterly earnings Ex-99.1: Net Debt ÷ trailing 12-month Adjusted EBITDA, read to one decimal (a two-decimal print rounds, so 5.58x reads 5.6x) | Year-on-year % change in the balance-sheet line "Advance ticket sales" at quarter-end, minus year-on-year % change in same-quarter Capacity Days, in percentage points to two decimals. Both come from the same Ex-99.1 (PRIMARY) |
| **Window** | One reading per quarterly print. No move between prints | Same print |
| **Revision policy** | First print governs. A later restatement is noted and regrades nothing | Same |

## Reading on the current print

| Leg | 9/30/26 reading | Cell | Source |
|---|---|---|---|
| Leverage | **5.5x** printed (5.49x computed: Net Debt $14,830.0M ÷ trailing Adj EBITDA $2,699.0M) | ORANGE (3) | 8-K acc 0001171843-26-006957 Ex-99.1, 10/29 |
| Deposits | Advance ticket sales $3,142.0M, **−0.16%** YoY; Capacity Days 6,766,454, **+5.43%** YoY; gap **−5.59pp** | ORANGE (3) | Same; capacity also in 10-Q acc 0001104659-26-120217 |
| **Row** | (3 + 3) ÷ 2 = **3** | **ORANGE (3)** | Convergence 10/20 → 9/20 if ruled |

## History, the cells applied backward

Twelve quarter-ends. Net Leverage is not printed before 12/31/23. Deposits cross-checked to XBRL `ContractWithCustomerLiabilityCurrent` on all 12; capacity quarters sum to the printed year totals (asserts in `calc.py`).

| Quarter-end | Printed leverage | Computed | Advance ticket sales YoY | Capacity YoY | Gap pp | Gap on next quarter's capacity | Leverage leg | Deposit leg | Row |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 12/31/23 | 7.3x | 7.34 | +21.62% | +17.24% | +4.39 | +13.77 | RED | GREEN | ORANGE |
| 3/31/24 | 6.3x | 6.31 | +14.25% | +7.86% | +6.39 | +10.20 | RED | GREEN | ORANGE |
| 6/30/24 | 5.9x | 5.94 | +12.95% | +4.05% | +8.91 | +9.29 | ORANGE | GREEN | YELLOW |
| 9/30/24 | 5.58x | 5.58 | +6.05% | +3.66% | +2.38 | +7.22 | ORANGE | GREEN | YELLOW |
| 12/31/24 | 5.27x | 5.27 | +1.48% | −1.17% | +2.65 | +3.88 | YELLOW | GREEN | YELLOW |
| 3/31/25 | 5.66x | 5.66 | +3.65% | −2.40% | +6.06 | −1.85 | ORANGE | GREEN | YELLOW |
| 6/30/25 | 5.3x | 5.33 | +1.45% | +5.51% | −4.06 | −4.92 | YELLOW | ORANGE | ORANGE |
| 9/30/25 | 5.4x | 5.45 | +0.07% | +6.36% | −6.29 | −7.28 | YELLOW | ORANGE | ORANGE |
| 12/31/25 | 5.3x | 5.27 | +3.05% | +7.35% | −4.30 | −9.10 | YELLOW | ORANGE | ORANGE |
| 3/31/26 | 5.3x | 5.33 | −1.15% | +12.15% | −13.30 | −10.03 | YELLOW | RED | ORANGE |
| 6/30/26 | 5.3x | 5.33 | −4.76% | +8.88% | −13.64 | −10.20 | YELLOW | RED | ORANGE |
| 9/30/26 | 5.5x | 5.49 | −0.16% | +5.43% | −5.59 | not yet known | ORANGE | ORANGE | ORANGE |

## Where each line comes from

| Line | Anchor |
|---|---|
| 4.9x | Below every print on record (low 5.27x, 12/31/24). The company's guide for 2025 was "approximately 5x"; its July 2024 target was "the mid 4's by 2026" (Ex-99.1 4/30/25, 7/31/24). Neither was met |
| 5.4x / 5.5x | 6 of the last 8 prints sit at 5.3x to 5.4x. The two outside are 5.7x (Norwegian Aqua delivered, 3/31/25) and 5.5x (9/30/26) |
| 6.0x | Above every print since 6.3x at 3/31/24, so a reading here gives back part of the 2024 deleveraging |
| 0.00pp | Deposits growing exactly as fast as capacity |
| −3.00pp, −8.00pp | Placed in empty space in the record: no reading between +2.38 and −4.06, none between −6.29 and −13.30 |

## The next print

Q4 2025 Adj EBITDA, implied: trailing $2,699.0M less implied nine months of 2026 ($2,550M guide less $414M Q4 guide = $2,136M) = **$563M**. It leaves the trailing year and $414M replaces it, so trailing Adj EBITDA falls to about **$2,550M** at 12/31/26. These are company guides; the leverage below is my ESTIMATE, and the company printed no year-end leverage figure.

| 12/31/26 case | Net Debt | Leverage | Leverage leg |
|---|---:|---:|---|
| Net Debt unchanged from 9/30 | $14,830M | **5.82x** | ORANGE |
| Printed 6.0x needs Net Debt of at least | $15,173M (+$343M) | 5.95x rounds to 6.0x | RED |
| Rest-of-2026 capex $1,200M (10-Q: growth $1.1B; other ~$100M, my assumption) less Q4 operating cash at last year's level $383M | $15,647M (+$817M) | **6.14x** | RED |

The company's "~5.2x" year-end guide of 3/2/26 is not repeated in the 5/4, 7/30 or 10/29 Ex-99.1 (text search 11/6 on "end the year", "year-end", "leverage is expected", "leverage guidance"). Call transcripts are unread, so whether management still holds a year-end figure is unknown.

Deposit leg at that print: Q4 2026 capacity is not guided in the 10/29 Ex-99.1 or 10-Q (text search 11/6). At the `CRU-13` line of $3,264.6M, deposits read +2.00% YoY, and the gap reads −4.00pp at +6% capacity (ORANGE). The deposit leg turns RED at +6% capacity if deposits fall more than 2.00% YoY.

So on the base case the row reads RED + ORANGE = **RED(4)** at the Q4 print. The prior two Q4 prints landed 2/27/25 and 3/2/26; the next date was not checked.

## Limits that could change the ruling

1. **The fall to ORANGE(3) is a rule outcome, not a calmer company.** Part of it is a label fix: the old row scored its ORANGE letter ("guide lowered + yields flat/neg") as RED(4) and treated the RED letter as score 5 (9/19 Note). The draft maps ORANGE to 3.
2. **The lines were set after seeing this history, and after the 6.14x estimate.** The table above is an in-sample fit, not a validation.
3. **Guidance leaves the row.** A guide cut reaches it only through Adj EBITDA at the next print. `VX-CRU-03` RED still carries "value operator guides down". Liquidity also stays outside the row: the 11/17 test remains at DOCKET L715 and on the STATUS upgrade-trigger line.
4. **The row moves once a quarter.** Between prints it cannot move.
5. **Same-quarter capacity is a proxy.** Deposits fund future sailings, and forward capacity is not disclosed. On next-quarter capacity, 12/31/25 reads −9.10pp, which is RED on the deposit leg rather than ORANGE; the row there stays ORANGE.
6. **The deposit leg does not see quality.** The refundable share is 45% vs 40% at 9/30/25 (KB-CRU-227), and a lower ticket price shrinks deposits with no change in volume. FX also moves the balance.
7. **Leverage moves on things other than stress.** Euro debt is marked to market (Ex-99.1 7/31/25), and ship deliveries step it up (3/31/25, Aqua). This quarter's rise was earnings-driven: trailing Adj EBITDA −$82.5M, Net Debt +$13.3M.

## Alternative

**Hold RED(4) and apply these cells from the Q4 print.** That avoids a step down and likely step back up inside one quarter. I do not recommend it: the row would keep a score that no letter supports, which is the defect WQ-627 fixes.
