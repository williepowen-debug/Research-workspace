# Startup threshold check — October 29 evening ET

Pull began 2026-10-30T00:51:31.653072Z (October 29 ET). Raw evidence: observations.json; publisher SKEW_History.csv. Four families read: 12 RED / 8 REGINALD / 11 CREED / 17 HANS. This is a partial scan, not a family-wide clearance or an owner grade.

| Registered instrument | Observation, evaluation and limit |
|---|---|
| HY OAS, FRED BAMLH0A0HYM2 | 314 bp [October 28], latest and requested first-published result agree; returned first_published field equals observation date and is retained as returned, not independently validated as actual release time. Prior 318 [October 27]. FT-02 / REG-T-03 remain in fired state; exit runs <300 ×3 / ≤300 ×5 both 0. 14 bp / 4.7% above exit = unchanged near-exit watch, already carded in 017. REG-T-04 >350 ×3 remains 36 bp away. No fresh onset. |
| CCC OAS | 1,307 bp [October 28]; FT-07 fired/banked, no exit <930 ×3. |
| VIXCLS / ^VIX | FRED 16.91 [October 28], FT-06 exit ≥18 ×5 reset, 0. Vendor ^VIX 17.20 [October 29] is a second witness, not a FRED sustain completion. No observed >30 / +5-point safety-net condition. |
| Cboe SKEW, publisher CSV | 151.80 [October 23], 150.97 [26], 149.22 [27], 148.74 [28]. FT-10 fired, exit <140 ×4 is 0. October 29 absent at pull; no forward-fill or mirror substitution. Prior Cboe block does not apply to this successful current-runtime read. |
| SOFR−IORB | Matched October 28: 3.94−3.90 = +4 bp. REG-T-08 >15 ×3 not met. Later IORB effective rows are not paired with an older SOFR observation. |
| T5YIFR | 2.23% [October 29]; FT-09 >2.55 ×5 not met. |
| Claims, ICSA | 194,000 w/e October 24; FT-05 >250 thousand and REG-T-05 >300 thousand not met. First-release vintage not independently archived here. Monthly CPI FT-08 has no new scheduled release since owner fire. |
| Treasury FT-11 | October 21→28 five-session endpoints: DGS30 5.42→5.37 = −5 bp, not ≤−10.2. Butterfly (2×20Y−10Y−30Y) 0.37→0.40 = +3 bp, not ≤−4. Neither new precondition met. Integer-bp/Decimal arithmetic; no owner classification or weight changed. |
| KRE / WAL | Vendor quote as_of October 29: KRE 72.86 (+1.04%), WAL 77.80 (+2.42%). History pull returns October 29 NULL and complete=false for both; October 28 last complete rows KRE 72.11 / WAL 75.96. Latest quotes are not used to certify missing history closes. REG-T-01 remains unbreached on available complete rows; WAL remains cycle-2 fired/re-entry, exit ≥81.90 ×3 not met on available rows. |
| Cushing, EIA | 26.970 million bbl, w/e October 23; prior 27.594, w/e October 16. Above boundary #3 <20M. Next scheduled weekly print November 4. |
| Oil boundaries / RED Brent | Vendor BZZ26 115.50 is EVENING-NEXT-SESSION (trade date October 30), metadata month unresolved by truncated name. It is not an October 29 settle. No Brent sustain completed; do not inherit the prior midday distance as current. #6/#8 official-settlement grades incomplete; #8 remains December through October 30, January from November 2. #5 Worldscale UNINSTRUMENTED. |
| HANS gas storage | GIE AGSI gas day October 28: fill 74.89%; mean of five same-day AGSI years 89.656%; gap −14.766 pp. HANS-T-08 remains open inside hysteresis dead band, no >−12 exit. Norm economic usefulness remains unvalidated; this arithmetic does not remove owner's composition caveat. |
| HANS TTF | Vendor TTFZ26 97.51 [October 29], month metadata unresolved; not ICE Endex settlement. HANS-F-007 L3 owner fire retains its disputed-settle caveat; no re-grade by WALTER. |
| Remaining HANS / CREED / REGINALD event rows | Owner monthly values retain registry dates, not live quotes. HANS daily sovereign/compound legs not independently pulled; T-12 UNINSTRUMENTED. Event and cohort censuses, REG-T-06 quarterly FHLB and REG-T-07 monthly office DQ not newly graded. No whole-family no-fire claim. |

Calendar rule: sustain counts bridge registered non-sessions; latest evaluated October 21–29 endpoints contain no full-close holiday. No new sustained cross established within completed evidence; no new signal or fire-ledger row owed from these completed checks.
