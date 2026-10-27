# ISHM file and evidence build — October 26, 2026

**Scope:** expand the existing desk within its frozen eight-company perimeter. Evidence cutoff October 26 ET; some retrieval UTC clocks fall on October 27. This is research-library construction, with no new collector, recurring monitor, forecast, trade or registered band.

## What changed

| Surface | Before | Now |
|---|---|---|
| Navigation | Startup files and a large first-session source folder | Root README, data guide, company guide, dated build report |
| Regional histories | Current releases plus Richmond history; full same-month panel not assembled | Five primary histories; 1,974 region-month records, 268 complete five-region months, June 2004–September 2026 |
| Hard-data library | Separate FRED CSV captures | 14 series aligned over 1,293 monthly dates; source-specific starts, units and missing values retained |
| Equipment baseline | Detailed Q2 BEA equipment table not recovered | Primary Section 5 workbook, exact table/line extraction, 317 quarterly dates; latest Q2 2026 |
| Company evidence | Four latest October reports read; other four next dates established | Latest accepted earnings read for every frozen name, eight checklist cells each; 42 total PRINTS rows, up from 37 |
| Persistence research | Single-month descriptive frequencies | 24 two-month comparisons across full, recent and pandemic-excluded samples |
| Reader declaration | Delivered, not registered | `read_cap_check --agent ISHM` returns rc 0, ATTESTED; registration dependency closed |

Panels and metadata: ../../data/README.md. Corporate source extracts and regional files are in sources/. Source integrity inventory: SNAPSHOTS.json. `build_panels.py` reproduces tables offline using these snapshots and the first-session sources. The current ledger remains ../../workbook/PRINTS.tsv.

## Same-month orders, not unlike headline averages

| Reference month | NY | Philadelphia | Richmond | Kansas City | Dallas | Negative new-order indexes |
|---|---:|---:|---:|---:|---:|---|
| September 2026 | 2.0 | 29.2 | −6 | 24 | 30.7 | 1 of 5 |
| October 2026, before Richmond | 23.2 | 4.3 | UNKNOWN | 3 | 9.3 | UNKNOWN; only 4 of 5 observed |

Values are issuer current-vintage SA new-order diffusion points, not output growth rates. Historical files do not independently supply each month's first-release clock. October Richmond is due October 27 at 10:00–10:10 ET. Its missing value cannot become a zero or a complete calm panel. Sign counts are breadth within five survey districts, not a national manufacturing-output estimate.

**Correction:** ISHM's initial Philadelphia PRINTS notes transcribed September new orders as 29.5. Both the saved October primary release and the recovered historical file say **29.2**. October new orders 4.3 and headline 20.9 are unchanged. This is an ISHM transcription correction, not an issuer revision; PRINTS and KB record the reason. Dallas production 29.5 is a different valid figure and must not be replaced.

## BEA equipment: a real baseline, an incomplete current-quarter test

BEA's September 30 revised vintage, NIPA Table 5.3.1 lines 9, 10, 11 and 13, gives Q2 2026 real growth at **13.4% equipment, 7.6% information processing, −6.7% computers, 27.0% industrial equipment**, q/q SAAR. Table 5.3.6 supplies corresponding real levels in millions of chained 2017 dollars SAAR. Chained components are not additive.

Information-processing growth slowed from Q1's 38.8% SAAR; the computer subset fell after Q1's 70.1%. This is actual measured investment but is neither an AI-specific allocation nor the missing Q3 result. Q3 advance arrives October 29; September FT-900 imports arrive November 4. J1 still needs quarter-aligned domestic, imported and real-investment evidence. Nominal imports require suitable deflators for a real-import comparison; domestic M3 plus imports is not an additive capex total.

## Company additions and a comparison trap

Read CAT Q2 (August 4), Deere fiscal Q3 (August 20), Parker fiscal Q4 (August 6) and Emerson fiscal Q3 (August 4) at primary sources. These join GE, HON, MMM and UNP reports already read. Different fiscal quarters prevent treating the eight files as one synchronized survey.

Parker's legacy total-order increase is 19%, but its comparable rolling 12-month figure is **12%**. North American industrial orders are 16% on the legacy method versus 9% on the rolling method; international 24% versus 10%. FY2027 switches industrial orders to the 12-month method. November 5 must be compared with the rebased series; a mechanical method change is not measured demand deterioration.

CAT's Q2 power-generation sales rose 29%, but the release does not quantify the AI or grid shares. CAT's $392 million and Deere's $110 million quarterly tariff recoveries are recoveries, not newly incurred costs or economy-wide tariff relief. Emerson's underlying orders rose 7% excluding AspenTech. Company files retain each exception and `NOT-STATED` checklist cells; absent disclosure never means zero exposure.

## Persistence evidence and its limits

All candidates remain unregistered. Two observations mean adjacent reference months, not agent sessions; calendar gaps are refused. Full output: ../../data/CALIBRATION.tsv. Units below are overlapping qualifying monthly pairs divided by all eligible adjacent pairs.

| Research comparison | Full sample | Recent window from October 2016 | Excluding March 2020–June 2021 |
|---|---:|---:|---:|
| Core capex nominal y/y <0% twice | 108/402 (26.9%) | 39/118 (33.1%) | 99/385 (25.7%) |
| Core capex nominal y/y <−5% twice | 46/402 (11.4%) | 7/118 (5.9%) | 40/385 (10.4%) |
| Cass shipments y/y <0% twice | 65/116 (56.0%) | 65/116 (56.0%) | 58/99 (58.6%) |
| Cass shipments y/y <−5% twice | 27/116 (23.3%) | 27/116 (23.3%) | 21/99 (21.2%) |
| Monthly rail carloads y/y <−5% twice | 48/306 (15.7%) | 16/117 (13.7%) | 38/289 (13.1%) |
| At least 3/5 regional orders negative twice | 74/267 (27.7%) | 42/119 (35.3%) | 72/250 (28.8%) |
| At least 4/5 regional orders negative twice | 43/267 (16.1%) | 29/119 (24.4%) | 41/250 (16.4%) |

The Cass sample begins January 2017 after the 12-month growth calculation; its recent window therefore contains the same observations as full history and is not an independent sensitivity. Monthly rail is the BTS SA monthly estimate derived from AAR inputs; it cannot calibrate weekly NSA four-week sums. Recent and pandemic-excluded comparisons retain the same variable definition, but do not remove revision bias. Full source-specific windows and left-censored episode-start counts are in the table.

These are current-vintage descriptive frequencies, not first-publication backtests, independent recession events, credit probabilities or approval to fire a new band. Overlapping pairs cluster heavily. ISM orders-minus-inventories remains uncalibrated without long comparable components. Proposed recovery-side rules and joint J1 events also need their own calibration before registration.

## Remaining dependencies

| Dependency | Owner / next touch | Independent work still available |
|---|---|---|
| Long ISM/S&P component history and first-release vintages | ISHM / existing approved access, November 2 | Read new primary releases; keep current final above superseded flash |
| Weekly AAR four-week calibration | ISHM, November 4 batch | Read current weekly issuer volumes without transferring monthly percentiles |
| Broader independent freight/HY episodes | LIQUID / RED input; ISHM November 13 | Existing narrow J2 sample stays explicitly restricted |
| Real imported-hardware and AI attribution | ISHM supplies physical figures; VULCAN verdict, October 29 / November 4 | Use recovered Q2 baseline; no domestic-only AI falsification |
| Aligned industrial-equity event returns | ISHM / HENRY consequence, October 29 | Mechanism scores remain usable; thermometer excluded |
| Grid ownership reply and HENRY trigger pointers | WATT / HENRY; ISHM follows October 27 | Keep actual ownership at canonical WQ-507 and WATT boundary |
| Deere event body/time and next advisories | ISHM, November 12 / November 6 | Qualified dates remain in docket; no invented event time |

FERT's October 26 reply accepts the farm-input boundary and records consumption of ISHM's original packet. It does not establish farm-income or Deere-demand effects. PROME's ROSTER now names ISHM's inherited trigger correctly; the HENRY charter's two old rows remain recipient-owned repairs. No broader desk launch or company expansion was needed.
