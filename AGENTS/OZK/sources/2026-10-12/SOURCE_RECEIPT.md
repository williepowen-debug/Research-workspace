# L635 source receipt

Written 2026-10-12T10:45:02.689886-04:00. Retrieved under approved read-only network escalation.

| File | Source / basis | SHA-256 |
|---|---|---|
| FDIC_FLNG_12019_8K.pdf | FDIC cert 110, FLNG 12019/1, report 2026-10-12; read full document | 13585c0379a619112e32c3776dad2bab89c56be4d47abc09ff985ea6fed19d01 |
| FDIC_FLNG_12019_8K.txt | FDIC cert 110, FLNG 12019/1, report 2026-10-12; read full document | 1bcb26971b9f7151cf89a8610676a784572aefbce81215a7ef5d17c37a6f0bd3 |
| FDIC_FILINGS.json | FDIC /api/instflng/cert/110, 183 IDs; fetched October 12 ~10:35 ET | e324d7a96704a6bb536e5ceb8854a4573e6bb6e64ac344ed7a8a604a6ddd9e3a |
| MARKET_OZK_KRE.json | FORGE/yfinance, October 12 ~10:37 ET; final dated bar unfinished intraday, not a close | ddd6c49687488d9d8c2b0698d8ff152939db4d6ac14de4844f2797c26277098e |
| BOOT.txt | FORGE/yfinance, October 12 ~10:37 ET; final dated bar unfinished intraday, not a close | f42d4cc00ee2e1f025b2ff2321ec52c0a77dd3b829aa6ffc73c6cb97888fef1b |

Primary URL: https://securitiesfilings.fdicconnect.fdic.gov/api/instflng/12019/attachment/1
County recorder web open October 12 returned 403; no county instrument preserved.
Boot initial sandbox run failed DNS; preserved BOOT.txt is the successful network-enabled run.

PDF page count verified with pdfminer.pdfpage: **3**, Item 7.01 terms on p.2. pdfplumber import failed (not installed in this runtime venv); paragraph-based full extraction succeeds with pdfminer.
