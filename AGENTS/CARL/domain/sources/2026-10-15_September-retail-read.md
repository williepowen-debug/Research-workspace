# September 2026 advance retail sales — CARL read (docket row 2026-10-15; T1 trade-down tripwire)

**Written:** 2026-10-15 08:31 ET (`date`), CARL (Claude Code `desk` spawn, Opus 5.5), PROME-directed follow-up inside the approved L672 workstream. **Release:** U.S. Census Bureau, Advance Monthly Sales for Retail and Food Services, September 2026, CB26-165, Thu 2026-10-15 08:30 ET. **Read at the primary:** `marts_current.xlsx` Table 1 fetched 08:30:5x ET (sha256 dd8278fe3224…, saved as `2026-10-15_retail/census-marts-CB26-165-2026-10-15.xlsx`); PDF headline cross-read ($745.0B, +0.8%; August revised $739.3B, +1.3%). FRED had NOT updated at 08:31 ET (RSAFS still the 9/28 benchmark August 737,763), so no FRED cross-check; every figure below is the as-published advance vintage, one report, one vintage. Arithmetic: `2026-10-15_retail/derive.py` → `derived.json` (method = the 10/12 recompute: control = total − 441 − 444 − 447 − 722).

## 1. Cells (SA, $M, as published 10/15)
| Series | Sep-26 (a) | Aug-26 (p) | Jul-26 (r) | Sep-25 (r) | m/m Sep | m/m Aug | y/y Sep |
|---|---:|---:|---:|---:|---:|---:|---:|
| Retail & food services total | 745,021 | 739,322 | 729,915 | 700,948 | **+0.771%** | +1.289% | +6.288% |
| Gasoline stations (447) | 68,021 | 63,950 | 61,509 | 53,119 | **+6.366%** | +3.969% | +28.05% |
| Total ex auto & gas | 537,167 | 535,847 | 529,828 | 511,473 | +0.246% | | |
| **Control group** (derived) | 400,184 | 399,642 | 394,943 | 382,456 | **+0.136%** | +1.190% | +4.635% |
| Control ex nonstore | | | | | +0.067% | | |
| Food & beverage stores (445) | 85,056 | 84,727 | 84,556 | 84,301 | +0.388% | | +0.896% |
| Food services & drinking (722) | 92,906 | 91,882 | 90,652 | 86,837 | +1.114% | | +6.989% |
| General merchandise (452) | 81,776 | 81,844 | 81,233 | 78,476 | −0.083% | | |
| Clothing & accessories (448) | 26,478 | 26,486 | 26,327 | 25,222 | −0.030% | | |
⚠️ Sep-25 and Aug-25 food-services cells are both printed 86,837 (identical, as published); carried, not corrected.

**Read:** September's nominal gain is the pump. Gasoline stations +6.4% m/m (gasoline CPI +9.1%) carried most of the +0.77% headline; the control group rose only **+0.14%** after August's strong **+1.19%**. Deflated roughly by CPI core goods (+0.251% m/m, CUSR0000SACL1E) the control group is **about −0.1% real**; the headline deflated by all-items CPI (+0.649%) is about +0.1% real. ⚠️ These deflations are approximations (the control group includes groceries and services-like nonstore sales; no official real control series). One month, after a strong August; a slowdown, not a contraction, and no cohort split in this release.

## 2. T1 trade-down tripwire (`thesis/TRADEDOWN_INSTRUMENTS.md`; disconfirmation only, never confirmation)
| Leg | Rule (mechanism predicts) | September 2026 | Verdict |
|---|---|---|---|
| T1-a food at home vs away, real y/y | grocery > restaurants | grocery proxy **−0.85%** (445 ÷ CPI food-at-home SA 321.111/315.540) vs restaurants **+3.41%** (722 ÷ CPI food-away 398.783/385.451); spread **−4.27pp** | **AGAINST** |
| T1-b general-merchandise share of retail | share rising | **12.779% (Sep-25) → 12.540% (Sep-26)**; 12.641% Aug | **AGAINST** (falling y/y and m/m) |
| T1-c apparel, real y/y | falling | **+1.56%** (448 ÷ CPIAPPSL 136.875/132.411) | **AGAINST** |
**T1 = 3 of 3 AGAINST for September** (August current-vintage was also 3/3 against). Per the registered rule, T1 is masked by construction and cannot confirm the leg; it does not by itself kill it either — the leg dies on Tier 2 (DG ~Dec) or if Tier 2 also stops showing the signature. **No score, instrument or prediction changes.** Proxies, not measured units (food-store sales vs food-at-home CPI coverage mismatch, as before).

## 3. What it means for CARL's working hypothesis
- Supports the **energy cost-squeeze** mechanism in the narrow sense: nominal dollars went to fuel while core goods spending stalled in real terms in the same month gasoline CPI jumped 9.1%.
- Does **not** support broad downward spending convergence (scope review 10/12 stands): y/y control +4.6% nominal, restaurants +7.0% nominal, and T1 stays against trade-down.
- Next: October advance retail **Tue 2026-11-17** (per the release's "Next release" line).
