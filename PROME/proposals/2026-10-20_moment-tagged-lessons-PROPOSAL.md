# PROPOSAL — moment-tagged lessons (a "Verses line" for memories)

**Status:** PROPOSAL, nothing built. Drafted 2026-10-20 22:0x ET by PROME (session b94e8a3e) on Will's ask after a side question, a Red Alert 2-style `rules.ini` warhead `Verses=` line. Run it as a **light experiment** (`feedback_experiments_run_light_not_fleet_process`): fast to a working thing, no fleet process.

## The idea in one paragraph
The game file scores every warhead against ONE fixed list of armor types, with a strength per type. Applied here, every lesson (auto-memory file) is scored against ONE fixed list of **moments**: the points in a session where mistakes actually happen. Each moment gets a strength of H/M/L, and at that moment the tool already running prints the top lessons for it.

**Why moments, not topics:** encoding specificity (Tulving and Thomson). A cue only retrieves a memory if the cue was part of how it was stored. Today's case: the lesson "check the target, not the record" exists (`finding_record_of_an_action_is_not_the_action`, n=19) and still did not fire when PROME twice stated push state without fetching (10/20, ~13:00 and 16:5x ET). It is filed under a topic, and the moment that needed it was "reporting status".

**What already exists:** faceted classification (Ranganathan), agent-memory scoring (recency + importance + relevance, Park et al. 2023), and phase-of-flight checklists. None of them scores lessons against a fixed list of moments. The lessons-learned literature also shows that passive stores go unused, while pushing lessons at the moment of use works. Sources are listed in the 10/20 conversation summary in `memory/2026-10-20.md`.

## The moment vocabulary (10, fixed; named keys, never positional)
| Key | The moment |
|---|---|
| `status-report` | Stating what is committed / pushed / verified / done, incl. closeout and boot reports |
| `relay` | Passing on a desk's, peer's or reviewer's claim, figure or ruling |
| `number-in-brief` | Writing a price, level, date or figure into a message for Will |
| `record-edit` | Editing a ledger or canon/state doc (DOCKET, GATES, WILL_QUEUE, STATUS, charters, TSVs) |
| `check-change` | Building or repairing a check, gate, guard, script or test |
| `commit` | Staging, committing, shell heredocs, message files |
| `stamp` | Writing a time or date stamp |
| `trade-card` | Anything touching a held position, a card, an expiry or a fill |
| `packet-spawn` | Writing a packet, launching a desk, or asking one to close out |
| `boot` | Reading state at session start |

Levels: **H** = must surface at this moment · **M** = surface if room · **L** = omit (default; not written).

## The first 20 lessons, tagged
| # | Lesson (auto-memory slug) | Moments |
|---|---|---|
| 1 | finding_record_of_an_action_is_not_the_action | status-report=H · relay=H · record-edit=M |
| 2 | finding_a_stamp_written_from_narrative_drifts_from_the_wall_clock | stamp=H |
| 3 | finding_heredoc_terminator_ends_the_and_chain | commit=H |
| 4 | finding_unquoted_heredoc_expands_dollar_figures | commit=H · number-in-brief=M |
| 5 | finding_crlf_textmode_tsv_flip | record-edit=H |
| 6 | finding_a_correction_pass_is_unreviewed_work | check-change=H · record-edit=M · status-report=M |
| 7 | finding_test_the_guard_not_just_the_guarded | check-change=H |
| 8 | finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction | check-change=H |
| 9 | finding_instrument_reports_clean_against_the_wrong_reference | check-change=H · boot=M |
| 10 | finding_asymmetric_rigor_counterparty_claims | relay=H |
| 11 | finding_attribution_authenticates_a_figure_its_named_source_never_produced | number-in-brief=H · relay=H |
| 12 | finding_exact_level_authenticates_a_wrong_direction | number-in-brief=H · relay=M |
| 13 | finding_two_legs_with_independent_vintage_clocks_mix_dates_invisibly | number-in-brief=H |
| 14 | finding_a_daily_bar_read_after_the_evening_open_belongs_to_the_next_session | number-in-brief=H · trade-card=M |
| 15 | finding_guard_scope_expires_at_the_fill | trade-card=H |
| 16 | feedback_will_sells_or_rolls_before_expiry (incl. 10/20 no-nag) | trade-card=H · number-in-brief=M |
| 17 | finding_prome_inbox_is_repo_root_not_under_agents | packet-spawn=H |
| 18 | finding_closed_out_teammate_does_not_resume_on_reping | packet-spawn=H |
| 19 | finding_correction_beside_an_instruction_leaves_two_live_instructions | record-edit=H |
| 20 | feedback_skipped_control_is_reported_as_skipped | status-report=H |

Coverage check: every moment has at least one H. `boot` has only an M, which is deliberate: boot is already the most-instrumented moment.

## How it would work
1. **Tag:** one frontmatter line per memory file, `moments: status-report=H relay=H record-edit=M`. Edit the 20 files only; the index rows stay as they are.
2. **Lookup:** a ~40-line script, `scripts/moment_lessons.py <moment>`, prints the top 3 for that moment (H first, then by citation count `n=`), one line each: slug + its ≤80-char hook.
3. **Push (phase 2, only if phase 1 earns it):** the tools already running at those moments print the lookup themselves:
   - `commit_check.py`: `commit`
   - `safe-push.sh` and the closeout gate: `status-report`
   - the boot gate: `boot`

   The lessons-learned research says this push step is what makes the difference.

## Experiment and success test
- **Phase 1 (one session, about an hour):** tag the 20 files, write the script, and call it by hand at each moment for a week.
- **Measure at one week:** did a tagged lesson's mistake recur at its H moment? Today's baseline is 2 push-status misstatements in one session. Did the printed top 3 contain the lesson that was actually needed? Record yes or no per use.
- **Kill it if** the printouts are ignored or mostly irrelevant after a week. That would show it adds noise rather than recall.
- **Keep it if** it catches at least one would-be repeat. Then do phase 2 (wire 2 tools).

## What this is NOT
- No new canon and no fleet rule. No change to other desks.
- No percentages: H/M/L only, because judgment calls do not support false precision.
- Not a replacement for the existing topic index. Moments are a second axis on the same files.

## Decisions for Will
1. Approve phase 1 as a light experiment (next session, counted as one process change).
2. Adjust the 10 moments or the 20 picks if any look wrong to you.
