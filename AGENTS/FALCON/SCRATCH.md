# FALCON SCRATCH — 2026-09-17

## CURRENT MARKS
B/C/D 3/22/75 retained; convergence 43/50 retained. FAL-05 OPEN 55%, resolves 2026-10-07. Sep 17–18 registered review-window graded 2026-09-17: no route fires. GATE-FALCON-001 legs 1/3 fired-and-holding, leg 2 UNGRADED-ON-BASIS (DAEDALUS 9/17 gate-basis-sweep #1). No settle-count clock live; step 12b is a no-op.

## CHANGES SINCE LAST SESSION
- FAL-05 Sep 17–18 review-window graded UNFIRED across all three routes. Full grade: reports/2026-09-17_fal05-review-window-grade.md.
- SIG-W-20260917-001 (Kpler 9/17): duration ≥7d clears today marginally; Kpler 4.5 mb/d halted is vendor ESTIMATE, does not clear the letter's operator/state/wire-primary attribution — route (b) volume limb NOT ESTABLISHED. Route (a) ⛔ kill-on-sight guard against "de facto FM" holds.
- SIG-W-20260917-007 (Reuters 9/16 STS-off-Sohar): Aramco offering Arab Light/Medium/Heavy to Asian term buyers via STS off Sohar; Ras Tanura+Juaymah doubled to ~4 mb/d, 4 VLCCs/8M bbl at RT on 9/16. This is a HAND-OFF, not a route — shuttles STILL transit Hormuz. Anti-FM read strengthens; no new registered watch this session.
- DAEDALUS PR#6 (9/17): FAL-05 needs a dated search window by 2026-09-24. Design task; not addressed.
- DAEDALUS gate-basis-sweep #1 (9/17): GATE-FALCON-001 leg 2 has no magnitude; owed by 2026-09-30. Pre-9/4 letter — annotated, not re-graded.

## WHAT I DID THIS SESSION
- Spawned by PROME (prome-89, DESKTOP-BC6EF81) at ~19:57 ET for WQ-184 L0 due-row grading; Opus.
- Explicitly read root CLAUDE (auto-injected), USER, FALCON CLAUDE, STATUS, SCRATCH, MEMORY (incl. 🔴 CARRIED OPEN), FAL-05 PREDICTIONS row, two WALTER SIGs, two DAEDALUS packets, two HAWK 9/16 packets.
- Graded FAL-05 against the CANONICAL row letter (thesis/PREDICTIONS.tsv:28), not against WALTER's summary. Route-by-route rationale in reports/2026-09-17_fal05-review-window-grade.md.
- Updated STATUS.md: header, marks table row for FAL-05, Pending Evidence rows for routes (b)/(c), added rows for both DAEDALUS asks, BOTTOM LINE.
- Logged board_log rows for SIG-W-20260917-001 (acted) and SIG-W-20260917-007 (acted).
- Moved processed WALTER packets to inbox/WALTER/processed/.
- Delivered completion memo to outbox/to-PROME/ and returned COMPLETION block to spawner.

## NEXT SESSION (dated, future-verifiable)
1. **2026-09-24 (DAEDALUS PR#6 deadline):** author a DATED SEARCH WINDOW for FAL-05 — the precondition half of a negative-resolution profile. Where and how to look for a firing event between now and 2026-10-07, in checkable form.
2. **2026-09-30 (DAEDALUS gate-basis-sweep #1 deadline):** give GATE-FALCON-001 leg 2 a magnitude + reference window in the form "≥X% below the trailing-7d mean of TankerMap Bab transits, window W, on ≥2 prints" — OR declare UNGRADEABLE-until-banded with a date. Pre-9/4 letter is annotated, never re-graded.
3. **2026-10-07:** FAL-05 window close + resolution grade. Kharg-leg resolvability guard must be closed on dark-immune routes only (kharg_loadings_watch.py may never be used to close it).
4. **Continuous through window:** watch for the SINGLE operator/state/wire-primary offline-capacity print that would fire route (b) — the row is ONE STATEMENT AWAY. Same for a SECOND independent dark-fleet-capable Yanbu route (TankerTrackers/Windward/direct satellite) that would fire route (c).

## OPEN THREADS / WATCHES
- **🔴 CARRIED OPEN (from MEMORY.md, re-read at every boot until closed):**
  - **KB-168 Yanbu terminus proxy** — unbuilt, spec'd 2026-09-10, due 2026-09-14, NOT DELIVERED. Binding gap on FAL-05 route (b). Highest-value acquisition on this desk alongside a standing Iranian-export series.
  - **WQ-230 WARRISK** — access decision owed by Will; six documented pulls all SEARCH-NOT-FOUND; 5 rows +42d expired. Do NOT re-run as a data task.
  - **April Petroline precedent correction consumed 2026-09-16.** Not restated.
- Previously approved: explicit sub-$80 duration, empty-series guard, archive-content guard, dated EXIT_PROTOCOL boot reader, vessel/casualty reconciliation. Approvals preserved.
- HAWK 9/16 asks: (a) working-cutoff 18:40 UTC vs actual 18:29 — my 9/16 committed report reads 18:28:37 UTC; the working-draft number was superseded, no correction needed. (b) reconcile ANALYSIS_2026-09-11.md with 9/11b correction — carried; ANALYSIS regeneration is a separate closeout task, not addressed this session.

## PREDICTIONS DUE / DECISIONS PENDING
No prediction resolved today. FAL-05 OPEN. No new trade or research approval requested. Route (a) SEARCH-NOT-FOUND at OilPrice/Argus/Reuters/Bloomberg/Kpler primaries — a wire-recovered absence, not a claim of absence at scope.

## MAIL STATE
Two WALTER SIGs (001 kpler, 007 sohar-STS) consumed, board-logged and git-mv'd to inbox/WALTER/processed/. Two DAEDALUS packets (PR#6, gate-basis-sweep #1) consumed and moved to inbox/processed/ with rationale in SCRATCH; deadlines carried to NEXT SESSION #1 and #2. Two HAWK packets (9/16) consumed and moved; (a) resolved by-artifact, (b) carried. Completion memo authored to outbox/to-PROME/ with COMPLETION block.

## PENDING PUSH / GIT
Session commit: FALCON-owned paths only (pathspec, no broad add). Auto-push via scripts/safe-push.sh; a non-ff abort recovers per root Git Protocol session-end step 3.
