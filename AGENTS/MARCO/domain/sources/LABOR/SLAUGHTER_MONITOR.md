# SLAUGHTER MONITOR — Weekly Meatpacking Throughput (SDL-01 leading indicator)

**Owner:** MARCO | **Built:** 2026-04-21 | **Script:** `tools/slaughter_pull.py` | **Data:** `baselines/slaughter_weekly.tsv`

---

## VERDICT

**NO labor-disruption signal currently visible in weekly slaughter data.** Cattle throughput IS down sharply (-11.1% YoY week, -10.2% YoY YTD, z=-2.0 vs 2-year baseline), but this is almost entirely explained by the 75-year-low cattle herd (Jan 2026 inventory 86.2M head, beef cows at 1961 levels, year 8 of cyclical contraction). **Hogs are normal** (+1.3% vs baseline, YTD -0.8%). **Poultry is running hot** (chicken YTD +3%, turkey YTD +6%) — a labor-disruption signal would show the OPPOSITE pattern (hogs and poultry throughput dropping alongside cattle). Current data is **consistent with herd contraction, inconsistent with meatpacking labor crisis**. Monitor for hog/poultry deviations as the tell.

---

## CURRENT WEEK (as of pull 2026-04-21)

| Category         | Week Ending   | Head         | Prior Wk  | YoY same-wk   | 2026 YTD vs 2025 YTD  |
|------------------|---------------|--------------|-----------|---------------|-----------------------|
| Cattle           | 18-Apr-2026   | 514,000      | 512,000   | 578,000 (-11.1%) | -10.2%             |
| Hogs             | 18-Apr-2026   | 2,502,000    | 2,472,000 | 2,367,000 (+5.7%) | -0.8%             |
| Calves           | 18-Apr-2026   | 5,000        | 5,000     | 2,000 (+150%)    | -14.6%             |
| Sheep/Lambs      | 18-Apr-2026   | 34,000       | 30,000    | 45,000 (-24.4%)  | -3.9%              |
| Young Chickens   | 11-Apr-2026   | 171,173K     | 168,174K  | 167,206K (+2.4%) | +3%                |
| Total Turkeys    | 11-Apr-2026   | 3,490K       | 3,151K    | 3,418K (+2.1%)   | +6%                |

---

## 52-WEEK BASELINE (livestock, archived releases Aug 2023 – Sep 2025, n=100)

| Category   | Mean      | StDev    | p10       | p50       | p90       | Min       | Max       |
|------------|-----------|----------|-----------|-----------|-----------|-----------|-----------|
| Cattle     | 590,710   | 38,424   | 544,700   | 602,000   | 631,000   | 434,000   | 647,000   |
| Hogs       | 2,469,460 | 145,822  | 2,323,600 | 2,483,500 | 2,624,300 | 1,846,000 | 2,702,000 |
| Calves     | 4,740     | 645      | 4,000     | 5,000     | 5,000     | 2,000     | 6,000     |
| Sheep      | 36,050    | 3,214    | 32,000    | 36,000    | 40,100    | 27,000    | 45,000    |

Baseline excludes 2026 data. Poultry baseline not yet built (archive has no usable series for NW_PY017 — YoY relies on embedded prior-year row in live file).

---

## CURRENT DEVIATION FROM BASELINE

| Category | Current | Baseline Mean | % Dev  | Z-score | Interpretation          |
|----------|---------|---------------|--------|---------|-------------------------|
| Cattle   | 514,000 | 590,710       | -13.0% | -2.00   | p~2.5 — extreme, but herd-explained |
| Hogs     | 2,502,000 | 2,469,460   | +1.3%  | +0.22   | Normal                  |
| Calves   | 5,000   | 4,740         | +5.5%  | +0.40   | Normal                  |
| Sheep    | 34,000  | 36,050        | -5.7%  | -0.64   | Normal                  |

---

## DEVIATION THRESHOLD FRAMEWORK

Thresholds are **per-species**, applied to single-week head count deviation from 52-week rolling mean, adjusted for known holiday weeks (see Data Quality below). Labor signal requires **multi-species confirmation** because single-species drops can be supply-side (herd cycle) or demand-side (cold-storage buildup).

| Level                   | Threshold                                  | Action                                   |
|-------------------------|--------------------------------------------|------------------------------------------|
| Normal variance         | z ∈ [-1.0, +1.0] OR \|%dev\| < 5%          | No flag                                  |
| Elevated concern        | z ∈ [-1.5, -1.0] OR %dev ∈ [-8%, -5%]      | Log, watch for persistence ≥2 wks        |
| Labor disruption suspected | z ∈ [-2.5, -1.5] AND multi-species drop (hogs OR poultry also down ≥5%) | 🟠 signal to LABOR, CARL             |
| Breach                  | z < -2.5 AND persistent ≥2 wks AND multi-species | 🔴 signal to LABOR, CARL, PROME    |

**Cattle-specific caveat:** Cattle will show z < -1.5 for most of 2026 due to herd contraction. Use **hog z-score as the primary labor signal** (hog herd is stable; any sustained drop is process-driven, not supply). Poultry is the second tell (broiler placements have 6-7 week lead; slaughter gap vs available placements in NW_PY017 flags process friction).

**Hog-specific signal levels (primary labor proxy):**
- Normal: z ∈ [-1, +1] (~2.32M–2.62M/week)
- Elevated: z ∈ [-1.5, -1] (~2.25M–2.32M)
- Labor suspected: z < -1.5 AND YoY < -3% for ≥2 weeks
- Breach: z < -2 AND YoY < -5% for ≥2 weeks (would equate to weekly hogs < 2.18M sustained)

---

## REFRESH CADENCE

**Weekly, Friday evening or Saturday morning.** SJ_LS712 releases Friday ~midday Central for the week ending Saturday. NW_PY017 releases Thursday noon Central for the week ending prior Saturday. Run cron:

```
# Saturday 0900 ET
0 9 * * 6  cd /home/willi/Research-workspace && .venv/bin/python AGENTS/MARCO/tools/slaughter_pull.py
```

Hot-refresh on Friday afternoon if an active signal is being tracked.

---

## DATA QUALITY NOTES

| Issue                | Detail                                                                                    |
|----------------------|-------------------------------------------------------------------------------------------|
| Revisions            | Preliminary week is subject to revision. Prior-week row in next release is the revised estimate. Year-ago row is actual. |
| Holiday weeks        | Watch: week containing Jan 1, Memorial Day (last Mon May), Jul 4, Labor Day (1st Mon Sep), Thanksgiving, Christmas. 2025 Jul 5 week: cattle 474K (-20% vs mean), hogs 1,846K (-25%) — holiday artifact, NOT a signal. |
| Archive gap          | ESMIS archive covers Aug 2023 → Sep 26 2025; no archived per-week files Oct 2025 – Apr 2026. Current week comes from live `.txt`; embedded same-week-prior-year row covers YoY. |
| Poultry history      | Live NW_PY017 has prior-week + same-week-yr-ago + YTD; archive retrieval not built (low priority given no current disruption). Add if poultry YTD turns negative. |
| Report consolidation | SJ_LS711 and SJ_LS710 were consolidated into AMS_3658 (PDF) Dec 2022 — SJ_LS712 remains the weekly text source. |
| MARS API             | MARS API (marsapi.ams.usda.gov) requires registration for JSON access. Current script uses public text files — no key needed. Migrate if AMS kills public txt. |

---

## CROSS-AGENT LINKS

- **LABOR:** slaughter deviations feed meatpacking labor thesis. Minnesota rural meatpacking ICE raids noted in MARCO STATUS — watch for MN/IA state-level confirmation if aggregate moves.
- **CARL:** beef price pass-through from lower cattle throughput (supply-driven right now, not labor-driven) = consumer cost pressure; confirms herd-contraction → grocery inflation channel.
- **BRENT / inputs:** none direct.

---

## APPENDIX — SOURCE URLS

- Livestock live: https://www.ams.usda.gov/mnreports/sj_ls712.txt (Fri ~12:30 Central)
- Poultry live: https://www.ams.usda.gov/mnreports/nw_py017.txt (Thu 12:00 Central)
- Livestock archive: https://esmis.nal.usda.gov/concern/publications/2j62s4898
- Poultry archive: https://esmis.nal.usda.gov/concern/publications/bz60cw27k
- Cattle inventory context: USDA NASS Jan 2026 Cattle report — 86.2M head (75-yr low)
