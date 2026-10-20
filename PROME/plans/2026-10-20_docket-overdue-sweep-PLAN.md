# PLAN — DOCKET overdue sweep (2026-10-20)

**Authority:** Will 2026-10-20 13:45 ET, verbatim *"Yes I want all of these fixed"*, on PROME's finding #2: the calendar is mostly overdue backlog. **Status: PLAN, awaiting one independent plan read** (`PROME/CLAUDE.md` § Session Process Controls: a broad batch gets a pre-edit cold read; PROME's two-correction stop also tripped on `prome_gate.py` today). Already done without the plan, each verified at its record: L686/L705/L706/L756 (C5 rows, commit 0112a9694) and L427/L451/L725/L599 (finished work).

**Invariant:** no row is called done unless its completion is verified at the artifact. A re-date is never a resolution. Every edit prepends a dated token and keeps the prior cell verbatim (DOCKET's own convention). DOCKET.tsv has no CRLF; the edit preserves that.

## A. PROME-owned process/tooling rows — 52 rows → RE-DATE to Sun 2026-10-25 under L600
L600 (WQ-299, Will-ruled) already makes the PROME process backlog ONE dated obligation for the 10/25 review, where Will approves consolidation candidate by candidate. Proposed token: `PENDING · RE-DATED <old>→2026-10-25 (L600 WQ-299 process-backlog review; 10/20 overdue sweep, Will 13:45 ET)`. Exception: any row in this list that the reader finds already finished at its artifact is RESOLVED instead, with the evidence.

- L350 (09-19, PROME) — FIVE DESKS HAVE A BOOT READ OVER BUDGET — the first fleet-wide measurement the READS/read_cap work has made p
- L358 (09-19, PROME) — SPINE AUDIT #13 MINOR RESIDUE — carried, not fixed, so it does not disappear under "17 blocking repaired." Th
- L361 (09-19, PROME) — A CLOSEOUT SHOULD RE-MEASURE EVERY FIGURE IT WRITES ABOUT ITS OWN ARTIFACTS — the dominant defect class acros
- L362 (09-19, PROME) — A SHUTDOWN THAT CAN ONLY BE APPROVED IN PROSE IS A CONTROL WITH NO CARRIER — raised by ARGUS about its own sh
- L364 (09-19, PROME) — THE THIRD OBLIGATION CATEGORY IS MISSING FROM THE INSTALLED RULE — "must handle or assign this obligation" is
- L367 (09-19, PROME) — ARGUS SCOPE — ONE DESIGN QUESTION + FOUR FAIL-CLOSED RESIDUE ITEMS from the round-3 independent review (2026-
- L368 (09-19, PROME) — `spawn_list.py` SUPPRESSED ALL THREE DOCKET ROWS DUE TODAY — third instance of one class. 2026-09-13: L248 (C
- L370 (09-19, PROME) — THE `DOCKET lands-today dispositioned` BLOCKING GATE CAN BE CLEARED BY APPENDING ANY TEXT, AND IT IS INVERTED
- L378 (09-19, PROME) — MECHANIZE THE SPAWN-CLOSEOUT ASK (WQ-249, Will-ruled 2026-09-14 15:36 ET, verbatim "Just get those agents clos
- L392 (09-19, PROME) — CALIBRATE contract_probe STALE_S — the 900-second constant is uncalibrated and load-bearing when the MATCHED c
- L402 (09-19, PROME) — THE ARGUS `OWNED` LANE SAYS "PROME's OWN OUTPUT" BUT CLASSIFIES BY PATH PREFIX, SO OTHER SESSIONS' WORK LANDS
- L403 (09-19, PROME) — ARGUS ⚠️ RESIDUE FROM THE 2026-09-15 CLOSEOUT — SIX FLAGS ON PROME'S OWN LEDGER AND ARCHIVE HYGIENE, DECLARED
- L413 (09-19, PROME) — A DESK ALERT PRINTS A ROUTE PROME NEVER CAUSED — VIOLET's `cheap_tail.py` closes every OPEN alert with "Route
- L419 (10-09, PROME) — ROOT OUTPUT CANON operator-surface clause — TWO WORDING DEFECTS found by the THIRD read after root CLOSED for
- L423 (10-07, PROME) — FOURTH INDEPENDENT READ of the WILL_QUEUE-table parser repair chain (8130dae8d → 4c59c850b → the 9/18 13:1x th
- L429 (09-30, PROME) — L409 SCOPE WIDENED — THE CONTINUATION-TICKER DEFECT IS NOT ONLY DAY-CHANGES; IT REACHES LEVEL THRESHOLDS, AND
- L431 (09-25, PROME) — A METRIC-NAME SPLIT IN `PUBLISHED.tsv` ORPHANS THE NEW VALUE AND LEAVES THE SUPERSEDED ONE READING CURRENT —
- L441 (09-30, PROME) — FLEET SWEEP — WHICH DERIVED METRICS ARE GRADED AGAINST A HARDCODED BASELINE, NORM OR DENOMINATOR? Raised by H
- L442 (09-25, PROME) — TWO CODE PATHS THAT AGREE IN EVERY NORMAL RUN AND DIVERGE EXACTLY AT THE MOMENT OF FAILURE ARE NOT REDUNDANCY
- L444 (09-28, PROME) — CLASSIFY `PROME/state/ORCH_LOG.tsv` SPAWNS AS CAP-BEARING vs CAP-EXEMPT — the `session_id` field ALREADY EXIS
- L450 (09-28, PROME) — THE BURIED-STATE-TOKEN GUARD PASSES A DEFECT OF EXACTLY THE CLASS IT WAS BUILT FOR — and 'falsified before be
- L458 (09-25, PROME) — CLOSEOUT STEP 12 STRANDS A FILE AND THE SWITCHING CHECKLIST SAYS NOTHING MAY BE STRANDED — two PROME canon st
- L459 (10-07, PROME) — L446 RESIDUE — `spawn_list.py` cadence-reader defects the independent reader found, all FAIL-SAFE (none moves
- L465 (09-28, PROME) — WQ-256 (a) SL-5 CANON AMENDMENT — draft the EXACT clause: a quantifier word in a gate letter ('sustained' · 'r
- L467 (10-07, PROME) — FLG RENT-FREEZE INTAKE TERM — RETIRE OR DROP TO ROUTINE: the `flg-rent-freeze-litigation` Google News query +
- L557 (10-12, PROME) — L462 RESIDUAL REPAIRS EB1–EB3 (from CATO's Will-authorized independent review 2026-09-29 19:42 ET, `AGENTS/CAT
- L591 (10-12, PROME) — ARGUS AUDIT-PERIMETER ROW FOR `USER.md` — OWED since 2026-09-30 (prome-2a found `USER.md` matches no `PROME/st
- L604 (10-05, PROME) — SPAWN SLATE B1/B2 — DAEDALUS's standards-slate reader findings (10/3): B1 the slate's top summary overclaims o
- L607 (10-09, PROME) — WQ-367 ENCODE — the five closeout-process changes RULED APPROVE (Will 10/3 21:09 ET by Deck tap): P1b · P2 · P
- L610 (10-09, PROME) — RESEARCH-INTAKE edgar_8k ENTITY-CLASS MIS-TAG — a megacap filed as `entity_class: "other"`: Micron's Q4 FY26 8
- L628 (10-13, PROME) — PROME R1 SLOT — APPLY DAEDALUS's summons fix (L548 patch, AGENTS/DAEDALUS/builds/summons_fix_2026-10-08/; inde
- L629 (10-12, PROME) — PROME TEST DEFECT — `test_no_bare_check_call_sites_remain` (prome_gate test suite) FAILS on live HEAD (DAEDALU
- L634 (10-12, PROME) — CONFIG MIRROR DRIFT — `FORGE/tools/news-sweep/config.py` WATCH_FOR no longer matches the live collector's `~/R
- L640 (10-12, PROME) — PROME PROCESS SLOT — the receipt command changed (WQ-399, DAEDALUS 112ccb908): fix PROME's own stale field-les
- L642 (10-12, PROME) — `FORGE/tools/market-data/fetch.py` — CONTINUOUS-CONTRACT LABEL DEFECT, second instance today: `fetch.py price
- L644 (10-12, PROME) — WQ-369 NARROW C8 — CHARTER ENCODE OWED (Will 10/4 ~20:00 ET to WALTER, verbatim "WQ-369 yes"; committed relay
- L645 (10-12, PROME) — `PROME/SYSTEM.md` MIRROR-MAP WALK OWED AFTER WQ-385 (root runtime amendment 10/5, 88417ced3): Mirror-Map row 4
- L646 (10-15, PROME) — `FORGE/STATUS.md` WRITE MODE — the mirror re-breaches its read cap every reconcile week (10/01 rotation → 100
- L647 (10-10, PROME) — WQ-371 ENCODE — `PROME/CLAUDE.md` CONSOLIDATION C2 · C3 · C4 (Will 2026-10-08 20:09 ET "WQ-371 approve"; the f
- L648 (10-13, PROME) — L546 RIDER — THE FLOAT-TIE CLASS REACHES THREE SIBLING COMPARISONS THE classify() REPAIR DOES NOT COVER (inde
- L655 (10-12, PROME) — PROME BLIND COUNTERPART READ OF DAEDALUS's STARTUP PROCESS (DAEDALUS packet 6d8ae5e5c, Will-requested inward D
- L664 (10-12, PROME) — PROME BLIND COUNTERPART READ OF DAEDALUS's CLOSEOUT at 718390f3b (DAEDALUS packet 2026-10-09_from-DAEDALUS_clo
- L675 (10-12, PROME) — PROME PROCESS BACKLOG FROM THE 10/10 CHAIN REVIEW (WALTER · CATO · PROME; Will 13:45 ET: "Proceed with the sch
- L676 (10-14, PROME) — JANUS BUILD — the boot triage clerk Will approved (WQ-416, 10/10 15:01 ET; record PROME/proposals/2026-10-10_t
- L679 (10-12, PROME) — LEGACY DONE-ROW RECORD SWEEP (26 rows, WQ-369…WQ-407, carrying 43 advisory flags) — rides with spine audit #16
- L696 (10-13, PROME) — COR-20261012-25 historical consumer review: HEARTBEAT_COLD.md former September2 CARL paragraph calls97.4bp a c
- L697 (10-13, PROME) — Reconcile STUE ES-01/04/06 owner identity and authorized assignment: WQ413 never covered STUE.
- L698 (10-19, PROME) — FORGE native-price precision — MIDAS maintenance referral: price_history rounds Close to2dp; prepare additive
- L702 (10-15, PROME) — Closeout display applicability — prepare implementation from CATO PC14-1 bounded proposal; bind current facts
- L710 (10-15, PROME) — PROME DEDICATED MAINTENANCE SESSION (WQ-430 RULED 10/14 21:32 ET) — the one-process-change ceiling lifted for
- L728 (10-19, PROME) — WQ-187 RECEIPT CHECK — Will tapped DONE (hands complete) on the Telegram morning-digest steps 2026-10-15 12:27
- L744 (10-19, PROME) — HANDOFF DATED-ENTRY TRIM — plan item 4 (`PROME/plans/2026-10-16_boot-closeout-cost-PLAN.md`): each dated HANDO

## B. Desk-owned rows — 18 rows → consumer read at the owner's artifact, then resolve or re-date
For each row: read the owner's latest return (the spawn slate's RETURN FOUND pointers cover most). If the return answers the row, RESOLVED with the commit. If it doesn't, RE-DATED to the owner's next likely session, with a packet to the owner naming the missing leg. Never graded on the owner's behalf. Special case: **L384** is condition-keyed, so its date cell is vestigial by its own text. Re-key it to an undated session key (`on-next-matched-basis-fire-time`) rather than re-date it.

- L40 (10-12, DAEDALUS/NEXUS) — Amendment-12 watch grades (the format-vs-recogniser discriminator's own test): am.11 shipped 8/7 (NEXUS self-r
- L176 (09-30, MIDAS/BRENT/SAM/ORACLE) — Forum-4 WITHDRAWAL TESTS grading riders (Will-ruled batch 8/11): WT-1 (Q-C shared-purpose; size-knob axis, MID
- L263 (09-18, DAEDALUS) — WQ-171 ③ COMMISSION (Will 9/3 21:54 'Approve WQ-171 ① and ②' → ③ as a DOCKET row per PROME's rec): DAEDALUS bl
- L321 (10-02, HAWK) — HAW-19 capacity-only SUCCESSOR registered (WQ-212 RULED 9/10: HAW-19 resolves 9/30 as a DEFECTIVE INSTRUMENT,
- L334 (10-15, WALTER) — INFO-BACKLOG PREDICTIVE STUDY — does a desk's UNCONSUMED info backlog PREDICT anything? WALTER's design, PROME
- L384 (09-22, HENRY) — RE-KEYED 2026-09-14 16:09 FROM A DATE TO A CONDITION — PROME REGISTERED THIS ROW DATE-KEYED AND THAT IS THE D
- L464 (09-25, VIOLET) — WQ-259 EXECUTION — VIOLET refreshes + republishes its two Will-facing pages (vol cheat-sheet · operating pictu
- L490 (10-09, DAEDALUS) — DAEDALUS OWED SET carried from the 9/25 L290 spawn (DAEDALUS cadence WEEKLY declared 9/25 ⇒ this is its next w
- L499 (10-12, DAEDALUS) — CANON ENCODE of the WQ-298 STANDING RULE (Will 9/25): "a desk that finds a measurement unreachable files it on
- L517 (09-29, WAL) — PLAZA CONTINENTAL (3700 Inland Empire Blvd, Ontario CA) — single-asset Ch.11 8:26-bk-10986-MH, STIPULATION HEA
- L526 (10-12, DAEDALUS) — BRENT AUTONOMOUS-ROUTINE FALSE-FORK — FIFTH RECURRENCE (9/11 · 9/18 · 9/21 · 9/25 · 9/28): the scheduled cont
- L530 (10-09, DAEDALUS) — `read_cap_check.py` PERIMETER GAP — a boot-read-WHOLE surface at 84% of budget is INVISIBLE to the gate becau
- L548 (10-07, DAEDALUS) — `prome_gate.check_desk_catalyst_summons` HIDES THE ROWS IT EXISTS TO SHOW — flags sort by date ASCENDING and
- L568 (10-09, LIQUID) — LIQUID DOLLAR SWAP-LINE INSTRUMENT (`AGENTS/LIQUID/scripts/usd_swapline.py`) — WITHHELD FROM USE; FIX PASS +
- L639 (10-13, NEXUS) — S1 SPECIFIED BUILD — DESIGN (re-opened per WQ-191's pre-registered condition; L304 graded YES 2026-10-08 on tw
- L657 (10-14, RED) — BRK-26 'FIRST FILING' SPEC QUESTION (BROCK 10/9, memo PROME/inbox/processed/2026-10-09_from-BROCK_kellermeyer-
- L667 (10-14, VIOLET) — VIOLET — RED-FT-10 COUNT ON THE CBOE SKEW BARS 10/12 · 10/13 · 10/14, graded the evening of 10/14 at CBOE's pu
- L704 (10-19, GIBBS) — GIBBS FIRST LIVE SESSION (PROME spawn, Tier 1 under WQ-426) — retrospective read of the firms already printed

## C. Will-owned — 1 row(s)
- L597 (10-09, Will) — DBPR GovQA PORTAL CHECK — status of CORAL's Step-1 records request (request W212505-100226, from Will's activa
Proposed: move to WILL_QUEUE as a hands item (check the DBPR portal), with the DOCKET row RE-DATED to the next check date Will names.

## Acceptance
1. After execution, the calendar's OVERDUE line counts only rows whose date is before today because the work is genuinely late, not stale bookkeeping.
2. `prome_gate.py` DOCKET checks stay green: overdue-unannotated and buried-token.
3. `spawn_list.py` wakes no desk on a row this sweep closed.
4. No row was resolved without a cited artifact.
