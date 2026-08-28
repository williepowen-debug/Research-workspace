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

**🆕 S38g (2026-08-28, ~15:1x ET) — HOUSEKEEPING: P1 read-cap fold on STATUS + board_log. Both went 🔴 OVER-CAP → green (STATUS 🟡 rotate-tier under cap; board_log ✅). NO WEIGHT MOVED.**

- **STATUS folded 86,955 B → 29,689 B (66% reduction).** State line was 32,053 B alone (98% of cap on ONE row) — rewritten to day-summary only. S38 + S35 sections archived verbatim → `reports/2026-08-28_S35-S38_status_narrative_archive.md`. FALSIFICATION CRITERIA table compressed to firing rows + registry pointer. OPEN CHALLENGES compressed to headline row per CHG (canonical detail in workbook TSV). TOP PRIORITIES compressed to 7 standing items (live queue lives in SCRATCH). Full verbose forms preserved in the archive under STATUS SECTION SNAPSHOTS.
- **board_log rotated 100,890 B → 3,907 B.** 220 rows dated pre-2026-08-28 moved verbatim to `archive/board_log_pre-2026-08-28.tsv`. Live retains header + 12 rows dated 2026-08-28.
- **Residual over-budget (both under cap, no fix owed today):** MEMORY.md 92% (Will-ruled 7/28: flag to PROME, do NOT compact); CALENDAR.md 74% (rotation candidate at next housekeeping pass, resolved catalysts to archive).
- **Instrument note:** DAEDALUS's `read_cap_check.py` was updated same-day and now correctly recognizes RED's existing scope markers ("last 2-3 entries" for CHANGELOG, scripted reads on KB/CHALLENGES). Those three files are now ℹ️ scoped-not-lean, not counted — no wording fix needed for them.
- **MAINTENANCE entry filed** naming files touched, boot-impact, residuals, and provenance.

**🆕 S38f (2026-08-28, ~14:4x ET) — Will-ruled A on DAEDALUS item 3: T6 falsifier-seat PRE-STAGE COMPLETE. Verdict NO-VERDICT (trigger-never-fired). NO WEIGHT MOVED.**

- **Assignment path (put on the grade record via F3):** DAEDALUS relay → RED refused-and-surfaced → Will "A" in-session. Proceeded on Will's word; F3 flags the missing FORUM-spec provenance.
- **Pre-stage verdict: T6 = NO-VERDICT (trigger-never-fired branch), confidence VERY HIGH.** Trigger = Sept-hike <25%; never fired (window low 25.0% touched 8/14-16, strict less-than never crossed; current Kalshi 31.0% / PM 30.5%, 6pp above trigger).
- **Formal grade waits on DGS30 8/28 publication ~Mon 8/31 (T+1 per R3).** BOND/LIQUID own the formal grade; RED contributes as falsifier seat.
- **Four adversarial findings flagged (F1-F4), none verdict-changing:** OR-leg spec ambiguity (F1) · missing 8/28 Sept-hike pin (F2) · RED-seat provenance owed on grade record (F3) · pre-stage-vs-grade language ambiguity (F4). Full detail in `reports/2026-08-28_T6_falsifier_pre_stage.md`.
- **Adversarial contribution beyond the spec check:** the F1 spec-interpretation ambiguity on the OR-leg is future-relevant even if today's verdict is unchanged — flagged so BOND/LIQUID name their reading on-the-record at grade time. Class: any adversarially-built joint spec inherits ambiguity when read across authors' native framings; F1 is a live instance.
- **Tomorrow's execution needs:** pull DGS30 8/28 + ORACLE 8/28 close (BOND/LIQUID own); apply spec; either branch lands NO-VERDICT; post grade with F1-F4 findings recorded and RED-falsifier-seat provenance cited.
- **No task on RED for T6 tomorrow unless BOND/LIQUID need a re-verify or the F1 ambiguity needs adjudication.**

**🆕 S38e (2026-08-28, ~14:1x ET) — Top-priority focus item: VX-RED-004 CLOSED as FLIPPED-BEAR-TERMINAL. Flip_If was a dead firing record 87 days; refused to fake-re-spec it into the 9/3 auction. NO WEIGHT MOVED.**

- **The dead line:** VX-004's Flip_If was `30Y JGB >2.5% sustained` — but that fired 6/2 at 3.859% and lives 154bp below the current instrument (**4.039% [MOF 8/26]**, stable at/above 4.00 for two weeks per SAM). A Flip_If that has already fired is a firing RECORD, not a test — and I was carrying it into 9/3 30Y JGB auction where SAM adjudicates CH-009/CH-012/CH-016 on the same instrument family.
- **Chosen path: CLOSURE.** Strength FLIPPED-BEAR → **FLIPPED-BEAR-TERMINAL**. Flip_If rewritten to state firing history + owner-signalled reopening (if SAM materially reverses their JGB rail). Bear_Wt/Bull_Wt unchanged at 80/20 (TERMINAL is a CLOSURE label, not a weight change). Last_Reviewed → 2026-08-28. VX_HISTORY row logged.
- **Rejected: fake un-flip line** (e.g., <3.5% s=5). Exactly the ML-RED-203 defect NEXUS charged RED with THIS morning — amend-without-re-base-rating on a level I cannot verify without SAM's series. **Closure needs no base rate.**
- **Compliant with:** boot 9c review-debt (terminal rows owed no review), ML-RED-203 (edit-axis staleness), CHG-051 charge B extended to closures, SAM ownership.
- **VX live-count 9-of-17 → 8-of-16 unreviewed.**
- **SAM courtesy packet queued for closeout** — RED closing a vector on their turf; they own the instrument via their rail.
- **The transferable finding + audit trigger for 9/12 VX re-review:** any FLIPPED VX row whose Flip_If describes what FIRED it (not what would UN-FIRE it) is in the same TERMINAL-vs-re-spec question. Run each FLIPPED row through this test.
- **ML-RED-204 filed** naming the closure as a live application of ML-203.

**🆕 S38d (2026-08-28, ~13:5x ET) — PROME doorbell: R1 receipt APPLIED + FT-12 8/28-cell pre-registration + WILL_QUEUE row 106 label-only-change context. NO WEIGHT MOVED.**

- **R1 rc=1 was a REAL block** — COR-20260828-01 (WALTER's BZ correction; Brent 8/26 close $87.84 not $86.36). Found live cite on OUTBOX line 71 (RED-TO-PROME-030), corrected in-place with strike-through leaving a trail. Receipt written APPLIED via `corrections_boot_check.py RED --receipt COR-20260828-01 --action APPLIED`; `registry/corrections_receipts.tsv` created; rc=0 now.
- **FT-12 8/28-cell pre-registered UNGRADEABLE-PENDING-PUBLICATION.** Monday discipline written onto the row: read 8/28 obs at BAMLH0A0HYM2 on FRED at boot; if <260 → start sustain-3 as day 1 (needs 8/31 AND 9/1 also <260 to fire); if ≥260 → count stays 0. Absence-of-print does NOT clear a sustain count and does NOT extend one.
- **WILL_QUEUE row 106 context noted on FT-12 row** — PROME proposes reserving "kill" for the registry 2-close rung, labelling the other three (LIQUID intraday, RED/LIQUID s=3, HENRY s=5) OBSERVABLES. **FT-12 LETTER unchanged if Will rules** (mechanics, trigger, weight, exit all identical); only vocabulary shifts.
- **Monday MIDAS-06 verifier duty (post-16:15 ET)** — packet still in processed; briefing already consumed at S38 boot. VerifyResolution authoring rides that.

**🆕 S38c (2026-08-28, ~12:2x ET) — WALTER hand-carry: Chicago PMI 47.1 + Polymarket HIKE-2026 67%. Pre-registration owed on FT-12 counter-pressure. NO WEIGHT MOVED.**

- **Chicago PMI collapsed to 47.1 from 57.6** (~10.8pt miss vs consensus 57.9 — WALTER corrected a Schiff relay quoting 59; "biggest since Feb 2015" claim unsourced, treat as color).
- **FT-12 row rider added: counter-pressure pre-registered on the row.** If <260 s=3 prints INTO a growth-shock tape (Chicago PMI sub-50), the divergence is the object, not the fire itself. Weight mechanics unchanged (−2 on fire); the transferable content moves to the DIVERGENCE record. Recorded pre-fire so the finding cannot be reverse-engineered after the print.
- **Polymarket HIKE-2026 odds jumped to 67% (+12pts)** on Warsh's *"still has work to do"* line. **⛔ NOT MOVING POLICY RESCUE ON THIS**: one-hop relay, ORACLE-owned instrument, LABOR §3b guard binding (no attribution before NFP 9/4). It DOES reverse the direction of the 8/12 ORACLE stale-carry that moved Rescue 2→4 — audit owed at 9/4-9/11 window on ORACLE's own primary, not on this relay.
- **⛔ WALTER's packet: "this is NOT a dispatch, walter-0828 is live on this desk and I'm holding all BOARD/log writes."** Do NOT log dispositions to board_log for this; when WALTER's archive lands, that's the file record. Local files (FT-12 row + STATUS + SCRATCH) are RED-owned.
- **Chicago PMI is regional; national ISM Mfg is next Tue 9/2** — that's the direct RED-book counter to the growth-shock reading. Watch, don't pre-price.

**🆕 S38b (2026-08-28, ~12:0x ET) — WILL-DIRECTED FOCUS-LIST ITEM #1: CHG-046 + CHG-043-B BOTH RESOLVED-CONVERGED same-sitting at NEXUS's own resolution artifact. NO WEIGHT MOVED.**

- **CHG-046:** NEXUS graded their own successor split-falsifier at ~10:4x ET: Branch C, NO-VERDICT, EARNED, FINAL (arithmetic — neither A nor B can fire on any 8/28 value; verdict robust to the unpublished 8/28 cell and to both readings of "sustained 3"). Non-renewable clause CORRECTLY ARMED (C #1 of a max 2), next evaluation ~9/11 CPI, second C forces T-12 re-spec off pre-named candidate list with reachability base-rating required before freezing.
- **NEXUS §6.2 self-charge is stronger than RED's 8/12 delta-form rec:** the ADDENDUM 2 ruling repaired A's unreachability by silently moving it onto B. Stripping B's ratio leg left B = HY <260 s=3 alone; B's reachability lived entirely in the discarded ratio leg. Measured at primary: B went from 85.9% base rate to 0.0% as a side effect. **The 8/28 falsifier as it graded could only produce C. It was not a test.** This is worse than RED's original charge (3), which had described only that "resolves on HY alone."
- **CHG-043-B:** NEXUS practiced Disc-H on today's live artifact (their FT-12 flag packet) — flagged RED-FT-12 + branch-B + HENRY H-1 as one-instrument-three-desks on the shared HY <260 line, with the specific caution *"three desks, one route, count once."* Both legs of CHG-043 now RESOLVED-CONVERGED (FALCON S32 8/20, NEXUS S38b 8/28).
- **⚑ ML-203 filed — the inbound extension to RED's registry.** NEXUS explicitly named their §6.2 finding as the sibling class to CHG-051 charge B (base rates "computed once at registration and never recomputed"): same disease, EDIT axis not TIME axis. Any RED trigger whose legs were AMENDED after base rates were computed inherits the ORIGINAL's construction certificate. **First audit candidates: FT-01 (S36d relabel), FT-06 (post-hoc magnitude ML-144), FT-07 (window re-spec 9/4-9/11 — the check MUST precede the amendment, not follow it).**
- **FT-12 registry row extended:** NEXUS branch B added as IDENTICAL instrument (verbatim same line, not a distinct state). Reader rule now reads 'four surfaces, three distinct states.'
- **STATUS + CHANGELOG + OUTBOX (-033) + NEXUS_BRIEF vS38b all folded** per A4 (registered-challenge state changed).
- **NEXUS packet + LABOR packet + BRENT packet + LIQUID retraction packet** all queued for `git mv` to processed/.

**🆕 S38 (2026-08-28, boot 10:28 ET / QCEW graded ~10:5x ET — stamps from `date`) — LIVE CATALYST DAY, FROZEN TREE EXECUTED. NO WEIGHT MOVED: HOLD 69 / net-bear 60 (13th consecutive session).**

## CHANGES SINCE (S37 closeout → this boot)

- **QCEW preliminary benchmark = −79,000 total nonfarm** (private −178K, government +99K; retail trade −154.6K; T&W +135.1K; info +87K). Source **BLS USDL-26-1425**, 10:00 ET. LABOR's independent grade landed same-morning (their card called Band E, executed vector 8 4→2 and LAB-08 15%→4%).
- **FT-12 tightened another 4bps** on the 8/27 close: 267 [8/26] → **263 [8/27]** — nearest live registered trigger on the entire fleet board, per WALTER's 6c pass. Sustain-3 not started (needs <260); 8/28 close not yet published (T+1 series).
- **Brent 8/26 close corrected to $87.84** (WALTER self-flag; not published $86.36).
- **WAL 78.57 live intraday** — REG-T-02 <78 s=1 is 0.73% above.
- **5y5y 2.35** — drifting up toward FT-09's 2.55 (20bps).
- Inbox arrived overnight: CARL CHG-049-accepted, MIDAS Q-…006a verifier duty Mon 8/31, PROME + DAEDALUS sitting-2 review DISCHARGED (Will substituted DAEDALUS in-session), DEWEY CARL-DR-2 verdict against containment (counter-thesis evidence separated out per pre-registered routing rule).

## WHAT I DID

1. **Read the QCEW print.** Retrieved via LABOR primary chain (RED's own BLS fetch 403s this run; the L-24 lesson — reachability grades the moment it ran — cuts both ways; non-independence discount honored per RED-22's provenance line).
2. **Graded RED-22 against the frozen §3 bands: BAND D (−200 < R < +200) → NO VERDICT.** §4 Band D row executed exactly as tabled: all six hypothesis weights UNCHANGED, confidence UNCHANGED, net-bear UNCHANGED.
3. **G1-G5 all answered in writing** (STATUS S38 section). LAB-08 does NOT resolve on this print (G2 — final Feb-2027).
4. **RED-22 finalized WRONG.** 20% mass on Band D; Brier 0.808 vs uniform 0.80. Sharp A+B leg (40%) falsified. Free parameter w=0.30 was too high; the regime shift Berger flagged was real. Recorded as calibration hit; framework behaved.
5. **Symmetry check re-run:** Band A would have given Soft −2 / Managed +3 (net-bear −2). Band E gives Soft +2 / Managed −2. Band D gives 0. The tree is symmetric around 0, and D landed. Consistent.
6. **Predictions Scorecard updated:** 8 WRONG → 9 WRONG (adding RED-22); tally 9/12/1.
7. **CATALYSTS row 60 resolved** with the full outcome + composition + LAB-08 non-resolution note.
8. **CHANGELOG entry filed.** Prediction resolved → registered-state changed → W3 mandatory per A4.
9. **WALTER's cross-session 6c pass consumed:** FT-12 3bps, WAL intraday 78.57, Brent correction, FT-01 relabel consumed correctly (their language: "change in what a fire *means*, not when it fires"). Nothing owed back per WALTER's own line. Standing warning: WALTER's downstream router could read "trigger fired" as thesis-kill — risk lives at their end, they named it.
10. **Composition note filed for CARL/REGINALD** (info route, not a RED action): private layer −178K = 2.25× the top line; retail trade −154.6K. Consumer-facing sectors were revised down hard even as the top line came in benign.

## ⚑ THE SESSION'S FINDING, AND IT IS TWO-SIDED

**One:** The framework behaved. A print pre-committed to move nothing on RED's book, moved nothing on RED's book — even though it moved LABOR meaningfully (vector 8 4→2, LAB-08 15%→4%). **That asymmetry is a real property of two independently-calibrated frameworks, not a defect.**

**Two:** RED-22's probability distribution was still wrong, and calling it wrong in writing is what stops that from getting laundered by a "we didn't need to act on it" story. **20% mass on the outcome. Brier worse than uniform. w=0.30 was too high. The sharp A+B leg was falsified. Calibration hit taken.**

## NEXT SESSION (dated, priority-ordered)

1. **🟡 Mon 8/31 post-16:15 ET — MIDAS-06 verifier duty.** Read the four-branch mapping (packet §2) before verifying. ⛔ Do NOT verify (d) INDETERMINATE as NO — reserved for branch (b). On current tape (gold clears, DFII10 6bp short) (d) is LIKELY. Verify at the sources (COMEX GC settlement + FRED DFII10 obs dated 8/28), not MIDAS's write-up.
2. **🟡 Wed 9/3 — 30Y JGB (CHG-047 / CH-009 / CH-012).** SAM rail perimeters STATED.
3. **🟠 Fri 9/4 — NFP August.** The re-test: does −23K survive revision, does the labor force stop shrinking?
4. **🟡 9/4–9/11 re-spec window — FT-04 / FT-07 / VX-004 / FT-08 re-spec, on a day the bear is not losing.** ⚠️ RED-22's w=0.30 miss is one more input to this window's FT-01 magnitude review.
5. **🟠 Tue 9/9 — FT-11 goes LIVE.** Δ5(DGS30) precondition already satisfied on the 8/27 tape (−11.0bp) — may fire immediately on go-live day; the FLOW verdict downgrades the 30/70 row to 50/50 but moves NO hypothesis weight.
6. **🟡 Wed 9/10 — CARL V2 (subprime auto instrument, OTTO 7-deal 10-D panel).** Owner dark 8/20–8/27 but their 8/27 packet says "OTTO live tonight" → expect grade.
7. **🟠 Fri 9/11 08:30 ET — Aug CPI.** CHG-028 note: 9/11 is a pre-registered NON-EVENT for the oil→core channel (that resolves 10/14 + 11/10, two-print).
8. **🟡 Mon 9/15 — CHG-044 (BROCK) + CHG-049 (CARL) re-reviews.**
9. **🟢 Tue 9/30 — CHG-042 hard backstop retired unused** (34d pre-backstop resolution S37).
10. **Daily monitors:** ^SKEW vs 150 (FT-10 reload, 5.95 away) · **HY vs 260 (FT-12, 3bps and tightening — nearest board line)** · CCC vs 1000 (streak extends, 1031 [8/27]) · WL-07 USDJPY vs 160 (0.07 away) · WL-11 Brent <95 (firing).

## OPEN THREADS

- **🟠 The composition read on QCEW (private −178K, retail −154.6K) is routed as info to CARL/REGINALD but NOT graded by RED.** If CARL or REGINALD write it into their books, RED consumes their read — not the other way around. **Don't re-derive.**
- **⚑ RED still has no APPARATUS self-challenge that names a live testable defect on the registry itself.** CHG-051 is one (RED's first). ML-185 obligation: ≥1 live at all times. Next candidate: the free-parameter-w defect QCEW just exposed — RED-22's mixture parameter had no independent instrument for regime-persistence, and I set it by intuition. **This class extends to any RED prediction that carries a subjective mixture weight.**
- CHG-042 backstop retired unused; **but the S28b "unfetched-vs-unavailable" test resolved 34d early — the ML-136 class is one to keep testing on ACTIVE-BLOCKED rows.**
- VX-RED-004's flip line (30Y JGB >2.5% vs live ~4.1%) still needs re-spec; **9/4-9/11 window, do NOT carry it into 9/3.**
- CHG-047 rail: **CH-009/CH-012 next adjudicate at the 9/3 30Y JGB auction.** VX-004 defect lives in the same instrument family — connected work.
- Publisher-side routing unfixed as a class (ORACLE side; RED does not own the fix).
- Independence discount stands (ML-133) — and now practiced twice on the QCEW print (RED↔LABOR chain read once; not counted twice on the RED book).

## PENDING WILL-DECISIONS

- **None blocking.** MIDAS-06 verifier duty runs mechanically on Monday. Sitting-2 substitution rule ruled/discharged. C8 conditions all executed and re-verified.

## GIT STATE (one line)

On master; S38 committed path-scoped (`AGENTS/RED/` only — STATUS · SCRATCH · CHANGELOG · CATALYSTS · PREDICTIONS · OUTBOX · NEXUS_BRIEF · ML · KB); auto-push via `scripts/safe-push.sh` at closeout.

---


**🆕 S37 (2026-08-27, boot 14:36 ET / close ~14:4x ET — stamps from `date`) — PLAIN BOOT, ONE INBOUND CONSUMED. NO WEIGHT MOVED: HOLD 69 / net-bear 60.**

*S37 first-half narrative (HENRY packet, LIQUID retraction, BOND/REGINALD routing answers, CARL V2 re-date, MF-starts + CHG-042 resolution, 1b routing pass, Increment 2 review + re-verify) archived in git history — the last S37-family entries were folded at that closeout; durable outcomes live in the workbook + STATUS S38's counterweight row + the S37 final-closeout summary below.*

**🏁 S37 FINAL CLOSEOUT (Will-worded, ~18:0x ET).** The day in one line: **four Will-directed sweep items executed (MF-starts · CHG-042 · CARL V2 · 1b routing) + 3 same-day routing answers encoded on owner words + the Increment 2 review delivered and re-verified — and NO WEIGHT MOVED at any of the day's endings.** Cross-session traffic: HENRY ×5, LIQUID ×2, BOND, REGINALD, ORACLE ×2, PROME ×n. RED defects owned on ledger: ML-196 (conjunction-from-a-sentence) · ML-198 (peer-axis tidiness) · ML-200 (second un-encoded transfer). Checks at close: schema 12/12 · boot.py ⑤ 🟢 · orphan/claim per closeout run · memory committed carve-out ③ ×2.

---

*S36, S36b, S36c, S36d and S35 blocks archived in git history at commit `dbd0b8034` — the C8 review, the six pre-next-sitting conditions, FT-11 pre-data amendment, and CHG-051 deliverables (registry 15→17 cols, `base_rate_review.py`, FT-12 registration, FT-01 relabel). All durable outcomes live in the registry, `CHALLENGES.tsv`, `PREDICTIONS.tsv`, and the S36/S35 CHANGELOG entries.*
