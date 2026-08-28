# AEOLUS · WATER — worker run report

```
run_date:   2026-08-27 (Thursday)
window:     closes the 6-day observation gap 2026-08-21 → 2026-08-27
scope:      AGENTS/AEOLUS/water/ only. Nothing outside was read for write or written.
grading:    NONE. No channel scored, no trigger fired, no prediction resolved. Values + margins only.
```

> **Headline: C5 upgrade-trigger 3-day grade is FAIL/FAIL/FAIL — the Rhine is nowhere near firing, Duisburg-Ruhrort is at a folder-record HIGH.**
> **Two named gaps CLOSED: Panama's Gatun Lake elevation (61-year daily CSV + forward projection, found via ACP's own site nav) and the Mississippi/Ohio low-water reference (NWS AHPS `MEMT1`, Memphis, `lowThreshold -8 ft`).** Both are proposal-only — no SERIES.tsv rows added under unapproved instrument names, per AGENT.md.
> **Mead and Powell both still falling on 6-day rates; margins narrowed 0.39 ft (Mead) and 0.72 ft (Powell) since 8/20.**

---

## observations_added

| File | Rows |
|---|---|
| `workbook/SERIES.tsv` | **+39** (287 → 326 lines) |
| `workbook/LOG.tsv` | **+11** (50 → 61 lines) |
| `DOSSIER.md` | new 8/27 top-of-section blocks in §1 Drought, §2 Colorado, §3 River Navigation; two-clock header → **`Last real data refresh: 2026-08-27`**; OPEN QUESTIONS items 11-14 added |

**Integrity checks run:** all 326 SERIES rows have exactly 7 tab-separated fields (the one 0-field line, #252, is a pre-existing blank line from before this session — verified, not introduced here); all 61 LOG rows have exactly 6. **Two deliberate revisions** (Kaub 8/21, Duisburg-Ruhrort 8/21) — the 8/21 partial-day rows (n=93) are superseded by complete-day rows (n=96); both new rows carry `REVISED: supersedes...` in `notes`, nothing overwritten.

**No new instrument names invented.** Every SERIES.tsv row uses a name already in the AGENT.md controlled vocabulary. **Two high-value new series (Gatun Lake elevation, Mississippi stage at 3 stations) were found and verified but NOT written to SERIES.tsv** — they have no approved instrument name. Full command + values are in `DOSSIER.md` §2/§3 and `LOG.tsv`, proposal-only, for AEOLUS to register.

---

## threshold_state

**Reported as level + margin. NOT GRADED — AEOLUS adjudicates every line below.**

| Threshold | Value | As-of | Margin | State |
|---|---:|---|---:|---|
| Powell vs all-time low **3,519.92 ft** | **3,518.48** | 8/26 | **−1.44 ft (below)** | unchanged direction, falling further past the 8/15 break |
| Powell vs ROD protection line **3,510 ft** | 3,518.48 | 8/26 | **+8.48 ft** | above; narrowed 0.72 ft since 8/20 (9.20 ft) |
| **Mead vs Hoover 1,035 ft** *(BINDING)* | **1,039.05** | 8/26 | **+4.05 ft** | above; narrowed 0.39 ft since 8/20 (4.44 ft) |
| Powell vs min power pool 3,490 ft | 3,518.48 | 8/26 | +28.48 ft | above |
| **Kaub vs 25 cm NNW** | **59.979** (unrounded, complete day) | 8/27 | **+34.979 cm** | well above; 6 of 7 recent days ≥+34 |
| **Duisburg-Ruhrort vs 153 cm NNW** | **194.146** (unrounded, complete day) | 8/27 | **+41.146 cm** | **folder-record high**; above since 8/22 |
| **C5 trigger — 3-day grade (8/25, 8/26, 8/27)** | both legs FAIL all 3 days | — | — | **FAIL/FAIL/FAIL — not close** |
| USDM CONUS **D1–D4** | **56.61%** | valid 8/25 | +3.91 pp w/w | 4th straight week every tier up; acceleration itself accelerating |
| Panama booking-slot cap (A-29-2026) | 32/day from 9/1 | eff. 9/1/26 | — | **unmodified** — A-30-2026 checked, procedural only |
| Gatun Lake elevation *(new, proposal-only)* | **83.80 ft** | 8/26 | 1.22 ft below the one prior anchor (85.02 ft, 8/2024) | inside 82-87 ft normal range, low side, falling ~0.037 ft/day |
| Memphis Mississippi stage vs AHPS lowThreshold *(new, proposal-only)* | **12.47 ft vs −8 ft** | 8/27 | **+20.47 ft** | not stressed |

### 🔑 C5 grade detail — the number AEOLUS asked for directly

**3 most recent complete days, unrounded daily means:**

| Date | Kaub | ≤25? | Duisburg-Ruhrort | ≤153? |
|---|---:|---|---:|---|
| 8/25 | 71.969 | ❌ | 170.208 | ❌ |
| 8/26 | 65.406 | ❌ | 187.219 | ❌ |
| 8/27 | 59.979 | ❌ | 194.146 | ❌ |

**Both legs fail on all 3 days — margin is 34-47 cm at Kaub and 17-41 cm at Duisburg, not a close call.** Duisburg-Ruhrort crossed above its NNW on **8/22** (was still −0.969 cm below on 8/21, the last day of the 11-day joint-below run reported at 8/21 closeout) and has climbed every day since, closing 8/27 at its **highest reading in this folder's Duisburg record**.

---

## changes

### 1 · Mead/Powell — both still falling, margins narrowing at a stated (unextrapolated by default) 6-day rate

| | 8/20 | 8/26 | Δ (6 days) | rate/day | driver check |
|---|---:|---:|---:|---:|---|
| **Powell** | 3,519.20 | 3,518.48 | −0.72 | **−0.12 ft/day** | Powell's own Aug→Sep base rate (5/5 years decline, mean −5.57) is **not** release-contingent (§ DOSSIER) |
| **Mead** | 1,039.44 | 1,039.05 | −0.39 | **−0.065 ft/day** | Lees Ferry release sits at a **flat** −41% deficit across 3 overlapping windows — not accelerating |

**If extrapolated at these rates (reported per L-16, not asserted as forecast):** Mead reaches 1,035 ft ≈ **2026-10-27**; Powell reaches the 3,510 ft ROD line ≈ **2026-11-04**. **AEOLUS's call whether a 6-day linear rate outweighs the (already-flagged-contaminated) 5-year seasonal base rate.**

**Lees Ferry, 8/13-26 mean (n=14, no gaps this window): 7,905.0 cfs vs 2018-25 same-window mean 13,411.6 cfs = −41.06%.** Third consecutive read of essentially the same deficit level (−42.4% on 8/01-12, −41.5% on 8/13-20, −41.06% on 8/13-26) — **a flat level, not a still-deteriorating slope.**

### 2 · 🔴🔴 Gatun Lake elevation — INSTRUMENT FOUND (was UNINSTRUMENTED as of 8/21)

The 8/21-flagged lead ("Daily average level of Gatun Reservoir for the last 12 months") resolves via ACP's own site navigation, not the broken Tableau URL. `https://evtms-rpts.pancanal.com/eng/h2o/index.html` links a **history CSV** (1965-01-01 → 2026-08-26, 22,518 rows, daily, feet) and a **forward projection CSV** (through 2026-10-27, tying lake level to `surcharge_pcent` and `max_neopanamax_draft_ft`/`max_panamax_draft_ft`). Both HTTP 200, both plain CSV, both re-pullable. Latest: **83.80 ft (8/26)**, trending **−0.037 ft/day** over the last 9 complete days. Corroborates the single prior spot-anchor in this folder (85.02 ft, A-27-2024, 2024-08-09) — same unit, same datum family, plausible YoY decline.

⚠️ **The projection CSV's modeled draft-step dates (~9/12-13, ~10/9) do not match A-29-2026's officially announced dates (9/2, 10/1)** — an 8-10 day gap between two primary ACP publications. Flagged, not reconciled.

⚠️ **The old Tableau URL is now definitively dead for a different reason than 8/21** — it returns HTTP 200 but resolves to ACP's unrelated procurement/bidding portal, not a broken cert or JS shell. Retire it from `SOURCES.md`; point to the working nav page instead.

### 3 · 🔴 Mississippi/Ohio — GAP CLOSED with a working command AND a documented low-water reference

`api.water.noaa.gov/nwps/v1/gauges/MEMT1` (Memphis, TN) returns both a current stage (`status.observed.primary`) and a **published `lowThreshold` field (−8 ft)** — an authoritative low-water reference, not carried or inferred. Verified 8/27: **12.47 ft, +20.47 ft above threshold, not stressed.** Baton Rouge (`BTRL1`) also live (14.43 ft, rising) but has no `lowThreshold` published. USGS NWIS St. Louis (07010000) gauge height is live and **falling fast** (8.15→4.27 ft, 8/23→8/27, ~1 ft/day the last 2 days) but has no low-water reference found this session. Memphis discharge (USGS 07032000, 00060) corroborates a non-stressed river: 508k→597k→586k cfs, 8/20-26.

### 4 · Danube — the below-LKV count collapsed 14→5, but Pfelling REVERSED

Non-sentinel below-LKV stations fell from 14 (8/21) to 5 (8/27); longest contiguous run fell from 11 stations/195.3 km to 2 stations/48.6 km. **But Pfelling (Bavaria), recorded "+30 recovered" at 8/21 closeout, is now −4, below its (real, 2018-08-22) LKV again** — alongside a newly-below Hofkirchen (−2, LKV 2003-08-27). Both are in the upper/German reach that had fully recovered on 8/21, while the middle Hungarian reach (Vác, Budapest) that was still deteriorating on 8/21 has now recovered. **The divergence pattern flipped ends within the week — do not assume persistence of either recovery.**

### 5 · Paraná — receding from the peak, still not close to firing

Rosario 2.87 m (8/27), down from 2.97 (8/21) and the trailing-year max 3.02/3.03 (8/12-13). Re-pulled the full 366-day distribution: current ranks the **91.5th percentile**, down from 96.2nd (8/21) and 99th (8/13) — a real but modest recession, nowhere near the P10≈1.40 working low-water reference.

### 6 · USDM — 4th straight week up, and the weekly move is itself accelerating

D1-D4 56.61% (8/25), +3.91 pp vs 8/18's +2.32 pp move. D4 +30% w/w again (1.35%→1.75%). **State cut confirms the split held and sharpened**: OK now 100% D1+ (D4 8.68→12.06%), TX D1 36.11→57.36%, AR D1 71.01→84.90%; NE actually improved (D1 77.82→67.43%); IL/IN/IA flat to slightly better. ⚠️ **Self-caught error, not shipped:** TX's `none` figure fell (22.09→9.94%), which is MORE area affected, not less — an earlier same-session read of that pair alone as "TX improving" would have been a denominator-direction mistake; the full-tier read corrects it before it reached any durable surface.

### 7 · A-30-2026 checked — no further Panama postponement or deepening

Read in full at the primary PDF: booking/tiebreaker procedural rules only. A-29-2026's 9/1 slot cap (32/day) and draft schedule (48.0 ft → 9/2, 47.5 ft → 10/1) stand unmodified.

---

## proposed_findings

*(PROPOSALS ONLY — AEOLUS adjudicates and assigns KB-AEO-NN IDs.)*

1. **Gatun Lake elevation is now a re-pullable 61-year daily series with a live forward projection** — closes this folder's single highest-value open gap. Register `gatun_elev` (ft, `ACP-GATUN-CSV`, daily) in AGENT.md's vocabulary.
2. **Memphis Mississippi stage (NWS AHPS `MEMT1`) carries a published low-water reference (`lowThreshold −8 ft`)** — closes the "Rhine/Mississippi level vs navigable minimum" threshold row's zero-metric-surface gap for the Mississippi leg. Register `memphis_stage` (ft, `NWS-AHPS-MEMT1`) at minimum; `batonrouge_stage`/`stlouis_stage`/`memphis_q` as secondary legs.
3. **The C5 upgrade trigger is unambiguously not firing** — both legs sit 17-47 cm above their NNW thresholds on every one of the 3 most recently graded days, and Duisburg-Ruhrort is at a record high. The 11-day near-miss run (8/09-19) looks, one week later, like a transient rather than the start of a sustained event.
4. **Two ACP primaries (the Gatun projection CSV and Advisory A-29-2026) disagree by 8-10 days on the draft-step schedule** — worth a reconciliation note in DOSSIER/KB once AEOLUS decides which governs.
5. **The Danube's upper/lower divergence reversed ends within one week** (Pfelling/Hofkirchen newly below; Vác/Budapest recovered) — a possible general lesson about how fast this instrument's spatial pattern can flip, worth a KB row if the pattern repeats.
6. **USDM state-cut geography (OK/TX/AR deteriorating, NE improving, IL/IN/IA flat) held and sharpened for a second consecutive week** — strengthens the 8/13-originated "pull the state cut before reading drought into C2/C4" discipline as a repeatable finding, not a one-off.

---

## gaps

*(Required output, not an admission of failure — see AGENT.md.)*

1. **Vicksburg and Cairo, IL — no working AHPS lid found this session.** Guessed lids (`VICM6`, `VKBM6`, `VIKM6` for Vicksburg; `CAIA2`, `CACT1` for Cairo) all returned HTTP 404. The AHPS `usgsId=` query parameter did not filter as expected (returned the full unfiltered gauge list instead, ~20,000+ entries, and a follow-up call timed out after 2 minutes) — **not chased further, per the bounded-effort instruction.** Memphis + Baton Rouge + St. Louis (via USGS NWIS) are the three stations actually verified.
2. **St. Louis (USGS 07010000) has no low-water reference plane found** — only a raw, fast-falling stage reading (8.15→4.27 ft, 8/23-27). A documented reference for this specific gauge was not located this session.
3. **Yangtze was NOT refreshed this session** — out of the scope given for this pass (items a-f + the two named gaps); last read remains the 8/21 pull in DOSSIER.md. Flagging so the gap is visible rather than silently stale.
4. **Gatun and Mississippi instruments are proposal-only** — by design, per the no-invented-instrument-name hard limit. They will not appear as SERIES.tsv rows until AEOLUS approves names, even though both commands are verified working right now.
5. **No command failed outright this session.** Every pull attempted (Mead/Powell CSV, Lees Ferry NWIS, Kaub/Duisburg PEGELONLINE, USDM CONUS + 7 states, Danube ArcGIS, Rosario + historico, Memphis/Baton Rouge/St Louis AHPS+NWIS, Gatun CSV ×2, A-30-2026 PDF) returned data on the first or second try.
