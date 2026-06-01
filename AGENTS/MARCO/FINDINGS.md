# MARCO FINDINGS INDEX
**Last Updated:** 2026-05-31 | **Purpose:** Category map of MARCO research docs. Not a synthesis — a navigator. For live state see `STATUS.md`.

---

## How to use this file

Each section below is a **thesis bucket**. Under each bucket: the research docs that support or bound it, one line each. Follow the path to read the full writeup. When a bucket has a live data tool, it's called out.

---

## 🟠 SDL-01 — Self-Deportation Ledger (BREACHED, 80% conf — formalized VX 2026-04-21)

**Core claim:** ~2.2M undocumented workers self-deported in 2025 (CBO). Structural supply shock, not cyclical. Transmission now quantified via 1930s historical template.

📁 `domain/sources/SDL/`

| Doc | What it contains |
|-----|------------------|
| `SDL_HISTORICAL_ANALOGS.md` | 1929-33 Mexican Repatriation, 1954 Operation Wetback, 2008-11 Recession — transmission templates and timelines (weeks to 5+yr). |
| `BANXICO_STATE_REVERSE.md` | Methodology + data: US state-of-origin reverse-mapping from Banxico Mexican-state destinations. AZ -6.1%, TX -5.8%, MI -5.6% lead decline; CA least impacted. |

🔧 Live tool: `tools/banxico_reverse.py` → `baselines/us_state_sender_implied.tsv`

**Transmission elasticities (Santanna/Xu NBER 1930s paper, cited in SDL_HISTORICAL_ANALOGS):**
- 8.2pp house value decline per 1% Mexican population drop in a city
- 13.3pp building permit decline per 1 SD repatriation exposure

---

## 🟡 EMG-01 — American Emigration (PENDING/watch, 65% conf)

**Core claim:** US-born citizen emigration rising (IRS renunciations Q1 2025 +102% YoY; Brookings net migration negative first time since ~1935). WSJ "1930s levels" headline PARTIALLY SUPPORTED. Not tradeable yet — 2-3yr watch.

📁 `domain/sources/EMG/`

| Doc | What it contains |
|-----|------------------|
| `EMG_WSJ_VALIDATION.md` | WSJ "1930s levels" claim validation. Net-migration angle supported; citizen-exodus angle hyperbole. |
| `EMG_DATA_STREAMS.md` | Data stream scoping: IRS Federal Register quarterly expatriation lists, Canada IRCC US-PR stats, Portugal AIMA. Recommended watch sources. |

**Upgrade trigger:** 3+ quarters IRS Federal Register >1,500 AND Canada IRCC US PRs >500/mo sustained.

---

## 🔴 LABOR — H-2A, Slaughter, Meatpacking

**Core claim:** Ag labor is broken — federal surveys defunct (NASS canceled, NAWS walled), H-2A certified demand up +9.3% with 4.1% backlog, JOLTS hires at COVID-low means substitution mechanism broken (no domestic reserve). Meatpacking labor has NOT yet disrupted — but beef-belt consolidation is happening independently.

📁 `domain/sources/LABOR/`

| Doc | What it contains |
|-----|------------------|
| `AG_LABOR_ALT_SOURCES_MAR26.md` | Replacement framework for canceled NASS/NAWS surveys. OFLC H-2A + BLS QCEW + NASS Crop Progress + State H-2A visas + CPI F&V. |
| `OFLC_H2A_PULL.md` | H-2A certified FY25 = 398,059 (prior "415K" was positions REQUESTED). FY22→25 trajectory, +9.3% apps, FL #1 at 56,818. Wayback CDX methodology for Akamai wall. |
| `SLAUGHTER_MONITOR.md` | Weekly USDA multi-species throughput. Cattle -11.1% is 75yr-low herd cycle (NOT labor). Hog z-score is the clean labor proxy. |
| `BEEF_BELT_CONSOLIDATION.md` | Why Tyson/JBS/Cargill plant closures in Great Plains are SEPARATE from SDL-01. 1990-wave immigrant workers relocate within US, don't self-deport. Candidate for VX-BEEFBELT-01 distinct vector. |

🔧 Live tools: `tools/h2a_pull.py`, `tools/slaughter_pull.py`

---

## Live state (not in this index) — refreshed 2026-05-31

- **THESIS INFLECTION (2026-05-31):** cyclical stress reversed, structural supply-shock persists. See STATUS.md top block. Durable signal = produce CPI F&V +6.1% YoY (ag-labor stock loss).
- **FL triple exposure** — COOLING. Condo 8.9mo Apr (below 9.0, tightening); Canadian air -8.1% (headline flipped +1.4%); Miami migration -2.0% stale. Aggregate $ stress pushed to winter 2026-27. Lives in `STATUS.md`.
- **DHS shutdown** — RESOLVED Apr 30 (76-day record). ICE/CBP carved to $71.7B reconciliation (text May 4, Jun 1 target). Lives in `STATUS.md`.
- **ICE raids** — PIVOTED OFF FARMS (harvest-protection; enforcement to Democratic cities). Flow softened; 2.2M stock loss irreversible. Lives in `STATUS.md`.
- **Canadian travel** — Apr +1.4% YoY headline (first rise since Dec '24, auto-driven); air channel -8.1% still bleeding. Lives in `STATUS.md`.
- **Remittances** — Mar +4.9% YoY ($5.39B record), Q1 +1.4%; count -3.6% (likely 1% tax pull-forward). Lives in `STATUS.md`.
- **Thesis** — `thesis/THESIS.md` (v2.0, canonical) + `thesis/CHANGELOG.md` (version history) + `thesis/TIMELINE.md`.
- **Predictions** — `thesis/PREDICTIONS.tsv` (MAR-08, MAR-27 now CONFIRMED), active set in `STATUS.md`.
- **Vectors** — `workbook/VX.tsv`.

---

## Other archived/reference material

- `domain/sources/_archive/` — old STATUS snapshots.
- `archive/`, `handoffs/`, `research/`, `sub_agents/` — older working files, pre-reorg.
