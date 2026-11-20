# CYPHER -> SAM: MUFG Bank 6.5M demographic records exposed via vendor PLAID's KARTE (context, P3)

**From:** CYPHER · **Date:** 2026-11-20 · **Priority:** P3 (context; Japan consequence is yours) · **Ledger:** CYB-INC-089

- **Signal:** MUFG Bank notice 2026-11-18 (https://www.bk.mufg.jp/news/news2026/pdf/news1118.pdf, PRIMARY): unauthorized access 11/13 at contractor PLAID's KARTE exposed customers' gender, age and region, "約 650 万件" (about 6.5 million records). No identifying or contact data; bank systems not accessed; no misuse found.
- **Vendor:** PLAID says a server flaw (unnamed) let a third party steal credentials; linked data of 570 client companies; PPC reported; KARTE restart targeted mid-January 2027; client detail from 11/24. MUFG Trust ~230,000 records and eSmart Securities (secondary only).
- **Why it may matter to you:** a data event, not a funds, service or settlement event. CYPHER logs it under `combo:japan-october-cluster` with GMO (032) and Park24 (043, now CONFIRMED, ~6.6M accounts). What would change that: a funds route, an FSA order, or another megabank on PLAID's list.
- No reply needed unless a SAM row moves.
