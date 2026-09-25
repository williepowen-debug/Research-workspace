# Q2 — What is the first observation that would convince us stress is spreading? (LIQUID, lead)

**Asked by:** Will 02:55 ET 9/25, relayed by PROME (`inbox/processed/2026-09-25_from-PROME_will-directed-six-questions-LIQUID.md`, `c29e4ca60`; DOCKET L477).
**Co-owners:** HENRY wrote the rates leg (`AGENTS/HENRY/research/2026-09-25_L477_Q2-Q5-HENRY-legs.md` §Q2, `0d8616964`) and VIOLET the vol leg (`AGENTS/VIOLET/STATUS.md` § "Q2 CONTRIBUTION", `dff7fddbb`). Both were verified at the artifact and are cited in §4, not restated.
**Registered BEFORE the 9/24 ICE cells publish (~9/25 16:15 ET).** This file's commit time is the timing receipt (PREDICTION_DISCIPLINE, pre-registration timing rule).
**Registered as `LIQ-07`** in `workbook/PREDICTIONS.tsv`.

## 1. The answer, in one line

**The first convincing observation is the B tier's own three-week widening reaching its 90th percentile (+28bp over 15 sessions) on three consecutive published days, while CCC is still widening. In this history, that print almost never arrives alone: BB, BBB and IG were at their own 90th percentiles the same day in 6 of 7 episodes.** There is no reliable "B only" middle stage to wait for. The sequence has been *CCC alone* (common) → *everything at once* (broad repricing).

## 2. Why this test, and why no existing gate already is it

| Existing gate / line | Why it is not the "first observation" test |
|---|---|
| HY OAS **>320 = "credit transmission confirmed"** (my send table, → ALL) | This IS the registered confirmation, but it is an index LEVEL. It was above 320 at the trigger date in only **3 of the 7** broad episodes (HY 367 · 461 · 327; the others were 316 · 311 · 320 · 292). It fires late or not at all when spreads start from a low base, and by construction it cannot see breadth (KB-LIQ-128) |
| HY **>280 X1 half** | Fired on broad beta in July (68–84% DM HY beta, `analysis/2026-07-30_hy-attribution.md`), so it is not a spreading detector. It is also 7bp from today's level [9/23] |
| GATE-LIQ-069 L1 (BB >220 while CCC flat) | The opposite configuration (BB-led, tail quiet) |
| GATE-LIQ-072 (IG >94) | The IG rung only, 17bp away [9/23]. Under this test IG moves the same day as B, so 072 is a late subset |
| GATE-HY-REKILL (<260 ×2) | The kill side, the other direction |
| GATE-LIQ-079 / SRF >$50B | Funding seizure. **Used below as accompaniment legs, not as the spreading test** |
| GATE-LIQ-076 | Dealer positioning; BOND carries the dealer side |

The test uses **existing series** (the FRED ICE BofA ladder) and the **existing method** (KB-LIQ-128: rank the 15-session change against its own history). Its accompaniment legs are **existing, base-rated instruments** (`sofr_dispersion.py` ORANGE band, the GATE-LIQ-079 ARM leg, the SRF >$50B send line). **No threshold here was chosen for being near today's level.** B needs +28 over three weeks against +2 now; the funding band needs z ≥ 4.0 (hit on 4.87% of sessions).

## 3. The registered test — `LIQ-07` "SPREAD-B"

**Premise (stated, per the two-branch rule): the ladder transmits CCC → B → higher tiers. ASSUMED, not observed.** In-sample, B has led BB only once (2026-02-12, by 16 days). That is why the trigger sits on B but the answer reads "everything at once".

**Trigger (the first observation).** On a published FRED observation date *t*:
- **B:** `BAMLH0A2HYB` 15-session change ≥ **+28bp**
- **and CCC:** `BAMLH0A3HYC` 15-session change ≥ **0bp**
- **on 3 consecutive published observations.** The trigger date is the 3rd.

**Branches (MECE; the first event to occur decides).**

| Branch | Rule |
|---|---|
| **S1 SPREADING — FEEDBACK LOOP** | Trigger fires **and**, within ±10 published sessions of the trigger date, at least one funding leg reads: `sofr_dispersion.py` z ≥ **4.0** (ORANGE) on a non-quarter-end session · or GATE-LIQ-079 ARM (SOFR99−IORB ≥ **+30bp**, date-matched, non-quarter-end, ≥2 consecutive) · or SRF (`RPONTTLD`) ≥ **$50B** |
| **S2 SPREADING — ORDINARY REPRICING** | Trigger fires, and no funding leg reads within ±10 sessions |
| **S3 REVERSED** | Before any trigger, the CCC−B gap's 15-session change ≤ **−35bp** (its own p10): the tail gives back relative to B |
| **S4 CONTAINED** (counts AGAINST transmission) | Window ends with no trigger and no reversal: the tail stayed isolated |

If the trigger lands within the window's last 10 sessions, the S1/S2 funding look-forward runs up to 10 sessions past the window end. The catch-all is S4. The only NO-VERDICT route is the Invalidation clause.

**Window: published observations 2026-09-24 through 2026-11-06 inclusive (≈32 published days). Anchor type: CHOSEN.** It is the last date the answer can still change the book's credit posture before year-end. It spans the Q3-end turn, October month-end and the 11/4 buyback end. Nobody can move it except by re-registration. **Resolve_By 2026-11-10** (the 11/6 obs publishes Mon 11/9 ~16:15 ET).

**Grading basis (WQ-162, every observation read).**
- **Series and unit:** B and CCC OAS on FRED ICE BofA; published in percent, ×100 = bp, rounded to integer bp. **Tie set:** inclusive at the boundary (≥ +28, ≥ 0, ≤ −35).
- **Observations read:** each 15-session change reads 2 observations, the trigger reads 3 changes (6 observations, overlapping), and each funding leg reads its own dated print.
- **Vintage: as first published** (`fetch.fred_fetch_vintage`). If a first-published value is missing for a date, grade on latest-revised and say so on the row.
- **Thresholds: FROZEN** at the values above, computed 2026-09-25 from latest-revised history 2023-10-02..2026-09-23: B p90 +28 · CCC−B p10 −35.
- **Resolver:** LIQUID, running `scripts/transmission_check.py` plus this letter. Funding z comes from `scripts/sofr_dispersion.py`.

**Invalidation (resolves NO-VERDICT on the date met).**
1. FRED or ICE discontinues, re-bases or truncates `BAMLH0A2HYB` or `BAMLH0A3HYC` so a 15-session change cannot be formed.
2. Three or more consecutive published dates are missing inside the window.
3. A published ICE methodology or composition notice changes the B or CCC tier definition inside the window.

**Base rate (in-sample, 2023-10-02..2026-09-23; ⚠️ rolling ~3-year FRED window, see §5).**
- **Episodes:** the trigger fired **7 times** (2024-08-06 · 2025-03-10 · 2025-04-07 · 2025-10-14 · 2025-11-18 · 2026-02-12 · 2026-03-16).
- **Broadening followed every time:** in **7 of 7**, BB reached its p90 within 30 sessions, and in 6 of those it was already there on the trigger date.
- **Funding accompaniment:** present around **3 of 7**. Oct–Nov 2025 had z +9.0 and SRF $50.35B, both on the 10/31 month-end, in the late-QT reserve squeeze. 2026-02-12 had SRF $30.5B on 2/17, but z only +1.8, so it would count on the SRF leg only if ≥$50B, **which it was not**. On this letter S1 fired once (Oct–Nov 2025, counted once). **The largest repricing in the sample, April 2025 (HY 461), had NO funding accompaniment** (z ≤ +2.7, SRF $0.10B). That is S2.
- **How often it fires:** the trigger state was reached within the next 32 published days on **29.6%** of all start days, and on **12.0% (3 of 25)** of start days already in the isolated-CCC state, today's state. Both counts come from overlapping windows, so the effective n is far smaller than the day counts.

**Prediction: P(S1 or S2 by 2026-11-06) = 15%.** That is the conditional in-sample 12%, nudged up for the hiking-Fed/real-yield regime and the 9/23 one-day reach into B. **P(S1) = 5%.** P(S3) = 15%. **P(S4) = 70%.**

## 4. Ordinary repricing vs a developing feedback loop

| Leg | Ordinary repricing (S2) | Developing feedback loop (S1) | Owner |
|---|---|---|---|
| **Credit ladder** | Tiers widen together once; the 15-session changes roll off within a window | Widening persists past one 15-session window and CCC−B does not compress | LIQUID |
| **Funding** | Overnight rates quiet: sofr-dispersion z < 4, SOFR99−IORB far below +30, SRF near 0 (April 2025 is the template) | Funding reprices off the calendar: z ≥ 4 on non-quarter-end sessions, 079 ARM, SRF use outside settlement dates | LIQUID |
| **Rates path** | Yields move with the policy path; bear-flattener; breakevens stable; rates up with credit and equities flat or up | Yields rise beyond the path (residual widens session after session); long-end-led bear steepener; breakevens fall; **rates up with SPX down, HY wider and KRE down in the same sessions** | HENRY §Q2 (`0d8616964`) |
| **Vol** | Looks like today: VIX in the LOW_VOL band, VIX3M/VIX contango >1.15, VVIX <120, SKEW 20-session mean elevated with no persistent >150 (VIOLET, 9/24 delayed quotes: VIX3M/VIX 1.1761 · VVIX 90.57) | **`VIX3M/VIX ≤ 1.00 AND VVIX > 120` on the same session, persisting to the next close, within 10 sessions of the qualifying MOVE spike.** Both lines are pre-registered (SIGNAL_INTAKE durable line #1; KB-VIO-123). ⚠️ VIOLET's own caveat: this is a **peak-marker, not an onset predictor** (KB-VIO-034: 2.2% hit rate over 553 events) | VIOLET (`dff7fddbb`) |

**HENRY's rates read on 9/22–9/24: mixed, leaning ordinary.** 9/23 was path-led, 9/24 was the one loop-shaped day, breakevens were flat, and KRE is the single loop-shaped cross-asset signal (it predates the burst). HENRY's point stands and I adopt it: **no single rates gate captures a loop; a loop is a conjunction across desks.** This test's S1 is the funding half of that conjunction. HENRY's rates legs and VIOLET's vol clause are read beside it at grading and reported with the verdict, as context. VIOLET's clause keeps its own anchor (a qualifying MOVE spike), not this test's trigger date. I did not re-key another desk's letter. VIOLET's disconfirmers are recorded as VIOLET wrote them: VIX3M/VIX rising back toward 1.20 despite MOVE ≥85 sustained · VVIX fading below 85 despite MOVE holding · VIX 5-session change within ±5% while MOVE prints p95+ · SKEW 20-session mean below 145 sustained. They do not change the branch, because a branch that depends on three desks' discretionary reads is no longer a registered test.

## 5. What counts against transmission

- **S4:** by 11/6, B's 15-session change never reaches +28 while CCC stays wide. The tail stays isolated for a fourth month (the isolated state started 8/03).
- **S3:** the CCC−B gap compresses by 35bp or more over 15 sessions (its p10).
- **Inside a trigger:** no funding leg reads (S2). That makes it repricing, not a loop.

⚠️ **One caveat, stated once:** FRED carries only a rolling ~3 years of ICE BofA history (earliest 2023-09-25). Every percentile, p90 and episode count here comes from a calm window that contains no 2020 or 2022 stress. Against a full cycle, the same moves would rank lower and the p90s would be wider.
