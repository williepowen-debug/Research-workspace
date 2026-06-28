# BOOT_PROTOCOL — rationale, provenance & incident history

*Companion to the lean boot/closeout checklist in `AGENTS/WALTER/CLAUDE.md` (SPAWN PROTOCOL section). The checklist is the source of truth for **what to do**; this file is the **why / when / who** behind each step — read it before *modifying* a step, not needed to *run* one. Each CLAUDE.md step carries a `[→ BP §x]` pointer to the matching section here.*

*Split out 2026-06-28 (Will-directed) to keep CLAUDE.md — auto-loaded into every WALTER session's context — lean and execution-focused. Behavior-gates (caveats that change what you do) stayed in the checklist; only provenance/rationale moved here.*

**Spec ownership:** the CLAUDE.md checklist owns the ACTION; this doc owns the RATIONALE. A behavior change edits the checklist; a new lesson/incident appends here. (Reflected in the CANONICAL-SOURCE LOOKUP table.)

---

## §0.5 — walter_doctor.py (the 15 checks)

Built 2026-06-16; mechanizes the manual domain audit. Read-only, stdlib-only, ~1s, one extra FRED-pull-free. Exit code = count of HIGH/MED. The 15 checks:

1. **version_drift** — core spec self-declared header versions vs `STATE.md` §1.
2. **claude_md_version_drift** — CLAUDE.md KEY-DESIGN-FILES version claims vs spec headers (guards the boot doc itself).
3. **board_reconcile** — BOARD INDEX ToC counts = section rows = SIG files on disk.
4. **log_reconcile** — route_log / delivery_log SIG-ids ↔ BOARD files (orphans / missing).
5. **cron_liveness** — the step-7c feeds (news-sweep / filing-watch / SIGNALS) vs their cadence limits.
6. **cushing_capability** — EIA `.env` / key present → Boundary-#3 Cushing auto-fire live (silent-death guard; the gitignored `.env` has vanished before — `[[finding_gitignored_private_drop_boot_surfaced]]`).
7. **outbox_age** — stale `outbox/REQ-*` drafts.
8. **registry_staleness** — REGISTRY Tier-1 rows >14d.
9. **registry_lag** — board-lags-agents: a registry row older than the agent's last commit (`[[finding_board_lags_agents_not_vice_versa]]`); distinguishes dormant (accurate) from lagging (refresh owed).
10. **liaison_enum** — enumerate `handoff_WALTER/LIAISON.md` channels + last-turn age.
11. **delivered_but_unconsumed** — handoff in a recipient's `inbox/WALTER/` not consumed after 2d. **Collapsed 2026-06-28 to a one-line ACTION/INFO role-split** (ACTION = real risk; INFO cc-pile = low-stakes, per the 2026-06-23 delivery-telemetry calibration `[[feedback...]]`) — was one MED line per item, which buried genuine findings.
12. **written_but_undelivered** — handoff committed-local but not on origin (git-derived; the Routing-v2 delivery-layer anti-rot telemetry).
13. **deep_research_pending_overdue** — DEEP_RESEARCH_FLAGGED_LOG rows PENDING past deadline / stale `open` >30d (the Phase-2.8 flag loop-closer).
14. **staleness_sweep_overdue** — last STALENESS_SWEEP vs 14d cadence (lifecycle-tagging-lapse guard).
15. **boot_protocol_xref** — every `[→ BP §x]` pointer in CLAUDE.md resolves to a real `## §x` section here, and every section is pointed-to (added 2026-06-28 per PROME review of the boot-protocol split — guards the split's one new failure mode: cross-ref drift when a step is renumbered or a §x renamed. Dangling pointer → MED; orphan section → LOW. Same mechanize-the-audit philosophy as claude_md_version_drift).

Doc/infra + delivery health — distinct from step 6c (market-data threshold scan). HIGH (version drift, BOARD miscount) → fix before proceeding; MED (dead crons, undelivered-to-CC) → surface/escalate, not blocked on. Adding a new core spec? Add its path to the `SPECS` list in `version_drift_check.py`.

## §1 — STATUS.md + IRAN_WAR anchor

STATUS is a lean dashboard after the 2026-05-04 Pass 1+2 refactor (`[[finding_walter_refactor_pattern]]`). The Iran anchor was pulled out of STATUS on 2026-05-04 (Pass 3) so it can be updated in place with its own verified-as-of stamp + re-verify trigger; **history-split 2026-06-28** → current state in `anchors/IRAN_WAR.md` (lean), full stamp/state history in `anchors/IRAN_WAR_HISTORY.md`. The re-verify trigger is weekly-minimum because the state evolves fast; domain owners (BRENT/HAWK/SAM) often run ahead of the anchor (`[[finding_board_lags_agents_not_vice_versa]]`) — read their STATUS as a re-verify input.

## §6b — threshold registries

Pattern locked 2026-05-06 (RED LIAISON, `JOINT_PROPOSAL_2026-05-06_red_walter` §2, Will sign-off) and extended 2026-05-11 (REGINALD LIAISON Q2 LOCK Turn 3). Both registries use an identical 8-col schema (trigger_id / metric / threshold_op / threshold_value / sustain_window / action / recipient_chain / falsification_thesis_ref). RED-FT-NN namespace (7 rows v0.1); REG-T-NN namespace (8 rows v0.1). REG-T-01 KRE<$60, REG-T-02 WAL<$78, REG-T-05 INITIAL-CLAIMS>300K are binary price/event triggers (sustain=1, fire now); REG-T-03/04 HY OAS, REG-T-06 FHLB, REG-T-07 OFFICE-CMBS-DQ, REG-T-08 SOFR-IORB are sustain=3 (credit metrics smoothed for noise). Fire-history ledgers (`FALSIFICATION_FIRED_LOG.tsv` + `REG_THRESHOLDS_FIRED_LOG.tsv`, 5-col, shipped 2026-05-11 REG LIAISON Turn 4) preserve Critical-Rule-#2 (no hallucinated fires) and drive stale-fire suppression within the sustain window. At-dispatch eval + auto-dispatch logic is codified in CHECKLIST Phase 2 step 7.

## §6c — passive at-boot threshold scan

Added 2026-06-06 (CHECKLIST v0.12, 5-decision-walkthrough closeout) to close the dispatch-empty-session detection hole. Before v0.12 the eval only ran at-dispatch, so a binary-trigger crossing during a multi-day dispatch-empty WALTER gap stayed unrouted until the next dispatch session. **Prototype incident:** RED-FT-07 CCC-OAS >930 was structurally met since ~5/29 (938/941/946/944/947 across 6 sessions) but the 6/02 session was anchor-only / dispatch-empty, so the eval didn't run; it evaluated for the first time at the 6/4 AM boot and fired retroactively. So the eval now runs once at every boot regardless of dispatches. **Cost:** ~1 FRED-pull (~30s, free); zero verify-spawn cost (pure threshold scan). **Cushing (2026-06-22, Will-authorized):** the FORGE dashboard natively pulls Cushing crude stocks via the EIA v2 API (`config.py` source `eia`, series `W_EPC0_SAX_YCUOK_MBBL`, M bbl), covering ROUTING_TABLE Boundary #3 — 🔴 (<20M) fires IMMEDIATE (BRENT-primary / WALTER-fallback); 🟡 (20–25M) → near-trigger watch. FRED carries only Cushing *price*, not stocks — the EIA v2 route is the working source; key lives in gitignored `FORGE/tools/market-data/.env` (see §0.5 silent-death guard). A fired falsification trigger re-approaching its threshold from the fired side is approaching its EXIT/un-fire, not a fresh fire — check the FIRED_LOG first (`[[finding...]]` 2026-06-26).

## §7b — EVENT_WINDOW_STATE.md (BURST_WINDOW)

Added 2026-05-08 (`JOINT_PROPOSAL_2026-05-05_walter_carl_brent` §2d, Will sign-off). WALTER + BRENT both have write access; the file is the canonical current state. OPEN-window posture (Phase-2-cluster → FLASH; **verify-research mandatory on extreme-claim items**; threaded Telegram; daily 00:00 UTC roll-up; close-of-window summary) per FILTER_SPEC v0.5. The >7d-stale-while-OPEN gate prevents sitting in declared-OPEN forever on memory alone. Per-signal field tagging via CHECKLIST Phase 2 step 4.5 + Phase 2.5 precedence-override.

## §7c — cron-driven feed sources

Added 2026-05-08 (Will direction msg 1597 — resolved the long-pending "Autonomous news-scan policy" open decision). Three external scrapers, none WALTER-owned (WALTER reads only):
- `FORGE/tools/news-sweep/latest.md` — thesis-tagged Google News RSS, 15 queries, M-F 8:30 AM ET cron (PROME).
- `FORGE/tools/filing-watch/latest.md` — EDGAR filing radar, SEC submissions API for high-signal forms (10-K/10-Q/8-K/NT/Form 4/SC 13D/SC 13G), PROME MVP (commit `e5bbb9ac`).
- `SIGNALS/inbound.md` — SENTRY-owned RSS/Atom scanner (EIA Today in Energy + SEC EDGAR getcurrent + more), GitHub Action 2×/day 10:00 + 22:00 UTC.

**All 3 DARK as of 2026-06-28** (news-sweep ~42d / filing-watch ~52d / SIGNALS ~26d). Go-forward is the Scout build (DEWEY-track), not a live-feed fix; SENTRY's GitHub Action was DISABLED 6/2 (auto-commit-to-master friction). The doctor's cron_liveness check surfaces staleness each boot, so skipping the read loses nothing. Triage discipline when live: dedupe URL > headline-string > company-CIK against BOARD INDEX + kill_log; surface novel items, never auto-dispatch (Will-curated loop). Complementary to (not the same as) the §2b calendar-driven scheduled-scan workflow for BLS/EIA data releases.

## §7d — DEWEY deep-research deliverable consumption

Added 2026-06-20 (DEWEY revival Phase 2). DEWEY hands finished `/deep-research` reports back via a create-only handoff in `AGENTS/WALTER/inbox/DEWEY/` (NEW state), pointing at its `output/YYYY-MM-DD_topic.md` + the originating Phase-2.8 flag ID. This is the consumption end of the Phase-2.8 flag→execute→route loop (CHECKLIST v0.20) — an internal DEWEY→WALTER lane, NOT a cron feed. Route per CHECKLIST Phase 2.8b (one `research-output` BOARD signal, verbatim packet embed + per-recipient genuine-delta wrapper, no verify-spawn → VERIFIED-PRIMARY), close the DEEP_RESEARCH_FLAGGED_LOG row, `git mv` the handoff to `processed/` to prevent repeat-routing. Full WALTER only.

## §8 — registry refresh + fs-scan

The fs-scan exists because reading only the KNOWN (already-registered) set structurally cannot discover a newly-scaffolded agent. **Caught TERRY 2026-06-21** (a full CC peer scaffolded the prior evening — would have stayed invisible) and **DAEDALUS + AEOLUS 2026-06-28**. Classify each gap: live new agent (STATUS/CLAUDE + recent commits) → add a row; old dormant scaffold (no STATUS, months-stale) → flag Will for a completeness decision, don't auto-add (stale rows worse than none, RULE 4). See `[[feedback_verify_counts_before_propagating]]` (verify against ground truth, not the known list). Promoted to this protocol from MEMORY 2026-06-21.

## §9 — LIAISON channel discovery

Added 2026-05-06 (Phase 1 scaffolding). The STATUS "Active liaison channels" subsection is the manifest; the generic glob `find AGENTS/*/handoff_WALTER -name LIAISON.md` covers all current+future channels with no agent hardcoding, and cross-checks against the manifest to detect drift. Use git log on the LIAISON.md as the authoritative last-turn timestamp. Auto-flag ACTIVE → DORMANT after 30d without a turn. Outbox REQ queue: surface any >14d unresolved for retry/escalation.

## §11 — archive + delivery (Routing v2)

Delivery layer shipped 2026-06-17 (WALTER Routing v2), superseding the Apr-14 BOARD-only model — it closed the "in BOARD ≠ received" gap that the 2026-06-13 BRENT routing-bug exposed (SIG-W-20260610-001/-002 reached HAWK but never BRENT; BRENT ran two events behind on the Jun 8-11 escalation). Canonical: `design/BOARD_CONSUMPTION_SPEC.md` v0.6. `delivered` is uniform single-machine (committed + on-origin) since the OpenClaw cut 2026-06-26; handoffs sit `written_not_delivered_pending_push` (surfaced by walter_doctor) until the closeout auto-push sweeps them. Recipients consume from `inbox/WALTER/` (Phase-2 boot-step, time-boxed). The `cluster:` header value must be one of the 11 buckets in CLUSTER_TAXONOMY (BOARD restructured into cluster sections 2026-05-05).

## §closeout — tiered closeout

Tiering added 2026-06-26 (Will-directed), superseding the prior "full closeout mandatory at every session end" — that framing over-rotated, making agents snap-close on quiet/live sessions (`[[finding_boot_protocol_live_event_override]]`). The anti-rot principle still holds: handoff docs must not silently rot. The floor (Tier 1 commits load-bearing state + a breadcrumb every time) exists because of the **2026-05-08 skip-closeout failure** — handoff docs went N sessions stale, forcing blind git-log archaeology at the next boot. Tier 1 prevents that: the next boot is never blind, only narrative regeneration is batched. Worked example of a clean Tier-1: the 2026-06-26 session (`2b75d3de`). The ≥3-breadcrumb backstop catches a Tier-2 that's slipped too long. Will's persistent-session workflow (multiple routing sessions/day, closeout when context fills) is the design target.

## §12 — STATUS closeout

`network_uncertainty_peak` (≥5 `cluster_mediating`/calendar-day → Telegram-ping) per `JOINT_PROPOSAL_2026-05-06_red_walter` §5.5b; it has fired above naive base rate (21-in-day 5/11) — calibration watch on whether ≥5 stays useful. NETWORK AWARENESS "Today's routing + stale agents" regenerates at closeout (Pass 4 option A — don't carry forward stale rows; the embedded per-agent table was dropped 2026-05-05 because it duplicated REGISTRY and rotted). A doc with multiple live-level blocks needs ALL regenerated together — a stale live level is the one thing that must never carry forward (2026-06-26 consistency-critic finding).

## §14 — MEMORY promotion paths

Findings should live in the highest-leverage layer they apply to, not all three. Domain-process → the owning design spec (per CANONICAL-SOURCE LOOKUP; bump version). Cross-agent workflow/calibration → auto-memory (loads at every boot via the harness, so it reaches future WALTER AND other agents from turn 1). Remove from local MEMORY after promotion — a duplicate is just two-places-to-sync + silent drift.

## §16 — git commit + push

Pathspec commits replace the prior `git reset HEAD → git add AGENTS/WALTER/` flow per `[[finding_pathspec_commit_race_safety]]` + `[[finding_concurrent_commit_index_race]]`: the shared `.git/index` makes `git reset HEAD` a global op that can clobber concurrent agents' staged work, and the gap between `git add` and `git commit` can let a concurrent agent commit YOUR staged files under THEIR message. Pathspec commits close both windows. Pre-commit sanity: `git diff --stat <pathspecs>`; never unilaterally `git restore --staged`/`reset` (both touch the shared index) — flag foreign pre-staged work to Will instead. Push is automated at closeout via `scripts/safe-push.sh` (ff-gated, fails safe, per root CLAUDE.md); a non-ff abort means origin diverged (2nd machine pushed) = the tripwire to switch to per-agent branches — do NOT force, flag Will. Defer push if concurrent uncommitted foreign work was observed (`[[feedback_defer_push_coordinate]]`, `[[finding_push_train_pattern]]`). LIAISON shared-write zones can be in WALTER's pathspec when writing the WALTER-side of a turn; verify the target isn't concurrently active (`[[feedback_agent_git_isolation]]`).

---

*Maintenance: when you change a boot/closeout STEP's behavior, edit the CLAUDE.md checklist (source of truth for action). When you add a lesson/incident/provenance about WHY a step is the way it is, append it here. Keep the `[→ BP §x]` tags in sync.*
