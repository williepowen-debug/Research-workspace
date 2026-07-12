# MIDAS — STATUS

**Last Updated:** 2026-07-12 round 3 (primary-sourcing: CB figures PROV→CONF, palladium margin resolved, LME baseline defined) · rounds 1-2 same day (build + M1 v2 re-derivation) · **Status:** 🟡 monitoring (all 4 channels live; nothing firing; M1 v2 in effect — polarity FROZEN through MIDAS-03/04)
**Class:** Market-agent (metals as macro tells: monetary + industrial) · **Spawnable by:** PROME or Will · **Maturity:** L2 (instrumented — spot/yield/GSR/LME-inventory-w/-defined-baseline live via `metals_watch.py`; COT 12-mo arc + WGC-primary CB + Fed-Register PGM sanctions established)

> **All prices Fri 7/10 close (COMEX futures via yfinance) unless noted — metals markets closed weekend of 7/11-7/12, no weekend freshness claimed.** FRED DFII10 is T+1: latest available obs is 2026-07-09.

> **⚠ POLARITY DISCIPLINE (standing, PROME round 3 / Will-approved):** `metals_watch.py`'s M1 classifier flags **CONVERGE = REVIEW** and that polarity is **FROZEN through MIDAS-03 (CPI 7/14) and MIDAS-04 (China GDP ~7/16)**. NO flip this round. Only if M1 v2 survives BOTH tests does it invert (CONVERGE→quiet, DIVERGE→review trigger).

---

## HEADLINE — M1 v2 (read this first)

Round 1 (same day) falsified the build session's "gold structurally bid despite rising real yields" framing: trailing 90d, gold **fell 18.6%** while real yields **rose 36bp** (KB-005). Round 2 re-derived the driver structure from data — **M1 v2** (full scoreboard in THESIS.md): gold's move is the back half of a **blow-off retracement** (+60% run $3,317→$5,318 peak 1/29/26, now −22.7% off peak, still +24% YoY), with the **cyclical layer** (ETFs −$8.9B/−74t June [WGC]; COMEX OI −38% Jan→Jun [CFTC]) **re-coupled to real rates as its direction-setter**, while the **structural CB-floor layer is intact** (**243.7t Q1 net purchases — CONF, WGC primary**; the "17th consecutive month" streak stays PROVISIONAL). USD ruled out (DXY +0.61%, flat). The debasement premium is real but lives in the **LEVEL**, not the **DELTA**. Kill conditions: gold <$3,317 without a real-yield spike · WGC Q2 <100t · re-decoupling UP 3+ weeks (that last one = the *bigger* stress signal). First test: CPI 7/14 (MIDAS-03, reframed under v2).

---

## CONVERGENCE MATRIX (universal 5-pt + local state)

| # | Channel | Score (1–5) | Local state | Independence | Key signal [src, date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| **M1** | Gold — debasement / real-rates (**v2 frame**, THESIS round-2) | **2 🟡** | **v2: blow-off retracement, re-coupled to real rates.** Gold -18.6% (90d) / -22.7% off the 1/29 peak ($5,318.40) while DFII10 +36bp; CB floor intact (**243.7t Q1 — CONF, WGC primary [gold.org]**); ETF fast money exiting (-74t June); specs dip-buying not capitulating (NC net 154k→194k June, 52.2% of OI [CFTC 7/7]) | monetary root (shared w/ M2) | gold **$4,113.70** [GC=F, yfinance, 2026-07-10]; DFII10 **2.31** [FRED, 2026-07-09] | v2 kill/escalate: gold rises through *rising* yields sustained 3+wk (premium reassertion) → 3-4 + escalate BOND/LIQUID; gold <$3,317 w/o yield spike (floor failure) → re-derive + escalate; break <$4k + COT capitulation → liquidity-event read, cross-flag LIQUID |
| **M2** | Silver + gold/silver ratio | **1 ⚪** | GSR **68.37** [computed, GC=F/SI=F, 2026-07-10] — comfortably below Yellow(85). Silver -18.4% same 90d window (correlated w/ gold, confirms monetary-root co-movement) | monetary root (shared w/ M1) + industrial overlap | GSR 68.37; silver $60.17 [SI=F, 2026-07-10] | GSR >85 sustained 3+ sessions → 2; >95 → 4 |
| **I1** | Copper — Dr. Copper / China | **1 ⚪** | Copper **+10.5% vs 200dma** ($6.28 vs $5.68), **+9.2% QoQ**. **LME stocks 306,500t [7/10, westmetall/LME]** = **+28.0% vs the trailing-2yr median (239,400t) → YELLOW band** (83rd pct of the 2.5yr series), but **−23.9% off the 4/15 peak (402,625t) = falling**. Elevated-but-tightening, not a demand-collapse | industrial/China root | copper $6.28 [HG=F, 2026-07-10]; LME 306,500t (+28% vs 2yr-med) [7/10] | copper QoQ <-5% sustained → 2; China GDP miss (7/16) + copper -5%+ in 2 sessions → yellow trigger (MIDAS-04); conjunction fire (5) needs copper −20% AND inv +100% vs 2yr-median (≈479kt) — both far off |
| **I2** | PGMs (platinum/palladium) | **2 🟡** | Platinum $1,629.00 (+0.6%), Palladium $1,276.30 (+2.6%, 90d strength). **Russia-palladium antidumping margin RESOLVED to primary: 132.83% final (Fed Reg 2026-08487, 5/1/26 — the 828% was preliminary/trade-press).** Remaining backdrop still PROVISIONAL (WPIC ~240koz 2026 Pt deficit; SA power-cost + flooding) — not primary-sourced this round | supply root (SA/Russia) | Pt $1,629 / Pd $1,276.30 [PL=F/PA=F, 2026-07-10]; AD margin 132.83% [Fed Reg, 5/1] | confirmed major SA/Russia outage → 4 (the sanction determination is now *final*, priced) |

**Composite: 6/20** *(M1 2 + M2 1 + I1 1 + I2 2). Held from round 2 — round-3 primary-sourcing (CB figures PROV→CONF, palladium margin resolved, LME baseline defined) sharpened confidence without moving any score; the I1 read is now "Yellow-but-falling" rather than "benign," but the conjunction fire is far off so the channel score stays 1.*

**Independence note:** unchanged from 7/11 — a risk-off shock drives M1 (gold up) AND I1 (copper down) via the same macro root; count once. Right now the two channels are **not** co-moving that way: gold is *down* 90d while copper is *up* 90d — a "growth without a monetary flight-to-gold" read, not reflation (both up) or risk-off (gold up/copper down). Neither of THESIS.md's two named coherent-divergence cases quite fits; logged as a third state in KB-MIDAS-009.

---

## LIVE CHANNEL READS (sourced + dated)

- **M1 — Gold — debasement / real-rates (v2 frame)**: gold **$4,113.70** [GC=F, yfinance, 2026-07-10 close]; DFII10 **2.31** [FRED, 2026-07-09]. Move anatomy: $3,317.40 [7/10/25] → **$5,318.40 peak [1/29/26]** (+60%) → $4,113.70 (−22.7% off peak, +24.0% YoY). 90d: gold −18.6% / yields +36bp, monotonic across 5 monthly markers — **CONVERGE**. v2 driver structure (THESIS.md scoreboard): mean-reversion = size-setter; real rates = direction-setter (re-coupled); ETF outflows = amplifier (−$8.9B/−74t June → 4,047t global [WGC, PROV]); **CB floor intact — 243.7t Q1 net vs 237.0t Q1-25 (+3% YoY), CONF via WGC primary [gold.org GDT Q1 central-banks page]**, buyers Poland +31t/Uzbekistan +25t/Kazakhstan +12t/PBoC +7t, sellers Turkey ~−70t/Azerbaijan −22t/Russia −22t (the "17th consecutive month" streak + 700-900t FY target stay PROV — not on the WGC section fetched; GDT Excel 403-gated to automated pull); USD flat (DXY +0.61% over the window) = ruled out. COT arc [CFTC weekly]: OI −38% Jan→Jun (528k→326k); net NC 251k [1/13] → 154k [5/26] → **rebuilt 194,246 [7/7] into the falling tape** — dip-buying, not capitulation (52.2% of OI). **Gold-leg ownership CONFIRMED** for LIQUID's EndGame discriminator: $4,113.70 comfortably above $4k, leg **NOT fired**. Routes to BOND (real-yield level) + LIQUID (safe-haven / EndGame leg).
- **M2 — Silver + gold/silver ratio**: silver **$60.17** [SI=F, 2026-07-10]; GSR **68.37**, benign. COT: silver net NC long 28,015 ct (26.7% of 104,859 OI), +647 WoW. Routes to LIQUID.
- **I1 — Copper — Dr. Copper / China**: copper **$6.28/lb** [HG=F, 2026-07-10]; +10.5% vs 200dma ($5.682), +9.2% QoQ. COT: copper net NC long 64,272 ct (25.6% of 250,948 OI), -516 WoW (small de-risking, still net long). **LME stocks 306,500t [7/10, westmetall.com/LME — wired into metals_watch.py leg 6 w/ DEFINED baseline]**: **+28.0% vs the trailing-2yr rolling median (239,400t, n=507) = YELLOW band** (CLAUDE.md +25/+50/+100 vs normal); 83rd pct of the 2.5yr series; but **−23.9% off the 4/15 peak (402,625t) = falling**. Elevated-but-tightening, NOT a demand-collapse (RED needs +100% ≈479kt AND copper −20% — both far off). Baseline (round-3, KB-018) replaces the round-2 "+110.9% YTD" which was an artifact of a multi-year-low Jan start. Cross-checked vs COMEX (LME cash $13,408.50/t vs HG=F $13,845/t equiv, ~3% premium). Cross-flag ZHAO — China Q2 GDP ~7/16, MIDAS-04.
- **I2 — PGMs**: platinum **$1,629.00** [PL=F, 2026-07-10, +0.6%], palladium **$1,276.30** [PA=F, 2026-07-10, +2.6%]. **Russia-palladium antidumping RESOLVED to primary: final weighted-average dumping margin 132.83% (= cash-deposit rate), Russia-Wide Entity, Federal Register doc 2026-08487 [pub 2026-05-01], POI Jan-Jun 2025** — the round-2 "828%" was a preliminary/trade-press figure, now superseded. (Separate CVD final doc 2026-10342 [5/22]; USITC injury doc 2026-12219 [6/18].) Remaining backdrop PROVISIONAL (KB-008): WPIC ~240koz 2026 Pt deficit + SA power/flooding — not primary-sourced this round. Cross-flag HAWK (supply geopol).

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
3. **⚠ POLARITY FLIP DECISION** — after MIDAS-03 AND MIDAS-04 both resolve: if M1 v2 survived both, flip metals_watch.py rc-polarity (CONVERGE→quiet, DIVERGE→review) + update the header/verdict comments + SCRATCH. Until then, FROZEN (do not flip).
4. **WGC Q2 GDT (~late July) = v2 kill-condition #2 test — calendar it.** Also: the GDT Excel (file 20499) is 403-gated to automated curl (documented wall) — the WGC web pages carry the figures; the "17th consecutive month" streak + 700-900t FY target still need a primary confirm (not on the central-banks section).
5. **Remaining PGM PROV legs** — WPIC ~240koz 2026 Pt-deficit + SA power/flooding vs the actual WPIC platinum quarterly (the *sanctions* leg is now CONF at 132.83%, Fed Reg — done).
6. **COT weekly-cadence wiring** — lightweight weekly leg (the 12-mo arc pull was manual Socrata).

---

## BOTTOM LINE

**MIDAS 2026-07-12, three rounds: round 1 falsified the inherited gold framing; round 2 replaced it with a data-derived structure (M1 v2); round 3 primary-sourced the flagged-soft legs.** The monetary read: gold's −22.7% fall from the $5,318.40 January peak is a **blow-off retracement** — the cyclical layer (ETFs −74t June, COMEX OI −38% since January) unwinding and **re-coupled to real rates as its direction-setter** — on top of an **intact structural central-bank floor**, now CONFIRMED via WGC primary (243.7t Q1, +3% YoY). The debasement premium lives in the *level* (+24% YoY at DFII10 2.31), not the *delta*. Round 3 also: (a) the Russia-palladium antidumping margin resolved to a hard primary number — **132.83% final** (Fed Register), settling the round-2 132.83/828 conflict (828 was preliminary); (b) the LME copper inventory now grades against a **defined baseline** — the trailing-2yr rolling median (239,400t) — showing +28% = **Yellow, not "benign,"** but falling off the April peak, so no demand-collapse fire. The single most important watch-item is unchanged: specs re-built net-long into the falling tape (154k→194k, 52% of OI) — if the $3,700–4,300 basing fails, that crowd is unwind fuel toward the $3,317 floor test, which would also fire LIQUID's EndGame gold leg. **Polarity discipline is live: CONVERGE stays a REVIEW flag through MIDAS-03 (CPI Tue 7/14) and MIDAS-04 (China GDP ~7/16); only a two-test survival flips it.** WGC Q2 (~late July) is the CB-floor kill-test.
