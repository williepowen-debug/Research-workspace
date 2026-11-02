# KRE prospective evaluation: pre-registration (DRAFT, awaiting Will's approval)

**Status:** proposal only. Not registered, not scheduled, no agents contacted, no repository changes. Operational use requires Will's approval.
**Information cutoff:** 10/30/2026 close. **Drafted:** 11/02/2026 (Nisaba, session 14).
**Frozen resolver:** `resolver.py`, sha256 `b98e22f29d3f49a7bd9add75021ba4621d139e49d4d1ba707861eaf45dc9fae3`. It reproduces the reference-window values exactly (corr 0.7193, vol 0.1561, beta 0.3275, rate beta −0.0620).

### 0. Leakage disclosure (read first)
- All base rates and thresholds below use data through 10/30 only.
- **Exception:** in the earlier study-6 data pull (before this brief existed), the drafter saw near-close prices for **11/02/2026, session 1 of the evaluation window**: KRE 73.73 (+2.4%), KBWB 89.60 (+1.3%).
- The thresholds come from the brief and from earlier studies, so they were not affected. The proposed probabilities could in principle have been nudged by one of the 63 days.
- **Rule for the approver:** if you have viewed post-10/30 KRE/KBWB/SPY data before approving, record that next to the approval and mark the registration "late". It can still be scored.

## 1. Window
- **Evaluation window E:** the first 63 completed NYSE sessions after the 10/30/2026 close.
  - Scheduled dates: **Mon 11/02/2026 → Tue 02/02/2027.**
  - Session 21 = 12/01/2026, session 42 = 12/31/2026.
  - Full closures excluded: 11/26, 12/25, 1/1, 1/18 (NYSE calendar). The early closes on 11/27 and 12/24 count as sessions.
- **Unscheduled closures:** the window becomes the first 63 *actual* sessions, and the end date moves later.
- **Resolution date:** on or after **Wed 02/03/2027**. Target completion by 02/05/2027.
- E does not overlap the reference window (8/4–10/30). E is one independent observation, so the result is n = 1.

## 2. Data definitions (fixed)
1. **Returns:** daily simple returns from adjusted closes (dividends and splits) for KRE, KBWB, SPY and IWM, with base = the 10/30 close. Exactly 63 returns.
   - Primary source: Yahoo Finance v8 `adjclose`.
   - Fallback source: exchange closing prices plus issuer-published distributions.
2. **Correlation:** Pearson correlation of the 63 KRE and KBWB daily returns.
3. **Volatility:** sample standard deviation (ddof = 1) of KRE daily returns × √252.
4. **Market beta:** cov(KRE, SPY) / var(SPY) on daily returns, univariate.
5. **Rate beta:** OLS fit of r_KRE = a + b_m·r_SPY + b_rate·Δy10.
   - Δy10 = daily change in the U.S. Treasury Daily Par Yield Curve 10-year rate, in percentage points.
   - On bond-market holidays when stocks trade (e.g. Veterans Day, 11/11/2026), carry the prior yield forward.
6. **Missing data:**
   - If a close is missing from both sources, drop that session for all series. The next session's return then spans both days.
   - More than 3 dropped sessions → **VOID_DATA.**
   - If KRE or KBWB is delisted, merged, or switches benchmark index → **VOID.**
7. **Comparisons** use full precision and the inequalities exactly as written.
   - Values within the near-threshold band (corr ±0.005, vol ±0.002, beta ±0.02, rate beta ±0.005) are **flagged**, and the fallback source is cross-checked.
   - The resolution still uses the primary source.

## 3. Primary claims (3), base rates, proposed probabilities

**Base-rate method.** For every day *t* from 2006 to 2026 whose trailing 63-session state matches the condition, take the outcome over the next non-overlapping 63 sessions.
- KBWB returns are used from its launch; before 11/2011 the KBW Bank Index (BKX) stands in (daily corr 0.995 on the overlap).
- The days overlap, so "episodes" (clusters of days) are the real sample size.
- References since 2012: corr median 0.940, 10th pct 0.863; KRE vol median 23%, below 20% on only 28% of days; beta 10th pct 0.78, median 1.10.

### C1. Correlation: persistence vs calm vs stress normalization
Outcome categories over E:
- **persist:** corr ≤ 0.863
- **calm_norm:** corr > 0.863 and vol < 0.20
- **stress_norm:** corr > 0.863 and vol ≥ 0.20

| Conditioning state at t | episodes | persist | calm_norm | stress_norm |
|---|---|---|---|---|
| All days | — | 0.17 | 0.20 | 0.63 |
| corr < 0.863 (day-weighted) | 13 | 0.36 | 0.17 | 0.46 |
| corr < 0.863 (episode-weighted) | 13 | 0.22 | 0.22 | 0.56 |
| corr < 0.80 | 6 | 0.42 | 0.22 | 0.36 |
| corr < 0.863 and vol < 0.20 | 9 | 0.12 | 0.42 | 0.46 |
| Current episode only (Jun–Aug 2026 start dates) | 1 | 1.00 | 0 | 0 |
| **Proposed** | | **0.50** | **0.20** | **0.30** |

**Why the proposal departs from the long-run rate.**
- Of 13 historical episodes, the 2026 one is the only one that has not normalized so far.
- The current correlation, 0.72, is about 2.3 standard errors below the threshold.
- The drivers identified in study 6 (market-beta collapse since H1-2026, a bank-wide factor shift) were still present at the cutoff.
- Even so, long history says normalization is more likely than not, which is why persist is held at 0.50 rather than higher.

### C2. Market-beta recovery: KRE beta to SPY over E ≥ 0.80

| State | episodes | P(beta ≥ 0.80) |
|---|---|---|
| All days | — | 0.91 |
| beta < 0.5 | 3 (2018, 2024, 2026) | 0.32 day-weighted / 0.50 episode-weighted |
| beta < 0.6 | 5 | 0.39 / 0.64 |
| corr < 0.863 and beta < 0.6 | 3 | 0.20 / 0.41 |
| **Proposed** | | **0.35** |

### C3. Rate regime: KRE rate beta over E
Outcome categories: **neg** < −0.03 · **zero** in [−0.03, +0.03] · **pos** > +0.03. (Current value −0.062, standard error 0.023, so the band is about ±1.3 SE and classification is noisy.)

| State | episodes | neg | zero | pos |
|---|---|---|---|---|
| All days | — | 0.11 | 0.32 | 0.57 |
| rate beta < −0.03, 2006–2026 | 13 | 0.25 | 0.47 | 0.28 |
| rate beta < −0.03, since 2012 | 6 | 0.39 | 0.27 | 0.34 |
| Closest analog (9/2023–7/2024) | 1 | 0.54 | — | — |
| **Proposed** | | **0.40** | **0.35** | **0.25** |

**Scoring.**
- Multi-category Brier score for C1 and C3, binary Brier for C2.
- Each is compared against the **day-weighted conditional base rate**, which is the stated reference forecast:
  - C1: 0.36 / 0.17 / 0.46
  - C2: 0.32
  - C3: 0.25 / 0.47 / 0.28
- One window cannot validate a forecaster. The scores are recorded for the ledger only.

## 4. Descriptive only (no prediction, no score)
- **Relative performance:** KRE − KBWB and KRE − IWM total return over E, reported separately from C1–C3. Historical 63-day KRE − KBWB standard deviation is about 6.9pp (KRE ahead 47% of the time). Study 6 showed that a gap of this size is noise-level, so it is **not** evidence for any hypothesis.
- **Optional interim readings** at sessions 21 and 42 (12/01, 12/31). These are descriptive only and **never** an early resolution.
- **Optional diagnostics** (from study 6): KRE correlation with the EW basket of traditional large banks; bank-stock beta to HY OAS changes.

## 5. How outcomes map to the competing interpretations

| Outcome over E | "Temporary shock" (large-bank/yield shocks) | "Regime" (changed pricing of regional-bank risk) |
|---|---|---|
| calm_norm **and** C2 = YES | **Supported** | Weakened |
| calm_norm, C2 = NO | Partly supported | Unresolved (correlation back, beta still low) |
| stress_norm | **Unresolved.** Correlations rise mechanically when volatility spikes. Leans "temporary" only if C2 = YES as well | Not refuted |
| persist, vol < 0.20, C2 = NO | Weakened | **Supported** |
| persist, vol ≥ 0.20 | Weakened | Supported (decoupling survives stress), but a different regime from the calm one |

- **C3** reads separately. "neg" means the **bank-wide** inverse-yield regime is still active; that bears on the rate-relief channel, not on decoupling itself.
- C1 = persist together with C3 = zero/pos would further weaken the idea that the decoupling is rate-driven (Hypothesis A).

## 6. Freeze rules
- Thresholds, definitions and categories are fixed now.
- Probabilities may be changed only by Will at approval, and only if he has not viewed post-10/30 data. Otherwise the drafted values stand.
- No edits after approval. Any departure from protocol is logged, not silently applied.
- The resolver is run unchanged (hash above). If a bug is found, the fix and its effect are logged and both outputs are reported.

## 7. Known weaknesses
- The thresholds were chosen in-sample, on the same series that motivated the study.
- Base rates rest on 13 overlapping episodes at most. The current regime has 1–2 episodes, which matter most and are the weakest evidence.
- Yahoo `adjclose` can be revised after a dividend. Resolution uses the snapshot taken at resolution, and the data hash is recorded.
- n = 1: the outcome can support or weaken an interpretation but cannot establish it.
