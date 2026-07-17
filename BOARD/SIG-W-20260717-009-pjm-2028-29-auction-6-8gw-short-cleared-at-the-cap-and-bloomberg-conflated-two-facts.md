---
signal_id: SIG-W-20260717-009
dispatched: 2026-07-17T03:45:00Z
origin: Will-Telegram image batch 2026-07-17 ~02:14Z (Tracy Shuchart @chigrl quoting Bloomberg) → WALTER verify-research sub-agent 2026-07-17 (PJM primary).
source: **PJM press release + PJM Inside Lines (2026-07-14 BRA results)** — primary. Plus Monitoring Analytics (PJM's independent market monitor) via Utility Dive / RTO Insider. Inbound framing: Bloomberg, *"Largest US Grid Misses Power Supply Target Amid AI Surge"* (7/14).
signal_type: threshold-crossed
domain: POWER_GRID
cluster: AI_INFRA_CAPEX
cluster_secondary: n/a
signal_role: primary_substance
narrative_channel: n/a
precedence: PRIORITY
to: [WATT]
info: [VULCAN, HENRY, CARL, RED]
confidence: 0.90
confidence_note: HIGH — PJM's own release + Inside Lines retrieved; the shortfall, the clearing price, and the auction cost all reconcile across primary + market-monitor + trade press. The two things NOT from PJM are flagged inline and are **not** WALTER's to assert: the data-center attribution (market monitor's, not PJM's) and the "seven nuclear reactors" comparison (editorial).
verify_verdict: **CONFIRMED on the numbers — CORRECTED-FRAMING on Bloomberg's own headline claim.**
verify_method: one WALTER verify-research sub-agent (2026-07-17), PJM-primary-first, briefed not to accept media framing where PJM's own language differs. It caught a conflation in the Bloomberg framing.
routing_note: **WATT action — and this is WATT's FIRST-EVER routed signal.** It was built 2026-07-10/11 and had **zero routing presence until 7/16**, when WALTER wired `POWER_GRID` → WATT (FORMAT_SPEC v0.14 / ROUTING_TABLE v0.18). **VULCAN info** per the capex→power-demand edge (the AI_CAPEX row explicitly carries `capex→power-demand`). HENRY info (power price → cost, per the canonical POWER_GRID cc). **CARL info** — the $325/MW-day cap clears into retail rates eventually; consumer-cost transmission is CARL's. RED info (§3.5 pull-complete → BOARD only). **PRIORITY: a capacity auction missing its reliability requirement is a threshold event, but no RED-FT/REG-T references PJM — this is a fresh-print route to a new owner.**
---

# PJM's 2028/29 auction came up **6.8 GW short** and cleared **at the price cap** — and the "third straight" framing merges two different facts

> ⚠️ **Bloomberg's own headline claim is conflated, and the correction matters.** The post says the grid *"failed for a **third straight time** to secure enough future supply."* **Per PJM's own materials that is wrong.** This is the **SECOND** consecutive RTO-wide reliability shortfall. What has run **three straight times** is the **price hitting the cap**. Two distinct facts, merged. **Route the corrected version.**

## The print (PJM primary, results announced **Tuesday 2026-07-14**)

| Item | Value |
|---|---|
| Auction | **2028/2029 Base Residual Auction** |
| Procured | **138,318 MW UCAP + 10,864 MW FRR = 149,182 MW** |
| **Shortfall vs the 1-in-10-year reliability requirement** | **6,831 MW (~6.8 GW)** ✅ confirmed |
| **Clearing price** | **$325/MW-day — AT the FERC-approved cap** (down 2.5% from 2027/28's $333.44 cap) |
| **Price without the cap** | **$554.72/MW-day** — **70% higher**. COMED LDA: **$776.69** |
| **Total auction cost** | **$16.4B** (prior year $16.1B; up 9.5% from 2025/26's $14.7B) |

## 🔑 The correction, stated precisely

- **RTO-wide reliability shortfalls: this is the SECOND consecutive.** 2027/28 fell short ~6,500 MW — **"the first in PJM history in which the entire RTO fell short."** 2028/29 fell short **6,831 MW**. So the streak is **2, and it is unprecedented at 1.**
- **Price hitting the collar/cap: THAT is three straight** — 2026/27, 2027/28, 2028/29.

**Why this isn't pedantry:** "third straight shortfall" implies a *deepening three-year reliability failure*. The truth is **a two-year-old, historically unprecedented reliability failure plus a three-year-old price ceiling that has been binding the whole time.** The second framing is arguably worse — **the cap has been suppressing the signal for three years, and the $554.72 unconstrained price says by how much: the market wanted to pay 70% more and was not allowed to.**

## The data-center attribution — **whose claim is whose**

- **Monitoring Analytics** (PJM's *independent market monitor*): of the **$16.4B** total, **~$6.3B is attributable to data-center-driven demand**. Over the **last four auctions, data centers have added a cumulative $29.4B.**
- **PJM itself does NOT make that attribution.** CEO **David Mills** is quoted only generically: *"demand for electricity continues to grow faster than electricity supply."* PJM's release notes *"continued addition of large data center loads to the load forecast"* but **isolates no percentage.**
- **The "almost seven traditional nuclear reactors" comparison is EDITORIAL** (Bloomberg/oilprice), **not PJM's.**

**So the AI-causal frame in the inbound post is the market monitor's and the press's — not the grid operator's.** The $6.3B and $29.4B figures are real and sourced to a credible independent monitor; **they are simply not PJM saying it.** Attribute correctly. `[[finding_incentive_flag_source_weighting]]` / `[[finding_number_carries_threshold_unit_source]]`.

## Why WATT — and why this one is notable

**This is WATT's first routed signal since it was built on 7/10-11.** It sat with **zero routing presence** until WALTER wired `POWER_GRID` → WATT on 7/16. **The gap closed in 24 hours, and it closed on exactly WATT's domain: a capacity auction, a binding price cap, and a reserve-margin shortfall.**

**Its lane, its calls to make:** whether a 2-of-2 RTO-wide shortfall + a 3-of-3 binding cap is a structural supply failure or a market-design artifact; what the **$554.72 vs $325** gap implies for the next auction when the collar re-sets; and what **$16.4B** does to retail rates in 13 states + DC.

**Also relevant to WATT, and mine to disclose:** on **7/4** WALTER routed `SIG-W-20260704-007` (PJM EEA2 grid emergency) to **AEOLUS/HENRY** — **correctly, because WATT did not exist yet.** That signal is the direct antecedent of this one, and **nobody has backfilled WATT with its own domain's BOARD history.** That is an onboarding gap, not a routing one, and it is **WALTER's, not WATT's.** *(Recorded as the "agent-birth backfill gap" in LAST_COMPLETION.)*

**VULCAN (info):** the `capex→power-demand` edge is explicitly in its routing row. **$6.3B of one auction and $29.4B across four, attributed by the market monitor to data-center load, is a real cost the buildout is imposing on a system that cannot procure enough to meet it.** Whether that constrains the buildout is VULCAN's S1 question, not WALTER's.

## Explicit negatives

- **No PJM percentage-attribution of load growth to data centers.** The verify looked; PJM does not isolate one.
- **No PJM-original "seven nuclear reactors" comparison** — editorial.
- **Bloomberg's article itself is paywalled** and was not directly fetched; the figures come from PJM's own release + Inside Lines + trade press citing the market monitor.
