# AEOLUS · WILDFIRE — live dossier

**As-of: 2026-08-27.** Consolidated from KB-AEO-030/031/032/037/056 + the 2026-08-21 and 2026-08-27 worker runs.

> **Last real data refresh: 2026-08-27**  ·  **Dossier written: 2026-08-27**
> *Two-clock header (PAT-044) — `scripts/ledger_staleness.py` reads the first line. **The data date, not the edit date**: a hygiene edit must NOT bump it.*
> **Observations → `wildfire/workbook/SERIES.tsv`** · findings → central `workbook/KB.tsv` · synthesis → `STATUS.md`. **Flow is one-way.**
> **Feeds:** C4
> ⚠️ **The peril figures below are 2026-08-27 (fresh). The reinsurer cat-loss figures are still H1 2026 (published Jul–Aug) — that leg is genuinely stale between publications and is labelled so.** No new Spokane loss estimate since **2026-08-06** (checked 8/27, none found). **NEW this run: a national+regional non-renewal-rate instrument (FIO/NAIC PCMI, 2018-2022) partially closes the standing non-renewal gap — see §6.**
**C4 score: worker does not score. Last AEOLUS-set score was 3 🟠 ↗ (8/13); the 8/21 and 8/27 refreshes are un-adjudicated.**

---

## 1. PERIL LEG — mixed: acreage % eased, but the large-fire count reversed higher

| Instrument | Value | As-of | Δ vs 8/21 | Read |
|---|---|---|---|---|
| **NIFC Preparedness Level** | **5 of 5** — since **7/18/26 07:30 MDT**, now **41 days inclusive** (40 elapsed) | 8/27 | +6 days | max tier held for the entire season to date |
| **Acres YTD** | **7,971,399** = **164%** of 10-yr avg | 8/27 | **+329,317 ac · 171% → 164%** | ⚠️ **ACREAGE. Not a loss figure.** Pct FELL despite absolute acres RISING — the accreting to-date 10-yr-avg denominator grew faster than the numerator (implied avg 8/21 ≈4.47M → 8/27 ≈4.86M ac). **Not a real deceleration signal on its own.** |
| **Fires YTD** | **51,434** = **127%** of 10-yr avg | 8/27 | +1,357 · 129% → 127% | same denominator-growth effect as acres |
| **Uncontained large fires** | **94** | 8/27 | **+18 (from 76)** | 🔴 **REVERSES the 8/21 improvement.** 7 new large fires reported yesterday (8/26), 1 contained |
| **Personnel assigned** | 21,854 | 8/27 | **−2,411** | down even as large-fire count rose — worth AEOLUS's read (demobilization vs reallocation) |
| **Aug potential outlook** | above-normal W + N-central US, **southern Plains (TX/OK), Lower Mississippi Valley, s. Florida, PR/USVI** | **issued 8/01, still current** | unchanged | **next issuance 9/01 (~5 days out) — re-verified via direct PDF text extraction 8/27, not assumed** |
| **Drought (CONUS D1–D4)** | **cite `../water/workbook/SERIES.tsv`** — not copied here | — | — | `water/` owns drought (shared input to C2/C4/C5/C6) |

**Geographic spread (8/27):** Oregon leads with 16 large fires, Washington tied at 16, Montana at 12 (per the page narrative on new-fire reporting — full 10-area breakdown was not re-pulled this run, only the leaders). "Elevated fire conditions" flagged for the Inland Northwest, northern Rockies, and northern Great Basin on 35–45 mph gusts + 5–20% RH; locally critical conditions possible NE California/NW Nevada into SE Oregon/SW Idaho.

⚠️ **The 10-year-average YTD Fires/Acres fields on the NIFC page render BLANK in the served HTML** (unchanged from 8/21) — the 127% / 164% figures come from NIFC's own narrative paragraph. Implied averages **derived, not published**: acres ≈ 4,860,609; fires ≈ 40,499 (both grew vs the 8/21 implied values, confirming this is a seasonally-accreting comparator, not a fixed denominator).

---

## 2. INSURED-LOSS LEG — still soft at the aggregate level; no new estimate since 8/6 (checked)

**Aggregate (the RED-band instrument) — UNCHANGED since 8/13, no new publication:**

| Instrument | Value | As-of |
|---|---|---|
| **H1 2026 US insured nat-cat** | **~$36B**, **~25–28% BELOW** the 10-yr avg — lowest H1 since 2018 | H1 2026 |
| Global H1 | ~$47B (US ~75%), 11 US billion-dollar insured events | H1 2026 |
| Reinsurance ROL (July renewal) | **soft** — global cat −16%, NA −20/25%; capital at a record **>$700–790B** | Jul 2026 |

**NEW — Spokane single-event insured loss (Artemis.bm, 2026-08-06, citing Gallagher Re + AM Best):**

- **Gallagher Re:** insured losses *"will minimally reach into the hundreds of millions (USD); with a plausible chance and likelihood of this becoming a billion-dollar event."* Expected to rank among — possibly as — **the costliest insured wildfire event in Washington's history**.
- **AM Best:** *"the losses do not appear to be in the same order of magnitude as the 2025 California wildfires and likely will have minimal impact on the current softening prices in the reinsurance market; however, there could be a reassessment in localized areas."*
- **AM Best flags a WA FAIR Plan assessment path** — same premium-share mechanics as the CA FAIR Plan, all state insurers are mandatory members.
- **WA-exposed cat bond sponsors:** State Farm, Allstate, USAA, Travelers. Aggregate-layer retention erosion possible; **per-occurrence structures unlikely to be touched at current damage levels.**

**Structure count — REVISED (and this is the warned-about direction):**

| Vintage | Figure | Issuing authority | As-of |
|---|---|---|---|
| prior dossier | ~640–700 structures / ~5,390 acres | Spokesman / WA-EOC | 8/1–2 |
| **current** | **">700 homes" destroyed / "over 10,000 acres" / ~65,000 evacuated** | **Gallagher Re** (via Artemis) | **8/6** |
| *separate object* | *"as many as 1,100 properties may have been **damaged or destroyed**" based on aerial imagery* | *unnamed fire officials* | *8/6* |

⚠️ **The 1,100 is a damaged-OR-destroyed economic count from fire officials — not a destroyed-structure EOC tally.** Do not merge the two.

**8/27 check:** Artemis.bm wildfire-tag listing + site search for Spokane coverage after 8/6 returned nothing new — the Gallagher Re/AM Best estimate remains the only insured-loss figure for this event. H1 2026 aggregate corroborated by an independent republication (Gallagher Re global H1 $46bn/28% below avg) — consistent with the $47B/~$36B figures already on record, no new post-H1 tally. **Noted but NOT a wildfire figure:** an Aug 9–12 Midwest derecho pushed 2026 US severe-convective-storm losses past $35bn (Aon/Gallagher Re) — a different peril, flagged only to prevent future confusion with the fire tally.

---

## 3. 🔑 THE DIVERGENCE — wider than it was on 8/13

**Physical peril now at 171% of average acreage (was 155%) while aggregate insured losses still run 25–28% below it.** The gap between the two legs **widened by 16 percentage points on the peril side while the loss side did not move at all.** The down-stack migration claim is unchanged: reinsurance stays soft on record capital, so stress lands on primary carriers, **state residual pools** (CA FAIR Plan **+29.1%** and its first **$1B** assessment in 30 years; **WA FAIR Plan now flagged by AM Best as a live assessment path**), and property-exposed munis.

⚠️ **REGINALD's standing counter, carried honestly:** the *softening* leg is the better-evidenced one; down-stack migration is the load-bearing claim and is not yet independently confirmed. ZION remains the one weak name on the CA-muni-conduit side (monitor-only).

⚠️ **WA remains the underpriced-state tell — and it now has an insurer-side number attached to it**, which it did not on 8/13. A hundreds-of-millions-to-$1B event landing in a state whose rate structure never anticipated wildfire is the concrete form of the down-stack claim.

---

## 4. WHAT WOULD ACTUALLY MOVE C4 — margins, not grades

| | Condition | Value | Margin |
|---|---|---|---|
| **Upgrade 3 → 4** | carrier **insolvency** OR a single **>$10B** insured cat | Spokane: hundreds of millions, high case ~**$1B** | **~$9B short — roughly one order of magnitude below the trigger.** No insolvency reported. |
| **RED band** | reinsurer cat tally **≥150%** of 10-yr avg | ~**72–75%** (H1 2026) | **~75 pts below the RED band and below even Yellow (110%)** — pointing the opposite way |
| **Channel-kill** | H1 cat <110% of avg **AND** non-renewals stable 2+ quarters | loss leg ~72–75% (satisfies); non-renewal leg unevidenced outside CA | conjunction unsatisfied on the second leg |

🔴 **171% is an ACREAGE percentage. The RED band is a CAT-LOSS percentage at ~72–75%. They are different rows of the threshold table and different units.** Anyone reading "PL5 for 35 days, 171% of average acreage, most destructive fire in WA history" and inferring a hard insurance market has substituted the peril leg for the loss leg. **The two legs are now further apart than at any prior read.**

---

## 5. AEO-09 CHECKPOINT — status only, not resolved

AEO-09 turns on **NIFC removing above-normal potential for TX and OK in an outlook issued on or before 2026-12-01.**

**Current instrument: the outlook issued 2026-08-01. Next issuance 2026-09-01 — header-verified today, not assumed.**

| Panel | TX / OK status | Verbatim |
|---|---|---|
| **August (current month)** | **ABOVE-NORMAL — still there** | above-normal potential for "much of the northern Plains, northern Minnesota, **southern Plains**, Lower Mississippi Valley, south Florida, and Puerto Rico and the U.S. Virgin Islands" |
| **September** | **returns to normal** | "For September, potential is forecast to return to **normal in much of the Southern Area**, western Colorado, and southwest Wyoming" |
| **October / November** | normal | normal everywhere except northern Minnesota, PR, USVI |

**Southern Area regional narrative — and it does NOT read the same as the Executive Summary:**
> "Above normal significant fire potential is forecast to **develop through large parts of Oklahoma and Texas** into southern and eastern Arkansas, Louisiana, Mississippi, and southwestern Alabama in the coming weeks… Above normal significant fire potential **has the potential to carry into September, especially over the southern Plains**."

⚠️ **AEOLUS must adjudicate two things the worker will not:** (a) whether "removed" means the **current-month panel** or **any panel** — the same 8/01 outlook already returns much of the Southern Area to normal in its September panel while keeping TX/OK above-normal in August; (b) the **internal tension** between the Exec Summary ("return to normal in much of the Southern Area") and the Southern Area section ("potential to carry into September, especially over the southern Plains").

**ENSO context carried from the 8/13 read (unrefreshed here — `regime/` owns it):** the outlook itself attributes the southern-Plains dryness to "a common theme in summers with **intensifying El Niño** conditions," and attributes Caribbean fire activity and offshore-kept rainfall to El Niño shear. **The outlook is using El Niño to explain the ABOVE-normal fire potential in the very region where AEO-09 expects El Niño to remove it.** That is directly load-bearing on the prediction and is AEOLUS's to adjudicate.

---

## 6. 🔑 NON-RENEWAL LEG — gap PARTIALLY CLOSED 2026-08-27 (national + regional instrument found)

**The standing problem:** the non-renewal leg of the channel-kill conjunction had NO metric surface anywhere in the tree — only the band definition (`README.md` § STANDING BANDS). It rested on CA evidence alone, and even that was never a pulled number.

**What was found:** US Treasury FIO, *"Analyses of U.S. Homeowners Insurance Markets, 2018-2022: Climate-Related Risks and Other Factors"* (published Jan 2025), built on the NAIC/FIO PCMI Data Call — 80% of HO-3/HO-5 policies nationwide by premium, 45M+ policies/yr, 33,000+ ZIP codes. **Definition (verbatim, p.7): "Nonrenewal Rate = Count of Nonrenewals in Reporting Year / Policies in Force at End of Reporting Year."** Verified pull command → `SOURCES.md`.

| Cut | Nonrenewal rate (2018-2022 avg) | Note |
|---|---|---|
| **National** | **1.04%** | rose to 1.20% by 2022 (from ~flat 2018-19, dip 2020-21 on COVID moratoria) |
| National, Highest-Risk TLCR quintile | **1.61%** | rose 1.10%(2018) → 2.37%(2022), more than doubled |
| National, Lowest-Risk TLCR quintile | 0.90% | |
| **Southwest region** (CA/AZ/NV/CO/NM/UT — the wildfire-dominant HOI-peril region per this report) | **1.28%** (+23.5% vs national) | Highest-Risk category **1.92%**, Higher-Risk 1.38% |
| **Northwest region** (WA/OR/ID/MT/WY/AK — the *other* wildfire-dominant region) | **0.67%** (−35% vs national) | Highest-Risk **0.86%**, Higher-Risk 0.74% |

⚠️ **TENSION FLAG for AEOLUS:** the Northwest is where 2026's *live* fire activity concentrates (OR 16 / WA 16 large fires, 8/27) — but its 2018-2022 non-renewal baseline runs **below** the national average, opposite of what the current peril read would suggest. The dataset predates the 2026 season (and 2023-2025) by construction, so it cannot yet confirm or refute this year's stress; the tension is a reason to watch for a fresher cut, not a contradiction to resolve now.

⚠️ **What remains open:** the report **explicitly excludes 2023 and 2024** and states in its own limitations section that "public data suggests that premiums and nonrenewals" have likely continued rising since. **No WA-state-specific cut exists** (regional only — WA is bundled into "Northwest" with OR/ID/MT/WY/AK). **Texas is excluded from the nonrenewal calculation entirely** (insurer data gap, per the report's own Figure 8 footnote). CA DOI's own wildfire-insurance and CA FAIR Plan policy-in-force pages returned HTTP 404 on direct fetch (`SOURCES.md`); a CA FAIR Plan policy-count-growth figure surfaced via search only (not a direct primary fetch) and is **not** logged as fact here per hard limits — a fresher CA-specific number remains unclosed.

**Bottom line for the channel-kill conjunction:** the non-renewal leg now has a real, sourced, defined-denominator instrument for the first time — but it is a **2018-2022 vintage** reading being asked to speak to a **2026** question. AEOLUS's call: whether "non-renewals stable 2+ quarters" can be evaluated at all against a series with no observation newer than 2022, or whether this closes the definitional gap only and the evidentiary gap stays open pending a 2023+ source.

---

## OPEN QUESTIONS / GAPS

1. **Spokane: insured-loss estimate unchanged since 8/6** (Gallagher Re, hundreds of millions → plausibly $1B; re-checked 8/27, no newer item on Artemis). **Structure count still >700 destroyed (Gallagher Re, 8/6).** ❌ **Still no WA state EOC FINAL tally** — not re-attempted this run.
2. **Sep-1 NIFC outlook** — the real AEO-09 checkpoint. **Not yet issued** as of 8/27 (re-verified via direct PDF extraction). Due ~2026-09-01, ~5 days out.
3. **Full-year cat tallies (Jan)** — aggregate loss leg is stale between publications and labelled so.
4. **Non-renewal data — PARTIALLY CLOSED this run (§6):** national + Southwest + Northwest regional rates now sourced (FIO/NAIC, 2018-2022 vintage). **Still open:** no post-2022 cut, no WA-state-specific cut, CA DOI/FAIR Plan primary sources returned 404.
5. **Utility ignition liability** — not tracked here; **WATT's** if a named utility is implicated.
6. **The 10-yr average YTD fields still render blank on the NIFC page** (confirmed again 8/27). Percentages are taken from NIFC's narrative. If AEOLUS wants the published averages rather than derived ones, the NICC annual report / IMSR is the place, and it was not pulled this run.
