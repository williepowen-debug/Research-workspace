# BRENT SCRATCH — October 21 catch-up (21:11–21:4x ET)

## CHANGES SINCE LAST SESSION
- EIA week 10/16 (released 10/21): commercial crude −3.061 M to 412.517 M; gasoline −2.952 M; distillate +1.674 M; production 13,269 kb/d (−410 w/w). Gasoline demand four-week +1.46% YoY.
- Brent December (`BZZ26`) hit $111.99 intraday on 10/20 (five-month high), settled $108.79, then $108.82 on 10/21. WTI December (`CLZ26`) settled $97.15; November expired 10/20 at $101.79. Evening 10/21 bid: `BZZ26` $110.44.
- Saudi Shaybah drone intercepted 10/21; debris killed two outside the perimeter; operations unaffected (Saudi MoE). Tankers hit off Bukha (10/21) and Al Faw (10/20). JMIC: Hormuz SEVERE, wider Gulf SUBSTANTIAL.
- Russia: a partial 500 kt diesel permission, not a lift (WALTER -016 correction). Kremlin says the first 40 kt loads "in two to three days" (intent). Russia agreed to resume US-mediated Ukraine talks (bearish price driver on 10/21).
- Kpler via WSJ: Hormuz volume ~14 mb/d, 82% of pre-war, week to 10/18; all Middle East routes >24 mb/d vs 23.3 pre-war (preliminary, relayed).

## WHAT I DID THIS SESSION
- Boot rc=2 (FRED dead from scheduled maintenance; JWC and tanker-liveness stale; 25 aged INCIDENTS rows; LESSONS_INDEX ledger stale). Origin had no new commits, so no pull was needed.
- **Boot step 2b slip:** my first listing sorted `eia_2026-10-21.md` out of view. Caught before any STATUS write; its figures match mine exactly. Next boot: list routine outputs by mtime (`ls -t`), not alphabetically.
- BRT-31 week two evaluated from a release-day primary capture: +1.461596692482385%, NON-QUALIFYING, streak 0, price +41.90%, counter 0 of 3; OPEN at 40%. Recorded in the PREDICTIONS row, prediction note and CHANGELOG.
- Hormuz basis settled for PROME/HAWK: PortWatch is an AIS lower bound; one volume figure recorded with its basis. Packets to HAWK inbox and PROME/inbox. [Report](research/2026-10-21_eia-oct21/REPORT.md).
- TRACKER: lines 4, 6, 10 and 11 refreshed, plus a SCOPED-PARTIAL stamp. STATUS judgment, limits and summary updated; NEXUS_BRIEF refreshed.
- Ten mail items consumed and filed (eight WALTER, two PROME). HENRY 10/19 and OSPREY 10/15 remain deferred.

## NEXT SESSION (dated, future-verifiable)
1. **DONE 21:35 ET:** HENRY December observations ADOPTED (native-tick basis), extended to 10/20 100.1768 and **10/21 95.0479 (near-line)**. [Adoption](research/2026-10-21_henry-december-adoption/REPORT.md). Next: if TERRY or Will reads the CME 10/21 HOZ26/CLZ26 settlements, record them; they govern. The 10/22 window crack is the next leg-A input (TERRY grades).
2. **Friday 10/23 ~15:30 ET:** COT #11 (as-of 10/20). Run `cot_grade.py --expect 2026-10-20` after release only. Record the Baker Hughes print only.
3. **Monday 10/26:** grade BRT-30 on the JWC circular number (10/21 index: newest JWLA-035 Black Sea). Read the complete note `thesis/prediction_notes/BRT-30.md` first. The USO short-interest publication is the same day.
4. **Wednesday 10/28 10:30 ET:** EIA week 10/23, the third BRT-31 window week; it can only start a streak. Price leg: retail on 10/26 vs 2025-10-27.
5. OSPREY ask: confirm Bloomberg Russia four-week seaborne exports to 10/11 (~3.7 M bpd) at text if access allows.

## OPEN THREADS / WATCHES
- 🔴 Hormuz: the Kpler October primary is unread; the ~14 mb/d is relayed and preliminary. Watch for revision and for any Kpler daily collapse like 10/11 (~2.9 M bbl relayed).
- 🟠 Saudi/Houthi strikes: the 10/19 Houthi claims (Yanbu, Shaybah) have no Saudi confirmation. The 10/21 Shaybah event was an intercept. FALCON grades; there is no BRENT INCIDENTS row without confirmed facility damage.
- 🟠 Russia diesel: producer restriction expires 10/31 (docket). The 40 kt first loading is intent; departures (Leruo, Dolunay) are not deliveries.
- 🟠 KILL-LEG2-JWC-LISTING REGISTRY stamp is still 10/05 (instrument check STALE). Tonight's index read was not written into REGISTRY; re-stamp at the BRT-30 grade.
- 🟡 NC gasoline-tax and 50-state contamination caveat carries forward for any final BRT-31 NOT MET. Jet-margin basis, DOE reserve conflict and USO short-interest gaps remain deferred.

## POSITION DECISIONS PENDING
- None new for Will. TRADE owns structural receipts; broker truth is off-repo; TERRY constructs and grades. USER.md: no expiry reminders.

## MAIL STATE
- Inbox: OSPREY 2026-10-15 (deferred, item 5). HENRY 10/19 consumed and filed 21:35 ET. WALTER lane clear as of 21:18 ET.
- Outbox: HAWK, PROME, HENRY and TERRY packets written 10/21; publication is not consumption.

## WORKBOOK HEALTH
- LESSONS_INDEX ledger is flagged STALE +11d by ledger_staleness; no lesson touched this session. INCIDENTS: 25 rows past re-verify budgets (flags only). FRED-keyed thresholds were ungradeable tonight because of FRED maintenance, not a key fault.
