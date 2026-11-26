# D:L1290 Part B — 11/25 full-day DTCC read: CoreWeave, SoftBank, Oracle, Alphabet, SpaceX CDS

**LIQUID, 2026-11-25, read 19:00–19:10 ET** (laptop, Claude Code / Opus 5.5). Run early on Will's 18:46 ET word ("should be able to move forward now").

## Source and method

- **Data:** DTCC PPD SEC-regime intraday credit slices 1–631 for 2026-11-25 (`pddata.dtcc.com/ppd/api/report/intraday/sec/SEC_SLICE_CREDITS_2026_11_25_N.zip`), 2,102 rows, latest report time 23:44Z (18:44 ET), latest execution 23:33Z. Slice 632 returned 404 at 19:05 ET. Cumulative full-day file: 404 at 18:46 ET (posts about 20:15 ET). The slices cover the trading day; the cumulative file is a confirmation diff, recorded below when it posts.
- **Conversion:** `scripts/crwv_cds_grade.py` `conv_spread` (flat hazard, R 40%, discount 4% USD, **1% for the JPY SoftBank contract**). Clean = UFRO read as clean upfront; dirty = cash net of accrued (headline basis from 11/25, KB-LIQ-163). TERRY's gate uses **clean**.
- **Reader:** `read_slices.py` here; output `read_output.txt`; evidence rows `rows_5names_2026-11-25.csv` (46 rows: every row for the five names plus every cancel row naming one of their trade IDs). Prior days: `crwv_1120_1124_output.txt` (fixed script on the 11/20, 11/23, 11/24 cumulative files; the 11/24 file was copied from PROME's session cache, the others downloaded).

### Two reader blind spots found and fixed (KB-LIQ-166)

1. **Cancel rows often carry no company name.** 90 of 114 cancel rows (CANC/ERRO/EROR/TERM) in the 11/25 slices had a blank name. A filter by name before matching cancels misses them. This is how the 07:56 ET CoreWeave 5Y odd lot (cancelled EROR, slice 306) read as live on a name filter tonight; the morning correction COR-20261125-22 stands.
2. **Some rows carry the name only in `UPI Underlier Name`**, not `Underlying Asset Name` (the SoftBank 09:32 ET trade; five more Oracle trades).

`crwv_cds_grade.py` had blind spot 1 (and 2 for any CoreWeave row so written): on the 11/25 data the old version lists 6 live CoreWeave prints, including the cancelled 1,363 odd lot; the fixed version lists 5. Fixed in place 2026-11-25. `dtcc_cds_probe.py` (repo `scripts/`, not LIQUID's) is not checked; carry with its known repair.

## CoreWeave (500 bp coupon)

| Execution (ET) | Maturity | Notional | Clean / dirty bp | Status |
|---|---|---|---|---|
| 11/25 07:56 | Dec-2031 (5Y) | 95,000 | 1,363 / 1,410 | **CANCELLED** (EROR, slice 306) |
| 11/25 08:20 | Dec-2030 (4Y) | 2,000,000 | **1,379 / 1,429** | live (corrected, same terms) |
| 11/25 12:22 | Dec-2030 (4Y) | 1,000,000 | **1,366 / 1,415** | live, non-standard term flag |
| 11/25 12:29 | Dec-2028 (2Y) | 3,000,000 | 1,382 / 1,450 | **CANCELLED** (EROR, slice 587) |

- **No valid 5Y CoreWeave trade on 11/25 at DTCC: SEARCH-NOT-FOUND.** Last valid 5Y: **1,314 clean / 1,359 dirty [11/24, 15:12 ET, $3M; also 10:23 ET, $2M, non-standard flag]**.
- **Same-contract change, Dec-2030 (4Y), clean:** 11/20 1,116–1,145 (1,240 at 15:32 ET), 11/23 1,054–1,093, 11/24 1,214–1,239, **11/25 1,366–1,379**: about **+130 bp on 11/25** against the 11/24 range.
- **Curve shape:** on 11/24 the 5Y (1,314) sat about 75 bp over the 4Y (1,239), normal upward slope. My 18:16 ET chat remark that 4Y over 5Y showed near-term worry compared 11/25's 4Y with 11/24's 5Y; **withdrawn**, it was a two-day comparison, not a curve.
- **5Y on 11/25, INFERRED:** if the 11/24 4Y–5Y gap held, about 1,440–1,455 clean. Two 4Y trades, one non-standard; an inference, not a reading.
- **WALTER cards 035/036 ask (Bloomberg-relayed "five-year protection rose by the most ever", no level):** not confirmable at DTCC; no valid 11/25 5Y trade disseminated. The same-contract 4Y move (+130 bp) and the 11/24 5Y move (11/23 1,076–1,123 to 11/24 1,267–1,314 clean, about +190 bp) are consistent with a record move on either day. Bloomberg's level likely rests on dealer quotes, not these trades (INFERRED).

### For TERRY's card (GATE-TERRY-CRWV-AIFIN-01; terms are TERRY's)

- Latest LIQUID CoreWeave 5Y read: **1,314 clean [11/24]**, above 1,200; far from the 1,000 void.
- Freshness count: sessions 11/24 and 11/25 (11/26 Thanksgiving, no session). For an entry on Fri 11/27 the 11/24 read is 2 sessions back; for an entry on Mon 11/30 or later it is 3 or more unless a 11/27 5Y trade prints. Whether 11/27 (early close) counts as a session for the card is TERRY's reading.
- The 4Y at 1,366–1,379 clean on 11/25 and the inferred 5Y near 1,440–1,455 point the same way: no sign of a fall toward 1,000.
- 039 context (WALTER card, CoreWeave 10-Q, Sep 30, not re-read at SEC by LIQUID): principal due $2.433B rest of 2026 and $10.974B in 2027 of $47.505B; $4.122B cash, $5.7B undrawn. Refinancing access is the near-term question; this read does not price it.

## SoftBank (JPY, 100 bp coupon, 1% discount)

- **11/25 09:32 ET, Jun-2030 (3.5Y), ¥796M+ capped: 548 / 555**, matches the morning packet. One other row (Dec-2028, ¥100M, 23:14 ET 11/24) carries no upfront, so no level.
- **No 5Y SoftBank trade on 11/25: SEARCH-NOT-FOUND.** Last 5Y 466 / 471 [11/24 Tokyo]. 5Y INFERRED 560–600 stands on that one 3.5Y trade. Most SoftBank swap trading is outside this US-nexus report.

## Oracle (100 bp coupon)

- **5Y Dec-2031: 9 live trades, 362–372 clean / 367–377 dirty; afternoon 362–364, last 364 / 369 at 13:32 ET.** High 372 / 377 at 10:07 ET; settled about 8 bp under it. One 362 trade at 12:40 ET cancelled (EROR, slice 498).
- Curve: Jun-2029 271 / 279; Jun-2030 300 / 306 (two trades); Dec-2030 347 / 353; Jun-2031 367 / 372.
- Against 11/24 disseminated quotes of 365–370: about flat on the day after the morning high.

## Alphabet and SpaceX

- **Alphabet:** the one 5Y trade (108 / 112, 14:49 ET, capped) was **CANCELLED** (EROR, slice 620). One Jun-2027 trade, too short to convert. **No valid 11/25 5Y**; last 96–97 [11/24].
- **SpaceX:** 5Y Dec-2031 **293 / 298** (11:30 ET, capped, non-standard flag); Dec-2027 128 / 145. Against 286–295 dirty [11/24]: flat to +3 bp dirty.

## Limits

- DTCC PPD is the US-reportable sample, not the whole market; capped notionals hide size.
- Conversion approximates the ISDA model (script header: about 7–8 bp low vs ISDA on a Treasury-proxy curve at September levels).
- 4Y-to-5Y inference uses the 11/24 gap; curves can twist on a day like this.
- No investment implication from LIQUID; the card and its terms are TERRY's.

## Cumulative-file confirmation

(pending; appended when the 11/25 cumulative file posts)
