# Q3 bank comparison: source check and EagleBank definition test

> **Latest November 11 continuation:** `output/2026-11-11_003R-full-population-refresh.md` completes the full Q3 population and current-placement leg. Larger-band QoQ trigger OFF; smaller-band result requires the United Fidelity cash-basis/concentration qualification. Exact EagleBank bridge remains UNKNOWN. Historical tables below retain their stated vintage.

**Date:** 2026-11-11 | **Mode:** Thesis | **Commission:** REQ-DEWEY-20261022-003R / L1119 | **State:** PARTIAL | **Confidence:** High on retrieved cells; UNKNOWN on unexplained difference.

## Key finding

A fresh source check still does not supply the full Q3 population: FDIC returns zero rows and FFIEC's selected single-period bulk product ends at June 30. EagleBank's fresh June and September filings reproduce the previously reported amounts. Reading the current regulator instructions does not establish a source-explained reconciliation. This pass does not change the earlier six-bank findings or their historical placement.

## Evidence

[PRIMARY: FFIEC RetrieveFacsimile SDF, bank RSSD 2652092, June and September 2026; retrieved November 11. Full responses and hashes: `research/2026-11-11_003R-next-pass/`. All amounts below $thousands.]

| Measure | June 30 | September 30 |
|---|---:|---:|
| RC-N total nonaccrual, RCON1403 | 136,915 | 179,722 |
| RC-R held-for-investment category, RCONS449 | 111,124 | 166,021 |
| RC-R held-for-sale category, RCONS423 | 25,656 | 13,534 |
| Arithmetic difference | 135 | 167 |
| RC-N held-for-sale nonaccrual memo, RCONC226 | 0 | 0 |

The current [FFIEC instructions](https://www.ffiec.gov/sites/default/files/data/reporting-forms/FFIEC031_FFIEC041_202609_i_0.pdf) sharpen three constraints:

- RC-N uses balance-sheet amounts before credit-loss allowances, with applicable unearned income netted (printed RC-N-1, PDF page 337). It is not generically a contractual-principal measure.
- Its held-for-sale memo asks for carrying amounts of qualifying past-due/nonaccrual loans (RC-N-14, PDF page 352). Held-for-sale status alone does not explain a zero memo.
- RC-R's held-for-investment delinquent/nonaccrual category excludes specified mortgage, sovereign and high-volatility CRE exposures (RC-R-110, PDF page 535). Its scope cannot automatically be equated with RC-N.

Consequently, a generic accounting explanation is not a verified bridge. The company's nonaccrual categories also do not map one-for-one to regulatory categories. The [September 10-Q](https://www.sec.gov/Archives/edgar/data/1050441/000105044126000113/egbn-20260930.htm) and [June 10-Q](https://www.sec.gov/Archives/edgar/data/1050441/000105044126000096/egbn-20260630.htm), saved in the preceding pass, remain the issuer evidence; no disclosed loan-level crosswalk was identified. Exact agreement between one company total and one RC-R cell is numerical corroboration, not proof that the two schedules cover identical loans.

## Full-population dependency

The fresh [FDIC query](https://api.fdic.gov/banks/financials?filters=REPDTE%3A20260930&fields=CERT,ASSET,LNATRES,NCLNLS&limit=10000) returned `meta.total=0`. A new normal GET and product-selection postback to the [FFIEC bulk page](https://cdr.ffiec.gov/Public/PWS/DownloadBulkData.aspx) again returned June 30 as the newest period. Saved options and retrieval hashes establish the observed selector state.

Individual filings remain available, as this pass demonstrates. No full-population individual-file assembly was performed. Therefore the aggregate trigger and current-Q3 comparison remain uncomputed, not disproved or impossible. The existing November 16 touch remains; the previously documented November 14 publication expectation is not a guarantee. No new schedule or collector is created.

## Counter-evidence and limits

The original historical study found no useful standalone predictive contribution from falling coverage at the requested horizon. This check adds no predictive evidence. The six banks cannot stand in for all regional banks; CECL limits comparisons across accounting eras. The unexplained schedule difference is not evidence of misstatement, and no speculative cause is adopted.

## Process report and next action

Two fresh bank filings, one FDIC query, a fresh FFIEC product selection, issuer-table comparison and current instruction review. One targeted web-search call with two queries; no subagents. Direct PDF download returned 403; the web tool supplied the official document. No paid source or external inquiry used. Repeat source checks alone cannot finish the population calculation: a complete bulk release or validated individual-file population is required. EagleBank needs an explanatory disclosure or a defensible source crosswalk; the difference stays UNKNOWN meanwhile.

**Do-not-relay-as:** completed 003R, absent individual Q3 filings, an exact EagleBank bridge, a principal-versus-book-value explanation, or a new predictive/trade signal.
