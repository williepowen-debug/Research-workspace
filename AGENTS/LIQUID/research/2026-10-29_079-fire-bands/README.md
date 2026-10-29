# GATE-LIQ-079 FIRE-leg bands — census behind the 10/31 proposal (DOCKET L261)

**LIQUID · 2026-10-29 00:12 ET.** ⛔ PROPOSAL INPUT, NOT A REGISTERED LETTER. Bands are Will's word; the proposal itself is in the LIQUID → PROME packet of 10/29. `fire_bands.py` reproduces every figure below (FRED: SOFR99, SOFR1, IORB spliced to IOER at 2021-07-29, EFFR, EFFR75, EFFR99, RPONTTLD; 2,138 SOFR days 2018-04-03 → 2026-10-27, 1,607 non-calendar under `fp_backtest_079.py`'s ±2-business-day rule, holidays not removed). Output: `fire_bands_result.json`.

**ARM history under the letter (≥ +30, non-calendar, ≥ 2 consecutive):** 11 ARMED days in 4 episodes — 2019-07-05 (1 day, peak 41, FP) · **2019-09-16→25 (6 days, peak 690, the one true positive)** · 2019-10-16→17 (2 days, peak 40, TP-continuation) · 2020-03-17→18 (2 days, peak 90, shock archetype, vetoed by leg 1).

| Candidate band | Non-calendar days met (all history) | ARMED days met | ARM episodes met | Sep-2019 days met (8) | Non-cal days met since 2025-08-14 |
|---|---|---|---|---|---|
| 3a EFFR − IORB ≥ 0bp (level) | 253 / 1,607 (15.7%) | 11/11 | 4/4 | 8 | 0 |
| **3a′ EFFR − IORB 10-day change ≥ +3bp** | **36 (2.2%)** | 9/11 | 3/4 | 8 | 0 |
| 3a″ same, ≥ +5bp | 15 (0.9%) | 9/11 | 3/4 | 8 | 0 |
| **3b EFFR75 − IORB > 0bp** | **202 (12.6%)** | 11/11 | 4/4 | 8 | 0 |
| 3b′ EFFR99 − IORB ≥ +10bp | 466 (29.0%) | 11/11 | 4/4 | 8 | 0 |
| 4a SOFR99 − SOFR1 ≥ 20bp | 273 (17.0%) | 11/11 | 4/4 | 8 | 13 |
| **4a′ SOFR99 − SOFR1 ≥ 30bp** | **53 (3.3%)** | 9/11 | 4/4 | 6 | 2 |
| 4a″ same, ≥ 50bp | 16 (1.0%) | 5/11 | 2/4 (TP + 2020-03) | 4 | 0 |
| **4b repo-op take-up (RPONTTLD) ≥ $10B** | **131 (8.2%)** | 9/11 | 3/4 | 7 | 4 |
| 4b′ same, ≥ $1B | 154 (9.6%) | 9/11 | 3/4 | 7 | 17 |

**Joint (proposed): ARMED AND (3a′ OR 3b) AND (4a′ OR 4b)** → 11 days, all 4 ARM episodes.

**What the census says, plainly:**
1. **Conditional on ARM, legs 3–4 add almost no discrimination at n = 1 true positive.** Every historical ARM episode meets the proposed joint bands, the 2019-07 false positive included. FIRE's real filters are leg 1 (the archetype call) and ARM's persistence. Banding legs 3–4 turns FIRE from UNGRADEABLE into gradeable; it does not make it more accurate.
2. The only band that separates the true positive from both 2019 false positives is SOFR99 − SOFR1 ≥ 50bp — fitted after seeing one hit, the in-sample move the letter already refused for the calendar filter. Offered as an option, not recommended.
3. In the current drained regime (since 2025-08-14) the slow-lead bands have never been met on a non-calendar day (EFFR − IORB −2bp throughout); repo-op take-up of $1B–$30.5B happened on 17 non-calendar days (Sep 2025 – Feb 2026), none of them ARMED (max SOFR99 − IORB +28). Leg 4b alone is a frequent non-event; it only matters inside ARM.
4. Not banded, and why: **reserve-demand slope** (no daily series reachable; NY Fed elasticity estimates are periodic) · **GCF − TriParty premium** (OFR STFM series not base-rated in this pass) · **AI-HY basket dispersion** (a credit tell, KB-LIQ-073, not a funding-dispersion measure — proposed for removal from leg 4; a letter change, Will's). Each stays UNGRADEABLE, never "not met".
5. Limits: holidays are not removed from the historical calendar; RPONTTLD before 2019-09-17 is empty (no operations), so 4b had no chance to fire before the true positive began; first-published vintages were not used for this census (latest-revised, as in the 7/23 ARM census).
