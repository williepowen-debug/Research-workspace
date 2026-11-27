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

## Slow retry of the price library, ordered by Will 2026-11-23 14:14 ET (appended 2026-11-23 14:26 ET)

Same plain session named `research-bot/1.0`, one call every 90 seconds, two rounds, stamps from `date`:

| Time ET | Call | Result |
|---|---|---|
| 14:14:33 | history, 5 days | Too Many Requests |
| 14:16:03 | company info | Too Many Requests |
| 14:17:33 | option expiries | Too Many Requests |
| 14:19:03 | option chain | Too Many Requests |
| 14:20:34 | history, 5 days | OK (723.71) |
| 14:22:04 | company info | failed (empty answer) |
| 14:23:34 | option expiries | Too Many Requests |
| 14:25:04 | option chain | Too Many Requests |

**Established:** at one call per 90 seconds, 7 of 8 failed, over 11 minutes. Company info and options failed every time in both runs (0 of 6). Price history worked 1 time in 3. The fleet tool, which uses the Chrome-imitating session, pulled prices from this same laptop at 12:04 and 13:00 ET today.
**Inferred, not proven:** this is a refusal of the honest client on Yahoo's cookie-based calls, reported as a rate limit. A real rate limit would not persist at this pace, and the browser-named tool was not limited the same day. No side-by-side browser request was sent, by the rule.
**Consequence:** the price tool cannot be switched to the honest name and keep working. It stays unswitched and goes to Will on 12/07 with a replacement proposal.

## Addendum 2026-11-25 (PROME prome-77, 2026-11-25 12:52 ET): sources the 11/23 scan missed

An outside commit review (read at origin/master 1c7f415407; Will gave PROME the file at 12:50 ET 11/25) found five live scripts at four desks that still send a browser string and were not in this test: the scan matched some string forms and not others. PROME verified each at the file, then ran each untested source ONCE with `research-bot/1.0` from the laptop, 12:50 to 12:52 ET 11/25 (curl; the PJM page with the site's own redirect followed).

| Source | Desk and script | Result under the honest name |
|---|---|---|
| emergencyprocedures.pjm.com | WATT `power_watch.py` | works: HTTP 200 after the site's redirect to `/ep/pages/dashboard.jsf`, 120,221 B |
| www.eia.gov wholesale xlsx (`ice_electric-2026.xlsx`) | WATT `power_watch.py` | works: HTTP 200, a valid xlsx |
| www.westmetall.com | MIDAS `metals_watch.py` | works: HTTP 200, 32,252 B |
| www.cftc.gov `deafut.txt` | MIDAS `cot_gold.py`, `cot_metals.py` | works: HTTP 200 |
| www.federalreserve.gov FOMC calendar | BOND `monitors/rates_context.py` | works: HTTP 200 |
| www.newyorkfed.org ACM term-premium file | BOND `monitors/rates_context.py` | works: HTTP 200, 10,177,024 B |
| news.google.com RSS search | CYPHER `boot.py` leg 10 | works: HTTP 200, valid RSS |

BOND `monitors/dm_cross_section.py` uses ECB, Bank of England and Japan MoF, which are in the table above from 11/23; not re-run. Packets sent 11/25 to WATT, MIDAS, BOND and CYPHER (`AGENTS/<desk>/inbox/2026-11-25_from-PROME_WQ-735-honest-client-name.md`). Limits: one request each; no desk parser was exercised; the count of script files still carrying "Mozilla/5.0" was 127 at this check, most of them research and archive scripts that no longer run (not classified one by one). The second pass over written recipes is D:L1239.

## Addendum 2026-11-26 (PROME prome-80, 2026-11-26 22:27 ET): written pull recipes, the second pass (D:L1239)

The 11/23 test scanned scripts only. Written recipes carry the same browser string (AEOLUS's packet of 11/23). Census 22:25 ET 11/26: `grep -rIn --include='*.md' Mozilla AGENTS FORGE`, archives, inboxes, outboxes and processed folders excluded, gives 78 lines in 36 files. PROME sorted them by reading the lines: standing recipes a desk re-runs (19 lines in 11 files: AEOLUS 15 in 7, and one each at OZK, TERRY, BRENT and ORACLE), notes that mention the string without sending it (AEOLUS `SCRATCH.md`, RED and VIOLET `MAINTENANCE.md`, CYPHER `DATA_ROUTES.md`, CATO `TASK_INDEX.md`, CORAL `STATUS_DETAIL.md`, one AEOLUS 403 note), and dated research records that quote what a past session ran (DEWEY, WALTER, HAWK, YURI, HOMER, DAEDALUS, CYPHER, CATO, BRENT, HANS, CORAL; left as written, not tested). The sorting is PROME's judgment and was not read by anyone else.

Each recipe source not already in the tables above was requested ONCE under `research-bot/1.0` from the laptop, 22:25:30 to 22:26:27 ET 11/26 (curl, redirects followed, 30 s limit; raw log `probe_2026-11-26_recipes.tsv`).

| Source | Desk and recipe | Result under the honest name |
|---|---|---|
| www.contargo.net | AEOLUS `water/SOURCES.md` | works: HTTP 200, 72,956 B |
| www.fastenergy.de | AEOLUS `water/SOURCES.md` | works: HTTP 200, 117,174 B |
| pancanal.com advisory index | AEOLUS `water/SOURCES.md`, `water/PANAMA_SERIES.md` | works: HTTP 200, 778,464 B |
| volcano.si.edu weekly RSS | AEOLUS `seismic/SOURCES.md` | works: HTTP 200, 31,540 B, XML |
| www.usda.gov WASDE page | AEOLUS C2 instrument file | works: HTTP 200, 159,363 B |
| www.sagis.org.za dates PDF | AEOLUS C2 instrument file | works: HTTP 200, a PDF, 359,455 B |
| bepi.mpob.gov.my | AEOLUS C2 instrument file | works: HTTP 200, 188,208 B |
| www.fao.org food price index CSV | AEOLUS C2 instrument file | works: HTTP 200, a CSV, 48,217 B |
| www.bsee.gov `rss.xml` | AEOLUS `hurricane/SOURCES.md` | works: HTTP 200, RSS, 35,425 B |
| www.artemis.bm cat-bond yield page | AEOLUS `hurricane/SOURCES.md` | REFUSED: HTTP 403, a bot challenge page; AEOLUS had the same on 11/23 under curl's default name |

Not requested again, host already passed above: home.treasury.gov and www.eia.gov (AEOLUS), securitiesfilings.fdicconnect.fdic.gov (OZK), fred.stlouisfed.org (TERRY), services9.arcgis.com (BRENT). NOT TESTED: Polymarket's price-history call (ORACLE `SCRATCH.md`); it needs a live token identifier from ORACLE's pins, so ORACLE is asked to run it once at its next session.

Packets sent 11/26 to AEOLUS, OZK, TERRY, BRENT and ORACLE (`AGENTS/<desk>/inbox/2026-11-26_from-PROME_WQ-735-written-recipes.md`); each switches at its next ordinary session.

Additions to the 12/07 list from this pass and since 11/25: www.artemis.bm (AEOLUS; loses the mid-cycle cat-bond spread it uses to search for AEO-03, not that forecast's resolving instrument; replacement asked of AEOLUS, none tested) · CourtListener's docket web page (DEWEY, 11/26: HTTP 403 to the honest name; loses free full-text docket descriptions; replacement: the CourtListener API with a token, which is WILL_QUEUE row 687, Will's hands). REMOVED as a refusal: GIE's storage API (HANS 11/26: it answers the honest name when the fleet's existing key is sent; BRENT asked to confirm for its probe).

Limits: one request per source; no desk parser was exercised; same-host files other than the one requested are assumed, not shown, to behave alike; no browser-name request was sent for comparison.
