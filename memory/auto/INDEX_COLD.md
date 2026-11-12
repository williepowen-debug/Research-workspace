# Fleet Auto-Memory — COLD INDEX

> ⚠️ **CEILING: keep under 51,200 B** (Will-approved 2026-08-23). This is the SINK for `MEMORY.md`'s flow rule and nothing bounded it — it hit **58,825 B and truncated silently**, stranding 26 slugs while the hot index kept advertising them. **A pointer to unreachable text is worse than none.**
> **Legal: TRIM hook text · ROTATE waves out · SHARD by theme.** ⛔ Never delete a row (pointers — deleting orphans a memory). ⛔ Never raise the ceiling. ⛔ Demoted rows append at the END and the cut takes the END, so the newest rescues fall first.
> Check: `read_cap_check.py memory/auto/INDEX_COLD.md` (its % is vs a 60%-of-cap budget; the hard line is the measured **53,819 B**). **2026-08-23 pass: 60 hooks → ≤80 canon, 58,825 → 45,641 B, slugs 333==333 proven. ~134 still over canon.** **2026-08-28 TRIM pass (PROME-executed clerk, DAEDALUS TRIM-this-wave rec): 107 hooks → canon, 48,674 → 37,101 B = 72.5% of ceiling; row-slugs 329==329 AND whole-file slug tokens 363==363 proven (6 rows embed other slugs in their hooks — prose-only trimmed, still over canon by design). Next-wave form pre-registered: SHARD by theme when the file re-crosses ~43 KB (80% of the hard line).** **2026-09-30 flow pass (PROME, at a boot — skipped at two closeouts): 18 settled rows demoted in, 2 promoted out; this file RE-CROSSED the ~43 KB line ⇒ the pre-registered SHARD-by-theme wave is OWED at the next flow pass (current size: `PROME/tools/measure.py`).**

## Embedded → canon sections — MOVED to `memory/auto/INDEX_COLD_EMBEDDED.md` (shard 2026-09-06)
- The eight census sections (Boot/closeout · Closeout-moment · Sub-agents/orchestration · Spawn delivery · Git rows · Prediction & calibration · Trade/risk · Deep-research) live verbatim in the shard, crc32 2994654163 over its body; every slug they carry is still indexed (readers glob `INDEX_COLD*.md`). This file keeps the agent pointers, project-state, tool gotchas, rare infra and every demotion wave (the 2026-08-12 to 08-21 waves are in the closed shard `INDEX_COLD_2026-08-waves.md`).

## Agent-specific pointers — embed-pending → each agent's own CLAUDE.md/boot card (packets 2026-07-31)
- **LABOR:** project_labor_standing_nexus_brief — LABOR keeps a standing NEXUS_BRIEF.md refreshed every closeout [embedded→LABOR]
- **BRENT:** project_energy_strike_ledger — HAWK keeps ONE cross-theater strike ledger, not silos [embedded→BRENT]
- **HENRY:** feedback_henry_macro_focus_not_positions — macro + market trends, NOT trade-position management · feedback_henry_vol_broadcast_to_violet — VIOLET owns vol-regime broadcast · reference_henry_operating_dashboard — LIVING Artifact, refresh the SAME URL · *all 3 embedded → AGENTS/HENRY/CLAUDE.md*
- **RED:** feedback_red_edge — always present the best counter-case, honest and realistic, not contrarian [embedded→RED — confirmed 2026-08-02 (RED OUTBOX item 4), PROME-verified at AGENTS/RED/CLAUDE.md 2026-09-07]
- **WALTER:** project_walter_cop_direction — RESOLVED/tombstoned — shipped as WALTER's BOARD; design against BOARD_CONSUMPTION_SPEC · project_walter_image_signal_intake — WALTER owns image/screenshot intake · feedback_walter_autonomous_verify — may spawn verify-research without asking · feedback_walter_no_kill_on_lede — read the body before classifying · finding_walter_refactor_pattern — sequenced-pass structural refactor recipe · project_telegram_plugin_scope — plugin config at AGENTS/WALTER/.claude/settings.json · feedback_telegram_reply_required — Telegram asks get Telegram replies · *all 7 embedded → AGENTS/WALTER/CLAUDE.md*
- **CARL:** feedback_carl_kb_architecture — keep CARL KB thesis-level; push domain data to sub-agent KBs [embedded→CARL]
- **TERRY:** project_terry_daytrading_review_system — standing day-trading review loop; Will wants trades tracked · reference_terry_desk_dashboard — LIVING desk dashboard Artifact · *both embedded → AGENTS/TERRY/CLAUDE.md*
- **DAEDALUS:** project_daedalus_maturity_map_hygiene_input — the L0-L5 maturity map is a hygiene input, not a scoreboard [embedded→DAEDALUS]
- **VIOLET:** reference_violet_vol_cheatsheet — LIVING vol cheat-sheet Artifact; refresh in place to the same URL · reference_violet_operating_picture — LIVING Operating Picture Artifact, same URL · *both embedded → AGENTS/VIOLET/CLAUDE.md*

## Project-state (Tier-3 COLD, no embed target — read on demand)
- project_messaging_overhaul — don't invest in inbox/outbox hygiene — file messaging is being replaced
- project_public_prep_anthropic_fellows — repo being prepped public as portfolio for Will's Anthropic Fellows (Economics &
- project_automem_symlink_migration — TOMBSTONE — folded into the hardlink-inplace-edit finding; kept as a name-anchor
- project_phone_signal_architecture — Will wants reliable phone→fleet signal ingestion (Telegram drops)

## Tool gotchas — embed-pending → tool headers
- finding_printf_format_tsv_append_corruption — shell printf corrupts a TSV/log row when the data contains [embedded→scripts/tsv_append.py — DEWEY-verified 2026-08-02, PROME-verified 2026-09-07]
- finding_market_data_venv_invocation — market-data scripts need repo .venv python; system python3 fails (embed-pending)
- finding_subdir_launch_hooks_dont_fire — root .claude/settings.json hooks do NOT fire for subdir-launched sessions [embedded→PROME/BOOT.md step 0 — cited by slug; DEWEY-verified 2026-08-02, PROME-verified 2026-09-07]
- finding_truncated_read_is_not_a_verification — truncation drops the TAIL, where the exculpatory half lives

## Rare infra findings (Tier-3 COLD)
- finding_parallel_agents_sharing_one_scratchpad_overwrite_each_others_files — parallel agents in one scratchpad clobber q.txt; prefix per agent
- finding_never_infer_a_documents_subject_from_token_presence — name-in-body is not about; reports all FRESH, goes quiet forever
- finding_gh_run_watch_exit_status_unreliable — gh run watch --exit-status can lie; confirm via gh run view --json conclusion
- finding_injection_claim_is_openclaw_vestige — verify a file is actually boot-loaded before calling it load-bearing
- finding_fdic_securities_filings_api — FDIC securities-filings JSON API (securitiesfilings.fdicconnect.fdic.gov) gives
- finding_tic_cslt_country_transactions — country TIC net transactions moved to CSLT JSON; S-forms frozen, mfh.txt is dead
- finding_pandas_column_method_collision — pandas columns named like DataFrame methods return the METHOD via dot-access
- finding_expiry_dated_suppression_register — every suppression row carries a MANDATORY expiry, so none outlives its check
- finding_composite_least_reliable_at_extreme_amplitude — a composite is least reliable at the amplitude that makes you want to cite it: e
- reference_bright_data_web_unlocker — free-tier bot-wall bypass; WALTER-only; key per-machine; budget API 403s

## Demotion waves 2026-08-12 to 2026-08-21 — MOVED to `memory/auto/INDEX_COLD_2026-08-waves.md` (shard 2026-11-07)
- Moved verbatim, 169 rows, crc32 1501470166; every slug stays indexed through the `INDEX_COLD*.md` glob. "Every demotion wave" in this header now means this file plus that closed shard; the append-at-END rule applies to this file.

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

## Demoted 2026-09-11 EVE (PROME flow pass at WALTER's 75% flag — 19,284 B = 75% of the boot-load cap, the 8/12 trip line; WALTER's two new rows tonight contributed and it flagged rather than compacting, per the 7/28 ruling. Predictable-trigger lanes: commit-moment git rows · prediction re-pricing · cross-entity comparison · source-evaluation · artifact republish. Hooks cut to the ≤80-char canon AS THEY MOVE (8/23). ZERO deletions; memory FILES unchanged; rollback = move a row back to MEMORY.md.)
- finding_path_scoped_git_log_measures_inbound_traffic — `git log -- AGENTS/X/` is inbound mail, not a heartbeat; match the SUBJECT (n=4)
- finding_pathspec_commit_race_safety — a scoped add does NOT bound a pathspec-less commit; it sweeps the whole index
- finding_confidence_walk_is_selected_for_on_the_rows_that_carry_the_most_brier_weight — re-priced rows ARE the heavy-Brier rows (n=2)
- finding_rank_is_a_property_of_a_sovereign_window_pair — a rank is a (sovereign, WINDOW) pair; 4/4→1/4 inverted on 8 shared days
- finding_cross_entity_comparison_needs_same_perimeter — also test the stock-vs-flow twin
- finding_apparent_confabulation_is_often_a_baseline_mismatch — check the baseline before crying fake
- finding_derived_metric_across_vintages_biases_toward_stale_leg — a correction delta is a BASIS CHANGE, not a trigger
- finding_self_attack_defends_the_argument_not_the_apparatus — your attack list is blind to the APPARATUS; carry one
- finding_re_derivation_surfaces_concept_failure
- finding_divergence_requires_fresh_likeforlike_baseline
- finding_fail_loud_on_incomplete_data
- finding_fused_true_facts_false_premise
- finding_visibility_is_layered_not_binary — "is it reported?" decomposes into independent gates
- finding_market_ignoring_is_not_market_refuting — price refutes a TIMING claim, never a MECHANISM one
- finding_confounds_align_with_the_prior_you_brought — every confound pointing one way is about your SEARCH
- finding_artifact_republish_from_a_new_session_requires_reading_the_live_version_in_chunks — read live in ≤48 KB chunks, never `force`

## Promoted BACK to HOT — 2026-09-11 EVE (PROME, same evening as that day's demotion pass — recorded so the flow rule is visibly two-way, not a one-way drain). The **data-wall / access finding** (now live in `MEMORY.md` § Rail & scope discipline; slug token intentionally not repeated here — see the ⚠️ below) was demoted in the 19:0x flow pass as a predictable source-evaluation trigger. Its n+1 limb (FALCON, six identical re-pull negatives over six weeks escalated as a DATA problem when the third was already an ACCESS problem) fires mid-research on the Nth failed attempt, which is the definition of unpredictable — and it had just cost six weeks of a live pricing leg. Promotion executed, not deferred to the next pass. ⚠️ *(2026-09-20 flow pass, PROME: the exact slug token was removed from this provenance note because `memory_index_check` counted it as a false DOUBLE-LISTING against the live HOT row (SAM flag, 9/20). The history stands; the row lives HOT.)*

## Demoted 2026-09-17 — flow pass (PROME closeout; hot 19,233 B / 75.1% → under 70%; the +250 B that crossed the line were BOND's two promotion rows at `acd6a2167`, so this pass is chargeable to 2026-09-17, not drift; settled/predictable-trigger rows, hooks trimmed to ≤80 chars on the move, ZERO slugs deleted)
- finding_a_pinned_reproduction_cannot_confirm_a_cure — replay fixtures, never the pinned script
- finding_regression_test_pinned_to_a_live_surface_rots_on_the_next_edit — freeze the fixture
- finding_a_hash_pin_authenticates_the_reference_not_your_agreement_with_it — WHICH doc, not agreement
- finding_measure_actionable_not_gross_rate — actionable rate, never gross
- finding_ledger_drift_behind_narrative — STATUS canonical; ledgers rot silently (root rule)
- finding_normalization_choice_picks_opposite_winners — the disagreement IS the finding
- finding_silent_blank_evades_review — count blanks stratified
- finding_spread_metric_blind_to_common_mode — component LEVELS beside any gap/ratio
- finding_disambiguation_costs_bytes_so_a_capped_surface_cannot_absorb_every_flag — flags + cap = ONE budget
- finding_liveness_gate_keyed_on_an_artifact_that_must_exist_first — sequence inert→pin→commit
- finding_a_true_measurement_carried_to_an_overstated_reason — prefer the weakest reason that settles it
- finding_a_mature_surface_at_cap_has_no_padding_relocate_before_pruning — at a cap, no fat: RELOCATE after grepping for a home [n=2]

## Authored COLD — rows written cold at creation (NOT demoted; no wave, no rollback target in MEMORY.md)
*New memories whose trigger is a PREDICTABLE MOMENT go straight here per `MEMORY.md`'s append rule, rather than entering hot and being demoted later. Recorded as its own section so a dated demotion wave is never mistaken for the origin of a row it never held.*

- finding_the_artifact_built_to_prevent_bias_is_the_one_nobody_audits — re-derive a frozen prep file's numbers; its errors point your way [SAM 2026-09-19]
- finding_a_convention_tie_broken_toward_the_forecast_manufactures_calibration — ambiguous terms: never break the tie with your own forecast [SAM 2026-09-19]
- finding_write_timestamps_from_the_clock_not_the_narrative — `date` before EVERY stamp; drift grows with session length, runs both ways [demoted from HOT 2026-09-19, prome-92 flow pass]
- finding_imperfect_level_to_the_right_owner_beats_a_perfect_one_to_nobody — half a dispatch's value is the OWNER RE-READING ITS OWN FILE; don't withhold [demoted from HOT 2026-09-19, prome-92 flow pass]
- finding_ambiguous_coordinator_instruction_mints_a_propagating_event — a relayed deadline read as an EVENT spreads; agreement is not verification [demoted from HOT 2026-09-19, prome-92 flow pass]
- finding_a_ruling_governs_the_next_write_not_the_existing_state — a ruling touches nothing already on disk; pair it with a retroactive sweep [demoted from HOT 2026-09-19, prome-92 flow pass]
- finding_a_registry_reclassification_is_an_interface_consumers_guard_one_way — retiring/re-classing a desk is an INTERFACE — audit consumers BOTH ways [demoted from HOT 2026-09-19, prome-92 flow pass]
- finding_remote_control_rows_are_own_subagents_under_aliases — Remote Control rows on this host = your OWN subagents; count Teammates first [demoted from HOT 2026-09-19, prome-92 flow pass]
- finding_grep_respects_gitignore_so_ignored_zones_are_invisible — root sweeps silently skip ignored paths — a zero there is not an absence [demoted from HOT 2026-09-19, prome-92 flow pass]
- finding_flat_pdf_parse_returns_a_perfectly_counted_wrong_alignment — flat multi-page PDF extract: counts match, alignment WRONG — check a KNOWN row [demoted from HOT 2026-09-19, prome-92 flow pass]

### Demoted 2026-09-24 (PROME flow pass at the prome-1f closeout — hot index hit 75%; predictable-trigger rows; ZERO slugs deleted)
- finding_the_calendar_tracks_events_and_never_asks_if_the_market_is_open — a docket of RELEASES has no row for the market being SHUT
- finding_term_hit_absence_check_needs_a_pre_event_baseline — boilerplate hits every time; baseline the term pre-event
- finding_a_file_that_examples_its_own_structure_is_ambiguous — a template quoting its own headings: anchored edits write INTO the example
- finding_anchor_splice_deletes_everything_between_nested_anchors — rotation success and failure look identical; census the union (n=3)
- finding_a_read_only_agent_is_the_one_you_assume_has_nothing_to_lose — a read-only spawn writes nothing, so its loss is invisible; ask it anyway
- finding_a_rescue_instruction_ages_faster_than_the_finding — escalating guarantees concurrent work; the fix rots before the diagnosis
- finding_route_by_decay_rate_not_by_confidence — sort by DECAY RATE not confidence; a stated caveat makes fast routing safe
- finding_declared_data_wall_needs_fleet_memory_check — at 3 identical negatives the finding is ACCESS, not data
- finding_an_exit_legs_justification_expires_unwatched — nothing owns the RATIO between a row's two legs
- finding_a_scope_rule_allocates_visibility_not_superior_judgement — a scope rule names who can SEE the population, never who judges better
- finding_an_amendment_read_for_one_item_leaves_the_others_derived_from_the_original_live — a SELF-authored refutation has no trigger at all (n=3)
- reference_bank_loan_sale_and_lien_record_sources — FDIC JV bid summaries (leverage column) + Fairfax CPAN lien records
- feedback_will_sells_or_rolls_before_expiry — 9/30 sell-or-roll card rail WITHDRAWN 11/12; he manages his own expiries

### Demoted 2026-09-30 (PROME flow pass at the prome-2a boot — hot index at 75%; settled rows: no extension since 9/7 or earlier, no daily-note cite since 9/16; ZERO slugs deleted)
- finding_verify_reader_before_source — "tool is broken" may be a READER bug; verify the reader first
- finding_read_the_artifacts_own_header_first — read the artifact's own header before asserting a defect in it
- finding_scope_negative_needs_the_counterparty_standard — "it's noise/absent" stops the search; give it one-check rigor first
- finding_claim_outlives_its_discredited_instrument — instrument fails ≠ claim false; re-test before retracting
- finding_level_without_a_reference_has_two_failure_modes — saying nothing is a gap; attaching an adjective is a wrong finding
- finding_verified_figures_do_not_verify_the_shape_claim — name the denominator AND beat the noise before any shape word
- finding_impeachment_must_be_scoped_to_the_claim_not_the_source — invalidate per USE — level, delta, parse — not per source (n=2)
- finding_composition_mask_unmask_discriminator — grade the un-maskable sub-signal, not the managed headline
- finding_plausible_stale_value_evades_review — audit dashboards by AGE
- finding_loadbearing_number_must_be_reproducible — the ship-gate for a count is re-running its recipe
- finding_partial_record_written_as_final_never_heals — one partial row is permanent; audit by DISPERSION
- finding_delivery_check_is_not_a_knowledge_check — "did it arrive?" ≠ "do they know?"; grep the owner's KB
- finding_inherited_defect_propagates_though_both_ends_act_correctly — consumer is RIGHT not to re-derive; the defect propagates anyway
- finding_guard_pointed_at_another_desks_surface_inherits_its_workflow — HISTORY ⇒ read the diff; LIVE-STATE ⇒ glob by commit time (n=3)
- finding_owner_of_record_means_authoritative_not_correct — tie-break destroys the correct copy; redaction hides a falsifier
- finding_live_claim_in_a_closed_container_is_invisible — container status wins BOTH ways; CLOSED under Live manufactures work
- finding_ask_which_surface_the_reader_travels_not_where_the_fact_belongs — which surface does the reader consult? (n=6, 5 desks, 9/2)
- finding_correction_to_the_sequence_survives_every_fact_check — facts re-verify clean while the ORDER inverts the call

## Demoted 2026-10-15 — flow-rule pass (hot 19,339 B = 75% → under 70%; PROME prome-81 closeout; settled/predictable-trigger rows; hooks trimmed to ≤80 chars on the move; slug union proven in the commit body)
- finding_rederived_signal_loses_the_senders_caveats — caveats don't survive a hop; carry the sender's wording
- finding_retired_figure_relabelled_onto_another_subject_evades_its_guard — DO-NOT lists key on SUBJECT; same subject, prior event (n=2)
- finding_a_run_and_a_count_are_different_statistics — a RUN and a COUNT differ; write BOTH off official series
- finding_one_percentile_rule_is_several_rules_across_strata — a percentile is a SHAPE claim; measure the bite per stratum
- finding_a_summary_statistic_manufactures_a_verdict_when_the_threshold_is_inside_the_distribution — a mean LOOKS correct when the threshold sits inside the distribution
- finding_verify_recommended_fix_not_just_finding — verify the recommended FIX, not only the finding
- finding_prose_claims_escape_test_rigor — prose claims escape the rigor tests apply to numbers
- finding_a_column_that_is_both_record_and_instrument_basis_fails_twice — record AND instrument-basis column fails twice; the 2nd is silent
- finding_a_warning_dated_on_its_own_event_fires_too_late — a review_by set TO its own event fires one tick too late
- finding_bracket_test_cannot_parse_base_prefix — `[ 10#..-ge ]` is always false; use (( )) (n=2)
- finding_grading_a_disposition_on_a_book_you_do_not_own — the tape says WORTH, never whether it was HELD (n=2)
- feedback_research_sessions_living_page_plain_updates — one living page + plain milestone updates, not every delivery
- finding_lenient_parser_reports_unparseable_as_a_behavior — headline count == unparseable cells ⇒ parseability, not behavior
- finding_truncation_returns_a_plausible_answer_not_an_error — the cut end of an append-only log is its NEWEST rows
- finding_rebase_continue_blames_conflicts_for_a_foreign_dirty_file — continue refuses on ANY dirty tracked file; abort wipes it
- finding_marker_word_in_prose_disables_the_scanner_that_reads_for_it — prose MENTIONING a marker reclassifies the file; monitoring dies silently
- project_research_intake_collection_lane — WATCH_FOR matcher: ≤3-char words dropped, substring, ALL-CAPS = required entity
- finding_crashed_session_state_lives_in_its_transcript — clean tree after a crash hides context losses; transcript jsonl = third source
- finding_missing_output_is_not_a_dead_agent — no output file ≠ dead agent; stop it or use a NEW path before relaunching
- finding_crash_residue_over_claims_toward_completion — crash residue reads as FINISHED, to a scanner too; the owner commits it (n=2)
- finding_frozen_spec_and_the_surfaces_describing_it_drift_apart — the LETTER can't drift; its describing surfaces do; read the letter (n=5)
- finding_float_precision_empties_the_tie_set_and_voids_the_operator — float ×100 empties the tie set; exact-boundary rows mis-grade BOTH ways (n=4)
- finding_a_spread_needs_a_basis_neutral_to_what_its_legs_do_not_share — same basis on unlike legs IS the bias; one leg's dividend flips the spread
- finding_a_named_unchecked_fallback_makes_an_absence_closable — name the unchecked doc; CHECK a declared-empty cell; NEGATIVE result = a fence
- finding_rereading_a_rows_conditions_without_its_verdict_cell_regrades_a_dead_card — read the REC/verdict cell before re-grading a row; a kill is a WINDOW property
- finding_a_verbatim_cell_without_its_column_header_reads_as_the_wrong_claim — verbatim is (header + cell); a loss cell under one label read as a payoff
