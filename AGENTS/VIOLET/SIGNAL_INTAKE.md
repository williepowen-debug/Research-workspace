# VIOLET — Signal Intake Spec

**Owner:** VIOLET | **Consumer:** Routing agent (WALTER) | **Last Updated:** 2026-07-17 (added JPY 10d RV carry→vol threshold line, KB-VIO-117)
**Domain:** VIX complex, vol term structure, vol-of-vol (VVIX), SKEW/tail pricing, credit-to-vol transmission timing, vol-regime classification.

---

## ⚠️ How to read this file

Routing rules are durable; **dated state is not in this file.** Live source map:

| Need | Live source |
|------|-------------|
| Current vol-surface values (VIX/VIX9D/VIX3M/VVIX/SKEW, regime, convergence) | `STATUS.md` |
| Forward catalysts (CPI/FOMC/BOJ/VIX expiries) | `workbook/CATALYSTS.tsv` (+ `CALENDAR.md` human twin) |
| Trade setups, vehicles, sizing | `TRADE.md` + `thesis/VIX_THESIS.md` (L1 canonical base-rate table) |
| Episode-level signal history | `workbook/KB.tsv` |

Per auto-memory `[[project_messaging_overhaul]]`: don't extend or patch routing infra here. New operational routing logic (auto-scan/auto-dispatch trigger rows) is negotiated via LIAISON with Will sign-off — registry pattern (future `VIO-T-NN` per the RED-FT-NN / REG-T-NN schema), not this file. **This file is scope-of-attention + exclusions + keywords + a short durable-lines table.**

VIOLET self-pulls at boot (don't route raw data): vol surface (yfinance), FRED credit, CFTC COT VIX, VIX options OI. What VIOLET needs routed is what boot can't compute: **news, narrative, structural events, and other agents' domain reads.**

---

## PRIORITY LEVELS

| Priority | Meaning | Delivery |
|----------|---------|----------|
| 🔴 IMMEDIATE | Could change vol-regime read, a position gate, or a probability within hours | As soon as detected |
| 🟠 SAME DAY | Informs the surface read; not instant-action | Within the trading day |
| 🟡 WEEKLY BATCH | Background / trend tracking | Batched weekly |

---

## 🔴 IMMEDIATE

### Vol-market structural events
- Vol ETP stress or termination events (SVIX/UVXY/VXX-class rebalance stress, AP withdrawal, fund blowup)
- Vol-targeting / vol-control / CTA de-risking flow reports (the structural un-pinning class — record-GEX suppression is the active mechanism hypothesis, KB-VIO-055/062)
- Dealer gamma FLIP reports (HENRY owns the mechanics; VIOLET needs the flip event itself)
- CBOE/VIX product or methodology changes; vol-market microstructure breakdowns

### Catalyst tail outcomes
- Scheduled-print TAIL surprises (CPI/NFP/FOMC/BOJ materially off consensus) — the analysis, not the routine print (VIOLET tracks the calendar itself)
- Unscheduled central-bank action (intermeeting moves, emergency liquidity ops, intervention)

### Geopolitical / credit stress events with vol transmission
- War escalation/de-escalation inflections, Hormuz-class chokepoint events (HAWK substance; VIOLET owns equity-vol transmission — validated 6/10: Iran overnight = third vol leg)
- Credit stress EVENTS: BDC gating, fund redemption halts, HY new-issue freeze, major default/downgrade cascade (LIQUID/BROCK own substance; credit-to-vol timing is VIOLET's specialty)

### Cross-Agent Signals (threshold-breach class → 🔴 per template rule)
- **BROCK:** BDC gating event, PC redemption stress `[verify with owner — categories from Apr spec]`
- **LIQUID:** HY OAS +50bps/1wk-class spread spike; funding stress (SOFR-IORB >0.25 `[verify with owner]`); gold margin cascade `[verify with owner]`
- **HENRY:** FOMC surprise read, zero-gamma breach / dealer short-gamma flip
- **HAWK:** war escalation, ceasefire breakdown, Hormuz closure threat
- **RED:** adversarial scenario activation with vol-spike pathway ("Scenario D" `[verify with owner — pre-May vocabulary]`)
- **SAM:** BOJ hawkish-of-pricing outcome, carry-unwind trigger (fuel-load danger-zone breach)

## 🟠 SAME DAY

### Positioning & flow intelligence
- Institutional positioning datapoints: prime-broker/desk notes, BofA FMS vol items, institutional C/P ratio prints (Citadel-class), SpotGamma/Menthor-class structure summaries when they surface in feeds
- VIX options flow stories (large prints, tail-strike accumulation/unwind — VIOLET tracks OI levels itself; route the narrative/attribution)
- Short-vol crowdedness commentary (ETP AUM spikes, retail vol-selling trend pieces)

### Cross-agent context reads
- **HENRY:** breadth/gamma regime reads, factor-unwind assessments
- **SAM:** CFTC yen fuel-load updates, BOJ pricing shifts
- **BRENT:** oil-vol state changes (OVX regime moves — the oil-vol vs equity-vol transmission gauge, KB-VIO-081)
- **LIQUID:** credit-spread trend analysis (levels VIOLET self-pulls; route the read)

### Policy / structure
- SEC/CFTC rule changes affecting vol products, options market structure, 0DTE
- Exchange margin changes on VIX futures/options

## 🟡 WEEKLY BATCH

- Vol-structure research pieces (academic, sell-side primers on term structure / VRP / skew dynamics)
- Positioning trend summaries (COT-adjacent commentary — raw COT is self-pulled)
- Vol ETP AUM / flows trend data
- Realized-correlation and dispersion trend pieces

---

## KEYWORD PATTERNS

**High confidence (almost always VIOLET):**
VIX, VVIX, SKEW index, vol-of-vol, term structure inversion, backwardation, contango, volatility regime, vol spike, vol crush, volmageddon, short-vol unwind, vol ETP, UVXY, SVIX, VXX, variance swap, tail hedge, crash protection, put skew, vol-targeting, vol-control funds, CTA de-risk, gamma flip, VIX expiration, VIX futures positioning

**Medium confidence (relevant in context):**
implied volatility, realized volatility, vol risk premium, VRP, dispersion, correlation break, hedging flows, protection bid, dealer positioning, OPEX, quad witching, 0DTE (index-vol context), MOVE index, OVX, carry unwind (vol-transmission angle), risk reversal (index)

**Low confidence (only with index-vol angle):**
options, hedge, fear gauge, market stress, panic, drawdown, tail risk

---

## WHAT NOT TO SEND

- Dealer gamma / put-wall / 0DTE flow MECHANICS → HENRY (VIOLET wants flip events + regime implication only)
- Equity price action, breadth, single-stock moves → HENRY
- Single-stock options flow, earnings IV (non-index) → HENRY
- Credit spread LEVELS / routine OAS prints → LIQUID (self-pulled at boot; VIOLET wants stress events + reads, not data)
- Private credit / BDC fundamentals → BROCK (VIOLET wants gating-class events only)
- Oil price / supply / OPEC substance → BRENT / HAWK (VIOLET wants the oil-vol→equity-vol transmission angle only)
- FX / yen-carry substance, BOJ policy analysis → SAM (VIOLET wants carry→vol transmission triggers only)
- Treasury auctions, rates substance → LIQUID / SAM
- Routine scheduled macro prints (CPI/NFP as-expected) → CARL / HENRY (VIOLET tracks the calendar; route tails only)

---

## ACTIVE THRESHOLDS — durable structural lines only

**Header rule:** this table holds VIOLET's standing regime/trigger LINES — the levels worth interrupting for. **Live readings, margins, and current-episode gates live in `STATUS.md`, never here.** *(Documented divergence: CARL's post-5/31 reference pattern drops this section entirely; VIOLET keeps a lines-only version because the four lines below are stable calibration values with multi-month-to-multi-year shelf lives, useful for routing pattern-matches. If they start needing per-episode edits, follow CARL and delete the section.)*

| Metric | Level | Direction | Why It Matters |
|--------|-------|-----------|----------------|
| VVIX | 120 | Above | Vol-of-vol stress — option market repricing the vol distribution; vol sellers at risk |
| VIX3M/VIX | 1.0 | Below | Term-structure inversion — **marks vol peaks, exit-timing signal (KB-VIO-034: 2.2% hit rate as onset predictor). NOT a crash-onset leading indicator.** |
| 20d SKEW avg | 140 | Below, sustained 4+ td | Elevated-SKEW regime termination test (R-series regimes, KB-VIO-043/061). Single-day dips are noise — sustained breaks are the signal |
| VIX | 30 / 40 | Above | Regime lines: >30 equity stress confirmed; >40 crash regime (credit-vol lead relationship inverts above 40) |
| JPY 10d RV (USDJPY, carry→vol) | p90 WATCH / p95 FIRE (percentile-anchored, **re-derived each run** — current ~13.97 / 15.21; Aug-2024 unwind anchor 18.0) | Above | Carry-unwind → equity-vol transmission (KB-VIO-102 Aug-2024 replay class). IV/RV >2× (FXY OI-wt near-ATM call IV) = event premium priced; →1× w/o RV spike = risk passed; RV>IV = unwind underway. Owner: VIOLET (transmission read) / SAM (substance). Instrument LIVE 7/16 (`scripts/jpy_vol.py`, boot-wired); ratified KB-VIO-117. Route on FIRE: outbox SAM + PROME. |

---

## OUTBOUND (pointer only)

VIOLET's outbound signal protocol lives in `CLAUDE.md` (write-back step 12): **NEXUS_BRIEF.md is the primary cross-agent surface; `outbox/` is reserved for 🔴 acute, time-sensitive signals only.** No outbound routing rules are defined in this file.

---

**Review triggers (per template):** thesis version change · threshold line breached/shifted · new vector enters domain · received signals not needed (add exclusion) · missed a signal that mattered (add intake).

*Rebuilt to SIGNAL_INTAKE_TEMPLATE.md v0.1 on 2026-06-10, orchestrator-verified (first conformant version — the Apr 12 original predated the 4/14 rollout and was never restructured). Prior content was archived at `archive/SIGNAL_INTAKE_2026-04-12_pre_template.md`, but the whole `VIOLET/archive/` dir was deleted in the 2026-06 public-prep prune (`1cb18fbc`/`7133b7d6`) — recover via git history only (ref fixed 2026-07-11, DAEDALUS L4 packet #5). Trade setups and sizing live exclusively in TRADE.md / thesis (KB-VIO-079 canonical base-rate table).*
