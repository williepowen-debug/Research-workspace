# Finance verification — October 25, 2026

Bounded WALTER helper; Codex/OpenAI runtime, exact variant UNKNOWN. Root CLAUDE.md/AGENTS.md and local WALTER rules explicitly read. No domain-owner files or git state changed. Raw SEC XML/downloads remain in /tmp. Published cards 010/016/017 and prior full review read.

## CalPERS — CONFIRMED figure, CORRECTED-framing on exposure

**Claim checked:** direct Magnificent Seven holdings fell 26% in H1 2026.

**Evidence locators:** SEC CalPERS CIK 919079 Form 13F information tables: [2025-12-31, filed February 12, accession 0000919079-26-000003](https://www.sec.gov/Archives/edgar/data/919079/000091907926000003/form13fInfoTable.xml); [2026-06-30, filed August 14, accession 0000919079-26-000011](https://www.sec.gov/Archives/edgar/data/919079/000091907926000011/form13fInfoTable.xml). Both downloaded HTTP 200 and parsed directly; report dates/filing IDs checked against SEC submissions. [Bloomberg Tax October 23 relay](https://news.bloombergtax.com/financial-accounting/calpers-pivots-from-us-tech-giants-to-private-equity-ft-reports), accessible paragraphs explicitly describe combined share counts, citing FT calculations. Full FT interview not recovered.

**Supporting observation (shares, XML sshPrnamt; all non-option):**

| Name | December 31 | June 30 |
|---|---:|---:|
| AAPL | 36,375,266 | 29,642,254 |
| MSFT | 21,124,113 | 15,795,039 |
| NVDA | 76,375,762 | 46,071,341 |
| AMZN | 20,049,877 | 18,696,461 |
| META | 5,824,493 | 4,961,480 |
| TSLA | 5,231,555 | 5,574,336 |
| GOOG | 12,344,566 | 9,358,074 |
| GOOGL | 15,378,439 | 12,083,544 |
| Total | 192,704,071 | 142,182,529 |

Calculation: 142,182,529/192,704,071 − 1 = −26.217%. Combined filed market value $53.862B → $40.908B = −24.050% (quarter-end valuations, not transaction proceeds).

**Bounded conclusion:** 26% rounds correctly for aggregate direct share count, including both Alphabet classes. Raw shares across issuers are not an economic exposure weight; Tesla increased 6.55%, so not an across-all-seven 26% cut. Neither these two snapshots nor the article establish sale proceeds, timing of private-equity purchases, net commitments, or total exposure through pooled funds/managers. Primary allocation paper retrieval returned 403; no cash-flow causality independently established.

## JetBlue — CONFIRMED instrument; INDETERMINATE actual trade prices

**Claim checked:** $2B loyalty-backed 2031 notes fell from ~80c early October to ~40c October 22; creditors hired advisers.

**Evidence locators/observation:** [JetBlue SEC 8-K, August 27, 2024 financing](https://www.sec.gov/Archives/edgar/data/1158463/000121390024075128/ea0213241-8k_jetblue.htm), Items 1.01/2.03, directly read: co-issued $2B 9.875% notes, mature September 20, 2031, first lien on specified TrueBlue collateral alongside term loan. [Fund SEC N-PORT](https://www.sec.gov/Archives/edgar/data/1388485/000094040026025253/primary_doc.xml), indexed search field identifies 144A CUSIP 476920AA1; full XML unavailable through browser. [Bloomberg Law October 23 23:18 UTC](https://news.bloomberglaw.com/bankruptcy-law/jetblue-lenders-organize-after-stock-debt-fall-to-record-lows), two accessible paragraphs name PJT Partners/Akin Gump for holders of $2B notes and $742M loan, citing anonymous people.

**Bounded conclusion:** instrument/collateral established; actual October 22 TRACE executions and 80c starting observation not independently retrieved. FINRA public landing gave no trades; iShares historical CSV request returned a 200 HTML landing, not holdings. Bloomberg price/excerpt and adviser story remain one reporting organization, not independent witnesses. No issuer/adviser statement or bankruptcy/default filing established by this check. Retain distress lead and explicit secondary price attribution.

## France — CONFIRMED rating outcome; INDETERMINATE 7bp intraday move

**Claim checked:** 10-year OAT–Bund premium narrowed 7bp October 23; Moody’s review outcome.

**Evidence locator/observation:** [French Finance Ministry October 23 release 1146](https://presse.economie.gouv.fr/notation-moodys-reaction-de-roland-lescure/) explicitly says Moody’s maintained Aa3 with negative outlook. [AFT ratings listing](https://www.aft.gouv.fr/en/frances-credit-ratings) still shows April 10 as latest and October 23 as next: a stale listing, not contrary evidence. Moody’s original detailed rationale not recovered.

**Bounded conclusion:** no downgrade onOctober 23 is established at a government primary. Exact 7bp headline, start/end values and same-basis closing OAT/Bund pair remain unsupported after targeted searches; later Reuters summaries describe persistent stress but cannot falsify an intraday narrowing. AFT indexed TEC10 = 5.05% for October 23 is a synthetic constant-maturity rate, not that matching benchmark pair. Do not calculate a spread or grade HANS’s threshold from it.
