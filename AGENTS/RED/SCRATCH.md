# RED SCRATCH — Canonical Session Handoff

<!-- TEMPLATE — rewrite in place at W5 every session; git history versions this file.
     Section order (headings written WITHOUT the "##" here ON PURPOSE — see below):
       1. CHANGES SINCE   — what moved while RED was offline
       2. WHAT I DID
       3. NEXT SESSION    — dated, priority-ordered
       4. OPEN THREADS
       5. PENDING WILL-DECISIONS
       6. GIT STATE       — one line

     !! DO NOT restore the "##" prefixes to the list above. !!
     They were verbatim copies of the live body headings until 2026-08-12, which made every
     heading-anchored edit AMBIGUOUS: a scripted insert anchored on "## OPEN THREADS" matched
     THIS BLOCK first and wrote the content inside the comment. It happened three times on
     8/12; one instance was committed and pushed (4b3bb1b55) with two carry-forward threads
     rendering as nothing while present in the file.
     No check can see that class — claim_check, ledger_staleness, orphan_check and a content
     grep all PASS on a file whose content is commented out. (ML-RED-155)

     If you script an edit to this file: anchor on a body-unique string, and verify placement
     by heading OFFSET (which occurrence), never by presence.
-->

**🆕 S40 (2026-09-02, boot ~22:48 ET on PROME wave-4 spawn / close ~23:2x ET — stamps from `date`) — TWO GRADING BASES DECLARED (FT-10 under WQ-162, FT-11 v1.1 on BOND's call), and a TIE-SET DEFECT found in RED's own base rate seven days from go-live. NO WEIGHT MOVED: HOLD 69 / net-bear 60 (15th consecutive session). No threshold set or moved; no capital path.**

## CHANGES SINCE (S39 close ~11:0x ET → this boot)

- **WQ-162 RULED** (Will 21:29, verbatim *"Approve WQ-162 with your recs"*): **a grade on an unnamed basis is NO-VERDICT.** Every letter must name series · unit+conversion · vintage (as-first-published) · operator/boundary · consecutiveness · reset, for **every** published observation the grade reads. FT-10 named as an instance.
- **VIOLET `495437ace`:** the 8/28 `^SKEW` bar is **absent** from yfinance; CBOE carries **149.77**. FT-10's closest approach is 0.23 below, not 0.77. The same absent bar flipped HENRY's cross-back grade by **0.04**.
- **CREED `9dce322ba`:** a strict inequality against a fixed-precision series has a **non-empty tie set**, undeclared anywhere in registration canon. Routed to DAEDALUS.
- **BOND** adopted all three FT-11 v1.1 menu items on-menu (cut −4bp · FLOW-alternative · **second precondition path YES**) with one ask: print the non-rally-window partition if cheap before 9/9.
- **CORAL** confirmed both FL rows, re-dated to 11/15; separately published (`53dc298b6`) that **FMHPI excludes condos by construction**.
- **NEXUS:** RED's brief carried the wrong Jackson Hole date (`~8/21`); NEXUS carried it too.
- **Tape (boot.py, live):** SKEW **144.12** [9/2] · HY **265** (FT-12 5bps, widening away) · CCC **1,049** · VIX **15.20** · USDJPY **157.82** · Brent **95.43** (WL-11 un-fired, 0.43 above).

## WHAT I DID

1. **FT-10 GRADING BASIS DECLARED (WQ-162) and the row RE-GRADED.** Old letter audited against the six-item checklist → **silent on four** (unit, vintage, tie, missing-bar; reset lived only in MEMORY) ⇒ prior grades were NO-VERDICT. New basis, 8 clauses, on **CBOE `SKEW_History.csv` = publisher of record**; Yahoo demoted to a **provisional same-day mirror that cannot complete a grade**. **VERIFIED first-hand at the publisher** (HTTP 200, 202,828 B, 9,219 rows, `08/28/2026,149.770000`; precision exactly 2dp on 9,219/9,219 rows). **GRADE: ARMED — NOT FIRED, s=0-of-4; 144.12 [9/2] = 5.88 below; closest approach 149.77 [8/28] = 0.23 below.** `0.77` **WITHDRAWN**. → `research/2026-09-02_FT10_GRADING_BASIS_DECLARED.md`, ML-RED-209.
2. **🆕 Went past VIOLET's packet:** widened their 10-session check to **253 sessions** → the mirror has **TWO defect modes** (omitted 8/28 **and** a value disagreement 2025-12-24, CBOE 161.30 vs 160.53) = **0.79%/session**. Their proposed completeness-check hardening catches one and is **blind to the other** — the argument for replacing rather than hardening. ML-RED-210.
3. **FT-11 v1.1 ENCODED as ONE letter both desks carry.** BOND's three calls adopted verbatim + scope fence + the no-weight-moves rule. **Answered BOND's ask: the partition does NOT transfer** — 2nd-path n=51 resolves **17.6%** (FLOW 5 / FUND 4 / NV 42) vs **95.0%** in rally windows; both branches key on a 2Y move non-rally windows lack (FUND 8% vs 89%; median |Δ5 2Y| 7bp vs 12bp) ⇒ **butterfly-only FLOW FLAG**. Adopted anyway: **v1.0 slept through the entire 8/19–8/24 step-up cluster (4 windows); the 2nd path wakes on all four.** → `research/2026-09-02_FT11_v1.1_second_path_partition_AND_tie_set.md`.
4. **🔴 FOUND A DEFECT IN MY OWN MORNING NUMBER.** The registered `≤ −4bp` base rate (5.0%/3.8%, LR≈34) is the **STRICT** cut `< −4`. On the letter as written **and as BOND adopted it**, the leg fires **8.5%/6.2%, LR≈21 — 1.7×.** The statistic is integer bp; **the tie atom at exactly −4 holds 23 of 661 windows = 3.5%, more mass than the whole tail beyond it ⇒ 41% of the fires.** Declared + corrected pre-go-live. **CREED's finding validated n=2 desks in 4 hours; RED's instance the larger.** Second RED instance same pass: **FT-10's realised tie set is on the EXIT leg** (`{140.00}` ×2: 2016-01-04, 2022-03-29) while the fire leg's `{150.00}` is empty in 9,219 obs. ML-RED-211.
5. **CORAL's FL rows encoded verbatim** — KB-046/052 `Stale_By` → **2026-11-15**; the owner's closed-quarter caveat carried on **both** rows (*a benign Q2 does not shrink the 30% winter tail*); the 5-way convergence recorded as **raising** the unanimity flag, not lowering it. **FMHPI exposure CHECKED AND ABSENT — VERIFIED** (owner-declared path = each row's own Source cell, plus a desk-wide grep; zero FMHPI-based condo claims on any live RED surface).
6. **Jackson Hole corrected and killed on sight**, and **VERIFIED AT PRIMARY: `kansascityfed.org` returns 200** (Aug 27–29; theme *Financial Innovation*). **The fleet's 403 premise is false** — `[[finding_unfetched_is_not_unavailable]]`, RED's own canon, second instance. Keynote day 8/28 stays **INFERRED**. ML-RED-212.
7. **`NEXUS_BRIEF.md` rebuilt + rotated for the READER's cap** (READ_CAP rule 15): the wrong JH row sat in a FORWARD CATALYSTS table where **7 of 12 rows were resolved August events** — whole table rebuilt; NEXT DECISION POINT rewritten; six dated FOLD blocks moved **verbatim, crc-stamped**. **43,094 → 31,811 B (132% → 98%).** Also contested NEXUS's slate item 4 as invited (**de-duplicate the COUNT, never the INSTRUMENT** — FT-10 is the counter-example: redundancy is what found the defect).
8. **SAM rail:** armed read recorded **pre-print** on CHG-RED-047 with a pre-committed refusal. **RED does not grade SAM's letter** — SAM's grade is pre-registered NO-VERDICT (no 30Y leg).
9. **Inbox drained 5/5; `inbox/WALTER/` VERIFIED EMPTY at the path** (0 files top-level, `processed/` 118). **BOARD: 0 signals dated 9/2** (VERIFIED by count) — nothing undispositioned. **7 board_log rows.** 6 packets out (carve-out ①): VIOLET · HENRY · BOND · CREED · NEXUS · PROME memo.

## NEXT SESSION (dated, priority-ordered)

1. **✅ DONE IN-SESSION (S40 addendum, 9/3 ~07:2x ET — the session crossed midnight and the auction had already printed): 30Y JGB recorded as a dated observation.** cover **3.79** (prev 3.86, **12-mo avg 3.52**), tail **0.28** (prev 0.21), yield **4.080%**. ⚠️ **INFERRED/RELAYED — MOF primary NOT reached** (2 guessed paths 404; explicitly NOT called a block). **Two-sided print; RED's own orderly/disorderly branches both fail to fit — ML-213.** CH-009/CH-012 unmoved; SAM packeted. **🔴 STILL OWED NEXT BOOT: (i) pull the MOF primary — find the current path and upgrade INFERRED → VERIFIED; (ii) disposition CHG-RED-047 at W2 on SAM's write-back; (iii) re-spec RED's armed-read template to name the BASELINE of each branch.**
2. **🟠 Fri 9/4 08:30 ET — August NFP.** Does **−23K** survive revision; labor force. **Independence discount (ML-133): JOLTS hires-rate 3.2 is ratio-estimated to CES — one read, not two.**
3. **🔴 9/4–9/11 re-spec window, and it now carries a deadline-bound item:**
   - **⚠️ The FT-11 v1.0 partition reconciliation MUST land before Wed 9/9.** Registered 4/68/8 vs non-strict 5/71/4 vs strict 4/60/16; **cause UNKNOWN**. Candidate: the v1.0 legs' own boundary atoms (`≤ −3`, `≤ 4`, `≤ 6`), and/or the registered partition being a carry from the n=657 registration rather than a recomputation.
   - **⚠️ Wiring gap: `boot.py` still evaluates FT-10 off the DISQUALIFIED mirror.** Correct tonight only because the two series agree. Point it at the CBOE CSV **or** label its output PROVISIONAL. `[[finding_guard_correctness_and_wiring_are_independent]]`.
   - **🆕 Registry-wide tie-set audit** — every RED row with a `>`/`<`/`≥`/`≤` band over a rounded or integer series: census the **atom size** at the boundary, not just the tail beyond it. **Both ends of every two-way trigger.**
   - **🆕 NEXUS's one-sided-conjunction shape, applied to RED** (easy leg near, hard leg receding — FT-10 is exactly that: 140 modal, 150 at 5.88 and moving away). Credited to NEXUS.
   - Carried: FT-04/07/08 re-spec · full-registry ML-203 audit · registry prose split · VX 9/12 re-review.
4. **🟠 Wed 9/9 — FT-11 goes LIVE** + stepped-up buybacks begin. **BOND routes the F2 read per operation, never batched.** Also FT-01 6/15-fire outcome grade + FT-06 8/11-fire grade at 20 obs.
5. **🟡 9/8–9/10 — WQ-157 leg ①: the BOND kill leg stays DUAL-PRINTED; a bare I′ fire moves nothing.**
6. **🔴 Fri 9/11 08:30 ET — August CPI** (FT-08 manual: core 3-mo annualized ≥3.0). **CHG-028: 9/11 is a pre-registered NON-EVENT for oil→core.**
7. **🟡 Tue 9/15 — CHG-044 (BROCK) + CHG-049 (CARL) re-reviews.** 9/10 CARL V2 / BCRED SC TO-I (BROCK owns).
8. **📏 `STATUS.md` is at 98.6% of the read-cap budget (32,087 B) — this is the next rotation and it should not be deferred twice.**
9. **Daily monitors:** FT-12 HY vs 260 (265, widening away) · **FT-10 ^SKEW vs 150 on the CBOE basis** (144.12, 5.88, s=0) · CCC 1,049 · WL-07 USDJPY vs 160 · WL-11 Brent <95 (95.43, un-fired).

## OPEN THREADS

- **FT-11 v1.0 partition reconciliation — UNRESOLVED, hard-dated to 9/9.** Disclosed to BOND rather than papered over; direction of BOND's design call unaffected.
- **BOND may re-decide on the corrected leg-(iv) numbers.** The packet says so explicitly and there is time. If BOND holds, nothing further is owed; if BOND moves, the menu re-runs.
- **The base-rate artifact class.** S39b recorded its construction as *"code in this session's transcript"* — **not registered, remembered.** Standing rule adopted: every RED base-rate artifact carries its comparison operators explicitly and its construction in the file. **Retro-sweep of prior base-rate files not yet run** (`[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]`).
- **Fleet consumers of the withdrawn FT-10 margin** — `HEARTBEAT.md`, `WALTER/REGISTRY.tsv`, `WALTER/STATUS.md`, `HENRY/STATUS.md`. HENRY packeted directly; HEARTBEAT + WALTER routed to PROME (OUTBOX-036 item 2). **RED does not edit them.**
- **CREED's tie-set case at DAEDALUS** — RED contributed three proposed canon clauses and n=2 evidence. Not RED's to rule.
- **CRL-05 basis exposure** (CARL's disclosure, >13.74% GFC line is Equifax-3.0-era) — unchanged, not RED's to fix.
- **Root carve-out ④ vs runbook §successor scope** — still Will-gated (DAEDALUS 9/1). Unchanged.
- **ML-185 apparatus self-challenge obligation:** CHG-051 live. ⚠️ **Note honestly: tonight's two best apparatus findings (the omitted bar, the tie set) both came from OUTSIDE — VIOLET and CREED.** The self-attack blind spot ML-185 describes is still live and unfixed by more care.
- `outbox/kernel/submissions/CMD-01a06273….json` is **IMMUTABLE** — never edit/move/delete; not a boot read.

## PENDING WILL-DECISIONS

- **None blocking.**

## GIT STATE (one line)

On master; S40 committed path-scoped (`AGENTS/RED/` + five carve-out ① packets into VIOLET/HENRY/BOND/CREED/NEXUS inboxes + the PROME memo copy); auto-push via `scripts/safe-push.sh`; five other desks committing concurrently, so a non-ff is routine — root Git Protocol session-end step 3, never force.

---

*S39 block archived in git history; durable outcomes in the registry, workbook, `thesis/CHANGELOG.md` S39/S40 entries and `MAINTENANCE.md`.*
