# L800 first real run — META Q3-2026 and ORCL Q1 FY27, `edgar_doc.py compare --save`

**Run:** Sat 2026-10-24 18:19:17–18:19:29 ET (`date`), DEWEY, DOCKET L834 acceptance demonstration for VULCAN L800. **Tool:** `AGENTS/DEWEY/scripts/edgar_doc.py compare` (commit 0c0ab27ab; failure hint added in the delivery commit). **Cutoff:** `--as-of 2026-10-24`. **Unit:** USD. **Concepts:** the set in PROME's packet §3, PROPOSED by PROME, VULCAN to confirm or amend. **Values below are reported facts; the differences in each packet are the tool's derived arithmetic. No TTM, no quarter subtraction, no interpretation.**

CIKs verified at `https://www.sec.gov/files/company_tickers.json` 2026-10-24 18:18 ET: META 0001326801 · ORCL 0001341439 · MSFT 0000789019 (PROME's recollection was correct) · GOOGL 0001652044 · AMZN 0001018724.

## Saved packets (raw response sha256 verified equal to each record's `response_sha256`)

| Issuer | Concept | Prior window | Current window | Prior val | Current val | Accession (both) | Folder |
|---|---|---|---|---:|---:|---|---|
| META | NetCashProvidedByUsedInOperatingActivities | 2025-01-01 to 2025-09-30 | 2026-01-01 to 2026-09-30 | 79,586,000,000 | 96,873,000,000 | 0001628280-26-066773 | `2026-10-24_0001326801_NetCashProvidedByUsedInOperatingActivities_USD/` |
| META | PaymentsToAcquirePropertyPlantAndEquipment | 2025-01-01 to 2025-09-30 | 2026-01-01 to 2026-09-30 | 48,308,000,000 | 83,055,000,000 | 0001628280-26-066773 | `2026-10-24_0001326801_PaymentsToAcquirePropertyPlantAndEquipment_USD/` |
| META | FinanceLeasePrincipalPayments | 2025-01-01 to 2025-09-30 | 2026-01-01 to 2026-09-30 | 1,770,000,000 | 2,769,000,000 | 0001628280-26-066773 | `2026-10-24_0001326801_FinanceLeasePrincipalPayments_USD/` |
| META | PaymentsOfDividends | 2025-01-01 to 2025-09-30 | 2026-01-01 to 2026-09-30 | 3,986,000,000 | 4,060,000,000 | 0001628280-26-066773 | `2026-10-24_0001326801_PaymentsOfDividends_USD/` |
| META | PaymentsOfDividends | 2025-07-01 to 2025-09-30 | 2026-07-01 to 2026-09-30 | 1,330,000,000 | 1,361,000,000 | 0001628280-26-066773 | same folder, second record |
| META | PaymentsForRepurchaseOfCommonStock | 2025-01-01 to 2025-09-30 | 2026-01-01 to 2026-09-30 | 26,248,000,000 | 0 | 0001628280-26-066773 | `2026-10-24_0001326801_PaymentsForRepurchaseOfCommonStock_USD/` |
| ORCL | NetCashProvidedByUsedInOperatingActivities | 2025-06-01 to 2025-08-31 | 2026-06-01 to 2026-08-31 | 8,140,000,000 | 23,103,000,000 | 0001193125-26-389274 | `2026-10-24_0001341439_NetCashProvidedByUsedInOperatingActivities_USD/` |
| ORCL | PaymentsToAcquirePropertyPlantAndEquipment | 2025-06-01 to 2025-08-31 | 2026-06-01 to 2026-08-31 | 8,502,000,000 | 28,499,000,000 | 0001193125-26-389274 | `2026-10-24_0001341439_PaymentsToAcquirePropertyPlantAndEquipment_USD/` |
| ORCL | PaymentsOfDividendsCommonStock | 2025-06-01 to 2025-08-31 | 2026-06-01 to 2026-08-31 | 1,413,000,000 | 1,565,000,000 | 0001193125-26-389274 | `2026-10-24_0001341439_PaymentsOfDividendsCommonStock_USD/` |

Every prior-year value above was selected from the CURRENT filing's comparative column (latest filed on or before the cutoff), as the selection policy states; the earlier filing carries the same value for every one of these nine windows (checked in the saved raw responses).

## Explicit failures (exit 2, nothing saved) — verbatim cause

| Issuer | Concept | Window pair | Cause |
|---|---|---|---|
| META | OCF, capex (PP&E), FinanceLeasePrincipalPayments, PaymentsForRepurchaseOfCommonStock | three-month Q3 (2025-07-01→09-30 vs 2026-07-01→09-30) | `Missing period ['2025-07-01', '2025-09-30'] in unit USD; no proxy substituted` — the 10-Q cash-flow statement tags only the year-to-date window (re-run with the added hint: `windows reported ending 2025-09-30: 2025-01-01 to 2025-09-30 (no quarter subtraction is performed)`) |
| META | PaymentsOfDividendsCommonStock | nine-month and three-month | `Missing period … no proxy substituted` — the Q3-2026 10-Q does not use `PaymentsOfDividendsCommonStock`; its rows run only through the FY2025 10-K |
| META | PaymentsToAcquireProductiveAssets | nine-month | `HTTP 404 … not found` — META does not use the tag |
| ORCL | FinanceLeasePrincipalPayments | Q1 FY27 vs Q1 FY26 | `Missing period ['2026-06-01', '2026-08-31'] in unit USD; no proxy substituted` — latest row in the API ends 2026-02-28 (Q3 FY26 10-Q); neither the FY26 10-K nor the Q1 FY27 10-Q carries it under this tag |
| ORCL | PaymentsForRepurchaseOfCommonStock | Q1 FY27 vs Q1 FY26 | `Missing period ['2026-06-01', '2026-08-31'] …` — latest row is the FY26 10-K (2025-06-01→2026-05-31, $95M); the Q1 FY27 10-Q carries no row under this tag |
| ORCL | PaymentsOfDividends | Q1 FY27 vs Q1 FY26 | `HTTP 404 … not found` — ORCL uses `PaymentsOfDividendsCommonStock` (saved above) |
| ORCL | PaymentsToAcquireProductiveAssets | Q1 FY27 vs Q1 FY26 | `HTTP 404 … not found` |

## Observations for the consumer (facts, not interpretation)

- **Two concepts, two values, one window, one filing — META dividends:** the Q3-2025 10-Q (acc 0001628280-25-047240) tags the 2025-07-01→09-30 window as **$1,330M** under `PaymentsOfDividends` and **$1,323M** under `PaymentsOfDividendsCommonStock` (saved raw response sha edf89e62a125…; `facts` 2026-10-24). The Q3-2026 10-Q carries only `PaymentsOfDividends`. Which concept a desk picks changes the figure; the tool does not reconcile them (limit 2) and does not choose between them.
- **Cross-check (DEWEY derived, not tool output):** META Q3-2026 three-month OCF = 96,873 − 64,088 (Q2 YTD, acc 0001628280-26-050705) = $32,785M, matching KB-VULCAN-248 and DEWEY's 2026-10-22 Table 1 input. ORCL Q1 FY27 capex $28,499M matches KB-VULCAN-156.
- **Not run — not yet on EDGAR:** GOOGL Q3-2026, AMZN Q3-2026, MSFT Q1 FY27 10-Qs (prints expected ~10/28–29; the XBRL facts arrive only after each 10-Q is filed and processed, so the print day itself will not be in the API).
