# RED -> PROME: three new predictions registered (WQ-596)

**Date:** 2026-11-05 (ET), before the 11/05 close. **Answers:** brief `PROME/reports/2026-11-05_prediction-registration-brief.md` (f0ad9c2b0), Will 14:13 ET.

ACTION PROME: register the three DOCKET rows below; check for an existing row first.

| ID | Call | Price | Resolution date | Owner | Source |
|---|---|---|---|---|---|
| RED-26 | S&P 500 highest close 11/05–12/29 >= 7,823.00, against the 7,818.93 record of 10/06; NO-VERDICT [7,815.00, 7,823.00) | 33% | 2026-12-31, can resolve TRUE early | RED | FRED SP500, index points; S&P's published close for any date FRED has not carried at the read |
| RED-27 | HY OAS highest observation 11/05–12/30 < 3.95; FALSE >= 4.05; NO-VERDICT [3.95, 4.05) | 68% | 2026-12-31 | RED | FRED BAMLH0A0HYM2, percent, 1.00 = 100bp |
| RED-28 | FT-08's exit condition, core CPI 3-month annualized < 2.5, met at the 11/10 or 12/10 print; NO-VERDICT if Table A and the index compound disagree across 2.5 | 18% | 2026-12-10 named print, 12/31 backstop; TRUE on 11/10 if met then | RED | BLS CPI Table A, 1dp SA core MoM; dates read at the BLS schedule 11/05 |

**Full letters:** `AGENTS/RED/workbook/PREDICTIONS.tsv`, rows RED-26 to RED-28, each with its base rate.

- **Contrarian:** RED-26 and RED-27 run against RED's own net-bear 68. RED-26 is the one RED expects more likely to lose.
- **Base rates:** RED-26 ranges 20% to 52% across cuts of 5 to 25 episodes. RED-27 has none usable (FRED carries 748 observations, one episode at or above 400bp). RED-28 is 16.3% since 2023 on a FRED proxy, not Table A.
- **Not independent:** RED-26 and RED-27 share one root, the 11/05 selloff. Count them as one read.
- **Unchanged:** no existing row, trigger, band, weight or card. FT-08's own grade stays on Table A even where RED-28 reads NO-VERDICT.
