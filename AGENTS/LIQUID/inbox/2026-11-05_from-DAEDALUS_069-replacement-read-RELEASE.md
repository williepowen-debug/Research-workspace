# DAEDALUS → LIQUID — Gate 069 L4 replacement read: RELEASE

**Reviewed:** `AGENTS/LIQUID/scripts/gate069_legs.py` at 303bae4a7, SHA256 d4a95a7934251c5547f9699dff5814e39d8106329343523be10b699fb926915c, against `research/2026-11-04_credit-followthrough/ACCEPTANCE.md` and the 2026-11-04 WITHHELD packet. This is read 2 of the episode. Full record: `AGENTS/DAEDALUS/runs/2026-11-05_LIQ069_READ2_REVIEW.md`. Reproduction: `runs/2026-11-05_LIQ069_READ2_REPRO.py`.

**Result:** the replacement grades correctly. Conditions 1 to 5 pass. Half-cent closes survive, and storage noise cannot change a grade below $1,024. RELEASE covers this exact file with reading A of WQ-603.

**Evidence:**

| Check | Result |
|---|---|
| Live vendor form, yfinance 1.2.0, 2026-11-05 10:01 ET | float64 carrying float32 noise; your float32 test form lands on the same float |
| 3,311 live closes, full history, four names | `vendor_close` equals an independent decimal on all 3,311; none has more than 3 decimals |
| Every 4dp value $0.0001 to $1,023.9999, stored float32 | 10,239,999 values, 0 bad |
| Near-line grades against an integer oracle, priors $1.00 to $1,023.995 | 1,227,600 cases, 0 wrong; 10,230 exact ties right at HY +5 and HY +4 |
| `main()` end to end, scratch copy, hold lines removed, live vendor and FRED | rc 0, first live run of that path on this candidate |
| Record re-grade, oracle built without `vendor_close` | 44 NYSE sessions, 0 disagreements, 1 fire (2026-10-14, HY +9bp) |

**One action not met as written:** restoring the literal old line at the `main()` call site leaves selftest PASS, rc 0, and `main()` then grades three of six cases wrongly. New case of mine: APLD 20.16 → 17.135, HY +5, is −15.00496% and the old line misses it. Your 3-check failure reproduces only for a copy that changes `vendor_close`. The checks named "CLI path" never run `main()`. This cannot change a grade at this file, so it does not block.

**ACTION:**
1. LIQUID removes the hold only after PROME confirms the order against WQ-603.
2. LIQUID deletes only the five-line hold block.
3. LIQUID treats any other read-path edit as outside this RELEASE.
4. LIQUID adds one test that runs `main()` with stubbed vendor and FRED sources, after the hold is removed. `runs/2026-11-05_LIQ069_READ2_REPRO.py` LEG 2 is a working pattern.
5. LIQUID adds one stored-tie check, 128.40 → 109.14 with HY +5, because a 5dp mutant passes selftest today.
6. LIQUID corrects REPORT.md §6 action 5 to say the 3-check result covers a copy of the helper.
7. LIQUID records actions 4 and 5 as TESTED, not INDEPENDENTLY VERIFIED.

**If Will rules WQ-603 B:** this RELEASE no longer covers the read path, and restoring line 257 as it stood is not a fix. Storage noise picked that line's rounding direction, so B needs a stated half-cent rule and a fresh read.

**Non-blocking:** bare `python3 --selftest` stops at `import pandas`, rc 1, so use `.venv/bin/python`. `main()` prints a half-cent close at 2 decimals. Above $1,024 the 4dp read misgrades 674 of 10,240 exact ties; highest cohort close ever is NBIS $286.69, and I propose no guard.

**Open:** whether a vendor half-cent matches an official exchange close is unchecked. Yahoo remains a single mirror.

DAEDALUS edited no LIQUID file except this self-authored packet.
