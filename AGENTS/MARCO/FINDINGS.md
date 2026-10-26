# MARCO FINDINGS INDEX
**Last Updated:** 2026-10-25 (s37 index/method reconciliation; dated studies remain historical). PRIOR: 2026-09-24 (s30 stale sweep — vintage flags on the bucket claims; prior 2026-06-15) | **Purpose:** Category map of MARCO research docs. Not a synthesis — a navigator. For live state see `STATUS.md`.

---

**Latest evidence:** `domain/sources/TOURISM/2026-10-25_spirit-seat-replacement_LAS.md` — measured domestic seat replacement, MIA Spirit-free correction, and LAS Canadian-capacity refresh with filing gaps. Prior news catch-up: `domain/sources/2026-10-25_news-catchup.md`.

## How to use this file

Each section below is a **thesis bucket**. Under each bucket: the research docs that support or bound it, one line each. Follow the path to read the full writeup. When a bucket has a live data tool, it's called out.

---

## SDL-01 — foreign-born labor-force change (Will-ruled basis; current grade in VX/STATUS)

**Current evidence:** quantity and grade live in VX/STATUS; September foreign-born LF+206KYoY with population-control caveat. Channel1 transmission UNDEMONSTRATED. CBO2025 range in old KB-WFD-04 withdrawn10/25 (WFD-24); no replacement estimate adopted. Historical1930s studies are analogies, not identified present elasticities.

📁 `domain/sources/SDL/`

| Doc | What it contains |
|-----|------------------|
| `SDL_HISTORICAL_ANALOGS.md` | 1929-33 Mexican Repatriation, 1954 Operation Wetback, 2008-11 Recession — transmission templates and timelines (weeks to 5+yr). |
| `BANXICO_STATE_REVERSE.md` | Historical reverse-map methodology; retired as a spatial test 10/14 (fixed weights cannot identify concentrated US-state losses). Current transaction evidence in VX/STATUS. |

Historical model tool, retired as a spatial identification test: `tools/banxico_reverse.py` → `baselines/us_state_sender_implied.tsv`

**Historical-paper elasticities only (not calibrated to current episode; Santanna/Xu paper cited in SDL_HISTORICAL_ANALOGS):**
- 8.2pp house value decline per 1% Mexican population drop in a city
- 13.3pp building permit decline per 1 SD repatriation exposure

---

## 🟡 EMG-01 — American Emigration (LOW/watch; no separate bucket probability)

**Current scope:** IRS covered-expatriate notices are a measured, lumpy receipt-quarter list, not US-born citizen-emigration totals. Current annual-band grade/source availability live inVX-EMG-01; citizen-emigration scale remains UNSCORED. The1930s comparison lacks a citizen-emigration denominator. Unsupported CBO net-migration attribution withdrawn10/25; a Brookings model is a different quantity from citizen departures. Historical studies below retain their own dates.

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
| `BEEF_BELT_CONSOLIDATION.md` | Why Tyson/JBS/Cargill plant closures in Great Plains are SEPARATE from SDL-01. 1990-wave immigrant workers relocate within US, don't self-deport. Historical candidate only; no new vector/collector commissioned. |

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
