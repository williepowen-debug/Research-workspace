# AEOLUS · HURRICANE — live dossier

**As-of: 2026-09-18.** Basin state, ACE, both seasonal outlooks and the loss leg re-pulled from primaries this date. **C1 score: 1 as last held by AEOLUS 2026-09-11 (drain session) — a worker does not score; nothing below re-grades it.**

> **Last real data refresh: 2026-09-18**  ·  **Dossier written: 2026-09-18**
> *Two-clock header (PAT-044) — `scripts/ledger_staleness.py` reads the first line. **The data date, not the edit date**: a hygiene edit must NOT bump it.*
> **Observations → `hurricane/workbook/SERIES.tsv`** · findings → central `workbook/KB.tsv` · synthesis → `STATUS.md`. **Flow is one-way.**
> **Feeds:** C1
**The climatological peak (~Sep 10) has PASSED.** *(CSU's own 9/16 words: "This period immediately follows the climatological peak of the season.")* Peak season runs to mid-Oct.

> ⚠️ **PRIOR DOSSIER VINTAGE WAS 2026-08-27 — a 22-day gap, of which the folder was unread 8/28–9/17.** The 9/11 AEOLUS drain session logged TS Edouard from a **secondary** and explicitly owed this pass: ATCF pull, ACE recompute, CSU 9/02 read. **All three are discharged here.** The §0 headline below **supersedes** the 8/27 "silence ended (Dolly)" headline.

---

## 0. 🔴 THE HEADLINE — TWELVE CONSECUTIVE DAYS OF A BLANK BASIN ACROSS THE CLIMATOLOGICAL PEAK; ACE NOW BELOW EVERY YEAR OF THE NORMALS PERIOD

**Every one of the 48 NHC Tropical Weather Outlook issuances from 2026-09-01 through 2026-09-12 inclusive carried the line *"Tropical cyclone formation is not expected during the next 7 days."*** Four issuances a day, all retrieved and read. **Twelve consecutive days of a completely blank Atlantic formation outlook — and the ~September 10 climatological peak of the season sits inside that window.** First re-entry 9/13 at near-0%/20%.

**Season-to-date Atlantic ACE = 4.3950 on Sep 18, against a to-date normal of 73.7248 — 5.96%.** **2026 is now lower than every one of the 30 years 1991-2020 at this calendar date.** The previous low was 1994 at 11.2500; 2026 sits at 39% of it. **The 8/27 convention-sensitivity caveat no longer bites** — 2026 ranks 1st-lowest of 30 under *both* the exclusive and the inclusive convention.

**Five Atlantic named storms — Arthur, Bertha, Cristobal, Dolly, Edouard — all Tropical Storms. ZERO Atlantic hurricanes. ZERO majors. Season peak intensity 50 kt, 17 weeks in.**

> 🔑 **The one thing that moved against the pattern: TS Edouard made landfall.** AL05 formed in the Gulf 8/31, reached 50 kt and came ashore at Johnson Bayou LA on 9/1 — **the first Atlantic landfall of 2026, and the first 2026 system that did not shear apart before the western basin.** It is a Gulf, not a Florida, system and it was a tropical storm, not a hurricane. **§5 flags it as the first non-conforming instance of the peak-season tell; AEOLUS adjudicates whether the tell survives.**

---

## 1. BASIN STATE (NHC TWO, 200 PM EDT Fri Sep 18 2026 — Forecaster Papin)

`CurrentStorms.json` returned **0 active storms in ALL basins** — no basin filtering needed this run.

| System | Odds 48h / 7d | Location | Fires the trigger? |
|---|---|---|---|
| **AL99** | **70% / 70%** | Eastern Subtropical Atlantic, low pressure several hundred mi **SW of the Azores**, 33.0N 34.2W | ❌ ~3,500 mi from Florida; subtropical eastern-Atlantic system |

**The TWO carries nothing else.** AL99 is the only entry in the basin.

> 🔴 **GULF / FLORIDA: NO. Escalation line NOT FIRED.** Reported as state; AEOLUS grades.

**AL99's prose, read per the 8/13 discipline — the number and the text point different ways again:** 70% is the highest formation probability the basin has shown since August, and the same paragraph says the system is *"expected to move slowly over the next couple of days remaining southwest of the Azores, followed by a turn to the southwest by early next week, **when environmental conditions are forecast to become less favorable for additional development**."* **A 70% that NHC already expects to run out of runway.** It rose intraday 20/30 (8 AM) → 60/60 (Special TWO, 10:30 AM) → 70/70 (2 PM).

### What happened in the 9/1 → 9/18 gap

| Date(s) | State |
|---|---|
| **9/1** | TS **Edouard (AL05)** landfall Johnson Bayou LA. Formation outlook already blank; the only Gulf references are to Edouard's own inland remnant as an *Active System* |
| **9/2** | *"The Weather Prediction Center is issuing advisories on Tropical Depression Edouard, located inland over eastern Texas."* Formation line blank |
| **9/3 – 9/12** | **Blank on all 40 issuances.** No invests, no percentages anywhere in the basin |
| **9/13 – 9/18** | **AL98** (central subtropical Atlantic, E of Bermuda) — near-0%/20% → **peak 40%** 9/14-15 → 30% → 10% → **removed from the outlook by a Special TWO, 10:30 AM EDT 9/18**, *"development of this system is no longer expected"* |
| **9/17 – 9/18** | **AL99** appears and climbs to 70%/70% |

**No named storm formed between Edouard (8/31) and today.** The ATCF b-deck listing carries only `bal01`–`bal05` plus the two live invest decks `bal98`/`bal99` — a primary-source negative, not an inference.

### The shear prose — the mechanism is still being named by both issuers

| Product | Date | Prose |
|---|---|---|
| **CSU two-week** | **9/02** | *"Global model signals for TC development in the next two weeks are **remarkably weak**, given the next two weeks include the **climatological peak of the season**"* |
| **CSU two-week** | **9/16** | *"the base state across the Atlantic is quite TC-unfavorable, given the **strong El Niño and associated high levels of vertical wind shear**"* — third consecutive issue naming it |
| **NHC TWO (AL98)** | **9/18 0800 EDT** | *"Development of this system is no longer expected as it drifts slowly over the subtropical Atlantic"* |
| **NHC TWO (AL99)** | **9/18 1400 EDT** | *"environmental conditions are forecast to become less favorable for additional development"* |

---

## 1b. ACE — recomputed 9/18, method re-validated end-to-end

| | value |
|---|---:|
| **2026 season-to-date ACE** | **4.3950** |
| — per storm | Arthur **0.4050** · Bertha **2.2425** · Cristobal **0.4425** · Dolly **0.4900** · Edouard **0.8150** · invests AL98/AL99 **0.0000** |
| **Change since 8/27** | **+0.9375** — Edouard 0.8150 (new) + Dolly **revised 0.3675 → 0.4900** |
| 1991-2020 normal, **full season** | **122.58** (mean) · **129.25** (median) — re-validated, unchanged |
| **To-date normal, Sep 18** | **73.7248** *(exclusive)* · **75.5129** *(inclusive)* — **freshly recomputed this run, NOT reused from 8/27** |
| **2026 vs Sep-18 to-date normal** | **5.96%** *(exclusive)* · **5.82%** *(inclusive)* — was 12.94% on Aug 27, 16.3% on Aug 21, 23.3% on Aug 13 |
| **Seasonal accrual by Sep 18** | **60.14%** of seasonal ACE has normally accrued *(vs 21.8% by Aug 27)* |
| **Hurricanes / majors to date** | **0 / 0.** Season peak intensity **50 kt** (Bertha 7/21-22; Edouard 9/1) |
| AEO-01 criterion | season-end **< 110.3257** ⇒ **105.931 ACE units of headroom remain** |

✅ **Parse re-validated end-to-end this run:** the same computation returns **14.40 mean named storms / 7.20 mean hurricanes** against NOAA's published 1991-2020 normals of 14 / 7, and reproduces Arthur/Bertha/Cristobal at 0.4050/2.2425/0.4425 exactly.

⚠️ **DOLLY'S FIGURE WAS REVISED, not recomputed differently.** 8/27 recorded **0.3675** from three synoptic times *while the storm was still active*; the completed b-deck adds **2026082806 at 35 kt**, giving **0.4900**. **This is the generic hazard in logging an ACE leg for an ongoing storm — the value is provisional by construction and nothing in the row said so.** Appended as a revision, original preserved.

⚠️ **The denominator has now outrun the numerator by a factor of 22 since 8/13.** A normal season's to-date normal went 13.25 → 26.72 → **73.7248** (Aug 13 → Aug 27 → Sep 18) as peak season ran; 2026 went 3.09 → 3.4575 → **4.3950**. **The ratio falling from 12.94% to 5.96% across a period that contained a landfalling tropical storm is almost entirely the calendar, not new quiet.** Read the mechanism, not the sign.

⚠️ **DO NOT reuse the Aug-27 to-date normal of 26.72 on any later date.** The hazard has now recurred three times (Aug-13→21, Aug-21→27, Aug-27→Sep-18). It only ever flatters the ratio.

⚠️ **Denominator hazard vs NOAA — unchanged and still open.** NOAA CPC states 2026 ACE as **30-90% of the MEDIAN**; AEOLUS's bands are % of the **MEAN**. Mean 122.58, median 129.25. NOAA's band = **38.8–116.3 ACE = 31.6–94.9% of the mean**. **NOAA's upper bound of 116.3 sits ABOVE AEO-01's <110.3257 line. The two "90%" figures are not the same number and must never be read across.**

### Residual-season context — recomputed at Sep 18 (measurement, not a probability)

**What a normal season has left after Sep 18** (1991-2020, full season minus inclusive-to-date):

| | ACE |
|---|---:|
| mean remaining | **47.071** |
| median remaining | **47.189** |
| max remaining | **119.905 (1998)** |
| min remaining | **2.242 (1997)** |
| median per-year *share* of season remaining | **34.84%** |

**AEO-01 needs 105.931 further ACE units from here. Exactly ONE of the 30 years — 1998, at 119.905 — accrued that much after September 18.** 1998 is AEOLUS's own standing counter-analogue.

### The lowest-to-date base rate, recomputed like-for-like at Sep 18 — **it moved hard**

Share of the lowest-to-date cohorts that finished **<110.3257** (<90% of the mean):

| Slice | at **Aug 21** *(carried in the 8/27 dossier)* | at **Sep 18** |
|---|---:|---:|
| bottom-6 | 3/6 = 50% | **6/6 = 100%** |
| bottom-8 | 5/8 = 62% | **8/8 = 100%** |
| bottom-10 | 7/10 = 70% | **10/10 = 100%** |

Unconditional, all 30 years: **13/30 = 43%.** The Sep-18 bottom-10 cohort is 1994, 2002, 2013, 2015, 1991, 1992, 1993, 2014, 1997, 2009 — full-season ACE 32.0 to 76.2, i.e. **every one finished well under the line.**

> ⚠️ **Why it moved:** the late-August cohorts still contained seasons that were quiet through August and then exploded in September (1998, 1999). **By September 18 the September explosion has either happened or it has not** — that is most of what this table is measuring, and it is exactly why the *date* of a base rate is load-bearing. n is still small. **AEO-01 is AEOLUS's to grade — this is reported as an observation.**

---

## 2. SEASON OUTLOOKS — seasonal legs unchanged; **two missed two-week issues recovered**

| Source | 2026 forecast | Date | State on 9/18 |
|---|---|---|---|
| **CSU (Klotzbach)** seasonal | **9 / 4 / 1** (NS/H/MH) · **ACE 50** · ACE W-of-60W 25 | 8/5 | **RE-VERIFIED UNCHANGED** — 8/5 remains the final seasonal issuance; page schedule lists Nov 2026 Verification next |
| **NOAA CPC** | **7-13 / 2-6 / 0-2**, **75%** below-normal | 8/6 | **RE-VERIFIED UNCHANGED** — page still carries the 6 August issuance |
| **CSU two-week** | Sep 16-29 window: **below-normal 78%** | **9/16** | latest issue; next **9/30**, then 10/14 |

⚠️ **NOAA's page text is now stale on observed counts** — it still reads *"including the 2 named storms recorded thus far"* and *"the 3% recorded thus far."* Those are 8/6 vintage. **Actual is 5 named storms.** The *forecast* is unchanged; the embedded observation is not current. Do not quote the page's "thus far" figures.

### CSU two-week series — the full 2026 record, both missed issues now read

| Issued | Window | Below-normal tercile | Forecast | **Observed ACE in window** |
|---|---|---|---|---:|
| 8/05 | Aug 5-18 | `<2` | below-normal **80%** | **0.4425** |
| 8/19 | Aug 19 - Sep 1 | `<7` | below-normal **70%** | **1.1450** |
| **9/02** | **Sep 2-15** | `<11` | **below-normal 97%** · near 3% · above ~0% | **0.1600** |
| **9/16** | **Sep 16-29** | `<11` | **below-normal 78%** · near 20% · above 2% | **0.0000** *(window open through 9/29)* |

**The 9/02 issue is the highest below-normal confidence of the 2026 series (80 → 70 → 97 → 78)** — and CSU issued it *for the fortnight containing the climatological peak.* Its window closed 9/15 with a single qualifying synoptic time in it (Edouard at 2026090200, 40 kt).

> ⚠️ **TERCILE BOUNDARIES DIFFER PER WINDOW** (Aug 5-18 below = `<2`; Aug 19-Sep 1 = `<7`; Sep 2-15 = `<11`; Sep 16-29 = `<11`). **Never compare the LABEL across windows.** Observed values are reported as measurement — **AEOLUS decides whether a window verified.**

---

## 3. ⚠️ PERIL vs LOSS — RE-PULLED THIS RUN, and the divergence is now **directional agreement**

**PERIL AND LOSS ARE DIFFERENT INSTRUMENTS. This section never speaks for §1b and §1b never speaks for it.**

**No newer catastrophe-loss market tally exists than the vintage already held.** Gallagher Re's Q3 report lands ~October.

| Instrument | Value | Vintage | Note |
|---|---|---|---|
| **Gallagher Re** H1 2026 global insured nat-cat | **$46bn, 28% below the $64bn 10-yr average** | **Aug 2026** | lowest H1 since 2018; 5th straight quarter with no single insured cat loss >$10bn; 11 events >$1bn vs a 10-yr average of 16; economic losses $142bn, −10% |
| **Swiss Re Institute** H1 2026 global insured nat-cat | **$42bn vs a $66bn long-term trend** | **Aug 2026** | **NEW second independent read.** ⚠️ **Secondary-sourced only — the Swiss Re primary page returned HTTP 403** (see §Gaps) |
| **Moody's** buyer survey, Jan-2027 property reinsurance | **most likely −7.5% to −15%**; **86%** expect declines (vs 74% for 2026) | **2026-09-16** | pre-Monte-Carlo. **A survey of expectations, NOT a transacted rate-on-line** — does not satisfy the ROL threshold row |
| **Swiss Re** Florida scenario | Cat-5 Miami/Tampa **$300bn+**; 1926 Miami repeat **$200bn+**; Andrew repeat **~$100bn** | **2026-09-16** | ⚠️ **MODELLED SCENARIO, NOT A LOSS TALLY.** FL specifics are **CORAL's** |

> ⚠️ **DO NOT reconcile $46bn and $42bn into one figure.** Different publishers, different perimeters, different denominators (10-yr average vs long-term trend). Carry both, labelled.

⇒ **Peril and loss are no longer pointing in opposite directions.** At 8/13 and 8/27 the basin had activity while the loss leg was soft. **Now both legs point the same way — a basin at 6% of its to-date normal, and a reinsurance market whose sell-side survey expects another 7.5-15% off in January.** That is a change in the *relationship between the two legs*, which is itself the C1 read. **AEOLUS scores it.**

### 🔑 NEW — a mid-cycle price surface, which this folder has been missing (PROPOSAL, §Open Questions 2)

AEOLUS's standing complaint is that **rate-on-line is visible only at Jan/Jun renewals, so a landfall between them has no price surface.** One exists and is machine-readable:

**Artemis "Catastrophe Bond Market Yield"** — the page embeds its full Highcharts series **inline in the HTML**, no JS execution needed. **827 weekly points, 2010-10-08 → 2026-08-28**; series: *Insurance Risk Spread*, *Collateral Yield* (3m T-Bills), *Expected Loss*. Data collated by **Plenum Investments AG**.

```bash
curl -s -A "Mozilla/5.0" -L "https://www.artemis.bm/catastrophe-bond-market-yield/"
# then regex the categories:[...] array and each  name:'X' ... data:[...]  block
```

| | 2025-08-29 | 2026-01-09 | 2026-07-10 | **2026-08-28** |
|---|---:|---:|---:|---:|
| Insurance risk spread | 6.07% | 5.29% | 5.75% | **5.05%** |
| Expected loss | 2.24% | 2.35% | 2.50% | **2.50%** |
| **spread / EL** | 2.71x | 2.25x | 2.30x | **2.02x** |

**−16.8% YoY. −12.2% across peak season (7/10 → 8/28) with expected loss FLAT at 2.50 — a pure price move, not a risk-mix move.**

> ⚠️ **TWO HARD CAVEATS, both load-bearing.**
> **① STALE BY DESIGN.** The page refreshes **monthly**; the newest point is **2026-08-28, three weeks behind today.** It is a between-renewals surface, not a daily one — **a landfall would not show for up to a month.** That limits, but does not remove, its value.
> **② IT IS NOT RATE-ON-LINE.** A cat-bond insurance risk spread and a reinsurance ROL are different instruments on different perimeters. Correlated, not interchangeable. **It must NOT be entered against the ROL threshold row.** If adopted it needs its own instrument name, its own band, and an explicit un-base-rated flag.
> **Instrument creation is AEOLUS's call. A worker does not invent an instrument — this is a proposal and nothing has been written to `SERIES.tsv` under a new name.**

---

## 4. THE ENSO MECHANISM (sign from `../regime/` — cited, not copied)

**El Niño → increased vertical wind shear over the tropical Atlantic → suppressed cyclogenesis.**

Corroboration state as observed **inside my own products** this run:

1. **Seasonal** — CSU held at 9/4/1 with ACE 50; NOAA held at 75% below-normal.
2. **Sub-seasonal** — CSU's 9/02 and 9/16 two-week forecasts both name the mechanism for the current window; 9/02 at **97%** confidence, for the fortnight containing the peak.
3. **Storm-level** — NHC's 9/18 prose on both AL98 (*"no longer expected"*) and AL99 (*"less favorable"*).
4. **Outcome-level** — five 2026 Atlantic named storms, **zero hurricanes**, ACE 4.3950 = **5.96%** of the to-date normal, **lowest of the 30-year normals period at this date**; twelve blank outlook days across the climatological peak.
5. **NOAA's own base rate, verbatim:** *"All hurricane seasons coincident with strong (≥1.5 °C Niño3.4) El Niño events since 1950 have featured below-normal seasonal activity."*

⚠️ **ENSO index values are `regime/`'s instrument** (SHARED-INPUT RULE). **No ENSO index value was pulled or recorded in this folder this run.** The July NOAA ENSO probabilities carried in the 8/27 dossier are **not refreshed here and are now ~10 weeks old** — reconcile at `regime/`, do not quote them from this file as current.

⚠️ **Standing caveat unchanged (L-14/L-17):** at record amplitude the underpinning composites are least reliable.

---

## 5. 🔑 THE PEAK-SEASON TELL — **FIRST NON-CONFORMING INSTANCE. Flagged, not adjudicated.**

**The question: do shear-flagged systems keep shearing apart before reaching the western basin?**

**Resolved since 8/27:**

| Instance | Outcome |
|---|---|
| **AL04 / Dolly** — the live fifth test | ✅ **CONFORMED.** Degenerated to a remnant low after 2026082806, never regained 34 kt; deck ends 2026083112 at 20.0N 70.6W near Hispaniola. NHC's SW-shear/dry-air degeneration forecast verified directionally (deck ran ~18h past the nominal 72h hour as a tracked remnant). Never reached the Gulf or FL |
| **AL98** (9/13-9/18) | ✅ **CONFORMED.** Peaked 40%/7d, died; *"development of this system is no longer expected"*; removed by Special TWO 9/18. Peaked 25 kt, ACE 0.0000 |
| 🔴 **AL05 / Edouard** | ❌ **DID NOT CONFORM.** Formed in the Gulf 8/31, intensified to **50 kt**, and made **landfall at Johnson Bayou LA on 9/1** — the first Atlantic landfall of 2026 and the first 2026 system that did not shear apart before the western basin |

**Running tally: six conforming instances (AL92, AL94, AL92-Caribbean-remnant, AL93/Cristobal, AL04/Dolly, AL98) and ONE exception (AL05/Edouard).**

> 🔴 **The 8/27 dossier's "FOUR confirming instances, zero exceptions" line cannot be carried forward unchanged.** There is now an exception. **Whether the tell survives it is AEOLUS's call, not a worker's** — the arguments run both ways and both are recorded here: Edouard remained a **tropical storm**, produced no hurricane, and the season still holds **zero hurricanes**, so a reading in which the tell is about *intensity* survives intact; a reading in which it is about *geography* — systems dying before the western basin — has a clean counterexample. **AL99 is not a new instance yet**; it is a live 70% system with unfavorable conditions forecast for early next week.

⚠️ **The falsifier, both directions, unchanged:** a single **Gulf/FL major landfall** reverses ROL, the C1 score and the pre-registered RNR entry. **A suppressed season is a probability statement, not a guarantee** — 1992 (Andrew, in a quiet season) is the standing reminder, and **Edouard is this season's small live demonstration of exactly that**: a quiet basin still produced a US landfall.

---

## 6. PREDICTIONS — **not resolved here; worker reports value and margin only**

- **AEO-01** — season-end ACE **< 110.3257** AND ≤7 hurricanes, resolves **11/30**.
  **State 9/18: ACE 4.3950 → 105.931 units of headroom below the threshold. Hurricanes: 0 → 7 of 7 remaining.** Season-to-date is **5.96% of the Sep-18 to-date normal** (exclusive convention), **lowest of all 30 years 1991-2020 at this date under both conventions**. Residual-season context: mean remaining after Sep 18 is **47.071**, and **1 of 30 years (1998, 119.905)** accrued the 105.931 required. Bottom-6/8/10 lowest-to-date cohorts all finished **<110.3257 (100%)** — recomputed this run, superseding the 8/21-vintage 50/62/70% figures. **AEOLUS grades AEO-01.**
- **AEO-03** — property-cat reinsurance still soft at the **Jan-2027** renewal (ROL ≤+5% YoY), resolves **1/15/27**. **New indirect evidence, both soft-side:** Moody's 9/16 survey puts Jan-2027 property reinsurance at **−7.5% to −15%** with **86%** expecting declines; the cat-bond insurance risk spread is **−16.8% YoY** with expected loss flat. ⚠️ **Neither is a transacted ROL print.** No renewal instrument resolves before December.

---

## OPEN QUESTIONS / GAPS

1. ✅ **ACE instrument — CLOSED 8/13, RE-VALIDATED 8/21, 8/27 and 9/18.** Runs clean end-to-end; all five storm legs reproduce. **New sub-hazard surfaced this run:** an ACE leg logged for an **ongoing** storm is provisional and nothing marks it so (Dolly 0.3675 → 0.4900). **Propose: any ACE row for a live storm carries `ONGOING - provisional` in `notes`.** AEOLUS's call.
2. 🔴 **NEW — adopt or reject the cat-bond risk-spread instrument (§3).** A verified, machine-readable, monthly-refreshed weekly series back to 2010 that gives C1 a **between-renewals price surface**, which this folder has never had. **Needs: an instrument name, a band, an un-base-rated flag, and an explicit "not ROL" caveat.** Worker cannot create it.
3. 🔴 **NEW — `SOURCES.md` has no loss-leg COMMANDS, only publisher names.** Every loss-leg figure this run came through search or a third-party report page, and the **Swiss Re primary 403'd**. The peril leg has copy-paste commands and the loss leg does not — **the asymmetry is why the loss leg keeps going stale between vintages.** Propose adding the Artemis command above plus a verified Gallagher Re report URL.
4. 🔴 **NEW — `AGENT.md`'s "WHAT TO REPORT" table is 8/13-vintage** and still shows "CSU 9/4/1 HELD 8/5 · ACE 3.09 · AL92 deep-Atlantic" as the reference state. It is a **spawn brief a worker reads before the dossier** — the same class of staleness as open question #1's 8/13-8/21 episode, where the brief instructed against the instrument it was spawning for. Not edited by me (worker limits). AEOLUS's call.
5. ✅ **CSU two-week cadence — held.** Both 9/02 and 9/16 issues found on schedule and read. **The 8/28-9/17 dark window cost nothing on this instrument** because both PDFs remain live at their permanent URLs. Next: **9/30**, then **10/14**.
6. **Denominator reconciliation (NOAA median vs AEOLUS mean)** — still open, unchanged, now with a sharper consequence: NOAA's page *also* carries stale "thus far" observation figures (§2).
7. 🔴 **STORMS.tsv 2026-09-01 row needs a unit correction or caveat.** Its secondary gives *"8 AM CDT advisory 29.3N 93.0W 40 mph"*; the b-deck at that exact position and hour reads **40 KNOTS (~46 mph)**. Position matches to the tenth of a degree, the unit does not. **Not edited by me — a worker does not rewrite an adjudicated row.**
8. **AL99 resolution (next few days).** Does it become TD Six / TS Fiona SW of the Azores and then die in the unfavorable conditions NHC already forecasts for early next week? Either way it is not a Gulf/FL system. Check `bal062026` and the TWO at next spawn.
