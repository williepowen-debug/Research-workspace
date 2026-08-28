# AEOLUS · HURRICANE — live dossier

**As-of: 2026-08-27.** Basin state, ACE and both seasonal outlooks re-pulled from primaries this date. **C1 score: 2 🟡 as last graded by AEOLUS 8/13 — a worker does not score; nothing below re-grades it.**

> **Last real data refresh: 2026-08-27**  ·  **Dossier written: 2026-08-27**
> *Two-clock header (PAT-044) — `scripts/ledger_staleness.py` reads the first line. **The data date, not the edit date**: a hygiene edit must NOT bump it.*
> **Observations → `hurricane/workbook/SERIES.tsv`** · findings → central `workbook/KB.tsv` · synthesis → `STATUS.md`. **Flow is one-way.**
> **Feeds:** C1
**We are in peak season (mid-Aug → mid-Oct).** *(CSU's own 8/19 words for the current window: "This period historically marks the real ramp-up for Atlantic TC activity.")*

---

## 0. 🔴 THE HEADLINE — THE 14-DAY SILENCE ENDED (Dolly, 8/27) — STILL NO GULF/FL SYSTEM

**The Atlantic basin was silent 2026-08-13 through 2026-08-27 (14 days) until Tropical Storm Dolly (AL04) formed 8/27 1100 AM AST, central tropical Atlantic (13.6N 38.7W).** NHC forecasts Dolly to degenerate into a tropical wave by Friday/Saturday under increasing SW shear and dry air, **DISSIPATED by 72h (~8/30 1800Z), before reaching the Leeward Islands.** Not a Gulf/FL system on the current forecast track. Ongoing — not yet resolved.

**NHC's own 2026 season archive index (last checked 8/21) plus this run's ATCF pull: four Atlantic named storms — Arthur, Bertha, Cristobal, Dolly — all Tropical Storms. ZERO Atlantic hurricanes. ZERO majors, 14 weeks into the season.**

> 🔑 **Prior headline (8/13–8/21), preserved for continuity:** eight days of complete Atlantic silence, corroborated by `CurrentStorms.json` (0 Atlantic active), ATCF `/btk/` (no `bal04` for 8 days) and ATCF `/dis/` (no `al04` discussion) — see LOG.tsv `atlantic_eight_day_silence`. **The archive gap that headline flagged (8/14–8/18 outlook text unrecoverable) is now CLOSED — see §7.** It surfaced one more system this dossier had not recorded: **AL92's remnant briefly reached the Southeastern Caribbean Sea on 8/15 AM at near-0% formation odds before dissipating within six hours** (STORMS.tsv). It was never a Gulf/FL threat, but it was a Caribbean presence the "eight days of complete silence" framing did not capture — silence in the Atlantic-wide advisory record is not the same claim as silence in the outlook prose.

---

## 1. BASIN STATE (NHC TWO, 800 PM EDT Thu Aug 27 2026 — Forecaster Hagen)

| System | Odds 48h / 7d | Location | Fires the trigger? |
|---|---|---|---|
| **TS Dolly (AL04)** | active, advisories issued | central tropical Atlantic, 13.7N 40.7W, moving fast **W** at 21 kt under a ridge | ❌ forecast track dissipates before the Leeward Islands; not Gulf/Caribbean |

**Today's TWO, verbatim on everything else: *"Tropical cyclone formation is not expected during the next 7 days."*** No invests, no formation percentages anywhere in the basin — the only system is Dolly itself, already past the outlook stage.

> 🔴 **GULF / FLORIDA: NO.** Dolly's NHC forecast track (Discussion #2, 500 PM AST 8/27) has it **degenerating into a strong tropical wave Friday/Saturday and DISSIPATED by 72h (~8/30 1800Z)** — i.e. the storm is forecast to end *before* it reaches the Leeward Islands, let alone the Caribbean or Gulf. Heavy-rain risk to the Leewards/VI/PR/Hispaniola is flagged in NHC's Key Messages as a **post-tropical remnant-moisture** hazard, not a Gulf/FL cyclone risk. **No other invest exists anywhere in the basin.** *(Prior 8/21 read, preserved: peak formation odds were 20% on two non-tropical/subtropical NE-Atlantic and central-subtropical lows, neither Gulf/FL, both since dissipated per the archive close in §7.)*
>
> **Escalation line NOT FIRED.** Reported as state; AEOLUS grades.

### The shear prose — now carried by Dolly's own discussion

| Product | Date | Prose |
|---|---|---|
| **NHC Cristobal Discussion #5** | 8/13 1500Z | *"entrenched in a hostile environment, with cool SSTs, **strong northerly vertical wind shear** and dry mid-level air"* |
| **CSU two-week forecast** | 8/19 | *"the base state across the Atlantic is quite TC-unfavorable, given the **strong El Niño and associated high levels of vertical wind shear**"* |
| **NHC AL92 archived TWO** (via IEM, closes §7 gap) | 8/15 0800 AM EDT | *"Development of this system is not expected due to **strong upper-level winds and dry air**"* |
| **NHC Dolly Discussion #2** | **8/27 500 PM AST** | *"The environment around Dolly will likely become unfavorable for strengthening on Friday with **increasing southwesterly shear** due to a central Atlantic upper-level trough, fast forward motion and dry air aloft… Global and regional models all show Dolly degenerating into a strong tropical wave"* |

> ⚠️ **The mechanism is back on a live storm, in NHC's own forecaster prose, for the first time since Cristobal on 8/13.** Dolly is a direct, named, currently-active test of the same El Niño shear mechanism that killed AL92, AL94 and the AL92 Caribbean remnant. **Not yet resolved** — verifies when the 72h dissipation forecast either verifies or busts (~8/30).

---

## 1b. ACE — recomputed 8/27, method re-validated end-to-end

| | value |
|---|---:|
| **2026 season-to-date ACE** | **3.4575** — Arthur 0.405 · Bertha 2.2425 · Cristobal 0.4425 · **Dolly 0.3675 (ongoing, still active)** |
| **Change since 8/21** | **+0.3675 — first ACE accrual in 14 dark days** (all from Dolly's 3 synoptic times ≥34 kt so far: 8/27 12Z/18Z, 8/28 00Z, all 35 kt) |
| 1991-2020 normal, **full season** | **122.58** (mean) · **129.25** (median) — re-validated, unchanged |
| **To-date normal, Aug 27** | **26.72** *(exclusive convention — same convention that reproduced 13.25 for Aug 13 and 18.98 for Aug 21 exactly)* · **28.41** *(inclusive)* — **freshly recomputed this run, NOT reused from 8/21** |
| **2026 vs Aug-27 to-date normal** | **12.94%** *(exclusive)* · **12.17%** *(inclusive)* — was 16.3% on Aug 21, 23.3% on Aug 13 |
| **Seasonal accrual by Aug 27** | **21.8%** of seasonal ACE has normally accrued *(vs 15.48% by Aug 21, 10.81% by Aug 13)* |
| AEO-01 criterion | season-end **< 110.3** ⇒ **margin 106.8 ACE units of headroom remain** |

✅ **Parse re-validated end-to-end this run:** same computation reproduces **14.40 mean named storms / 7.20 mean hurricanes**, full-season normal **122.58**, and Arthur/Bertha/Cristobal's 0.405/2.2425/0.4425 exactly. Dolly's leg computed from `bal042026.dat` tau=0 rows at 2026082712Z/18Z/2026082800Z (all TS, 35 kt): 3 × 35²/10⁴ = 0.3675.

⚠️ **The ratio FELL again despite an active storm forming — read the mechanism, not just the sign.** A normal season's to-date-normal climbs **~7.7 ACE units** between Aug 21 and Aug 27 (18.98 → 26.72) as peak season ramps; 2026 added only **0.37** over the same 6 days. **12.9% < 16.3%: an active storm and a falling ratio can both be true at once** when the seasonal base is accelerating faster than the observed accrual.

⚠️ **DO NOT reuse the Aug-21 to-date normal of 18.98 on Aug 27 or later.** It is date-specific and the standing hazard has now recurred twice (Aug-13→Aug-21, Aug-21→Aug-27): reusing a stale to-date normal always flatters the ratio, because the denominator only grows through peak season.

⚠️ **Convention sensitivity — flagged, not chosen.** Under the **inclusive** convention 2026 is the **lowest of all 30 years** through Aug 21. Under the **exclusive** convention (the one that reproduces the recorded 8/13 figures) 2026 is **2nd-lowest**, and the single year below it is **1998 at 3.08** — AEOLUS's own standing counter-analogue. **The dramatic reading and the folder-consistent reading differ. AEOLUS picks the convention.**

⚠️ **Denominator hazard vs NOAA.** NOAA CPC states 2026 ACE as **30-90% of the MEDIAN**. AEOLUS's bands are % of the **MEAN**. Recomputed from the same file: mean 122.58, **median 129.25**. NOAA's band = **38.8–116.3 ACE = 31.6–94.9% of the mean**. **NOAA's upper bound of 116.3 sits ABOVE AEO-01's <110.3 line.** The two "90%" figures are not the same number.

### ⚠️ The Aug-13 base rate does NOT hold at the same strength on Aug 21 — **NOT re-run this session (8/27); table below is 8/21 vintage**

Like-for-like recompute — share of the lowest-to-date seasons that finished **<90% of normal**:

| Slice | at **Aug 13** | at **Aug 21** |
|---|---:|---:|
| bottom-6 | **5/6 = 83%** | **3/6 = 50%** |
| bottom-8 | 6/8 = 75% | 5/8 = 62% |
| bottom-10 | 7/10 = 70% | **7/10 = 70%** |

**Why it moves:** the Aug-21 bottom-6 cohort is **1998 (148%), 2002 (55%), 1992 (62%), 2019 (108%), 1999 (144%), 1993 (31%)** — it picks up **three big-finish seasons** the Aug-13 cohort did not contain. Seasons that are quiet *through late August* include some that then exploded in September.

> ⚠️ **Read the sensitivity, not the headline.** n=6 is small and **bottom-10 is stable at 70% on both dates**, so this is partly a ranked-head artefact. But it is a real directional caution against carrying the "5 of 6" figure forward as though it were date-independent. **AEO-01 is AEOLUS's to grade — this is reported as an observation.**

---

## 2. SEASON OUTLOOKS — both re-verified UNCHANGED again; CSU two-week cadence held its schedule

| Source | 2026 forecast | Date | State on 8/27 |
|---|---|---|---|
| **CSU (Klotzbach)** seasonal | **9 / 4 / 1** (NS/H/MH) · **ACE 50** | 8/5 | **RE-VERIFIED UNCHANGED** |
| **NOAA CPC** | **7-13 / 2-6 / 0-2**, **75%** below-normal | 8/6 | **RE-VERIFIED UNCHANGED** — page still carries the 6 Aug issuance |
| **CSU two-week** | Aug 19-Sep 1 window: **below-normal 70%** | 8/19 | still the latest issue — **no interim issue landed 8/21-8/27**; next scheduled **9/2**, confirmed on-page |

**`csu_ace_forecast` RATIFIED this run:** CSU's live table still reads `Accumulated Cyclone Energy (ACE) 50 / Average for 1991-2020: 123`, unchanged since 8/5 and matching the vocabulary entry added 8/21 exactly (name and value both correct in `SOURCES.md`/`AGENT.md`). **50 = 40.8% of the 122.58 normal.**

### CSU peak-season two-week cadence — held its schedule this time (contrast with the 8/13-8/21 miss)

Unlike the 8/13→8/21 gap (which missed the 8/19 issue because the folder wrongly believed the series had ended), **the 8/21→8/27 gap contains no missed issue** — the schedule (Aug 5 · Aug 19 · **Sep 2** · Sep 16 · Sep 30) puts the next issue six days past this run's write date. Confirmed directly on CSU's page: the 2-week forecast list still ends at "(Aug 19, 2026)" before "(Sep 2, 2026)."

| CSU two-week | Window | Terciles (1966-2025) | Forecast |
|---|---|---|---|
| issued 8/5 | Aug 5-18 | <2 / 2-6 / >6 ACE | below-normal 80% — **verified: observed 0.4425, inside tercile** |
| issued **8/19** | Aug 19 - Sep 1 | <7 / 7-22 / >22 ACE | **BELOW-NORMAL 70% · near 28% · above 2%** — **not yet gradeable (window runs through 9/1); Dolly's ACE (0.3675 so far) counts toward this window** |

> ⚠️ **Note the tercile widening — Aug 5-18 below-normal was `<2 ACE`; Aug 19-Sep 1 below-normal is `<7 ACE`.** CSU's own climatology confirms the ramp the accrual base rate measures. **A "below-normal" label means a different quantity in each window; do not compare the labels across windows.**

---

## 3. ⚠️ PERIL vs LOSS — NOT RE-PULLED THIS RUN

**The loss leg carries its 8/13 vintage and is now 14 days older.** Commercial publishers run on their own schedule (H1 ~Jul-Aug, full-year ~Jan); nothing new was expected or pulled. **Labelled stale rather than substituted.**

Last read (8/13): July renewal global cat **−16%**, NA **−20/25%**; capital at a record **>$700-790B**; H1 US insured nat-cat **~$36B, ~25-28% BELOW** the 10-yr average.

⇒ **Peril and loss diverge again as of 8/27** — a system (Dolly) is now active, however unlikely to matter, while the loss leg is unchanged and stale. Not the same alignment as the 8/21 empty-basin read.

---

## 4. THE ENSO MECHANISM (sign from `../regime/` — cited, not copied)

**El Niño → increased vertical wind shear over the tropical Atlantic → suppressed cyclogenesis.**

Corroboration state as observed **inside my own products** this run:

1. **Seasonal** — CSU held at 9/4/1 with ACE 50; NOAA held at 75% below-normal.
2. **Sub-seasonal** — **NEW LEVEL:** CSU's 8/19 two-week forecast names the mechanism explicitly for the current window.
3. **Storm-level** — NHC's final Cristobal discussion named *strong northerly vertical wind shear and dry mid-level air*.
4. **Outcome-level** — **NEW:** three 2026 Atlantic named storms, **zero hurricanes**, ACE 3.09; the Pacific basins carry three hurricanes over the same season.
5. **NOAA's own base rate, verbatim:** *"All hurricane seasons coincident with strong (≥1.5 °C Niño3.4) El Niño events since 1950 have featured below-normal seasonal activity."* NOAA's July ENSO forecast: **90%** chance of strong-or-very-strong El Niño during ASO (RONI ≥1.5 °C), **48%** very strong (RONI ≥2.0 °C).

⚠️ **ENSO index values are `regime/`'s instrument** (SHARED-INPUT RULE). The RONI/Niño3.4 figures above are quoted **as they appear inside my own outlook products** and are **not** copied into this folder's series. Reconcile at `regime/`.

⚠️ **Standing caveat unchanged (L-14/L-17):** at record amplitude the underpinning composites are least reliable.

---

## 5. 🔑 THE TELL TO WATCH THROUGH PEAK SEASON — now FOUR confirming instances, plus a live fifth test

**Do 80%-probability (or shear-flagged) systems keep shearing apart before reaching the western basin?**

**AL92 (orig. 8/12-13, 80%/80%) — NEVER DEVELOPED.** No `bal04`, no `al04` discussion, invest deck purged.
**AL94 (8/13, 30%/50%) — NEVER DEVELOPED.** Archive close (§7) adds the exact death: 8/15 1400Z, *"moving into an area of less favorable environmental conditions and development of this system is not expected."*
**AL92's Caribbean remnant (NEW, recovered from the archive close, §7) — 8/15 0800 AM EDT, Southeastern Caribbean Sea, near-0%/near-0%, *"development not expected due to strong upper-level winds and dry air."*** Dropped from the very next issuance six hours later.
**AL93/Cristobal (8/13) — became a fish storm near the Azores, dissipated.**

**Running tally: FOUR failed-development instances, zero exceptions, all citing the same shear/dry-air mechanism in NHC's own prose.**

🔴 **A live FIFTH test is now running: TS Dolly (AL04, formed 8/27).** NHC's own forecast (Discussion #2) predicts the identical outcome — SW shear + dry air degenerating Dolly into a tropical wave by 8/29-30, dissipated by 72h, before reaching the Leeward Islands. **Not yet resolved.** If it verifies, the tell reaches 5-for-5; if Dolly instead re-organizes past the Leewards, it is the first break and should be flagged hard.

⚠️ **The falsifier, both directions, unchanged:** a single **Gulf/FL major landfall** reverses ROL, the C1 score and the pre-registered RNR entry. **A suppressed season is a probability statement, not a guarantee** — 1992 (Andrew, in a quiet season) is the standing reminder.

---

## 6. PREDICTIONS — **not resolved here; worker reports value and margin only**

- **AEO-01** — season-end ACE **< 110.3** AND ≤7 hurricanes, resolves **11/30**.
  **State 8/27: ACE 3.4575 → 106.8 units of headroom below the threshold. Hurricanes: 0 → 7 of 7 remaining.** Season-to-date is **12.94% of the Aug-27 to-date normal** (exclusive convention) — down from 16.3% on Aug 21, despite Dolly's active formation, because the to-date normal outran the accrual (§1b).
  ⚠️ **8/21 base-rate figures (bottom-6 = 50%, 1998 counter-analogue) were NOT re-run this session** — carried forward unchanged, not re-verified. **AEOLUS grades AEO-01.**
- **AEO-03** — property-cat reinsurance still soft at the **Jan-2027** renewal (ROL ≤+5% YoY), resolves **1/15/27**. **Loss leg not re-pulled this run** — no new evidence either way.

---

## OPEN QUESTIONS / GAPS

1. ✅ **ACE instrument — CLOSED 8/13, RE-VALIDATED 8/21 AND 8/27.** Method runs clean end-to-end; all legs reproduce, including the new Dolly leg. ✅ **`AGENT.md` correction CONFIRMED APPLIED** — its instrument table and open question #1 now correctly read "COMPUTED... see SOURCES.md" / "CLOSED 2026-08-13" as of this run's read. *(This item's 8/21 complaint is resolved; no further action.)*
2. ✅ **AL92's track — ANSWERED.** Never developed. See §5.
3. **Peak-season tell (§5)** — **now FOUR confirming instances** (AL92, AL94, AL92-Caribbean-remnant, AL93/Cristobal) plus a **live fifth test running now (Dolly)**. Track through mid-Oct.
4. **Jan-2027 renewal** — AEO-03's resolution; watch Artemis / Guy Carpenter from December.
5. ✅ **CSU two-week correction CONFIRMED APPLIED** — `SOURCES.md` now carries the full corrected cadence and schedule as of this run's read. *(This item's 8/21 complaint is resolved; no further action.)*
6. ✅ **CLOSED 8/27 — archived TWO text.** Verified working second/independent archive: **IEM AFOS** (`mesonet.agron.iastate.edu`), two-step `list.json` + `nwstext` command — see LOG.tsv `two_archive_gap_CLOSED` for the exact commands. All 20 issuances for 8/14-8/18 retrieved and read; confirms no Gulf/FL system in the window and surfaces the AL92-Caribbean-remnant instance (STORMS.tsv). **8/20 was NOT re-attempted this run** (out of the originally-flagged 8/14-8/18 scope) — trivial to close with the same command if needed. *(Proposed `SOURCES.md` addition — AEOLUS owns it.)*
7. **Denominator reconciliation** — NOAA quotes ACE vs **median**; AEOLUS's bands use **mean**. Still open, not addressed this run. See §1b.
8. **NEW — Dolly resolution (~8/30).** Does the shear/dry-air degeneration forecast verify (5th confirming tell instance) or bust (first break, Gulf/FL implications if it re-organizes past the Leewards)? Check ATCF for `bal04` status and any renewed `al04` discussion at next spawn.
