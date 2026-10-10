# AEOLUS · WILDFIRE — live dossier

**As-of: 2026-10-09.** Consolidated from KB-AEO-030/031/032/037/056 + the 2026-08-21, 2026-08-27, 2026-09-18, 2026-09-28 and 2026-10-09 worker runs. **The 9/28 refresh and the 9/18 body (§1–§6) were rotated to archive 10/10 — pointer below; the 10/09 block is the live state.**

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

## ROTATED 2026-10-10 — the 9/28 refresh and the 9/18 body (§1–§6)
Verbatim → `../archive/WILDFIRE_DOSSIER_ARCHIVE_2026-10-10_9-28-refresh-and-sec1-6.md`. It holds: the 9/28 refresh · two 9/28 corrections · §1 peril leg · §2 insured-loss leg (H1 vintage; Spokane two estimates; **three irreconcilable structure counts — never merge or average**) · §3 peril/loss divergence · §4 margins that move C4 · §5 the 9/01 AEO-09 checkpoint · §6 non-renewal leg (MCAS 2024 vintage; **CA censored by law**). **Standing rule: acreage is PERIL, never loss.**

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
