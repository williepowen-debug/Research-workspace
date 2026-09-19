# OSPREY SCRATCH — 2026-09-18

## CURRENT MARKS
C1/C2/C3 **4/5/3**, band **~30%, 25–35% EST** — all UNCHANGED. Brent prices deferred to BRENT. **Nothing was self-ruled this session.** Full state + obligation register: STATUS.

## CHANGES SINCE LAST SESSION
- **Yaroslavl/YANOS 9/17 logged** — crude processing suspended, AVT-3 (40%) damaged, AVT-4 (33%) already down from 8/28. Three-leg confirmation. **Band unmoved: tempo, not barrels.**
- **`GATE-OSPREY-001` GRADED** (overdue since 9/15): LIVE — (a) NOT FIRED · (b) FIRED 7/24 · (c) NOT FIRED, on fresh 9/02→9/18 verification.
- **HAWK dyad boundary RULED** — concur on the axis + 3 amendments; `VX-HAWK-EURMIL-01` unblocked.
- **OWED-39 MEASURED, not ruled** — 4 scope instances, clock 8/30→17/30 across drawings, no drawing kills.
- ⛔ **A 9/8 CPC event was missing from `STRIKES.tsv` inside a window marked swept-complete.** Backfilled. See below.

## WHAT I DID THIS SESSION
Read `AGENTS/OSPREY/CLAUDE.md` explicitly first (spawned from PROME's cwd — own canon not auto-injected), then root CLAUDE/AGENTS/USER. Drained the **whole inbox**: HAWK boundary packet (ruled + answered), NEXUS R9 receipt (consumed, no reply needed), WALTER `SIG-W-20260917-006` (actioned: no-truce state logged, the "~4 M bpd" figure searched and marked UNVERIFIED). Two read-only research subagents on Opus. Wrote 12 KB rows (120–131), 2 STRIKES rows, 1 dated record, 3 outbound packets. No prices, no capital, no approvals changed, no threshold moved.

## ⛔ THE THING NEXT SESSION MUST NOT FORGET
**My founding calibration lesson (HAW-15) recurred.** A **2026-09-08 CPC Marine Terminal** event was absent from `STRIKES.tsv` although the header certified the window swept-complete through 9/16. **It was found by a subagent checking the gate — not by a sweep, not by me.** It had already caused me to compute and write a **false kill-clock alarm** (Channel 2 at 35/30 with both limbs satisfied); the backfill falsified it (true max 17/30, no kill). **Both the alarm and its refutation are preserved in order** in `domain/energy-strikes/OWED39_CHANNEL2_SCOPE_2026-09-18.md` §0.
⇒ **OWED-41 is the consequence: a backfill sweep of 9/01→9/16 is owed.** One accidental find is not a completeness check.

## NEXT SESSION
1. **Backfill sweep 9/01→9/16** against the feed for further holes (OWED-41 ①), **then sweep 9/17–18** — both deliberately left UNSWEPT; the mark was NOT advanced.
2. **Black Sea AWRP full 10-outlet canvass + TD6** — data clock 8/21, **28-day gap**, not canvassed this session. Declared, not hidden.
3. Run `scripts/strike_feed.py` — **not run this session.**
4. **OWED-42 basis pair:** July runs 3.6 (EA) vs 3.91 (Bloomberg) — same month, 0.31 gap into a runs-derived band. Flag to HAWK's basis-pair audit; **do not re-centre on either.**
5. Carried: decree authentication, Komysh vessel identity, unit restarts / pre-strike throughput (this is what blocks every incremental-barrels read).
6. 10/6 L309 feed acceptance test (recall + precision). OSP-06 dated search obligation 10/8–15.

## OPEN THREADS / WATCHES
All inherited OWED IDs preserved. **NEW: 41** (ledger completeness) and **42** (basis pair). **39 measured, still unruled — dated 9/19, Will's word.** 40 partially worked. 33 re-asked of BRENT with an either-answer-closes-it form. 8 not canvassed. 1/13/14/17/18/24/31/34/35/36 unchanged. **Nothing closed by silence.**

## PREDICTIONS DUE / DECISIONS PENDING
**OSP-06 OPEN 45%, deadline 10/15** — 3.54 to 9/13 does not fail it; VOID not armed (instrument still publishing). **No prediction due today.** No new trade proposal or approval request. **Live decision awaiting Will: the OWED-39 drawing (A/B/D), DOCKET L396, dated 9/19.**

## MAIL STATE
Inbox **fully drained**. Self-authored packets written AND committed (carve-out ①) to: **HAWK** (boundary ruling + 4 ledger corrections), **BRENT** (Yaroslavl confirmation + the not-barrels correction + OWED-33 re-ask), **PROME** (gate grade + OWED-39 + a correction owed to DOCKET L396's own text). NEXUS receipt consumed, no reply needed. WALTER lane actioned and logged. **Delivery is on commit; receiver integration UNKNOWN in every case.**

## PENDING PUSH / GIT
Own files + self-authored inbox packets committed with explicit pathspecs. **Other desks' work was dirty at boot (ZHAO, HANS) — not touched, not stashed, not pulled around.** Exact hashes in git history.
