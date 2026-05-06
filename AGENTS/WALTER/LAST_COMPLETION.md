# LAST_COMPLETION — WALTER

*Overwritten each session. STATUS / CHANGED / RESULT / GAPS / WILL_NEEDS / FOLLOW-UP / OPEN DESIGN DECISIONS. Source-of-truth for handoff carry-forward — when a future session boots, this is what tells them what's outstanding.*

---

## STATUS

Session 2026-05-06 mid-day Wed (~14:18-15:30 UTC) — **second WALTER session today**. Will-triggered RED LIAISON channel session. **5-turn same-day architectural-thread convergence** (RED Turns 1/3/5; WALTER Turns 2/4) — same as BRENT, faster than CARL (7). **0 BOARD dispatches** (architectural session). 0 sub-spawns. **RED revived overnight with 6 Session-8 commits + opened LIAISON channel 8 minutes before Will paged WALTER.**

Boot-state at session start: clean working tree (origin diverged — earlier session's `edfaaa6d` BRENT LIAISON closeout still pending push from 00:46 EDT this morning). Pull was Already up to date. Discovered RED untracked at `AGENTS/RED/handoff_WALTER/{LIAISON.md, README.md}` placed 10:08-10:10 EDT (file mtime).

Closeout shipped per CLAUDE.md spawn-protocol steps 12-16: STATUS lead-paragraph rewritten for second-session arc + LIAISON manifest RED row PENDING → ACTIVE Turn 5 closed; NETWORK AWARENESS regen (RED moves to ≤7d active per Session 8 + LIAISON convergence; routing pressure deltas reflect REQ-RED supersession by RED revival); SESSION LOG entry prepended (the second 5/6 entry — first BRENT-LIAISON entry retained as the prior-session row); REGISTRY refresh (RED row YELLOW + Updated 5/6 + LIAISON-converged Focus; WALTER row updated for second session); MEMORY CHANGES SINCE / NEXT SESSION rewrite + 2 new findings (LIAISON convergence accelerator pattern locked at 3-channel sample; empirical-dispatch-surface check before accepting routing-gap diagnosis); LAST_COMPLETION rewrite (this file); existing LIAISON convergence accelerator finding REFINED inline (substrate prep is helpful but not load-bearing per RED counter-evidence).

## CHANGED

### Session arc (Will-triggered RED LIAISON pickup + 4 turns + JOINT_PROPOSAL §2+§3+§5)

1. **Boot ping (msg 1372, 14:18 UTC):** Boot reads clean — STATUS / IRAN_WAR anchor / MEMORY / LAST_COMPLETION (yesterday's BRENT-closeout version) / REGISTRY / ROUTING_TABLE v0.6 / BOARD INDEX cluster ToC. Pull was Already up to date (origin reflects the 00:46 EDT BRENT-closeout `edfaaa6d`). LIAISON channel discovery via boot-step 9 found new untracked `AGENTS/RED/handoff_WALTER/` directory + git log showed RED Session 8 commits 08:56→10:03 EDT.
2. **Surfaced finding to Will (msg 1374):** RED revived this morning with 6 commits then placed untracked LIAISON channel 8 min before Will paged. RED revival resolves "Tier 1 highest priority blocked on revival" follow-up from yesterday's session; 3 of CC-side Tier-1 LIAISON channels could now be active simultaneously. Offered to draft Turn 2 reply.
3. **Will pick "Yes lets have you read and reply to RED"** (msg 1375) — drafted Turn 2 in WALTER tree at `handoff_RED/LIAISON_TURN_2_DRAFT.md` (~12KB). **Open-with-substance disposition retrospective from WALTER's side** flipped RED Turn 1's "WALTER mostly absent" framing — empirical grep across 110 BOARD signals: RED in `to:` 19 (17%) + `info:` 100 (91%) = 107 (97%) routing-target. Verdict distribution 45 CONFIRMED / 44 CORRECTED-FRAMING / 3 INDETERMINATE / 2 FALSE → CORRECTED-FRAMING tied with CONFIRMED at 47% modal, validating RED's MEMORY observation empirically. 21 historical bifurcation/divergence/tape-vs-substance tagged signals as Q3 floor. **6 pre-cosigns (Q1/Q2/Q3/Q4/Q6/Q7) + 2 deferred (Q5 CHG-RED-024 propagation / Q8 5-10 cluster_mediating empirical pass) + 4 questions back (Q9 boot-step / Q10 prediction-resolution scope / Q11 unanimity threshold / Q12 CORRECTED-FRAMING auto-cc).**
4. **Will direct-write authorized (msg 1377):** Turn 2 appended to RED's LIAISON.md (~14:25 UTC turn stamp).
5. **RED Turn 3 came back fast** (msg 1379, file mtime 10:36 EDT — 25 min after Turn 2 landed). Substantive: 8/8 questions resolved (7 pre-cosigned including new Q12) + 4 deliverables shipped in-turn at RED tree. **Concession-on-diagnosis pattern:** RED explicitly logged "Turn 1 framed this backwards. The architectural fix is RED-side consumption, not WALTER-side dispatch." Q11 sharpening: ≥3 → ≥4 (RED4/RED5 = trade-actionable consensus). Honest gap: 5 event-type triggers (WAL MI3 / BTFP 2.0 / OZK NCO / bypass-pair / etc.) don't fit threshold-cross 8-col schema; defers schema v2 with `trigger_type` discriminator.
6. **Drafted Turn 4 directly** (~6KB, lighter): Q11 ACCEPT + bull-side calibration flag (current `unanimity_bull` would fire 50%+ from STALE-YELLOW agents; proposed fresh-active ≤14d denominator); Q8 priming-offer ACCEPT (RED to pre-classify 21 historical bifurcation signals); CHG-RED backfill proposal (WALTER takes complete via `handoff_RED/CHALLENGES_BACKFILL_diff.tsv` preserving Critical Rule #2); joint-proposal artifact paths proposed; 3 close-loop questions Q13-Q15.
7. **RED Turn 5 wrap** (10:52 EDT) — channel CONVERGED in 5 turns total. Q13 LOCK TSV → bifurcation_classification TSV shipped 22 signals (8 HENRY-tape / 9 RED-structural / 5 both = 14/22 lean structural matches Turn 2 hypothesis); Q14 LOCK WALTER takes complete CHG backfill; Q15 LOCK fresh-active-only denominator. **3 findings emerged from classification pass:** (a) VIOLET emerges as primary on 3 vol-family signals — distinct from HENRY in REGISTRY; (b) all 5 "both" signals event-anchored; (c) Apr 19 had 9/22 bifurcations (41% in 1 day) — dense-bifurcation-day = high-stakes-decision-day pattern, proposed `network_uncertainty_peak` closeout-level flag.
8. **Will-prompted "joint proposal sections" command** (msg follow-up 1382-pre): drafted WALTER §2+§3+§5 at `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-06_walter_red_sections.md` (28K / 316 lines, similar density to RED's §1+§4 at 20K/233 lines).
9. **Will closeout greenlight (msg 1382 "lets work on closing out")** → this commit.

### Files touched this session

**New (1) in WALTER design/:**
- `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-06_walter_red_sections.md` — 316 lines / 28K — §2 FALSIFICATION_TRIGGERS WALTER eval logic + §3 ROUTING_TABLE v0.7 + CHECKLIST delta + §5 v0.9 unanimity_state with sub-tag candidates

**New directory (1) in WALTER tree with 1 file:**
- `AGENTS/WALTER/handoff_RED/LIAISON_TURN_2_DRAFT.md` — Turn 2 draft (~12KB; landed in RED tree via direct-write auth)

**Closeout files (refreshed):**
- `AGENTS/WALTER/STATUS.md` — Updated stamp; lead-paragraph rewritten for second-session-arc with 3-LIAISON-active-converged framing; LIAISON manifest RED row PENDING → ACTIVE Turn 5; NETWORK AWARENESS "Today's routing" subsection regen (RED moved to ≤7d active); SESSION LOG entry prepended for today's mid-day session
- `AGENTS/WALTER/REGISTRY.tsv` — RED row refreshed (was STALE 18d, now ACTIVE-ELEVATED YELLOW; new Focus reflecting Session 8 + LIAISON convergence + 6 deliverables); WALTER row refreshed for second session
- `AGENTS/WALTER/MEMORY.md` — CHANGES SINCE / NEXT SESSION rewrite; 2 new findings + LIAISON convergence finding refined inline (3-channel sample now locks the pattern; substrate prep helpful-not-load-bearing per RED counter-evidence)
- `AGENTS/WALTER/LAST_COMPLETION.md` — this file (rewritten for today's second session)

**RED tree (RED-OC commits, NOT WALTER's to stage — Critical Rule #2):**
- `AGENTS/RED/handoff_WALTER/LIAISON.md` — Turns 1-5 (623 lines / 60K)
- `AGENTS/RED/handoff_WALTER/README.md` — channel conventions + 12-anchor RED identifier index
- `AGENTS/RED/handoff_WALTER/bifurcation_classification_2026-05-06.tsv` — 22-signal classification (Q8/Q13 deliverable)
- `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` — 7 threshold triggers in 8-col schema
- `AGENTS/RED/design/JOINT_PROPOSAL_2026-05-06_red_sections.md` — §1 + §4 + §6 + §7 (233 lines / 20K)
- (RED also already-shipped `workbook/CHALLENGES.tsv` col-11 BOARD_Refs + 5 backfilled and `workbook/SCHEMA.tsv` updates as part of his Session 8 commits 08:56-10:03)

### Sub-agent spawns (0)

No sub-agent spawns this session. Architectural-alignment + execution session only.

### Spec changes

**None committed yet.** ROUTING_TABLE v0.6→v0.7 + CHECKLIST Phase 2 steps 5-7 add are drafted in JOINT_PROPOSAL §3 pending Will sign-off.

### Commits

Closeout commit pending (this session). Earlier same-day session's BRENT-LIAISON closeout `edfaaa6d` (00:46 EDT) is in WALTER's pending-push backlog from this morning.

## RESULT

**RED LIAISON converged in 5 turns same-day — 3 of CC-side Tier-1 LIAISON channels (CARL/BRENT/RED) now active-converged in 48 hours.** Today's session validates and locks the LIAISON convergence pattern at a 3-channel sample, with one significant pattern refinement vs yesterday's BRENT-only finding:

1. **LIAISON convergence accelerator pattern locked at 3-channel sample (REFINED finding).** Open-with-substance + concede-on-diagnosis-when-data-inverts-it + ship-deliverables-Turn-3 + close-Turn-5 = 5-turn baseline. Substrate prep doc (BRENT_LIAISON_PREP.md) was hypothesized load-bearing yesterday — RED converged in 5 turns without one. Refines the pattern to: prep doc helpful but not required; the load-bearing accelerators are open-with-substance + concede-on-diagnosis. Apply: NEXUS / REGINALD / HENRY / BROCK next-LIAISON setups expect 5-turn convergence as baseline.

2. **Empirical-dispatch-surface check before accepting routing-gap diagnosis (NEW finding).** RED Turn 1 framed the gap as "WALTER mostly absent" with only 1 retro signal. Turn 2 grep-pass surfaced 107/110 routing-target rate (97%); RED Turn 3 explicitly conceded the reframe; architectural fix shifted from "more dispatch" to "structured artifacts that let high-volume routing become consumable." This was the highest-leverage finding of the LIAISON — a CARL/BRENT-style "more push" architecture would have been the wrong fix entirely. Process discipline: every future LIAISON Turn 2 brings routing-side data the target can't see (counts, verdict distribution, cluster-mediating volume) regardless of whether Turn 1 surfaced a gap.

3. **Concession-on-diagnosis as a pattern-class.** RED Turn 3 logged the reframe explicitly, converting what could have been a defensive thread into a generative one. Worth flagging as a sub-pattern of the convergence accelerator: the agent who concedes the diagnostic gets the architectural design they actually need, not the one their Turn 1 framing assumed. Apply: when WALTER Turn 2 inverts Turn 1's diagnosis, frame the inversion as data-not-criticism so the responder can absorb-and-pivot.

4. **WALTER tree growth scoreboard for the day:** earlier session shipped §2a-§2d + §3b + §3d (475 lines / BRENT). This session shipped §2 + §3 + §5 (316 lines / RED). 791 lines of joint-proposal architecture-spec across two parallel proposals to Will-surface, both pending sign-off. Two parallel surfaces, not one super-proposal — Will can sign per-§ across both proposals as he has bandwidth.

5. **VIOLET as distinct primary axis discovery.** RED's bifurcation classification surfaced VIOLET as primary on 3 vol-family signals (419-002, 419-003, 419-007) — distinct from HENRY's tape-regime axis. Implication for `unanimity_state` v0.9 computation: VIOLET must be in the agent-set; today's fresh-active N=9 includes her. Worth tracking for whether other axis-distinct primaries surface (BOND on rates? OZK on bank-CRE-narrow?).

## GAPS

### Today's open items (carry-forward — added to FOLLOW-UP list below)

- **Will sign-off on RED+WALTER 2-way JOINT_PROPOSAL** — 5 batched items: §2 FALSIFICATION_TRIGGERS WALTER eval logic / §3 ROUTING_TABLE v0.7 + CHECKLIST delta / §4.3 RED CLAUDE.md boot-step b / §4.4 RED MEMORY 97%-routing-target entry / §5 v0.9 unanimity_state
- **Repo-root stitch** `design/JOINT_PROPOSAL_2026-05-06_red_walter.md` — assemble RED §1+§4+§6+§7 + WALTER §2+§3+§5 + repo-root sequencing once both side-files are committed (RED's pending RED-OC next-boot)
- **WALTER `design/CROSS_REFS/RED.md` cache scaffold** (no sign-off needed) — populate from handoff_WALTER/README.md 12-anchor identifier index; unblocks Q14 complete-CHG-RED-backfill
- **WALTER complete CHG-RED backfill** via `handoff_RED/CHALLENGES_BACKFILL_diff.tsv` (post-CROSS_REFS, preserves Critical Rule #2)
- **WALTER FALSIFICATION_TRIGGERS at-dispatch eval logic** implementation (post-§2 sign-off; WALTER spawn-protocol step 6b extension + parallel ledger scaffold)
- **WALTER ROUTING_TABLE v0.7 + CHECKLIST** ship (post-§3 sign-off; mechanical update to existing files)
- **WALTER unanimity_state v0.9 stack readiness** (post-§5 sign-off + post-v0.8-land)
- **WALTER `network_uncertainty_peak` closeout flag** — extend STATUS lead-paragraph step 12 with daily bifurcation count; auto-flag when ≥5 in single calendar day; lightweight, ships with §3
- **RED CLAUDE.md boot-step b add** — RED post-Will sign-off task (RED holds CLAUDE.md edit per his discipline)
- **RED MEMORY.md 97%-routing-target calibration entry** — RED post-Will sign-off task

### Pre-existing carry-forward (still open, brought forward from yesterday's BRENT-LIAISON closeout)

- **3-way joint proposal stitch** — WALTER stitches at repo-root when CARL §1+§3a+§3c+§4 sections land (CARL Turn 7 self-task, ETA this week)
- **Will sign-off on 3-way JOINT_PROPOSAL §2 stack** — 4 items: §2a FORMAT_SPEC v0.8 (4 fields + 9-value enum) / §2b scheduled-scan budget ($0.30-0.50/wk per side) / §2c BRENT-IMMEDIATE 8-row threshold list / §2d BURST_WINDOW protocol
- **BOARD_CONSUMPTION_SPEC v0.2 dual-pattern doc** — WALTER self-task this week (CARL consumer-domain + BRENT energy-domain templates)
- **CROSS_REFS/{CARL,BRENT}.md cache scaffolds** — WALTER self-tasks this week
- **EVENT_WINDOW_STATE.md scaffold** — WALTER post-Will-sign-off on §2d BURST_WINDOW
- **HAWK-proxy archive** to `design/history/hawk_proxy_synthesis_2026-05-05.md` — when actual HAWK refresh lands
- **FORMAT_SPEC v0.7 → v0.8 land in spec** — post-Will-sign-off on §2a
- **CHECKLIST update for v0.8** — post-Will-sign-off
- **BRENT CLAUDE.md spawn-protocol delta** — BRENT next session
- **BRENT DATA_RELEASE_CALENDAR.md** — BRENT post-back-disposition pass
- **CARL DATA_RELEASE_CALENDAR.md** — CARL self-task this week
- **OZK Q1 post-mortem** — REGINALD pickup pending since Apr 16
- **ROAD Act House reconciliation timing** — BARON pickup
- **HENRY + RED SIGNAL_INTAKE.md prompts on disk** (HENRY remains; RED's signal-intake is partially superseded by FALSIFICATION_TRIGGERS.tsv)
- **BOARD_CONSUMPTION_SPEC propagation to 14 Tier 1 agent CLAUDE.md files** (CARL + BRENT mostly done; RED has the boot-step add pending Will sign-off; remaining 11)
- **Tier 2 staleness** (ZHAO 34d / SHADE 6+wk / OTTO 21d / ORACLE 35d / FERT 6+wk / ATHENA 7+wk / CRUISE 6+wk / DARWIN dormant)
- **"verified-as-of" pattern extension** (second anchor candidate — Fed-framework / BOJ / OPEC+)
- **design/STATE.md maintenance discipline**
- **Lead-paragraph regeneration cadence decision**
- **Filter v2 Segment D** (~1hr, decided option A)
- **Signal Registry v2** (deferred)
- **COP refresh resume trigger** (paused Apr 14)
- **Autonomous news-scan policy**
- **HAWK-proxy synthesis policy**
- **CONSUMER_STAGFLATION 5-axis sub-cluster spawn decision**
- **Pandemic-meta-cluster informal watch** (14-day window)

### Resolved this session (removed from carry-forward)

- **RED LIAISON setup** (was item 23 in 5/6 morning FOLLOW-UP) — converged in 5 turns same-day.
- **RED revival blocker** — RED ran Session 8 + opened LIAISON; no longer blocked.
- **REQ-RED Wirth-1970s steelman supplement** — superseded by RED revival; RED has the BRENT 5/12-features-present decomposition in his MEMORY now and LIAISON is the venue going forward.
- **WALTER joint-proposal §2+§3+§5 sections drafted** — 316 lines / 28K shipped.
- **Bifurcation cluster classification empirical pass** (was item Q8 deferred at Turn 2) — RED shipped TSV in Turn 5; replaces my 5-10-dispatch tracking pass.

## WILL_NEEDS

1. **Sign-off on RED+WALTER 2-way JOINT_PROPOSAL** (5 batched decision items in `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-06_walter_red_sections.md` + `AGENTS/RED/design/JOINT_PROPOSAL_2026-05-06_red_sections.md`):
   - §2 FALSIFICATION_TRIGGERS WALTER eval logic (read-loop + 5-step at-dispatch eval + parallel ledger preserving Critical Rule #2)
   - §3 ROUTING_TABLE v0.7 delta (new "By Tag/By Verdict" section, 3 rules + de-dupe) + CHECKLIST Phase 2 steps 5-7 add
   - §4.3 RED CLAUDE.md boot-step (b) scoped scan (RED implements post-sign-off)
   - §4.4 RED MEMORY.md 97%-routing-target calibration entry (RED implements post-sign-off)
   - §5 v0.9 candidate `unanimity_state` 4-val enum + RED-level ≥4 cutoff + fresh-active ≤14d denominator + sub-tag candidates `event_anchored: true` + `network_uncertainty_peak` closeout flag
2. **Sign-off on 3-way (CARL/BRENT/WALTER) JOINT_PROPOSAL §2 stack** — 4 items per yesterday morning's WILL_NEEDS (still pending; carry-forward)
3. **Decide repo-root stitch timing** — stitch now, or hold until per-§ sign-off lands? My read: hold; sign-off can happen against side-files; stitch is mechanical post-sign-off.
4. **Decide next-LIAISON priority** — RED resolved. Remaining: REGINALD (CC-side, unblocked, top of queue) > NEXUS (blocked on spawn) > HENRY (post-RED+REGINALD) > BROCK (mid-priority).
5. **Iran-war anchor re-verify boundary 5/11 minimum** OR earlier on visible kinetic state-change (carry-forward).
6. **Tomorrow's intake watch:** OBDC Q1 5/6 AMC (BROCK pre-built); LYV Q1 from 5/5 surfaces in tomorrow's intake.

## FOLLOW-UP (canonical running list — survives handoff via this file)

**Time-sensitive (this/next session):**
1. **OBDC Q1 5/6 AMC** — BROCK pre-built threshold reads. Surfaces in tomorrow's intake.
2. **LYV Q1 from 5/5 post-market** — high-signal CONSUMER_STAGFLATION discretionary-sub-vector confirm/deny.
3. **NFP Friday 5/8** — LABOR carry-forward.
4. **Q1 Call Report window May 1-10** — REGINALD recheck.
5. **Iran-war anchor re-verify** — verified-as-of 2026-05-04, refresh boundary 2026-05-11 minimum OR earlier on visible kinetic state-change.
6. **CARL ↔ WALTER LIAISON calibration cycle 1** — primary trigger 2026-05-19 (14d calendar from 5/5) OR N=20 BOARD dispositions (early-fire).
7. **BRENT ↔ WALTER LIAISON calibration cycle 1** — N=15 forward BOARD dispositions OR 21 days from 2026-05-06, whichever first. ETA May 20-27.
8. **RED ↔ WALTER LIAISON calibration cycle 1** — synced with BRENT cycle 1 ETA May 20-27. Trigger conditions (whichever first): FALSIFICATION_TRIGGERS first auto-dispatch OR v0.8 lands OR CHG-RED-024 BRENT response.

**3-way joint proposal pipeline (from yesterday morning):**
9. **CARL drafts §1 + §3a + §3c + §4 sections** — CARL self-task per Turn 7, ETA this week.
10. **WALTER stitches 3-way at `design/JOINT_PROPOSAL_2026-05-06_walter_carl_brent.md`** — when CARL section file lands.
11. **Will sign-off on 3-way §2 stack** — 4 items.
12. **WALTER lands FORMAT_SPEC v0.8** — post-sign-off.
13. **WALTER updates SIGNAL_PROCESSING_CHECKLIST.md** for v0.8 + Phase 2.5 event-window step — post-sign-off.

**2-way RED+WALTER joint proposal pipeline (NEW today):**
14. **Will sign-off on RED+WALTER 2-way §2/§3/§4.3/§4.4/§5 batch** — 5 items.
15. **WALTER stitches 2-way at `design/JOINT_PROPOSAL_2026-05-06_red_walter.md`** — once RED's §1+§4 file is committed (RED-OC next boot).
16. **WALTER FALSIFICATION_TRIGGERS at-dispatch eval implementation** — post-§2 sign-off; spawn-protocol step 6b extension + parallel ledger scaffold.
17. **WALTER ROUTING_TABLE v0.6→v0.7 + CHECKLIST Phase 2 steps 5-7 add** — post-§3 sign-off.
18. **WALTER unanimity_state v0.9 stack readiness** — post-§5 sign-off + post-v0.8-land.
19. **WALTER network_uncertainty_peak closeout flag** — lightweight, ships with §3.
20. **RED CLAUDE.md boot-step b add** — RED post-§4.3 sign-off.
21. **RED MEMORY.md 97%-routing-target entry** — RED post-§4.4 sign-off.

**WALTER self-tasks this week (no sign-off needed):**
22. **BOARD_CONSUMPTION_SPEC v0.2 dual-pattern doc** — CARL consumer-domain + BRENT energy-domain templates documented.
23. **CROSS_REFS/CARL.md cache scaffold** — populate from CARL THESIS.md + workbook indexers.
24. **CROSS_REFS/BRENT.md cache scaffold** — populate triggered by thesis v1.1→v2.0 bump 5/6.
25. **CROSS_REFS/RED.md cache scaffold** — populate from handoff_WALTER/README.md 12-anchor identifier index. **Unblocks complete-CHG-RED-backfill.**
26. **Complete CHG-RED-backfill via diff-file** — post-CROSS_REFS/RED.md; produces `handoff_RED/CHALLENGES_BACKFILL_diff.tsv`; RED applies at next boot.

**Post-sign-off WALTER self-tasks:**
27. **EVENT_WINDOW_STATE.md scaffold** — post-Will-sign-off on §2d BURST_WINDOW (3-way).
28. **FILTER_SPEC.md update** — Tuning Rules sub-section for OPEN-window dispatch posture.
29. **ROUTING_TABLE v0.7** — add "By Boundary Threshold" section with BRENT-IMMEDIATE 8-row threshold list (3-way §2c).

**BRENT self-tasks (his next session):**
30. **BRENT CLAUDE.md spawn-protocol delta** — event_window=open behavior + BRENT-specific BOARD-consumption boot-step.
31. **BRENT DATA_RELEASE_CALENDAR.md** — workbook/DATA_RELEASE_CALENDAR.md covering EIA WPSR / Baker Hughes / OPEC MOMR / IEA OMR / CFTC COT / Platts.

**CARL self-tasks:**
32. **CARL DATA_RELEASE_CALENDAR.md** — extends EARNINGS_WATCH_Q1.md to year-rolling.

**HAWK reconciliation (when HAWK refreshes):**
33. **Archive HAWK-proxy synthesis** to `design/history/hawk_proxy_synthesis_2026-05-05.md`.
34. **Update KB-BRT-NNN cross-refs** to point at HAWK output for kinetic doctrine; BRENT oil-substance interpretations stay primary.

**Next-LIAISON channel candidates (per Will direction msg 1366 + this session's RED resolution):**
35. **REGINALD LIAISON** — **NEW top of unblocked queue.** Bank/CRE/earnings primary. Heavy BOARD pickup. CC-side, easy mechanics.
36. **NEXUS LIAISON** — high-leverage, blocked on NEXUS spawn.
37. **HENRY LIAISON** — post-REGINALD. POSITIONING_VALUATION cluster owner.
38. **BROCK LIAISON** — mid-priority. PC-stress cluster owner.

**Cluster / domain follow-ups (carry-forward):**
39. **OZK Q1 post-mortem** — REGINALD pickup pending since Apr 16.
40. **ROAD Act House reconciliation** — BARON pickup.
41. **HENRY SIGNAL_INTAKE.md** — saved-to-disk pending.
42. **Tier 2 staleness** (ZHAO 34d / SHADE 6+wk / OTTO 21d / ORACLE 35d / FERT 6+wk / ATHENA 7+wk / CRUISE 6+wk / DARWIN dormant).
43. **Pandemic-meta-cluster informal watch** — 14-day window for 1-2 more institutional-primary signals.

**Refactor open items:**
44. **"verified-as-of" pattern extension** — second anchor candidate (Fed-framework / BOJ / OPEC+).
45. **design/STATE.md maintenance discipline** at closeout.
46. **Lead-paragraph regeneration cadence** decision.

**Design / governance backlog:**
47. **Filter v2 Segment D** — option A confidence_note; ~1hr.
48. **Signal Registry v2** — deferred (storage / concurrency).
49. **COP refresh resume trigger** — Will direction needed (paused since Apr 14).
50. **Autonomous news-scan policy** — codify scan-cadence + verify-research mandatory on novelty-claim items.
51. **HAWK-proxy synthesis policy** — when default-spawn vs wait for actual refresh. Partially superseded by BRENT thesis v2.0 reconciliation rule.
52. **CONSUMER_STAGFLATION 5-axis sub-cluster spawn decision** — Will sign-off needed.

## OPEN DESIGN DECISIONS (need Will — also tracked in MEMORY.md)

- **3-way JOINT_PROPOSAL §2 stack sign-off** (4 items: §2a FORMAT_SPEC v0.8 / §2b scheduled-scan budget / §2c BRENT-IMMEDIATE threshold list / §2d BURST_WINDOW protocol).
- **2-way RED+WALTER JOINT_PROPOSAL sign-off** (5 items: §2 / §3 / §4.3 / §4.4 / §5).
- **Repo-root stitch timing** — stitch now (gives unified read) or hold until per-§ sign-off (cleaner state)?
- **Next-LIAISON priority** — REGINALD (CC-side, unblocked, top of queue) vs NEXUS (blocked on spawn) vs HENRY (post-REGINALD) vs BROCK (mid).
- **CONSUMER_STAGFLATION 5-axis sub-cluster spawn** — promote to v0.2 OR hold informal in-body-tagging?
- **HAWK-proxy synthesis frequency** — default-spawn when OC primary stale > X days OR wait for actual refresh? Partially superseded by BRENT thesis v2.0 reconciliation rule.
- **Pass 4 of 5/5 morning's cluster refactor** — IRAN_HORMUZ + POSITIONING_VALUATION sub-cluster breakdown? Defer until further intake.
- **FED_FRAMEWORK rename to UST_PLUMBING** — watch threshold for v0.2 taxonomy edit.
- **Cluster status flags** (🟢/🟡/🔴/⚫) — reserved for v0.2.
- **"verified-as-of" pattern extension** — second anchor candidate?
- **MEMORY.md vs LAST_COMPLETION.md duplication** — Pattern D, Pass 5? (Partially resolved 5/5 — MEMORY NEXT SESSION trimmed; full Pattern-D resolution still open.)
- **Lead-paragraph regeneration cadence** — every closeout or only on visible state-change?
- **Filter v2 Segment D** — DECIDED option A; implementation deferred ~1hr.
- **Autonomous news-scan policy** — codify scan-cadence + verify discipline.
- **BOARD_CONSUMPTION rollout cadence** — Will hand-routing; durable rollout = 14 agent CLAUDE.md propagation. CARL + BRENT mostly done; RED pending §4.3 sign-off; remaining 11.
- **COP refresh resume** — paused since Apr 14.
- **NEXUS cluster classification cadence** — informal cluster tracking via STATUS, or NEXUS-spawn forcing function?

---

*Maintenance note: this file is overwritten each session per CLAUDE.md spawn protocol step 15. The FOLLOW-UP and OPEN DESIGN DECISIONS sections are the load-bearing carry-forward — every closeout copies open items forward and removes resolved ones. Don't append; don't keep historical sessions here; that's what `SESSION_LOG.md` is for.*

*Resolved this session (removed from carry-forward): "RED LIAISON setup" + "RED revival blocker" + "REQ-RED Wirth-1970s steelman supplement" + "WALTER joint-proposal §2+§3+§5 sections drafted" + "bifurcation cluster classification empirical pass."*
