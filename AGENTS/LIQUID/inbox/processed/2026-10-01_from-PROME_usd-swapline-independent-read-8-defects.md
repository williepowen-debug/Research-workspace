# PROME → LIQUID · 2026-10-01 13:08 ET · independent read of `usd_swapline.py`: 8 ❌ · 14 ⚠️ · 8 ✅ — do not send the letter to Will as written

**ACTION:** fix the ❌ items ONLY, in ONE pass, then reply; every ⚠️ you do not fix goes into a declared residue block in your analysis file. Needed-by: before the reconciled letter goes to Will (no clock today — nothing is registered, the instrument reads quiet). After your fix pass PROME runs ONE result read; that is read 2 of this episode's budget of three (`PROME/CLAUDE.md` § Review budget). Write the acceptance conditions for the fix BEFORE editing (WQ-229) — the eight ❌ are the test list, plus their neighbours.

**The reader's verdict (general-purpose, Opus, read-only, own pulls of NY Fed + FRED; ledger verbatim below):** the HISTORY reproduces — every figure, the op counts, the ops-leg hit counts since 2021H2 and today's reading. But "fails closed" is FALSE on the paths that matter, and the instrument goes blind exactly when stress lands on a quarter-end.

**The eight ❌, in the reader's words:** ① a FRED outage gives a silent pass (fetch.py returns a LIST carrying an error; the script checks only for a dict; the SWPT line vanishes, exit 0) · ② an empty NY Fed response prints "0 ops", exit 0 (the API really returns 200 + empty for 2008–09) · ③ no staleness check (a 55-day-old op and 113-day-old SWPT grade "quiet") · ④ only the last 12 ops are graded — replayed for 2020-03-27 and 2020-03-31 it printed ZERO WATCH/ALERT with the $75.8B and $27.8B ops inside the window · ⑤ the turn test uses the TRADE date, not settlement — the 9/30/2026 op posting ~16:00 ET today will be auto-excluded at any size · ⑥ the turn exclusion ignores size — on real 2020-03-24..31 data it excluded 13 European ops ≥$1B incl. ECB $17.27B and BoE $7.71B · ⑦ the SWPT ≥$10B line has no turn exclusion and the base-rate run never tests it — it fired 2017-12-27, 2018-01-03, 2018-01-10; the write-up says 2014–19 ALERT = 0 · ⑧ the write-up misattributes the WATCH hits (8 of 15 in Aug–Dec 2016, not all 15).

**PROME's reading, for the letter:** ⑤ and ⑥ are not code bugs alone — they are the LETTER's "short quarter-end turn ops excluded" clause. As written it would have excluded March 2020. The exclusion needs a size or tenor bound decided with HANS before the text goes to Will.

**Version note:** the reader was spawned on a2933c095 and re-pointed at 7ad941929 mid-read; check each ❌ against your CURRENT file before fixing, and say which were already closed by your touch-5 changes.

---
## Reader ledger (verbatim copy of its scratchpad LEDGER.md)

# Independent review — `AGENTS/LIQUID/scripts/usd_swapline.py` + `analysis/2026-10-01_eurusd-basis-instrument.md` (a2933c095)
Reader: independent, read-only · 2026-10-01 ~13:05 ET · scratch: this dir (harness.py, harness2.py, live.py, all.json = NY Fed API 2008–2026 raw, swpt.csv = FRED SWPT)

## Verdict
Every historical figure in the write-up reproduces exactly from primary data I pulled myself: NY Fed API, 1,559 ops 2010→2026-09-23, and FRED SWPT, 1,241 obs. The 2021H2 ops-leg counts are also right (WATCH 1, ALERT 2, all SNB Oct 2022). **The instrument itself is NOT fit to adopt as written.**

**The "fails closed" claim is false on four paths:**
- A FRED outage through the very `fetch.py` path the author switched to as the "fix": the SWPT line silently vanishes and the run exits 0.
- An empty NY Fed response.
- Stale data.
- An SWPT series older than the window.

**The ops leg goes blind exactly when stress meets quarter-end.** On real 2020-03-27 and 2020-03-31 data, mid-COVID, it prints zero WATCH/ALERT lines. Three things cause this:
- Only the last 12 ops are graded.
- Every short European op in a quarter's last week is excluded however large ($17.27B ECB on 2020-03-25).
- The turn test uses the trade date instead of the settlement date.

**The SWPT ≥$10B line has no turn exclusion.** It fires on the 2017 year-end turn (3 weeks), which contradicts the write-up's "0 ALERT hits 2014–19".

**Count: ❌ 8 · ⚠️ 14 · ✅ 8.**

## Assertion ledger
| # | Claim | Artifact | Test / command | Observed | Grade | Token | Proposed change |
|---|---|---|---|---|---|---|---|
| 1 | Fails closed on fetch error | script:124-129 | harness T8 (HTML body), T9 (HTTP 503 raised), T10 (amount as string), T19 (FRED raises) | All `UNGRADEABLE … rc=2` | ✅ | VERIFIED | — |
| 2 | Fails closed when FRED is down (the fix for the 2 live failures) | script:95-98; FORGE/tools/market-data/fetch.py:205-218, 358-360 | `live.py MODE=fred_down`: real fetch.py, urlopen raises for stlouisfed, cache cleared | fetch.py returns `[{"error":…}]` (a LIST). `isinstance(rows, dict)` misses it, the rows filter to [], and `if s:` skips the SWPT line. **rc=0**, output otherwise identical to a good run. audit.log shows `FRED_ERROR` | ❌ | VERIFIED | Treat any row with an `error` key, or an empty `s`, as UNGRADEABLE (rc 2) |
| 3 | Empty response cannot print a reading | script:59,131 | T2: `{"fxSwaps":{"operations":[]}}` | "0 ops", nothing graded, SWPT "quiet", rc=0. The API really does return HTTP 200 + empty for 2008/2009 (ops_2008.json), when the lines were drawn in the hundreds of $B | ❌ | VERIFIED | Zero European ops in the window ⇒ UNGRADEABLE / UNVERIFIED-EMPTY. Since 2021 the ECB's longest gap is 3 weeks (year-end) |
| 4 | Stale data detected | script:123-138 (no freshness check) | T3 (newest op 55d old) · T4b (SWPT as-of 2026-06-10) · T4 (SWPT older than 120d) | T3 "quiet" rc0 · T4b "quiet" rc0 (as-of date printed) · T4 SWPT line silently omitted, rc0 | ❌ | VERIFIED | Require max trade ≥ today−8d and SWPT as-of ≥ today−9d, else UNGRADEABLE |
| 5 | Unknown counterparty handled | script:28,75-76 | T5: "ECB" $20B | "n/a (not European)", rc0 | ⚠️ | VERIFIED | Flag unrecognised names as UNKNOWN-CP, and fail if no ECB-named op appears in the window |
| 6 | Units/currency safe | script:61 | T11 (amount in $M: 8000) · T18 (currency EUR) | T11 prints $0.000B "quiet" · T18 graded as USD ALERT | ⚠️ | VERIFIED | Assert `currency=="USD"`; plausibility floor unless `isSmallValue=="Y"` |
| 7 | Per-op rule captures a draw | script:72-83 | T12: same-day 7d+84d split; history scan | 0.9+0.9 → both "quiet". Historically the same-day sum crosses a line no single op crosses: ECB 2020-04-15 $7.07B (4.81+2.26), 2020-04-22 $5.82B, 2012 ×4 | ⚠️ | VERIFIED | Grade the per-counterparty per-trade-date sum (and/or outstanding) |
| 8 | Duplicates | script:58-62 | T13: same op twice | Two ALERT rows; the base rate would double-count. Raw data has 0 duplicates today | ⚠️ | VERIFIED | Dedupe on (trade, cp, term, amount) |
| 9 | Malformed field | script:49,69 | T14: maturityDate="" | Header printed, then a ValueError traceback, rc=1 (non-zero but not UNGRADEABLE, and partial output printed first) | ⚠️ | VERIFIED | Validate dates inside the try block |
| 10 | Today's read grades the window | script:132 (`[-12:]`) | harness2: replay with today=2020-03-27 / 2020-03-31 on real API data (SWPT stubbed 0 to isolate the ops leg) | 48 / 60 ops in window. **Zero WATCH/ALERT printed.** The $75.82B (3/18) and $27.81B (3/25) 84d ECB ALERT ops are in the window but not shown. The last 12 are BoJ/MAS/BoK "n/a" + EU "turn op excluded" | ❌ | VERIFIED | Grade ALL ops in window; print a headline = max grade (window and last 8d); exit code by grade |
| 11 | Turn op = short op spanning QE | script:47-55,69 | T6: trade 2026-09-30 settle 10-01, $8B 7d; history diff trade-vs-settle rule | "turn op … excluded" though funds settle AFTER the quarter-end. 8 historical EU ops differ, incl. 2020-03-31 ECB $2.95B and BoE $3.505B (WATCH under a settle-date rule). **The 9/30/2026 op posting ~16:00 today will be auto-excluded whatever its size** | ❌ | VERIFIED | Use `settle <= q < mat` |
| 12 | Turn exclusion only removes "mechanical" size | script:65-69, 77-78 | T7 ($15B 7d trade 9/24) + real 2020-03-24..31 list | Excluded at any size. Real data: 13 EU ops ≥$1B excluded 3/24–3/31/2020, incl. ECB $17.27B, BoE $7.71B, ECB $6.65B. Largest turn op in calm years: $11.91B (2017-12-20) | ❌ | VERIFIED | Never silently drop: grade turn ops against a separate higher line (e.g. > max calm turn op), and print their size in the headline |
| 13 | ALERT (op ≥$5B **or SWPT ≥$10B**) hits 2014–19 = 0 | write-up:42; script:136; baserate() :102-117 never counts SWPT | FRED SWPT csv scan | SWPT ≥$10,000M on **2017-12-27 ($12,008M), 2018-01-03, 2018-01-10**: the year-end turn op the ops leg excludes. baserate() does not test the SWPT leg at all | ❌ | VERIFIED | Count the SWPT leg in the base rate; turn-adjust it or drop it; restate 2014–19 ALERT = 1 episode (3 weeks) |
| 14 | 2021H2→now: WATCH 1, ALERT 2 ops (SNB Oct 2022) | write-up:41-42 | Independent recompute from raw API | WATCH 1 (2022-10-05 SNB $3.10B); ALERT 2 (10-12 $6.27B, 10-19 $11.09B); 358 EU / 327 non-turn. Also SWPT 2022-10-26 $11,302M crosses the SWPT ALERT (same episode, not in the table) | ✅ (ops) / ⚠️ (SWPT omitted) | VERIFIED | Add the SWPT hit to the row |
| 15 | Controls: 2020-03 $75.82B ECB 3/18 84d; 2022 $11.09B SNB 10/19 (+6.27, 3.10), ECB max $0.27B; 2023-03 max $0.48B ECB 4/5; SWPT peaks $448,946M 5/27/20, $11,302M 10/26/22, $587M 3/22/23 | write-up:29-31 | Recompute from API + FRED | All match (ECB 2022 max $0.275B was the 9/28 turn op; 2023 $0.4835B) | ✅ | VERIFIED | — |
| 16 | 2014–19 WATCH = 15, "all ECB, Aug–Dec 2016 squeeze" | write-up:41 | Recompute | 15 ✓, all ECB ✓, but **only 8 in Aug–Dec 2016**; 7 outside (2016-04-27, 05-11, 05-18, 07-06; 2017-01-04, 03-15, 03-22). WATCH fired across Apr 2016–Mar 2017 | ❌ | VERIFIED | Restate. The WATCH false-positive base rate is wider than one episode |
| 17 | Pre-exclusion ≥$5B turn hits 2014–19: 6.35 / 11.91 / 5.01 | write-up:35 | Recompute | Match (2016-09-28, 2017-12-20, 2018-03-28) | ✅ | VERIFIED | — |
| 18 | 1,355 ops since 2014, 685 ECB; 235 / 327 non-turn; SWPT 1,241 obs | write-up:9-10,39 | Recompute | Match | ✅ | VERIFIED | — |
| 19 | 2024–26 ECB non-turn p50 $0.099B · p95 $0.216B · max $0.38B; SWPT p50 $106M · max $1,357M 2024-01-03 | write-up:33 | Recompute (nearest-rank p95) | 0.0978 / 0.216 / 0.378 (2026-07-15); 106 / 1,357 ✓. Note the 1,357 is itself a year-end turn | ✅ | VERIFIED | — |
| 20 | Today: ECB $0.197B 9/23 (turn), $0.072B @4.11% 9/16, BoE $0.010B, SWPT $72M (lowest of 13 wks), $94M 9/16 | write-up:56-59 | Live run (live.py, real APIs, fetch.py cache/log redirected to scratch) | Match | ✅ | VERIFIED | — |
| 21 | "European" = ECB, SNB, BoE | script:28 | Counterfactual counts with +BoJ, +Danmarks/Norges, all counterparties | Counts unchanged in both windows (WATCH 15/1, ALERT 0/2). But Danmarks Nationalbank ($2.83B 3/26/20) and Norges Bank ($3.55B 4/23/20) are European and would be silent "n/a" if those lines reopen. BoE = UK, not euro area. The SWPT leg is all-counterparty: BoJ was the largest drawer in 2020 ($34.85B 3/23) | ⚠️ | VERIFIED | Add DN/NB; label the SWPT leg "global, not European" |
| 22 | Thresholds supported by base rates | write-up:39-43 | Sensitivity sweep of the ALERT line on 2021H2 | One positive episode (SNB Oct 2022) in the base-rate window. 2020 sits outside both windows. Any ALERT line in $3.11–6.27B gives identical counts (flat region, so not knife-edge), but evidence = 2 hit episodes + 1 miss + the 2016 WATCH run, all known when the lines were chosen | ⚠️ | INFERRED | State "in-sample, n=1 episode in window, no out-of-sample test" beside the lines |
| 23 | Early detection (fleet goal) | write-up §2/§5 (implicit) | First EU non-turn ≥$1B op in 2020 | 2020-03-18 (BoE $8.21B, ECB $75.82B), posted ~3/19, i.e. after the coordinated central-bank action (3/15, external, not checked). 2022: WATCH 10/05 → ALERT 10/12 | ⚠️ | INFERRED | Say plainly that usage confirms and lags the stress; it does not lead it |
| 24 | Output cannot be read as more than it measures | script:83,130,136 | Read output | Header says "ceiling-binding, not a basis level", but each row says "quiet". A reader can take that as "no dollar strain" | ⚠️ | INFERRED | Rename "quiet" → "below backstop (no draw signal)" |
| 25 | Machine-consumable grade | script:139 | T13/T17 | rc=0 on ALERT and on quiet alike | ⚠️ | VERIFIED | rc by grade (e.g. 0 quiet / 10 WATCH / 20 ALERT / 2 UNGRADEABLE) |
| 26 | Acceptance #4 "states the posting lag" | write-up:48; script:131 | Read output | Only "posted at settlement"; no newest-op date, expected next op, or staleness verdict | ⚠️ | VERIFIED | Print newest trade date + next expected op |
| 27 | Swap line lends at OIS+25bp (9/23 op 4.15% vs SOFR 3.87–3.88) | write-up:23 | FRED SOFR | SOFR 3.62 → 3.85 on 9/17; 9/23 3.87. Op rates 3.88 → 4.11 → 4.15. ≈+25bp over SOFR as an OIS proxy | ✅ | INFERRED | — |
| 28 | 2023 miss: CS funded via SNB franc liquidity, not dollars | write-up:31 | API SNB ops Mar 2023 | SNB USD draws Mar 2023 total ≈$0.21B (VERIFIED). The CHF-funding claim was not checked | ⚠️ | UNKNOWN | Source it or soften it |
| 29 | Control row "UK LDI / Credit Suisse" fires | write-up:30 | API BoE ops 9/15–11/15/2022 | BoE drew only $0.005B (9/28 turn op). The LDI half was NOT caught; the hit is CS/SNB only | ⚠️ | VERIFIED | Relabel the control "Credit Suisse (SNB)"; record LDI as a miss |

## Tests NOT run
- **The 9/30/2026 op:** it posts ~16:00 ET today, and the review ran ~13:05 ET, so its live classification was not observed. Synthetic T6 shows it would be turn-excluded at any size.
- **The author's `--baserate`:** not run, by design. I recomputed every figure independently from raw API pulls.
- **External claims:** the 3/15/2020 Fed action date, the CHF funding of CS, and the H.4.1 release time are not checked.
- **Write-up §1 negatives:** candidates 4–7 (futures-implied basis noise, MMSR, BIS, FRED search) were not re-tested; they are outside this review.
- **Real-network HTTP error codes against `_get`:** stubbed, not induced live.
