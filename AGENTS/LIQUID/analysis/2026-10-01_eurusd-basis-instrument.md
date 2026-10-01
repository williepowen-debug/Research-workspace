# EUR/USD funding blind spot: a quoted basis LEVEL is not reachable free; USAGE of the Fed swap lines is. Instrument built, lines PROPOSED, today quiet

**LIQUID · 2026-10-01 ~13:0x ET · PROME touch 4 on Will's word ("go for the six", 12:49 ET).** Co-owned with HANS: proposed split sent by SendMessage at 12:50 (LIQUID = US side / usage; HANS = European side / any quoted basis, HANS-T-12); my pulls sent to HANS at 12:59. No reply from HANS at writing. $0 · no trade · no threshold registered · X1 CLOSED.

## 1. Candidates tested (each pull shown; confidence tokens per Class 13)

| # | Candidate | Pulled today? | Result | Lag | Verdict |
|---|---|---|---|---|---|
| 1 | **NY Fed USD liquidity swap operations, per op, by counterparty** (`markets.newyorkfed.org/api/fxs/usdollar/search.json`) | ✅ yes, HTTP 200 in 0.1s; full history 2014→9/23 (1,355 ops, 685 ECB) | Amount, term, rate, counterparty per op | posted at settlement (trade T, settle T+1, ~16:00 ET) | **REACHABLE, USABLE** (VERIFIED) |
| 2 | **FRED `SWPT`** (H.4.1 central-bank liquidity swaps, $M, Wed level) | ✅ yes, 2002-12-18 → 2026-09-23 (1,241 obs) | Aggregate across all counterparties | weekly, Thu ~16:30 ET | **REACHABLE, USABLE** (VERIFIED) |
| 3 | ECB USD operation allotments | not built separately | **The same transaction as #1 from the ECB's side** (the ECB on-lends what it draws on the Fed line); HANS's side if HANS wants the ECB page | — | covered by #1 |
| 4 | **CME EUR/USD futures-implied basis** (yfinance `6E=F` vs `EURUSD=X`, with SOFR [FRED] and €STR [ECB API], IMM-dated tenor) | ✅ reachable: 1,624 dated pairs 2019-10→10/01 | **Unusable.** Implied basis: calm 2025–26 median +144bp, SD 513bp, daily-change SD **709bp**; 2020-03 median +89bp, SD 815bp. Real stress moves are tens of bp. The spot and futures closes are not synchronous, so timestamp noise swamps the signal by ~10×. | daily | **ACCESS YES, DATA NO** (VERIFIED by computation). A synchronous settle-vs-fix pair is not free |
| 5 | FRED series search ("cross currency basis", "FX swap basis", "covered interest parity", "dollar funding basis") | ✅ API answered | 0 relevant series | — | **SEARCH-NOT-FOUND** |
| 6 | ECB `MMSR` public dataflow | ✅ 446 series pulled | Segments **O (OIS) · T · U only; no FX-swap segment** in the public set | — | **VERIFIED absent** in the public dataflow (the non-public MMSR FX-swap data exists, not reachable) |
| 7 | BIS SDMX catalog (`stats.bis.org/api/v1/dataflow`) | ✅ HTTP 200, 28 dataflows listed | No basis or CIP dataflow by name (BIS charts the basis from vendor data) | — | **SEARCH-NOT-FOUND** (catalog names only) |

**The access-vs-data finding:** three routes to a quoted basis LEVEL fail (4 unusable, 5/7 not found, 6 absent). One reaches the server and returns numbers that are noise; a reachable feed is not a usable instrument. What is reachable and clean is **usage**.

⚠️ **A reachability trap found while building:** FRED's `fredgraph.csv` *tarpitted* a Python request carrying this script's User-Agent (read timeout, 13.5s), while curl's UA returned in 0.4s and the NY Fed API answered the same Python request in 0.1s. The first two live runs printed `UNGRADEABLE` (fail-closed worked). Fixed by pulling SWPT through the standing `fetch.py` FRED API path. A negative here was a claim about the request, not about FRED.

## 2. What usage measures, and what it cannot

The swap line lends at **OIS + 25bp** (the 9/23 op priced 4.15% against SOFR 3.87–3.88). A bank with central-bank access draws only when dollars bought through the FX-swap market (including the basis) cost more than that. **So usage is a ceiling-binding indicator.** A material draw says the basis has reached the backstop for some borrower. It is **not a basis level**, it is **silent below the ceiling**, and it carries **stigma** (banks avoid it until they cannot).

## 3. Controls and base rate (`scripts/usd_swapline.py --baserate`; European counterparties = ECB · SNB · BoE)

| Window | Largest European op | SWPT peak | Reads as |
|---|---|---|---|
| **2020-03 (COVID)** | **$75.82B ECB [2020-03-18, 84d]** | **$448,946M [2020-05-27]** | fires, unmistakably |
| **2022-10 (Credit Suisse, via the SNB)** | **$11.09B SNB [2022-10-19]** (also $6.27B [10/12], $3.10B [10/05]); ECB max $0.27B | $11,302M [2022-10-26] | fires, on the SNB. ⚠️ **The UK LDI half was NOT caught** (BoE drew $0.005B, a turn op) *(relabelled 10/1, reader ⚠️#29)* |
| **2023-03 (SVB / Credit Suisse)** | **$0.48B ECB [2023-04-05]** | $587M [2023-03-22] | ⛔ **MISSED.** The Fed moved the lines to daily ops and almost nobody drew. Credit Suisse was funded through SNB franc liquidity, not dollars |
| Apr 2016 → Mar 2017 (incl. the Oct 2016 US money-fund reform squeeze) | $3.54B ECB [2016-10-19]; 15 ECB ops ≥$1B, **8 in Aug–Dec 2016 and 7 outside it** (2016-04-27, 05-11, 05-18, 07-06; 2017-01-04, 03-15, 03-22) | — | fires at WATCH across a year, so the WATCH false-positive rate is wider than one episode *(restated 10/1 after the independent read, ❌#16)* |
| 2024–26 | ECB per-op p50 $0.099B · p95 $0.216B · max $0.38B (non-quarter-end) | p50 $106M · max $1,357M [2024-01-03] | calm |

**Turn ops are graded on their own higher lines, never dropped** *(replaced 10/1 after the independent read, ❌#11/#12; the original "excluded by design" would have hidden ECB $17.27B and BoE $7.71B on 2020-03-25)*. A turn op = term ≤21 days whose funds are out over a quarter-end (**settle** ≤ QE < maturity). Lines: TURN-WATCH ≥ $5.0B · TURN-ALERT ≥ $15.0B. Calm 2010–2026 turn-op max $11.91B (2017-12-20); TURN-ALERT fires only on 2011-12-21 ($33.0B) and 2020-03-25 ($17.27B); TURN-WATCH fires on 3 calm turn ops (2016-09-28 · 2017-12-20 · 2018-03-28) plus 3 in March 2020. In-sample fit, said plainly.

## 4. PROPOSED lines (⛔ NOT registered; Will's word)

| Line | Rule (European counterparty, single op, short turn ops excluded) | Hits 2021H2→now (327 non-turn ops) | Hits 2014–19 (235) |
|---|---|---|---|
| **WATCH** (a look, no route) | non-turn op ≥ **$1.0B** and < $5B · turn op ≥ $5.0B | **1** (SNB $3.10B [2022-10-05]) | 15 non-turn (Apr 2016 → Mar 2017; 8 in Aug–Dec 2016) + 3 turn |
| **ALERT** (route via WALTER) | non-turn op ≥ **$5.0B** · turn op ≥ **$15.0B** · SWPT ≥ **$10,000M** outside a turn window (≥ $15,000M inside one: as-of QE −7 … +14 days) | **2 ops + SWPT 2022-10-26, one episode** (SNB Oct 2022) | **0** (under the old un-adjusted SWPT rule: 1 episode, the 2017 year-end, 2017-12-27 → 2018-01-10, $12.0B, ❌#13) |

**Acceptance conditions, written before any registration (WQ-229 shape):**
1. Fires on 2020-03 and on Oct 2022 (✓ both at ALERT). The 2023-03 miss is stated on every grade.
2. Never grades a short quarter-end turn op (✓ 2014–19 turn hits removed; the 9/23 op is labelled "turn op, excluded").
3. Fails closed: a failed fetch prints `UNGRADEABLE`, never "quiet" (✓ observed twice today, live).
4. Grades on the trade date and states the posting lag. An op is visible about T+1, and SWPT only on Thursday.
5. Prints PROPOSED on every line until Will rules (✓).
6. **Not yet done:** an independent reader (a consequential instrument under WQ-229) and a `--selftest` set. Both are owed before any registration.

## 5. Today's reading

| Read | Value | Grade |
|---|---|---|
| ECB 7-day op, trade 9/23 (matures 10/1) | **$0.197B @ 4.15%** | turn op (spans 9/30), excluded; ≈ the 2024–26 p95 for an ordinary op anyway |
| ECB 7-day op, trade 9/16 | $0.072B @ 4.11% | quiet |
| BoE, trade 9/23 | $0.010B | turn op, excluded |
| SWPT as-of 9/23 | **$72M** (lowest of the last 13 weeks; $94M [9/16]) | quiet |

**⇒ Nothing. No European draw on the Fed line through 9/23.** ⚠️ **The reading cannot yet see 10/01's periphery widening.** The 9/30 op (posts ~16:00 ET today) was bid before the move. **The first op that can show it trades 10/7 and posts 10/8;** SWPT as-of 10/7 publishes 10/8. And because usage is ceiling-bound, a quiet read after 10/7 would mean "the basis has not reached the backstop", not "no dollar strain".

## 6. Ownership

Proposed to HANS 12:50 ET; no objection or reply received by writing. **Instrument `usd_swapline.py` = LIQUID (US-funding consequence). Any quoted basis level = HANS (HANS-T-12).** PROME confirms or re-assigns.

## 7. Independent read (PROME touch 6, 8 ❌ · 14 ⚠️ · 8 ✅) — ACCEPTANCE CONDITIONS, written 2026-10-01 ~13:2x ET BEFORE the fix edit

The reader read a2933c095 and was re-pointed at 7ad941929. **Checked each ❌ against 7ad941929 by test before writing these:** ❌#2 (FRED down → silent pass) **already CLOSED** by touch-5's `verdict()` (a list carrying an error → no rows → `UNGRADEABLE`, rc 2; tested). ❌#10 (last-12 display) **CLOSED for the headline** (replays of 2020-03-27 and 2020-03-31 give ALERT) but **OPEN for display**. ❌#3 **partly** closed (a fully empty response → UNGRADEABLE, but only-non-European ops → "quiet"). ❌#4, #11, #12, #13, #16 **OPEN**.

| AC | Defect | Condition (the test list) |
|---|---|---|
| AC1 | #2 | Any FRED error row or empty SWPT → `UNGRADEABLE`, rc 2; the SWPT line is never silently omitted. (Already true; kept as a regression test) |
| AC2 | #3 | No European op in the window, or the newest European op older than 22 days (the longest normal ECB gap is a 3-week year-end op) → `UNGRADEABLE`, rc 2 |
| AC3 | #4 | SWPT as-of older than 10 days (weekly + a holiday-delayed H.4.1) → `UNGRADEABLE`, rc 2, not just a flag |
| AC4 | #10 | Every European op in the window is printed and graded, none hidden by a row cap. The headline grade covers the last 14 days and names the newest European trade date. Real-data replays 2020-03-27 and 2020-03-31 → ALERT |
| AC5 | #11 | The turn test uses SETTLEMENT: an op is a turn op iff term ≤ 21d AND settle ≤ quarter-end < maturity. Trade 9/30, settle 10/1 → NOT a turn op. Trade 9/29, settle 9/30, maturity 10/7 → turn op |
| AC6 | #12 | Turn ops are never dropped. They are graded on their own higher lines and printed with size: **TURN-WATCH ≥ $5.0B · TURN-ALERT ≥ $15.0B.** Real 2020-03-25 ECB $17.27B → TURN-ALERT; 2011-12-21 ECB $33.0B → TURN-ALERT; calm 2010–2026 turn ops → TURN-ALERT 0 times (calm max $11.91B, 2017-12-20) |
| AC7 | #13 | SWPT leg turn-adjusted and counted in `--baserate`: ALERT ≥ $10,000M outside a turn window; ≥ $15,000M inside one (as-of within quarter-end −7 … +14 days). Calm 2017-12-27 … 2018-01-10 ($12.0B) → not ALERT; 2022-10-26 ($11.3B, outside) → ALERT |
| AC8 | #16 | Write-up restated: 2014–19 WATCH = 15 ops, **8 in Aug–Dec 2016 and 7 outside it** (Apr 2016 → Mar 2017); 2014–19 SWPT ≥$10B under the old rule = 1 episode (the 2017 year-end), 0 under AC7 |

**Neighbours (WQ-229, considered):**
- **ordinary:** today's live run must still grade, newest ECB op 9/23.
- **overlap:** an op that is both a turn op and large is graded on TURN lines, never on both.
- **wrong owner:** a large non-European op stays `n/a`, and SWPT is labelled global. This is ⚠️#21, residue.
- **missing information:** a malformed date is ⚠️#9, residue.
- **concurrent:** N/A. A read-only script with no shared state.

**Bound provenance, stated so nobody reads it as joint:** HANS agreed (a)(b)(c) at `06e40bb7a`. **The size bound on the turn exclusion (AC6/AC7) is LIQUID's post-read change, NOT yet seen by HANS.** It is fitted in-sample: $15B sits $3.1B above the calm maximum and $2.3B below the 2020 hit.

### 7a. Fix pass result (one pass, 2026-10-01 ~13:2x ET)

| AC | Result | Evidence |
|---|---|---|
| AC1 | ✅ | selftest (no SWPT rows → UNGRADEABLE). Was already closed at 7ad941929 |
| AC2 | ✅ | selftest: no ops / only BoJ / newest European op 23d old → UNGRADEABLE; 22d → graded |
| AC3 | ✅ | selftest: SWPT 11d old → UNGRADEABLE; 10d → graded |
| AC4 | ✅ | **real-data replays**: 2020-03-27 (31 European ops) and 2020-03-31 (36) → ALERT. The live run prints all 10 European ops in 60 days (no row cap); the headline names the newest European op and the SWPT as-of |
| AC5 | ✅ | selftest; real 2020-03-31 ECB $2.95B and BoE $3.50B (trade 3/31, settle 4/1) now grade WATCH, not turn |
| AC6 | ✅ | `--baserate`: TURN-ALERT = 2011-12-21 $33.0B, 2020-03-25 $17.27B only; the calm max $11.91B is TURN-WATCH |
| AC7 | ✅ | `--baserate`: SWPT episodes 2008-01, 2008-04, 2011-12, 2012-10, 2020-03, 2020-12 (the tail of the 2020 regime, $10.0B), 2022-10. The 2017 year-end is no longer an ALERT |
| AC8 | ✅ | §3 and §4 restated in place (replaced, with the reason inline) |

**States (WQ-229): IMPLEMENTED ✅ · TESTED ✅** (selftest 32/32, live, `--baserate`, two real-data replays) · **INDEPENDENTLY VERIFIED: NO**, pending PROME's result read (read 2 of 3) · **STILL UNRESOLVED:** the ⚠️ residue below, and the turn bound is not yet seen by HANS.

**Declared residue (⚠️ not fixed in this pass, by the reader's number):**
- #5 unknown counterparty names grade "n/a", not flagged.
- #6 no `currency == "USD"` assert and no units plausibility check.
- #7 per-op, not per-counterparty same-day sum (ECB 2020-04-15 $7.07B split 4.81 + 2.26 crosses ALERT only when summed).
- #8 no de-duplication.
- #9 a malformed date raises outside the try (rc 1, not UNGRADEABLE).
- #21 Danmarks Nationalbank and Norges Bank are not in the European set; SWPT is now labelled global.
- #22 the lines are in-sample, n = 1 episode in the base window, no out-of-sample test.
- #23 usage confirms and lags; it does not lead (2020: first ≥$1B non-turn op 3/18, after the 3/15 coordinated action, UNVERIFIED date).
- #24 "quiet" is renamed in the HEADLINE only; per-row grades still say "quiet".
- #25 the exit code does not encode the grade.
- #26 no "next expected op" line.
- #28 the CHF-funding-of-CS claim in §3 is UNKNOWN (unsourced): treat it as unsourced.
- ⚠️ **Not residue, and outside the ❌-only scope, disclosed:** ⚠️#14 (the SWPT 2022-10-26 hit, added to the §4 ALERT row) and ⚠️#29 (2022 control relabelled to Credit Suisse via the SNB, with the LDI miss recorded) were fixed **in the same table rows AC8 restated**. They are two cell edits, no code.
- Also pending from the HANS replay: excluding NY Fed `isSmallValue = Y` test ops (it does not change any line here; deferred so as not to widen this pass).

**The 9/30 op:** not yet posted at writing (NY Fed posts at settlement, ~16:00 ET 10/1). **Not graded tonight with any turn test; to be reported raw** per PROME. Note: under AC5 a trade-9/30 / settle-10/1 op is not a turn op at all.

**Letter clause, re-settled:** the reconciled letter's "short (≤21 days) ops spanning a quarter-end excluded" is REPLACED by the AC5/AC6/AC7 turn rule (settlement-keyed; turn ops on their own lines; SWPT turn-adjusted). **HANS agreed (a)(b)(c) at `06e40bb7a`; the size/tenor bound on the turn exclusion is LIQUID's post-read change, NOT yet seen by HANS.**
