# AEOLUS · WATER — hydrology (drought · water levels · allocation)

**Created:** 2026-08-13 · **Scope broadened same day** (Will: *"I was thinking this would handle drought, water levels, etc."*) · **Owner:** AEOLUS

---

## WHAT THIS FOLDER IS

**The physical state of water across the US and the major trade basins** — and the **shared upstream input** that sets conditions on four separate channels.

> **`water/` is the hydrological twin of `../regime/`.** `regime/` holds the **atmospheric** driver (ENSO); `water/` holds the **hydrological** state it produces. **Neither is a channel and neither gets a score** — they are the roots that the channels' signs are derived *from*, and counting a root once is the whole job of the Independence column (**L-02**).

### The correction that produced this scope (Will, 2026-08-13)

The first build scoped this folder to **allocation + navigation** only, and filed **drought (USDM) inside `wildfire/SOURCES.md`** — because that was where I happened to be using it that session. **That was a misfiling of a shared instrument into one consumer's folder.** Drought is not wildfire's instrument. It is upstream of **four** channels at once:

```
                    ┌─→ C2  crops / food            (soil moisture → yield)
   DROUGHT ─────────┼─→ C4  wildfire fuel state     (fuel dryness → fire potential)
   (USDM, PDSI,     ├─→ C5  river navigation        (low flow → barge draft)
    soil moisture)  └─→ C6  reservoir allocation    (low inflow → shortage tier)
```

**Filing a shared input under one consumer makes it invisible to the other three.** It also let the same dataset produce a *different* read in two places without anyone noticing — the exact failure the reconcile-to-one-figure rule exists to prevent.

## SCOPE — what lives here

| Layer | Instruments | Feeds |
|---|---|---|
| **Drought** | USDM (D0–D4), Palmer/PDSI, soil moisture | **C2 · C4 · C5 · C6** |
| **Snowpack** | NRCS SNOTEL basin % of median (Apr-1 sets allocation) | C6 · C2 |
| **Streamflow** | USGS NWIS gauges — **incl. Lees Ferry, the compact division point** | C6 · C5 |
| **Reservoirs** | USBR elevation — Powell, Mead | **C6** (allocation) |
| **River stage** | WSV/PEGELONLINE (Rhine), USACE (Mississippi/Ohio) | **C5** (navigation) |
| **Groundwater** | USGS NWIS well levels; Ogallala as long-horizon | C2 · watch-note only |
| **Allocation policy** | Reclamation shortage tiers, Colorado Post-2026 Guidelines, compacts | **C6** |

**Major navigable trade rivers under Will's standing directive (2026-08-03):** **Rhine · Mississippi/Ohio · Yangtze · Danube · Paraná** + the **Panama** chokepoint. *An empty river read is a gap to close, not idle background.*

**Not mine — route, don't deep-dive:** hydro **generation** → **WATT** (I own the water, WATT owns the MW) · ag/municipal **cost** → **CARL/MARCO** · data-center **capex** → **VULCAN** · ag-lending/muni **credit** → **REGINALD/CREED** · **Florida** → **CORAL**.

## ⚠️ THE TWO SPLITS THAT MUST NOT BLUR

**① C6 allocation vs C5 navigation — different mechanisms, different clocks.**

| | **C6 ALLOCATION** | **C5 NAVIGATION** |
|---|---|---|
| Mechanism | reservoir depletion → shortage-tier/compact decision → delivery cuts + hydropower loss | low stage → barge draft limits → freight ↑ → goods/industrial cost |
| Instrument | reservoir **elevation** vs a decision threshold | **gauge level** vs navigable minimum + freight rate |
| Clock | **quarters** (policy) | **weeks** (physical) |

**② Colorado and the Rhine are SEPARATE ANTECEDENTS.** The Colorado runs on the **ENSO / Western-hydrology** root shared with C2/C3; the **Rhine is an independent European basin.** ⚠️ **Never stack them as convergent evidence.**

## 🔴 THE SOURCING RULE THIS FOLDER ENFORCES (L-15)

**Use the issuing agency. Never a tracker.**

On 2026-08-12 I published Lake Powell at **3,524.20 ft, "risen 2.2 ft"** from a tracker. The **USBR primary** said **3,520.37 ft, having fallen every day for 15 days** — wrong by **3.83 ft and wrong on the trend sign**, which made my conclusion the exact inverse of the truth. I was grading against a **0.45 ft** margin using sources that disagreed by **3.83 ft**.

> **Before grading any threshold: what is the margin, and what is the source spread? If spread ≥ margin, a secondary is UNUSABLE — not merely less precise.**

**And never cite percent-full.** The 19%-vs-23.1% conflict that cost me a session came from trackers using different capacity bases. **Elevation is the threshold instrument.**

## FILES

| File | Purpose |
|---|---|
| `README.md` | this charter |
| `DOSSIER.md` | live hydrological state — drought, levels, flows, the Colorado system, rivers |
| `AGENT.md` | Spawn brief for a domain worker — scope, instrument vocabulary, hard limits, return contract. |
| `RUN_REPORT.md` | **The deliverable of the most recent worker run** (overwritten each run). Absent = no run, or a run that died. |
| `workbook/SERIES.tsv` `LOG.tsv` | **Observations** — time series + dated events. Keyed by `(date, instrument)`; append-only. |
| `SOURCES.md` | **verified working pull commands** — copy-paste, never reconstruct |

⚠️ **Central `workbook/` stays canonical** — no forked ledger here.
