run_date: 2026-09-18

observations_added: 25 rows to `workbook/SERIES.tsv`, 12 rows to `workbook/LOG.tsv`. `DOSSIER.md` updated (two-clock header, §1 state, §1b NEW forward curve, §2 re-derived on ERSSTv6, §4 guard ① tested, §5, §6 NEW, OPEN QUESTIONS rewritten).

---

## 🔑 THE FOUR-BASELINE TABLE — all four refreshed, none interchangeable

| Baseline | Value | Period | As-of / pulled | Source | Δ vs prior |
|---|---|---|---|---|---|
| **ONI** | **+1.80** | **JJA 2026** | pulled 2026-09-18 | `CPC-oni.ascii` (ERSSTv6) | **no new season since 9/11** — JJA was already recorded. vs MJJ +1.39 = **+0.41/season**. Next season (JAS) posts with the 8 Oct discussion |
| **RONI** | **+1.36** | **JJA 2026** | pulled 2026-09-18 | `CPC-RONI.ascii` (ERSSTv6) | 🔴 **NEW SEASON — the baseline that had no working address is refreshed.** Prior last value MJJ **+0.98** (8/21), which now reads **+0.97** (revision). MJJ→JJA = **+0.39** |
| **OISST monthly** | **+2.52** | **Aug 2026** | pulled 2026-09-18 | `CPC-sstoi.indices` col 4 | **NEW MONTH.** Jul +2.03 → Aug +2.52 = **+0.49** |
| **weekly** | **+2.9** | **week centred 09SEP2026** | pulled 2026-09-18 | `CPC-wksst9120.for` col 3 | prior 19AUG **+2.6** → **+0.3**. **Season high.** |

**No baseline failed to refresh. All four are simultaneously true: +1.80 · +1.36 · +2.52 · +2.9.**

**Weekly trajectory (current vintage, so the turn is visible):**
`22JUL +2.2 → 29JUL +2.4 → 05AUG +2.5 → 12AUG +2.6 → 19AUG +2.6 → 26AUG +2.6 → 02SEP +2.7 → **09SEP +2.9**`
Companion regions 09SEP: Niño-1+2 **+4.5** · Niño-3 **+3.7** · Niño-4 **+0.9** (the only region not rising).

---

## 🔴 THE RONI RE-LOCATION RESULT — **NO RE-LOCATION WAS NEEDED**

**The 404 recorded on 2026-09-11 DID NOT REPRODUCE.** The `SOURCES.md` command, run verbatim and unmodified:

```bash
curl -s "https://www.cpc.ncep.noaa.gov/data/indices/RONI.ascii.txt" | tail -6
```
→ **HTTP 200**, 14,720 bytes, 920 data rows, series complete through **JJA 2026**. Verified a second time with an independent `curl -sI`: `HTTP/1.1 200 OK · Date: Fri, 18 Sep 2026 17:53:08 GMT`.

**The recorded address is correct and is still the canonical CPC location. No URL was reconstructed and no source was substituted.** The 9/11 failure was transient or client-side.

**Worth adding to `SOURCES.md` anyway** (navigation path, so a future 404 never becomes a search): the official CPC RONI product **home**, linked directly from `ensodisc.shtml`, is `https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/`. It carries the full HTML table, the v5 archive, and the revision notice.

---

## INSTRUMENT TABLE — value | unit | as-of | source | Δ

| Instrument | Value | Unit | As-of | Source | Δ vs prior |
|---|---|---|---|---|---|
| `historic_prob_ond` | **75** | pct | 10 Sep 2026 | `CPC-ensodisc` | 🔴 **69 → 75 (+6)** |
| `verystrong_prob_ond` | **90** (">90%") | pct | 10 Sep 2026 | `CPC-ensodisc` | unchanged — **but now VERIFIED, was INFERRED relay** |
| `oni` | +1.80 | degC | JJA 2026 | `CPC-oni.ascii` | +0.41 vs MJJ |
| `roni` | +1.36 | degC | JJA 2026 | `CPC-RONI.ascii` | +0.39 vs MJJ (+0.97, rev. from +0.98) |
| `nino34_monthly` | +2.52 | degC | Aug 2026 | `CPC-sstoi.indices` | +0.49 vs Jul |
| `nino12_monthly` | +4.08 | degC | Aug 2026 | `CPC-sstoi.indices` | +0.52 vs Jul +3.56 |
| `nino34_weekly` | +2.9 | degC | 09SEP2026 | `CPC-wksst9120.for` | +0.3 vs 19AUG |
| `oni_minus_roni` | **+0.44** | degC | JJA 2026 | `derived-CPC` | +0.42 at MJJ — **narrowing within the event** |
| `djf_temp_northeast_corridor` (PJM) | **40** | pct above-normal | Fcst 20260917 | `CPC-GIS-lead3DJF` | **UNCHANGED vs 8/20** |
| `djf_temp_abovenormal_max` (PJM) | 50 (Cleveland) | pct | Fcst 20260917 | `CPC-GIS-lead3DJF` | unchanged |
| `djf_temp_florida_category` | 33 (near-normal favoured) | pct | Fcst 20260917 | `CPC-GIS-lead3DJF` | unchanged |

---

## threshold_state (state only — **no grading, no prediction resolved**)

- **ONI vs the ≥1.5 "strong" line** — **+1.80 (JJA 2026)**. The line is **crossed**; margin **+0.30 above**. ⚠️ **AEO-02 is specified on an NDJ season, and NDJ has not arrived.** Measurement and margin supplied; **AEOLUS resolves.**
- **RONI vs the +2.5 OND "historic" bar** — **+1.36 (JJA 2026)**, **1.14 below**. NOT-FIRED. CPC's own RONI outlook median reaches 2.5 only at **OND (2.67)**.
- **RONI vs 2023-24's peak (+1.40)** — **+1.36, i.e. 0.04 BELOW it.** On the dynamical instrument this event has **not yet matched the last one.**
- **Very-strong probability** — **>90%**, NH fall/winter 2026-27. Restated verbatim, unchanged.
- **Historic-event probability (≥ +2.5 RONI, OND)** — **75%**, raised from 69%.
- **P(RONI ≥ 2.0) by season** — ASO 77 · **SON 97 · OND 98** · NDJ 93 · DJF 75 · JFM 39 · FMA 5 · MAM 0 · AMJ 0.
- **Forecaster's stated peak timing** — **OND 2026** (RONI outlook median **2.67**, the series maximum; 98% ≥ 2.0). CPC prose: *"El Niño will continue to strengthen through the end of the year."*

### CPC ENSO STRENGTH PROBABILITIES + RONI OUTLOOK — both "Issued September 2026", both verified on RONI (1991-2020 base)

| Season | P(≥2.0 °C) | RONI 25th | **median** | 75th |
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

---

## changes

**1. 🔴 The September discussion raised the historic-event odds, and nothing else moved.** Verbatim (10 Sep 2026): *"During the October–December 2026 season, there is a **75% chance of a historic event that would exceed the strength of previous El Niño events dating back to 1950** (+2.5 °C or more for a 3-month RONI value)."* Very-strong odds restated **unchanged** at *">90% ... during the Northern Hemisphere fall and winter 2026-27."* Alert status **El Niño Advisory**. **Next discussion 8 October 2026.**
**Provenance effect:** AEOLUS's STATUS carried ">90% very strong" as **PROME's relay, tagged INFERRED**. This pull is the primary. **It is now VERIFIED, and it is correct as relayed.**

**2. 🔴 CPC changed the basis of ONI and RONI on 2026-08-10 — `SOURCES.md` is stale.** CPC's own dated footnote, verbatim from the 14Sep2026 deck: *"8/10/26: NCEI is discontinuing ERSSTv5, so RONI values have switched to ERSSTv6. The weekly OISSTv2.1 data remains unaffected."* **Confirmed independently, not taken on the footnote's word:** `RONI.ascii.txt` matches the v6 HTML table and **not** v5 at three discriminating seasons (JFM 2025 −0.8 v6 / −0.9 v5; JJA 2025 −0.4 / −0.5; OND 2025 −1.0 / −0.9), and `oni.ascii.txt` matches the ONI v6 page exactly across all twelve 2025 seasons. **`SOURCES.md` ① and ② both still say ERSSTv5.**

**3. ✅ §2's reconciliation survives the basis change.** I re-derived the decadal offsets from today's v6 files: **1950s −0.17 · 1970s −0.17 · 1990s −0.11 · 2000s +0.01 · 2010s +0.22 · 2020s +0.44** — **exact to 2 dp against the 8/13 table**, n=120/decade. The peak-event table also reproduces exactly (1997-98 +0.09 · 2015-16 +0.34 · 2023-24 +0.59). **Nothing derived from §2 breaks.**

**4. ⚠️ NEW: the ONI−RONI offset is narrowing *within* this event.** `FMA +0.55 → MAM +0.50 → AMJ +0.46 → MJJ +0.42 → JJA +0.44`. **Third independent demonstration that a fixed conversion is invalid** — not constant across decades, not across events, **not within one event.** At +0.44, +2.5 RONI ⇒ ~**+2.94** ONI.

**5. ✅ The DJF 2026-27 outlook is FETCHED** — see `proposed_findings` #1. `Fcst_Date 20260917`.

**6. ⚠️ The weekly series was revised, and it erases an event the prior pass recorded.** See `contradictions` below.

**7. 🔴 The weekly-basis "stale slide" hypothesis is REFUTED.** See `contradictions` below.

---

## proposed_findings — **PROPOSALS ONLY. AEOLUS adjudicates. Nothing here was scored, fired, resolved or routed.**

**① 🔴 DJF 2026-27 outlook: the PJM read is 40% above-normal — and the outlook DID NOT MOVE while the event strengthened.**
Retrieved at the primary as GIS polygons (`seastemp_202609.zip` / `seasprcp_202609.zip`, `lead3_DJF_temp` / `lead3_DJF_prcp`), `Fcst_Date` **20260917**, `Valid_Seas` **"DJF 2026-2027"**.
- **PJM footprint, above-normal temperature:** **40%** at Washington DC, Baltimore, Philadelphia, Newark, Pittsburgh, Columbus, Dayton, Indianapolis, Chicago, Charleston WV, Louisville; **50%** at Cleveland; **33%** on the southern VA edge (Richmond, Roanoke).
- **Δ vs the 8/20 issuance: IDENTICAL at all 8 PJM points tested**, and identical at 9 of 10 precip points.
- ⚠️ **The decision-relevant part: CPC raised historic-event odds 69% → 75% over that same month and did not strengthen the DJF CONUS signal at all.** A rising ENSO amplitude is not translating into a stronger forecast CONUS anomaly. **This is §5's reliability problem appearing inside CPC's own product.**
- **AEO-07 / AEO-08 bear on this** (PJM DJF mean above normal 70%; ≥1 PJM cold-alert event despite the warm mean 65%). **Measurement supplied; not graded.**

**② 🔴 The Colorado Upper Basin caveat was TESTED, not repeated — and it HOLDS, having moved further against relief.**
DJF precipitation category at 12 Upper Basin points: **Equal Chances (33%, no tilt either direction)** at Grand Lake (Colorado headwaters), Steamboat Springs/Yampa, Aspen, Pinedale WY (Green River headwaters), Vernal/Uinta, Flaming Gorge, Grand Junction, Moab, **Page AZ / Lake Powell**, and Salt Lake City. A weak **Above 33%** reaches only the southernmost sub-basins (Gunnison, Durango/San Juan).
Contrast: **coastal CA and Tucson 50% Above**, Phoenix 40% Above, FL 50–60% Above; **Northern Rockies DRY — Great Falls MT Below 40%, Missoula Below 33%.**
⇒ **Wet signal south and coastal; Northern Rockies dry; Powell's inflow zone in Equal Chances between them.** Exactly the geometry AEOLUS's guard describes.
⚠️ **And the one thing that changed since 8/20 moved the wrong way for relief:** **Aspen CO dropped OFF its weak Above-normal tilt into Equal Chances** — the wet tilt retreated *southward, away from* the Upper Basin. **"Do NOT assume El Niño refills the Colorado" is strengthened, not weakened.**

**③ 🔴 `SOURCES.md` needs three corrections** (worker did not edit it — it is not my file to re-author beyond reporting):
- ① and ② document ONI/RONI as **ERSSTv5**; both are now **ERSSTv6** as of 2026-08-10.
- ② should carry the CPC revision notice, which explains the MJJ +0.98 → +0.97 move: *"values may change up to two months after the initial 'real time' value is posted. Therefore, the most recent RONI values should be considered an estimate."*
- ② should record the product **home** page as the documented navigation path for a future 404.

**④ The two observations with no canonical instrument name were logged, NOT written to SERIES.tsv.** AGENT.md forbids inventing instruments. **Proposed for AEOLUS's approval:** `djf_prcp_upperbasin_category`, `djf_prcp_nrockies_category`. Also flagged: SERIES.tsv has drifted to non-vocabulary names (`oni_jja`, `roni_mjj`, `nino34_monthly_oisst`) and keys seasonal rows two different ways (`2026-DJF` vs a pull date). **This pass used the AGENT.md canonical names.** A normalisation pass is AEOLUS's call.

**⑤ On the weekly-basis question AEOLUS asked me not to resolve** — the file header bears on it and says **nothing**: `wksst9120.for` carries only *"Weekly SST data starts week centered on 2Sept1981"* and the column labels. No basis note, no offset note. **The only CPC documentation is the deck footnote: weekly SST monitoring (slides #4-9) uses OISSTv2.1 and "remains unaffected" by the ERSST version change.** ⇒ **AEOLUS's current position — NO offset applied — is what CPC's documentation supports.** Reported, not resolved.

---

## ⚠️ CONTRADICTIONS WITH `DOSSIER.md` — flagged loudly, NOT silently overwritten

**A. 🔴 The "first WoW pullback this season" no longer exists in the live series.**
DOSSIER (8/27) and the 8/27 RUN_REPORT both record: *"05AUG +2.6 → 12AUG +2.7 → **19AUG +2.6**: first WoW pullback, still 3rd-highest week of season."*
**Today's file reads 05AUG +2.5 · 12AUG +2.6 · 19AUG +2.6 — a flat top, not a pullback.** CPC revised three recorded weeks (29JUL 2.3→2.4, 05AUG 2.6→2.5, 12AUG 2.7→2.6; also Niño-3 19AUG 3.3→3.2, Niño-1+2 12AUG 4.0→4.1).
**Handled as a revision, not as anyone's error** (AGENT.md: *"NEVER treat an ERSSTv5 revision as an error"* — same principle, OISST near-real-time). Revision rows appended to SERIES.tsv with `revised from X`. **The narrative claim in DOSSIER is the thing that needs AEOLUS's attention, not the numbers.**

**B. 🔴 The 8/27 "stale / not-regenerated slide" hypothesis is REFUTED.**
The 14Sep2026 deck's *"latest weekly SST departures"* bullet slide **did** regenerate: **0.0/1.8/2.5/3.2 → −0.1/2.0/2.8/3.7** (Niño-4/3.4/3/1+2). It is not a frozen artifact.
**The mismatch persists and stays near-uniform:** `wksst9120.for` 09SEP reads 0.9/2.9/3.7/4.5 ⇒ deltas **−1.0 / −0.9 / −0.9 / −0.8**.
**NEW INDEPENDENT DISCRIMINATOR:** the same near-uniform gap appears between two *monthly* products for the *same month* — the 9/10 discussion's August ERSST quad **(0.1/1.8/2.5/3.4)** vs `sstoi.indices` August OISST quad **(0.93/2.52/3.13/4.08)**, deltas **−0.83 / −0.72 / −0.63 / −0.68**.
⇒ **The gap tracks ERSST-vs-OISST, not staleness.** ⚠️ **But that contradicts CPC's own footnote, which states those weekly slides use OISSTv2.1 — the same product as `wksst9120.for`.**
**VERDICT: STILL UNRESOLVED**, but the mechanism is now a *documented CPC self-contradiction* rather than a suspected stale artifact. **Ruling unchanged: `wksst9120.for` is the sole authoritative weekly figure (KB-088).** ⛔ **I did NOT derive a conversion offset** — a uniform gap inferred across a handful of coincidences is the free-parameter crosscheck that validates nothing.

**C. DOSSIER §2 said "Current offset (MJJ 2026): +0.41."** On the current vintage MJJ reads **+0.42** (RONI revised 0.98→0.97), and the current season **JJA is +0.44**. Updated in place with the revision noted.

---

## gaps — instruments NOT pulled, with exact commands and exact errors

**No registered source failed. Every `SOURCES.md` command returned HTTP 200 on the first attempt**, including the one recorded as 404 last session.

| Item | Status | Exact detail |
|---|---|---|
| `RONI.ascii.txt` | ✅ **HTTP 200** | The 9/11 404 **did not reproduce** — see the re-location section. No substitution made. |
| **MJO** | ⛔ **NO REGISTERED SOURCE** | `SOURCES.md` carries no MJO pull command. The deck discusses MJO qualitatively but publishes no index value. **Nothing substituted.** |
| **PDO** | ⛔ **NO REGISTERED SOURCE** | No CPC PDO product in `SOURCES.md`; `grep -niE 'PDO\|decadal' deck.txt` → **no match**. **Nothing substituted.** |
| **IOD** | ⛔ **NO CPC PRODUCT EXISTS** | `grep -niE 'dipole\|IOD' deck.txt` → **no match**. The operational IOD index is **Australian BoM**, which is outside `SOURCES.md`'s "CPC primaries only — never a secondary" rule. **I did not pull a BoM or third-party figure.** ⚠️ **This is a real gap for C2** — AEOLUS names IOD as modulating the El Niño → Australian-wheat / SE-Asian-palm transmission, and there is currently **no instrument behind that leg.** Registering a source is AEOLUS's call. |
| **SOI** | 🟡 **QUALITATIVE ONLY** | The only figure-free statement available at a registered primary, verbatim (9/10): *"The traditional and equatorial Southern Oscillation indices remained negative."* No numeric SOI in the deck. |
| ONI **JAS 2026** | ⏳ not yet published | `oni.ascii.txt` ends at **JJA 2026**. Next season posts with the **8 Oct 2026** discussion. |
| RONI **JAS 2026** | ⏳ not yet published | `RONI.ascii.txt` ends at **JJA 2026**. CPC RONI page: *"This page is updated by the 5th of each month."* |
| `sstoi` **Sep 2026** | ⏳ month incomplete | File ends at **Aug 2026**, as expected on 18 Sep. |
| weekly **16SEP2026** | ⏳ not yet published | `wksst9120.for` ends at the week centred **09SEP2026**. |

⚠️ **Note on the deck's text layer:** `pdfminer` extracts the deck's prose and footnotes cleanly, but its **data tables flatten into bare digit columns with the row/column structure lost.** I read **no numeric value off a flattened table** — every figure in this report comes from an ASCII data file, an HTML table, a shapefile attribute, or deck *prose*.
