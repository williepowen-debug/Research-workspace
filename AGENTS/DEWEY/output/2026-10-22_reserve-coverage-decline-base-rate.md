# Rising bad loans with falling reserve coverage: does it predict bank losses?

**Date:** 2026-10-22 | **Mode:** Thesis | **Confidence:** (a) hit rate: Medium on the data, Low on generalising it (n ≈ 10 episodes from about 3 real loss cycles) · (b) size of the rise: Medium · (c) cross-section: Medium-High for 2007–10, Low for 2015–16 · today's placement: Medium (Q2-2026 call reports only; Q3 not yet filed; CECL break) · collateral record: Medium (based on failed banks) | **Request:** REQ-DEWEY-20261022-003 (WALTER) | **Recipients:** REGINALD (action); GIBBS, CREED, WAL, OZK, FLG, RED, PROME (info)

## Key Finding

From 1984 to 2026, in the $10–100B bank band, the combined pattern (problem-loan ratio up while allowance ÷ noncurrent loans falls, year over year) was followed by a material charge-off rise (≥25bp annualised) within 4 quarters in **2 of 10 episodes. Across all quarters, the rate was 41/166 (25%)**. So the pattern shows no lift at the 2–4 quarter horizon asked about. It shows modest lift only at 8 quarters: 5/10 vs 36% for charge-offs, and 7/10 vs 49% for provisions. Every one of those charge-off hits came from a pre-CECL episode, and the result rests on about 3 loss cycles. At the bank level in 2007–10 (n = 373), the banks whose coverage fell most did **not** take the largest later losses (ρ = −0.064, p ≈ 0.21). The largest-decline quintile had the *lowest* failure rate, 5.6%. The rise in problem loans carried the signal instead (ρ ≈ +0.46). Today the aggregate trigger has been on for **10 straight quarters (2024Q1–2026Q2) while charge-offs stayed flat (0.35% → 0.36%)**. That episode is unresolved. CECL, the 2020-era reserve standard, lifts every post-2020 coverage level, so comparisons with pre-2020 history overstate today's cushion.

## Intake check

| Kill condition | Test | Result |
|---|---|---|
| 1. Prior work already answers it | Is there a historical coverage-decline study covering ≥2 downturns in REGINALD or GIBBS? | **None found.** Mentions of coverage in those desks cover the current quarter or a single bank. **Run proceeds.** |
| 2. History not retrievable | Can FDIC/FFIEC bank-level call-report data be pulled for multiple cycles? | **Retrievable.** The FDIC BankFind API returns bank-level call-report data from 1984Q1 to 2026Q2. 2026Q3 returned 0 rows on 2026-10-22, so Q3 call reports are not yet loaded (expected ~10/30). **Run proceeds.** |

Scope: DEWEY reports evidence only. This report does not grade REGINALD's reading, rank banks, propose or register a threshold, or make a stock call. Will holds a bank view, and this is not a trade input.

## Evidence

### How the numbers were built

All aggregate and cross-section figures are DEWEY's own computation from FDIC BankFind call-report data, pulled 2026-10-22 [PRIMARY: FDIC BankFind API]. The ratios are defined as follows:

- **Coverage** = allowance (LNATRES) ÷ noncurrent loans (NCLNLS). Noncurrent = nonaccrual + 90+ days past due. The identity NCLNLS = NALNLS + P9LNLS holds in 100% of the bank-quarters checked.
- **NPL ratio** = NCLNLS ÷ gross loans.
- **Charge-offs and provisions** use FDIC's quarterly fields (NTLNLSQ, ELNATQ), annualised. The YTD fields de-cumulate to match them in 98.5% of 197,009 bank-quarters.
- Aggregates are ratios of sums. Insured branches of foreign banks (BKCLASS OI/NC) are excluded because they report noncurrent loans but no allowance. Including them lowers 2026Q2 band coverage from **116.0% to 112.75%** (ΣLNATRES 33,818,317 ÷ ΣNCLNLS 29,994,535, $K, DEWEY pull).

The bank groups are:

- **G1:** nominal $10–100B.
- **G1x:** G1 excluding 4 card specialists.
- **G1r:** the same band in 2026 dollars (GDP deflator).
- **G2:** $1–10B community banks.

**Pre-registered trigger and outcome definitions** were timestamped Thu Oct 22 12:51:32 EDT 2026, before any outcome series was viewed. Verbatim:

- `T-QoQ : NPL_t > NPL_t-1 AND COV_t < COV_t-1`
- `T-YoY : NPL_t > NPL_t-4 AND COV_t < COV_t-4`
- An episode is a maximal run of consecutive trigger quarters, starting at t0.
- **Material rise:** the annualised single-quarter NCO rate is at least +0.25pp above t0 at any quarter from t0+1 to t0+4. "By t+8" is also reported, with the same thresholds for provisions.
- **False alarm:** no hit by t+4.
- **Miss:** an NCO-rise episode with no trigger in the window [s0−8, s0].

Two smaller notes. The 1984–86 data are lower quality: NCO fields are partly null and the 1985Q2/Q3 values are duplicated. Some pre-1989 savings-bank NCO fields are also null.

### Table 1: Episodes and named-cycle verdicts

**1a. G1 ($10–100B nominal), year-over-year trigger.** Changes are in percentage points of annualised rate versus the trigger quarter t0 [PRIMARY: FDIC BankFind API, DEWEY computation].

| Trigger start (t0) | End | Qtrs | NPL% t0 | Cov% t0 | NCO% t0 | ΔNCO t+1 | t+2 | t+4 | t+8 | ΔProv t+4 | ΔProv t+8 | NCO hit by t+4 | by t+8 | Era |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1987Q1 | 1987Q1 | 1 | 5.04 | 35.75 | 0.85 | −0.06 | −0.08 | +0.24 | −0.03 | +0.24 | −0.32 | YES | YES | pre-CECL |
| 1990Q4 | 1991Q4 | 5 | 4.09 | 72.31 | 1.77 | −0.61 | −0.06 | +0.06 | −0.45 | −0.10 | −1.00 | no | no | pre-CECL |
| 1999Q1 | 1999Q1 | 1 | 0.91 | 172.37 | 0.65 | −0.08 | −0.01 | −0.01 | +0.27 | +0.10 | +0.44 | no | YES | pre-CECL |
| 1999Q3 | 1999Q4 | 2 | 0.90 | 177.17 | 0.64 | +0.03 | −0.01 | +0.08 | +0.31 | +0.16 | +0.42 | no | YES | pre-CECL |
| 2000Q2 | 2002Q3 | 10 | 0.93 | 167.87 | 0.64 | +0.08 | +0.21 | +0.31 | +0.52 | +0.19 | +0.32 | YES | YES | pre-CECL |
| 2006Q2 | 2010Q2 | 17 | 0.72 | 178.31 | 0.56 | +0.11 | +0.15 | +0.05 | **+1.01** | +0.17 | **+2.21** | no | YES | pre-CECL |
| 2016Q3 | 2016Q4 | 2 | 1.32 | 105.43 | 0.60 | +0.10 | +0.07 | +0.03 | −0.12 | +0.15 | −0.19 | no | no | pre-CECL |
| 2019Q4 | 2019Q4 | 1 | 1.01 | 110.75 | 0.53 | +0.06 | +0.07 | −0.14 | −0.33 | −0.31 | −0.44 | no | no | pre-CECL |
| 2021Q1 | 2021Q2 | 2 | 1.33 | 135.90 | 0.29 | −0.01 | −0.09 | −0.06 | +0.13 | +0.38 | +0.74 | no | no | post-2020 |
| **2024Q1** | **2026Q2 (live)** | **10** | 0.84 | 165.29 | 0.35 | 0.00 | −0.00 | +0.02 | +0.01 | +0.08 | −0.02 | no | no | post-2020 |

Medians across the 10 episodes (DEWEY computation from Table 1a):

| Horizon | Median ΔNCO | ΔNCO range | Median ΔProvision |
|---|---|---|---|
| t+4 | **+0.04pp** | −0.14 to +0.31 | **+0.16pp** |
| t+8 | **+0.07pp** | −0.45 to +1.01 | +0.15pp |

The quarter-over-quarter trigger produced 24 G1 episodes. The full matrix for both triggers is in Table 2.

**1b. Named cycles: did the trigger lead the loss cycle?** These are G1/G1x, year-over-year trigger unless noted. NCO4 is the trailing-4-quarter charge-off rate [PRIMARY: FDIC BankFind API, DEWEY computation].

| Cycle | Aggregate NCO path | Verdict | Detail |
|---|---|---|---|
| 1989–91 New England / CRE | G1 NCO4 0.84% → **1.96%** (peak 1990Q2) | **MISSED** in the nominal band | No year-over-year trigger in the prior 8 quarters. It fired only in 1990Q4–1991Q4, *after* the peak. Aggregate coverage was *rising* into the peak (67.8% → 79.3%) as reserves were built. **Caught** in G1r (1987Q1, 1988Q3, 1991Q1) and G2 (1986Q3, 1989Q2–Q4, 1991Q1). |
| 2001–02 | G1 NCO rose from 2001Q1 | **Caught** | 8-quarter lead (2000Q2 trigger) |
| 2007–10 GFC | G1 NCO4 0.63% → **3.19%** (peak 2010Q1); G1x 0.26% → 2.30% | **Caught early** | Fired 2006Q2, **six quarters before NCOs began rising in 2007Q4**. Counts as a hit by t+8, *not* by t+4. |
| 2015–16 energy | G1 0.61% → 0.70%; G1x 0.19% → 0.21% | **False alarm** | Triggers in 2015Q1 (QoQ) and 2016Q3 (YoY). In G2 there was no trigger and no rise, a correct negative. |
| 2020 COVID | G1 NCO4 0.53% → 0.57% | **Provisions rose, NCOs did not** | 2019Q4 trigger. In G1x, provisions rose +1.19pp at t+1. |
| **2023–26 office CRE** | G1 NCO4 0.23% → 0.38% (2025Q3); G1x 0.07% → 0.25% | **UNRESOLVED** | Trigger on for 10 straight quarters (2024Q1–2026Q2). Band coverage **165.3% → 116.0%**, NPL **0.84% → 1.16%**, NCO **0.35% → 0.36%**. G2 is also live: coverage 194.3% → 150.8%. |

**The miss test is weak.** A random 9-quarter window contains at least one trigger quarter **65% (YoY) / 85% (QoQ)** of the time in G1. "Caught" is therefore a low bar.

### Table 2: Hit rate vs the unconditional rate, by group and era

The comparison row is "unconditional": all quarters, whether or not the trigger fired. Format is hits/resolved episodes [PRIMARY: FDIC BankFind API, DEWEY computation].

| Group | Trigger | Era | Episodes | NCO ≥25bp by t+4: trigger vs uncond. | NCO ≥25bp by t+8: trigger vs uncond. | Prov ≥25bp by t+4: trigger vs uncond. | Prov ≥25bp by t+8: trigger (uncond. all-era) |
|---|---|---|---|---|---|---|---|
| **G1** | YoY | All | 10 | **2/10 (20%) vs 41/166 (25%)** | **5/10 (50%) vs 58/162 (36%)** | 3/10 (30%) vs 54/166 (33%) | **7/10 (70%)** (80/162, 49%) |
| G1 | YoY | pre-CECL | 8 | 2/8 (25%) vs 41/144 (28%) | 5/8 (62%) vs 58/144 (40%) | 2/8 (25%) vs 48/144 (33%) | 6/8 (75%) |
| G1 | YoY | post-2020 | 2 | 0/2 vs **0/22** | 0/2 vs 0/18 | 1/2 vs 6/22 (27%) | 1/2 |
| G1 | QoQ | All | 24 | 8/23 (35%) vs 41/166 (25%) | 13/22 (59%) vs 58/162 (36%) | 10/23 (43%) vs 54/166 (33%) | 13/22 (59%) |
| G1 | QoQ | pre-CECL | 20 | 8/20 (40%) vs 41/144 (28%) | 13/20 (65%) vs 58/144 (40%) | 10/20 (50%) vs 48/144 (33%) | 13/20 (65%) |
| G1 | QoQ | post-2020 | 4 | 0/3 vs 0/22 | 0/2 vs 0/18 | 0/3 vs 6/22 | 0/2 |
| G1x (ex-card) | YoY | All | 10 | 1/10 (10%) vs 34/166 (20%) | 3/10 (30%) vs 49/162 (30%) | 3/10 (30%) vs 47/166 (28%) | 7/10 (70%) (69/162, 43%) |
| G1x | YoY | pre-CECL | 8 | 1/8 (12%) vs 34/144 (24%) | 3/8 (38%) vs 49/144 (34%) | 2/8 (25%) vs 42/144 (29%) | 6/8 (75%) |
| G1x | YoY | post-2020 | 2 | 0/2 vs 0/22 | 0/2 vs 0/18 | 1/2 vs 5/22 (23%) | 1/2 |
| G1r (2026 $) | YoY | All | 11 | 4/11 (36%) vs 33/166 (20%) | **7/11 (64%) vs 51/162 (31%)** | 6/11 (55%) vs 48/166 (29%) | 8/11 (73%) (69/162, 43%) |
| G1r | YoY | pre-CECL | 9 | 4/9 (44%) vs 33/144 (23%) | 7/9 (78%) vs 51/144 (35%) | 5/9 (56%) vs 44/144 (31%) | 7/9 (78%) |
| G1r | YoY | post-2020 | 2 | 0/2 vs 0/22 | 0/2 vs 0/18 | 1/2 vs 4/22 (18%) | 1/2 |
| G2 ($1–10B) | YoY | All | 12 | 4/12 (33%) vs 37/166 (22%) | 6/12 (50%) vs 55/162 (34%) | 4/12 (33%) vs 47/166 (28%) | 5/12 (42%) (75/162, 46%) |
| G2 | YoY | pre-CECL | 9 | 4/9 (44%) vs 37/144 (26%) | 6/9 (67%) vs 55/144 (38%) | 4/9 (44%) vs 44/144 (31%) | 5/9 (56%) |
| G2 | YoY | post-2020 | 3 | 0/3 vs 0/22 | 0/3 vs 0/18 | 0/3 vs 3/22 (14%) | 0/3 |

**Robustness checks.**

- **Smoothed charge-offs.** When the outcome is the trailing-4-quarter NCO rate up ≥25bp at t+4, almost nothing passes: G1 YoY 0/10, G1 QoQ 1/23 (the 2008Q4 start), G1x YoY 0/10, G1r YoY 0/11, G2 YoY 1/12. Many single-quarter "hits" are Q4 charge-off seasonality or one-quarter spikes.
- **Merged episodes.** Merging runs separated by one quarter gives similar or weaker rates. For example, G1 YoY is 1/8 by t+4 and 3/8 by t+8.

**Small n, stated plainly.** Every rate in this table rests on **8–12 overlapping episodes from about 3 real loss cycles** (1986–91, 2000–02, 2007–10). **One episode moves a rate by 8–10 points.** The episodes are serially dependent, so no significance test is reported. **Post-2020 shows 0 NCO hits in every group, but the unconditional rate is also 0/22.** With nothing to predict, the trigger is *untestable* after 2020. The zero is not reassuring.

### Table 3: Cross-section. Did the banks whose coverage fell most lose the most?

**3a. 2007–10.** Banks ≥$1B with loans ≥10% of assets and NPL ≥0.25% at the start. The formation window runs 2006-12-31 → 2008-06-30. The outcome is cumulative 8-quarter NCO ÷ prior-quarter loans, 2008Q3–2010Q2. **Failed banks are kept** (38 failed by 6/2010; 48 by 2012). n = 373 [PRIMARY: FDIC financials and failures APIs, DEWEY computation, pre-registered].

| Quintile (Q5 = largest coverage decline) | n | ΔCov median (pp) | ΔNPL median (pp) | NPL₀ median % | Cov₀ median % | Cov₁ median % | NCO median % | NCO p75 % | Fail % to 6/2010 | Fail % to 2012 |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (coverage rose) | 74 | +29.0 | −0.05 | 0.92 | 132.6 | 191.8 | 2.31 | 5.48 | 6.8 | 8.1 |
| Q2 | 74 | −15.4 | +1.04 | 1.39 | 61.7 | 44.8 | 3.27 | 6.11 | **17.6** | 20.3 |
| Q3 | 75 | −52.9 | +0.72 | 0.76 | 129.7 | 77.1 | 2.87 | 5.21 | 12.0 | 13.3 |
| Q4 | 78 | −102.1 | +0.62 | 0.53 | 200.0 | 93.3 | 2.60 | 4.97 | 9.0 | 11.5 |
| **Q5 (largest decline)** | 72 | −194.4 | +1.20 | **0.40** | **307.0** | 81.6 | 3.18 | 6.10 | **5.6** | 11.1 |

| Test (n = 373) | Result |
|---|---|
| Spearman ΔCov ~ cumulative NCO (pre-registered primary) | **ρ = −0.064, p ≈ 0.21** |
| Same, alternative outcome denominator | ρ = −0.051, p = 0.32 |
| Spearman Δlog-coverage ~ NCO (secondary) | ρ = −0.179, p = 0.0005 |
| Spearman ΔNPL ~ NCO | **ρ = +0.464, p < 0.0001** |
| Spearman Δ(allowance/loans) ~ NCO | ρ = +0.549, p < 0.0001 (faster reserve *builders* lost more) |
| Subset "coverage fell AND NPL rose" (n = 324) | ρ(ΔCov, NCO) = +0.037, p = 0.51 (flat to inverted) |
| OLS NCO: ΔNPL + NPL₀ + CRE share → add ΔCov | **R² 0.088 → 0.094**; ΔCov t = **−1.35** (adjusted R² 0.081 → 0.084) |
| OLS NCO: + Δlog-coverage instead | R² 0.096; t = −1.63 |
| Failure model (linear probability): add ΔCov to ΔNPL model | R² 0.344 → 0.363; ΔCov t = **+3.31**: a *bigger* decline goes with *lower* failure risk |
| Mechanical confound | Spearman(ΔCov, Cov₀) = −0.60; Spearman(ΔCov, ΔNPL) = −0.43 |
| Sensitivities: NPL screen 0.5%; no screen; alt window 2007Q4–2008Q2 | ρ = −0.063 / +0.013 / +0.011, all not significant |
| Post-hoc: real-estate lenders only (RE share ≥25%, n = 350) | ρ = −0.151 (p = 0.004), but ΔCov t = −1.43 once ΔNPL is in the model |

**Coverage level, not change (post-hoc).** The 2008-06-30 coverage level sorts failures better than the change does. The lowest end-coverage quintile (1.1–44.8%) had **26/75 = 34.7%** failures, against 0–6.8% elsewhere. Even so, once the end-of-window NPL level is controlled, coverage level adds little: failure-model R² rises 0.321 → 0.324; NCO-model R² rises 0.066 → 0.086, with a card-driven wrong sign.

**3b. 2015–16 energy.** Formation window 2015-06-30 → 2016-03-31; outcome 7 quarters, 2016Q2–2017Q4; n = 542; 2 failures [PRIMARY: FDIC APIs, DEWEY computation].

| Test | Result |
|---|---|
| Spearman ΔCov ~ NCO, raw | ρ = −0.257, p < 0.001 |
| OLS: add ΔCov to ΔNPL model | R² 0.153 → 0.154; ΔCov t = **−1.09** |
| Subset with rising NPL (n = 201) | ρ = +0.017, p = 0.81 |
| TX/OK/LA only (n = 62) | ρ = −0.332 (suggestive only at this n) |
| Size of losses | Median cumulative NCO 0.08–0.27% by quintile |

The raw energy correlation is the NPL change in disguise. Losses were too small to test much.

**Answer to (c): no.** In neither episode did the banks whose coverage fell most take the largest later losses once the NPL rise is accounted for. The rise in problem loans itself is what predicted losses.

### Table 4: Today's banks against the historical range

**4a. Six banks named in REGINALD's flag.** Company-reported figures and call-report figures sit in **separate columns** and are not like-for-like. They differ in period (Q3 vs Q2) and probably in definition. Percentile = share of ≥$1B banks with lower call-report coverage at that date. Banks are listed in REGINALD's order, not ranked.

| Bank (FDIC CERT) | Company-reported coverage, 2Q26 → 3Q26 (company basis; not recomputed by DEWEY) | Call-report coverage 2026-06-30 (LNATRES ÷ NCLNLS) | Call-report NPL 2026Q2 | Pctl vs 2006Q4 | Pctl vs 2008Q2 | Pctl vs 2026Q2 | Call-report coverage path 2024Q2 → 2026Q2 | Definition note |
|---|---|---|---|---|---|---|---|---|
| SSB (33555) | not in DEWEY's inputs | 213.8% | 0.54% | 46.7 | 78.2 | 52.9 | 241.2 → 213.8 | 24.3% of noncurrent government-guaranteed; ex-wholly-guaranteed 263.3% |
| VLY (9396) | ~131% → 117% [as relayed in WALTER signal] | **123.3%** ($590,072K ÷ $478,695K) | 0.91% | 25.8 | 59.2 | 30.4 | 163.4 → 123.3 | 0% guaranteed; nonaccrual-only 127.5% |
| HBAN (6560) | not in DEWEY's inputs | 160.3% | 1.06% | 35.0 | 70.5 | 40.4 | 254.3 → 160.3 | 40.3% guaranteed; ex-wholly-guaranteed 197.6%; nonaccrual-only 204.4% |
| EGBN (34742) | 109% → 73% [as relayed in WALTER signal] | **88.5%** ($121,141K ÷ $136,915K) | 2.05% | 15.9 | 44.6 | 18.1 | 108.1 → 88.5 (low 54.8 at 2024Q4) | ~0% guaranteed; all nonaccrual; 88.5% on every definition |
| BKU (58979) | 97.14% → 83.96% [PRIMARY: BKU 8-K, bank's own ratio] | **53.9%** | 1.69% | 7.7 | 24.1 | 7.8 | 56.7 → 53.9 (low 39.1 at 2025Q2) | **51.8% of noncurrent loans government-guaranteed; nonaccrual-only coverage 95.5%**, largely a definition effect |
| ZION (2270) | total not in DEWEY's inputs; CRE allowance "4.4x CRE nonaccruals" (CRE only) | 224.1% | 0.47% | 49.1 | 79.9 | 54.9 | 260.0 → 224.1 | 5.2% guaranteed; ex-wholly-guaranteed 234.0% |
| *Ref: EGBN at company 3Q 73%* | — | — | — | 11.9 | 36.3 | 12.7 | — | not like-for-like with call-report distributions |
| *Ref: VLY at company 3Q 117%* | — | — | — | 24.1 | 57.6 | 29.0 | — | not like-for-like |

Sources: [PRIMARY: FDIC BankFind API, CERT filter, REPDTE 2024-06-30..2026-06-30, DEWEY pull 2026-10-22]; BKU from the bank's 8-K EX-99.1 (Oct 21, 2026).

The comparison cross-sections, for banks ≥$1B with loans ≥10% of assets:

| Date | n | Median coverage | p25–p75 coverage | Median NPL |
|---|---|---|---|---|
| 2006Q4 | 623 | 227.9% | 120.0–463.9% | 0.48% |
| 2008Q2 | 661 | 96.6% | 56.1–190.5% | 1.23% |
| 2026Q2 | 1,023 | 196.4% | 104.8–396.2% | 0.57% |

**The company figures do not match call-report coverage.** EGBN's company Q2 figure (109%) compares with a call-report 88.5%. VLY's (~131%) compares with 123.3%. The likely causes are a different NPL base, inclusion of the unfunded-commitment reserve, or holding-company scope [inference, unverified].

**Choosing the cleaner percentile.** CECL lifts post-2020 coverage, so the 2008Q2 percentiles overstate today's relative cushion. The cleaner reads are the **2026Q2 today-vs-today** and the 2006Q4 columns.

**NPL percentiles carry more information.** Table 3 shows the NPL level carries more information than coverage. Against 2008Q2 peers, NPL percentiles are:

| Bank | NPL pctl vs 2008Q2 |
|---|---|
| ZION | 17.9 |
| SSB | 20.9 |
| VLY | 38.0 |
| HBAN | 44.3 |
| BKU | 63.8 |
| EGBN | 70.3 |

**4b. Aggregate band at 2026-06-30** [PRIMARY: FDIC BankFind API, DEWEY computation; FDIC QBP 2Q 2026].

| Series | Coverage | Pctl 1990–2026 | Pctl pre-CECL 1990–2019 | Pctl post-2020 | NPL | NCO ann. | Prov ann. |
|---|---|---|---|---|---|---|---|
| G1 $10–100B (n = 126, $3.70T) | **116.0%** | 40 | 48 | **4** | 1.16% | 0.36% | 0.33% |
| G1 incl. foreign-bank branches | 112.75% | — | — | — | — | — | — |
| G1x ex-card (n = 122) | **100.3%** | 45 | 54 | 4 | 1.15% | 0.24% | 0.20% |
| G1r 2026-$ band | 116.0% | 48 | 55 | 15 | — | — | — |
| G2 $1–10B (n = 890) | 150.8% | 53 | 62 | 8 | 0.87% | 0.30% | 0.39% |
| Industry, all insured (QBP) | 172.7% | — | — | — | — | — | — |
| Community banks (QBP) | 145.6% | — | — | — | — | — | — |

Only 2026Q1 (115.8%) is lower than today's 116.0% since CECL adoption.

**4c. The pre-loss distribution.** These are the 4 quarters before each classic loss peak (1990, GFC, energy; 12 quarters). All are pre-CECL.

| Group | p25 | Median | p75 | Max |
|---|---|---|---|---|
| G1x (ex-card; most like-for-like with single banks) | 54.2% | **74.8%** | 81.9% | **92.3%** |
| G1 | 76.1% | 89.6% | 108.0% | 122.1% |
| G2 | 50.8% | 59.9% | 76.1% | 85.0% |

On that pre-CECL scale:

- EGBN's company 73% sits near the G1x pre-loss median.
- EGBN's call-report 88.5% sits inside the pre-loss range.
- VLY at ~117% (company) or 123.3% (call report) sits above every pre-loss quarter.
- BKU's call-report 53.9% sits near the pre-loss p25. Its nonaccrual-only 95.5% sits above the pre-loss maximum.

**Two caveats travel with this table.** CECL raises all post-2020 levels, so placing today's numbers on a pre-2020 scale **overstates the cushion**. An asset-weighted aggregate is also not like-for-like with a single bank, whose ratio swings with one large nonaccrual.

**Cross-regime and post-hoc, illustrative only.** In the 2008Q2 end-coverage quintiles:

- EGBN at 88.5% would fall in Q3 (NCO median 2.95%, failure 5.3%).
- EGBN at 73% and BKU at 53.9% would fall in Q2 (3.71%, 6.8%).
- None of the six is near the <45% bucket, where 34.7% of banks failed.

### Table 5: The collateral defense

**5a. Loss severity by episode.** Each row has its own basis, so do not pool rows.

| Episode | Loan type | Figure | Basis | Source |
|---|---|---|---|---|
| 1986–92 FDIC receiverships (mid-1992) | Nonperforming CRE | Collateral value **−54%** on average vs original. ≥63% decline for half the CT loans; ≥58% for half the TX/LA loans | Collateral-value decline, **not loss-given-default**; 224 loans | [PRIMARY: FDIC, *History of the Eighties*, Ch. 3] |
| 1987–93 market | Prime office (Russell-NCREIF) | −26% | Appraisal-based index | same |
| 2008–13 failed banks | **Construction & development (C&D)** | **53.3%** weighted (mean 57.4%, median 63.3%) | Loss ÷ balance at default, incl. interest and expenses; >50,000 loans | [PRIMARY/ACADEMIC: FDIC WP 2015-06] |
| same | Other CRE | **38.5%** weighted | same | same |
| same | C&D by workout time | **12.3%** (<6 months) → 47.3% (12–18m) → 63.5% (2–3 yrs) → **72.2%** (>3 yrs); 44% took >2 yrs | same | same, Table 4 |
| same | Closed with no loss or cured | C&D **17%**, other CRE **28%** | same | same |
| 2008–13 failed banks | CRE (all) | Mean **44%** vs a local price decline of ~20% (origination → disposition); 10% had loss >100% | 14,425 loans at 295 failed banks | [ACADEMIC: FDIC WP 2015-03; *JREFE* 2021] |
| 2022 CMBS liquidations | Office | 73.9% | Moody's severity; 156 loans | [INSTITUTIONAL via NEWS: MBA NewsLink citing Moody's] |
| 1995–Q1 2025 conduit CMBS | Office | 33.5% all resolved; 51.4% for loans with >2% loss | KBRA severity | [INSTITUTIONAL: KBRA, Jul 31, 2025] |
| 1993–Sep 2025 single-borrower CMBS | All types | 11.2% average; 21 of 29 resolutions <1% loss | KBRA | [INSTITUTIONAL: KBRA via CREFC] |

**Caveat that must travel:** the bank figures come from **failed** banks. They include fire-sale and receivership effects and likely overstate losses at going-concern banks [DEWEY inference]. The FDIC authors give the same warning about their sample.

**5b. Appraisal lag and the "well-secured" record.**

| Item | Evidence | Source |
|---|---|---|
| Transaction prices lag | Prices "still may not fully reflect the deterioration in CRE market prices because… many owners wait for more favorable conditions" | [PRIMARY: Fed FSR, Nov 22, 2024] |
| Appraisal updates are a judgment call | Updates are triggered by "material deterioration"; "A new appraisal may not be necessary when an evaluation… appropriately updates the original appraisal assumptions"; no charge-off required on a performing loan "solely because the value of the underlying collateral has declined" | [PRIMARY: 2023 interagency CRE workout statement, SR 23-5] |
| Stale appraisals accepted, 2008–11 | Examiners "in six of the seven instances appeared to accept the dated appraised values" | [PRIMARY: FDIC OIG EVAL-13-002, Jan 2013] |
| Failed banks under-reserved | **15 of 19 (78.9%)** sampled failed banks "did not have sufficient ALLL"; 26.5% of 136 open-bank exam reports said the same | same |
| Extend-and-pretend, post-2022 | Weakly capitalised banks extended maturities on distressed CRE "to preserve capital", raising "the risk of large losses materializing over a short period" | [ACADEMIC: NY Fed Staff Report 1130, rev. June 2026] |
| Extension option narrowing | "this option may be increasingly limited going forward" | [PRIMARY: Fed FSR, May 8, 2026] |
| Delayed loss recognition | Delayed recognition creates "expected loss overhangs that threaten future capital adequacy" | [ACADEMIC: Bushman & Williams, *JAR* 2015] |

No source gives a loan-level accuracy rate for "well-secured, no specific reserve" calls. The closest proxy is the 17–28% no-loss share in failed-bank data.

**5c. Q3-2026 bank statements** (verbatim from SEC 8-K exhibits) [PRIMARY].

| Bank (8-K date) | Statement |
|---|---|
| VLY (Oct 22, 2026) | "The $30.1 million construction loan is considered well-secured and did not require a specific reserve within our allowance for credit losses… based upon the estimated value of the underlying collateral." Deck: LTVs "based on most recent appraisal, seasoned on average 2.5 years." Non-accrual CRE fell "primarily reflecting repayments and partial charge-offs." |
| EGBN (Oct 21, 2026) | NPAs "increased by $52.9 million to $166.0 million… 76.0% of which resulted from a single loan migration" (a $56.0M multifamily loan). Slides: "LTVs are based on most recently appraised value, which do not necessarily reflect current market conditions." Two pass-rated construction loans ($94.0M, $88.5M) carry appraisals dated 11/14/2022 and 5/09/2023. |
| ZION (Oct 19, 2026) | "Approximately 42% of CRE classified balances have 2026 appraisals, 30% in 2025, 2% 2024, 8% 2023 and earlier." These sum to 82%; 18% is unstated. |
| BKU (Oct 21, 2026) | ACL ÷ NPLs 83.96% vs 97.14% (company basis). No collateral statement on the NPL increase. The office weighted LTV of 64.9% is a text-order reading and needs a slide check. |
| HBAN (Oct 22, 2026) / SSB (Oct 21, 2026) | No collateral, LTV or appraisal language in the releases. |

### Table 6: The CECL break and what the coverage ratio actually measures

**6a. Two coverage regimes** (all insured institutions) [PRIMARY: FDIC QBP; Fed FEDS Note 2021].

| Date | Coverage | Regime / note |
|---|---|---|
| 4Q 2004 | 167.8% | Incurred-loss model |
| 4Q 2006 | 136.8% | Down from $1.48 to $1.37 per $ noncurrent |
| 4Q 2007 | 92.5% | Coverage below 100% for the first time since 1993; **preceded 2008–10 losses** |
| 4Q 2009 | **58.1%** | Incurred-loss low |
| 4Q 2012 | **58.5%** | Reserves fell for the 11th straight quarter as losses receded |
| 4Q 2019 | 129.7% | Last incurred-loss-only quarter |
| 1Q 2020 | **192.2%** | CECL day-1 effect plus COVID builds; noncurrent loans *rose* 7.3% |
| 1Q 2023 | **219.5%** | CECL peak; universal adoption ($3.0B day-one adjustment for about 4,000 banks) |
| 1Q 2026 | 166.8% | CECL-era low |
| 2Q 2026 | **172.7%** | Latest; community banks 145.6% |

**Other figures on the break.**

- **Size groups across adoption (4Q19 → 1Q20):** $10–250B rose from 127.1% to 208.4%. $1–10B, mostly later adopters, moved from 151.8% to 147.3%.
- **The 2020 adopters:** their allowances rose **+37%** at adoption.
- **Mid-size day-1 effect:** 0.38% of loans for 2020 adopters and 0.10% for 2023 adopters.
- **No CECL-consistent restatement** of pre-2020 coverage has been published. DEWEY's rough inference from the Fed figures is that CECL coverage runs about 1.3–1.4× the old-standard equivalent for the same credit state. That multiplier is unpublished.

**6b. Why the ratio is mechanically ambiguous.** Under both regimes, the confirmed shortfall on a collateral-dependent loan is **charged off**, not just reserved. The 2006 policy says it "should be promptly charged off against the ALLL", and the 2023 statement classifies the excess over collateral value less costs to sell as "loss". The remaining nonperforming balance then sits at collateral value with little specific reserve, so coverage falls. A falling ratio can therefore mean two opposite things:

| Reading | Mechanism | Historical instance |
|---|---|---|
| Benign: losses already recognised | Charge-downs shrink the allowance; guaranteed or written-down loans dominate NPLs; reserves released in recovery; one-off sales | Coverage sat at ~57–64% from 2009 to 2012 while reserves were released 11 straight quarters to 4Q12. 4Q 2025 dip attributed by the FDIC to a pending portfolio sale. BKU's guaranteed share today |
| Adverse: new NPLs labelled well-secured on stale values | Denominator grows faster than the allowance; no specific reserve on "well-secured" loans | Coverage fell **$1.48 → $0.93** per $ of noncurrent loans over 2006–07, just before the 2008–10 losses |

The two readings can only be separated with charge-off history and appraisal dates, loan by loan. The cross-section also shows **reserve builders lost more** (ρ = +0.549 for change in allowance/loans). A bank that builds reserves fast on visible losses shows *higher* coverage, which is the opposite of the "low coverage = under-reserved" logic.

## Counter-Evidence

**Against "the pattern does not predict losses":**

- **Pre-CECL, at 8 quarters, there is lift.** In the 2026-dollar band it is 7/9 (78%) vs 35%. In G1 it is 5/8 (62%) vs 40%, and provisions are 6/8 (75%).
- **The trigger caught the costliest cycle (GFC) with a 6-quarter lead.** A 2–4 quarter test window scores that as a miss, so the question's horizon may be the wrong one, not the signal.
- **Charge-off data understate losses in the cycles that matter.** Aggregate NCO excludes losses the FDIC absorbed at failed banks (1989–92, 2009–11). In the cross-section, failed banks' NCOs are a lower bound; four failures, including WaMu and IndyMac, report zero outcome quarters. Survivorship does not appear to hide a positive result: failures cluster in Q2–Q3, not Q5.
- **Some post-hoc cuts show a weak effect.**
  - Real-estate-lender subsample: ρ = −0.151, p = 0.004.
  - Log coverage change: ρ = −0.179, p = 0.0005.
  - TX/OK/LA in 2015–16: ρ = −0.33, n = 62.
  - None survives control for the NPL change at 5%.
- **Low coverage level, separate from the change, coincided with failure.** 34.7% of banks below 45% at 2008Q2 failed.
- **Supervisory and academic records on reserves are poor in downturns.** 15/19 sampled failed banks were under-reserved. Examiners accepted stale appraisals. Delayed recognition raises downside risk. Post-2022 extend-and-pretend at weak banks may be *suppressing* today's charge-offs. That would make the 2024–26 flat-NCO run a delay, not a false alarm, and the Fed says the extension option "may be increasingly limited."

**Against reading today's decline as a warning:**

- **Coverage falls for benign reasons**: charge-downs, guaranteed loans, releases, one-off sales. BKU's low call-report figure is mostly guaranteed loans.
- **The industry is still building reserves.** Provisions exceeded NCOs in 1Q 2026, and industry coverage rose to 172.7% in 2Q 2026.
- **Regulators call credit risk "manageable in aggregate"** (OCC Spring 2026). The Fed frames the issue as methodology and level review at CRE-concentrated banks.
- **CECL levels remain above every incurred-loss year-end from 2007 to 2019.**

**Counter-evidence DEWEY could not find:** no peer-reviewed study tests allowance ÷ NPL *on its own* as a predictor of charge-offs or failure. The literature is indirect: Ng & Roychowdhury (2014) find that loan-loss reserves added back to capital were *positively* associated with 2008–10 failure risk.

## Unknowns

| Unknown | Why it matters | When / how it resolves |
|---|---|---|
| Q3-2026 call reports | All bank-level placement here uses Q2 | FDIC load expected ~10/30/2026 |
| Company vs call-report definitions (EGBN 109% vs 88.5% at Q2) | Determines which series REGINALD's figures belong to | 10-Q / Y-9C reconciliation |
| Appraisal dates and LTVs on VLY's $30.1M and EGBN's $56.0M new nonaccruals | The "well-secured" call depends on how current the value is | 10-Qs (early Nov 2026) or earnings-call Q&A (transcripts not accessible this run) |
| Whether the 2024–26 episode ends in a charge-off rise | It is the only post-CECL test case | Data in coming quarters; a post-CECL loss cycle is needed to calibrate anything |
| CECL-consistent restatement of pre-2020 coverage | Every cross-era percentile is biased upward | No published series |
| Office/CRE-segment charge-offs (fields NTREQ etc.) | Aggregates dilute concentrated cycles (1989–90, energy, office) | Not pulled this run |
| Loss-inclusive outcome (FDIC resolution cost merged with NCO) | Removes the failed-bank lower-bound bias | `COST` field already pulled, not merged |
| ZION's 18% of classified CRE with unstated appraisal vintage; BKU office LTV mapping | Completeness of today's collateral statements | Slide check / 10-Q |

## Source Quality Assessment

- **Spine: Strong.**
  - The aggregate and cross-section numbers are [PRIMARY] FDIC call-report data, computed by DEWEY to pre-registered definitions.
  - Field identities were verified in the data.
  - The aggregates track the Fed's "banks not among the 100 largest" series: G2 vs CORALOBN ρ = 0.975, G1x 0.932.
- **The main weakness is sample size, not sourcing.**
  - There are about 3 independent loss cycles.
  - Episodes overlap.
  - Group membership drifts every quarter: G1 n ranges from 26 to 128, and the band was dominated by money-center banks in 1988–92.
  - There is no significance test.
- **The CECL break** is documented by [PRIMARY] FDIC QBPs and [PRIMARY/ACADEMIC] Fed staff work.
- **The collateral evidence** is [PRIMARY/ACADEMIC], but the denominators are failed banks. CMBS figures are [INSTITUTIONAL], some via [NEWS].
- **Company Q3 figures:**
  - BKU's comes from its own 8-K.
  - **EGBN 109% → 73% and VLY ~131% → 117% are as relayed in the WALTER signal and were not recomputed by DEWEY.**
- **Excluded from this report:**
  - A news item on an FDIC appraisal case at an entity named "Valley Bank" (search snippet only; the entity is ambiguous and not confirmed to be VLY).
  - A First NBC failure-cause claim (unsourced).
  - Capital One, Synovus, CFS and Hawthorn filing figures (from search summaries; filings not re-read).

## References

All accessed 2026-10-22 unless noted.

**FDIC data (DEWEY primary pulls)**
- FDIC BankFind financials API: https://api.fdic.gov/banks/financials
- Latest-quarter G1 pull: https://api.fdic.gov/banks/financials?filters=REPDTE:20260630%20AND%20ASSET:%5B10000000%20TO%20100000000%5D&fields=CERT,BKCLASS,ASSET,LNATRES,NCLNLS,LNLSGR,NTLNLSQ,ELNATQ&limit=10000
- Q3 availability check (0 rows): https://api.fdic.gov/banks/financials?filters=REPDTE:20260930&fields=CERT&limit=1
- FDIC data dictionary: https://api.fdic.gov/banks/docs/risview_properties.yaml
- FDIC failures API: https://api.fdic.gov/banks/failures?filters=FAILDATE:%5B%222006-01-01%22%20TO%20%222018-12-31%22%5D&fields=CERT,NAME,FAILDATE,CITYST,QBFASSET,COST,RESTYPE,RESTYPE1&limit=10000
- FDIC institutions API: https://api.fdic.gov/banks/institutions

**FRED series**
- GDPDEF: https://fred.stlouisfed.org/series/GDPDEF
- CORALOBN: https://fred.stlouisfed.org/series/CORALOBN
- DRALOBN: https://fred.stlouisfed.org/series/DRALOBN

**FDIC Quarterly Banking Profiles**
- 4Q 2004: https://www.fdic.gov/analysis/quarterly-banking-profile/qbp/2004dec/qbp.pdf
- 4Q 2006: https://www.fdic.gov/analysis/quarterly-banking-profile/qbp/2006dec/qbp.pdf
- 4Q 2007: https://www.fdic.gov/analysis/quarterly-banking-profile/qbp/2007dec/qbp.pdf
- 4Q 2008: https://www.fdic.gov/analysis/quarterly-banking-profile/qbp/2008dec/qbp.pdf
- 4Q 2009: https://www.fdic.gov/analysis/quarterly-banking-profile/qbp/2009dec/qbp.pdf
- 4Q 2010: https://www.fdic.gov/analysis/quarterly-banking-profile/qbp/2010dec/qbp.pdf
- 4Q 2012: https://www.fdic.gov/analysis/quarterly-banking-profile/qbp/2012dec/qbp.pdf
- 4Q 2014: https://www.fdic.gov/analysis/quarterly-banking-profile/qbp/2014dec/qbp.pdf
- 4Q 2019: https://www.fdic.gov/analysis/quarterly-banking-profile/qbp/2019dec/qbp.pdf
- 1Q 2020: https://www.fdic.gov/analysis/quarterly-banking-profile/qbp/2020mar/qbp.pdf
- 4Q 2021: https://www.fdic.gov/analysis/quarterly-banking-profile/qbp/2021dec/qbp.pdf
- 4Q 2022: https://www.fdic.gov/analysis/quarterly-banking-profile/qbp/2022dec/qbp.pdf
- 1Q 2023: https://www.fdic.gov/analysis/quarterly-banking-profile/qbp/2023mar/qbp.pdf
- 4Q 2023: https://www.fdic.gov/analysis/quarterly-banking-profile/qbp/2023dec/qbp.pdf
- 1Q 2025: https://www.fdic.gov/quarterly-banking-profile/quarterly-banking-profile-first-quarter-2025.pdf
- 4Q 2025: https://www.fdic.gov/quarterly-banking-profile/quarterly-banking-profile-fourth-quarter-2025.pdf
- 1Q 2026: https://www.fdic.gov/quarterly-banking-profile/quarterly-banking-profile-first-quarter-2026.pdf
- 2Q 2026: https://www.fdic.gov/quarterly-banking-profile/quarterly-banking-profile-2q-2026

**CECL**
- Fed FEDS Note, "New Accounting Framework Faces Its First Test: CECL During the Pandemic" (Dec 3, 2021): https://www.federalreserve.gov/econres/notes/feds-notes/new-accounting-framework-faces-its-first-test-cecl-during-the-pandemic-20211203.htm
- Ranish & Vojtech, "How Did CECL Affect Bank Lending?", FEDS 2026-066 (Aug 2026): https://www.federalreserve.gov/econres/feds/files/2026066pap.pdf
- 85 FR 61577 (Sep 30, 2020): https://www.govinfo.gov/content/pkg/FR-2020-09-30/html/2020-19782.htm

**Collateral, loss severity and appraisal**
- Shibut & Singer, FDIC CFR WP 2015-06: https://www.fdic.gov/analysis/cfr/working-papers/2015/2015-06.pdf
- Ross & Shibut, FDIC CFR WP 2015-03: https://www.fdic.gov/analysis/cfr/working-papers/2015/2015-03.pdf
- FDIC, *History of the Eighties*, Ch. 3: https://www.fdic.gov/bank/historical/history/137_165.pdf
- GAO-13-71 (Jan 3, 2013): https://www.gao.gov/products/gao-13-71
- FDIC OIG EVAL-13-002 (Jan 2013): https://www.fdicoig.gov/sites/default/files/reports/2022-08/13-002EV.pdf
- SR 06-17 attachment (2006 ALLL policy): https://www.federalreserve.gov/boarddocs/srletters/2006/SR0617a1.pdf
- SR 23-5 attachment (2023 CRE workout statement): https://www.federalreserve.gov/supervisionreg/srletters/SR2305a1.pdf
- Fed FSR, Nov 22, 2024: https://www.federalreserve.gov/publications/files/financial-stability-report-20241122.pdf
- Fed FSR, Nov 7, 2025: https://www.federalreserve.gov/publications/files/financial-stability-report-20251107.pdf
- Fed FSR, May 8, 2026: https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf
- Crosignani & Prazad, NY Fed Staff Report 1130 (rev. Jun 2026): https://doi.org/10.59576/sr.1130
- Bushman & Williams (2015) metadata and abstract: https://api.crossref.org/works/10.1111/1475-679X.12079
- Ng & Roychowdhury (2014): https://ideas.repec.org/a/spr/reaccs/v19y2014i3d10.1007_s11142-014-9281-z.html

**CMBS and market**
- KBRA conduit CMBS default and loss study (Jul 31, 2025): https://www.kbra.com/publications/wdqmQrBV
- KBRA single-borrower CMBS study via CREFC (Spring 2026): https://www.crefc.org/common/Uploaded%20files/Learn/CREFC%20World/Spring%2026/Single-Borrower-CMBS-Default_Final.pdf
- MBA NewsLink citing Moody's 2022 loss severities (Apr 3, 2023): https://newslink.mba.org/?p=195479

**Supervisory views**
- Fed Supervision & Regulation Report, Jun 2026: https://www.federalreserve.gov/publications/files/202606-supervision-and-regulation-report.pdf
- Fed Supervision & Regulation Report, Dec 2025: https://www.federalreserve.gov/publications/files/202512-supervision-and-regulation-report.pdf
- OCC Semiannual Risk Perspective, Spring 2026: https://www.occ.treas.gov/publications-and-resources/publications/semiannual-risk-perspective/files/pub-semiannual-risk-perspective-spring-2026.pdf
- Richmond Fed Supervision News Flash (Aug 2024): https://www.richmondfed.org/banking/banker_resources/news_flash/2024/202408_ACL

**SEC 8-K exhibits, Q3 2026.** These are EDGAR folder URLs built from the accession number. The writer did not re-fetch them.

| Bank | Accession | URL |
|---|---|---|
| VLY | 0000714310-26-000045 | https://www.sec.gov/Archives/edgar/data/714310/000071431026000045/ |
| EGBN | 0001050441-26-000110 | https://www.sec.gov/Archives/edgar/data/1050441/000105044126000110/ |
| ZION | 0000109380-26-000125 | https://www.sec.gov/Archives/edgar/data/109380/000010938026000125/ |
| BKU | 0001504008-26-000088 | https://www.sec.gov/Archives/edgar/data/1504008/000150400826000088/ |
| HBAN | 0000049196-26-000084 | https://www.sec.gov/Archives/edgar/data/49196/000004919626000084/ |
| SSB (CIK 764038) | 0001193125-26-427824 | https://www.sec.gov/Archives/edgar/data/764038/000119312526427824/ |

**Reproduction recipe: aggregate base rate**

1. **Pull.** Make one call per quarter for REPDTE 19840331..20260630 (170 quarters):
   `https://api.fdic.gov/banks/financials?filters=REPDTE:{YYYYMMDD} AND ASSET:[500000 TO 200000000]&fields=CERT,REPDTE,BKCLASS,ASSET,LNATRES,NCLNLS,NALNLS,P9LNLS,NTLNLS,NTLNLSQ,ELNATR,ELNATQ,ELNLOS,LNLSGR&limit=10000`
   Make a second pass with `fields=CERT,REPDTE,LNCRCD`. The API returns HTTP 429 above about 4 concurrent requests, so back off and retry.
2. **Clean.** Drop BKCLASS OI and NC. Flows come from NTLNLSQ and ELNATQ. Where those are missing, de-cumulate the YTD fields (Q1 = YTD; Qn = YTDn − YTDn−1, same CERT and year).
3. **Group** each quarter on ASSET ($K):
   - G1 = [1e7, 1e8]
   - G1x = G1 with LNCRCD/LNLSGR ≤ 0.25
   - G1r = G1 bounds × GDPDEF_t / 133.411
   - G2 = [1e6, 1e7)
4. **Build ratios.** Ratios are sums over banks. NCO = 4 × ΣNTLNLSQ / Σ avg(LNLSGR_t, LNLSGR_t−1). Apply the triggers and outcomes exactly as pre-registered above.

**Reproduction recipe: cross-section**

1. **Pull.** For each date (20061231, 20071231, 20080630 … 20100630 quarterly; 20150630, 20160331 … 20171231 quarterly; 20260331, 20260630), call:
   `https://api.fdic.gov/banks/financials?filters=REPDTE:<YYYYMMDD>&fields=CERT,NAME,REPDTE,STALP,ASSET,LNATRES,NCLNLS,NTLNLS,NTLNLSQ,ELNATR,LNLSGR,LNRE,LNRECONS,LNRENRES,LNREMULT,NALNLS,P9LNLS&limit=10000&sort_by=CERT&sort_order=ASC`
   Pause about 8 seconds between quarters.
2. **Screen.** Keep ASSET ≥ 1,000,000, LNLSGR/ASSET ≥ 10%, and NCLNLS/LNLSGR ≥ 0.25% at the start of the window.
3. **Compute.**
   - Outcome = Σ NTLNLSQ_q / LNLSGR_(q−1).
   - Failures come from the failures API with RESTYPE = FAILURE.
   - Quintiles are taken on ΔCov.
   - Spearman correlations use the normal-approximation p-value.
   - OLS uses HC1 standard errors, with regressors winsorised at 1/99.
4. **Today's banks.** Use CERT filters 33555, 9396, 6560, 34742, 58979 and 2270. Guaranteed-loan fields are NAGTY, P9GTY, NCGTYPAR and IDNCGTPR.

## Process Report

- **DEWEY verification and provenance:**
  - DEWEY ran both kill checks itself: a grep of REGINALD/GIBBS found no ≥2-downturn study, and the FDIC BankFind aggregation was confirmed live for 1990Q1 through 2026Q2.
  - DEWEY re-pulled the EGBN (88.5%) and VLY (123.3%) Q2 call-report coverage and the band total including foreign branches (112.75%), and all three match.
  - Four Opus legs ran in data-return mode with pre-registered triggers. A report-writer sub-agent drafted this report; DEWEY reviewed it before filing.
  - **Rerun owed after ~10/30**, when the Q3 call reports land, for the bank-level placement.
- **Searches run:**
  - About 200 shared web-search calls were used before the budget ran out. The collateral leg then switched to direct fetches of primary documents.
  - The core evidence is direct FDIC API pulls, which needed no search:
    - 170 quarterly aggregate pulls, 1984Q1–2026Q2.
    - Bank-level cross-sections for 2006–10, 2015–17 and 2026.
    - The failures list.
  - FRED supplied the deflator and cross-check series.
  - About 30 fetches covered FDIC QBPs and Fed papers for the CECL break.
  - Six SEC 8-K exhibit sets covered the Q3-2026 statements.
  - This synthesis ran no new searches.
- **Data gaps:**
  - 2026Q3 call reports are not yet loaded.
  - There is no CECL-consistent coverage history.
  - CRE and office segment NCOs were not pulled.
  - No constant-membership panel was built.
  - FDIC resolution costs were not merged into the loss outcome.
  - Not found: RTC recovery rates, LGD on 2015–16 energy loans, 2024–26 CMBS office severities, and a loan-level accuracy rate for "well-secured" calls.
  - Company coverage definitions for EGBN and VLY were not reconciled to call-report values.
- **Source frustrations:**
  - The FDIC dictionary carries titles only, with empty descriptions.
  - The FDIC API rate-limits (HTTP 429).
  - 1984–86 data are duplicated or partly null.
  - Quartr returned "subscription_required", so there were no Q3 call transcripts.
  - A Reiprime/Trepp page returned HTTP 403.
  - Fed OIG summary URLs returned 404.
  - The FDIC 2026 Risk Review page is JS-rendered and returned no usable text.
  - Some filing figures came only from search summaries and were excluded.
- **Confidence in findings:**
  - (c), the cross-section "no": Medium-High for 2007–10. It is pre-registered, n = 373, failures are kept, and it is robust across 5 of 6 variants.
  - (a)/(b), the aggregate hit rates: Medium on the data, Low on generalising. Results come from about 3 cycles, and one episode moves a rate 8–10 points.
  - Today's placement: Medium. It uses Q2 data across the CECL break.
  - Post-2020 hit rates: uninformative by construction.
- **If I had more time/tools:**
  - Rerun the bank-level placement on Q3 call reports after about 10/30.
  - Merge FDIC resolution cost into a loss-inclusive outcome.
  - Pull CRE and office NCO fields.
  - Build a constant-membership panel.
  - Compute median-bank rates alongside the asset-weighted ones.
  - Read the Q3 transcripts for NPL-specific LTVs and appraisal dates.
- **Suggestions:**
  - **BACKLOG promotion candidate:** an `fdic_xsec.py` helper in `scripts/` for one-command cross-sections, with built-in 429 backoff and OI/NC exclusion. Building it is Will-greenlit per the build gate.
  - Add an OI/NC-exclusion warning to any fleet coverage aggregate; it is worth about 3pp at 2026Q2.
  - Revisit this question once the 2024–26 episode resolves either way. It is the only post-CECL test case.
