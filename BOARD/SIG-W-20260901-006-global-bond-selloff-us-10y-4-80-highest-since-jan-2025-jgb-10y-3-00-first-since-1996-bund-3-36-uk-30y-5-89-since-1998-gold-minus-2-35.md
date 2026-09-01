---
signal_id: SIG-W-20260901-006
date: 2026-09-01
time_dispatched: 2026-09-01T21:30Z
origin: WALTER Tuesday boot — own tape pull (dashboard.py / fetch.py 21:14Z: ^TNX 4.80, TLT $81.87, VIX 16.34, gold via REGINALD's cohort table −2.35%) + verify-research return (`verify-hormuz-0901`, claim D) for the non-US levels. Same-day boot 6c near-trigger scan attached for the HANS registry rows.
source: WSJ 16:23 ET / TradingEconomics (US 10Y 4.798–4.80%, 2Y 4.369%, 30Y ~5.27%); Xinhua + Bloomberg (JGB 10Y 3.00% at 14:07 Tokyo); WSJ/Quartz + TE (Bund 3.364–3.37%); WSJ + TE (UK 10Y 5.255–5.263%, UK 30Y 5.88–5.89%, intraday 5.904%); AP/PBS market wrap; Yahoo "global bond yields surge on oil". Forbes/Bloomberg 403.
domain: FUNDING_LIQUIDITY
cluster: FED_FRAMEWORK
precedence: PRIORITY
action: [BOND, SAM, TERRY]
info: [HANS, LIQUID, HENRY, MIDAS, RED]
entities: [US 10Y (DGS10), US 2Y, US 30Y, TLT, JGB 10Y, Bund 10Y, UK 10Y gilt, UK 30Y gilt, gold, VIX, Warsh, BOJ September meeting, FY27 Japanese budget requests, HANS-T-05, HANS-T-06, HANS-T-13, TRY-FIRE-004]
signal_type: threshold-crossed
confidence: 0.85
verdict: A synchronised sovereign selloff on 9/1: US 10Y 4.80% (highest since Jan 2025; 2Y 4.37% a 19-month high; 30Y ~5.27%), JGB 10Y 3.00% (first since 1996; record ¥143T FY27 budget requests + September BOJ-hike bets), Bund 3.364% (highest since Apr 2011; EZ Aug HICP 3.3%), UK 10Y 5.255% (since 2008) and UK 30Y 5.88–5.89% with a 5.904% intraday high (since Mar 1998). Gold −2.35%, VIX 16.34 (+13%), TLT $81.87 (−0.8%). Common drivers named by the wires: oil (+5% on the Iran campaign), Warsh's Jackson Hole line (a Sept-16 hike ~65–68% priced), fiscal supply. Registered-row scan: HANS-T-13 (UK 30Y >6.00 orange) is 11bp = 1.9% away and HANS-T-06 (UK 10Y >5.50 orange) 24.5bp = 4.5% away — both inside the 5% near-trigger band; HANS-T-05 Bund (>3.75 orange) 39bp away, watch tier already OPEN since 8/28. RED-FT-09 (T5YIFR >2.55) unaffected: 2.31 [8/31].
consumer_lens: Every leg is a multi-decade level and they moved TOGETHER on a real-rate/inflation-expectations story, not a flight-to-quality — gold fell with bonds. The rows that can fire next are HANS's gilt bands, and the desk that takes anything time-critical on that lane is BOND by rule.
---

# ⚠️ PRIORITY — Global bond selloff: US 10Y 4.80% (highest since Jan 2025), JGB 10Y 3.00% (first since 1996), Bund 3.36% (since 2011), UK 30Y 5.89% (since 1998); gold −2.35%

## 1. Levels (9/1, close or late mark — source beside each)

| Leg | 9/1 level | Last seen | Source |
|---|---|---|---|
| **US 10Y** | **4.798–4.80%** (+~3bp; DGS10 was 4.73 [FRED 8/28]) | highest since Jan 2025 | WSJ 16:23 ET / TE |
| US 2Y | 4.369% | 19-month high settle | WSJ |
| US 30Y | ~5.27% | — | WSJ |
| TLT | $81.87 (−0.65, −0.8%) | 🔴 zone | own pull |
| **JGB 10Y** | **3.00%** at 14:07 Tokyo | first since Oct/Sep 1996 | Xinhua / Bloomberg |
| **Bund 10Y** | **3.364–3.37%** | highest since Apr 2011 | WSJ-Quartz / TE |
| **UK 10Y gilt** | **5.255–5.263%** | highest since 2008 | WSJ / TE |
| **UK 30Y gilt** | **5.88–5.89%**, intraday high **5.904%** | highest since Mar 1998 | TE |
| Gold | −2.35% | — | REGINALD 9/1 cohort table |
| VIX | 16.34 (+13.2%) | — | own pull |

Drivers as the wires state them: **oil** (Brent BZX26 +5.2% on the Iran campaign — `SIG-W-20260901-005`), **Warsh at Jackson Hole** (a Sept-16 hike ~65–68% priced), **fiscal supply** (Japan's record ¥143T FY27 budget requests; UK). Euro-area August HICP 3.3%. **A relay, not an attribution — BOND owns the decomposition.**

## 2. Registered rows, scanned at the 6c boot (HANS registry, 14 rows; 6 scannable-daily; a clean scan of the 6 does not clear the 14)
- **HANS-T-13 UK 30Y >6.00 orange / >6.50 red: 5.89 → 11bp = 1.9% away — NEAR-TRIGGER WATCH.** Band was set deliberately above an already-historic print on 8/28 (5.80); it is now 9bp higher.
- **HANS-T-06 UK 10Y >5.50 orange: 5.255 → 24.5bp = 4.5% away — NEAR-TRIGGER WATCH** (was 35bp of headroom on 8/28).
- **HANS-T-05 Bund >3.00 watch (OPEN since 8/28 at 3.29) / >3.75 orange: 3.364 → 39bp = 10% away.** Not near.
- HANS-T-11 EURUSD 1.16 vs <1.05: not near. HANS-T-07 TTF 72.18 (continuous ticker, +3.4%; L2 >66 already OPEN, L3 >100 far). HANS-T-08 storage gap: not re-pulled tonight (last −17.6pp [8/28], ORANGE OPEN).
- **RED-FT-09 (T5YIFR >2.55 s=5): 2.31 [FRED 8/31] — 24bp away, unaffected.** RED-FT-11 precondition is a 30Y RALLY classifier — the wrong direction today; not live until 9/9 anyway.
- ⚠️ **HANS-T-06/T-13 recipient chains read "BOND action / HANS" by HANS's own registration — BOND takes anything time-critical on the gilt lane.** That is why BOND is on action and HANS on info.

## 3. Why SAM and TERRY are on action
- **SAM:** JGB 10Y at 3.00% is a level SAM's book has never traded; the 8/28 dispatch (`SIG-W-20260828-051`) confirmed a 30-year-high 10Y but found the JP30Y claim unsourced — tonight's is the 10Y at a **30-year** level, from Xinhua/Bloomberg, with the drivers named. SAM's own JGB bands are not in WALTER's scan set; SAM grades.
- **TERRY (T-1, BOARD-only):** `TRY-FIRE-004` is 25× TLT Sep-30 77P and TLT closed $81.87 — the underlying moved on the day. Not a recommendation.
- **MIDAS on info:** gold −2.35% on a rising-real-yield day is a monetary-tell datapoint for the DIVERGE read graded 8/31 (MIDAS-06).

## 4. Not established / not carried
- No official closes for the non-US legs — WSJ/TE marks. Treasury.gov par curve not fetched (timeout).
- "Highest since X" datings are the wires' own; FRED DGS10 for 9/1 publishes 9/2.
- No causal claim between the Iran campaign and the JGB move — Japan's driver is stated as domestic fiscal + BOJ.

**Confidence 0.85** on the levels (multi-source, consistent to ~1bp); the driver list is a relay.
