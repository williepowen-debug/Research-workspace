# Fleet Auto-Memory — COLD INDEX

> ⚠️ **CEILING: keep under 51,200 B** (Will-approved 2026-08-23). This is the SINK for `MEMORY.md`'s flow rule and nothing bounded it — it hit **58,825 B and truncated silently**, stranding 26 slugs while the hot index kept advertising them. **A pointer to unreachable text is worse than none.**
> **Legal: TRIM hook text · ROTATE waves out · SHARD by theme.** ⛔ Never delete a row (pointers — deleting orphans a memory). ⛔ Never raise the ceiling. ⛔ Demoted rows append at the END and the cut takes the END, so the newest rescues fall first.
> Check: `read_cap_check.py memory/auto/INDEX_COLD.md` (its % is vs a 60%-of-cap budget; the hard line is the measured **53,819 B**). **2026-08-23 pass: 60 hooks → ≤80 canon, 58,825 → 45,641 B, slugs 333==333 proven. ~134 still over canon.** **2026-08-28 TRIM pass (PROME-executed clerk, DAEDALUS TRIM-this-wave rec): 107 hooks → canon, 48,674 → 37,101 B = 72.5% of ceiling; row-slugs 329==329 AND whole-file slug tokens 363==363 proven (6 rows embed other slugs in their hooks — prose-only trimmed, still over canon by design). Next-wave form pre-registered: SHARD by theme when the file re-crosses ~43 KB (80% of the hard line).**

## Boot / closeout / handoff / revival / sync — embedded → `PROME/BOOT.md` § Boot-class fleet memories (2026-07-31; regrouped 8/29, all 14 slugs still named there)
- finding_display_filter_gating_safety_net — a forward-section display filter silently gates the past-due safety net too
- finding_boot_protocol_live_event_override — SPAWN PROTOCOL framing pulls agents to CLOSEOUT mid-event; needs a live override
- finding_boot_predictions_scan — a boot-time PREDICTIONS due/stale scan catches silently-stale OPEN predictions
- finding_boot_closeout_hardening_recipe — phased recipe: mirror, strip live-state, audit doc-ownership, punch-list
- finding_boot_py_cadence_skip_pattern — low-frequency desks: run-at-boot-defensively + mtime cadence-skip, not opt-in
- finding_boot_sweep_macro_regime_context — boot sweeps should check WHO runs the central banks, not just feeds
- finding_revival_proxy_pattern — Step 4 of PROME/ORCHESTRAL_LAYER_DESIGN.md
- finding_revival_boot_doc_sweep — reviving a 30d-stale agent: sweep every boot doc, not just STATUS — it compounds
- feedback_scan_agent_outboxes_at_boot — at PROME boot scan AGENTS/*/outbox/ too — signals sit outbox-resident
- feedback_front_load_planning — surface all decisions in a pre-execution pass; Will batch-approves, then execute
- finding_freshness_audit_vs_caught_up — fresh mtime ≠ caught up — an agent can still be behind inbox AND its own STATUS
- finding_gitignored_private_drop_boot_surfaced — gitignore hides private drops from git status too — pair with a boot-card line
- finding_fetch_before_trusting_boot_sync — git ahead/behind reads a stale local ref; fetch before declaring "synced"
- finding_inbound_lane_is_the_falsification_channel — a lane that can carry a falsifier for a thesis you own is boot-mandatory

## Closeout-moment rows — embedded → `PROME/CLOSEOUT.md` §Fleet-memory embeds (2026-07-31)
- finding_a_finding_written_too_abstract_will_not_bind_you — enumerate the STATES; a principle won't bind its own author
- finding_closeout_as_writeback_tail — codify closeout in the auto-loaded CLAUDE.md, not a standalone doc
- feedback_intra_day_closeout_discipline — run closeout at EVERY session end, not just end-of-day
- feedback_handoff_cadence — Will prefers handoffs at natural breakpoints over riding to degradation
- finding_state_token_sweep_all_surfaces — When a gate/decision state flips (e.g
- finding_completion_stamp_skip_reads_as_current — a file NAMED for currency that skips a closeout reads as current and wrong
- finding_derived_surface_fold_is_the_last_writeback — 5-of-5 stale derived surfaces were MID-SESSION writes left behind by later prima

## Sub-agents, teams & workflow orchestration — embedded → `PROME/ORCHESTRATION_PLAYBOOK.md` §Fleet-memory embeds (2026-07-31)
- finding_subagent_escalation_mode_discriminator — propose-only spawns: money/irreversible → Will; reversible → default + log
- feedback_subagent_prompt_discipline — 4 rules to keep research-spawn returns efficient without over-templating
- finding_subagent_idle_is_not_delivery — idle ≠ report delivered; make the FINAL TURN TEXT the deliverable (n=2)
- finding_subagent_memory_split — split spawn specs: durable mandate + dated MEMORY half, or spawns can't orient
- finding_subagent_baseline_audit — a maintain-a-set spec needs a BASELINE audit rubric, not just incremental
- finding_subagent_naming_identity_over_functional — Multi-agent systems with named sub-agents should prefer identity-naming (unique
- feedback_subagent_propagation_gap — sub-agent work doesn't rise to the parent; scan spawn KB/STATUS at closeout
- finding_subagent_prefire_date_verification — re-fetch cadence-derived dates within N days of fire; caught 2-day errors
- feedback_subagent_web_tools_not_autoloaded — research spawns may load WITHOUT WebSearch/WebFetch and silently return no data
- finding_subagent_year_verification — confirm the YEAR at the primary source; aggregators quote prior-year prints
- feedback_parallel_spawn_independent_agents — independent spawns go as multiple Agent calls in ONE message, never sequentially
- feedback_named_spawn_teams_mode — Naming an Agent spawn via the `name` parameter triggers team-mode (mailbox-based
- finding_fence_orchestration_live_agent — a directory fence must be ANNOUNCED to the live session and its commits watched
- finding_teams_mode_domain_agent_spawn — Teams-mode (named-spawn) works for domain agents like BOND
- finding_draft_only_teams_spawn — teams-mode pattern: draft into proposals/ only, no live-state edits
- finding_teams_mode_iterative_tasks — SendMessage beats spawn for ITERATIVE work; spawn is fine single-turn
- feedback_warm_parked_agent_collision — warm named teams agents collide next session; release at closeout or alias them
- feedback_orchestration_mode_split — split fan-out (Workflow) from live orchestration (teams-mode) before spawning
- finding_workflow_concurrency_529 — concurrent Workflow runs + live siblings hit account-API 529; cap parallelism
- finding_workflow_agent_unprompted_commit — workflow spawns have Edit+Bash and commit unprompted; scope them RESEARCH-ONLY
- finding_investigation_routing_discriminator — route by "do I need the answer THIS session?" — yes→inline verify, no→assign it
- finding_workflow_subagent_repo_sandbox — Workflow spawns are sandboxed to the repo tree; pass in-repo paths
- finding_write_behavior_check_before_agent_tool_run — grep another agent's tool for write ops first; a test run can become a write
- finding_workflow_scratch_crash_recovery — a crashed Workflow leaves spawn output in /tmp scratch; salvage it
- finding_workflow_rate_limit_resume_recovery — A /deep-research or Workflow killed mid-run by a session rate limit is recoverab
- finding_teams_mode_no_split_pane — teams mode has no split-pane on WSL2; Agent View is the second pane
- finding_batch_extraction_fanout_then_route — split mechanical extraction (fan out) from judgment (owner keeps routing)
- finding_warm_agent_multiround_sweep — keep named spawns resident, re-task in rounds — later rounds are cheap
- finding_duplicate_the_decision_changing_finding — run the ONE decision-changing finding twice, independent agents
- finding_warm_agent_proposal_round — After a task wave, a proposal round
- finding_scheduled_print_spawn_armed_state_report — require an ARMED-STATE report before first idle, else armed looks dropped
- finding_spawn_packet_seed_premise_verification — Coordinator-authored spawn-packet context claims (current time

## Spawn delivery contract — embedded → `PROME/COMPLETION_SPEC.md` §Fleet-memory embeds (2026-07-31)
- finding_two_phase_spawn_grader_contract — waiting on a print? two spawns, a FROZEN grader as the handoff contract
- finding_terminated_notice_can_precede_delivery — A teammate_terminated notice + an empty disk check does NOT prove a spawned agen
- finding_idle_notification_is_not_a_result — an idle spawn is not a report; chase the deliverable, check DISK before re-spawn
- finding_spawned_agents_ship_artifact_skip_writeback — spawns ship the artifact and SKIP their STATUS — put write-back in the contract

## Git rows verbatim in root canon — embedded → root `CLAUDE.md` Git Protocol (pre-existing text; no edit needed)
- feedback_agent_git_isolation — never stash/commit other agents' files; scope strictly to your own directory
- feedback_check_staged_before_commit — run git diff --cached before committing — catches pre-staged files
- feedback_git_mv_for_inbox_processing — use git mv not bash mv for inbox→processed; bash mv leaves the deletion unstaged
- feedback_defer_push_coordinate — push is automated at closeout via ff-gated safe-push; non-ff = rebase
- finding_push_train_pattern — one push ships every agent's unpushed commits; automated at closeout
- feedback_shared_log_row_author_commits — the author of a row in a shared log commits that row itself (Will-ratified 7/24)

## Prediction & calibration — embedded → `FORGE/PREDICTION_DISCIPLINE.md` (2026-07-31; hot residue re-based 2026-08-21 pass #5; **2 more embedded + demoted 2026-08-30, see that dated section**) ⚠️ **The "canon file carries the FULL set" claim has now gone FALSE TWICE (9 rows at 8/21, 2 rows at 8/30) — it is a live assertion that decays every time a prediction memory is written. Check it at each flow pass; never inherit it.**
- finding_widened_scope_needs_rescoped_instrument — widening a prediction's scope with the old base-rate instrument can pre-fail it
- finding_discovery_instrument_defines_the_claim — press-sampling measures YOUR discovery latency, not the world — name the scan
- finding_redated_falsifier_inherits_premise — When you re-date a falsifier/prediction because a catalyst moved
- finding_prereg_dates_the_event_not_the_artifacts_cadence — a prereg resolving on an ARTIFACT is dated by that artifact, not the event
- finding_lessons_file_cannot_detect_own_contradictions — A prose lessons/LEARNINGS file cannot detect its own contradictions
- finding_prereg_symmetric_magnitudes_can_hide_an_unreachable_branch — a trigger that CANNOT fire; re-run reachability on the AMENDED text (n=4)
- finding_pre_register_against_the_carrying_filing — Pre-register a threshold against the FILING/SOURCE that carries the metric
- finding_anchor_prediction_to_surprise_not_priced — anchor event→reaction to the SURPRISE-vs-pricing, not an already-priced outcome
- finding_continuation_hits_are_not_calibration — split a prediction book's hit rate by CONTINUATION vs TURN
- finding_thin_liquidity_prediction_market_discipline — thin prediction-market single prints aren't "holds"; cross-verify (≥3d)
- finding_calibration_discount_regime_conditional — an earned calibration discount is conditional on its pricing regime
- feedback_two_way_read_directional_clarity — When presenting a \two-way read\" or scenario branches"
- feedback_corrected_framing_calibration — verify-research's modal verdict is CORRECTED-FRAMING; keep the direction
- finding_threshold_vs_mechanism — separate "mechanism intact" from "threshold holds" — TRUE-letter, FALSE-spirit
- finding_catalyst_vs_consequence_conflation — catalyst probabilities inflate as consequence; require P(C|catalyst)
- feedback_prediction_canonical_measure — When revising a prediction
- feedback_single_month_subcomponent_skepticism — Single-month sub-component metric moves (ISM internals, CMBS by-property-type **[+REVISION axis, CARL 9/5, n=1 — the 2nd-print remedy does NOT cover it; promotion flagged to PROME]**
- finding_noise_filter_erases_signal_class — before widening a noise filter, check if the true positives live in the noise
- feedback_forward_discovery_prediction_spirit — resolve forward-discovery by SPIRIT (found in-window?), not literal text
- feedback_litigation_allegation_weighting — Plaintiff/litigation-allegation-only signals should be weighted ≤40% confidence
- finding_base_rate_vs_mechanism_discriminator — a novel mechanism bypasses discriminators, emitting a confident wrong veto
- finding_catalyst_path_decoupling — level trigger ≠ path trigger; another upstream path kills the path claim only
- finding_pre_registration_discipline_through_corroboration — hold a pre-registered mark through interim corroboration; don't fire early
- finding_level_conditional_probability_remarking — a probability attached to a price level re-marks itself as spot moves
- finding_sustain_count_role_discriminating_power — a registered trigger needs a stated ROLE; "can't catch that" is an answer
- finding_delta_vs_own_prior_local_extreme — a Δ against your OWN prior misleads if that prior was a local extreme
- feedback_dont_retire_dormant_thesis — de-escalated catalyst → dormant/armed convexity + re-arm trigger, don't kill it
- finding_flow_discriminator_vs_narrative — trust the pre-registered discriminator over the street, after a staleness check
- finding_seasonal_trough_baseline_resolves_true_on_normal — a falsifier baselined on a seasonal trough resolves TRUE on ordinary recovery
- finding_sample_size_vs_identification_defect — "more data" fixes a sample-size defect, never an identification one; check which
- finding_perturb_inputs_to_test_base_rate — reproducing a base rate proves arithmetic; perturb its INPUTS at source instead
- finding_gate_bias_is_placement_error_compare_to_margin — a threshold bias is a PLACEMENT error; compare it to the realized margin first
- finding_absence_tell_needs_a_talkative_instrument — "they didn't mention X" needs a source with room and habit to mention it

## Trade / position / risk discipline — ✅ **embedded → `AGENTS/TERRY/RISK_RULES.md`** (all 13 rows below; TERRY-confirmed 2026-08-04, new section "Durable findings — EMBEDDED FROM AUTO-MEMORY 2026-08-04", above Postmortem Tags). Grouped not flat, at TERRY's judgment — RISK_RULES is a **fire-time** document, and a flat 13 is scanned while a grouped one is found. ⚠️ `finding_profit_zone_needs_its_own_harvest_rule` is labelled there as **NO_HARVEST_RULE** (Will-ruled fleet-wide 7/31) with its cost attached — root cause of this desk's only realized loss, −$111.60 on TRY-VIOLET-VIXCS. **Embedding the finding is NOT adoption of the NO_HARVEST template** (WILL_QUEUE row 11, still open)
- feedback_deploy_on_trigger_not_calendar — Will deploys fresh capital ONLY on a fired trigger, never on book-maintenance
- feedback_position_cost_basis_not_authoritative — never cite cost-basis/P&L from state files as authoritative; confirm with Will
- feedback_put_vs_duration_expression — in a suppressed tape single-name puts bleed; match vehicle to the OPEN channel
- feedback_exit_recommendations_need_mark_context — surface the execution mark before recommending an exit, else propose a window
- finding_option_marks_need_live_chain — carried option marks go phantom; pull the live chain at every decision point
- finding_workbook_demote_by_verification — verify live-consumer + counterparty BEFORE freezing a ledger; triage by Group
- finding_risk_control_separate_from_sizing — a collapsed AND-leg DISARMS the stop; re-spec is risk control, not sizing
- finding_registered_killswitch_cost_datum — when a kill-switch fires, hold the verdict, log the cost, never retro-apply
- finding_vrp_split_rates_vs_singlename — The post-2012 SPX variance-risk-premium collapse does NOT apply uniformly
- finding_cooldown_gate_differential_main_vs_hedge — A vol/cooldown gate blocks fresh MAIN-arm capital deployment (paying vega on a n
- finding_fill_in_principle_vs_final_approve_pattern — Two-stage fill approval: Will [Approve in principle] unblocks TERRY's live re-ma
- finding_profit_zone_needs_its_own_harvest_rule — triggers keyed to a further move leave none that fires on merely profitable
- finding_grade_execution_only_against_same_timestamp_marks — grading a fill against marks from another time manufactures a fake finding

## Deep-research method — embed-pending → `AGENTS/DEWEY/CLAUDE.md` (already cited inline there; packet 2026-07-31)
- finding_a_challenge_that_strengthens_its_target_is_a_success — conclusion survives, evidence replaced IS the finding, not a null
- finding_deep_research_stale_vintage_headline — the load-bearing headline figure is often a stale VINTAGE; refresh it
- finding_deep_research_slate_mining — Build deep-research prompt slates by mining agents' SELF-flagged gaps
- finding_deep_research_primary_pull_owns_three_data_classes — deep research cannot reach paywalled, live-reading, or single-name filings

## Agent-specific pointers — embed-pending → each agent's own CLAUDE.md/boot card (packets 2026-07-31)
- **LABOR:** project_labor_standing_nexus_brief — LABOR keeps a standing NEXUS_BRIEF.md refreshed every closeout [embedded→LABOR]
- **BRENT:** project_energy_strike_ledger — HAWK keeps ONE cross-theater strike ledger, not silos [embedded→BRENT]
- **HENRY:** feedback_henry_macro_focus_not_positions — macro + market trends, NOT trade-position management · feedback_henry_vol_broadcast_to_violet — VIOLET owns vol-regime broadcast · reference_henry_operating_dashboard — LIVING Artifact, refresh the SAME URL · *all 3 embedded → AGENTS/HENRY/CLAUDE.md*
- **RED:** feedback_red_edge — always present the best counter-case, honest and realistic, not contrarian
- **WALTER:** project_walter_cop_direction — RESOLVED/tombstoned — shipped as WALTER's BOARD; design against BOARD_CONSUMPTION_SPEC · project_walter_image_signal_intake — WALTER owns image/screenshot intake · feedback_walter_autonomous_verify — may spawn verify-research without asking · feedback_walter_no_kill_on_lede — read the body before classifying · finding_walter_refactor_pattern — sequenced-pass structural refactor recipe · project_telegram_plugin_scope — plugin config at AGENTS/WALTER/.claude/settings.json · feedback_telegram_reply_required — Telegram asks get Telegram replies · *all 7 embedded → AGENTS/WALTER/CLAUDE.md*
- **CARL:** feedback_carl_kb_architecture — keep CARL KB thesis-level; push domain data to sub-agent KBs [embedded→CARL]
- **TERRY:** project_terry_daytrading_review_system — standing day-trading review loop; Will wants trades tracked · reference_terry_desk_dashboard — LIVING desk dashboard Artifact · *both embedded → AGENTS/TERRY/CLAUDE.md*
- **DAEDALUS:** project_daedalus_maturity_map_hygiene_input — the L0-L5 maturity map is a hygiene input, not a scoreboard [embedded→DAEDALUS]
- **VIOLET:** reference_violet_vol_cheatsheet — LIVING vol cheat-sheet Artifact; refresh in place to the same URL · reference_violet_operating_picture — LIVING Operating Picture Artifact, same URL · *both embedded → AGENTS/VIOLET/CLAUDE.md*

## Project-state (Tier-3 COLD, no embed target — read on demand)
- project_messaging_overhaul — don't invest in inbox/outbox hygiene — file messaging is being replaced
- project_research_intake_collection_lane — RESEARCH-INTAKE = always-on data lane, separate repo; agents read-only
- project_public_prep_anthropic_fellows — repo being prepped public as portfolio for Will's Anthropic Fellows (Economics &
- project_automem_symlink_migration — TOMBSTONE — folded into the hardlink-inplace-edit finding; kept as a name-anchor
- project_phone_signal_architecture — Will wants reliable phone→fleet signal ingestion (Telegram drops)

## Tool gotchas — embed-pending → tool headers
- finding_crlf_textmode_tsv_flip — two silent whole-file TSV rewrites; guard = git diff --stat *(n=3)*
- finding_printf_format_tsv_append_corruption — shell printf corrupts a TSV/log row when the data contains (embed-pending)
- finding_market_data_venv_invocation — market-data scripts need repo .venv python; system python3 fails (embed-pending)
- finding_subdir_launch_hooks_dont_fire — root .claude/settings.json hooks do NOT fire for subdir-launched sessions
- finding_truncated_read_is_not_a_verification — truncation drops the TAIL, where the exculpatory half lives

## Rare infra findings (Tier-3 COLD)
- finding_never_infer_a_documents_subject_from_token_presence — name-in-body is not about; reports all FRESH, goes quiet forever
- finding_gh_run_watch_exit_status_unreliable — gh run watch --exit-status can lie; confirm via gh run view --json conclusion
- finding_injection_claim_is_openclaw_vestige — verify a file is actually boot-loaded before calling it load-bearing
- finding_fdic_securities_filings_api — FDIC securities-filings JSON API (securitiesfilings.fdicconnect.fdic.gov) gives
- finding_tic_cslt_country_transactions — country TIC net transactions moved to CSLT JSON; S-forms frozen, mfh.txt is dead
- finding_pandas_column_method_collision — pandas columns named like DataFrame methods return the METHOD via dot-access
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
- feedback_cross_agent_inbox_writes — author commits own cross-agent packet; 'leave untracked' DEAD [cold-direct 8/28]

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
- finding_prereg_branch_label_can_contradict_its_condition — check the branch LABEL against the sign of its CONDITION; NO-CALL if not
- finding_named_risk_underweighted_is_its_own_error — you WROTE the caveat then priced it low; PROVISIONAL must show in the NUMBER
- finding_priced_probability_destroys_surprise_room — track the UNPRICED remainder, not the level
- finding_expected_window_rederived_from_now_drifts — pin the anchor; consume, never re-derive; past it = channel finding
- finding_pre_decision_condition_vs_rationale — report CONDITION and RATIONALE separately; adjudicate neither
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
- finding_roster_change_propagates_to_all_surfaces — the surface a sweep cannot catch = the PARENT threshold registry [n=3; promo flag 9/1 DECLINED — hot at 74%]
- finding_reconcile_match_on_key_not_substring
- finding_owned_surface_without_a_ledger_destroys_history — ownership ≠ retention
- finding_proposed_rule_must_be_canon_tested — canon-test a NEW rule before downstream is written against it
- finding_ownership_claim_is_last_to_move — when the OWNER moves, docs saying who owns it go stale and defend themselves
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
- **Demoted from hot 2026-08-20 (flow-rule pass #2, PROME closeout — settled rows; ZERO deleted):** finding_diff_the_vintages_not_just_refresh — reversals live in the DELTA · finding_per_share_figures_break_across_splits — carry the split-invariant RATIO · finding_exemption_is_where_a_rule_self_certifies — errors cluster in the CARVE-OUT; key to the mechanism, strict default · finding_rows_leave_when_the_reader_can_discharge_them — rows the reader can't close alone park forever · finding_anniversary_article_is_a_consensus_decoy — date-check it · finding_edgar_fts_refutes_tradepress_negatives · finding_ais_port_export_darkfleet_blind · finding_terms_volume_lead_price_private_structures · finding_edgar_403_user_agent_header · finding_cftc_cot_raw_file_beats_socrata_lag — grade off raw f_disagg.txt · user_cruise_interest · feedback_dont_grade_solely_by_tradeable
- **Demoted from hot 2026-08-20 tranche 2 (same pass — failure-moment infra + settled conventions):** feedback_check_existing_design_docs · finding_ohlc_verify_before_session_claims · finding_announcement_type_and_filing_precheck · finding_csv_as_ground_truth · finding_quote_carries_data_minute · finding_tool_default_asof_date_drift · finding_yahoo_sparse_index_date_shift · finding_ragged_row_tolerance_hides_schema_change — 3 SILENT ways a scripted TSV write hides data; write .tmp+os.replace, field-count the file · finding_partitioned_source_returns_stale_window_at_200 — a clean 200 for a STALE partition · finding_skill_regated_not_removed — check the changelog · finding_blocked_mirror_is_not_an_unreachable_primary — a 403 is about ONE MIRROR; try the API · finding_automation_reads_its_own_error_back_as_canon — audit its commits by git AUTHOR · finding_subtotal_column_in_a_flattened_table_triple_counts — an API over a PRINTED table returns SUBTOTALS

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
- finding_board_lags_agents_not_vice_versa — ahead/behind is per-LEG, not per-agent [n=2; promo flag 9/1 DECLINED — hot at 74%]
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
- finding_projection_behind_a_confidence_is_an_unbase_rated_instrument — the "on pace" under a confidence is an instrument; 88% sat 50 days on one
- finding_redacting_command_output_is_not_evidence — a command written to HIDE a value can't report on it; test by length/exit code
- finding_same_datum_two_evidentiary_standards *(evidence queue, plain)*
- finding_thesis_loadbearing_sweep_scope *(evidence queue, plain)*
- finding_verify_live_api_schema_over_docs *(evidence queue, plain)*
- finding_threshold_level_is_a_measurement_not_a_constant — state FROZEN vs TRACKED *(embedded → PREDICTION_DISCIPLINE 2026-07-31)*
- finding_compound_gate_jointly_unsatisfiable — base-rate JOINTLY and CONDITIONALLY [embedded→PREDICTION_DISCIPLINE]
- finding_confidence_priced_against_thesis_not_letter — resolves on the LETTER you wrote; invert it [embedded→PREDICTION_DISCIPLINE]
- finding_base_rate_the_threshold_before_building_it — base rate AND separation before shipping [embedded→PREDICTION_DISCIPLINE]
- finding_prereg_verdict_boundary_must_be_a_number — a NUMBER + a NO-VERDICT band *(embedded → PREDICTION_DISCIPLINE 2026-08-21)*
- finding_unnamed_instrument_makes_a_threshold_a_family — unnamed instrument = you pick post-hoc [embedded→PREDICTION_DISCIPLINE]
- finding_enumerated_mechanism_test_hides_a_completeness_claim — an N-leg row silently claims a COMPLETE list [embedded→PREDICTION_DISCIPLINE]
- feedback_register_the_call_even_when_you_expect_to_lose_it — register the call you expect to LOSE [embedded→PREDICTION_DISCIPLINE]
- finding_overlapping_window_inflates_the_base_rate — de-cluster before base-rating *(embedded → PREDICTION_DISCIPLINE 2026-08-21)*
- finding_broken_conjunction_leaves_its_other_legs_unrecorded — a NOT-MET conjunction leaves its legs scoreless [embedded→PREDICTION_DISCIPLINE]
- finding_extend_the_sample_before_publishing_a_coefficient — double n first *(embedded → PREDICTION_DISCIPLINE 2026-08-21)*

## Demoted 2026-08-21 — flow pass #6 / WAVE 2 "already embedded in canon" sweep (Will-ruled "approved go ahead with wave 2"; record `PROME/proposals/2026-08-21_wave-2-already-embedded-sweep-RULED.md`). All 129 hot slugs grepped against 14 canon surfaces; 16 hits each adjudicated at citation context; 11 graduated (embed real + audience served), 3 kept hot with recorded reasons (record_of_an_action n=11 · a_ruling_governs_next_write · hygiene_commit_rearms), 2 HELD-HOT skipped by declaration. ZERO deletions; rollback = move a row back.
- finding_count_what_published_before_reading_the_verdict — no adverse reading and "no reading" record identically
- finding_mtime_is_corrupted_by_git_sync — fails FALSE-NEGATIVE; derive vintage from content [embedded→root CLAUDE.md]
- finding_freshness_check_cannot_catch_a_fresh_lie — add a positive AGREEMENT check vs an external truth source
- finding_fired_gate_needs_owner_independent_ledger *(embedded → PROME/CLOSEOUT.md symmetry table + ORCHESTRATION_PLAYBOOK; GATES.tsv itself is the institutionalized form)*
- finding_backstop_redelivery_is_a_paraphrase_not_a_copy *(embedded → STRICT_TEXT banked incident class)*
- finding_number_carries_threshold_unit_source *(embedded → STRICT_TEXT rule 7 by name + root Output Canon "no naked numbers")*
- finding_registry_names_a_concept_tool_resolves_an_instrument — diff the registry against the code; n=4 in one day [embedded→STRICT_TEXT r7]
- finding_deliberate_and_unnoticed_asymmetry_look_identical — read the RATIONALE before flagging [embedded→CHECK_STANDARD §6]
- finding_standing_guard_is_a_false_negative_risk — a guard against a known FP waves away the real event [embedded→CHECK_STANDARD] [n=4 forms; promo flag 9/1 DECLINED — embedded, hot at 74%]
- finding_verification_zero_is_ambiguous — NO findings ⊇ "read nothing"; a check certifies SCOPE [embedded→CHECK_STANDARD]
- finding_unfetched_is_not_unavailable — UNCHECKED ≠ UNAVAILABLE — classify before "blocked" [embedded→CHECK_STANDARD §8]

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

## Demoted from HOT — 2026-08-28 (flow-rule pass at PROME closeout; hot index hit the 75% trip line; settled/predictable-trigger rows, hooks cut to canon as they move)
- finding_date_keyed_scanner_cannot_see_an_early_resolver — date-keyed due-scan reads an EARLY resolver as all-clear [n=3, FLG 8/28]
- finding_frozen_fixture_control_is_blind_to_resolution_faults — frozen fixture tests the parser, certifies a broken pipeline
- finding_joint_base_rate_is_explained_by_its_rarest_leg — joint rate is small because ONE leg is rare; compare to product of marginals
- finding_univariate_residual_is_a_claim_about_the_model — 'X% unexplained' is a claim about your MODEL; a co-symptom control is a MEDIATOR
- finding_parse_failure_folded_into_a_benign_bucket — a failure counted as 'Routine' fabricates a finding; split the counter
- finding_rising_stock_flat_inflow_means_slower_outflow — flat inflow = the DRAIN slowed; ask what empties the stock
- feedback_number_every_decision_by_will_queue_row — ⚖️ blocks cite their WQ row, registered before the ask (rule lives in WQ + USER.md)
- finding_reading_review_cannot_find_what_an_executing_stranger_finds — 4 read passes → 0 ❌; 2 EXECUTING strangers → 6 defects, 5 in the manuals pointed at (8/29)

## Demoted from HOT — 2026-08-29 EVE (structure lane, Will "approved go ahead" 22:17; two prediction rows RETURNED to hot 22:3x pending their real canon embed — Codex, verified; hot index at 74.7% = one row from the 75% trip — pre-emptive pass under the 8/12 flow rule; settled/predictable-trigger rows, hooks cut to canon as they move; ZERO deletions; rollback = move a row back)
- finding_fdic_failures_api_lags_the_newest_failure — FDIC failures API lags ~7d; HTML paginates; neither naive read is complete
- finding_continuous_front_ticker_rolls_so_deltas_lie — a continuous front ticker rolls, so deltas across the roll lie (HEARTBEAT canon)
- finding_historical_fire_count_assumes_one_regime — 'would it have fired before?' scores correct old-regime fires as false positives
- finding_inherited_default_threshold_is_a_silent_decision — set the bound from the CADENCE of what you measure, vs a companion artifact
- finding_escalation_ladder_blind_to_its_first_observable — HYPOTHESIS n=1: counterparty PAUSE may precede official acts; candidate rung (0)
- finding_bare_since_date_drops_same_day_commits — --since=DATE means 'since now-o'clock today'; a zero-result delivery check lies

## Demoted 2026-08-30 — embed-then-demote (PROME, WQ-133 leg; Will *"proceed with the two prediction-canon embeds if they are already scoped under WQ-133"* — verified scoped, rec column reads "PROME runs these in a structure session; no ruling needed"). Both rows were demoted-pending-embed and grepped **ZERO** in `FORGE/PREDICTION_DISCIPLINE.md`, so `MEMORY.md`'s "full canon is embedded" header was FALSE for them (SCRATCH kill-on-sight #6, now discharged). **Embedded first, demoted second — the order WQ-133 required.** ZERO deletions; memory FILES unchanged; rollback = move a row back to MEMORY.md.
- finding_conditional_swap_needs_base_rate_at_registration — base-rate the swap-in leg at REGISTRATION [embedded→PREDICTION_DISCIPLINE]
- finding_corrective_inherits_the_anchor_it_corrects — write it cold, score the correction [embedded→PREDICTION_DISCIPLINE]

## Demoted 2026-09-01 NIGHT (PROME flow pass — MEMORY.md 75%→<70%; predictable-moment git/closeout triggers; hooks ≤80 canon at the move; slug-conservation proven in the commit)
- finding_pathspec_rename_needs_both_paths — a pathspec commit of a rename needs BOTH the old and the new path
- finding_dirty_path_means_in_flight_not_orphaned — a dirty path is a peer's in-flight work, never an orphan to sweep
- finding_push_train_hides_a_failed_commit — "Pushed." can be true of OTHERS' commits; verify your own paths after
- finding_git_mv_rescopes_gitignore_rules — a tree move un-ignores files silently; git status after ANY move
- feedback_git_reconcile_scope
- finding_add_with_one_bad_pathspec_stages_nothing — `git add A B C` is ATOMIC: one bad path stages NOTHING (root Git Protocol)
- finding_banner_is_a_warning_not_a_fix — pair every banner with a dated rewrite trigger
- finding_hygiene_commit_rearms_the_staleness_lie — a sweep COMMIT re-arms git-time freshness fallbacks
- finding_dated_stamp_is_a_trigger_not_a_shield — a stamp older than last session forces re-pull-or-freeze
- finding_canonical_surfaces_stale_inbox_carries_live_state — the live fact rides the unprocessed INBOX, not the canonical surface
- finding_reconcile_mismatch_does_not_say_which_side_is_wrong — adjusting the COUNT destroys the evidence; flags are a LOWER BOUND
- finding_persistence_threshold_needs_panel_depth_not_just_a_metric — N-period rule on a panel never observed N times; 0 fires is structural
- finding_gate_calibration_is_a_claim_about_its_remedys_price — cheaper remedy = stale gate; the risky error flips to the SILENT one
- finding_spec_that_is_both_falsifier_and_trigger_permits_only_disambiguation — rule the definition, escalate the retune; measure direction
- finding_a_fix_can_relocate_a_constraint_and_report_it_removed — a fix whose precondition is the obstacle's class reads as a solution
- finding_supersession_marker_suppresses_the_live_value_beside_it — the archival value is what travels; scoring conventions suppress too
- finding_option_menu_omitting_the_owners_choice_reads_as_silence — a closed menu makes an off-menu disposition invisible (3d early read 30d late)
- finding_ranked_head_sample_is_not_the_population — a rate off an age-ranked head over-estimates; age correlates with outcome
- finding_hypothesis_needs_an_instrument_for_its_defining_mechanism — name the instrument for the mechanism the NAME refers to
- finding_executability_is_a_separate_audit_axis — can the rule be graded AND acted on inside its instruments' window?
- finding_rejecting_an_instrument_is_an_audit_of_it — ruling a tool out for one question? audit it before setting it aside
- finding_banded_threshold_with_no_metric_surface_is_untrippable — no metric vector = untrippable threshold; row-counting audits pass clean
- finding_port_exposes_what_share_propagates — reinvent HIDES defects, share PROPAGATES, port EXPOSES

## Demoted 2026-09-06 (PROME flow pass at WALTER's 75% flag, 19,323 B → <70%; predictable-trigger / grade- and audit-moment rows; hooks cut to ≤80 chars on the move; slug union conserved — see the commit)
- finding_definition_change_moves_the_evidence_for_the_level — rule the DEFINITION first; it moves the level's own n= [HOMER 8/22, caught pr…
- finding_relative_threshold_cannot_be_graded_by_a_one_sided_instrument — a comparative threshold needs BOTH sides; a clean one-sided measure cannot re…
- finding_registered_trigger_can_fire_on_an_unnamed_mechanism — metric hit, registered CAUSE absent = NOT a fire; re-read the mechanism clause
- finding_frozen_spec_and_the_surfaces_describing_it_drift_apart — the LETTER cannot drift; the surfaces DESCRIBING it do, and those are what yo…
- finding_dormant_instrument_is_a_query_plus_unexercised_reading_rules — dormant instrument = query + unexercised reading-rules; "runs?" certifies half
- finding_verify_loadbearing_before_trade
- finding_relayed_level_predates_the_event
- finding_coverage_gap_needs_all_surface_check
- finding_registered_gate_captures_attention — sweep the un-gated instruments separately
- finding_bypass_turns_a_flow_proxy_into_a_routing_metric — a bypass turns a flow proxy into a ROUTING metric; meaning moves, instrument…
- finding_level_published_in_narrative_can_vanish_from_an_edition — a level in a chart/prose can vanish from an EDITION; the re-point recreates it
- finding_measurement_bias_sign_is_fixed_harm_direction_is_not — a bias's SIGN is fixed; whether it's protective or dangerous belongs to the T…
- finding_instrument_cadence_cannot_resolve_the_claims_window — samples slower than the window the claim is about; freshness checks are blind
- finding_cohort_too_small_to_move_the_index — do the WEIGHT arithmetic before blaming a cohort
- finding_window_start_at_an_extremum_inverts_the_move — a Δ off a local peak measures the EXTREMUM; price the window BEFORE it
- finding_effect_below_instrument_detection_floor — below the noise floor is no evidence, not weak evidence
- finding_backup_copy_must_carry_the_predeclared_negative — a pre-declared negative doesn't compress; it insures the wrong half
- finding_deferral_rule_hides_its_own_cost — a HOLD rule's cost is invisible when you obey it; for a pull-complete recipie…
- finding_retired_threshold_has_no_publisher — retirement is a side effect nothing announces; readers travel against the links
- finding_anti_ratchet_governs_state_not_prose — counts rows, never WORDS; a REWRITE pass can ADD bytes (n=2)
- finding_synthetic_artifact_defeats_provenance_tracing — trace-to-originator INVERTS on generated media; primary for WHAT HE SAID only
- finding_primary_is_not_one_tier — a contract is WEAK about third-party docs it recites; one source cannot see it
