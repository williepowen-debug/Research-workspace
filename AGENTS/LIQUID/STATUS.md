# LIQUID STATUS
**Last Updated:** 2026-06-08 (live-tape catch-up from 5/20, ~19d stale) | **Agent:** LIQUID | **Status:** 🟡 **APO co-trigger RE-ARMING** (APO ran $130→$131.5, +3.1% on 6/8 annual-meeting day — re-crossed the $130 line; needs 3 sustained sessions to fire Trigger C); HY OAS 276bps (16bps above 260 kill — cushion NARROWING); Brent reversed $110→~$91 (reflation loop cooling); USD/JPY 160.30 crossed trigger; duration eased off 5/19 peak (10Y 4.55, 30Y 5.01 still >5% sustained)

> ⚠️ **CATCH-UP GAPS (not yet integrated):** 5/21 10Y reopening result, 5/26 2Y / 5/27 5Y / 5/28 7Y auction internals, 5/28 April PCE, 6/5 May NFP detail. Dashboard market levels are 6/5-6/8 live; **auction-internals rows (Dashboard 3) remain 5/20 and are flagged stale.** May CPI 6/10 (T-1).

---

## Thesis-Kill Proximity (6/8)

**HY OAS 276bps (6/5). Kill 260 (HEARTBEAT line 80). Cushion: 16bps** (NARROWING from 26bps on 5/20; re-tagged the 5/17 cycle-tight of 276). Still 44bps below 320 confirmation. **Thesis grinding toward the kill side, not toward confirmation.**

**APO co-trigger RE-ARMING 🟡** — APO **ran $130 → ~$131.5 (+3.1%) on 6/8** (annual-meeting day; climbed intra-session $129.93→$131.55, live yfinance). Retraced from the ~$135 mid-May peak to the line, then **re-crossed above $130 on the 6/8 bounce.** KILL_MEMO Trigger C precondition (APO >$130 concurrent with HY OAS compression) is **back in play** but needs **3 sustained sessions >$130** to fire — one bounce-print isn't the full signal. Watch whether it holds >$130. (Dashboard had $127.57 — stale; live primary is the truth here.)

> **🎯 Current framing:** "thesis grinding but intact via credit-compression-toward-kill" — the duration channel that was acute on 5/19 (30Y 5.168 intraday) has eased (30Y 5.01, 10Y 4.55), AND the reflation co-driver (Brent) collapsed -$17. The live tell is now **HY OAS cushion to 260** (16bps, narrowing) rather than the APO co-trigger. Watch for HY OAS <265 (kill-memo Trigger A) on the compression side, OR a re-widening if a credit event prints.

POV-arc for how we got here: see `thesis/CHANGELOG.md` § POV Pivots (5/20, 5/19, 5/18).

---

## Recent History + Open Auction Gap (as of 6/8)

**5/20 20Y auction (resolved → KB-LIQ-057):** NEW issue $16B, BTC 2.55 / **indirect 67.7% (STRONG)** / tail 0bp / dealer 9.4% — soft-but-functional, no orange. Disproved the foreign-demand-canary read of the 5/13-5/19 long-end break: **term-premium digestion, not broken auction mechanism.** Full detail in KB-LIQ-057 (read-before-citing preamble there).

**Duration peak was 5/19:** 30Y tagged **5.168% intraday** (first 5% since 2007), 10Y 4.647. Whole curve at 1mo highs, parallel bear. As of 6/5 the curve has **eased off that peak** — 30Y 5.01 (still >5% sustained), 10Y 4.55. Channel migrated PLUMBING→DURATION over the Apr-May gap (KB-LIQ-051/052); duration is now grinding, not spiking, and the Brent reflation co-driver has reversed.

> ⚠️ **NOT YET INTEGRATED (auction internals):** 5/21 10Y reopening (was Leg 2 corroboration gate), 5/26 2Y, 5/27 5Y, 5/28 7Y. I have live market *levels* but not BTC/indirect/tail for these. Dashboard 3 auction rows remain 5/20. **Fill when BOND outboxes / Treasury results are pulled** — flagged as a follow-up, not silently assumed clean.

---

## Dashboard 1 — Credit Spreads (6/5-6/8)

| Metric | Threshold | Current | Status |
|--------|-----------|---------|--------|
| **HY OAS (macro)** | confirmation >320 / freeze >350 / **kill <260** | **276** (6/5, +2 daily) | 🟡 44bps below 320; **16bps cushion above 260 kill (NARROWING from 26).** ⚠️ **Partially artificially strong** — CCC widened +17 while macro compressed -10 (~27bps bifurcation); decompose before citing as "calm" (KB-LIQ-058). Watch <265 = Trigger A. |
| **HY Energy OAS** | >300 = energy-credit trip | **~285 (Apr 28, 40d STALE)** | 🟠 The primed corner — Brent -15% + live Hormuz; energy credit decouples from oil on geo-risk (BRENT). Likely wider than 285, plausibly at/through 300. **Needs live ICE/BBG pull (BRENT/data-fetch).** |
| **APO co-trigger** | >$130 for 3 sessions (HEARTBEAT line 80) | **~$131.5** (+3.1%, live 6/8) | 🟡 **RE-CROSSED $130** on 6/8 bounce (annual-mtg day). Day 1 of 3 — needs sustained holds >$130 to fire Trigger C. Watch the count. |
| CCC OAS | >1000bps | 952 (6/5, +6) | 🟡 48bps away — quality bifurcation still widening but not at trigger |
| BIZD | mark stress | $12.56 (+0.84%, live 6/8) | 🟡 Back above $12.50 trigger on 6/8 bounce (BROCK had it "cracked" at $12.49 on 6/5). FSK -9.9% mark direction intact |
| VIX | >25 | 18.92 (6/8) | 🟢 Well below; up modestly from 5/20 (17.47). Gamma-suppression hypothesis still live |
| BDC Q1 marks | rolling | FSK -9.9% in; OBDC/ARCC/BXSL/MAIN — **status not re-verified post-5/20** | 🟡 See `workbook/BDC_MARK_CONVERGENCE_MONITOR.md` — needs refresh |

---

## Dashboard 2 — Domestic Plumbing (6/5-6/8)

| Metric | Threshold | Current | Status |
|--------|-----------|---------|--------|
| **SOFR** | >3.70 | 3.63% (6/5) | 🟢 Normalized; +8bps vs 5/18 but below threshold |
| **SOFR-IORB** | sustained >0 | **-2bps** (6/5) | 🟢 Drifting toward zero (from -12), still negative/clean. No funding stress signal |
| **10Y yield** | >4.50% sustained | 4.55% (6/5) | 🔴 Still >4.50 sustained but **eased off 5/19 peak (4.647)**; grinding not spiking |
| **30Y yield** | >5% sustained | **5.01% (6/5, ~5.02 live)** | 🔴 Still >5% sustained; off the 5.168 intraday peak. First sustained 5% regime since 2007 holds |
| TLT | level | $84.62 (6/8) | 🔴 Duration repricing intact; recovered from 5/19 lows |
| RRP buffer | >$5B | $0.158B (Apr 16, stale) | 🔴 Structural zero — no buffer to drain |
| SRF usage | >$50B | TBD | — Check next NY Fed refresh (stale since 4/16) |
| Reserve floor | >$2.8T | ~$3.0T (stale) | 🟡 Cushion intact but draining; needs refresh |
| CP-TBill | spread health | 0.11 (6/5) | 🟢 Plumbing clean |

> *Yield-curve and dealer-positioning scope migrates to BOND-primary when stood up; LIQUID retains repo/SOFR/reserves at thesis level (THESIS v2.0 §8).*

---

## Dashboard 3 — Foreign Official (FX/Brent live 6/8; auction internals STALE 5/20)

| Metric | Threshold | Current | Status |
|--------|-----------|---------|--------|
| **Auction Indirect** | <55% sustained | **67.7%** (5/20 20Y, last verified) | 🟢 Last print STRONG; ⚠️ **5/21-5/28 cycle not integrated** — see auction-gap note above |
| **Auction Mix** | BTC ≥2.60, tail ≤+1bp, dealer ≤10% | BTC 2.55 / tail 0bp / dealer 9.4% (5/20) | 🟡 Last print soft-but-functional; stale, needs 2Y/5Y/7Y refresh |
| **USD/JPY** | >160 | **160.22** (6/8) | 🔴 **TRIGGER FIRED** — crossed 160. SAM-domain co-watch; BOJ intervention-risk acute |
| **Brent** | reflation watch | **$89.95** (-4.56%, live 6/8) | 🟡 **REVERSED ~-$20 from $110.59, sub-$90.** Reflation/CPI-passthrough loop cooling hard — eases the inflation co-driver of the duration channel (HAWK/BRENT-domain) |
| Foreign CB UST | stable | $2.7T (lowest since 2012, stale) | 🔴 Structural outflow |
| Belgium TIC | >$500B = ORANGE | $481B (Nov 2025) | 🟡 Watch; **next data 6/18 (May TIC = April flows)** per KB-LIQ-055 framework |

---

## Cross-Domain Signals (6/8)

- **APO co-trigger RE-CROSSED $130 (~$131.5, +3.1% on 6/8) → BROCK:** Bounced back above the trigger on annual-meeting day. Day 1 of 3 — needs sustained holds to fire Trigger C. BROCK tracks the SAME $130 line ("reclaims $130 sustained → reassess puts"); their APO Dec $95P thesis vehicle. The 6/8 risk-complex bounce (APO +3%, BIZD +0.8%) reverses Fri 6/5's equity crack — watch whether it holds. Outbox candidate.
- **USD/JPY 160.22 TRIGGER FIRED → SAM:** Crossed the 160 line I'd been co-watching. BOJ verbal/actual intervention risk now acute. SAM owns; flag for confirmation of repatriation read.
- **Brent reversal $110.59 → $89.95 (sub-$90) → HAWK, BRENT, CARL:** ~-$20. Cools the reflation/CPI-passthrough loop materially ahead of **May CPI 6/10**. Removes one co-driver of the duration channel.
- **Duration eased off 5/19 peak → HENRY, REGINALD:** 30Y 5.168 intraday → 5.01; 10Y 4.647 → 4.55. Still >threshold sustained, but grinding not spiking. Less acute than the 5/18-5/19 escalation.
- ✅ **SOFR-IORB read sent to BOND (5/20)** — `outbox/2026-05-20_to-BOND_sofr-iorb-ample-reserves-read.md`. (Was BOND active? confirm delivery in delivered/.)
- ~~SOFR>IORB → RESOLVED MECHANICAL.~~ See KB-LIQ-051.

- **T-08 credit-pin (HAW-11 leakage node) → NEXUS:** ✅ Verified intact-and-primed. Caveat: a leakage event may widen HY *without* the usual safe-haven UST bid (30Y>5%, foreign exit, JPY 160) — no duration cushion = node-amplifier. Graded soft-but-primed (not dormant). On daily watch through Hormuz window (Jun 8-22).
- ✅ **NEXUS C3 + T-08 reads delivered 6/8** — `outbox/2026-06-08_to-NEXUS_c3-t08-credit-reads.md`; Will-decision resolved Option-A to PROME. Both blockers cleared for 6/9-12 cluster.

---

## Active Proposals (6/8)

**PROPOSAL 3 — CRUDE SHORT ON HOLD.** Hormuz/Dimona active; Brent reversed to $93.43 (was $110.59). Short thesis less urgent at lower spot, but war-premium-collapse already partly realized.
**PROPOSAL 4 — HYG PUT REVIEW → RECOMMEND CLOSE/EXPIRE.** HYG **$79.54** vs $75 strike — deep OTM, June expiry (~6/19, T-10). HY OAS **276 tightening AWAY from the 320 trigger**; thesis (retest to 350) did not play. Theta-killer with no path. **Will decision: let expire worthless vs cut for residual.** (see `put_vs_duration_expression` memory — equity/credit puts bleed in regime-suppressed tape.)
**PROPOSAL 5 — BCRED Q2 HARD GATE.** APO re-crossed $130 (~$131.5, +3.1% on 6/8) + FSK NAV -9.9% + BROCK Stage 2→3 pivot (4-fund gate cluster, record 6% default) = substance accelerating while APO equity bounces. Mixed signal; revisit on BCRED Q2 window. (BROCK owns the gate-cascade detail.)

## Active Positions

| Position | Expiry | Thesis | Status (6/8) |
|----------|--------|--------|--------|
| TEN calls (Jun $30) | Jun 2026 | Triple premium | TEN $36.83 — **ITM ~$6.83, winner.** Dimona/HAWK co-watch. Hold/evaluate near expiry. |
| HYG $75P Jun x10 | Jun 2026 | LIQ-01 retest to 350 | **Thesis broken.** HYG $79.54 deep OTM; HY OAS 276 tightening away from trigger. → close/expire (Will decision). |

---

## Danger Windows + Watch (6/8)

| Window / Frequency | Risk |
|---|---|
| **Daily** | HY OAS 260 kill proximity (**16bps cushion, NARROWING**; <265 = Trigger A); 10Y/30Y duration regime; USD/JPY post-160-trigger follow-through; SOFR/SOFR-IORB stability |
| **This Week (Jun 8-12)** | **May CPI Wed 6/10** (Brent reversal eases passthrough — does core stay sticky?); initial claims Thu 6/11; BDC Q1 wrap |
| **Next Week (Jun 15-19)** | **June FOMC decision Wed 6/17** (dot plot, Warsh succession color, liquidity-facility language); **May TIC = April flows Thu 6/18** (Japan/Belgium proxy/FOI hole); **June monthly opex 6/19** (HYG/TEN expiry) |
| **Late June** | BCRED Q2 redemption window (hard gate? >7% cap test); June Treasury auction cycle (30Y is the live tell at 5.01) |
| **Powell → Warsh transition** | Policy continuity vs hawkish shift; intervention willingness collapse risk |

## Active Playbooks / Monitors

| File | Purpose | Active window |
|------|---------|---------------|
| `workbook/KILL_MEMO_HY_OAS_260.md` | Pre-written 1-pager: actions that fire when HY OAS <265 for 2 sessions OR <260 intraday | live until thesis reframed |
| `workbook/BDC_MARK_CONVERGENCE_MONITOR.md` | Public-BDC mark watch; TCW Red Lobster follow-through — checks my own "PC decelerating" narrative | rolling, Q1 BDC earnings active (FSK May NAV -9.9% in; OBDC etc. pending) |

---

## Durable Signals Log

All durable findings live in `workbook/KB.tsv` (57 entries, KB-LIQ-001 through KB-LIQ-057). Query that file for signal lineage. Notable recent anchors:
- **KB-LIQ-057** (5/20) — Foreign demand showed at price; term-premium digestion ≠ broken auction
- **KB-LIQ-052** (5/18) — Duration regime break May 2026; channel migrated PLUMBING → DURATION
- **KB-LIQ-051** (5/18) — April SOFR-IORB breach resolved mechanical (tax-day TGA)
- **KB-LIQ-053/054** (3/10, 3/11) — Stagflation trap structural / Financial hub transmission (4-path)
- **KB-LIQ-055/056** (2/11) — Foreign custodial flow disaggregation / Collateral velocity (Belgium/SIFMA)

For pre-KB historical entries (PC Stage 3 cadence: Barings/Blue Owl/FT-Stanger gates, MS $85B BD→bank, WFC $200B SPOF, Janus, Foreign CB UST trough, Goldman TRS pause) see git history of this file pre-5/20 OR earlier STATUS snapshots in `archive/status_snapshots/`.

---

*Domain: Financial plumbing — repo markets, funding rates, credit spreads, foreign Treasury demand, dealer capacity.*
