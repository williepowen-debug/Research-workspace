# Evidence persistence — October19

The RESULT source table gives primary URLs and exact document locators. source-receipts.json records HTTP retrieval time, status and validity. source-manifest.json hashes every raw/parsed capture in sources.tar.gz. Invalid403 bodies remain invalid and are not parsed. RCL final prospectus and NCLH Q2 release were read through browser despite shell403; decisive fields are recorded with their source/section in RESULT. July board8-K was read through browser and concerns a director appointment; it adds no financing event.

WALTER RCL/NCLH chart bodies are exact copies of its October19 historical-cases-and-credit/raw captures; SHA256 in calculations.json matches that owner's source-receipt.json. They supply vendor-adjusted returns, not official exchange total-return series. No new factor model was fit.

Reproduce from this directory: `tar -xzf sources.tar.gz`, then `python3 reconcile.py`. The script writes only calculations.json and prints arithmetic; it does not collect prices, invoke CRU-11's resolver, or alter state/thresholds. Source inputs are dated in RESULT.

All linked cruise primary bodies in WALTER RESULT reopened October19. CCL May31 10-Q read for fiscal-date exclusion. Linked historical warning/chronology sources opened as context; LPL2023 refetch failed404 (WALTER attribution retained). No regrade/research extension.
