# Feb 2018 Volmageddon M1:M2 Analog

**Date:** 2026-06-01 (evening session)
**Author:** VIOLET
**Script:** `scripts/feb2018_m1m2.py` (re-runnable)
**Data:** `workbook/FEB2018_VOLMAGEDDON_M1M2.csv` (37 rows, 2018-01-02 → 2018-02-23)
**Source:** CBOE archive `cdn.cboe.com/resources/futures/archive/volume-and-price/CFE_<CODE>_VX.csv` — F18 (Jan), G18 (Feb), H18 (Mar), J18 (Apr) per-contract settlement series

Closes **Priority 1 piece (c)** — Feb 2018 M1:M2 Volmageddon analog comparison.

---

## TL;DR

- **The "13% contango" framing of KB-VIO-064 is partially supported but materially refined by the Feb 2018 analog.** Yes, +11-12% M1:M2 contango readings DID occur in Jan 2018 — but during the F18-as-M1 phase at dte=12-15, NOT immediately before the Feb 5 spike. The immediate pre-spike contango was **+1% to -4%**, not +13%.
- **The Volmageddon spike happened with FLAT-to-INVERTED contango, not pile-up contango.** Trajectory Feb 2018: contango compressed from +12% (Jan 5) → +5% (Jan 18 G18 roll) → +1% (Jan 30) → -4% (Feb 2) → -16% (Feb 5 spike day) → -25% (Feb 9 trough).
- **CRITICAL CALIBRATION for KB-VIO-064 falsifiable trigger:** the original "M1:M2 ≤8% by 6/10 = trap releasing → downgrade" framing is **incorrect-by-itself**. In Feb 2018, compression of contango was the pre-spike trajectory, not the dis-confirming signal. The DISAMBIGUATING variable is **direction of spot VIX during compression**: rising VIX + compressing contango = pre-spike; falling VIX + compressing contango = bona fide trap-releasing.
- **Current setup (5/15 → 6/1) is in the EARLIEST analogous phase**: M1:M2 +12.93% with M1 dte=12 mirrors Jan 5 2018 (F18 +11.93%, dte=12, VIX=9.22 at absolute regime low). If the analog holds, the trajectory now would be: 3-4 weeks of compression alongside RISING VIX, then sharp inversion + snap, hitting the 6/12-6/26 window — exactly where the 6/17 FOMC + SEP + VIX-Jun-quarterly gate sits.
- **Or the analog DOESN'T hold** — current regime is GEX-suppressed, SKEW-rebid, gradual-fade, with the contango pile-up reflecting Jun-event-hedger-bid on M2 rather than F18-style structural pre-spike vol pricing. Disambiguation: watch whether contango compresses with VIX rising (analog active) or with VIX falling (analog fails).
- **The 6/05 COT release** retains its disambiguation status (KB-VIO-065) and now layers with the VIX-direction disambiguation.

---

## Why this analog matters

KB-VIO-064 made a strong shape claim about the current 5/15→6/1 M1:M2 contango explosion (+5.66% → +13.40%): "Volmageddon 2018 setup shape (Feb 2018 M1:M2 was similarly steep before the short-vol unwind)." That claim needed historical grounding. This study provides it.

The result is more nuanced than the claim. Yes, Feb 2018 had ~12% M1:M2 readings. But the immediate-pre-spike structure was already in backwardation, NOT pile-up contango. The KB-VIO-064 trigger logic was built on the implicit assumption that "Volmageddon was a 13%-contango pile-up that snapped" — actually Volmageddon was "13% contango (Jan) → flat (Jan 30) → backwardation (Feb 2) → spike (Feb 5)." The pile-up didn't snap; the COMPRESSION snapped.

---

## Methodology

### Data source
CBOE futures historical archive (per-contract daily settles):
- `CFE_F18_VX.csv` — Jan 2018 expiry (Wed 1/17), 186 rows
- `CFE_G18_VX.csv` — Feb 2018 expiry (Wed 2/14), 186 rows  ←  the Volmageddon M1
- `CFE_H18_VX.csv` — Mar 2018 expiry (Wed 3/21), 168 rows
- `CFE_J18_VX.csv` — Apr 2018 expiry (Wed 4/18), 149 rows

### M1:M2 rule
For each trade date `d`, M1 = nearest non-expired contract on `d`; M2 = next-nearest. Contango = `(M2_settle - M1_settle) / M1_settle * 100`.

### Window
Jan 2 → Feb 23 2018 (37 trade dates), centered on the Feb 5 Volmageddon spike.

### Spot VIX context
From `research/crisis_analogs/feb2018_vix_spike.csv` (existing daily VIX/VIX3M/VVIX/SKEW data).

---

## Full daily series

| Trade Date | M1 (dte) | M1 settle | M2 | M2 settle | Contango | Spot VIX | VIX3M/VIX | Phase |
|---|---|---|---|---|---|---|---|---|
| 2018-01-02 | F18 (15) | 10.88 | G18 | 11.97 | **+10.11%** | 9.77 | 1.291 | F18-as-M1 plateau |
| 2018-01-03 | F18 (14) | 10.68 | G18 | 11.82 | +10.77% | 9.15 | 1.346 | |
| 2018-01-04 | F18 (13) | 10.57 | G18 | 11.82 | +11.82% | 9.22 | 1.328 | |
| 2018-01-05 | F18 (12) | 10.47 | G18 | 11.72 | **+11.93%** | 9.22 | 1.308 | **VIX absolute low** |
| 2018-01-08 | F18 (9) | 10.47 | G18 | 11.68 | +11.46% | 9.52 | 1.276 | |
| 2018-01-09 | F18 (8) | 10.68 | G18 | 11.78 | +10.30% | 10.08 | 1.231 | |
| 2018-01-10 | F18 (7) | 10.57 | G18 | 11.57 | +9.46% | 9.82 | 1.259 | |
| 2018-01-11 | F18 (6) | 10.47 | G18 | 11.57 | +10.50% | 9.88 | 1.231 | |
| 2018-01-12 | F18 (5) | 10.57 | G18 | 11.68 | +10.40% | 10.16 | 1.201 | |
| 2018-01-16 | F18 (1) | 11.78 | G18 | 12.07 | +2.55% | 11.66 | 1.135 | F18 expiry approach |
| 2018-01-17 | F18 (0) | 12.61 | G18 | 12.12 | -3.85% | 11.91 | 1.113 | F18 final |
| 2018-01-18 | **G18 (27)** | 12.07 | H18 | 12.78 | **+5.80%** | 12.22 | 1.111 | **G18-as-M1 begins** |
| 2018-01-19 | G18 (26) | 11.93 | H18 | 12.53 | +5.03% | 11.27 | 1.157 | |
| 2018-01-22 | G18 (23) | 11.82 | H18 | 12.47 | +5.50% | 11.03 | 1.178 | |
| 2018-01-23 | G18 (22) | 11.97 | H18 | 12.72 | +6.26% | 11.10 | 1.191 | |
| 2018-01-24 | G18 (21) | 12.22 | H18 | 12.93 | +5.73% | 11.47 | 1.180 | |
| 2018-01-25 | G18 (20) | 12.43 | H18 | 13.03 | +4.83% | 11.58 | 1.181 | |
| 2018-01-26 | G18 (19) | 12.32 | H18 | 13.07 | +6.09% | 11.08 | 1.215 | |
| 2018-01-29 | G18 (16) | 13.53 | H18 | 13.82 | +2.22% | 13.84 | 1.083 | **VIX inflecting up** |
| 2018-01-30 | G18 (15) | 13.97 | H18 | 14.07 | **+0.72%** | 14.79 | 1.070 | **Contango bottoming** |
| 2018-01-31 | G18 (14) | 13.47 | H18 | 13.68 | +1.48% | 13.54 | 1.100 | |
| 2018-02-01 | G18 (13) | 13.28 | H18 | 13.43 | +1.13% | 13.47 | 1.093 | |
| 2018-02-02 | G18 (12) | 15.62 | H18 | 14.97 | **-4.16%** | 17.31 | 0.984 | **First backwardation** |
| 2018-02-05 | G18 (9) | **33.23** | H18 | 27.98 | **-15.80%** | **37.32** (close 30.0) | <0.8 | **🚨 VOLMAGEDDON** |
| 2018-02-06 | G18 (8) | 23.88 | H18 | 21.02 | -11.94% | 29.98 | 0.792 | |
| 2018-02-07 | G18 (7) | 23.43 | H18 | 19.88 | -15.15% | 27.73 | 0.831 | |
| 2018-02-08 | G18 (6) | 28.10 | H18 | 21.65 | -22.95% | 33.46 | 0.817 | Peak VIX close |
| 2018-02-09 | G18 (5) | 27.18 | H18 | 20.43 | **-24.84%** | 29.06 | 0.858 | Backwardation trough |
| 2018-02-12 | G18 (2) | 25.82 | H18 | 19.82 | -23.23% | 25.61 | 0.893 | Recovery start |
| 2018-02-13 | G18 (1) | 25.23 | H18 | 19.82 | -21.41% | — | — | |
| 2018-02-14 | G18 (0) | 21.87 | H18 | 17.88 | -18.27% | 19.26 | — | G18 final |
| 2018-02-15 | **H18 (34)** | 17.52 | J18 | 17.32 | **-1.14%** | — | — | **H18-as-M1 begins** |
| 2018-02-16 | H18 (33) | 17.77 | J18 | 17.38 | -2.25% | 19.46 | — | |
| 2018-02-20 | H18 (29) | 18.38 | J18 | 17.82 | -2.99% | 20.60 | — | |
| 2018-02-21 | H18 (28) | 18.57 | J18 | 18.07 | -2.69% | 20.02 | — | |
| 2018-02-22 | H18 (27) | 18.07 | J18 | 17.62 | -2.49% | 18.72 | — | |
| 2018-02-23 | H18 (26) | 16.77 | J18 | 16.90 | +0.75% | 16.49 | — | Normalization |

---

## Phase mapping

| Phase | Period | M1 | DTE | Contango | VIX | Read |
|---|---|---|---|---|---|---|
| **A. F18-as-M1 plateau** | Jan 2-12 | F18 | 15→5 | +9.5 to +12% | 9.2-10.2 (LOW) | Long-DTE M1 + low spot = wide contango. ANALOG to current 6/1 setup. |
| **B. F18 expiry compression** | Jan 16-17 | F18 | 1→0 | +2.5% → -3.9% | 11.7-11.9 | Normal expiry-day compression as M1 prices converge to spot |
| **C. G18-as-M1 entry** | Jan 18-26 | G18 | 27→19 | +4.8 to +6.3% | 11.0-12.2 | Roll to new M1 = step-down in contango. G18-as-M1 ran ~5-6% throughout this phase |
| **D. Pre-spike compression** | Jan 29-Feb 2 | G18 | 16→12 | +6.1 → -4.2% | 13.8 → 17.3 | **VIX rising AND contango compressing — the pre-spike trajectory** |
| **E. Spike + backwardation** | Feb 5-9 | G18 | 9→5 | -16% → -25% | 30 → 33 (peak 37) | XIV/SVXY unwind, sharp backwardation |
| **F. Recovery** | Feb 12-23 | G18→H18 | post-spike | -23% → +0.75% | 25 → 16 | Mean reversion |

---

## Direct comparison: Feb 2018 vs Current

| Variable | Feb 2018 (analog point) | Current 2026-06-01 | Read |
|---|---|---|---|
| **M1:M2 contango** | +11.93% (Jan 5, F18 dte=12) | **+12.93%** (6/1, VX/M6 dte=12) | **Direct match in magnitude AND M1-DTE** |
| **Spot VIX at that contango** | 9.22 (absolute regime low) | 16.05 | Current VIX is 75% HIGHER at the same contango point |
| **VIX3M/VIX ratio** | 1.308 (deep contango proxy) | 1.21 (less deep) | Current term-structure less steep on constant-maturity basis |
| **Days from contango peak to spike** | ~24 cal days (Jan 5 → Feb 5) | TBD — onset 5/15, current 6/1 = 17 cal days in | Window points to **6/8-6/14 if analog precise** |
| **Pre-spike spot-VIX trajectory** | RISING through compression (9.2 → 17.3 over 22 td) | FALLING through pile-up (-1.86 over 12 td) | **OPPOSITE direction** |
| **Spot direction during M1:M2 evolution** | Bullish-on-vol (VIX rising) | Bearish-on-vol (VIX falling) | Current is NOT analogous on the spot leg |
| **Pre-event SKEW** | ~135-140 area | 142.46 (rebid from 132 low) | Both elevated; current slightly higher |
| **Pre-event credit** | HY OAS ~3.36 (stable through spike) | HY OAS 2.74 (eased -12bps) | Both credit-stable-while-vol-builds |
| **Catalyst overlap** | Feb 2 wage data + UST bear move | 6/12 May CPI + 6/17 FOMC + SEP | Both have macro gate in pre-spike window |

---

## Refined KB-VIO-064 falsifiable trigger

**Original framing (pre-this-analog):**
> if M1:M2 flattens to ≤8% by 6/10 → trap releasing without event → confirm GEX/absorption regime, downgrade conviction. If holds ≥10% or widens → short-vol pile-up intensifies; snap probability climbs.

**Problem revealed by Feb 2018 analog:** compression of M1:M2 contango IS the pre-spike trajectory, not the dis-confirming signal. Feb 2018 G18-as-M1 contango went +5.8% → +5% → +6.3% → +2.2% → +0.7% → +1.5% → +1.1% → -4.2% over 14 td before the spike. A "8% threshold breached" on Jan 30 2018 would have been a TRUE-positive snap-warning signal, not a downgrade.

**Refined framing (this study):**

| Compression direction | VIX during compression | Read | Action |
|---|---|---|---|
| ≤8% by 6/10 | VIX FALLING | True trap-releasing | Downgrade conviction |
| ≤8% by 6/10 | VIX RISING | Pre-spike trajectory (Feb 2018 analog active) | **Upgrade**, monitor for backwardation as imminence signal |
| Holds ≥10% | VIX FALLING | Pile-up persisting in absorption regime | Hold (consistent with KB-VIO-067 DIET signature + KB-VIO-062 event-hedger-bid) |
| Holds ≥10% | VIX RISING | Pile-up AND spot stress | Strong upgrade — least common state historically |
| Inverts (<0%) | regardless of compression path | Imminence | Position-armed, watch credit substance for confirmation |

**Disambiguating questions a single trigger can't answer alone:**
1. Is spot VIX direction during compression a leading or lagging signal? (Feb 2018 = leading by ~22 td; cannot generalize from N=1)
2. Does credit substance need to confirm? (Feb 2018: HY stable through spike; current: HY easing — both could be "true" pre-spike trajectories)
3. What is the 6/05 COT (KB-VIO-065) read? Lev Money positioning depth tells us whether contango is pure-speculator-crowding (analog active) or M2-event-hedger-bid (analog inactive).

---

## Forward implications

### Bull case for the trap thesis (analog active)
- M1:M2 12.93% at M1 dte=12 = direct magnitude match to Jan 5 2018
- 5/15 onset of pile-up + Feb 2018 spike was ~24 cal days from contango peak → 6/8-6/14 window
- 6/12 CPI + 6/17 FOMC + 6/17 VIX June quarterly settlement = primary spike-window catalysts
- DIET coiled-spring (KB-VIO-067) firing 5/20-5/29 = additional 65% peak-gt-50% hit-rate signal
- KB-VIO-066 sustained tail-call concentration = hedgers positioned for the gate

### Bear case (analog fails)
- Feb 2018 pre-spike spot-VIX was RISING; current spot-VIX is FALLING — opposite direction is the highest-confidence dis-analog
- Feb 2018 contango compressed steadily over Jan 18-Feb 2; current contango EXPANDED from 5/15 to peak 5/29 (the opposite trajectory at the analog T-24 point)
- Current SPX at new ATHs, breadth degraded but no break; Feb 2018 SPX was at ATHs but bond bear-move (UST 10Y +50bps Jan-early Feb) was the cross-asset stress signal — current has rallying USTs (10Y -20bps last 8td)
- GEX regime is structurally different — Feb 2018 had not-yet-record-call-notional positioning

### Watch list (next 10 td)
- **6/02-6/04:** Does M1:M2 compress below 12% while VIX rises? = analog active. Or compress with VIX falling = trap-releasing.
- **6/05 (Fri):** COT release for Tue 6/02 positions (KB-VIO-065). Lev Money pct3y <10 = speculator-crowding-confirmed (analog-supportive); pct3y >15 = M2-event-hedger-bid (analog-weakening).
- **6/10 (Wed):** original falsifiable date. Under refined framing, the question is "compression + which spot direction?" not "compression yes/no."
- **6/12 (Fri):** May CPI release — first cross-asset macro stress test in window.

---

## Limitations

- **N=1 historical analog.** Volmageddon is the closest M1:M2 pile-up to current setup but it's a single observation. Other modest-contango periods (no clean candidates in the 2007-2026 sample) would provide control comparisons.
- **Different regime structure.** 2018 = pre-record-GEX, fast-moving regime; current = record-GEX, structurally absorbed. The analog may underweight regime-conditional differences.
- **Event-driver mismatch.** Volmageddon was triggered by inverse-vol ETP unwind mechanics (XIV/SVXY); the current short-vol pile-up vehicle base is different (more institutional VIX futures + structured products, less retail-ETP). The unwind dynamics could differ.
- **No XIV equivalent exists in 2026.** XIV terminated Feb 2018; the SVXY and UVXY structures changed after Volmageddon (capped vega exposure). Whether 2026 short-vol vehicles can produce a similar unwind cascade is itself an open question (see future research candidate).
- **20 td vs 22 td window** — Feb 2018 contango peak to spike was ~22 cal days; current 5/15 onset to 6/12-6/17 gate is 18-24 cal days. Close match but the precise mapping is loose.

---

## Follow-on research candidates

1. **Other M1:M2 pile-up windows** — historical scan for 10%+ contango periods in long-DTE M1 phases. Identify any that did NOT produce a spike (control set).
2. **2026 short-vol vehicle inventory** — what's the current institutional/structured-product exposure to short-vol carry? Where would the 6/17 unwind cascade if it triggers?
3. **VIX3M/VIX ratio as compression-direction proxy** — VIX3M/VIX 1.31 (Jan 5 2018) → 0.98 (Feb 2). Current 1.21 (6/1). Does this ratio's trajectory map more cleanly than M1:M2?
4. **GEX-conditional Volmageddon-shape** — if a historical GEX series exists back to 2018, condition the M1:M2 pile-up on GEX percentile and see if recovery vs spike outcomes split.

---

*Output CSV: `workbook/FEB2018_VOLMAGEDDON_M1M2.csv` (37 daily rows, Jan 2 → Feb 23 2018).*
*Re-runnable: `.venv/bin/python3 scripts/feb2018_m1m2.py`.*
