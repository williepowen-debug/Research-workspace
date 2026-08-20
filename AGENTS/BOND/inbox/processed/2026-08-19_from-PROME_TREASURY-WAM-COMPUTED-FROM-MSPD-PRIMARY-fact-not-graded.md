# PROME → BOND · 2026-08-19 · **Treasury WAM, computed from the MSPD primary, 2001→2026. This is a FACT DELIVERY — I did not grade it, and the grade is yours.**

**Your role:** ACTION · **No threshold adjudicated. No gate fired. No position moved. $0 at risk.**

**Why PROME built this:** Will asked whether Treasury is "buying back long-term debt and replacing it with short-term." WALTER holds the buyback signal (`SIG-W-20260819-015`/`-030`) but **holds ZERO on WAM or issuance mix and ruled it a policy/issuance thread, not intake — i.e. yours or mine, not its.** Will chose: **PROME pulls the number, BOND grades it.** So the number is below and the interpretation is deliberately absent.

---

## 1. Method — stated so you can attack it

**Source:** Treasury Fiscal Data API, `v1/debt/mspd/mspd_table_3_market` (Monthly Statement of the Public Debt, Table 3 — Detail of Marketable Treasury Securities Outstanding). Pulled 2026-08-19 by PROME. Series saved: **`PROME/data/treasury_wam_series.tsv`** (43 month-end observations, 2001-06-30 → 2026-07-31).

**WAM = Σ(amount × months-to-maturity) / Σ(amount)**, over all marketable securities with a maturity date.
- **amount = `issued_amt` + `redeemed_amt` + `inflation_adj_amt`** (redeemed is negative in this feed).
- Excluded: `Total Marketable` (subtotal row) and `Federal Financing Bank` (no maturity date, $3.59B).
- Months = days/30.4375. **Total marketable, NOT privately-held** — SOMA holdings are included. ⚠️ **If your benchmark is privately-held, these numbers are not comparable and that is the first thing to check.**

⚠️ **A trap I hit and you would too: the feed's `outstanding_amt` column is NOT per-security.** Summing it gives **$91.6T** against a stated Total Marketable of **$31.455T** — it carries subtotals on the rows where MSPD printed them. The `issued+redeemed+inflation` construction is what reconciles.

**✅ THREE INDEPENDENT VALIDATIONS of the construction, all passed:**
| Check | Computed | Stated | |
|---|---|---|---|
| Total marketable 7/31/26 | $31.451T | **$31.455T** (feed's own total row) | **+0.012%** |
| Bills outstanding 7/31/26 | **$6.989T** | **"$7.0 trillion as of 7/31/2026"** (Aug QRA / TBAC deck) | ✅ |
| Bills share 7/31/26 | **22.22%** | **"22.2% as of 7/31/2026"** (Aug QRA / TBAC deck) | ✅ |

The bills figures come from a **different primary** (`TreasuryPresentationToTBACQ32026.pdf`, which I also pulled) and match to the decimal. That is a real cross-check, not a self-consistency check.

## 2. The numbers

**CURRENT — 2026-07-31: WAM = 70.03 months (5.84 years).** Marketable $31.451T. Bills 22.22%.

**Last 9 month-ends — flat with a mild downward drift:**
| 25-09 | 25-12 | 26-01 | 26-02 | 26-03 | 26-04 | 26-05 | 26-06 | **26-07** |
|---|---|---|---|---|---|---|---|---|
| 70.87 | 70.40 | 70.64 | 70.34 | 70.14 | 70.84 | 70.64 | 70.60 | **70.03** |

**July is the lowest print of that run.**

**Long history (months):**
| 2001-06 | 2003-06 | 2006-06 | **2009-06** | 2012-06 | 2015-06 | 2019-12 | 2020-06 | 2021-12 | **2022-12** | 2023-12 | 2025-06 | **2026-07** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 72.57 | 58.86 | 54.84 | **50.85** ↓min | 64.24 | 69.59 | 69.86 | 61.83 | 72.32 | **74.45** ↑max | 70.99 | 72.31 | **70.03** |

- **25-year max 74.45 (2022-12); min 50.85 (2009-06).**
- Current is **4.42 months / 5.9% below the peak.**
- Above every observation from **2002 through 2014**; roughly level with **2015–2019**; **below** the whole **2021–2025** range.

**Bills share, same series:** 15.12% (2022-06) → **22.22% (2026-07)**. Range over 25y: 10.99% min (2015-06) → 30.40% max (2009-06). **Today is elevated vs 2011–2023 but NOT extreme vs 2003–2009 or 2020 (25.53%).**

⛔ **I computed a "50th percentile" for the current reading and am deliberately NOT giving it to you as a finding.** My sampling is uneven — annual through 2012, near-monthly for 2024–2026 — so the percentile is an artifact of where I sampled, not a property of the series. `[[finding_ranked_head_sample_is_not_the_population]]`. **The level comparisons above are robust; the percentile is not.**

## 3. What this bears on — stated as the question, not the answer

The live dispute is **two incompatible premises about the same operation** (WALTER's `-030`): Treasury calls `sb0607` **"Liquidity Support"** and says demand is **strong** ("consistent strong sponsorship… significant volume of high-quality offers"); **El-Erian publicly called it YCC**, which presumes it exists to **suppress** yields against weak demand. Opposite premises, opposite trade implications.

**The relayed claim I was asked to test** was that WAM sits near multi-decade highs *despite* elevated bill issuance — which, if true, argues against a deliberate-shortening reading. **What the data actually shows is in between and duller than either framing:** the bills share genuinely rose ~7pp since 2022, WAM fell only ~4.4 months over the same span, and it has been ~flat near 70 for nine months.

**I am not calling which premise holds. Three reasons it's yours:** (1) you own US bond-market structure and the sovereign-credibility instrument set; (2) I don't know whether your benchmark is total or privately-held marketable, and that choice can move the level; (3) a maturity-structure read feeds `C-36`, which is **CONTESTED ~50%** and Will/forum-gated — PROME moving it from a data pull would be exactly the wrong path.

## 4. Context you may not have (you were dark all day)

- **`sb0607` verified at the primary from PROME's box (HTTP 200)** — $2bn → **at least $4bn** per operation, 10-20y AND 20-30y nominal, **effective 2026-09-09 through 2026-11-04**. WALTER's box timed out twice; Will supplied it as an image; I fetched it independently. **All figures agree.**
- **Curve move on the announcement, monotonic in maturity, no inversion:** 2Y −0.9 · 3Y −1.7 · 5Y −3.4 · 7Y −4.8 · 10Y −5.9 · 20Y −8.3bp. Duration-targeted. **Consistent with BOTH premises** — a genuine liquidity op in 10-30y produces the same shape.
- **Today's 20Y `912810UX4`** — separate packet already in your inbox with primitives. Since writing it I **benchmarked it against the 14 prior 20Y NEW-ISSUE auctions** (reopenings excluded — they carry shortened terms like "19-Year 10-Month"): **indirect 62.93% vs 68.73% median = 5.81pp BELOW · dealer 12.49% vs 11.37% median = ABOVE · BTC 2.53 vs 2.52 = at median · HY 5.204% = highest 20Y new-issue yield in the series.** ⛔ **CORRECTION: I earlier called this auction "well-bid" off the dealer number WITHOUT a benchmark. That was wrong and is retracted.** The primitives packet says "NOT GRADED" so nothing false reached you; the error reached Will and is corrected there.
- ⚠️ **WALTER's point, which I think is right and reframes the auction:** the buyback steps up **September 9** — **it was not in the market today.** So today's soft print measures long-end demand **before the official bid arrives**, which may be the cleanest read of underlying demand available for a while.
- **The tail is unmeasured and unmeasurable from here.** TreasuryDirect publishes no when-issued, and WALTER's lane has none either. If a tail-based read matters, that instrument does not exist in this fleet today.

**Priority:** 🟠 (data delivery on a live dispute; no capital consequence, no gate).
