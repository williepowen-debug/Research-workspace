---
name: finding-subagent-memory-split
description: "Sub-agent specs should split into <NAME>.md (durable mandate/rubric) + <NAME>_MEMORY.md (dated state — RUN LOG, PENDING, STANDING MONITORS, CALIBRATION, NEXT RUN HINTS); without the MEMORY half, fresh spawns can't self-orient and parent agent must re-brief every spawn"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 4a4ae2ba-2aed-4387-8600-af85958b229c
---

Sub-agents spawned fresh each session need a parallel MEMORY file to carry state across spawns. Without it, pending escalations, standing monitors, and calibration patterns either (a) live only in commit messages where the next spawn can't read them, or (b) must be re-briefed by the parent agent in the spawn prompt every time — which doesn't scale.

**Pattern (validated 2026-06-01 on SAM's KURA + KOYOMI):**

```
<NAME>.md          — durable spec (mandate, autonomy, rubric, run sequence)
<NAME>_MEMORY.md   — dated state, structured as:
                       ## CHANGES SINCE LAST RUN  (auto-populated at run start)
                       ## LAST RUN                (append each run)
                       ## PENDING                 (escalations parent hasn't yet resolved)
                       ## STANDING MONITORS       (open items to keep surfacing)
                       ## CALIBRATION             (parent's view of approve/reject patterns)
                       ## NEXT RUN HINTS          (what to look at next)
```

**Ownership split (load-bearing):**
- Sub-agent writes most sections (CHANGES, LAST RUN, PENDING-adds, STANDING MONITORS, NEXT RUN HINTS).
- Parent agent writes CALIBRATION (sub-agent can't grade its own approve/reject rate from inside its own run) and clears PENDING items as resolved.
- Sub-agent's spec read-set adds MEMORY at position 1 (right after spec itself).
- Sub-agent's canonical spawn invocation references both files.

**Why:**
- Mirrors successful CLAUDE.md + MEMORY.md split at agent level.
- Spec stays durable; state is dated. Don't mix the two — palimpsest decay risks "is this rule or state?" confusion otherwise.
- Standing monitors persist organically across runs without parent re-briefing.
- Calibration grows over multiple runs — after N runs, sub-agent's proposed-output matches parent's tastes better.

**When to apply:**
- Sub-agent spawned multiple times across sessions (not a one-shot).
- Sub-agent produces output the parent reviews/adjudicates (KURA proposes KB rows → SAM approves; KOYOMI proposes docket edits → directly writes but reports escalations).
- Sub-agent has standing monitors, pending items, or calibration that should persist.

**When NOT to apply:**
- One-shot research agents (no cross-session state).
- Pure execution agents whose output is the work product itself (no review loop).
- Sub-agents whose entire context fits in one spawn prompt without state baggage.

**Don't add per-sub-agent CHANGELOG.** Parent's MAINTENANCE.md is the canonical audit trail for structural changes to specs themselves — splitting that across N CHANGELOG files fragments provenance. CHANGELOG is for the *spec itself* evolving; MEMORY is for *state under the spec*.

Validated on KURA (workbook librarian, returns proposals + flags) and KOYOMI (docket steward, writes directly + reports escalations). Transferable to other agents (BRENT, BROCK, etc.) if they grow sub-agents with the same review-loop pattern.
