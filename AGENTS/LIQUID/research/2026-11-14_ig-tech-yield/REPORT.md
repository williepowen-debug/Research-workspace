# IG tech bond yield "highest since 2009": how much is spread, how much is Treasuries

**LIQUID, 2026-11-14 (Saturday), session started 11:25 ET.** Commission: PROME prome-fe brief under C9 (WQ-538 A), from WALTER card **SIG-W-20261114-007 item 1** (Will's bookmark of 2026-11-13). $0. No gate graded, no level, operator or letter changed.

## 0. Answer in four lines

1. **Almost all of it is Treasuries.** Over one year the broad ICE BofA US Corporate index yield rose **+114 bp** (4.82% → 5.96%, November 12, 2025 → November 12, 2026); its spread rose **+6 bp** (83 → 89). **About 95% is the Treasury leg.** Every rating tier and maturity bucket gives 93% to 95% on the same one-year base. Over the last week (November 5 → 12) the spread *tightened* 4 bp while yields rose 25 bp.
2. **"Highest since 2009" is a Treasury fact first.** The 10-year Treasury (FRED DGS10) at 5.10% [November 12] is its highest since **July 2007**; Treasury's par curve has it at **5.15% on November 13**. Moody's Aaa corporate yield 6.12% [November 12] is its highest since **November 2008**. Any high-grade yield index sits near multi-decade highs when the 10-year does.
3. **The tech-specific premium is Oracle, not "AI borrowers".** On State Street fund marks [November 12], Amazon, Alphabet, Meta and Microsoft bonds trade **5 to 26 bp inside** non-tech bonds of matched maturity out to 10 years, and **+17 to +28 bp** wide only beyond 10 years. Oracle trades **+149 to +213 bp** wide of non-tech at every maturity.
4. **Oracle's new notes are below reoffer, but the spread did not move.** The four new notes held in the funds fell 0.97 to 1.74 points from November 5 to November 12, while their spreads moved −5 to +1 bp. The price loss is the Treasury move.

## 1. Sources, observation dates and what I could not reach

| Item | Series / source | Observation date | Status |
|---|---|---|---|
| Bloomberg "IG tech bond index YTW" | Bloomberg US Corporate Technology (terminal) | — | ⛔ **NOT REACHABLE.** No sector index on FRED (FRED series search, 11:26 ET). Level 6.1% is WALTER's read of a tweeted image |
| Bloomberg article ("AI Borrowers Pay Most Since GFC"; Felder quote) | bloomberg.com | — | ⛔ NOT FOUND/READ (web search 11/14: no copy). The quote stays opinion as tweeted |
| Broad IG spread, effective yield, semi-annual yield to worst | FRED ICE BofA BAMLC0A0CM, BAMLC0A0CMEY, BAMLC0A0CMSYTW | November 12, 2026 (latest; November 13 cell publishes Mon November 16) | Read 11:27 ET, latest-revised |
| IG rating tiers (A, BBB), maturity buckets (7–10y, 10–15y, 15y+) | FRED ICE BofA BAMLC0A3CA/…EY, BAMLC0A4CBBB/…EY, BAMLC4A0C710Y/…EY, BAMLC7A0C1015Y/…EY, BAMLC8A0C15PY/…EY | November 12 | Read 11:27 ET. ⚠️ FRED ICE window now starts **2023-11-14** (rolling ~3 years): the October 2023 peak is outside it |
| Long history check | FRED DGS10, DGS30, DAAA, DBAA (Moody's), HQMCB10YR, HQMCB30YR (monthly) | November 12 (daily); October 2026 (HQM) | Read 11:27 ET |
| Treasury par curve | home.treasury.gov daily par yield CSV | November 12 and 13 | 10Y 5.10 / 5.15, 7Y 5.02 / 5.05, 30Y 5.43 / 5.47 |
| Name-level tech bonds | State Street SPIB and SPBO daily holdings xlsx, "As of 12-Nov-2026" | November 12 | Evaluated fund marks, not trades. One date only |
| History of name-level marks | iShares LQD holdings with `asOfDate` | — | ⛔ Returns an HTML page, not the file. Wayback has no SSGA file (redirect only). **So tech-premium CHANGE over time is not measurable here**, except Oracle's new notes against my November 5 read |
| TRACE trades, Bloomberg/ICE sector sub-indices | — | — | ⛔ Terminal-gated (standing §5 caveat) |

## 2. Decomposition on the reachable index (FRED ICE BofA, latest-revised)

Rate leg = change in (effective yield − OAS). This keeps each index's own duration, so it is not the 10-year change.

| Index [Nov 12] | Base | Yield change | Spread change | Rate leg | Spread share |
|---|---|---:|---:|---:|---:|
| US Corporate (all IG), 5.96%, OAS 89 | Nov 12, 2025 | +114 | +6 | +108 | 5% |
| | Dec 31, 2025 | +112 | +10 | +102 | 9% |
| | Feb 23, 2026 (2026 low, 4.71%) | +125 | +9 | +116 | 7% |
| | Nov 5, 2026 | +25 | −4 | +29 | — (spread tighter) |
| BBB, 6.18%, OAS 111 | Nov 12, 2025 | +116 | +6 | +110 | 5% |
| A, 5.79%, OAS 73 | Nov 12, 2025 | +111 | +5 | +106 | 5% |
| 7–10 year, 6.09%, OAS 106 | Nov 12, 2025 | +116 | +8 | +108 | 7% |
| 10–15 year, 6.29%, OAS 107 | Nov 12, 2025 | +106 | +7 | +99 | 7% |
| 15 year+, 6.53%, OAS 107 | Nov 12, 2025 | +89 | +6 | +83 | 7% |

Treasury check, same dates: 7Y +116, 10Y +102, 30Y +76 bp over the year; 10Y +26 bp November 5 → 12, then +5 more to 5.15% on November 13 (par).

**Where the level sits.** The broad IG yield's 2026 high is **6.03% effective / 6.05% YTW on October 5**; November 12 is 5.96% / 5.97%, the highest since October 13. The 10-year's 2026 high was also October 5 (5.31%). Moody's Aaa 6.30% and Baa 6.77% also peaked October 5. With the November 13 Treasury move (+3 to +5 bp across 7–30 years) and a flat spread, the broad index would sit near **6.0% on November 13** — about at, not clearly above, the October 5 high [INFERENCE; the ICE November 13 cell is unpublished]. ⚠️ So if Bloomberg's tech index really made a new high on November 13 above its own early-October level, the excess over the broad index would be tech-specific spread widening since October. I cannot measure that; the chart read is ±0.1 point.

**Is a ~6.1% tech level consistent with the broad index?** Yes. The ICE 7–10 year bucket yields 6.09% and the 10–15 year 6.29% [November 12]. A tech index longer than the broad index (hyperscaler issuance is long-dated) would print about 6.1% with little or no tech premium [INFERENCE].

## 3. Name-level: State Street holdings, November 12 marks

Method: yield from market value ÷ par as a clean price, semi-annual, settlement November 13; spread = yield − Treasury par interpolated (November 12 curve). Same method as `research/2026-11-06_oracle-cds-loop/REPORT.md` §3. 6,216 fixed-coupon bonds, $8.99B, SPIB + SPBO, deduplicated by CUSIP, variable-rate notes and maturities under 200 days excluded. ⚠️ Whether the fund's market value includes accrued interest is not stated. Treated as clean, the whole fund's weighted spread is 84 bp against ICE's 89 OAS; treated as dirty it is 121. The clean reading fits, so it is primary; both are in `tech_output.txt`. Tech-minus-non-tech differences barely change between the two (≤13 bp).

| Group | Bonds | Weighted maturity | Yield | Spread |
|---|---:|---:|---:|---:|
| All holdings | 6,216 | 6.0y | 5.80% | 84 |
| Non-tech | 5,665 | 6.0y | 5.78% | 81 |
| Tech (50-name list) | 551 | 6.6y | 5.99% | 101 |
| AI builders: Oracle, Meta, Alphabet, Amazon, Microsoft | 156 | 7.8y | 6.25% | 124 |
| AI builders excluding Oracle | 103 | 8.0y | 5.77% | 75 |
| Other tech | 395 | 5.6y | 5.79% | 84 |

Matched maturity, spread minus non-tech (bp):

| Maturity | Tech | Builders excl. Oracle | Oracle |
|---|---:|---:|---:|
| 1–3y | +6 | −26 | +149 |
| 3–5y | +11 | −20 | +186 |
| 5–7y | +25 | −5 | +203 |
| 7–10y | +28 | −7 | +201 |
| 10–20y | +46 | +17 | +204 |
| 20–40y | +51 | +28 | +213 |

Issuer averages (spread, weighted maturity): Oracle 273 (7.3y), Meta 111 (8.9y), Broadcom 117, Intel 117, Dell 101, Amazon 67, Alphabet 62, Microsoft 46, Apple 26.

**So what.** A tech index that weights Oracle heavily will show a premium. The other four builders pay a small premium only at the long end, where their jumbo long bonds sit. **Read: rising cost driven by rates, plus one name priced like high yield.** Oracle's average spread (273) is 90 bp wide of the ICE BB index (183, November 12) while Oracle is rated investment grade. That is the existing ORCL fallen-angel map's subject, not a new finding.

**Oracle new notes (issued November 4) against reoffer and against my November 5 read:**

| Note | Reoffer | Nov 5 mark | Nov 12 mark | Pricing spread | Nov 5 spread | Nov 12 spread |
|---|---:|---:|---:|---:|---:|---:|
| 7.000% 2029 | 99.835 | 100.535 | 99.563 | +240 | +228 | +227 |
| 7.450% 2031 | 99.942 | 100.206 | 98.826 | +275 | +281 | +279 |
| 7.850% 2033 | 99.995 | 100.894 | 99.159 | +305 | +298 | +299 |
| 8.650% 2046 | 99.840 | 100.594 | 99.046 | +335 | +332 | +327 |

(The 8.000% 2037 is not in either file. Accrued since issue is 0.17 to 0.22 points; under the dirty reading the spreads are +3 to +6 bp higher.) **All four notes are now below reoffer by 0.27 to 1.12 points, and their spreads are at or inside the pricing spread.** Investors who bought the deal are losing money on the Treasury move, not on Oracle credit. This is the second bond point owed in STATUS §3 (closes that row's bond half; the `dtcc_cds_probe.py` fix stays owed).

## 4. What this does to the open question: has falling price become a financing constraint for AI builders?

| Evidence | Reading | Date / basis |
|---|---|---|
| IG tech yield ~6.1%, "highest since 2009" | Cost is up. ~95% of the broad-index rise is Treasuries | FRED ICE Nov 12; chart read Nov 13 |
| AI builders excl. Oracle | At or inside non-tech spreads to 10y; +17 to +28 beyond | SSGA marks Nov 12 |
| Oracle bonds | ~273 avg spread; new notes below reoffer, spread flat | SSGA marks Nov 12 |
| Oracle 5Y CDS | about 295, flat against 300–302 [Nov 10] | DTCC Nov 12 full file (prior read) |
| CoreWeave 5Y CDS | about 1,065, about 90 tighter than 1,154 [Nov 10] | DTCC Nov 12 full file (prior read) |
| Oracle's $20B raise | Cleared in 7 days, early November | KB-LIQ-153 |
| IG OAS / HY−IG basis | 89 (fails >94), 231 | ICE Nov 12; GATE-LIQ-072 price leg NOT FIRED (graded 11/13, not re-graded) |

**Verdict: no change. Not shown.** The bookmark documents a higher cost of borrowing. That cost is mostly Treasuries, and the debt is still being sold and priced. A financing constraint would need a deal pulled, priced wide of talk, or a lender refusing. The Felder quote ("banks are dumping AI loans") is an opinion I could not read at source. The ING loan auction, bids due November 19 (KB-LIQ-153), is the nearest named test of the bank-loan half. The Nscale "needs more cash" headline (SIG-W-20261114-006 item 3) is VULCAN's and is not a refusal. One real effect: a Treasury-led rise raises the coupon on every new AI bond. If the 10-year holds above 5%, the cost of the IG-funded build goes up with no help from credit. That is a cost story, not a constraint [INFERENCE].

**Gates: none due, none re-graded.** GATE-LIQ-069 (review recommended November 19) and GATE-LIQ-072 (December 31) are unchanged. The HY November 13 cell is out of scope (publishes Monday, November 16).

**For TERRY (via PROME):** the evidence here is against "AI credit is breaking on its own". The move is rates. Oracle's spread is wide but flat, and the approved Oracle put-spread card stays NOT FIRED (WQ-514 A; TERRY's to manage). I see no new credit-specific trade signal. Whether a rates-led rise in AI funding costs is tradeable is TERRY's read; "no card" is a complete answer.

## 5. Reproduce

`decomp.py <dir-with-fred-json>` → `decomp_output.txt`; `tech.py <dir-with-ssga-xlsx>` → `tech_output.txt` (the November 12 State Street files are saved in `data/`, because State Street serves only the latest file; to re-run, point `tech.py` at a directory holding them as `ssga/spib.xlsx` and `ssga/spbo.xlsx`; FRED inputs re-pull by series id).
