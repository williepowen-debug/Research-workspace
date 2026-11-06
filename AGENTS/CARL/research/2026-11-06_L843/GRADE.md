# D:L843 — ALLY matched-vintage loss comparison and Q3 filing notes

**Stamp:** 2026-11-06 07:43 ET. **Owner:** CARL. **Authority:** WQ-626 A, bounded session, PROME prome-96. No trade, card, gate, band or threshold moved. Score 53/70 v2.6.6 unchanged.

## Answer

**CRL-21 resolves MISSED. The comparison the 10/26 review called unavailable was computable from Ally's own filings, and it shows the opposite of the forecast.** At the same age, Ally's 2025 loans have charged off 38 bp LESS than its 2023 loans, not 50 bp more. 2026 loans are 5 bp lower on charge-offs after nine months.

**The reading is not all-clear.** FY2024 was the best vintage. FY2025 is 16.6 bp worse than FY2024 at the same age, and FY2026 is the first vintage whose early delinquency sits above FY2023: 1.94% vs 1.79% at 30+ days, 0.58% vs 0.49% at 60+ days. FY2026 is nine months old, so that is a question for the 10-K, not a finding about its losses (CRL-36).

## 1. The comparison

**Measure:** cumulative gross charge-offs by origination year ÷ retail originations of that year (used + new, excluding lease). Ally consumer automotive, on book. Sources: origination-year gross charge-off tables, Notes to the 10-Qs of 9/30/23, 9/30/24, 9/30/25, 9/30/26 and the 10-Ks of 2023, 2024, 2025; originations from each MD&A. Reproduce: `tools/vintage_loss.py`, output `VINTAGE_OUTPUT.txt`.

| Age (end of month, year of origination + n) | FY2023 | FY2024 | FY2025 | FY2026 | FY2025 − FY2023 | FY2026 − FY2023 |
|---|---:|---:|---:|---:|---:|---:|
| Sep Y+0 (÷ nine-month originations) | 0.344% | 0.247% | 0.222% | 0.294% | −12.3 bp | **−5.0 bp** |
| Dec Y+0 | 0.606% | 0.449% | 0.428% | | −17.8 bp | |
| Sep Y+1 | 2.133% | 1.587% | 1.753% | | **−38.0 bp** | |
| Dec Y+1 | 2.705% | 2.034% | | | | |
| Sep Y+2 | 4.251% | 3.295% | | | | |
| Dec Y+2 | 4.717% | | | | | |
| Sep Y+3 | 5.851% | | | | | |

Second denominator (on-book balance at the vintage's first 9/30 or 12/31): FY2025 −51.1 bp at Sep Y+1, FY2026 −6.4 bp at Sep Y+0. Same direction.

Dollars behind the headline row: FY2023 $225M + $567M = $792M on $37,123M; FY2025 $168M + $520M = $688M on $39,240M.

**Comparable seasoning holds:** nine-month share of annual originations was 75.9%, 73.9% and 74.7% for FY2023/24/25, so average loan age at each date differs by under a month.

**Transcription check:** each of the seven source rows sums to its printed total (1,634 · 2,284 · 1,976 · 2,681 · 1,937 · 2,610 · 2,022).

### Delinquency at matched age (on book, leads charge-offs)

| Age | FY2023 30+/60+ | FY2024 30+/60+ | FY2025 30+/60+ | FY2026 30+/60+ |
|---|---:|---:|---:|---:|
| Sep Y+0 | 1.79 / 0.49 | 1.55 / 0.42 | 1.47 / 0.41 | **1.94 / 0.58** |
| Dec Y+0 | 2.46 / 0.74 | 1.93 / 0.58 | 2.02 / 0.62 | |
| Sep Y+1 | 4.65 / 1.70 | 3.87 / 1.38 | 4.35 / 1.58 | |

Source: origination-year credit quality tables, same filings; `tools/vintage_tables.py`.

## 2. Deal-level CNL, the evidence class the row names

Five publicly registered AART deals, 114 certificates, parsed to `AART_PANEL.tsv`; manifest with SHA-256 at `sources/aart/manifest.json`.

| Deal | Coupon | Age at cut-off | CNL month 8 | CNL month 13 | Latest |
|---|---:|---:|---:|---:|---:|
| 2023-1 | 8.68% | 9.6 mo | 0.1924% | 0.4123% | 1.3822% (m40) |
| 2024-1 | 9.62% | 17.2 mo | 0.2398% | 0.4767% | 1.1579% (m32) |
| 2024-2 | 9.89% | 16.9 mo | 0.1693% | 0.3490% | 0.7161% (m26) |
| 2025-1 | 9.52% | 17.1 mo | 0.2396% | 0.4466% | 0.4466% (m13) |
| 2026-1 | 9.10% | 16.9 mo | 0.1477% | | 0.1477% (m8) |

- Same deal month, against 2023-1: 2025-1 **+3.4 bp** at month 13; 2026-1 **−4.5 bp** at month 8. Inside ±25 bp, nowhere near +50 bp.
- Matched on loan age, 2023-1's loss between ages about 17 and 30 months is about 0.59% against 0.4466% for 2025-1: about **−15 bp** (rough interpolation; 2023-1's base has already amortized, so the true gap is wider).
- ⚠️ These pools do not isolate origination years. At 17 months old at cut-off, 2025-1's average loan dates to about spring 2024 and 2026-1's to about autumn 2024. Corroboration only. The 10-Q table is the cohort-true read.

## 3. How the result was tested

| Risk | Test | Result |
|---|---|---|
| Sold loans leave the numerator | Added every off-balance-sheet auto net loss of 2025 and 9M-2026 ($249M) to FY2025 alone, none to FY2023 | **+25.4 bp**, still under +50 bp. Deliberately impossible: those losses span all vintages |
| The bar is lifetime, the read is at about 21 months | FY2023 at Sep Y+1 is 36.5% of its Sep Y+3 total, so +50 bp scales to about +18 bp at this age | Measured −38 bp. Only the impossible bound clears the scaled bar |
| Gross, not net | Recoveries are not disclosed by vintage. Consumer auto recoveries ÷ gross charge-offs were 34.7% FY23, 32.5% FY24, 36.2% FY25, 40.9% 9M-26 | Rising recoveries do not narrow the gap |
| Excluded items | Held-for-sale write-downs of $41M (2023), $5M (2024), $5M (2025) are excluded from the tables | Not attributable to a vintage; too small to matter |
| Post-hoc construction | CARL chose this measure after the outcome existed | ⚠️ Disclosed. Two denominators, the deal-level class and the bound all point the same way; no specification tried reaches +50 bp |

## 4. Resolution of CRL-21

| Reading of the letter | NCO two-quarter leg | Vintage ≥ +50 bp | Result |
|---|---|---|---|
| Headline, AND | Failed 7/21 (Q2 −40 bp) | Not met | MISSED |
| Dated operative Notes, OR | Failed | Not met | MISSED |

The row misses under both constructions, so the AND/OR ambiguity does not need settling. Q3 window unchanged, no extension. Marked at 25%.

**Why this is not a substitute basis.** The row's Notes name the evidence: "mgmt commentary, ABS prepay/loss curves, deal-level CNL trajectories", against the "FY2023 vintage trajectory", and its Instrument cell is ALLY quarterly filings. Realized trajectories from Ally's filings and AART certificates sit inside that. STUCK stood on the claim that no measurable input existed, and that claim is withdrawn below. ⚠️ **What a reader can contest:** the letter says "projections", and no lifetime projection is published anywhere. If PROME or Will reads that word strictly, the row stays STUCK forever on a comparison that points the other way. CARL's view is that this would turn NO-VERDICT into an escape from an ordinary miss, which the 11/5 brief forbids. It is reversible on their word.

**Negative-resolution search, dated 2026-11-06:** EDGAR submissions for ALLY and five AART trusts; full-text search of the Q3 10-Q; 10/26 EX-99.2 and EX-99.3 retained. ⚠️ **Management's call commentary was NOT read:** Benzinga returned 403, Fortune carries the header only, Quartr is not used under Will's standing note. A qualitative remark could not supply the numeric +50 bp, so the gap does not change the grade, but it is a gap.

**Invalidation clause not triggered on its letter:** it needs NCO QoQ <+30 bp (Q3 was +32 bp) and vintages within ±25 bp (FY2025 is outside that band, on the better side). The row resolves on its hit condition instead. WQ-288 does not apply.

**⚖️ Position clause, for Will via PROME.** The row carries a pre-registered commitment on failure: trim shorts 25% and extend duration to Q2-2027 or later. Will's 7/24 ruling deferred it, and Cell B on 8/15 set "hold, revisit at the ~Oct vintage leg". That leg has now read, so the revisit is due. CARL holds no book; the paper sleeve closed 10/28. The only live candidates visible are FORGE D-74's bank/credit put cluster (41 contracts, 14 lines, basis $6,644.24, value $554.00, Fidelity marks intraday 11/5), whose owner, card and approval are recorded UNKNOWN. Nothing here is a card or a trade. S&P fell 4.4% on 11/5, so the position question should be read against today's tape, not this evidence alone.

## 5. Correction to CARL's 10/26 review

ALLY_RITM_GRADE.md said the Q2 10-Q origination-year table was "a snapshot of balances/DQ by origination year" and graded the row STUCK as an "instrument/publication gap". **That was incomplete.** The same Note has carried gross charge-offs by origination year since the 2023 filings, and AART 2023-1, 2024-1 and 2024-2 were reachable for a same-month CNL match. A true statement (no published lifetime projection) carried a false conclusion (no measurable comparison). The search stopped at the first table that looked like the answer. No figure in that review is wrong; its conclusion is withdrawn. M68 extended.

## 6. Q3 filing notes

### ALLY 10-Q, filed 2026-11-02 (0000040729-26-000023)

| Item | Q3 2026 | Comparison | Read |
|---|---:|---:|---|
| Consumer auto 30+ | $4.5B, +$49M vs YE | "decline in delinquency rate trends" (MD&A) | Portfolio growth, company's words |
| Nonprime share of HFI auto | 11.0% | 10.1% at YE | Credit box widening |
| Nonprime originations (<620) | 11% | 9% Q3-25 | Same |
| 76+ month term, share of retail | 26% | 23% | Longer terms |
| Used average FICO | 698 | 702 | Slight drop; new 730 vs 725 |
| S-tier share | 44% | 47% Q2 (EX-99.2) | Mix shift |
| Carvana share of auto loans | 12.7% | 10.4% at YE; facility +$2.0B to $8.0B | Company: performance "consistent" with similar credit |
| Off-book whole-loan balance | $4,253M | $2,190M YE, $1,155M YE-24 | "Record passthrough volume" above $1B in Q3 (EX-99.2) |
| Whole-loan 60+ | $238M, 5.6% | On-book auto about 1.84% | Different credit box, see below |
| Whole-loan net losses | $46M | $28M Q3-25 | |
| Lease average loss per vehicle | $914 | $53 gain Q3-25 | Plug-in hybrid and recall pressure, company's words |

**Not hidden on-book loss.** The filing describes pass-through programs for applications that "do not meet our underwriting criteria", sold to third-party lenders, and no held-for-investment auto loans moved to sale in 2025 or 2026. The Note says "includes" pass-through, so that is not proven to be the whole pool. What it does show is that private money is increasingly funding borrowers Ally itself declines: the pool grew 3.7× in 21 months, at about three times the on-book 60+ rate.

Company language at EX-99.2: provision build reflects "strong asset growth" and "stabilization in credit trends"; FY retail auto NCO guide 1.8–2.0%, "tracking toward midpoint". Filing silent on vintage expectations.

### RITM 10-Q, accepted 10/30, filing date 11/02 (0001556593-26-000035)

| Item | 9/30/26 | 6/30/26 | 12/31/25 | 9/30/25 | Read |
|---|---:|---:|---:|---:|---|
| Ginnie Mae loans subject to repurchase | $4.6B | $4.3B | $4.0B | n/a | Loans 90+ late or in qualifying forbearance; UPB only +3.0% YTD ($151.7B to $156.3B). Rounded figures |
| Foreclosure advances | $1,050.2M | $1,070.1M | $941.7M | $849.0M | +23.7% YoY, −1.9% QoQ |
| P&I advances | $547.5M | $509.6M | $539.4M | $583.7M | −6.2% YoY |
| Advance reserve provision, year to date | $94.0M | $54.6M | | $38.6M | Q3 alone $39.5M, above all of 9M-25 |
| Advance write-offs, year to date | $82.2M | $48.6M | | $42.5M | |

**CRL-20 stays 1%.** The filing supports the supplement's GNMA direction with a deeper-stage measure. It says nothing on modification accounting (zero hits for partial claim, loss mitigation or modification accounting), so "despite the mod-accounting cushion" stays untestable. Issuer perimeter: RITM's owned book and repurchase right, not all Newrez servicing, and GNMA is not FHA-only. Rising advance reserves are consistent with stress and also with reserve practice; the filing does not separate them.

## 7. What this changes

| Surface | Change |
|---|---|
| CRL-21 | STUCK → MISSED, 2026-11-06, scored at 25% |
| CRL-20 | Unchanged 1%; RITM filing note appended |
| CRL-31 | Unchanged 50%; ALLY Q4 is one of its legs |
| Masking framework | The intermediate falsifier missed. The outer falsifier CRL-20 is at 1%. Mechanism not killed: FY2026 delinquency and the sequential worsening since FY2024 are live, and neither is a loss result |
| Score | 53/70 unchanged. No vector letter fired |
| New | CRL-35 (ALLY Q4 NCO) and CRL-36 (FY2026 vintage at 12/31) carry this forward prospectively |
