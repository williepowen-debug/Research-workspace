# Honest-name test of every scripted source, 2026-11-23

**Ordered by Will** in PROME's chat 2026-11-23 13:57 ET (WQ-735 approved with a condition; record `PROME/proposals/2026-11-23_wq735-RULED.md`). Run by PROME prome-77 from the laptop, 13:59:54 to 14:01:35 ET (stamps in `probe.tsv`), Statistics Canada and the price-library run between 14:01 and 14:05 ET (bounded by the last probe stamp and commit 3f1dcdfd35; an earlier draft of this file carried typed clock times that ran ahead of the clock). Script: `probe.py` beside this file.

## Method

One request per source under the client string `research-bot/1.0`, at the address the desk's script really asks for (a dated file, a series, a search), with the desk's own key where the source needs one. No retry and no second identity. Nine small or flagged answers were fetched a second time under the same honest name to read the body (AGSI, FRED graph, Wayback, Bank of England, Japan MoF, Cboe settlement, ChartExchange, TrendForce); all nine held real data, and `fred.stlouisfed.org` was reclassified from unclear to works on that reading (199 bytes of real rows).

## Result: 54 sources, 49 work, 3 refused, 2 gave no answer

| Source | Desks | Honest name |
|---|---|---|
| agsi.gie.eu | BRENT,DEWEY,HANS | works |
| alsi.gie.eu | DEWEY | works |
| api.hkma.gov.hk | ZHAO | works |
| api.nasdaq.com | REGINALD | no answer |
| api.stlouisfed.org | BRENT,CARL | works |
| cdn.cboe.com | HENRY,RED,VIOLET | works |
| cdn.finra.org | REGINALD | works |
| chartexchange.com | REGINALD | works |
| data-api.ecb.europa.eu | HANS | works |
| data.texas.gov | LABOR | works |
| data.wa.gov | DEWEY | works |
| dos.fl.gov | MARCO | works |
| feeds.bbci.co.uk | HAWK | works |
| feeds.reuters.com | HAWK | no answer |
| fred.stlouisfed.org | BRENT,ZHAO | works |
| gasprices.aaa.com | CARL | works |
| home.treasury.gov | SAM | works |
| iq.usembassy.gov | FALCON | refused |
| markets.newyorkfed.org | LIQUID | works |
| news.google.com | HAWK,WALTER | works |
| oag.ca.gov | DEWEY | works |
| pddata.dtcc.com | LIQUID | works |
| query1.finance.yahoo.com | FORGE price tool (all desks) | works |
| rigcount.bakerhughes.com | BRENT | refused |
| securitiesfilings.fdicconnect.fdic.gov | OZK,REGINALD | works |
| services.nvd.nist.gov | DEWEY | works |
| services9.arcgis.com | FALCON | works |
| stats.bis.org | SAM | works |
| transtats.bts.gov | MARCO | works |
| trends.google.com | MARCO | works |
| web.archive.org | MARCO | works |
| www.aljazeera.com | HAWK | works |
| www.atg.wa.gov | DEWEY | works |
| www.bankofengland.co.uk | HANS | works |
| www.banxico.org.mx | MARCO | works |
| www.cboe.com | FORGE,VIOLET | works |
| www.cftc.gov | BRENT,LIQUID,SAM,VIOLET | works |
| www.chinamoney.com.cn | ZHAO | works |
| www.cisa.gov | DEWEY | works |
| www.customs.go.jp | SAM | works |
| www.dol.gov | MARCO | works |
| www.eia.gov | BRENT | works |
| www.gpif.go.jp | SAM | works |
| www.investing.com | VIOLET | refused |
| www.ishares.com | DEWEY | works |
| www.mof.go.jp | SAM | works |
| www.newyorkfed.org | DEWEY | works |
| www.pbc.gov.cn | ZHAO | works |
| www.ssga.com | DEWEY,VULCAN | works |
| www.totan.com | SAM | works |
| www.trendforce.com | VULCAN | works |
| www.trepp.com | CREED | works |
| www.twc.texas.gov | LABOR | works |
| www150.statcan.gc.ca | MARCO | works |
| Yahoo price library (yfinance) | every desk, through the FORGE price tool and 20 desk scripts | mixed, see below |
| www.sec.gov, efts.sec.gov | DEWEY, REGINALD | not tested: already sent the declared client name SEC requires |

## The price tool (Yahoo, through yfinance 1.4.1)

The library builds a Chrome-imitating session by default. Run once with a plain session named `research-bot/1.0`, in that same window: last price, quote time, an index (^VIX), a future (CL=F) and a currency (HKD=X) came through. The first history call, the company-info call and both option calls returned "Too Many Requests". One run cannot tell an identity refusal from an ordinary rate limit, and it was not retried. **The price tool is NOT switched.**

## Not working under the honest name (the 12/07 list)

| Source | Desk | What the desk would lose | One proposed replacement |
|---|---|---|---|
| iq.usembassy.gov (403, also 11/20) | FALCON | the automatic watch on US Embassy Baghdad security alerts | the State Department's travel-advisory feed at travel.state.gov, untested |
| rigcount.bakerhughes.com (403, also 11/20) | BRENT | the weekly US rig count behind BRT-26 | EIA's rig series, which is monthly and so slower; untested |
| www.investing.com (403, also 11/20) | VIOLET | its primary reading of the MOVE bond-volatility index | none free and official found yet; Yahoo's ^MOVE is the desk's own cross-check and the desk calls it unreliable alone |
| api.nasdaq.com (no answer in 30 s, also 11/20) | REGINALD | settled daily bars for its tickers | the fleet price tool's daily bars, if that tool passes |
| feeds.reuters.com (host does not answer) | HAWK | nothing: one script already marks this feed dead | delete the two remaining lines |
| Yahoo, cookie-based calls | every desk | company info and option chains for certain; the first history call also failed | to be compared by 12/07 |

## Limits

- One request per source, one machine, one minute of one day. A source that answered may refuse a different file or a faster cadence.
- No script was run under the honest name except `FORGE/tools/market-data/vix_futures.py` (switched and run in that same window, settlement 2026-11-20 parsed). "Works" means the source served real data to the honest name, not that each script's parser was exercised.
- No browser-name request was sent for comparison, so a refusal is not proven to be about the name.
- `FORGE/tools/news-sweep/sweep.py` names itself "Prome/1.0" inside a Mozilla-form string and takes its feeds from configuration; its feeds were not in this test.
- OSPREY's `strike_feed.py`, DEWEY's `site_passive_check.py` and LABOR's `fetch_primary.py` carry the browser string but no fixed source address; nothing to test.
- Added 2026-11-23 14:07 ET, a sourced receipt: this test scanned script files only. AEOLUS reported that written pull recipes carry the same browser string; 21 desk markdown files do, with about 20 source addresses not tested here (DOCKET row dated 2026-11-27). AEOLUS disclosed two browser-named requests at 13:56 ET before it had seen the ruling (kunc.org answered; pslc.org refused and it stopped).
