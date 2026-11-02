---
title: "KRE Study 4 — Market leadership vs. regional-bank decoupling"
subtitle: "Data through the 10/30/2026 close · prepared 11/02/2026 · read-only research"
---

# Answer in one paragraph

**Mostly the market changed, not regional banking.**

* **Why KRE's beta to SPY collapsed (1.13 → 0.33).** Once value, size and momentum factors are added, KRE's own market loading is normal: **1.09, about the 60th percentile.** The low SPY beta comes from a change in how the *factors* move against SPY. Value now has a beta of **−0.85** on SPY, against a pre-2025 median of −0.04. Small caps (SMB) have stopped moving with SPY: their beta is +0.03, against +0.15. Holding KRE's loadings fixed at their 2012–2024 values, that change in market structure accounts for −1.10 of the −0.87 fall in beta. KRE's own loadings moved the *other* way (+0.22).
* **The beta collapse is not specific to regional banks.** All ten comparison ETFs have a 63-session SPY beta at or below their own 10th percentile (0th–9th). They are the seven predetermined nonbank sectors (XLU, IYR, ITB, XLI, XLB, IYT, KIE) plus small value (IWN), financials (XLF) and KBWB.
* **Factor models stopped working market-wide.** Their fit broke down out of sample in Jul–Oct 2026 for KBWB, XLI, XLF and XLB as much as for KRE.
* **The KRE–KBWB correlation fell (0.95 → 0.72) mainly because the shared factor variance halved.** KRE's factor-driven volatility fell from 26.6% to 12.3%, while its residual volatility stayed near normal (9.5% vs 8.3%; 69th percentile). Two smaller pieces remain:
  * **KBWB itself moved toward the mega-cap market.** Its market loading rose from 1.07 to 1.59. That is why its SPY beta held up better than KRE's.
  * **The bank-specific residual correlation between KRE and KBWB is modestly low:** 0.54, at the 14th percentile, or the 24th once volatility is matched. That is the only piece that could reflect regional-bank risk being priced differently, and it is not extreme.
* **Study 3's "rate-beta flip" belongs to the value regime.** The value factor itself now has a record negative yield sensitivity (−0.073, 0th percentile), and small value (IWN, −0.061) matches KRE (−0.062). With style factors controlled, KRE's yield loading is ordinary (34th percentile).

All of this is historical association within one regime, not proof of cause.

---

# 0. Verification of the brief's numbers (rebuilt from raw data)

| Brief | Re-derived (63 sessions to 10/30, univariate, simple daily returns) |
|---|---|
| KRE–KBWB corr 0.719, median ≈0.940 | 0.7193; median since Feb 2012 0.940; 1.5th pct ✓ |
| KRE SPY beta ≈0.33, median ≈1.11 | 0.328; median since Feb 2012 1.105 (1.3th pct); median 2012–2024 1.13 ✓ |
| KBWB SPY beta ≈0.83 | 0.825 (10th pct) ✓ |
| Partial corr given SPY ≈0.728, ~10–11th pct | 0.7276; 11.1th pct ✓ |

**Data**

* **Prices:** Yahoo v8 adjusted closes for 21 ETFs.
* **Factors:** daily Fama-French 3 factors and momentum from the Kenneth French Data Library. The files were built from the CRSP 202609 database, so they **end on 2026-09-30.** For October 2026 (22 sessions) I spliced in ETF proxies:
  * MKT = SPY − RF (correlation with the French series 0.995 over 2013-05 → 2026-09);
  * SMB = IWM − SPY (0.91);
  * HML = IWD − IWF (0.80);
  * MOM = MTUM − SPY (0.68).
* **Robustness to the splice:** every factor result is also shown for the window ending **9/30**, using pure French data. The conclusions are the same.
* **Other series:** Δ10y from the Treasury par curve; ΔBaa from FRED BAA10Y.
* **Reference distributions:** 2012-02 → 2024-12, so 2025–26 is out of sample, unless stated otherwise.
* **Pre-registration:** the spec, hypotheses, model list and ETF set were fixed before any statistic was computed (`SPEC.md`).

---

# 1. Ranked explanations

| Rank | Explanation | What it explains | Key evidence for | Key evidence against |
|---|---|---|---|---|
| **1** | **Market structure / leadership change.** SPY is now driven by mega-cap growth, value trades *against* it, and small caps trade apart from it. | ~All of the SPY-beta collapse; most of the KRE–KBWB correlation drop | Structure term −1.10 vs total −0.87; KRE market loading normal (1.09, 60th pct); corr(SPY, RSP) 0.64 (0th pct); 59% of SPY variance not explained by equal-weight RSP (median 5%); the same collapse in IWN, XLF, KIE, XLB, IYT; vs RSP most sectors are normal; factor fit broke down market-wide | It started in Jan 2025 (SPY–RSP split) and value's negative beta was already deep in mid/late 2024, yet KRE's beta stayed normal until June 2026. Structure alone does not time the onset (see §5). KRE is still lowish against RSP (beta 7th pct) and IWN (corr 4th pct). |
| **2** | **KBWB moved toward the market** (large banks' market loading rose) | Why KBWB's SPY beta fell less (0.82) than KRE's (0.33); part of the KRE–KBWB split | KBWB market loading 1.59 vs 1.07 median (+0.55 to its beta); KBWB market term 1.53 in 2026 H1 | Inference from factor loadings only, not holdings. KBWB's residual volatility and out-of-sample fit deteriorated *more* than KRE's. |
| **3** | **Low-volatility attenuation** | Part of the low *correlations* | Vol-matched windows move KRE–RSP corr to the 25th pct, KRE–IWN to the 21st, partial corr given SPY to the 30th, residual KRE–KBWB corr to the 24th | Does not touch the betas. KRE SPY beta, raw KRE–KBWB corr and 5-factor R² stay at the 0th pct even vol-matched. |
| **4** | **Rate regime** (regionals fall when yields rise) | A small part of fit; links to study 3 | Δ10y adds +0.035 to KRE's out-of-sample R² in Jul–Oct 2026 (historically +0.02); last-21d Δ10y loading at the 3rd pct | It is a **value-factor** property: value (IWD−IWF) yield beta −0.073 (0th pct), IWN −0.061, XLF −0.052, KBWB −0.031. With style controlled, KRE's 63d yield loading is normal (34th pct). |
| **5** | **Regional-bank-specific risk repricing** | At most a modest remainder | Residual KRE–KBWB corr 0.54 (14th pct); KRE–IWN corr 4th pct; last-21d value loading 4th pct; 10/22 behaviour (study 3) | KRE residual vol only 69th pct, *less* elevated than XLI (97), XLF (95), IWN (93), KIE (95). KRE's 63d alpha (−10%) is no worse than KBWB's (−13%). KBWB's factor fit broke down more. Residual corr is 24th pct vol-matched and 29th with pure French data. |

---

# 2. KRE's sensitivities: historical vs recent

### Table 2a — Univariate 63-session correlation and beta against benchmarks (percentile vs 2012–2024)
{{T_SENS}}

Reading: KRE is decoupled from **SPY** (0th pct), **QQQ** and **XLF**. Against **equal-weight RSP** it is low (6th–7th pct). Against **small value IWN** its *beta* is normal (0.97, 20th pct), though the correlation is lower (4th pct). Against bank ETFs (KBE) it is normal. KBWB is in the same position against RSP (10th pct) and IWN (23rd pct), and less extreme against SPY.

### Table 2b — KRE five-factor loadings (Mkt, SMB, HML, MOM, Δ10y) over 21/63/126 sessions vs history
Format is "now", then "median · percentile" against rolling windows of the same length from 2012–2024. "Now" ends 10/30 using the spliced factors. The pure-French column ends 9/30.

{{T_FACTOR}}

**KRE's factor loadings are ordinary.**

* **Market** loading: 31st–84th pct depending on the window.
* **Size** loading: 48th–85th pct.
* **Value** loading is somewhat low: 12th–16th pct (43rd with pure French data), and 4th pct over the last 21 days.
* **Δ10y** loading is normal over 63 and 126 sessions; it is low only over the last 21 days.

**What is abnormal is the R²** (0th–5th pct), and that happens with **near-normal residual volatility** (64th–78th pct). The residual KRE–KBWB correlation is the 10th–30th pct.

### Table 2c — Explanatory power of each model (KRE, in-sample)
{{T_MODELS}}

Adding the style factors raises KRE's 63d R² from 0.05 (SPY only) to 0.61. Rates, the SPY−RSP concentration spread and the Baa spread add almost nothing in sample (0.61 → 0.63). An equal-weight market (RSP) explains 0.30, far more than SPY's 0.05.

---

# 3. Is the market different? (sub-question 1)

### Table 3a — Market-structure metrics
{{T_LEAD}}

**What this shows**

* SPY and the equal-weight S&P have come apart. Their correlation is 0.64, the lowest in the 2012–2024 reference, and 59% of SPY's daily variance is now not explained by RSP (the reference median is 5%).
* RSP–QQQ correlation is at the 2nd pct. Value moves against SPY (corr −0.66).
* The split shows up in 2025 (median SPY–RSP corr 0.83) and deepens in late 2026.
* **This is a change in what "the market" means.** An index dominated by mega-cap growth now moves partly independently of, and partly opposite to, value and small-cap stocks.

### Table 3b — How KRE's SPY beta is assembled (63d; beta = Σ loading × factor's beta on SPY + residual)
{{T_TERMS}}

**Reading the decomposition**

* KRE's **market term has stayed about 1.1 throughout**, apart from a dip to 0.93 in Jul–Sep 2026.
* The beta fell because the **value term** went from −0.06 to −0.83 and the **size term** went from +0.08 (and +0.2 to +0.34 in 2025) to about 0.
* In 2025 the size and momentum terms offset value's negative co-movement. In mid-2026 small caps stopped co-moving with SPY, and that offset vanished.
* **That is why KRE's beta held up in 2025 despite the SPY–RSP split, and collapsed in June 2026.**
* KBWB faced the same value drag (−0.86), but its market term rose to 1.62.

---

# 4. Is it specific to regional banks? (sub-question 2)

The nonbank set was predetermined: XLU, IYR, ITB (rate-sensitive); XLI, XLB, IYT (cyclical); KIE (non-bank financial). IWN, XLF and KBWB are shown for comparison.

### Table 4 — SPY-beta collapses across sectors (63d; percentile vs 2012–2024)
"Structure" means the change caused by factors' co-movement with SPY, holding the ETF's 2012–24 loadings fixed. "Own loadings" means the change in the ETF's own factor loadings.

{{T_SECT}}

**What this shows**

* **SPY-beta collapses below the 10th percentile were common in 2025–26.** XLB was below on 68% of 2025 days and 85% of 2026 days. KIE was below on 100% of 2026. XLF and IYR on 72% of 2026. IYT on 44%, and IWN on 40%.
* **KRE (57% of 2026 days) is in the middle of this group, not an outlier.**
* For the cyclical and value ETFs (IWN, XLF, XLB, IYT, XLI, KIE), most of the fall is **structure**, as it is for KRE.
* For the rate-sensitive ones (XLU, IYR, ITB), it is mostly **own-loading** change: they now behave as bond proxies.
* **Relative to RSP**, most nonbank ETFs look normal (IYR 69th pct, IYT 66th, XLU 64th). KRE (7th), XLF (8th), IWN (9th), KBWB (10th) and XLI (6th) remain lowish. So among assets that load on value and the business cycle, KRE is a typical member, not a unique case.

---

# 5. What remains unexplained? (sub-question 3)

### Table 5a — KRE–KBWB correlation split into common-factor and residual parts (same 5-factor model)
{{T_CORR}}

**What this shows**

* Most of the drop in the KRE–KBWB correlation (0.95 → 0.72) comes from the **common-factor part** (0.83 → 0.52). The factors that both ETFs load on now have much less combined variance, because market and value offset each other: KRE factor volatility is 12% vs 27%.
* The residual contribution actually *rose* (0.12 → 0.19).
* The residual correlation (0.54) is below the pooled reference (0.76). Against rolling windows it is the 14th pct, a modest bank-level split.
* That split was **more pronounced in 2025**: it was below the 10th pct on 56% of 2025 days, but on only 6% of 2026 days.

### Table 5b — Volatility-matched comparison
Reference: the 10% of 2012–2024 windows closest to now in KRE volatility (15.6%) and SPY volatility (10.5%); 325 windows.

{{T_VM}}

Matching on volatility moves the *correlation* measures against the broad market, small value and the residual into the 21st–30th percentile, which is unremarkable. It leaves the SPY beta, the raw KRE–KBWB correlation, the factor R² and the SPY–RSP correlation at the extreme.

### Table 5c — Out-of-sample R² (fit on the prior 126 sessions, predict the next non-overlapping 21-session block)
{{T_OOS}}

**What this shows**

* **The style factors are the important addition out of sample** (KRE 0.43–0.89, against −0.10 to 0.52 for SPY alone).
* **Δ10y adds a little** (KRE +0.035 in Jul–Oct 2026).
* **The concentration spread (SPY−RSP) and ΔBaa add nothing.**
* **In Jul–Oct 2026 every model's out-of-sample fit fell for KRE *and even more for KBWB*** (0.33 vs 0.46).
* The same breakdown appears in XLI (0.86 → 0.45), XLF (0.91 → 0.37), XLB (0.78 → 0.29) and IYT (0.75 → 0.41) (Table 4).
* This was not cherry-picked: none of these out-of-sample results were used to choose models.

### How much of the unusual behaviour remains

| Unusual feature | Explained by common factors? | What remains |
|---|---|---|
| KRE SPY beta 0.33 vs 1.13 | Yes. Residual term +0.01; KRE's own loadings moved *up* (+0.22). Out-of-sample check, freezing KRE's loadings from one window and applying the next window's factor structure: for the window ending 8/3 it predicted 0.49, against a realized 0.30 and a naive 0.84, so about 65% of the drop was predicted ahead of time. For the window ending 10/30 it predicted −0.10, against a realized 0.33: KRE stayed *more* market-sensitive than structure alone implied. Neither miss points to an extra regional-specific decoupling. | ≈0 |
| KRE–KBWB corr 0.72 vs 0.94 | Mostly: the common-factor part fell 0.83 → 0.52 | Residual corr 0.54: 14th pct (24th vol-matched; 29th pure French) |
| R² 0.62 vs 0.87 | The share explained fell because factor variance shrank | Residual variance is about 1.3× normal. That excess equals **≈9% of KRE's current variance** ((9.5%² − 8.3%²) / 15.6%²) |
| Return path (63d alpha −10%) | No | But KBWB −13%, XLF −6%, IWN −4%: a common drag on value and financials, not KRE-specific |

---

# 6. When did the change occur? (sub-question 4)

### Table 6 — First 10-session run below the 2012–24 10th percentile, and share of days below, by year
{{T_ONSETS}}

![Timeline](out/fig_timeline.png)

**Sequence (association only)**

1. **Jan 2025 — the market changes first.** SPY decouples from equal-weight (60% of 2025 days below p10), and value moves against SPY (32% of days). KRE's SPY beta stays normal through 2025, because positive size and momentum terms offset the value drag.
2. **2025 — a bank-specific piece appears and fades.** The residual KRE–KBWB split is pronounced from Jan 2025 (56% of days below p10). The raw KRE–KBWB correlation dips from **Sept 2025**, at the same time as an RSP–QQQ correlation break (Sept 2025). That earlier episode coincides with a market-structure shock.
3. **Jan–Mar 2026 — co-movement erodes.** KRE–KBWB correlation below p10 from Jan 2026 (70% of 2026 days); KRE–RSP correlation from March 2026. KRE's Δ10y loading turns low from Feb 2026.
4. **June–July 2026 — a near-simultaneous step.** KRE SPY beta (6/5), KRE–IWN correlation (6/5), KRE factor R² (6/5), KBWB SPY beta (6/15), XLU SPY beta (6/22), KRE–XLI correlation (7/1), IWN SPY beta (7/9) and value's beta on SPY (7/9). Small caps' beta on SPY fell to about 0 in Q3 2026. Several unrelated sectors breaking at the same time points to a **market-wide change in June–July 2026**, not a regional-bank event.
5. **Aug–Oct 2026 — deepening.** KRE's RSP beta goes below p10 (8/18). Value's beta on SPY reaches −0.85 by 10/30.

So the relationships did **not** change together. The market moved first (2025), the bank-specific residual split was strongest in 2025, and the KRE beta collapse came in June 2026 alongside other sectors.

---

# 7. Link to study 3 (rate-beta flip)

### Table 7 — Δ10y sensitivity, controlling for SPY (63d)
{{T_RATE}}

The negative rate sensitivity is shared by the value factor (record low) and by small value (IWN) at almost exactly KRE's level. KRE's own yield loading is normal once style factors are in the model (Table 2b). Study 3's flip is best read as "value and small-cap stocks now fall when yields rise," with KRE inheriting it.

---

# 8. Evidence against each explanation (summary)

* **Market structure:**
  * It does not by itself time the June 2026 onset. Value's negative co-movement was deep in mid/late 2024 and 2025 without a KRE beta collapse; the timing needed the size offset to disappear.
  * KRE is still lowish against equal-weight and small value on correlation (6th / 4th pct raw).
  * The ETF proxies for October HML and MOM are imperfect (correlation with French 0.80 / 0.68).
* **KBWB moved:**
  * This is inferred from loadings, not holdings.
  * It cannot explain KRE's own decline against RSP and IWN.
  * KBWB's residual volatility and out-of-sample fit also deteriorated, so "KBWB became a market proxy" is incomplete.
* **Low volatility:**
  * It explains the correlations only partly, and not the betas or R².
* **Rates:**
  * Not regional-specific: value, IWN and XLF share it.
  * Adds only about 0.03 out-of-sample R².
* **Regional-bank repricing:**
  * KRE's residual volatility is normal and less elevated than nonbank cyclicals'.
  * Its factor breakdown is shared.
  * Its alpha is no worse than KBWB's.
  * What supports it: a residual KRE–KBWB correlation at the 14th pct, a last-21-day drop in KRE's value loading (4th pct), and the unique 10/22 behaviour (study 3). These are modest and short-window.

---

# 9. The single most useful next test

**A frozen-loading forecast for the next non-overlapping 63 sessions (11/2/2026 → about 2/2/2027).**

1. **Freeze KRE's current 5-factor loadings:** Mkt 1.09, SMB 0.66, HML 0.98, MOM 0.12, Δ10y 0.024.
2. **At the end of the next window, compute each factor's beta on SPY over that window.** Predict KRE's SPY beta as Σ loading × factor beta.
3. **Compare with the realized beta.**

**Calibration.** On 49 non-overlapping windows from 2012–2024, this forecast's error had a standard deviation of 0.27 (10th / 90th percentiles −0.29 / +0.38). A naive "beta stays the same" forecast had 0.55.

**Decision rule**

* **Market structure:** KRE's SPY beta moves with the prediction, for example recovering if value's and small caps' co-movement with SPY normalizes.
* **Regional-bank-specific repricing:** realized beta falls below the prediction by more than 0.29 while the factor structure normalizes. The same rule applied to KBWB (error sd 0.22) separates "KBWB changed" from "KRE changed".

**Why this one.** It is cheap, reproducible from the scripts here, set before the outcome is known, and it directly tests the claim that the structure terms in Table 3b predicted the beta change. That claim was tested twice. For 5/1 → 8/3 it predicted 0.49 (naive 0.84; realized 0.30), getting most of the drop. For 8/3 → 10/30 it predicted −0.10 against a realized 0.33. That error (+0.43) is beyond the historical 90th percentile, in the direction of KRE being *more* tied to the market than structure implied. So the method is informative but noisy in this regime. That is another reason to pre-register it now rather than fit it after the fact.

---

# 10. Confidence & gaps

* **Confidence:**
  * The beta collapse being market-structural: **medium–high**. The decomposition is an identity given the factors; the out-of-sample timing check passed once; the cross-sector evidence is broad.
  * The correlation drop being mostly factor-variance-driven: **medium.**
  * A modest regional/large-bank residual split existing: **low–medium.** It sits at the 14th–30th pct depending on volatility matching and factor source.
* **Gaps:**
  * French factors end 9/30. October uses proxies, and the HML/MOM proxies are imperfect, although the pure-French 9/30 window gives the same picture.
  * This is association, not causation. "Mega-cap/AI leadership" is my label for the observed SPY-vs-RSP/value split. I did not test what drove that split.
  * The size/value factors are broad: they do not separate "bank" from "value" by construction. A characteristic-matched non-bank portfolio (holdings-level) would be a stronger control, but was not built.
  * KBWB's loading shift is inferred, not decomposed by holdings.
  * Thin out-of-sample samples: 2026 periods have 5 blocks each.
  * The 2025 bank-specific residual episode was not investigated for causes.

# Appendix — Files

| File | Content |
|---|---|
| `SPEC.md` | pre-registered spec + change log |
| `build.py` | builds `data/panel.csv` from Yahoo JSON, French CSVs, study-3 Treasury/BAA master |
| `q124.py` | benchmarks (Q1), sector beta collapses (Q2), rolling series, 21d blocks → `out/q1_*.csv`, `out/q2_sectors.csv`, `out/rolling_63.csv`, `out/blocks21.csv`, `out/onsets.csv` |
| `q3.py` | factor models M0–M4/E1–E2 over 21/63/126 → `out/q3_exposures.csv`, `out/q3_unexplained.csv`, `out/q3_volmatched.csv`, `out/q3_oos*.csv`, `out/q3_rolling63.csv` |
| `q3b.py` | beta and correlation decompositions; sector R²/OOS → `out/q3b_*.csv` |
| `q3c.py` | rate beta of value factor; alphas → `out/q3c_*.csv` |
| `q4.py`, `q4b.py` | timing → `out/q4_*.csv`, `out/q4b_rolling_beta_terms.csv`, `out/fig_timeline.png` |
| `q5_nexttest.py` | frozen-loading test calibration → `out/q5_frozen_loading_test.csv` |
| `make_report.py` | fills `REPORT_template.md` → `REPORT.md` |

**Sources**

* Kenneth R. French Data Library: daily F-F Research Data Factors and Momentum Factor, files built from CRSP 202609 (`https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip`, `…/F-F_Momentum_Factor_daily_CSV.zip`).
* US Treasury daily par yield curve.
* FRED BAA10Y.
* Yahoo Finance chart API: adjusted closes, the only non-primary source, used for ETF prices.
