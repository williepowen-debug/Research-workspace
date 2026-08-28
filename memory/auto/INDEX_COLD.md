# Fleet Auto-Memory — COLD INDEX

> ⚠️ **CEILING: keep under 51,200 B** (Will-approved 2026-08-23). This is the SINK for `MEMORY.md`'s flow rule and nothing bounded it — it hit **58,825 B and truncated silently**, stranding 26 slugs while the hot index kept advertising them. **A pointer to unreachable text is worse than none.**
> **Legal: TRIM hook text · ROTATE waves out · SHARD by theme.** ⛔ Never delete a row (pointers — deleting orphans a memory). ⛔ Never raise the ceiling. ⛔ Demoted rows append at the END and the cut takes the END, so the newest rescues fall first.
> Check: `read_cap_check.py memory/auto/INDEX_COLD.md` (its % is vs a 60%-of-cap budget; the hard line is the measured **53,819 B**). **2026-08-23 pass: 60 hooks → ≤80 canon, 58,825 → 45,641 B, slugs 333==333 proven. ~134 still over canon.**

## Boot / closeout / handoff / revival / sync — embedded → `PROME/BOOT.md` §Fleet-memory embeds (2026-07-31)
- finding_display_filter_gating_safety_net — a forward-section display filter silently gates the past-due safety net too
- finding_boot_protocol_live_event_override — "SPAWN PROTOCOL framing pulls agents toward CLOSEOUT after boot even mid-event; the fix is neutral \"Write-back\" framing + explicit live-event override in EXECUTE step. Validated on VIOLET 2026-06-05 mid-VIX-spike."
- finding_boot_predictions_scan — A cheap boot-time PREDICTIONS due/stale scan catches silently-stale OPEN predictions; caught a 24d-stale MISS on first run. Transferable to any agent with a predictions TSV.
- finding_boot_closeout_hardening_recipe — "Phased recipe for hardening an agent's boot/closeout protocol — mirror, strip live-state, audit-produce doc-ownership + deferred punch-list"
- finding_boot_py_cadence_skip_pattern — "For monthly/low-frequency-data agents, the mature boot.py pattern is SAM/BRENT run-at-boot-defensively + mtime cadence-skip on fetchers — NOT a read-only/--pull opt-in split"
- finding_boot_sweep_macro_regime_context — boot sweeps should check WHO runs the central banks, not just feeds
- finding_revival_proxy_pattern — Step 4 of PROME/ORCHESTRAL_LAYER_DESIGN.md
- finding_revival_boot_doc_sweep — "When reviving an agent stale 30+ days, sweep boot docs (CLAUDE.md, MEMORY.md, CALENDAR.md, STRATEGY.md, IDENTITY.md, USER.md) alongside STATUS — staleness compounds across all of them, not just the dashboard"
- feedback_scan_agent_outboxes_at_boot — "When booting PROME, scan AGENTS/*/outbox/ for PROME-targeted signals — not just AGENTS/PROME/inbox/ — to close the outbox-resident signal discovery gap"
- feedback_front_load_planning — "For multi-step deterministic work, surface all decisions in a pre-execution planning pass; let Will batch-approve defaults; then execute mechanical with proceed-pacing at step boundaries"
- finding_freshness_audit_vs_caught_up — mtime/STATUS-freshness ≠ caught-up; a fresh agent can still be behind on inbox backlog AND on a pending test in its own STATUS that already resolved
- finding_gitignored_private_drop_boot_surfaced — gitignore hides private drops from git status too — pair with a boot-card line
- finding_fetch_before_trusting_boot_sync — At boot, git ahead/behind reads the LOCAL remote-tracking ref and is stale until you `git fetch` — a `0/0` can hide a large gap (53 commits here), especially right after a serial-multi-machine switch; fetch before declaring "synced" or reading state.
- finding_inbound_lane_is_the_falsification_channel — "If a signal lane can carry a falsifier for a thesis you own, it is boot-mandatory not spawn-optional — HAWK's 9-day-unread WALTER signal contained the exact correction to its own canonical thesis"

## Closeout-moment rows — embedded → `PROME/CLOSEOUT.md` §Fleet-memory embeds (2026-07-31)
- finding_closeout_as_writeback_tail — "Codify session closeout as the write-back tail of the auto-loaded CLAUDE.md SPAWN PROTOCOL, not a standalone doc; auto-load is the decisive factor"
- feedback_intra_day_closeout_discipline — Run WALTER closeout (spawn-protocol steps 12-15) at every session end, not just end-of-day; multi-session-days must honor intermediate closeout to prevent STATUS-staleness gap
- feedback_handoff_cadence — Will prefers clean handoffs at natural breakpoints over riding a long session into degradation
- finding_state_token_sweep_all_surfaces — When a gate/decision state flips (e.g
- finding_completion_stamp_skip_reads_as_current — "a file whose NAME promises currency (LAST_COMPLETION) that SKIPS a closeout doesn't read as stale — it reads as current and wrong; detect by mtime vs STATUS.md"
- finding_derived_surface_fold_is_the_last_writeback — 5-of-5 stale derived surfaces were MID-SESSION writes left behind by later prima

## Sub-agents, teams & workflow orchestration — embedded → `PROME/ORCHESTRATION_PLAYBOOK.md` §Fleet-memory embeds (2026-07-31)
- finding_subagent_escalation_mode_discriminator — Propose-only sub-agents (KOYOMI/KURA/METSUKE pattern) should discriminate escalation handling — money/irreversible blocks on Will; low-stakes/reversible structural applies sane default + logs rationale + flags for veto
- feedback_subagent_prompt_discipline — When spawning research sub-agents, 4 rules to keep returns efficient without over-templating
- finding_subagent_idle_is_not_delivery — idle ≠ report delivered; "main" unaddressable from below, make the FINAL TURN TEXT the deliverable; chase by name, pre-authorize splitting, stand down duplicates (n=2: 7/28 + 8/7)
- finding_subagent_memory_split — split sub-agent specs: durable mandate + dated MEMORY half, or spawns can't orient
- finding_subagent_baseline_audit — a maintain-a-set spec needs a BASELINE audit rubric, not just incremental
- finding_subagent_naming_identity_over_functional — Multi-agent systems with named sub-agents should prefer identity-naming (unique
- feedback_subagent_propagation_gap — "Sub-agent good work doesn't reliably rise to the parent — at parent closeout, scan sub-agent KB/STATUS for unpropagated facts"
- finding_subagent_prefire_date_verification — re-fetch cadence-derived dates within N days of fire; caught 2-day errors
- feedback_subagent_web_tools_not_autoloaded — "General-purpose research sub-agents may spawn WITHOUT WebSearch/WebFetch loaded, silently returning no data on web-dependent tasks; confirm tooling in the prompt or do the lookup in-session"
- finding_subagent_year_verification — "Before citing any web-pulled metric as load-bearing, confirm the YEAR explicitly from the primary source; aggregator articles silently reference prior-year prints"
- feedback_parallel_spawn_independent_agents — When spawning multiple sub-agents whose work doesn't depend on each other, always send them as multiple Agent calls in a single message — never sequentially
- feedback_named_spawn_teams_mode — Naming an Agent spawn via the `name` parameter triggers team-mode (mailbox-based
- finding_fence_orchestration_live_agent — a directory fence must be ANNOUNCED to the live session and its commits watched
- finding_teams_mode_domain_agent_spawn — Teams-mode (named-spawn) works for domain agents like BOND
- finding_draft_only_teams_spawn — "Teams-mode domain-agent spawn pattern where agent is briefed to draft into proposals/ only, no live state file edits; iterative Will + Prome review via SendMessage across multiple turns before recipient adopts"
- finding_teams_mode_iterative_tasks — SendMessage beats spawn for ITERATIVE work; spawn is fine single-turn
- feedback_warm_parked_agent_collision — "leaving named teams-mode agents \"warm\" across sessions causes next-session same-name collisions + cleanup-sweep kills; release at closeout or use collision-proof aliases"
- feedback_orchestration_mode_split — multi-agent sessions — split fan-out (Workflow) from live orchestration (teams-mode) before spawning; see ORCHESTRATION_PLAYBOOK
- finding_workflow_concurrency_529 — "concurrent Workflow runs + live sibling agents overload the account API (529); cap parallelism, degrade to inline/sequential"
- finding_workflow_agent_unprompted_commit — workflow research subagents have Edit+Bash and can commit to canonical files unprompted; scope them RESEARCH-ONLY or route writes to proposals/
- finding_investigation_routing_discriminator — "route signal-investigation by \"do I need the answer THIS session to make a routing call?\" — yes→inline verify, no→assign a dedicated research agent; a paywalled headline is an investigation POINTER not route-or-kill"
- finding_workflow_subagent_repo_sandbox — "Workflow subagents are sandboxed to the repo working tree; pass in-repo paths (not ~/.claude or /tmp) and hardcode script values rather than relying on args binding."
- finding_write_behavior_check_before_agent_tool_run — "Before test-running another agent's tool, grep it for write ops — \"boot kit\" and \"tracker\" scripts mutate their agent's data files, and a verification run becomes an ownership violation"
- finding_workflow_scratch_crash_recovery — a crashed /deep-research (or any Workflow) session leaves sub-agent outputs recoverable in /tmp task scratch — salvage before re-running
- finding_workflow_rate_limit_resume_recovery — A /deep-research or Workflow killed mid-run by a session rate limit is recoverab
- finding_teams_mode_no_split_pane — Teams mode does not appear to support split-pane visibility on WSL2 even with teammateMode=tmux + TMUX env present; Agent View is the feature that provides the second pane
- finding_batch_extraction_fanout_then_route — split mechanical extraction (fan out) from judgment (owner keeps routing)
- finding_warm_agent_multiround_sweep — keep named spawns resident, re-task in rounds — later rounds are cheap
- finding_duplicate_the_decision_changing_finding — run the ONE decision-changing finding twice, independent agents
- finding_warm_agent_proposal_round — After a task wave, a proposal round
- finding_scheduled_print_spawn_armed_state_report — require an ARMED-STATE report before first idle, else armed looks dropped
- finding_spawn_packet_seed_premise_verification — Coordinator-authored spawn-packet context claims (current time

## Spawn delivery contract — embedded → `PROME/COMPLETION_SPEC.md` §Fleet-memory embeds (2026-07-31)
- finding_two_phase_spawn_grader_contract — waiting on a print? two spawns, a FROZEN grader as the handoff contract
- finding_terminated_notice_can_precede_delivery — A teammate_terminated notice + an empty disk check does NOT prove a spawned agen
- finding_idle_notification_is_not_a_result — an idle spawn is not a report — chase the deliverable; check DISK before re-spawn
- finding_spawned_agents_ship_artifact_skip_writeback — spawns ship the artifact and SKIP their STATUS — put write-back in the contract

## Git rows verbatim in root canon — embedded → root `CLAUDE.md` Git Protocol (pre-existing text; no edit needed)
- feedback_agent_git_isolation — When pushing changes for one agent, never stash/commit other agents' files — scope strictly to the agent's directory
- feedback_check_staged_before_commit — Always run git diff --cached before committing to catch pre-staged files from other agents/sessions
- feedback_git_mv_for_inbox_processing — "When moving inbox files to processed/ subfolder, use `git mv` not bash `mv` — bash mv leaves the deletion unstaged and creates a two-commit hygiene problem."
- feedback_defer_push_coordinate — Push is automated at closeout via ff-gated safe-push.sh (serial multi-machine) — pathspec commit, let safe-push sweep the train; non-ff abort = routine rebase, escalate only on simultaneous-use signatures
- finding_push_train_pattern — one push ships every agent's unpushed commits; automated at closeout
- feedback_shared_log_row_author_commits — "Will ratified (2026-07-24, to LABOR) that the agent who authors a row in the shared AGENTS/SIGNALS.md commits that row itself rather than flagging it to PROME — uncommitted shared-file edits orphan by design."

## Prediction & calibration — embedded → `FORGE/PREDICTION_DISCIPLINE.md` (2026-07-31; hot residue re-based 2026-08-21 pass #5 — canon file now carries the FULL set, only the 2 HELD-HOT rows stay in MEMORY.md)
- finding_widened_scope_needs_rescoped_instrument — Widening a prediction's scope while keeping the old base-rate instrument can make it already-failed at registration — and you cannot see it from inside the derivation
- finding_discovery_instrument_defines_the_claim — press-sampling measures YOUR discovery latency, not the world — name the scan
- finding_redated_falsifier_inherits_premise — When you re-date a falsifier/prediction because a catalyst moved
- finding_prereg_dates_the_event_not_the_artifacts_cadence — a prereg resolving on an ARTIFACT is dated by that artifact's own publication history, not the event; a mis-dated read manufactures a "disclosure missing" signal out of a calendar
- finding_lessons_file_cannot_detect_own_contradictions — A prose lessons/LEARNINGS file cannot detect its own contradictions
- finding_prereg_symmetric_magnitudes_can_hide_an_unreachable_branch — a registered trigger that CANNOT fire; re-run reachability on the AMENDED text, not just the original (n=4 desks, 1 day)
- finding_pre_register_against_the_carrying_filing — Pre-register a threshold against the FILING/SOURCE that carries the metric
- finding_anchor_prediction_to_surprise_not_priced — "Anchor an event→reaction prediction to the SURPRISE-vs-pricing, not to a named outcome that's already priced; dovish/hawkish labels can invert"
- finding_thin_liquidity_prediction_market_discipline — "Thin-liquidity binary prediction-market single-print moves are not \"holds\"; require cross-source verification + ≥3-day re-check + earned-discount calibration before any mark update"
- finding_calibration_discount_regime_conditional — An earned calibration discount is conditional on the pricing regime it was earned in — re-derive before applying at a different market-confidence level
- feedback_two_way_read_directional_clarity — When presenting a \two-way read\" or scenario branches"
- feedback_corrected_framing_calibration — WALTER verify-research's most-frequent verdict is CORRECTED-FRAMING; live distribution 0.60-0.88 confidence (median ~0.77), retain directional thesis, flag specifics as imprecise
- finding_threshold_vs_mechanism — separate "mechanism intact" from "threshold holds" — TRUE-letter, FALSE-spirit
- finding_catalyst_vs_consequence_conflation — Probability-shaped signals derived from catalyst probabilities silently inflate when transcribed as consequence probabilities — require the explicit P(consequence | catalyst fires) conditional
- feedback_prediction_canonical_measure — When revising a prediction
- feedback_single_month_subcomponent_skepticism — Single-month sub-component metric moves (ISM internals, CMBS by-property-type
- finding_noise_filter_erases_signal_class — before widening a noise filter, check if the true positives live in the noise
- feedback_forward_discovery_prediction_spirit — resolve forward-discovery by SPIRIT (found in-window?), not literal text
- feedback_litigation_allegation_weighting — Plaintiff/litigation-allegation-only signals should be weighted ≤40% confidence
- finding_base_rate_vs_mechanism_discriminator — a novel mechanism bypasses discriminators, emitting a confident wrong veto
- finding_catalyst_path_decoupling — "Level trigger ≠ path trigger — a pre-registered conjunction anchored on an assumed catalyst path can be hit via a different upstream path; that invalidates the path-dependency, not the level read. SAM-23, 2 windows Jun 2026"
- finding_pre_registration_discipline_through_corroboration — "Hold a pre-registered trigger's mark through interim corroborating evidence — don't discretionary-fire early; cost = days of mark-lag, benefit = clean spec test. Validated SAM-21 Jun 3→9 2026"
- finding_level_conditional_probability_remarking — "A forward probability attached to a price level/range silently re-marks itself as spot moves; ask what spot was when it was computed, and split range-composites into per-level ladders"
- finding_sustain_count_role_discriminating_power — "A registered trigger needs a stated ROLE, not just a derived number — test what the instrument can and cannot catch; the derivation may return \"this tool can't catch that failure class\""
- finding_delta_vs_own_prior_local_extreme — "a Δ measured against your OWN last reading misleads if that prior was a local extreme — contextualize a short-window delta against the medium-term trajectory before calling a reversal/regime-change"
- feedback_dont_retire_dormant_thesis — "de-escalated catalyst -> dormant/armed convexity + re-arm trigger, don't kill the thesis"
- finding_flow_discriminator_vs_narrative — trust the pre-registered discriminator over the street, after a staleness check
- finding_seasonal_trough_baseline_resolves_true_on_normal — A falsifier baselined on the LATEST single period of a seasonal series can pick the trough — then ordinary seasonal recovery resolves it TRUE while carrying zero information about the event being tested
- finding_sample_size_vs_identification_defect — "More data" fixes a sample-size defect and never fixes an identification defect — check which one you have before promising that another period, quarter, or print will settle it
- finding_perturb_inputs_to_test_base_rate — Reproducing a base rate only proves the arithmetic; the real test is correcting its INPUTS at source and seeing whether the conclusion survives — do it before the number carries a live position or prediction
- finding_gate_bias_is_placement_error_compare_to_margin — A known bias in a threshold is a PLACEMENT error and only binds near the boundary — quantify it in the metric's own units and compare to the realized margin before discounting a verdict
- finding_absence_tell_needs_a_talkative_instrument — "they didn't mention X" needs a source with room and habit to mention it

## Trade / position / risk discipline — ✅ **embedded → `AGENTS/TERRY/RISK_RULES.md`** (all 13 rows below; TERRY-confirmed 2026-08-04, new section "Durable findings — EMBEDDED FROM AUTO-MEMORY 2026-08-04", above Postmortem Tags). Grouped not flat, at TERRY's judgment — RISK_RULES is a **fire-time** document, and a flat 13 is scanned while a grouped one is found. ⚠️ `finding_profit_zone_needs_its_own_harvest_rule` is labelled there as **NO_HARVEST_RULE** (Will-ruled fleet-wide 7/31) with its cost attached — root cause of this desk's only realized loss, −$111.60 on TRY-VIOLET-VIXCS. **Embedding the finding is NOT adoption of the NO_HARVEST template** (WILL_QUEUE row 11, still open)
- feedback_deploy_on_trigger_not_calendar — "Will deploys fresh capital ONLY on a fired trigger, never on mechanical book-maintenance; limited funds = preserve dry powder"
- feedback_position_cost_basis_not_authoritative — Never cite position cost-basis / P/L from STATUS or state-file figures as authoritative — confirm with Will; recorded fills can be wrong and even fail to reconcile
- feedback_put_vs_duration_expression — in a suppressed tape single-name puts bleed; match vehicle to the OPEN channel
- feedback_exit_recommendations_need_mark_context — surface the execution mark before recommending an exit, else propose a window
- finding_option_marks_need_live_chain — Option position marks carried forward in state files go phantom — pull the live chain (last/bid/ask) at every decision point; sanity-check vs moneyness/DTE
- finding_workbook_demote_by_verification — "demoting a dormant agent ledger — verify live-consumer + cross-agent counterparty BEFORE freezing; triage by Group not ID-range; UNVERIFIED-RETIRED for LLM rows; re-verify your correction's own provenance"
- finding_risk_control_separate_from_sizing — a collapsed AND-leg DISARMS the stop; re-spec is risk control, not sizing
- finding_registered_killswitch_cost_datum — "When a pre-registered kill-switch fires against a paying framework, hold the verdict, log the counterfactual cost as a datum on the switch, and queue refinements for the next calibration pass — never retro-apply"
- finding_vrp_split_rates_vs_singlename — The post-2012 SPX variance-risk-premium collapse does NOT apply uniformly
- finding_cooldown_gate_differential_main_vs_hedge — A vol/cooldown gate blocks fresh MAIN-arm capital deployment (paying vega on a n
- finding_fill_in_principle_vs_final_approve_pattern — Two-stage fill approval: Will [Approve in principle] unblocks TERRY's live re-ma
- finding_profit_zone_needs_its_own_harvest_rule — Every management trigger keyed to a further move leaves NO rule that fires when the position is merely profitable — add a P/L-keyed harvest, and check the trigger variable is one the profit zone actually reaches.
- finding_grade_execution_only_against_same_timestamp_marks — Grading a fill against marks pulled at a different time in a moving market manufactures a fake execution finding — establish the fill timestamp FIRST, then compare like with like.

## Deep-research method — embed-pending → `AGENTS/DEWEY/CLAUDE.md` (already cited inline there; packet 2026-07-31)
- finding_deep_research_stale_vintage_headline — on a deep-research run the load-bearing headline figure is disproportionately a stale/trough/early-estimate VINTAGE of a periodically-revised series — refresh each to its latest print as a standing step
- finding_deep_research_slate_mining — Build deep-research prompt slates by mining agents' SELF-flagged gaps
- finding_deep_research_primary_pull_owns_three_data_classes — deep research cannot reach paywalled, live-reading, or single-name filings

## Agent-specific pointers — embed-pending → each agent's own CLAUDE.md/boot card (packets 2026-07-31)
- **LABOR:** project_labor_standing_nexus_brief — "LABOR now maintains a standing NEXUS_BRIEF.md (Tier-1 treatment), refreshed every closeout — not Tier-2 \"skip\"" · *embedded → AGENTS/LABOR/CLAUDE.md C1 + FILES row (confirmed 2026-07-31, `009334be`; embedded from the memory FILE — adopts the stricter every-closeout-incl-no-change-re-bump reading, flagged to Will)*
- **BRENT:** project_energy_strike_ledger — "HAWK maintains a unified cross-theater energy-infrastructure strike ledger (STRIKES.tsv + SUMMARY.md); one table, theater column, not per-theater silos" · *embedded → AGENTS/BRENT/CLAUDE.md closeout step 10 (confirmed 2026-07-31, `0832c484`)*
- **HENRY:** feedback_henry_macro_focus_not_positions — "HENRY focus is macro + market trends, NOT trade-position management; Will's open trade positions (TLT puts etc.) are retired as dead/closed" · feedback_henry_vol_broadcast_to_violet — HENRY uses VIX/vol as input but does NOT broadcast vol-regime signals to the network — VIOLET owns that · reference_henry_operating_dashboard — "HENRY Will-facing Operating Dashboard Artifact (thresholds, open predictions w/ falsifiers, catalyst ladder, cascade state, calibration record); LIVING — refresh the SAME URL, do not mint a new one" · *all 3 embedded → AGENTS/HENRY/CLAUDE.md IDENTITY (confirmed 2026-07-31, `a5cb00c9`)*
- **RED:** feedback_red_edge — Will wants RED to maintain adversarial edge — always present the best possible counter-case, even when it's losing, but be honest and realistic, not contrarian for its own sake.
- **WALTER:** project_walter_cop_direction — "RESOLVED/historical (tombstoned 2026-07-17, Will-approved) — the 2026-04 'COP integrator' direction SHIPPED as WALTER's BOARD (shared archive) + audited per-signal delivery; canonical = AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md. Do NOT design against the old COP frame." · project_walter_image_signal_intake — WALTER + Prome only on Telegram; WALTER owns image/screenshot intake since Prome's Kimi LLM can't reliably analyze images · feedback_walter_autonomous_verify — Will authorized WALTER to spawn verify-research sub-agents without asking each time · feedback_walter_no_kill_on_lede — When Will offers the full article body, read it before classifying; body often has extractable data the lede obscures · finding_walter_refactor_pattern — Sequenced-pass structural refactor recipe — diagnostic → plan → per-pass Will checkpoint → POV check mid-flight → persisted running list. Useful when any agent's STATUS.md or boot doc-set has grown sprawling. · project_telegram_plugin_scope — Telegram plugin enablement belongs at AGENTS/WALTER/.claude/settings.json (proje · feedback_telegram_reply_required — When Will messages via Telegram, ALL substantive replies must go through the Telegram reply tool, not session output · *all 7 embedded → AGENTS/WALTER/CLAUDE.md "EMBEDDED AUTO-MEMORY" block (confirmed 2026-08-02, `ace7a534d`; PROME artifact-verified all 7 `[[slug]]` links present)*
- **CARL:** feedback_carl_kb_architecture — Will wants CARL KB lean (thesis-level only); push domain-specific data down to sub-agent KBs · *embedded → AGENTS/CARL/MEMORY.md boot step 1b (confirmed 2026-07-31, `1f8824b8`)*
- **TERRY:** project_terry_daytrading_review_system — TERRY runs a standing day-trading review loop (AGENTS/TERRY/daytrading/) — Will wants trades tracked regularly to understand mistakes · reference_terry_desk_dashboard — "TERRY's visual desk dashboard (Artifact) — shadow book + card pipeline + live position; how to update it, and Will's refresh cadence." · *both **embedded → `AGENTS/TERRY/CLAUDE.md`** new "Standing context — two things that are true every session" block at end of BOOT (confirmed 2026-08-04)*
- **DAEDALUS:** project_daedalus_maturity_map_hygiene_input — DAEDALUS maturity map (L0-L5) is a hygiene input, not the scoreboard · *embedded → AGENTS/DAEDALUS/CLAUDE.md MATURITY LADDER section (confirmed 2026-07-31, `0c37a365`)*
- **VIOLET:** reference_violet_vol_cheatsheet — "VIOLET's Will-facing vol cheat-sheet Artifact (gauges explainer + dated snapshot); LIVING reference, refresh in place to the same URL after material vol shifts / post-FOMC" · reference_violet_operating_picture — "VIOLET's Will-facing Operating Picture Artifact (live agent state + how-to-read-the-agent explainer); LIVING, refresh in place to the same URL post-FOMC / on material state change" · *both embedded → AGENTS/VIOLET/CLAUDE.md "Will-facing published Artifacts" block (confirmed 2026-07-31; embedded from the memory FILES — fuller than the packet paraphrase, incl. repo-source paths + same-URL redeploy)*

## Project-state (Tier-3 COLD, no embed target — read on demand)
- project_messaging_overhaul — Don't invest in inbox/outbox/HERMES hygiene — file-based messaging is being replaced
- project_research_intake_collection_lane — "RESEARCH-INTAKE = always-on data lane (GitHub Actions, separate repo); agents read it read-only"
- project_public_prep_anthropic_fellows — repo being prepped public as portfolio for Will's Anthropic Fellows (Economics &
- project_automem_symlink_migration — "TOMBSTONE (2026-07-17, Will-approved) — folded into the hardlink-inplace-edit finding (hot index); docs/AUTO_MEMORY.md is canonical for the current model. File kept as a name-anchor for older docs that cite this slug."
- project_phone_signal_architecture — Will wants reliable phone→fleet signal ingestion (Telegram drops)

## Tool gotchas — embed-pending → tool headers
- finding_crlf_textmode_tsv_flip — two silent whole-file TSV rewrites (CRLF, csv re-quote); guard = git diff --stat · *n=3 (RED 6/23; CARL 8/12 ×2)* · *embed-pending → scripts/tsv_append.py header (pending scripts/-ownership ruling, queue row 6)*
- finding_printf_format_tsv_append_corruption — Appending TSV/log rows via shell printf corrupts the row when the data contains · *embed-pending → scripts/tsv_append.py header (pending scripts/-ownership ruling, queue row 6)*
- finding_market_data_venv_invocation — market-data fetch.py/dashboard.py need the repo .venv python — plain system python3 fails with ModuleNotFoundError (yfinance) · *embed-pending → FORGE/tools/market-data/README.md*
- finding_subdir_launch_hooks_dont_fire — Claude Code hooks (SessionStart etc.) configured in the repo-root .claude/settings.json do NOT execute for sessions launched from subdirectories (CC bug · *embed-pending → PROME/BOOT.md (already cited there — pure dedup)*
- finding_truncated_read_is_not_a_verification — truncation drops the TAIL, where the exculpatory half lives

## Rare infra findings (Tier-3 COLD)
- finding_gh_run_watch_exit_status_unreliable — "`gh run watch --exit-status` can report failure on a run that actually succeeded; confirm via `gh run view --json conclusion`"
- finding_injection_claim_is_openclaw_vestige — "verify a file is actually boot-loaded before calling it load-bearing; SOUL/USER/AGENTS \"always injected\" is vestigial"
- finding_fdic_securities_filings_api — FDIC securities-filings JSON API (securitiesfilings.fdicconnect.fdic.gov) gives
- finding_tic_cslt_country_transactions — Country-level TIC net transactions moved to the CSLT JSON (S-form files frozen at Jan-2023); mfh.txt serves a dead vintage; press-notice PDFs are named by release month not data month
- finding_pandas_column_method_collision — "pandas columns named like DataFrame methods (skew, var, std, count, min, max, mean, rank, diff, size) silently return the METHOD via dot-access — bracket-index every financial-series column"
- finding_expiry_dated_suppression_register — every suppression row carries a MANDATORY expiry, so none outlives its check
- finding_composite_least_reliable_at_extreme_amplitude — a composite is least reliable at the amplitude that makes you want to cite it: e

## Demoted from HOT — 2026-08-12 flow-rule pass (Will-approved; PROME-executed per the standing flow rule; index rows only, memory FILES unchanged; rollback = move a row back to `MEMORY.md`)
### Git / multi-machine
- finding_two_machine_partition_clean_merge
- finding_stranded_commit_payload_retriage
- finding_curated_worktree_branch_landing
- finding_git_crash_object_corruption_recovery
- finding_forced_update_rebase_churn
- finding_shallow_clone_false_fork
- finding_difftree_multihash_tree_diff_false_positive
- finding_backtick_command_substitution_in_commit_message
- feedback_cross_agent_inbox_writes — author commits own cross-agent packet; 'leave untracked' DEAD; untracked = 1 box [cold-direct 8/28: predictable trigger; 5/21 body superseded in-file by carve-out ① + row 102]

### Verify before acting
- feedback_verify_etf_vs_fx
- feedback_verify_treasury_security_type
- feedback_ocr_verify_input_first
- finding_confabulated_counterparty_position
- finding_verify_roster_by_commit_activity
- finding_history_scrub_verify_by_content_not_pickaxe
- finding_daedalus_encode_existing_needs_live_read
- finding_first_session_falsifies_build_assertions
- finding_verify_runtime_context_before_tool_broken
- finding_credential_scrub_envstripped_verify
- finding_triage_summary_compression_inversion
- finding_verify_fix_against_capable_case
- finding_theater_check_before_gate_check
- finding_analogue_asset_class_must_match
- finding_weekday_assumed_never_evaluated — n=3
- finding_date_gate_beats_weekday_name
### Prediction & calibration
- finding_update_size_must_track_instrument_distance_from_evidence — size the move by your instrument's distance from the finding; outcome≠direction
- finding_rebased_metric_check_made_date — if the NEW metric was already true at Made_Date, retire+replace
- finding_threshold_spec_fails_before_world
- finding_n_of_m_test_needs_intentions_realized_balance — tag each condition INTENTIONS/REALIZED; require one of each
- finding_gross_flow_cannot_test_a_net_claim — base-rate a proxy/target split: rare-and-now = REGIME, not a bad measure
- feedback_dont_bank_unpassed_forecast
- finding_count_the_connectives_in_versus_out — enter any-1-of-N, exit all-N = a RATCHET
- finding_policy_day_print_counts_in_sustain_window
- finding_escalation_line_needs_delta_not_level — would it fire on DAY ONE? then it's a descriptor
- feedback_date_specificity_weakest_link
- finding_resolvability_defect_is_status_not_confidence — STUCK, not a confidence cut
- finding_prereg_branch_label_can_contradict_its_condition — check the branch LABEL against the sign of its CONDITION; grade the condition, NO-CALL if they disagree
- finding_named_risk_underweighted_is_its_own_error — you WROTE the caveat then priced it low; a PROVISIONAL grade must show up in the NUMBER, not just the prose
- finding_priced_probability_destroys_surprise_room — track the UNPRICED remainder, not the level
- finding_expected_window_rederived_from_now_drifts — pin the anchor; consume, never re-derive; past it = channel finding
- finding_pre_decision_condition_vs_rationale — delivering into someone's pre-registration: report CONDITION and RATIONALE separately, adjudicate neither
### Numbers & staleness
- finding_level_vs_monthly_average_cpi_landing
- finding_blended_index_masks_bifurcation
- feedback_yoy_baseeffect_use_multiyear_stack
- finding_series_reconstruction_extension
- finding_derived_surface_band_rot
- finding_ratio_gauge_denominator_branch
- finding_flow_sign_vs_program_direction
- finding_selfstamp_estimate_drift
- finding_decouple_idiosyncratic_from_systemic_leg
- finding_proxy_segment_masks_trigger_series
- finding_curve_shape_policypath_vs_termpremium
- finding_fill_rate_misread_as_recovery_price
### Cross-agent coordination
- finding_liaison_convergence_pattern
- feedback_adversarial_brief_for_pair_teams
- finding_domain_agent_steelman_backstop
- feedback_consolidate_domain_pressure
- finding_nexus_brief_drafting_cross_check
- finding_fleet_selfreport_convergence
- finding_sibling_agent_protocol_drift
- finding_retraction_culture_cluster_ratio
### Doc & state-file hygiene
- finding_refresh_not_retire_perentity_profiles
- finding_framing_precision_overlay
- finding_pov_changelog_pattern
- finding_schema_conformance_not_clean_text
- finding_path_b_trim_pattern
- finding_dead_path_regrows_unless_senders_repointed
- finding_premise_residue_survives_date_fix
- finding_followup_audit_pass
- feedback_audit_behavioral_ranking
- finding_doc_mirror_consistency_check
- finding_documented_divergence_as_discipline
- finding_governance_doc_stale_default_drift
- finding_status_spine_staleness_under_appended_top
- finding_passive_surface_rot_push_not_dashboard
- finding_roster_change_propagates_to_all_surfaces
- finding_reconcile_match_on_key_not_substring
- finding_owned_surface_without_a_ledger_destroys_history — ownership ≠ retention
- finding_proposed_rule_must_be_canon_tested — canon-test a NEW rule before downstream is written against it; off-repo plans escape canon_check by construction
- finding_ownership_claim_is_last_to_move — when the canonical OWNER moves, the docs saying who owns it go stale and defend themselves with the ruling that made them right
### Evidence & source quality
- finding_migration_tally_inventory_incomplete
- finding_insurer_entity_scope_trap
- finding_count_measures_intake_not_domain
- finding_discovery_tool_wrong_slice_false_zero
- finding_magnitude_ranked_discovery_blind_to_deep_slow
- finding_refuted_claim_citation_vs_fact_failure
- finding_designation_date_lags_event_date
- finding_edgar_entity_hit_direction_and_doctype
- finding_relabeled_number_viral_stat
- finding_credit_absorbed_vs_liquidity_transmission
### Infra & tooling
- finding_offrepo_routine_prompt_rot — mirror in a registry; thresholds read from files at run time
- feedback_weight_plumbing_by_target_scale
- feedback_script_labels_match_thesis
- feedback_flag_friction_realtime
- finding_webfetch_pdf_saves_despite_parse_error
- finding_automem_hardlink_inplace_edit
- finding_unversioned_local_secret_fails_silently — check the secret before debugging the service
- finding_artifact_redeploy_same_url
- finding_representative_leg_by_recency_not_magnitude
- finding_stale_executable_exits_clean — RUN legacy tooling before judging it
- finding_holiday_calendar_domain_mismatch — USFederalHolidayCalendar has no Good Friday
- **Demoted from hot 2026-08-20 (flow-rule pass #2, PROME closeout — settled/predictable-trigger rows; ZERO deleted, slug-conservation proven in commit):** finding_diff_the_vintages_not_just_refresh — reversals live in the DELTA between editions · finding_per_share_figures_break_across_splits — carry the split-invariant same-year RATIO · finding_exemption_is_where_a_rule_self_certifies — errors cluster in the CARVE-OUT, because quoting it feels like compliance; key exemptions to the mechanism (the clock), never a category name, and give the unlisted case the STRICT default · finding_rows_leave_when_the_reader_can_discharge_them — rows the reader can't close ALONE park forever; date-cap broadcasts · finding_anniversary_article_is_a_consensus_decoy — date-check the prior-year article · finding_edgar_fts_refutes_tradepress_negatives · finding_ais_port_export_darkfleet_blind · finding_terms_volume_lead_price_private_structures · finding_edgar_403_user_agent_header · finding_cftc_cot_raw_file_beats_socrata_lag — Socrata lags the 3:30 post; grade off raw f_disagg.txt · user_cruise_interest · feedback_dont_grade_solely_by_tradeable
- **Demoted from hot 2026-08-20 tranche 2 (same pass — failure-moment-triggered infra + settled conventions):** feedback_check_existing_design_docs · finding_ohlc_verify_before_session_claims · finding_announcement_type_and_filing_precheck · finding_csv_as_ground_truth · finding_quote_carries_data_minute · finding_tool_default_asof_date_drift · finding_yahoo_sparse_index_date_shift · finding_ragged_row_tolerance_hides_schema_change — 3 SILENT ways a scripted TSV-ledger write destroys/hides data (ragged tolerance = zero-row read · QUOTE_NONE truncate-then-raise · append w/o trailing newline merges records); write to .tmp+os.replace, field-count the WHOLE file *(hook re-joined 8/21 — the 8/20 pass-#2 demotion split it: tail stranded slug-less in the hot Infra line, head truncated here)* · finding_partitioned_source_returns_stale_window_at_200 — a clean 200 for a STALE partition; treat 200-with-empty and 200-that-stops-early as failures; audit the path before escalating · finding_skill_regated_not_removed — may be USER-invocable now; check the changelog · finding_blocked_mirror_is_not_an_unreachable_primary — a 403 is a fact about ONE MIRROR; enumerate hosts + try the API · finding_automation_reads_its_own_error_back_as_canon — audit its commits by git AUTHOR; output must never double as input without a staleness self-check · finding_subtotal_column_in_a_flattened_table_triple_counts — an API over a PRINTED table puts SUBTOTALS in a per-row column; my sum ran 3x

## Demoted 2026-08-20 (flow-rule pass #3, PROME closeout — hot index ≥75%; settled/predictable-trigger rows; ZERO deletions)
- feedback_pull_live_primary_not_dashboard
- feedback_read_research_before_opining
- feedback_verify_counts_before_propagating
- finding_verification_correction_downstream_propagation
- finding_external_consumer_check_before_restructure
- finding_comprehensive_grep_over_sampling
- feedback_suspect_fresh_pull_over_curated_record
- finding_sustain_trigger_effective_date_points_backward — dates to the EARLIEST print of the run; ask when the NEWEST one PUBLISHED
- finding_shared_antecedent_independence_test
- finding_independent_convergence_validates_schema
- finding_circular_corroboration_via_state_file
- feedback_outbox_restraint_for_push_friction
- finding_convergence_sign_check
- finding_cluster_adversarial_catches_framing
- finding_asymmetric_records_need_reconciliation
- finding_adversarial_verify_own_convergence
- feedback_break_multifile_updates
- feedback_behavior_language_over_hash_pinning
- finding_cross_surface_validation_pattern
- feedback_doc_routing_data_drops
- finding_seeded_selfsweep_secondary_surface_rot
- feedback_audit_packet_before_approval
- finding_outside_this_rail_disclosure
- feedback_refuse_rail_scope_creep
- feedback_evidence_standalone
- finding_board_lags_agents_not_vice_versa
- feedback_check_domain_owner_before_messaging
- feedback_check_recipient_before_sharing
- finding_coordinator_packet_position_row_staleness
- feedback_cross_agent_inbox_writes
- feedback_route_to_domain_agent
- finding_cross_flag_routing
- finding_concentration_disclosure_blind_to_backlog — keys on RECOGNIZED revenue; read RPO/backlog
- finding_just_read_artifact_frame_contamination
- feedback_single_source_liveevent_is_a_lead

## Demoted 2026-08-21 — flow-rule pass #4 residue AFTER the same-day v2 rollback (the v1 single-source queue was 86% false-cold: 12 of 14 rows artifact-rescued by census v2 and RETURNED to hot the same afternoon, fixture-verified; these 2 were cold on BOTH sources and stand)
- finding_overlapping_prereg_branches_restore_grader_discretion — two branches BOTH true = grader picks post-hoc; scope each branch to ONE surface
- finding_publication_date_is_not_the_event_date — weekday≠date means TWO dates in one sentence
## Demoted 2026-08-21 — flow pass #5 (Will-ruled in-session "okay lets execute it now"; ruling record `PROME/proposals/2026-08-21_flow-pass-5-embed-then-demote-RULED.md`). FIRST EMBED-THEN-DEMOTE pass (PAT-123 valve, first live use): 5 rows = census-v2 evidence queue (cold on BOTH sources 30d, 0 HELD); 11 rows = embed-GRADUATED (content verified present in `FORGE/PREDICTION_DISCIPLINE.md` — 3 since 7/31, 8+1 written 8/21 same pass after the "full canon" claim was found FALSE for 9 rows). ZERO deletions; memory FILES unchanged; rollback = move a row back to MEMORY.md.
- finding_projection_behind_a_confidence_is_an_unbase_rated_instrument — the "on pace" under a confidence is an instrument; 88% sat 50 days on one *(evidence queue + embedded → PREDICTION_DISCIPLINE 2026-08-21)*
- finding_redacting_command_output_is_not_evidence — a command written to HIDE a value can't report on it; test by length/exit code *(evidence queue, plain)*
- finding_same_datum_two_evidentiary_standards *(evidence queue, plain)*
- finding_thesis_loadbearing_sweep_scope *(evidence queue, plain)*
- finding_verify_live_api_schema_over_docs *(evidence queue, plain)*
- finding_threshold_level_is_a_measurement_not_a_constant — state FROZEN vs TRACKED *(embedded → PREDICTION_DISCIPLINE 2026-07-31)*
- finding_compound_gate_jointly_unsatisfiable — base-rate JOINTLY and CONDITIONALLY *(embedded → PREDICTION_DISCIPLINE 2026-07-31)*
- finding_confidence_priced_against_thesis_not_letter — resolves on the LETTER you wrote; run the inversion test *(embedded → PREDICTION_DISCIPLINE 2026-07-31)*
- finding_base_rate_the_threshold_before_building_it — base rate AND separation before shipping; "don't build it" is a real answer *(embedded → PREDICTION_DISCIPLINE 2026-08-21)*
- finding_prereg_verdict_boundary_must_be_a_number — a NUMBER + a NO-VERDICT band *(embedded → PREDICTION_DISCIPLINE 2026-08-21)*
- finding_unnamed_instrument_makes_a_threshold_a_family — unnamed instrument = you pick the flattering member post-hoc *(embedded → PREDICTION_DISCIPLINE 2026-08-21)*
- finding_enumerated_mechanism_test_hides_a_completeness_claim — an N-leg row silently claims the list is COMPLETE; outcomes arrive off-list *(embedded → PREDICTION_DISCIPLINE 2026-08-21)*
- feedback_register_the_call_even_when_you_expect_to_lose_it — the canon is ALL brakes; register the call you expect to LOSE, adjust the PRICE not the decision *(embedded → PREDICTION_DISCIPLINE 2026-08-21)*
- finding_overlapping_window_inflates_the_base_rate — de-cluster before base-rating *(embedded → PREDICTION_DISCIPLINE 2026-08-21)*
- finding_broken_conjunction_leaves_its_other_legs_unrecorded — a NOT-MET conjunction makes its other legs scoreless; scoreless is what nobody logs *(embedded → PREDICTION_DISCIPLINE 2026-08-21)*
- finding_extend_the_sample_before_publishing_a_coefficient — double n first *(embedded → PREDICTION_DISCIPLINE 2026-08-21)*

## Demoted 2026-08-21 — flow pass #6 / WAVE 2 "already embedded in canon" sweep (Will-ruled "approved go ahead with wave 2"; record `PROME/proposals/2026-08-21_wave-2-already-embedded-sweep-RULED.md`). All 129 hot slugs grepped against 14 canon surfaces; 16 hits each adjudicated at citation context; 11 graduated (embed real + audience served), 3 kept hot with recorded reasons (record_of_an_action n=11 · a_ruling_governs_next_write · hygiene_commit_rearms), 2 HELD-HOT skipped by declaration. ZERO deletions; rollback = move a row back.
- finding_count_what_published_before_reading_the_verdict — no adverse reading and "no reading" record identically
- finding_mtime_is_corrupted_by_git_sync — fails FALSE-NEGATIVE; derive vintage from content *(embedded → root CLAUDE.md Data Hygiene — auto-injected fleet-wide — + PROME/SYSTEM.md)*
- finding_freshness_check_cannot_catch_a_fresh_lie — add a positive AGREEMENT check vs an external truth source
- finding_fired_gate_needs_owner_independent_ledger *(embedded → PROME/CLOSEOUT.md symmetry table + ORCHESTRATION_PLAYBOOK; GATES.tsv itself is the institutionalized form)*
- finding_backstop_redelivery_is_a_paraphrase_not_a_copy *(embedded → STRICT_TEXT banked incident class)*
- finding_number_carries_threshold_unit_source *(embedded → STRICT_TEXT rule 7 by name + root Output Canon "no naked numbers")*
- finding_registry_names_a_concept_tool_resolves_an_instrument — diff the registry against the code; n=4 in one day *(embedded → STRICT_TEXT rule 7, exact sentence)*
- finding_deliberate_and_unnoticed_asymmetry_look_identical — read the RATIONALE before flagging *(embedded → CHECK_STANDARD §6 DECLARED ASYMMETRY, Batch B 8/21)*
- finding_standing_guard_is_a_false_negative_risk — the guard against a known FP is what waves away the real event *(embedded → CHECK_STANDARD bias-statement clause)*
- finding_verification_zero_is_ambiguous — NO findings ⊇ "read nothing" and "never in its scope"; a check certifies its SCOPE, not your capability *(embedded → CHECK_STANDARD scope clause)*
- finding_unfetched_is_not_unavailable — UNCHECKED ≠ UNAVAILABLE — classify before "blocked"; refuse offered stamps *(embedded → CHECK_STANDARD §8 rule 4 CANNOT-REACH vs GENUINELY-EMPTY — pointer corrected 8/21, DAEDALUS-caught)*

## Flow-rule demotion wave 2026-08-27 (hot 19,693 B / 76.9% → <70%; PROME executes per the 8/12 rule; hooks trimmed on move per 8/23 canon)
- finding_concurrent_agents_one_box_is_supported
- finding_concurrent_commit_index_race
- finding_pathspec_wildcard_ending_at_directory_matches_nothing
- feedback_verify_existence_external_primaries
- finding_ex_ante_filter_must_key_on_reach_not_consequence — hindsight rule; key ex-ante filters on REACH [n=1; hot at n≥2]
- finding_run_the_falsifier_before_promoting
- finding_audit_resolution_path_before_reattempt — usually the PATH, not missing data
- finding_guidance_is_not_the_instrument
- finding_url_date_inference_has_no_error_signal — inferred dates fail confidently
- finding_digit_regex_on_markup_can_match_the_threshold_value — an HTML digit-grep can return your exact frozen level
- finding_agreement_at_one_date_can_be_cancelling_errors — backfill across DATES
- finding_single_witness_guard_deletes_real_data
- finding_new_pin_needs_trajectory_before_level_read — pull history first
- finding_base_rate_the_instrument_before_its_event_table
- finding_never_received_is_not_doesnt_hold
- feedback_reconciliation_is_last_line_move_catch_upstream
- finding_no_action_ruling_does_not_disarm_an_automatic_mechanism — ask the BOOK (n+1: $71.3K)
- finding_private_by_construction_unverifiable
- finding_incentive_flag_source_weighting
- finding_audit_the_founding_metaphor_first
- feedback_trump_rhetoric_tape_not_info
- finding_complete_vs_selective_scan_drop_safe
- finding_a_teaching_surface_ages_like_data — date the figure half of canon
- finding_settle_basis_trigger_needs_a_post_close_observer — can't collect pre-close
- finding_a_guard_whose_only_remedy_is_rewording_a_true_line — FP on an honest line; reword-the-truth trap [n=1; hot at n≥2]
- finding_a_path_is_not_a_level_appending_asserts_unfetched_observations — endpoint right, direction wrong; re-pull the window [n=1; hot at n≥2]
