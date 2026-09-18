# AEOLUS · REGIME — live dossier

**As-of: 2026-09-18**, all figures CPC primary. Consolidated from KB-AEO-016/021/038/045/046/053/054/111 + VX-19/20.

> **Last real data refresh: 2026-09-17**  ·  **Dossier written: 2026-09-18**
>
> **2026-09-18 — worker pass. Four baselines all refreshed; three of the folder's standing open items moved.**
> 1. 🔴 **Historic-event odds RAISED 69% → 75%** in the 10Sep2026 Diagnostic Discussion. Very-strong restated UNCHANGED at ">90%". **This also converts the ">90% very strong" figure from PROME's INFERRED relay into AEOLUS's own VERIFIED primary read.**
> 2. 🔴 **CPC switched RONI (and ONI) from ERSSTv5 to ERSSTv6 on 2026-08-10** — CPC's own dated footnote, confirmed independently against the v5/v6 tables. **`SOURCES.md` still documents both files as ERSSTv5 and is stale.** §2's decadal and peak-event tables were re-derived on the new basis and **reproduce exactly** — they survive the change.
> 3. ✅ **The CPC DJF 2026-27 outlook is FETCHED.** The PUBLIC-AND-UNFETCHED item, open since 8/12, is **closed** — §6.
> 4. ✅ **RONI's 9/11 404 did not reproduce.** The `SOURCES.md` address returned HTTP 200 and a complete series. **No re-location was needed and no source was substituted.**
>
> ⚠️ **CONTRADICTION WITH THE PRIOR PASS, flagged not overwritten.** The 8/27 entry recorded *"05AUG +2.6 → 12AUG +2.7 → **19AUG +2.6** — first WoW pullback this season."* **On today's vintage those weeks read 2.5 / 2.6 / 2.6 — a flat top, not a pullback.** CPC revised three previously-recorded weeks (29JUL 2.3→2.4, 05AUG 2.6→2.5, 12AUG 2.7→2.6). **Treated as a revision, not an error at either date** (AGENT.md rule). **The pullback described in the prior pass is not present in the live series.**
>
> 🔴 **8/21's weekly-basis trap — the STALE-SLIDE hypothesis is REFUTED; verdict still UNRESOLVED.** The 14Sep2026 deck's bullet slide **did** regenerate (0.0/1.8/2.5/3.2 → **−0.1/2.0/2.8/3.7**), so it is not a frozen artifact. The near-uniform gap vs `wksst9120.for` persists (09SEP: 0.9/2.9/3.7/4.5 ⇒ −1.0/−0.9/−0.9/−0.8). **New discriminator:** the same gap appears between two *monthly* products for the same month — the 9/10 discussion's August ERSST quad (0.1/1.8/2.5/3.4) vs `sstoi` August OISST quad (0.93/2.52/3.13/4.08), deltas −0.83/−0.72/−0.63/−0.68. **The gap tracks ERSST-vs-OISST, not staleness — but CPC's own footnote says those weekly slides use OISSTv2.1, the same product as `wksst9120.for`.** So the mechanism is now a *documented CPC self-contradiction* rather than a suspected stale slide. **Ruling unchanged: `wksst9120.for` is the sole authoritative weekly figure (KB-088); never cite the deck bullet numbers for anything scored.**
>
> **Prior pass (2026-08-27).** Weekly deck discovered and registered as SOURCES.md ⑥; mismatch investigation opened. **Prior pass (2026-08-21, AEOLUS directly).** First RONI pull; DJF read as a GIS product rather than an image.
> ⚠️ **Known-bad: `wksst8110.for`** — reconstructed from memory once, got a dead file ending 27JAN2021. `SOURCES.md` had the right one (`wksst9120.for`) all along.
> *Two-clock header (PAT-044) — `scripts/ledger_staleness.py` reads the first line. **The data date, not the edit date**: a hygiene edit must NOT bump it.*
> **Observations → `regime/workbook/SERIES.tsv`** · findings → central `workbook/KB.tsv` · synthesis → `STATUS.md`. **Flow is one-way.**
> **Feeds:** C1 · C2 · C3 · C5 · C6 (root: owns the ENSO indices)

---

## 1. STATE — four instruments, all correct, none interchangeable

**All four refreshed 2026-09-18. Every one moved up.**

| Instrument | Value | As-of | Basis | Reads |
|---|---|---|---|---|
| **ONI** (official level) | **+1.80** | **JJA 2026** | ERSSTv6, 30-yr centred | **+0.41 in one season** (MJJ +1.39). **The ≥1.5 "strong" line is now CROSSED at JJA** — margin **+0.30 above** it |
| **RONI** (dynamical) | **+1.36** | **JJA 2026** | ERSSTv6, 1991-2020 | **+0.39** on MJJ (+0.97, itself revised from +0.98). **1.14 below** the +2.5 OND "historic" bar |
| **OISST monthly** (trend) | **+2.52** | **Aug 2026** | OISST, 1991-2020 fixed | Apr +0.47 → May +0.94 → Jun +1.55 → Jul +2.03 → **Aug +2.52** |
| **Weekly** (fast trend) | **+2.9** | **week ctr 09SEP 2026** | OISSTv2.1, 1991-2020 | 19AUG +2.6 → 26AUG +2.6 → 02SEP +2.7 → **09SEP +2.9 — season high** |
| Niño-1+2 | **+4.08** monthly (Aug) / **+4.5** weekly (09SEP) | Aug / 09SEP 2026 | | *the number that gets misquoted as "3.4"* |
| Niño-4 | **+0.93** monthly (Aug) / **+0.9** weekly (09SEP) | Aug / 09SEP 2026 | | **the only region NOT rising** — CPC notes it *decreased* to +0.1 °C in August on the ERSST basis |

⚠️ **Four simultaneously-true numbers for "the ENSO state" today: +1.80 (ONI) · +1.36 (RONI) · +2.52 (OISST monthly) · +2.9 (weekly).** Name the instrument beside the number, every time.

**CPC forward odds (10 Sep 2026 Discussion, verbatim):**
- *"El Niño is strengthening, with a **greater than 90% chance of a very strong event** during the Northern Hemisphere fall and winter 2026-27."* — **restated unchanged** from 8/13. **Now a VERIFIED primary read, no longer an INFERRED relay.**
- *"During the October–December 2026 season, there is a **75% chance of a historic event that would exceed the strength of previous El Niño events dating back to 1950** (+2.5 °C or more for a 3-month RONI value)."* — 🔴 **RAISED from 69%.**
- Alert status: **El Niño Advisory** (unchanged). **Next discussion: 8 October 2026.**

### 1b. THE FORWARD CURVE — CPC's own RONI forecast (both tables "Issued September 2026", both verified on RONI, 1991-2020 base)

| Season | P(RONI ≥ 2.0) "very strong" | RONI 25th | **RONI median** | RONI 75th |
|---|---|---|---|---|
| ASO 2026 | 77% | 1.96 | 2.07 | 2.18 |
| SON 2026 | 97% | 2.26 | 2.43 | 2.60 |
| **OND 2026** | **98%** | **2.44** | **2.67** | **2.90** |
| NDJ 2026-27 | 93% | 2.28 | 2.57 | 2.85 |
| DJF 2026-27 | 75% | 1.94 | 2.27 | 2.59 |
| JFM 2027 | 39% | 1.50 | 1.82 | 2.14 |
| FMA 2027 | 5% | 0.97 | 1.26 | 1.54 |
| MAM 2027 | 0% | 0.54 | 0.79 | 1.05 |
| AMJ 2027 | 0% | 0.12 | 0.38 | 0.65 |

⇒ **Forecast peak timing = OND 2026** (median 2.67, the series maximum; 98% ≥ 2.0). CPC prose: *"El Niño will continue to strengthen through the end of the year."*
⇒ **The OND 25th percentile (2.44) sits just below the +2.5 historic bar** — arithmetically consistent with the 75% headline. **Decay is forecast to be fast:** ≥2.0 odds fall 93% → 75% → 39% → 5% across NDJ→FMA.

---

## 2. 🔑 THE ONI↔RONI RECONCILIATION — RE-DERIVED 2026-09-18 on the new ERSSTv6 basis

🔴 **BASIS CHANGE, 2026-08-10.** CPC's own footnote, verbatim: *"NCEI is discontinuing ERSSTv5, so RONI values have switched to ERSSTv6. The weekly OISSTv2.1 data remains unaffected."* Confirmed independently: `RONI.ascii.txt` and `oni.ascii.txt` both match the **v6** product tables, not v5. A v5 archive remains at `/products/analysis_monitoring/enso/roni/v5/`.
✅ **The tables below were re-derived from the v6 files and reproduce the 8/13 figures EXACTLY to 2 dp. This section survives the basis change intact.**

**The offset is NOT a constant. It has grown monotonically, every decade:**

| Decade | mean ONI − RONI | n seasons |
|---|---|---|
| 1950s | −0.17 | 120 |
| 1960s | −0.09 | 120 |
| 1970s | −0.17 | 120 |
| 1980s | −0.00 | 120 |
| 1990s | −0.11 | 120 |
| 2010s | **+0.22** | 120 |
| **2020s** | **+0.44** | 79 |

**That drift *is* the tropical-mean warming, showing up inside the instrument.**

**⚠️ NEW THIS PASS — the offset is NARROWING *within* this event as it grows:**
`FMA +0.55 → MAM +0.50 → AMJ +0.46 → MJJ +0.42 → **JJA +0.44**`
**This is the third demonstration that a fixed conversion is invalid** — it is not constant across decades, not constant across events, and **not constant within a single event.**

### What CPC's "+2.5 RONI" implies — and the honest caveat

At the current **+0.44** offset (JJA 2026), **+2.5 RONI ≈ +2.94 ONI.** For scale (re-derived on v6, unchanged):

| Event | ONI peak | RONI peak | offset |
|---|---|---|---|
| 1997-98 | **+2.37** (NDJ) | +2.28 | +0.09 |
| 2015-16 | **+2.59** (NDJ) | +2.25 | +0.34 |
| 2023-24 | +1.99 (NDJ) | +1.40 | +0.59 |

⇒ **In RONI space** (CPC's framing, and the fair cross-era comparison) **+2.5 exceeds 1997 and 2015 by ~0.25.**
⇒ **In raw ONI space** it would imply roughly **+2.94**, ~0.35 above the 2015-16 record.

⚠️ **Both statements are true and they answer different questions.** RONI asks *"is this event dynamically stronger than past ones?"*; ONI asks *"how warm is the water?"* **Do not present one as a correction of the other, and do not carry a single-number conversion forward.**

### 🔑 The under-appreciated read — RESTATED AT THE NEW LEVELS

**ONI +1.80 is "strong" (line crossed at JJA). RONI +1.36 is still only "moderate-to-strong" on the dynamical scale — and it has NOT yet reached the level 2023-24 peaked at (+1.40).** The gap is the warming background, not the event.

**This matters because teleconnections respond to the atmospheric circulation — driven by SST *gradients* and convection — rather than to absolute SST**, which is precisely why CPC frames its headline in RONI.

⇒ **Keying composite expectations to ONI risks over-calling the teleconnection.** ⚠️ **Stated as a caution, not a correction**: the channel signs have **still not** been re-derived against RONI. **Registered as an open question below.**
⚠️ Note this cuts **against** alarm: it argues the atmospheric response may be *milder* than "historic El Niño" headlines imply — the opposite of the direction a dramatic number pulls you.

---

## 3. PER-CHANNEL SIGN TABLE — what the regime sets

| Channel | Sign | Confidence | Basis |
|---|---|---|---|
| **C1** hurricane | **SUPPRESS** ↓ | **HIGH** — mechanism now visible in storm-level forecasts (NHC names *"strong upper-level winds and dry air"* on AL92) | shear |
| **C2** crops | ambiguous | **LOW** — currently **refusing to confirm** (corn 61 / soy 62 G/E, 6 pts above my band) | drought geography is southern Plains, not the corn belt |
| **C3** winter demand | **MEAN down** ↓ · **PEAK: no sign** | mean HIGH · **peak REFUSED** | n=2 very-strong analogues, **split 1-1** |
| **C4** fire | southern-Plains fire risk should **abate** by late autumn | MED | the wet-south signal — **AEO-09 tests it** |
| **C5** Panama | drought risk ↑ | MED | El Niño → Panama hydrology |
| **C5** Rhine | **NO SIGN — separate basin** | — | ⚠️ **European basin. Never weld to the ENSO root.** |
| **C6** Colorado | **NOT relief** | MED | see §4 |

**Independence accounting:** C1 + C2 + C3 + C5-Panama + C6 share **ONE** root. **Count it once.** C5-Rhine is independent.

---

## 4. ⚠️ TWO GUARDS AGAINST INTUITIVE-BUT-WRONG READS

**① A record El Niño does NOT refill the Colorado.** The reliable wet signal is the **Southwest / Lower Basin**; **Powell's inflow is UPPER Basin**, near the ENSO precipitation **dipole pivot** where the signal is weak and sign-ambiguous. **The wet anomaly lands downstream of the reservoir that needs it.** Full treatment → `../water/DOSSIER.md`.

> ✅ **TESTED AGAINST THE LIVE 9/17 OUTLOOK, NOT REPEATED — AND IT HOLDS.** DJF 2026-27 precipitation probabilities, read at the CPC primary as GIS polygons (`lead3_DJF_prcp`, Fcst_Date 20260917):
> | Upper Basin point | DJF precip category |
> |---|---|
> | Grand Lake CO (Colorado hdwtrs) · Steamboat Spgs/Yampa · Aspen · Pinedale WY (Green R hdwtrs) · Vernal/Uinta · Flaming Gorge · Grand Junction · Moab · **Page AZ / Lake Powell** · Salt Lake City | **Equal Chances (33%) — NO tilt, either direction** |
> | Gunnison CO · Durango CO (San Juan) — the southernmost sub-basins only | Above 33% (weak) |
> | *contrast:* coastal CA, Tucson | **Above 50%** |
> | *contrast:* Phoenix | Above 40% |
> | *contrast:* **Great Falls MT / Missoula MT (N Rockies)** | **BELOW 40% / Below 33% — dry tilt** |
> ⇒ **The wet signal is south and coastal; the Northern Rockies are dry; and Powell's inflow zone sits between them in Equal Chances at 10 of 12 headwaters points tested.** Exactly the geometry this guard describes.
> ⚠️ **AND IT MOVED THE WRONG WAY FOR RELIEF:** the single change from the 8/20 issuance is **Aspen CO dropping OFF its weak Above-normal tilt into Equal Chances** — the wet tilt retreated *southward, away from* the Upper Basin, while historic-event odds rose 69→75%. **Evidence strengthened, not weakened.**

**② The northern tier goes MILDER, not colder — I got this backwards once and shipped it.** On 8/3 I told MARCO a very-strong El Niño gives an "active/cold Northern-tier winter." **CPC says the inverse:** storm track shifts **SOUTH**, the North goes **milder and less stormy**. I reasoned validly from an unchecked premise, produced a confident coherent wrong finding, and **MARCO logged it as a valued counterweight to its own thesis** — the worst place for a wrong finding to sit. Found by accident 9 days later, pulling the same primary for an unrelated question (**L-13**).

> **The rule that came out of it: when a packet's CONCLUSION turns on a directional climate premise, pull the primary for THAT premise in the same session. It is one fetch. And a well-argued packet deserves MORE premise-scrutiny than a hedged one, because its polish suppresses the reader's own checking.**

---

## 5. THE RELIABILITY PROBLEM — now governing (L-14 → L-17)

Composites are built mostly from **weak and moderate** events. I hit the degradation **three times in one afternoon** on 8/12, at an amplitude *below* the current forecast:

1. **PJM winter peak** — n=2 very-strong analogues, split 1-1; **both of PJM's highest winter peaks came in *non*-strong-El-Niño winters.**
2. **PNW snowpack** — UW: WA snowpack "fared pretty well" in all three very-strong events (1984/1998/2016), against the composite's dry signal.
3. **Polar vortex** — NOAA's own caveat that **1997-98 produced no major SSW.**

⇒ **With CPC now at 75% (raised from 69% on 9/10) for an out-of-sample event, the analogue set trends to n=0 and every composite becomes an extrapolation.** **The composite still gives the mean sign; it does not give the tail, and at extreme amplitude it may not give the mean either.**

**The only non-extrapolated substitute is a season-specific forecast** → **CPC DJF 2026-27 outlook.** ✅ **FETCHED 2026-09-18 — see §6.** The PUBLIC-AND-UNFETCHED status is closed.

⚠️ **But it does not retire L-14, and the prior pass already established why:** CPC states it *"strongly utilized"* ENSO composites in building this outlook **because of the magnitude of the event** (logged 8/21). **A season-specific outlook is not composite-independent — L-14 constrains this product rather than being retired by it.**

---

## 6. ✅ THE CPC DJF 2026-27 OUTLOOK — FETCHED 2026-09-18 (the standing open item, closed)

**Product:** CPC seasonal outlook, retrieved at the primary as **GIS shapefiles** (`seastemp_202609.zip` / `seasprcp_202609.zip`, layers `lead3_DJF_temp` / `lead3_DJF_prcp`) — **not** an image and **not** a search summary.
**`Fcst_Date` = 20260917 · `Valid_Seas` = "DJF 2026-2027"** — the issuance of Thursday 17 Sep 2026.

### TEMPERATURE — the PJM footprint

| Location | DJF above-normal probability |
|---|---|
| **Cleveland OH** | **50%** |
| Washington DC · Baltimore · Philadelphia · Newark NJ · Pittsburgh · Columbus OH · Dayton OH · Indianapolis · Chicago (ComEd) · Charleston WV · Louisville | **40%** |
| Richmond VA · Roanoke VA (southern edge) | 33% |

**Florida:** *near-normal* remains the **favored** temperature category (33%) at Miami / Orlando / Tampa.
**Northern tier:** Seattle, Boise, Missoula, Great Falls all **40% above-normal** — consistent with guard ② (the North goes **milder**, not colder).
**Southwest:** Los Angeles, San Diego, Phoenix, Tucson, Denver all **Equal Chances** on temperature.

### ⚠️ THE MOST IMPORTANT THING ABOUT THIS OUTLOOK IS THAT IT DID NOT MOVE

Polygon-to-polygon against the 8/20 issuance (`lead4_DJF` in `seastemp_202608`): **identical at all 8 PJM points tested**, and identical at 9 of 10 precipitation points. **CPC raised historic-event odds 69% → 75% over the same month and did not strengthen the DJF CONUS signal at all.**
⇒ **A rising ENSO amplitude is not translating into a stronger forecast CONUS anomaly.** That is itself the reliability problem of §5 showing up in CPC's own product, and it is the single most decision-relevant thing in this pass for anyone keying a winter view to "historic El Niño."

---

## OPEN QUESTIONS

1. ✅ **CLOSED — CPC DJF 2026-27 outlook.** Fetched 2026-09-18 (§6). **Still owed to WATT and MARCO**, whose 8/12 packets were built on composites this product supersedes — **and the headline for them is that the outlook did NOT strengthen** while the event did.
2. **Should channel signs be re-derived against RONI rather than ONI?** (§2). Real work, not a one-line fix, **still not done.** The two reads at the current season, side by side, never averaged:
   - **ONI-based read (JJA 2026): +1.80** — the ≥1.5 "strong" line is **crossed**, margin +0.30. On this basis the event reads *strong, and approaching historic.*
   - **RONI-based read (JJA 2026): +1.36** — **has not yet reached the level 2023-24 peaked at (+1.40)**, and sits **1.14 below** the +2.5 OND bar CPC quotes odds against. Trajectory FMA −0.44 → MAM −0.04 → AMJ +0.49 → MJJ +0.97 → **JJA +1.36**.
   - ⚠️ **The two instruments have never disagreed more about what kind of event this is.** **Would likely *soften* several composite-derived reads if RONI became the keying instrument.** Worth doing **before winter**, and worth telling WATT/MARCO if it changes anything.
   - **CPC's own forecast bridges the gap:** its RONI outlook takes +1.36 (JJA) → **2.07 (ASO) → 2.43 (SON) → 2.67 (OND)**. The +2.5 bar is reached **only at OND, and only at roughly the 30th percentile upward** (§1b).
3. **Track the ONI−RONI offset as OND approaches.** Current **+0.44** (JJA); at that value +2.5 RONI implies ~**+2.94** ONI. ⚠️ **NEW: the offset is narrowing within this event** (+0.55 → +0.44 since FMA). **Re-compute every pass, never carry the conversion forward.**
4. 🔴 **NEW — the ERSSTv5 → v6 basis change (2026-08-10) needs an AEOLUS ruling.** `SOURCES.md` documents ONI and RONI as ERSSTv5; **both files are now v6.** §2's tables reproduce exactly, so nothing derived here breaks — **but `AEO-02 resolves on ONI`, and the instrument it resolves on changed basis mid-prediction.** Worker reports; **AEOLUS grades.** Also: `SOURCES.md` ①/② need their basis line corrected.
5. 🔴 **NEW — the weekly-basis mismatch is now a documented CPC self-contradiction, not a stale slide.** The stale-slide hypothesis is refuted (the slide regenerated). The ~−0.8/−0.9 uniform gap tracks ERSST-vs-OISST, yet CPC's footnote says the weekly slides use OISSTv2.1. **Ruling stands: `wksst9120.for` only.** The open question for AEOLUS is whether to stop re-investigating and simply register the gap as a known product discrepancy.
6. **AEO-02** (ONI ≥1.5 in an **NDJ** season) resolves on **ONI**, now **+1.80 at JJA**. ⚠️ **The threshold is met at the current season but AEO-02 is specified on NDJ — the season has not arrived. Worker does not resolve predictions; the measurement and the margin are above.**
7. **AEO-07 / AEO-08 (PJM DJF).** Measurement supplied, not graded: **PJM is 40% above-normal** across the footprint (50% at Cleveland, 33% on the southern VA edge) — **unchanged from the 8/20 read.**
8. **AEO-09** (`../wildfire/`) remains the cheapest live test of composite reliability: does the wet-south signal verify **where it is strongest**? If not, L-14 governs and the C1 suppression leg — same composite machinery — downgrades with it.
9. **NEW — no registered source for MJO / PDO / IOD / SOI.** `SOURCES.md` carries no numeric pull for any of them and the weekly deck carries no extractable figure. Only qualitative CPC text exists (*"the traditional and equatorial Southern Oscillation indices remained negative"*, 9/10). **The IOD has no CPC product at all** — its operational index is Australian BoM, outside the "CPC primaries only" rule. **Nothing was substituted.** AEOLUS's call whether to register them.
