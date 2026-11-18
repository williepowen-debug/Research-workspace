# Production Review #10 — Reader D1 (cohort: VIOLET, BRENT, SAM, BOND, ZHAO)

**Reader:** read-only subagent for DAEDALUS (Claude Code, Opus 5.5) · **Written:** 2026-11-18 · **Pinned cutoff:** `208bd704ea` (PROME closeout 11/17 evening) · **Period:** 2026-11-02 00:00 to cutoff · Brief: `runs/2026-11-16_PR10/READER_BRIEF_RERUN.md`. Nothing edited, staged or committed except this file. File reads at the cutoff use `git show 208bd704ea:<path>`; where a fleet tool had to run on the working tree, the post-cutoff difference for that desk is stated beside the result.

Ladder used: `AGENTS/DAEDALUS/OPERATIONS.md` § MATURITY LADDER (floor L0 skeleton, L1 STATUS + current judgment under reading B, L2 structured record accruing; Market L3 convergence matrix + exit rules + predictions resolving + dated falsification surface; Market L4 trade leg under reading A; L5 clean closeouts, current, mechanical-QC leg N/A). All five cohort desks are Market class.

Fleet tools run by this reader (working tree, read-only): `scripts/read_cap_check.py --agent <NAME>`, `scripts/ledger_staleness.py <NAME>`.

---

## VIOLET (Market, map L4 / M, last scored 2026-10-21)

### (a) Commits in period
**129** commits touch `AGENTS/VIOLET/` (`git log --after='2026-11-02 00:00' 208bd704ea -- AGENTS/VIOLET/ | wc -l`); about 70 are VIOLET's own, the rest are WALTER card routings and PROME packets. Working tree equals the cutoff for `AGENTS/VIOLET/` (`git diff --stat 208bd704ea -- AGENTS/VIOLET/` empty). Structural events:

| Date | Event | Evidence |
|---|---|---|
| 11/05 | Path A F2 audit pre-registered, then run: "not runnable, no gate, about 70% not replicated" (KB-VIO-372) | `cc62521acd`, `69259b5a66`; `research/2026-11-05_path-a-f2/REPORT.md` |
| 11/05 | WQ-611 A encoded: Path A to WATCH on measured rates (6 of 19 vs 13.7% base; 8 of 19 vs 21.4%), Lag Trade entry/target/stop/sizing withdrawn from thesis and TRADE.md; thesis v4.1.7 | `5fbbcc2fe6` |
| 11/05 | WQ-614 A ("yes to all") encoded: credit-flat row redefined (HY OAS 5-session change no wider than +25bp), MOVE pause/resume line retired with no successor, desk CLAUDE.md MAIL paragraph replaced; thesis v4.1.9 | `3ecb11e729`, `c2497133a1` |
| 11/06–11/10 | Predictions resolving: VIO-PRED-10 CONFIRMED 11/09, VIO-PRED-07 CONFIRMED 11/10 | `d23cfff754`, `bb2e50f113`; `workbook/PREDICTIONS.tsv` |
| 11/10 | DOCKET L342 fix: `scripts/thresholds.py` refuses an orphan-VIX row on market-closure dates; acceptance test written first and passed (Labor Day 9/07 row refused, ledger byte-identical; 8 suites, 52 checks) | `f385b5f0cf`; `research/2026-11-10_L342/ACCEPTANCE.md` |
| 11/06, 11/10 | Hand-typed clock stamps self-corrected to `date` | `609978b64f`, `bf4802de8a` |
| 11/16 | Closeout after restart; PROME 11/16 outside-audit packet answered ("nothing changed") and moved to processed | `47125539ad`; `STATUS.md:145`; `inbox/processed/2026-11-16_from-PROME_outside-audit-items-verify-first.md` |
| 11/17 | Nvidia close read: VIX 25.46, cash curve inverted (VIX3M/VIX 0.9811), VVIX 121.28; credit-vol WATCH closed NOT MET; closeout receipt to PROME | `079c3d1434`, `195a3d6258`, `f770e8e444`; `STATUS.md:9-33` |

### (b) Current Gaps / Next_upgrade claims

| # | Claim in current row | Verdict | Evidence |
|---|---|---|---|
| G1 | KB.tsv still opens directly on its schema: two-clock vintage-header leg NOT MET | STILL-TRUE — line 1 of KB.tsv is the column header (`ID Date Group ...`); 402 lines, 809,415 B at cutoff. `ledger_staleness.py VIOLET` reads KB.tsv `ok +0d` on its git-time fallback, so the alert works without the header | `git show 208bd704ea:AGENTS/VIOLET/workbook/KB.tsv \| head -1`; ledger_staleness run |
| G2 | October 19 official-check/feed-repair evidence and STATUS are current within their declared windows | OVERTAKEN as a dated fact — STATUS is now 11/17 16:5x ET with "Last real data refresh: 2026-11-17", History SETTLE through 11/16 | `STATUS.md:3-7` |
| G3 | read-cap rotation_due=0 | **OVERTAKEN — now rotation_due=1.** `MEMORY.md` 25,741 B = 79% of budget (rotate tier; 2,957 B to remove to reach the 70% stop). STATUS 11,972 B (37%) | `read_cap_check.py --agent VIOLET` (rc 0, `rotation_due=1`) |
| G4 | Full standard-match confirmation and whole-profile refresh remain DAEDALUS-owed; profile clock FIRED September 25 | STILL-TRUE; body still 9/04 and its anatomy is now wrong (see e) | `profiles/VIOLET.md:6,20-22` |
| N1 | L5 candidate after KB.tsv gains its two-clock header and a clean closeout is verified, with rotation_due=0 | STILL-TRUE as an open gate, two of its three legs currently unmet (header absent; rotation_due=1). Reachable in VIOLET's own tree. Note: the header is the root "preferred" signal, not a hard rule (root CLAUDE.md § Data Hygiene), and the git-time fallback already reads KB.tsv; whether a comment line breaks `validate_workbook` was not checked | G1, G3 |
| N2 | Conf M-to-H requires DAEDALUS's full profile/standard-match read, not another owner deliverable | STILL-TRUE; reachable (DAEDALUS work) | — |
| N3 | checkpoint next PR completion | STALE FORM — this PR is that checkpoint; the clause carries no fact after PR10 closes | — |

Additional current facts not in the row: three inbox packets unprocessed at cutoff — DAEDALUS WQ-678 harness lines (11/12; VIOLET's own STATUS schedules A15 for the 11/18 wake, `STATUS.md:142,157`), PROME 11/16 stale KB rows (47 rows, VIOLET's count matches, `STATUS.md:144`), PROME 11/17 WQ-715 probability on every new call. Boot red carried: CANARY_MAP has 1 dark ledger; thesis-currency advisory at 21 KB rows since v4.1.9 (`STATUS.md:146`).

### (c) Proposed replacement cells

- **Gaps:** `KB.tsv opens on its column header with no two-clock vintage line; ledger_staleness reads it on the git-time fallback. MEMORY.md is 25,741 B, 79% of the read-cap budget, rotation_due=1 (2026-11-18 run). Thesis v4.1.9 (WQ-611 A and WQ-614 A encoded November 5; Path A on WATCH, Lag Trade withdrawn, MOVE line retired). Inbox at cutoff holds WQ-678 harness lines, 47 stale KB rows (PROME November 16) and WQ-715 probability packet, all scheduled on STATUS. CANARY_MAP carries 1 dark ledger. Profile body is September 4 and its file anatomy is wrong at every whole-read surface.`
- **Next_upgrade:** `L5 requires MEMORY.md rotated under 70% of budget (rotation_due=0), the KB.tsv two-clock header or an owner statement that the git-time fallback is its declared vintage, and an independently read clean closeout. Conf M to H requires DAEDALUS's whole profile refresh and standard-match read.`

### (d) Grade verdict — RETAIN L4 / M

| Leg | Verdict | Basis |
|---|---|---|
| L0 skeleton | PASS | `AGENTS/VIOLET/CLAUDE.md` present (27,865 B) |
| L1 STATUS + current judgment (reading B) | PASS | `STATUS.md:9` BOTTOM LINE states the current regime read |
| L2 structured record accruing | PASS | KB-VIO-372 to KB-VIO-401 added in period; LEDGER_GLOB declares `workbook/*.tsv`, `registry/*.tsv`, `board_log.tsv`; 17 ledgers scanned, none stale |
| L3 convergence matrix | PASS (carried, not re-read) | profile §2 and 10/21 row; no change found in period |
| L3 exit rules | PASS | WQ-614 A re-cut the credit-flat row and retired MOVE (`3ecb11e729`) — exit and pause rules are actively maintained |
| L3 predictions resolving | PASS | VIO-PRED-07 and -10 CONFIRMED in period; PRED-08 (11/20) and -09 (12/31) OPEN (`workbook/PREDICTIONS.tsv`) |
| L3 dated falsification surface | PASS | STATUS invalidator table (`STATUS.md:111`); Path A F2 audit pre-registered before outcome (`cc62521acd`) |
| L4 trade leg (reading A) | PASS | flat by record (`TRADE.md:9`: no VIOLET-owned position; no new proposal); signals demonstrably reach consumers — 11/17 rows to LIQUID, HENRY, RED by outbox SIG and NEXUS_BRIEF (`STATUS.md:29-33`); invalidators sent to TERRY |
| L5 clean closeouts, current | FAIL on the row's own named leg | rotation_due=1 now (MEMORY 79%); closeouts otherwise frequent with receipts to PROME (`f770e8e444`, `47125539ad`); 11/11 closeout self-records the window was not held to the close (`07663ada56`) |

### (e) Profile trigger
Profile `**Refresh clock: 21 d → 2026-09-25**`, or at the 9/16 letter grade, the KB.tsv two-state ruling, or the next external review round (`profiles/VIOLET.md:6`). **Date-age: FIRED** (54 days past). **Content trigger: FIRED** — the 11/16 outside audit relayed by PROME (`e40c030896`) is an external review round. **Structural defeat: YES** — the body's file anatomy (`profiles/VIOLET.md:20-22`) gives STATUS 32,546 B "at 99.99%", SCRATCH 17,997, MEMORY 21,457, CALENDAR 20,880; at cutoff they are 11,972 / 4,785 / 25,741 / 10,484, and MEMORY is now the rotation-due surface rather than STATUS. A bounded delta cannot carry this; whole refresh warranted.

### (f) Cross-agent observations
- DAEDALUS: the WQ-678 harness-lines packet (11/12) is still in VIOLET's inbox at cutoff; VIOLET has scheduled it for the 11/18 wake (`STATUS.md:142`). Not overdue on VIOLET's account, but DAEDALUS's own delivery record should not show it consumed.
- PROME: VIOLET has no declaration in `PROME/registry/READS.tsv`; read_cap verdict is "clean within what the scan found", not a clean bill (read_cap_check output).

---

## BRENT (Market, map L5 / M, last scored 2026-10-21)

### (a) Commits in period
**152** commits touch `AGENTS/BRENT/`; **64** carry a `BRENT` subject prefix. Working tree differs from the cutoff only by four new 11/18 inbox packets (FALCON, WALTER SIG-W-20261118-001/-004/-006; `git diff --stat 208bd704ea -- AGENTS/BRENT/`), not material. Structural events:

| Date | Event | Evidence |
|---|---|---|
| 11/05 | Four new predictions registered BRT-32 to BRT-35 (Yanbu loading halt, Brent M1-M3 under +3.50 before the January roll, distillate under 95M, retail gasoline under $4) | `cc0221b31d`; `thesis/PREDICTIONS.tsv` rows BRT-32..35 |
| 11/05 | Wednesday EIA routine failed on the usage limit; Thursday fallback did the full EIA primary pull and superseded the "NOT yet recorded" warning | `8411a92901` |
| 11/06–11/10 | BRT-34 mechanism resolved; BRT-35 confirmed; CL over $100 un-fire graded (DOCKET L1089) | `e2a1f95e46`, `9d2f187f38`, `c8ced15f5a` |
| 11/12 | WPSR week 11/6 graded: BRT-31 NOT MET unreachable; CATO M12-4 correction applied (holiday explanation dropped) | `407be551d6`, `1ef6a1290c` |
| 11/12–11/14 | Three verbatim STATUS rotations with crc receipts; 11/14 took STATUS to 22,775 B and TRADE to 22,631 B (70%) | `d70b1f99a0`, `baa3e5f73d`, `6f78c71c03` |
| 11/16 | COT #14 graded at the CFTC raw file: JOINT NOT-SPENT, eighth consecutive | `73b48100a2`; `STATUS.md:5` |
| 11/17 | Same-session self-correction before closeout: invalidation item 4 re-graded NOT met (the 14:46 note had called it met at the margin), PROME told 14:49 ET; outside-audit packet deferred and logged | `a6efd265ef` → `3bfbe07d7d` |

### (b) Current Gaps / Next_upgrade claims

| # | Claim in current row | Verdict | Evidence |
|---|---|---|---|
| G1 | October 20 cleanup and EIA evaluation landed | STILL-TRUE as history; carries no current fact | — |
| G2 | STATUS now 20188 B and read-cap rotation_due=0, refuting the old 85% blocker | **OVERTAKEN — STATUS 26,433 B, 81% of budget, rotation_due=1.** The 11/14 rotation reached 22,775 B (70%); three days of dated blocks re-grew it 3,658 B (PAT-055 regrowth). NEXUS_BRIEF.md, read whole by NEXUS, is 25,329 B (78%, owner notice) | `read_cap_check.py --agent BRENT` (rc 0, rotation_due=1); `6f78c71c03` body |
| G3 | scripts/boot.py still has no version-sweep invocation | STILL-TRUE — boot.py's last stage is `render_calendar.py --check`; no version or consistency stage and no such script in `scripts/` | `git show 208bd704ea:AGENTS/BRENT/scripts/boot.py` lines 163-186; `git ls-tree` of `scripts/` |
| G4 | Latest owner STATUS explicitly retains source-age/coverage/ledger/standing-reconciliation findings; no all-clean claim | STILL-TRUE — every dated block in period is stamped SCOPED-PARTIAL; CME IP block since 10/28 retained as the official boundary; Gulf throughput UNRESOLVED on a measured basis | `STATUS.md:3,5,7,11,13` |
| G5 | Profile FIRED on rule 19 restructure and TRADE split; body September 7 | STILL-TRUE; the body is now also wrong on file anatomy (see e) | `profiles/BRENT.md:8-9` |
| N1 | Conf M-to-H after version-consistency check is wired and observed on capable/clean cases | STILL-TRUE, reachable in BRENT's own tree | G3 |
| N2 | calendar twin passes | STALE FORM — boot.py's own comment says the twin-diff was a migration instrument that retired when the generator landed; the live check is `render_calendar.py --check` (wired at boot). Not run by this reader (desk script); the 11/14 closeout reports "calendar re-rendered, check clean" | boot.py lines 163-186; `6f78c71c03` body |
| N3 | a bounded clean closeout with rotation_due=0 is independently read | STILL-TRUE; rotation_due is 1 now | G2 |
| N4 | Keep current source/coverage findings explicit; do not equate compact files with clean evidence | STILL-TRUE as a standing caution | — |
| F1 | Gaps cell text "old85%" and "rule19" | STALE FORM — words glued together (root Output Canon) | FLEET_MAP BRENT row |

Additional current facts: `ledger_staleness.py BRENT` reports `workbook/LESSONS_INDEX.tsv` STALE +39d (KB, VX, FLOW, GROUP_MAP FROZEN with banners). One inbox packet open at cutoff: PROME 11/16 outside-audit items, deferred by BRENT and logged (`3bfbe07d7d` body). STATUS line 21 carries glued text ("GulfTimes October12", "RBRTE125.44 on10/6", "the10/8") against the root Output Canon.

### (c) Proposed replacement cells

- **Gaps:** `STATUS.md is 26,433 B, 81% of the read-cap budget, rotation_due=1 (2026-11-18 run): the November 14 rotation reached 70% and three days of dated blocks re-grew it. NEXUS_BRIEF.md, read whole by NEXUS, is 78%. scripts/boot.py has no version-consistency stage. Every November session is stamped SCOPED-PARTIAL; CME IP block since October 28 and unmeasured Gulf throughput are retained explicitly. LESSONS_INDEX.tsv reads STALE at 39 days. Profile body is September 7 and describes a 38,591 B charter that is now 22,539 B.`
- **Next_upgrade:** `Conf M to H after a version-consistency check is wired into boot.py and observed on a capable and a clean case, STATUS and NEXUS_BRIEF are under 70% of budget at a closeout an independent reader reads clean, and LESSONS_INDEX.tsv is refreshed or frozen.`

### (d) Grade verdict — RETAIN L5 / M

| Leg | Verdict | Basis |
|---|---|---|
| L0 skeleton | PASS | `CLAUDE.md` present (22,539 B) |
| L1 STATUS + current judgment (reading B) | PASS | `STATUS.md:3` "v5.13 / WAIT unchanged; nothing armed" with dated reasoning |
| L2 structured record accruing | PASS (with one stale ledger) | REGISTRY, PREDICTIONS, CATALYSTS accruing; LESSONS_INDEX.tsv STALE +39d |
| L3 convergence matrix | PASS (carried, not re-read) | no change found in period |
| L3 exit rules | PASS | WQ-386 held-VLO exit discharged 11/05 (`TRADE.md` WQ-386 block); invalidation items graded and corrected same session (`3bfbe07d7d`) |
| L3 predictions resolving | PASS | BRT-32..35 registered 11/05; BRT-35 confirmed, BRT-31 NOT MET unreachable, BRT-33 window graded daily |
| L3 dated falsification surface | PASS | BRT-33 F-a line with dated window; pre-flight check header on PREDICTIONS.tsv |
| L4 trade leg (reading A) | PASS | TRADE.md current to the 11/05 FORGE reconcile; stance WAIT with WQ-192 stand-down and named authority scopes (`TRADE.md:1-14`) |
| L5 clean closeouts, current | PASS WITH DEBT | daily closeouts with verbatim rotations, crc receipts and same-session corrections; debt: rotation_due=1 (STATUS 81%), one stale ledger, one deferred PROME packet. Not a LOWER: the owner rotates on cadence and nothing is over budget |

### (e) Profile trigger
Profile `**Staleness / refresh clock:** 45 d → 2026-10-22`, or earlier on THESIS major version, TRADE split, rule-19 restructure, a Conf/level change at PR#6 (`profiles/BRENT.md:9`). **Date-age: FIRED** (27 days past). **Content trigger: FIRED** (already recorded 10/21; THESIS now v5.13 against v5.8 in the body). **Structural defeat: YES** — the body's source list reads `CLAUDE.md` whole at 38,591 B (`profiles/BRENT.md:8`); it is 22,539 B at cutoff, and the boot anatomy (8-entry sequence) was not re-counted. Whole refresh warranted; a bounded delta cannot carry it.

### (f) Cross-agent observations
- NEXUS: BRENT's NEXUS_BRIEF.md (25,329 B, 78% of budget) is in NEXUS's declared whole-read perimeter; it is turning toward NEXUS's own read cap.
- PROME: the 11/16 outside-audit packet is deferred by BRENT at cutoff (`3bfbe07d7d`); PROME's audit-tracking should show it open, not delivered.
- DAEDALUS: the BRENT FLEET_MAP row itself carries glued words ("old85%", "rule19"); fix in the replacement cell.

---

## SAM (Market, map L4 / H, last scored 2026-10-21)

### (a) Commits in period
**119** commits touch `AGENTS/SAM/`; **48** carry a `SAM` subject prefix, all dated 11/06 to 11/12. **No SAM session after 11/12 20:16 ET** (`8996cd579c` is the last; STATUS "Last written: 2026-11-12 20:13 ET", `STATUS.md:3`). Working tree differs from the cutoff only by three new 11/18 WALTER cards (not material). Structural events:

| Date | Event | Evidence |
|---|---|---|
| 11/06 | SoftBank funding stack read at primary (bridge repaid, leverage about 22 to 24%); a mislabelled WQ-643 tag withdrawn the same day as ISHM's | `a71eeb11cb`, `75307fc093` |
| 11/09 | 8/3 intervention ambiguity resolved from the MOF Q3 per-operation record | `624f265b9b` |
| 11/10 | SoftBank Q2 graded ESTIMATE CONFIRMED (9/30 LTV 15.9%; rolled to Arm $183.26 = 22.5% against a pre-registered 21.6%); card 010 re-read corrected a grade line without moving the verdict | `bbd8974416`, `c3e000bc76`; `STATUS.md:7` |
| 11/10 | RED S62b reproduced SAM's ABB-inclusive SoftBank leverage | `09464c7478` |
| 11/11 | `ltv_lookup.py` FX defect documented and a visible warning added before any figure (CATO MW2) | `d346a52192`, `56154ee62d` |
| 11/12 | WQ-680 C9: USD/JPY 160 row graded for 11/12 (touch yes, close no); packet to PROME answering asks 2-5; narrative-drifted stamps corrected to the clock | `669524e2fd`, `3607f04e92`, `aadac2268f` |

### (b) Current Gaps / Next_upgrade claims

| # | Claim in current row | Verdict | Evidence |
|---|---|---|---|
| G1 | SAM-42 resolved FALSE/FAILED October 31; only SAM-33 remains OPEN | STILL-TRUE — one OPEN row (SAM-33, BOJ no emergency long-end capping through 12/31); last row SAM-42; no prediction registered in period | `git show 208bd704ea:AGENTS/SAM/thesis/PREDICTIONS.tsv \| grep -c -P '\tOPEN\t'` = 1 |
| G2 | Current CLAUDE line 93 is a neutral messaging notice; old hygiene-avoidance claim withdrawn | STILL-TRUE as history; carries no current gap — drop | 11/02 PR reader B |
| G3 | Existing cross-desk primary verification is real | STILL-TRUE — SoftBank read at SoftBank's own documents, reproduced by RED S62b; MOF and BOJ primaries cited | `09464c7478`; `STATUS.md:7,9` |
| G4 | a two-direction reconciliation receipt is not established | **STALE FORM / UNREACHABLE AS WORDED.** `RECONCILIATION.md` (unchanged since `40c839d17a`, 2026-06-16) prescribes owner-doc-first, derived-after order plus a grep sweep and a true-up; it contains no "both directions" check (`RECONCILIATION.md:9-54`). The gap asks for a receipt the contract never requires. Its routing also names KOYOMI and METSUKE (`:48`), neither of which appears in `PROME/ROSTER.md` at cutoff | `git show 208bd704ea:AGENTS/SAM/RECONCILIATION.md`; ROSTER grep empty |
| N1 | Inspect first post-SAM-42 closeout for one figure checked both directions under the existing reconciliation contract | RE-CUT — same defect as G4. The reachable test under the actual contract: at the next scheduled-catalyst write-back, the grep sweep for a changed mark returns only dated hits and CALENDAR and CATALYSTS agree. SAM's 11/12 SoftBank and 160-row write-backs fold NEXUS last (`45f55278b2`, `7cdbce78ed`), consistent with the owner-first order; this reader did not run the sweep | G4 |
| N2 | Retain actual source/rotation limits | STILL-TRUE and now sharper: rotation_due=2 (below) | — |

Additional current facts not in the row:
- **Read cap: rotation_due=2.** STATUS.md 29,559 B = 91% of budget; MEMORY.md 28,808 B = 89% (`read_cap_check.py --agent SAM`, rc 0). STATUS is also read whole by NEXUS.
- `ledger_staleness.py SAM`: `workbook/BIS_GLI.tsv` STALE +59d (VX, XCCY_BASIS FROZEN).
- **Five unprocessed inbox packets at cutoff**, oldest 11/13: CYPHER GMO 4784 compensation cost (11/13); PROME USD/JPY 160 combination-theme question (11/14); PROME independent read of the SoftBank LTV roll — one blocking finding, "25% at Arm about $145" too low, reader range $142 to $157 (11/16); PROME outside-audit items (11/16); PROME stale-ledger refresh or freeze (11/16). Plus 14 WALTER cards. Every packet says "next session"; none asks a wake. The backlog is a launch gap, not an owner failure.
- Charter `CLAUDE.md` is 41,853 B (under the 50,000 B charter ceiling).

### (c) Proposed replacement cells

- **Gaps:** `No SAM session since November 12; five packets wait at cutoff, including PROME's November 16 independent read with one blocking finding on the SoftBank 25% Arm price (reader range $142 to $157 against SAM's about $145). STATUS.md 91% and MEMORY.md 89% of the read-cap budget, rotation_due=2. BIS_GLI.tsv STALE at 59 days. Only SAM-33 OPEN (to December 31); no prediction registered since SAM-42. RECONCILIATION.md (June 16) has no two-direction check and routes to KOYOMI and METSUKE, neither on ROSTER.`
- **Next_upgrade:** `L5 requires STATUS and MEMORY rotated under 70% of budget, the November 16 SoftBank finding graded, and one scheduled-catalyst write-back whose grep sweep and CALENDAR to CATALYSTS lockstep an independent reader confirms clean. RECONCILIATION.md routing to be re-pointed to live owners.`

### (d) Grade verdict — RETAIN L4 / H

| Leg | Verdict | Basis |
|---|---|---|
| L0 skeleton | PASS | `CLAUDE.md` 41,853 B |
| L1 STATUS + current judgment (reading B) | PASS (as of 11/12) | `STATUS.md:5` "View: no fresh observed Japan-led carry unwind, tested again 11/6 and 11/10" |
| L2 structured record accruing | PASS (one stale ledger) | USDJPY, MOF_FLOWS, RATE_DIFFERENTIAL ok; BIS_GLI.tsv STALE +59d |
| L3 convergence matrix | PASS (carried, not re-read) | — |
| L3 exit rules | PASS (carried) | TRADE.md retired frame with explicit "nothing re-arms" rules (`TRADE.md:23-34`) |
| L3 predictions resolving | PASS, thin | SAM-42 resolved 10/31; SAM-33 open to 12/31; none registered in period; SoftBank estimate pre-registered and graded (`bbd8974416`) |
| L3 dated falsification surface | PASS | SAM-33 dated through 12/31; USD/JPY 160 row graded on a dated rule (`669524e2fd`) |
| L4 trade leg (reading A) | PASS | TRADE.md HISTORICAL since 8/7 with the re-entry condition stated: separately argued thesis, review and Will approval, construction TERRY (`STATUS.md:81`); signals reach consumers (RED S62b reproduction, WQ-680 packet to PROME) |
| L5 clean closeouts, current | NOT MET | rotation_due=2, five packets and 14 cards unprocessed since 11/12; not adjudicated beyond that |

### (e) Profile trigger
Profile `**Staleness:**` 45 days from vintage 2026-09-17, or (a) THESIS leaves v1.7, (b) RED sweep line advances past 2026-08-20, (c) OPEN set no longer exactly {SAM-28, SAM-31, SAM-33}, (d) hard floor 2026-11-01 (`profiles/SAM.md:12`). At cutoff: (a) NOT fired (`THESIS.md:1` "v1.7"); (b) **FIRED** (`red/CHALLENGES.md:4` "Last RED sweep: 2026-10-01"); (c) **FIRED** (OPEN set {SAM-33}); (d) **FIRED** (date-age, 45 days = 11/01). **Structural defeat: PARTIAL** — the body's claim that STATUS stays "at 67% of budget" (`profiles/SAM.md:88`) is now 91%, and the bounded 11/02 delta (`profiles/SAM.md:1`) does not carry rotation. A bounded delta could carry the rest (thesis unchanged, same file set); whole refresh not strictly required, but due by the date floor.

### (f) Cross-agent observations
- PROME: SAM has not been launched since 11/12 and holds five packets (one blocking finding from PROME's own 11/16 commissioned read). PROME owns whether a wake is warranted; none is asked by any packet.
- PROME/WALTER: the 11/14 combination-theme question (USD/JPY near 160) remains unanswered, so WALTER's `combo:none` tagging for that subject persists until SAM's next session.
- NEXUS: SAM STATUS (91% of budget) is in NEXUS's whole-read perimeter.

---

## BOND (Market, map L4 / H, last scored 2026-10-21)

### (a) Commits in period
**92** commits touch `AGENTS/BOND/`; **43** carry a `BOND` subject prefix (11/02 to 11/16). Working tree differs from the cutoff only by two new 11/18 WALTER cards (not material). Structural events:

| Date | Event | Evidence |
|---|---|---|
| 11/05 | Catch-up: November QRA graded (F1 and F3 NOT FIRED, guidance dropped "at least"), auction health 4 to 3 under WQ-536 A; THESIS v1.2.13; MEMORY rotated | `39aa057688`, `7a5b997431`, `ca9ae25f5f`; `thesis/THESIS.md:3` |
| 11/05 | Predictions BND-33 (pre-print) and BND-34 to BND-37 (WQ-596) registered | `3f084dd286`, `85529bd1b6` |
| 11/05 | ta_ws_schema repair: acceptance conditions written before editing, findings F1-F9 and O1 repaired, PROME re-read ACCEPT-WITH-RESIDUE (DOCKET L859 closed) | `6578a5bbbf`, `3036cea011`, `844a9ef2c9` |
| 11/06 | Self-correction: closeout commit `30a0e63c7d` went in ungated (freeze verify was MOVED), recorded by `c85c7b09c7` | `c85c7b09c7` |
| 11/09–11/12 | Refunding graded: 3Y I′ fire (BND-33 TRUE, DOCKET L924), 10Y I′ fire, 30Y CLEAN (68.11 vs 63.89); VX-BND-17 2 to 1 | `cf19bacf7e`, `99d32a6dad`, `dad27cd31a`, `d7f63e88ce` |
| 11/13 | WQ-682 RULED A encoded: VX-BND-18 red leg is the CFR collateral ratio; C12 consumer scan run | `67fc152632`, `78fec255bf`; `SCRATCH.md:1-8` |
| 11/16 | Long-end read and FHLB Q3 re-score (VX-BND-18 held at 2; 20Y and TIPS bars frozen); mortgage-spread basis reconciled with HOMER: survey-matched about 213bp governs, BOND's 201bp same-date pair withdrawn as basis (KB-BND-583). Commit body: "Not a closeout." | `01a56f5f16`, `d945c4111a` |

### (b) Current Gaps / Next_upgrade claims

| # | Claim in current row | Verdict | Evidence |
|---|---|---|---|
| G1 | Current owner v1.2.12, FLAT and 18/35 | **OVERTAKEN** — v1.2.13 (11/05), FLAT since 10/30, composite 17/35 | `THESIS.md:3`; `STATUS.md:93`; bond-state comment in `TRADE.md` and `STATUS.md` |
| G2 | old profile/version/score snapshots superseded | History; drop | — |
| G3 | Named core TSV headers remain schema-only | STILL-TRUE — KB, VX, FLOW and thesis/PREDICTIONS.tsv each open on the column header | `git show 208bd704ea:AGENTS/BOND/workbook/{KB,VX,FLOW}.tsv \| head -1` |
| G4 | LEDGER_GLOB absent at inspected paths | STILL-TRUE — `workbook/` holds FLOW, KB, SCHEMA, VX only; `ledger_staleness.py BOND` falls back to the default glob and reads all three ok | `git ls-tree 208bd704ea AGENTS/BOND/workbook/`; ledger_staleness run |
| G5 | Memory bytes not remeasured | **RESOLVED** — MEMORY.md 24,011 B = 74% of budget; BOND read cap rc 0, rotation_due=0, perimeter DECLARED and attested in READS.tsv | `read_cap_check.py --agent BOND` |
| G6 | WQ-536 counters are audit-only | **OVERTAKEN** — the registered clean-auction counter now drives auction health (4 to 3 on 11/05; counter reset by the 11/9 3Y I′ fire, 1 after the 11/12 30Y) | `THESIS.md:3,119`; `STATUS.md:93` |
| G7 | November 2 refunding bars frozen | **RESOLVED** — all three refunding auctions graded against the frozen bars 11/09 to 11/12 | (a) |
| N1 | Existing header/declaration/rotation and clean-closeout requirements remain; verify actual target core files, never invent a fifth header | STILL-TRUE for header and declaration legs (reachable in BOND's own tree); rotation leg now met | G3-G5 |
| N2 | November 4 QRA and November 5 grade remain owner work | **RESOLVED** — QRA graded 11/05; BND-33 registered 11/05 and graded TRUE 11/09 | `7a5b997431`, `cf19bacf7e` |

Additional current facts not in the row:
- **STATUS lags the ledger after the 11/16 non-closeout session.** STATUS still reads "Last session update: 2026-11-13 11:40 ET" and carries 201bp as the PMMS spread basis (`STATUS.md:45,105`; `NEXUS_BRIEF.md:7`), which BOND itself withdrew as basis on 11/16 (KB-BND-583, `d945c4111a`). VX-BND-17's score is 1 on both bases, so no score is wrong; WQ-699 RULED A (switch to the matched basis) waits in the inbox.
- Five inbox packets at cutoff, none older than 11/16: WQ-699 RULED A, outside-audit items, stale KB rows (11/16); Florida municipal spread question and scorer-archive layout check (11/17, addressed to the 11/18 session).
- Monitors: 18 `.py` at cutoff (profile anatomy says 12, `profiles/BOND.md:43`).
- Glued text in live surfaces against the root Output Canon: `workbook/FLOW.tsv` FL-BND-01 ("October20refresh:10/7dealerTOTAL+2.022B"), `THESIS.md:65` ("September23").

### (c) Proposed replacement cells

- **Gaps:** `THESIS v1.2.13, FLAT since October 30, composite 17/35. KB, VX, FLOW and PREDICTIONS open on their column header with no two-clock line; workbook/LEDGER_GLOB absent (ledger_staleness uses the default glob). Read cap rc 0 on a declared perimeter, rotation_due=0 (MEMORY 74%). STATUS was last written November 13 and still carries the 201bp mortgage-spread basis BOND withdrew on November 16; WQ-699 RULED A waits in the inbox. BND-34 to BND-37 OPEN. Profile body is September 17; monitors now 18, not 12.`
- **Next_upgrade:** `L5 requires workbook/LEDGER_GLOB declared, two-clock headers on the declared core ledgers, STATUS and NEXUS_BRIEF carrying the matched mortgage-spread basis after WQ-699 is encoded, and an independently read clean closeout.`

### (d) Grade verdict — RETAIN L4 / H

| Leg | Verdict | Basis |
|---|---|---|
| L0 skeleton | PASS | `CLAUDE.md` 34,362 B |
| L1 STATUS + current judgment (reading B) | PASS, stale by one session | `STATUS.md` "## Current judgment" section; last written 11/13 |
| L2 structured record accruing | PASS | KB-BND-561 to KB-BND-583 in period; VX rows re-scored on their letters |
| L3 convergence matrix | PASS | composite 17/35 with per-vector breakdown (`STATUS.md:93`) |
| L3 exit rules | PASS | bond-state token `kill=MET-REC@2026-10-01; posture=FLAT@2026-10-30`; WQ-592 put spreads declined (`STATUS.md` Regime and capital record) |
| L3 predictions resolving | PASS | BND-33 TRUE 11/09; BND-32 FALSE 10/29; BND-34..37 OPEN |
| L3 dated falsification surface | PASS | THESIS F1/F2/F3 graded 11/05 with F2 carrier extended to 2/9/2027 (`THESIS.md:3`) |
| L4 trade leg (reading A) | PASS | FLAT declared with state tokens and a declined proposal on record; signals reach consumers (BOND to PROME, LIQUID, ZHAO on the 3Y fire, `cf19bacf7e`; F2 read to RED, `d95da250ff`) |
| L5 clean closeouts, current | NOT MET | header and LEDGER_GLOB legs unmet; 11/16 work landed without a closeout, leaving STATUS one session behind its own KB |

### (e) Profile trigger
Profile `**Staleness:**` fires on any of (1) THESIS leaves 1.2.7, (2) TRADE Last Updated leaves 2026-09-09, (3) read_cap rc ≠ 0, (4) monitors `.py` count leaves 12, (5) composite leaves 12/35, (6) more than 45 days ⇒ 2026-11-01 (`profiles/BOND.md:12`). At cutoff: (1) **FIRED** (1.2.13); (2) **FIRED** (11/05); (3) not fired (rc 0); (4) **FIRED** (18); (5) **FIRED** (17/35); (6) **FIRED**. **Structural defeat: YES** — the monitor anatomy (`profiles/BOND.md:43`, "12 .py"), the charter size (36,493 B in the body, 34,362 B now) and the score all moved. Whole refresh warranted.

### (f) Cross-agent observations
- NEXUS: BOND's NEXUS_BRIEF.md line 7 still cites the 201bp same-date mortgage spread that BOND withdrew as basis on 11/16; NEXUS should not carry it forward until BOND encodes WQ-699.
- HOMER: the 11/16 reconciliation agreed one figure (survey-matched about 213bp); this reader did not check HOMER's side.

---

## ZHAO (Market, map L4 / H, last scored 2026-10-21)

### (a) Commits in period
**60** commits touch `AGENTS/ZHAO/`; **21** carry a `ZHAO` subject prefix. Working tree differs from the cutoff by one new 11/18 WALTER card (not material). Structural events:

| Date | Event | Evidence |
|---|---|---|
| 11/06 | ZHA-21 graded NO; ZHA-22 to ZHA-25 registered with probabilities; ZHA-24 withdrawn VOID and ZHA-26 registered on the overnight rate (WQ-647 A) | `7db67c7dbf`, `b8847bde79`; `STATUS.md:140` (60 / 68 / 12 / 18%) |
| 11/06 | Matrix moved: V5 4 to 5 on the construction-PMI re-raise leg, total 29/60 (two-sided shadow 32) | `5d1fe2b687`; `STATUS.md:6,61,93` |
| 11/06 | PBOC anchor caught up: overnight reverse repo became the main policy rate 11/02; STATUS self-records "desk 4 days late" | `f9dc663a33`; `STATUS.md:68` |
| 11/09 | SAFE October reserves and gold read at primary (KB-ZHAO-251); 11/10 clocks read at primaries, all four re-suspended to about 1/10/2027 | `d42ff089bf`, `b779a53ac8` |
| 11/10 | ZHA-19 and ZHA-20 YES; `boot.py` PBOC-rate line now checks the PBOC notice (implemented and tested); CATO finding MC1 fixed 11/11 | `2cbc0f65d4`, `8e6c1e2845`, `711dcd8f28` |
| 11/11 | WQ-660 and WQ-660 A charter lines applied (WQ-622 combination-watch line; CLAUDE.md line 37 alignment) | `711dcd8f28` |
| 11/16 | Read-cap false breach fixed in the charter; October credit and activity graded at NBS primary; PROME declined the proposed READS row for KB.tsv with a test | `bb2e282816`, `7e64758f04`; `STATUS.md:4` |
| 11/17 | China-side read of the BIS chip rule at primaries ("a conditional threat, no measure"); three routes proposed to PROME, consumed; VULCAN rule packet processed | `6f678bd18d`, `fe85e90b1a`; `STATUS.md:16-21` |

### (b) Current Gaps / Next_upgrade claims

| # | Claim in current row | Verdict | Evidence |
|---|---|---|---|
| G1 | ZHA-18 graded NO October 16 | STILL-TRUE as history; carries no current gap — drop | `STATUS.md:111` |
| G2 | Belgium kill leg replaced October 29 by prospective China-flow letter; old pending October 23 re-spec superseded | STILL-TRUE as standing design; the kill letter at `STATUS.md:105` is the 10/29 re-specification | `STATUS.md:105` |
| G3 | Primary GACC reconciliation remains owed | STILL-TRUE — October trade is still "nominal, carriers not GACC tables" (`STATUS.md:66`); KB-ZHAO-252 re-dated the GACC read to 11/10 "consensus only" (`d42ff089bf` body) |
| G4 | July/August reserve reconciliation remains owed despite later backfills | STALE FORM — SAFE end-October reserves were read at primary on 11/09 (KB-ZHAO-251, `STATUS.md:65`); July/August reserves are not on the owner's current owed lists (`STATUS.md:22,152-153`). Whether the July/August reconciliation itself was ever done was not established by this reader |
| G5 | Reading-A conditioned-freeze branch retained | STILL-TRUE and now firm — the re-arm rule is in TRADE.md line 1 and in the charter file table: unfreeze when TERRY carries a card whose primary rationale cites a ZHAO vector, or ZHAO proposes one | `TRADE.md:1`; `CLAUDE.md:260` |
| G6 | October 14 whole profile vintage unchanged | STILL-TRUE | `profiles/ZHAO.md:7` |
| N1 | L5 requires actual source-debt dispositions and independently verified clean/current closeout | STILL-TRUE, reachable. Owner's current source debt is concrete: GACC tables, the August China −$12.25B and Belgium +$19.85B holdings residuals, the chinamoney.com.cn fixing series, CFETS close leg (`STATUS.md:152-153`) |
| N2 | no repeat Belgium re-spec or ZHA-18 grade | History; drop |

Additional current facts: read cap rc 0, rotation_due=0 (STATUS 22,159 B, 68%); perimeter is the charter heuristic (2 files), no READS.tsv declaration. Two inbox packets at cutoff: PROME 11/16 stale KB rows (owner count 123 by boot.py against PROME's 106, scheduled for the next ordinary session, `STATUS.md:22`) and VULCAN 11/17 Malaysia loans (arrived after the 11/17 closeout). ZHAO's predictions already carry stated probabilities (`STATUS.md:140`), so the 11/17 WQ-715 packet needs no change in practice. Next wake 11/18: September TIC, ZHA-22, BIS re-check (`STATUS.md:16`).

### (c) Proposed replacement cells

- **Gaps:** `Matrix 29/60 (V5 4 to 5 on November 6); September TIC (November 18) resolves ZHA-22 and carries the owed Vector 1 rescore question. Source debt open: GACC October tables (carrier nominal figures only), August China and Belgium holdings residuals unexplained, no chinamoney.com.cn fixing series. PBOC anchor change on November 2 was caught four days late; boot.py now checks the PBOC notice (November 10). TRADE frozen with a stated re-arm rule (TRADE.md line 1, charter file table). Read cap rc 0, perimeter undeclared. Profile body October 14.`
- **Next_upgrade:** `L5 requires the GACC tables read or a declared substitute, the August residuals explained or closed as unknown, and an independently read clean closeout after the September TIC session.`

### (d) Grade verdict — RETAIN L4 / H

| Leg | Verdict | Basis |
|---|---|---|
| L0 skeleton | PASS | `CLAUDE.md` 32,406 B |
| L1 STATUS + current judgment (reading B) | PASS | `STATUS.md:4,6` "THIS WEEK, IN ORDER OF WHAT MATTERS" and Overall Status |
| L2 structured record accruing | PASS | KB-ZHAO-251 to KB-ZHAO-283 in period; ledger_staleness 6 ledgers ok |
| L3 convergence matrix | PASS | `STATUS.md:72-93`, total computed from the rows |
| L3 exit rules | PASS | kill letter re-specified 10/29 with all-legs conjunction (`STATUS.md:105-111`) |
| L3 predictions resolving | PASS | ZHA-19, -20 YES; ZHA-21 NO; ZHA-24 VOID with withdrawal recorded; four OPEN with probabilities |
| L3 dated falsification surface | PASS | kill letter and dated OPEN rows (11/18, 11/30, 12/31) |
| L4 trade leg (reading A) | PASS | frozen WITH an explicit re-arm rule (`TRADE.md:1`), now also in the charter (`CLAUDE.md:260`); signals reach consumers (routes to VULCAN, HAWK, HANS, YURI, TERRY 11/17, consumed by PROME `1e99de828d` per `STATUS.md:16`) |
| L5 clean closeouts, current | NOT MET | closeouts current (11/06, 11/09, 11/11, 11/16, 11/17); source debt per N1 open; 4-day PBOC anchor lag in period |

### (e) Profile trigger
Profile `**Staleness:** refresh at the next post-TIC session that changes the matrix, or >45d → checkpoint 2026-11-28` (`profiles/ZHAO.md:9`). **Date-age: NOT FIRED** (11/28). **Content trigger: AMBIGUOUS.** Read literally it FIRED: the August TIC was pulled 10/16, after the 10/14 profile, and the 11/06 session changed the matrix (V5 4 to 5, `5d1fe2b687`). Read as intended (a TIC-driven matrix change) it has not: the 11/06 move came from construction PMI, and September TIC lands 11/18, after the cutoff. **Structural defeat: NO** — charter, TRADE and file set are the same shape; a bounded delta can carry the period. Recommend re-cutting the trigger to name the TIC release explicitly (for example: "the first session after a TIC release that re-scores Vector 1, or 2026-11-28").

### (f) Cross-agent observations
- PROME: ZHAO STATUS plans to "re-try the API on 11/18; if still 403, tell Will" for the MOFCOM list API and SAMR, both HTTP 403 on 11/17 (`STATUS.md:20`). The root Blocked-sites rule says a site that blocks automated access is unusable: stop, use another source, tell Will. Whether a single 403 is a block, and whether one retry is allowed, is PROME's call under WQ-701; flagged, not judged.
- PROME: the stale-KB count differs (ZHAO boot.py 123, PROME scan 106, `STATUS.md:22`); PROME's packet says the owner's count governs.

---

## Not read / limits

| Item | Status | Effect on this report |
|---|---|---|
| Desk charters (`CLAUDE.md`) for all five desks | Not read whole; grepped for targeted lines only | Charter-conformance claims not made; L0 graded on presence |
| Convergence matrices for VIOLET, BRENT, SAM | Not re-read in period; carried from the 10/21 row and profiles | Those L3 legs say "carried, not re-read" |
| Desk-local scripts (`boot.py`, `render_calendar.py --check`, `validate_workbook`, VIOLET `canary_staleness`) | Not run (desk-owned) | BRENT calendar check and VIOLET KB header compatibility unverified |
| `read_cap_check.py` and `ledger_staleness.py` | Run on the working tree, not the cutoff | Working tree equals the cutoff for VIOLET; for BRENT, SAM, BOND, ZHAO it differs only by new 11/18 inbox cards, none of which is a measured file |
| WALTER cards and full inbox packet bodies | Listed and counted; only the packets quoted were read | Packet dispositions stated from the desks' own STATUS lines |
| HOMER side of the BOND mortgage-spread reconciliation | Not read | Agreement stated from BOND's commit only |
| SAM RECONCILIATION sweep execution on 11/10 to 11/12 write-backs | Not reproduced | N1 re-cut is about the contract text, not a finding of non-performance |
| Whether KOYOMI and METSUKE exist as spawnable tool-class agents outside ROSTER | Not checked beyond a ROSTER grep | SAM routing claim limited to "not on ROSTER" |
| ZHAO July and August reserve reconciliation history | Not traced through archives | ZHAO G4 marked STALE FORM, not RESOLVED |
| Profile bodies | Head, staleness line and anatomy lines only | Structural-defeat calls rest on the named anatomy lines |

END OF REPORT
