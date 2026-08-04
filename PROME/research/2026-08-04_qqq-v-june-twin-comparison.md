# QQQ V-recovery twin comparison — 2026-06-15 (FAILED) vs 2026-08-04 (LIVE)

**Date:** 2026-08-04 · **Author:** PROME subagent (sonnet), Will-requested · **Data pull timestamps:** yfinance (QQQ/^GSPC/RSP/^VIX daily bars, `.venv/bin/python3` + `yfinance` 1.4.1) pulled **2026-08-04 18:18-18:22 UTC (~14:18-14:22 ET)**; FRED `BAMLH0A0HYM2` (HY OAS) pulled via direct HTTPS to `api.stlouisfed.org` at the same session, key from `FORGE/tools/market-data/.env`.

⚠️ **8/4 is a live trading day — the 8/4 row is an intraday snapshot at pull time (~14:20 ET, market closes 16:00 ET), not a settled close.** QQQ printed 723.41 at pull time vs the ~722.67 cited in the same-day base-rate memo (`PROME/research/2026-08-04_qqq-v-recovery-base-rate.md`, pulled earlier) — the ~$0.75 difference is intraday drift between two pulls, not a data error. Re-verify at/after the 16:00 ET close if this memo is cited after today.

## Methodology (stated once, applied identically to both episodes)

- **Signal date** = the date given (2026-06-15, 2026-08-04); both are actual NYSE trading days (no substitution needed).
- **3-session close return into signal** = `close[t] / close[t-3 trading days] − 1`.
- **Trough** = the minimum close in the 15 trading days *preceding* the 3-session rally window (i.e., ending at `t-3`, excluding the rally itself) — the local V-bottom by close.
- **Pre-drawdown 252d high** = the max close in the 252 trading days ending at the trough date — the high the market was actually falling *from*. (Distinct from "252d high as of signal date," which — for SPX/RSP in both episodes — has already been re-set by the recovery itself; anchoring drawdown depth to a post-recovery high would tautologically read 0%, so the two highs are computed separately and both reported.)
- **Distance vs 252d high at signal** = `close[t] / (252d high as of t) − 1`.
- **Fresh 3-month high** = is `close[t]` the max close of the trailing 63 trading days (yes/no), with the actual level+date reported.
- **Realized vol** = stdev of daily log returns × √252, annualized, close-to-close.
- **HY OAS "as of" a signal date** = the latest FRED observation dated on-or-before that date (per the guard in the task spec).

## Two-column comparison

| Metric | **2026-06-15 V (FAILED)** | **2026-08-04 V (LIVE)** |
|---|---|---|
| **1. QQQ price action** | | |
| 3-session close return into signal | **+7.25%** (693.69 [6/10] → 744.00 [6/15]) | **+5.83%** (683.55 [7/30] → 723.41 [8/4, intraday]) |
| Trough (close basis) | 693.69 on **6/10** | 661.73 on **7/29** |
| Pre-drawdown 252d high (anchor) | 746.16 on **6/2** | 746.16 on **6/2** (same anchor — no new 252d high since) |
| Drawdown at trough vs pre-drawdown high | **−7.03%** | **−11.32%** |
| Signal-close distance vs 252d high (as of signal) | **−0.29%** (746.16, 6/2) | **−3.05%** (746.16, 6/2) |
| **2. Breadth / leadership** | | |
| SPX 3-session return | +3.95% (7266.99 [6/10] → 7554.29 [6/15]) | +4.13% (7437.63 [7/30] → 7744.81 [8/4]) |
| SPX drawdown at trough | trough 7266.99 [6/10] vs pre-drawdown hi 7609.78 [6/2] = **−4.50%** | trough 7316.15 [7/29] vs pre-drawdown hi 7609.78 [6/2] = **−3.86%** |
| SPX distance vs 252d high at signal | **−0.73%** (7609.78, 6/2) | **0.00%** — signal close (7744.81) IS the 252d high |
| SPX fresh 3-month (63td) high? | **NO** (63td hi 7609.78 on 6/2; signal close −0.73% below) | **YES** (7744.81 = the 63td high) |
| RSP 3-session return | +3.07% (206.53 [6/10] → 212.88 [6/15]) | +2.13% (215.38 [7/30] → 219.96 [8/4]) |
| RSP drawdown at trough | trough 201.62 [5/19] vs pre-drawdown hi 204.97 [2/27] = **−1.63%** | trough 211.92 [7/23] vs pre-drawdown hi 215.06 [7/16] = **−1.46%** |
| RSP distance vs 252d high at signal | **0.00%** — signal close (212.88) IS the 252d high | **0.00%** — signal close (219.96) IS the 252d high |
| RSP fresh 3-month (63td) high? | **YES** (212.88 = the 63td high) | **YES** (219.96 = the 63td high) |
| QQQ−RSP 20-trading-day relative return into signal | QQQ +4.95% / RSP +5.62% → **−0.67pp** (QQQ lagged) | QQQ +1.97% / RSP +2.44% → **−0.46pp** (QQQ lagged) |
| **3. Vol** | | |
| VIX level at signal | **16.20** | **16.56** |
| VIX 5-session change | **−2.72** (18.92 [6/8] → 16.20 [6/15]) | **−1.65** (18.21 [7/28] → 16.56 [8/4]) |
| SPX realized vol, 5d (annualized) | **22.31%** | **22.10%** |
| SPX realized vol, 10d (annualized) | **21.59%** | **18.19%** |
| Implied − realized gap (VIX − RV5d) | **−6.11** | **−5.54** |
| **4. Volume** | | |
| QQQ mean daily volume, 3 rally sessions | 56,559,167 (6/11, 6/12, 6/15) | 45,549,229 (7/31, 8/3, 8/4) |
| QQQ mean daily volume, preceding 4 selloff sessions | 76,068,650 (6/5, 6/8, 6/9, 6/10) | 54,516,800 (7/27, 7/28, 7/29, 7/30) |
| Rally-vs-selloff volume ratio | **0.74×** | **0.84×** |
| **5. Credit (HY OAS, FRED BAMLH0A0HYM2)** | | |
| Level as of signal date | **266bps [6/15]** | **285bps [7/31, 4d stale — no 8/1-8/4 print published]** |
| 10-trading-day change | **−6bps** (272bps [6/1] → 266bps [6/15]) | **+12bps** (273bps [7/17] → 285bps [7/31]) |
| **6. Driver (one line, repo-cited)** | | |
| | Contested Iran/Gulf de-escalation: ceasefire announced but unsigned — WALTER's 6/16 repair re-stamped the Iran anchor to **"DE-ESCALATION PENDING / unsigned MOU / fragile truce"** (`memory/2026-06-16.md:102`); ORC's 6/16 NEXUS read: **"ceasefire announcement ≠ verified reopening"** (`memory/2026-06-16.md:91`); PROME's 6/15 BRENT heartbeat: tape priced reopen/de-escalation **faster than physical repair was confirmed** (`memory/2026-06-15.md:44-45`). | Contested Iran de-escalation headline (8/2) Tehran denied on the record ~18:30 ET, tape did not give it back — read as pricing "the pause," not an agreement (`PROME/HANDOFF.md`, 8/2 Night Addendum entry) + **confirmed** coordinated US-Japan FX intervention, Bessent 7:00 PM 8/2, first since 2011 (`PROME/HANDOFF.md`, same entry; also `PROME/SCRATCH.md`). |

## Where they differ materially

**Measurement (numbers only, no interpretation):**

1. **QQQ drawdown depth: −7.0% (June) vs −11.3% (Aug) — a ~1.6× factor.** The Aug V is recovering from a meaningfully deeper hole.
2. **QQQ distance from the 252d high at signal close: −0.3% (June) vs −3.1% (Aug) — a ~10× factor.** June's V had almost fully recaptured the old high by the signal date; Aug's V, despite a comparable 3-session rally size, remains well short.
3. **SPX fresh-3-month-high status flips: NO (June, −0.73% below) → YES (Aug, at the high).** A binary breadth-confirmation difference — SPX was still repairing on 6/15; SPX is at a fresh high on 8/4.
4. **HY OAS 10-day change flips sign: −6bps (June, compressing) vs +12bps (Aug, widening) — with the Aug level itself 19bps wider (285 vs 266) even before direction.** ⚠️ The Aug figure is **[7/31, 4d stale]** — no FRED print for 8/1-8/4 exists as of this pull; treat the direction as the last-confirmed trend into the episode, not a live read of credit today.
5. **SPX RV10d: 21.59% (June) vs 18.19% (Aug) — Aug's 10-day realized-vol window ran ~16% calmer.**

**Not materially different by measurement:** RSP drawdown depth (−1.6% vs −1.5%), RSP breadth (fresh high in both), QQQ-RSP 20td relative return (−0.67pp vs −0.46pp, same sign/order of magnitude), VIX level (16.20 vs 16.56) and IV-RV gap (−6.11 vs −5.54), QQQ rally-vs-selloff volume ratio (0.74× vs 0.84×, both show fading rally volume).

**JUDGMENT** *(clearly separated from the measurements above — this is interpretation, not computed fact):* The credit divergence (#4) is the most economically loaded difference if it holds up past the staleness gap, because it's the one metric where the two episodes point in *opposite* directions rather than just different magnitudes of the same direction — June's V rallied into compressing credit (a supportive underlying condition that the June memo's own driver citations show matched the "reopening priced faster than physical repair" story cooling off), while Aug's V is rallying into the last-confirmed credit trend still widening. That said, #1-#3 (QQQ falling further, recapturing less, while SPX/RSP both already made fresh highs) read, on their face, as a *broader* breadth base under the Aug bounce than June had (SPX confirming, not lagging) even though QQQ itself is in a deeper, less-recovered hole — which is a genuinely mixed signal, not a clean "better" or "worse" setup than June's failed one. Two episodes cannot statistically discriminate which factor dominates; this paragraph is a read, not a conclusion.

## Caveats

- **n=2 decides nothing alone.** This is a twin-episode comparison, not a base rate. The already-published base-rate memo (`PROME/research/2026-08-04_qqq-v-recovery-base-rate.md`) situates both inside a 19-episode "true analogue" cohort (14/18 resolved positive at 1m and 3m) — read this memo alongside that one, not instead of it.
- **HY OAS for the Aug signal is [7/31, 4d stale]** — 8/1 (Sat), 8/2 (Sun) are non-trading; 8/3 and 8/4 have no published print as of this pull. The +12bps 10-day change and the 285bps level are both last-confirmed-as-of-7/31 reads, not live 8/4 credit conditions. Per `PROME/SCRATCH.md`, this is a known open item (3-8/4 decides several other agents' pending gates too).
- **8/4 QQQ/SPX/RSP/VIX values are intraday, not settled closes** (pulled ~14:20 ET, market closes 16:00 ET). All Aug-4 cells should be re-verified against the actual close if this memo is cited after today's session ends.
- **Trough-window methodology is a stated convention (15 trading days pre-rally), not a universal standard.** A different lookback could shift the exact trough date/level by a few sessions, though the deep vs shallow *pattern* (QQQ trough ≫ SPX/RSP trough in both episodes) is robust to reasonable window choices — spot-checked by eye against the daily closes.
- **Driver citations are qualitative, not measured.** Section 6 is repo-sourced narrative (memory files, HANDOFF), included per the task spec, but it is not a computed statistic like sections 1-5.
- No number in this memo was estimated or backfilled — every FRED/yfinance series pulled cleanly for both dates; nothing was left UNAVAILABLE.
