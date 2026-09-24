# VIOLET STATUS

**As of:** 2026-09-24 00:5x ET (pre-open). Market basis: the **September 23 session close** for the VIX complex and MOVE. Every cell dated otherwise says so. Thesis **v4.1.1**. Grade records: [part 1](research/2026-09-17_VIO-FOMC-0916_GRADE_part1.md) · [part 2](research/2026-09-18_VIO-FOMC-0916_GRADE_part2.md) · **[part 3: LEG 2 + WHOLE LETTER](research/2026-09-24_VIO-FOMC-0916_GRADE_part3.md)**. The previous state (9/18 close basis) is in git.

⚠️ **PUBLISHER CAVEAT FOR EVERY 9/23 SPOT CELL BELOW.** At 00:4x ET, CBOE had not posted 9/23 on any surface: the history CSV ends at 9/22, the delayed-quote snapshot is stamped 2026-09-23 03:43, and FRED VIXCLS ends at 9/22. **9/23 VIX-complex cells are yfinance readings,** cross-checked across three yfinance paths for VIX. The `VX_DAILY` 9/23 row is **provisional (no basis stamp)**. ⛔ **Re-pull CBOE at the next boot and supersede that row.** The 9/18–9/22 rows are CBOE history, stamped SETTLE. The 9/18 row was **corrected** this session: VIX 14.82→14.81, VVIX 87.69→87.38.

## BOTTOM LINE

🔴 **VIO-FOMC-0916 IS FULLY GRADED, AND THE LETTER FAILED ON EVERY LEG GRADED ON SUBSTANCE.**
- **Leg 2 = KILL.** VIX went 17.71 [9/16 CBOE] → **15.18** [9/23 yfinance, not yet CBOE-confirmed] = **−14.29%**, against a kill line of −1.41%.
- The verdict holds unless the true 9/23 close was ≥17.46, which is 2.28 points above the reading.
- **Final scoreboard: 0 CONFIRM · 2 KILL · 1 MISS · 1 VOID · 1 HELD-with-defect.**
- **The three substantive failures (legs 2, 3, 4) are one error on one event, not three findings.** The letter treated the FOMC as a stress event; the market treated it as a resolution event. Most of the premium unwound in the first session (VIX −12.82% on 9/17) and did not rebuild.

⛔ **A correction to my own record (part 3 §4, KB-VIO-309).**
- **The 9/18 MOVE bar did print: 80.64.** WALTER had it on 9/19, and the signal sat unconsumed in my inbox for five days.
- The leg-3 verdict is unchanged and **stronger**: branch B now holds 3/3 cells on direct evidence.
- Part 2's claim that *"all three A-cells moved monotonically opposite"* is **withdrawn**: MOVE rose 5.80% on 9/18.
- H-approach-vs-delivery loses its third observation.

🟠 **9/23 was a rates-vol shock.** MOVE jumped **+21.5% to 95.45** [9/23, investing.com PRIMARY, cross-check agrees], the highest value in my 57-row ledger. The 10Y yield rose from 4.963 [9/21] to **5.114**, and TLT fell 1.6%. VIX rose only 6.83% and VIX3M/VIX was still 1.193 (contango). **Rates vol is leading equity vol again, one week after the event.** I have not attributed a cause; the rates substance belongs to HENRY/BOND.

**No thesis bump: v4.1.1 stands.** An event map proven wrong does not make the vol framework wrong. **No trade proposed, no threshold moved, no score changed; the book is flat.**

## SIGNAL DASHBOARD

| Metric | Value | As of | Source / interpretation |
|---|---:|---|---|
| VIX | **15.18**; +6.83% vs 14.21 (9/22) | Sep 23 close | [CONF yfinance ×3 paths; CBOE unposted]. **−14.29% from the 9/16 event close. Leg 2 KILL.** Not a fill-forward (co-moves with five other series) |
| VIX9D | **13.45**; +10.9% | Sep 23 close | [CONF yfinance]; 9/22 CBOE 12.13 |
| VIX9D / VIX | **0.886** | Sep 23 | same-date calc |
| VIX3M / VIX6M | **18.11 / 20.11** | Sep 23 close | [CONF yfinance]; 9/22 CBOE 17.61 / 19.79 |
| VIX3M / VIX | **1.193** (9/22: 1.2393) | Sep 23 | Contango still steep. It was 1.2393 at the 9/22 close, the steepest of the post-event run, and gave some back on the rates shock |
| VVIX | **88.60**; +6.5% vs 83.17 | Sep 23 close | [CONF yfinance]. Below the ≤90 cheap line; watch level is >100. ⚠️ The CBOE delayed-quote VVIX close at 16:05 is **not final** (9/18: 87.63 vs history 87.38). Grade VVIX only on the history file |
| SKEW daily | **146.15** [9/23 yfinance, provisional] · **144.80** [9/22 CBOE] | Sep 22–23 | 9/18 CBOE bar published late: **148.10**. Below 150 on every bar since 9/15 |
| SKEW 20-session mean | **147.46** (8/25→9/22) | Sep 22 | [CONF] VX_DAILY CBOE bars |
| Adjusted M1:M2 | **+3.679%** [9/18], Oct/Nov | Sep 18 settle | ⚠️ **NOT RE-READ.** The 9/21–9/23 rows have blank m1m2 by backfill convention. Next post-close boot |
| MOVE | **95.45**; +16.89 (+21.5%) vs 78.56 | Sep 23 | [CONF] investing.com PRIMARY, yfinance agrees. **Ledger max.** Margins: **+19.95 vs confirm-3 75.50 · +23.04 vs F1 72.41.** 9/18 **80.64**, 9/21 81.20, 9/22 78.56 |
| OVX | 50.39, ratio 3.40 (p96.4), FIRE | **Sep 18** ⚠️ | **NOT RE-READ.** A pre-open boot writes a 9/24-dated row from 9/23 data |
| JPY RV10 | 11.1%, p72.6, CALM | **Sep 18** ⚠️ | **NOT RE-READ** (same reason). WALTER SIG-W-20260921-001: Japan reportedly ran a rate check at ~¥158 (press-reported, unconfirmed); Tokyo reopens 9/24. SAM owns the substance |
| COR1M / COR3M | 9.20 / 10.90 | **Sep 18** ⚠️ | NOT RE-READ |
| HY / CCC / BB OAS | **2.68 / 10.75 / 1.56%** | Sep 22 FRED | [CONF] direct FRED. CCC−BB **9.19 pp**. **BIN-B block active** (CCC 10.75 ≥ 9.55). LIQUID owns the interpretation |
| IG OAS | **0.77%** | Sep 22 FRED | [CONF] |
| COT VIX positioning | Lev money net **−16,504**, p69.9; OI 446,060 | Sep 15 report | [CONF] CFTC TFF. The 9/22 report publishes Fri 9/25 15:30 ET |
| VIX options positioning | C/P OI 3.38 | **Sep 18** after-hours | Not re-read; after-hours artifact caveat as before |

**Spot integrity:** `backfill.py --spot-only` made CBOE the authority. It created the missing 9/21 and 9/22 rows (SETTLE), corrected 4 cells on 9/18, and wrote 9/23 as provisional yfinance. `vx_daily_gapcheck` rc=0: 427 sessions, no gaps, and 9/23 is ahead of the publisher, so it is not graded.

## GATE STATUS

| Instrument | State | Exact scope / next step |
|---|---|---|
| **VIO-FOMC-0916** | ⛔ **CLOSED: LETTER FAILED** | Leg 1 VOID · **leg 2 KILL (−14.29%)** · leg 3 CONFIRM B / MAP MISS (now 3/3 on direct evidence) · leg 4 KILL · leg 5 HELD-with-defect. Letter sha256 `ead84431…` re-verified 9/24. **One disagreement is recorded, not applied:** leg 2 borrowed the cohort of VIX ≤16 at T-1 but had no void clause. The level cohort that did apply (VIX >16 at T-1, n=34) was 53% up, not 88%. This is acceptance condition ⑤. |
| **Cheap-tail alert** | ⚫ WQ-258 LAPSED 9/18; **not re-read since** | A new OPEN on a later settle would be a **NEW** alert. Not run this session (pre-open write hazard). WALTER's ¥158 rate-check signal is INFO; it decays at Tokyo's reopen today |
| F-B | **HELD** (window closed 9/16) | Unchanged |
| Coiled spring (STRICT / DIET) | **NOT RE-READ** (last read NOT FIRING on the 9/17 window) | SKEW is 144.80–146.15, far below any ≥+10 ΔSKEW build |
| GATE-VIO-RV1 | **RETIRED**, F2-killed Aug 27 | — |
| RED-FT-10 | **RED-OWNED** | CBOE bars since 9/15: 146.61 · 145.95 · 145.70 · **148.10** (9/18) · 142.19 · 144.80. None ≥150. Bars supplied by me; **RED owns the count** |
| RED-FT-06 | **RED-OWNED** | VIX 15.18 [9/23]; RED grades |
| KB-VIO-123 crack/fade tree | MOVE leg **above line, margin +19.95** | No longer fragile: MOVE 95.45. VVIX >120, VIX >20, inversion and COT ≥95 are **not** met. The credit leg is LIQUID's |
| BIN-A / BIN-B | BIN-A STUCK; **BIN-B block active** | CCC 10.75 [9/22] |
| GATE-VIO-116 | RESOLVED July 16 | MOVE monitoring continues; no deployment authorisation |
| T9 self-falsifier | NOT MET | MOVE is far above <66 |

## CONVERGENCE MATRIX

**Convergence Score: 27/50** (10 vectors × 5), **unchanged**. The rates-vol vector was already at 5; the 9/23 MOVE spike takes it from *breached, fragile* to *breached, well clear*. That changes the substance of the vector, not its score. ⚠️ **Four vectors (oil vol, JPY carry vol, implied correlation, positioning) carry their 9/18 or 9/15 values** because they were not re-read this session. Each is flagged in its row.

| Vector | Score | Current reasoning |
|---|---|---|
| Rates vol | 🔴🔴 **5** | MOVE **95.45** [9/23], margin +19.95 over confirm-3, ledger max, +21.5% in one day with the 10Y yield +15bp |
| SKEW / tail bid | 🔴 **4** | 20-session mean 147.46 elevated; latest bars 144.80 [CBOE 9/22] / 146.15 [yf 9/23], under 150 |
| Oil vol | 🔴 **4** | ⚠️ 9/18 value: OVX ratio 3.40 p96.4 FIRE, denominator-led |
| Credit | 🟠 **3** | CCC 10.75 distressed tail; HY 2.68 tight |
| Positioning | 🟠 **3** | ⚠️ 9/15 report: lev money p69.9 |
| JPY carry vol | 🟡 **2** | ⚠️ 9/18 value CALM; the ¥158 rate-check report is unconfirmed (SAM) |
| VVIX | ⚪ **1** | 88.60, below 90 |
| Front curve | ⚪ **1** | 3M/VIX 1.193, 9D/VIX 0.886: contango, calm |
| Implied correlation | 🟡 **2** | ⚠️ 9/18 value |
| Equity concentration | 🟡 **2** | VULCAN's structural watch; WALTER SIG-W-20260921-008 breadth claim is INFO (HENRY/RED own it) |

## REGIME STATUS AND DRIFT

- Price classification: **LOW_VOL** (VIX 15.18 [9/23, provisional]; it was COMPLACENCY at 14.21–14.87 from 9/18 to 9/22). No terminated regime of ≥60 sessions is asserted.
- **The post-FOMC path, from the 9/16 close:** VIX −12.82% (9/17) → −16.37% (9/18) → −16.04% (9/21) → **−19.76% (9/22, low)** → −14.29% (9/23). **The premium unwound in the first session and did not come back.** This is the resolution-event signature named in part 2 §5.
- 🔴 **The graded finding, final form:** the letter's legs 2, 3 and 4 all failed on one event because the letter modelled a stress event. Recorded **once**, as n=1, for **H-resolution-vs-stress**. It must be pre-registered before it is graded, and the FOMC-date base rate is the instrument it needs.
- 🟠 **9/23 reverses the post-event direction in rates, not in equity vol.** MOVE was 78.56 → **95.45** while VIX3M/VIX stayed in contango at 1.193. One day is not a regime. ⚠️ **H-approach-vs-delivery is weaker, not stronger:** its 9/18 observation became +5.80% once MOVE printed (KB-VIO-309). ⛔ Do not read 9/23 as a confirmation of it; there was no event to approach.
- **Unadjudicated and still so:** whether the 9/18 opex removed the dealer amplifier (HENRY) or a relief tape absorbed it (mine). KB-VIO-307: do not resurrect without new evidence.

## POSITIONS

Last recorded VIOLET book: **FLAT**. `TRY-VIOLET-VIXCS` closed July 30; FORGE's September 10 mirror confirms the closure. **No broker refresh, no order, no proposal this session; $0 moved.**

## RESEARCH QUEUE

1. **Next boot (post-close): re-pull the CBOE history** and supersede the provisional 9/23 `VX_DAILY` row. Run the full `boot.py` post-close so OVX, JPY, cheap-tail, COR and m1m2 re-read on a clean basis. ⛔ Leg 2 cannot move (2.28-point margin).
2. **Write the next pre-registered letter against the FIVE acceptance conditions** (part 3 §5):
   - ① branches partition the realised state space;
   - ② every cell must fail against the T-1 close;
   - ③ a declared fallback plus an exhaustion check for any source with no SLA;
   - ④ **build the FOMC-date base rate** from federalreserve.gov dates, and verify 2024-09-18 first;
   - ⑤ **NEW:** a leg that borrows a conditioned base rate carries the same void clause, or states the unconditional prior beside it.
3. **L441 follow-through:** PROME implements the FORGE `AVG_STEEPNESS` vintage and re-check (spec in KB-VIO-310). **Build the KB-VIO-032 rolling percentile** alongside the static band; it is additive.
4. **Will-facing artifacts: WQ-259 is Will's call.** ⚠️ **The published pages were last refreshed 2026-08-18** (commit `d1bab0c8b`), not 7/30. The repo sources were refreshed to 9/14 closes and **never redeployed**. So the published pages show a pre-FOMC regime, the pre-grade letter and a stale score.
5. Regular-hours VIX options OI (H-new, untested).
6. Tooling debt:
   - pre-open TICK-row defect not fixed in code (this session avoided it by not running boot);
   - no guard contract on `m1m2_settle_date`;
   - false-zero COR1M d/d;
   - cheap-tail use-time mirror check unwired;
   - **new:** yfinance served malformed index bars (^VIX 9/23 O/H/L = 0.00, and the 9/22 index bars were missing entirely). backfill's CBOE authority handled it; a yfinance-only consumer would not.
7. Research: Path-A F2 audit; H-carry event-conditioned RV study; L342 holiday-counter audit before Nov 26.

## OPERATING LIMITS

- **Session:** PROME WQ-184 Tier-1 due-row spawn (DOCKET **L278**), pre-open 9/24.
- ⚠️ **`boot.py` was deliberately NOT run in full.** Its thresholds, OVX, JPY and cheap-tail stages write a row stamped with today's date, and a pre-open run would write 9/23 data under 9/24 (KB-VIO-303 class). I ran only the stages that write nothing under today's date: `move.py --boot --strict`, `fred_fetch.py --summary`, `cftc_cot.py --boot`, `vx_daily_gapcheck.py`, `catalyst_countdown.py` and `validate_workbook.py`, plus `backfill.py --spot-only`. **Skipped stages are reported as skipped, not as clean.**
- **Inbox FULLY DRAINED (L0, every sender):** 4 items, all logged to `board_log.tsv` and moved with `git mv` to `processed/`.
  - PROME L441: **acted** (DECLARED, spec in KB-VIO-310).
  - WALTER SIG-W-20260919-001: **acted** (corrected part 2).
  - SIG-W-20260921-001: **noted** (INFO, SAM-owned, decays today).
  - SIG-W-20260921-008: **noted** (INFO, HENRY/RED-owned).
- ⛔ **$0 moved.** No trade, card, order or proposal. **No threshold was set, moved or fired.** The m1m2 green edge 5.6 is DECLARED with a vintage and re-check date; its value is unchanged.
- 🔴 **`closeout_guard` shows the CANARY_MAP contract RED on 3 ledgers, and that is intended this session.**
  - The ledgers: JPY_VOL and OVX are DARK at 6d; CHEAP_TAIL is DARK at 7d.
  - Why they were not refreshed: each one is keyed by the run date. A pre-open run on 9/24 would stamp 9/23 data as a 9/24 row, which is the KB-VIO-303 defect this desk has already hit twice.
  - **They clear at the next post-close boot.** Until then, their last values are dated in the dashboard and not presented as current.
- ℹ️ The thesis-currency advisory is over its review threshold (41 KB rows since v4.1, 3 retractions). It was **not re-read this session.** This is an advisory; it does not block. It is deferred to the next full session.
