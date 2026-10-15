# S52 — September CPI graded on the pre-written tree: `RED-FT-08` FIRES

**Written:** 2026-10-14 20:17 EDT (from `date`). **Session:** S52, launched by Will; RED had been offline since S51 (10/09). **Tree:** [`research/2026-10-14_SEPT_CPI_DECISION_TREE.md`](../research/2026-10-14_SEPT_CPI_DECISION_TREE.md), written 2026-10-01, 13 days before the data. **Nothing was improvised.** The one judgment made today, about a conflicting older note, is in §2 with its direction labelled.

---

## 1. FT-08: fired, on both bases

**Primary:** BLS CPI news release, Table A, read 2026-10-14 ~20:15 ET ([cpi.nr0.htm](https://www.bls.gov/news.release/cpi.nr0.htm)). Index cross-check: FRED `CPILFESL`, pulled the same minute.

| Month | Table A core MoM (published, SA) | Unrounded from SA index | Index level |
|---|:-:|:-:|:-:|
| Jun 2026 | 0.0 | — | 336.065 |
| Jul 2026 | **0.2** | 0.2154 | 336.789 |
| Aug 2026 | **0.3** | 0.2898 | 337.765 |
| Sep 2026 | **0.3** | **0.3348** | 338.896 |

- **Jul and Aug were NOT revised** in the 10/14 release. Jun 336.065 and Aug 337.765 match the levels in the tree, so the published-as-of-10/14 values equal the tree's inputs.
- **Table A, which governs (S50 ruling):** (1.002 × 1.003 × 1.003)^4 − 1, computed in Decimal = **3.247216% → 3.2 at 1dp ≥ 3.0 → FIRE.**
- **Index-level cross-check:** (338.896 / 336.065)^4 − 1 = **3.4124% → FIRE.** The two bases agree, so there is **no straddle** and no disagreement to record. Sept's unrounded 0.3348 is well above the 0.2347 index-basis line and outside the 0.235–0.249 straddle band.
- **WALTER's independent compound** (SIG-W-20261014-001: 3.247216%) matches mine to six decimals. Same inputs, so this checks the arithmetic, not the data.

**Action on the letter:** **Stagflation +3** (net-bear +3). CONF unchanged, because the row carries no CONF leg. **Pre-registered offset (S50, 10/01): Managed −2, Soft −1.**

| Hypothesis | S51 (10/09) | **S52 (10/14)** | Δ | Basis |
|---|:-:|:-:|:-:|---|
| Managed Decline / Muddle | 31 | **29** | −2 | FT-08 offset (pre-registered) |
| Full Stagflation Spiral | 32 | **35** | +3 | **FT-08 FIRE (mechanical)** |
| Acute Financial Dislocation | 14 | 14 | = | — (FT-10 pending, §4) |
| War Escalation | 14 | 14 | = | — |
| Soft Landing | 5 | **4** | −1 | FT-08 offset (pre-registered) |
| Policy Rescue | 4 | 4 | = | — |
| **Net-bear (Stag + Acute + War)** | **60** | **63** | **+3** | |

Sum 100. **Confidence 70, unchanged.**

**Exit, so the reversal is mechanical too:** core 3-mo annualized **< 2.5** at a later print, s=1 → Stag −3, returned to Managed +2 / Soft +1. At the **Nov 10 (October CPI)** print the window is Aug 0.3 · Sep 0.3 · Oct x. On Table A, **Oct 0.0 gives 2.43, which exits**, and Oct 0.1 gives 2.84, which holds. Only a flat or negative October core print reverses this fire.

## 2. A conflicting older note, and how it was ruled (labelled judgment)

The registry row's `exit_source` cell carries an S29d (8/12) sentence: *"MoM ≥ 0.4 is RETAINED as a human-side confirmation note, NOT as a machine leg … if it fires while MoM is < 0.4 the move is a base-effect roll-off rather than a fresh impulse, which is a NO-VERDICT worth looking at, not an automatic fire."* September's core print was 0.3. **Read literally, that note says no-verdict. The S50 tree says fire.** WALTER flagged the same conflict in its signal and said the note must not veto the ruling. RED owns the grade, so the ruling is mine, and here is the reasoning rather than the conclusion alone:

1. **The later, more specific pre-data text governs.** The S50 tree (10/01, Will-approved sweep item B5) names the exact case: *"Sep 0.3 → 3.25 → 🔴 FIRE."* It was written with the roll-off in view; its arithmetic table is headed *"June's −0.0 rolls out of the window."* The 8/12 note never saw a 0.3 case and is, by its own words, not a machine leg.
2. **The note's own diagnosis is absent here, and only its proxy is tripped.** The note exists to stop a fire caused by a weak month rolling out while the new month is benign. **That is not this fire.** A September 0.2 would have produced 2.84 and **no fire**. The fire needs the new print, which ran at 0.3348% unrounded, about a 4.1% annualized pace for that single month. All three months in the window are ≥ 0.2. The 0.4 threshold is a coarse stand-in for "fresh impulse," and this case is a fresh impulse that falls under it.
3. **Direction, stated:** this ruling moves weight toward the bear and **against RED's own S41 view** ("stagflation is not the shape of this economy"). A rule only proves itself in the session it charges you (MEMORY, S28).

**Apparatus defect, routed and not fixed here:** two pre-data texts on one row gave opposite instructions for the 0.3 case, and nothing flagged it until the data arrived. That is the same class as ML-RED-274's *"a row whose basis columns describe two computations."* It goes to the **CHG-051 spec review on 10/31**, with the FT-08 `exit_source` 0.4 note named for retirement or re-statement. The note is left in place today, unedited. A fired row is not amended on fire day.

## 3. CHG-RED-028 leg 1, the oil-to-core channel: NOT MET on the September print

| Component (FRED, SA) | Aug index | Sep index | Sep MoM | Registered bar | Met? |
|---|:-:|:-:|:-:|:-:|:-:|
| Airline fares `CUSR0000SETG01` | 323.244 | 326.991 | **+1.159%** | ≥ 2.35% (2023+ p75) | **NO** |
| Transportation services `CUSR0000SAS4` | 460.542 | 463.237 | **+0.585%** | ≥ 0.51% (p50) | yes |
| **Joint leg** | | | | **both** | **NOT MET** |

- **Consequence for the 11/10 verdict:** REALIZED needs the leg met on **both** prints, so **REALIZED is now foreclosed.** What remains possible is NOT REALIZED (the leg is missed again in October **and** core 3-mo < 2.5) or NO VERDICT.
- **What the composition says, plainly:** core accelerated, but not mainly through the channel the stagflation-by-oil story needs. BLS names recreation, used cars, education, airline fares, medical care and apparel as the risers. Shelter rose 0.4 (0.3 in Aug). Airfares rose, but at well under the p75 pace they ran at in three of May–Aug. **So FT-08 says core is running hot again; CHG-028 says the oil pass-through is not what is doing it.** Both are recorded. Neither is netted against the other: FT-08 is a mechanical level test and CHG-028 is a composition test (ML-RED-085).
- Headline: +0.6% m/m, +3.7% y/y; energy +5.2%, gasoline +9.1%. Core y/y is 2.6%.

## 4. The other registered lines at the 10/14 boot

| Row | Reading | State |
|---|---|---|
| **FT-10** ^SKEW ≥150 s=4 (Acute +2 / Managed −2 on fire) | Cboe `SKEW_History.csv`: 149.19 [10/08] · **154.34 [10/09] = 1** · **155.06 [10/12] = 2** · **154.74 [10/13] = 3**. The CSV has **no 10/14 bar** at 20:14 ET. Cboe's own delayed-quote feed shows **157.30, last trade 2026-10-14 17:00:19** (`_SKEW.json`, pulled 20:14 ET). | **3 of 4. PENDING the official 10/14 bar.** The registered basis is the history CSV, and the quote feed **cannot complete a grade** (`instrument_basis_operative`). VIOLET's count (3 through 10/13) and WALTER's (SIG-W-20261014-012) agree. **If the CSV prints 10/14 ≥ 150.00, FT-10 FIRES**: Acute 14 → 16 and Managed 29 → 27, so **net-bear 63 → 65**. Below 150, it resets to 0. |
| **FT-02** HY OAS >320 s=3 | 311 [10/9] · 311 [10/12, a holiday forward-fill: Columbus Day, identical to 10/9 in all four ICE tiers] · **316 [10/13]** | **0 of 3, 4bp away, NOT FIRED.** 10/8→10/13: BB −3 · B +2 · CCC +15 (1,267). The tail is still doing most of it. |
| **FT-06** VIX <16 s=5 (banked) | VIXCLS 15.27 [10/13]; ^VIX 16.87 on 10/14 (+10.5%, yfinance) | Banked. Exit ≥ 18 s=5 is not engaged. |
| **FT-07** CCC >930 s=1 (banked) | 1,267 [10/13] | Banked; no change. |
| **FT-09** 5y5y >2.55 s=5 | 2.34 [10/14] | Clear. |

## 5. Market reaction on CPI day (recorded; scores nothing, ML-RED-085)

5y5y **2.34** (+0.01) · VIX **16.87** (+10.5%) · SPY −1.08% · IWM −1.93% · TLT +0.66% (10Y yield down on the day) · HY OAS T+1 not yet published. **A hot core print met falling long yields, a flat 5y5y and lower stocks.** That reads as risk-off, not an inflation scare. It is the bull's best line against the fire meaning a spiral: **long-run inflation compensation did not move.** That witness is named here, and it does not touch the mechanical grade.

## 6. What this does NOT do

- It does not re-derive the discretionary weights. Two items from the catch-up week go to the next re-derivation, not into today's mechanical move: (a) **OZK's largest San Diego credit (RaDD) was extended to Dec 2029 with $100M in fresh capital (OZK 8-K, 10/12)**, which is bull counter-evidence against the structural bank leg; (b) **two more Gulf ship strikes (GFS PRIDE sank 10/13, GFS GISELLE hit 10/14, Singapore MPA)** against the IEA's estimate of Gulf crude exports recovering to 13.9 Mb/d in September.
- It makes no trade view. $0.

Sources: BLS CPI release 2026-10-14 (Table A and text); FRED `CPILFESL`, `CUSR0000SETG01`, `CUSR0000SAS4`, `BAMLH0A0HYM2`, `BAMLH0A1HYBB`, `BAMLH0A2HYB`, `BAMLH0A3HYC`, `VIXCLS`, `T5YIFR` (pulled 2026-10-14 ~20:15 ET); Cboe `SKEW_History.csv` and `_SKEW.json` (pulled 20:14 ET); WALTER SIG-W-20261014-001 / -012; VIOLET packet 2026-10-14; OZK 8-K via SIG-W-20261012-005; MPA via SIG-W-20261014-002; IEA OMR via SIG-W-20261014-003.
