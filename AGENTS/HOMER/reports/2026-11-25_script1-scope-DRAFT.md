# Script 1 — public-series fetcher: SCOPE DRAFT for Will (nothing built)

**Written 2026-11-25 17:31 ET.** Plan of record item 2 (Will 17:19 ET): scope approved before any build.

**What it does:** one command, run by hand, fetches four public files, saves what HOMER uses with the fetch time and SHA-256, and prints what is new since the last save. It grades nothing, writes no ledger, STATUS or reading cell, and sends nothing.

| Feed | Address check 2026-11-25 17:29 to 17:30 ET | Saved | Size kept per refresh |
|---|---|---|---|
| Freddie mortgage rate (PMMS) | 200, 98,473 B, last row 11/25/2026 = 7.21 | last 60 weekly rows | ~2 KB |
| Freddie home prices (FMHPI) | 200, 16,472,112 B, last month 2026-09 | national + the states and metros HOMER quotes, 60 months (first print and revisions compared) | ~100 KB |
| Treasury curve | 200, 18,416 B, newest row 11/25/2026 | current-year file | ~18 KB |
| Apartment List city rents | page 200; newest file named is 2026_10 (November not out) | roster-100 extract, as today; then the operator runs `rent_breadth.py` | ~68 KB |

**Must fail loudly:** non-200, wrong columns, fewer rows than last save, newest date older than last save, or a file that parses to nothing = nonzero exit, named feed, nothing saved for that feed, others still run. No retry with a different identity; a block stops that feed.

**Why these four:** each feeds a band, kill leg or prediction (PMMS: A2 and a band; FMHPI: HENRY trigger; Treasury: the 10Y-FRM spread; Apartment List: a band and HOM-06), and each has been read by hand every refresh. The shared `fetch.py` was one week behind Freddie's own file on PMMS when DAEDALUS compared them (2026-11-25 16:09 ET).

**Not included:** ICE, ATTOM, MBA, Fannie, NAR, Trepp and NAHB (not machine feeds, or blocked here). Those prints stay read in full.

**Test before use:** each feed with a truncated file, a renamed column and a stale copy; all three must fail. Then one live run checked against today's hand readings.

**Cost and stop rule:** one file, about 150 lines, no new rule, check, band or boot step. If it does not plainly save time over the December refreshes, delete it and stop.

**Expected benefit:** modest. It saves a few minutes per refresh and keeps dated first prints, so revisions are exact. It would not have caught this month's errors, which were reading errors.

**Decision for Will:** A build as scoped (recommended) · B leave out Apartment List · C do not build.
