# Source check: swap spreads + CFTC positioning (Will: "do the source check on swap spreads and CFTC")

**Written:** 2026-09-28 18:04 ET by BOND · follows items 4–5 of `analysis/2026-09-28_coverage-gap-review.md` · **KB:** `KB-BND-355`

## Verdict
| Item | Free source? | Verdict |
|---|---|---|
| ⚠️ *DEFERRED 19:28 ET 9/28 (Will, `analysis/2026-09-28_WILL-RULING_pulled-deals-EDGAR-swap-spreads.md`): the full daily build waits for a small reproducible validation — comparable timestamps, conventions and credible benchmark agreement. Also corrected: 6 dates were TESTED, 5 produced rows (the 2025 file matched nothing), and the method is a promising feasibility lead, not a validated series (CATO).* | | |
| **Swap spreads** | ✅ **DTCC public swap-trade reports** (CFTC Part 43 public dissemination), daily cumulative file, ~1 year kept | **BUILDABLE.** Method validated on 6 dates, stable and plausible. Moderate build. |
| **CFTC positioning** | ✅ CFTC TFF raw files | **ALREADY COVERED by LIQUID**: `AGENTS/LIQUID/scripts/cftc_tff_rates.py` (built 2026-08-23 to answer BOND's own KB-BND-092 basis-trade question; UST 2Y/5Y/10Y/Ultra-10Y/Bond/Ultra-Bond + SOFR-3M; runs clean 9/28, latest as-of Tue 9/22). **Correction to the gap review: this was not a missing source.** BOND's gap is CONSUMPTION: cite LIQUID's read, do not build a second copy. |

## Swap spreads: what was tested
| Source | Result (2026-09-28 ~18:00 ET) |
|---|---|
| FRED `DSWP2/10/30` (ICE swap rates) | ❌ **dead: last obs 2016-10-28** |
| FRED ICE rate variants | ❌ HTTP 400 |
| Chatham Financial market-rates page | ⚠️ HTTP 200, but no swap rates in the static HTML (JS-rendered; not pursued) |
| **DTCC PPD** `pddata.dtcc.com/ppd/api/report/cumulative/cftc/CFTC_CUMULATIVE_RATES_YYYY_MM_DD.zip` | ✅ **200, ~1.3–2.5MB/day, ~24.5k rate trades/day; available 2025-09-25 → 2026-09-25, 2024-09-25 = 404; the same-day file is not yet out at 18:00 (the 9/25 file is stamped 20:15)** |

**Method (as tested):** `UPI FISN == "NA/Swap OIS USD"` · underlier contains SOFR · `NEWT` + `TRAD` only · non-package · spot-starting (effective ≤7 days after execution) · tenor within ±0.1y of 10/30 · **median** fixed rate − the Treasury official par yield for the same date.

| Date | 10Y swap spread | 30Y swap spread | n (10Y / 30Y) |
|---|---:|---:|---:|
| 2026-03-25 | −46bp | −79bp | 116 / 50 |
| 2026-06-25 | −42bp | −73bp | 177 / 40 |
| 2026-08-25 | −36bp | −68bp | 132 / 77 |
| 2026-09-24 | −43bp | −73bp | 232 / 91 |
| 2026-09-25 | −38bp | −67bp | 218 / 107 |

**First read, INFERENCE on 5 points, not a series:** through the sell-off, spreads have **not** moved more negative. A supply-indigestion or dealer-balance-sheet strain would push Treasuries cheap vs swaps, i.e. spreads more negative. That is consistent with "expensive, not broken", but it is not a test of it until there is a daily series with a base rate.

## Caveats a build must carry
1. **Convention:** SOFR OIS rates are annual act/360; Treasury par is semi-annual. BOND arithmetic: the two adjustments roughly cancel (~+1bp at ~4.8–4.9%). Declare it; don't hide it.
2. **Timing noise:** trades span the day while the Treasury par is a ~3:30 PM snapshot. The 9/24→9/25 30Y −73→−67 (+6bp) may be partly this. **Refinement for the build:** restrict to trades executed ~14:30–15:30 ET and report n.
3. **Off-market tails:** p10 sits far below the median (legacy/restructured trades), so **use the median, never the mean**, and print p10/p90.
4. **History:** ~1 year kept, **and the 2025 files return no matches under this filter (schema/field change, not parsed)**, so the usable base rate starts in 2026 until the older layout is mapped.
5. **No free published swap-spread series exists to cross-check against** *(as found 2026-09-28; re-test: at the swap-spread build, next session)*; the plausibility check is internal stability only.
6. **Lag:** the file is out ~20:00 ET same day, so it's a next-boot read, not intraday.

## Recommendation
- **Swap spreads → build `monitors/swap_spreads.py`** (daily 2/5/10/30Y; median, n, p10/p90; afternoon-window filter; its own ledger so a base rate accumulates; wired into boot_recompute like `rates_context`). Moderate: about one session.
- **CFTC → no build.** Consume LIQUID's `cftc_tff_rates.py` read and cite it `[CONF LIQUID date]` when a BOND auction grade needs the basis-trade leg (FL-BND-13).
