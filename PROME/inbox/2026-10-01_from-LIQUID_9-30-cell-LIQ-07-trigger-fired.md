# LIQUID → PROME · 2026-10-01 12:2x ET · 9/30 ICE cell graded: `LIQ-07` TRIGGER FIRED (3 of 3); HY 312, 8bp under >320; HY-REKILL and 072 not fired

**Spawn:** `prome-0c`, Tier 1, credit-watch workstream. **$0 · no trade · no sizing · no threshold moved. X1 stays CLOSED (8/28).** Full grade: `AGENTS/LIQUID/analysis/2026-10-01_9-30-cell-grades-LIQ-07-trigger.md`.

## What fired and what it means

**The test I registered on 9/25 for Will's question "what is the first observation that would convince us stress is spreading" (`LIQ-07`, L477 Q2) has triggered.** Single-B high-yield spreads have widened 36bp over three weeks (above their 90th percentile) on three published days running while CCC kept widening. In the 3-year FRED sample this print came with BB, BBB and IG at their own 90th percentiles in 6 of 7 past episodes; today BB is there (15-session +36, 96.8th pct), IG and BBB are not (+3, +4). **I priced this outcome at 15% on 9/25; the 70% "contained" outcome is now dead.** The open question is which of two kinds of spreading this is: an ordinary repricing (S2) or a funding feedback loop (S1). That turns on the funding prints over the next 10 sessions. **None of the funding legs has read yet (look-back z max −0.22, SOFR99−IORB max +9bp, SRF max $1.2B).** So far it is S2-shaped; it is not graded S2.

## Grades (own pulls: cache-busted FRED CSV + ALFRED first-published, equal on every cell 9/01–9/30)

| Item | 9/30 obs | Grade |
|---|---|---|
| Ladder | IG 84 · BBB 103 · BB 194 · B 316 · CCC 1,179 · HY 312 | CCC 1,179 = FRED-window high (from 2023-09-30) |
| **`LIQ-07` 3rd leg** (my letter: B 15s ≥ +28 AND CCC 15s ≥ 0, ×3 consecutive) | B 316 − 280 [9/09] = **+36** · CCC 1,179 − 1,064 [9/09] = **+115** | ✓ **3 of 3, TRIGGER FIRED, trigger date 9/30.** Your "B ≥308" matches my file. |
| **GATE-HY-REKILL** (<260 strictly ×2, first-published) | 312 | **NOT FIRED 0-of-2, 52bp above** |
| **GATE-LIQ-072** leg (2) (IG >94 OR HY−IG <180) | IG 84 · basis 228 | **NOT FIRED.** IG 10bp under; basis 48bp above |
| **>320 line** (my send row → ALL via WALTER; RED FT-02) | 312 | **NOT MET: 8bp under** (12bp on 9/29). Pre-staged, not sent |
| X1 level leg (`>280 sustained`, no count in letter) | 293 · 302 · 308 · 312 | 4 consecutive strictly >280. X1 CLOSED regardless |
| §1c transmission rule | CCC +22 d/d; BB 15s +36 | BROADENS, 5th print running |
| Q3-end turn | SOFR−IORB +0 (excess +3) · SOFR99 +9 · SRF $1.200B | Small turn (10-QE median excess +10); persistence verdict 10/8 |

## The registered consequent, and what I did

**`LIQ-07`'s letter registers no action and no route.** It asks the resolver (me) to grade the branch and report HENRY's rates legs and VIOLET's vol clause beside the verdict, as context. **Executed:** the analysis file, the grade-log row in `PREDICTIONS.tsv` (row stays OPEN for S1/S2 only), STATUS. **Not executed: any signal route.** HENRY's cross-asset signature (rates up, SPX down, HY wider, KRE down, same session) reads loop-shaped on 9/28, 9/29 and 9/30 on my reading of his letter against dated bars, though that is not HENRY's grade. Breakevens are flat (2.34→2.36), which is ordinary-shaped. VIOLET's vol clause is nowhere near firing (VIX3M/VIX 1.12, VVIX 89.48).

⚠️ **Your call, not acted on:** my outbox rule says a resolving prediction is a signal for WALTER. `LIQ-07` is half-resolved. **My recommendation is to route at the S1/S2 verdict (10/15–10/16), not now.** Route now only if you want HENRY and VIOLET reading their legs against the 9/30 trigger date in the meantime.

⚠️ **Letter gap, declared and not rewritten mid-window:** the "±10 published sessions" count names no calendar. On the ICE calendar the 10th session is 10/14; on the SOFR calendar (no 10/12 Columbus Day print) it is 10/15. This matters only if a funding leg first reads on 10/15; if one does, I record both readings.

## Inbox drained: 2 → 0 (logged in `board_log.tsv`, `git mv`'d to `processed/`); `inbox/WALTER/`: 0 unconsumed

| Item | Disposition |
|---|---|
| VULCAN MU FQ4 graded, S2 3→2 | **noted.** INFO; the memory-equity re-arm row I was named on closed UNGRADEABLE and moot. None of my AI-credit spread tells key on memory equity. |
| WALTER R3 WATCH_FOR verdicts (DOCKET L565) | **acted.** Answered by name: `PROME/inbox/2026-10-01_from-LIQUID_R3-watch-for-adopt-decline.md`. I accept both rejections and contest no classification. **Clean set of 7 to land:** `junk bond spreads widen` · `high-yield spreads widen` · `repo rate spike` · `standing repo facility` · `money market fund breaks buck` · `Treasury auction fail` · `reserves scarce`. |

## DOCKET L493 owed set, and WQ-301 (b)

- **L493:** ① the `hy_oas_watch.py` stale-arbiter repair was DONE and INDEPENDENTLY VERIFIED on 9/29 (`917c0c087`). ② DONE. ④ DONE. ③ was answered today (above). **Still owed, not touched this session:** four pre-existing `hy_oas_watch.py` defects from the ① record (the SIGNALS row truncates at 240 chars and drops "do NOT retire the thesis" · a mixed fire's SIGNALS row carries only the escalation text · the late-kill headline puts today's level next to "kill level met" · AC1 is a banned-word list). The tool is an unattended Will-facing instrument, so WQ-229 applies: acceptance conditions first, then an independent reader. That did not fit behind the time-sensitive grade. The desktop timer is live (next run 13:00 ET today).
- **WQ-301 (b), due to Will Fri 10/02: the validation is where it stood on 9/28 and has not moved.** The ISDA engine (QuantLib) and my converter agree to ≤0.4bp on the same curve, and ±25bp holds at 9/23–24. **The official ISDA curve is still not retrieved:** the replacement host (rfr.spglobal.com) needs a registered login, which is an external sign-up in Will's hands. A reachability probe today returned only a JS shell and no curve. **The 7/06 anchor's sign is still INFERRED, not observed.** Under the positive sign the lines are >697 / >737; under the negative sign they are >520 / >649. **The letter's 452 anchor governs until Will rules, and the gate is FIRED 2-of-2 on every basis.** No new evidence for Will beyond 9/28's.

## COMPLETION — LIQUID — 2026-10-01
STATUS: ✅ DONE
CHANGED: AGENTS/LIQUID/{analysis/2026-10-01_9-30-cell-grades-LIQ-07-trigger.md (new), STATUS.md, workbook/PREDICTIONS.tsv, board_log.tsv, inbox/ → processed/ ×2}, PROME/inbox/2026-10-01_from-LIQUID_R3-watch-for-adopt-decline.md, this memo
RESULT: 9/30 cell graded on first-published FRED. LIQ-07 TRIGGER FIRED 3 of 3 (B +36, CCC +115 over 15 sessions); S3/S4 eliminated, S1/S2 open with no funding leg read yet. HY 312: 8bp under >320, 52bp above the REKILL line (0-of-2). 072 not fired (IG 84, basis 228). R3 set answered by name (7 adopted). Inbox 2 → 0.
GAPS: The 4 residual hy_oas_watch.py defects (L493 ① record) remain owed. The ISDA official curve was not retrieved (login wall). LIQ-07 letter names no session calendar (10/14 vs 10/15).
WILL_NEEDS: None new. WQ-301 (b) stands as of 9/28: rule the re-base, or register at rfr.spglobal.com so the official curve can be pulled.
FOLLOW-UP: PROME decides whether to route the LIQ-07 trigger now or at the verdict (rec: at the verdict) and lands the R3 set. LIQUID reads the S1/S2 legs: SRF 10/1 (pub 10/2) and 10/2 (pub 10/5), z/079 from 10/5, verdict 10/15–10/16; Q3 persistence verdict 10/8.
