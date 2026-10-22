# CREED — does the junk-spread widening transmit to CRE refinancing? (Will's question, SIG-W-20261022-005)

**Written:** 2026-10-22 12:25 ET (clock-stamped) · **Session:** Will-launched CREED boot (Will 12:19 ET: *"boot up … catch up on any new data or signal"*); this launch is the answer to WQ-478 (whether to launch CREED for the CRE leg) · **Answers:** WALTER SIG-W-20261022-005 (CREED ACTION) and the "Route 2: UNKNOWN" row of SIG-W-20261022-012.
**Moves no band, score, trigger or prediction. Convergence stays 27/45.** Descriptive watch lines below are NOT registered thresholds (bands gate on Will).

---

## 1. Answer in one paragraph

**The direction is right, but the channel into CRE is the 10-year Treasury rate, not junk spreads. Securitized CRE credit has not repriced with junk bonds.** Through 10/16, new CMBS and CRE CLO AAA spreads sat at their 3-month averages (CREFC, primary-read). What has risen is the **loan coupon**: 5-year conduit pools averaged **6.89%** over the last 3 months vs **6.53%** YTD, because the 10-year sat at 5.0–5.3%. That shrinks the loan a property can refinance into, which is the maturity-default path behind `CREED-T-02` (fired 8/20) and the office clock `T-01a` (leg 1 of 2). **The lenders' stocks took a rare hit**: the commercial mREIT index fell **−16.6% in 21 sessions to 10/21**, the 1.6th percentile since mid-2021. But they fell only **−4.3pp more than agency mREITs**, which carry the rate shock with almost no credit risk. That gap is inside one standard deviation (5.5pp), so it reads as a **rate shock like Sep–Oct 2022, not a credit shock like March 2023**, though it has drifted slightly toward the credit side since early October.

## 2. Evidence table

| Leg | Figure [date, basis] | Source (remove) | Read |
|---|---|---|---|
| HY / CCC / BB / IG OAS | HY 266 [9/21] → 333 [10/20] → 327 [10/21]; CCC 1,327 [10/20]; BBB 108 [10/20]; IG 87 [10/20] | FRED via `fetch.py`, first-published (PRIMARY-READ); 9/21 and 10/21 values per WALTER 005/012 | Widening led by CCC; the IG/BBB tier, where CRE REIT unsecured debt sits, moved ~+10bp |
| 10-year Treasury | 4.96 [9/21 ^TNX] → 5.28 [10/2 official, per LakeRock citing Treasury] → 5.12 [10/20 FRED DGS10] → 5.15 [10/21 ^TNX] → **5.00 intraday 10/22** | FRED / yfinance (PRIMARY-READ); 10/2 = SECONDARY | The variable that actually prices CRE refinancing |
| New-issue CMBS / CRE CLO spreads | Week to 10/9: 5-yr conduit LCF AAA **T+83** (3-mo avg T+83; year-earlier 82) · fixed SASB AAA T+100 (avg 122) · floating SASB AAA S+175 (avg 159) · CRE CLO Class A **S+150** (avg 143; year-earlier 152). Week to 10/16: BLK 2026-FL1 Class A **S+150** | CREFC CMBS New Issue Snapshot, data through 10/9/26 and 10/16/26, from Commercial Mortgage Alert (PRIMARY-READ, `pdftotext -layout`) | **No spread transmission through 10/16.** The floating SASB print was 16bp wide on one hotel deal (JPMCC 2026-ARLO), one deal |
| Loan coupons (the actual refinancing cost) | 5-yr conduit coupon **6.89%** last 3 mo (4 deals) vs **6.53%** YTD; fixed SASB coupon 6.27% vs 5.94%; floating SASB spread S+242 vs S+219 | CREFC, same files (PRIMARY-READ) | **Borrower cost is up ~35bp, from base rates rather than bond spreads.** Lower supportable proceeds → more maturity defaults |
| Issuance volume | YTD private-label $146.1B, **+19.0%** YoY [10/16]; CRE CLO $38.0B, **+64.3%**; SASB 81.7% refinance-purpose | CREFC (PRIMARY-READ) | Market open, refinancing flowing through securitization |
| Thin week | Week to 10/16: 1 deal ($1.25B CRE CLO); **"first week since the New Year holiday week without a conduit or SASB pricing; 2025 had six such weeks"** | CREFC (PRIMARY-READ) | Weak tell. One week, and it happened six times in 2025 |
| Withdrawn deal / weakening demand | "Bridge Investment Group withdrew a planned $1.2B CRE CLO as spreads deteriorated"; Green Street headline 10/16 "demand for CMBS weakens as spreads widen" | Search-engine summaries attributing to Commercial Mortgage Alert / Green Street. **NOT READ: CMA and Green Street paywalled; a direct search found no withdrawal report.** UNVERIFIED | **Do not cite as fact.** If true, it is the first credit-closure tell in this episode |
| Commercial mREIT equity | 9/21 → 10/21 total return: GPMT −42.2 · ABR −33.2 · ACRE −25.1 · CMTG −25.0 · BXMT −20.1 · FBRT −19.5 · KREF −17.6 · STWD −16.3 · TRTX −15.8 · **LADR −2.7** · ARI −1.4 (liquidating; excluded) | yfinance, Adj Close, dividends in window checked (PRIMARY-READ tape) | Severe and broad; LADR the outlier |
| Corporate actions (trap #1) | No 8-K 9/21–10/22 at BXMT, KREF, STWD, ABR, FBRT, CMTG. **GPMT 1-for-10 reverse split eff. 10/5** (series confirmed split-adjusted, continuous across 10/6). ARI to delist ~10/27, last NYSE trade ~11/6 (8-K 10/16, Item 3.01). ACRE sold a deed-in-lieu NC office for $64M (8-K 9/22). TRTX and GPMT financing 8-Ks (10/5–10/6) | SEC EDGAR (PRIMARY-READ) | **The drawdown is a cohort-wide market move, not name news.** ARI's tape is distribution-anchored and excluded |
| Agency mREIT control | AGNC −10.8 · NLY −12.3 · MORT −13.7 · REM −13.6 (TR, same window) | yfinance | The rate effect alone is ~−11 to −12% |
| Base rate (n = 1,334 sessions since 2021-06) | Commercial index (median daily TR of 9 names ex-ARI, ex-GPMT) 21-session TR **−16.6%** = 1.6th pct (23 sessions worse). Excess vs agency **−4.29pp**: 21.8th pct; mean −0.96, sd **5.46** | CREED computation (ANALYTICAL): yfinance auto-adjusted closes 2021-06-01 → 2026-10-21; commercial = cross-sectional MEDIAN of daily returns of BXMT KREF LADR STWD ABR TRTX ACRE FBRT CMTG, compounded; agency = mean of AGNC NLY; 21-session compounded returns; excess = commercial − agency | Rare level, ordinary relative move |
| Analogues | **Sep–Oct 2022 (rate shock):** commercial −17 to −19%, **+6 to +20pp vs agency**. **Mar 2023 (SVB, credit):** −17 to −24%, **−6 to −10pp vs agency**. **Oct 2026:** −16.6 to −19%, **−1.8 to −2.0 (10/2–10/6), +1.8 (10/7), −4.1 (10/19), −3.7 (10/21)** | same | Between the two, nearer the rate case, drifting toward the credit case |
| Same-day check, 10/22 intraday | SPY −0.99%, dealer gamma negative (WALTER 004); 10y −14bp intraday; every commercial mREIT +3% to +10% (CMTG +10.4) | yfinance intraday ~12:20 ET (NOT a close) | Lenders traded on rates, not on the risk-off. One intraday day: corroboration, not proof |
| Lender fundamentals, first Q3 print | Ladder Q3: GAAP pre-tax $67.3M ($0.53); distributable $0.35 ($0.38 before charge-offs); **"grew book value"**; >$700M new investments; Baa3/BBB- stable | LADR 8-K Ex-99.1, 2026-10-16 (PRIMARY-READ) | Counter-evidence to lender-capital withdrawal. One name, the most conservative in the cohort |

## 3. Why the channel is rates, not spreads (mechanism, ANALYTICAL)

1. CRE refinancing is priced off Treasuries/SOFR **plus a CRE-specific spread**. Corporate HY OAS is not a quoted CRE loan spread. The two co-move only when the same risk appetite reprices both, as in March 2023.
2. October's HY widening is **CCC-only** (REGINALD/BROCK via WALTER 012: CCC +112bp, BB −2bp, 10/1 → 10/20). The CRE debt stack's marginal buyers (CMBS AAA–BBB, CRE CLO AAA, life companies, banks) sit in the IG/BB tier, which barely moved.
3. The base rate **did** move: 10y 4.79 [9/2] → 5.28 [10/2] (secondary). On a **DSCR-constrained interest-only** loan, proceeds scale with 1/coupon, so 6.53% → 6.89% cuts supportable proceeds ~5% and +50bp ~7% (arithmetic, ESTIMATE). A loan bound by a debt-yield test is unaffected by the coupon. A loan already short of a refinance gets shorter. That is how the matured-balloon book is **converting to non-performing** (Trepp Sept, `KB-CREED-057`) instead of clearing.
4. ⇒ **If HY widening reaches CRE at all, it comes through the lenders' cost of capital** (mREIT equity, CRE CLO senior spreads, bank warehouse lines to debt funds), not through the borrower's coupon. That is the leg to watch.

## 4. What would change this read (descriptive, NOT registered thresholds)

| Watch | Now | What it would mean |
|---|---|---|
| CRE CLO Class A new-issue spread | S+150 [10/13], 3-mo avg S+143 | A print well wide of the 3-mo average, or deals pulled, would show the spread channel opening. Source: CREFC weekly snapshot (free, Fridays) |
| Commercial mREIT excess vs agency, 21 sessions | −3.7pp [10/21], sd 5.46 | Sustained −8pp or worse looks like March 2023 (credit-type), not 2022 |
| mREIT Q3 prints (BXMT, STWD, KREF, ABR ~10/23–11/7) | LADR only: book value up | Dividend cuts plus realized book erosion across names = `CREED-T-08b` (graded at primary, routes to LIQUID) |
| Trepp October DQ (~early Nov) | Office 12.16 [Sep] | ≥ 12.01 = `CREED-T-01a` FIRES (leg 2 of 2) |
| 10-year | 5.00 intraday [10/22] | Back above ~5.25 re-tightens refinancing; a sustained fall below 5 is the relief path |

## 5. Caveats that travel with this answer

- **CREFC spread data runs through 10/16.** HY widened a further ~9bp to 10/20 before easing to 327 on 10/21. The week to 10/23 is not yet published.
- **The Bridge withdrawal and "demand weakens" items are unverified.** CREED could not reach the source. If either is real, the "no spread transmission" line weakens.
- **The base-rate index is method-dependent.** Median of daily returns (−16.6%) vs median of window returns (−19.5%). The rate-versus-credit classification holds on both.
- **10/22 figures are intraday.** S8a reads −11.79pp TR intraday; the stored `VX-CREED-7.01` stays the 10/21 close (−11.48).
- **The bank side is REGINALD's and BROCK's** (BANK-ABSENT, ~0.6; non-bank-lender lending growing, no losses). CREED does not re-grade it. **Broad CRE-to-bank transmission is not confirmed.**
- **Source-unblock note (Standing Obligation 5):** the CREFC snapshot gives free weekly AAA and AS/AM new-issue CMBS/CRE CLO spreads. It does **not** give BBB−. That narrows obligation 5 rather than discharging it.

## 6. Vectors this feeds (trap #8, a grade is a propagation)

`VX-CREED-3.01/3.04` (maturity path: no value change, mechanism note only) · `VX-CREED-7.01` (unchanged; intraday not stored) · `VX-CREED-10.02` (its registered definition is mREIT vs office equity REITs, a **different** measure; NOT re-measured on that definition, the KB-062 measure is not substituted into it) · `VX-CREED-10.01/10.03/10.04` (unchanged; Q3 census not re-run, LADR only) · Standing Obligation 5 (narrowed). KB rows: `KB-CREED-061` (CREFC spreads), `KB-CREED-062` (mREIT drawdown classification), `KB-CREED-063` (LADR Q3).
