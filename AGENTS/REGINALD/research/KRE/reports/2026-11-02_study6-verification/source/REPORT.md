# KRE Study 6: Independent Verification of the KBWB Holdings Attribution

**Data cutoff:** close of October 30, 2026. **Window:** 63 sessions; returns run 8/4 to 10/30, measured from the 8/3 close.
**Status:** research only. The original Study 6 report is not edited; this document sits beside it. Canonical bank judgments, prediction ledgers and trading authority are untouched.
**Reproduce:** `scripts/fetch.sh` (re-download), then `scripts/run_all.sh`. Every number below appears in `out/log_*.txt` or `out/*.csv`.

---

## 0. Plain-English summary

* **The basic numbers check out.** Over the 63 sessions KRE returned −6.02% and KBWB −8.43%, both with dividends included. KRE was ahead by 2.41 points. If you rebuild KBWB from its actual filed holdings and leave out JPMorgan, Bank of America, Goldman Sachs, Morgan Stanley and Citigroup, the rest of KBWB returned −6.62%. In the October 14–30 rally the rest returned +5.00%. Both numbers reproduce exactly.
* **The "1.81 points" is close but slightly overstated.** It compares a *rebuilt* portfolio with the *actual* ETF, so it includes 0.04 points of ordinary ETF tracking difference (fees, cash, etc.). Comparing like with like gives **1.77 points, or 73% of the gap** (Study 6 said about 75%).
* **The component breakdown is wrong as presented.** Study 6's BAC, GS+MS and JPM+C figures were each worked out by removing *one group at a time*. Numbers made that way do not add up to the effect of removing all five together. When you remove one group, the benchmark it is compared against still contains the other weak big banks. This is the whole reason 1.45 ≠ 1.81. A breakdown that does add up gives **BAC +1.04, GS+MS +0.90, JPM+C −0.17** (plus 0.04 tracking), which sums to 1.81.
* **It is really three banks, not five.** Bank of America, Goldman Sachs and Morgan Stanley pulled KBWB down. JPMorgan did *better* than the rest of KBWB and works against the story. Citigroup was roughly neutral.
* **"Most of the gap" depends on the exact dates.** With the same 8/3 start, the five-bank share is 37% if you stop at 10/14, about 51% if you stop at 10/22–10/27, and 73% if you stop at 10/30. Holding the 10/30 end fixed and moving the start date gives 41–98%. From 8/3 to the 10/14 low, removing the five banks changes KBWB by only 0.34 points.
* **It does not explain the unusual daily correlation.** Even after removing the five banks, KRE's 63-day correlation with the rest of KBWB is 0.82. That is the lowest of any comparable window since 2015.
* **It does not say *why*, or whether it will last.** This is bookkeeping: which holdings the gap came from. It says nothing about the reasons those stocks fell or what they will do next.

---

## 1. Sources and holdings dates (exact)

| Item | Source | Date / identifier |
|---|---|---|
| KBWB holdings, June-rebalance share set | SEC Form **N-PORT-P**, Invesco Exchange-Traded Fund Trust II (CIK 1378872), series "Invesco KBW Bank ETF" (S000034530), accession **0001378872-26-001970**, filed 2026-10-30 — https://www.sec.gov/Archives/edgar/data/1378872/000137887226001970/primary_doc.xml | Report period **2026-08-31**. 24 common stocks + Invesco Gov't & Agency MMF (0.12%), 74 E-mini Financial Select futures, securities-lending vehicles. Net assets $6,766,699,597.93. Monthly NAV total returns: Jun +7.262%, Jul +3.302%, Aug −0.731%. |
| KBWB holdings, September-rebalance share set | Invesco holdings API (CUSIP 46138E628) — https://dng-api.invesco.com/cache/v1/accounts/en_US/shareclasses/46138E628/holdings/fund?idType=cusip&productType=ETF | `effectiveBusinessDate` **2026-10-30**. 24 stocks + IXAZ6 future (75 contracts, 0.19%), AGPXX (0.14%), cash. Saved as `data/kbwb_hold_now.json`. |
| September rebalance timing and rules | KBW Nasdaq Bank Index methodology — https://www.kbw.com/uploads/pdf/indexes-etfs/Methodology_BKX.pdf | Caps: five largest ≤ 8%, all others ≤ 4%. Weights are set from closing prices on the **last trading day of Feb/May/Aug/Nov**. Changes take effect **after the close on the third Friday** of Mar/Jun/Sep/Dec, i.e. **after 9/18/2026**. |
| Fund expenses | KBWB Summary Prospectus, Form 497K, 2025-12-19 — https://www.sec.gov/Archives/edgar/data/1378872/000119312525325636/d54028d497k.htm | Management fee 0.35%, other expenses none, **total 0.35%**. |
| Shares outstanding (for the re-indexing robustness test) | SEC XBRL `dei:EntityCommonStockSharesOutstanding`, cover pages of 10-Q/10-K filed on or before each reference date | Q1-2026 10-Qs (for 5/29) and Q2-2026 10-Qs (for 8/31). |
| Daily prices, dividends, splits | Yahoo Finance v8 chart API (close, ex-dividend amounts, adjusted close) | 1/2/2026 to 10/30/2026 (and 2014+ for the correlation history). No splits in any of the 24 names. |
| KRE NAV | SSGA NAV history — https://www.ssga.com/library-content/products/fund-data/etfs/us/navhist-us-en-kre.xlsx | Daily through 10/30/2026. |

**Not obtained.** I found no daily KBWB NAV series: the Invesco NAV/price endpoints return errors, and the Wayback Machine is blocked from this environment. No intermediate (e.g. 9/30) KBWB holdings file exists publicly. The next N-PORT with public portfolio detail is the 11/30 filing. **These gaps turn out not to matter (see §2.2):** the two holdings files are exactly the index's own share sets.

---

## 2. Q1: Can the KBWB holdings reconstruction be verified? **Yes.**

### 2.1 Validation of the holdings files themselves
* N-PORT units × Yahoo 8/31 close reproduce every reported `valUSD` within 0.03%. Invesco units × 10/30 close reproduce `marketValueBase` within 4×10⁻⁸.
* Both files contain the same 24 stocks. Equity is 99.8% (8/31) and 99.7% (10/30) of net assets.

### 2.2 The decisive check: each holdings file is exactly the index's share set
Each set of holdings, priced at the index's rebalance reference date, gives exactly the weights the methodology prescribes:

| Unit set | Priced at | Top-5 weights | Next 8 (capped) |
|---|---|---|---|
| N-PORT 8/31 | **5/29/2026** (last trading day of May → June rebalance) | 8.001, 8.001, 8.001, 8.001, 8.000 | 4.001, 4.000 … 4.000 |
| Invesco 10/30 | **8/31/2026** (last trading day of Aug → Sept rebalance) | 8.004, 8.000, 8.000, 8.000, 7.999 | 4.001 … 3.999 |

So KBWB fully replicates the index. The share count per stock is fixed between rebalances, and creations and redemptions scale every holding in proportion. Over the window that means exactly **one** holdings change: the 8/31 N-PORT share set applies through the 9/18 close, and the 10/30 share set from 9/21 on.

As an independent check, I re-implemented the KBW capping rule from SEC cover-page share counts. It reproduces actual fund weights within **0.004 points** at both reference dates (`out/log_reindex_check.txt`).

What the September rebalance changed (share count per stock, 10/30 vs 8/31, normalised): State Street ×0.86, **BAC ×0.885**, JPM ×0.89, BNY ×0.92 … MS ×1.04, **GS ×1.06**. BAC fell from 8.76% of the fund (8/31) to 6.94% (10/30) through a mix of this rebalance and its price drop.

### 2.3 Daily reconstruction method
* Daily stock total return = (Close + ex-date dividend) / previous close − 1.
* Portfolio return on day t = Σ unitsᵢ·(Pᵢ,t + Dᵢ,t) / Σ unitsᵢ·Pᵢ,t−1. Units are the share set in force at the t−1 close, so weights drift with prices every day.
* Dividends are reinvested on the ex-date (the BKXTR convention). KBWB's own 9/21 $0.46 distribution is handled through Yahoo's adjusted close.
* Fees: 0.35%/252 per day is deducted for the "net" series.

### 2.4 Reconstructed vs actual ETF (cumulative, not just correlation)

| Measure | Value |
|---|---|
| KBWB actual, market-price total return | **−8.435%** (price only −8.892%) |
| Reconstructed, gross | **−8.391%** |
| Reconstructed, net of 0.35% expense | −8.471% |
| Cumulative ETF minus reconstructed: end / max / min along the path | −0.044 / +0.063 (9/8) / −0.101 (9/17) pp |
| By segment, ETF vs reconstructed | 8/3–8/31 −1.721 vs −1.712; 8/31–9/18 −3.449 vs −3.371; 9/18–10/30 −3.503 vs −3.544 |
| Daily correlation / tracking error / largest daily miss | 0.9994 / 3.85 bp per day / 11 bp |
| **Monthly check against N-PORT NAV returns** | July: reconstructed net **3.297** vs NAV **3.302**; August: **−0.736** vs **−0.731** |

The monthly NAV check is the strongest evidence. Reconstructed returns minus the published fee match the NAV returns reported in the N-PORT within about 0.005 points. Over the full window, the ETF's *market-price* return (−8.435) falls between the gross and net reconstructions. The remaining ~0.04 points is plausibly a change in the premium/discount plus securities-lending income and cash/futures drag. It cannot be split further without daily NAV.

**Switch-date sensitivity.** Moving the September switch anywhere from 8/31 to 10/30 changes the reconstructed 63-day return by at most 0.08 points (−8.365 to −8.446). Market-price tracking error barely differs between dates (3.78–4.03 bp/day), so the data alone cannot pin the date, but the methodology does (after 9/18). The date does not affect any conclusion.

---

## 3. Q2: Does removing the five capital-markets banks eliminate most of KRE's lead?

### 3.1 Construction and redistribution assumptions (baseline)
"KBWB ex-five" keeps the **index share counts of the 19 remaining stocks** in each period and drops JPM, BAC, GS, MS and C. Equivalently:

1. Each day, the excluded weight is spread across the remaining 19 **in proportion to their current (drifted) weights**.
2. At the 9/18 rebalance, the remaining names take their new September share counts. Their relative weights are what the index set at 8/31 prices, renormalised to 100%.
3. The KBW 8%/4% caps are **not** re-applied to the 19 names. That variant is test F in §5.
4. Dividends and switch timing are the same as in the full reconstruction.

### 3.2 Results

| | 63 sessions (8/3→10/30) | Selloff (8/3→10/14) | Rally (10/14→10/30) |
|---|---|---|---|
| KRE (actual TR) | **−6.021** | −10.550 | **+5.063** |
| KBWB (actual TR) | **−8.435** | −11.469 | +3.427 |
| KBWB reconstructed | −8.391 | −11.406 | +3.404 |
| **KBWB ex-five (reconstructed)** | **−6.619** ✔ (Study 6: −6.62) | −11.066 | **+5.001** ✔ (Study 6: +5.00) |
| KRE minus KBWB (the gap) | **+2.414** ✔ | +0.919 | +1.635 |
| KRE minus KBWB ex-five (what remains) | +0.598 | +0.517 | +0.062 |
| Five-bank effect (ex-five minus reconstructed) | **+1.772** | **+0.340** | +1.597 |
| Five-bank effect as Study 6 measured it (ex-five minus *actual* ETF) | +1.816 ✔ (Study 6: 1.81) | +0.403 | +1.574 |

On the full window and its end date, removing the five shrinks KRE's lead from 2.41 to 0.60 points, a reduction of 1.77 (73%). In the rally the lead almost disappears (1.64 → 0.06).

On NAV rather than market prices, KRE's NAV total return is −5.946% (SSGA). KBWB's NAV is estimated at −8.47% (reconstructed net, which matches N-PORT NAV monthly). That makes the NAV-basis gap about 2.5 points and the five-bank share about 70%. This is an estimate, because there is no daily KBWB NAV.

---

## 4. Q3: Reconciling 1.45 vs 1.81

### 4.1 What Study 6 actually computed (reproduced)

| Calculation | Vs actual ETF (Study 6 basis) | Vs reconstructed KBWB | Study 6 displayed |
|---|---|---|---|
| Remove BAC only | 1.025 | 0.981 | 1.04 |
| Remove GS+MS only | 0.774 | 0.730 | 0.78 |
| Remove JPM+C only | −0.381 | −0.425 | −0.37 |
| **Sum of the three separate removals** | **1.418** | **1.286** | **1.45** |
| Remove all five together | **1.816** | **1.772** | **1.81** |

The three displayed components reproduce as **separate, one-group-at-a-time removals** to within about ±0.02. No switch-date or dividend convention I tried reproduces them to the last digit (the closest variants are within ±0.03), so the source of that last-digit difference is unknown. The joint figure reproduces exactly.

### 4.2 Why separate removals cannot add up to the joint removal
In one holding period with group weights w_G, total weight W = Σw_G (≈ 35.5% here), full-fund return R_K and group return r_G:

* Remove group G alone: effect **E_G = w_G (R_K − r_G) / (1 − w_G)**. The group is judged against the *full fund*, which still contains the other weak big banks, and is rescaled by 1/(1 − w_G).
* Remove all groups: effect **E = Σ_G w_G (R_X − r_G)**, where R_X is the ex-five return. Each group is judged against the *19 remaining stocks*, which did better than the full fund.

Combining these gives an exact bridge: **E = Σ_G E_G·(1 − w_G) / (1 − W)**. With average weights (BAC 8.13%, GS+MS 14.93%, JPM+C 12.42%) the bridge gives 1.783, against the exact 1.772. The difference is daily drift and the rebalance. The **interaction term is 1.772 − 1.286 = 0.486 points** (reconstructed basis), or 0.398 on Study 6's ETF basis.

In plain terms, adding up "remove BAC", "remove GS+MS" and "remove JPM+C" counts against three slightly different benchmarks. None of them is the 19-stock portfolio behind the 1.81.

### 4.3 The four calculation types, kept separate

| Method | Five-bank total | BAC | GS+MS | JPM+C | Adds up? |
|---|---|---|---|---|---|
| (a) Arithmetic sum of daily differences (no compounding) | 1.925 | 1.122 | 0.959 | −0.157 | Adds to 1.925, which is **not** the compounded 1.772 |
| (b) **Compounded, linked exactly (recommended)** | **1.772** | **1.038** | **0.899** | **−0.166** | **Yes, zero residual** |
| (c) Separate one-at-a-time removals (Study 6 components) | 1.772 (joint) | 0.981 | 0.730 | −0.425 | **No** (sum 1.286) |
| (d) Sequential removal | 1.772 | 0.98–1.43 | 0.73–1.12 | −0.43 to −0.21 | Yes, but depends on removal order |
| (d′) Shapley (average over all orders) | 1.772 | 1.192 | 0.911 | −0.332 | Yes, order-free, but its components are averages over hypothetical intermediate portfolios |

How method (b) works. Each day the identity X_t − K_t = Σ_{i∈five} w_{i,t−1}(X_t − r_{i,t}) holds exactly, where X is the ex-five portfolio and K the full fund. The daily terms are combined across days with the telescoping link factor A_t = Π_{s<t}(1+K_s)·Π_{s>t}(1+X_s). By construction this sums exactly to compounded X − compounded K. Each bank's component is read as **its weight × (return of the remaining 19 − its own return)**, accumulated over the window.

Rebalance and drift choices change the components by a few hundredths (§5). They do **not** explain the 1.45 vs 1.81 gap. That gap is entirely the difference between method (c) and a joint counterfactual.

### 4.4 Corrected, internally consistent attribution table (63 sessions, method (b))

| Line | Points | Share of gap |
|---|---|---|
| **KRE minus KBWB (actual ETF, total return)** | **+2.414** | 100% |
| KRE minus KBWB ex-five (reconstructed) | +0.598 | 25% |
| Five-bank effect (KBWB ex-five minus KBWB reconstructed) | **+1.772** | **73%** |
| &nbsp;&nbsp;Bank of America | +1.038 | 43% |
| &nbsp;&nbsp;Goldman Sachs | +0.451 | 19% |
| &nbsp;&nbsp;Morgan Stanley | +0.448 | 19% |
| &nbsp;&nbsp;JPMorgan | **−0.239** | −10% |
| &nbsp;&nbsp;Citigroup | +0.074 | 3% |
| ETF tracking (KBWB reconstructed minus KBWB actual) | +0.044 | 2% |
| **Check: sum** | **2.414** | residual 0.000 |

On Study 6's own convention (tracking folded into the five), the components are **BAC 1.04 + GS+MS 0.90 + JPM+C −0.17 + tracking 0.04 = 1.81**.

The same method by sub-period (`out/corrected_attribution_linked.csv`):

| | BAC | GS | MS | JPM | C | Five total | KRE − ex-five | Tracking | Gap |
|---|---|---|---|---|---|---|---|---|---|
| 8/3→10/14 | +0.509 | +0.223 | +0.246 | −0.545 | −0.094 | +0.340 | +0.517 | +0.063 | +0.919 |
| 10/14→10/30 | +0.568 | +0.244 | +0.215 | +0.376 | +0.194 | +1.597 | +0.062 | −0.024 | +1.635 |

### 4.5 Per-stock contribution to KBWB's return (a different question)
This answers "how much of KBWB's −8.39% came from each stock", not "how much of KRE's lead". The table is in `out/kbwb_contrib_63d.csv`. Linked results: BAC −1.60 (stock −19.6%), MS −0.94 (−12.2%), GS −0.94 (−12.5%), M&T −0.44, Citizens −0.39, WFC −0.37, PNC −0.36, C −0.33, JPM −0.31 (−3.9%), … East West −0.02.

Study 6's working figures (BAC −1.69, MS −0.97, GS −0.95, JPM −0.31, WFC −0.35) match an **unlinked arithmetic sum of daily weight × return** (−1.68, −0.98, −0.96, −0.31, −0.35). Those sum to −8.42, not the compounded −8.39. It is a small additional mix of additive daily and compounded figures.

---

## 5. Q4: Robustness

Effects are in points relative to each construction's own full portfolio (`out/robustness_grid.csv`).

| Construction | Remove BAC | Remove GS+MS | Remove JPM+C | **Remove all five** | Remove BAC+GS+MS |
|---|---|---|---|---|---|
| A. Holdings, switch after 9/18 (baseline) | 0.981 | 0.730 | −0.425 | **1.772** | 1.984 |
| B. Holdings, switch after 8/31 | 0.948 | 0.758 | −0.419 | 1.767 | 1.979 |
| C. Holdings, switch after 9/21 | 0.984 | 0.734 | −0.419 | 1.788 | 1.991 |
| D. June share set (N-PORT) throughout | 1.057 | 0.660 | −0.445 | 1.766 | 1.991 |
| E. September share set (10/30) throughout | 0.954 | 0.722 | −0.408 | 1.745 | 1.947 |
| F. KBW caps re-applied to the 19 remaining names | 0.964 | 0.894 | −0.091 | 1.811 | 2.013 |
| G. Fixed 8/3 weights, rebalanced daily | 1.120 | 0.630 | −0.449 | 1.807 | 2.043 |
| I. Baseline, price-only (no dividends) | 0.971 | 0.718 | −0.458 | 1.694 | 1.958 |
| *H. Equal-weight 24 vs equal-weight 19, daily rebalanced (a **different portfolio**, not KBWB)* | *0.544* | *0.404* | *−0.159* | *0.941* | *1.022* |

**Holdings/rebalance treatments (A–G, I).** All realistic treatments land between 1.69 and 1.81 for the five-bank effect. The two most likely (A and F) are 1.77 and 1.81. BAC alone is 0.95–1.12, GS+MS 0.63–0.89, and JPM+C always negative. **Conclusion: robust to construction.**

**Equal weight (H)** roughly halves the effect, because the five drop from about 35% of the portfolio to 21%. That is a statement about a different portfolio, not about KBWB.

**Window choice is the real fragility.**

| Start (base close), end 10/30 | Gap | Five-bank effect | KRE − ex-five | Five-bank share |
|---|---|---|---|---|
| 7/31 | 2.72 | 1.98 | 0.70 | 73% |
| **8/3 (Study 6)** | **2.41** | **1.77** | **0.60** | **73%** |
| 8/14 | 3.79 | 1.73 | 2.06 | 46% |
| 8/31 | 5.28 | 2.74 | 2.50 | 52% |
| 9/11 | 6.24 | 2.53 | 3.74 | 41% |
| 9/14 | 4.20 | 1.76 | 2.44 | 42% |
| 9/30 | 2.34 | 2.03 | 0.27 | 87% |
| 10/14 | 1.64 | 1.60 | 0.06 | 98% |

| End, start 8/3 | 10/14 | 10/21 | 10/22 | 10/23 | 10/27 | 10/28 | 10/29 | **10/30** |
|---|---|---|---|---|---|---|---|---|
| Gap | 0.92 | 0.95 | 3.14 | 3.89 | 2.97 | 1.78 | 1.78 | **2.41** |
| Five-bank effect | 0.34 | 1.23 | 1.61 | 2.03 | 1.51 | 1.23 | 1.50 | **1.77** |
| Share | 37% | 130% | 51% | 52% | 51% | 69% | 84% | **73%** |

The five-bank effect itself is fairly stable at about 1.2–2.7 points once 9/14 is inside the window. The *rest* of the gap (KRE versus the other 19 KBWB banks) swings from −0.3 to +3.7 points depending on the dates. "Five banks explain most of the gap" holds for the 8/3→10/30 window and the rally. It does not hold for many nearby windows. KRE also *trailed* KBWB for the first six weeks, and the five banks were *helping* KBWB until 9/14 (see `out/fig_verification.png`, right panel).

---

## 6. Required conclusions (answered separately)

**1. Which stocks account for KBWB's weaker cumulative return?**
In accounting terms, over 8/3→10/30: **Bank of America (+1.04 points of the gap), Goldman Sachs (+0.45) and Morgan Stanley (+0.45)**. Together that is 1.94 points, more than the 1.77 total for all five, because **JPMorgan (−0.24) beat the other KBWB banks** and offsets part of it. Citigroup (+0.07) was roughly neutral. Removing BAC, GS and MS alone leaves KRE only 0.39 points ahead of the rest of KBWB. The rest of KBWB still trailed KRE by 0.60 points, so this group does not explain everything. These results hold across holdings treatments but depend on the window (§5).

**2. Does that explain the unusually low daily KRE–KBWB correlation?** **No.**

| 63-day correlation with KRE (window ending 10/30) | Value | Percentile since 2015 | Rank among 47 non-overlapping windows |
|---|---|---|---|
| KBWB (actual) | 0.719 | 1.9 | 1st (lowest) |
| KBWB reconstructed | 0.718 | — | — |
| **KBWB ex-five** (holdings; history uses a fixed-weight proxy, r = 0.99997 with the holdings series in-window) | **0.824** | **0.3** | **1st (lowest)** |
| Ex-five, equal-weight | 0.859 | 0.2 | 1st |
| Five-bank basket | 0.445 | 2.3 | 2nd |

Removing the five lifts the correlation from 0.72 to 0.82. Before 2025 the median for the ex-five proxy was 0.96 and its 10th percentile 0.92. The ex-five figure is therefore *more* extreme by percentile than the raw KRE–KBWB figure. Removing the five reduces the variance of the daily KRE–KBWB gap by only 36%. The cumulative-return story and the co-movement anomaly are different phenomena. (This agrees with Study 6's own statement that the capital-markets explanation covers the return gap, not the co-movement.) Caveat: the historical proxy uses today's 19 names at today's weights back to 2015, which introduces survivorship bias.

**3. Does the attribution establish why those stocks underperformed, or whether the weakness will persist?** **No.**
A holdings attribution is an identity: it splits a return difference into weight × relative-return pieces. It does not identify causes. In particular:

* It does not show that a "capital-markets shock" caused the weakness. GS and MS fell about 12% despite strong Q3 results reported in Study 6's sources, and JPM, also a capital-markets bank, did *better* than the rest.
* It does not show that KRE's lead is "really" about big banks rather than regional strength. The remaining lead depends on the window.
* It carries no forecasting content. A 2.4-point 63-day gap is about 0.4 standard deviations of the historical distribution (Study 6 / session-14 estimate, not re-derived here), and the five-bank share moves from 37% to 98% with small date changes.

Any statement about persistence needs a separate, pre-specified test.

---

## 7. Claim-by-claim assessment of Study 6

| Study 6 claim | Verdict | Verified value / note |
|---|---|---|
| KRE −6.02% (8/3→10/30) | **Verified** | −6.021% market-price TR (NAV TR −5.946%) |
| KBWB −8.43% | **Verified** | −8.435% market-price TR. It must be total return: price-only is −8.892%. |
| KRE outperformed by ~2.41 points | **Verified** | +2.414 (NAV basis ≈ +2.5, estimated) |
| KBWB holdings reconstruction is valid | **Verified, with stronger evidence** | Share sets are exactly the index share sets; monthly NAV match within ~0.005 points; cumulative −8.39 vs −8.44 |
| KBWB ex-five returned −6.62% | **Verified** | −6.619%; range −6.58 to −6.70 across holdings treatments |
| Ex-five rally 10/14→10/30 ≈ +5.00% | **Verified** | +5.001% (KRE +5.063%) |
| ~1.81 points (≈75%) attributable to the five | **Corrected** | 1.81 subtracts the *actual* ETF, so it includes 0.044 of tracking difference. Like-for-like figure: **1.77 (73%)**. Robust to construction, **not** to window. |
| Components BAC +1.04, GS+MS +0.78, JPM+C −0.37 as a breakdown of the 1.81 | **Unsupported as an additive breakdown** | The values are (approximately) separate removal effects, which are non-additive (interaction ≈ 0.4–0.5). Correct additive split: **BAC +1.04, GS+MS +0.90, JPM+C −0.17** (+0.04 tracking). |
| Per-stock contributions to KBWB (BAC −1.69, …) | **Minor correction** | Unlinked daily sums; linked BAC −1.60, MS −0.94, GS −0.94 |
| "Five major banks explain most of KRE's relative outperformance" | **Survives only in a narrowed form** | True as *accounting* for the 8/3→10/30 endpoint (73%). In substance it is three banks (BAC, GS, MS), with JPM working against it. It is not robust to start/end date (37–98%), is mostly a late-October phenomenon (0.34 of 0.92 points up to 10/14), says nothing about the correlation anomaly, and is not evidence of cause. |

**Does the original conclusion survive?** **Partly.** The endpoint arithmetic survives almost exactly (1.77 vs 1.81). The breakdown into individual banks does not, as published. The word "five" overstates the case (JPM went the other way). And "most of the outperformance" is true for this specific window, not as a general property of the KRE–KBWB divergence.

---

## 8. Confidence and gaps

* **High confidence:** holdings, rebalance mechanics and timing (exact cap reproduction at both reference dates, an independent re-implementation of the rule, and the methodology document); ex-five −6.62 / +5.00; the joint effect of 1.77–1.81; the algebraic explanation of 1.45 vs 1.81; JPM's negative contribution; the correlation conclusion.
* **Medium:** the split of the ~0.04-point ETF-vs-reconstruction residual (fee vs premium/discount vs securities lending vs futures), because there is no daily KBWB NAV. The exact last digits of Study 6's component values (reproduced only to ±0.02; source of the difference unknown).
* **Source disagreements:** none between primary sources. Yahoo adjusted close and the explicit (close + dividend) method agree to 0.002 points. N-PORT values and Yahoo closes agree within 0.03%.
* **Not covered / out of scope:** KRE's own holdings attribution (KRE is taken as the actual ETF return; KRE's N-PORT for 9/30 is not yet public); any causal or forecasting claim; the correlation history uses a constant-composition proxy, not point-in-time KBWB holdings since 2015.
* **Weakest link in the original claim:** the window. Any downstream use of "75%" should carry the date range.

## 9. File map
* `REPORT.md`: this document. `out/fig_verification.png`: cumulative paths and running gap decomposition.
* `out/corrected_attribution_linked.csv` (§4.4), `out/robustness_grid.csv` (§5), `out/start_date_sensitivity.csv`, `out/end_date_sensitivity.csv`, `out/corr_history.csv`, `out/kbwb_contrib_63d.csv`, `out/daily_reconstruction.csv` (daily KRE, ETF, reconstructed, ex-five, the five's weights, daily contributions and link factors), `out/log_*.txt` (full console output, including `log_validation.txt` for §2 and §4.1–4.3).
* `scripts/`: `load.py` (prices), `holdings.py` (N-PORT/Invesco parsing), `replicate.py` (portfolio engine), `attribution.py` (exact linked attribution), `validate.py` (holdings checks, separate/sequential/Shapley/bridge), `reindex.py` (KBW rule), `robust.py`, `corr_start.py`, `corr_hist.py`, `end_date.py`, `final_tables.py`, `fetch.sh`, `run_all.sh`.
* `data/`: raw inputs as downloaded on 2026-11-02.
