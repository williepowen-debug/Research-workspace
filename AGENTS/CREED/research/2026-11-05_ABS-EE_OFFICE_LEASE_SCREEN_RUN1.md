# ABS-EE office lease screen — run 1, October 2026 reporting cycle

**Written:** 2026-11-05 (Thu), started 11:35 ET on Will's word ("yes"). **Scope:** `research/2026-10-22_ABS-EE_LEASE_SCREEN_SCOPE.md`. **Script:** `scripts/absee_office_screen.py` (34 fixture tests in `scripts/test_absee_office_screen.py`). **Data:** `research/data/2026-10_absee_office_lease_loans.tsv` (824 flagged loans) and `..._summary.json`.

**Use (Will, 2026-11-05 13:08 ET):** *"Keep this as a descriptive lease-rollover screen, with no new recurring cadence or predictive study. Preserve the exploratory two-year result separately. Finish the existing lender earnings grades, and use the loan list when it bears on a specific exposure we already care about."* This is a descriptive record of one cycle. No re-run is scheduled. The two-year window now lives in `research/2026-11-05_ABS-EE_TWO_YEAR_WINDOW_EXPLORATORY.md`; this file carries the approved test only.

**Perimeter, in every sentence that quotes this file:** registered CMBS trusts that file Form ABS-EE, roughly 2017+ vintages, single-property office loans, performing. It does **not** see 144A SASB, CRE CLOs, pre-2017 conduits or bank balance sheets. It is not "the office market" and must not be summed with Trepp's all-CMBS figures.

---

## Bottom line

| Finding | Figure |
|---|---|
| Performing office debt maturing 2026–29, fresh tenant data | **828 loans, $31.87B** |
| Largest tenant's lease ends before the loan matures | 222 loans, **$5.80B (18.2%)** |
| ...and that tenant holds more than 30% of the building | 93 loans, **$2.36B** |
| ...and the loan is already thin (DSCR < 1.25x or occupancy < 80%) | 19 loans, **$0.47B** |

**Read:** in this slice, the anchored, already-thin refinancing exposure through 2029 is small: $0.47B of a $31.87B book (1.5%). The broader rollover exposure is larger: $5.80B (18.2%) has its largest lease ending before maturity.

**The limit that governs all of this:** the flag does **not** separate distressed loans from healthy ones today (§4). It sizes lease rollover. Nothing here shows that it predicts default, so this run does not support the scope's "size the next wave of conversions" framing.

**This changes no band, score or trigger.** S1 stays 4, composite 28/45. Broad CRE-to-bank transmission is not confirmed.

---

## 1. The screen

Book: performing, undefeased, single-property office loans, with each building's notes merged. Tenant data reviewed within about 15 months. Cells are loans / balance. Observation: October 2026 cycle.

| Maturity year | Fresh book | Lease ends first | Share | Largest tenant >30% | Largest tenant >50% | >30% and thin |
|---|---|---|---|---|---|---|
| 2026 | 24 / $0.84B | 3 / $0.05B | 6.5% | 1 / $0.02B | 0 / $0.00B | 1 / $0.02B |
| 2027 | 210 / $8.27B | 30 / $0.58B | 7.0% | 16 / $0.25B | 8 / $0.14B | 1 / $0.03B |
| 2028 | 265 / $9.08B | 70 / $1.65B | 18.2% | 29 / $0.41B | 19 / $0.33B | 7 / $0.10B |
| 2029 | 329 / $13.68B | 119 / $3.52B | 25.7% | 47 / $1.67B | 29 / $1.03B | 10 / $0.33B |
| **2026–29** | 828 / $31.87B | 222 / $5.80B | 18.2% | 93 / $2.36B | 56 / $1.49B | 19 / $0.47B |
| 2030+ | 594 / $23.33B | 340 / $11.62B | 49.8% | 137 / $4.86B | 82 / $2.83B | 10 / $0.50B |
| **All** | 1,422 / $55.20B | 562 / $17.42B | 31.5% | 230 / $7.21B | 138 / $4.32B | 29 / $0.98B |

⚠️ **The rising Share column is not a trend (trap #6).** A loan due in eight months has little time for a lease to end first, so the rate climbs with remaining term by construction. Do not read 7.0% → 49.8% as worsening.

**A known gap in the scoped test:** a lease ending just after maturity passes it, yet a refinancing lender would still see almost no lease term. CREED's exploratory two-year window measures that gap and is kept apart in `research/2026-11-05_ABS-EE_TWO_YEAR_WINDOW_EXPLORATORY.md` (`KB-CREED-105`).

### Largest names in the thin list (2026–29, tenant >30%, lease ends first)

These are candidates to read, not findings of distress. All are performing. "Thin" mixes two tests, so read the cell.

| Balance | Loan | Maturity | Largest tenant (share) | Lease end | DSCR | Occupancy | Note |
|---|---|---|---|---|---|---|---|
| $150.0M | 805 Third Avenue, New York | 2029-12-06 (modified) | Meredith Corporation (35.7%) | 2026-12-31 | 0.99x | 58% | |
| $75.0M | 450-460 Park Avenue South, New York | 2029-05-11 | "460 PARK ave South Tenant LL" (37.7%) | 2028-12-31 | 1.32x | 77% | |
| $41.2M | SunTrust Center, Richmond VA | 2028-06-06 (ARD) | SunTrust Bank (60.8%) | 2028-03-31 | 1.81x | 73% | |
| $25.0M | 16027 Ventura Boulevard, Encino CA | 2027-09-06 | Life Alert (31.6%) | 2027-07-31 | 0.65x | 67% | |
| $24.9M | Tetra Technologies, Spring TX | 2028-02-06 | Tetra Tech (100%) | 2027-12-31 | 2.40x | 23% | occupancy conflicts with a 100% tenant, unresolved |

None of the 19 name-matched a row in `cases/`. The name match is loose, so that is not proof of absence. None adopted: `cases/` is for distress, and these loans are performing.

---

## 2. Perimeter and what fell out

| Step | Loans or rows | Balance | Note |
|---|---|---|---|
| Registered CMBS trusts | 375 trusts | | Class read from each filing header |
| Live assets, all property types | 16,129 rows | $294.46B | |
| Single-property office | 2,397 rows | $67.08B | |
| After merging notes per building | 1,744 loans | $67.08B | 330 multi-note loans; dollars unchanged |
| Defeased, removed | 4 | $0.11B | |
| Delinquent, removed | 121 | $4.75B | Payment status 1, 2, 3, 5 |
| Special servicing, not delinquent, removed | 52 | $2.89B | |
| Status unknown, removed | 1 | $0.15B | 65 Broadway: blank code, paid through June 2024 |
| **Performing book** | **1,566** | **$59.17B** | |
| No lease or maturity to test | 90 | $2.33B | Counted, not imputed |
| Past maturity | 2 | $0.16B | |
| Forward book | 1,474 | $56.69B | |
| Tenant data stale, not tested | 52 | $1.48B | Review over about 15 months old |
| **Fresh book** | **1,422** | **$55.20B** | |

**Office debt the screen does not test, even inside the perimeter:**

| Excluded | Size | Why |
|---|---|---|
| All-office portfolio loans | 130 rows, $4.43B | Tenants are per property; the schema has no allocated balance |
| Mixed-use | 997 rows, $23.92B | Coded MU. Some may be office in substance; not sized |
| Blank property type with a real name | 133 rows, $3.79B | Includes office portfolios such as Corporate Woods |
| Multi-tenant rollover | not measured | Only the largest tenant is tested; a tower can empty through many small tenants |

**Timing of the data:** 371 trusts on the October cycle, 2 on a November period date, 2 on September (§3). 74.2% of the performing balance has a lease review dated 6/30/2026 or 3/31/2026.

---

## 3. Data defects found, all reproduced in the script

| Defect | Size | Treatment |
|---|---|---|
| **Misfiled October tapes.** `BANK 2022-BNK40` (filed 10/27, accession `0001888524-26-019296`) carries BANK 2021-BNK36's tape: 136 assets, one match to the cent, originations ending 9/2021, where September showed its own 113 assets starting with 601 Lexington. `Wells Fargo 2026-5C10` (filed 10/27, accession `0001888524-26-019376`) carries 2024-5C2's tape, 2024 originations in a 2026 deal. | $1.08B and $0.72B double counted if unrepaired | `find_duplicate_tapes()` flags a full match and uses the name year to pick the wrong trust. Their September filings stand in, so those 2 trusts are one cycle old |
| **Blank payment status.** 248 office rows, $5.81B | | Judged on paid-through date: 247 current, 1 unknown and excluded |
| **Trusts disagree on one loan.** 65 of 346 multi-note groups showed different lease dates in the first pass; the same loan passed in one trust and failed in another in 29 | | One record per building: freshest lease review wins, credit status is worst-of. 50 disagreeing loans remain after the same-building key, all resolved this way |
| **Separate buildings under one origination.** Empire Tower I/II/III, 750/770/790 The City Drive | | Key changed to same building; each keeps its own tenant |
| **ARD versus legal maturity.** A loan can show a legal maturity years past its anticipated repayment date | 5 hits, $0.36B on ARD basis | Earliest date used; ARD basis disclosed. Missing an ARD is not a default event |

**Scope correction:** §4 step 2 and §5 of the scope said pari-passu pieces "double-count" balances. Tested and wrong for dollars: each trust reports only its own note (1633 Broadway, 14 notes summing to $730.0M on a $2.4B valuation). Dollars add; only loan counts need merging. The real dollar double count was the misfiled tapes, which the scope did not anticipate.

**Checked and found small:** DSCR can set whole-building cash flow against one trust's debt service (18.76x on one row), but only 34 of 2,107 rows exceed 5x, so the thin cut is not materially distorted.

---

## 4. Positive control

| Test | Trepp (8/21/2026, August data) | This run (October cycle) | Verdict |
|---|---|---|---|
| 5454 Beethoven Street | $33M, Activision 100%, lease to 3/2029, loan to 4/2029 | $33.0M, Activision 100%, 3/31/2029, 4/6/2029 | ✅ Exact on every field |
| One California Plaza | CSAIL 2017-CX10 piece, matured, transferred to special servicing | $43.4M, status 4, transfer 6/22/2026 | ✅ Agrees |
| Second Century | $475.0M | Not in the filings | Consistent with off-EDGAR; deal not confirmed |
| LA MSA lease-first share | 46% of suburban | 47.7% of non-city-of-LA | Same shape, proxy perimeter |
| LA MSA largest-tenant share | 35.9% | 32.6% | Close, proxy perimeter |
| LA MSA lease-first with tenant >50% | $236M | $163M | Not reproduced |
| LA MSA suburban book | 111 loans, $3.5B | 130 loans, $3.93B | Not comparable: different perimeters |
| Whole MSA balance | $11.3B | $6.50B (57%) | Expected: no SASB, no pre-2017 |

**Verdict: PARTIAL.** The fields are right at the loan level. The aggregate does not reproduce within any tolerance CREED can defend, because:
- Trepp's urban/suburban is its own subtype and ABS-EE has no such field. CREED's proxy is outside the city of Los Angeles, so Santa Monica and Beverly Hills count as suburban here.
- "Los Angeles MSA" comes from Trepp's Table 2 label. CREED ran LA County first (32.5%), then LA plus Orange. The MSA reading is the defensible one, but two perimeters were tried, so the 47.7% match is not evidence on its own.
- The scope set no numeric tolerance, and CREED did not invent one after seeing the result.

**Does the flag mean anything? Tested cross-sectionally, it does not separate:**

| Group | Loans | Balance | Lease first | Lease first, tenant >30% |
|---|---|---|---|---|
| Performing | 1,566 | $59.17B | 32.0% | 13.3% |
| Delinquent or special servicing | 174 | $7.79B | 34.4% | 13.7% |

Not a clean backtest: today's tenant fields postdate the distress, and 25.0% of the distressed balance has a stale lease review. But it gives no support to the flag as a distress predictor. One California Plaza makes the same point: AECOM holds 11.8%, with a lease to 2032, so the screen would never have flagged it. Trepp's distress there came from many tenants shrinking, which this screen does not measure.

**Field lag:** the One California row reports 73% occupancy against Trepp's 55% (July 2026, servicer commentary), with a lease review dated 6/21/2024. Occupancy fields can run well behind reality, so "thin" likely understates. That row is excluded here on servicing status, not on this test.

**Slice delinquency, for scale:** $4.75B of $66.96B = 7.1%, open special servicing 11.2%, against Trepp's national office 12.33% DQ [October] and 16.85% SS [September]. Definitions are not identical. Lower is the expected direction, since the worst SASB and pre-2017 loans are outside this slice.

---

## 5. What Will should know

1. **It answers part of the question.** The scoped number exists and is small. It is a floor for the anchored, already-thin case only, and only inside registered conduits.
2. **The Wilshire Courtyard, EY Plaza and Second Century type of loan is invisible here.** That is where Trepp's Los Angeles distress actually sits.
3. **Not a VX vector (WQ-613, 11/05).** It has not shown it predicts anything.
4. **Descriptive only (Will, 11/05).** No recurring cadence and no predictive study. Use the loan list when it bears on a specific exposure already under watch. See `README.md` for how to read it, including what absence from the list does not mean.

## 6. Not done

Multi-tenant rollover · portfolio loans · mixed-use with office tenants · confirmation of Second Century's deal · any non-office type · loan-level reading of the flagged names · resolving the Tetra Technologies occupancy conflict · notifying the trustees or the filing agent of the two misfiled tapes.
