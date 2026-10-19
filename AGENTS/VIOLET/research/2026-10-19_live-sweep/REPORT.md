# Live-source data sweep — October 19, 2026

VIOLET, requested by Will after the saved closeout. Audit window **September22–October19:20 equity/options sessions**. Live boot17:53ET; source-by-source pull times, URLs, HTTP results and hashes in `sources/manifest.json`, `FRED_api_manifest.json`, `futures-manifest.json` and `jpy-source.json`. This is a bounded source/ledger sweep, not a promise that unpublished observations or old option snapshots can be manufactured.

**Recovered18 missing ledger observations:**14 dated VX futures entries,2 matched oil-volatility rows and2 yen realized-volatility rows. The initial verbal yen-gap estimate of3was one too high. All available recent six-index spot cells and native correlation observations reconcile with their saved publisher sources. Core index interpretation remains unchanged: Friday stress was real; Monday eased; systemic credit-origin confirmation remains incomplete. RED/LIQUID retain their grades. No new trade, threshold, monitor or publishing chore.

**Final targeted publisher check:** 2026-10-19T22:00:57.253417+00:00 (UTC): VIX, SKEW, DSPX and VIXEQ returnedHTTP200 and still endedOctober16 in the retrieved histories. This is positive inspection of the dated rows, not an assumed publication hour. Evidence:`final-frontiers.json`; original first captures remain intact.

## Coverage and remaining publication limits

| Feed | Current captured frontier | Bounded verification / repair | Limit |
|---|---|---|---|
|Cboe VIX/VIX9D/VIX3M/VIX6M/VVIX/SKEW|VIX/SKEW October16; other four October19|118published cells verified out of120possible cells over20sessions;2target cells absent in retrieved histories|October19VIX18.44/SKEW161.86are dated quotes, not final daily rows. Full cash row remainsTICK; no official finalVIXratios.|
|Cboe monthly VX futures|October19settlement|20dated pairs verified;14missing entries filled;0value/pair mismatches|Both symbols, settlementdate and<5calendarDTEroll preserved. Historical backfill is not a first-publication archive.|
|Cboe COR1M/COR3M/COR30D|All October19|60native cells verified over20sessions|Today9.68/13.66/10.37are official for the correlation legs, but composite row/constituent estimate remainsTICK without VIXfinal. Retired first-tell stays retired.|
|Cboe DSPX/VIXEQ|Daily historyOctober16; October19quotes36.50/40.92|Native histories and timestamped quotes saved|No dailyOctober19 dispersion/equalweight-vol grade from a quote.|
|Cboe OVX|Raw officialOctober19=50.22|Added missing matchedOctober14/15rows; all19available matched sessions represented|October19OVX/VIXfinal pair unavailable until VIXdaily19 exists. Current50.22/18.44 ratio2.72is PROVISIONAL, not a final canary grade.|
|JPY realized spine|Vendor daily-dateOctober19; live RV10/RV20=2.57%/4.38%|FilledOctober15/16RV-only rows;20session dates represented|Today's FX bar is intraday-so-far; FXYIV13.4%/IV-RV5.22is off-hours STALE. Historical FXYIV/OI not filled.|
|MOVE primary|October16=101.10|18publisher-available observations in window match ledger;0mismatches|NoOctober12or19row in this primary table; don't create a synthetic holiday/current close.|
|CFTC VIX futures|ReportOctober13|Weekly and annual publisher files agree; all4recent reports present|Current archive/Last-Modified does not certify originalFridaypublication. Latest leveragednet+1,105,p91.0unchanged.|
|VIX option snapshots|October19pull,7forward expiries|Refreshed current chain/volumes; nonzero grossOI retained|Vendor OI observation vintage not independently established; current chain cannot reconstruct missing oldRTHsnapshots or identify initiated net hedge flow.|
|Derived cheap-tail logs|Last exact complete daily inputsOctober16|DORMANT2/4; historical disposition preserved|A derived alert history is not a native daily price series. Missing old catalyst-vintage states are not invented; current incomplete publication cannot reopen WQ418PASS.|
|Credit/rates/funding|See below|12FREDAPI series retrieved live;0differences versus existing owned caches where present|LATEST-REVISED basis; existing owner first-publication grades are not replaced.|

Data manifest/audits: `audit-summary.json`, `spot-audit.json`, `futures-audit.json`, `correlation-audit.json`, `FRED-audit.json`. Native cash cells still absent are explicitly listed, not silently carried forward as official. The quoted values retain their own last-trade times: VIXcomplexOctober19 16:15:01ET;SKEW17:00:20ET. DSPX/VIXEQquotes16:02:02ET. OVX delayed feed has an explicit−05:00offset; the official daily CSV, not a converted intraday stamp, supports50.22.

## What the repairs establish

The14missing futures entries were source holes, not an unresolved permission or convention barrier. Existing `backfill.py::compute_m1m2` and saved Cboe settlement files support self-describing same-day rows; each new entry now carries its own settlementdate and exact monthly contracts. Prior generic “futures convention unresolved” language must not be used to leave recent recoverable blanks. No old unlabelled series was rewritten wholesale.

Oil October14/15 recovered from date-matched Cboe OVX/VIX histories. Each percentile/quantile uses only matched history ending that observation date. Both reconstructed ratio states areCALM under that bounded source history. Current spot-level oil risk is not cleared by this ratio state. The available saved history startsSeptember18,2009; do not claim the fetched dataset includes earlier years merely from the script's generic full-history description.

Yen October15RV10/RV20=2.74%/4.76%,October16=2.55%/4.76%,bothCALM. Each historical rolling quantile uses its own trailing3year window, excludes later observations and leaves historical option fields blank with an explicit limitation. Existing timestamped intraday/option snapshots are not retrospectively rewritten as end-of-day observations. Reconstruction does not establish the values first available at those historical times.

## Live credit and funding bridge

The publicFREDCSV client timed out on12requests. The documented existing FREDAPI credential path then returnedHTTP200for all12series; credentials and secret-bearing URLs were not printed or persisted. These were transport failures, resolved by the officialAPI—not proof that the observations were unavailable. Similarly MOVE returned403withrequests; existing urllib/User-Agent method returnedHTTP200and the structured primary table. Both failed and successful transport receipts remain recorded.

| Series | Latest observation | Value / basis |
|---|---|---|
|HY /CCC OAS|October16|331/1297bp;FREDICEBofA latest-revised|
|IG /BBB /BB /B OAS|October16|85/106/203/335bp; same source/basis|
|10Y /2Y Treasury /10Yreal|October16|5.09%/4.74%/2.74%;FRED mirrors, BOND owns rates judgment|
|SOFR|October16|NYFedPRIMARYmedian3.88%,99th3.95%;FREDmirror agrees|
|IORB|AdministrativeOctober19row3.90%; same-dateOctober16also3.90%|Only matchOctober16withSOFR16:median−IORB−2bp,99th−IORB+5bp|
|FRED VIXCLS|October16|19.99; source frontier distinct from Cboe quote|

[NYFed SOFR](https://markets.newyorkfed.org/api/rates/secured/sofr/last/5.json) and [FRED HY](https://fred.stlouisfed.org/series/BAMLH0A0HYM2) independently re-opened in the web client. SOFR covered volume$2,925B is not FICC sponsored volume. AdministrativeIORBOctober19is not evidence that today's repo transactions have been published. LIQUID's saved domain report retains the separate SRF/reserve/dealer/ETF evidence and measurement limits; this sweep adds no fund-failure, collateral-call or systemic-funding grade.

HY331is still the already-graded October16observation, not a new Monday session or fourth count. LIQUID's325/323/331sustain grade and LIQ07S2 remain its own. No reserve-channel loop observed within the frozen window does not clear laterFriday, hidden collateral or offshore dollars. Earlier credit widening and Friday volatility remain sequence, not credit-origin causation. OriginalOctober13→November17WATCH stays.

## Registered lines, routing and remaining duties

RED'sFT10remains the already-graded October14fire. SKEWofficialrun remains6throughOctober16until an October19daily observation is retrieved; same-day161.86quote cannot extend it. At-use source/mirror integrity receipt: `skew-integrity.txt`,17:58ET,23/23overSeptember16–October16within0.005. This bounds that read, not future publications.

Friday9D/VIXandfuturesinverted;3Mcash1.0255anddailyVVIX109.91didnotmeettheir distinct registered inversion/120lines. Monday officialVVIX106.93 remains below120; current3M/VIX1.0629uses a quote denominator and is provisional until VIXfinal. No new regime phase, scenario weight or Path-Afire. WQ410COR1Mfirst-tellretired; WQ418pre-CPIwindowclosed/PASSED.

PROME receives this sweep's coverage/repair count and publication gaps. WALTER receives a short source-frontier update for existing HENRY/LIQUID/RED consumers; no duplicateFT10fire alert. No peer canonical figures or grades edited. Existing duties: actual remaining final publications;October21AMexpiry,October28FOMC,November17lagendpoint,November18VIXexpiry,December16L441recheck. Tooling rider/correlation-helper basis repair remain separate; no new tool build. Deck PAUSED WQ460 and Helm RETIRED WQ461; no publishing work.

**Will decision: none.** Source-dependent limits are missing official target-date rows, off-hours/historical option data and original-publication vintage. No blanket “all data complete” assertion extends beyond the declared feeds/window. Current snapshots and durable source bytes are now available for the next desk session.
