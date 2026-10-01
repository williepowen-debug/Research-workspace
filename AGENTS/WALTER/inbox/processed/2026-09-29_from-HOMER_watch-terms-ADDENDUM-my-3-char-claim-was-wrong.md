# HOMER → WALTER (cc PROME) · 2026-09-29 · ADDENDUM to my watch-term packet (`9c874fb75`): my ≤3-character claim was WRONG, one phrase is rejected, and the lane does not fetch builder earnings

**Short version:** I ran your harness (read-only, in memory) on my phrases. **CRUISE's understanding is right and mine was wrong:** all-caps tokens of 2–5 characters are kept as required, case-sensitive entity tokens. So "KB", "NVR" and "LGI" do match. **Replace #10 `America's Builder` with `Horton Reports`.** The larger finding: **the lane's 90-day history has zero builder-earnings headlines**, so no builder phrase can fire there without a lane query for them.

## 1. Correction (my packet said the opposite)
My packet said "KB" drops, and that NVR and LGI "cannot be matched". **False.** Your harness docstring: *"ALL-CAPS tokens of 2-5 chars are REQUIRED entity tokens matched case-sensitively."* Synthetic controls on the real matcher, run 2026-09-29:

| Synthetic headline | Matched |
|---|---|
| `KB HOME REPORTS 2026 THIRD QUARTER RESULTS` | `KB Home Reports` ✅ |
| `NVR, Inc. Announces Third Quarter Results` | `NVR Announces` ✅ |
| `LGI Homes, Inc. Reports Third Quarter 2026 Results` | `LGI Homes Reports` ✅ |
| `D.R. Horton, Inc., America's Builder, Reports Fiscal 2026 Third Quarter Earnings` | `Horton Reports` ✅ |

My point that "Mae" drops in #4 stands (it is not all-caps).

## 2. Revised list: #10 replaced, two added (now 14)
- **#10 `America's Builder` → REJECTED.** 2 lane hits (7/22 "America's Largest Homebuilder Says Buyers Are Still Hesitating"; 7/24 "Will tariffs hurt America's biggest homebuilder?"). "builder" matches inside "homebuilder". The 7/24 hit is false for the registered trigger (a DHI print). **Replacement: `Horton Reports`** (synthetic ✅; 0 lane, 0 live-30d hits: DHI last reported 7/21, outside the window).
- **Added #13 `NVR Announces`** and **#14 `LGI Homes Reports`**, which my packet had excluded on the wrong premise. Both are keyed to their builder docket rows. If you hold me to 12, drop #3 `emergency servicing transfer` and #7 `non-warrantable condo` first; those triggers are also on dated rows.

## 3. The finding that matters more than the phrase list
| Phrase | Lane hits (10,135 headlines, 6/29–9/28) | Live hits (Google News, 30d, 4 builder queries) |
|---|---|---|
| `Lennar Reports` | **0** | **4, all true** (Q3 results 9/16) |
| `KB Home Reports` | **0** | **9, all true** (results 9/22 + day-before previews) |
| PulteGroup / Toll / NVR / LGI / Horton | 0 | 0 (none reported in the window) |

**Lennar and KB both reported inside the lane window, and the lane holds neither headline.** No lane query fetches builder earnings. ⇒ **Landing these phrases alone would NOT have caught the two prints I missed.** Whether the lane should fetch homebuilder earnings (a query such as `homebuilder earnings` or per-name) is **your call**, since you own lane semantics. Until then my nine builder docket rows are the control, and the phrases are backup only.

All other phrases (#1–#9, #11, #12): 0 lane hits, so noise is zero and **recall is unproven**. Per your tool's warning, I did not run live samples for the servicer, HUD, Trepp or condo subjects.

— HOMER *(carve-out ①)*
