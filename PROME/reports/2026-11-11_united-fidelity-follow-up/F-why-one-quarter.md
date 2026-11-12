# United Fidelity Bank: why $2.14B moved to nonaccrual in one quarter (leg F)

> ⚠️ **Read with the corrections of 2026-11-12:** `SYNTHESIS.md` in this folder, the paragraphs headed "Correction 2026-11-12" and "Correction 2026-11-12, second". The text below is the researcher's original of 2026-11-11, unchanged; no figure was altered. Three headline readings go past their evidence and are not carried forward as written. Answer 2, "Nothing was maturing": the Call Report bucket counts maturity or repricing and leaves nonaccrual loans out, so it rules out a portfolio-wide maturity wall, not maturities among the affected loans. Answer 3, income that "brought in no cash": the fee receivable grew $83.1M against $76.6M of fees booked, a bridge that does not close, so the line carries other entries and the cash collected is UNRESOLVED. Answer 5, a collateral-value review as the cause: the cause of the one-quarter move is UNRESOLVED; the two hypotheses (a value review, a cash squeeze in the owner group) stay, unranked. Banner added 2026-11-12 14:21 ET by PROME on Will's word (PROME's chat, 2026-11-12 14:18 ET: future use of the unchanged researcher reports carries the corrections). It restates the synthesis corrections and adds no finding.

**Written:** 2026-11-11 20:34 EST (read-only researcher, scratchpad only). **Entity:** United Fidelity Bank, fsb, Evansville IN · RSSD 391575 · FDIC cert 29566. **Units:** $ millions unless marked $K; quarterly income = YTD minus prior YTD.
**Tags:** VERIFIED (read at source this session) · INFERRED · SEARCH-NOT-FOUND (a statement about my search) · UNKNOWN. All read dates 2026-11-11.

## 6-line answer

1. **The loans were current on the record, yes:** multifamily past due and modifications were essentially zero every quarter 2021Q4 to 2026Q2. The bank's books also fit borrowers still paying cash in Q3: loan interest fell only $6.9M, close to the $5.8M of accrued interest that was reversed. VERIFIED (Call Reports); the cash reading is INFERRED.
2. **Nothing was maturing:** at 6/30/2026, $3.09B of loans had 1 to 3 years to maturity or repricing and only $89M fell within 12 months. The drop in that bucket at 9/30 comes from the rule that leaves nonaccrual loans out of it (the buckets sum to gross loans minus nonaccrual, exact to $0.1M). It does not show loans maturing. VERIFIED.
3. **What did change earlier:** net interest income turned negative in 2023Q2 and lost **$120M** over the 12 quarters to 2026Q2. Reported profit rested on related-party income that brought in no cash: the development-fee receivable rose $60M to $147M, more than all the fees booked. Owners put in **$121M** of capital over the same 12 quarters. VERIFIED figures; the "brought in no cash" reading is INFERRED.
4. **Credit protection ended in 2024Q3:** credit default swaps bought by the bank, $868.7M at peak (12/2022) and $586.7M through 6/2024, went to **$0 at 9/30/2024**. That matches AM Best's "discontinued in the third quarter of 2024". The allowance then rose from $40.8M to $81.4M over four quarters, and the bank had its first 90-day delinquency ($3.0M). VERIFIED.
5. **Why it happened in one quarter is not shown by any public document.** The pattern (no delinquency, no maturity, no modification, all at once, written down 14.5%) fits a judgment-driven reclassification after a collateral-value review, most likely under supervisory pressure. INFERRED. No examiner record is public.
6. **Owner-side income is weak:** the bank's earnings, the fee receivable and the $1.03B real-estate venture book all depend on the same sponsor's projects. That makes a sponsor cash squeeze and a forced reclassification hard to tell apart. No sponsor or property distress was found in public news 2024–2026 (SEARCH-NOT-FOUND, weak).

## Sources for the table

- S1: FFIEC CDR public bulk download, "Call Reports — Single Period", tab-delimited, 19 periods 12/31/2021–6/30/2026, https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx (no login; public form). VERIFIED, read 2026-11-11. Parsed by `scripts/parse_bulk.py` → `ufb_hist.json`.
- S2: 9/30/2026 Call Report rows already parsed by DEWEY (`AGENTS/DEWEY/research/2026-11-11_united-fidelity/20260930-rows.json`, last update 2026-10-30). The 9/30 bulk file was not yet on CDR's bulk list (latest 6/30/2026).
- S3: FDIC BankFind financials API, https://api.fdic.gov/banks/financials?filters=CERT:29566 (index built 2026-08-19, latest REPDTE 20260630), used for NIM, earning-asset yield and cost of funds. VERIFIED.
- Cross-check: FDIC and FFIEC values agree on the overlapping items checked (loan income, NII, net income, brokered deposits, allowance). DEWEY's 6/30 rows match the bulk 6/30 file except 5 "CONF" (confidential) cells.

## 1. Quarterly table, 2022Q1–2026Q3 (2021Q4 balances appear in `table_raw.txt`)

| Item | 2022Q1 | 2022Q2 | 2022Q3 | 2022Q4 | 2023Q1 | 2023Q2 | 2023Q3 | 2023Q4 | 2024Q1 | 2024Q2 | 2024Q3 | 2024Q4 | 2025Q1 | 2025Q2 | 2025Q3 | 2025Q4 | 2026Q1 | 2026Q2 | 2026Q3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Total assets $M | 3,367.2 | 4,168.0 | 4,928.5 | 5,651.8 | 5,905.3 | 6,208.0 | 6,183.8 | 6,353.4 | 6,380.8 | 6,380.6 | 6,386.0 | 6,353.1 | 6,332.6 | 6,366.4 | 6,284.2 | 6,295.1 | 6,332.5 | 6,493.3 | 5,915.5 |
| Multifamily loans $M | 1,139.7 | 1,849.8 | 2,431.1 | 3,008.0 | 3,275.0 | 3,392.9 | 3,292.1 | 3,304.3 | 3,291.2 | 3,274.3 | 3,263.1 | 3,219.5 | 3,221.1 | 3,178.8 | 3,163.1 | 3,148.9 | 3,135.8 | 3,089.0 | 2,721.6 |
| Total gross loans $M | 1,557.0 | 2,292.8 | 2,916.8 | 3,517.3 | 3,777.5 | 3,906.0 | 3,797.4 | 3,804.7 | 3,781.3 | 3,750.8 | 3,727.3 | 3,677.7 | 3,666.5 | 3,554.1 | 3,537.7 | 3,516.1 | 3,495.0 | 3,436.1 | 3,059.4 |
| Loan int+fee income, qtr $M | 11.0 | 16.7 | 23.6 | 31.8 | 34.2 | 36.2 | 35.7 | 36.4 | 36.1 | 35.8 | 35.8 | 35.7 | 34.5 | 34.0 | 33.9 | 34.1 | 33.2 | 33.2 | 26.3 |
| Loan yield, annualized % (qtr inc x4 / avg gross loans) | 3.25 | 3.48 | 3.63 | 3.95 | 3.75 | 3.76 | 3.71 | 3.83 | 3.81 | 3.80 | 3.83 | 3.86 | 3.76 | 3.77 | 3.83 | 3.87 | 3.79 | 3.84 | 3.24 |
| Total interest income, qtr $M | 17.1 | 23.4 | 30.5 | 39.0 | 41.7 | 46.9 | 45.7 | 47.2 | 47.6 | 47.4 | 47.3 | 47.3 | 45.5 | 45.1 | 45.1 | 45.7 | 44.3 | 44.8 | 38.4 |
| Total interest expense, qtr $M | 1.9 | 4.5 | 13.0 | 27.6 | 39.9 | 48.1 | 53.4 | 58.4 | 59.8 | 60.0 | 60.5 | 58.7 | 56.2 | 56.1 | 55.8 | 53.6 | 50.5 | 50.2 | 50.6 |
| Net interest income, qtr $M | 15.2 | 18.9 | 17.5 | 11.3 | 1.8 | -1.3 | -7.7 | -11.2 | -12.2 | -12.6 | -13.2 | -11.4 | -10.7 | -11.0 | -10.7 | -7.9 | -6.2 | -5.4 | -12.3 |
| NIM qtr % (FDIC NIMYQ) | 2.41 | 2.42 | 1.81 | 1.01 | 0.15 | -0.1 | -0.6 | -0.86 | -0.93 | -0.97 | -1.01 | -0.89 | -0.84 | -0.87 | -0.85 | -0.64 | -0.5 | -0.43 |  |
| Cost of funding earning assets qtr % (FDIC INTEXPYQ) | 0.3 | 0.57 | 1.34 | 2.45 | 3.23 | 3.75 | 4.13 | 4.48 | 4.55 | 4.6 | 4.65 | 4.56 | 4.42 | 4.43 | 4.45 | 4.32 | 4.07 | 3.98 |  |
| Yield on earning assets qtr % (FDIC INTINCYQ) | 2.72 | 2.99 | 3.16 | 3.46 | 3.38 | 3.65 | 3.53 | 3.62 | 3.62 | 3.63 | 3.64 | 3.67 | 3.57 | 3.56 | 3.6 | 3.69 | 3.57 | 3.56 |  |
| Accrued interest receivable $M | 8.6 | 11.0 | 13.0 | 15.9 | 16.8 | 16.8 | 17.0 | 18.2 | 18.9 | 19.1 | 20.1 | 21.0 | 21.4 | 21.8 | 23.1 | 24.3 | 24.6 | 25.4 | 19.7 |
| AIR in months of total interest income | 1.51 | 1.40 | 1.27 | 1.22 | 1.21 | 1.08 | 1.12 | 1.16 | 1.19 | 1.21 | 1.28 | 1.33 | 1.41 | 1.45 | 1.54 | 1.59 | 1.66 | 1.70 | 1.54 |
| Dev & constr fee receivable $M | 54.6 | 50.8 | 53.6 | 60.2 | 64.3 | 68.4 | 66.5 | 94.2 | 109.4 | 108.4 | 106.5 | 114.3 | 121.6 | 121.0 | 130.4 | 133.7 | 136.5 | 143.3 | 146.7 |
| Dev & constr fee income, qtr $M (RI-E 1h) | n/a | n/a | n/a | n/a | 7.4 | 8.0 | 1.0 | 10.9 | 15.6 | 0.2 | 0.1 | 3.9 | 8.3 | 0.5 | 10.3 | 3.7 | — | 6.9 (H1) | 3.4 |
| RE venture investments $M | 438.5 | 450.0 | 493.2 | 614.8 | 595.6 | 756.4 | 781.5 | 808.6 | 854.4 | 898.8 | 920.4 | 974.9 | 976.0 | 1,016.1 | 1,019.2 | 1,021.9 | 1,035.1 | 1,063.2 | 1,032.0 |
| LP pass-through income, qtr $M (RI-E 1j) | 4.8 | 4.0 | 24.6 | 36.6 | 10.9 | 22.3 | 20.8 | 15.2 | 45.6 | 14.2 | 18.2 | 38.3 | 18.0 | 31.0 | 5.2 | 15.3 | 9.4 | 9.1 | 8.0 |
| Derivative FMV change, qtr $M (RI-E 1i) | 9.0 | 8.7 | 11.9 | -0.1 | -9.8 |  |  |  |  |  | -9.2 |  | -5.9 | -3.5 | -2.5 | -0.4 |  | +3.3 (H1) | 7.5 |
| Other noninterest income, qtr $M (RI 5l) | 23.0 | 23.4 | 49.0 | 50.3 | 14.9 | 45.7 | 36.7 | 21.7 | 72.8 | 20.0 | 2.5 | 53.8 | 26.1 | 33.7 | 18.8 | 24.2 | 16.8 | 24.2 | 26.0 |
| Noninterest income, qtr $M | 29.8 | 61.8 | 68.9 | 50.3 | 59.4 | 46.1 | 36.9 | 21.6 | 73.0 | 20.2 | 3.1 | 54.0 | 26.2 | 36.2 | 26.4 | 30.0 | 20.1 | 27.0 | 26.4 |
| Net income, qtr $M | 21.8 | 47.5 | 53.3 | 30.5 | 32.0 | 13.9 | 4.5 | -4.1 | 31.9 | -8.9 | -21.5 | 8.4 | -13.1 | 0.5 | 3.6 | 3.4 | -3.9 | 1.1 | -246.9 |
| Provision for loan credit losses, qtr $M | 1.8 | 3.0 | 1.8 | 2.3 | 3.0 | 9.7 | 9.1 | 1.0 | 0.8 | 1.2 | 12.0 | 11.0 | 11.7 | 5.9 | 0.5 | 0.0 | 0.0 | 0.0 | 287.1 |
| Allowance (loans) $M | 8.2 | 11.2 | 13.0 | 15.3 | 19.0 | 28.7 | 37.9 | 38.9 | 39.6 | 40.8 | 52.9 | 63.9 | 75.5 | 81.4 | 81.9 | 81.8 | 81.8 | 81.7 | 6.3 |
| Allowance / MF loans % | 0.72 | 0.61 | 0.54 | 0.51 | 0.58 | 0.85 | 1.15 | 1.18 | 1.20 | 1.25 | 1.62 | 1.98 | 2.34 | 2.56 | 2.59 | 2.60 | 2.61 | 2.65 | 0.23 |
| MF 30-89 PD $K | 171 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 140 | 0 | 0 | 0 | 0 | 0 | 177 | 0 | 0 |
| MF 90+ PD $K | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2,997 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| MF nonaccrual $K | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 134 | 129 | 123 | 121 | 121 | 121 | 121 | 2,143,246 |
| Mods to borrowers in fin. difficulty, all, $K (HK25+HK26+HK27+HK28) | 2,099 | 2,058 | 2,045 | 1,672 | 1,664 | 1,548 | 1,226 | 1,135 | 1,080 | 1,014 | 989 | 920 | 389 | 381 | 370 | 0 | 0 | 0 | 11,325 |
| MF mods (K111-K113) $K | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Credit default swaps, bank as beneficiary, notional $M (RC-L C969) | 416.6 | 602.2 | 716.4 | 868.7 | 809.4 | 794.4 | 586.7 | 586.7 | 586.7 | 586.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Loans in maturity/repricing 1-3y $M (excl. nonaccrual) | 42.3 | 47.2 | 44.3 | 57.4 | 69.1 | 80.9 | 80.5 | 84.9 | 83.2 | 81.8 | 75.9 | 103.5 | 357.3 | 1,134.2 | 1,832.3 | 2,691.6 | 2,977.4 | 3,090.2 | 638.7 |
| Loans in maturity/repricing 3-5y $M | 100.6 | 93.7 | 88.6 | 118.2 | 403.1 | 1,237.6 | 1,948.0 | 2,835.5 | 3,109.7 | 3,259.5 | 3,302.5 | 3,228.5 | 2,960.5 | 2,129.3 | 1,410.3 | 529.3 | 241.9 | 80.7 | 14.2 |
| Loans maturing/repricing within 12m (A570+A571) $M | 125.5 | 89.8 | 125.0 | 124.9 | 121.9 | 121.0 | 120.0 | 125.5 | 127.4 | 124.8 | 119.1 | 122.4 | 127.8 | 100.5 | 101.6 | 106.4 | 93.4 | 88.9 | 88.2 |
| Sum of maturity buckets vs gross loans minus nonaccrual $M | 1,554.2 vs 1,554.2 | 2,290.1 vs 2,290.1 | 2,914.0 vs 2,914.0 | 3,514.6 vs 3,514.6 | 3,774.8 vs 3,774.8 | 3,903.8 vs 3,903.8 | 3,794.9 vs 3,794.9 | 3,801.9 vs 3,801.9 | 3,778.3 vs 3,778.3 | 3,747.4 vs 3,747.4 | 3,710.8 vs 3,710.8 | 3,662.3 vs 3,662.3 | 3,648.9 vs 3,648.9 | 3,536.8 vs 3,536.8 | 3,517.4 vs 3,517.4 | 3,497.4 vs 3,497.4 | 3,479.4 vs 3,479.4 | 3,419.9 vs 3,419.9 | 900.3 vs 900.3 |
| ORE $K | 3,066 | 2,821 | 2,821 | 1,664 | 1,655 | 1,655 | 1,420 | 1,420 | 1,420 | 1,252 | 1,105 | 183 | 183 | 57 | 57 | 57 | 0 | 0 | 0 |
| Total deposits $M | 2,239.3 | 3,050.6 | 3,786.5 | 4,348.1 | 4,543.5 | 4,793.7 | 5,159.9 | 5,192.7 | 5,057.8 | 5,178.6 | 5,212.6 | 5,159.8 | 5,184.8 | 5,219.1 | 5,130.1 | 5,113.1 | 5,152.9 | 5,297.4 | 5,046.0 |
| Brokered deposits $M | 360.4 | 872.5 | 1,596.8 | 1,998.3 | 1,884.3 | 2,068.1 | 2,481.6 | 2,525.9 | 2,344.2 | 2,309.8 | 2,209.6 | 2,162.6 | 1,993.3 | 1,934.1 | 1,723.5 | 1,581.1 | 1,225.7 | 1,153.5 | 1,006.5 |
| Preferred dividends declared, qtr $M | 0.91 | 0.92 | 1.84 | 1.75 | 1.90 | 1.90 | 1.90 | 0.64 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| Common dividends declared, qtr $M | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| Capital contributions from owners, qtr $M (RI-E 5a cash + 5b non-cash) | 1.6 | 1.9 | 5.3 | 22.1 | 1.0 | 18.9 | 7.5 | 35.6 | 8.6 | 18.3 | 1.6 | 4.1 | 10.6 | 0.5 | 10.6 | 14.5 | 5.9 | 3.2 | 1.5 |
| Equity capital $M | 289.5 | 360.2 | 389.2 | 443.9 | 479.8 | 511.3 | 496.4 | 545.5 | 591.7 | 595.4 | 600.2 | 597.1 | 599.1 | 604.5 | 621.8 | 648.8 | 643.9 | 652.5 | 389.7 |
| Total capital ratio % | 10.5201 | 11.2018 | 10.3951 | 10.5945 | 11.0544 | 11.5298 | 12.1352 | 12.6753 | 13.4064 | 13.6146 | 13.9057 | 14.2040 | 14.2812 | 14.5380 | 14.6901 | 15.0240 | 14.9695 | 15.0851 | 7.2647 |
| CET1 ratio % | 8.0746 | 6.9508 | 6.8435 | 7.2347 | 7.7494 | 8.0884 | 8.4163 | 9.0087 | 9.7471 | 9.9326 | 9.7681 | 9.8856 | 9.9562 | 10.1677 | 10.5198 | 10.9417 | 10.9853 | 11.0824 | 4.7392 |
| Tier 1 leverage % | 8.0553 | 8.5974 | 8.0704 | 8.0213 | 8.0514 | 8.0942 | 7.9715 | 8.4291 | 9.0520 | 9.1145 | 9.1356 | 9.2431 | 9.3252 | 9.4822 | 9.7733 | 10.0825 | 10.1288 | 10.1619 | 5.8188 |

Notes on the table:
- RI-E itemized items (development fees, LP pass-through, derivative change) are itemized only above a size threshold; a blank cell means the item was not itemized, not that it was zero. Before 2023 the "development fee" line (RI-E 1h) was labelled "Net Rent Income", so it is shown as n/a.
- Loan yield = quarterly loan interest and fees (RIAD4010) × 4 ÷ average gross loans (RCFD2122). Fees and amortized origination fees are included, which is why it runs above the 2.78–3.35% HMDA contract rates.
- "Sum of maturity buckets vs gross loans minus nonaccrual" is a control row: the buckets equal gross loans minus total nonaccrual (RCFD1403) in every period. That proves the buckets exclude nonaccrual loans, so 6/30 → 9/30 the 1–3 year bucket fell because loans went nonaccrual, not because they matured.
- The derivative in RI-E 1i is an interest-rate contract ("variable portion of derivative"; RC-L 8725 interest-rate notional $330M at 9/30). The credit protection is the separate RC-L line C969.

### Arithmetic behind the answer (VERIFIED arithmetic on S1/S2; interpretation tags inline)

| Calculation | Figures | Result |
|---|---|---|
| Cumulative net interest income, 2023Q3–2026Q2 (12 qtrs) | −7.7 −11.2 −12.2 −12.6 −13.2 −11.4 −10.7 −11.0 −10.7 −7.9 −6.2 −5.4 | **−$120.2M** |
| Owner capital contributions, same 12 qtrs (RI-E 5a+5b) | 7.5+35.6+8.6+18.3+1.6+4.1+10.6+0.5+10.6+14.5+5.9+3.2 | **+$121.0M** |
| Net income, same 12 qtrs | 4.5−4.1+31.9−8.9−21.5+8.4−13.1+0.5+3.6+3.4−3.9+1.1 | +$1.9M |
| Negative carry on the loan book, 2026Q2 | loan yield 3.84% − cost of funding earning assets 3.98% (FDIC) | −0.14 pp; ≈ −$4.3M/yr on $3.09B of multifamily loans |
| Negative carry at its widest, 2024Q3 | 3.83% − 4.65% | −0.82 pp; ≈ −$26.8M/yr on $3.26B |
| Bank-wide spread, 2024 full year | interest income $189.6M − interest expense $239.1M | **−$49.5M** |
| 3.0% fixed loan funded at a 4.20–4.45% CD (bank's posted rate, report A) | 3.0 − 4.3 | ≈ −1.3 pp before any operating cost |
| Development-fee receivable vs fees booked, 12/2022 → 6/2026 | receivable 60.2 → 143.3 (+83.1); fees booked 2023 27.3 + 2024 19.7 + 2025 22.7 + 2026H1 6.9 = 76.6 | receivable grew **108%** of fees booked → no net cash collected (INFERRED; the line may carry other entries) |
| Same, Q3 2026 | receivable +3.4 (143.3 → 146.7); fees booked +3.4 | 100% accrued, 0 net cash (INFERRED) |
| LP pass-through income 2023–2026H1 vs venture book | income 69.2+116.3+69.5+18.5 = 273.5; ventures 614.8 (12/22) → 1,063.2 (6/26) = +448.4 | equity-method income largely retained in carrying value (INFERRED; contributions also feed the book) |
| Accrued interest receivable build | 18.2 (12/23) → 25.4 (6/26) = +7.3 while quarterly interest income fell 47.2 → 44.8; months of income 1.16 → 1.70 | weak sign of slower collection (INFERRED; the line includes securities) |
| AIR reversal at nonaccrual | 25.4 → 19.7 = −5.8; one month's interest on ≈$2.5B at 3.3% ≈ $6.9M | reversal ≈ less than one month of interest, consistent with loans current to ~1 month (INFERRED) |
| Q3 loan interest drop vs reversal | 33.2 → 26.3 = −6.9 vs AIR −5.8 | consistent with borrowers continuing to pay cash in Q3 (INFERRED; the cost-recovery vs cash-basis split is not disclosed beyond TEXT4769) |
| Write-down depth | charge-offs 362.5 ÷ (nonaccrual 2,143.2 + 362.5) | **14.5%**, if all charge-offs fell on the nonaccrual set (INFERRED) |
| Implied collateral value fall (illustration) | 85% median LTV at origination (HMDA, researcher's read) × (1 − 0.145) = 72.7% of purchase value retained; at a ~5% cost-to-sell, value ≈ 76.5% of purchase | ≈ **−23%** from purchase, IF loans were written down to collateral value less costs to sell and the median LTV applies. Stacked junior liens would make it deeper. ILLUSTRATION, not a finding |
| Multifamily book change, Q3 | 3,089.0 → 2,721.6 = −367.4 vs charge-offs 362.5 | only ≈$4.9M of net paydowns: no sales or payoffs of size |
| Legal lending limit proxy (15% × total capital, RCFA3792) | 12/2022 486.2 → 72.9 · 9/2024 687.6 → 103.1 · 6/2026 728.4 → 109.3 · 9/2026 402.1 → 60.3 | PROXY ONLY: the statutory base is capital and surplus, near total capital. Example: The Westcott's two liens ($77.9M + $16.3M = $94.2M, report E) exceeded the 12/2022 proxy and exceed the 9/2026 proxy (INFERRED) |

### Amended filings (S1 "Last Date/Time Submission Updated On", VERIFIED)

| Period | Last updated | Reading |
|---|---|---|
| 6/30/2022 | 2022-09-30 | refiled about 2 months after the due date |
| 12/31/2022, 3/31/2023, 6/30/2023 | **all 2023-09-05** | three quarters refiled the same day, 8 weeks before the OCC order (2023-10-31). The order's Art. XII requires refiling Call Reports if the allowance is found miscalculated. Whether this refiling was the cause is INFERRED. Content of the changes UNKNOWN (bulk shows current versions only) |
| **12/31/2025** | **2026-04-27** | refiled ~3 months late, two quarters before the Q3 2026 action. What changed is UNKNOWN. The current 12/31/2025 version shows no multifamily delinquency and an allowance of $81.8M |
| 3/31/2026, 6/30/2026 | 2026-04-30, 2026-07-30 | original-deadline filings; no later amendment |
| 9/30/2026 | 2026-10-30 (DEWEY rows) | original; later amendment possible |

### Where the change shows BEFORE 2026Q3

| Quarter | What changed (VERIFIED in S1/S3) |
|---|---|
| 2022Q4–2023Q1 | Cost of funds jumps 1.34% → 3.23% while the loan book is fixed near 3.7–3.9%; NIM 1.81% → 0.15%. Peak credit-default-swap protection $868.7M (12/2022) |
| 2023Q2 | Net interest income turns negative (−$1.3M), and stays negative every quarter after. Allowance build starts (+$9.7M, +$9.1M). Three earlier quarters refiled 2023-09-05 |
| 2023Q3 | Swap protection cut $794.4M → $586.7M (the order's "diminished credit derivatives' structure", 2023-10-31) |
| 2023Q4 | First quarterly loss (−$4.1M); preferred dividends stop after a $0.64M final payment. Development-fee receivable jumps $66.5M → $94.2M; owners contribute $35.6M |
| **2024Q3** | **Swap protection $586.7M → $0.** First 90+-day multifamily delinquency ($3.0M) plus $0.14M at 30–89 days. Provision $12.0M; interest-rate derivative loss $9.2M; net loss $21.5M |
| 2024Q4–2025Q2 | Provisions $11.0M, $11.7M, $5.9M: allowance on multifamily rises 1.25% → 2.56% of loans. First multifamily nonaccrual ($134K). Remaining terms cross into 1–3 years (3–5y bucket $3.23B → $2.13B) |
| 2025Q4 | 12/31/2025 report refiled 2026-04-27. Brokered deposits keep falling ($2.53B peak 12/2023 → $1.58B) |
| 2026Q1–Q2 | Zero provisions; owner contributions slow to $5.9M and $3.2M; brokered $1.23B → $1.15B. The 6/30 explanation field mentions only rental income |
| 2026Q3 | $2.14B nonaccrual, $362.5M charge-offs, $287.1M loan provision plus $31.9M on other amortized-cost assets (RIADJJ02), allowance drawn down to $6.3M, total capital ratio 15.09% → 7.26% |


## 2. The sister insurer (Pedcor Assurance Company) and the 2023 order

| Claim | Source (source date · read date) | Tag |
|---|---|---|
| AM Best revised Pedcor Assurance's long-term issuer credit rating outlook to **positive from stable**, and affirmed financial strength B++ (Good), outlook stable, and the issuer rating "bbb" (Good) | https://news.ambest.com/pr/PressContent.aspx?refnum=37144&altsrc=2 (2026-03-25 · 2026-11-11) | VERIFIED |
| Reasons: balance sheet strength "strong", operating performance "adequate", business profile "limited", risk management "appropriate". The outlook cites "solid retained earnings, more moderate premium growth, and the **elimination of credit derivative business in 2024**" | same | VERIFIED |
| "Pedcor previously wrote a fair amount of credit derivatives to support its parents' banking operation. This business was discontinued in the third quarter of 2024 and Pedcor no longer has any exposure to credit derivatives." **No reason for stopping is given.** | same | VERIFIED |
| UFB "is working to clear the remaining articles of the consent order and is in compliance with all capital ratios"; "The OCC has thus far not lifted its consent order." Dividends on "$11 million of UFB's non-cumulative perpetual preferred shares held on Pedcor's balance sheet were not declared and paid in 2024 and 2025"; Pedcor "temporarily suspended dividends on the $24.8 million non-cumulative perpetual preferreds due to its affiliates"; AM Best expects the impact of the order "to be limited and temporary" | same | VERIFIED. The Call Reports agree: preferred dividends $0 from 2024Q1 |
| Nothing in the release on the bank's loans, multifamily, affordable housing, or the parent's condition beyond the above | same | VERIFIED (absence within this release) |
| January 2022 assignment of ratings: the captive was set up to insure properties tied to Pedcor Financial Bancorp and to back its banks with a credit default product, and the parent guarantees certain receivables | https://www.businesswire.com/news/home/20220121005476/en/ (2022-01-21) — **403 on fetch**; content seen only as a search summary | INFERRED (snippet only) |
| No AM Best action on Pedcor Assurance dated 2024 or 2025 was found | query: `AM Best "Pedcor Assurance Company" credit rating 2024 OR 2025` | SEARCH-NOT-FOUND. ambest.com archive pages redirect to a bot-check (perfdrive); not followed |

**Bank side of the same contract (S1, VERIFIED):** Call Report RC-L line C969 (credit default swaps on which the bank is beneficiary, i.e. protection bought) was $263.8M (12/2021) → $868.7M (12/2022) → $809.4M → $794.4M → **$586.7M (9/2023–6/2024) → $0 (9/30/2024)**. The bank booked "Amortization of Credit Derivative" as an expense in 2023 ($1.06M through 6/30, $1.54M through 9/30; RI-E). The bank never sold protection (C968 = 0).

**OCC consent order 2023-031, effective 2023-10-31** (https://www.occ.gov/static/enforcement-actions/ea2023-031.pdf, read 2026-11-11, VERIFIED quotes):
- Art. XIII(2)(a): "a plan to address the Bank's current exposure to loans exceeding its legal lending limit inappropriately supported by the diminished credit derivatives' structure;"
- Art. XIII(2)(b): "the inclusion of gross loan balances of loans with credit derivatives to calculate credit concentrations, the ACL, and capital stress tests and update internal policies and procedures to reflect this change;"
- Art. XIII(2)(d)(ii): counterparty analysis must include "an evaluation of the risk that the counterparty could default or deteriorate in creditworthiness before final settlement of contractual obligations."
- Art. X(2)(g): "a plan to address the Bank's current exposure to loans exceeding the Bank's legal lending limit and supervisory LTV limits, with concrete strategies and associated timelines;"
- Art. XII(1)(a): ACL segmentation "including the multi-family housing portfolio … including risk layering". Art. XII also says: "If previously filed call reports are determined to be inaccurate due to a miscalculated ACL, the Bank must refile such call reports within sixty (60) days of this order."
- Art. II findings: unsafe or unsound practices including "concentration risk management; credit review; credit analysis; risk assessment; allowance for credit losses methodology". Art. XVII: "troubled condition". Art. IV: minimums of CET1 8%, leverage 9%, tier 1 10%, total 12%.

**Reasoning (labelled INFERRED, not a finding):**
1. The order says some loans exceeded the legal lending limit and were "supported" by the swaps. That implies the bank had treated swap-covered exposure as reducing what it counted against the limit, or against concentration and the allowance. Art. XIII(2)(b) orders the gross balance used instead. Once the swaps were cut (2023Q3) and then ended (2024Q3), the full gross exposure to each related borrower group counted against capital: concentration, allowance and the lending limit.
2. A captive insurer owned by the same parent cannot transfer risk out of the group. Its claims-paying capacity is the group's own capital. The OCC language on counterparty deterioration points the same way. The protection was therefore always weaker than the notional, and the OCC called it "diminished" in 2023.
3. With protection gone, the bank had three ways to deal with over-limit exposure to related borrowers. It could sell participations (no buyer is visible: report E found no assignments in seven UCC histories). It could have the borrowers refinance elsewhere (no outside lender found). Or it could hold the loans and reserve against them gross. The allowance build of $40.6M over 2024Q3–2025Q2 fits the third. Capital ratios kept rising because owners contributed capital and the book ran down slowly.
4. Q3 2026 nearly halved the lending-limit base (proxy $109M → $60M). The losses therefore push more single-borrower exposures over the limit, so the problem compounds after the event.
5. What the record does NOT show: any link in time between the end of protection (2024Q3) and the nonaccrual (2026Q3), two years later. The loss of protection explains a slow reserve build. It does not by itself explain a one-quarter move of $2.14B.

## 3. Property and sponsor findings, 2024–2026

Delegated to a parallel read-only search pass; full file: `property-news.md` in this folder (about 30 searches and fetches, 2026-11-11). Its tags are relayed, not rechecked by me.

| Finding | Source (source date) | Tag |
|---|---|---|
| **No 2024–2026 public evidence of property-level distress** (fire, code action, condemnation, lawsuit, foreclosure, receivership, tenant-complaint coverage) at any named property | many queries, see file | SEARCH-NOT-FOUND (weak: county deed and court records, the official Indiana WARN list and local newspaper archives not checked) |
| Naples 701 (3531 Plantation Way, Naples, Pedcor-managed) appears listed for sale; LoopNet listing posted 2025-06-03, Crexi listing (broker Horvath & Tremblay) | https://www.crexi.com/properties/1952990/florida-naples-701 (2025-06-03) — **403**, search summary only | UNVERIFIED; sale status UNKNOWN. If it sold, it may be one of the two 2025–2026 deed transfers |
| The second sponsor at 8902 N Meridian St is probably **Birge & Held** (Birge & Held Asset Management, Suite 205). Listings show it managing Dublin Square (Columbus OH) and Flats at Spring Mill Station (Westfield IN); it bought Northlake Village (Noblesville) in 2020 | directory listing, undated | INFERRED |
| Fort Walton Beach: Pedcor bought Greens on 5th (5 Mooney Rd) and Elevate at 604 West for $30.6M combined, 98% and 97% occupied at sale | https://rebusinessonline.com/cushman-wakefield-arranges-30-6m-sale-of-two-apartments-in-fort-walton-beach-florida (2021-10-25) | VERIFIED (purchase context, not distress) |
| The Westcott sold to Pedcor Homes Corporation about 2022-08 | berkadia.com (about 2022-08), search summary | snippet only |
| Address matches: 6308 Panther Ln = Cypress West (Pedcor); 17200 NW 64th Ave appears tied to Lakeridge at the Moors (manager "Locayt", no Pedcor link found); 600 Denton Blvd, Gables Dr Fishers and Creek Stone Way not identified | see file | INFERRED / UNKNOWN |
| Fed action against the bank and its parents reported 2024-06-26 (order dated 2024-06-25). Banking Dive calls it a cease-and-desist; report B records it as written agreement 24-014, executed 2024-06-18 | https://www.bankingdive.com/news/indiana-united-fidelity-bank-federal-reserve-order-occ-capital-planning-risk-management/719921/ (2024-06-26) | VERIFIED article. **The type of action is a discrepancy; report B's reading at the Fed source governs** |
| Bank said it is slowing affordable-housing lending (local coverage of the OCC order) | https://www.youarecurrent.com/2024/02/06/pedcor-owned-united-fidelity-bank-taking-steps-to-address-unsafe-or-unsound-practices/ (2024-02-06) | VERIFIED (relayed). Fits HMDA: originations $2.8B (2022) → $443M (2023) → $0 (2024) |
| Sponsor level: no Pedcor layoffs, WARN notices, lawsuits, portfolio sales, leadership changes or statements about Florida insurance or property taxes | queries in file | SEARCH-NOT-FOUND |
| Florida insurance and tax costs as a driver | — | **No evidence tied to these properties or stated by the sponsor**; not used |

## 4. Candidate explanations, ranked by fit to the evidence (none is established)

| Rank | Explanation | Evidence for | Evidence against | Public record that would confirm or kill it |
|---|---|---|---|---|
| 1 | **Judgment reclassification after a collateral-value review, under examiner pressure.** An appraisal or impairment review of 2021–22 purchases found principal not fully collectible, so the loans went nonaccrual and were written down while still paying | All at once with no delinquency, no maturity and no modification trigger; cash-basis note says "current"; 14.5% write-down ≈ value decline ~23% under the median LTV (illustration); bank in "troubled condition" under an order that targets ACL, concentration and multifamily segmentation; ACL frozen at $81.7M for three quarters, then the jump; 12/31/2025 report refiled 2026-04-27 | No public exam record or OCC statement; the Q3 explanation names no trigger; the timing (why Q3 2026, not earlier) is unexplained | OCC November 2026 enforcement release (amended order, or PCA directive) · the bank or parents' Q4 Call Report text · a parent annual report on NIC · county records showing new appraisals or loan modifications |
| 2 | **Sponsor liquidity squeeze inside the group.** Group-wide related-party income (development fees, LP distributions) stopped being collectible, which exposed the borrowers' and the bank's dependence on the same cash | Fee receivable never paid down (108% of fees booked since 2023 accrued); $1.03B of venture investments in the same projects; owner capital contributions fell from $35.6M (2023Q4) to $1.5M (2026Q3); Fed agreement bars parent distributions and new debt; HMDA originations stop 2024; RIADJJ02 provision of $31.9M on other amortized-cost assets in Q3 (UNKNOWN which asset) | Borrowers appear to have kept paying in Q3 (INFERRED); no layoffs, suits or portfolio sales found; the venture book was written down only $31M | Parent filings on NIC (FR Y-9 type, if filed) · HUD or state tax-credit compliance records · any deed-in-lieu or deed transfer to the bank (the two 2025–26 transfers in report E's sample) · Naples 701 sale outcome |
| 3 | **Loss of credit protection plus lending-limit excess**, a slow-burn cause that set up the event | Swaps $868.7M → $586.7M (2023Q3) → $0 (2024Q3); order Art. XIII language; allowance and delinquency move in the same quarter the swaps end; lending-limit base halves after Q3 | Two-year gap between the end of protection and nonaccrual; protection loss explains reserves, not nonaccrual of loans that were paying | OCC order amendment or termination text · AM Best's full rating report (paid, not used) · a Pedcor Assurance statutory statement (Vermont captive; not public as far as found) |
| 4 | **Negative carry; interest accrued but not collected in cash** | NII negative 14 straight quarters, 2023Q2–2026Q3 (−$120.2M over the 12 from 2023Q3 to 2026Q2); accrued interest receivable rose 1.16 → 1.70 months of income | Loan interest receipts look intact: Q3 interest fell only ≈ the $5.8M reversal; the reversal is under one month of interest; multifamily past due ≈ 0 throughout. Negative carry is the BANK's problem (funding cost), not a borrower default | A Q4 2026 Call Report showing cash-basis interest income collapsing (borrowers stopped paying) or holding up (they pay) |
| 5 | **Balloon maturity or refinance wall** | 250 of 256 loans interest-only balloons (HMDA, researcher's read); remaining terms crossed into 1–3 years during 2025 | At 6/30/2026 only $88.9M of all loans fell within 12 months; the $3.09B sat at 1–3 years (maturities about 7/2027–6/2029). A maturity could have driven a forward-looking collectability judgment but did not occur in Q3 | Loan documents or recorded mortgages with maturity dates (county records) |

Not ranked: Florida insurance or tax cost increases (no property-tied evidence); the 2025–26 deed transfers (identities unknown).

## 5. Searched and found nothing

| Search | Result |
|---|---|
| AM Best Pedcor Assurance actions 2024 or 2025 (web search, query above) | SEARCH-NOT-FOUND; AM Best archive pages behind a bot-check, not followed |
| Any multifamily modification to borrowers in financial difficulty, 2023–2026 (RC-C/RC-N K111–K113, HK25–HK28) | $0 multifamily in every quarter; total modifications fell from $2.1M to $0, then $11.3M of "all other loans" in Q3 2026 (VERIFIED absence in the filings) |
| Multifamily other real estate owned or foreclosure on the books | ORE $0 from 2026Q1 (VERIFIED) |
| Property and sponsor distress, 2024–2026 | see section 3 and `property-news.md` |
| Content of the 2023-09-05 and 2026-04-27 refilings | not public in the bulk data (current versions only); UNKNOWN |

## 6. Open unknowns

- The trigger: who decided, and on what evidence (appraisal, examination, auditor, sponsor event). No public record.
- Whether the $2.14B borrowers are still paying in cash after 9/30 (Q4 2026 Call Report, due about 2027-01-30).
- What the 12/31/2025 refiling changed (2026-04-27).
- What the $31.9M Q3 provision on "other amortized-cost financial assets" covers. The development-fee receivable is a candidate (INFERRED) but is still reported gross at $146.7M.
- The terms of the credit default swaps (reference loans, premium, settlement) and why they stopped in 2024Q3. AM Best gives the date, not the reason.
- Exact legal-lending-limit excess by borrower group (needs loan-level data; the proxy above only illustrates).
- Identity of the two 2025–2026 deed transfers and whether Naples 701 sold.

## Fetch failures (not evaded)

Business Wire 2022 release (403) · pubt.io mirror (503) · news.ambest.com archive page (bot-check redirect, not followed) · Crexi and LoopNet Naples 701 listings (403, relayed). FFIEC CDR bulk download and FDIC API both worked without a login.

## Files

- Table data: `ufb_hist.json` (parsed S1), `qtable.md`, `table_raw.txt`; scripts in `scripts/`; raw zips in `bulk/` (~117MB); OCC order text `dl/ea2023-031.txt`; FDIC pulls `dl/fin_sel.json`.
