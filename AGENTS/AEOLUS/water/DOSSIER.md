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

### 🔴 THE FINAL EIS SHORTAGE MATRIX — PRIMARY-VERIFIED 8/13

**Source: USBR Post-2026 Final EIS, Executive Summary (`P26_FEIS_ExecSummary_508.pdf`), downloaded and text-extracted 2026-08-13.**

> ⚠️ **The EIS does not publish "the cuts." It publishes a MATRIX of maximum shortage by ALTERNATIVE.** Any single triple quoted as "the plan" has silently picked a cell.

**Maximum shortage (maf)** — *"any modeled reduction to the ability of an entitlement holder to exercise an entitlement":*

| Alternative | Total LB | Arizona | California | Nevada |
|---|---:|---:|---:|---:|
| No Action | 0.60 | 0.47 | 0.00 | 0.03 |
| Basic Coordination | 1.48 | 1.15 | 0.00 | 0.08 |
| Enhanced Coordination | 3.00 | 0.93 | 1.47 | 0.10 |
| Maximum Operational Flexibility | 4.00 | 1.93 | 1.28 | 0.20 |
| Supply Driven (LB Priority) | 2.10 | 1.22 | 0.44 | 0.09 |
| Supply Driven (LB Pro Rata) | 2.10 | 0.92 | 0.76 | 0.07 |
| **🔴 REPRESENTATIVE PREFERRED** | **3.6** | **1.96** | **0.90** | **0.21** |

**Separately, the Preferred Alternative's operational sideboard:** *"Lower Basin Shortage Guidelines: **Up to 3.0 maf** to provide protection of critical infrastructure at Hoover Dam."* ⚠️ **A sideboard is not the modeled maximum — 3.0 and 3.6 are two numbers doing different jobs. My CALENDAR's "up to 3.0 MAF" was right about the sideboard and silent about the 3.6.**

**Distribution rule (2027-28):** shortages **up to 1.5 maf** are distributed by a **Lower-Division-States-developed distribution**; shortages **exceeding 1.5 maf** revert to **priority**. After 2028, priority governs unless agreements are reached. ⚠️ **1.5 maf is a DISTRIBUTION-METHOD BREAKPOINT, not a cut volume.**

#### 🔴 The news layer does not survive the primary — three specific corrections

Widely reported as *"AZ −760k AF, CA −440k AF, NV −50k AF, 16-20% through 2028."* Against the table above:

| Claim | Verdict |
|---|---|
| **Arizona 0.76 maf** | **Appears nowhere in the Arizona row.** It is **California's** value under Supply Driven (LB Pro Rata) — consistent with a **row/column transposition** in the relay chain. |
| **California 0.44 maf** | Real, but belongs to **Supply Driven (LB Priority)** — **not the preferred alternative.** |
| **Nevada 0.05 maf** | **Appears nowhere** in the Nevada row. |
| **"16–20% cuts"** | **No basis.** The only 16%/20% figures in the ES are *"percent of modeled futures that meet the preferred minimum performance"* — an unrelated quantity. |

⇒ **Against the Representative Preferred Alternative the reporting UNDERSTATES by AZ 2.6× · CA 2.0× · NV 4.2× · Total 2.4×.** The headline triple **spans different columns**, so it describes no alternative that exists.

⚠️ **Scope of this check, stated because a zero is ambiguous:** I read the **Executive Summary only** — not Volumes I–III or the technical appendices. **I can say these figures are unsupported by the ES; I cannot say they appear nowhere in the EIS.**

> **Two of my own failures, both worth keeping.** (1) I registered this dated instrument, tracked its date faithfully, and never read its contents (**L-20**). (2) My first automated check reported the news figures as "PRESENT" because it tested value-membership across the whole table rather than membership in the **state's row** — **a table is not a set** (**L-21**).

### ⚠️ STRUCTURAL — an inflow term my model does not contain (added 8/13)

**California irrigation may be partly feeding the Colorado, and SGMA will reduce it.**

- **Lo & Famiglietti 2013 (GRL):** Central Valley irrigation initiates an anthropogenic loop — **summer precipitation +15%**, with a corresponding **Colorado River streamflow increase of ~30%.**
- **SGMA:** critically-overdrafted basins must reach groundwater sustainability by **2040**; **500,000–1,000,000 acres** of San Joaquin Valley farmland projected fallowed/retired/repurposed by then.

**Three caveats, all load-bearing:**
1. **Model, not observation.** Single coarse-resolution GCM with **parameterized convection**; the later literature finds such schemes **may overestimate remote precipitation responses** vs convection-permitting runs. **Read ~30% as a plausible upper bound, not a central estimate.**
2. **🔑 Timeline mismatch, and it is decisive.** SGMA lands in **2040**; the cuts are **2027–28**. **This feedback cannot be driving the current cuts.** Any framing implying it does is wrong on the clock.
3. **Why it still matters:** it is an **independent antecedent — anthropogenic land use, not ENSO** — so it does not double-count against the ENSO root, and it points the **same direction** as the dipole-pivot guard below. **My inflow model has snowpack and ENSO terms and no term for anthropogenic precipitation recycling.**

⇒ **Status: structural, Tier-2, horizon stated (2040).** It graduates past a pure watch-note under my own C6 discriminator because **SGMA has reached an acreage decision**. It is **not** a score-mover. → **KB-061.**

### ⚠️ El Niño does NOT refill the Colorado
The robust El Niño wet signal is the **Southwest / Lower Basin**. **Powell's inflow is UPPER Basin**, near the ENSO precipitation **dipole pivot** where the signal is weak and sign-ambiguous. **The wet anomaly lands downstream of the reservoir that needs it.** *(B2 — a do-not-assume, not a directional call.)*
⇒ **The ROD (~10/1) and the 12/31 expiry are decided at the hydrological bottom; relief arrives spring-2027 at the earliest. The policy clock and the hydrology clock are two quarters out of phase.**

---

## 3. 🔴 RIVER NAVIGATION (C5)

### 🔴 Rhine — SIX-STATION READ, 8/13 17:45 CEST (WSV/PEGELONLINE primary)

**Previously this section was Kaub-only. The full six-station pull shows the low-water event is basin-wide, and that FOUR gauges are below their published all-time lows — not just Kaub.**

| Station | km | **Current** | 7d min–max | 7d trend (8/07→8/12 daily means) | **All-time low (NNW)** | **vs NNW** |
|---|---|---|---|---|---|---|
| MAXAU | 362.3 | 294 | 292–328 | 318.6→298.1 = **−20.5** (−4.09/d) | 231 (1885-01-28) | **+63** |
| WORMS | 443.4 | −15 | −15–13 | 8.0→−10.3 = **−18.4** (−3.67/d) | 2 (2018-10-20) | **−17** |
| MAINZ | 498.3 | 110 | 109–128 | 124.1→110.8 = **−13.4** (−2.67/d) | 110 (1947-11-02) | **±0** *(7d min 109 = 1 cm through)* |
| **KAUB** | **546.2** | **13** | **10–28** | 24.2→11.3 = **−12.8** (−2.57/d) | **25 (2018-10-22)** | **−12** |
| **DUISBURG-RUHRORT** | **780.8** | **134** | **134–153** | 145.4→136.8 = **−8.7** (−1.73/d) | **153 (2018-10-23)** | **−19** |
| EMMERICH | 851.9 | −11 | −11–0 | −5.7→−10.4 = **−4.6** (−0.93/d) | −1 (2022-08-18) | **−10** |

*All values cm. Current = `/W/currentmeasurement.json`. **All six return `stateMnwMhw: "low"`** — the API's own classification.*

> ✅ **BASIS RESOLVED at closeout — CANONICAL IS THE DAILY-MEAN TREND (the table above).** The worker flagged two figures on different bases and recommended picking one before the number travels; picking it is an adjudication, so it waited for me. **Canonical = mean of each calendar day's 96 readings, full days only**, because **that is the same statistic the C5 trigger grades on** — a trend on one basis and a trigger on another is how the two drift apart. The spot figures below are retained as an **as-of snapshot**, not a trend. ⚠️ **Original note, kept because it explains the two numbers:** two trend figures appear in this section and they are **NOT in conflict.** The table above is **daily mean 8/07 → daily mean 8/12** (full days only). The *"Full profile, 7-day change"* line further down is **spot 8/06 → spot 8/13**. Different windows and different statistics, so Maxau reads **−20.5** here and **−32** there. **Both are correct on their own basis; neither is a revision of the other.** Quote the basis whenever either number travels. *(Flagged by the water worker on finding the two side by side — same metric, two surfaces.)*

**Every station is still falling; none has stabilised.** The gradient is **steepest upstream** (Maxau −4.09 cm/d) and **shallowest downstream** (Emmerich −0.93 cm/d) — the drawdown is propagating down-basin, not yet easing at the top.

**Trigger-leg daily means, measured** *(observation only — AEOLUS grades, see the re-specified trigger below)*:

| date | Kaub mean | ≤25? | Duisburg mean | ≤153? | joint |
|---|---:|---|---:|---|---|
| 8/07 | 24.17 | ✅ | 145.43 | ✅ | **BOTH** |
| 8/08 | **25.72** | ❌ | 141.91 | ✅ | no — **run break** |
| 8/09 | 21.12 | ✅ | 143.85 | ✅ | **BOTH** |
| 8/10 | 16.51 | ✅ | 143.73 | ✅ | **BOTH** |
| 8/11 | 14.61 | ✅ | 140.14 | ✅ | **BOTH** |
| 8/12 | 11.32 | ✅ | 136.76 | ✅ | **BOTH** |
| 8/13 | 11.53 | ✅ | 135.65 | ✅ | **BOTH** *(partial, n=72 to 17:45)* |

⚠️ **PRECISION HAZARD on the new trigger.** `SERIES.tsv` stores daily means **rounded to whole cm** (the pre-existing convention). The trigger tests `daily mean ≤ 25 cm`. **A true mean of 25.4 rounds to 25 and would read as satisfying a threshold it does not meet.** No such case occurs in this window — the nearest is **25.72 on 8/08**, which fails on both the rounded and unrounded value — but **the trigger should be graded on unrounded means**, which are recomputable from the API and are given above.

🔑 **The 25 cm benchmark is now PRIMARY-VERIFIED, not carried.** Station metadata returns Kaub `NNW = 25.0 cm, occurred 2018-10-22` and `NW = 25.0` for the 2010-11→2020-10 reference decade. **Kaub 13 cm is 12 cm below it and 64 cm below `GlW` 77 cm** (the reference low-water level fairway depths are guaranteed against).

⚠️ **DATUM CAVEAT, load-bearing on a 12 cm margin.** Each gauge publishes a `gaugeZero` with its own `validFrom` — **Kaub's is 2019-11-01, i.e. AFTER its 2018 record date**; Maxau's is 2017 against an 1885 record. **The API does not state whether historic NNW values were re-referenced to the current datum.** The Kaub 25 cm figure matches the carried/reported 2018 value, so it is at least self-consistent — but **cross-era margins of a few cm should not be treated as exact.** Unresolved; see gaps.

### 📉 WSV publishes an official FORECAST — new instrument, found 8/13

`/stations/<S>/WV/measurements.json` returns `type=forecast`, `initialized 2026-08-13T07:00`, ~4-day horizon. **Available at KAUB, DUISBURG-RUHRORT, EMMERICH; HTTP 404 at MAXAU, WORMS, MAINZ.** ⚠️ **It is NOT listed in the station's `timeseries` array** (which shows only `Q` and `W`) — undiscoverable from metadata alone.

| Station | now | forecast min | **8/17 end** | shape |
|---|---|---|---|---|
| **KAUB** | 13 | **6** (8/14–15) | **11** | falls further, then **partial rebound** |
| **DUISBURG-RUHRORT** | 134 | 129 | **129** | **monotonic decline** |
| **EMMERICH** | −11 | −15 | **−15** | **monotonic decline** |

⇒ **The binding shoal is forecast to trough ~6 cm and recover slightly; the two downstream stations are forecast to keep falling.** A Kaub-only read would call this "stabilising" and miss that Duisburg and Emmerich are not.

### Cost/loading layer — ⚠️ UNVERIFIED, trade-press relay only
| Loadings | ~16% of normal (~800 t vs 5,100 t) |
|---|---|
| Freight | ~€150/t vs ~€20 normal |
| Macro cost | German Q3 GDP −0.1/−0.2% (€1.2–2.3B) — Kiel Institute |

⚠️ **None of these three is re-pullable from a registered primary.** `SOURCES.md` has **no verified freight source**; `rhine_freight_eur_t` remains an instrument with no source. **Do not treat these as measured.**

### 🔴 8/13 — the trigger is re-specified, and BOTH stations are below their all-time records

**The WSV publishes official navigation reference values per station** (`stations/<ST>/W.json?includeCharacteristicValues=true`). **These are the authority's own numbers, not mine:**

| Station | now (8/13) | **NNW** *(record low)* | GlW *(nav. reference)* | MNW *(mean low)* | MW *(mean)* |
|---|---:|---:|---:|---:|---:|
| **Kaub** (km 546) | **13** | **25** *(2018-10-22)* | 77 | 65 | 208 |
| **Duisburg-Ruhrort** (km 781) | **134** | **153** *(2018-10-23)* | 227 | 201 | 394 |

🔴 **Kaub is 12 cm below its all-time record. Duisburg-Ruhrort is 19 cm below its all-time record.** Duisburg is **93 cm below GlW**, the level German navigation planning is built around.
✅ **My "25 cm 2018 record" for Kaub is independently confirmed by the WSV's own `NNW`** — and now dated precisely to **2018-10-22**.

**Full profile, 7-day change (8/13):** Maxau **294** (−32) · Worms **−15** (−26) · Mainz **110** (−13) · **Kaub 13** (−8) · **Duisburg 134** (−19) · Emmerich **−11** (−8). **All six falling; three sitting exactly at their 7-day minimum.** *(Negative readings at Worms/Emmerich are **below gauge datum**, a local reference mark — not "below empty.")*

#### The re-specified C5 → 5 trigger

**Old:** *"sustained below minimum AND Duisburg cutoff."* **It named a station and never defined a level — unfalsifiable as written.** I held C5 at 4 for two sessions "pending the Duisburg leg," and **Duisburg has been below its all-time record since 8/07.** The leg was never unconfirmed; it was **unmeasured because undefined.**

**New:** **Kaub daily mean ≤ 25 cm AND Duisburg-Ruhrort daily mean ≤ 153 cm, on 10 consecutive days.** Both thresholds are the WSV's own `NNW`.

**Base rate, 31 days to 8/13:** joint-below on **7 of 31 days**, runs of **[1, 1, 5]**.
**State: 5 of 10 consecutive days** (run began **2026-08-09**) — **NOT FIRED.** At the current trajectory it would fire ~**8/18**.

⚠️ **Stated plainly because the trigger now measures something different:** the old leg aimed at an **operational** event (loading suspension); the new one measures **hydrological persistence across 235 km of the navigable reach.** I traded an unverifiable economic leg for a verifiable physical one. **A separate operational leg stays UNARMED — there is no resolvable barge-freight or transit-suspension feed** (see `SOURCES.md`).

**Held at 4, not 5** — now for a stated, checkable reason rather than a vague one. Relief needs weeks of rain; risk flagged **into October**. *(Duisburg level + trend now measured above — **AEOLUS grades the trigger, this folder does not.**)*

**The unpriced join (→ DEWEY, delivered 8/13):** EU gas storage is at a five-year low (**59.32%**, ~10–13 pp light), dangerous *conditional on a cold winter*. **The Rhine adds a second conditional — even a normal winter draws harder if the barge leg is impaired, because the substitutes for gas move by water.** ⚠️ Mechanism A2; **magnitude unpulled and not asserted.**

### Other watched rivers
- **Mississippi / Ohio** — ~normal. **Autumn (Sep–Nov) is the window.**
  > ⚠️ **STRUCTURAL headwind added 8/13, not a current read.** DeAngelis et al. 2010 (JGR-Atmos) find 20th-century **July precipitation rose 15–30% downwind of the Ogallala, from eastern Kansas through Indiana**, with timing/month/pattern consistent with post-WWII irrigation history; a 2015 J.Hydromet study reports observational evidence of Great Plains irrigation enhancing Midwest summer precipitation. **That rain falls into the Mississippi basin.** The Ogallala is **fossil water** that cannot meaningfully recharge, so the subsidy is finite. ⇒ **A slow structural headwind on the low-water seasons that produce 2022-style barge disruptions.** ⚠️ **I have NOT quantified the share of Mississippi flow and will not assert one; the decline is DECADAL. Tier-2 note with the horizon stated — NOT a C5 score-mover.** Unlike SGMA, the Ogallala has **not** reached an acreage/pricing decision, so it stays a watch-note under the C6 discriminator. → **KB-062.**
- ✅ **Yangtze · Danube · Paraná — SOURCED AND READ 8/13** (first time; previously neither a read nor a source entry existed).
  - **Yangtze** (Changjiang WRC, 16:00 UTC): **Yichang 44.43 m / 17,800 m³/s** · **Hankou 20.61 / 27,600** · **Datong 10.06 / 31,100** · Three Gorges Reservoir **157.30 m**.
  - **Danube** (OVF Hungary, 18:00 local): **Budapest 24 cm** · Baja −4 · Mohács 10. ⚠️ **Local datum — negatives are normal.**
  - **Paraná** (UNL-FICH): **Rosario 3.02 m** (Δ −0.01) · Santa Fe 3.18 · Corrientes 3.28. 🔑 **Rosario is the grain-export gauge** — the Up-River cluster handles most Argentine grain/soy-product exports → **CARL / MARCO**.
  > ✅ **BOTH SUB-GAPS CLOSED 8/13 — and the references reversed both reads.**
  >
  > 🔴 **DANUBE — 13 CONSECUTIVE stations are BELOW their all-time records.** Hungary's OVF publishes per-station **`LKV`** (lowest-ever level) with its date, via a queryable ArcGIS service covering **44 stations from Ingolstadt (km 2457) to Novo Selo (km 834)** — plus **`LKV_viszony`, the authority's own below/above flag.** Unbroken from **Vác (km 1679.5) → Mohács (km 1446.9) = 233 km**: Mohács **−40 cm**, Baja −31, Paks −23, Dunaföldvár −15, Budapest −9. Pfelling (Bavaria) −27. **Every one of those records was set 2018-10-24/26.**
  > 🔴 **INDEPENDENCE — do NOT stack this on the Rhine.** The Rhine's Kaub/Duisburg records were set **2018-10-22/23**; the Danube's **2018-10-24/26**. **Same drought, same week.** Rhine-below-record and Danube-below-record are **ONE European event observed in two basins, not two witnesses.** C5-Rhine is already separated from the ENSO root — correct — but **Rhine and Danube share a root with each other and must be counted once.**
  > ⚠️ **Filter LKV dates:** 5 of 44 stations carry `1799-12-31` / `1884-12-31` / `1894-12-31` — **null-date sentinels, not records.**
  >
  > 🔴 **PARANÁ — I called it "mid-range" this morning; the distribution says 99th percentile.** 366 daily Rosario records (13/08/2025→13/08/2026): min **1.08** · P10 **1.40** · median **2.14** · max **3.03**. **Current 3.02 m is one centimetre off the trailing-year maximum** — near the *top* of its range, not the middle. **Working low-water reference: P10 ≈ 1.40 m.**
  > ⚠️ **One year is a short base, and this one is benign.** The 2021 crisis went far lower (Rosario ~0.08 m in May 2020; 2021 lowest since 1944; discharge ~6,200 m³/s vs ~17,000 normal). **A trailing-year percentile is a rank within a benign year, not a historic reference.**
  > **Commercially: a high Paraná is GOOD for grain logistics** — no draft-restriction pressure at the Up-River cluster. **→ CARL / MARCO.**
- **Panama** — ✅ **INSTRUMENT GAP CLOSED 8/13.** The instrument is the **ACP Monthly Canal Operations Summary**, published as a *numbered Advisory to Shipping*, which carries **oceangoing transits, daily average** — exactly the quantity the threshold bands use. **Verified: `A-14-2026` (April 2026 data, dated 2026-05-08) → 38.70 transits/day**, high 42, low 31, total 1,161. **Above the ~36 baseline — which this anchors for the first time.** ⚠️ **Read TRANSITS (38.70), not the adjacent ARRIVALS (40.5).**
  > 🔴 **CORRECTION — and the caveat discipline here was the worker's, not mine.** The earlier read was *"the Advisories index's newest entry is A-46-2024 ⇒ no 2026 restriction advisory is published at the issuing authority,"* **correctly hedged in this file as "'not published on these two pages' is narrower than 'does not exist.'"** **That hedge was right and I dropped it when I relayed the finding onward** — I reported it as a closed gap. **`A-14-2026` exists.** The advisories **index is JS-rendered and silently stale**: `curl` and `WebFetch` both return a fragment ending at 2024, and **two fetch tools agreeing is not corroboration when they share a blind spot.** The *no-2026-RESTRICTION* half may still hold; the *ACP-has-published-nothing-since-2024* premise does not. → **KB-067, L-24, L-25.**
  > **Retrieval:** discover the PDF by search (`"Monthly Canal Operations Summary" pancanal <month> 2026`), then fetch. **Never scrape the index. Filenames are not predictable** — a 5-month × 23-number brute force found only the one already known.

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
5. ✅ **Panama — instrument CLOSED 8/13** (ACP Monthly Canal Operations Summary; 38.70 transits/day, April 2026). Remaining: **retrieve the current month's summary** — filenames are unpredictable, so discover by search, never by the stale index.
6. **Yangtze / Danube / Paraná** — ⚠️ **no live read AND no entry in `SOURCES.md`.** These cannot be pulled without registering a primary first — **the blocker is a missing source registration, not a missed pull.** Gaps under the standing directive.
6b. **Mississippi has a working primary but no registered instrument.** USGS `07289000` Vicksburg discharge returns cleanly — **349,000 cfs on 8/12** — but **gauge height (`00065`) returns an empty `timeSeries`** at the daily-values service, and no Mississippi name exists in the observation vocabulary. **Needs an instrument name before it can be logged.**
7. **Upper-Basin snowpack for winter 2026-27** — the leg that tests the dipole-pivot guard. CPC DJF outlook (~8/20) is the first read; Apr-1 resolves it.
