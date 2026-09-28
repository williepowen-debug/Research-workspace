# CORAL bankruptcy per-capita instrument (falsify criterion 5)

**Built 2026-09-28** to discharge OQ H — `thesis/THESIS.md` criterion 5 *"Bankruptcy acceleration fades on a per-capita basis"* scored UNGRADED (0) on 8/23 for want of an instrument.

**Inputs (PRIMARY):** AOUSC Table F-2, 12-month rolling (`bf_f2_MMDD.YYYY.xlsx`) and quarterly (`q3m/bf_f2.3_MMDD.YYYY.xlsx`), from `https://www.uscourts.gov/data-news/data-tables/YYYY/MM/DD/bankruptcy-filings/f-2` (quarterly: `…/f-2-three-months`). Take the `.xlsx` link from the page — the file folder changes between years. Census Vintage 2025: `co-est2025-alldata.csv` (county, ~2 MB, not committed — re-download from `www2.census.gov/programs-surveys/popest/datasets/2020-2025/counties/totals/`) and `NST-EST2025-ALLDATA.csv` (`…/2020-2025/state/totals/`).

**Run:** put the two Census CSVs beside the script, then `python3 build_bkcy.py` → `build_output.txt` + `bkcy_extract.json`. It asserts: period + title of every table, 67 counties mapped to N/M/S districts per 28 U.S.C. §89, district populations summing to the FL Census total. `f5a_fl_check.txt` = F-5A county check (99.5–99.9% of each district's filers live in its counties).

**Validation:** national totals reproduce AOUSC press releases exactly (608,511 yr-to-6/30/26; 557,376 yr-to-9/30/25).

## Reading of record — 12 months to 2026-06-30 (pulled 2026-09-28)

| Basis | per 100k | YoY filings |
|---|---:|---:|
| M.D.+S.D. all chapters | **217.1** | +21.2% |
| M.D.+S.D. nonbusiness | 205.5 | +21.1% |
| M.D.+S.D. Ch.7 | 151.5 | +23.6% |
| FL statewide nonbusiness (reproduces the carried "~190", which was 189.6 at 3/31/26) | 199.0 | +21.2% |
| S.D. Fla alone, all chapters | 230.0 | +13.5% |
| US (50+DC) all chapters | 176.3 | +12.3% |

FL/US ratio (M.D.+S.D. all chapters): 1.205× (3/31/26) → **1.231×** (6/30/26). FL growth ~9pp above US.

## ✅ RULED 2026-09-28 (Will): WQ-321 — criterion 5 = leg A absolute (≥5pp below prior-four-table max, two consecutive tables), leg B relative reported only; basis = all chapters M.D.+S.D. · WQ-322 — the ~230/260 LEVEL trigger RETIRED (not replaced); growth-warning rule kept unchanged and unvalidated. The defects below are the history that led there.

## Spec defects as found (history)
1. **Basis is internally inconsistent.** The carried spec says "Ch.7 per capita M.D.+S.D., tripwire >~230/100k", but the "~190" it was anchored on is **statewide NONBUSINESS all-chapter**, and Ch.7 M.D.+S.D. is only 151.5. The basis choice moves the tripwire date by ~1 year.
2. **"Fades" has no number.** Candidate readings: FL YoY ≤ US YoY; or the per-capita YoY increase shrinking two quarters running.

⭐ **Why the 11/15 grade does not wait on either:** on every basis above, FL filings are growing ~+21% YoY, ~9pp faster than the US, and the FL/US ratio is widening. Under any candidate reading of "fades", criterion 5 reads **NOT MET** today. The defects matter for the *tripwire date*, not for the direction.

**Next data:** 12 months to 9/30/2026 — no official calendar; expect late Oct–Nov 2026 (the 9/30/25 table posted 11/19–24/2025). Watch `/2026/09/30/bankruptcy-filings/f-2` from ~10/20.
