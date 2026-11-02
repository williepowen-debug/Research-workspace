# What is driving the KRE–KBWB decoupling? Testing hypotheses A, B and C
Study 6 · data through the 10/30/2026 close · written 11/02/2026

## Bottom line

The brief bundles two different things under "decoupling". Once they are separated, the three hypotheses rank differently for each.

1. **The cumulative return gap** (KRE −6.02% vs KBWB −8.43% over the 63 sessions from 8/3 to 10/30, so +2.41pp for KRE). This gap is **small and ordinary**: it equals 0.40 standard deviations of the 63-day tracking error, and 55% of past non-overlapping 63-day windows since 2012 had a bigger gap. It also depends on the start date: KRE was **3.9pp behind** KBWB on 9/11. About three-quarters of the gap is accounted for by five capital-markets names inside KBWB (JPM, BAC, GS, MS, C), with BAC alone about 1.0pp. **Hypothesis B explains the return gap. It is mostly a temporary, large-bank-specific shock.**
2. **The co-movement anomaly** (63-day correlation 0.719, about the 1st–2nd percentile). This one is real and **not** explained by B. KRE's correlation with *traditional* large banks (0.882) is even rarer, at the 0.24th percentile since 2015. It also isn't explained by A: in the window, KRE and traditional banks have identical sensitivity to Treasury yields. What sets KRE apart is a **collapsed equity-market beta** (0.33 against a since-2015 median of 1.09). That beta has been falling since the first half of 2026, before 9/14. Alongside it there is a **bank-wide** change in how bank stocks respond to rates and credit: they now fall when yields rise, and they no longer fall when HY spreads widen. **A narrow version of C (a change in what risk regional banks are priced on) describes this, but not the version where investors reward stronger banks.** There is no sign of quality discrimination.

**Central question.** The *return* separation is mostly temporary, driven by shocks to large banks (BAC above all) plus one unique day (10/22). The *pricing structure*, meaning low market beta, inverse yield sensitivity and indifference to HY spreads, has persisted since early-to-mid 2026. It is not a product of the 9/14 or 10/22 shocks. That structure is a shared repricing of bank risk, partly sector-wide. It is not investors sorting regional banks by fundamentals.

### Ranked assessment

| Rank | Hypothesis | Verdict | Distinguishing evidence |
|---|---|---|---|
| 1 | **B. Large-bank capital-markets shocks** | **Explains most of the return gap, but not the correlation anomaly** | Removing CM5 from KBWB (holdings-based) shrinks the gap from 2.41pp to 0.60pp. 9/14 alone = 85% of the summed daily gap. Rally 10/15–10/30: KBWB-ex-CM +5.00% vs KRE +5.06%, so no gap. **Against:** KRE vs traditional-15 corr is at the 0.24th pct. GS and MS fell about 12% *despite* large Q3 beats, so this is not a realized-earnings story. The 9/14 hit also spread to non-CM banks. |
| 2 | **C. Changed risk pricing (narrow form)** | **Partly supported: bank-wide factor shift plus KRE-specific beta collapse, no quality sorting** | Bank betas to ΔHY OAS were −0.3 to −0.9 per 10bp (t −2 to −4.6) in every period from 2020 to H1-2026; in the window they are +0.18 (KRE), +0.38 (traditional). 10/22 is unique: KRE fell on all 23 prior "Treasuries up, credit wider, stocks down" days since 2020 and rose 2.5% on 10/22. **Against:** returns are not explained by ROA, capital or earnings growth. Vol-adjusted dispersion is normal (68th pct). Size/beta dominates. Much of the shift is bank-wide, not regional-specific. |
| 3 | **A. Regional-specific rate/balance-sheet sensitivity** | **Weakest as an explanation of the *separation*.** Inverse yield sensitivity is real but shared by all banks | Window: KRE and traditional banks both move −0.67% per +10bp in the 10y; the KRE-minus-traditional gap has a rate coefficient of −0.01 (t −0.03). That relative sensitivity was *larger* in 2024–25 (t ≈ −2.6). Unrealized-loss/equity does not predict yield beta or the 10/22 move (16-bank and 150-bank samples; signs often opposite). On the hike day (9/16) KRE beat traditional banks by 1.9pp. Over the 63 days yields rose (10y +24bp), so A predicts KRE *lagging*. **For:** A explains part of the late-October rally direction for all banks, and loan/deposit ratio (funding) lines up with yield beta. |

---

## Data and design (what was actually done)

- **Window:** 63 daily returns, 8/4–10/30/2026 (base close 8/3). Sub-windows: selloff 8/4–10/14, rally 10/15–10/30. Comparison periods: 2015–19, 2022-03–2023-07, 2023-H2, 2024, 2025, 2026-01–07.
- **Prices:** Yahoo daily adjusted closes. **Yields:** U.S. Treasury daily par curve (3m, 2y, 10y). **HY/IG OAS:** ICE BofA via FRED (daily values spot-checked against the FRED series page; the full series came from a FRED mirror because FRED's CSV endpoint was unreachable from this environment).
- **Point-in-time KBWB weights:** SEC **Form N-PORT** for Invesco KBW Bank ETF as of 8/31/2026 (June-rebalance share counts, used 8/4–9/18) and Invesco's 10/30 holdings file (post-September-rebalance share counts, used 9/21–10/30), both drifted daily with prices. Replication vs actual KBWB: daily corr 0.9994, tracking 3.8bp/day, cumulative −8.38% vs −8.43%. **KRE weights:** SSGA 10/30 holdings (point-in-time June-rebalance file not found; replication corr 0.998).
- **Bounded company sample (16, fixed by rule before looking at window returns; spec in PREREGISTERED_SPEC.md):** G1 capital-markets JPM BAC GS MS · G2 traditional super-regionals in KBWB only USB PNC FITB KEY · G3 four largest KBWB∩KRE by assets TFC HBAN CFG MTB (CFG replaced RF under the asset rule; logged) · G4 small/mid KRE-only ASB TCBI CUBI TOWN.
- **Fundamentals:** 6/30/2026 SEC XBRL (10-Q) for all names; FDIC call reports for TowneBank (an FDIC filer), Truist's HTM fair value and M&T's deposit cost. Q3 XBRL covers only about 42 of 176 banks so far, and FDIC 9/30 call reports are not loaded yet, so Q2 is the cross-sectional baseline. Q3 earnings-release facts come from the prior study-2 reading of 8-K exhibits.
- **"Traditional 15"** = EW basket of WFC, USB, PNC, FITB, KEY plus the 10 KBWB names also in KRE (TFC, MTB, HBAN, CFG, RF, EWBC, PNFP, FHN, ZION, WAL).
- All regressions use daily returns with HAC (5-lag) standard errors. Coefficients are % return per +10bp.

---

## Hypothesis B: large-bank capital-markets shocks

**Contribution of the big banks to KBWB's underperformance** (holdings-based, sum of daily weight × return, 63 days):

| Name | Avg weight | 63d return | Contribution |
|---|---|---|---|
| BAC | 8.1% | −19.6% | −1.69pp |
| MS | 7.5% | −12.2% | −0.97pp |
| GS | 7.4% | −12.5% | −0.95pp |
| MTB | 3.9% | −11.0% | −0.44pp |
| CFG | 3.4% | −11.5% | −0.39pp |
| WFC | 8.2% | −4.6% | −0.35pp |
| JPM | 8.4% | −4.0% | −0.31pp |
| C | 4.0% | −8.2% | −0.34pp |

Group contributions: CM5 −4.26pp of KBWB's −8.40pp (summed). Custody (BNY, NTRS, STT) −0.76. Traditional large −1.27. The 10 overlap regionals −1.90.

**Counterfactual KBWB (weights renormalized):**

| | 63d | selloff 8/4–10/14 | rally 10/15–10/30 |
|---|---|---|---|
| KRE | −6.02 | −10.55 | +5.06 |
| KBWB | −8.43 | −11.47 | +3.43 |
| KBWB ex BAC | −7.40 | −10.86 | +3.89 |
| KBWB ex CM5 | **−6.62** | −11.07 | **+5.00** |
| Traditional 15 (cap-wt / EW) | −6.83 / −6.89 | −11.37 / −11.66 | +5.12 / +5.40 |

**Was the 9/14 BAC guidance unusually important?** Yes, for returns. On 9/14 KRE rose 0.28% and KBWB fell 1.89%. That one-day gap of +2.17pp equals **85% of the summed daily gap** over the window. But on 9/14 KRE still beat KBWB-ex-CM by 1.29pp, because non-CM large banks (NTRS, WFC and others) also fell. BAC's own shocks came in three parts: the CEO's verbal guidance at the Barclays conference, a record AML penalty announced 10/13, and a Q3 report on 10/14 that analysts called the worst capital-markets result in its peer group.

**The capital-markets shock was not sector-wide.** GS and MS beat estimates by wide margins in Q3. JPM missed. Citi's IB fees fell 13% QoQ. So "capital-markets weakness" is better described as **BAC-specific plus capital-markets equity derating**. GS and MS fell about 12% while reporting record equities revenue. That is consistent with investors pricing future capital-markets or AI-financing risk rather than realized results. That reading is a hypothesis; this study did not test it.

**Is KRE still unusually independent of traditional commercial banks? Yes. This is the main evidence against B as the full story.**

| 63d corr with KRE | value | pct since 2015 | median | partial \| SPY (pct) |
|---|---|---|---|---|
| KBWB | 0.719 | 1.9 | 0.946 | 0.728 (2.6) |
| Traditional 15 EW | 0.882 | **0.24** | 0.973 | 0.884 (3.7) |
| 10 overlap regionals EW | 0.900 | **0.10** | 0.976 | 0.904 (5.2) |
| CM5 EW | 0.456 | 2.4 | 0.853 | 0.419 (8.7) |

Large banks also split among themselves: traditional-15 vs CM5 is 0.688, the 5.8th pct.

**Do ETF weights explain it?** Membership matters, the weighting scheme much less. KBWB equal-weighted would have returned −7.63% (vs −8.43%, so 0.8pp). KRE's members cap-weighted would return −6.17% (vs −6.02%). The relevant structural fact is that KBWB holds **35.5% in CM5**, a result of the KBW index's 8% cap on its five largest names. KRE holds none of them and has only 11% in the overlap names.

---

## Hypothesis A: interest-rate and balance-sheet sensitivity

**Does regional relative performance improve when yields fall?** Against KBWB, slightly: the gap coefficient is −0.19%/10bp on Δ10y, t −0.7, not significant. Against traditional banks, **not at all** in the window:

| Δ10y coefficient (%/+10bp) | KRE | KBWB | Trad15 | KRE−KBWB | KRE−Trad15 |
|---|---|---|---|---|---|
| 2015–19 | +1.83 | +1.77 | +1.88 | +0.05 | −0.06 (t −2.6) |
| 2022-03..2023-07 | +0.27 | +0.18 | +0.33 | +0.09 | −0.06 |
| 2023-08..12 | −0.91 | −0.67 | −0.91 | −0.25 | −0.01 |
| 2024 | −0.04 | +0.16 | +0.11 | −0.19 | −0.15 (t −2.75) |
| 2025 | +0.33 | +0.46 | +0.48 | −0.13 | −0.16 (t −2.55) |
| 2026-01..07 | −0.68 | −0.53 | −0.53 | −0.15 | −0.15 |
| **Window** | **−0.67** | −0.49 | **−0.67** | −0.19 (t −0.7) | **−0.01 (t −0.03)** |

2y yields give the same picture, and the curve slope (10y−2y) is insignificant in the window. Adding SPY as a control: KRE −0.62, Trad15 −0.54, KRE−Trad15 −0.08 (t −0.6).

**Policy rate vs Treasury yields.** On the 9/16 hike day (2y +7bp, 3m +3bp) KRE fell 1.77%, but KBWB fell 2.88% and traditional banks about 3.65%. KRE outperformed on a hawkish policy event, the opposite of the A prediction. On 10/28 (hold with two hawkish dissents; 2y −3bp, 10y +6bp) KRE lagged KBWB by 1.28pp. The Fed's policy rate changed once. Most of the yield variance in the window came from term and global-safety moves (10/22), not from the policy path.

**Do banks with larger unrealized losses react more strongly to falling yields?** No.
- *16-bank sample* (after-tax unrealized loss/equity ranges from −25% at BAC and −20/−21% at TFC/USB down to about −2 to −7% for the small G4 names). Spearman with window yield beta: −0.16 (p .54), and the sign is opposite to A (bigger losses → *less* negative beta). BAC has the biggest loss and near-zero yield beta.
- *All KRE names with XBRL (n=150)*: unrealized loss/equity vs yield beta ρ −0.04 (p .63); vs 10/22 return +0.05; multivariate with size t −0.6 / +0.2. **Null.** This matches study 3, which used FDIC data.
- What does line up: **loan/deposit ratio** (16 banks: ρ −0.64 with the 126-day yield beta, +0.67 with excess return on falling-2y days, both p ≈ .01), and size (larger → more negative yield beta, ρ −0.22, p .005). Both point to a *funding/deposit-competition* channel, not an AOCI channel. The L/D link weakens to insignificance once the four G1 banks are dropped.
- Deposit costs (from prior study-2 Q3 releases): deposit costs rose QoQ at 8 of 10 sample banks after the September hike, while NIMs were up at 10 of 16. That is consistent with hikes being a mixed rather than clearly negative shock for regionals.

**Different from 2024–25?** Yes, in two ways that both work against A as an explanation of the separation. First, absolute bank yield betas are negative in 2026, as they were in 2023-H2, after being strongly positive in 2015–19. That shift is bank-wide. Second, the regional-*relative* yield sensitivity that existed in 2024–25 disappeared in the window.

---

## Hypothesis C: a change in how investors price banking risk

**Do HY spreads, yields and the market explain regional relative returns?** (window model: SPY + Δ10y + ΔHY)

| | R² KRE | R² gap (KRE−KBWB) | KRE β to ΔHY (%/10bp) | Trad15 β to ΔHY |
|---|---|---|---|---|
| 2020-07..2021 | 0.38 | 0.02 | −0.37 | −0.47 |
| 2022-03..2023-07 | 0.49 | 0.01 | −0.31 (t −2.3) | −0.38 |
| 2024 | 0.26 | 0.06 | −0.71 (t −3.1) | −0.64 |
| 2025 | 0.55 | 0.02 | −0.50 (t −4.3) | −0.50 |
| 2026-01..07 | 0.21 | 0.16 | −0.82 (t −3.2) | −1.00 |
| **Window** | **0.16** | **0.23** | **+0.18 (t 0.9)** | **+0.38 (t 1.3)** |

- Bank stocks **stopped responding to HY spread widening** in the window: HY OAS went from 2.78 to 3.44, IG OAS from 0.78 to 0.94. This happened across banks: rolling percentiles since 2020-10 are KRE 87th, traditional 98th, KBWB 91st. Positive HY betas occurred in about 16–25% of past windows, so this is rare but not unprecedented. A plausible reason, supported by credit-market commentary but **not tested here**, is that the widening was concentrated in AI-related borrowers while the rest of credit stayed tight. That would make HY a poor signal of domestic bank credit risk.
- The gap's explained share rose to 23%, almost entirely through **market beta**: KRE's SPY beta is 0.35 against 0.78 for traditional banks, and the gap's SPY coefficient is −0.48. SPY was flat over the window (+0.1% summed), so market beta contributes almost nothing to the *cumulative* gap while dominating the *daily* correlation.

**Was 10/22 a flight to Treasury safety despite widening spreads?** For Treasuries, yes. For regional banks it was without precedent in the data. On 10/22 SPY fell 1.18%, the 10y fell 17bp and HY widened 13bp, yet KRE rose 2.53%. KBE rose 2.38%, traditional banks 1.12%, KBWB 0.16% and CM5 −0.64%. Homebuilders (+5.4%), utilities (+2.1%) and REITs (+1.1%) rallied, while QQQ (−2.9%) and momentum (−3.7%) fell. The window factor model, fitted excluding 10/22, predicts KRE −0.09%, leaving a residual of +2.6%. **In all 23 prior days since 2020 with 10y ≤ −10bp, HY ≥ +8bp and SPY ≤ −0.75%, KRE fell (−0.75% to −15.5%).** On that day regional banks traded as a rate-sensitive *domestic* asset, like homebuilders and utilities, and not as a credit asset. The trigger was AI-capex doubts after Meta's results, plus French fiscal stress and oil. That fits the narrow C story but is one day.

**Comparable historical periods.** Negative bank yield betas: 2023-H2, much of 2024, 2026. The 10/22 pattern: none since 2020 (study 3 found only 2008-01-22 since 2006, the day of an emergency Fed cut). Study 3 also found that after falling-2y windows KRE *lagged* KBWB over the next 60 sessions (about −2pp, t ≈ −3). That is weak evidence that rate-relief rallies in regionals do not persist relative to big banks.

**Quality vs shared risk.** The evidence points to shared risk.
- Average pairwise correlation among KRE names is 0.643, the 42nd pct of 31 non-overlapping windows since 2019, which is normal. Raw cross-sectional dispersion of 63-day returns is the lowest of 31, but after dividing by average stock vol (itself at the 3rd pct) it is normal (68th pct).
- Q2 ROA, equity/assets and NI growth do not explain 63-day, selloff or rally returns (n ≈ 150; all |t| < 1.5, except high-ROA banks *lagging* the rally, t −2.0). Size explains a lot (selloff t −6.6, rally +3.0), which is a beta pattern.
- Q3 earnings-window reactions in the study-2 sample: median −0.5% vs KRE, with only weak, insignificant links to NIM and deposit-cost changes.

---

## How much of the divergence each mechanism accounts for

The two lenses below are **not additive**. CM names are also less rate-sensitive, so "rates" and "CM composition" overlap.

**Lens 1: exact holdings accounting (compound 63d gap = +2.41pp)**

| Component | pp | share |
|---|---|---|
| BAC in KBWB | +1.04 | ~43% |
| GS + MS | +0.78 | ~32% |
| JPM + C (beat KRE) | −0.37 | −15% |
| **All CM5** | **+1.81** | **~75%** |
| KRE vs KBWB-ex-CM (everything else) | +0.60 | ~25% |

**Lens 2: daily factor model on the summed gap (+2.56pp), window betas**

| Component | no event dummies | with 9/14 & 10/22 dummies |
|---|---|---|
| Market (SPY) | −0.06 | −0.04 |
| Rates (Δ10y, +24bp net) | **−0.65** | −0.18 |
| HY spread (+66bp; β insignificant) | +0.64 | +0.51 |
| 9/14 (BAC guidance day) | — | +2.00 |
| 10/22 (AI/Treasury rally day) | — | +1.75 |
| Intercept × 63 / other days | +2.64 | −1.46 |

**Defensible reading.** B accounts for roughly 1.8 of the 2.4pp. Rates, the A mechanism, **work against** the full-window gap: yields rose, and KRE's yield beta was slightly more negative than KBWB's. Rates help explain about 0.7pp of the 1.6pp late-October rally gap, but in the rally that overlaps completely with the CM-composition effect (KBWB-ex-CM matched KRE). HY spreads (C) are statistically indistinguishable from zero. Two days, 9/14 and 10/22, contribute 3.75pp, more than the whole gap, offset by −1.5pp over the other 61 sessions. **For the correlation anomaly** the decomposition is different: the stress test (study 1) found that KRE's low market beta and low volatility account for roughly half of the shortfall, and B accounts for little (vs traditional banks the anomaly is *larger*).

---

## Most important unresolved contradictions

1. **"Regional banks outperformed" vs "KRE trailed for six weeks."** KRE was 3.9pp behind on 9/11 and 2.4pp ahead on 10/30. Two event days produced the sign. Any explanation of *outperformance* is explaining 0.4σ of noise plus two shocks.
2. **Inverse yield sensitivity during a hiking cycle.** Bank stocks fall when yields rise even though BAC is guiding to higher NII on *three more hikes* and regional NIMs mostly rose in Q3. Equity markets are pricing rate rises as bad for banks, possibly via credit, funding or valuation, while earnings guidance says they are good. The AOCI channel, the textbook reason, is absent from the cross-section.
3. **Credit spreads widened while bank stocks ignored them.** This is either rational (AI-specific widening) or complacent. If HY widening broadens to non-AI sectors, the zero HY beta should revert. Q4 provisions will be the test.
4. **GS and MS fell about 12% after blowout quarters.** The CM shock that drives B is not realized earnings. If it is AI-financing or underwriting risk, B and C are the same story seen from the big-bank side, and the "temporary shock" label may be wrong.
5. **KRE's low beta: regime or artifact?** Traditional banks' beta also collapsed (0.34 in Jul–Aug, 0.63 now; median 1.13), so part of it is sector-wide. KRE–traditional correlation fell from 0.97 (2025) to 0.93 (Aug) to 0.88 (Oct), steepest in Sep–Oct, *after* 9/14. So events did deepen a split that had started earlier.

---

## Three indicators to monitor (November–December 2026)

1. **KRE's 63-day beta to SPY and its correlation with traditional large banks.** Now 0.33 and 0.882. Since-2015 references: beta 10th pct 0.73, median 1.09; correlation 10th pct 0.948, median 0.973. *Regime fading:* beta back above about 0.7 and correlation above about 0.95. *Regime entrenching:* correlation stays below about 0.90 while traditional banks' beta recovers (the split becomes regional-specific). This tests C against "temporary".
2. **Bank-stock sensitivity to HY OAS (rolling 63-day β of KRE and traditional banks to ΔHY), read alongside HY OAS itself (3.44 on 10/30).** *Credit re-coupling:* β turns back to ≤ −0.3%/10bp, especially if HY keeps widening beyond AI names. That would mean the market has resumed treating credit spreads as bank risk, and the 10/22-type behaviour should stop. *Mechanism still active:* β stays near zero or positive as spreads move.
3. **KRE minus KBWB-ex-capital-markets, and KRE-minus-traditional on the Dec 8–9 FOMC day.** If the KRE−KBWB gap keeps growing only through JPM/BAC/GS/MS/C, it is B. Watch mid-quarter guidance at December investor conferences, the counterpart to BAC's 9/14 remarks. If KRE underperforms *traditional* banks on a hawkish Dec 9 outcome (2y up), regional-specific rate sensitivity (A) has returned. In the window it was zero, and on the 9/16 hike KRE outperformed.

---

## Confidence & gaps

- **High confidence:** the holdings-based B accounting (N-PORT plus Invesco replication within 5bp cumulative); KRE vs traditional-bank correlation rarity; the KRE-minus-traditional gap having no rate sensitivity in the window; 10/22 being without precedent since 2020; the gap being statistically small.
- **Medium:** the HY-beta flip (63 daily observations, t < 1.5; strong only as a contrast with t −2 to −4.6 in every earlier period); the AOCI null (Q2 data, XBRL tag heterogeneity fixed by hand; the 16-bank sample is small).
- **Low or untested:** *why* GS/MS derated (AI-financing exposure is a hypothesis); *why* HY widened (sector composition is attributed to credit-strategy commentary, not measured here); deposit-cost effects (Q3 releases only for the study-2 sample; FDIC 9/30 call reports not yet loaded); securities duration (not collected, because releases report it inconsistently).
- **Source limits:** BAC's 9/14 guidance was verbal, with no SEC filing, so it rests on media accounts (CNBC, Reuters-based outlets). HY OAS is licensed ICE data obtained via a FRED mirror; values were checked against FRED's page. KRE point-in-time weights before the September rebalance were not found (KRE replication with 10/30 shares: corr 0.998, cumulative −5.72% vs −6.02%). FRED's CSV endpoint failed all session.
- **Correction to the brief's premises:** (i) the 63-session outperformance is start-date dependent and small; (ii) KRE's negative yield relationship is shared by traditional banks and KBWB, so it is not regional-specific in this window.

## Files
REPORT.md (this file) · fig_study6.png · PREREGISTERED_SPEC.md · scripts/ (panel.py builds the panel and point-in-time KBWB weights; hypA_ts, hypA_xs, hypB, hypB_corr, hypC–C4, attrib, weights, thresholds, figure) · out/ (all result CSVs; KBWB N-PORT XML and 10/30 holdings JSON; KRE 10/30 holdings).
