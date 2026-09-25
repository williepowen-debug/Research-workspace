# VIOLET STATUS

**As of:** 2026-09-24 21:1x ET, **post-close**. Market basis: the **September 24 session close** for the VIX complex and MOVE. Every cell dated otherwise says so. Thesis **v4.1.1**. Grade records: [part 1](research/2026-09-17_VIO-FOMC-0916_GRADE_part1.md) · [part 2](research/2026-09-18_VIO-FOMC-0916_GRADE_part2.md) · [part 3: LEG 2 + WHOLE LETTER](research/2026-09-24_VIO-FOMC-0916_GRADE_part3.md). Prior state (9/23-close basis) is in git.

⚠️ **CBOE history has NOT published 9/23 OR 9/24.** `backfill.py --spot-only` this session: 0 corrections, 0 SETTLE stamps for the last two rows. **9/23 and 9/24 VIX-complex cells are the CBOE delayed-quote API + yfinance readings the boot pulled post-close;** the `VX_DAILY` rows carry no SETTLE stamp. ⛔ **Re-pull at next boot** — leg 2 KILL still rests on the 9/23 non-history reading (margin +2.28 points remains large).

## BOTTOM LINE

🔴 **Two-day bond selloff with rates vol pricing it in full; equity vol has moved less.** 10Y yield **4.96 [9/22] → 5.11 [9/23] → 5.18 [9/24] = +22bp over 2 sessions** [CONF HENRY/BOND per Treasury H.15]. TLT 81.75 → 80.46 → **79.42** = **−2.9% cumulative** on 59M volume 9/24. MOVE 78.56 → 95.45 → **104.58** = +33.1% cumulative. **MOVE and the rates move are COINCIDENT, not leading** — same-day jumps both sessions (MOVE +21.5% & VIX +6.83% on 9/23; MOVE +9.55% & VIX +3.23% on 9/24); MOVE is doing what MOVE does when duration sells off. Rates substance is HENRY / BOND, not mine. *(Prior draft carried the ^TNX vendor series unlabeled at +20bp 2d; corrected to H.15 basis per HENRY peer-read 9/24.)*

⚠️ **Scope note on the "ledger max" language:** the MOVE ledger is 58 rows starting 2026-07-06 (2.7 months). MOVE 104.58 is p98.3 of THAT window; it is not "record" in any historical sense (MOVE routinely printed 140-200 in the 2022-2023 regime). The direction is real; the "record" shape is a sample artifact of a short ledger.

🟠 **VVIX crossed above 90 for the first time in the post-FOMC run.** 83.17 [9/22] → 88.60 [9/23] → **90.57 [9/24]**. Below the >100 watch level. The **VIX3M/VIX ratio compressed further** — 1.2393 [9/22] → 1.193 [9/23] → **1.1761 [9/24]** — the compression flagged in SCRATCH NEXT-SESSION #2 has confirmed for a second bar. Curve is still in contango; no inversion.

🟠 **VIX rose 3.23% on the day to 15.67** (from 15.18), regime shifted COMPLACENCY → LOW_VOL. The vol-complex response over 2d: VIX +10.3%, VVIX +8.9%, VIX3M/VIX −5.1%. **The observation is a SPREAD: rates vol has repriced further than equity vol on the same catalyst.** Whether equity vol follows depends on the bond selloff's driver (HENRY/BOND). ⚠️ **Prior draft said "rates-vol is leading equity vol" — walked back;** that is a temporal claim the data doesn't support.

🟠 **CCC widened 10.75 [9/22] → 10.93 [9/23 FRED] = +18bp (~2.6σ, 60d daily std 6.9bp).** Above p95 of the 519d FRED series (10.49) and a 30d high (prior 10.85 on 9/15). BIN-B block already active (CCC ≥ 9.55, standing). CCC−BB 9.34 pp. **The rest of the tail did not move meaningfully:** HY 2.68 → 2.73 (+5bp, ~1.5σ), BB 1.56 → 1.59 (+3bp, ~1σ), IG 0.77 → 0.77 flat. HY at 2.73 is p25 of the 519d series — historically tight. **Only CCC moved.** LIQUID owns the interpretation. ⚠️ **Prior draft said "tight-tail cohort with rates-vol firing preceded credit non-confirmation" — walked back;** no base rate behind that claim, and KB-VIO-071 Path B is defined by credit NOT widening, so the citation would have been wrong even if the base rate existed.

**Thesis v4.1.1 stands. Book flat, no trade proposed, no threshold moved. Convergence 27 → 28/50 (VVIX and front-curve up 1 each, JPY down 1). NEXUS CROSS-DOMAIN to HENRY / LIQUID / BRENT / BOND updated below.**

⚠️ **Prior draft's "signature thresholds" (VVIX toward 100, VIX3M/VIX toward 1.10, MOVE ≥100) — walked back and stay withdrawn.** RQ #8 v1 (KB-VIO-311) HAS BEEN SUPERSEDED by KB-VIO-312 after a CATO-caught / PROME-verified return-clock defect: v1 cohort forward return spanned T-1→T+k while unconditional baseline spanned T→T+k; the two clocks don't compare. **Headline verdict (Will 2026-09-25 01:01 ET):** ***"The corrected ten-event sample does not establish a forward VIX signal in either direction."*** Evidence table on matched T→T+k windows: T+1 +0.005σ, T+3 −0.28σ, T+5 −0.41σ, T+10 −0.24σ. The v1 "T+1 +12.4% / 1.68σ" is WITHDRAWN — it was the +8.9% event-day co-move carried into a two-session return. What survives: MOVE 2d ≥30% events coincide with a ~+9% median VIX event-day co-move; the ten-event sample does not establish forward transmission either way. RQ #8 **PARKED** at Will's direction; RQ #8a-d HELD, none started. Report: `research/2026-09-24_RQ-8_move-2d-jump-forward-vix.md` §1a-§7 (KB-VIO-312).

**WQ-259 refresh (Will-approved 2026-09-24) — CONDITION NOT MET.** The packet gates republish on CBOE confirming the 9/23 close; CBOE has not published it. Deferred to the next post-close boot after CBOE catches up. **Rider (CLAUDE.md:194) — DONE this session.**

## SIGNAL DASHBOARD

| Metric | Value | As of | Source / interpretation |
|---|---:|---|---|
| VIX | **15.67**; +3.23% vs 15.18 (9/23) | Sep 24 close | [CONF] CBOE delayed-quote + yfinance × three paths; history CSV not yet posted. Regime LOW_VOL |
| VIX9D | **14.11**; +4.9% | Sep 24 close | [CONF]; 9/23 13.45 |
| VIX9D / VIX | **0.9004** | Sep 24 | Same-date calc; still under 1.0 |
| VIX3M / VIX6M | **18.43 / 20.35** | Sep 24 close | [CONF]; 9/23 18.11 / 20.11 |
| VIX3M / VIX | **1.1761** (9/23: 1.193; 9/22: 1.2393) | Sep 24 | Contango compressing 2 sessions. Not inverted |
| VVIX | **90.57**; +2.2% vs 88.60 | Sep 24 close | [CONF]. **First close above the 90 cheap-line since the post-FOMC run began.** Watch line remains >100 |
| SKEW daily | **146.04** [9/24] · 146.15 [9/23] · **144.80** [9/22 CBOE SETTLE] | Sep 22–24 | 9/18 CBOE SETTLE 148.10. Below 150 on every bar since 9/15 |
| SKEW 20-session mean | **147.46** (8/25→9/22) | Sep 22 | [CONF] VX_DAILY CBOE bars; will refresh after CBOE publishes 9/23–9/24 |
| Adjusted M1:M2 | **+4.17%** [9/24 SETTLE], VX/V6/VX/X6 | Sep 24 settle | [CONF] `thresholds.py`. **BELOW_AVG** vs the 5.6 average (KB-VIO-310); rising from +3.679% at 9/18 |
| MOVE | **104.58**; +9.13 (+9.55%) vs 95.45 | Sep 24 | [CONF] investing.com PRIMARY, yfinance secondary agrees. p98.3 of the **58-row ledger** (2026-07-06→9/24) — not "record" historically (MOVE regularly printed 140-200 in 2022-2023 SVB regime). Margins: +32.17 over F1 (72.41) · +29.08 over confirm-3 (75.50) |
| OVX | **54.45**, ratio **3.47** (p97.0), p89.7 · FIRE | Sep 24 | [CONF] `ovx_read.py` boot leg. Gap 38.78 (p94.5). Oil-vol → equity-vol channel LOADED |
| JPY RV10 | **6.5%**, p29.1, CALM | Sep 24 | [CONF] `jpy_carry_vol.py`. USDJPY 158.26. Down sharply from 11.1% p72.6 [9/18] |
| COR1M / COR3M | **9.17 / 10.66** (COR30D 7.91) | Sep 24 SETTLE | [CONF] `implied_corr.py`. Constituent-vol[EST] 51.7 — DISPERSED |
| HY / CCC / BB OAS | **2.73 / 10.93 / 1.59%** | Sep 23 FRED | [CONF] FRED direct read. CCC−BB **9.34 pp**. BIN-B block standing. LIQUID owns. *(Prior draft carried 2.72/1.58 — 1bp rounding errors from summary output; corrected against series.)* |
| IG OAS | **0.77%** | Sep 23 FRED | [CONF] FRED direct. *(Prior draft carried 0.78 — 1bp error, corrected.)* |
| COT VIX positioning | Lev money net **−16,504**, p69.9; OI 446,060 | Sep 15 report | [CONF] CFTC TFF. Next report 9/22 publishes Fri 9/25 15:30 ET |
| VIX options C/P OI (forward 5) | 0.00 (post-close artifact) | Sep 24 after-hours | ⚠️ post-close OI=0 artifact (KB-VIO known caveat); use intraday runs for OI. Call vol 397k, Put vol 145k this run |

**Spot integrity:** `backfill.py --spot-only` this session: 2562 cell agreements against CBOE, 0 corrections, 0 blanks filled, 0 new SETTLE stamps. Two most recent rows (9/23, 9/24) not yet in CBOE history; 9/24 row basis stamp is `SETTLE` for m1m2 (VX futures settlement), spot is delayed-quote. `vx_daily_gapcheck` rc=0.

## GATE STATUS

| Instrument | State | Exact scope / next step |
|---|---|---|
| **VIO-FOMC-0916** | ⛔ **CLOSED: LETTER FAILED** | Verdict unchanged. Leg 2 KILL at −14.29% [9/23] — 9/24 close 15.67 is −11.52% off the 9/16 event close 17.71, so leg 2 KILL cannot flip on either the 9/23 or 9/24 reading. Letter sha256 `ead84431…` re-verified. Acceptance condition ⑤ (leg carrying a borrowed cohort must carry the void clause) stands |
| **Cheap-tail alert** | 🟣 **OPEN 4/4** (as of 9/22 CBOE basis) | L1 VVIX 83.17 ≤ 90 · L2 VIX 14.21 ≤ 16 · L3 SKEW 144.80 ≥ 140 · L4 nearest catalyst 6d (MU 9/30). ⚠️ **The 9/22 basis is the last CBOE-SETTLE row;** on the newer readings VVIX 90.57 exceeds L1 and VIX 15.67 stays under L2 — this is the alert re-evaluating whether the window is still open. Not run against 9/24 pending CBOE 9/23/24 publication (SKEW 20-sess mean lags one CBOE cycle). **OPERATOR SURFACE, NOT A TRADE** — TERRY constructs, Will approves |
| F-B | **HELD** (window closed 9/16) | Unchanged. `fb_falsifier.py` threshold 17.84% ann |
| Coiled spring (STRICT / DIET) | NOT FIRING | SKEW 144.80–146.04 on every bar since 9/15; no ≥+10 ΔSKEW build |
| GATE-VIO-RV1 | RETIRED | F2-killed Aug 27 |
| RED-FT-10 | RED-OWNED | CBOE bars since 9/15: 146.61 · 145.95 · 145.70 · **148.10** (9/18) · 142.19 · 144.80 · 146.15 (9/23 yf) · 146.04 (9/24 yf). None ≥150. RED owns the count |
| RED-FT-06 | RED-OWNED | VIX 15.67 [9/24]; RED grades |
| KB-VIO-123 crack/fade tree | MOVE leg **above line, margin +29.08 confirm-3 / +32.17 F1** | Now 2 consecutive sessions. VVIX crossed 90 but not 120, VIX <20, curve compressing but not inverted, COT positioning not ≥95. **Credit leg (CCC 10.93) is LIQUID's** |
| BIN-A / BIN-B | BIN-A STUCK; **BIN-B block active** | CCC 10.93 [9/23 FRED T+1] |
| GATE-VIO-116 | RESOLVED July 16 | MOVE monitoring continues; no deployment authorisation |
| T9 self-falsifier | NOT MET | MOVE 104.58 far above the <66 line |

## CONVERGENCE MATRIX

**Convergence Score: 28/50** (10 vectors × 5), **+1 vs prior 27/50**. VVIX ⚪ 1 → 🟡 2 (crossed 90); front-curve ⚪ 1 → 🟡 2 (compression across 2 sessions); JPY 🟡 2 → ⚪ 1 (RV10 collapsed). Rates-vol stays 5, no longer one-day.

| Vector | Score | Current reasoning |
|---|---|---|
| Rates vol | 🔴🔴 **5** | MOVE **104.58** [9/24], p98.3 in 58-row ledger, +33.1% 2d cumulative. 10Y +22bp 2d [H.15 via HENRY/BOND]; TLT −2.9% 2d on 59M vol. Substance HENRY/BOND |
| SKEW / tail bid | 🔴 **4** | 20-session mean 147.46 elevated; latest bars 144.80 [CBOE 9/22] → 146.15/146.04 [yf 9/23–24], under 150 |
| Oil vol | 🔴 **4** | OVX 54.45, ratio 3.47 p97.0, gap 38.78 p94.5, FIRE. Sustained since 9/18 |
| Credit | 🟠 **3** | CCC 10.93 (+18bp, ~2.6σ, above p95 519d, 30d high); HY 2.73, BB 1.59, IG 0.77 all noise-band or flat — **only CCC moved** |
| Positioning | 🟠 **3** | ⚠️ 9/15 report: lev money p69.9. New report Fri 9/25 |
| Implied correlation | 🟡 **2** | COR1M 9.17, COR3M 10.66, dispersed; constituent-vol[EST] 51.7 |
| Equity concentration | 🟡 **2** | VULCAN's structural watch; WALTER SIG-007/014 negative-beta chart is INFO (HENRY/RED own) |
| VVIX | 🟡 **2** | **NEW 9/24: 90.57 crossed the 90 cheap-line.** Watch level >100 |
| Front curve | 🟡 **2** | **NEW 9/24: compression confirmed 2nd session** — 3M/VIX 1.2393 → 1.193 → 1.1761. Still contango |
| JPY carry vol | ⚪ **1** | RV10 6.5% p29.1 CALM. Fell sharply from 9/18. No confirm on ¥158 report |

## REGIME STATUS AND DRIFT

- **Price classification: LOW_VOL** (VIX 15.67 [9/24], from COMPLACENCY 14.21–14.87 across 9/18–9/22). No terminated regime of ≥60 sessions is asserted.
- **The post-FOMC vol path, from the 9/16 close (VIX 17.71):** −12.82% (9/17) → −16.37% (9/18) → −16.04% (9/21) → −19.76% (9/22 low) → −14.29% (9/23) → **−11.52% (9/24)**. **The vol premium is rebuilding — quietly and slowly — while rates-vol is running.** Not a stress event; not a resolution event; a cross-market read.
- 🔴 **The graded finding, final form:** the letter's legs 2, 3, 4 all failed on one event because the letter modelled a stress event. n=1 for **H-resolution-vs-stress**. Needs the FOMC-date base rate before it is graded again.
- 🟠 **9/23–9/24 confirm the rates-vs-equity-vol spread is not one-day.** Two consecutive p98-of-ledger MOVE prints, VIX3M/VIX compression across two sessions, VVIX crossing 90 — every one within-bounds so far (no inversion, no VVIX>120, no VIX>20). **Rates vol repriced further than equity vol on the same catalyst; MOVE and VIX moved SAME-DAY both sessions — not lead-lag.** Broadcast as CROSS-DOMAIN only, not as a VIOLET regime-shift. *(This line missed the walk-back in the first pass; HENRY peer-read caught it. Fixed 2026-09-24 22:5x ET.)*
- 🟠 **H-approach-vs-delivery** loses its 9/18 observation to +5.80% (KB-VIO-309). MOVE's 9/23–24 spike had no event to approach, so it is not evidence either way for that hypothesis.
- **Unadjudicated:** whether the 9/18 opex removed the dealer amplifier (HENRY) or a relief tape absorbed it (mine). KB-VIO-307 stands.

## POSITIONS

Last recorded VIOLET book: **FLAT**. `TRY-VIOLET-VIXCS` closed July 30; FORGE's September 10 mirror confirms the closure. **No broker refresh, no order, no proposal this session; $0 moved.**

## RESEARCH QUEUE

1. **Next post-close boot: re-pull CBOE history** and stamp 9/23 and 9/24 with SETTLE. Leg 2 KILL cannot flip (VIX 15.67 [9/24] still >2 points inside the KILL margin).
2. **Read MOVE follow-through and any 3rd-day print.** Two p98-of-ledger prints in a row plus the underlying rates selloff (10Y +22bp 2d [H.15 via HENRY/BOND], TLT −2.9% 2d) is real; HENRY/BOND own the rates driver. **RQ #8 verdict (KB-VIO-312, PARKED at Will's direction 9/25):** ***"The corrected ten-event sample does not establish a forward VIX signal in either direction."*** Intuition thresholds remain unsupported. Continue to observe without a named signature.
3. **Write the next pre-registered letter against the FIVE acceptance conditions** (part 3 §5): partition state space · every cell fails against T-1 · fallback + exhaustion for no-SLA sources · FOMC-date base rate built from federalreserve.gov (verify 2024-09-18) · void-clause on any cohort-borrowing leg.
4. **L441 follow-through:** PROME implements the FORGE `AVG_STEEPNESS` vintage and re-check (spec in KB-VIO-310). Build the KB-VIO-032 rolling percentile alongside the static band; additive.
5. **WQ-259 half-satisfied:** rider (CLAUDE.md:194) fixed this session; artifact republish deferred to the next post-close boot after CBOE confirms 9/23–9/24.
6. Regular-hours VIX options OI (H-new, untested).
7. Tooling debt: pre-open TICK-row defect not fixed in code · no guard contract on `m1m2_settle_date` · false-zero COR1M d/d · cheap-tail use-time mirror check unwired · yfinance malformed index bars (9/22–9/23) handled by backfill's CBOE authority but a yfinance-only consumer would fail.
8. **RQ #8 rates-vol → equity-vol base-rate study — PARKED at Will's direction 2026-09-25 01:01 ET** (KB-VIO-312 supersedes KB-VIO-311; report `research/2026-09-24_RQ-8_move-2d-jump-forward-vix.md` §1a-§7; §1 pre-reg still frozen at `949fd172b`). **Verdict:** ***"The corrected ten-event sample does not establish a forward VIX signal in either direction."*** Evidence: matched-clock separations T+1 +0.005σ, T+3 −0.28σ, T+5 −0.41σ, T+10 −0.24σ. Contemporaneous event-day VIX co-move ~+9% median at T=0 is real but tautological. Rules PASS-a and FAIL simultaneously satisfied; §1a-B collision disclosure kept verbatim; 9/24 basis-dependent qualification (§1a-C) kept verbatim. **RQ #8a-d HELD; none started.**
9. Research: Path-A F2 audit; H-carry event-conditioned RV study; L342 holiday-counter audit before Nov 26.

## OPERATING LIMITS

- **Session:** post-close 9/24 catch-up per Will's ask. Full boot ran; every "NOT RE-READ" cell from the pre-open session is refreshed.
- **Inbox drained:** 3 items — PROME WQ-259 (acted: CLAUDE.md rider done, republish deferred pending CBOE); SIG-W-20260924-007 (info-only); SIG-W-20260924-014 (info-only, correction to -007). All logged and moved.
- ⛔ **$0 moved.** No trade, card, order or proposal. **No threshold set, moved or fired.** m1m2 average 5.6 remains DECLARED (KB-VIO-310).
- 🟢 **`closeout_guard` expected clean** — every canary was re-read. `MOVE`, `OVX`, `JPY_VOL`, `CHEAP_TAIL`, `IMPLIED_CORR`, `VIX_OPTIONS`, `VX_DAILY` all appended a 9/24 row.
- ℹ️ Thesis-currency advisory: 41 KB rows since v4.1, 3 retractions, over review threshold. **Not re-read this session** (advisory, does not block). Deferred to the next full session.

## Q2 CONTRIBUTION — Will-directed six-questions (DOCKET L477, needed-by Sat 9/26)

*LIQUID leads Q2 ("What is the first observation that would convince us stress is spreading?"); I contribute the vol leg. Constraints (per PROME packet 02:57 ET 9/25): existing data + existing gates only, no new thresholds near today's levels, no revival of the withdrawn "signature levels", no trade proposal.*

**Vol leg (VIOLET, one paragraph):** Under **ORDINARY REPRICING** the vol complex looks essentially like today: VIX in the LOW_VOL band, VIX3M/VIX contango >1.15, VVIX below the KB-VIO-123 crack line (120), SKEW 20-session mean elevated but no persistent >150 bars — MOVE can print elevated with none of these transmitting. Under a **DEVELOPING FEEDBACK LOOP** the sharpest existing observable is the pre-registered peak-marker line **VIX3M/VIX ≤ 1.00** (SIGNAL_INTAKE durable line; KB-VIO-034 falsification says this marks the top, not the onset — 553 events, 2.2% hit rate for +50% follow-through) firing together with **VVIX > 120** (KB-VIO-123 crack line, existing gate) on **two consecutive sessions**, while MOVE holds elevated. Neither is a new threshold: the inversion line sits 15% below the current VIX3M/VIX 1.1761 [9/24, delayed-quote] and the VVIX line 32% above 90.57 [9/24, delayed-quote]. **Observation window: 5-10 sessions from the qualifying MOVE spike**; beyond that the coincident window closes and ordinary repricing is the operating conclusion. **What counts AGAINST transmission (any one is disconfirming):** (a) VIX3M/VIX rising back toward 1.20 despite MOVE ≥85 sustained; (b) VVIX fading below 85 despite MOVE holding; (c) VIX 5-session cumulative change stays within ±5% while MOVE prints in the p95+ zone; (d) SKEW 20-session mean drops below 145 sustained. **On the parked RQ #8 base rates (n=10, 2002-2026, KB-VIO-312):** matched-clock forward VIX separations are 0.005σ / −0.28σ / −0.41σ / −0.24σ at T+1/3/5/10, so the ten-event sample does not establish a forward VIX signal in either direction from MOVE 2d ≥30% events — ordinary repricing is at least as likely as transmission on the historical record. **The existing gate that IS the transmission test is `VIX3M/VIX ≤ 1.00 AND VVIX > 120, both firing on two consecutive session closes within 10 sessions of the MOVE spike`** — if that fires, "stress is spreading" is supported by an existing peak-marker gate; if it does not fire within 10 sessions of the MOVE spike, ordinary repricing is the operating conclusion. This is not a trade proposal.

**One-line vol confirmation clause for LIQUID's prospective test:**
> Vol confirmation (VIOLET): **`VIX3M/VIX ≤ 1.00 AND VVIX > 120` both firing on the same session AND persisting to the next session's close, within 10 sessions of the qualifying MOVE spike.** Not a new threshold — both lines are pre-registered (SIGNAL_INTAKE durable line #1 for inversion; KB-VIO-123 for VVIX). Values as of 2026-09-24 delayed-quote: VIX3M/VIX 1.1761 (15% above inversion line), VVIX 90.57 (32% below the crack line).
