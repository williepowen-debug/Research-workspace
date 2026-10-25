# L818 follow-up — is there observable evidence of borrowers shifting from market financing to bank credit?

**LIQUID, 2026-10-23 22:2x–22:5x ET** (Will-launched, CATO's bounded follow-through, ~45 min). Parent: `analysis/2026-10-23_L818-repricing-vs-restriction.md`. No monitor, gate, threshold or approval added or changed; WQ-512's approved disclosure rider (Will 10/23 17:01 ET) untouched.

## What the series measure (before any reading)

- **Source and vintage:** Fed H.8, release **2026-10-23** (primary dated page `releases/h8/20261023/`), pulled as FRED weekly series all `last_updated` 2026-10-23 15:17–15:22 CT. That gives one vintage for every cell. **Seasonally adjusted**, Wednesday levels, $B (borrowings published in $M, converted). Latest observation **week ending Wed 10/14**; 9 observations 8/19 → 10/14 give 8 weekly changes. Check: large + small C&I = domestic C&I (FRED CILDCBW027SBOG) to 0.0 on all 9 dates.
- **Series:** C&I = CIBOARD (large), CILSCBW027SBOG (small). Loans to nondepository financial institutions (NDFI, a separately published H.8 line) = LNFLCBW027SBOG / LNFSCBW027SBOG. Deposits DPS{L,S}CBW027SBOG · cash CAS{L,S}CBW027SBOG · borrowings H8B3094NLGA / H8B3094NSMA. Large = the top 25 domestically chartered banks by assets; small = all other domestic banks.
- **These are balance-sheet STOCKS.** A rise can reflect the net result of originations or line draws less repayments, purchases or acquisitions, reclassification between lines, and weekly-to-quarterly benchmarking to Call Reports. **Nothing in the H.8 identifies revolver utilisation.** No increase below is called a drawdown.
- **Structure and reclassification:** the H.8 "Notes on the Data" (`releases/h8/h8notes.htm`, last update 10/23) lists one entry in the window: **9/30, $5.2B of auto loans divested to nonbanks (cash +$5.2B)**. It touches neither C&I nor NDFI. Levels (unlike the release's percent-change table) are **not** adjusted for structure activity. Bank-to-bank reclassifications below the $5B note threshold are not disclosed.
- **Quarter-end is where reclassification lands.** Large-bank C&I fell **$116.5B** in the week of 2025-01-01 while NDFI rose **$97.8B**. Other quarter-ends: C&I −$26.8B / −$38.8B against NDFI +$45.9B / +$31.1B (2025-Q1, 2025-Q2). The current move falls on the 9/30 and 10/7 weeks, so the same caution applies.

## Table — SA, $B, weeks ending Wednesday; release 10/23

| Line | Large 10/14 | Large w/w (last 4 wks: 9/23 · 9/30 · 10/7 · 10/14) | Large 4-wk | Large 8-wk | Small 10/14 | Small 4-wk | Small 8-wk |
|---|---:|---|---:|---:|---:|---:|---:|
| **C&I loans** | 1,615.0 | −2.7 · **+10.7 · +19.8** · −1.8 | **+26.0 (+1.64%)** | +35.5 (+2.25%) | 742.0 | +4.6 (+0.62%) | +7.2 (+0.98%) |
| **NDFI loans** | 1,364.0 | +5.9 · +7.6 · +13.9 · +5.5 | **+32.9 (+2.47%)** | +52.2 (+3.98%) · **up 8 of 8 weeks** | 202.3 | +2.4 (+1.19%) | +2.2 (+1.08%) |
| Deposits | 12,466.2 | +26.6 · +90.0 · +26.3 · +25.2 | +168.1 (+1.37%) | +197.5 | 5,695.4 | +26.5 (+0.47%) | +20.9 |
| Cash assets | 1,384.8 | +47.4 · +26.4 · +44.3 · −12.4 | +105.6 (+8.26%) | +53.8 | 494.2 | +21.3 (+4.50%) | +10.7 |
| Borrowings | 1,066.8 | −5.4 · −14.6 · +7.0 · +4.3 | −8.7 (−0.81%) | −2.5 | 316.4 | **+30.0 (+10.49%)** | +33.7 (+11.94%) |

Full 9-week levels and all eight weekly changes, with each series' units, SA flag and FRED `last_updated` stamp: `research/2026-10-23_evening/h8_8wk_fred.txt` (borrowings there in $M).

**Base rates (same FRED vintage, weekly since 2015, 2020 excluded):**
- Large C&I 4-week +1.64% ranks at the **94th percentile**. The +$19.8B week (10/7) is the largest weekly rise since 2026-02-04. Prior-year average weekly change: +$2.55B.
- Quarter-end two-week change in large C&I: **+$30.5B now**, the largest in 14 quarter-ends since 2023-Q2. The next largest were +$18.0B (2023-Q3) and +$16.6B (2026-Q1).
- Large NDFI 4-week +2.47% ranks at the **87.5th percentile**. The 8-week average weekly change is +$6.5B against a prior-year average of +$4.46B. Quarter-end two-week +$21.5B sits inside the 2025–26 range (+$16.4B to +$51.1B).
- Small C&I 4-week +0.62% ranks at the **75th percentile**: ordinary.

## Reading

| Line | Classification | Why |
|---|---|---|
| Large-bank C&I | **ISOLATED MOVE** | Two weeks at quarter-end (+$30.5B, the largest quarter-end gain in the sample), then −$1.8B. Quarter-end weeks carry reclassification and benchmark effects; one episode is not a trend. **Timing does not fit a market-to-bank shift cleanly:** the jump came 9/24–10/7, after a heavy September for HY issuance (~$51B, one Bloomberg snippet) and before October's narrowing (from ~10/13). |
| Large-bank NDFI | **PERSISTENT, but on a pre-existing trend** | Up 8 of 8 weeks, modestly above its own one-year pace. This is the line that would carry fund-finance and lender-finance lending, but it has grown for years (multi-year structural shift of credit to nonbanks financed by banks). It cannot be told apart from draws, new facilities or reclassification. |
| Small-bank C&I and NDFI | **NO CHANGE** | Inside normal ranges. |
| Small-bank borrowings | Persistent rise (+$30.0B over 4 weeks) | Bank-side funding, not borrower demand. Deposits and cash rose too, so this is not deposit replacement on these weeks. |
| Large-bank deposits and cash | Rising | Consistent with funded lending **or** inflows; uninformative about the channel. |

**Overall: INSUFFICIENT EVIDENCE of a shift from market financing to bank credit.** One quarter-end C&I jump at large banks that does not line up in time with the October issuance slowdown, plus an NDFI line growing on its existing trend. Public weekly data **cannot distinguish** draws from originations, purchases or reclassification. That is the documented limit, and the work stops here.

## What this adds to "mainly repricing"

It does not change the conclusion. The data shows no measured restriction channel and no visible substitution into bank credit beyond one isolated quarter-end move. The large-bank C&I jump is the single item that would fit a substitution story if it continues. Without a utilisation series, it stays unidentified.

## The missing observation

- **Revolving-credit utilisation:** bank unused commitments (Call Report RC-L item 1, quarterly) and more specific issuer facility disclosures can provide leads. Unused commitments falling while loan balances rise does **not** by itself identify draws. Reconcile, ideally for the same facility/entity and interval, new commitments/originations and draws, repayments, expirations/cancellations or limit cuts, purchases/sales and reclassifications. Aggregate RC-L categories need not match the H.8 C&I/NDFI populations. A matched draw record or explicit borrower/lender disclosure is needed, and the financing motive remains a separate attribution question. The previously scheduled Q3 Call Report publication window (~November) can narrow coverage, not guarantee identification.
- **Demand attribution:** the previously scheduled October2026 SLOOS release (early November) gives aggregate bank-reported reasons for C&I demand, including reported movement from less-attractive bank/nonbank financing sources. It can support or weaken a substitution hypothesis in the surveyed population, but does **not** match a named borrower/facility, establish a bond-market origin, or prove that the H.8 balance changes are those draws. Use it as context alongside matched entity evidence, not a direct case-level test.
- Next weekly check: the H.8 of Fri 10/30 (week ending 10/21) shows whether large-bank C&I resumes rising or the quarter-end level holds flat.


**Correction 2026-10-25T14:40:14-04:00 — WQ-523 / DOCKET L839 (Will-approved; PROME packet October25):** the former unused-commitment bullet said the paired stock changes “would identify draws”; the former SLOOS bullet called it “the direct test” of substitution. Both identification claims are withdrawn. Additional stock/flow changes and population mismatches must be reconciled; SLOOS is aggregate reported context. Original dated H.8 values, percentiles, classifications, INSUFFICIENT EVIDENCE verdict and next weekly check are preserved. Pre-correction text: `research/2026-10-25_WQ523-carmart/sources/before-2026-10-23_L818-followup-H8-bank-credit-shift.md`.
