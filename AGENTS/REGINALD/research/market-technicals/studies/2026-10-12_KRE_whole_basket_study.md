# KRE whole basket breadth and market study

**Authority:** Will approved the [research proposal](2026-10-12_KRE_next_research_proposal.md) with **“Okay approved. Go ahead”** on October 12, 2026. Separate from L694. **Observation end:** October 9 settled equity prices; primary Treasury series ends October 8. **Fresh history collection:** October 12, **14:37:20–14:37:35 EDT**; per-request times in the source receipt. No new intraday quote sweep, bank commission, recurring monitor, trade or threshold change.

**Result:** the weakness reaches almost the entire current KRE basket. It survives dividend adjustment and the moving-average checks. Higher long-term rates are a plausible contributor; volume does not establish heavy institutional distribution. Existing bank-credit evidence remains concentrated and older than the price observations. Whole-fund historical contributions remain unresolved.

[Charts PNG](2026-10-12_KRE_whole_basket_charts.png) · [Charts SVG](2026-10-12_KRE_whole_basket_charts.svg) · [Full bank metrics CSV](2026-10-12_KRE_full_basket_metrics.csv) · [Daily breadth CSV](2026-10-12_KRE_daily_breadth.csv)

## Coverage and breadth

All **167 bank holdings** in State Street's October 9 published basket returned usable prices for both comparison windows. They account for **99.885822% of the published weights**; the two cash entries are excluded from bank counts. All 175 requested histories, including eight benchmarks or rate references, returned. Bank currencies and response symbols/types were verified. CBC's shorter history starts November 21, 2025, but covers the study windows and moving averages. Current membership is selected at the end of the window; this is not a reconstructed July 10 portfolio.

| Measurement | July 10 to October 9 | September 11 to October 9 |
|---|---:|---:|
| Banks with negative price returns | 130 / 167 | **165 / 167** |
| Published weight in those declining banks | 87.07% | **98.79%** |
| Banks with negative dividend-adjusted returns | 127 / 167 | **164 / 167** |
| Median bank price return | −4.32% | **−5.41%** |
| Median dividend-adjusted return | −3.79% | **−5.30%** |
| KRE price return | −8.01% | **−6.62%** |
| KRE dividend-adjusted return | −7.49% | **−6.09%** |

At the October 9 close, **164 / 167** banks were below their 20-day simple moving averages and **165 / 167** below their 50-day averages. Those averages use raw vendor Close bars, all settled. This describes price weakness, not a new registered trigger or evidence that every bank's loans have deteriorated.

**Exceptions:** EGBN gained **2.25%** over the later window; CBC was barely positive, **+0.03%**. Preferred Bank (PFBC) fell **0.39%** in price but gained **0.37%** after dividends. EGBN and CBC were the two above their 50-day averages; TFIN was also above its 20-day average. Dividend adjustment changes the exact count, but not the broad conclusion.

## Banks versus other markets and interest rates

| Instrument | July 10 to October 9 price return | September 11 to October 9 price return |
|---|---:|---:|
| KRE | −8.01% | −6.62% |
| KBE broader bank ETF | −8.17% | −7.22% |
| SPY broad large-cap equities | +3.13% | +1.87% |
| IWM smaller-company equities | −5.76% | −3.44% |
| XLF broader financials | −1.76% | −4.40% |
| QQQ | +3.55% | +5.09% |
| TLT long-term Treasury ETF | −7.68% | −3.57% |

Banks underperformed the broad stock market and smaller-company benchmark. KBE also fell, so the pressure extends beyond KRE's particular regional-bank selection. This is a benchmark comparison, not a statistical estimate of a bank-specific causal factor.

The **Federal Reserve's 10-year constant-maturity yield** rose **4.56% → 5.22%, +66 basis points**, July 10–October 8; it rose **4.96% → 5.22%, +26 basis points**, September 11–October 8. On that latter exactly matched date window KRE fell **5.83% in price / 5.30% dividend-adjusted**. [Rate comparison CSV](2026-10-12_KRE_rate_comparison.csv), [Federal Reserve DGS10 via FRED](https://fred.stlouisfed.org/series/DGS10).

Higher long rates can affect bank funding, securities values, borrower refinancing and valuation. Their rise is a plausible contributor, **not a demonstrated cause or estimated share of this selloff**. FRED's latest retrieved observation is October 8; no October 9 or holiday October 12 yield is filled in. Yahoo's separate TNX index is not substituted for the primary constant-maturity series.

## Weighted declines and historical attribution

The largest percentage fall was **CCB, −48.08%** over three months, but its October 9 weight was only **0.273%**. The following table ranks the later-window declines after multiplying dividend-adjusted returns by October 9 weights:

| Bank | October 9 published weight | Four-week price decline | Fixed-weight diagnostic effect |
|---|---:|---:|---:|
| FLG | 1.004% | −14.11% | −0.142 percentage points |
| BOH | 0.926% | −11.86% | −0.110 pp |
| RF | 1.064% | −10.29% | −0.109 pp |
| CFG | 1.078% | −9.80% | −0.106 pp |
| OZK | 1.073% | −9.53% | −0.102 pp |

**These are exposure diagnostics, not actual historical fund contributions.** They treat the end-date allocations as fixed starting weights. Their full-basket adjusted-return diagnostic totals −5.88 percentage points in the later window, compared with KRE's observed −6.09% adjusted return; proximity does not authenticate the model. No one of these names explains most of the loss. [Full diagnostic CSV](2026-10-12_KRE_weighted_decline_diagnostic.csv).

We recovered the correct KRE **June 30 SEC NPORT portfolio**, filed August 28: trust CIK1064642, seriesS000012325, accession0001410368-26-089196. It has **161 equity positions**, versus 167 current bank holdings. **157 share lines match the current snapshot by exact CUSIP**; four do not, including a common issuer name with a different identifier. No silent ticker or corporate-action substitution was made. July 10 and September 11 actual allocations and the September rebalance transactions remain unobserved. Thus exact historical contribution and a complete historical membership bridge are unresolved. [Primary filing](https://www.sec.gov/Archives/edgar/data/1064642/000141036826089196/primary_doc.xml), [parsed historical holdings](../../../domain/sources/2026-10-12_KRE_basket_study/KRE-nport-2026-06-30-holdings.csv).

## Volume qualifies the bearish reading

Over the last 20 settled sessions, KRE had **12 down sessions, 7 up sessions and 1 flat session**, classified by adjusted returns. Total down-day volume was **1.75 times** up-day volume, but **average volume per down session was only 1.02 times** the average up session. The total ratio largely reflects more down days. The October 9 volume was **0.93 times** the preceding 20-session mean.

At the individual-name level average down/up volume ratios were FLG1.20, OZK1.25, ZION1.34 and EGBN0.87. Across all 167 banks the median was0.97; 76 were above1.0. That is mixed evidence rather than a uniform high-volume liquidation. No current covering or institutional-flow claim follows from these measures. Historical frozen positioning ledgers were not revived. [Volume comparison CSV](2026-10-12_KRE_volume_comparison.csv).

## Existing bank evidence and counterevidence

| Price observation | Existing evidence | Interpretation limit |
|---|---|---|
| FLG severe decline | Existing rent-regulated multifamily problem and settled RED ladder | Consistent with known bank-specific stress; does not turn every other bank's fall into the same mechanism |
| EGBN positive later window | [Primary-verified office cleanup](../../../reports/2026-10-12_EGBN_cleanup_figure_verification.md), June 30 vintage | A credible improving-bank control; investor reward is still an inferred driver |
| OZK weak through October 9 | [Executed extension and new capital](../../../reports/2026-10-12_morning-regional-bank-tape.md) disclosed October 12 | Subsequent counterevidence to near-term maturity failure; cannot be used as information already available throughout the historical window |
| CCB extreme decline | Existing KB188/189 VLY–Bluevine partner-transition evidence and WQ-228 BaaS perimeter | Possible event-related repricing, not proof of current deposit flight or a credit loss |
| Wide bank-stock decline | [Existing Q3 read plan](../../../reports/2026-10-09_Q3_earnings_read_plan.md) still finds June 30 bank-credit deterioration concentrated | Prices may be anticipating a change; current broad price weakness does not itself satisfy the registered bank-credit spread test |

CCB already fell **42.88%** July 10–September 25, then **16.23%** from the September 25 close to September 28, around the already-recorded VLY–Bluevine agreement/8-K. It recovered **8.51%** from September 28 to October 9. This timing makes the existing partner-transition question relevant, but the September event cannot explain the entire earlier decline. On-balance-sheet versus swept deposits at CCB remain unknown. No new CCB investigation is commissioned. [Event comparison CSV](2026-10-12_KRE_BaaS_event_comparison.csv).

## What this changes and what remains open

The study strengthens the **technical evidence of broad bank-equity weakness** through October 9. The most useful existing next test is whether the upcoming Q3 bank evidence broadens balance-sheet deterioration or instead shows stable funding/credit alongside macro repricing. The original L180 and other grading definitions remain unchanged. The 167-name market dataset does not expand the frozen bank-credit cohort. EGBN cleanup, mixed volume and higher rates all qualify a simple blanket credit-collapse explanation.

Exact historical fund attribution, a causal rates/credit decomposition and current positioning remain unresolved. Those limits are retained in the conclusion; this study adds no new monitoring commitment, trade recommendation, price target or credit-score change. The approved dated package is delivered with a coverage table, full bank metrics, benchmark/rate/volume comparisons, diagnostic chart and preserved primary holdings search.

## Source and calculation record

[Fetch receipt](../../../domain/sources/2026-10-12_KRE_basket_study/fetch-receipt.json), [validation](../../../domain/sources/2026-10-12_KRE_basket_study/validation.json), [daily history](../../../domain/sources/2026-10-12_KRE_basket_study/daily-history.csv.gz), [holdings series selection](../../../domain/sources/2026-10-12_KRE_basket_study/nport-series-selection.json). Yahoo is the single historical price vendor; adjusted closes are its dividend-adjusted return proxy. All old top-ten return calculations reproduce within floating-point precision. Split events are retained in validation.

An issuer weights/shares/close cross-check is coherent at a common denominator, but that denominator is about0.57% above the issuer's rounded published NAV AUM. Its gross/net/timing bridge is unresolved; this was not treated as independent exact-price or NAV validation. Published weights remain exposure diagnostics. Rejected different-trust and different-series candidates are explicitly recorded in receipts and preserved locally under ignoredraw/.

Collector: `scripts/kre_basket_study.py`. [Artifact rebuild script](2026-10-12_KRE_rebuild_artifacts.py) rebuilds the dated exports and charts from saved data without network requests. Plotting dependencies were installed only in a temporary directory; the shared environment was not modified. Regeneration uses a standard Matplotlib installation or the script's optional `--plot-deps` path.
