# SAM stale-data sweep — September 14 ET / September 15 JST, 2026

## Result

Live summaries, the candidate rider, seven institution profiles and forward calendars have been reconciled with the latest obtainable sources. All 19 root workbook TSVs passed field-count checks and have explicit cadence classifications. The retired v1.7 frame, three OPEN prediction terms, and historical trading records are unchanged. “Latest available” is recorded separately from “recent observation.” No peer messages were sent; findings are available in NEXUS_BRIEF.

## Material corrections

### 1. Positioning: legacy net long does not mean leveraged funds are long

September 8 CFTC legacy net is +10,796; leveraged-fund TFF net remains −49,098 and asset-manager net −570. Legacy longs rose 61,622, shorts fell 41,401; OI rose 87,753 to 499,635. Both TFF sides reconcile to OI including spreading. Rising aggregate OI cannot exclude forced covering within a cohort. The old “not a squeeze” conclusion was too strong and has been removed from current tables. The September 11 review is resolved; September 9–14 is outside this positioning snapshot. [CFTC TFF](https://www.cftc.gov/dea/futures/financial_lf.htm), [review and calculations](../docket/2026-09-11_CFTC_REVIEW.md).

### 2. Named institutions: August quarterly reports had not reached the profiles

| Institution | June 30 disclosure now recorded | Main limit |
|---|---|---|
| Nippon | Internal ESR 190% versus 195% March; regulatory 195% group / 206% standalone | Internal decline mainly rising rates; models differ |
| Meiji Yasuda | Group ESR 209%, lower of standard 214% and internal 209% | Valuation changes are not sales |
| Sumitomo | Internal consolidated ESR 197%, unchanged | Preliminary; ESR page updated August 27 |
| Daiichi | Internal group ESR about 206%, source-reported decline about 13pp | Higher mass-lapse risk and M&A effects; rounded estimates |
| Fukoku | Foreign securities ¥1,875.779B; foreign bonds ¥974.463B | Stock increases do not prove purchases |
| Japan Post | Group assets ¥58,286.805B; standalone foreign securities ¥2,134.726B | No comparable June ESR established in reviewed workbook |
| Norinchukin | Credit/other assets ¥21.8T vs ¥22.2T March; securities revaluation +¥54.8B | Redemptions plus new investment, not identified forced sales; no June CLO-only balance established |

Each [profile and TRACKER](../insurers/TRACKER.md) links its issuer source and saved evidence. Quarterly balance sheets do not establish the existing Channel-1 reactivation requirement: direct foreign-credit net sales in two consecutive windows at two eligible institutions. March CLO ¥10.1T and March CET1 17.81% remain dated observations. Unsupported claims of a Big-3-only ESR disclosure obligation have been withdrawn from current headers. Old plans, position sizes and May/June interpretations remain explicitly historical.

### 3. GPIF: reconcile accounting scope before computing sale capacity

The latest report is still FY2026 Q1. Its headline GPIF assets are ¥317,759.6B, but its allocation table totals ¥320,373.2B because it includes the Pension Special Account (about ¥2.6T). Displayed components sum to ¥320,373.1B, a rounding difference. Neither total should be overwritten. Foreign bonds ¥81,145.4B / 25.33%; current policy target 25%, band ±5pp. A static broad-category reduction to 20% is ¥17,070.76B, not a UST-specific sale estimate. Hedged foreign bonds may be classified under domestic bonds. [Q1 report, PDF pages 2–3](https://www.gpif.go.jp/operation/38371785gpif/2026_1Q_0807_en.pdf), [current policy](https://www.gpif.go.jp/gpif/portfolio.html).

**WALTER-010 disposition:** broad band/headroom arithmetic checked; third-party $62B UST capacity cannot be reproduced from this category table. GPIF assets and official FX reserves are separate holders. Capacity, allocation drift and intervention funding are not transactions. Scope is now documented beside the ledger schema; existing numeric rows were already valid.

### 4. Short bills and carry attribution

MOF 3M issue 1406, September 11 auction: average yield **1.1149%**, cutoff **1.1867%**. Six-month issue 1405, September 9: average **1.2887%**, cutoff **1.3009%**. These do not validate social-media September 14 secondary-market quotes of 1.25/1.34% or the historical-high claim; dates and yield bases differ. [3M result](https://www.mof.go.jp/english/policy/jgbs/auction/calendar/etbill/etbillresul/eresul20260911.htm), [6M result](https://www.mof.go.jp/english/policy/jgbs/auction/calendar/etbill/etbillresul/eresul20260909.htm).

**WALTER-007 disposition:** bill auction evidence obtained; secondary quotes/superlatives remain unverified. A technology-stock headline cannot prove the absence of a carry channel. CFTC cohort decomposition and actual funding observations are the independently checked evidence. No causal “AI, therefore no carry unwind” conclusion adopted.

### 5. Funding and official-action monitoring

Latest obtainable New York Fed effective-date series: **September 11 SOFR 3.62%, EFFR 3.63%**. Same-date IORB **3.65%** gives SOFR−IORB **−3bp**. FRED/ICE September 11 HY OAS **265bp**, IG **80bp**. [NY Fed SOFR](https://markets.newyorkfed.org/api/rates/secured/sofr/last/10.json), [EFFR](https://markets.newyorkfed.org/api/rates/unsecured/effr/last/10.json), [IORB](https://fred.stlouisfed.org/series/IORB), [HY](https://fred.stlouisfed.org/series/BAMLH0A0HYM2), [IG](https://fred.stlouisfed.org/series/BAMLC0A0CM).

September 14 Central Tanshi: unsecured O/N provisional **0.977%**, Tokyo repo T+1 **1.000%**; GC T/N commentary about **1.005%** is separate. [Broker report](https://www.central-tanshi.com/media/files/_u/short_term_market_report/centdaily20260914.pdf).

BOJ fiscal factors, ¥B (source units ¥100M converted): September 10 final **+340**, projection +220, residual +120; September 11 final **−1,060**, projection −1,040, residual −20; September 14 final **+1,450**, projection +1,360, residual +90. Finals equal provisional. These are forecast differences, not intervention amounts. September 7–8 attribution stays unresolved; Japan settlement data cannot exclude a US-only operation. September 15 projection −590B is not an actual. [BOJ daily source directory](https://www.boj.or.jp/en/statistics/boj/fm/juq/index.htm); exact worksheets and hashes are in the source manifests.

**WALTER-016 disposition:** [Reuters September 8 reporting](https://www.marketscreener.com/news/us-treasury-chief-bessent-backs-using-us-financial-power-as-foreign-policy-tool-ce785bd9d88ef724) corroborates Bessent's SMU remarks as referring back to July's joint intervention. No Treasury/SMU primary transcript located in the targeted search; primary verbatim verification remains unavailable. No new September operation or FIMA financing is inferred. Unauthenticated social-account BOJ statements remain unadopted.

### 6. Domestic data, calendars and market clocks

- July customs balance is **−¥638.3B**, imports **+27.9% YoY**, from the August 28 revised stage. −¥634.5B / +27.8% is the provisional vintage. Crude volume/value fields were already current in the ledger. [Customs revised XML](https://www.customs.go.jp/toukei/shinbun/trade-st/2026/2026075.xml).
- CPI ledger already contains Tokyo August **1.9/1.8/2.0%**, 2025 base; warm reference now includes it beside July national **1.9/1.8/1.9%**. Next national release September 18; do not roll dates forward before publication.
- Raw BOJ 2026 calendar confirms **October 1 Tankan and September-MPM Summary of Opinions**, **September 28 July minutes**, and **October 30 Outlook Report**. Added near-term September 17 Flow of Funds/MOF flows, September 18 CFTC and September 25 Japan BIS release. Calendar and catalyst rows now match. [BOJ calendar](https://www.boj.or.jp/en/about/calendar/index.htm), [MPM table](https://www.boj.or.jp/en/mopo/mpmsche_minu/index.htm).
- Existing startup marks remain dated: MOF September 14 curve; September 15 11:15 JST reviewed Totan; September 14 completed USDJPY. Older bank ADRs, ETFs, VIX/S&P/DXY rows were refreshed separately from Yahoo with per-instrument clocks. No mixed-clock oil-in-yen multiplication or unregistered five-session count was manufactured.
- BIS global GLI latest-observation API still returns **2026-Q1**, but its values were revised: total yen credit **¥65.83T → ¥65.91T**, loans **¥42.01T** at stored precision, debt securities **¥23.82T → ¥23.90T**. The old append-only loader silently skipped same-quarter revisions. It now replaces changed observations by quarter/series and preserves unchanged timestamps; two regression tests cover revisions/idempotence and duplicate rejection. Ledger regenerated from the saved source. USD figures retain the explicit 158.65 JPY/USD translation convention, not a fresh FX quote. These remain broad borrowing stocks excluding FX swaps, not measured carry positions; the retired v2.0 verdict is unchanged. [BIS API](https://stats.bis.org/api/v1/data/WS_GLI/all/all?lastNObservations=1&format=csv). The September 25 Japan banking release is a different dataset. GPIF Q1 and August MOF sector flows are also publication-current, not silently stale.

## Genuine gaps and next checks

| Gap | Current disposition / next check |
|---|---|
| Actual offshore yen cross-currency basis | Unavailable; expired CME residual frozen/unwired. No replacement feed activated. Requires an actual instrument and source controls. |
| Current CME FedWatch probabilities | CME tool opened, but QuikStrike returned access denied; old Sep-10 54% removed from current table. Secondary/other-venue probabilities not substituted as CME. |
| June Norinchukin CLO-only balance/CET1; comparable June Fukoku/Japan Post ESR | Not established in the reviewed sources. Named gaps remain in profiles; no stale-number carry-forward as current. |
| September 15 20Y auction | Not published at the 12:21 JST check (HTTP 404); stays forward until actual result. |
| SAM-28/31 episode conventions | Existing ambiguity preserved; no retrospective term changes. Review September 18 close. |
| Intervention funding/account split | Pending future MOF/FRBNY disclosures; approximate November dates remain estimates. |
| New half-year institutional disclosures | Approximately November, issuer dates to confirm. Quarterly stocks alone cannot prove flows. |

## Evidence, coverage and closeout

[Ledger inventory](../research/outputs/2026-09-14_stale-sweep/ledger-inventory.tsv), [arithmetic](../research/outputs/2026-09-14_stale-sweep/calculations.json), source manifests and raw files are under `research/outputs/2026-09-14_stale-sweep/`. Before-images preserve changed current files. HTTP 200 alone is not acceptance: FRED graph URLs returned HTML/404 and were replaced by authenticated API observations; one guessed BOJ operation index and a BIS PDF URL returned 404. Failed attempts remain in manifests, not accepted data.

Scope: boot/live surfaces, all root workbook ledgers, seven institution profiles, owner research review, forward docket, candidate rider and current thesis sections. Historical reports, frozen predictions, old trade records and archives are preserved. This is a stale-data sweep, not a fresh full geopolitical or successor-thesis study. Shared VIOLET/PROME edits prevent pull/push under repository rules; SAM changes are committed locally with explicit paths.

Validation results are recorded in `research/outputs/2026-09-14_stale-sweep/validation.txt` after final checks.
