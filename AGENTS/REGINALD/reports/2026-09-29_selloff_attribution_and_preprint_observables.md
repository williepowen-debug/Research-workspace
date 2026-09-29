# Regional-bank selloff, 8/13 → 9/29: attribution of both legs + the pre-print observable set

**Author:** REGINALD · **Date:** 2026-09-29 ~19:0x ET (corrected at closeout against `date`; written as ~19:3x) · **Asked by:** Will (*"Lets address these gaps"* — ① the unattributed 8/14→9/14 leg; ② the desk's blindness to credit before the Q3 prints) · **Data:** yfinance settled closes through 9/29 (`scratchpad/closes.csv`); FRED H.8 weekly (SA, through **9/16**) and H.4.1 (through **9/23**), own pull 9/29 ~19:1x ET; cohort metrics from `reports/2026-09-24_cohort_AOCI_exposure.md`, `workbook/NDFI_COHORT.tsv` [6/30], `workbook/CRE_RCN_COHORT.tsv` [6/30], `BANK_EXPOSURE_MATRIX.md` v2.0. **Nothing here moves a score, threshold or trade.**

## 0. Findings in five lines

1. **Leg 1 (8/13 → 9/14, KRE −4.7%) is attributed: market + small-cap beta.** A five-factor model fit on the prior year explains −3.9 of −4.8 log-%: S&P −1.9, small-cap-vs-S&P −2.3, financials-vs-S&P **+0.1**, duration −0.4. Residual −0.9%. **There was no bank-sector component** — XLF tracked SPY and KBWB (large banks) fell the same as KRE. The "catalyst unidentified" thread closes as **ROTATION / RISK-OFF BETA, not a bank event.**
2. **Leg 2 (9/15 → 9/29, KRE −5.8%) is a FINANCIALS-SECTOR move led by the LARGEST banks.** Factors explain −7.1 of −5.9: financials-vs-S&P **−5.0**, small-cap −2.7, duration −0.7, credit ETF +0.8 (offsetting). **KRE's residual is +1.1%: regionals did BETTER than their factor loading.** KBWB −7.4% and IAT −7.7% fell more than KRE.
3. **Cross-section, 14 cohort names: leg 2 sorted on SIZE (Spearman −0.72), not on any credit metric I own.** The six largest (CFG, HBAN, MTB, ZION, FLG, VLY) fell −8.1 to −9.5%; the four smallest (EGBN, AMTB, WAL, BKU) fell −0.1 to −4.3%. My matrix score correlates **+0.48** (higher-risk names fell LESS); AOCI exposure −0.30 (right sign, weak); NDFI/PC-NDFI −0.2 to −0.4 (weak); CRE concentration +0.25 (wrong sign). n=14, none of the credit sorts is distinguishable from zero.
4. **Credit instruments barely moved while bank equity did:** over leg 2 HYG −1.5%, bank preferreds (PFF) −1.4%, BDCs (BIZD) −0.8%. The selloff is in bank EQUITY multiples, concentrated in incumbents' size, not in bank CREDIT.
5. **Pre-print observables (H.8 through 9/16, H.4.1 through 9/23) show NO transmission yet:** small-bank deposits flat, C&I +0.4%, CRE +0.2%, loans to non-bank financials **+1.1% (still growing)**, discount-window primary credit $6.2B (ordinary: 60-week median $5.8B, 28 of 60 weeks ≥ $6B). The set is registered below as the weekly read until the prints.

## 1. Factor decomposition (KRE daily log returns)

Model: KRE = α + β₁·SPY + β₂·(IWM−SPY) + β₃·(XLF−SPY) + β₄·TLT + β₅·(HYG−TLT), OLS on 2025-09-02 → 2026-08-13 (n=238, R² 0.63). Betas: SPY 0.84 · small-cap 0.76 · financials 0.85 · TLT 0.22 · credit 0.42.

| Leg | KRE actual | Explained | Residual | S&P | Small-cap | Financials | Duration | Credit-ETF |
|---|---|---|---|---|---|---|---|---|
| **L1 8/14→9/14** | **−4.8%** | −3.9% | −0.9% | −1.9 | −2.3 | **+0.1** | −0.4 | +0.2 |
| **L2 9/15→9/29** | **−5.9%** | −7.1% | **+1.1%** | +0.4 | −2.7 | **−5.0** | −0.7 | +0.8 |
| Total 8/14→9/29 | −10.7% | −10.9% | +0.2% | −1.5 | −5.0 | −4.9 | −1.2 | +1.0 |

*(log-% contributions; factor moves in the same windows: L1 SPY −2.2 / IWM−SPY −3.1 / XLF−SPY +0.1 / TLT −2.0; L2 SPY +0.4 / IWM−SPY −3.6 / XLF−SPY −5.9 / TLT −3.4 / HYG−TLT +1.9.)*

**Reading.** Leg 1 is what a 5% small-cap drawdown does to a regional-bank ETF with a 0.76 small-cap beta; the bank sector contributed nothing. Leg 2 is the financials sector repricing (−5.9% vs the S&P) while the S&P itself was flat; regionals carried their sector beta and no more. ⚠️ The credit-ETF term is POSITIVE in leg 2 because HYG fell less than TLT — cash-bond ETFs did not transmit the B/CCC OAS widening; that widening is visible in FRED's OAS series, not in these prices.

## 2. Cross-section: what the 14 names sorted on

| | L1 % | L2 % | Total % | Matrix | AOCI/CET1 % | NDFI % | PC-NDFI % | CRE conc % | MF % | Nonacc % | Assets $B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FLG | −8.8 | −9.1 | **−17.0** | 6 | 6.9 | 5.7 | 1.8 | 64.9 | 48.6 | 5.49 | 87.7 |
| VLY | −7.9 | −8.1 | −15.3 | 3 | 1.5 | 3.4 | 2.7 | 58.2 | 17.0 | 0.86 | 66.2 |
| MTB | −6.1 | −8.5 | −14.1 | 1 | 0.4 | 9.5 | 4.0 | 24.7 | 4.8 | 1.10 | 218.8 |
| HBAN | −5.6 | −8.9 | −14.1 | 0 | 8.7 | 9.2 | 3.8 | 13.2 | 2.0 | 0.59 | 283.1 |
| CFG | −4.8 | −9.4 | −13.8 | 0 | 10.7 | 14.7 | 10.7 | 20.0 | 5.5 | 1.07 | 232.5 |
| ZION | −3.4 | −9.5 | −12.6 | 1 | 22.3 | 4.0 | 1.9 | 38.1 | 4.9 | 0.53 | 91.0 |
| OZK | −6.0 | −5.9 | −11.6 | 2 | 0.5 | 10.0 | 8.6 | 64.5 | 11.5 | 0.46 | 41.7 |
| BKU | −7.0 | −4.3 | −11.0 | 2 | 6.5 | 9.0 | 2.2 | 34.4 | 2.9 | 1.60 | 34.9 |
| CUBI | −5.4 | −5.6 | −10.7 | 1 | 2.5 | 34.1 | 20.0 | 33.6 | 15.3 | 0.17 | 26.5 |
| SBCF | −4.4 | −5.8 | −9.9 | 2 | 4.3 | 0.5 | 0.3 | 55.4 | 2.6 | 0.55 | 21.3 |
| SSB | −4.3 | −5.7 | −9.8 | 2 | 4.7 | 1.5 | 0.6 | 55.3 | 5.9 | 0.62 | 68.8 |
| WAL | −3.1 | −4.3 | −7.3 | 2 | 5.9 | 24.1 | 7.5 | 26.4 | 1.5 | 0.86 | 98.6 |
| EGBN | −2.8 | **−0.1** | −2.9 | 5 | 7.7 | 1.4 | 0.0 | 77.0 | 14.1 | 3.23 | 9.6 |
| AMTB | +1.2 | −1.4 | −0.2 | 5 | 2.5 | 1.3 | 0.0 | 49.9 | 5.2 | 1.77 | 10.3 |

**Spearman rank correlation, leg return vs metric** (negative = higher metric ⇒ worse return; n=14, |ρ| < ~0.5 is not distinguishable from zero):

| Metric | L1 | L2 | Total |
|---|---|---|---|
| **Assets (size)** | −0.29 | **−0.72** | **−0.61** |
| Matrix score (v2.0) | +0.03 | **+0.48** | +0.25 |
| AOCI / CET1 | +0.25 | −0.30 | −0.03 |
| Securities / assets | +0.35 | +0.15 | +0.32 |
| NDFI % loans | −0.29 | −0.22 | −0.28 |
| PC-NDFI % loans | −0.37 | −0.33 | −0.38 |
| CRE concentration | −0.03 | +0.25 | +0.13 |
| Multifamily % | −0.31 | −0.07 | −0.25 |
| Nonaccrual % | −0.05 | +0.23 | −0.01 |

**Reading.** Leg 2 is a SIZE sort: the market sold the biggest banks in the cohort hardest and left the small ones nearly alone — the opposite of a credit-quality sort (my matrix's top names, EGBN and AMTB, are the two best performers). Two candidate mechanisms fit a size sort and neither is a regional-credit event: **(a) the rate/AOCI leg in DOLLARS** (the largest securities books are at the largest banks; the AOCI/CET1 ratio sorts only weakly because ZION's outsized ratio sits on a mid-size bank), and **(b) the "AI disruption of incumbents" narrative NEXUS carries as candidate Root B** (WQ-341) — a deposit-franchise repricing story that targets the largest deposit franchises first. ⚠️ The two NYC rent-regulated multifamily names (FLG, VLY) are the exception that IS credit-shaped: worst in BOTH legs, and FLG broke its ORANGE price band 9/28. **Total-period NDFI/PC-NDFI sorts stay weak (−0.28 / −0.38), confirming the August negative result that WQ-318 must retain.**

## 3. Pre-print observables — the weekly read until the Q3 prints

Every instrument this desk owns reads a closed quarter. These are the weekly public series that would move FIRST if cause ② (credit reaching banks through non-bank lending) or a funding leg were real. Values are levels in $B, SA, from FRED; H.8 lags ~9 days, H.4.1 ~1 day.

| Observable | FRED id | 8/12 | 9/16 (latest) | Δ 5 wk | What a transmission would look like | Read 9/29 |
|---|---|---|---|---|---|---|
| Loans to non-depository financials, all banks | `LNFACBW027SBOG` | 2,024.8 | **2,047.0** | **+1.1%** | a STALL or contraction (banks pulling fund-finance/warehouse lines) | 🟢 still growing (+2.3% since 7/22) |
| … domestically chartered banks | `LNFDCBW027SBOG` | 1,503.5 | 1,522.9 | +1.3% | same | 🟢 |
| Small-bank deposits | `DPSSCBW027SBOG` | 5,652.8 | 5,655.5 | +0.05% | a multi-week decline while large-bank deposits rise (flight) | 🟢 flat; large banks 12,284 → 12,298 (+0.1%) |
| Small-bank large time deposits (the expensive money) | `LTDSCBW027SBOG` | 735.2 | 732.4 | −0.4% | a RISE = replacing lost cheap deposits with brokered/CD money | 🟢 falling |
| Small-bank borrowings (FHLB + other) | `H8B3094NSMA` | 284.3 | 288.7 | +1.5% | a step-up ≥ +5% in a month | 🟡 up, inside its Jul–Sep range (283–289) |
| Small-bank C&I loans | `CILSCBW027SBOG` | 736.3 | 739.3 | +0.4% | a DRAW spike (borrowers pulling lines) | 🟢 |
| Small-bank CRE loans | `CRESCBW027SBOG` | 2,097.4 | 2,102.1 | +0.2% | — (context) | 🟢 |
| Discount-window primary credit | `WLCFLPCL` | 5.64 | **6.24 [9/23]**; 6.88 [9/16] | +11% | > p90 of the last 60 weeks (**$7.9B**) for 2+ weeks | 🟢 ordinary (median 5.8; max 9.9) |
| KRE shares outstanding (`boot.py` float) | — | — | 56.11M [9/29] | +3.5% vs 9/14 | creations during a fall = short-via-ETF / inflows; redemptions = exit | 🟡 creations 9/14→9/26 (+2.3M), −0.46M since |
| Bank preferreds · BDCs (credit tell on the same names) | PFF/PGX · BIZD | — | — | L2: −1.4 / −2.6 · −0.8 | preferreds falling with common = capital/credit; falling alone = rates | 🟢 preferreds ≈ rates; BDCs +2.4% since 7/15 |

**Cadence:** pull at every boot (one `fetch.py` loop; add to `boot.py` as a deliberate task, not a closeout squeeze). **Bars above are descriptive, NOT registered triggers** — base-rate each before any registration (the same rule as the OREO and Chapter-11 candidates). What this set CANNOT see: idiosyncratic name-level credit (only a print or an 8-K shows that), and anything inside H.8's 9-day lag.

## 4. What this changes, and what it does not

- **ROADMAP "8/14+ de-rating: catalyst unidentified" → RESOLVED: small-cap/market beta, no bank component** (§1 L1). The 26-name sort TERRY's persistence leg was waiting on is unnecessary for this question.
- **The blind-spot thread gets its first non-credit instrument set** (§3), on-demand weekly; registration deferred to a base-rate pass.
- **The bear case is NOT strengthened by leg 2's shape:** the market is repricing big-bank equity, not regional credit. **It is not weakened either:** FLG/VLY are credit-shaped, B/CCC OAS is widening, and none of §3 can see a name-level problem before ~10/20. The honest state is *"price is ahead of any evidence I can produce, and the evidence I can produce says nothing has transmitted yet."*
- **For TERRY's KRE card (Will-asked 9/29):** the factor and size sorts say a KRE put is a bet on the financials-sector/large-bank leg continuing, with regionals carrying beta; it is NOT yet a bet on regional credit. That is a construction input, not a recommendation.

## 5. Caveats (carry them)

Betas are one-year OLS on ETF proxies (R² 0.63); a five-factor model attributes, it does not prove cause. n=14 cross-section: no |ρ| below ~0.5 is significant; the size sort (−0.72) is the only robust one. Cohort metrics are 6/30 Call Report vintage; AOCI exposure is the reported ratio, not a duration-adjusted dollar sensitivity (which would sort MORE on size). H.8 is seasonally adjusted and revised; latest week 9/16 predates the 9/23–9/28 credit widening by a week. Consensus figures and the Root-B narrative are secondary/NEXUS-owned.
