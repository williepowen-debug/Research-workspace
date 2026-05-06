# LAST_COMPLETION — WALTER

*Overwritten each session. STATUS / CHANGED / RESULT / GAPS / WILL_NEEDS / FOLLOW-UP / OPEN DESIGN DECISIONS. Source-of-truth for handoff carry-forward — when a future session boots, this is what tells them what's outstanding.*

---

## STATUS

Session 2026-05-06 early morning Wed (~03:00-05:00 UTC) — Will-triggered BRENT LIAISON channel session. **5-turn architectural-thread convergence** (BRENT 1/3/5; WALTER 2/4) — half a cycle faster than CARL's 7-turn dialog 24h earlier. **0 BOARD dispatches** (closeout-arc focused on architectural alignment + Turn-4 self-task execution, not new dispatches). ~$0.10 in tokens for sub-spawns. **BRENT shipped 6 parallel commits** during/after the dialog: thesis v1.1→v2.0 + 47-signal back-disposition pass + JOINT_PROPOSAL §1.1+§2e+§3e+§4+§5 sections + FLOW.tsv outbound expansion + STATUS LIAISON infra + Turn 5 wrap.

Boot-state at session start: clean working tree (origin = HEAD `a97dff17`), BRENT files untracked from 5/5 mid-session work. Pull was Already up to date.

Closeout shipped per CLAUDE.md spawn-protocol steps 12-16: STATUS lead-paragraph + manifest LIAISON BRENT row PENDING_NEXT_SESSION → ACTIVE Turn 5 closed; NETWORK AWARENESS regen (BRENT moves to ≤7d active, WALTER moves to ≤7d active); SESSION LOG entry; REGISTRY refresh (BRENT row + WALTER row); MEMORY CHANGES SINCE / NEXT SESSION rewrite + 3 new findings; LAST_COMPLETION rewrite (this file).

## CHANGED

### Session arc (architectural-alignment + Turn-4 follow-ups + parallel BRENT execution)

1. **Boot ping (msg 1349, 02:52 UTC):** Boot reads clean — STATUS / IRAN_WAR anchor / MEMORY / LAST_COMPLETION / REGISTRY / ROUTING / BOARD INDEX cluster ToC. Discovered BRENT had committed `707a2f79` (channel scaffold + Turn 1 + STATUS retro-tag of -012 + BOARD_LOG scaffold) at 5/5 ~22:49 UTC — ~3h after my closeout. BRENT files untracked because BRENT-OC hadn't pushed yet.
2. **Will pick A (msg 1352)** — draft Turn 2 reply. Generated `route_log_brent_slice.tsv` (48 BRENT-routed signals Apr 14 → 5/5, 35 primary + 13 info). Drafted Turn 2 in WALTER tree at `handoff_BRENT/LIAISON_TURN_2_DRAFT.md` (~7KB; answers Q1 slice deliverable, Q2 cosign as 3rd agent + push-back on `refining_margin_pass_through`, Q3 substance-fold authoritative + narrative-with-placeholder-caveat pending NEXUS, Q4 accept all 8 thresholds with 2 redlines, Q5 BURST_WINDOW state machine surfaced as joint-proposal §2d candidate, Q6 BRENT FLOW.tsv as canonical source, Q7 5 questions back).
3. **Will copies Turn 2 to BRENT tree manually + BRENT ships Turn 3** (file mtime 03:10 UTC; Turn 3 stamp 04:00 UTC). Turn 3 substantive: accepts both my redlines + push-back; **Q8 Wirth magnitude 0.6× with 5/12 features-present structural decomposition** (5 present: ME shock + oil-price direction + refining margin compression + jet fuel substitution + mechanism analog; 7 attenuated/absent: wage-spiral mechanism, US net-exporter, SPR/IEA cushion, demographic, energy intensity, Fed credibility, smaller price magnitude); Q9 tape-vs-substance read mixed (i)+(iii)+(ii), reject (iv); Q10 HAWK-proxy useful for events less for doctrine, HAWK supersedes proxy on refresh; Q11 `energy_transmission` accepts 8-value with 2 add-ons (`refining_capacity` + `freight_premium`) + rename `inventory_drawdown` → `inventory_dynamics`; Q12 BOARD consumption (c) hybrid with 6-row signal-type triage; 3 close-loop questions Q13-Q15.
4. **Will direct-write auth (msg 1359 "ah you write directly")** — drafted Turn 4 in WALTER tree, then appended to BRENT's LIAISON.md directly (file 318→424 lines). Turn 4: substantive accepts on Wirth decomposition for RED steelman; HAWK-proxy archive location decided (`design/history/hawk_proxy_synthesis_2026-05-05.md`); BURST_WINDOW state machine codified (BRENT-declares-open / WALTER-declares-close after ≥48h stable); BOARD_CONSUMPTION_SPEC v0.2 dual-pattern; answered Q13-Q15 (WALTER stitches; cycle 1 = N=15 forward post-back-pass OR 21d; BURST_WINDOW declared on announcement per asymmetric cost). One close-loop Q16 — v0.8 vs v0.9 surface mechanics.
5. **Will direction "yes lets keep going" (msg 1360)** — drafted WALTER §2a-§2d + §3b + §3d sections at `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-05_walter_sections.md` (was 277 lines from Phase 1 scaffolding 5/5, now 475 lines: added §2c BRENT-IMMEDIATE threshold list + §2d BURST_WINDOW state machine + §5 v0.9 future-work + extended §3d for BRENT cache + updated §2a enum 8→9 values with `lng_substitution`).
6. **3 Turn-4 self-tasks shipped:** SIG-W-20260505-009 dispatch_note retro-tag (confidence 0.85→0.75 + corporate-amplification-bias flag + BRENT 5/12-features-present decomposition reference); REQ-RED outbox supplement (full BRENT decomposition table appended); ROUTING_TABLE v0.5→v0.6 (Iran-cluster CARL-info override + boundary-trigger threshold-cross sub-rule).
7. **Will surfaces BRENT shipped Turn 5 + 6 commits in parallel (msg 1367):** BRENT thesis v1.1→v2.0 + 47-signal back-disposition + JOINT_PROPOSAL §1.1+§2e+§3e+§4+§5 sections + FLOW.tsv expansion + STATUS infra + Turn 5 wrap. Turn 5 closes Q16 with (a) accept (single 3-way proposal w/ §5 future-work) + suggested §5.1/§5.2/§5.3/§5.4 sub-structure. Architectural thread closed.
8. **Will direction next-LIAISON priorities (msg 1366):** ranked Tier 1 (RED + NEXUS, blocked on revival/spawn) + Tier 2 (REGINALD top of unblocked queue, BROCK + HENRY behind). LABOR/SAM/VIOLET hold per CARL Turn 5 + my analysis.
9. **Will closeout green light (msg 1365 "no we are ready to close out")** → this commit.

### Files touched this session

**Modified (4):**
- `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-05_walter_sections.md` — 277 → 475 lines (added §2c + §2d + §5 + extended §3d for BRENT + updated §2a 9-value enum)
- `AGENTS/WALTER/design/ROUTING_TABLE.md` — v0.5 → v0.6 (Iran-cluster CARL-info override + boundary-trigger threshold-cross sub-rule)
- `AGENTS/WALTER/outbox/REQ-RED-20260505-wirth-1970s-analog-steelman-falsification.md` — appended BRENT 5/12-features-present decomposition supplement
- `BOARD/SIG-W-20260505-009-chevron-ceo-wirth-milken-bloomberg-physical-oil-shortages-1970s-eu-jet-fuel.md` — confidence 0.85→0.75; dispatch_note retro-tagged with BRENT magnitude assessment

**New directory (1) with 3 files:**
- `AGENTS/WALTER/handoff_BRENT/route_log_brent_slice.tsv` — 48-row Q1 deliverable
- `AGENTS/WALTER/handoff_BRENT/LIAISON_TURN_2_DRAFT.md` — Turn 2 draft (now landed in BRENT tree)
- `AGENTS/WALTER/handoff_BRENT/LIAISON_TURN_4_DRAFT.md` — Turn 4 draft (now landed in BRENT tree)

**Closeout files (refreshed):**
- `AGENTS/WALTER/STATUS.md` — Updated stamp; lead-paragraph rewrite; manifest LIAISON BRENT row ACTIVE; NETWORK AWARENESS regen; SESSION LOG entry
- `AGENTS/WALTER/REGISTRY.tsv` — BRENT row + WALTER row refreshed for 5/6
- `AGENTS/WALTER/MEMORY.md` — CHANGES SINCE / NEXT SESSION rewrite; 3 new findings (LIAISON convergence accelerator pattern; 3-way joint-proposal pattern; Post_Hoc_Conf retro-uplift insight)
- `AGENTS/WALTER/LAST_COMPLETION.md` — this file (rewritten for today's session)

**BRENT tree (BRENT-OC commits, NOT WALTER's to stage):**
- `AGENTS/BRENT/handoff_WALTER/LIAISON.md` — Turns 1-5 (424→506 lines after Turn 5 added)
- `AGENTS/BRENT/handoff_WALTER/README.md` — channel conventions
- `AGENTS/BRENT/board/BOARD_LOG.tsv` — 47-signal back-disposition pass (commit `bf8c2c9e`)
- `AGENTS/BRENT/design/JOINT_PROPOSAL_2026-05-05_brent_sections.md` — 206 lines (commit `8f2331f1`)
- `AGENTS/BRENT/thesis/THESIS.md` — v1.1 → v2.0 (commit `00958e15`)
- `AGENTS/BRENT/workbook/FLOW.tsv` — 5 new outbound rows (commit `1a3c691c`)
- `AGENTS/BRENT/STATUS.md` — retro-tag of -012 + LIAISON infra block (commits `707a2f79` + `2954bd5f`)

### Sub-agent spawns (0)

No sub-agent spawns this session. Session was architectural-alignment + Turn-4 self-task execution — no verify-research / synthesis / scan needs.

### Spec changes

- **ROUTING_TABLE v0.5 → v0.6** (Iran-cluster CARL-info override + boundary-trigger threshold-cross sub-rule for ≤$95/5sess and ≥$115/5sess CARL-side dispatch). BRENT-IMMEDIATE 8-row "By Boundary Threshold" section deferred to v0.7 pending Will sign-off on JOINT_PROPOSAL §2c.

### Commits

Closeout commit pending (this session). BRENT shipped 7 commits during/after session (`707a2f79` + `bf8c2c9e` + `8f2331f1` + `1a3c691c` + `00958e15` + `2954bd5f` + `03cb878d`) — all pushed and integrated.

## RESULT

**Architectural-alignment session executed cleanly. BRENT LIAISON converged in 5 turns vs CARL's 7 — half a cycle saved by substrate prep + open-with-substance + retro-disposition-pass-on-Turn-3.** Today's session validates several patterns:

1. **LIAISON convergence accelerator pattern (NEW finding).** BRENT 4-turn architectural convergence vs CARL 6-turn — substrate prep doc (`BRENT_LIAISON_PREP.md` shipped 5/5) + open-with-substance (BRENT Turn 1 with domain summary + I-receive-from + honest gap + 7 questions in one turn) + retro-disposition-pass on Turn 3 (BRENT shipped 47-signal back-disposition + Post_Hoc_Conf deltas in commit `bf8c2c9e` parallel to Turn 3 dialog) = ~2× faster convergence. Apply to RED/NEXUS/REGINALD next-LIAISON setups.

2. **Three-way joint proposal pattern (NEW finding).** Q16 surfaced choice between (a) single 3-way proposal w/ §5 future-work for v0.9 candidates vs (b) two separate proposals 1-2 weeks apart. Both BRENT Turn 5 and WALTER Turn 4 chose (a) — single doc shows architectural arc, decisions-now/decisions-later visible in one read, v0.9 candidates need scoping not sign-off. §5.1/§5.2/§5.3/§5.4 sub-structure per BRENT Turn 5 suggestion accepted.

3. **Post_Hoc_Conf retro-uplift (NEW finding).** BRENT's back-disposition pass surfaced 5 deltas — 4 downward + 1 retrospective uplift (SIG-019-030 InfraA Qatar LNG 0.50→0.85 verified by my later SIG-005-002 IEA primary). Verify-research threshold tuning isn't symmetric — false-positive cost (reroute on bad signal) vs false-negative cost (under-route on real signal that surfaces in primary later) calibrate differently. Calibration cycles need to track BOTH directions.

4. **Cross-tree write authorization works at one-time-per-channel granularity.** Will gave direct-write auth for BRENT LIAISON.md mid-session ("ah you write directly" msg 1359). Followed CARL pattern (uncommitted in BRENT's tree → BRENT-OC commits at next boot). Cleaner than Will-mediated copy-paste for Turn 4 onward.

5. **Per-agent section files + WALTER stitches at repo-root pattern.** WALTER drafts §2a-§2d + §3b + §3d in own tree; CARL drafts §1+§3a+§3c+§4 in own tree (ETA this week); BRENT drafts §1.1+§2e+§3e+§4-coda in own tree (shipped 5/6 `8f2331f1`). WALTER stitches 3-way at repo-root `design/JOINT_PROPOSAL_2026-05-06_walter_carl_brent.md` when CARL section file lands.

## GAPS

### Today's open items (carry-forward — added to FOLLOW-UP list below)

- **3-way joint proposal stitch** — WALTER stitches at repo-root when CARL §1+§3a+§3c+§4 sections land (CARL Turn 7 self-task, ETA this week)
- **Will sign-off on JOINT_PROPOSAL §2 stack** — 4 items: §2a FORMAT_SPEC v0.8 (4 fields + 9-value enum) / §2b scheduled-scan budget ($0.30-0.50/wk per side) / §2c BRENT-IMMEDIATE 8-row threshold list / §2d BURST_WINDOW protocol
- **BOARD_CONSUMPTION_SPEC v0.2 dual-pattern doc** — WALTER self-task this week (CARL consumer-domain + BRENT energy-domain templates documented)
- **CROSS_REFS/{CARL,BRENT}.md cache scaffolds** — WALTER self-task this week (BRENT cache populated triggered by thesis v1.1→v2.0 dual-trigger fired today)
- **EVENT_WINDOW_STATE.md scaffold** — WALTER self-task post-Will-sign-off on §2d BURST_WINDOW
- **HAWK-proxy archive** to `design/history/hawk_proxy_synthesis_2026-05-05.md` — WALTER, when actual HAWK refresh lands
- **FORMAT_SPEC v0.7 → v0.8 land in spec** — WALTER, post-Will-sign-off on §2a (Field Definitions table + 4 new fields + 9-value enum)
- **CHECKLIST update for v0.8** — WALTER, post-Will-sign-off (Phase 2 tag-application step + Phase 2.5 event-window state check step)
- **BRENT CLAUDE.md spawn-protocol delta** — BRENT next session (event_window=open behavior + BRENT-specific BOARD-consumption boot-step)
- **BRENT DATA_RELEASE_CALENDAR.md** — BRENT post-back-disposition pass (workbook/DATA_RELEASE_CALENDAR.md covering EIA WPSR / Baker Hughes / OPEC MOMR / IEA OMR / CFTC COT / Platts)
- **CARL DATA_RELEASE_CALENDAR.md** — CARL self-task this week (extends EARNINGS_WATCH_Q1.md to year-rolling)

### Pre-existing carry-forward (still open, brought forward)

- OZK Q1 post-mortem (REGINALD pickup pending since Apr 16).
- ROAD Act House reconciliation timing (BARON pickup; SIG-W-20260429-005 dispatched).
- HENRY + RED SIGNAL_INTAKE.md prompts on disk.
- BOARD_CONSUMPTION_SPEC propagation to 14 Tier 1 agent CLAUDE.md files (CARL + BRENT mostly done; remaining 12).
- Tier 2 staleness (ZHAO 34d / SHADE 6+wk / OTTO 21d / ORACLE 35d / FERT 6+wk / ATHENA 7+wk / CRUISE 6+wk / DARWIN dormant).
- "verified-as-of" pattern extension (second anchor candidate — Fed-framework / BOJ / OPEC+).
- design/STATE.md maintenance discipline.
- Lead-paragraph regeneration cadence decision.
- Filter v2 Segment D (~1hr, decided option A).
- Signal Registry v2 (deferred).
- COP refresh resume trigger (paused Apr 14).
- Autonomous news-scan policy.
- HAWK-proxy synthesis policy (when default-spawn vs wait for actual refresh).
- CONSUMER_STAGFLATION 5-axis sub-cluster spawn decision (Will sign-off needed).
- Pandemic-meta-cluster informal watch (14-day window for 1-2 more institutional-primary signals).

### Resolved this session (removed from carry-forward)

- **BRENT LIAISON setup** (was item 9 in 5/5 FOLLOW-UP) — converged in 5 turns 5/5-5/6.
- **WALTER joint-proposal §2a-§2d + §3b + §3d sections drafted** — 475 lines at `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-05_walter_sections.md`.
- **ROUTING_TABLE v0.6 land Iran-cluster CARL override** (was 5/5 FOLLOW-UP) — shipped this session.
- **SIG-W-20260505-009 retro-tag** (Turn 4 commitment) — shipped this session (confidence 0.85→0.75 + corporate-amplification-bias + BRENT decomposition reference).
- **REQ-RED supplement with BRENT decomposition** (Turn 4 commitment) — shipped this session.

## WILL_NEEDS

1. **Sign-off on JOINT_PROPOSAL §2 stack** (4 decision items in `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-05_walter_sections.md`):
   - §2a FORMAT_SPEC v0.8 (4 fields: `consumer_transmission` 9-value enum incl. `lng_substitution` / `signal_role` 4-value / `consumer_lens` 4-value / `cluster_secondary` comma-separated) — CARL+BRENT+WALTER pre-cosigned
   - §2b Scheduled-scan budget ($0.30-0.50/wk CARL-primary + $0.40-0.60/wk BRENT-primary; total $0.70-1.10/wk; cap $1.50/wk hard kill)
   - §2c BRENT-IMMEDIATE 8-row threshold-cross dispatch list (Brent ≥$120/3sess + ≤$75/3sess + Cushing <20M + HY-Energy OAS >400 + VLCC ≥2× 30d-median + gasoline crack threshold-cross logic + US rigs +50 + 3:2:1 crack >$50)
   - §2d BURST_WINDOW protocol (BRENT-declares-open / WALTER-declares-close after ≥48h stable; FLASH-burst with threaded Telegram; state machine `open → verify → close-or-confirm`)
2. **Decide next-LIAISON priority** — RED revival (CC-side, blocked on Will spawn) OR REGINALD start (CC-side, unblocked, top of unblocked queue). NEXUS spawn is highest-leverage but blocked.
3. **Iran-war anchor re-verify boundary 5/11 minimum** OR earlier on visible kinetic state-change.
4. **Tomorrow's intake watch:** OBDC Q1 5/6 AMC (BROCK pre-built); LYV Q1 from 5/5 surfaces in tomorrow's intake.

## FOLLOW-UP (canonical running list — survives handoff via this file)

**Time-sensitive (this/next session):**
1. **OBDC Q1 today 5/6 AMC** — BROCK pre-built threshold reads. Surfaces in tomorrow's intake.
2. **LYV Q1 from 5/5 post-market** — high-signal CONSUMER_STAGFLATION discretionary-sub-vector confirm/deny. Surfaces in tomorrow's intake.
3. **NFP Friday 5/8** — LABOR carry-forward.
4. **Q1 Call Report window May 1-10** — REGINALD recheck.
5. **Iran-war anchor re-verify** — verified-as-of 2026-05-04, refresh boundary 2026-05-11 minimum OR earlier on visible kinetic state-change.
6. **CARL ↔ WALTER LIAISON calibration cycle 1** — primary trigger 2026-05-19 (14d calendar from 5/5) OR N=20 BOARD dispositions (early-fire). Whichever first → CARL summarizes Post_Hoc_Conf deltas → WALTER tunes verify-research thresholds.
7. **BRENT ↔ WALTER LIAISON calibration cycle 1** — N=15 forward BOARD dispositions OR 21 days from 2026-05-06, whichever first. ETA May 20-27.

**3-way joint proposal pipeline:**
8. **CARL drafts §1 + §3a + §3c + §4 sections** — CARL self-task per Turn 7, ETA this week.
9. **WALTER stitches 3-way at `design/JOINT_PROPOSAL_2026-05-06_walter_carl_brent.md`** — when CARL section file lands.
10. **Will sign-off on §2 stack** — 4 items per WILL_NEEDS above.
11. **WALTER lands FORMAT_SPEC v0.8** in `AGENTS/WALTER/design/SIGNAL_FORMAT_SPEC.md` — post-sign-off.
12. **WALTER updates SIGNAL_PROCESSING_CHECKLIST.md** for v0.8 + Phase 2.5 event-window step — post-sign-off.

**WALTER self-tasks this week (no sign-off needed):**
13. **BOARD_CONSUMPTION_SPEC v0.2 dual-pattern doc** — CARL consumer-domain + BRENT energy-domain templates documented.
14. **CROSS_REFS/CARL.md cache scaffold** — populate from CARL THESIS.md + workbook indexers; dual-trigger refresh mechanism wired.
15. **CROSS_REFS/BRENT.md cache scaffold** — populate triggered by thesis v1.1→v2.0 bump that fired today; FLOW.tsv expansion captured.

**Post-sign-off WALTER self-tasks:**
16. **EVENT_WINDOW_STATE.md scaffold** — default CLOSED state file ready for first declaration.
17. **FILTER_SPEC.md update** — Tuning Rules sub-section for OPEN-window dispatch posture.
18. **ROUTING_TABLE v0.7** — add "By Boundary Threshold" section (parallel to "By Signal Domain" + "By Signal Type") with BRENT-IMMEDIATE 8-row threshold list.

**BRENT self-tasks (his next session):**
19. **BRENT CLAUDE.md spawn-protocol delta** — event_window=open behavior + BRENT-specific BOARD-consumption boot-step.
20. **BRENT DATA_RELEASE_CALENDAR.md** — workbook/DATA_RELEASE_CALENDAR.md covering EIA WPSR / Baker Hughes / OPEC MOMR / IEA OMR / CFTC COT / Platts.

**HAWK reconciliation (when HAWK refreshes):**
21. **Archive HAWK-proxy synthesis** to `design/history/hawk_proxy_synthesis_2026-05-05.md`.
22. **Update KB-BRT-NNN cross-refs** to point at HAWK output for kinetic doctrine; BRENT oil-substance interpretations stay primary.

**Next-LIAISON channel candidates (per Will direction msg 1366):**
23. **RED LIAISON** — Tier 1 highest priority, blocked on RED revival (Will trigger). Substrate prep doc: shape from BRENT_LIAISON_PREP template.
24. **NEXUS LIAISON** — high-leverage, blocked on NEXUS spawn. Locks cluster-narrative authority precedence rule + closes ~5 placeholder-pending-NEXUS narratives in BOARD.
25. **REGINALD LIAISON** — top of unblocked queue. Bank/CRE/earnings primary. Heavy BOARD pickup. CC-side, easy mechanics.
26. **HENRY LIAISON** — post-RED+REGINALD. POSITIONING_VALUATION cluster owner.
27. **BROCK LIAISON** — mid-priority. PC-stress cluster owner.

**Cluster / domain follow-ups (carry-forward):**
28. **OZK Q1 post-mortem** — REGINALD pickup pending since Apr 16.
29. **ROAD Act House reconciliation** — BARON pickup.
30. **HENRY + RED SIGNAL_INTAKE.md** — saved-to-disk pending.
31. **Tier 2 staleness** (ZHAO 34d / SHADE 6+wk / OTTO 21d / ORACLE 35d / FERT 6+wk / ATHENA 7+wk / CRUISE 6+wk / DARWIN dormant).
32. **Pandemic-meta-cluster informal watch** — 14-day window for 1-2 more institutional-primary signals.

**Refactor open items:**
33. **"verified-as-of" pattern extension** — second anchor candidate (Fed-framework / BOJ / OPEC+).
34. **design/STATE.md maintenance discipline** at closeout.
35. **Lead-paragraph regeneration cadence** decision.

**Design / governance backlog:**
36. **Filter v2 Segment D** — option A confidence_note; ~1hr.
37. **Signal Registry v2** — deferred (storage / concurrency).
38. **COP refresh resume trigger** — Will direction needed (paused since Apr 14).
39. **Autonomous news-scan policy** — codify scan-cadence + verify-research mandatory on novelty-claim items.
40. **HAWK-proxy synthesis policy** — when default-spawn vs wait for actual refresh. Pattern emerged 5/5; partially superseded by BRENT thesis v2.0 supersedes-on-doctrinal rule.
41. **CONSUMER_STAGFLATION 5-axis sub-cluster spawn decision** — Will sign-off needed.

## OPEN DESIGN DECISIONS (need Will — also tracked in MEMORY.md)

- **JOINT_PROPOSAL §2 stack sign-off** (4 items: §2a FORMAT_SPEC v0.8 / §2b scheduled-scan budget / §2c BRENT-IMMEDIATE threshold list / §2d BURST_WINDOW protocol).
- **Next-LIAISON priority** — RED (blocked on revival) vs NEXUS (blocked on spawn) vs REGINALD (unblocked, top of queue).
- **CONSUMER_STAGFLATION 5-axis sub-cluster spawn** — promote to v0.2 OR hold informal in-body-tagging?
- **HAWK-proxy synthesis frequency** — default-spawn when OC primary stale > X days OR wait for actual refresh? Partially superseded by BRENT thesis v2.0 reconciliation rule.
- **Pass 4 of morning's cluster refactor** (5/5) — IRAN_HORMUZ + POSITIONING_VALUATION sub-cluster breakdown? Defer until further intake.
- **FED_FRAMEWORK rename to UST_PLUMBING** — watch threshold for v0.2 taxonomy edit.
- **Cluster status flags** (🟢/🟡/🔴/⚫) — reserved for v0.2.
- **"verified-as-of" pattern extension** — second anchor candidate?
- **MEMORY.md vs LAST_COMPLETION.md duplication** — Pattern D, Pass 5? (Partially resolved 5/5 — MEMORY NEXT SESSION trimmed; full Pattern-D resolution still open.)
- **Lead-paragraph regeneration cadence** — every closeout or only on visible state-change?
- **Filter v2 Segment D** — DECIDED option A; implementation deferred ~1hr.
- **Autonomous news-scan policy** — codify scan-cadence + verify discipline.
- **BOARD_CONSUMPTION rollout cadence** — Will hand-routing; durable rollout = 14 agent CLAUDE.md propagation. CARL + BRENT mostly done; remaining 12.
- **COP refresh resume** — paused since Apr 14.
- **NEXUS cluster classification cadence** — informal cluster tracking via STATUS, or NEXUS-spawn forcing function?

---

*Maintenance note: this file is overwritten each session per CLAUDE.md spawn protocol step 15. The FOLLOW-UP and OPEN DESIGN DECISIONS sections are the load-bearing carry-forward — every closeout copies open items forward and removes resolved ones. Don't append; don't keep historical sessions here; that's what `SESSION_LOG.md` is for.*

*Resolved this session (removed from carry-forward): "BRENT LIAISON setup" + "WALTER joint-proposal §2a-§2d + §3b + §3d sections drafted" + "ROUTING_TABLE v0.6 land Iran-cluster CARL override" + "SIG-W-20260505-009 retro-tag" + "REQ-RED supplement with BRENT decomposition."*
