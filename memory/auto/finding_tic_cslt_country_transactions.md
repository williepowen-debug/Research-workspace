---
name: finding-tic-cslt-country-transactions
description: Country-level TIC net transactions moved to the CSLT JSON (S-form files frozen at Jan-2023); mfh.txt serves a dead vintage; press-notice PDFs are named by release month not data month
metadata: 
  node_type: memory
  type: reference
  originSessionId: 58c28045-37e7-4e1e-9d46-cee27e2d00f9
---

**TIC country-level flow data — where it actually lives (verified 2026-07-16, ARM-#3 grade):**

- **Net TRANSACTIONS by country (the valuation-adjusted flow measure):** Treasury/Fed **CSLT** dataset — `https://ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/cslt.zip` (~121MB JSON, ~4,260 series). Series IDs: `for_lt_treas_net_<code>`, `for_st_treas_net_<code>` (also `_agcy_`, corp, equity variants). Country codes: China Mainland **41408**, Japan **42609**. Observation arrays are **newest-first**. Measure = "net purchases at market value" from the position-change decomposition (net purchases / valuation / residual) — exactly the F10 "net transactions, valuation-adjusted" spec.
- **Dead ends (all frozen at Jan-2023, the S-form discontinuation):** `Publish/snetus.csv`, `s1_globl.csv`, `tressect.txt`. Do not cite their newest rows as current.
- **`ticdata.treasury.gov/Publish/mfh.txt` serves a DEAD Jan-2023 vintage** (even with cache-busters). Current Major-Foreign-Holders holdings = `Documents/slt_table5.txt` (or the .html view).
- **Press-notice PDFs are named by RELEASE month, not data month:** `Press-notice-TIC-for-May-2026.pdf` = March data released in May; May-2026 DATA = `...TIC-for-Jul-2026.pdf`. Check the embargo line inside the PDF for the actual release date — the 5/2026 notice proved the May-data release was **7/14**, catching a 2-day docket vintage error ([[finding_tool_default_asof_date_drift]] class).
- Fed-PDF/treasury binary reads: WebFetch auto-saves the binary; run pdfminer over the local copy (DEWEY's proven workaround).

Consumers: BOND (foreign demand), ZHAO (China), SAM (Japan), LIQUID (demand-hole), TERRY/PROME (TIC-keyed gates).
