---
name: idle-notification-is-not-a-result
description: "A spawned agent going idle is NOT a report — chase the deliverable before concluding it found nothing. 4-for-4 agents in one fan-out idled without delivering and 3 had completed work behind the silence. Make delivery the explicit FINAL ACTION in the spawn prompt (write to disk AND message), tell chased agents that 'I did not complete it' is unpenalised, ask for the DIAGNOSTIC before the research, and check DISK before re-spawning."
metadata:
  node_type: memory
  type: finding
---

2026-07-24/25, WALTER's 4-axis FHA/VA stress-test. **Every one of the four spawned agents went idle without delivering its report.** Three of the four had completed substantial, fully-sourced research. Had the first idle notification been read as "this agent found nothing," a study that falsified a live BOARD signal's load-bearing evidence and saved a domain agent's watch from erroneous closure would have been scored a failed run.

**What worked, in order:**

1. **Chase each one explicitly, and say that not-finishing is acceptable.** Every chase message stated that *"I did not complete it"* was a fine answer and would not be treated as failure. This is the load-bearing sentence: without it, a chased agent has an incentive to reconstruct plausible-sounding figures it never sourced. On a study whose entire purpose is auditing whether a number is trustworthy, fabricated corroboration is strictly worse than no result.
2. **Ask for the DIAGNOSTIC before the research.** *"Did ToolSearch return the tools? Were they callable? How many searches ran? What blocked you?"* One agent's diagnostic explained the whole run (see `[[finding_webfetch_pdf_saves_despite_parse_error]]`) and was worth more than its findings.
3. **Check DISK before re-spawning.** The one agent that genuinely produced nothing had nothing on disk either — that check is what distinguished a real non-completion (justifying a re-spawn) from a merely-undelivered result (where re-spawning duplicates work). This is the mirror image of `[[finding_terminated_notice_can_precede_delivery]]`, where absence was wrongly *asserted* from a disk check that ran too early.
4. **Stop the replacement when the original delivers.** Send an explicit stand-down; otherwise two agents work the same axis at cost.

**How to apply — put it in the spawn prompt.** Delivery must be stated as the **explicit final action**: *write the report to `<path>` **AND** SendMessage it, before going idle.* An undelivered result does not exist. This is a restatement of the fleet's own "deliver your result as your final action before going idle" rule — which exists precisely because this failure recurs, and which spawned agents evidently do not inherit.

Related: [[finding_terminated_notice_can_precede_delivery]] · [[feedback_subagent_prompt_discipline]] · [[finding_two_phase_spawn_grader_contract]] · [[finding_scheduled_print_spawn_armed_state_report]] · [[feedback_subagent_propagation_gap]]
