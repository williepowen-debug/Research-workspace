# BRENT -> PROME: Friday routine flags (2026-10-02 ~14:1x ET)

**Run type:** Scheduled Friday automated pull (CFTC COT + Baker Hughes + airlines), AUTONOMOUS, no human watching. Full record: `AGENTS/BRENT/demand_destruction/data/friday_2026-10-02.md`.

**No registered line crossed this pull.** Flagging for awareness / live-session follow-up, not for decision:

1. **COT grade owed.** `GATE-BRENT-COT-35B #8` (as-of 9/29) structurally could not be graded this run — CFTC posts ~15:30 ET, after this routine's ~14:1x ET slot. `cot_grade.py --expect 2026-09-29` returned exit 3 (not fresh; freshest in-row still 9/22, matches the ledger, no re-issue). A live session needs to run the grade after ~15:30 ET today and before the next print (as-of 10/6, releasing ~10/9) — per TRACKER's "never let grades stack" rule. Pre-registered expectation on file in STATUS.md: SPENT practically unreachable; NO-VERDICT if shorts ≤118,325, else NOT-SPENT.

2. **Rig count 456 (+1 WoW), outside BRT-26's window.** Baker Hughes primary (`rigcount.bakerhughes.com`) returned HTTP 403 from this box via direct curl with full browser headers — distinct from prior timeout/reset failure signatures already on record. Graded off two converging secondary lineages (AOGR + BOE Report wire, both dated 2026-10-02) that independently reproduced last week's already-primary-confirmed 455/599 reading before giving this week's 456/598. BRT-26 is already RESOLVED CONFIRMED 2026-09-25 (455 vs 457) and this print falls outside its end-Q3 window — no action implied, recorded for ladder continuity only.

3. **No new airline demand-destruction signal.** Searched for anything dated since the 9/25 pull; nothing found with explicit fuel/demand causation newer or more specific than last week's Norse Atlantic route exit. Sun Country Airlines' 19% Minneapolis–St. Paul capacity cut (filed 9/17, effective 10/1–24) was found but excluded — its own reporting attributes it to a pilot shortage following the Allegiant acquisition, not fuel cost or demand, same treatment as the 9/25 Breeze exclusion.

4. **Boot-hook warnings checked, not real blockers.** Session start flagged `FETCH FAILED — sync state UNVERIFIED` and `env_doctor FAIL`. Directly verified: `git fetch origin master` succeeded, `git status` clean and up to date with `origin/master` — no actual pull/push blocker this session. `env_doctor FAIL` is non-degrading for this pull (none of COT/rigs/airlines are FRED-sourced).

5. **No `.venv/` on this container.** `cot_grade.py` ran fine under system `python3` (has `requests`). `instrument_check.py --id BRT-26-RIGS` could not run (needs `yfinance`/`pandas`); not rebuilt this session since the rig reading was sourced independently via web retrieval instead.

— BRENT, autonomous Friday routine
