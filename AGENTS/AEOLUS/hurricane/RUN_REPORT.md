# AEOLUS · HURRICANE — worker run report

```
run_date:            2026-09-18 (Friday)  ·  data as-of 2026-09-18, pulls 17:52–18:4x UTC
prior run:           2026-08-27 (22-day gap; folder unread 8/28–9/17)
scope discharged:    the three items the 2026-09-11 AEOLUS drain session recorded as OWED —
                     ATCF pull, season ACE recompute, CSU 9/02 two-week read. All three done.
```

---

## observations_added

**9 rows → `workbook/SERIES.tsv`** · **14 rows → `workbook/LOG.tsv`** · **4 rows → `workbook/STORMS.tsv`** · `DOSSIER.md` rewritten, two-clock header advanced 2026-08-27 → 2026-09-18.

No new instrument name was created in `SERIES.tsv`. One new instrument is **proposed** (§proposed_findings P5) and lives only in `LOG.tsv` pending AEOLUS's adjudication.

---

## threshold_state

*Values and margins only. Nothing below is a score, a fire, or a resolution.*

| Instrument | Value | Band / line | Margin | State |
|---|---|---|---|---|
| **ACE vs normal** (peril) | **4.3950** season-to-date, 9/18 | Yellow ≥134.8 · Orange ≥159.4 · Red ≥183.9 + landfall | **130.4 below Yellow** | **NOT-FIRED** |
| **AEO-01 criterion** | **4.3950** | season-end **<110.3257** | **105.931 units of headroom** | open, resolves 11/30 |
| **Hurricane count** | **0** | AEO-01 leg ≤7 | 7 of 7 remaining | open |
| **Major-hurricane count** | **0** | — | — | — |
| **C1 escalation line** — *"NHC lights a GULF/FL system"* | only system in basin is **AL99, SW of the Azores** (~3,500 mi from FL) | needs **GULF/FL** | not a Gulf/FL system | **NOT-FIRED** |
| **Reinsurance ROL** (loss) | **no transacted print** | Yellow +5% · Orange +15% · Red +25% YoY | n/a — instrument only visible at Jan/Jun renewals | **NOT OBSERVABLE** until Jan-2027 |
| Reinsurer cat-loss tally | **$46bn H1'26 = 72% of the $64bn 10-yr avg** (Gallagher Re, Aug vintage) | Yellow ≥110% · Orange ≥130% · Red ≥150% | 38 pts below Yellow | **NOT-FIRED** |

> 🔑 **PERIL AND LOSS ARE DIFFERENT INSTRUMENTS.** The two blocks above are not substitutes and neither speaks for the other.

---

## changes

### 1. Basin state — 9/18 at the NHC primary

- `CurrentStorms.json`: **0 active storms in ALL basins.**
- **TWO, 200 PM EDT Fri Sep 18 2026 (Forecaster Papin) — ONE entry in the whole basin: `AL99`**, eastern subtropical Atlantic, low several hundred mi **SW of the Azores**, **70% / 70%**. Rose intraday 20/30 (8 AM) → 60/60 (Special TWO 10:30 AM) → 70/70 (2 PM).
  **Prose, read per the 8/13 discipline:** *"…followed by a turn to the southwest by early next week, **when environmental conditions are forecast to become less favorable for additional development.**"* A 70% NHC already expects to run out of runway.
- **🔴 GULF/FL: NO. Escalation line NOT FIRED** — reported as state.

### 2. The 9/1 → 9/18 gap, closed at the archive

**Every one of the 48 TWO issuances from 9/01 through 9/12 inclusive carried *"Tropical cyclone formation is not expected during the next 7 days."*** Four a day, all retrieved and read.
**Twelve consecutive days of a completely blank Atlantic formation outlook — and the ~Sep 10 climatological peak sits inside that window.**

| Date(s) | State |
|---|---|
| 9/1 | Edouard landfall; formation line already blank (Gulf text = Edouard's inland remnant as an *Active System*) |
| 9/2 | *"WPC is issuing advisories on Tropical Depression Edouard, located inland over eastern Texas."* Formation line blank |
| 9/3 – 9/12 | **blank on all 40 issuances** |
| 9/13 – 9/18 | **AL98** near-0%/20% → **peak 40%** (9/14-15) → 30% → 10% → **removed by Special TWO 10:30 AM 9/18**, *"development of this system is no longer expected"* |
| 9/17 – 9/18 | **AL99** appears, climbs to 70%/70% |

**No named storm formed between Edouard (8/31) and today** — the ATCF b-deck listing carries only `bal01`–`bal05` plus live invests `bal98`/`bal99`. A primary-source negative, not an inference.

### 3. 🔴 AL05 VERIFIED — the 9/1 "inferred, NOT verified at ATCF" flag is settled

`ftp.nhc.noaa.gov/atcf/btk/bal052026.dat` exists; name field reads **EDOUARD**, genesis-num 014. **Edouard is AL05.**
Full tau=0 track recovered: genesis 2026082818 (20 kt DB, 29.6N 87.3W) → INVEST 8/29-8/31 → **TD FIVE** 2026083112 → **TS EDOUARD** 2026090100 at 35 kt → **PEAK 50 kt / 998 mb at 2026090118, 29.7N 93.6W** → TD 2026090206 → DB 2026090218 → deck ends 2026090306 over east Texas.
**2026090118 is the landfall hour and position** (Johnson Bayou LA ≈29.76N 93.55W; secondary reported 3:20 PM EDT = 1920Z, 60 mph — consistent, 50 kt rounds to 60 mph in NHC advisories). **STORMS.tsv's `0/0 = not recorded` lat/lon is now filled.**

### 4. ACE — recomputed, and the ratio broke to a new floor

**Season-to-date Atlantic ACE 9/18 = 4.3950.**

| Storm | ACE | synoptic pts ≥34 kt |
|---|---:|---:|
| Arthur (AL01) | 0.4050 | 3 |
| Bertha (AL02) | 2.2425 | 12 |
| Cristobal (AL03) | 0.4425 | 3 |
| **Dolly (AL04)** | **0.4900** | 4 |
| **Edouard (AL05)** | **0.8150** | 5 |
| invests AL98 / AL99 | 0.0000 | 0 |
| **TOTAL** | **4.3950** | **27** |

| | value |
|---|---:|
| **to-date normal, Sep 18 — EXCLUSIVE** *(declared convention)* | **73.7248** |
| to-date normal, Sep 18 — inclusive | 75.5129 |
| **2026 as % of to-date normal** | **5.96%** *(excl.)* · 5.82% *(incl.)* |
| prior reads | 12.94% (8/27) · 16.3% (8/21) · 23.3% (8/13) |
| seasonal accrual by Sep 18 | **60.14%** of full-season mean *(vs 21.8% by Aug 27)* |
| full-season normal | mean **122.58** · median **129.25** |
| **hurricanes / majors** | **0 / 0** — season peak intensity **50 kt** |

✅ **Parse re-validated end-to-end:** same computation returns **14.40 mean named storms / 7.20 mean hurricanes** vs NOAA's published 14 / 7, and reproduces Arthur/Bertha/Cristobal exactly.

**🔴 2026 is now lower than every one of the 30 years 1991-2020 at this calendar date.** Previous low: **1994 at 11.2500** — 2026 sits at **39% of the lowest year in the normals period**. **The 8/27 convention-sensitivity caveat no longer bites:** 1st-lowest of 30 under *both* conventions.

⚠️ **Read the mechanism, not the sign.** The ratio fell 12.94% → 5.96% across a period that contained **a landfalling tropical storm.** The to-date normal went 26.72 → 73.7248 in 22 days while 2026 added 0.9375. **That move is almost entirely the calendar.**

### 5. Seasonal outlooks — seasonal legs unchanged; **two missed two-week issues recovered**

- **CSU seasonal: UNCHANGED** — 9 / 4 / 1, ACE **50**, ACE-W-of-60W 25. 8/5 remains the final seasonal issuance; page schedule lists Nov 2026 Verification next.
- **NOAA CPC: UNCHANGED** — page still carries the **6 August 2026** issuance, 7-13 / 2-6 / 0-2, **75%** below-normal. NOAA's cadence is May initial + early-August update only; **no September product exists.**
- **CSU two-week — both missed issues read:**

| Issued | Window | Below-normal tercile | Forecast | **Observed ACE in window** |
|---|---|---|---|---:|
| 8/05 | Aug 5-18 | `<2` | below-normal 80% | 0.4425 |
| 8/19 | Aug 19-Sep 1 | `<7` | below-normal 70% | 1.1450 |
| **9/02** | **Sep 2-15** | `<11` | **below-normal 97%** · near 3% · above ~0% | **0.1600** |
| **9/16** | **Sep 16-29** | `<11` | **below-normal 78%** · near 20% · above 2% | **0.0000** *(open to 9/29)* |

**9/02 is the highest below-normal confidence of the 2026 series (80 → 70 → 97 → 78)** — issued *for the fortnight containing the climatological peak*, which closed with a single qualifying synoptic time in it.
Verbatim 9/02: *"Global model signals for TC development in the next two weeks are **remarkably weak**, given the next two weeks include the **climatological peak of the season**."*
Verbatim 9/16: *"the base state across the Atlantic is quite TC-unfavorable, given the **strong El Niño and associated high levels of vertical wind shear**."*
⚠️ **Tercile boundaries differ per window — never compare the "below-normal" LABEL across windows.** Observed values are measurement; **AEOLUS decides whether a window verified.**
**Next issues: 9/30, then 10/14.**

### 6. Loss leg — no newer market tally, but three genuinely new items

| Instrument | Value | Vintage |
|---|---|---|
| **Gallagher Re** H1'26 insured nat-cat | **$46bn, 28% below the $64bn 10-yr avg**; lowest H1 since 2018; 5th straight quarter with no single insured loss >$10bn; 11 events >$1bn vs 10-yr avg 16; economic $142bn (−10%) | **Aug 2026** *(same vintage AEOLUS holds)* |
| **Swiss Re Institute** H1'26 insured nat-cat | **$42bn vs a $66bn long-term trend** | **Aug 2026** — **NEW second independent read**; ⚠️ secondary-sourced, primary 403'd |
| **Moody's** Jan-2027 property reinsurance survey | **most likely −7.5% to −15%**; **86%** expect declines (vs 74% for 2026); some >15% on portfolio-wide placements | **2026-09-16** |
| **Swiss Re** Florida scenario | Cat-5 Miami/Tampa **$300bn+** · 1926 Miami repeat **$200bn+** · Andrew repeat **~$100bn** | **2026-09-16** — ⚠️ **MODELLED SCENARIO, NOT A TALLY** |

⚠️ **Do NOT reconcile $46bn and $42bn.** Different publishers, perimeters and denominators (10-yr average vs long-term trend). Carry both, labelled.
⚠️ **Moody's is a survey of expectations, not a transacted ROL.** It does not satisfy the ROL threshold row.
**Gallagher Re's Q3 report lands ~October — that is the next real loss vintage.**

### 7. 🔴 The peril↔loss *relationship* changed

At 8/13 and 8/27 the two legs pointed **opposite** ways (basin active, market soft). **They now point the same way:** a basin at **6% of its to-date normal**, and a reinsurance market whose sell-side survey expects **another 7.5-15% off in January**. **That change in the relationship is itself the C1 read — AEOLUS scores it.**

---

## proposed_findings

*All PROPOSALS. AEOLUS adjudicates; nothing here is a score, a fire or a resolution.*

**P1 — 2026 Atlantic ACE has fallen below the entire 1991-2020 distribution at this calendar date.**
4.3950 on Sep 18 vs a to-date normal of 73.7248 = **5.96%**; previous 30-year low at this date was **1994 at 11.2500**. Zero hurricanes, zero majors, season peak intensity 50 kt, 17 weeks in. **Source:** NHC ATCF b-decks + HURDAT2, computed by the `SOURCES.md` method, parse re-validated (14.40/7.20 vs NOAA's 14/7). **Candidate KB row.**

**P2 — The climatological peak passed with a completely blank formation outlook for twelve consecutive days.**
All 48 TWO issuances 9/01–9/12 carried *"Tropical cyclone formation is not expected during the next 7 days."* **This is the observable AEOLUS was dark for, and it is a stronger signal than the ACE number** — ACE can be depressed by weak storms, but a blank *outlook* across the peak means NHC saw nothing worth assigning a percentage to for twelve days. **Source:** IEM AFOS archive (all 48 products retrieved); current day verified at the NHC primary. **Candidate KB row.**

**P3 — 🔴 The peak-season tell has its first non-conforming instance, and the 8/27 "four-for-four, zero exceptions" line cannot be carried forward.**
Resolved this run: **Dolly CONFORMED** (degenerated to a remnant low after 2026082806, deck ends 2026083112 at 20.0N 70.6W near Hispaniola; NHC's shear/dry-air forecast verified directionally). **AL98 CONFORMED** (peaked 40%, died, *"no longer expected"*, removed by Special TWO). **But AL05/Edouard DID NOT** — formed in the Gulf 8/31, reached 50 kt, made landfall at Johnson Bayou LA 9/1.
**Tally: six conforming, one exception.** **Both readings are recorded and neither is adjudicated here:** if the tell is about *intensity*, it survives intact (Edouard stayed a TS; the season still holds zero hurricanes); if it is about *geography* — systems dying before the western basin — it has a clean counterexample. **AEOLUS's call.**
**Second-order:** Edouard is this season's small live demonstration of the standing 1992/Andrew caveat — **a quiet basin still produced a US landfall.**

**P4 — Peril and loss now point the same direction for the first time in this folder's record.** See §changes 7. **Candidate KB row** — the *divergence* was a logged finding, so its ending is one too.

**P5 — 🔴 HIGHEST-VALUE: a mid-cycle reinsurance-price surface exists and is machine-readable. PROPOSED NEW INSTRUMENT — worker cannot create it.**
AEOLUS's standing complaint is that ROL is visible only at Jan/Jun renewals, leaving a landfall between them with no price surface. **The Artemis "Catastrophe Bond Market Yield" page embeds its full Highcharts series inline in the page HTML — no JS execution required.** **827 weekly points, 2010-10-08 → 2026-08-28.** Series: *Insurance Risk Spread*, *Collateral Yield* (3m T-Bills), *Expected Loss*. Data collated by **Plenum Investments AG**.

```bash
curl -s -A "Mozilla/5.0" -L "https://www.artemis.bm/catastrophe-bond-market-yield/"
# then regex the  categories:[...]  array and each   name:'X' ... data:[...]   block
```

| | 2025-08-29 | 2026-01-09 | 2026-07-10 | **2026-08-28 (latest)** |
|---|---:|---:|---:|---:|
| Insurance risk spread | 6.07% | 5.29% | 5.75% | **5.05%** |
| Expected loss | 2.24% | 2.35% | 2.50% | **2.50%** |
| **spread / EL** | 2.71x | 2.25x | 2.30x | **2.02x** |
| Collateral yield | 4.15% | — | 3.79% | **3.81%** |

**−16.8% YoY. −12.2% across peak season (7/10 → 8/28) with expected loss FLAT at 2.50 — a pure price move, not a risk-mix move.** YTD −4.5%.

> ⚠️ **TWO HARD CAVEATS, both load-bearing:**
> **① STALE BY DESIGN** — the page refreshes **monthly**, so the newest point is **2026-08-28, three weeks behind today**. **A landfall would not show for up to a month.** It is a between-renewals surface, not a daily one.
> **② IT IS NOT RATE-ON-LINE** — a cat-bond insurance risk spread and a reinsurance ROL are different instruments on different perimeters. Correlated, not interchangeable. **It must NOT be entered against the ROL threshold row.** If adopted it needs its own instrument name, its own band, and an explicit un-base-rated flag.

**P6 — An ACE leg logged for an *ongoing* storm is provisional by construction, and nothing marks it so.**
Dolly was recorded at **0.3675** on 8/27 while still active; the completed b-deck gives **0.4900** (gained 2026082806 at 35 kt). The 8/27 row said "ONGOING" in prose but the **value** carried no provisional flag. **Propose: any ACE row for a live storm carries `ONGOING - provisional` in `notes`.** Small, mechanical, and it is the same class as the stale-to-date-normal hazard this folder already guards.

**P7 — The lowest-to-date base rate moved hard between Aug 21 and Sep 18, and the direction is informative.**

| Slice | at Aug 21 *(carried in the 8/27 dossier)* | **at Sep 18** |
|---|---:|---:|
| bottom-6 | 3/6 = 50% | **6/6 = 100%** |
| bottom-8 | 5/8 = 62% | **8/8 = 100%** |
| bottom-10 | 7/10 = 70% | **10/10 = 100%** |

Unconditional, all 30 years: **13/30 = 43%.** **Why it moved:** the late-August cohorts still contained seasons quiet through August that then exploded in September (1998, 1999); **by Sep 18 the September explosion has either happened or it has not.** n is still small. **This is precisely why a base rate's DATE is load-bearing — the 8/27 dossier carried an Aug-21 vintage table forward unrecomputed, and it was wrong by 50 points.**

**P8 — Residual-season context, reported as measurement and deliberately NOT converted to a probability.**
ACE accruing **after Sep 18**, 1991-2020: mean **47.071**, median **47.189**, **max 119.905 (1998)**, min 2.242 (1997); median per-year share of season remaining **34.84%**.
**AEO-01 requires 105.931 further units from 4.3950. Exactly ONE of the 30 years — 1998, at 119.905 — accrued that much after September 18.** **1998 is AEOLUS's own standing counter-analogue**, which is a reason to state the number precisely rather than round it into a verdict. **AEOLUS grades AEO-01.**

**P9 — AEO-03 indirect evidence, both soft-side, neither a resolving instrument.**
Moody's 9/16: Jan-2027 property reinsurance **−7.5% to −15%**, **86%** expecting declines. Cat-bond insurance risk spread **−16.8% YoY** with expected loss flat. **Neither is a transacted ROL print; no renewal instrument resolves before December.**

---

## gaps

*Required output. A reported failure beats a worked-around one.*

**1. 🔴 Swiss Re primary — HTTP 403, two independent attempts.**
```
WebFetch https://www.swissre.com/institute/research/topics-and-risk-dialogues/climate-and-natural-catastrophe-risk/first-half-2026-insured-catastrophe-losses.html
  -> "The server returned HTTP 403 Forbidden."
curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" -L <same URL>
  -> HTTP 403, 5984 bytes
```
**Consequence: the Swiss Re H1 2026 figure of $42bn vs a $66bn trend is SECONDARY-SOURCED ONLY and unverified at the issuer.** Labelled as such everywhere it appears. **Not substituted, not silently upgraded.**

**2. Gallagher Re's own site returns a JS shell with no content.**
```
curl -s -A "Mozilla/5.0" "https://www.ajg.com/gallagherre/news-and-insights/"  -> HTTP 200, 212 bytes
```
The H1'26 figures were taken from Artemis / Reinsurance News reporting of the Gallagher Re report, **not from Gallagher Re directly.** Same vintage AEOLUS already holds, so nothing new rests on it — but the loss leg has **no verified primary command** and that is open question #3 below.

**3. Plenum's own index pages — HTTP 404 (my URL guesses, not `SOURCES.md` entries; no instrument lost).**
```
https://www.plenum.ch/en/plenum-cat-bond-indices/  -> 404
https://www.plenum.ch/en/cat-bond-indices/         -> 404
https://www.artemis.bm/dashboard/cat-bond-ils-index/ -> 404
```
The Plenum-collated data was reached through the Artemis page instead, which **is** the verified route (P5).

**4. 🔴 `SOURCES.md` has no loss-leg COMMANDS — only publisher names.**
The peril leg has copy-paste commands; the loss leg has a table of four publisher names and a caveat. **Every loss-leg figure this run was reached by search rather than by a verified command, and the one primary I tried 403'd.** **That asymmetry is a structural reason the loss leg keeps going stale between vintages** — a worker cannot execute a publisher name. Proposed additions: the Artemis command in P5, plus a verified Gallagher Re report URL. **AEOLUS owns `SOURCES.md`.**

**5. No ENSO index value pulled.** Correct under the SHARED-INPUT RULE — ENSO is `regime/`'s instrument. **Flagging it because the 8/27 dossier's NOAA July ENSO probabilities (90% strong, 48% very strong) are now ~10 weeks old and must not be quoted from this folder as current.** Reconcile at `regime/`.

**6. Not attempted, out of scope:** the Spokane wildfire loss figures named in the spawn brief are `../wildfire/`'s instrument, not mine.

---

## ⚠️ CONTRADICTS `DOSSIER.md` — flagged, not silently overwritten

| # | Prior state | This run | Handling |
|---|---|---|---|
| 1 | §5 *"FOUR confirming instances, **zero exceptions**"* | **One exception: AL05/Edouard** (Gulf landfall, 50 kt, did not shear out) | §5 rewritten to six-and-one with **both readings stated and neither adjudicated**. **P3.** |
| 2 | §1b Dolly ACE **0.3675** | **0.4900** — completed deck adds 2026082806 | Appended as a **revision**, original preserved. **P6.** |
| 3 | STORMS.tsv 9/1: *"AL05 (inferred from name order; **NOT verified at ATCF**)"* | **VERIFIED** — `bal052026.dat`, name field `EDOUARD`, genesis-num 014 | New row supersedes; old row left intact |
| 4 | STORMS.tsv 9/1 lat/lon **`0/0` = not recorded** | **29.7N 93.6W** at 50 kt, 2026090118 | New row carries it |
| 5 | STORMS.tsv 9/1 secondary: *"8 AM CDT advisory 29.3N 93.0W **40 mph**"* | b-deck at that **exact position and hour** reads **40 KNOTS (≈46 mph)** | 🔴 **Unit discrepancy in the secondary. NOT edited — a worker does not rewrite an adjudicated row.** AEOLUS's call. |
| 6 | §1b base rate **bottom-6 = 50%** (Aug-21 vintage, explicitly "NOT re-run") | **bottom-6 = 100%** at Sep 18 | Recomputed like-for-like; both vintages shown side by side. **P7.** |
| 7 | §0 headline: *"the 14-day silence ended (Dolly, 8/27)"* | superseded — twelve blank days across the peak, and a landfall | §0 rewritten, prior headline referenced as superseded |
| 8 | §3 *"loss leg NOT re-pulled this run"* | re-pulled; **no newer market tally**, but a second H1 read + two new 9/16 items | §3 rewritten with a vintage column |

**Also stale, not mine to edit:** `AGENT.md`'s "WHAT TO REPORT" table is **8/13 vintage** — it still shows *"CSU 9/4/1 HELD 8/5 · ACE 3.09 · AL92 deep-Atlantic"* as the reference state. **It is the spawn brief a worker reads BEFORE the dossier** — the same class as open question #1's 8/13-8/21 episode, where the brief instructed against the very instrument it was spawning for. **AEOLUS's call.**
