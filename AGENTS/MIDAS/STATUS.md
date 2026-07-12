# MIDAS — STATUS

**Last Updated:** 2026-07-12 round 2 (M1 v2 re-derivation + LME inventory wall broken; round 1 same day: `metals_watch.py` built + first live baseline) · **Status:** 🟡 monitoring (all 4 channels live; nothing elevated; M1 re-derived — THESIS.md M1 v2)
**Class:** Market-agent (metals as macro tells: monetary + industrial) · **Spawnable by:** PROME or Will · **Maturity:** L2 (instrumented — spot/yield/GSR/LME-inventory live via `metals_watch.py`; COT baseline + 12-mo arc established; PGM-supply confirmation + WGC primary pulls still owed)

> **All prices Fri 7/10 close (COMEX futures via yfinance) unless noted — metals markets closed weekend of 7/11-7/12, no weekend freshness claimed.** FRED DFII10 is T+1: latest available obs is 2026-07-09.

---

## HEADLINE — M1 v2 (round 2, read this first)

Round 1 (same day) falsified the build session's "gold structurally bid despite rising real yields" framing: trailing 90d, gold **fell 18.6%** while real yields **rose 36bp** (KB-005). Round 2 re-derived the driver structure from data — **M1 v2** (full scoreboard in THESIS.md): gold's move is the back half of a **blow-off retracement** (+60% run $3,317→$5,318 peak 1/29/26, now −22.7% off peak, still +24% YoY), with the **cyclical layer** (ETFs −$8.9B/−74t June [WGC]; COMEX OI −38% Jan→Jun [CFTC]) **re-coupled to real rates as its direction-setter**, while the **structural CB-floor layer is intact** (243.7t Q1 net purchases, 17th consecutive month [WGC, PROVISIONAL]). USD ruled out (DXY +0.61%, flat). The debasement premium is real but lives in the **LEVEL**, not the **DELTA**. Kill conditions: gold <$3,317 without a real-yield spike · WGC Q2 <100t · re-decoupling UP 3+ weeks (that last one = the *bigger* stress signal). First test: CPI 7/14 (MIDAS-03, reframed under v2).

---

## CONVERGENCE MATRIX (universal 5-pt + local state)

| # | Channel | Score (1–5) | Local state | Independence | Key signal [src, date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| **M1** | Gold — debasement / real-rates (**v2 frame**, THESIS round-2) | **2 🟡** | **v2: blow-off retracement, re-coupled to real rates.** Gold -18.6% (90d) / -22.7% off the 1/29 peak ($5,318.40) while DFII10 +36bp; CB floor intact (243.7t Q1 [WGC, PROV]); ETF fast money exiting (-74t June); specs dip-buying not capitulating (NC net 154k→194k June, 52.2% of OI [CFTC 7/7]) | monetary root (shared w/ M2) | gold **$4,113.70** [GC=F, yfinance, 2026-07-10]; DFII10 **2.31** [FRED, 2026-07-09] | v2 kill/escalate: gold rises through *rising* yields sustained 3+wk (premium reassertion) → 3-4 + escalate BOND/LIQUID; gold <$3,317 w/o yield spike (floor failure) → re-derive + escalate; break <$4k + COT capitulation → liquidity-event read, cross-flag LIQUID |
| **M2** | Silver + gold/silver ratio | **1 ⚪** | GSR **68.37** [computed, GC=F/SI=F, 2026-07-10] — comfortably below Yellow(85). Silver -18.4% same 90d window (correlated w/ gold, confirms monetary-root co-movement) | monetary root (shared w/ M1) + industrial overlap | GSR 68.37; silver $60.17 [SI=F, 2026-07-10] | GSR >85 sustained 3+ sessions → 2; >95 → 4 |
| **I1** | Copper — Dr. Copper / China | **1 ⚪** | Copper **+10.5% vs 200dma** ($6.28 vs $5.68), **+9.2% QoQ**. **LME stocks 306,500t [7/10, westmetall/LME — wall broken round-2]**: −23.9% off the 4/15 peak (402,625t), drawing down ~3 months = tightening, growth-consistent; +110.9% YTD but off a multi-year-low Jan base (145,325t) | industrial/China root | copper $6.28 [HG=F, 2026-07-10]; LME 306,500t [7/10] | copper QoQ <-5% sustained → 2; China GDP miss (7/16) + copper -5%+ in 2 sessions → yellow trigger (MIDAS-04); conjunction fire (5) needs copper −20% AND inv +100% *vs a defined baseline — definition owed* |
| **I2** | PGMs (platinum/palladium) | **2 🟡** | Platinum $1,629.00 (+0.6%), Palladium $1,276.30 (+2.6%, 90d strength). Structural backdrop (PROVISIONAL, WebSearch — needs primary verify): WPIC ~240koz 2026 Pt deficit; SA power-cost + flooding constraints; US Commerce anti-dumping action on Russian Pd (rate unreconciled: 132.83% vs 828% cited by different sources/stages) | supply root (SA/Russia) | Pt $1,629 / Pd $1,276.30 [PL=F/PA=F, 2026-07-10] | confirmed major SA/Russia outage or finalized sanction determination → 4 |

**Composite: 6/20** *(M1 2 + M2 1 + I1 1 + I2 2). Down from the 7/11 provisional 9/20 — reflects the M1 correction (3→2) and the other three channels resolving to genuinely benign reads (2→1 for M2/I1) rather than "gap" placeholders. All 4 channels now carry a dated live read for the first time.*

**Independence note:** unchanged from 7/11 — a risk-off shock drives M1 (gold up) AND I1 (copper down) via the same macro root; count once. Right now the two channels are **not** co-moving that way: gold is *down* 90d while copper is *up* 90d — a "growth without a monetary flight-to-gold" read, not reflation (both up) or risk-off (gold up/copper down). Neither of THESIS.md's two named coherent-divergence cases quite fits; logged as a third state in KB-MIDAS-009.

---

## LIVE CHANNEL READS (sourced + dated)

- **M1 — Gold — debasement / real-rates (v2 frame)**: gold **$4,113.70** [GC=F, yfinance, 2026-07-10 close]; DFII10 **2.31** [FRED, 2026-07-09]. Move anatomy: $3,317.40 [7/10/25] → **$5,318.40 peak [1/29/26]** (+60%) → $4,113.70 (−22.7% off peak, +24.0% YoY). 90d: gold −18.6% / yields +36bp, monotonic across 5 monthly markers — **CONVERGE**. v2 driver structure (THESIS.md scoreboard): mean-reversion = size-setter; real rates = direction-setter (re-coupled); ETF outflows = amplifier (−$8.9B/−74t June → 4,047t global [WGC, PROV]); CB floor intact (243.7t Q1 net, 17th consecutive month [WGC GDT Q1, PROV]); USD flat (DXY +0.61% over the window) = ruled out. COT arc [CFTC weekly]: OI −38% Jan→Jun (528k→326k); net NC 251k [1/13] → 154k [5/26] → **rebuilt 194,246 [7/7] into the falling tape** — dip-buying, not capitulation (52.2% of OI). **Gold-leg ownership CONFIRMED** for LIQUID's EndGame discriminator: $4,113.70 comfortably above $4k, leg **NOT fired**. Routes to BOND (real-yield level) + LIQUID (safe-haven / EndGame leg).
- **M2 — Silver + gold/silver ratio**: silver **$60.17** [SI=F, 2026-07-10]; GSR **68.37**, benign. COT: silver net NC long 28,015 ct (26.7% of 104,859 OI), +647 WoW. Routes to LIQUID.
- **I1 — Copper — Dr. Copper / China**: copper **$6.28/lb** [HG=F, 2026-07-10]; +10.5% vs 200dma ($5.682), +9.2% QoQ. COT: copper net NC long 64,272 ct (25.6% of 250,948 OI), -516 WoW (small de-risking, still net long). **LME stocks 306,500t [7/10, westmetall.com/LME — wall broken round-2, wired into metals_watch.py leg 6]**: 2026 arc 145,325t [1/2] → peak 402,625t [4/15] → −23.9% drawdown to current — ~3 months of tightening, growth-consistent; cross-checked vs COMEX (LME cash $13,408.50/t vs HG=F $13,845/t equiv, ~3% COMEX premium). Cross-flag ZHAO (China demand) — China Q2 GDP due ~7/16 (NBS calendar), MIDAS-04 registered as the reaction-test resolver.
- **I2 — PGMs**: platinum **$1,629.00** [PL=F, 2026-07-10, +0.6%], palladium **$1,276.30** [PA=F, 2026-07-10, +2.6%]. Structural backdrop PROVISIONAL (KB-MIDAS-008) — needs primary-source verification (Federal Register / Commerce Dept determination, WPIC platinum quarterly) before treating as EMPIRICAL. Cross-flag HAWK (supply geopol).

**Inherited cross-agent context:** BOND owns the real-rate level MIDAS's M1 diverges (or, currently, does NOT diverge) from; ZHAO owns the China demand MIDAS's copper reads; LIQUID owns the EndGame liquidity-event discriminator whose gold leg MIDAS now confirms live.

---

## EXIT / INVALIDATION (standing-rule-vs-state triad)

| Channel | Standing rule | Current state @ level | FIRED? |
|---|---|---|---|
| M1 (v2) | v2 kill-triad: gold <$3,317 w/o yield spike (floor failure) · WGC Q2 <100t (CB collapse) · gold re-decouples UP 3+wk (re-coupling dead → premium reassertion) | gold $4,113.70, +24% above the $3,317 shelf; CB Q1 243.7t; re-coupled (CONVERGE) this window | **NOT-FIRED** (all three legs comfortably clear) |
| M2 | gold/silver ratio >95 sustained (risk-off) | GSR 68.37, well below Yellow(85) | NOT-FIRED |
| I1 | copper −20% AND LME inventory +100% (demand collapse) | copper **+9.2% QoQ**; LME stocks **falling** −23.9% off the 4/15 peak (306,500t [7/10]) | NOT-FIRED (both legs directionally opposite) |
| I2 | major SA/Russia PGM supply outage/sanction | structural deficit + sanctions proceeding ongoing, no confirmed acute outage | NOT-FIRED |

**Fired-count: 0 of 4.** **Thesis-kill vs channel-kill:** v1's premium claim (gold bid *above* real rates at the margin) was falsified round-1 and REPLACED by v2 (round-2) rather than the channel dying — the debasement thesis migrated from the DELTA to the LEVEL. v2 now carries its own kill-triad (row above), each leg testable on a dated release: CPI 7/14 (MIDAS-03), WGC Q2 GDT ~late July, the $3,317 shelf continuously.

**Cleanest bidirectional flip (BRENT discipline), v2 edition:** if gold *bases in $3,700–4,300 while DFII10 holds 2.2–2.5*, v2 is confirmed (floor forming above the pre-run shelf); if gold *breaks below $3,317 without a real-yield spike*, v2's structural floor is falsified. And in the other direction: a sustained UP-decoupling re-falsifies v2's "re-coupled" claim — which would be a bigger monetary-stress signal than v2 itself (escalate, don't celebrate).

---

## OPEN ON MIDAS (next session)

1. **MIDAS-03 resolution (CPI 7/14)** — same-day gold-vs-real-yield sign check under the v2 framing, resolves by 7/16 (DFII10 T+1 publish). First v2 test.
2. **MIDAS-04 resolution (China Q2 GDP ~7/16)** — verify exact NBS release date/time; copper 2-session reaction test, resolves by 7/20.
3. **WGC primary pulls (upgrade PROVISIONAL → EMPIRICAL)** — GDT Q1 CB data file + goldhub ETF-flows CSV (KB-014/015 are WebSearch/WebFetch-summarized; two passes consistent but L-05 says pull raw). **WGC Q2 GDT (~late July) = v2 kill-condition #2 test — calendar it.**
4. **I2 primary-source verification** — reconcile the 132.83%/828% Russian-palladium tariff figures (Federal Register / Commerce determination); WPIC 240koz Pt-deficit vs the actual WPIC quarterly.
5. **I1 inventory-threshold baseline definition** — "+100% vs normal" has no defined normal (Jan base was a multi-year low); proposal: rolling 2-yr median of LME stocks. Now data-feasible (westmetall series is live in metals_watch.py).
6. **COT weekly-cadence wiring** — lightweight weekly leg (the 12-mo arc pull this session was manual Socrata).
7. **metals_watch.py rc-polarity revisit** — CONVERGE currently trips REVIEW (v1 logic, kept deliberately until v2 survives MIDAS-03/04); if v2 holds, flip: CONVERGE = quiet, DIVERGE = REVIEW.

---

## BOTTOM LINE

**MIDAS 2026-07-12, two rounds: round 1 falsified the inherited gold framing; round 2 replaced it with a data-derived structure (M1 v2).** The monetary read now: gold's −22.7% fall from the $5,318.40 January peak is a **blow-off retracement** — the cyclical layer (ETFs −74t in June, COMEX OI −38% since January) unwinding and **re-coupled to real rates as its direction-setter** — sitting on top of an **intact structural central-bank floor** (243.7t bought in Q1, 17th consecutive month). The debasement premium is real but it lives in the *level* (gold +24% YoY with real yields at 2.31), not the *delta*. The single most important watch-item: specs re-built their net-long into the falling tape (154k→194k contracts in June, 52% of OI) — if the $3,700–4,300 basing zone fails, that crowd is unwind fuel toward the $3,317 structural-floor test, which would also fire LIQUID's EndGame gold leg on the way. The industrial channel is genuinely benign: copper +9.2% QoQ with LME stocks drawing down 24% from the April peak — tightening, growth-consistent, and now fully instrumented (the LME inventory wall broke this session via westmetall; wired into metals_watch.py). Next: CPI Tuesday is v2's first live test (MIDAS-03), China Q2 GDP Thursday is I1's (MIDAS-04); WGC Q2 in late July is the CB-floor test.
