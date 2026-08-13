# AEOLUS — sub-agent architecture · DESIGN FOR REVIEW

**Status: PROPOSAL — nothing built.** · **Author:** AEOLUS · **Date:** 2026-08-13
**Directed by Will:** *"STATUS can't hold everything a domain should be tracking. STATUS should be the synthesized version with key data points. I am thinking each of these sub folders should have their own workbooks. We can have AEOLUS spawn these sub agents and act as the orchestration synthesis layer?"*
**Decisions already taken by Will (8/13):** spawning is **on-demand by need**, not every session · **design reviewed before build.**

---

## 1. THE PROBLEM, RESTATED PRECISELY

STATUS.md is doing two incompatible jobs: **the synthesized view** *and* **the primary record**. At 154 lines against a 250-line cap it already strains, and the strain is not from too many findings — it is from **domain depth that has nowhere else to go.**

## 2. 🔑 THE KEY DISTINCTION — and it changes the design I expected to write

I planned to propose splitting `workbook/KB.tsv` across the five folders. **The migration survey says don't.** Two hard findings:

**① The rows worth most are cross-domain.** 11 of 59 rows carry multiple channel tags; **KB-053 alone touches six.** The highest-value rows are precisely the synthesis ones — the WATT ENSO sign answer (045), the self-caught MARCO inversion (046), the C2-vs-C4 drought discrimination (056), the base-rate-contamination finding (059). **A folder split fragments exactly the rows that justify having a knowledge base.**

**② A migration would silently misfile.** Early rows have schema drift — **KB-002/003/004/014/017 carry `DerivedFrom` values in the `Vectors` column.** Any automated migration keyed on that column mis-sorts them, and 19 rows carry cross-references that would break. **The migration is the risky part of this proposal and the survey says it is also the unnecessary part.**

**So the split is not KB-by-domain. It is by KIND of data:**

| Layer | Holds | Lives in | Example |
|---|---|---|---|
| **SYNTHESIS** | convergence matrix, scores, exit triad, BOTTOM LINE | `STATUS.md` | "C6 3🟠, Powell 0.45 ft from record" |
| **FINDINGS** | sourced, dated, durable conclusions — **frequently cross-domain** | `workbook/KB.tsv` **(central, unchanged)** | "the base rate is contaminated because releases fell 42%" |
| **OBSERVATIONS** | time series, event logs, the raw domain tracking | **`<domain>/workbook/` (NEW)** | Powell daily elevation 2021-2026; Lees Ferry Aug means by year |

> **The gap is the OBSERVATION layer, and it is real and measurable.** Today I computed Powell's five-year seasonal base rate and Lees Ferry's nine-year August series, used them for two findings, and **threw the underlying data away.** Next session I recompute both from scratch. **That is pure waste, and it is also a correctness risk — a recomputed series can silently differ from the one a published conclusion rested on.**

**⇒ NO MIGRATION. `KB.tsv` stays central, live and unchanged.** Domain workbooks are **new, forward-only, and hold data that does not exist anywhere today.** Nothing breaks because nothing moves.

## 3. LAYER CONTRACT — direction of flow

```
   OBSERVATIONS  →  FINDINGS  →  SYNTHESIS  →  Will / other agents
   <domain>/workbook/   KB.tsv     STATUS.md      packets, NEXUS_BRIEF

   sub-agent owns  │  AEOLUS adjudicates  │  AEOLUS owns
```

**Flow is one-way and that is the anti-drift mechanism.** A number appears **once** as an observation; a finding **cites** it; STATUS **summarizes** the finding. **STATUS never holds a number that isn't traceable down the stack** — which is exactly the drift risk I created this morning and could not close.

## 4. DOMAIN WORKBOOKS — schemas

Each domain gets `<domain>/workbook/` with **two files minimum**:

### `SERIES.tsv` — the time series (append-only)
```
date	instrument	value	unit	source	pulled_at	notes
2026-08-12	powell_elev	3520.37	ft	USBR-919-49	2026-08-13	primary
2026-08-12	lees_ferry_q	7930	cfs	USGS-09380000	2026-08-13	daily mean
2026-08-11	usdm_conus_d1d4	50.38	pct	USDM-API	2026-08-13	valid date
```
**`instrument` is a controlled vocabulary per domain**, declared in the folder README. **`source` names the endpoint, not a description** — so any row is re-pullable.

### `LOG.tsv` — dated events/observations that aren't a series
```
date	event	detail	source	pulled_at	routed_to
2026-08-13	nhc_two	AL92 80/80 "expected to weaken - strong upper-level winds"	NHC-TWO	2026-08-13	
```

**Optional third, domain-specific** (e.g. `hurricane/workbook/STORMS.tsv`, `seismic/workbook/EVENTS.tsv`).

**IDs:** observations need **no ID scheme** — they are keyed by `(date, instrument)`. **This avoids the ID-namespacing problem entirely.** Only findings have IDs, and those stay `KB-AEO-NN` in the central ledger.

## 5. 🔑 THE SHARED-INPUT RULE (the thing that broke this morning)

**An observation lives in the folder that OWNS the instrument, never in a folder that CONSUMES it.**

| Instrument | Owner | Consumers |
|---|---|---|
| USDM drought | **`water/`** | C2 crops · C4 fire · C5 navigation · C6 inflow |
| ENSO indices | **`regime/`** | C1 · C2 · C3 · C5 · C6 |
| Reservoir elevation, streamflow | **`water/`** | C6 · C5 |
| NIFC PL / acreage | **`wildfire/`** | C4 |
| NHC / CSU / NOAA seasonal | **`hurricane/`** | C1 |

**Consumers CITE, never copy.** A wildfire finding that depends on drought cites `water/workbook/SERIES.tsv` rather than restating the number. **This is the direct fix for the misfiling Will caught, applied one level down before it can recur.**

## 6. SUB-AGENT CONTRACT

**Model precedent: ANVIL** (PROME's reconcile clerk) — a spawned worker with a defined job, owned by an orchestrating agent. **No thesis, no decisions, no roster seat, no inbox, not routed to by WALTER.**

### What a domain worker READS (the folder is already its briefing packet)
1. `<domain>/README.md` — scope, boundaries, what routes elsewhere
2. `<domain>/SOURCES.md` — **verified commands + known-bad list**
3. `<domain>/DOSSIER.md` — current state
4. `<domain>/workbook/SERIES.tsv` — what's already recorded

### What it DOES
Pull the instruments in `SOURCES.md`; append to `SERIES.tsv`/`LOG.tsv`; refresh `DOSSIER.md`.

### What it RETURNS (structured, to me)
```
observations_added:  N rows
threshold_state:     per registered threshold — value, band, FIRED/NOT-FIRED
changes:             what moved vs the previous read
proposed_findings:   candidate KB rows, with sources — NOT written to KB
gaps:                instruments it could not pull, and the error
```

### ⛔ HARD LIMITS — what a worker must NOT do
- **Never write to `workbook/KB.tsv`, `PREDICTIONS.tsv`, `STATUS.md`, or any file outside its folder.** It *proposes* findings; **I adjudicate.**
- **Never score a channel, fire a trigger, or resolve a prediction.** Those are synthesis-layer acts.
- **Never route to another agent.** All cross-agent packets stay mine.
- **Never substitute a source.** If a `SOURCES.md` command fails it **reports the failure** — it does not go find a tracker. *(This is the direct guard against L-15; the whole reason `SOURCES.md` exists is so a worker never has to choose a source.)*
- **Never assert a threshold is "approached" as if breached.** Report the number and the margin.

### Why this contract shape
The failure I most fear from spawned workers is **a confident wrong number entering the record unadjudicated** — Critical Rule #3, and the exact shape of yesterday's tracker error. **Making findings proposal-only means a worker's error costs me a rejected proposal, never a corrupted ledger.**

## 7. SPAWN TRIGGERS (on-demand — Will's ruling)

Spawn a domain worker when **any** of:
1. A **dated catalyst** for that domain is within its window (`CALENDAR.md`)
2. Its dossier is **stale** relative to its instrument cadence (USDM weekly, NASS weekly, USBR daily, NHC daily-in-season)
3. A **threshold is near firing** (the Powell record watch is the live example)
4. An **inbox signal** routes to that domain
5. **I need depth** I don't have for a synthesis question

**No trigger ⇒ no spawn, and that is a correct outcome.** `seismic/` will usually not spawn — by design.
**Record in SCRATCH which domains spawned and why**, so a quiet domain is visibly a decision rather than an oversight.

## 8. WHAT STAYS MINE (the synthesis layer)

Convergence matrix + scores · independence accounting · **cross-channel discrimination** (the C2-vs-C4 drought call is the archetype — **no single domain worker could have made it**) · adjudicating proposed findings into KB · `PREDICTIONS.tsv` and all grading · all cross-agent routing and packets · `STATUS.md` and BOTTOM LINE · thresholds and triggers.

## 9. RISKS & OPEN QUESTIONS — honest list

| # | Risk | Mitigation / status |
|---|---|---|
| R1 | **Spawn cost.** 5 workers/session is real tokens | On-demand triggers (§7); most sessions spawn 1-2 |
| R2 | **Worker hallucinates a number** | Findings are **proposal-only**; `SOURCES.md` removes source choice; I verify before adjudicating |
| R3 | **`SERIES.tsv` grows unbounded** | Append-only + dated; revisit at ~5k rows. **Note USBR/USGS hold full history — I can always re-pull, so this is a convenience store, not a system of record** |
| R4 | **Dossier drift** (the risk I created this morning and did NOT close) | **Add the content-derived `Last real data refresh: YYYY-MM-DD` two-clock header (PAT-044) to every DOSSIER — `scripts/ledger_staleness.py` reads it.** ⚠️ **Should ship WITH this, not after** |
| R5 | **C2 (crops) and C3 (energy) have no folder** — 8+ KB rows homeless | **Open question below** |
| R6 | Worker writes outside its folder | Contract forbids it; **I check `git status` before committing**, as today's WALTER halt showed works |
| R7 | The observation layer becomes make-work | **Only record instruments a threshold or prediction actually consumes.** No collecting for its own sake |

### ❓ Open questions for Will
1. **Does `crops/` become a 6th folder?** C2 has a genuine observation layer (weekly NASS G/E by crop and state) and currently has no home. **My lean: yes, but AFTER this ships — one change at a time.**
2. **C3 energy demand — leave inline?** **My lean: yes.** WATT owns power pricing; my C3 is a detection layer and its weather driver already sits in `regime/`. A folder would mostly mirror WATT.
3. **Should DAEDALUS see this?** It is the fleet architect and this is a structural change to an active agent. **My lean: notify after Will approves, as information rather than a gate** — these are intra-agent workers with no roster seat, so no ROSTER/WALTER/NEXUS obligations change.

## 10. BUILD PLAN (on approval)

| # | Step | Risk |
|---|---|---|
| 1 | Add `Last real data refresh:` two-clock header to all 5 DOSSIERs **(R4 — do first)** | none |
| 2 | Create `<domain>/workbook/` + `SERIES.tsv`/`LOG.tsv` headers; declare instrument vocab in each README | none |
| 3 | Backfill the series **I already pulled today** — Powell/Mead daily, Lees Ferry annual Aug means, USDM 3 weeks, Kaub, NHC, NIFC, USGS quakes, volcano alerts | none — **recovers work already done and currently discarded** |
| 4 | Write `<domain>/AGENT.md` — the spawn brief encoding §6 | none |
| 5 | Update `CLAUDE.md`: layer contract, spawn triggers, shared-input rule, hard limits | none |
| 6 | **Dry-run ONE worker** (`water/` — richest, has a live threshold) and check its return against a manual pull | **the real test** |
| 7 | Only then treat the model as live | — |

**Nothing in steps 1-5 touches `KB.tsv`, `PREDICTIONS.tsv`, `STATUS.md` or any existing row. The proposal is purely additive** — which is why I am confident recommending it despite the scale.

---

**Recommendation: approve steps 1-6, with step 6 as a real gate rather than a formality.** If the `water/` worker's return doesn't match a manual pull, the contract is wrong and I would rather find that on one domain than five.
