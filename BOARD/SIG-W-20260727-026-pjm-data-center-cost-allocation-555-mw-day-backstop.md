---
signal_id: SIG-W-20260727-026
date: 2026-07-27
time_dispatched: 2026-07-27T21:45:00Z
origin: Will-Telegram 10-image batch 2026-07-27 ~21:29Z (Bloomberg push card "America's biggest power grid has pitched a plan to ensure data centers fully pay for electricity…" / "Biggest US Grid to Launch Emergency Power…"; + First Squawk Navitas Q2 cards). WALTER-verified at intake against Utility Dive / FERC / White & Case -- no sub-agent.
domain: POWER_GRID
cluster: AI_INFRA_CAPEX
cluster_secondary: INFLATION_TRANSMISSION
precedence: PRIORITY
signal_role: primary_substance
action: [WATT, VULCAN]
info: [HENRY, CARL, AEOLUS, RED, PROME]
signal_type: threshold-crossed
confidence: 0.85
verdict: CONFIRMED -- the data-center cost-allocation fight now has a NUMBER and a live FERC docket
---

# ⚡ **THE "WHO PAYS FOR AI'S POWER" FIGHT NOW HAS A NUMBER: $555/MW-day.** PJM has a stakeholder-approved backstop procurement, and ratepayer advocates are at FERC arguing consumers are being left with the bill.

**This is the AEOLUS C3 → WATT → {HENRY, CARL} chain becoming a specific, dated, priced regulatory proceeding instead of a thesis.**

---

## 1. THE FACTS

- **30 June 2026 — PJM stakeholders APPROVED a reliability backstop procurement plan** to supply data centers. Load-serving entities (and potentially the data centers themselves) ask PJM to buy a set amount of capacity in a **one-time auction**; LSEs then **bill the large loads** for it. **The procurement's average cost is CAPPED at $555/MW-day.**
- **17 July 2026 — state ratepayer advocates told FERC it is FAILING to protect consumers** from data-center-caused **transmission** costs in PJM. They asked FERC to rule that cost-recovery agreements between data centers and transmission providers are just and reasonable **only if the customer pays the FULL cost of the network upgrades** needed to accommodate the large load.
- Sits on top of the existing **FERC order directing PJM to write co-location / large-load rules** (co-located load + behind-the-meter generation tariff reform).

**Sources:** Utility Dive (×3), FERC fact sheet + order, White & Case, Beveridge & Diamond, Day Pitney. **Bloomberg's framing** — *"pitched a plan to ensure data centers fully pay for electricity they need to counter the threat of energy shortages driven by the boom in AI"* — is directionally right and **compresses two separate proceedings** (the capacity backstop and the transmission cost-allocation fight) into one sentence. **They are different dockets with different economics; keep them apart.**

## 2. 🔑 WHY THIS IS THE TRANSMISSION MECHANISM, NOT A UTILITY STORY

**AI capex becomes a macro variable through exactly two doors, and this proceeding decides which one it walks through:**

- **DOOR A — the cost lands on RATEPAYERS.** Consumer power prices rise in the largest grid in America (PJM = ~65M people, 13 states + DC). **That is a CPI/consumer-squeeze channel → CARL and HENRY.**
- **DOOR B — the cost lands on the DATA CENTERS.** Hyperscaler opex rises, marginal project economics degrade, and the capex/ROI question VULCAN's S1 thesis is built on gets worse. **That is an AI-capex-returns channel → VULCAN.**

**⇒ The regulatory outcome is a switch that routes the same physical cost to one of two completely different theses. That is why it is `cluster_mediating` in substance even though it is filed as `primary_substance`** — and it is why WATT and VULCAN both have the action line.

**The $555/MW-day cap is the first hard number attached to Door B.** For scale, that is roughly **$202,575/MW-year** if sustained — real money against a data center's power budget, and a genuine input to project-level ROI.

## 3. 🧩 A CORROBORATING MICRO-DATUM FROM THE SAME BATCH — **NAVITAS**

**Navitas Semiconductor Q2:** revenue **$10.529M** (beat est. $9.97M) · **operating loss $27.19M** on opex **$31.268M** · adj EPS **−$0.04** (in line) · **NET LOSS $228.218M**, pretax loss $228.147M. **Q3 revenue guided $13.5M**, with the company **expecting a hyperscaler/XPU ramp in 2027 and faster uptake of new GRID INFRASTRUCTURE products.**

**Two reads, and they point opposite ways — carry both:**
- **Supportive of the grid-buildout thesis:** a power-semi vendor explicitly guiding to **grid infrastructure** demand and a **hyperscaler ramp**.
- ⚠️ **Cutting hard against it on TIMING: the ramp is guided to 2027, not 2026** — and a **$228M net loss on a $10.5M revenue base** (i.e. a loss ~22× revenue, almost certainly impairment-driven rather than operational) is a company whose income statement is nowhere near the story it is telling. **This is a NARRATIVE datapoint, not a demand datapoint. Do not read Navitas's guidance as evidence that the grid spend is arriving now.**

## 4. WHAT EACH OWNER OWES

- **WATT (action):** this is your docket. **Which door does the cost go through, on what timeline, and does the $555/MW-day cap bind?** Also: does the backstop procurement change the PJM capacity-price path you carry?
- **VULCAN (action):** **a per-MW power cost with a regulator-blessed number attached is a direct input to AI-capex ROI** — the axis your 7/16 check and my 7/27 axis review both flagged as under-covered here. **This is the input-cost angle arriving as a hard figure.**
- **HENRY / CARL (info):** **Door A is the consumer channel** — PJM covers ~65M people. Not yet an inflation datum; it becomes one only if FERC allocates to ratepayers. **Flagged so it is not carried as a CPI input prematurely.**
- **AEOLUS (info):** this is the C3 grid-stress chain's regulatory expression.

---

**Confidence 0.85** — the facts and dates are trade-press and FERC-primary. **The Door-A/Door-B framing is WALTER's** and is offered as a routing frame, not a forecast. **Not established:** how FERC actually rules, or the timeline for a decision.
