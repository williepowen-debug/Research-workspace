---
name: path-b-trim-pattern
description: "When a state file has bloated past its design-doc-prescribed shape, read SYSTEM/BOOT for the file's design role, audit current vs role, trim everything that duplicates other owner files, refresh remaining sections to live state"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 93c60a77-e8e4-4422-945e-267bc5b8b93d
---

Recipe for trimming bloated state files back to design-doc-prescribed shape without losing load-bearing content. Applied to HEARTBEAT.md 5/21 (98 → 38 lines).

**Why:** *State files drift toward append-only over time. Each session adds context, nothing prunes. Eventually the file is doing 2-3 jobs (current-state pointer + historical log + duplicate of other owner files). The cure isn't "rewrite from scratch" (loses load-bearing content) or "trim by feel" (asymmetric: drops things future-me will need). The cure is "trim against the design-doc-prescribed role" — SYSTEM.md and BOOT.md already spell out what each file owns vs. doesn't.*

**How to apply:**

1. **Read SYSTEM.md and BOOT.md** for the file's design role. Find the row in the Doc Ownership table.
2. **Identify duplicate content** — anything that belongs in another owner file's scope (per the same table).
3. **Audit current vs role:** list every section in the current file; tag each as `keep` (matches role) / `cut` (duplicates other owner) / `refresh` (matches role but stale).
4. **Cut duplicates first** (lowest-risk; other owner file is authoritative anyway).
5. **Refresh the keep+refresh sections** to live state in one pass.
6. **Show diff to Will before commit** — cross-surface boundary if the file is shared (HEARTBEAT, MEMORY).
7. **Document the trim** in the closeout entry: lines before/after, what was cut, what was kept.

**When to use:**
- State file is >2× its typical size
- File contains multiple sections that belong elsewhere per Doc Ownership
- File hasn't been refreshed in N sessions and feels like a museum

**When NOT to use:**
- File is on the do-not-touch list (other agent's domain)
- Design role itself is ambiguous (fix SYSTEM.md first)
- Will hasn't approved the cross-surface boundary cross (HEARTBEAT, root MEMORY)

**Validated:** HEARTBEAT.md 5/21 (98 → 38 lines, commit `8f3fa922`). Cut: multi-day Key Updates blocks (duplicates SCRATCH/STATUS/memory), Active Spawns (ephemeral), Operating Notes (SYSTEM/BOOT own that). Kept + refreshed: Regime, Stress dashboard, Thresholds, Blocking-on-Will.

**Transferable targets:** any owner-file in the BOOT.md Doc Ownership table that has drifted from its row's "Owns / Does NOT contain" cells. Likely candidates: TODAY.md (often duplicates STATUS), STATUS.md (often duplicates SCRATCH narrative), HANDOFF.md (often duplicates CLAUDE_CODE_HANDOFF).

**Related:**
- [[finding_walter_refactor_pattern]] — same family; agent-STATUS-specific
- [[feedback_check_existing_design_docs]] — read the design doc before writing/restructuring
