# COMPLETION SPEC — Sub-Agent Report Standard

**Created:** ~2026-05 · **Updated:** 2026-08-13 (delivery method 1 RE-KEYED from overwrite-in-place `LAST_COMPLETION.md` to a DATED outbox memo — BRENT domain-review flag, PROME-lane fix: an overwritten file whose NAME promises currency is the `finding_completion_stamp_skip_reads_as_current` rot mechanism, and it duplicated live state that each agent's own SCRATCH/STATUS canonically holds [BRENT's opened by declaring that conflict]. Dated memos are what live practice already used. Existing `LAST_COMPLETION.md` files: no longer required — owners may freeze/banner their copy at their next closeout [BRENT's freeze Will-approved 8/13]; HENRY's "LAST_COMPLETION block" mixed-vintage banner pattern cited in CLOSEOUT stamp canon is a PATTERN name, unaffected) · Prior: 2026-08-09 (spine-audit #8 — header stamp ADDED per the 8/9 stamp canon [file had none while carrying a 7/31 migration]; §6 routing examples re-based to WAL's 7/25 promotion out of REGINALD)
**Purpose:** Every spawned sub-agent writes this block at the END of its work. Prome reads it to update live owner files (`PROME/STATUS.md`, `PROME/SCRATCH.md`, `PROME/ACTIVE_DECISIONS.md`, routing inboxes) without parsing the full agent output.

---

## Required: TWO delivery methods (belt and suspenders)

**1. Write to file** — a **DATED delivery memo** at `AGENTS/{your-agent-name}/outbox/{YYYY-MM-DD}_to-PROME_{slug}.md` (and, when the work answers a PROME task packet, a copy/packet to `PROME/inbox/`). Never an overwrite-in-place status file: a file whose name promises currency reads as current-and-wrong the first closeout it skips (`finding_completion_stamp_skip_reads_as_current`), and it forks live state your own SCRATCH/STATUS canonically owns. The memo ends with this block:
```
## COMPLETION — {agent name} — {date}
STATUS: ✅ DONE | ⚠️ PARTIAL | ❌ BLOCKED
CHANGED: [comma-separated list of files created/modified]
RESULT: [2-3 sentences. What was accomplished. Be specific — numbers, counts, key findings.]
GAPS: [What couldn't be done and WHY. "None" if fully complete.]
WILL_NEEDS: [Anything that requires Will's direct action. "None" if not applicable.]
FOLLOW-UP: [Next action needed. "None" if self-contained.]
```

**2. Include in task output** — same block at the end of your response so the system message carries it.

Both are required. The file is the backup; the system message is the primary channel.

---

## Rules

1. **Max 10 lines.** If you need more, you're not summarizing — you're reporting. Put the detail in the files, put the summary here.
2. **GAPS must include WHY.** "Couldn't pull transcript" is useless. "Couldn't pull transcript — not published yet, check after 9 AM ET Thu" is actionable.
3. **WILL_NEEDS is sacred.** Only things that literally require Will's hands, eyes, or judgment. Not "Will should review" — that's always true. More like "needs brokerage screenshot" or "requires login credentials" or "judgment call on position sizing."
4. **STATUS must be honest.** ⚠️ PARTIAL is not failure — it's useful information. ❌ BLOCKED means the task literally cannot proceed without intervention.
5. **RESULT must include at least one number.** Forces concreteness. "Integrated 3 signals, added 2 KB entries, updated scenario probability from 68% to 78%" beats "updated agent status with new information."

---

## Example

```
## COMPLETION — BROCK — 2026-08-16
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/BROCK/STATUS.md, AGENTS/BROCK/workbook/KB.tsv, AGENTS/BROCK/research/outputs/RP-BRK-1.3_pik_shadow_defaults.md
RESULT: Integrated BlackRock HPS gating ($26B, $1.2B redemptions) and MS 8% default projection. Gate count updated to 10. Contagion map advanced to Stage 2.5. KB entries KB-BRK-047 and KB-BRK-048 added.
GAPS: Could not verify exact BlackRock HPS 8-K filing date — SEC EDGAR search returned 403. Need to retry or Will can check manually.
WILL_NEEDS: None.
FOLLOW-UP: ARESSI data drops Wed — spawn BROCK again to integrate when available.
```

---

## How Prome Uses This

1. Read COMPLETION block from sub-agent output.
2. If WILL_NEEDS is not "None" → add the blocker to `PROME/ACTIVE_DECISIONS.md` or `PROME/STATUS.md`, then surface to Will when relevant.
3. If FOLLOW-UP is not "None" → capture the next action in the owner file (`PROME/SCRATCH.md` for immediate continuity, `PROME/STATUS.md` for work queue, or an agent inbox for routed domain work).
4. If the work produced a system/process decision, log it in the appropriate live owner file. Trade/portfolio decisions go to FORGE/TERRY + broker truth *(the legacy `PROME/TRADE_DECISIONS.md` log was archived 2026-06-30)*; non-trade architecture/state decisions go to `PROME/STATUS.md`/`PROME/HANDOFF.md` as appropriate.
5. If STATUS is ❌ BLOCKED → surface to Will immediately.
6. **Post-completion routing** — scan RESULT for cross-agent references. If agent A's output names agent B (e.g., "OTTO mapped a Western Alliance exposure chain → **WAL** should integrate" — WAL is its own agent since 2026-07-25, promoted out of REGINALD), write a routing signal to `AGENTS/{B}/inbox/` with the key finding. This is Tier 1 — no proposal needed.

   Examples:
   - OTTO maps First Brands → Barclays → Apollo → WAL → route to **WAL** inbox (WAL promoted out of REGINALD 7/25 — example re-based 8/9)
   - SAM flags independent Fed-cut JPY path → route to NEXUS inbox
   - BRENT updates NOPI estimate → route to HENRY inbox (demand destruction)
   - Any agent shifts scenario probability → route to RED inbox

   **Format:** `{YYYY-MM-DD}_from-{SOURCE}_{slug}.md` (the fleet's date-first convention — 538 live files vs 52 on the older `{SOURCE}_ROUTING_{DATE}.md` form, which stays readable but is no longer the spec; re-keyed 8/29 audit #11) — 5 lines max. Signal, source, why it matters to the recipient. Don't duplicate the full output — just the actionable fragment.

---

## Delivery-contract fleet memories (fleet-memory embeds — migrated 2026-07-31, Phase-2 restructure)
*One-liners embedded from memory/auto/ (files unchanged); index rows now in memory/auto/INDEX_COLD.md.*

- finding_two_phase_spawn_grader_contract — "For a session that must wait hours for a scheduled data release: split it into two spawns with a FROZEN MECHANICAL GRADER as the handoff contract (prep session builds grader+memo, shuts down; fresh session at release-time runs the grader). Zero context loss, no idle session, and the grader's input-refusal doubles as stale-data discipline." `[[finding_two_phase_spawn_grader_contract]]`
- finding_terminated_notice_can_precede_delivery — "A teammate_terminated notice + an empty disk check does NOT prove a spawned agent delivered nothing — its commits/message can land after the check; never assert absence in a re-spawn prompt, instruct verify-existing-first instead." `[[finding_terminated_notice_can_precede_delivery]]`
- finding_idle_notification_is_not_a_result — "A spawned agent going idle is NOT a report — chase the deliverable before concluding it found nothing. 4-for-4 agents in one fan-out idled without delivering and 3 had completed work behind the silence. Make delivery the explicit FINAL ACTION in the spawn prompt (write to disk AND message), tell chased agents that 'I did not complete it' is unpenalised, ask for the DIAGNOSTIC before the research, and check DISK before re-spawning." `[[finding_idle_notification_is_not_a_result]]`
- finding_spawned_agents_ship_artifact_skip_writeback — "Spawned agents reliably deliver the requested artifact and reliably SKIP writing back to their own STATUS — 3-for-3 in one session, including one agent that flagged its own stale surface inside the memo and then didn't fix it. A deliver-before-idle contract buys the deliverable, not the state update; put the write-back in the spawn contract and disk-verify STATUS mtime, not just the outbox." `[[finding_spawned_agents_ship_artifact_skip_writeback]]`
