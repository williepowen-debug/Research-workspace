# CRWV insider claim — CORRECTED-framing

Observed 2026-10-20T15:54Z. Bookmark `2112362966737936583`, DarioCpx, October 20. Narrow WALTER Rule 9 verification; no domain grade or trade recommendation.

**CLAIM:** Every insider, including lower management, is dumping as many shares as possible as fast as possible below the all-time high.

**LOCATOR / offered material:** [Recovered screenshot](https://pbs.twimg.com/media/HVCevS4asAAOxEr?format=png&name=large), visually read whole; rows displayed September 22–October 13, 2026. Local temporary image `/tmp/walter-insiders.png`, SHA256 `b39ab1868bd09d171ffe4b9fe7282509f560b1c753c5b6f4d52bd96b2a38fb5d`. It mixes **Sale** and **Proposed Sale**, repeats named insider/date/quantity across those categories, and contains 3–5-share sales. Proposed and completed sales must not be summed as separate completed transactions.

**OBSERVATION / primary check:** [SEC submissions](https://data.sec.gov/submissions/CIK0001769628.json) retrieved HTTP 200. Read all 13 Forms 4 filed October 1–14 (accessions `0001769628-26-000437` through `-000449`), the latest Form 4s returned as of retrieval. Periods reported September 29–October 13. Raw XML body and footnotes read, not aggregator classifications.

| Primary locator | What it establishes |
|---|---|
| [437, CEO Intrator, filed Oct 1](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000437/form4.xml) | September 29 sales explicitly under a Rule 10b5-1 plan adopted November 20, 2025. Includes conversion and multiple ownership accounts; a zero in one account does not mean zero total beneficial holdings. |
| [438 CFO Agrawal](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000438/form4.xml), [439 Baker](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000439/form4.xml), [440 Goldberg](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000440/form4.xml), [441 Intrator](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000441/form4.xml), [442 Jain](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000442/form4.xml), [443 McBee](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000443/form4.xml), [444 McVeety](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000444/form4.xml), [445 Venturo](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000445/form4.xml), all filed Oct 2 | All eight explicitly identify September 30 sales as satisfying tax withholding from vested/settled restricted stock units. Quantities respectively **5, 5, 5, 78,552, 4, 56,531, 5, 65,616**. These are real sales; their disclosed purpose materially changes the panic-selling framing. |
| [446 Agrawal, filed Oct 8](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000446/form4.xml); [449, filed Oct 14](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000449/form4.xml) | October 6 **3-share** and October 12 **22,579-share** sales under a plan adopted August 27, 2025, modified November 18, 2025. 449 reports 110,017 directly held shares after those rows, alongside other holdings disclosures. |
| [447 Boone, filed Oct 8](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000447/form4.xml) | October 6 acquisition of **1,460** shares from RSU settlement; **no sale** in this filing. Not an open-market purchase. |
| [448 Jones, filed Oct 14](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000448/form4.xml) | October 11 RSU settlement **42,772**; October 12 tax-withholding sale **15,811**; October 13 sales total **21,569** under a plan adopted June 18, 2026. Preserve per-row footnote distinctions. |

**BOUNDED CONCLUSION:** Actual sales are confirmed, but the screenshot cannot establish every insider, lower management as a population, maximum feasible liquidation speed, or motive. Eight displayed September 30 officers' sales are explicitly tax-related; other large displayed sales were preplanned. A plan does not prove benign motive or eliminate economic significance. Boone's filing is a counterexample to treating all recent Form 4 activity as selling, not proof that she has never sold. No current price, all-time-high comparison, complete employee census, or lifetime insider-sale aggregate was independently established. Do not route the universal panic-dumping language as verified.

**Owner/BOARD dedup before web:** VULCAN STATUS dated October 16 and October 15 S5/S3 catch-up already recognize recent Forms 4/144, but do not contain this row-level tax/plan correction. Scoped BOARD insider/10b5 search yielded no matching CRWV correction. This helper does not determine novelty significance or owner grade.

**Runtime / instruction receipt:** Git root explicitly resolved to `/home/willi/Research-workspace`. Explicit reads of root CLAUDE.md, AGENTS.md, USER.md, WALTER CLAUDE.md startup instructions, COMPLETION_SPEC and orchestration Runtime mechanics. OpenAI/Codex thread-local verification helper; exact model/session identity unavailable. Shell, web, image inspection, file write and parent messaging verified. Bare `python` missing; `python3` and requests worked. Full WALTER boot/market clearance not attempted by this narrow helper. No owner files, credentials, live bookmark API, paid access, Git index or commit mutations used.

## COMPLETION — WALTER helper — 2026-10-20
STATUS: DONE (bounded verification).
CHANGED: This file only.
RESULT: Read one offered image and 13 primary Forms 4; corrected eight officers' tax-sale framing and identified preplanned sales.
GAPS: Universal population, motive and ATH comparison unproven; no claim dependent on them is certified.
WILL_NEEDS: None.
FOLLOW-UP: Parent decides routing and commits this artifact; helper is closed out, no work running.
