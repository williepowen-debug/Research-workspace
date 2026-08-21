# AEOLUS · WILDFIRE — live dossier

**As-of: 2026-08-21.** Consolidated from KB-AEO-030/031/032/037/056 + the 2026-08-21 worker run.

> **Last real data refresh: 2026-08-21**  ·  **Dossier written: 2026-08-21**
> *Two-clock header (PAT-044) — `scripts/ledger_staleness.py` reads the first line. **The data date, not the edit date**: a hygiene edit must NOT bump it.*
> **Observations → `wildfire/workbook/SERIES.tsv`** · findings → central `workbook/KB.tsv` · synthesis → `STATUS.md`. **Flow is one-way.**
> **Feeds:** C4
> ⚠️ **The peril figures below are 2026-08-21 (fresh). The reinsurer cat-loss figures are still H1 2026 (published Jul–Aug) — that leg is genuinely stale between publications and is labelled so.** The one NEW loss-leg item is the Spokane estimate, dated **2026-08-06**.
**C4 score: worker does not score. Last AEOLUS-set score was 3 🟠 ↗ (8/13); the 8/21 refresh is un-adjudicated.**

---

## 1. PERIL LEG — firing, and the acreage gap widened

| Instrument | Value | As-of | Δ vs 8/12 | Read |
|---|---|---|---|---|
| **NIFC Preparedness Level** | **5 of 5** — since **7/18/26 07:30 MDT**, now **35 days inclusive** (34 elapsed) | 8/21 | +9 days | max tier held through the whole 8-day AEOLUS dark period |
| **Acres YTD** | **7,642,082** = **171%** of 10-yr avg | 8/21 | **+1,194,640 ac · 155% → 171%** | ⚠️ **ACREAGE. Not a loss figure.** |
| **Fires YTD** | **50,077** = **129%** of 10-yr avg | 8/21 | +3,568 · 126% → 129% | **acres-per-fire still rising** — count up 7.7%, acres up 18.5% |
| **Uncontained large fires** | **76** | 8/21 | **−25 (from 101)** | the one instrument that IMPROVED; 8 new large fires yesterday, 1 contained |
| **Personnel assigned** | 24,265 | 8/21 | n/a | |
| **Acres on active large fires** | 3,571,843 | 8/21 | n/a | ~47% of YTD acreage is on currently-active fires |
| **Aug potential outlook** | above-normal W + N-central US, **southern Plains (TX/OK), Lower Mississippi Valley, s. Florida, PR/USVI** | **issued 8/01, still current** | unchanged | **next issuance 9/01 — verified from the PDF header, not assumed** |
| **Drought (CONUS D1–D4)** | **cite `../water/workbook/SERIES.tsv`** — not copied here | — | — | `water/` owns drought (shared input to C2/C4/C5/C6) |

**Geographic spread (8/21):** all ten geographic areas list ≥1 large fire. Northwest leads with 32 fires and **six fires >100,000 acres**. State counts: OR 18 · WA 13 · MT 12 · ID 7 · CO 5 · UT 5 · MN 3 · NV 3 · CA 2 · NM 1 · SD 1 · AK 1 · GA 1 · MS 1 · FL 1 · WY 1.

⚠️ **The 10-year-average YTD Fires/Acres fields on the NIFC page render BLANK in the served HTML** — the 129% / 171% figures come from NIFC's own narrative paragraph (the same place the 8/13 read's 126% / 155% came from). Implied averages **derived, not published**: acres ≈ 4,469,053; fires ≈ 38,819.

---

## 2. INSURED-LOSS LEG — still soft at the aggregate level; one new single-event estimate

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

## OPEN QUESTIONS / GAPS

1. **Spokane: insured-loss estimate NOW EXISTS** (Gallagher Re, 8/6, hundreds of millions → plausibly $1B). **Structure count revised to >700 destroyed (Gallagher Re, 8/6).** ❌ **Still no WA state EOC FINAL tally** — `mil.wa.gov/alerts` and `dnr.wa.gov/wildfires` returned HTTP 200 but carried no Spokane structure figure. **No newer insured-loss item on Artemis since 8/6** (site search returned only the one article), so the estimate has not been firmed by KCC / Verisk / Moody's RMS on the listed sources.
2. **Sep-1 NIFC outlook** — the real AEO-09 checkpoint. **Not yet issued.** Due ~2026-09-01, ~11 days out.
3. **Full-year cat tallies (Jan)** — aggregate loss leg is stale between publications and labelled so.
4. **Non-renewal data outside CA** — WA, CO, OR, TX filings still not pulled. **AM Best's WA FAIR Plan assessment flag is the strongest non-CA pointer yet**, but it is a mechanism note, not a filing.
5. **Utility ignition liability** — not tracked here; **WATT's** if a named utility is implicated.
6. **NEW — the 10-yr average YTD fields render blank on the NIFC page.** Percentages are taken from NIFC's narrative. If AEOLUS wants the published averages rather than derived ones, the NICC annual report / IMSR is the place, and it was not pulled this run.
