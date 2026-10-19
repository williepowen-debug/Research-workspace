# Source register — October19 after-close financing read

Read clock approximately21:53–21:56UTC, October19,2026. All repository paths resolve from `/home/willi/Research-workspace`. Browser opens/read locators were successful unless stated. No SEC source is replaced by a search-result snippet. Most HTML is not downloaded because the direct request failed; these are source/locator receipts, not a claim of a complete frozen raw-source archive.

| ID | Primary source | Document date / locator | Access and timing limit |
|---|---|---|---|
| N1 | [NCLH closing](https://www.sec.gov/Archives/edgar/data/1513761/000110465926116254/tm2627514d1_8k.htm) | October15; Items1.01/1.02 | Browser full8-K read; in return window |
| N2 | [NCLH amendment](https://www.sec.gov/Archives/edgar/data/1513761/000110465926116254/tm2627514d1_ex10-1.htm) | October15; amended agreement definitions and §§6.12–6.15 | Browser read; redline deletions distinguished from retained/added text; direct request403 in sec-direct-receipt.json |
| N3 | [NCLH10-Q](https://www.sec.gov/Archives/edgar/data/1513761/000110465926089657/nclh-20260630x10q.htm) | June30, filedAugust3; Note7 / liquidity | Predates formation; not September actual balances |
| N4 | [NCLH guidance](https://www.sec.gov/Archives/edgar/data/1513761/000110465926112116/tm2626633d1_8k.htm) | September30; Item7.01 | Forward-looking and simultaneous with refi announcement |
| V1 | [VZ10-Q](https://www.sec.gov/Archives/edgar/data/732712/000073271226000046/vz-20260630.htm) | June30, filedJuly31; Note5, MD&A Interest Expense, Market Risk | Predates formation; no latest-certificate claim |
| V2 | [VZ issuer debt PDF](https://ws01.static-verizon.com/about/sites/default/files/Verizon-IR-debt-portfolio-63026.pdf) | As-ofJune30; pp1/6/7 | Browser parsed plus p1 screenshot request; successful direct PDF download and pdftotext. Hash in vz-pdf-receipt.json. **First-publication timestamp UNKNOWN**; dated retrospective supplement, not independently certified point-in-time input |
| V3 | [VZ prospectus](https://www.sec.gov/Archives/edgar/data/732712/000119312526345341/d140600d424b2.htm) | August10; cover and Use of Proceeds | Pricing/expected settlement only; actual closing not separately verified |
| T1 | [T10-Q](https://www.sec.gov/Archives/edgar/data/732717/000073271726000297/t-20260630.htm) | June30, filedJuly22; MD&A Credit Facilities | Predates formation; later transaction changes exposure |
| T2 | [T acquisition close](https://www.sec.gov/Archives/edgar/data/732717/000119312526321053/d142142d8k.htm) | July28; Item2.03 | Closed cash transaction and bank draws |
| T3 | [T August3 issuance](https://www.sec.gov/Archives/edgar/data/732717/000119312526332110/d112584d8k.htm) | FiledAugust4; Item8.01 | Closing verified; actual use/retirements not established |
| T4 | [T August17 issuance](https://www.sec.gov/Archives/edgar/data/732717/000119312526354091/d153710d8k.htm) | August17; Item8.01 | Closing verified; after-hedge floating exposure unresolved |
| T5 | [T issuer debt PDF](https://investors.att.com/~/media/Files/A/ATT-IR-V2/financial-reports/quarterly-earnings/2026/2Q-2026/debt-list-20260630.pdf) | As-ofJune30; pp1–3 | Browser parsed plus p1 screenshot request; direct403 in t-pdf-receipt.json. **First-publication timestamp UNKNOWN**; not a frozen pre-window source |
| R1 | [RCL issuance](https://www.sec.gov/Archives/edgar/data/884887/000110465926099245/tm2623517d1_8k.htm) | August20; Item1.01 | Closed issue; intended use is not verified repayment |
| R2 | [RCL acquisition](https://www.sec.gov/Archives/edgar/data/884887/000110465926109755/tm2625963d1_8k.htm) | September23; Item8.01 | Announced definitive agreement/commitment; expected2027 closing |

Issuer fixed-income landing pages were used only to find the linked schedules. Their undated current ratings tables were **not** imported as point-in-time credit-action history. Search attempts did not establish a Verizon hybrid closing document or a LOW facility renewal; neither null result proves no event.

## Consumed repository evidence

- Required WALTER SIG015–018: delivered LIQUID handoffs, with intake rows in grep-only board_log.tsv. Those files move to `inbox/WALTER/processed/`; no WALTER source file edited.
- `AGENTS/WALTER/research/2026-10-19_breadth-followup/RESULT.md`; `TELECOM-PILOT.md`; `company-pairs/RESULT.md`, `SOURCE-REVIEW.md`, `exposures.json`.
- `AGENTS/WALTER/research/2026-10-19_historical-cases-and-credit/RESULT.md`, `CABLE-CHECK.md`, `cruise-exposures.json`.
- CRUISE `STATUS.md` and `domain/sources/2026-10-14_nclh-funding-position-after-the-930-refinancing.md`: owner context, not a fresh independent verification of its forecasts, covenant expectations or Treasury-spread decomposition. No owner files changed.
- Morning LIQUID `reports/2026-10-19_Will-closeout.md`, current STATUS/MEMORY and referenced completed sweep. No repeat of the morning research.

## Required boot / correction receipts

FRED-only `boot.py --quick` at17:53ET completed19series/0fetch errors. No new HY observation beyondOctober16 returned; existing count unchanged. H.15 October16 DGS10 5.09%/DGS30 5.43% are newer dated observations than the morningOctober15 cells, not numeric corrections. Quick mode deliberately skipped equity marks and076; no intraday prices represented as official closes. Full output boot-quick.txt.

COR-20261019-12 read at its named BOARD pointer: existing live LIQUID surfaces contained no Ally cancellation-cushion or warehouse-exit probability claim. NO-OP receipt written using the canonical writer; future use distinguishes whole-loan-purchase capacity from warehouse availability. OTTO forecast unchanged. First writer attempt refused a semicolon-containing scope and wrote nothing; corrected attempt succeeded and subsequent check returned0unreceipted. This receipt does not claim a fresh audit of OTTO's underlying contracts.

## Late cohort-source extension

Additional primary filing/release links and exact notes are in COHORT-FUNDING.md; all were opened in the browser approximately22:01–22:05UTC. The Coherent issuer10-K PDF was parsed by the browser, not frozen as a local download. Post-June search found SNDK’s September9 bank renewal; opened the controlling8-K and July3 debt note. Search nulls are not a complete later-event census. Attempted HENRY sndk-submissions.json reuse was rejected by JSON parsing: no data accepted, no file changed. System python lacks bs4; repository .venv python has it. Neither software limitation changed a financial input.

HENRY’s committed initial acknowledgment7def3935d was read. His later working selection files were observed and hashed, with their uncommitted/final-delivery limitation retained. CRUISE’s c45f20fb9 request was read; its evolving cushion result explicitly reuses LIQUID’s contract read, not an independent credit confirmation. No claim of consuming a final CRUISE version until committed packet reviewed.
