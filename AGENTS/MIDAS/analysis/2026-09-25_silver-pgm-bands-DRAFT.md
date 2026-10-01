# DRAFT — standalone alarm bands for SILVER, PLATINUM and PALLADIUM (for Will's ruling)

**Author:** MIDAS · **Date:** 2026-09-25 · **Status:** ⛔ **DRAFT, NOT IN FORCE.** Setting a threshold is Will's decision. Nothing here moves a score until Will rules.
**Why now:** Will, 2026-09-25: *"I do want MIDAS to cover other previous metals as well in addition to gold."* In 2026 silver fell **−45.4%** from its high (SLV $105.60 [1/28] → $57.62 [9/24]), platinum **−37.0%** and palladium **−38.1%**. MIDAS scored silver **1 (dormant)** and PGMs **2** throughout. **Its only silver band is the gold/silver ratio, and its only PGM trigger is a confirmed SA/Russia outage. Neither can see a price collapse.**
**Evidence:** `analysis/2026-09-25_band-base-rates.md` (every figure below; reproducible via `analysis/2026-09-25_band_stats.py`). Headline figures re-computed independently by MIDAS 9/25: SLV d200 −12.6% and dd252 −45.4%; PPLT −10.1 / −37.0; PALL −14.9 / −38.1; first 2026 d200 < −12% crossings PALL 6/3, PPLT 6/23, SLV 6/24 — all match.
**Data:** no-roll ETF closes (SLV / PPLT / PALL). This avoids the futures-roll and missing-settle defects (standing warnings ①–③). Split-adjusted (PPLT 10:1 and PALL 5:1 on 2026-05-18, continuity checked against futures).

---

## 1. The finding that shapes the design

**A trend band alone (distance below the 200-day average, the copper-style grid) is structurally LATE after a bubble.** On 1/30/2026 silver was already 28.6% off its high but still **72% ABOVE** its 200-day average, because the run-up had dragged the average up. Copper's −5/−12/−20% grid applied to silver would have fired on **6/10, 6/24 and 7/16**, 92–116 sessions after the top and 45–52% into the fall.

**A drawdown band (distance below the 252-session high) catches a crash in days** (−20% on 1/30, −30% on 2/2). **But it stays "on" for up to a year**, because the January high stays in the window until January 2027. Scored as a *state*, it would call silver **RED today** for a crash that bottomed in July, with silver up about 14% since (SLV $50.39 [7/16] → $57.62).

⇒ **The two legs need two different roles:** the trend leg is a **state** (scored while it holds), and the drawdown leg is an **event** (scored for a fixed window after it first crosses, then decays).

## 2. Proposed bands (candidates — each rate is historical episodes per year, full window / 2020+)

**Leg T — TREND (state):** ETF close vs its 200-session simple moving average (d200), on a completed close.
**Leg C — CRASH (event):** ETF close vs its running 252-session closing high (dd252). Scores for **21 sessions after its first crossing**, then decays one level per 21 sessions unless a deeper level fires.
**Leg S — SPIKE (state, upside, the L-13(a) lesson):** d200 above the line. It scores **monetary/speculative overheating**, not stress.

| Metal | Band | Leg T (d200 below) | Leg C (dd252 below) | Leg S (d200 above) |
|---|---|---|---|---|
| **Silver** | 🟡 Yellow → 2 | −5% (1.33 / 1.04) | −20% (0.77 / 0.89) | +30% (0.36 / 0.45) |
| | 🟠 Orange → 3 | −12% (0.87 / 1.04) | −30% (0.41 / 0.45) | +40% (0.20 / 0.30) |
| | 🔴 Red → 4 | −20% (0.36 / 0.45) | −40% (0.21 / 0.15) | — |
| **Platinum** | 🟡 | −10% (1.26 / 1.78) | −20% (0.76 / 0.89) | +30% (0.13 / 0.30) |
| | 🟠 | −15% (0.57 / 0.74) | −30% (0.19 / 0.30) | +40% (0.06 / 0.15) |
| | 🔴 | −20% (0.13 / 0.15), **2 episodes in 16 years** | — (not measured) | — |
| **Palladium** | 🟡 | −12% (1.13 / 1.78) | −20% (0.51 / 0.74) | +30% (0.31 / 0.45) |
| | 🟠 | −20% (0.44 / 0.59) | −30% (0.51 / 0.59) | +40% (0.25 / 0.30) |
| | 🔴 | −25% (0.38 / 0.45) | −40% (0.38 / 0.59) | — |

**Why the lines differ by metal:** silver's history fits copper's grid (d200 p10 −13.0%, p5 −18.0%). **Palladium does not:** it spent 28.9% of days since 2020 below −12%, so copper's grid would have been "on" for most of 2022–24. Its lines are wider. **Platinum** rarely falls far below trend (a −20% episode twice in 16 years), so its lines are tighter.

**Scoring rule:** a metal's score is the HIGHEST level any leg shows. **M2 = max(silver band, existing GSR band).** **I2 = max(Pt band, Pd band, existing supply trigger).**
**Shared-root rule (MIDAS independence):** since 2020, daily-return correlations are SLV–GLD 0.79, SLV–PPLT 0.71 and PPLT–PALL 0.64, rising to 0.87 / 0.82 / 0.82 over the last 120 sessions. The 2026 −12% crossings came within 15 sessions of each other. **When M2 and I2 bands fire within 15 sessions of each other, the note says "one root" and the composite carries a shared-root flag.** It is not a second independent signal.

## 3. What these bands would say TODAY [9/24 closes], if approved as drafted

| Metal | Leg T | Leg C | Leg S | Score |
|---|---|---|---|---|
| Silver | d200 **−12.6%** → 🟠 | dd252 −45.4%: first crossed −40% on 3/20, decayed out | — | **3 🟠** (M2 1 → 3) |
| Platinum | d200 **−10.1%** → 🟡 | dd252 −37.0%: first crossed −30% about s39 after the high, decayed out | — | **2 🟡** |
| Palladium | d200 **−14.9%** → 🟡 | dd252 −38.1%: decayed out | — | **2 🟡** (I2 stays 2) |

⇒ **Composite 8/20 → 10/20** (M2 +2), carrying a shared-root flag with M1's rate root. ⚠️ **What that 3 would mean:** silver is in a trend-level decline. With the GSR benign it reads as **risk appetite / industrial softness + speculative unwind, NOT monetary fear**, and routes to **LIQUID and HENRY**, not BOND.

## 4. Positioning (context only — NOT proposed as a band)

COT net/OI [as-of 9/15] vs the frozen 2010–26 reference (`sources/cot_metals_history_2010_2026.tsv`, n=872 per metal):
- **Silver:** 24.41%, 59.9th percentile. Not crowded.
- **Platinum:** 23.24%, 28.7th percentile. ⚠️ Specs have been structurally less long since 2022, so a full-window rank flatters how low this is.
- **Palladium:** −24.84% (net short), 20.0th on the full window but 65th within the post-2022 net-short regime (n=246).

⇒ **Two of three metals are regime-shifted**, and a single percentile band would mis-fire. Recommend carrying positioning as a context sub-vector (like gold's `VX-MIDAS-M1-POS`) until a regime-aware design is base-rated.

## 5. The decisions for Will (⚖️)

1. **Adopt standalone silver/PGM bands at all?** My recommendation: **yes.** Without them, silver can fall 45% while MIDAS reports "dormant", which fails the brief Will gave today.
2. **The two-leg design (trend = state, crash = event with 21-session decay) and the spike leg?** Recommendation: **yes.** A trend-only band would have missed 2026 by four months, and a state-scored drawdown band would call silver RED today on a July bottom.
3. **Accept the per-metal lines in §2, or ask for different ones?** The fire rates are shown so the trade-off is visible: tighter lines alert earlier and more often.
4. **Scoring effect:** approving as drafted moves **M2 1 → 3 immediately** (composite 8 → 10). That change is caused by the rule, not by a new market event, and the commit that encodes it will say so.

⚠️ **Limits that travel with this draft:**
- The rates are **not** out-of-sample. The 2025–26 spike and crash are a large share of the 2020+ window.
- 2020+ is 6.7 years, so a 0.15/yr rate is **one** episode.
- The 21-session decay and the 15-session shared-root window are **design choices, not measured optima**.
- No sustain clause is proposed, because its effect on the rates was not measured.
- **Timing claim:** these bands are **DESIGN-FIXED, not TIME-FIXED**. They are drafted on data that already contains the 2026 collapse, so they cannot claim they would have been set in advance (WQ-H4).

---

## ADDENDUM 2026-10-01 (Thu, ~12:5x ET): refreshed to 9/30 closes for Will's ruling (WQ-352). The 9/25 text above stands as drafted. No line was re-fitted.

**Status unchanged: ⛔ DRAFT, NOT IN FORCE.** No band, score or threshold moves until Will rules.
**Method:** `analysis/2026-09-25_band_stats.py` re-run unchanged, with its output directed to a scratch folder so the 9/25 evidence file was not overwritten. The run was at 12:50 ET 10/1, and the script dropped the partial 10/1 bars itself, so the last close used is **9/30 on every ETF** (SLV $54.51 · PPLT $15.41 · PALL $21.81).

### A1. Headline figures, 9/24 → 9/30 (no-roll ETFs)

| Metal | Off the 252-session high (dd252) | Distance from the 200-day average (d200) |
|---|---|---|
| Silver (SLV) | −45.4% → **−48.4%** | −12.6% → **−17.3%** |
| Platinum (PPLT) | −37.0% → **−38.9%** | −10.1% → **−12.9%** |
| Palladium (PALL) | −38.1% → **−41.3%** | −14.9% → **−19.0%** |

### A2. Would the newer data change any proposed line? **No.**

Every fire rate in the §2 table was re-computed. **No new episode starts at any drafted line.** Six cells moved by 0.01/yr (SLV T −5% 1.33→1.32; SLV T −20% / C −30% / S +30% 2020+ 0.45→0.44; PPLT T −10% 1.26→1.25 and −15% 0.57→0.56; PALL T −25% and S +30% 2020+ 0.45→0.44). That is a longer denominator, not a different history. Two new crossings happened at levels the draft does **not** use: PPLT d200 < −12% (first close 9/29) and SLV d200 < −15% (9/28). Neither is a proposed line, and none is proposed now.

### A3. Score under the draft, as of 9/30 vs 9/24

| Metal | Leg T (state) 9/30 | Leg C (event) 9/30 | Score 9/24 | **Score 9/30** | Distance to the next level |
|---|---|---|---|---|---|
| Silver | −17.3% → 🟠 | decayed: −40% first crossed 3/20 and never reset, so no new crossing | 3 🟠 | **3 🟠** | 2.7 pts to 🔴 (−20%) |
| Platinum | −12.9% → 🟡 | decayed: −30% first crossed 3/20 (−40% is not a drafted Pt line) | 2 🟡 | **2 🟡** | 2.1 pts to 🟠 (−15%) |
| Palladium | −19.0% → 🟡 | decayed: −40% first crossed 6/8 and never reset. Its 21-session steps ran out about 9/4 | 2 🟡 | **2 🟡** | ⚠️ **1.0 pt to 🟠 (−20%)** |

**M2 = max(silver 3, GSR band 1) = 3. I2 = max(Pt 2, Pd 2, supply trigger 2) = 2.** ⇒ **The composite effect of approval is still 8/20 → 10/20 (M2 +2), and all of it comes from the rule change.** ⚠️ **Palladium is one point from orange.** If PALL closes below −20% vs its 200-day average after approval, I2 goes 2 → 3 and the composite to 11.

### A4. My strongest objection to my own draft

**These bands arrive after the damage, and the fast part is already switched off.** Approve them today and the alarm you get is "silver is in a decline": orange on a metal that is already 48% off its high. Silver first crossed its −12% trend line on 6/24, about five months after the 1/28 top (it re-crossed on 9/10). The crash leg did see the fall within days in January, but by design it steps down one level every 21 sessions, so about four months after its last new crossing (−40% on 3/20) it reads nothing. On 9/30 it reads nothing, even though silver is near its lows. So the score jump would announce something you already know, and it would add two points to a composite that otherwise moves only on market events. It also rests on lines drawn from history that includes the very collapse they are meant to catch, so their good-looking fire rates are partly fitted to it (§5 limits, WQ-H4). **If you amend rather than decline,** the change I would accept first is to adopt the bands but leave them **unscored for one month**: they print a level, and it does not enter the composite until a line is crossed on data that arrives after approval. That way the first score move is a market event, not an accounting one.

### A5. Positioning (§4) is not refreshed

The 9/29 COT vintage has **not been published** (CFTC releases it Fri 10/2 15:30 ET; `cot_gold.py --expect 2026-09-29` → WAIT, the file served is still 9/22). The silver/Pt/Pd positioning context in §4 stays as-of 9/15. Positioning is context only and is not a proposed band.
