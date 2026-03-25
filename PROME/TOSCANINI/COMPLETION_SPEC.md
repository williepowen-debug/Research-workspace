# COMPLETION SPEC — Sub-Agent Report Standard

**Purpose:** Every spawned sub-agent writes this block at the END of its work. Prome reads it to update QUEUE.md and DECISIONS.md without parsing the full agent output.

---

## Required Block (append to end of task output OR write to assigned file)

```
## COMPLETION
STATUS: ✅ DONE | ⚠️ PARTIAL | ❌ BLOCKED
CHANGED: [comma-separated list of files created/modified]
RESULT: [2-3 sentences. What was accomplished. Be specific — numbers, counts, key findings.]
GAPS: [What couldn't be done and WHY. "None" if fully complete.]
WILL_NEEDS: [Anything that requires Will's direct action. "None" if not applicable.]
FOLLOW-UP: [Next action needed. "None" if self-contained.]
```

---

## Rules

1. **Max 10 lines.** If you need more, you're not summarizing — you're reporting. Put the detail in the files, put the summary here.
2. **GAPS must include WHY.** "Couldn't pull transcript" is useless. "Couldn't pull transcript — not published yet, check after 9 AM ET Thu" is actionable.
3. **WILL_NEEDS is sacred.** Only things that literally require Will's hands, eyes, or judgment. Not "Will should review" — that's always true. More like "needs brokerage screenshot" or "requires login credentials" or "judgment call on position sizing."
4. **STATUS must be honest.** ⚠️ PARTIAL is not failure — it's useful information. ❌ BLOCKED means the task literally cannot proceed without intervention.

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
