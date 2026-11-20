# Evidence for 8 dropped HENRY rows (collected 2026-11-20; evidence only, no verdicts)
Rows as of dropped-commit dacb0f8e86 (2026-04-15); text from `git show dacb0f8e86^:AGENTS/HENRY/workbook/PREDICTIONS.tsv`.
Methods: SPX = yfinance ^GSPC daily close (Close, auto_adjust=False), fetched 2026-11-20, data through 2026-07-15. PLTR = yfinance daily close. HY OAS = FRED BAMLH0A0HYM2 (%, 3.08 = 308bp), fetched 2026-11-20. Scripts/CSVs in the scratchpad dir (spx.csv, pltr.csv, hy.csv, an.py, h4.py, h4b.py, pl.py).

## HEN-01  NFP Feb 2026 <100K (resolve 3/6; invalidation: NFP >150K with positive revisions)
Row as written: confidence 70%, "<100K". Direction/sign is not specified beyond "<100K" (a negative print satisfies the letter).
| Vintage (ALFRED PAYEMS, thousands, level) | Dec-25 | Jan-26 | Feb-26 | Mar-26 | Feb m/m implied (Feb - Jan, same vintage) |
|---|---|---|---|---|---|
| 2026-03-06 (first print) | 158,432 | 158,558 | 158,466 | - | **-92** |
| 2026-04-03 | 158,432 | 158,592 | 158,459 | 158,637 | -133 |
| 2026-05-08 | 158,432 | 158,592 | 158,436 | 158,621 | -156 |
| 2026-11-19 (current) | 158,432 | 158,592 | 158,436 | 158,650 | -156 |
Source: `https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=PAYEMS&vintage_date=<date>` and FRED PAYEMS csv, pulled 2026-11-20.
- First print -92K confirmed by repo: memory/2026-03-06.md line 16 "NFP: -92,000 (8:30 AM ET) ... First negative NFP this cycle. Consensus +55-65K"; KB ML-HEN-092/107 "NFP -92K".
- Revisions: Jan level revised UP +34K in the 3/6 release->4/3 vintage (158,558->158,592); Feb level revised DOWN 30K total (158,466->158,436) by 5/8, unchanged through 11/19. Revision to Feb was negative, not positive.
- Not established: consensus/BLS-stated revision text from BLS (bls.gov 403s; not tried). The "implied m/m" is my arithmetic from ALFRED levels, not a quoted BLS figure; the -92 matches the repo's contemporaneous record.

## H1  SPX breaks 6494 -> CTAs flip -> $40-60B selling (2/18-3/31; invalidation: SPX sustains >7,000 for 5+ sessions)
Window 2026-02-18..2026-03-31 (30 closes). Source yfinance ^GSPC.
- 2/18 close 6,881.31. Max close in window 6,946.13 (2026-02-25). **Zero closes above 7,000** in window; longest run >7,000 = 0 sessions (invalidation not met in window).
- Min close in window **6,343.72 on 2026-03-30**.
- Closes under 6,494: **first 2026-03-26 (6,477.16)**, then 3/27 6,368.85, 3/30 6,343.72. 3/31 close 6,528.52 (back above 6,494). 3/20 close was 6,506.48 (above). So break occurred by 3/31 on closes (3 closes), not held at 3/31.
- Row note at drop (4/15): "6707 intraday breach Mar 3 not sustained close. 6494 = next threshold."
- NOT established: the CTA flip itself or "$40-60B selling" (UNSOURCED per HENRY CLAUDE.md; not measurable here). Row's letter conditions only on "SPX breaks 6494" in the prediction text; no close-vs-intraday definition.

## H4  Equity cannot bottom until HY OAS peaks (2/27-6/30; invalidation: SPX rallies >5% while HY OAS still widening)
Source: yfinance ^GSPC; FRED BAMLH0A0HYM2 (both through 2026-07-15).
- SPX lowest close in 2/27-6/30: **6,343.72, 2026-03-30**. SPX highest close in window 7,609.78 (2026-06-02).
- HY OAS in window: start 2/27 = 3.10 (310bp); **peak 3.46 (346bp) on 2026-03-30** (same day as SPX low); low 2.63 on 2026-06-17.
- HY on 3/27 3.42; 3/31 3.28; 4/8 2.94. (Row note at drop said HY 308bp on 3/3, floor rising 265->284->308; FRED series differs by day/vintage — I quote FRED only.)
- Both troughs coincide on 3/30 (SPX low and HY OAS peak same session).
- Invalidation test, definition used: for any pair of window closes i<j (2/27..6/30) with SPX[j]/SPX[i]-1 > 5% AND HY[j] > HY[i] (HY at end of rise above HY at start). Result: **1 pair-group only**, earliest pair 2026-04-14 (SPX 6,967, HY 2.84) -> 2026-05-19 (SPX 7,354, HY 2.86): HY +2bp. Script listed exactly 1 pair in total. Also tested 20-trading-day rolling: SPX >+5% with HY higher over the same 20d: 0 instances.
- Rally off the 3/30 low: first >5% above low on 2026-04-08 (SPX 6,782.81, HY 2.94 vs 3.46 at the low): HY had already fallen, not widening. Rally top by 4/9 6,824.66 (+7.6%), HY 2.90.
- Caveat: the 2bp pair is within noise of a daily-OAS series; whether "still widening" means vs start-of-rally, vs trailing trend, or from peak is not defined in the row's letter. Using HY-peak = SPX-low (3/30), no >5% rally occurred before HY peaked.
- Not defined by the row: what counts as "bottom" (SPX low 3/30 coincided with HY peak 3/30).

## H5  PLTR breaks $100 -> AI repricing (2/18-3/31; invalidation: PLTR holds >$120 through Q1 earnings)
Source: yfinance PLTR daily close.
- 2/18 close 135.38. Min close 2/18-3/31 **128.84 on 2026-02-24**; 3/30 close 137.55 (late-March low); 3/31 close 146.28. Max in window 160.84 (3/23).
- **Never closed under $100** (0 closes <100 in 2/18-5/31); never closed under $120 either (min through 5/31 = 128.06 on 2026-04-10; min 3/31-5/31 also 128.06 on 4/10).
- Q1 2026 earnings: 2026-05-04 after close (yfinance get_earnings_dates: EPS est 0.28, reported 0.33, +18.08%). Closes: 4/28 141.18, 4/29 137.97, 4/30 139.11, 5/1 144.07, **5/4 146.03, 5/5 135.91** (-6.9%), 5/6 133.79, 5/7 137.05, 5/8 137.80, 5/11 136.89, 5/12 136.00. All >$120.
- Ambiguity in the row: "Q1 earnings" could mean Q1 2026 results (reported 5/4, after the row's 3/31 resolve date) or Q4/FY25 results (reported 2026-02-02, before row creation per yfinance). Row resolve-by 3/31 precedes 5/4.

## H7  XLK breadth <40% precedes sector repricing (2/18-3/31; invalidation: XLK breadth recovers >60% sustained)
Search: `git log -S'breadth'`, grep of memory/ and AGENTS/HENRY at 07e54f82ab^.
- The row text defines NO measure (no % of constituents above what MA, no data source, no cadence). Row note at drop: "Currently <50%. Approaching trigger."
- The only defined figure in repo records: RP-HEN-6.5 (commit f83883857d, 2026-02-03), `AGENTS/HENRY/research/outputs/cluster_6_data_expansion/RP-HEN-6.5_technical_breadth_market_health.md`: table row "Technology (XLK) | 45.71% | % > 50-day MA", source MacroMicro (macromicro.me ... sp500-sectors-50ma-breadth), "early February 2026"; VX-HEN-12.05 "Tech Participation 45.7%, <40% (Danger), MacroMicro". KB ML-HEN-020 (1/26): "Tech 52.85% breadth".
- RECON_REPORT.md (at 07e54f82ab^, ~Mar 15): "XLK breadth % | <50% above 50-DMA | ~Mar 6 | ~9 days stale"; STAGE2_FINDINGS_2026-03-15.md: "XLK breadth: <50% last known (~Mar 6) | Not searched this session". TRADE.md (pre-drop) used a different stop: "recovers above 55%".
- No dated XLK breadth value after early Feb found in repo; no value ever recorded below 40% or above 60%. So the repo's implied definition is % of XLK/tech constituents above 50-day MA via MacroMicro, but the row itself does not say so. "Precedes sector repricing" has no defined repricing event/window. Not constructed from constituents (per instructions).

## HEN-02  ISM Services New Orders rolls over sharply in March (resolve 4/6; invalidation: March New Orders >58)
- Feb 2026 New Orders **58.6** (Jan 53.1). March 2026 **60.6** (+2.0). Source: ISM Services PMI March 2026 release via PR Newswire (ISM's own press release), 2026-04-06 10:00 ET, https://www.prnewswire.com/news-releases/services-pmi-at-54-march-2026-ism-services-pmi-report-302734026.html (fetched 2026-11-20): "The New Orders Index registered 60.6 percent, 2 percentage points above February's figure of 58.6 percent". Table: Mar higher 32.0/same 55.4/lower 12.6; Feb 32.8/53.4/13.8.
- Cross-check: (53.9 + 60.6 + 45.2 + 56.2)/4 = 53.98 ~ 54.0 headline (arithmetic mine, components from ISM page via search summary).
- Repo: ISM_SYNTHESIS_MAR4.md (git 07e54f82ab^) says Feb New Orders 58.6 (+5.5 pts), implying Jan 53.1. The row's own note says "+11.9pts" for a "backlog surge" (a different sub-index, Backlog of Orders) — not verified here.
- ISM website: ismworld.org report page redirects to an SSO login (ecommerce.ismworld.org/SSO/Login) — treated as blocked, not used. Press release and Haver/Trading Economics summaries used instead (labelled).
- Not defined by the row: what "rolls over sharply" means numerically other than the invalidation >58.

## HEN-03  March ISM Prices (Mfg + Services) exceeds February (resolve 4/6; invalidation: Mfg <68 AND Services <60)
| Series | Feb 2026 | Mar 2026 | Source |
|---|---|---|---|
| ISM Services Prices | 63.0 | 70.7 (+7.7) | PR Newswire ISM release 2026-04-06 (quote above): "Prices Index registered 70.7 percent in March, a 7.7-percentage point increase over February's figure of 63 percent" |
| ISM Manufacturing Prices | 70.5 | 78.3 | repo KB ML-HEN-063 (Feb: 70.5) and ML-HEN-123 (Mar 78.3, "highest since Jun 2022", logged 4/1); web-search summary of March mfg report agrees (78.3 from 70.5; fetched 2026-11-20, secondary, I did not open the ISM or PR page for mfg) |
- Both exceed Feb. Invalidation (Mfg <68 AND Svc <60) not met. Row ambiguity: "(Mfg + Services)" - could mean each, either, or sum; both rose individually.
- Mfg March release date 2026-04-01 (per KB date); services 2026-04-06 (rescheduled from 4/3).

## HEN-05  April Beige Book materially worse than March; layoffs replace attrition (resolve 5/10; invalidation: April BB improvement in 6+ districts OR hiring resumes)
Source: federalreserve.gov. April 2026 Beige Book dated 2026-04-15: https://www.federalreserve.gov/monetarypolicy/beigebook202604-summary.htm (fetched 2026-11-20). The "March" Beige Book (released ~Mar 4) is filed on the Fed site as **"Beige Book - February 2026"**: https://www.federalreserve.gov/monetarypolicy/beigebook202602-summary.htm (beigebook202603*.htm = 404).
April 2026 National Summary, verbatim:
- Activity: "Overall economic activity increased at a slight to modest pace in eight of the twelve Federal Reserve Districts, while two Districts reported little change and two Districts reported slight to modest declines."
- Labor: "On balance, employment was steady to up slightly during this reporting period, though one District noted a slight decline. Most Districts described labor demand as stable, with low turnover, minimal layoffs, and hiring mostly for replacement. Several Districts noted increased demand for temporary or contract workers, as firms remained cautious about committing to permanent hires. Many Districts reported that labor availability had improved ... some noted that AI-driven productivity improvements had enabled many firms to delay or reduce hiring."
March (Feb 2026 page) National Summary:
- Activity: "Overall economic activity increased at a slight to moderate pace in seven of the twelve Federal Reserve Districts, while the number of Districts reporting flat or declining activity increased from four in the prior period to five in the current period."
- Labor: "Employment levels were generally stable in recent weeks as seven of the twelve Districts reported no change in hiring. Contacts in several Districts cited rising nonlabor input costs, softer demand, or uncertainty ... as reasons for flat or lower employment levels."
Counts: activity growth 7 of 12 (March) -> 8 of 12 (April); flat/declining 5 -> 4 (2 flat + 2 declines). So April was not worse by district counts; "improvement in 6+ districts" not directly counted by the Fed (April: 8 reported growth, which is a level, not a change). Layoffs described as "minimal" in April; no layoffs-replace-attrition language found. Hiring: "mostly for replacement" (April), which is neither "resumes" nor layoffs.
- Not established: a per-district count of "improved vs prior" for April. District blurb seen: Third (Philadelphia) "Employment declined slightly" (April).

## Summary of gaps
- BLS pages not used (403). NFP vintages from ALFRED/FRED only.
- ISM site requires login; PR Newswire release used for services; mfg March prices from repo KB + secondary web summary.
- No XLK breadth series for Feb-Mar 2026 in repo beyond the 45.7% early-Feb MacroMicro figure and "<50%" notes.
- Intraday data not collected (all closes).
