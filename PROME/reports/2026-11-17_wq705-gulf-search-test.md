# WQ-705 A: the Gulf news search, tested once (2026-11-17)

**By:** PROME prome-19 · **Authority:** Will 2026-11-17 09:30 ET, verbatim "703 yes, 705 yes" (WILL_QUEUE row 705, RULED A) · **Run:** 09:33 to 09:35 ET, read-only, Google News RSS with the plain client string `research-intake-comparison-test`; nothing in `/home/willi/Research-Intake` was pulled, checked out or written. Raw responses: the session scratchpad only (not durable).

## Result under the ruling

The changed form the ruling named (last 24 hours, Bahrain added) did NOT return current Gulf headlines. **Under A, nothing changes in the collector, and nothing was changed.**

## What each form returned (first 15 items are what the collector keeps)

| Form | Retrieved | First 15 under 24 hours | First 15 over 72 hours | Bahrain in any title |
|---|---:|---:|---:|---:|
| The collector's search as it is (18 terms joined by OR) | 32 | 0 | 15 (14 over 30 days) | 0 |
| The same with `OR Bahrain when:1d` (the approved changed form) | 32 | 0 | 15 | 0 |
| The same with `when:1d` only | 32 | 0 | 15 | 0 |
| The same in brackets, `(...) when:1d` | 32 | 0 | 15 | 0 |
| The same in brackets with Bahrain, `(... OR Bahrain) when:1d` | 32 | 0 | 15 | 0 |
| A short search, `(Hormuz OR Houthi OR IRGC OR Bahrain OR "Bab el-Mandeb" OR Kharg OR Fujairah) when:1d` | 100 | 15 | 0 | 48 |
| The short search with no recency limit | 100 | 13 | 1 | 47 |

## Reading

- **Observed:** the 18-term search returns 32 items, none newer than about four days and most months old, with or without a recency limit. A seven-term search returns 100 items, nearly all from the last day. The recency limit is not what separates them; the length of the search is.
- **Inferred, not established:** Google's search degrades on the long OR chain. The threshold (how many terms is too many) was not measured.
- **Not established:** that this is what happened on 11/13. The 11/13 response was not stored. WALTER's packet suspected the 15-item cut and the missing recency limit; today's test points at the search's length instead.
- **Not tested:** every other search in `scripts/newsweep_config.py`. Several are as long as this one (the China search has 18 terms).
- The last four forms go one step past the two the ruling named: read-only probes to find why the approved form failed (class C11). No collector change follows from them without Will's word.

## Found in passing, UNVERIFIED

The short search's first items at 09:35 ET were titles about a new Iranian strike on US targets in Bahrain and a tanker struck in Hormuz (CNBC, Reuters, AP, Al-Monitor, Al Jazeera; 1 to 10 hours old). Titles only; PROME read no article. FALCON was woken to establish them (ORCH_LOG, 11/17, class C8).

## Every search, one read-only pass (2026-11-17 10:14 to 10:16 ET)

Run by PROME as preparation while WQ-706 was open; read-only, one request per search with the plain client string, nothing written in the collection repository. Raw results: `PROME/reports/2026-11-17_wq706-search-freshness.json`. The yardstick is PROME's own: of the first 15 items (what the collector keeps), how many are under 48 hours old.

**Of 61 searches: 15 STALE (none of the first 15 under 48 hours), 2 EMPTY, 20 THIN (1 to 3), 24 CURRENT (4 or more).** Of the 15 stale, 15 carry no recency limit; of the 20 thin, 12 carry none.

- **Observed:** a search with no recency limit comes back ranked by relevance, and old stories fill the 15 places (9 to 15 of 15 over 30 days old on most of them). A search that carries the collector's `when:` limit has none over 30 days. So the recency limit works on ordinary searches; it failed only on the 18-term Gulf search (and the 18-term China search returns 7 items, all months old).
- **Two faults, then:** no recency limit on 46 of 61 searches, and two searches too long for Google to serve properly (gulf-theater, china-asia).
- **Limits:** one pass at one time of day. A narrow search (a single quoted phrase, a litigation name) can truthfully have nothing new in 48 hours, so STALE on those is weaker evidence than on a broad theme. The collector's direct publisher feeds are a separate leg and were not tested; the lane is not blind overall. How long each search has been stale is not known.

| Search | Desks | Terms | Recency limit | Retrieved | First 15 under 48 h | First 15 over 30 days | Class |
|---|---|---:|---|---:|---:|---:|---|
| gulf-theater | FALCON, BRENT | 18 | no | 32 | 0 | 14 | STALE |
| china-asia | ZHAO | 18 | no | 7 | 0 | 7 | STALE |
| vol-regime | VIOLET | 10 | no | 41 | 0 | 12 | STALE |
| flg-rent-freeze-litigation | FLG | 6 | no | 54 | 0 | 15 | STALE |
| shade-E2 | SHADE | 6 | no | 39 | 0 | 15 | STALE |
| aramco-osp | BRENT | 4 | no | 5 | 0 | 5 | STALE |
| pe-insurance | BROCK, SHADE | 4 | no | 23 | 0 | 14 | STALE |
| shade-D2 | SHADE | 1 | no | 31 | 0 | 11 | STALE |
| shade-D3 | SHADE | 1 | no | 22 | 0 | 15 | STALE |
| shade-D4 | SHADE | 1 | no | 43 | 0 | 14 | STALE |
| shade-D6 | SHADE | 1 | no | 10 | 0 | 9 | STALE |
| shade-E1 | SHADE | 1 | no | 43 | 0 | 15 | STALE |
| gpu-obsolescence-2 | VULCAN, BROCK | 1 | no | 21 | 0 | 13 | STALE |
| gpu-obsolescence-3 | VULCAN, BROCK | 1 | no | 23 | 0 | 14 | STALE |
| gpu-obsolescence-4 | VULCAN, BROCK | 1 | no | 28 | 0 | 15 | STALE |
| ai-training-pause | VULCAN | 5 | yes | 0 | 0 | 0 | EMPTY |
| eu-sovereign-spreads | HANS | 3 | yes | 0 | 0 | 0 | EMPTY |
| ai-financing | LIQUID, BROCK, VULCAN | 15 | yes | 24 | 1 | 0 | THIN |
| housing | HOMER, CARL | 14 | no | 31 | 1 | 11 | THIN |
| bank-vendor-incidents-core | CYPHER | 13 | yes | 4 | 1 | 0 | THIN |
| fertilizer | FERT | 11 | yes | 5 | 1 | 0 | THIN |
| cruise-fundamentals | CRUISE | 9 | yes | 11 | 2 | 0 | THIN |
| pgm-producers | MIDAS | 9 | no | 41 | 3 | 11 | THIN |
| russia-fuel-export-ban | HENRY, OSPREY, BRENT | 7 | yes | 8 | 3 | 0 | THIN |
| bank-vendor-incidents-msp | CYPHER | 7 | yes | 30 | 3 | 0 | THIN |
| florida | CORAL, HOMER | 6 | no | 50 | 2 | 5 | THIN |
| russia-ukraine-energy | OSPREY, BRENT | 5 | no | 55 | 1 | 8 | THIN |
| diesel-export-policy | BRENT, TERRY, HENRY | 4 | no | 89 | 3 | 0 | THIN |
| credit-spreads | LIQUID | 4 | no | 42 | 1 | 12 | THIN |
| funding-stress | LIQUID | 4 | no | 30 | 1 | 11 | THIN |
| bank-stress | REGINALD, LIQUID | 4 | no | 40 | 1 | 9 | THIN |
| ecb-rate-decision | HANS | 4 | yes | 20 | 3 | 0 | THIN |
| consumer-stress | CARL | 3 | no | 22 | 1 | 12 | THIN |
| shade-D1 | SHADE | 1 | no | 35 | 2 | 9 | THIN |
| shade-D5 | SHADE | 1 | no | 7 | 1 | 6 | THIN |
| gpu-obsolescence-1 | VULCAN, BROCK | 1 | no | 34 | 1 | 11 | THIN |
| nano-banc | CREED, REGINALD, WAL, DEWEY | 1 | yes | 8 | 2 | 0 | THIN |
| cruise-operators | CRUISE | 15 | no | 100 | 14 | 0 | CURRENT |
| megacap-leadership-event | HENRY, VULCAN | 15 | yes | 31 | 4 | 0 | CURRENT |
| homebuilder-earnings | HOMER | 12 | yes | 17 | 5 | 0 | CURRENT |
| war-risk-insurance | FALCON, HAWK | 10 | yes | 14 | 5 | 0 | CURRENT |
| power-grid | WATT, VULCAN | 6 | no | 100 | 10 | 0 | CURRENT |
| climate-macro | AEOLUS | 6 | no | 100 | 11 | 1 | CURRENT |
| bdc-names | BROCK | 5 | no | 57 | 7 | 3 | CURRENT |
| japan-boj | SAM | 5 | no | 100 | 15 | 0 | CURRENT |
| memory-cycle | VULCAN | 5 | no | 100 | 9 | 1 | CURRENT |
| metals | MIDAS | 5 | no | 68 | 4 | 0 | CURRENT |
| memory-pricing | VULCAN | 5 | no | 96 | 8 | 3 | CURRENT |
| treasury-moves | BOND, HENRY | 4 | no | 100 | 15 | 0 | CURRENT |
| private-credit | BROCK | 4 | no | 100 | 13 | 0 | CURRENT |
| oil-energy | HENRY, BRENT | 4 | no | 100 | 14 | 0 | CURRENT |
| gas-supply | HENRY, BRENT | 4 | no | 100 | 13 | 0 | CURRENT |
| labor-layoffs | LABOR | 4 | no | 100 | 15 | 0 | CURRENT |
| labor-nfp | LABOR | 4 | no | 58 | 4 | 0 | CURRENT |
| position-banks | REGINALD | 4 | no | 43 | 4 | 1 | CURRENT |
| ai-capex | VULCAN, HENRY | 4 | no | 75 | 4 | 5 | CURRENT |
| saudi-redsea | FALCON, BRENT | 4 | no | 78 | 6 | 1 | CURRENT |
| cre-stress | REGINALD | 3 | no | 63 | 9 | 2 | CURRENT |
| position-pe | BROCK | 3 | no | 100 | 13 | 0 | CURRENT |
| ai-dc-force-majeure | VULCAN, LIQUID | 3 | yes | 6 | 5 | 0 | CURRENT |
| ttf-storage-gilts | HANS | 3 | yes | 27 | 7 | 0 | CURRENT |
