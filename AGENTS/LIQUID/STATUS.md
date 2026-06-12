# LIQUID STATUS
**Last Updated:** 2026-06-12 AM (boot refresh, all live-primary) | **Agent:** LIQUID | **Status:** 🟠 **APO >$130 ×3 closes — HEARTBEAT reassess trigger FIRED 6/11** (closes 6/9 $132.70 / 6/10 $131.14 / 6/11 $133.91; NOT Trigger C — HY OAS widened, concurrency fails); HY OAS 280 (6/10) — **direction REVERSED, cushion to 260 kill back out to 20bps**; May CPI HOT (headline 4.18% YoY accel, core 2.81%); USD/JPY 5 sessions >160; Brent $87.95 still collapsing; 30Y 5.03 >5% sustained

> ⚠️ **CATCH-UP GAPS (not yet integrated):** 5/21 10Y reopening result, 5/26 2Y / 5/27 5Y / 5/28 7Y auction internals, 5/28 April PCE, 6/5 May NFP detail. **Auction-internals rows (Dashboard 3) remain 5/20 and are flagged stale.**

---

## Thesis-Kill Proximity (6/12)

**HY OAS 280bps (6/10). Kill 260. Cushion: 20bps — direction REVERSED to widening** (274 on 6/4 → 280 on 6/10; first sustained move away from the kill since mid-May). Still 40bps below 320 confirmation. The compression-toward-kill grind paused; watch whether 6/11-6/12 prints extend the widening (May-CPI-hot + claims-creep is a credible widener).

**APO co-trigger: ≥3-session leg FIRED on closes 🟠 — but NOT Trigger C.** Daily closes: 6/9 $132.70, 6/10 $131.14, 6/11 $133.91 = 3 consecutive >$130. HEARTBEAT line-80 **REASSESS obligation fired 6/11.** KILL_MEMO escalation to Trigger C requires concurrency with **HY OAS compression** — HY widened 274→280 over the same window, so concurrency FAILS. Read: PC equity bid strong while credit tail (CCC 957) deteriorates = the known equity/mark decoupling (KB-LIQ-058 + durable finding "don't over-weight equity price action for Stage 3 timing"). Reassess output → BROCK (holds APO Dec $95P, tracks the same line); outbox sent 6/12.
> ⚠️ **Count correction (OHLC rule):** the 6/8 "Day 1" in the prior STATUS was an intraday print — APO's official 6/8 CLOSE was $127.57, below the line. Streak starts 6/9. Day-counts key off daily closes only.

> **🎯 Current framing:** "thesis intact; credit channel re-widening, duration channel sustained" — 30Y 5.03 >5% sustained, 10Y 4.55 >4.50 sustained. May CPI hot (4.18% headline accel) constrains the Fed into 6/17 FOMC while claims creep (210→229k over 4 wks) = stagflation-trap texture. Brent collapse ($87.95) eases *June* CPI passthrough but the May print already landed hot. Watch: HY OAS direction post-CPI, FOMC 6/17 dot plot, APO streak extension (Day 4 would be today's close).

POV-arc for how we got here: see `thesis/CHANGELOG.md` § POV Pivots (5/20, 5/19, 5/18).

---

## Recent History + Open Auction Gap (as of 6/8)

**5/20 20Y auction (resolved → KB-LIQ-057):** NEW issue $16B, BTC 2.55 / **indirect 67.7% (STRONG)** / tail 0bp / dealer 9.4% — soft-but-functional, no orange. Disproved the foreign-demand-canary read of the 5/13-5/19 long-end break: **term-premium digestion, not broken auction mechanism.** Full detail in KB-LIQ-057 (read-before-citing preamble there).

**Duration peak was 5/19:** 30Y tagged **5.168% intraday** (first 5% since 2007), 10Y 4.647. Whole curve at 1mo highs, parallel bear. As of 6/5 the curve has **eased off that peak** — 30Y 5.01 (still >5% sustained), 10Y 4.55. Channel migrated PLUMBING→DURATION over the Apr-May gap (KB-LIQ-051/052); duration is now grinding, not spiking, and the Brent reflation co-driver has reversed.

> ⚠️ **NOT YET INTEGRATED (auction internals):** 5/21 10Y reopening (was Leg 2 corroboration gate), 5/26 2Y, 5/27 5Y, 5/28 7Y. I have live market *levels* but not BTC/indirect/tail for these. Dashboard 3 auction rows remain 5/20. **Fill when BOND outboxes / Treasury results are pulled** — flagged as a follow-up, not silently assumed clean.

---

## Dashboard 1 — Credit Spreads (6/10-6/11 live)

| Metric | Threshold | Current | Status |
|--------|-----------|---------|--------|
| **HY OAS (macro)** | confirmation >320 / freeze >350 / **kill <260** | **280** (6/10; 274→275→278→280 from 6/4) | 🟡 **WIDENING — cushion to kill back out to 20bps.** 40bps below 320. Bifurcation persists: CCC−BB = 787 (KB-LIQ-058); decompose before citing aggregate. |
| **HY Energy OAS** | >300 = energy-credit trip | **~285 (Apr 28, 44d STALE)** | 🟠 Primed corner — Brent now $87.95; needs live ICE/BBG pull (BRENT/data-fetch). |
| **APO co-trigger** | >$130 ×3 sessions (HEARTBEAT line 80) | **$133.91 close 6/11; 3 consecutive closes >$130** | 🟠 **FIRED 6/11 (reassess leg).** NOT Trigger C — HY widening, concurrency fails. 6/8 close was $127.57 (intraday-print miscount corrected). Outbox → BROCK 6/12. |
| CCC OAS | >1000bps | 957 (6/10, BB 170) | 🟡 43bps away — tail keeps widening while BB barely moves |
| BIZD | mark stress | $12.62 (close 6/11) | 🟡 Above $12.50 trigger 3 straight closes. FSK -9.9% mark direction intact |
| VIX | >25 | 19.13 (6/12 pre-mkt; **spiked 22.22 on 6/10 CPI day**) | 🟡 Elevated floor vs May (15-17 range); two >21 spikes in 5 sessions (6/5, 6/10) |
| BDC Q1 marks | rolling | FSK -9.9% in; OBDC/ARCC/BXSL/MAIN — **status not re-verified post-5/20** | 🟡 See `workbook/BDC_MARK_CONVERGENCE_MONITOR.md` — needs refresh |

---

## Dashboard 2 — Domestic Plumbing (6/10-6/11 live)

| Metric | Threshold | Current | Status |
|--------|-----------|---------|--------|
| **SOFR** | >3.70 | 3.60% (6/11) | 🟢 Clean; drifted down from 3.63 |
| **SOFR-IORB** | sustained >0 | **-5bps** (6/11) | 🟢 Negative/clean. No funding stress signal |
| **10Y yield** | >4.50% sustained | 4.55% (6/10) | 🔴 Still >4.50 sustained; held through hot CPI (4.53→4.55) |
| **30Y yield** | >5% sustained | **5.03% (6/10)** | 🔴 Still >5% sustained (5.01-5.03 band all week). First sustained 5% regime since 2007 holds |
| TLT | level | $85.98 (close 6/11) | 🔴 Duration repricing intact; +$1.36 relief bid 6/11 post-CPI digestion |
| RRP buffer | >$5B | $0.158B (Apr 16, stale) | 🔴 Structural zero — no buffer to drain |
| SRF usage | >$50B | TBD | — Check next NY Fed refresh (stale since 4/16) |
| Reserve floor | >$2.8T | ~$3.0T (stale) | 🟡 Cushion intact but draining; needs refresh |
| CP-TBill | spread health | 0.11 (6/5) | 🟢 Plumbing clean |

> *Yield-curve and dealer-positioning scope migrates to BOND-primary when stood up; LIQUID retains repo/SOFR/reserves at thesis level (THESIS v2.0 §8).*

---

## Dashboard 3 — Foreign Official (FX/Brent live 6/12; auction internals STALE 5/20)

| Metric | Threshold | Current | Status |
|--------|-----------|---------|--------|
| **Auction Indirect** | <55% sustained | **67.7%** (5/20 20Y, last verified) | 🟢 Last print STRONG; ⚠️ **5/21-5/28 cycle not integrated** — see auction-gap note above |
| **Auction Mix** | BTC ≥2.60, tail ≤+1bp, dealer ≤10% | BTC 2.55 / tail 0bp / dealer 9.4% (5/20) | 🟡 Last print soft-but-functional; stale, needs 2Y/5Y/7Y refresh |
| **USD/JPY** | >160 | **160.27** (6/12 AM; closes 160.33/160.17/160.38/160.53 from 6/8) | 🔴 **5 consecutive sessions >160 — SUSTAINED.** SAM-domain co-watch; BOJ intervention-risk acute |
| **Brent** | reflation watch | **$87.95** (6/12 AM) | 🟡 **Collapse extending: $110.59 → $87.95 (-$22.6).** June CPI passthrough relief ahead — but May CPI already landed hot (4.18% YoY) on the lagged energy |
| Foreign CB UST | stable | $2.7T (lowest since 2012, stale) | 🔴 Structural outflow |
| Belgium TIC | >$500B = ORANGE | $481B (Nov 2025) | 🟡 Watch; **next data 6/18 (May TIC = April flows)** per KB-LIQ-055 framework |

---

## Cross-Domain Signals (6/12)

- **APO >$130 ×3 closes — reassess trigger FIRED → BROCK (outbox sent 6/12):** closes 6/9-6/11 all >$130 ($132.70/$131.14/$133.91). NOT Trigger C (HY widening, concurrency fails). BROCK holds APO Dec $95P and tracks the same line — their reassess to run.
- **May CPI HOT → CARL:** headline +0.48% MoM / 4.18% YoY (accel from 3.78%); core +0.21% MoM / 2.81% YoY. With claims creeping 210→229k over 4 weeks = stagflation-trap texture into 6/17 FOMC. CARL owns the macro read; my interest is the Fed-constraint angle on duration.
- **USD/JPY 5 sessions >160 SUSTAINED → SAM:** 160.17-160.53 closes since 6/8. BOJ intervention-risk acute; SAM owns.
- **Brent $87.95, collapse extending → HAWK, BRENT, CARL:** -$22.6 from peak. June CPI passthrough relief ahead; war-premium largely unwound.
- ✅ **SOFR-IORB read sent to BOND (5/20)** — still undelivered in outbox/ (HERMES sweep pending).
- ~~SOFR>IORB → RESOLVED MECHANICAL.~~ See KB-LIQ-051.

- **T-08 credit-pin (HAW-11 leakage node) → NEXUS:** ✅ Verified intact-and-primed. Caveat: a leakage event may widen HY *without* the usual safe-haven UST bid (30Y>5%, foreign exit, JPY 160) — no duration cushion = node-amplifier. Graded soft-but-primed (not dormant). On daily watch through Hormuz window (Jun 8-22).
- ✅ **NEXUS C3 + T-08 reads delivered 6/8** — `outbox/2026-06-08_to-NEXUS_c3-t08-credit-reads.md`; Will-decision resolved Option-A to PROME. Both blockers cleared for 6/9-12 cluster.

---

## Active Proposals (6/12)

**PROPOSAL 3 — CRUDE SHORT ON HOLD.** Brent $87.95; war-premium collapse largely realized. Short thesis stale at this spot.
**PROPOSAL 4 — HYG PUT REVIEW → RECOMMEND CLOSE/EXPIRE.** HYG **$79.94** vs $75 strike — deep OTM, **June expiry 6/19, T-5.** Thesis (retest to 350) did not play; HY at 280. Theta-killer with no path. **Will decision: let expire worthless vs cut for residual — decision window closing.**
**PROPOSAL 5 — BCRED Q2 HARD GATE.** APO trigger fired (3 closes >$130) + FSK NAV -9.9% + BROCK Stage 2→3 pivot = substance accelerating while PC equity bid strengthens. Mixed signal; revisit on BCRED Q2 window. (BROCK owns the gate-cascade detail.)

## Active Positions

| Position | Expiry | Thesis | Status (6/12) |
|----------|--------|--------|--------|
| TEN calls (Jun $30) | **Jun 19 (T-5)** | Triple premium | TEN $37.11 — **ITM ~$7.11, winner.** Exercise/sell decision needed BEFORE 6/19. Dimona/HAWK co-watch. |
| HYG $75P Jun x10 | **Jun 19 (T-5)** | LIQ-01 retest to 350 | **Thesis broken.** HYG $79.94 deep OTM. → close/expire (Will decision, window closing). |

---

## Danger Windows + Watch (6/12)

| Window / Frequency | Risk |
|---|---|
| **Daily** | HY OAS direction (widening resumed — 280; <265 = Trigger A still armed if it re-compresses); APO streak extension (Day 4 = today's close); 10Y/30Y duration regime; USD/JPY >160 follow-through; SOFR-IORB |
| **Next Week (Jun 15-19)** | **June FOMC decision Wed 6/17** (dot plot vs hot May CPI; Warsh succession color; liquidity-facility language); **May TIC = April flows Thu 6/18** (Japan/Belgium proxy/FOI hole — KB-LIQ-055); **June monthly opex Fri 6/19 — HYG puts + TEN calls BOTH expire** |
| **Late June** | BCRED Q2 redemption window (hard gate? cap test); June Treasury auction cycle (30Y the live tell at 5.03); Cliffwater CDLI Q1 |
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
