---
name: named-spawn-teams-mode
description: "Naming an Agent spawn via the `name` parameter triggers team-mode (mailbox-based, async, requires SendMessage to direct). Wrong tool for one-shot domain analytical work — use named spawns only for iterative coordination tasks."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: dfa2a11b-572d-41ae-90a2-9fb90c7415f3
---

Spawning a subagent with the Agent tool's `name` parameter puts the agent into **team-mode**: it sits idle in a mailbox after spawn waiting for SendMessage instructions, rather than executing the prompt synchronously. Discovered 2026-05-18 when spawning fleet-scanner v2 with `name: "fleet-scanner"` — the Agent call returned "Spawned successfully... will receive instructions via mailbox" rather than the synchronous-completion pattern of an unnamed spawn (v1 returned synchronously with full results). Required a follow-up SendMessage to actually execute the spawn prompt.

**Why:** *Named spawns are designed for iterative coordination (multi-turn refinement via SendMessage, like the memory-audit-001 teams test where curator + critic + reconciler exchanged messages). For bounded one-shot work — domain analysis, revival proxies, refactor passes, single-pass audits — the async + mailbox pattern adds overhead without benefit. The agent's initial prompt is treated as orientation, not instruction. Naming is the trigger for the entire teams primitive.*

**How to apply:**

1. **One-shot synchronous work** (domain proxies, fleet scans, revival packets, audits, single-question research): **omit the `name` parameter**. The Agent tool runs synchronously and returns the agent's full output in one call.

2. **Iterative coordination** (multi-turn refinement, adversarial pairs, team-based curation): **use `name`** to make the agent addressable via SendMessage. Expect to send a follow-up instruction message after spawn — the initial prompt won't execute on its own.

3. **If unsure:** default to **unnamed (synchronous)**. Easier to escalate to named if iteration emerges (re-spawn with name) than to recover from accidental teams-mode parking (the idle agent sits doing nothing until SendMessage).

4. **Avoid:** spawning a named agent and assuming the initial prompt will execute. You'll get an `idle_notification` and the work won't have happened.

5. **If you DO use named-spawn teams mode:** the initial prompt should be onboarding/context ("you are X, you do Y"), and the first SendMessage should be the actual work instruction ("now do this specific task"). Don't try to do both in the spawn prompt.

6. **Continuation via SendMessage, NOT respawn.** A named-spawned agent is persistent for the session — addressable via SendMessage to resume from transcript in background. Do NOT call Agent again to "respawn" them. Three validations 5/21: HENRY (`abf1cd8d4ed725569`), VIOLET (`ad7350e8d26f70249`), BOND (`ad32628b028661b70`) — all stayed addressable for multi-hour sessions across multiple SendMessage exchanges.

7. **Name handle drops after first turn — UUID is the persistent address.** Spawning with `name: "bond"` works on the first turn but SendMessage to `to: "bond"` returns "No agent named 'bond' is currently addressable. Use the agent ID." The UUID returned with the first Agent response is the only addressable handle afterward. Save UUIDs immediately when spawning multiple named agents.

**Cross-references:** [[revival-proxy-pattern]] explicitly requires unnamed-spawn · [[adversarial-brief-for-pair-teams]] explicitly requires named-spawn teams mode (the right tool for that pattern)
