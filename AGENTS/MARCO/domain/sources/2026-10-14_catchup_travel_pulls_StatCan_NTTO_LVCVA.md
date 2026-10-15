# MARCO fork — travel-flow catch-up pulls (2026-10-14, pulls 20:22–20:25 EDT)
Scope: StatCan Sep-2026 · NTTO Sep-2026 · LVCVA Aug-2026. **No repo file edited.** StatCan baseline was copied to scratch before the pull and confirmed BYTE-IDENTICAL after (`cmp` + empty `git diff --stat`); the pull ran in-memory via `statcan_travel.pull()`/`to_monthly()`, never `main()`. No BLS API calls.

---
## 1. StatCan SEPTEMBER 2026 — ✅ PUBLISHED (all 30 days present for both legs; Oct = 0 days)
**Source:** StatCan WDS `getDataFromCubePidCoordAndLatestNPeriods`, via `tools/statcan_travel.py` functions. AIR = PID 24-10-0056 coord 1.80.1.0.0.0.0.0.0.0 (v1324883057); LAND_AUTO = PID 24-10-0057 coord 125.65.1.3.3.0.0.0.0.0 (v1545883120). Daily leading-indicator data summed to months (incomplete months dropped; only 2023-09 dropped, 4 days). Pulled 2026-10-14 20:22:13 EDT. Daily points end 2026-09-30.
**Baseline stated:** 2-yr stack = Sep-2026 vs Sep-2024, same series, same leg. TOTAL = AIR + LAND_AUTO (this is how the carried −26.63% is built — reproduced below).

**Basis check (reproduction) — PASS:** `--verify` set Jun/Jul auto & air 2-yr all within 0.05pp (−29.61/−25.03/−28.85/−26.83 vs carried −29.6/−25.0/−28.9/−26.8). **Aug re-pull reproduces exactly:** air −22.67 / auto −27.39 / gap −4.72 / TOTAL −26.63%.

| Month | Air | Air YoY | Air 2-yr | Auto (land) | Auto YoY | Auto 2-yr | Gap (auto−air) | TOTAL | Total YoY | **Total 2-yr** |
|---|---|---|---|---|---|---|---|---|---|---|
| Aug-26 | 438,318 | +3.61 | −22.67 | 2,136,319 | +9.88 | −27.39 | −4.72 | 2,574,637 | +8.76 | **−26.63** |
| **Sep-26** | **415,008** | +11.55 | **−18.70** | **1,474,644** | +5.59 | **−31.11** | **−12.41** | **1,889,652** | +6.85 | **−28.72** |

**TOUR-01 (sustained 2-yr < −25% = BREACHED):** Sep total **−28.72% ⇒ BREACHED, 11th straight month.** The Aug "shallowest since Nov-2025" read did not extend — raw stack deepened 2.09pp, all of it the land leg.

**ID-01 — Sep leg, against the pre-committed letter (both Sep AND Oct must move the gap ≤ −2.5pp from the Aug pre-window baseline −4.72pp):**
- Gap Sep **−12.41pp** ⇒ move **−7.69pp** ⇒ **Sep leg MEETS** (≤ −2.5pp).
- Falsifiers: common-mode? **No** — air IMPROVED (−22.67 → −18.70, +3.97pp) while land WORSENED (−27.39 → −31.11, −3.72pp). Land improves vs air? **No** — the opposite. Neither falsifier fires.
- **ID-01 NOT resolved** — Sep alone cannot resolve it by the letter; the Oct print decides.
- ⚠️ Noise context (from the registered spec): pre-tariff transitions moved the gap mean 4.21pp, **max 7.95pp** — Sep's −7.69pp sits just inside the historical max. Large, but not outside the observed range on a single month.

**⚠️ Calendar-composition check (my construction, NOT MARCO's registered method — context only, the letter grades raw):** Sep-2026 has 8 Sat+Sun days vs 9 in Sep-2024; Aug-2026 had 10 vs 9 (land trips are weekend-heavy: Sep-26 Sunday 320k vs Thursday 145k). Re-weighting each month's mean-per-weekday onto the 2024 calendar:
| | Air 2-yr adj | Auto 2-yr adj | Gap adj | Total 2-yr adj |
|---|---|---|---|---|
| Aug-26 | −24.35 | −29.43 | −5.08 | −28.61 |
| Sep-26 | −16.37 | −27.84 | −11.47 | −25.63 |
⇒ **The raw total-stack DEEPENING Aug→Sep (−26.63 → −28.72) is a calendar artefact; weekday-adjusted it goes the other way (−28.61 → −25.63).** Still < −25% either way ⇒ BREACHED holds on both bases. **The ID-01 gap move survives adjustment** (−6.39pp adj vs −7.69pp raw) — the divergence is not a weekend-count effect. Labour Day falls inside September in both 2024 (9/2) and 2026 (9/7), so no cross-month holiday shift here.
⚠️ Leading-indicator daily data are preliminary and revise; Sep-2023 is incomplete in this pull so no 3-yr check.

---
## 2. NTTO SEPTEMBER 2026 — ✅ PUBLISHED (ADVANCE vintage)
**Source:** trade.gov/i-94-arrivals-program → `Advance_SummaryAnalysis_COR_September_2026.xlsx` (sites/default/files/2026-10/, "CBP, ADIS/I-94, received October 5"), Table A "Total Overseas". 2019 denominator: NTTO `Monthly Arrivals 2000 to Present – Country of Residence (COR)_1.xlsx`, sheet Monthly, OVERSEAS row located by label. Downloaded 2026-10-14 20:22:54 EDT.
⚠️ **Method deviation, disclosed:** the Advance workbook has **only Tables A/B/E — no Table C** (VX-1.02's named table). Used Table A "Total Overseas" instead. **Equivalence verified:** in the Aug Preliminary workbook, Table A Total Overseas = Table C first-block Aug = **3,079,268**; and the historical workbook's OVERSEAS row now carries Sep-2026 (labelled "Preliminary") = **2,703,912**, identical to Advance Table A. Sep YTD − Aug YTD = 24,110,749 − 21,406,837 = 2,703,912 (Jan–Aug unrevised in this vintage).

**Basis check (reproduction) — PASS:** same pull reproduces every carried monthly figure exactly: Jan −16.50 · Feb −14.85 · Mar −14.18 · Apr −26.45 · May −21.40 · Jun −21.04 · Jul −22.87 · **Aug −24.20** (3,079,268 vs 4,062,448) · **YTD Aug −20.73%** (21,406,837 vs 27,005,341).

| | 2026 | 2019 | vs 2019 | YoY (vs 2025) |
|---|---|---|---|---|
| **Sep (Advance)** | **2,703,912** | 3,484,495 | **−22.40%** | −4.33% |
| **YTD Jan–Sep** | 24,110,749 | 30,489,836 | **−20.92%** | −5.67% |

**VX-1.02:** **−22.40% ⇒ CRITICAL (≥15% and <25% below 2019), NOT BREACHED**; YTD −20.92% CRITICAL — month and YTD readings agree, so the period-ambiguity in the band does not bite. **The Jan→Aug widening run BROKE:** Jul −22.87 → Aug −24.20 → **Sep −22.40**. To reach the −25% line Sep would need ≤2,613,371 — it is **90,541 (3.35%) above**.
⚠️ Revision risk: **UNCHECKED** for Advance→Preliminary (no archived Advance Aug to compare). Preliminary→Final for July = **0** (3,085,919 both vintages). Advance excludes Canada and Mexico-land (overseas leg unaffected).
Side note (irrelevant to both legs, which reproduce): the historical workbook's header skips 2021-12 → 2022-10 in month labels.

---
## 3. LVCVA AUGUST 2026 Executive Summary — ✅ PUBLISHED (lapsed ~9/30, now read)
**Source:** lvcva.com/research/visitor-statistics/ → `assets.simpleviewcms.com/simpleview/image/upload/v1/clients/lasvegas/ES_Aug2026_3d0e4c3b-10da-4e90-9d6b-86610adeec6c.pdf`, browser-UA curl + pdfminer. Pulled 2026-10-14 20:24:27 EDT. Text → scratchpad `lvcva/ES_Aug2026.txt`.
**Baseline stated:** LVCVA's own Aug-2026 vs Aug-2025 (total Las Vegas, not Canadian — NV-01's Canadian basis stays unrefreshed).

**Basis check (reproduction) — PASS:** carried YTD-Jul visitors 22,754,200 + Aug 3,034,900 = **25,789,100 = printed YTD-Aug exactly.** Carried YTD-Jul air 30,203,954 + Aug 4,149,332 = 34,353,286 vs printed **34,353,312** (26-pax revision). YoYs recomputed from printed levels: air 4,149,332/4,567,908 = −9.16% ✓; Clark gaming 1,062.187/1,033.209 = +2.80% ✓.

| Metric | Aug-26 | YoY | YTD-Aug YoY | (Jul-26 YoY, carried) |
|---|---|---|---|---|
| Visitors | 3,034,900 | **−4.3%** | −0.1% (25,789,100) | +2.7% |
| Convention | 622,700 | +6.0% | +10.5% | −5.6% |
| Occupancy | 74.1% | −3.4pp | −0.3pp | +1.1pp |
| ADR | $150.32 | **−7.4%** | +1.9% | +1.8% |
| RevPAR | $111.39 | **−11.5%** | +1.5% | +3.2% |
| Strip ADR / RevPAR | $153.15 / $117.93 | −11.4% / −15.8% | +2.0% / +1.8% | — |
| Room nights | 3,461,500 | −3.7% | −0.3% | — |
| **Air en/deplaned (LAS)** | 4,149,332 | **−9.2%** | **−7.1%** (34,353,312) | −7.6% (YTD −6.9%) |
| Clark County gaming | $1,062.2M | +2.8% | +2.4% | +1.5% |
| Strip gaming | $684.1M | +0.7% | +2.9% | +3.6% |
| Auto traffic (I-15/I-11) | pending | — | — | — |

**ES-07 (>5% visitor decline):** −4.3% ⇒ **NOT met (5th read), the closest yet.** (Ledger note: `ES-MARCO-07` itself was resolved DID_NOT_APPEAR 6/30 for its Q2 window; STATUS carries the >5% line as an ongoing reading.)
**Docket letter ("Dollars negative again in Aug ⇒ June was not noise and NV may be entering the next stage"):** **FIRES on the letter for ROOM dollars** — ADR −7.4%, RevPAR −11.5% (deeper than June's −4.9%). **Gaming dollars did NOT turn** (Clark +2.8%, Strip +0.7%) — "dollars" splits into room vs gaming; name which.
⚠️ **Calendar confounder, named by LVCVA itself:** "the absence of Labor Day weekend that largely fell in August last year" + "a less packed event calendar." Labor Day 2025 = Mon 9/1 (Sat 8/30–Sun 8/31 inside Aug-2025); 2026 = Mon 9/7 (whole weekend in Sep-2026). A high-ADR holiday weekend moved out of the comparison month ⇒ **Aug's dollars and visitor declines overstate the underlying move; September should carry the offset.** ⇒ The "next stage" reading is **CONFOUNDED, not established**, by the same logic MARCO applied to June's single-month inversion. AIR −9.2% ≈ June's −9.3% — the durable leg; the holiday shift touches it too but air was already −7.6% in a clean July.
⚠️ **Numeric twin:** Aug-**2025** visitors **3,171,500** vs Jul-**2026** visitors **3,171,600** — different months, 100 apart. Don't let a grep match them.

**LVCVA September 2026: UNAVAILABLE (not yet published)** — the exec-summary page's newest PDF is ES_Aug2026; due ~late Oct.

---
## Summary
| Item | New print | Basis check | Verdict |
|---|---|---|---|
| StatCan Sep (TOUR-01) | Total 2-yr **−28.72%** (air −18.70 / auto −31.11) | Aug −26.63 reproduced exactly | **BREACHED, 11th month**; deepening is calendar artefact (wkday-adj −25.63, still breached) |
| StatCan Sep (ID-01 leg 1) | Gap **−12.41pp** (move −7.69pp; adj −6.39pp) | Aug gap −4.72 reproduced | **Sep leg MEETS ≤−2.5pp; not common-mode; unresolved until Oct** — move near historical max 7.95pp |
| NTTO Sep (VX-1.02) | **−22.40% vs 2019** (2,703,912 vs 3,484,495); YTD −20.92% | Jan–Aug −16.50…−24.20 / YTD −20.73 reproduced | **CRITICAL, not BREACHED**; widening run broke; ADVANCE vintage (no Table C — Table A equivalence verified) |
| LVCVA Aug (ES-07 / NV) | Visitors **−4.3%**, ADR −7.4%, RevPAR −11.5%, air −9.2%, Strip gaming +0.7% | YTD-Jul + Aug = YTD-Aug exactly | ES-07 **NOT met** (5th read); room-dollars letter FIRES but **CONFOUNDED** by Labor Day shift (LVCVA-named) |
| LVCVA Sep | — | — | **UNAVAILABLE** (not yet published, ~late Oct) |
