---
name: finding-governance-doc-stale-default-drift
description: "Shared governance docs (root CLAUDE.md) accumulate stale defaults that the fleet quietly papers over via per-agent local docs + auto-memory overrides; memory overriding the source-of-truth doc is fragile drift — reconcile the doc itself, and sweep the whole section, not one line"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 141e10be-bcd0-4cf8-874e-178bfa137697
---

**Observed twice in one day, 2026-06-08.** Root `CLAUDE.md` Git Protocol carried two stale defaults that the fleet had silently routed around:
1. `git reset HEAD` in "Before committing" — 4 agents (SAM/BRENT/REGINALD/BROCK) had each independently moved to pathspec in their *own* CLAUDE.md, with BROCK explicitly documenting "deviates from root — alignment pending."
2. "commit + push at session end" (in *two* spots — intro line + the At-session-end steps) — contradicted the standing **commit-local/defer-push** rule, working only because `[[feedback_defer_push_coordinate]]` auto-loads every boot and overrides it. This was the systemic cause of premature fleet pushes; CARL+BRENT co-diagnosed it on the desktop the same day.

**The pattern:** a shared source-of-truth doc has a default that's wrong under current practice; agents can't edit the shared doc (own-dir rule) so they override locally + via memory; the doc-vs-fleet gap reads as silent drift, and the memory-override is brittle (a new agent, a harness change, or an auto-memory miss flips the default back).

**How to apply:**
- **Memory/local-doc overriding a source-of-truth doc = a flag to fix the doc, not a stable state.** When ≥2 agents document "deviates from root," reconcile root.
- **PROME owns the shared-doc reconcile** (agents flag, PROME edits with Will approval) — and root edits must funnel through ONE clone to avoid two machines producing divergent roots.
- **Sweep the whole section, not the flagged line** — "push at session end" lived in 2 spots; surface-fixing one leaves the contradiction (cf. [[finding_verification_correction_downstream_propagation]]).
- **Re-point the now-stale overrides** afterward (the "overrides root doc" / "deviates from root" notes go false once the doc is fixed). Related: [[finding_pathspec_commit_race_safety]], [[feedback_defer_push_coordinate]].
