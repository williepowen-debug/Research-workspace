# Requested October 26 close snapshot

`capture.py` performs this dated public-source capture only. `access.json` records URL, status, retrieval times, byte counts and hashes for all raw responses. Yahoo chart JSON is MIRROR with native floating-point price precision. GLD issuer workbook and Treasury real-yield CSV are PRIMARY. Westmetall is a MIRROR of LME inventory. No CME request or paid access.

`calculate.py` reads saved inputs and writes extracted CSV histories plus `summary.json`; no canonical state writes, production-code changes or forecast grading. It uses the existing futures snapshot guard on the parsed daily history, so the newest daily futures row remains excluded. Raw chart responses also contain late-evening appended quotes sharing October26's local date. Duplicate groups must have exactly one midnight historical daily row and one later observation; the latter is retained in `excluded_live_appended_rows`, never silently substituted as the daily Close. Historical null-close rows are listed, omitted without filling, and required October23/26 closes must be numeric.

Fund bands use the approved 200/252-session methods. Crash legs are carried only after checking no new deeper crossing since the previous close. The first post-approval PPLT -20% crossing is October26. Actual scoring remains subject to the November1 floor; no prediction endpoint is graded.

The Westmetall stock-field URL changes column order versus the production cash-field URL. This one-off read locates `date` and `LME Copper stock` headers, skips repeated header rows, reconciles duplicate dated observations and calculates the registered trailing730-day median. It does not change the production parser.

Issuer October23/26 bullion rows are both newly held and their changes are measured separately. `GLD_latest_issuer.csv` retains recent issuer rows. Raw successful response files remain byte-identical to access hashes. Validation and unchanged-letter hashes are recorded in `validation.json`; all current-state changes are explicit in the accompanying report/state commit.
