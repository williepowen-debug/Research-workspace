# Browser-identity sample, 2026-11-20

**Asked by Will** in PROME's chat 2026-11-20 12:42 ET ("yes do the sample"), after WQ-723 A. Run by PROME prome-77, 12:43:26 to 12:45:07 ET (`date`), from the laptop. Written 2026-11-20 12:45 ET. DOCKET row dated 2026-11-24. Data: `probe.tsv` beside this file.

## What was done

63 script files carry a browser ("Mozilla") identity string (`grep -rIl Mozilla` over `AGENTS/*/scripts`, `AGENTS/*/tools`, `AGENTS/*/sub_agents`, `FORGE/tools`, `scripts`, `PROME/tools`; tests and archives excluded). The web addresses written in those files name 56 hosts; two are document-format namespaces, not data sources, and were dropped. Each remaining host got ONE request under the client string `research-bot/1.0`, at the first literal address found for it in a script, 20-second limit, no retry, no second identity. No script was changed.

## Result

| Class | Hosts | Meaning |
|---|---:|---|
| ANSWERED | 28 | HTTP 200 with a real body and no block marker under the honest string |
| REFUSED | 6 | HTTP 403, or a block marker in the body |
| INCONCLUSIVE | 16 | 400, 404, 500 or no answer: the address in the script is a base or needs parameters or a key, so the answer says nothing about the identity string |
| NOT-SAMPLED | 4 | SEC (requires its own declared client string) and Cboe (already refusing this laptop today) |

**ANSWERED:** data.texas.gov (LABOR), data.wa.gov (DEWEY), dos.fl.gov (MARCO), feeds.bbci.co.uk (HAWK), gasprices.aaa.com (CARL), oag.ca.gov (DEWEY), securitiesfilings.fdicconnect.fdic.gov (OZK,REGINALD), services.nvd.nist.gov (DEWEY), services9.arcgis.com (FALCON), stats.bis.org (SAM), transtats.bts.gov (MARCO), www.aljazeera.com (HAWK), www.atg.wa.gov (DEWEY), www.bankofengland.co.uk (HANS), www.chinamoney.com.cn (ZHAO), www.cisa.gov (DEWEY), www.customs.go.jp (SAM), www.dol.gov (MARCO), www.eia.gov (BRENT), www.gpif.go.jp (SAM), www.ishares.com (DEWEY), www.newyorkfed.org (DEWEY), www.pbc.gov.cn (ZHAO), www.ssga.com (DEWEY,VULCAN), www.totan.com (SAM), www.trendforce.com (VULCAN), www.trepp.com (CREED), www.twc.texas.gov (LABOR).

**REFUSED:** agsi.gie.eu (BRENT,DEWEY,HANS), alsi.gie.eu (DEWEY), cdn.finra.org (REGINALD), iq.usembassy.gov (FALCON), rigcount.bakerhughes.com (BRENT), www.investing.com (VIOLET).

**INCONCLUSIVE:** api.hkma.gov.hk (ZHAO), api.nasdaq.com (REGINALD), api.stlouisfed.org (BRENT,CARL), chartexchange.com (REGINALD), data-api.ecb.europa.eu (HANS), feeds.reuters.com (HAWK), fred.stlouisfed.org (BRENT,ZHAO), home.treasury.gov (SAM), markets.newyorkfed.org (LIQUID), news.google.com (HAWK,WALTER), pddata.dtcc.com (LIQUID), trends.google.com (MARCO), web.archive.org (MARCO), www.banxico.org.mx (MARCO), www.cftc.gov (BRENT,LIQUID,SAM,VIOLET), www.mof.go.jp (SAM).

**NOT-SAMPLED:** cdn.cboe.com (HENRY,RED,VIOLET), efts.sec.gov (DEWEY), www.cboe.com (FORGE,VIOLET), www.sec.gov (DEWEY,REGINALD).

## Limits (each could change the reading)

- One request per host, at one address, at one time of day, from one machine. A host that answers its front page may refuse a data file, and the reverse.
- The scripts were NOT run under either string. Nothing here shows that a script still parses what an honest request returns.
- No browser-string request was sent for comparison, so REFUSED is not proven to be caused by the identity string. agsi.gie.eu and alsi.gie.eu answered 200 with a 120-byte "access denied" body, which is as likely a missing API key as a client-string rule.
- INCONCLUSIVE is unknown, not safe. api.nasdaq.com and home.treasury.gov gave no answer inside 20 seconds, which some sites do to clients they do not like.
- Hosts were taken from literal addresses in the files; an address built at run time is not in the list.
- A count of hosts is not a count of scripts or of observations that matter: one refused host can carry a desk's key series.
