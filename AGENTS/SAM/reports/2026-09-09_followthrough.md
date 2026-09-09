# SAM follow-through — September 9, 2026

**Available work completed; startup promotion withheld, futures feed activation withheld, future releases still pending.** No trade, successor thesis or prediction grade. Source retrievals span 22:02–23:31 UTC September 9; source observation dates below govern freshness.

| Requested step | Result | Remaining dependency |
|---|---|---|
| Boot validation | Old Case 02 classified CASE-BUG; versioned replacement frozen; four fresh judgment responses recorded; orientation 21/21 PASS | Case 02 failed both rounds. Original startup instructions restored; candidate not promoted |
| BOJ pricing | New image visually reviewed, all five rows validated and ingested; repeat wrote zero rows | Next publisher image requires a new review |
| Near research deadlines | Funding, broker baseline, BOJ provisional/forecast, EIA and CFTC baseline refreshed; replacement pair assessed | Sep-11 CFTC/CPI unpublished; reliable replacement settlement feed not yet active |
| Sep-18 preparation | Original SAM-28/31 rows snapshotted; evidence and review sequence assembled; infrastructure dispositions recorded separately | BOJ/CPI/FOMC and window boundary still ahead; no early grades |

## BOJ pricing restored

[Totan chart](https://www.totan.com/archives/15647), printed **September 9, 15:15**, timezone not printed/JST assumed: September meeting OIS **1.2213%**, incremental change **0.2440pp**, **98% incremental 25bp equivalent**. October/December/January/March equivalents are 27/61/35/42%; cumulative counts 0.98/1.25/1.86/2.21/2.63 are not probabilities. Indicative OTC medians under the publisher's policy-only model, not trades or an unconditional forecast.

The original transparent PNG was inspected using a white display background; original bytes retained. [Review](../workbook/boj_ois_reviews/2026-09-09T1515-JST.json), image SHA256 `b48a71fb4cfec9191408059f1cfb07316eded17504cce4d103ffb8c80b5a239f`. Live validation passed at 22:20 UTC; ingestion at 22:23 UTC appended five rows. Live repeat at **23:31:06 UTC** confirmed the same chart and **0 new rows**. Existing history remains intact. Conservative review expiry is September 18 00:00 JST, or sooner if the image changes.

## Funding and intervention evidence

| Observation | Source vintage | Finding |
|---|---|---|
| SOFR / matched IORB | Sep-8 transactions / Sep-8 rate | 3.64 / 3.65%; **−1bp** spread; SOFR 99th 3.73%, **+8bp** over IORB; SOFR volume $2,904B |
| EFFR | Sep-8 | 3.63%; target 3.50–3.75% |
| HY / IG OAS | Sep-8 | **267 / 81bp** |
| Unsecured yen overnight | Sep-9 provisional | **0.977%** weighted average |
| Central GC T/N commentary / Tokyo repo benchmark | Sep-9 | Transactions around **1.005%** / benchmark T+1 **1.000%**; different observations |

Primaries: [NY Fed SOFR API](https://markets.newyorkfed.org/api/rates/secured/sofr/last/10.json), [EFFR API](https://markets.newyorkfed.org/api/rates/unsecured/effr/last/10.json), [IORB](https://fred.stlouisfed.org/series/IORB), [ICE HY](https://fred.stlouisfed.org/series/BAMLH0A0HYM2), [ICE IG](https://fred.stlouisfed.org/series/BAMLC0A0CM), [Central daily report](https://www.central-tanshi.com/media/files/_u/short_term_market_report/centdaily20260909.pdf). Match IORB to September 8; the fetched series also contains later dated rows, which are not used. These witnesses do not establish a funding cascade; they do not measure offshore yen swaps.

**The independent prior-baseline search succeeded.** [Ueda Yagi September forecast](https://www.uedayagi.com/wp/wp-content/uploads/2026/09/202609jukyu.pdf) is dated September 3; the publisher's HTTP Last-Modified is September 3 09:40:41 UTC, consistent with its September 3 listing. Page 2 was visually inspected. It anticipated a September 9 fiscal drain of **¥3,600B**, including 5Y issuance. This is a month-ahead broker expectation, not a same-day forecast. Its timing is supported by publisher metadata, not a third-party archival capture.

| Settlement date | Ueda Sep-3 fiscal forecast | BOJ later forecast | BOJ outcome | Outcome minus Ueda / BOJ |
|---|---:|---:|---:|---:|
| Sep-7 | +¥400B | +¥320B | +¥330B final | −¥70B / +¥10B |
| Sep-8 | +¥100B | −¥560B | −¥1,100B final | −¥1,200B / −¥540B |
| Sep-9 | −¥3,600B | −¥3,360B | **−¥3,590B provisional** | **+¥10B / −¥230B** |
| Sep-10 | +¥800B | **+¥220B** | Not yet published | Unknown |

All conversions are from source units of ¥100 million. Earlier final figures retain their [Sep-8 evidence package](2026-09-08_catchup-assessment.md). New primaries: [Sep-9 provisional](https://www.boj.or.jp/en/statistics/boj/fm/juq/d_release/jx/jx20260909.xlsx), [Sep-10 forecast](https://www.boj.or.jp/en/statistics/boj/fm/juq/d_release/jp/jp20260910.xlsx). Sep-9 net current-account change is separately −¥3,520B and outstanding accounts ¥411.66T. Sep-10 projected net addition is ¥990B.

**Inference:** September 9's large gross drain was already anticipated as ordinary fiscal funding; it supplies little incremental evidence of intervention. September 8 remains an unexplained drain relative to both baselines. Forecast errors, month-ahead uncertainty and holiday/value-date alignment prevent identifying an operation amount or exact trade date. Japan's settlement series still cannot exclude a U.S.-only operation. The Central September forecast also prints −¥3,600B, but its September 9 modification timestamp prevents treating it as independently authenticated pre-event evidence; it is corroboration only. No “no operation” conclusion.

## Positioning, energy and replacement measurement

CFTC's current publication remains **September 1**, rechecked September 9. Legacy non-commercial net **−92,227**, longs 117,169, shorts 209,396, OI 411,882. TFF leveraged funds: longs **58,529**, shorts **160,717**, net **−102,188**; weekly long change −7,999 and short change +17,147. Both snapshots predate the rally; neither establishes subsequent covering. Full cohort arithmetic and Sep-11 instructions are in the [review packet](../docket/2026-09-11_CFTC_REVIEW.md).

[September EIA STEO](https://www.eia.gov/outlooks/steo/pdf/steo_full.pdf), released September 9 with inputs finalized September 3, continues to anticipate constrained oil exports through end-2026, Middle East production below pre-conflict levels until 2Q27, and further inventory draws. It forecasts Brent around $90 in 2H26 and U.S. distillate inventories below 100 million barrels in September. These are forecasts, not observed recovery or live oil prices. Japan's energy headwind remains; weekly petroleum and August trade will supply further actuals.

The **December 2026–March 2027** fixed pair has confirmed contract dates and an exchange-settlement anchor. However, Yahoo rounds the March settlement enough to change the proxy by **3.06bp**, and its September 9 last-trade clocks differ by **10h29m46s**. **Contract choice validated; existing vendor feed not cleared for automatic replacement.** [Full validation and activation requirements](../research/outputs/2026-09-09_followthrough/FUTURES_PAIR_REVIEW.md). Existing Sep–Dec ledger and September 14 hard stop are unchanged.

## Review handoff

[Sep-18 adjudication packet](../docket/2026-09-18_SAM28_SAM31_REVIEW.md) carries original terms, historical candidates, missing price/episode conventions and the CPI→BOJ→close sequence. [Infrastructure agenda](../INFRA_AGENDA.md) now records all four dispositions under the original August 21 ruling; the disposition requirement has been fulfilled by action, not by assigning a fictitious exact deadline.

Evidence, collectors, calculations and hashes: [research directory](../research/outputs/2026-09-09_followthrough/). [Boot assessment](../evals/runs/2026-09-09_boot-promotion/ASSESSMENT.md). Failed downloads are recorded; browser-read CME values are explicitly distinguished from downloaded raw files. No source absence has been replaced with a stale current quote.

## Verification

All **40 script tests pass** (36 boot/BOJ/context tests plus four existing futures expiry/freshness guards). The first run exposed a test pinned to the live phrase `CURRENT UNAVAILABLE`; after restoring BOJ pricing that expectation was obsolete. The test now injects an explicitly unavailable fixture source and still verifies complete context, no network, no mutation and missing-data preservation. The 36-test suite then passed; no production monitor behavior was changed by this test repair.

Read-cap and weekday checks pass; STATUS is 19,513 bytes/137 lines and MEMORY 12,736 bytes/80 lines. Frozen THESIS, prediction and trade files remain byte-identical; BOJ ledger preserves its original prefix with exactly five appended rows. Eval history preserves its original prefix with exactly four actual-run rows. Separate fresh orientation coverage and ledger-hash proof are in the eval assessment.

Consumer scans for the HY refresh found dated July/September 7 records in BOND/BOARD, not incorrect September 8 values; they remain historical. Own prior reports/before-images likewise remain unchanged. The current NEXUS brief is refreshed at closeout. No peer messages or peer-file edits were made. Final validation details: `2026-09-09_followthrough-validation.json`.
