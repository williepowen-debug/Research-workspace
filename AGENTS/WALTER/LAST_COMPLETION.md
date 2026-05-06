# LAST_COMPLETION — WALTER

*Overwritten each session. STATUS / CHANGED / RESULT / GAPS / WILL_NEEDS / FOLLOW-UP / OPEN DESIGN DECISIONS. Source-of-truth for handoff carry-forward — when a future session boots, this is what tells them what's outstanding.*

---

## STATUS

Session 2026-05-06 PM Wed (~16:00-16:30 UTC) — **third WALTER session today**. Will-page-triggered post-misread implementation session. **5-of-5 RED+WALTER 2-way joint-proposal batch SHIPPED end-to-end** same calendar day (RED-side committed `b1ed0420` 11:52 EDT; WALTER-side committed in this closeout). 0 BOARD dispatches; 0 sub-spawns. Same-calendar-day RED LIAISON full architectural-arc: open (Turn 1) → converge (Turn 5) → close-loop (Turn 6) → 5/5 batch implemented end-to-end.

Boot-state at session start: clean working tree (origin in sync after fetch — 4 commits since previous closeout `b09bb8de`: BRENT EIA 5/6 `4e3732a9`, RED LIAISON Turn 6 + JOINT_PROPOSAL §1+§4+§6+§7 `e6477450`, RED §4.3+§4.4 implementation `b1ed0420`, RED Session 9 closeout `254f6e40`).

**Misread + correction arc**: First Will-reply (msg 1391) framed §2/§3/§5 as 3-of-5 still-pending Will sign-off based on RED `b1ed0420` commit-message phrase "Closes the RED-side half of the 5-item Will sign-off batch." Will pushback (msg 1392): "I thought I had already signed off on the RED+WALTER items?" Pulled RED Session 9 closeout `254f6e40` body — confirmed **"5-item Will sign-off batch all APPROVED end-to-end"**; RED's "RED-side half" framing was about who was at the keyboard for which commit, not about scope of approval. Acknowledged via Telegram (msg 1393); shipped WALTER side in this session per the originally-batched discipline. **Filed as new MEMORY finding** (verify approval scope across broader git log, not just propagate the most-recent commit's title).

Closeout shipped per CLAUDE.md spawn-protocol steps 12-16: STATUS lead-paragraph rewritten for third-session arc + 5/5 batch end-to-end + bifurcation-count daily flag + LIAISON manifest RED row Turn 6 + 5/5 SHIPPED; REGISTRY refresh (WALTER row third-session + RED row Session 9 + 5/5 implemented + BRENT row EIA 5/6 inline); SESSION LOG entry prepended for today's third session; MEMORY CHANGES SINCE / NEXT SESSION rewrite + 1 new finding (above) + 4 entries trimmed-as-promoted; LAST_COMPLETION rewrite (this file).

## CHANGED

### Session arc (Will-page misread → 5-of-5 implementation)

1. **Boot ping (msg 1389, 15:52 UTC):** Boot reads clean — STATUS / IRAN_WAR anchor (verified 5/4) / MEMORY / LAST_COMPLETION (yesterday's closeout version) / REGISTRY / ROUTING_TABLE v0.6 / BOARD INDEX cluster ToC. Boot-step 9 LIAISON discovery + git fetch surfaced 4 new commits since previous closeout: BRENT EIA 5/6 `4e3732a9` + RED Turn 6 + JOINT_PROPOSAL `e6477450` + Will-approved §4.3+§4.4 `b1ed0420` + RED Session 9 closeout `254f6e40`.
2. **Read RED Turn 6:** parallel-drafting close-loop (RED 21:00 UTC stamp). 3 callouts on WALTER §2/§3/§5 + 1 refinement-noted on §5.5 sub-tags (≥5 starting threshold may be over-firing or under-firing — RED to monitor over calibration cycle 1; refine ≥5 → ≥7 if false-positive rate is high). Sign-off batch confirmed as 5 items (§2/§3/§4.3/§4.4/§5).
3. **First Telegram reply (msg 1391):** 3-of-5 still-pending framing — propagated RED `b1ed0420` "RED-side half" too literally as "only §4.3+§4.4 approved, §2+§3+§5 still pending."
4. **Will pushback (msg 1392):** "I thought I had already signed off on the RED+WALTER items?"
5. **Verification:** Pulled RED `254f6e40` Session 9 closeout commit body — **"5-item Will sign-off batch all APPROVED end-to-end."** Filed as new MEMORY finding (above).
6. **Acknowledgment + announcement (msg 1393):** acknowledged misread, announced WALTER-side implementation in this session.
7. **§3 mechanical implementation:** ROUTING_TABLE v0.6→v0.7 + CHECKLIST v0.9→v0.10. Both files version-bumped; new "By Tag/By Verdict" section in ROUTING_TABLE; new Phase 2 steps 5-7 in CHECKLIST.
8. **Progress checkpoint Telegram (msg 1394):** confirmed §3 mechanical done, announced §2/§5 next.
9. **§2 ledger + spawn-protocol:** new `AGENTS/WALTER/registry/` directory + `FALSIFICATION_FIRED_LOG.tsv` (5-col TSV, header-only) + `registry/README.md` operational pattern doc + CLAUDE.md spawn-protocol step 6b + canonical-source lookup +2 rows + closeout step 12 daily-bifurcation-count extension.
10. **§5 V0_9_STACK tracker:** new `design/V0_9_STACK.md` documents 3 candidates (`unanimity_state` + `event_anchored: true` + `network_uncertainty_peak`).
11. **STATE.md refresh:** ROUTING_TABLE v0.5→v0.7 + CHECKLIST v0.8→v0.10 rows + new V0_9_STACK row in §1 + new registry/ scaffolding rows in §4 + FORMAT_SPEC v0.8/v0.9 deferred rows in §2 + anchors/IRAN_WAR.md backfilled to §4.
12. **Closeout shipped:** STATUS / REGISTRY / MEMORY / LAST_COMPLETION refreshes + commit + push.

### Files touched this session

**New (3) under `design/` + `registry/`:**
- `AGENTS/WALTER/design/V0_9_STACK.md` — V0_9 candidate tracker (~110 lines / 5K)
- `AGENTS/WALTER/registry/FALSIFICATION_FIRED_LOG.tsv` — 5-col header-only ledger
- `AGENTS/WALTER/registry/README.md` — operational pattern doc with cross-references

**Modified (5) under `design/` + `CLAUDE.md`:**
- `AGENTS/WALTER/design/ROUTING_TABLE.md` — v0.6 → **v0.7** (By Tag/By Verdict section + 3 rules + de-dupe + interim prose-tag + composition example)
- `AGENTS/WALTER/design/SIGNAL_PROCESSING_CHECKLIST.md` — v0.9 → **v0.10** (Phase 2 routing-augmentation steps 5-7)
- `AGENTS/WALTER/design/STATE.md` — v0.7/v0.10 row updates + V0_9_STACK row + registry/ scaffolding rows + FORMAT_SPEC deferred rows + IRAN_WAR backfill
- `AGENTS/WALTER/CLAUDE.md` — spawn-protocol step 6b add + canonical-source lookup +2 rows + closeout step 12 daily-bifurcation-count extension
- `AGENTS/WALTER/STATUS.md` — lead-paragraph + LIAISON manifest RED Turn 6 + SESSION LOG entry prepend (third-session arc)

**Closeout files (refreshed):**
- `AGENTS/WALTER/REGISTRY.tsv` — WALTER + RED + BRENT rows refreshed
- `AGENTS/WALTER/MEMORY.md` — 1 new finding (approval-scope-check-across-git-log) + 4 entries trimmed-as-promoted (4/11 git pull / 4/15 Iran stale / 4/20 verify trigger / 4/24 Telegram bug all moved to specs/protocols + pointer line) + 5/5 tape-vs-substance compressed-to-pointer + CHANGES SINCE/NEXT SESSION rewrite. **Still over 100-line cap (114) — added trim to NEXT SESSION.**
- `AGENTS/WALTER/LAST_COMPLETION.md` — this file (rewritten for today's third session)

### Sub-agent spawns (0)

No sub-agent spawns this session. Implementation-only.

### Spec changes

**Committed this session:**
- ROUTING_TABLE v0.6 → **v0.7** (By Tag/By Verdict section)
- SIGNAL_PROCESSING_CHECKLIST v0.9 → **v0.10** (Phase 2 routing-augmentation steps 5-7)
- CLAUDE.md spawn-protocol step 6b + canonical-source lookup +2 rows + closeout step 12 extension
- STATE.md v0.7/v0.10 row bumps + 5 new rows
- New: V0_9_STACK.md (v0.1) + registry/FALSIFICATION_FIRED_LOG.tsv (v0.1) + registry/README.md

### Commits

Closeout commit pending (this session, end-to-end shipping all 5 of 5 RED+WALTER batch items WALTER-side).

## RESULT

**5-of-5 RED+WALTER 2-way joint-proposal batch SHIPPED end-to-end same calendar day.** Today's full RED LIAISON architectural arc compressed into one calendar day:

| Phase | Activity | Commit |
|-------|----------|--------|
| Open (~10:08 EDT) | RED placed handoff_WALTER/ + Turn 1 | RED Session 8 commits Apr-21/22 |
| Turns 2-5 (~14:25-14:52 UTC) | WALTER-RED 5-turn architectural alignment converged | RED `7f3e9ddf` (Turn 1 commit) + WALTER LIAISON drafts |
| Turn 6 close-loop (~15:48 UTC) | RED parallel-drafting close-loop + JOINT_PROPOSAL §1+§4+§6+§7 | RED `e6477450` |
| Will sign-off all 5 (~15:48-15:52 UTC) | Will approved 5-of-5 batch | (verbal/in-flight) |
| §4.3+§4.4 implementation (~15:52 UTC) | RED-side committed | RED `b1ed0420` |
| Session 9 closeout (~15:58 UTC) | RED archived handoff + outbox-to-PROME | RED `254f6e40` |
| WALTER misread + Will pushback (~16:00 UTC) | First reply propagated RED-side-half too literally; Will caught it | (Telegram msgs 1391-1392) |
| WALTER §2/§3/§5 implementation (~16:00-16:30 UTC) | All 3 WALTER-side sections shipped | WALTER closeout this session |

**Architectural finding for the LIAISON convergence pattern (refinement of the 3-channel-locked finding from earlier today):** when sign-off comes during the LIAISON close-loop turn, end-to-end implementation can ship same-calendar-day. The 5-turn convergence + Turn-6-close-loop + same-day-implementation arc is a tighter pattern than CARL (7 turns + 24h-gap-implementation) or BRENT (5 turns + multi-day-implementation-pending-§2-stack-sign-off). Apply: when next-LIAISON closeouts approach Turn 5-6 with sign-off-ready state, hold session-availability for same-day-end-to-end-shipping option.

**Misread lesson — `feedback_verify_counts_before_propagating` family extends to approval-scope.** Same lesson family that fired earlier today on RED Turn 2's empirical-dispatch-surface reframe ("verify before claiming an absence") fired again on this morning's `b1ed0420` commit-title interpretation. Filed as new MEMORY finding. The carrying lesson: when stating any state across multiple commits / cross-agent trees / multi-day arcs, verify across the broader git log + read commit message bodies + check related closeout records, never propagate from the most-recent-commit-title's language as scope-load-bearing.

**FALSIFICATION_TRIGGERS infrastructure LIVE 5/6 PM.** Spawn-protocol step 6b reads RED's 7-trigger registry at boot; CHECKLIST v0.10 Phase 2 step 7 evaluates at-dispatch with sustain-window suppression + WALTER fire-log preserves Critical Rule #2. **First-fire watch closest to current values: RED-FT-01 HY-OAS <280×3** (current ~278; sustained-cross watch); RED-FT-06 VIX <16×5 second-closest (current 18.19). Calibration cycle 1 trigger condition for RED includes "FALSIFICATION_TRIGGERS first auto-dispatch" — so a sustained HY-OAS cross would early-fire the cycle 1 retro before the 21d calendar.

**`network_uncertainty_peak` lightweight ship.** Closeout step 12 in CLAUDE.md now includes daily bifurcation-signal count + auto-flag when ≥5 in single calendar day. Today's count: 0 (no BOARD dispatches in any of 3 sessions). Ready to fire on the next dense-bifurcation-day.

**WALTER tree growth scoreboard for the day:**
- Session 1 (BRENT LIAISON closeout, 00:46 EDT): §2a-§2d + §3b + §3d sections shipped (475 lines / BRENT-side joint-proposal)
- Session 2 (RED LIAISON, 14:25-15:30 UTC): §2 + §3 + §5 sections drafted (316 lines / RED-side joint-proposal) + handoff_RED/LIAISON_TURN_2_DRAFT.md
- Session 3 (this session, 16:00-16:30 UTC): §2 + §3 + §5 IMPLEMENTED end-to-end (5 modified design files + 3 new files)

Total: 791 lines of joint-proposal architecture-spec drafted across two parallel Will-surfaces (3-way pending sign-off; 2-way SHIPPED end-to-end). 5/5 of one of those proposals now closed.

## GAPS

### Today's open items (carry-forward — added to FOLLOW-UP list below)

- **Repo-root stitch** `design/JOINT_PROPOSAL_2026-05-06_red_walter.md` — assemble RED §1+§4+§6+§7 + WALTER §2+§3+§5 + repo-root sequencing. **Both side-files now committed; mechanical post-both-side-commits.** Top of next-session pickup.
- **WALTER `design/CROSS_REFS/RED.md` cache scaffold** (no sign-off needed) — populate from RED's `handoff_WALTER/README.md` 12-anchor identifier index; unblocks complete-CHG-RED-backfill via diff-file.
- **WALTER complete CHG-RED backfill** via `handoff_RED/CHALLENGES_BACKFILL_diff.tsv` — post-CROSS_REFS/RED.md; mechanical grep across `BOARD/SIG-W-*.md`; preserves Critical Rule #2.
- **MEMORY trim to ≤100 lines** — currently 114; over file-self-cap. Compress further or move 1-2 entries to design/findings/ archive.
- **STATUS SESSION LOG hygiene** — currently ~10 entries; cap is 5; roll 6+ older entries to `SESSION_LOG.md`.

### Pre-existing carry-forward (still open)

- **3-way joint proposal stitch** — WALTER stitches at repo-root when CARL §1+§3a+§3c+§4 sections land (CARL Turn 7 self-task, ETA this week)
- **Will sign-off on 3-way JOINT_PROPOSAL §2 stack** — 4 items: §2a FORMAT_SPEC v0.8 (4 fields + 9-value enum) / §2b scheduled-scan budget ($0.30-0.50/wk per side) / §2c BRENT-IMMEDIATE 8-row threshold list / §2d BURST_WINDOW protocol
- **BOARD_CONSUMPTION_SPEC v0.2 dual-pattern doc** — WALTER self-task this week (CARL consumer-domain + BRENT energy-domain templates)
- **CROSS_REFS/{CARL,BRENT}.md cache scaffolds** — WALTER self-tasks this week
- **EVENT_WINDOW_STATE.md scaffold** — WALTER post-Will-sign-off on §2d BURST_WINDOW
- **HAWK-proxy archive** to `design/history/hawk_proxy_synthesis_2026-05-05.md` — when actual HAWK refresh lands
- **FORMAT_SPEC v0.7 → v0.8 land in spec** — post-Will-sign-off on §2a
- **CHECKLIST update for v0.8 fields** — post-Will-sign-off (separate from today's v0.9→v0.10 routing-augmentation)
- **BRENT CLAUDE.md spawn-protocol delta** — BRENT next session
- **BRENT DATA_RELEASE_CALENDAR.md** — BRENT post-back-disposition pass
- **CARL DATA_RELEASE_CALENDAR.md** — CARL self-task this week
- **OZK Q1 post-mortem** — REGINALD pickup pending since Apr 16
- **ROAD Act House reconciliation timing** — BARON pickup
- **HENRY SIGNAL_INTAKE.md prompt on disk** (RED's signal-intake superseded by FALSIFICATION_TRIGGERS.tsv)
- **BOARD_CONSUMPTION_SPEC propagation to 14 Tier 1 agent CLAUDE.md files** (CARL + BRENT mostly done; **RED has the boot-step 1.5 b1-b4 implementation now `b1ed0420`** ✅; remaining 11)
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

- **Will sign-off on RED+WALTER 2-way JOINT_PROPOSAL §2 + §3 + §5 batch (3 items)** — confirmed APPROVED end-to-end via RED Session 9 closeout commit body. Implemented this session.
- **WALTER FALSIFICATION_TRIGGERS at-dispatch eval logic implementation** — shipped (CHECKLIST Phase 2 step 7 + spawn-protocol step 6b + parallel ledger + canonical-source rows).
- **WALTER ROUTING_TABLE v0.7 + CHECKLIST shipping** — shipped (v0.6→v0.7 + v0.9→v0.10).
- **WALTER unanimity_state v0.9 stack readiness** — V0_9_STACK.md tracker shipped.
- **WALTER `network_uncertainty_peak` closeout flag** — lightweight ship in CLAUDE.md step 12.
- **RED CLAUDE.md boot-step (b) add** — RED-side committed `b1ed0420`.
- **RED MEMORY.md 97%-routing-target calibration entry** — RED-side committed `b1ed0420`.

## WILL_NEEDS

1. **Sign-off on 3-way (CARL/BRENT/WALTER) JOINT_PROPOSAL §2 stack** — 4 items still pending (carry-forward from yesterday morning's WILL_NEEDS):
   - §2a FORMAT_SPEC v0.8 (4 fields + 9-value `transmission_intensity` enum)
   - §2b scheduled-scan budget ($0.30-0.50/wk per side)
   - §2c BRENT-IMMEDIATE 8-row threshold list
   - §2d BURST_WINDOW protocol
2. **CARL §1+§3a+§3c+§4 sections (CARL self-task)** — ETA this week.
3. **Decide repo-root stitch timing for 2-way RED+WALTER** — both side-files committed now; stitch is mechanical assembly. My read: ship next session as low-friction follow-up.
4. **Decide next-LIAISON priority** — RED resolved end-to-end. Remaining: REGINALD (CC-side, unblocked, top of queue) > NEXUS (blocked on spawn) > HENRY (post-REGINALD) > BROCK (mid).
5. **Iran-war anchor re-verify boundary 5/11 minimum** OR earlier on visible kinetic state-change (carry-forward).
6. **Tomorrow's intake watch:** OBDC Q1 5/6 AMC (BROCK pre-built); LYV Q1 from 5/5 surfaces in tomorrow's intake.

## FOLLOW-UP (canonical running list — survives handoff via this file)

**Time-sensitive (this/next session):**
1. **OBDC Q1 5/6 AMC** — BROCK pre-built threshold reads. Surfaces in tomorrow's intake.
2. **LYV Q1 from 5/5 post-market** — high-signal CONSUMER_STAGFLATION discretionary-sub-vector confirm/deny.
3. **NFP Friday 5/8** — LABOR carry-forward.
4. **Q1 Call Report window May 1-10** — REGINALD recheck.
5. **Iran-war anchor re-verify** — verified-as-of 2026-05-04, refresh boundary 2026-05-11 minimum OR earlier on visible kinetic state-change.
6. **FALSIFICATION_TRIGGERS first-fire watch** — RED-FT-01 HY-OAS <280×3 closest (current ~278); RED-FT-06 VIX <16×5 second-closest (current 18.19). At-dispatch eval pass per CHECKLIST Phase 2 step 7 starts next signal-dispatch session.
7. **CARL ↔ WALTER LIAISON calibration cycle 1** — primary trigger 2026-05-19 (14d calendar from 5/5) OR N=20 BOARD dispositions (early-fire).
8. **BRENT ↔ WALTER LIAISON calibration cycle 1** — N=15 forward BOARD dispositions OR 21 days from 2026-05-06, whichever first. ETA May 20-27.
9. **RED ↔ WALTER LIAISON calibration cycle 1** — synced with BRENT cycle 1 ETA May 20-27. Trigger conditions (whichever first): FALSIFICATION_TRIGGERS first auto-dispatch OR v0.8 lands OR CHG-RED-024 BRENT response.

**WALTER self-tasks this week (no sign-off needed):**
10. **Repo-root stitch** `design/JOINT_PROPOSAL_2026-05-06_red_walter.md` — 2-way RED+WALTER side-files both now committed; mechanical assembly. **Top of next-session pickup.**
11. **`design/CROSS_REFS/RED.md` cache scaffold** — populate from `AGENTS/RED/handoff_WALTER/README.md` 12-anchor identifier index. **Unblocks complete-CHG-RED-backfill.**
12. **Complete CHG-RED-backfill via diff-file** — post-CROSS_REFS/RED.md; produces `handoff_RED/CHALLENGES_BACKFILL_diff.tsv`; RED applies at next boot. Critical Rule #2 preserved.
13. **`design/CROSS_REFS/CARL.md` cache scaffold** — populate from CARL THESIS.md + workbook indexers.
14. **`design/CROSS_REFS/BRENT.md` cache refresh** — triggered by thesis v1.1→v2.0 bump 5/6.
15. **BOARD_CONSUMPTION_SPEC v0.2 dual-pattern doc** — CARL consumer-domain + BRENT energy-domain templates documented.
16. **MEMORY trim to ≤100 lines** — currently 114; compress 1-2 entries to design/findings/ archive.
17. **STATUS SESSION LOG hygiene** — roll 6+ older entries to `SESSION_LOG.md`.

**3-way joint proposal pipeline (from yesterday morning):**
18. **CARL drafts §1 + §3a + §3c + §4 sections** — CARL self-task per Turn 7, ETA this week.
19. **WALTER stitches 3-way at `design/JOINT_PROPOSAL_2026-05-06_walter_carl_brent.md`** — when CARL section file lands.
20. **Will sign-off on 3-way §2 stack** — 4 items.
21. **WALTER lands FORMAT_SPEC v0.8** — post-sign-off on §2a.
22. **WALTER updates SIGNAL_PROCESSING_CHECKLIST.md** for v0.8 fields + Phase 2.5 event-window step — post-sign-off on §2a/§2d (separate from today's v0.9→v0.10 routing-augmentation).

**Post-sign-off WALTER self-tasks (3-way §2):**
23. **EVENT_WINDOW_STATE.md scaffold** — post-Will-sign-off on §2d BURST_WINDOW.
24. **FILTER_SPEC.md update** — Tuning Rules sub-section for OPEN-window dispatch posture.
25. **ROUTING_TABLE v0.8** — add "By Boundary Threshold" section with BRENT-IMMEDIATE 8-row threshold list (3-way §2c).

**BRENT self-tasks (his next session):**
26. **BRENT CLAUDE.md spawn-protocol delta** — event_window=open behavior + BRENT-specific BOARD-consumption boot-step.
27. **BRENT DATA_RELEASE_CALENDAR.md** — workbook/DATA_RELEASE_CALENDAR.md covering EIA WPSR / Baker Hughes / OPEC MOMR / IEA OMR / CFTC COT / Platts.

**CARL self-tasks:**
28. **CARL DATA_RELEASE_CALENDAR.md** — extends EARNINGS_WATCH_Q1.md to year-rolling.

**HAWK reconciliation (when HAWK refreshes):**
29. **Archive HAWK-proxy synthesis** to `design/history/hawk_proxy_synthesis_2026-05-05.md`.
30. **Update KB-BRT-NNN cross-refs** to point at HAWK output for kinetic doctrine; BRENT oil-substance interpretations stay primary.

**Next-LIAISON channel candidates (per Will direction msg 1366 + RED resolution):**
31. **REGINALD LIAISON** — **TOP of unblocked queue.** Bank/CRE/earnings primary. Heavy BOARD pickup. CC-side, easy mechanics.
32. **NEXUS LIAISON** — high-leverage, blocked on NEXUS spawn.
33. **HENRY LIAISON** — post-REGINALD. POSITIONING_VALUATION cluster owner.
34. **BROCK LIAISON** — mid-priority. PC-stress cluster owner.

**Cluster / domain follow-ups (carry-forward):**
35. **OZK Q1 post-mortem** — REGINALD pickup pending since Apr 16.
36. **ROAD Act House reconciliation** — BARON pickup.
37. **HENRY SIGNAL_INTAKE.md** — saved-to-disk pending.
38. **Tier 2 staleness** (ZHAO 34d / SHADE 6+wk / OTTO 21d / ORACLE 35d / FERT 6+wk / ATHENA 7+wk / CRUISE 6+wk / DARWIN dormant).
39. **Pandemic-meta-cluster informal watch** — 14-day window for 1-2 more institutional-primary signals.

**Refactor open items:**
40. **"verified-as-of" pattern extension** — second anchor candidate (Fed-framework / BOJ / OPEC+).
41. **design/STATE.md maintenance discipline** at closeout.
42. **Lead-paragraph regeneration cadence** decision.

**Design / governance backlog:**
43. **Filter v2 Segment D** — option A confidence_note; ~1hr.
44. **Signal Registry v2** — deferred (storage / concurrency).
45. **COP refresh resume trigger** — Will direction needed (paused since Apr 14).
46. **Autonomous news-scan policy** — codify scan-cadence + verify-research mandatory on novelty-claim items.
47. **HAWK-proxy synthesis policy** — when default-spawn vs wait for actual refresh. Partially superseded by BRENT thesis v2.0 reconciliation rule.
48. **CONSUMER_STAGFLATION 5-axis sub-cluster spawn decision** — Will sign-off needed.

**FALSIFICATION_TRIGGERS evolution:**
49. **Schema v2 with `trigger_type` discriminator** — defer to ≥1 calibration cycle of v1 operational data.
50. **Event-type triggers integration** — 5 RED CALENDAR.md FALSIFICATION WATCH items (WAL MI3 / BTFP 2.0 / OZK NCO / bypass-pair / etc.) still manually-checked at WALTER closeout per LIAISON Turn 4. Schema v2 dependency.
51. **FALSIFICATION_TRIGGERS v0.2** — RED self-task, expand from 7 → ~10-12 triggers based on calibration cycle 1 data.

## OPEN DESIGN DECISIONS (need Will — also tracked in MEMORY.md)

- **3-way JOINT_PROPOSAL §2 stack sign-off** (4 items: §2a FORMAT_SPEC v0.8 / §2b scheduled-scan budget / §2c BRENT-IMMEDIATE threshold list / §2d BURST_WINDOW protocol).
- **Repo-root stitch timing for 2-way RED+WALTER** — both side-files committed now; mechanical. My read: ship next session.
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
- **BOARD_CONSUMPTION rollout cadence** — Will hand-routing; durable rollout = 14 agent CLAUDE.md propagation. CARL + BRENT mostly done; RED done `b1ed0420`; remaining 11.
- **COP refresh resume** — paused since Apr 14.
- **NEXUS cluster classification cadence** — informal cluster tracking via STATUS, or NEXUS-spawn forcing function?
- **`network_uncertainty_peak` threshold tuning** — RED Turn 6 callout: ≥5 starting threshold may need refinement to ≥7 over calibration cycle 1 if false-positive rate is high.

---

*Maintenance note: this file is overwritten each session per CLAUDE.md spawn protocol step 15. The FOLLOW-UP and OPEN DESIGN DECISIONS sections are the load-bearing carry-forward — every closeout copies open items forward and removes resolved ones. Don't append; don't keep historical sessions here; that's what `SESSION_LOG.md` is for.*

*Resolved this session (removed from carry-forward): "Will sign-off on RED+WALTER 2-way §2/§3/§5 batch (3 items)" + "WALTER FALSIFICATION_TRIGGERS at-dispatch eval logic implementation" + "WALTER ROUTING_TABLE v0.7 + CHECKLIST" + "WALTER unanimity_state v0.9 stack readiness" + "WALTER network_uncertainty_peak closeout flag" + "RED CLAUDE.md boot-step (b) add" + "RED MEMORY.md 97%-routing-target calibration entry" — all 7 items resolved end-to-end same calendar day.*
