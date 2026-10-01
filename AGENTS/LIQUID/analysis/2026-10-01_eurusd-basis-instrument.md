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
| **2022-09/10 (UK LDI / Credit Suisse)** | **$11.09B SNB [2022-10-19]** (also $6.27B [10/12], $3.10B [10/05]); ECB max $0.27B | $11,302M [2022-10-26] | fires, on the SNB (single-institution stress, CS) |
| **2023-03 (SVB / Credit Suisse)** | **$0.48B ECB [2023-04-05]** | $587M [2023-03-22] | ⛔ **MISSED.** The Fed moved the lines to daily ops and almost nobody drew. Credit Suisse was funded through SNB franc liquidity, not dollars |
| Oct–Dec 2016 (US money-fund reform squeeze) | $3.54B ECB [2016-10-19] and a run of $1.0–1.5B ops | — | fires at WATCH |
| 2024–26 | ECB per-op p50 $0.099B · p95 $0.216B · max $0.38B (non-quarter-end) | p50 $106M · max $1,357M [2024-01-03] | calm |

**Turn ops are excluded by design:** a short op (≤21 days) spanning a quarter-end is mechanically larger. Before that exclusion, all three ≥$5B hits in 2014–19 were turn ops (2016-09-28 $6.35B · 2017-12-20 $11.91B · 2018-03-28 $5.01B). A long op that spans a quarter-end (the 84-day 2020-03-18 op) still counts.

## 4. PROPOSED lines (⛔ NOT registered; Will's word)

| Line | Rule (European counterparty, single op, short turn ops excluded) | Hits 2021H2→now (327 non-turn ops) | Hits 2014–19 (235) |
|---|---|---|---|
| **WATCH** (a look, no route) | op ≥ **$1.0B** and < $5B | **1** (SNB $3.10B [2022-10-05]) | 15 (all ECB, Aug–Dec 2016 squeeze) |
| **ALERT** (route via WALTER) | op ≥ **$5.0B**, or SWPT ≥ **$10,000M** | **2 ops, one episode** (SNB Oct 2022) | 0 |

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
