# COMPLETION SPEC — Sub-Agent Report Standard

**Purpose:** Every spawned sub-agent writes this block at the END of its work. Prome reads it to update QUEUE.md and DECISIONS.md without parsing the full agent output.

---

## Required: TWO delivery methods (belt and suspenders)

**1. Write to file** — overwrite `AGENTS/{your-agent-name}/LAST_COMPLETION.md`:
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
## COMPLETION
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/BROCK/STATUS.md, AGENTS/BROCK/workbook/KB.tsv, AGENTS/BROCK/research/MS_DEFAULT_FRAMEWORK.md
RESULT: Integrated BlackRock HPS gating ($26B, $1.2B redemptions) and MS 8% default projection. Gate count updated to 10. Contagion map advanced to Stage 2.5. KB entries KB-BRK-047 and KB-BRK-048 added.
GAPS: Could not verify exact BlackRock HPS 8-K filing date — SEC EDGAR search returned 403. Need to retry or Will can check manually.
WILL_NEEDS: None.
FOLLOW-UP: ARESSI data drops Wed — spawn BROCK again to integrate when available.
```

---

## How Prome Uses This

1. Read COMPLETION block from sub-agent output
2. If WILL_NEEDS is not "None" → add to `TOSCANINI/WILL_QUEUE.md`
3. If FOLLOW-UP is not "None" → add to `TOSCANINI/QUEUE.md` as draft proposal
4. Update `TOSCANINI/DECISIONS.md` with outcome
5. If STATUS is ❌ BLOCKED → surface to Will immediately
6. **Post-completion routing** — scan RESULT for cross-agent references. If agent A's output names agent B (e.g., "OTTO mapped exposure chain → WAL → REGINALD should integrate"), write a routing signal to `AGENTS/{B}/inbox/` with the key finding. This is Tier 1 — no proposal needed.

   Examples:
   - OTTO maps First Brands → Barclays → Apollo → WAL → route to REGINALD inbox
   - SAM flags independent Fed-cut JPY path → route to NEXUS inbox
   - BRENT updates NOPI estimate → route to HENRY inbox (demand destruction)
   - Any agent shifts scenario probability → route to RED inbox

   **Format:** `{SOURCE}_ROUTING_{DATE}.md` — 5 lines max. Signal, source, why it matters to the recipient. Don't duplicate the full output — just the actionable fragment.
