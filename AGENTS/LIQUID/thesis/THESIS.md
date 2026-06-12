# LIQUID — Core Thesis v2.0

**Last Updated:** 2026-06-12 | **Conviction:** 60% (down from 65 — the "duration matured to regime" premise failed recomputation; see CHANGELOG 6/12 pivot) | **Status:** 🟠 ACTIVE — credit channel ambiguous (HY widening 274→280; APO >$130 ×3 closes fired 6/11, NOT Trigger C — concurrency fails), duration channel oscillating around the 5.00 pivot (30Y closed 4.951 on 6/11; unwind test <4.90 untouched), testing downside into FOMC 6/17

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
| PC public-equity sentiment | APO, ARES (level, day-count >$130 / >$120) | APO co-trigger per HEARTBEAT line 80; **day-counts on daily closes only** |
| Basis-trade exposure | $1.85T leverage estimate, tenor concentration | Structural tracking, not real-time |

**LIQUID does NOT actively own** (received from interfaces): individual bank fundamentals (REGINALD), BDC fundamentals (BROCK), Japan macro / BOJ (SAM), equity market structure / gamma (HENRY), oil and geopolitical (HAWK / BRENT), yield curve dynamics (BOND, when active).

---

## §3 — Three Structural Failure Legs

| Leg | Owner | Setup (structural) | Active transmission (6/12) |
|---|---|---|---|
| **A — Fed rate-control fragility** | LIQUID-primary | RRP $0, reserves $3.02T draining toward $2.7T floor, Fed BS stealth-growing via T-bills (TREAST $4.266T → $4.359T, +$93B in 7 weeks via reinvestment despite QT narrative). Buffers absent. | DORMANT (with caveat). April SOFR-IORB breach resolved mechanical (KB-LIQ-051); SOFR-IORB **-5bps (6/11)**. ⚠️ Reserves/SRF/RRP unverified since 4/16 — dormancy is partly assumption pending refresh (punchlist Tier 5). |
| **B — Foreign / Treasury-bid erosion** | LIQUID (flow); BOND (price, when active) | $300B+/yr demand hole, potentially $600–1080B (ZHAO Mar 12 upgrade, KB-LIQ-002). Japan + China + Korea + Gulf as four anchors. 30Y tenor priced by missing FOI bid. | **PRICING via long end — tenor-bifurcated, oscillating not sustained.** 30Y regime record (FRED H.15 canonical): 11 straight closes >5% (5/12–5/27, peak 5.18 on 5/19 — TIMELINE bear test fired), then decay to a 5.00-pivot oscillation — sub-5 closes 5/28–6/4 and 6/11 (4.951, the 30Y-auction relief day). Pre-registered unwind test (<4.90 sustained) never touched; low close of the May–June regime window 4.943 (5/6, CBOE). 10Y below 4.50 on 8 of 13 closes, 5/26–6/11 (FRED basis). June refunding split the demand picture: 10Y reopening 6/10 indirect **78.2%** / dealer 9.5% (STRONG — demand shows at price, corroborates KB-LIQ-057) vs 30Y 6/11 BTC 2.33 / indirect **59.9%** / dealer **14.7%** (SOFT-but-cleared — above the <55% trigger, soft is a grade not a signal fire; market rallied 7bps through it). The demand hole currently expresses as long-bond-specific softness absorbed via price, not auction failure. Resolvers: FOMC 6/17, TIC 6/18. |
| **C — Basis-trade hidden leverage** | LIQUID | $1.85T at 50–100× leverage, ~40% of marginal UST demand. Latent. Detonated by duration vol or repo stress. | LATENT. No detonation signal yet. |

---

## §4 — Transmission Channel Map

| Channel | Owner | Speed | 6/12 Status | Interface signal |
|---|---|---|---|---|
| Repo / SOFR spike → basis-trade unwind | LIQUID | HOURS | DORMANT (SOFR-IORB -5bps, 6/11) | SOFR >3.70 sustained or SOFR-IORB >0 on non-tax-day |
| Credit spread widening | LIQUID | DAYS–WEEKS | **AMBIGUOUS** — HY 280 (6/10), widening into and through the APO fire window (274 on 6/4 → 280 on 6/10); post-hot-CPI | 320 confirm / 260 kill (see §5) |
| Duration / yield repricing | BOND → LIQUID | DAYS | **OSCILLATING** — 5.00-pivot, not sustained (see §3 Leg B); unwind test <4.90 untouched; FOMC 6/17 resolver | 30Y sustained >5%, 10Y sustained >4.5% (KB-LIQ-052 — framing under re-derivation) |
| PC gate → dealer inventory → public marks | LIQUID / BROCK | WEEKS | **ACTIVE-ACCELERATING** — BROCK 6/8: Stage 2→3 pivot, 4-fund gate cluster, 3 regular-div cuts (MFIC/OCSL/OBDC), record 6% April default | 2nd PC fund hard-gate, BCRED Q2 |
| Japan repatriation → UST selling | SAM → LIQUID | DAYS | **TRIGGERED — awaiting flow confirmation.** 4 consecutive closes >160 (6/8–6/11); level is mine, the mechanism (actual repat flows) is SAM's to confirm | USD/JPY >160 crossed; TIC 6/18 next flow read |
| Oil-CPI loop → term premium | HAWK/BRENT → LIQUID | WEEKS | **REVERSED** — Brent closed $90.38 (6/11), peak $110.59; zero sub-$90 closes yet. May CPI still printed hot (4.18% YoY) on lagged energy; passthrough relief is a June+ story | Brent sustained >$100 (re-engage) / sustained <$90 (leg de-escalation watch) |

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
| **APO >$130 ≥3 sessions** | Co-trigger — public-equity PC sentiment recovered (**day-count on closes only**) | If concurrent with HY OAS compression run, treat as Trigger C precondition even without 260 breach |

**Currently (6/12):** HY OAS 280 (6/10, FRED), widening from the 274 cycle-tight (6/4); cushion above the 260 kill = 20bps, direction currently AWAY from the kill. **APO co-trigger:** the May run — initial cross 5/8 ($132.64), one-day dip 5/11 ($129.91), then eight consecutive closes >$130 from 5/12–5/21 — broke 5/22 ($128.51; one-day re-cross 5/27). A new fire printed 6/9–6/11 — three consecutive closes >$130 ($132.70 / $131.14 / $133.91). **This is NOT a Trigger C precondition: the co-trigger escalates only alongside HY OAS *compression*, and HY widened into and through the fire window (274 on 6/4 → 280 on 6/10).** What it did fire is the HEARTBEAT line-80 reassess obligation — resolved 6/12 with the equity/mark-decoupling read (PC equity bid strengthening while the credit tail deteriorates: CCC 957, CCC−BB 787bps; outbox → BROCK, who owns the APO Dec $95P reassess). Day-counts verify on daily closes only — the 6/8 intraday $131.5 was not a close; $127.57 was.

**Gamma-suppression caveat (5/14 signal, restamped 6/12):** The hypothesis described suppressed vol (VIX 15–17) against loud substance. Current tape is the reverse — the VIX floor lifted to 19–22 with two >21 closes within four sessions (21.51 on 6/5, 22.22 on 6/10) while HY sits at 280. Keep the durable lesson (too-calm prints during loud-substance windows are tape, not signal; cross-verify sub-280 prints against CCC OAS and 10Y direction), but the regime it described has shifted — the live question is now credit-vol catch-up, not vol suppression.

---

## §6 — Stagflation Trap (Structural)

**DOUBLE CONFIRMED** (Mar 10 + Apr 7–8): oil crashes do not produce bond rallies. Term-premium / FOI-exit pressure exceeds inflation-relief impulse. Safe-haven flows go to gold / JPY / cash, not 30Y bonds. 60/40 portfolio mechanics broken in both directions.

**Reinforced 5/19:** Brent $110.57 *and* 30Y 5.168 simultaneously is the textbook configuration. Oil up → inflation up → no Fed cut → debt service rising → supply growing → bid weakening → 30Y up. Doom-loop dynamics with no policy exit while supply / demand asymmetry persists.

**Third test (5/14 → 6/12 closes): INCONCLUSIVE-TO-WEAK.** Brent −$22 bought 30Y −22bps / 10Y −18bps from the 5/19 peaks (to 6/11 closes: 4.951 / 4.463), but measured against the pre-spike base (5/14: 30Y 5.01–5.02, 10Y 4.46–4.47) the long end round-tripped to ~flat — and since the 5/15–5/22 spike was auction/FOI-scare-driven, attributing the retracement to Brent at all is uncertain. The trap survives only in weak form: oil −20% produced no duration *rally*, merely a round-trip. Both anchors carried deliberately — anchor choice changes the verdict, so neither is cited alone. Macro texture still trap-consistent: May CPI hot (4.18% YoY headline accel on lagged energy) while claims creep (210k wk-5/16 → 229k wk-6/6).

---

## §7 — Kill Conditions

LIQUID stands down its bear thesis when:

| Condition | Channel killed |
|---|---|
| HY OAS sustained <260 ≥3 sessions | Credit-channel only (Trigger C) — see KILL_MEMO. Other legs may persist. |
| 10Y back below 4.30% sustained AND HY OAS <270 | Both credit + duration unwinding — full thesis reassessment |
| Fed expands liquidity facilities (SRF reform, standing repo, restart QE) | Leg A killed — Fed buffer restored |
| TIC confirms FOI buying resumed for 2+ consecutive prints | Leg B killed — demand hole closing |
| Ceasefire confirmed + Brent sustained <$90 + 10Y <4.30 | Stagflation trap leg killed *(6/12: LIVE-WATCH, not fired — zero sub-$90 Brent closes yet [6/11 closed 90.38], 10Y 4.46 vs <4.30, no ceasefire; deliberate annotation, conditions unchanged)* |
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
| **Day-counted triggers verify on daily closes, never intraday prints** | 6/8 APO miscount (intraday $131.5 vs close $127.57) | An intraday print mis-dated a HEARTBEAT-grade trigger by one day and started a phantom streak. Every day-counted threshold (APO, HY sustained-sessions, USD/JPY) keys off official closes/settles only. |
| **State-file narrative contaminates both writer and grader — re-derive counts from the raw series with source declared** | 6/12 coordinator review (3 instances in one day) | ">5% sustained" survived the agent (6/8) AND an independent reviewer (6/12) while 7 sub-5 closes sat in the record; the reviewer's correction-of-the-correction (APO "ten straight closes 5/8–5/21") also failed recomputation (5/11 closed $129.91). Agreement between layers that read the same STATUS is circular. Counts get recomputed from the raw series, with the source basis (FRED vs CBOE; accepted vs announced) declared inline. |

---

## Open Questions (as of 6/12)

1. **Does the HY widening extend, or was 274→280 noise?** The prior question ("compression: tape or real?") part-resolved — it broke *wider* on hot CPI rather than resolving cleanly through 265. <265 Trigger A remains armed if it re-compresses; >320 confirmation is 40bps away.
2. **FOMC 6/17: does the dot plot vs hot May CPI reprice the Fed-constraint into duration?** The 5.00-pivot oscillation resolves up (regime re-engages) or down (<4.90 sustained = pre-registered unwind) — this is the near-term conviction resolver (60% marked pending it).
3. **Stage 4 PC transition timing** — BCRED Q2 redemption window is the structural test; BROCK leads (substance accelerating per 6/8 read), LIQUID watches BIZD/BDC mark catch-down.
4. **Does Japan repatriation confirm in flows?** USD/JPY level triggered (4 closes >160) but the mechanism is unconfirmed — TIC 6/18 (April flows) and SAM's read are the gates. *(Prior Q4 — 30Y >5% ≥5 sessions — RESOLVED: fired 5/12–5/27, then decayed; regime question inverted to the downside, see Q2.)*

---

*Domain: Financial plumbing — repo markets, credit spreads, foreign Treasury demand, basis trade, public-BDC mark transmission. Transmission interfaces at duration / FX-repat / oil-CPI channels owned by BOND / SAM / HAWK.*
