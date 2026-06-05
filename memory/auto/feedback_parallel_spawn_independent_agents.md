---
name: Parallel-spawn independent sub-agents
description: When spawning multiple sub-agents whose work doesn't depend on each other, always send them as multiple Agent calls in a single message — never sequentially
type: feedback
originSessionId: 479e931e-b0d3-49e5-9dfe-7ab14098633f
---
When spawning multiple sub-agents (CARL sub-agents like POLLY/POP/GIG/PHAN, or cross-agent spawns) whose work is independent — they don't read each other's output, they just update their own files — always batch them into a single message with multiple Agent tool calls. Never spawn them one after another.

**Why:** Sequential spawning wastes elapsed time linearly. On 2026-04-17 CARL PM#3 I spawned POLLY, waited for it to return (~8 min), then spawned POP (~12 min) — ~20 min total when parallel would have been ~12 min. Will noticed and flagged. Small sessions hide this cost; multi-sub-agent sessions (typical CARL pattern) multiply it.

**How to apply:**
- Before dispatching Agent calls, check: do any of these spawns need to read another spawn's output?
- If no → single message, multiple Agent tool calls, parallel execution
- If yes → sequential is correct (rare — usually only when CARL itself synthesizes between rounds)
- Applies to ALL sub-agent spawns, not just CARL: REGINALD's BULSTE/NBSS/PE, SAM's sub-agents, verification spawns alongside refresh spawns.
- This is a baseline rule in the system prompt ("When you launch multiple agents for independent work, send them in a single message"). Don't need Will to remind me again.
