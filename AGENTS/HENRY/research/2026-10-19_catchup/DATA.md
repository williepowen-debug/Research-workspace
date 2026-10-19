# October19 catch-up — fuel, rates and earnings clocks

## F1 December measurement recovered; common published observation pending

Approved WQ-392 pair HOZ26×42−CLZ26 throughNovember19; $95/$90.16 unchanged. Own tier-3 settlement-window estimates:

|Observation date|14:28/14:29ET Close×Volume proxy, $/bbl|Compared with $95|
|---|---:|---|
|October15|98.921255|above, candidate NOT FIRED|
|October16|99.450909|above, candidate NOT FIRED|
|October19|99.865664|above, candidate NOT FIRED|

**Canonical shared F1 state remains UNKNOWN pending BRENT's publication/adoption on the common WQ-386/WQ-392 basis.** These are qualified HENRY measurements offered to BRENT, not a claim it has published them or a TERRY position grade. No stand-down, capital permission or funding signal follows from the candidate pass alone. October15 already had an accepted TERRY reading; do not replace its history. Missing October20+ data cannot be anticipated.

Hierarchy actually attempted: CME ULSD/WTI settlement pages were accessible through web but supplied only dynamic shells, no dated leg rows. First Yahoo daily retry429; successful User-Agent retry still fails finality quality: both legs repeat October15/16 daily volume (HO48065;CL249739), and October19 row is not certified final settlement. No tier-2 final label accepted. Thus use permitted tier3: each leg's two positive-volume bars labelled14:28 and14:29ET, unrounded decimal Close×Volume VWAP, HO×42 minusCL. Never include14:30, continuous contracts or daily close as settlement.

Contract proof retained in `raw/info-{HOZ26.NYM,CLZ26.NYM}.json`: NYM, FUTURE, USD, December26, underlyingHO.NYM/CL.NYM, expireDate November30/November20 UTC respectively. Separate delivery month from differing final-trade dates. Chart metadata corroborates exact symbols/names, NY time and1-minute granularity. Same-vendor SPY control October15/16/19 has390 regular bars09:30 through15:59 each: labels start minutes. `f1-calculations.json` retains every input bar/volume and unrounded calculation. Float32 representation bound<0.0001$/bbl (prices close to documented ticks) is negligible versus minimum $3.92 distance; original near-line ±0.15 rule unchanged. Close×Volume is a permitted proxy, not tick-trade VWAP or exchange settlement. Cross-owner acknowledgment UNKNOWN.

## Rates — dated official observations via mirror, separate model decomposition

Treasury XML, CSV and web text endpoints failed/time out in retained receipts. FRED's Treasury-series mirror succeeded; mark direct Treasury download UNAVAILABLE, not data unavailable. Latest aligned nominal/real observation October16:

|Series|October7|October16|Change bp|
|---|---:|---:|---:|
|2-year nominal|4.77%|4.74%|−3|
|10-year nominal|5.28%|5.09%|−19|
|30-year nominal|5.67%|5.43%|−24|
|10-year real|2.92%|2.74%|−18|
|30-year real|3.36%|3.16%|−20|
|10-year breakeven, aligned nominal−real|2.36%|2.35%|−1|

These are daily reference yields, not intraday CPI reaction estimates. October16 curve10s2s=+35bp;10-year>5.0 standing line remains met. DFII/DGS latestOctober16; T10YIE hasOctober19=2.35 but do not splice that later observation into anOctober16 real-yield subtraction. Vendor ^TNX5.14 onOctober19 is a separate index/date.

NYFed official ACM workbook retrievedOctober19, latestOctober16: fitted10-year5.066819%, risk-neutral expected-short-rate component4.310617%, term premium0.756202%. October7→16 fitted yield−20.597bp, premium−22.858bp, expected-rate component+2.261bp: the model attributes more than the full fitted-yield decline to lower premium, partly offset by expected rates. This is model-based attribution, not identified cause or direct evidence of Fed easing. Nominal-real/breakeven and ACM decompositions are different accounting/model views; do not add their components together. Workbook revisions are possible: September30 premium0.88501 in this vintage differs from older0.8889; retain older claim as its vintage, not an arithmetic error. Official model description:https://www.newyorkfed.org/research/data_indicators/term-premia-tabs ; workbook:https://www.newyorkfed.org/medialibrary/media/research/data_indicators/ACMTermPremium.xlsx . Binary is old XLS despite .xlsx suffix; direct xlrd reader succeeded. Reproducible extracts retained.

## AAL/LUV — issuer clocks and fixed grading checklist

|Carrier|Primary release timing|Call, Eastern|Source|
|---|---|---|---|
|LUV|WednesdayOctober21 AFTER MARKET CLOSE; exact minute not stated|ThursdayOctober22 10:00ET|https://investors.southwest.com/news-events/press-releases/detail/1943/southwest-airlines-to-discuss-third-quarter-2026-financial-results-on-october-22-2026|
|AAL|October22 report expected with quarterly results; exact release minute NOT stated by call announcement|ThursdayOctober22 08:30ET =07:30CENTRAL|https://news.aa.com/news/news-details/2026/American-Airlines-Group-announces-webcast-of-third-quarter-2026-financial-results-CORP-FI-10/default.aspx|

Search summary mislabeled AAL timezone; full issuer body controls. HEN-46 resolution date becomesOctober22 (both result events), replacingOctober31 fallback; no new post-release deadline invented. Ask PROME to register HENRY wake beforeOctober21 release andOctober22 call window; a durable request is NOT evidence of a working automatic wake.

Read and retain release/8-K, appendices, transcript and guidance comparators. Grade the **original** HEN-46 row: CONFIRM=AAL Q3 adjusted EPS below−$0.70 AND/OR LUV Q3fuel/gal≥$4.10; DENY=AAL inside/above guidance AND LUVfuel≤$3.85. Preserve original middle/unsupported outcomes and fuel-vs-other-driver distinction; a fuel-margin spot proxy is not realized quarter-average fuel expense. Do not silently substitute an analyst EPS surprise for the registered company-guide test. F4 requires a raised FYguide explicitly citing fare recapture; price or yield anecdotes alone do not meet it. F2 requires Aramco/SaudiMoE primary Jazan restart, still not certified here. F3spent/no successor.

F5 repaired as a path check: raw AAL daily bars September11–October19, including each intraday low, never fell below $11.308 (=12.85×0.88). Minimum close11.68; minimum low11.64, bothOctober19; latest price decline9.105%. Thus F5 NOT FIRED on retained single-vendor path, not merely on latest close. No entry or position state is asserted. `raw/supplement-AAL.json` and supplement receipt retain full series. The unverified commencement of any actual entry remains TERRY's book boundary.

## Other owed items

LIQUID fixed cohort completed in COHORT.md. CRUISE two new owner packets and LIQUID financing first-pass consumed as dated operating/funding evidence and replied to. Historical evaluator-timing interpretation remains with PROME; no unilateral regrade. Old Asia-halt/cyberattack attribution, full macro consensus, Muse/TLT-flow sources and historicalDGS30 scope remain explicitly unresolved. Current late data repair does not certify those unrelated claims. No new monitor, position or thresholds.
