# Recurring blocked data sources, ranked by consequence (from existing records only)

**Written:** 2026-11-22, PROME prome-77, on Will's word of 04:02 ET (WQ-727 item 7: idea 7 HELD; rank from existing records; no new logging programme or study; licensed feeds or official APIs only; no unblocking services, WQ-708; any purchase is Will's).
**Method and limit:** one Sonnet reader swept desk STATUS files, PROME's processed inbox from October and the daily notes, 2026-10-01 to 2026-11-21, counting distinct dates. ⚠️ PROME checked ONE row at the files (MIDAS 10/12, confirmed); the other counts and identifiers are the reader's, INFERRED until an owner confirms. Not searched: September packets, desk research folders, sources with no refusal word in the record.

| Rank | Source | Desks | Dated instances | What was weakened | Substitute used | Official or licensed route named in the records |
|---|---|---|---|---|---|---|
| 1 | cmegroup.com (address block since 10/28) | BRENT, MIDAS, HENRY, TERRY, VULCAN, FERT, DAEDALUS | about 12 | Every official CME settlement: BRENT's positioning grades and Brent window, MIDAS's gold settles, HENRY's rate-futures pricing | Vendor bars, labelled "vendor proxy, not settlement" | A licensed feed, Will's broker, or asking CME (`memory/auto/reference_cme_site_blocks_this_box_ip.md`) |
| 2 | cboe.com (intermittent) | HENRY, VIOLET, WALTER, TERRY | 3 (11/19 to 11/21) | No second source for the 11/20 red-line close; the 11/20 dealer map NOT PUBLISHED; the 11/20 VIX print provisional | Vendor index bar, FRED's VIX series, vendor option chain | None named |
| 3 | mba.org | HOMER, CARL | 3 | HOM-02 graded MISSED on a mirror; the housing thesis grade's FHA leg; CARL's FHA row | A blog quoting MBA verbatim, labelled secondary | None named |
| 4 | bls.gov web pages (the BLS API works) | CARL, VIOLET, HENRY, RED, SAM, BOND, WALTER | about 11 | Release pages unread; grades made on the API and FRED | BLS public API, FRED | The BLS API, already in use |
| 5 | Court dockets (CourtListener, Justia; PACER is paid) | AEOLUS, BROCK, CORAL, DEWEY, WAL, HAWK | 8 | AEOLUS's Colorado motion trigger unread; the Cable One order inferred; CORAL's Florida hearings | Press and feeds | A CourtListener token (WILL_QUEUE row 687, laptop) or PACER (ask-first) |
| 6 | PJM price feed (key refused) | WATT | 1 outage since 11/16 | WATT's power-price trigger reads UNKNOWN | None | Replace the key (WILL_QUEUE row 695) |
| 7 | mil.ru, mid.ru, tass.ru | YURI, HAWK | 5 and 1 | One YURI call's implementation leg skipped; one call may be answerable only there | Other primaries | None |
| 8 | Baker Hughes rig count | BRENT | 5 Fridays | The weekly rig-count grade | Two same-day secondaries | None |
| 9 | Japan Tobacco's sites | TERRY, YURI | 3 | The Russia-exposure input to TERRY's read | Tokyo exchange filings | The exchange's free disclosure system |
| 10 | ukmto.org | FALCON | 4 | Three incident notices not authenticated | Three outlets | None |

Lower: sec.gov document pages (3; the declared client string is the fix), opec.org (2), iea.org (2). Not recurring: Trepp (the "gated" belief was a retrieval error), P&I club circulars (one cluster, already in `PROME/registry/UNREACHABLE_MEASUREMENTS.tsv`).

**PROME's read.** Two gaps touch graded items every week and have no free official substitute: CME settlements and Cboe. Three are already fixable with what exists and cost nothing: the PJM key (row 695), the CourtListener token (row 687) and the BLS API (in use). Nothing is proposed for purchase here.

**Two identity changes after a refusal are in the record.** MIDAS, 2026-10-12, fetched a CME warehouse report with a browser-like client after a plain request got 403 (confirmed by PROME at `AGENTS/MIDAS/sources/2026-10-12_pgm-followup/cme_retry_access.json`); this was before the blocked-sites rule. REGINALD, 2026-11-16, did the same at regulations.gov and disclosed it as a breach the next day (reader's finding, not re-checked).
