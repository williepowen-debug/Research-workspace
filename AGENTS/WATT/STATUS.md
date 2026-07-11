# WATT — STATUS

**Last Updated:** 2026-07-10 (build session — DAEDALUS scaffold + first live read) · **Status:** 🟡 monitoring (structural capacity 🔴; live grid quiet)
**Class:** Market-agent (grid stress → power price → power cost) · **Spawnable by:** PROME or Will · **Maturity:** L1 (scaffold + first read; DAEDALUS FLEET_MAP)

> **Newborn agent, 2026-07-10.** Spun out of HENRY's provisional power leg (Will 7/9→7/10). P1/P2 seeded live this session; **P3/P4 carry inherited/structural reads but need WATT's own first data pull — flagged as gaps to close next session** (channels-first #1 guard).

---

## CONVERGENCE MATRIX (universal 5-pt + local state)

| # | Channel | Score (1–5) | Local state | Independence | Key signal [src, date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| **P1** | Stress → price | **2 🟡** | quiet-but-armed | shares heat-dome antecedent w/ P4 | PJM demand 119.7GW = 88.9% of 24h peak; 3 routine local warnings, **0 emergency-class** [power_watch, 7/11 02Z] | EEA2+ posting OR RT LMP >$1,000 → 5 |
| **P2** | Structural capacity cost | **4 🔴** | confirmed short | independent (auction structure) | 26/27 BRA at **$329.17 cap**; 27/28 at **$333.44 cap**, **6,623 MW short** of reliability req (uncapped sim ~$530) [PJM BRA] | 28/29 BRA (~Dec-26) clears at cap again → 5 |
| **P3** | Data-center demand leg | **3 🟠** *(gap)* | elevated, needs pull | couples to HEN-36 AI-capex | ⚠️ inherited read only — **WATT owes first interconnection-queue + IPP-load pull** (LBNL Queued Up; VST/CEG/NRG/TLN) | queue > 2× peak load OR IPP load-growth guide ↑ → 4 |
| **P4** | Gas → power coupling | **1 ⚪** *(gap)* | no live read | shares heat-dome antecedent w/ P1 | ⚠️ **WATT owes first spark-spread read** (Henry Hub via BRENT + PJM power price) | spark spread compresses 50% or negative → 3 |

**Composite: 10/20** *(P1 2 + P2 4 + P3 3 + P4 1). P3/P4 provisional — re-score after first WATT data pull. P2 carries the thesis; P1 is the live tripwire.*

**Independence note:** P1 and P4 share a heat-dome antecedent (a hot spell drives both demand-spike and gas-burn) — count the shared root once in any composite-stress call. P2 (auction structure) and P3 (buildout) are the two independent structural roots.

---

## LIVE CHANNEL READS (sourced + dated)

- **P1 — Stress → price** [power_watch.py, 2026-07-11 02Z]: PJM demand **119,652 MW = 88.9%** of the 24h peak (134,573 MW @7-10 20Z). Emergency board: **3 postings, all routine/localized** (Post Contingency Local Load Relief — DOM ×2 #105379-80, FE-AP #105378; **0 emergency-class**). Retail backdrop [EIA, 2026-04, ~2mo lag]: industrial **8.66¢/kWh**, residential **18.83¢/kWh**. **LMP price leg NOT wired** — needs `PJM_API_KEY` (free pjm.com registration, ~5min human one-time = Will).
- **P2 — Structural capacity cost** [PJM BRA]: the loud, high-conviction leg. 2026/27 base residual auction cleared at the **$329.17/MW-day cap**; 2027/28 at the **$333.44 cap AGAIN** (uncapped simulation ~$530), and 27/28 cleared **6,623 MW short** of the reliability requirement — driver is data-center load. Structural pass-through to retail/industrial bills is in train (ComEd/BGE/Dominion territory).
- **P3 — Data-center demand leg** ⚠️ GAP: inherited context only (AI-capex buildout, IPP names VST/CEG/NRG/TLN, couples to HENRY HEN-36 ~$290B AI-capex FCF node). **WATT owes the first interconnection-queue + IPP-load pull** (LBNL Queued Up 2026 edition; IPP earnings).
- **P4 — Gas → power coupling** ⚠️ GAP: no live spark-spread read yet. **WATT owes the first read** (Henry Hub from BRENT × PJM power price → gas-fired margin).

**Inherited event context (from HENRY provisional, 7/3–7/10):** PJM **EEA2 on 7/3** (KB-AEO-018) — the one realized emergency event; set the **DOE §202(c) precedent** (PJM can curtail ≥50 MW data centers). This is the n=1 that anchors the recurrence case; the structural tape (P2) is what makes it a thesis rather than a one-off.

---

## EXIT / INVALIDATION (standing-rule-vs-state triad)

| Channel | Standing rule | Current state @ level | FIRED? |
|---|---|---|---|
| P1 | EEA2+ posting OR RT LMP >$1,000 sustained 2+ intervals | quiet — 0 emergency-class, demand 88.9% peak [7/11] | NOT-FIRED (1 prior: 7/3 EEA2) |
| P2 | BRA clears at cap AND short of reliability req | 26/27 + 27/28 BOTH at cap; 27/28 short | **FIRED** (structural, 2 consecutive) |
| P3 | interconnection queue > 2× system peak load | needs first pull | NOT-SCORED |
| P4 | spark spread negative (gas-fired uneconomic) sustained 3+ sessions | needs first pull | NOT-SCORED |

**Fired-count: 1 of 4** (P2 structural). **Thesis-kill vs channel-kill:** a mild summer kills P1's live read for the season — it does NOT kill the thesis, which migrates to P2 (structural capacity) and P3 (buildout). The thesis dies only if the 28/29 BRA clears well below cap AND data-center queues drain — testable ~Dec-2026.

**Cleanest bidirectional flip (BRENT discipline):** the 28/29 BRA clear (~Dec-2026). Clears at cap again → thesis confirmed structural; clears materially below cap with queues draining → structural leg falsified.

---

## OPEN ON WATT (next session)

1. **P3 first pull** — interconnection-queue depth (LBNL Queued Up) + IPP load-growth guidance (VST/CEG/NRG/TLN earnings). Close the gap; re-score.
2. **P4 first pull** — spark spread from Henry Hub (ask BRENT) × PJM power price. Close the gap; re-score.
3. **PJM_API_KEY** — once Will registers, wire the LMP leg into `power_watch.py` (deepens P1 from demand-proxy to actual price).
4. **Seed PREDICTIONS.tsv** — first WATT-NN calls (28/29 BRA clear; summer EEA2 recurrence; IPP load guide).
5. **Process inbox** — HENRY handoff packet (ownership transfer detail), any AEOLUS C3 routing confirmation.

---

## BOTTOM LINE

**WATT is live as of 2026-07-10** — spun out of HENRY's provisional power leg (Will-directed) onto the Step-1 instruments already built. The single most important reading is **structural, not live**: PJM's capacity auctions cleared at cap two years running with 27/28 short of the reliability requirement (P2, 🔴) — power cost is becoming a first-order AI-capex FCF input and a retail-pass-through channel, while the live grid (P1) sits quiet-but-armed (demand 88.9% of peak, 0 emergency-class postings). Next: close the P3 (data-center queue) and P4 (spark-spread) gaps with WATT's own first data pulls, and seed the prediction ledger — the two channels currently carrying inherited reads rather than WATT-owned ones.
