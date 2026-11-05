# L920 leg 2 read 2, live day session, 2026-11-05 11:03 to 11:13 ET
Reader: one read-only counterexample reader under WQ-607 A. Candidate fetch.py at HEAD, sha256 cd98143c3a40dc17..., run from a byte-identical scratch copy with its own cache, so no repository write. Harness and raw pulls: l920/ beside this file (rounds.py, rounds.jsonl, an.py, fixtures.py, mock_sym.py, zb.py, prev.py). All prices are INTRADAY, vendor-delayed, from 11/5 between 11:05 and 11:12 ET.

**Verdict: ACCEPT-WITH-RESIDUE for the tolerance repair. One ❌ sits outside the repair and needs its own row.**

## ❌ Ranked findings
### 1. ❌ A bare root symbol serves a different instrument, silently, rc=0
- **Claim:** `fetch.py price CL` returns crude. FALSE. VERIFIED.
- **Artifact:** fetch.py price_fetch; INDEX_ALIASES has no futures roots; _BARE_DATED_RE only matches dated forms; _looks_like_future false for a bare root.
- **Command:** `fetch.py price CL` and NG, BZ, RB, ES, WTI, GOLD on the scratch copy; vendor metadata via yf.Ticker(s).history_metadata.
- **Observed:** CL = Colgate-Palmolive $100.96 +2.22% (intraday), NG = Novagold, BZ = Kanzhun, RB = ProShares ETF, ES = Eversource, WTI = W&T Offshore, GOLD = Gold.com. Each printed today's date, rc=0, no warning, no contract line. HO, GC and ZB error with rc=3 only because no such listing exists. Repo grep for these bare forms in commands: 0 hits (SEARCH-NOT-FOUND; pattern-limited, does not prove no desk types it).
- **Proposed change:** pre-existing, not caused by 2663082a0, so it does not reverse the tolerance repair. New DOCKET row. Smallest fix: refuse or warn when a registered futures root is passed bare, printing the working forms. Owner call: PROME.

## ⚠️ Residue
### 2. ⚠️ Every served row is about 10 minutes old and says only the date
- **Claim:** a `day` row is current. PARTLY. VERIFIED.
- **Artifact:** rounds.jsonl (ts minus regularMarketTime); _session_stamp prints the date only; README has no delay statement (grep "delay": 0 hits).
- **Command:** rounds.py 6 45; an.py. Clock check: curl date header matches `date -u` to the second.
- **Observed:** 204 pulls on live symbols, vendor timestamp age minimum 9.99, median 10.05, maximum 29.1 minutes (BZK27, thin). Clean stamp in every served case.
- **Proposed change:** state the delay in the README and the row note. Root rule #4 reads "live"; desks should not read a clean stamp as now.

### 3. ⚠️ The `day` branch has no wall-clock freshness check
- **Claim:** a frozen vendor feed would be caught. FALSE at the code; not seen live. VERIFIED by fixture.
- **Artifact:** futures_bar_session, fetch.py:1560-1580: no comparison of regularMarketTime against now.
- **Command:** fixtures.py with last trade 00:30 and 09:00 on the bar date.
- **Observed:** both return day, withhold False. Live the worst age was 29.1 minutes, so this stayed theoretical. A contract with a bar dated today and a morning last trade would print clean all afternoon.
- **Proposed change:** none required for L920. If row 2 is fixed, carry the age in the row and the case closes itself.

### 4. ⚠️ `price` is rounded to 2 decimals, in the JSON too
- **Claim:** a served price is the vendor's price. PARTLY. VERIFIED.
- **Artifact:** fetch.py:969-970.
- **Command:** rounds.jsonl raw quote against row price; prev.py.
- **Observed:** HOZ26 4.3359 prints $4.34; ZBZ26 108.71875 prints 108.72, which is not a tradable 32nd; 6JZ26 0.0063535 prints $0.01, with prev $0.01 while change_pct, computed on raw values, is right. A two-decimal HO leg moves a crack by up to about $0.21 a barrel (0.005 × 42). change_pct is unaffected.
- **Proposed change:** none for L920. Separate decision: keep raw price in JSON. Consumers parse this, so PROME decides. 5 rows off by >0.5 points in my recompute: all 6J, my recompute used the rounded prev; not a tool defect (see command output).

### 5. ⚠️ The metadata-symbol guard blanks the month and keeps the change
- **Claim:** EB2's "symbol guard remains in force" stops a mismatched row. PARTLY. Mock only.
- **Artifact:** fetch.py:1013-1014; session classification still runs.
- **Command:** mock_sym.py, a fake Ticker whose metadata says XXF27.NYM for BZF27.NYM.
- **Observed:** price and +4.67% served, clean date stamp, contract UNKNOWN with the mismatch named. Live: 0 of 216 rows had a symbol mismatch.
- **Proposed change:** withhold the change on a symbol mismatch. Low priority; no live case.

### 6. ⚠️ Rate-contract refusals are structural, roughly half the time at ZB and UB
- **Claim:** ZB is refused always (read 1: 6 of 6). FALSE; it depends on the price. VERIFIED.
- **Artifact:** fetch.py:1516; vendor chart price rounded to 4 decimals on ZB, 3 on UB.
- **Command:** zb.py (14 rounds), fixtures.py sweep, rounds.py.
- **Observed:** odd 32nds 16 of 16 refused (ZBZ26 4, ZB=F 6, UBZ26 6). Even 32nds 22 served, 4 refused: ZBZ26's 2 were a real move (108.6875 vs 108.7188); UBZ26's 2 not inspected, and UB's 3-decimal rounding can refuse some even 32nds too, so the odd/even rule is proven for ZB only. Fixture on 4-decimal rounding: ZB 16 of 32 served, ZN 16 of 64, ZF 48 of 128, ZT 112 of 256; adjacent tick admitted 0 of 480. Live, ZN and ZF served 6 of 6 because the vendor carried more decimals there, so the fixture overstates those two. Price is kept, change withheld, stamp ⚠unverif.
- **Wrong number possible:** no. The failure only withholds. No fleet config uses ZB, ZN or 6J (config.py, dashboard.py grep: 0 hits).
- **Proposed change:** none needed for L920. If ZB is ever wired in, compare at the vendor's rounding instead of widening the tolerance.

### 7. ⚠️ DOCKET's bare-symbol description is out of date
- **Claim:** "Bare symbols without .NYM still print ERROR exchangeTimezoneName." Not reproduced. SEARCH-NOT-FOUND in the day session.
- **Artifact:** fetch.py:928-943.
- **Command:** `fetch.py price` on BZF27, BZG27, BZH27, CLZ26, CLF27, HOZ26, RBZ26, NGZ26, HOX26, CLX26, BZZ26, GCZ26, ZBZ26, ESZ26.
- **Observed:** live energy contracts resolve through the .NYM retry and print "[resolved as ...]", rc=0. Non-NYMEX (GCZ26, ZBZ26, ESZ26) and expired (HOX26, CLX26) give ERROR, rc=3; the message suggests .NYM/.CME/.CBT and omits .CMX, the suffix gold needs. Wrong suffixes (GCZ26.CME, ZBZ26.NYM, CLZ26.CME and 4 more) all ERROR rc=3, 0 resolved to another contract. Expired BZZ26 serves its last price with date?⚠unverif, rc=0, change withheld. None gives a wrong number. Evening behaviour not tested; by code any other KeyError re-raises to an ERROR row.
- **Proposed change:** correct the DOCKET wording; add .CMX to the message. The risk is indirect: a desk sent away by the error may fall back to a continuous ticker (fetch.py:917-924 records that history).

## Measured, no change proposed
- **Day session (Q1), VERIFIED.** 6 rounds, 36 symbols, 216 pulls, 11:05:59 to 11:09:41 ET. 204 on live symbols: 170 served, 34 safely refused on a quote/chart gap, 0 errors, every row `day` or `unverified`. Expired BZZ26 6 of 6 unverified; expired HOX26 6 of 6 ERROR.
- **Served counts:** BZF27 6/6, BZ=F 6/6, CLZ26 5/6, CL=F 6/6, HOZ26 6/6, HO=F 5/6, NGZ26 6/6, NG=F 6/6, GCZ26 4/6, GC=F 5/6, ZBZ26 1/6, ZB=F 2/6, ESZ26 6/6, ES=F 2/6.
- **Served rows, VERIFIED.** Maximum quote/chart gap 5.46e-8 of price, under half the tolerance. No served row can differ by a tick.
- **Prior close, VERIFIED at vendor level.** The two series agree: 1-year Close[-2] equals 5-day Close[-2] on 6 of 6, dated 11/4. BZF27 94.62, CLZ26 88.12 and HOZ26 4.2055 tie BRENT's 11/4 marks (DTN, CNBC). Not an exchange settle: cmegroup.com not approached; BRENT notes a same-day DTN settle failed against CME once on 10/23, and HOZ26's mark is not labelled a settle.
- **The quote is not a separate quote.** yfinance 1.2.0 lastPrice is the last daily bar's Close (scrapers/quote.py:254), so the join compares two chart-endpoint pulls about a second apart. fetch.py's header says quote endpoint. Wording only.

## Not tested
Settle window 14:30 to 17:00 ET, the 17:00 boundary and the evening, a contract in its roll or expiry week, a real vendor freeze, a holiday session, the live dashboard renderer and tile, fleet_dashboard.py L641, an exchange settle (no CME read), fast tape (one 4-minute window, n small), `--delta` paths with a refused row.
