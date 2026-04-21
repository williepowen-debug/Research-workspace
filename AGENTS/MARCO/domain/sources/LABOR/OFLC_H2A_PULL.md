# OFLC H-2A Disclosure Data — Pull Verdict

*MARCO | 2026-04-21 | source: DOL/OFLC via Wayback Machine*

---

## VERDICT

**(1) Fresh FY2025 full-year number is 398,258 positions certified / 415,496 requested — VX-H2A-01 "415K" is the *requested* figure, not certified.** This matters: requested = demand floor (includes rejected/withdrawn), certified = what OFLC greenlit. Both tell the labor-tightness story but the denominator for "workers actually arriving" is the certified number. MARCO should track both and split the vector into H2A-REQ and H2A-CERT. The >400K breach threshold still fires on requested (415K) but not yet on certified (398K — one more year of growth gets there).

**(2) Growth has meaningfully accelerated but YoY is modest.** FY22→FY25 certified: 371,619 → 378,513 → 384,900 → 398,258 (+1.9%, +1.7%, +3.5%). Applications received jumped 9.3% YoY in FY25 — meaning demand ran ahead of certification rate (bottleneck forming at DOL processing? or more rejections?). The 14-year trajectory from ~150K in 2015 to ~400K in 2025 is the real story; H-2A is now ~8% of the U.S. crop workforce. **No acute cliff yet — the ag-labor crisis is a slow burn, not a Q-over-Q spike.**

**(3) Florida owns 14.3% of certified H-2A workers (56,818 / 398K FY25).** This is a direct MARCO compounding vector: FL is already triple-exposed (insurance + tourism + migration), and the single largest H-2A-dependent state. Any DHS enforcement shock or AEWR hike lands hardest on FL ag. Route to REGINALD/CORAL as additional localized stress input.

---

## Current Values (FY2025 Q4 complete — data as of Sept 30, 2025)

| Metric | Value |
|--------|-------|
| Total positions certified FY25 | **398,258** (DOL PDF) / 398,059 (my agg; 0.05% diff from status sub-categories) |
| Total positions requested FY25 | 415,496 |
| Applications received FY25 | 24,725 (+9.3% YoY) |
| Applications processed / certified | 24,526 / 23,424 |
| Median wage offer | $17.79/hr |
| Latest quarter (FY25 Q4 = Jul-Sept 2025) | 81,018 cert / 82,386 req |

### Top 5 states (worksite, certified)

| State | Workers | % |
|-------|---------|---|
| FL | 56,818 | 14.3% |
| GA | 42,723 | 10.7% |
| CA | 35,138 | 8.8% |
| WA | 34,560 | 8.7% |
| NC | 26,123 | 6.6% |

### Top 5 SOC occupations (certified)

| SOC | Workers | % |
|-----|---------|---|
| Farmworkers & Laborers — Crop, Nursery, Greenhouse | 325,931 | 82.0% |
| Agricultural Equipment Operators | 36,951 | 9.3% |
| Farmworkers — Farm, Ranch, Aquaculture (animals) | 19,820 | 5.0% |
| Heavy & Tractor-Trailer Truck Drivers | 4,468 | 1.1% |
| Construction Laborers | 2,659 | 0.7% |

Note: OFLC schema does **not** carry a crop field — "top crops" is not directly answerable from this file. Crop-level signal requires joining on Addendum A (`H-2A_Addendum_A_*.xlsx`) which lists work activities per worksite. Adding that is a future-spawn task; for now use top job titles as a proxy (Harvester = 10,297; Nursery Worker = 7,222; Field Workers = 6,251).

---

## YoY Trend

| FY | Requested | Certified | Cert YoY | Apps Rcvd | Apps YoY |
|----|-----------|-----------|----------|-----------|----------|
| FY22 | 382,354 | 371,619 | — | ~20.6K | — |
| FY23 | 389,908 | 378,513 | +1.9% | 20,881 | +1.4% |
| FY24 | 391,590 | 384,900 | +1.7% | 22,623 | +8.3% |
| FY25 | **415,496** | **398,258** | **+3.5%** | 24,725 | +9.3% |
| FY26 YTD | n/a | n/a | — | n/a (OFLC FY26 Q1 released but XLSX not yet in Wayback) | — |

Source: DOL H-2A Selected Statistics PDFs, FY22–FY25 Q4.

---

## Data Quality Notes

| Item | Status |
|------|--------|
| DOL `www.dol.gov` behind Akamai bot wall | .xlsx requests return 1,886-byte challenge HTML; .pdf passes. Scripted ingestion via direct URL **will not work**. |
| Wayback Machine CDX API | Reliable; current script uses it. FY25 Q4 snapshot archived 2026-01-13 (80 MB XLSX, byte-identical). |
| FY26 Q1 (Oct-Dec 2025) XLSX | DOL released per AILA/BAL news but **not yet archived in Wayback** as of today. Script auto-falls back to FY25 Q4. |
| Release lag | OFLC publishes ~5-6 weeks after quarter close. Wayback lag adds another 2-4 weeks. Effective MARCO lag: **~2 months behind quarter close.** |
| Revisions | OFLC does not revise prior-quarter files; each FY_QN file is cumulative YTD. Treat FY_Q4 as final. |
| Crop/commodity field missing | Schema has SOC/occupation and job title but no crop code. Real crop detail lives in Addendum A (separate file). |
| Wage offer stat skew | Median ($17.79/hr) is the clean signal. Mean ($113) contaminated by a handful of weekly/monthly wage units mis-stored in WAGE_OFFER; ignore mean. |
| CASE_STATUS variants | "Determination Issued - Certification" (active) and "...Certification (Expired)" both counted as certified (matches DOL PDF methodology). Partial certifications also included. |

---

## Refresh Cadence Recommendation

| Cadence | Action | Rationale |
|---------|--------|-----------|
| **Monthly** (1st of month) | Run `h2a_pull.py`; diff vs prior TSV | Wayback re-crawls DOL roughly monthly; catches new Q files within ~6 weeks of release |
| **Quarterly** (mid-Feb / May / Aug / Nov) | Deep review — update YoY table, regenerate verdict if thresholds shift | Aligns with OFLC release cycle |
| **Event-driven** | Re-run immediately on: DHS enforcement action, AEWR revision, ag-labor news story | Catch structural breaks |

Cost: ~$0 (just compute). Runtime: ~90 seconds (80 MB download + pandas aggregation).

**Next MARCO task** (not in scope now): add monthly State Dept H-2A visa issuance pull. The gap between OFLC certified positions and State Dept actual visas issued = unfilled demand, the sharper labor signal.

---

## Threshold Recommendations for VX-H2A-01

Current VX-H2A-01: BREACHED at 415K FY25 certifications.

**Recommended refinement:**

| Tier | Metric | Threshold | Current FY25 | Status |
|------|--------|-----------|--------------|--------|
| Base | H-2A positions certified | >400K | 398,258 | 🟡 1.7K short of breach |
| Base | H-2A positions requested | >410K | 415,496 | 🔴 BREACHED (+5.5K over) |
| Accel | YoY apps received | >10% | +9.3% | 🟡 Near-threshold |
| Accel | YoY positions certified | >5% | +3.5% | 🟢 Below |
| FL-specific | FL worksite workers certified | >55K | 56,818 | 🔴 BREACHED |
| Crisis | Cert / Req gap widening (rejection rate) | >5% gap | 4.1% (17.2K gap) | 🟡 Approaching |

**Proposed VX split:**
- **VX-H2A-01-REQ**: positions requested. Currently 415K. Threshold >410K = breach. FY25 BREACHED.
- **VX-H2A-01-CERT**: positions certified. Currently 398K. Threshold >400K = breach. FY25 not yet breached (fires ~Q2 FY26 based on trajectory).
- **VX-H2A-02-FL**: Florida-specific worksite certifications. >55K breach. FY25 BREACHED at 56,818.

The gap between requested and certified (17,238 positions, 4.1%) is itself a rising signal — if this widens past 5-6% it indicates DOL is getting stricter OR employer applications are deteriorating in quality. Track it.

---

## Script Reference

- Location: `AGENTS/MARCO/tools/h2a_pull.py` (94 lines, stdlib + requests + pandas + openpyxl)
- Output: `AGENTS/MARCO/baselines/h2a_latest.tsv`
- Run: `python3 AGENTS/MARCO/tools/h2a_pull.py`
- Fail mode: loud exit if Wayback has no snapshot OR downloaded file is <1 MB (indicates Akamai bot wall)
- Source URL: `https://web.archive.org/web/<TS>id_/https://www.dol.gov/sites/dolgov/files/ETA/oflc/pdfs/H-2A_Disclosure_Data_FY<YYYY>_Q<N>.xlsx`

To pick up FY26 Q1 when it hits Wayback (est. May-June 2026), no script change needed — CANDIDATES list already tries FY2026 Q1 first.

---

*Pull completed 2026-04-21. Next scheduled refresh: 2026-05-01.*
