---
name: draft-only-teams-spawn
description: "Teams-mode domain-agent spawn pattern where agent is briefed to draft into proposals/ only, no live state file edits; iterative Will + Prome review via SendMessage across multiple turns before recipient adopts"
metadata: 
  node_type: memory
  type: project
  originSessionId: 93c60a77-e8e4-4422-945e-267bc5b8b93d
---

When the work product is a structural change to a domain agent's owned files (matrix, framework, KB schema), spawn the agent in teams mode with **explicit DRAFT-ONLY scope**: output goes to `AGENTS/<NAME>/proposals/` with `_prome-spawned` suffix, no edits to live STATUS / TRADE / KB / matrix files. Iterate via SendMessage over multiple turns until Will approves; agent adopts on its own boot.

**Why:** *First instance was BOND matrix v2 draft (5/20-21). Without DRAFT-ONLY framing, a teams-spawned domain agent may treat a "help me think through this" prompt as authorization to edit live files. Once live files are edited under PROME's session, the agent's next-boot integration becomes a merge/reconciliation problem instead of a clean adopt-or-reject. DRAFT-ONLY preserves agent ownership of its own state surface while still getting the domain-expert input.*

**How to apply:**

1. **Brief explicitly:** "Draft to `AGENTS/<NAME>/proposals/<TOPIC>_DRAFT_prome-spawned.md`. Do NOT edit live STATUS / TRADE / KB / matrix files. Output is a proposal for your future-self to adopt."
2. **Use `_prome-spawned` suffix and PROVENANCE preamble** (same convention as revival proxy outputs).
3. **Iterate via SendMessage**, not via file rewrites — keeps the draft single-author until adopted.
4. **Surface Prome's own framing errors openly to Will** during iteration; invite the agent to push back (see [[finding_domain_agent_steelman_backstop]]).
5. **Adoption is the agent's own commit on next boot** — Prome does not merge the draft to live files.

**When to use:**
- Matrix surgery / threshold recalibration
- KB schema changes
- Framework version bumps (V2.1 → V2.2)
- Any restructure that changes how the agent thinks vs. just adding data

**When NOT to use:**
- Quick fact-checks (just SendMessage)
- Revival of long-stale agents (use [[finding_revival_proxy_pattern]] — different pattern)
- Live tape reads (no draft involved, agent directly contributes)

**Validated:** BOND matrix v2 draft 5/20-21 (Q1/Q3 resolved with BOND pushback on Prome misframings; Q2 parked; Q4 deferred-with-conditional-rule; Q5 open). Pattern produced strictly better outcomes than Prome + Will alone.

**Related artifacts in the same family:**
- [[finding_revival_proxy_pattern]] — also writes to agent inbox with PROVENANCE; difference: revival = stale agent, DRAFT-ONLY = active agent
- [[finding_framing_precision_overlay]] — also a Prome-authored note in agent's inbox; difference: overlay = correction of agent's existing output, DRAFT-ONLY = proposal for new agent work
