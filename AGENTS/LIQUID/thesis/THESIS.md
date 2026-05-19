# LIQUID — Core Thesis v2.0

**Last Updated:** 2026-05-19 | **Conviction:** 65% (partial, channel-dependent) | **Status:** 🟠 ACTIVE — credit channel ambiguous (APO co-trigger fired Day 7+), duration channel firing externally (30Y 5.168% fresh life-high 5/19)

> **Read-with:** `STATUS.md` (live state), `STRATEGY.md` (playbook), `workbook/KILL_MEMO_HY_OAS_260.md` (trigger ladder), `thesis/CHANGELOG.md` (how this view evolved), `thesis/TIMELINE.md` (forward decision windows).

---

## §1 — Core Frame

The financial system's three structural buffers are gone: RRP depleted to ~zero, foreign official sector demand for USTs structurally eroded ($300B+/yr hole, possibly $600–1080B), and basis-trade leverage ($1.85T at 50–100×) has replaced the absent bid. With buffers absent, the bear thesis transmits through whichever channel is currently active. **Channel migration is normal; thesis-abandonment requires multiple channels failing simultaneously.**

LIQUID monitors its own active channels (repo plumbing, credit spreads). Other channels (duration / yield, FX-repat, oil-CPI loop) transmit *into* LIQUID's domain from outside-agent territory; LIQUID tracks them at named interfaces, not as primary signals.

---

## §2 — What LIQUID Actively Owns (Narrow Scope)

| Domain | Primary metrics | Notes |
|---|---|---|
| Repo plumbing | SOFR, SOFR-IORB, SRF usage, RRP, reserves (WRESBAL), Fed BS (WALCL/TREAST), CP-TBill | Currently dormant after April resolved-mechanical |
| Credit spreads | HY OAS, IG OAS, CCC OAS, CDX-cash basis | Bilateral framework: 320 confirm / 260 kill |
| Public-BDC mark catch-down | BIZD level, BDC NAV deltas (FSK -9.9% Q1) | The Stage 3→4 transmission proxy |
| PC public-equity sentiment | APO, ARES (level, day-count >$130 / >$120) | APO co-trigger per HEARTBEAT line 80 |
| Basis-trade exposure | $1.85T leverage estimate, tenor concentration | Structural tracking, not real-time |

**LIQUID does NOT actively own** (received from interfaces): individual bank fundamentals (REGINALD), BDC fundamentals (BROCK), Japan macro / BOJ (SAM), equity market structure / gamma (HENRY), oil and geopolitical (HAWK / BRENT), yield curve dynamics (BOND, when active).

---

## §3 — Three Structural Failure Legs

| Leg | Owner | Setup (structural) | Active transmission (5/19) |
|---|---|---|---|
| **A — Fed rate-control fragility** | LIQUID-primary | RRP $0, reserves $3.02T draining toward $2.7T floor, Fed BS stealth-growing via T-bills (TREAST $4.266T → $4.359T, +$93B in 7 weeks via reinvestment despite QT narrative). Buffers absent. | DORMANT. April SOFR-IORB +7bps breach resolved mechanical (tax-day TGA build, KB-LIQ-051). SOFR-IORB -10 to -12bps currently. |
| **B — Foreign / Treasury-bid erosion** | LIQUID (flow); BOND (price, when active) | $300B+/yr demand hole, potentially $600–1080B (ZHAO Mar 12 upgrade, KB-LIQ-002). Japan + China + Korea + Gulf as four anchors. 30Y tenor priced by missing FOI bid. | **PRICING via 30Y** — 5.168% on 5/19 (fresh life-of-cycle high, first time above 5.046 since May 5; first time above 5% sustained since 2007). 10Y 4.647, +40bps over a month. |
| **C — Basis-trade hidden leverage** | LIQUID | $1.85T at 50–100× leverage, ~40% of marginal UST demand. Latent. Detonated by duration vol or repo stress. | LATENT. No detonation signal yet. |

---

## §4 — Transmission Channel Map

| Channel | Owner | Speed | 5/19 Status | Interface signal |
|---|---|---|---|---|
| Repo / SOFR spike → basis-trade unwind | LIQUID | HOURS | DORMANT | SOFR >3.70 sustained or SOFR-IORB >0 on non-tax-day |
| Credit spread widening | LIQUID | DAYS–WEEKS | **AMBIGUOUS** — HY OAS 280bps, compression run, APO co-trigger fired Day 7+ | 320 confirm / 260 kill (see §5) |
| Duration / yield repricing | BOND → LIQUID | DAYS | **ACTIVE** — 30Y 5.168 fresh life-high 5/19, +24bps/wk | 30Y sustained >5%, 10Y sustained >4.5% (KB-LIQ-052) |
| PC gate → dealer inventory → public marks | LIQUID / BROCK | WEEKS | ACTIVE — Stage 3 narrative recognized (Mar 25), Stage 4 pending | 2nd PC fund hard-gate, BCRED Q2 |
| Japan repatriation → UST selling | SAM → LIQUID | DAYS | ARMED, not firing | USD/JPY 160 trigger (currently 159.18, 0.82 away) |
| Oil-CPI loop → term premium | HAWK/BRENT → LIQUID | WEEKS | ACTIVE — Brent $110.57 reigniting April-CPI loop | Brent sustained >$100; back-month curve shape |

**Channel migration finding (KB-LIQ-052):** During the 32-day Apr 16 → May 18 staleness gap, the active transmission migrated from PLUMBING (Leg A, resolved) into DURATION (BOND-domain channel). The bear thesis didn't die; it changed addresses. Plumbing remains structurally fragile but is not the currently-firing leg.

---

## §5 — Bilateral Credit Framework

| Level | Implication | Action |
|---|---|---|
| HY OAS sustained >320bps | **Confirmation** — credit channel transmitting, systemic credit stress | Escalate to ALL agents (LIQ-01) |
| HY OAS 350bps | Issuance freeze begins | Position-scale escalation |
| HY OAS 400bps+ | Forced selling / full systemic | Crisis pricing |
| HY OAS 270–310 range | Hold / monitor | No action |
| HY OAS sustained <265 (≥2 sessions) | TRIGGER A — cut credit-thesis-only positions to half | See KILL_MEMO ladder |
| HY OAS <260 intraday | TRIGGER B — full credit-channel kill drill | See KILL_MEMO |
| HY OAS sustained <260 (≥3 sessions) | **TRIGGER C — credit-channel killed** (HEARTBEAT line 80) | Full kill, re-frame around duration only |
| **APO >$130 ≥3 sessions** | Co-trigger — public-equity PC sentiment recovered | If concurrent with HY OAS compression run, treat as Trigger C precondition even without 260 breach |

**Currently:** HY OAS 280 (20bps cushion above 260, closest of cycle 276 on 5/17). **APO co-trigger fired since 5/12 (Day 7+ as of 5/19).** Per KILL_MEMO co-trigger language, this is a Trigger C precondition.

**Gamma-suppression caveat (5/14 signal):** Positive gamma may suppress VIX and HY OAS prints even while substance accumulates (FSK NAV -9.9%, 2nd US bank failure 5/16, Brent reflation $98→$110). The 276–282 HY OAS floor that held May 6 → May 17 may be *tape, not signal*. Cross-verify any sub-280 print against CCC OAS and 10Y direction before treating as substance.

---

## §6 — Stagflation Trap (Structural)

**DOUBLE CONFIRMED** (Mar 10 + Apr 7–8): oil crashes do not produce bond rallies. Term-premium / FOI-exit pressure exceeds inflation-relief impulse. Safe-haven flows go to gold / JPY / cash, not 30Y bonds. 60/40 portfolio mechanics broken in both directions.

**Reinforced 5/19:** Brent $110.57 *and* 30Y 5.168 simultaneously is the textbook configuration. Oil up → inflation up → no Fed cut → debt service rising → supply growing → bid weakening → 30Y up. Doom-loop dynamics with no policy exit while supply / demand asymmetry persists.

---

## §7 — Kill Conditions

LIQUID stands down its bear thesis when:

| Condition | Channel killed |
|---|---|
| HY OAS sustained <260 ≥3 sessions | Credit-channel only (Trigger C) — see KILL_MEMO. Other legs may persist. |
| 10Y back below 4.30% sustained AND HY OAS <270 | Both credit + duration unwinding — full thesis reassessment |
| Fed expands liquidity facilities (SRF reform, standing repo, restart QE) | Leg A killed — Fed buffer restored |
| TIC confirms FOI buying resumed for 2+ consecutive prints | Leg B killed — demand hole closing |
| Ceasefire confirmed + Brent sustained <$90 + 10Y <4.30 | Stagflation trap leg killed |
| USD/JPY <140 (disorderly carry unwind) | DIFFERENT thesis activates — yen carry breakdown, not LIQUID core |

**Channel-kill vs full-thesis-kill is the key distinction.** v1.0 framework treated thesis as monolithic. v2.0 explicitly: each channel can kill independently; full abandonment requires multiple legs failing concurrently.

---

## §8 — Cross-Agent Interface Table

**LIQUID sends to:**

| Condition | Target | Priority |
|---|---|---|
| HY OAS >320bps confirmation | ALL | 🔴 |
| HY OAS <260 sustained (Trigger C) | ALL + PROME | 🔴 |
| SRF usage >$50B sustained | REGINALD, HENRY, PROME | 🔴 |
| Auction failure (BTC <2.0x) | ALL | 🔴 |
| Reserves <$2.8T | PROME | 🟠 |
| 2nd PC fund hard-gates | BROCK, REGINALD | 🟠 |
| APO Day 3+ >$130 | BROCK, PROME | 🟠 |
| Belgium proxy >$500B (RED proxy data) | SAM, PROME | 🟠 |

**LIQUID receives from:**

| Source | Signal type |
|---|---|
| BOND (when active) | Auction granular bid mechanics, yield curve shape, term-premium decomposition, dealer positioning |
| SAM | BOJ moves, USD/JPY level, Japan trade balance / repat acceleration |
| BROCK | BDC stress, PC gate events, BCRED redemption ramp |
| HAWK / BRENT | Oil price, Hormuz status, war-risk insurance, Gulf sovereign spreads |
| REGINALD | Bank-specific funding stress (KRE, WAL, OZK), Y-14Q NDFI exposure |
| HENRY | Equity / VIX / gamma context, retail flow signals |
| CARL / OTTO | Consumer credit health (ABS, subprime auto DQ, payment hierarchy) |

**BOND placeholder:** BOND agent scaffold exists (`AGENTS/BOND/`) but is not yet active. When BOND stands up, the following will migrate to BOND-primary with LIQUID-receive interface: yield curve dynamics, term-premium decomposition, granular auction absorption mechanics, dealer positioning. The thesis-level legs (FOI demand hole as flow, basis-trade leverage) remain with LIQUID.

---

## §9 — Epistemic Notes (Durable Findings)

| Finding | Source | Implication |
|---|---|---|
| **Channel migration** | KB-LIQ-052 (May 2026 revival) | When one transmission leg resolves, the bear thesis can fire through another. Scan all channels before declaring thesis abandonment. Don't read a single-channel resolution (e.g., SOFR-IORB normalizing) as full thesis-kill. |
| **1-day SOFR-IORB sign flip ≠ structural confirmation** | KB-LIQ-051 (Apr 15 mechanical) | Tax-day / quarter-end / settlement-window single prints are mechanical, not structural. Require 3+ sessions on non-mechanical catalyst before treating as Leg A activation. |
| **Trigger watch goes dormant during staleness** | May 2026 revival lesson | The APO co-trigger fired 5/12 (Day 3) and was missed for 6 sessions during LIQUID's 32-day gap. On revival (or any session after a gap), run a full named-threshold sweep with live data, not just a STATUS surgical edit. With Will's stated plan to run agents more often, this risk diminishes but doesn't disappear. |
| **Public-equity PC sentiment can decouple from underlying marks** | TCW Red Lobster 98%/par (Apr 14), FSK Q1 NAV -9.9% (5/18) | APO / BIZD price action is not a reliable Stage 3 indicator on its own. Cross-verify against actual NAV prints and gate events. |
| **Gamma-suppression hypothesis** | 5/14 Will/Prome signal | Positive gamma can suppress VIX / HY OAS prints even with loud substance accumulating. Treat too-calm prints during loud-substance windows as tape, not signal. Watch for gamma unwind as gap risk. |
| **Active channel migration without thesis abandonment** | Apr 16 → May 18 gap | Bear thesis stayed intact by migrating PLUMBING → DURATION. The agent's primary channels went dormant while transmission continued through external-domain channels. This is the operational lesson behind §1's "channel migration is normal" framing. |

---

## Open Questions (Carrying into Next Session)

1. **POSITIONS read still gating action** on HYG $75P Jun x10 given APO co-trigger fired and Trigger C precondition held ~7 sessions.
2. **Is the HY OAS 276–282 compression run gamma-suppressed tape, or genuine credit-channel resolution?** Resolution arrives via either (a) gamma unwind producing OAS gap-wider, or (b) sustained sub-265 confirming genuine resolution.
3. **Stage 4 PC transition timing** — BCRED Q2 redemption window is the structural test; BROCK leads, LIQUID watches BIZD/BDC mark catch-down.
4. **30Y 5.168 stickiness** — BOND-domain primary question, but feeds LIQUID's Leg B confirmation and dealer-balance-sheet drag. Watch for >5% to hold ≥5 sessions as durable regime.

---

*Domain: Financial plumbing — repo markets, credit spreads, foreign Treasury demand, basis trade, public-BDC mark transmission. Transmission interfaces at duration / FX-repat / oil-CPI channels owned by BOND / SAM / HAWK.*
