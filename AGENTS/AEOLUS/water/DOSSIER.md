# AEOLUS · WATER — live dossier

**As-of: 2026-08-13.** All figures primary (USDM API / USBR / USGS NWIS / WSV). Consolidated from KB-AEO-035/036/041/044/047-052/054/056.

> **Last real data refresh: 2026-08-13**  ·  **Dossier written: 2026-08-13**
> *Two-clock header (PAT-044) — `scripts/ledger_staleness.py` reads the first line. **The data date, not the edit date**: a hygiene edit must NOT bump it.*
> **Observations → `water/workbook/SERIES.tsv`** · findings → central `workbook/KB.tsv` · synthesis → `STATUS.md`. **Flow is one-way.**
> **Feeds:** C2 · C4 · C5 · C6 (root: owns drought + reservoirs + streamflow + river stage)

---

## 1. DROUGHT — the shared upstream input

| Category | 7/28 | 8/04 | **8/11** | Move |
|---|---|---|---|---|
| **D1–D4** (drought) | 47.89% | 48.54% | **50.38%** | **crossed 50%** |
| D0–D4 (incl. abnormally dry) | 67.92% | 70.95% | **73.62%** | +5.7 pp in 2 wks |
| D3 (extreme) | 10.00% | 9.51% | **10.27%** | |
| D4 (exceptional) | 0.86% | 0.95% | **1.04%** | |

**Every severity tier up week-over-week.** Deterioration concentrated in **Oklahoma and the Texas Panhandle**; improvement in parts of the Northeast/Southeast.

### 🔑 The same dataset produces OPPOSITE verdicts on two channels — and the geography is why

| Channel | Verdict | Basis |
|---|---|---|
| **C4 fire** | **firms** | southern-Plains dryness → NIFC's Aug outlook newly adds **TX, OK, Lower Mississippi Valley** |
| **C2 crops** | **refuses to confirm** | corn **61%** / soy **62%** G/E (wk-end 8/09) — **6 pts above my <55% band** |

⇒ **A national drought headline is not a channel signal.** Before reading drought into *any* channel, **pull the state/county cut and check the geography actually overlaps the exposure.** Running one dataset into two channels without that check is how both get mis-scored — and it is precisely the error that filing drought under `wildfire/` would have kept invisible.

---

## 2. 🔴 THE COLORADO SYSTEM (C6)

| Instrument | Value | As-of | Margin |
|---|---|---|---|
| **Lake Powell** | **3,520.37 ft** | 8/12 | **0.45 ft** above the all-time low **3,519.92** (2023-04-13) |
| **Lake Mead** | **1,039.82 ft** | 8/12 | **4.82 ft** above **Hoover 1,035** — the *binding* economic threshold |
| **Lees Ferry release** | **7,862 cfs** (Aug 1-12 mean) | 8/12 | **lowest in 9 years, −42.4% vs avg** |
| Colorado ROD | Final EIS published 7/31 | 7/31 | earliest ROD **~8/30** · target **~10/1** · **expiry 12/31/26** |

**Powell has fallen on every one of the 15 days 7/29 → 8/12** (mean −0.157 ft/day). **It should break its all-time low within days.**

#### 8/13 second pass — re-pull at 15:10 UTC, USBR has NOT posted 8/13

- **USBR 919/49 and 921/49 both still end 2026-08-12.** Powell **3,520.37**, Mead **1,039.82** — **byte-identical to yesterday's pull, no revision.** The record-break print is not yet available; **8/13 elevations do not exist at the primary as of this pass.**
- **The 3,519.92 threshold is now verified AT the primary, not carried.** Full-series scan of 919/49: the **post-1980 minimum is 3,519.92 ft on 2023-04-13**, and 2026-08-12's **3,520.37 ranks 6th-lowest on record** (the five below it are all 2023-04-09 → 04-15). *(The file's absolute minimum, 3,394.50 on 1964-05-11, is initial-fill and is **not** the operative record.)*
- **Daily declines 7/29→8/12: 15 of 15 negative**, mean **−0.158 ft/day**, range **−0.11 to −0.23**; the two largest single-day drops are the two most recent bracketing days (8/10 −0.23, 8/12 −0.21). **Rate stated, not extrapolated** (L-16).
- **Powell storage now logged alongside elevation** (919/17): **5,406,671 af (7/29) → 5,282,197 af (8/12)** = **−124,474 af in 14 days, ≈ −8,891 af/day.** The volumetric leg of the same drawdown; elevation remains the threshold instrument.
- **Lees Ferry back-filled daily** (8/01–8/11 were previously held only as the Aug 1-12 mean). Range **7,720–7,950 cfs**, **no trend within the window** — the 42% deficit is a *level*, not a still-deteriorating slope.

##### ⚠️ Powell has its OWN Aug→Sep base rate — and it points the same way as the current slope

`Aug 12 → Sep 30` change, USBR 919/49:

| 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| −6.48 | −4.84 | −4.22 | −4.47 | −7.86 |

**5 of 5 years decline; mean −5.57 ft.** Unlike Mead's Aug→Sep *rise*, this base rate is **not** contingent on Glen Canyon releases arriving — **Powell is the reservoir those releases drain**, so a low-release year is if anything a *weaker* drawdown than the sample. **The driver check (L-16) is therefore satisfied in the opposite direction from AEO-10's**: the mechanism behind Mead's base rate has changed, the mechanism behind Powell's has not. **Stated as an observation — AEOLUS grades.**

### 🔴 NEW 8/13 — the Powell↔Mead coupling is now MEASURED, not inferred

**Colorado River at Lees Ferry, mean daily discharge, Aug 1-12** *(this gauge sits below Glen Canyon Dam — it **is** the release that refills Mead)*:

| 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | **2026** |
|---|---|---|---|---|---|---|---|---|
| 14,425 | 14,933 | 14,000 | 12,483 | 11,953 | 16,575 | 12,408 | 12,400 | **7,862** |

**2026 is the lowest of nine years — 42.4% below the 2018-25 mean, and 34% below even the worst prior year (2022).**

**Yesterday I *inferred* this from USBR's projection** ("USBR forecasting Mead below every recent seasonal path is consistent with reduced Glen Canyon releases"). **Today it is measured.** The inference was right and the mechanism is confirmed.

### ⚠️ …and it CONTAMINATES the base rate I used yesterday — stated plainly

**AEO-10** (Mead does **not** breach 1,035 through 12/31, 80%) was registered on the seasonal base rate: *Mead rises Aug→Sep in 4 of 5 years* (+3.29, +2.96, +1.95, +2.89; 2021 −0.12).

> 🔑 **But Mead rises in those years BECAUSE Powell releases arrive — and 2026 releases are 42% below that sample's average. The base rate's generating mechanism has changed, so the base rate does not transfer.**

**This is the limit of L-16, found one day after writing it: a base rate is only valid while the mechanism producing it still holds.** Checking the *driver* is a separate step from computing the *rate*.

**Disposition — confidence HELD at 80%, basis CHANGED:**
- ❌ **No longer** "the seasonal base rate says Mead rises."
- ✅ **Now** "USBR projects **1,037.10 ft by 12/31** — a projection that already prices the reduced release schedule — leaving **2.1 ft** of buffer above 1,035."
- ⚠️ **Open and unquantified:** I have **not** base-rated USBR's own 24-month-study projection error. Until I do, the 2.1 ft buffer has no error bar and the 80% is a judgment, not a computation.
- **Falsifier to watch:** Lees Ferry releases falling further, or Mead tracking below USBR's monthly projection path.

### The hydropower leg (WATT owns generation — reconcile to one figure)
- **Hoover @ Mead 1,035 ft** = **economic** threshold: capacity **1,274 → 382 MW**; below it operating cost exceeds the power's value (Final EIS **TA-15**).
- **Glen Canyon @ Powell 3,490 ft** = a **~52% derate, not a cliff** (~630 MW vs 1,320 at 3,700). Generation ceases *below* 3,490.
- **Most of the loss is already realized:** combined generation **−27.6% vs the 2016 peak** (−6,285,948 MWh/yr, EIA). **Two-thirds of the decline predates any threshold being touched** — a threshold-watching frame misses it.

### ⚠️ El Niño does NOT refill the Colorado
The robust El Niño wet signal is the **Southwest / Lower Basin**. **Powell's inflow is UPPER Basin**, near the ENSO precipitation **dipole pivot** where the signal is weak and sign-ambiguous. **The wet anomaly lands downstream of the reservoir that needs it.** *(B2 — a do-not-assume, not a directional call.)*
⇒ **The ROD (~10/1) and the 12/31 expiry are decided at the hydrological bottom; relief arrives spring-2027 at the earliest. The policy clock and the hydrology clock are two quarters out of phase.**

---

## 3. 🔴 RIVER NAVIGATION (C5)

### Rhine at Kaub — record broken, still broken

| | |
|---|---|
| **Level** | **12–13 cm** (WSV, 8/13 15:15 CEST); 3-day range **10–17 cm** |
| **Prior all-time low** | **25 cm** (2018, set in **October** — 2026 did it in **August**) |
| **Loadings** | **~16% of normal** (~800 t vs 5,100 t) |
| **Freight** | **~€150/t** vs ~€20 normal |
| **Macro cost** | **German Q3 GDP −0.1/−0.2% (€1.2–2.3B)** — Kiel Institute |

**Held at 4, not 5:** the upgrade trigger's second leg is a **Duisburg cutoff**, and **reduced loading is not a suspension.** Relief needs weeks of rain; risk flagged **into October**.

**The unpriced join (→ DEWEY, delivered 8/13):** EU gas storage is at a five-year low (**59.32%**, ~10–13 pp light), dangerous *conditional on a cold winter*. **The Rhine adds a second conditional — even a normal winter draws harder if the barge leg is impaired, because the substitutes for gas move by water.** ⚠️ Mechanism A2; **magnitude unpulled and not asserted.**

### Other watched rivers
- **Mississippi / Ohio** — ~normal. **Autumn (Sep–Nov) is the window.**
- **Yangtze · Danube · Paraná** — ⚠️ **no current read. Open gaps under Will's standing directive.**
- **Panama** — **8/13: the ACP primary was checked and returned a documented NEGATIVE, which is the first real data on this gap.** The Advisories-to-Shipping index's newest entry is **A-46-2024 (FY2025 December)**; Notices-to-Shipping for 2026 lists **only the standing N-01…N-13 permanent notices.** ⇒ **No 2026 advisory imposing a draft or transit restriction is published at the issuing authority.** ⚠️ **Neither page publishes a transit COUNT**, so the `panama_transits` instrument is **still not sourced** — the "~38 transits" figure carried above has **no primary behind it in `SOURCES.md`** and should be treated as unverified until one is registered. **AEO-04 resolves on a binding restriction; none is published — but "not published on these two pages" is narrower than "does not exist."**

**Rhine at Kaub, 8/13 re-pull (17:00 CEST):** **13.0 cm**, unchanged from the 15:15 reading. Intraday 8/13 **10–14 cm**; 8/12 **10–13 cm** (the logged 8/12 point of 11.0 sits inside that band). **Still through both the 40 cm uneconomical line and the 25 cm 2018 record.**

---

## 4. SNOWPACK · GROUNDWATER

- **Snowpack:** seasonally near-zero in August — **correctly empty, not a gap.** Resumes as an instrument ~Nov; **Apr-1 % of median sets allocation.**
- **Groundwater / Ogallala:** long-horizon structural depletion. **Watch-note with the horizon stated** — not a score-mover until it reaches an acreage / cost / water-rights-pricing decision (C6 discriminator).

---

## 5. WATER AS AN AI-SITING CONSTRAINT

Water is the **third constraint on AI data centers after credit and power**. **New Aug 2026: Texas made water-use disclosure a condition of ERCOT grid access** (Abbott directive → PUCT/ERCOT audit of a 474 GW / >1,800-project queue, ~90% data centers).
⇒ Converts water from **an estimate** into a **regulatory filing with named projects, owners and volumes.**
⚠️ **An audit DIRECTIVE, not a published dataset** — no completion date, no commitment that filings become public. **Prospective, not live.** VULCAN owns capex; WATT owns the queue.

---

## OPEN QUESTIONS / GAPS

1. **🔴 Powell record break — daily check, ~2-3 days out.** On the print: **AEO-06 HIT**, **C6 → 4**, route. **Do not pre-fire.**
2. **🔴 Base-rate USBR's 24-month-study projection error** — AEO-10's 80% currently rests on a 2.1 ft buffer with **no error bar**.
3. **Track Lees Ferry weekly** — it is the leading indicator for Mead, ahead of Mead's own elevation.
4. **ROD watch ~8/25**, ahead of the earliest legal ROD 8/30.
5. **Panama 8/15** — ⚠️ **the gap is now specific, not vague: `SOURCES.md` has no command that returns a transit COUNT.** The ACP advisory/notice pages carry restriction *documents*, not the daily transit number. **AEO-04 needs either a registered count source or re-specification onto the published-advisory instrument that does exist.** *(Checked 8/13; the negative is logged in `workbook/LOG.tsv`.)*
6. **Yangtze / Danube / Paraná** — ⚠️ **no live read AND no entry in `SOURCES.md`.** These cannot be pulled without registering a primary first — **the blocker is a missing source registration, not a missed pull.** Gaps under the standing directive.
6b. **Mississippi has a working primary but no registered instrument.** USGS `07289000` Vicksburg discharge returns cleanly — **349,000 cfs on 8/12** — but **gauge height (`00065`) returns an empty `timeSeries`** at the daily-values service, and no Mississippi name exists in the observation vocabulary. **Needs an instrument name before it can be logged.**
7. **Upper-Basin snowpack for winter 2026-27** — the leg that tests the dipole-pivot guard. CPC DJF outlook (~8/20) is the first read; Apr-1 resolves it.
