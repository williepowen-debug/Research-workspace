# VIOLET — Signal Intake Spec

> ⚠️ **INSTRUMENT DISAMBIGUATION — "SKEW" NOW NAMES TWO UNRELATED THINGS FLEET-WIDE (adopted 2026-08-20, WALTER `SIG-W-20260819-031`).** Everywhere in VIOLET's files, **SKEW means `^SKEW`, the CBOE S&P 500 SKEW index** (equity-index tail pricing, 100-150 scale, VIOLET-owned). It is **NOT** the *3y10y swaption skew* (a 3-year option on a 10-year swap; **rates vol, BOND-owned**) that began circulating 8/19 at multi-year highs tilted to payers. A fleet grep for "SKEW" now returns both. **My rows are correct and were still unqualified** — 62 mentions across my cross-agent surfaces, only 8 explicitly tagged — so the defect materialises at the READER, not the writer. Qualify on first use in anything another desk reads; **rates-vol skew substance is BOND's, not mine.**

**Owner:** VIOLET | **Consumer:** Routing agent (WALTER) | **Last Updated:** 2026-08-10 (**COR1M first-tell + MOVE pause/resume added, both Will-ruled in-session — 2026-08-10 financial-conditions forum FINAL §5; a proposed SKEW>140 line was withdrawn in favor of RED's existing standing guard on the same number, KB-VIO-188..191**. Prior: 2026-07-30, KB-VIO-147 audit — ACTIVE THRESHOLDS rebuilt with explicit LEVEL + INSTRUMENT + WINDOW columns; two stale live readings removed from the table per its own header rule; first provenance pass this file has ever had. Prior: 2026-07-17, JPY 10d RV line, KB-VIO-117)
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

> ⚠️ **KB-VIO-147 AUDIT APPLIED 2026-07-30 — every line now carries LEVEL + INSTRUMENT + WINDOW.** A threshold with only a level is not a specification: on 7/29 I graded stand-down (i) by reading its *registration* rather than its number and found it was an **entry** guard that had expired at the fill, after presenting it as a live kill-line for the position's entire life. **Audit of this table found 5 of 6 rows with no WINDOW and 4 with no stated BASIS** (settle vs intraday tick) — the SKEW row was the only well-formed one and is the model. **INSTRUMENT is not decoration:** the VIX3M/VIX row reads index-vs-index while the position we held was on the **VX strip**, and on 7/29 the front strip basis inverted (−0.35) while this line read 1.0407 — the guard and the exposure were measuring different things (KB-VIO-129).

| Metric | **LEVEL** | **INSTRUMENT** (what exactly is measured) | **WINDOW** (what counts as a fire) | Why It Matters |
|--------|-------|-----------|----------|----------------|
| VVIX | **120** | `^VVIX` cash index | **SETTLE basis.** An intraday touch is a WATCH, not a fire | Vol-of-vol stress — option market repricing the vol distribution; vol sellers at risk. ⚠️ **Rare-trigger caveat (v3.4):** scarce in the GEX-suppression era — don't size watchlists as if it fires monthly |
| VIX3M/VIX | **1.000** | ⚠️ **CASH INDEX ratio, both legs SAME-SESSION** (`^VIX3M`/`^VIX`). **NOT the VX strip.** ⚠️ `^VIX3M` does **not** publish pre-open while `^VIX` quotes in CBOE global hours — any pre-open ratio is a **cross-date artifact and ungradeable** (guarded in code since 7/30, KB-VIO-149) | **SETTLE basis** | Term-structure inversion — **marks vol peaks, exit-timing signal (KB-VIO-034: 2.2% hit rate as onset predictor). NOT a crash-onset leading indicator.** 🔬 **H3 TESTED 7/30 — the timing claim FAILED, a coverage claim SURVIVED (KB-VIO-152).** The front basis does **not** meaningfully lead this ratio in time (median **+0.5 td**; it never *lagged*, 0 of 4, but that is not a lead). What it does do, over 248 td / 7 peaks: **front basis < −0.5 → 92.0% precision, 6/7 peak-coverage** vs this line's **84.6% / 4/7** — dominating on both axes in-sample, and catching 2 peaks this ratio never saw. Robust across min_dte 3/5/8. ✅ **TESTED OUT OF SAMPLE 7/30 PM (KB-VIO-159):** applied unchanged to **2013-05→2025-07, 3,069 days, 58 peaks never touched by the tuning** — basis **73.2% precision / 49-of-58 coverage** vs this line's **67.5% / 40-of-58**; fire rate stable (12.9%→12.5%), so **not overfit**. ⚠️ **But base-rated honestly: a random flag scores 48.5%, so that is lift 1.51× vs 1.39× — better, not transformative**, and in-sample precision was flattered (87.5%→73.2%). ⚠️ **EVIDENCED, NOT ADOPTED** — the original H3 *timing* claim stays FAILED, −0.5 remains an in-sample-chosen level, and swapping a registered line deserves a deliberate thesis bump with provenance. **This line stays as written on the cash index** |
| 20d SKEW avg | **140** | **20-day average** of `^SKEW` — ⚠️ **NOT the daily close**; the two break at different times and were historically conflated (MEMORY principle 10) | **Sustained 4+ td below.** Single-day dips are noise; sustained runs DO occur near termination (4 td 5/5-5/8, 8 td 5/18-5/28 2026) | Elevated-SKEW regime termination test (R-series regimes, KB-VIO-043/061). *Model row for this table — it was the only one already carrying all three fields* |
| VIX | **30 / 40** | `^VIX` cash spot | **SETTLE basis**, ≥1 close through | Regime lines: >30 equity stress confirmed; >40 crash regime (credit-vol lead relationship inverts above 40) |
| JPY 10d RV (USDJPY, carry→vol) | p90 WATCH / p95 FIRE (percentile-anchored, **re-derived each run**; Aug-2024 unwind anchor 18.0) | 10-day realized vol of USDJPY spot. Confirm leg = **FXY OI-weighted near-ATM call IV** ⚠️ which is thin and goes STALE off-RTH — `jpy_vol.py` flags it; **never broadcast a stale IV/RV ratio** (KB-VIO-141) | **State on the daily run.** RV is the leg the read rests on; the IV leg is confirmation only and may be absent | Carry-unwind → equity-vol transmission (KB-VIO-102 Aug-2024 replay class). IV/RV >2× = event premium priced; →1× w/o RV spike = risk passed; **RV>IV = unwind underway**. Owner: VIOLET (transmission) / SAM (substance). `scripts/jpy_vol.py`, boot-wired; KB-VIO-117. Route on FIRE: outbox SAM + PROME |
| OVX/VIX ratio (oil-vol→equity-vol) | ratio WATCH **p90** / FIRE **p95**; **FLOOR** OVX level ≥ **p75** (all percentile-anchored, full history 2007–, **re-derived each run** — do not hard-code) | `^OVX`/`^VIX`, both cash. ⚠️ **The ratio alone is blind to a common-mode move** — on 7/29 OVX rose 11.5% while the ratio looked flat (3.25→3.27) *because VIX rose too*; **always read the OVX LEVEL beside the ratio** | **State on the daily run** (context canary, **NOT an action-gate**) | Oil-vol→equity-vol **transmission** read (KB-VIO-081; VIOLET owns transmission, BRENT/HAWK own oil substance). Ratio isolates oil-vol LEADING from a broad co-move (Ukraine-2022 class = high OVX, low ratio = REFUSE); level floor rejects low-VIX artifacts. `scripts/ovx.py`, boot-wired; KB-VIO-120 |
| **COR1M first-tell** *(registered 8/10 — 2026-08-10 financial-conditions forum, Will-ruled in-session, FINAL §5)* | **≥ 8.43** (the 2026-07-29 pre-decline anchor), **2 consecutive sessions** | CBOE `_COR1M` (S&P 500 1-month implied correlation index) — `cdn.cboe.com/api/global/delayed_quotes/quotes/_COR1M.json` or `implied_corr.py` | **SETTLE basis only, not intraday tick** (COR1M has same-session-reversed before, 8.43→6.88 on 7/29→7/31); standing, no forward expiry | Vol-side migration first-tell: the correlation-collapse mechanism behind "suppressed, not asleep" equity vol reversing — idiosyncratic stress starting to co-move. KB-VIO-188. **Companion, not a substitute:** the harder self-falsifier (COR1M fresh low <6.77 **while** JPY RV<IV sustained **and** OVX<45 **and** MOVE<66.00, all in the same window) is the conjunctive test that a persistently *low* COR1M does NOT, on its own, argue against migration — KB-VIO-189 |
| **MOVE pause/resume** *(registered 8/10, same forum ruling)* — governs the rising-vol registration commission's rates-vol candidate, not a standalone regime line | **Retire** candidate: close **< 66.00**. **Re-arm**: close **≥ 72.41 for 2 consecutive sessions** | `^MOVE` proxy via `move.py` (investing.com PRIMARY, yfinance cross-check) | Settle basis; reuses the existing N1/F1 lines (KB-VIO-116) — invents no new number | Mechanical pause/resume for the Option-1 rising-vol design (PROME 7/31/8/5 commission) so the next session inherits a rule, not a fresh judgment call. **STATE: RE-ARMED 2026-09-01.** The re-arm condition (close ≥72.41 on **two consecutive sessions**) was met on **8/31 75.32 → 9/1 77.88**, and has since held **four consecutive closes** above the line (9/2 79.71 · 9/3 74.68) without once printing below it. ⇒ the rates-vol candidate is **back inside** the rising-vol registration commission; PROME consumed this 2026-09-04 and carries it on WQ-177. ⚠️ **Stated rather than hidden:** it re-armed on 9/1 and MOVE has since rolled over to 74.68 — **still above 72.41, so the re-arm stands exactly as written**, but the run that triggered it has largely given back (KB-VIO-223). A rule that re-arms two sessions before its underlying signal rolls over is worth a look at the rule; that is a separate question and does not override the mechanical state. ⚠️ **THIS CELL WAS WRONG FOR THREE SESSIONS AND THAT IS THE DURABLE LESSON:** it read *"Current: 72.03 [8/7], between the two lines, neither retired nor re-armed"* until **2026-09-04** — a 28-day-old reading describing a state that ended on 9/1. The rule was registered (KB-VIO-190) precisely *"so the next session inherits a rule, not a fresh judgment call"*, and **three sessions booted after the re-arm and none graded it**. A registered line with a purely mechanical condition should be graded by CODE at boot, not by a session remembering the rule exists — same remedy as KB-VIO-226. ⚠️ **And this cell should not carry a live reading at all** — this file's own header rule says *"Live readings, margins, and current-episode gates live in `STATUS.md`, never here."* The STATE is a rule outcome and belongs here; the **level** does not. KB-VIO-190, KB-VIO-231 |

⚠️ **SKEW>140 is NOT a VIOLET-owned trigger line — do not add one.** A "tail-reload watch" at this level was proposed in the 8/10 forum and **withdrawn** on discovering RED already owns a live, currently-armed guard on the identical number ("SKEW re-cross >140 re-opens the Acute vol leg," `AGENTS/RED/CALENDAR.md` § Standing guards) — looser than the proposed VIOLET version (single-session, no sustain count) and would fire first by construction. Arrangement: same as RED-FT-06 — **VIOLET supplies the measurement** (routine SKEW pulls), **RED adjudicates the re-open**. KB-VIO-191.

---

## OUTBOUND (pointer only)

VIOLET's outbound signal protocol lives in `CLAUDE.md` (write-back step 12): **NEXUS_BRIEF.md is the primary cross-agent surface; `outbox/` is reserved for 🔴 acute, time-sensitive signals only.** No outbound routing rules are defined in this file.

---

**Review triggers (per template):** thesis version change · threshold line breached/shifted · new vector enters domain · received signals not needed (add exclusion) · missed a signal that mattered (add intake).

*Rebuilt to SIGNAL_INTAKE_TEMPLATE.md v0.1 on 2026-06-10, orchestrator-verified (first conformant version — the Apr 12 original predated the 4/14 rollout and was never restructured). Prior content was archived at `archive/SIGNAL_INTAKE_2026-04-12_pre_template.md`, but the whole `VIOLET/archive/` dir was deleted in the 2026-06 public-prep prune (`1cb18fbc`/`7133b7d6`) — recover via git history only (ref fixed 2026-07-11, DAEDALUS L4 packet #5). Trade setups and sizing live exclusively in TRADE.md / thesis (KB-VIO-079 canonical base-rate table).*
