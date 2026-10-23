# KRE / QQQ — the transition signature into a joint decline

**HENRY (equity market structure) · written 2026-10-23 14:34 EDT (`date`) · PROME-spawned, Will-directed, read-only research.** No card, no gate, no threshold, $0 moved. Will's question (10/23 14:26 ET): *both QQQ and KRE eventually go down, maybe see-sawing on the way; what do the relationship and its patterns teach us?*

**Data, one caveat stated once:** yfinance auto-adjusted daily closes (KRE, QQQ, ^TNX, ^VIX), pulled 2026-10-23 14:32 EDT. These are vendor closes, not exchange-official. Definitive closes run to **2026-10-22**; the 10/23 bar was intraday at pull time and is scored separately as PROVISIONAL. HY OAS = FRED BAMLH0A0HYM2. FRED now serves only 2023-10-24 onward for it, so the history is VIOLET's frozen archived FRED pull (1996-12-31 → 2026-04-09, `AGENTS/VIOLET/workbook/hy_oas_fred.csv`) joined to the live FRED series. The two agree exactly on all 645 overlapping days (`build.py` stops the run if they ever disagree). Cross-checks on every day 0: FRED DGS10 vs ^TNX max gap 0.028 points; FRED VIXCLS vs ^VIX max gap 0.000. Every figure below comes from `build.py` stdout or `episodes.csv` in this folder.

---

## Bottom line (five sentences)

1. **The nine joint declines did not grow out of a see-saw. They started from lockstep.** The 20-day correlation was already a median **+0.57** on the day the decline began (anchor B), ranging **−0.02 to +0.71**. Over the 10 sessions before, it changed by a median **+0.00**. In none of the nine was it negative on day 0.
2. **No measure reliably "moved first."** Each of the six indicators started moving inside the 31-session window about as often as it does in any random 31-session window (Table N): the 10-year **8/9 vs 87%**, VIX **9/9 vs 76%**, the KRE/QQQ ratio **8/9 vs 84%**. Before the snap the typical state was calm: VIX median **14.6** and falling (5-session change **−0.74**), HY OAS flat (**−6bp** over 10 sessions). VIX spiked a median **+2 sessions** after day 0 and credit widened **+6.5 sessions** after. In these nine, credit followed equity; it did not lead.
3. **Today sits outside all nine on the defining measures.** On 10/22 the correlation was **−0.24** (nine-episode minimum −0.02); **80%** of the last 10 sessions had KRE and QQQ moving in opposite directions (maximum in the nine: 60%); QQQ was already **−5.8%** over 10 sessions (in all nine QQQ was near its high, worst −3.5%). Credit and volatility are already moving: HY OAS **3.40%**, up **25bp** in 10 sessions and up **74bp** from 2.66 on 9/21; VIX **19.03**. The one precedent with today's shape is **July 2024**, not one of the nine.
4. **No early-warning read beats chance by a usable margin.** On a random day the chance that a joint ≥10% decline starts within 20 sessions is **10.6%**. The best read, "banks bid while tech is sold" (KRE up ≥4% and QQQ down ≥3% over 10 sessions), fired **18 times** with outcomes known; **3** were followed by a joint decline and **15 were false positives**, a precision of 17% (1.6× chance). Chance alone would produce 3 or more hits about **30%** of the time. The rule was also picked after seeing the episodes. **It fired again at the 10/22 close.**
5. **For a two-sided book:** this refutes the timing half of "harvest the see-saw, hold the lockstep" and partly confirms the shape half (§ What this means).

---

## Method (fixed before results; one post-hoc block is labelled)

| Item | Definition |
|---|---|
| Qualifying day t | KRE **and** QQQ close-to-close return from t to t+60 sessions both ≤ −10% |
| Episode | First qualifying day after a gap of more than 60 sessions. **This reproduces PROME's nine exactly:** 2007-10-11, 2008-08-01, 2010-04-05, 2011-05-12, 2015-10-23, 2018-08-24, 2019-12-13, 2022-01-14, 2024-12-12 (189 qualifying days in all) |
| Anchor A | The episode's first qualifying day (PROME's cluster start) |
| **Anchor B ("snap", primary)** | The close of the equal-weight KRE+QQQ basket's high within [A−20, A+40] sessions. **Why:** A can sit weeks before the actual break; 2019-12-13 is 40 sessions before the February 2020 crash. B moves day 0 by −10 to +40 sessions (column "vs A") |
| July 2024 analog | Basket high within the hand-picked window 2024-07-01 → 2024-08-05, giving day 0 = **2024-07-23**. Not a mechanical episode: KRE did not fall 10% |
| Day 0 / before / during | Day 0 = the anchor close. "Before" = days −10..0. "During" (first 10 sessions of the decline) = days +1..+10 |
| c20 | 20-session Pearson correlation of daily % returns |
| Gap / ratio DD | Daily gap = KRE return minus QQQ return, in percentage points. Ratio DD = KRE/QQQ divided by its own 20-session high, minus 1 |
| Event onsets (Table B3) | The first session in −20..+10 where the condition turns true: (a) c20 up ≥0.20 over 5 sessions · (b) ratio DD ≤ −4% · (c) 10-year moves ≥0.15 points over 5 sessions, either direction · (d) VIX up ≥3.0 points over 5 sessions · (e) HY OAS up ≥30bp over 10 sessions · (f) a day both fell ≥1% |
| Signal test (Table S) | Alarm = first firing after 20 quiet sessions. Hit = a qualifying day within the next 20 sessions. Resolved only where 80 forward sessions exist (through 2026-06-30). S1–S8 were declared before looking; S9–S12 are **post-hoc** |

---

## Table B1: returns and the correlation path (anchor B)

| Episode | Day 0 | vs A | KRE −10→0 | QQQ −10→0 | KRE 0→+10 | QQQ 0→+10 | c20 −10 | c20 −5 | c20 0 | c20 +5 | c20 +10 | slope −10→0 | opp-sign pre / in |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 2007-10-11 | 2007-10-09 | -2 | +3.8% | +4.5% | -10.2% | +1.5% | +0.78 | +0.74 | +0.67 | +0.46 | +0.59 | -0.11 | 10% / 40% |
| 2008-08-01 | 2008-09-19 | +34 | +23.1% | -1.2% | -14.9% | -15.7% | +0.58 | +0.55 | +0.69 | +0.63 | +0.61 | +0.11 | 30% / 20% |
| 2010-04-05 | 2010-04-23 | +14 | +7.8% | +3.0% | -13.6% | -10.1% | +0.43 | +0.62 | +0.66 | +0.75 | +0.80 | +0.23 | 20% / 10% |
| 2011-05-12 | 2011-04-28 | -10 | +2.7% | +4.0% | -2.4% | -0.0% | +0.25 | +0.18 | +0.26 | +0.34 | +0.49 | +0.01 | 40% / 20% |
| 2015-10-23 | 2015-11-06 | +10 | +6.5% | +1.8% | -1.8% | -0.3% | +0.57 | +0.67 | +0.57 | +0.62 | +0.60 | +0.00 | 30% / 20% |
| 2018-08-24 | 2018-09-04 | +6 | -0.2% | +3.4% | -3.5% | -1.6% | +0.22 | +0.44 | +0.35 | +0.28 | +0.01 | +0.13 | 60% / 60% |
| 2019-12-13 | 2020-02-12 | +40 | +2.9% | +5.6% | -13.1% | -12.2% | +0.75 | +0.77 | +0.71 | +0.61 | +0.80 | -0.04 | 20% / 50% |
| 2022-01-14 | 2022-01-12 | -2 | +9.0% | -3.5% | -9.0% | -11.9% | +0.61 | +0.49 | +0.35 | +0.40 | +0.42 | -0.26 | 40% / 10% |
| 2024-12-12 | 2024-12-06 | -4 | +0.7% | +4.3% | -8.6% | -1.5% | +0.43 | +0.46 | -0.02 | +0.14 | +0.71 | -0.45 | 40% / 10% |
| 2024-07 analog | 2024-07-23 | +0 | +18.5% | -3.4% | -9.3% | -8.5% | -0.30 | -0.51 | -0.34 | -0.00 | +0.33 | -0.04 | 40% / 40% |

Nine-episode medians (anchor B): c20 **+0.57** at day −10, **+0.57** at day 0, **+0.60** at day +10. Slope −10→0 **+0.00**. Opposite-sign days **30%** before and **20%** during. KRE 0→+10 **−9.0%**, QQQ 0→+10 **−1.6%**: KRE usually fell first and hardest. Anchor A gives the same picture: c20 **+0.48 / +0.53 / +0.55**, with a minimum day-0 c20 of +0.17.

## Table B2: gap, ratio, rates, VIX, HY OAS and the first joint −1% day (anchor B)

| Episode | gap pre (pp/d) | gap in | ratio DD −10 / 0 / +10 | 10y day0 | 10y Δ5 day0 | 10y Δ −10→0 / 0→+10 | VIX day0 | VIX Δ5 day0 / +5 | HY OAS day0 | HY Δ10 day0 / +10 (bp) | first both ≤−1% (offset, date, c20 that day) |
|---|---:|---:|---|---:|---:|---|---:|---|---:|---|---|
| 2007-10-11 | -0.06 | -1.22 | -7.0% / -6.7% / -13.4% | 4.65 | +0.12 | +0.04 / -0.25 | 16.1 | -2.37 / +3.90 | 3.95 | -22 / +39 | +8, 2007-10-19, +0.52 |
| 2008-08-01 | +2.35 | +0.10 | +0.0% / -2.5% / -3.1% | 3.77 | +0.04 | +0.11 / -0.12 | 32.1 | +6.41 / +2.67 | 9.21 | +66 / +303 | -8, 2008-09-09, +0.49 |
| 2010-04-05 | +0.47 | -0.39 | -0.4% / -0.0% / -3.9% | 3.82 | +0.05 | -0.07 / -0.39 | 16.6 | -1.74 / +5.43 | 5.44 | -24 / +103 | -5, 2010-04-16, +0.62 |
| 2011-05-12 | -0.13 | -0.24 | -3.6% / -4.8% / -4.9% | 3.31 | -0.09 | -0.15 / -0.08 | 14.6 | -0.45 / +3.58 | 4.73 | +8 / +4 | none in −10..+10 |
| 2015-10-23 | +0.47 | -0.16 | -6.4% / +0.0% / -2.4% | 2.33 | +0.18 | +0.25 / -0.07 | 14.3 | -0.74 / +5.75 | 5.82 | -15 / +50 | +5, 2015-11-13, +0.62 |
| 2018-08-24 | -0.35 | -0.19 | +0.0% / -4.2% / -6.0% | 2.90 | +0.05 | +0.08 / +0.15 | 13.2 | +1.00 / +0.06 | 3.46 | -6 / -22 | none in −10..+10 (one at −13) |
| 2019-12-13 | -0.26 | -0.11 | -9.9% / -6.9% / -4.6% | 1.63 | -0.02 | +0.04 / -0.33 | 13.7 | -1.41 / +1.82 | 3.59 | -24 / +103 | -8, 2020-01-31, +0.79 |
| 2022-01-14 | +1.23 | +0.33 | -3.2% / -1.5% / -1.5% | 1.73 | +0.02 | +0.18 / +0.08 | 17.6 | -2.11 / +7.97 | 3.06 | +3 / +40 | +3, 2022-01-18, +0.47 |
| 2024-12-12 | -0.35 | -0.74 | -1.3% / -7.0% / -13.8% | 4.15 | -0.03 | -0.28 / +0.37 | 12.8 | -0.74 / +1.04 | 2.67 | +6 / +19 | +8, 2024-12-18, +0.69 |
| 2024-07 analog | +2.07 | -0.07 | -4.3% / +0.0% / -6.7% | 4.24 | +0.07 | -0.06 / -0.35 | 14.7 | +1.53 / +2.97 | 3.02 | -19 / +65 | +1, 2024-07-24, -0.01 |

Nine-episode medians (anchor B): ratio DD at day 0 **−4.2%** (KRE already lagging; 5 of 9 at ≤ −4%) · 10y Δ5 at day 0 **+0.04** · 10y over 0→+10 **−0.08** (it fell in 6 of 9; flight to safety during the decline, not before it) · VIX at day 0 **14.6** (7 of 9 at ≤17.6) · VIX Δ5 at day 0 **−0.74** (7 of 9 at ≤0) · HY Δ10 at day 0 **−6bp** (8 of 9 at ≤ +8bp) and **+40bp** by day +10 · first joint −1% day **+3 sessions**, with c20 that day a median **+0.62** (n = 7). The 2024-07 analog is the only case whose first joint −1% day came at near-zero correlation (−0.01).

## Table B3: which moved first? (session offset vs day 0, anchor B; blank = no onset in −20..+10)

| Episode | a corr jump | b ratio DD | c 10y move | d VIX jump | e OAS jump | f both −1% | first |
|---|---:|---:|---:|---:|---:|---:|---|
| 2007-10-11 | -17 | -12 | -13 | +5 | +8 | +8 | a |
| 2008-08-01 | -1 | +2 | -8 | -11 | -4 | -18 | f |
| 2010-04-05 | -4 | +6 | -8 | +2 | +8 | -5 | c |
| 2011-05-12 |  | -6 | -8 | +5 |  |  | c |
| 2015-10-23 | -8 | -17 | -3 | +4 | +5 | +5 | b |
| 2018-08-24 | -14 | -3 |  | -15 |  | -13 | d |
| 2019-12-13 |  | +9 | -12 | -12 | -12 | -12 | c, d, e, f (tie) |
| 2022-01-14 |  |  | -6 | +3 | +10 | +3 | c |
| 2024-12-12 | +4 | -20 | -6 | -11 |  | +8 | b |
| 2024-07 analog | +1 | -12 | -15 | -3 | +8 | +1 | c |

## Table N: the null check that undoes Table B3

| Event | Episodes with onset in range (B) | Episodes with onset ≤ day 0 (B) | Random-window share, onset in [−20,+10] | Random-window share, onset in [−20,0] |
|---|---|---|---:|---:|
| a corr jump | 6/9 | 5/9 | 53% | 40% |
| b ratio DD | 8/9 | 5/9 | 84% | 70% |
| c 10y move | 8/9 | 8/9 | 87% | 78% |
| d VIX jump | 9/9 | 4/9 | 76% | 63% |
| e OAS jump | 6/9 | 2/9 | 53% | 41% |
| f both −1% | 8/9 | 4/9 | 83% | 72% |

**Read:** the 10-year is "first" in 4 of the nine (5 counting the analog), median −8 sessions. But a 15bp five-session move turns up in 87% of all random windows, so being first is what noise looks like. Only (a) and (e) are rare enough to carry information, and (e), HY OAS, came **before** day 0 in only **2 of 9** (median +6.5 sessions). Anchor A gives the same conclusion: no event leads consistently, and OAS led in 1 of 9. **There is no common pre-snap trigger in these data. There is a common pre-snap state: coupled, calm, KRE lagging, QQQ near its high.**

## Reproducing PROME's first cut

| Claim (PROME, 10/23) | HENRY re-measure, same vendor | Verdict |
|---|---|---|
| Nine clusters (dates as listed) | Same nine dates (rule: 60-session forward return, both ≤ −10%, >60-session gap) | ✅ reproduced |
| c20 +0.67 inside vs +0.52 outside | **+0.67 vs +0.50** | ✅ (the small gap comes from how windows are defined) |
| Opposite-sign days 24% vs 33% | **25% vs 35%** | ✅ |
| Lag-1 cross-correlation ≈ 0 | **−0.09** (KRE today vs QQQ yesterday) / **−0.08** (QQQ today vs KRE yesterday); unchanged excluding 2008–09 (−0.086 / −0.085) | ⚠️ small and negative in both directions: a shared next-day reversal, not a lead. Neither leg leads |
| "Since 9/25: 62% opposite-sign, c20 −0.24 to −0.26" | 20 sessions 9/25→10/22: **65%** opposite-sign; c20 ranged **−0.24 to +0.21** and was ≤0 on **one** session (10/22). −0.258 is the 10/23 provisional intraday value | ❌ the range: TERRY's 13:4x correction stands. The negative regime is **one close old** (10/22) |
| c20 2nd percentile since 2024 | 10/22 **−0.2357** = **2.1st** percentile since 2024 · **2.8th** since 2006 | ✅ for the one close |

---

## Table S: early-warning candidates (full history; outcomes resolvable through 2026-06-30; chance of a hit on a random day **10.6%**)

| Signal | Alarms (resolved) | Hits | False positives | Precision | Lift vs base | Episodes warned (alarm in [B−20, B]) | Pending alarms | Fired 9/25→10/22/2026 |
|---|---:|---:|---:|---:|---:|---|---|---|
| S1 c20 crosses up through 0 after ≤−0.20 in prior 20 | 12 | 1 | 11 | 8% | 0.8× | 0/9 | — | — |
| S2 both ≤−1% day with prior-day c20 ≤ 0 | 9 | 0 | 9 | 0% | 0.0× | 0/9 | — | — |
| S3 both ≤−1% day (any) | 73 | 7 | 66 | 10% | 0.9× | 3/9 | 2026-09-01 | 2026-09-28 |
| S4 VIX Δ5 ≥ +3 and 10y Δ5 ≤ −0.15 | 48 | 4 | 44 | 8% | 0.8× | 2/9 | — | — |
| S5 HY OAS Δ10 ≥ +30bp | 59 | 4 | 55 | 7% | 0.6× | 2/9 | 2026-09-28 | 10 sessions 9/28→10/20 |
| S6 c20 Δ5 ≥ +0.20 and both legs down over 5 sessions | 55 | 4 | 51 | 7% | 0.7× | 1/9 | — | — |
| **S7 ratio DD ≤ −4% and QQQ 5-session ≤ −3%** (best declared in advance) | 40 | 6 | **34** | 15% | 1.4× | 1/9 | 2026-08-24, 2026-10-14 | 2026-10-14 |
| S8 S6 and VIX Δ5 ≥ +3 | 34 | 3 | 31 | 9% | 0.8× | 1/9 | — | — |
| S9 [post-hoc] VIX ≤ 16, ratio DD ≤ −4%, c20 ≥ +0.40 | 44 | 5 | 39 | 11% | 1.1× | 3/9 | 2026-08-25 | — |
| S10 [post-hoc] HY OAS Δ20 ≥ +40bp and VIX ≥ 18 | 41 | 2 | 39 | 5% | 0.5× | 1/9 | 2026-10-16 | 10/16, 10/19, 10/22 |
| S11 [post-hoc] both below 200-day average and c20 ≥ +0.40 | 20 | 3 | 17 | 15% | 1.4× | 0/9 | — | — |
| **S12 [post-hoc] KRE 10-session ≥ +4% while QQQ 10-session ≤ −3%** | **18** | **3** | **15** | **17%** | **1.6×** | 2/9 (2008-09, 2022-01) | 2026-07-07, **2026-10-22** | **2026-10-22** |

**The three S12 hits:** 2008-09-03 (QQQ −14.6% over the next 20 sessions), 2022-01-07 and 2022-02-16. **Its closest miss** is 2024-07-19. It counts as a false positive, yet KRE fell up to −6.9% and QQQ up to −8.5% within 20 sessions (the August 2024 drop); it just never reached −10% on both over 60 sessions. The remaining 14 false positives include rallies such as 2011-10-05 (KRE +14.1% over 20 sessions) and 2020-10-30 (KRE +15.7%, QQQ +11.2%). The alarm list with forward returns is reproducible from `build.py`'s definitions; it was printed in-session.

**Verdict on early warning.** The see-saw-ending reads (S1, S2) are the worst on the table: **1 hit in 21 alarms** combined. The credit read (S5) fires constantly and has a lift below 1. S12 is the best and the most relevant to today, but it has **15 false positives in 18**, it is post-hoc, and chance alone gives 3 or more hits about 30% of the time. Treat it as a description of today's shape with a thin, unproven link to joint declines, not as a trigger.

## Table V: the 10/22 close scored against the nine (anchor B, day 0)

| Measure | Nine: min | median | max | 2024-07 analog | **10/22/2026** | Inside the nine's range? |
|---|---:|---:|---:|---:|---:|---|
| c20 day 0 | −0.022 | +0.567 | +0.706 | −0.339 | **−0.236** | **NO** |
| c20 slope −10→0 | −0.448 | +0.001 | +0.227 | −0.038 | −0.315 | yes |
| ratio DD day 0 | −7.0% | −4.2% | 0.0% | 0.0% | **0.0%** | yes (at the edge: KRE at its relative high) |
| QQQ −10→0 | −3.5% | +3.4% | +5.6% | −3.4% | **−5.8%** | **NO** |
| KRE −10→0 | −0.2% | +3.8% | +23.1% | +18.5% | +4.1% | yes |
| 10y Δ5 | −0.088 | +0.039 | +0.182 | +0.072 | **−0.136** | **NO** |
| 10y Δ −10→0 | −0.281 | +0.037 | +0.250 | −0.061 | −0.278 | yes (at the edge) |
| VIX day 0 | 12.77 | 14.62 | 32.07 | 14.72 | 19.03 | yes (but above 8 of the 9; only 2008-09 higher) |
| VIX Δ5 | −2.37 | −0.74 | +6.41 | +1.53 | +2.57 | yes (but above 8 of the 9; only 2008-09 higher) |
| HY OAS day 0 (%) | 2.67 | 3.95 | 9.21 | 3.02 | 3.40 | yes |
| HY Δ10 (pts) | −0.24 | −0.06 | +0.66 | −0.19 | **+0.25** | yes (2nd highest; only 2008-09 higher) |
| opposite-sign share, last 10 | 10% | 30% | 60% | 40% | **80%** | **NO** |

**Score: 8 of 12 measures inside the nine-episode range. The 4 outside are the defining ones:** the sign of the correlation, the see-saw share, QQQ already falling and the 10-year falling fast. Today does not look like the eve of any of the nine. It looks like **July 2024 with more stress in credit and volatility.** That analog broke into joint selling within 1 session of its basket high (7/24/2024: first joint −1% day, c20 −0.34 → −0.01 in one session) and went 7/31 → 8/5/2024 KRE −10.2% / QQQ −7.6% (TERRY's measure). Then it recovered: over 60 sessions both legs were up (KRE +5.2%, QQQ +4.8% from 7/19/2024).

**PROVISIONAL, 10/23 intraday (yfinance bar at 14:32 EDT):** KRE 72.61 (+0.28%), QQQ 705.86 (+0.20%), 10y 4.988, VIX 19.90. If that holds to the close, c20 = **−0.258**. Same-sign day, small moves; nothing above changes.

**Table C, the last 10 definitive sessions (from `build.py`):**

| Date | KRE d | QQQ d | gap pp | c20 | ratio DD | 10y | VIX | HY OAS | HY Δ10 bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026-10-09 | -0.8% | +0.5% | -1.33 | +0.06 | -12.2% | 5.244 | 14.84 | 3.11 | +18 |
| 2026-10-12 | +0.8% | -0.7% | +1.49 | +0.03 | -10.9% | 5.240 | 15.21 | 3.11 | +9 |
| 2026-10-13 | -0.7% | -0.3% | -0.39 | +0.06 | -9.6% | 5.217 | 15.27 | 3.16 | +8 |
| 2026-10-14 | -0.8% | -2.0% | +1.21 | +0.09 | -6.9% | 5.190 | 16.87 | 3.25 | +13 |
| 2026-10-15 | +1.8% | -0.1% | +1.90 | +0.04 | -4.5% | 5.089 | 16.46 | 3.23 | -1 |
| 2026-10-16 | +0.1% | -2.5% | +2.59 | +0.00 | +0.0% | 5.098 | 19.99 | 3.31 | +21 |
| 2026-10-19 | -0.8% | +1.2% | -1.99 | +0.01 | -2.0% | 5.136 | 18.44 | 3.29 | +17 |
| 2026-10-20 | +2.0% | -0.1% | +2.07 | +0.07 | +0.0% | 5.117 | 17.31 | 3.33 | +30 |
| 2026-10-21 | +0.0% | +1.1% | -1.05 | +0.03 | -1.0% | 5.146 | 16.68 | 3.27 | +18 |
| 2026-10-22 | +2.5% | -2.9% | +5.39 | -0.24 | +0.0% | 4.953 | 19.03 | 3.40 | +25 |

⚠️ HY OAS has widened **+74bp in a month** (2.66 on 9/21 → 3.40 on 10/22, FRED) while KRE rose. The structural-vs-war test in HENRY's charter says it plainly: banks bid on falling yields while credit widens means the rate channel is outrunning the credit channel. That is the relationship to watch. It is not yet a call.

---

## What this means for an active two-sided book (plain language, for Will)

Your book holds bank puts and Nasdaq puts. The idea on the table is to take profits on whichever side is winning while the two see-saw, then hold both once they start falling together. Here is what 20 years of data say about each half.

- **"Hold through the lockstep": confirmed.** When KRE and QQQ really fall together, they move as one. In the first 10 sessions only about 1 day in 5 went opposite ways (median 20%), and correlation stayed near +0.6. Once a joint decline is under way there is little see-saw left to trade, and both legs pay at the same time. KRE usually goes first and hardest (median −9.0% in 10 sessions vs QQQ −1.6%).
- **"Harvest during the see-saw, then switch": the switch has no reliable signal.** None of the nine big joint declines started from a see-saw. Each started from a calm, already-coupled market: low VIX, flat credit, banks lagging, tech near its high. The usual sign that "the see-saw is ending" (correlation turning back up through zero, or the first day both fall 1%) came before a real joint decline **once in 21 tries**. Almost every see-saw since 2006 simply faded back into normal co-movement, and none produced a joint 10% fall (TERRY's episode study: **0 of 13** produced even a joint 5% fall within 40 sessions).
- **The one exception looks like today.** July 2024 had banks ripping, tech falling and yields easing, and it snapped into joint selling within days. KRE fell 10% and QQQ 8% over 7/31 → 8/5/2024, then both recovered within weeks. If today follows that path, the joint-fall payoff is sharp and short. Harvesting it means taking profits during that week, not holding for a long decline.
- **Practical reading.** While the see-saw lasts, each side's gains mostly cancel the other's losses and time decay costs both (TERRY's 13:4x scenario table puts the see-saw case at −$466 by 11/13). Harvesting the winning side when it is up a lot is consistent with the data. Rotating the proceeds back into the losing side is not: since 10/06 the gap between them has been a trend (KRE/QQQ ratio ≈ +11%), not noise that reverts. TERRY constructs any trade; this is a reading of the structure, not a recommendation, and nothing here bears on any expiry.
- **What would change this read.** Credit widening hard while KRE stops rising would be the July-2024-style break, here driven by credit rather than rates. Concretely: HY OAS keeps rising from 3.40% and KRE closes below its 20-session relative high by 4% or more, while QQQ is still falling. Separately, a correlation reading back near +0.5 with a quiet VIX would put the market back into the state the nine joint declines started from. Neither is in place on 10/22.

---

## Limits

| Limit | Effect |
|---|---|
| **n = 9 episodes plus 1 analog** | Every median rests on 7–9 points. One episode moves a median, and no percentage here is stable to ±10 points |
| **Overlap and clustering** | 2007-10 and 2008-08/09 are one crisis. 2019-12 is COVID, a one-day-at-a-time external shock. Arguably 6–7 independent regimes |
| **Selection of the nine** | The ≥10%-in-60-sessions rule is PROME's and was not tuned here. A −7% or 40-session rule would pick a different set; that was not tested. Anchor B was chosen by HENRY to fix anchor A's lag; Tables B1–B3 hold under both anchors (anchor A medians quoted beside each) |
| **Event thresholds** | The (a)–(f) cut-offs were fixed before computing, but they are HENRY's. Table N shows the "first-mover" ranking is noise at these thresholds; other thresholds were not searched, by design |
| **Post-hoc signals** | S9–S12 were written after seeing the episodes. S12's lift is in-sample, and 3 hits in 18 is not distinguishable from 10.6% chance (about 30% probability under chance alone). The alarms are also not independent |
| **Outcome definition** | A "hit" needs a qualifying day within 20 sessions. Firing inside a decline that still has 10% left counts as a hit. Near-misses (2024-07-19) count as false positives |
| **Vendor data** | yfinance auto-adjusted closes, not exchange-official. HY OAS before 2023-10-24 comes from VIOLET's frozen archived FRED file (exact match on 645 overlap days). The ^TNX vs DGS10 gap is ≤0.028 points on every day 0 |
| **Current regime is young** | c20 has been negative for **one** definitive close (10/22). The 10/23 bar is intraday |
| **Credit leads equity (HENRY charter rule H4)** | In these nine, HY OAS widened *after* the equity snap (median +6.5 sessions; before day 0 in only 2 of 9). That cuts against H4 ("credit leads equity by 2–3 sessions"). It is recorded here for HENRY's next writing session; no rule was changed in this read-only session |

## Files

- `REPORT.md` (this file) · `episodes.csv`: 19 rows, nine episodes × anchors A and B plus the 2024-07 analog (B only), every column above plus cross-checks · `build.py`: the full computation. Run from the repository root: `.venv/bin/python PROME/reports/2026-10-23_kre-qqq-transition-signature/build.py [--cache DIR]`. It pulls live, so a later run will extend the series past 10/22. The pulls used here sit in HENRY's session scratchpad and are not committed.
- Inputs read: `AGENTS/TERRY/research/2026-10-23_KRE-QQQ-relationship.md`, `AGENTS/TERRY/research/2026-10-23_KRE-QQQ-report/` (REPORT.md, FINDINGS_2026-10-23_pm.md). No STATUS-file level is cited as current.
