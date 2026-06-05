---
name: feedback-front-load-planning
description: "For multi-step deterministic work, surface all decisions in a pre-execution planning pass; let Will batch-approve defaults; then execute mechanical with proceed-pacing at step boundaries"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6aefca3b-c324-4c82-8d52-f261b8995394
---

For multi-step deterministic work (rehabs, refactors, structural edits), front-load the planning: surface every decision the execution will encounter, propose a default for each, let Will batch-approve, then execute mechanical with one-paragraph "proceed?" checkpoints at step boundaries.

**Why:** Will told me directly on 2026-05-21 during FORGE rehab planning: "I would prefer we front load our work with planning and answering questions ahead of time." Tested same session: 23 decisions surfaced + defaulted in advance (Q1-Q23 across 5 steps); Will pre-approved en bloc with "your defaults sound good"; 4 execution steps ran in ~25 min total tool time with zero mid-execution decision escalations. Without front-loading, the same work would have hit ~3-5 mid-execution stops to ask "should I do X or Y?" — fragmenting both my context and Will's attention.

**How to apply:** When you encounter work that's (a) multi-step, (b) deterministic enough to enumerate the decisions upfront, and (c) doesn't require live-data-driven branching mid-execution, run a planning pass before any file edits:
1. Walk the execution mentally; enumerate every decision point.
2. Propose a default for each (your recommendation + reasoning).
3. Surface them all in one message, grouped by step, numbered (Q1, Q2, ...).
4. Tell Will: "anything you don't override gets the default."
5. Execute mechanical. Between steps, send a one-paragraph "delta" message ("Step N done; here's what changed; proceed?"). No mid-step decision asks.

Step-by-step proceed-pacing — Will-driven cadence with "proceed to step N" gate — works well as the execution-time companion. Together: pre-execution decisions resolved en bloc + execution-time cadence Will-driven. Avoids both batch-everything-then-review (high-risk, hard to back out) and ask-at-every-decision (high-friction, breaks flow).

Doesn't apply when: (a) the work is genuinely exploratory (decisions depend on what earlier steps reveal), (b) it's short enough (1-2 decisions) that planning overhead exceeds execution overhead, (c) Will hasn't asked for it (some sessions Will prefers conversational tinkering — read the room).

Related: [[feedback-break-multifile-updates]] (execution-time chunking), [[feedback-check-existing-design-docs]] (pre-execution sweep for prior work).
