# MARCO FINDINGS INDEX
**Last Updated:** 2026-09-24 (s30 stale sweep — vintage flags on the bucket claims; prior 2026-06-15) | **Purpose:** Category map of MARCO research docs. Not a synthesis — a navigator. For live state see `STATUS.md`.

---

## How to use this file

Each section below is a **thesis bucket**. Under each bucket: the research docs that support or bound it, one line each. Follow the path to read the full writeup. When a bucket has a live data tool, it's called out.

---

## 🟠 SDL-01 — Self-Deportation Ledger (mark UNRULED since 2026-09-24: ELEVATED on YoY / CRITICAL on 2-yr — the old BREACHED was a retracted-2.2M residue; formalized VX 2026-04-21)

**Core claim:** a structural foreign-born labor-supply shock — **~1.0M realized labor-force decline / ~1.5M population** (NFAP/BLS-CPS; FRED LNU01073395), not cyclical. *(RE-MARKED v2.6, 2026-07-02: the prior "~2.2M self-deported (CBO)" figure was wrong — a mis-attributed disputed-DHS claim, NOT CBO, which estimates ≈290K+30K voluntary; direction/mechanism unchanged. Corroborated by June-2026 total LF −1M+ YoY. See thesis magnitude note + KB-MARCO-WFD-SDL-02.)* Transmission quantified via 1930s historical template.

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

**Core claim:** US-born citizen emigration rising (IRS expatriation list H1 2026 3,243 names, +38.5% YoY, trailing-4Q 5,790 — 9/24 FR count; the old "Q1 2025 +102% YoY" was quarter-on-quarter; Brookings net migration negative first time since ~1935). WSJ "1930s levels" headline PARTIALLY SUPPORTED. Not tradeable yet — 2-3yr watch.

📁 `domain/sources/EMG/`

| Doc | What it contains |
|-----|------------------|
| `EMG_WSJ_VALIDATION.md` | WSJ "1930s levels" claim validation. Net-migration angle supported; citizen-exodus angle hyperbole. |
| `EMG_DATA_STREAMS.md` | Data stream scoping: IRS Federal Register quarterly expatriation lists, Canada IRCC US-PR stats, Portugal AIMA. Recommended watch sources. |

**Upgrade trigger:** 3+ quarters IRS Federal Register >1,500 AND Canada IRCC US PRs >500/mo sustained.

---

## 🔴 LABOR — H-2A, Slaughter, Meatpacking

*(⚠️ Bucket claim below is Mar–Jun-2026 framing, kept as the index's record. Since thesis v3.0 (7/31) the labor **quantity** shock is well-measured but its **transmission to prices/costs is UNDEMONSTRATED** after three pre-registered nulls — read `thesis/THESIS.md` Channel 1 before citing any of it.)* **Core claim:** Ag labor is broken — federal surveys defunct (NASS canceled, NAWS walled), H-2A certified demand up +9.3% with 4.1% backlog, JOLTS hires at COVID-low means substitution mechanism broken (no domestic reserve). Meatpacking labor has NOT yet disrupted — but beef-belt consolidation is happening independently.

📁 `domain/sources/LABOR/`

| Doc | What it contains |
|-----|------------------|
| `AG_LABOR_ALT_SOURCES_MAR26.md` | Replacement framework for canceled NASS/NAWS surveys. OFLC H-2A + BLS QCEW + NASS Crop Progress + State H-2A visas + CPI F&V. |
| `OFLC_H2A_PULL.md` | H-2A certified FY25 = 398,059 (prior "415K" was positions REQUESTED). FY22→25 trajectory, +9.3% apps, FL #1 at 56,818. Wayback CDX methodology for Akamai wall. |
| `SLAUGHTER_MONITOR.md` | Weekly USDA multi-species throughput. Cattle -11.1% is 75yr-low herd cycle (NOT labor). Hog z-score is the clean labor proxy. |
| `BEEF_BELT_CONSOLIDATION.md` | Why Tyson/JBS/Cargill plant closures in Great Plains are SEPARATE from SDL-01. 1990-wave immigrant workers relocate within US, don't self-deport. Candidate for VX-BEEFBELT-01 distinct vector. |

🔧 Live tools: `tools/h2a_pull.py`, `tools/slaughter_pull.py`

---

## Live state — pointers ONLY (not restated here)

Live values drift between sessions; this navigator deliberately does **not** carry them (single-source-of-truth — restating values here is exactly the staleness this file is meant to prevent). Read the owner doc:

- **Current dashboard, active situations, thesis-inflection block** → `STATUS.md`
- **Canonical thesis (v3.2 — Channel 1 DEMOTED from spine, Channel 4 LOW after the 9/24 fiscal-terminus rebuild), 5 transmission channels, conviction-by-channel, kill conditions** → `thesis/THESIS.md` · version-transition log → `thesis/CHANGELOG.md` · dated event spine → `thesis/TIMELINE.md` *(version corrected v2.5 → v3.1 on 2026-08-12: this navigator line had been **6 versions adrift** and is boot-read. Found by `scripts/version_drift_check.py`, built the same day for exactly this class.)*
- **Predictions** (full detail + resolutions) → `thesis/PREDICTIONS.tsv`
- **Live indicator vectors** → `workbook/VX.tsv` · knowledge base → `workbook/KB.tsv` · transmission/cascade mechanics → `workbook/FLOW.tsv`
- **Forward catalysts / dates** → `docket/CATALYSTS.tsv` (machine feed) + `docket/CALENDAR.md` (countdown)
- **Cross-agent synthesis brief** → `NEXUS_BRIEF.md` · session handoff → `SCRATCH.md` · persistent learnings → `MEMORY.md`

---

## Other archived/reference material

- `domain/sources/_archive/` — old STATUS snapshots.
- `archive/`, `handoffs/`, `research/`, `sub_agents/` — older working files, pre-reorg.
