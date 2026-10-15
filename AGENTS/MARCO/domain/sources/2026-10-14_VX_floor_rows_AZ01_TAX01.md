# MARCO fork — VX floor-row refresh pulls: AZ-01 + TAX-01 (2026-10-14, pulls 21:05–21:07 EDT)
Scope: Realtor.com econdata S3 (AZ statewide + Yuma CBSA 49740) and NV Gaming Control Board monthly revenue reports. **No repo file edited.** Data: `scratchpad/rdc/` (two CSVs), `scratchpad/nvgcb/` (mrrmay/jun/jul/aug2026 PDFs + .txt). No BLS calls.

---
## 1. VX-MARCO-AZ-01 — AZ statewide active listings YoY (Realtor.com) — ✅ AUG + SEP 2026 PUBLISHED
**Source:** `econdata.s3-us-west-2.amazonaws.com/Reports/Core/RDC_Inventory_Core_Metrics_State_History.csv` (HTTP 200, 1,885,709 B) + `..._Metro_History.csv` (HTTP 200, 33,492,092 B), pulled 2026-10-14 21:05:49 EDT. Newest month in both = **2026-09**.
**Baseline stated:** active_listing_count, same month vs prior year; graded leg = AZ STATEWIDE (Yuma is context — the band does not grade it).

**Basis check — PASS:** AZ Jul-2026 **28,572, −1.78% YoY** (vendor yy −0.0178; recomputed from levels −1.78) — exact. Yuma Jul-2026 **654**, vendor yy **+8.37%** — exact on the vendor field. ⚠️ Recomputed from the file's own Jul-2025 level (604) Yuma is **+8.28%**, not +8.37% — the vendor's yy field and its levels disagree by 0.09pp (vendor likely computed off an unrevised base). Immaterial; cite the vendor field and note it. No revision to the carried AZ figures.

| Month | AZ active | AZ YoY | Band (letter) | AZ median DOM | AZ median list | Yuma active | Yuma YoY (vendor / calc) |
|---|---|---|---|---|---|---|---|
| Jul-26 (carried) | 28,572 | −1.78% | NORMAL | 67 | $467,000 | 654 | +8.37 / +8.28 |
| **Aug-26** | **28,603** | **+4.45%** | **NORMAL** (−10..+10) | 70 | $459,990 | 651 | +12.82 / +12.82 |
| **Sep-26** | **29,571** | **+6.72%** | **NORMAL** (−10..+10) | 65 | $459,900 | 687 | +17.96 / +18.04 |

- **Direction:** AZ YoY turned positive again (Jul −1.78 → Aug +4.45 → Sep +6.72) — inventory re-building into the season, still 3.3pp inside the +10% ELEVATED line. Median list price drifting down ($478,500 Apr high → $459,900 Sep). Yuma active listings +18% YoY in Sep (687, ~+105 units) — the snowbird town is building faster than the state, but the band does not grade Yuma and the base is tiny.
- **Seasonal/base context (the snowbird season starts ~Oct–Nov):** the 2025 comparators were themselves a big build — AZ YoY Oct-2025 **+23.06%**, Nov-2025 **+18.00%** (Jul-25 +36.30, Aug-25 +29.46, Sep-25 +26.56). So 2026 YoY is measured against an already-elevated 2025 base. 2-yr stacks (context only, NOT the band's basis): AZ Sep-26 vs Sep-24 **+35.07%** (Jul +33.88, Aug +35.23); vs Sep-2019 +36.70%. Yuma 2-yr Sep **+62.80%** (422 → 687); Yuma Oct-2025 YoY +41.93% (vendor) / Nov-2025 +19.77%.
- ⚠️ **Spec observation (flag, not a re-grade):** the band is YoY-only, so the 2025 build (which would have graded CRITICAL/ELEVATED on YoY at the time) is now IN the base — the same base-effect shape MARCO guards against on TOUR-01 and SDL-01. On a 2-yr stack AZ would read +35% (CRITICAL on the band's numbers if they applied). The letter grades YoY ⇒ NORMAL; the parent decides whether this is a spec defect to register.

**AZ-01 verdict on the letter: NORMAL (Sep-26 +6.72% YoY), trend re-building.**

---
## 2. VX-MARCO-TAX-01 — NV percentage-fee tax collections, FY total YoY — ✅ through SEPTEMBER 2026 collections
**Source:** NV GCB monthly revenue reports. ⚠️ **Route change:** `gaming.nv.gov/...` now **301-redirects to `www.gaming.nv.gov/siteassets/content/about/abb-revenue/mrr<mon><yyyy>.pdf`** — bare curl returned 301 / 0 bytes; `-L` follows. Pulled 2026-10-14 21:06:16–21:07:07 EDT: mrrmay2026 200 (750,054 B) · mrrjun2026 200 (253,308 B) · mrrjul2026 200 (747,820 B) · mrraug2026 200 (252,998 B) · **mrrsep2026 → 404** (HTML 37,348 B) ⇒ September WIN report **UNPUBLISHED as of 10/14** (expected ~late Oct), not blocked.
Report convention: report `mrr<M>` = gaming WIN for month M + percentage-fee COLLECTIONS for month M+1 (taxable revenue of M). FY = collection months July–June.

**Basis check — PASS:** mrrjun2026: July-2026 collections **$81,647,636, −6.99%** vs prior-year July **$87,781,999** ✓. mrrmay2026: FY26 total **$1,036,360,553 vs $986,388,785 = +5.07%** ✓ (carried figures $1,036,360,554 / $986,388,787 differ by $1–2 — rounding in the PDF's sum; immaterial). FY26 monthly YoY sequence +25.98 / −0.74 / +33.80 / −12.35 / +5.02 / −5.39 / −2.24 / −7.08 / −3.01 / +17.11 / +14.85 / +19.07 reproduces the carried list exactly.

### 🔴 FINDING — the current month's first print is PARTIAL, and its comparator is FINAL: July's −6.99% revised to −2.31%
Each report's newest collection month is footnoted "through the 21st" (Jul 21 / Aug 21 / Sep 21) and is **revised in the next report**; the prior-year comparator is the **same figure in every report** (Jul-2025 $87,781,999 appears unchanged in mrrjun/jul/aug2026 ⇒ it is the final value).

| Collection month | First print (report) | Revised (next report) | Revision | YoY first → revised |
|---|---|---|---|---|
| **July 2026** | $81,647,636 (mrrjun, "through July 21") | **$85,754,051** (mrrjul + mrraug) | **+$4,106,415 (+5.03%)** | **−6.99% → −2.31%** |
| August 2026 | $98,464,433 (mrrjul, "through Aug 21") | $98,442,120 (mrraug) | −$22,313 (−0.02%) | +3.44% → +3.41% |
| September 2026 | $72,563,543 (mrraug, "through Sep 21") | — (mrrsep not published) | ? | −5.98% (first print) |

⇒ The 8/21 row text says the July −6.99% "is a REAL reported figure" and withdrew the partial-month reading on the grounds that "the prior report carries the identical footnote." **Both reports DO carry the footnote — but it applies to each report's CURRENT month only; the prior-year comparator is final.** The July first print understated by 5.03% and its YoY moved 4.68pp on revision. **n=2 revisions measured (+5.03%, −0.02%) — the bias is real for July but not established as systematic.** ⚠️ The 8/21 skew test (FY26 mean +7.09%, 6/12 negative) was run on the FY26 table, whose earlier months are already-revised values, so it could not detect a first-print bias. Parent's call how to record this against the 8/21 self-correction; the FY-window band rule (which made the 8/21 mark NORMAL anyway) is unaffected.
⚠️ Label anomalies (observed, not interpreted): the 2026-27 tables label the current-year column **"FY26"** and prior **"FY25"** although they hold Jul–Sep **2026** collections vs Jul–Sep 2025 (the May report used the same labels for FY26 vs FY25) — a stale label; YTD resets at the July 2026 collection, so treat as FY27. mrraug2026's prose says September's decline is vs "the prior year's August" and its win sentence compares August 2026 "to August 2026" — prose typos; the tables are consistent. The "$1,829,717 transferable tax credits taken FYTD" line is **identical in all three FY27 reports** (Jul/Aug/Sep collections) — possibly boilerplate carry-over; UNCHECKED.

### FY27 collections (the graded quantity)
| Collection month | FY27 | FY26 (prior) | YoY |
|---|---|---|---|
| July (revised) | $85,754,051 | $87,781,999 | −2.31% |
| August (revised) | $98,442,120 | $95,192,220 | +3.41% |
| September (first print, through 9/21) | $72,563,543 | $77,181,555 | −5.98% |
| **FY27 YTD (Jul–Sep)** | **$256,759,713** | **$260,155,774** | **−1.31%** |

**TAX-01 on the letter: FY27-YTD −1.31% ⇒ NORMAL (decline <5%).** ⚠️ 3 of 12 months; the September leg is a partial first print (if it revises like July, YTD moves toward ~0%; like August, stays ~−1.3%). FY26 full year +5.07% NORMAL.

### Gaming WIN (context leg)
| Area | Aug-2026 | YoY | FYTD Jul–Aug 2026 | FYTD YoY |
|---|---|---|---|---|
| Statewide | $1,266,105,114 | **+3.14%** | $2,653,861,479 | **+2.58%** |
| Clark County | $1,062,187,208 | +2.80% | $2,235,318,495 | +2.12% |
| LV Strip | $684,087,062 | **+0.70%** | $1,460,425,655 | **+2.24%** |
| Downtown | $61,501,577 | −2.96% | $129,969,716 | −6.04% |
July-2026 statewide win $1,387,795,619, +2.07% (mrrjul2026). June-2026 (carried, reproduced): statewide +0.82%, Clark −0.72%, Strip −1.39%; FY26 statewide +2.59%, Strip +1.96%. ⇒ Strip win positive both months of FY27; consistent with LVCVA Aug (gaming +0.7% Strip) — gaming dollars have NOT turned even as LVCVA room dollars fell.

---
## Summary
| Row | New print | Basis check | Verdict (letter) |
|---|---|---|---|
| AZ-01 | AZ active listings **Sep +6.72% YoY** (29,571), Aug +4.45%; Yuma Sep +17.96% | Jul 28,572 / −1.78% and Yuma 654 / +8.37% reproduced (Yuma calc +8.28) | **NORMAL**; re-building into season; 2025 base was a +18..+36% build (2-yr +35%) — YoY-only band may be a spec gap |
| TAX-01 | FY27-YTD collections **−1.31%** ($256.76M vs $260.16M, Jul–Sep) | Jul $81,647,636 −6.99% and FY26 +5.07% reproduced | **NORMAL**; Sep leg partial (−5.98% first print) |
| TAX-01 finding | July first print **revised +5.03% → YoY −6.99% became −2.31%**; Aug revised −0.02% | prior-year comparator identical across reports (final) | the 8/21 "same footnote both sides" reasoning does not hold — current month partial, comparator final (n=2) |
| Win | Aug statewide +3.14%, Strip +0.70%; FYTD +2.58% / +2.24% | Jun/FY26 win reproduced | gaming not turning |
| NV route | `gaming.nv.gov` → 301 → `www.gaming.nv.gov` | — | use `-L` or the www host; mrrsep2026 404 = unpublished |
