# AEOLUS · WILDFIRE — live dossier

**As-of: 2026-10-09.** Consolidated from KB-AEO-030/031/032/037/056 + the 2026-08-21, 2026-08-27, 2026-09-18, 2026-09-28 and 2026-10-09 worker runs. **§1–§6 below are the 9/18 body. The 10/09 block directly beneath supersedes its peril figures AND its §5 AEO-09 grading inputs. The 9/28 block is kept for the delta.**

> **Last real data refresh: 2026-10-09**  ·  **Dossier written: 2026-10-09**
> *Two-clock header (PAT-044) — `scripts/ledger_staleness.py` reads the first line. **The data date, not the edit date**: a hygiene edit must NOT bump it.*
> **Observations → `wildfire/workbook/SERIES.tsv`** · findings → central `workbook/KB.tsv` · synthesis → `STATUS.md`. **Flow is one-way.**
> **Feeds:** C4
> ⚠️ **PERIL figures are 2026-10-09 (NFN report and statistics page, same day, agree on every field). Outlook = the 2026-10-01 issue. LOSS figures are still H1 2026, a period that ENDED 2026-06-30, before Spokane and before the whole August peak. That leg is ~3.3 months stale and is labelled so on every line.**
**C4 score: worker does not score. Last AEOLUS-set score was 3 🟠 ↗ (8/13); the 8/21, 8/27, 9/18, 9/28 and 10/09 refreshes are un-adjudicated.**

---

## 🆕 2026-10-09 WORKER REFRESH — supersedes the §1 peril figures and the §5 AEO-09 inputs

| Instrument | Value | As-of / surface | Δ vs 9/28 |
|---|---|---|---|
| **Preparedness Level** | **2 of 5**, *"as of September 22, 2026 at 7:30 a.m. MDT"* | NFN report dated 10/09 | unchanged; PL2 for 18 days inclusive |
| **PL step history** *(new)* | **5 → 4 on 9/4**, → 3 on 9/9, → 2 on 9/22 | 10/01 outlook Exec Summary | 🔴 **PL5 ran 7/18→9/4 = 49 days inclusive, NOT 54.** The 54 figure assumed PL5 held until the 9/9 PL3 banner. §1/§3/§4 corrected below |
| **Acres YTD** | **9,013,486** = **145%** | NFN + statistics, 10/09 | **+450,199** vs statistics 9/28. ⚠️ **A step, not burning.** The outlook gives **8,604,892 (141%) as of 9/30**, so **~409k acres arrived after 9/30**, at PL2. Cause not stated anywhere (LOG 10/09) |
| **Fires YTD** | **63,681** = **134%** | NFN + statistics, 10/09 | +6,342 vs 9/28. Most of it is already in the outlook's 9/30 figure (**62,369, 134%**) |
| **10-yr avg YTD (2016–2025)** | **47,686 fires · 6,204,304 ac**. The fields RENDER and **reproduce the narrative**: 145.28% / 133.54% | NFN 10/09 | open question #6 closed **for this read** (intermittent: rendered 9/18, blank 9/25) |
| **Large fires** | **8**. Narrative, NFN table and statistics "Being Suppressed" **all agree** | 10/09 | 9/25–9/28: 26 / 4 / 17 (P11 basis break). One-day agreement, not a fix |
| **Personnel** | **3,123** (both surfaces) | 10/09 | 5,697 (9/28) |
| Acres on active/large fires | 933,036 (NFN "all active" = statistics "on Large Fires") | 10/09 | fields differed by definition on 9/18; equal today |

⚠️ **ACREAGE, NOT LOSS.** 145% is an acreage percentage. The cat-loss band still reads ~72% on H1 2026. **No Q3 2026 aggregate tally appears on the Artemis homepage as of 10/09**; its only Q3 item is cat-bond *issuance*, which is not a loss figure.

### AEO-09 grading inputs — October issue (issued 2026-10-01, next 2026-11-02). NOT GRADED.

Rule handed down (**KB-AEO-128**): the CURRENT-MONTH panel is the designation; where map and regional narrative disagree, the regional section governs; any-part counts; a hedge is not a designation; out-months are forecasts.

| Panel | Southern Area section (governing) | Exec Summary | Map | TX | OK |
|---|---|---|---|---|---|
| **OCTOBER (current month)** | *"For October, above normal significant fire potential is most likely across western north Texas into western Oklahoma, in addition to east Texas and the Lower Mississippi Valley."* | *"October significant fire potential will remain above normal in portions of north Texas and western Oklahoma. Above normal potential is also forecast for much of east Texas into the Lower Mississippi Valley…"* | OK red in the western main body only (Panhandle + central/east white). TX red in two blocks: western north TX below the Red River, and east TX. The rest of TX is white | **NAMED, partial** | **NAMED, partial** |
| November | *"…expected from eastern Oklahoma into northeast Texas, Arkansas, north Mississippi, west and middle Tennessee, and Kentucky."* | agrees | E OK + NE TX red | above (NE) | above (E) |
| December | *"…will trend towards normal, though below normal significant fire potential is possible in some of the areas that can see dormant season fires in the Plains…"* | CONUS normal | CONUS normal | normal | normal |
| January | (same sentence) | *"Normal significant fire potential is forecast across the country for January."* | all normal | normal | normal |

✅ **No map/text disagreement in the October panel.** Map, Exec Summary and regional section all put TX and OK above-normal, both partial. ⚠️ The regional sentence says *"most likely"*. The map and the Exec Summary carry no hedge. **Whether "most likely" is a hedge under KB-AEO-128 rule (2) is AEOLUS's call.**
⚠️ **The geography moved since 9/01.** September red covered all of OK and the central/eastern two-thirds of TX. October red covers **western OK and two separate TX blocks**. **The TX Panhandle is white in October** even though the outlook still lists it among the extreme-to-exceptional drought areas.
**Mechanism text, verbatim:** *"Cool season grasses are likely to green up where the heaviest rain occurs in Texas and Oklahoma, mitigating fire activity until hard freezes occur later this winter."* · *"Drought relief will not be as widespread as needed to fully squash fire activity in the western two-thirds of the geographic area."*
**ENSO (cited, `regime/` owns it):** *"Central Tropical Pacific sea surface temperature anomalies are more than 2 C above average, the threshold for a very strong El Niño."*
⚠️ **Map method:** `pdfimages` is not installed (rc=127). Panels were read from a **pypdfium2** render of the same PDF. Sub-state boundaries are a visual read and are approximate.

**Other October above-normal areas:** Great Basin **Sierra Front + adjacent Lahontan Basin** (⚠️ in the regional section and on the map, **but missing from the Exec Summary list**) · Eastern Area **NE Minnesota, N Wisconsin, W Upper Michigan (PSAs EA03/EA04)** · Southern Area **east TX into the Lower Mississippi Valley** · **Puerto Rico, USVI**.

**New incidents since 9/28 (InciWeb set only):** Bouquet CA (10/03, 1,048 ac, Level-3 evacuation order) · Danny CA (10/08, 150 ac, evacuation order + warnings) · Bull NV (10/02, 1,529 ac, warnings lifted). **None publishes a structure-loss figure.** **No TX/OK incident appears on InciWeb at all.** The Hydra page now serves an empty template.

---

## 🆕 2026-09-28 WORKER REFRESH — supersedes the §1 peril figures (AEOLUS dark 9/18→9/28)

| Instrument | Value | As-of / surface | Δ vs 9/18 |
|---|---|---|---|
| **Preparedness Level** | **2 of 5** — *"as of September 22, 2026 at 7:30 a.m. MDT"* | NFN banner, fetched 9/28 | 🔽 **3 → 2 on 9/22.** PL3 held 9/9→9/22 (14 days inclusive). Only change observable in the window; NFN shows current level only |
| **Acres YTD** | **8,559,888** = **145%** *(narrative)* | NFN report 9/25 | +36,675 ac · 146% → 145% |
| Acres YTD | **8,563,287** | statistics page, 9/28 07:55 | +3,399 vs 9/25 |
| **Fires YTD** | **57,087** = **125%** | NFN 9/25 | +798 · 126% → 125% |
| Fires YTD | **57,339** | statistics page 9/28 | +252 vs 9/25 |
| **Large fires** | 🔴 **three numbers:** narrative **26** (9/25) · NFN table field **4** (9/25) · statistics "being suppressed" **17** (9/28) | — | 9/18: 50. **Basis break — see LOG 9/25** |
| **Personnel** | **6,824** (NFN 9/25) · **5,697** (statistics 9/28) | — | 9/18: 12,315 |

⚠️ **ACREAGE, NOT LOSS.** 145% is an acreage percentage; the cat-loss band still reads ~72% on H1 2026.
⚠️ **The 10-yr-average fields are BLANK again (9/25) and the narrative 145% does NOT reproduce:** the mean of the ten listed year rows gives **142.67%** (fires 124.47% vs narrative 125%). Open question #6 is **re-opened** — the 9/18 closure held for 9/18 only.
⚠️ **NFN now states "This report is currently updated on Fridays"** — a weekly surface; the statistics page (IMSR-sourced) updates daily.
**New incidents in the window:** southern-Plains fires small and contained-trending — Rafter 4B TX (9/26, 2,125 ac, "pipeline and structures were threatened"), Grover Bend TX (9/26, 321 ac), Seven Oaks TX (9/27, 250 ac), Stone Bridge OK (130 ac). **Hydra Fire, Meridian TX (origin 9/14, 933 ac)** evacuated the city of Meridian; InciWeb 9/23: *"Structures lost: Undetermined at this time"*. **No new large incident with a published structures-destroyed count found.**
**Outlook:** still the **9/01 issue** (Last-Modified 2026-09-01 18:29:32 GMT); October issue due 10/01. §5 grading inputs unchanged.
**Loss leg:** no new tally; Cotality Spokane $1.0–1.3B unchanged (page last updated 8/24). Swiss Re H1 2026 **$42bn** (Artemis 8/11) added as a fourth H1 issuer figure.
**Drought (cited from `../water/workbook/SERIES.tsv`, not pulled):** CONUS D1–D4 **59.37%**, mapDate **2026-09-15**.

---

## 🔴 TWO CORRECTIONS THIS RUN — read before using any prior figure

**① This dossier was carrying a superseded acreage percentage in two places.** §3 and §4 read **"171% of average acreage"** as the live figure. 171% was the **8/21** value; it was superseded by **164% on 8/27** and the §1 table was updated while §3 and §4 were not. Anyone reading the summary sections got a figure two vintages old. **It is now 146%.** *(`finding_summary_section_merges_what_the_body_separates` — the abstract is where a correction lands last.)*

**② The 8/27 claim that the Gallagher Re estimate "remains the only insured-loss figure for this event" was already false when written.** **Cotality issued a $1B–$1.3B preliminary insured-loss estimate for the three Spokane fires on 2026-08-18** — nine days earlier. The 8/27 check was **scoped to Artemis.bm** but its conclusion was **stated at world scope**. A negative is a claim about the set you searched. *(`finding_scan_keyed_on_naming_reads_local_form_as_absence`.)*

---

## 1. PERIL LEG — 🔽 COOLING ON EVERY FIELD EXCEPT ABSOLUTE ACRES

| Instrument | Value | As-of | Δ vs 8/27 | Read |
|---|---|---|---|---|
| **NIFC Preparedness Level** | **3 of 5** — *"as of September 9, 2026 at 7:30 a.m. MDT"* | 9/18 | 🔽 **5 → 4 → 3** | **The PL5 run ENDED 9/4 after 49 days inclusive (48 elapsed), 7/18→9/4**, then PL4 9/4→9/9. *(Corrected 10/09. This row said "ended 9/9 after 54 days". The step dates come from the 10/01 outlook Exec Summary; history in `workbook/LOG.tsv` 2026-09-04.)* At PL3 for 10 days inclusive as of 9/18. |
| **Acres YTD** | **8,523,213** = **146%** of 10-yr avg | 9/18 | **+551,814 ac · 164% → 146%** | ⚠️ **ACREAGE. Not a loss figure.** **Third consecutive read where the pct FELL while absolute acres ROSE.** Denominator effect, now *measured* rather than derived — see the row below. |
| **Fires YTD** | **56,289** = **126%** of 10-yr avg | 9/18 | +4,855 · 127% → 126% | same denominator effect |
| **Uncontained large fires** | **50** | 9/18 | 🔽 **−44 (from 94)** | 2 new large fires, 6 contained |
| **Personnel assigned** | **12,315** | 9/18 | 🔽 **−9,539** (from 21,854) | ⚠️ NFN narrative says *"over 12,000"*; the **statistics page gives the exact 12,315**. Two NIFC surfaces, same quantity, different precision — cite the exact one. |
| **Sept potential outlook** | above-normal: most of NW, far N California, C+S Idaho, N Nevada, N Utah, **southern Plains into Lower Mississippi Valley**, S Florida, N Minnesota, N Wisconsin, W Upper Michigan, PR/USVI | **issued 9/01** | ⬆️ **ISSUED — the 9/01 checkpoint is live.** Next issuance 10/01 | full AEO-09 grading inputs in §5 |
| **Drought (CONUS D1–D4)** | **cite `../water/workbook/SERIES.tsv`: 56.61%, valid 8/25** — not copied here | 8/25 | — | ⚠️ **water/'s own USDM series has not refreshed since 8/25 — 24 days.** Stale at the owner, not here. |

### 🔑 GAP CLOSED — the 10-yr-average fields now render, and the narrative pcts reproduce exactly

The **10-year-average YTD fields, BLANK in served HTML on 8/21 and 8/27**, render this run. **Published 10-yr avg YTD (2016–2025): 44,745 fires · 5,823,577 acres.**

- `8,523,213 / 5,823,577 = 146.36%` → NIFC's stated **146%** ✅
- `56,289 / 44,745 = 125.80%` → NIFC's stated **126%** ✅

**Both narrative percentages reproduce from the published averages.** The derived-vs-published gap (standing open question #6 since 8/21) is **CLOSED**, and the denominator effect is now measured, not inferred: the comparator grew from an implied ~4,860,609 ac (8/27) to a published **5,823,577 ac** (9/18) — **+962,968 acres of denominator in 22 days**, against +551,814 acres of numerator. **The percentage fell because the season's comparator is accreting faster than this year's fires. It is not a deceleration signal on its own.**

**Geographic spread (9/18) — the southern Plains have arrived:** WA 9 · **TX 6** · OR 6 · ID 6 · CA 5 · MT 5 · **OK 4** · CO 4 · NM 2 · UT 1 · WY 1 · AR 1. **TX + OK now carry 10 of the 50 large fires** — a shift absent on 8/27, when OR/WA/MT led and the Southern Area had no entry. This is the flash drought converting to fire, and it is **directly load-bearing on AEO-09** (§5).

⚠️ **Two NIFC active-acreage fields differ by definition — do not conflate:** NFN *"Acres from all active fires"* = **1,292,408**; statistics page *"Acres Burned on Large Fires"* = **2,523,653**. Statistics page *"Last Updated: Friday, September 18, 2026 - 08:37"*.

---

## 2. INSURED-LOSS LEG — 🔴 STILL IMMOBILE, and the vintage is now the problem

**Aggregate (the RED-band instrument) — NO NEW PUBLICATION. Unchanged since 8/13.**

| Instrument | Value | As-of | Vintage age |
|---|---|---|---|
| **H1 2026 global insured nat-cat** | **$46bn** (Gallagher Re) · **$44bn** (Munich Re) · **"at least $47bn"** (Aon) — **28% BELOW** the 10-yr avg, **lowest H1 since 2018** | **H1 2026** | **~2.5 months** |
| **H1 2026 US insured nat-cat** | **~$36B** (US ~75% of global), 11 US billion-dollar insured events | **H1 2026** | ~2.5 months |
| Reinsurance ROL (July renewal) | **soft** — global cat −16%, NA −20/25%; capital at a record **>$700–790B** | Jul 2026 | ~2.5 months |

🔴 **The vintage is the finding.** H1 2026 covers a period that **ended 2026-06-30 — before the Spokane Complex, before the entire August peak, before the PL5 run's second half.** The loss leg is not saying "losses are low despite the fires"; it is saying **nothing at all about the fires**, because the measurement window closed before they happened. Next vintages: **Q3 broker reports ~Oct 2026; full-year ~Jan 2027.** Checked 9/18 — no Q3 or post-H1 tally from Gallagher Re, Munich Re, Aon or Swiss Re.

⚠️ **NOT a 2026 tally:** Verisk (2026-09-01) put the global **modelled average annual loss** at **$171bn**. That is a forward AAL. **Never compare it to the $46bn.**

### Spokane single-event insured loss — a SECOND estimate exists, and it is higher

| Vintage | Estimate | Issuing authority | Note |
|---|---|---|---|
| **2026-08-06** | *"minimally reach into the hundreds of millions (USD); with a plausible chance and likelihood of this becoming a billion-dollar event"* | **Gallagher Re** (via Artemis) | on record since 8/21 |
| 🔴 **2026-08-18** | **"$1 billion to $1.3 billion in insured losses from the three Spokane fires"** | **Cotality** (Hazard HQ) | ⚠️ **MISSED by the 8/27 run.** **Cotality is NOT in `SOURCES.md`** — reported as a **PROPOSAL**; admitting the source is AEOLUS's call. |

- **AM Best (8/6, unchanged):** *"the losses do not appear to be in the same order of magnitude as the 2025 California wildfires and likely will have minimal impact on the current softening prices in the reinsurance market; however, there could be a reassessment in localized areas."* Flags a **WA FAIR Plan assessment path**; WA-exposed cat-bond sponsors State Farm, Allstate, USAA, Travelers — aggregate-layer retention erosion possible, per-occurrence unlikely at current damage levels.
- ⚠️ **$21B is EXPOSURE, never a loss.** Cotality: *"there are over 50,000 properties carrying a moderate or greater wildfire risk in the Spokane metropolitan area. Those properties have a combined Reconstruction Cost Value (RCV) of over $21 billion."*

### 🔴 Structure count — now THREE irreconcilable objects. DO NOT MERGE OR AVERAGE.

| Figure | Object | Issuing authority | As-of |
|---|---|---|---|
| **">700 homes"** | destroyed | Gallagher Re (via Artemis) | 8/6 |
| **"over 800 structures"** | burned | **NIFC** (monthly outlook) | **9/01** |
| **"5,256 properties damaged"**, of which **"226 … major damage or destroyed, including 42 classified as destroyed"** | aerial-imagery classification | **Cotality** | 8/24 |

**Cotality reports 42 destroyed against Gallagher Re's 700+ and NIFC's 800+ — a factor of ~17–19.** The worker does **not** reconcile these: different objects (homes / structures / properties), different methods (ground-EOC vs aerial imagery), possibly different perimeters. **The discrepancy IS the finding.** Note the direction, because it is counter-intuitive: **Cotality is the LOW outlier on destroyed structures yet carries the HIGHEST loss estimate** — so the loss estimate is not a simple function of its own destroyed-count. ❌ **Still no WA state EOC FINAL tally** — third consecutive run.

---

## 3. 🔑 THE DIVERGENCE — the peril leg is now falling toward the loss leg

**Acreage percentage: 155% (8/13) → 171% (8/21) → 164% (8/27) → 146% (9/18) → 145% (9/25) → 141% (9/30, outlook) → 145% (10/09, after a ~409k-acre step). PL 5 → 4 (9/4) → 3 (9/9) → 2 (9/22). Large fires 101 → 76 → 94 → 50 → 26/4/17 (three surfaces, 9/25–9/28) → 8 (10/09, all surfaces agree). Personnel 24,265 → 21,854 → 12,315 → 6,824 (9/25) → 5,697 (9/28) → 3,123 (10/09).** The loss leg has not moved at all — **it is still the same H1 print it was on 8/13.**

**So the gap is closing, but read WHY before reading it as convergence:**
- the **acreage percentage** is falling largely because the **denominator is accreting** (§1) — absolute acres are still rising;
- the **loss leg** is not falling *or* rising, it is **stale by construction** — its window closed 6/30.

⚠️ **The two legs are not converging on evidence; one is decaying and the other is frozen.** A genuine convergence read has to wait for the **Q3 tally (~Oct)**, which will be the first loss vintage that contains any of this season's fires.

**The down-stack migration claim is unchanged:** reinsurance stays soft on record capital, so stress lands on primary carriers, **state residual pools** (CA FAIR Plan **+29.1%** and its first **$1B** assessment in 30 years; **WA FAIR Plan flagged by AM Best as a live assessment path**), and property-exposed munis. ⚠️ **REGINALD's standing counter, carried honestly:** the *softening* leg is the better-evidenced one; down-stack migration is the load-bearing claim and is **not yet independently confirmed**. ZION remains the one weak name on the CA-muni-conduit side (monitor-only).

---

## 4. WHAT WOULD ACTUALLY MOVE C4 — margins, not grades

| | Condition | Value | Margin |
|---|---|---|---|
| **Upgrade 3 → 4** | carrier **insolvency** OR a single **>$10B** insured cat | Spokane: **$1–1.3B** (Cotality 8/18, source not yet admitted) / *"hundreds of millions … plausibly $1B"* (Gallagher Re 8/6) | **~$8.7–9B short — still roughly an order of magnitude below the trigger.** No insolvency reported. *(The higher estimate narrows the gap; it does not change the order of magnitude.)* |
| **RED band** | reinsurer cat tally **≥150%** of 10-yr avg | ~**72%** (H1 2026, 28% below avg) | **~78 pts below RED, below even Yellow (110%)** — and **measured on a window that closed 6/30**, so it is not yet evidence about this fire season either way. |
| **Channel-kill** | H1 cat <110% of avg **AND** non-renewals stable 2+ quarters | loss leg ~72% (satisfies); non-renewal leg: **a 2024-vintage annual series now exists — but see §6, it still cannot answer a quarterly question** | conjunction **unsatisfied** on the second leg |

🔴 **145% (9/25; 146% on 9/18) is an ACREAGE percentage. The RED band is a CAT-LOSS percentage at ~72%.** Different rows of the threshold table, different units. **Anyone reading "PL5 for 49 days, 9.0M acres, most destructive fire in WA history" and inferring a hard insurance market has substituted the peril leg for the loss leg.**

---

## 5. 🔴 AEO-09 CHECKPOINT — THE 9/01 OUTLOOK IS ISSUED. GRADING INPUTS ONLY — NOT RESOLVED.

> ⚠️ **SUPERSEDED FOR GRADING by the 10/01 issue. Its inputs are in the 2026-10-09 block at the top of this file.** The 9/01 material below is kept as the prior checkpoint.

AEO-09 turns on **NIFC removing above-normal potential for TX and OK in an outlook issued on or before 2026-12-01.**

**Instrument: the outlook issued 2026-09-01.** Header verbatim: *"Issued: September 1, 2026 / Next Issuance: October 1, 2026 / Outlook Period – September through December 2026."* **The October issue does not yet exist** (due 10/01).

**The grading rule as handed to the worker: read the CURRENT-MONTH panel; where map and regional narrative disagree, THE REGIONAL SECTION GOVERNS.** The worker applies it and does not re-adjudicate it.

### CURRENT-MONTH (September) panel

| | TX | OK | Evidence |
|---|---|---|---|
| **Southern Area regional narrative** *(governing)* | **ABOVE-NORMAL** | **ABOVE-NORMAL** | verbatim: *"An expansive area of above-normal significant fire potential is expected across **Texas, Oklahoma**, Arkansas, Louisiana, Mississippi, and southwestern Alabama for the month ahead."* |
| **Executive Summary** | above-normal | above-normal | verbatim: *"Above normal potential is also forecast for much of the **southern Plains** into the Lower Mississippi Valley, South Florida, northern Minnesota, northern Wisconsin, western Upper Michigan, Puerto Rico, and the U.S. Virgin Islands."* |
| **MAP panel** *(image extracted from p1 via `pdfimages`)* | **partially above-normal** — red across the central and eastern **two-thirds** to the Rio Grande Valley; **far-west TX (Trans-Pecos/El Paso) and part of the western Panhandle are WHITE/Normal** | **entirely above-normal** — all of OK red, Panhandle included | direct read of the September 2026 panel |

✅ **NO map-vs-text disagreement in the current-month panel** — map and regional section both designate TX and OK above-normal for September. The governing rule is therefore **not load-bearing this month**; it would only bite if AEOLUS chose to grade an out-month.
⚠️ **The one nuance the map adds that no text carries: TX is only PARTLY above-normal.** If "removed for TEXAS" is read as *any part of TX*, September fails it; if read as *whole-state*, far-west TX was already normal on 9/01. **That is a definitional question for AEOLUS, not a data question.**

### Out-month panels — and here the disagreement IS real

| Panel | Map | Exec Summary | Southern Area section |
|---|---|---|---|
| **October** | **TX/OK NORMAL** — red only over N Minnesota, N Wisconsin, W Upper Michigan, PR/USVI | agrees: *"For October, significant fire potential will be normal for most of the country except for northern Minnesota, northern Wisconsin, western Upper Michigan, Puerto Rico, and the U.S. Virgin Islands"* | 🔴 **hedges the other way:** *"These conditions may very well continue into October and November in portions of the region, but confidence is low as to where conditions will remain driest."* |
| **November** | CONUS all normal; PR/USVI above | agrees | as above |
| **December** | CONUS all normal; PR/USVI above | *"Significant fire potential will be normal for the contiguous U.S. and Alaska for November and December but will remain above normal for Puerto Rico and the U.S. Virgin Islands."* | — |

🔴 **The October panel is a genuine map/text disagreement, and it is the one the governing rule was written for.** Flagged, **not adjudicated.** Note it is a *hedge* ("may very well… but confidence is low"), not a competing designation — whether a low-confidence hedge counts as the regional section "disagreeing" is AEOLUS's call.

### The ENSO tension is NOT resolved — it is stronger

The 9/01 outlook, verbatim: *"El Niño continues to rapidly strengthen… anomalies are more than 1.5 C above average, the threshold for a strong El Niño, and are nearing the 2 C threshold for a very strong El Niño… The CPC forecasts El Niño to persist through the fall and winter, with 100% confidence, with a greater than 95% chance of a very strong El Niño by November… most of the models used by the CPC and internationally show this El Niño to be the strongest on record."* *(ENSO is `regime/`'s instrument — **cited, not adopted**.)*

⚠️ **The 8/13 load-bearing tension persists and has grown:** the outlook attributes the southern-Plains dryness and Caribbean fire activity to El Niño, i.e. **it is using El Niño to EXPLAIN the above-normal fire potential in the very region where AEO-09 expects El Niño to REMOVE it.** Against that, the same section offers the mechanism AEO-09 needs: *"El Niño's influence… setting the stage for what will likely be a very wet end to the year over much of the Southern Area"* — but attaches its own hedge: *"confidence is low in whether heightened late summer fire activity will bleed into the more traditional fall fire season."*

### Physical state has moved AGAINST removal since 8/27

*(9/28 note: by the 9/25 NFN table TX and OK carry **1 large fire each** of 4 listed; new TX fires 9/26–9/27 are ≤2,125 ac.)* **On 9/18 TX reported 6 large fires and OK 4** — together 10 of the nation's 50 (§1), where the Southern Area had none in the 8/27 read. Outlook, verbatim: *"Much of Texas and Oklahoma received less than 20% of normal rainfall for August"*, *"Rapid drought onset was observed in the southern Plains and Lower Mississippi Valley"*, and extreme-to-exceptional drought *"most widespread across central Oregon, the eastern Great Basin, central Rockies, **Texas Panhandle, and western Oklahoma**."*

---

## 6. NON-RENEWAL LEG — 🔑 VINTAGE ADVANCED 2022 → 2024. Still not a live read.

**New instrument found this run:** NAIC Center for Insurance Policy and Research, ***"Examining Homeowner Property Insurance Market Dynamics — An Assessment of Countrywide State-Level Data From 2018 to 2024"***, **FINAL RESEARCH REPORT dated 2026-07-31** (Czajkowski & Harms; NAIC press release 2026-08-05). Built on **Market Conduct Annual Statement (MCAS)** data — **a different collection from the FIO/NAIC PCMI Data Call** behind the 2018-2022 figures already on record.

**Denominator, verbatim:** *"we normalize the nonrenewal data by the total number of policies in force to get a ratio of company-initiated nonrenewals per 1,000 policies in force."*
**Headline, verbatim:** *"Insurers reported 2,019,799 homeowners company-initiated nonrenewals nationwide in 2024. Thirty-one percent of these company-initiated nonrenewals were incurred in the Southeast Zone, and 42% were incurred in the Western Zone."*

| NAIC Zone | 2024 rate per 1,000 PIF | Nonrenewals / policies in force | Worker's reproduction |
|---|---|---|---|
| **Western** | **25.1** | 852,019 / 33,987,845 | 25.07 ✅ |
| **Southeast** | **22.0** | 630,551 / 28,667,242 | 22.00 ✅ |
| **Midwest** | **14.2** | 352,847 / 24,907,688 | 14.17 ✅ |
| **Northeast** | **11.7** | 184,382 / 15,726,559 | 11.72 ✅ |

**All four reproduce, and the zone counts sum to exactly 2,019,799** — the stated national total. *(Load-bearing numbers must be reproducible; these are.)*

**Trend, verbatim:** *"Since 2018, the ratios of company-initiated nonrenewals per 1,000 policies in force have been increasing in all zones, anywhere from 96% to 216%. The most significant increases have occurred in the Northeast and Southeast Zones during this period at 147% and 216%, respectively."*
**Three-year, verbatim:** *"nonrenewal rates per 1,000 policies in force have nearly tripled in the Midwest and Western Zones, rising from 5.5 to 14.2 in the Midwest Zone and **8.0 to 25.1 in the Western Zone**"* (2022→2024). Western Zone's share of countrywide nonrenewals rose **25% (2022) → 42% (2024)**.

⚠️ **SECONDARY-SOURCE ERROR CAUGHT:** press coverage renders this as *"96% in the Southeast to 216% in the West"* — **inverted.** The report says **Southeast 216%, Northeast 147%.** Quote the report, not the coverage.

### ⚠️ A fresher vintage is NOT a live read — four limits survive

1. **The series ENDS 2024, and MCAS is ANNUAL.** The channel-kill leg needs *"non-renewals stable 2+ quarters."* **A quarterly stability test cannot be run on an annual series at all** — 2025 and 2026 are uncovered entirely.
2. **NO STATE CUT EXISTS.** Despite the title *"Countrywide State-Level Data"*, every narrative figure is aggregated to **four NAIC zones**; **no individual state appears anywhere in the extracted text.** "State-level" describes the data **source** (state-reported), not the reporting granularity. **There is no CA, WA, OR, TX or CO figure in this report.**
3. 🔴 **ZONE MEMBERSHIP IS NOT STATED** in the extracted text. **Which zone holds TX, WA, OR, CA or CO cannot be asserted from this source, and the worker does not supply it from memory.** **Until AEOLUS confirms membership from an NAIC primary, the Western 25.1 figure cannot be mapped onto the 2026 fire geography.**
4. **Coverage exclusions, verbatim:** *"Data is based on state-reported data and excludes Puerto Rico and North Dakota"*; *"New York does not provide MCAS data and, therefore, is excluded from the Northeast Zone."*

🔴 **DO NOT COMPUTE A DELTA AGAINST THE FIO 1.04% FIGURE.** FIO/PCMI (80% of HO-3/HO-5 by premium) and NAIC/MCAS are **different collections with different universes**. A `1.04% (2018-2022, PCMI)` vs `1.955% (2024 national, MCAS — worker-computed 2,019,799/103,289,334)` comparison **measures the instrument change, not the market.** **The MCAS 2022→2024 series is internally consistent and is the only usable trend here.**

### 🔴 And the CA measurement is CENSORED BY LAW

**California suppresses its own observed non-renewal rate**, so any CA or Western-zone figure is a **censored observation in exactly the geography under the most fire stress — censored hardest in the years and ZIP codes with the worst fires.**

CA DOI primary (fetched 9/18, live), verbatim: *"Following a Governor declaration of a state of emergency, the Department of Insurance partners with CAL-FIRE and the Governor's Office of Emergency Services to identify wildfire perimeters and adjacent ZIP codes"*; *"This one-year protection applies to all residential policyholders within the affected areas who suffer less than a total loss, including those who suffer no loss"*; *"The protection from cancellation or non-renewal lasts for one year from the date of the Governor's emergency declaration."* Most recent declarations listed: **2026-08-06 (Gann Fire)**, 2025-12-23 (Gifford), 2025-12-09 (Pack), 2025-09-19 (TCU September Complex), 2025-06-18 (Franklin) — **a CA moratorium is ACTIVE in the Gann Fire ZIPs through 2027-08-06.** The page publishes **no** rate or policy-count statistic with a denominator.

⚠️ **Consequence for the band, proposed not adjudicated:** AEOLUS's non-renewal band is a **CHANGE** band (+10/+25/+40% YoY), and a moratorium **mechanically holds the measured change down.** A reading at-or-below band in CA is consistent with **both** a calm market **and** a suppressed one — **the instrument cannot distinguish them, and a benign print must not be read as a channel-kill leg satisfied.**

**Prior-vintage figures retained** (FIO/PCMI, 2018-2022): National **1.04%** (1.20% by 2022); Highest-Risk TLCR quintile **1.61%** (1.10%→2.37%); Southwest region (CA/AZ/NV/CO/NM/UT) **1.28%**; Northwest region (WA/OR/ID/MT/WY/AK) **0.67%**. **TX excluded from the FIO nonrenewal calc entirely.** Still the only source in the tree that names its member states.

---

## OPEN QUESTIONS / GAPS

1. 🔴 **Q3 2026 cat tally (~Oct)** — **the single most important pending item.** It will be the **first loss vintage containing any of this fire season.** Until it lands the loss leg says nothing about 2026 fires either way. *(Checked 10/09: Q3 closed 9/30, and the Artemis homepage shows no Q3/9M 2026 insured nat-cat tally yet.)*
2. 🔴 **Cotality source admission** — a $1B–$1.3B Spokane estimate exists from a source **not in `SOURCES.md`**. AEOLUS decides whether to admit Cotality and whether to log its figure. **Reported as a proposal; not logged as fact.**
3. 🔴 **NAIC zone membership** — must be confirmed from an NAIC primary before the Western 25.1 figure can be mapped to fire geography (§6 limit 3).
4. **Spokane structure count — three irreconcilable objects** (§2). ❌ **Still no WA state EOC FINAL tally**, third consecutive run.
5. **AEO-09 definitional question for AEOLUS:** does "removed for TEXAS" mean *any part of* TX or *whole-state*? The 9/01 map already shows far-west TX normal. **Data cannot answer this; only AEOLUS can.**
6. ✅ **October outlook: ISSUED 10/01, read 10/09** (see the 10/09 block). TX and OK are both NAMED above-normal in the October current-month panel, both partial, and map and text agree. New sub-question for AEOLUS: is the regional *"most likely"* wording a hedge? **Next issuance 11/02**, which carries November as the current month.
6b. **The YTD step since 9/28 (+6,342 fires, +450,199 acres at PL2) is unexplained.** Is it a reconciliation or real activity? No surface read states the cause.
6c. **The "54-day PL5" figure may be cited outside this folder** (e.g. `SOURCES.md` line 131, which a worker may not edit). It is 49 days inclusive, 7/18→9/4.
7. ✅ **CLOSED — the 10-yr-average fields render again** and both narrative percentages reproduce from them (§1). Was open since 8/21.
8. **Utility ignition liability** — not tracked here; **WATT's** if a named utility is implicated.
9. **water/'s USDM series is 24 days stale** (newest observation 8/25). Not wildfire's to fix — flagged to AEOLUS as an owner-side gap that degrades this folder's fuel-state context.
