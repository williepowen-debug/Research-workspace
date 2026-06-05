---
name: adversarial-brief-for-pair-teams
description: "When spawning adversarial-pair teams via the Agent Teams primitive, the brief must explicitly prompt both members toward genuine disagreement — otherwise pair work collapses into mutual confirmation and the second voice is wasted spend"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d7a1fb7a-828b-4ebd-88ab-39b07cb8b670
---

When using the Claude Code Agent Teams primitive to run an adversarial-pair pattern (curator vs critic, proposer vs challenger, etc.), the spawn prompts must explicitly frame both roles toward genuine disagreement. Without this framing, pair work tends to collapse into mutual confirmation and the second teammate adds no independent information over solo work.

**Why:** Validated 2026-05-18 in the first bounded teams test (memory-audit-001). Critic's brief said "default to adversarial; the existing bar is high; default verdict on weak entries: reject." Curator's brief said "engage genuinely with critic's pushback; don't agree to be agreeable, and don't dig in for sport." Result: critic's solo file rejected 6/8 candidates, curator's solo file kept 4 — and reconciliation produced two genuine flips in each direction. The headline win (substrate-in-flux rejection of MEMORY draft #3 and #5) emerged only from the disagreement walk-through; neither standalone file would have produced it. Will confirmed the adversarial brief itself is the reusable lesson.

**How to apply:** When spawning an adversarial pair via TeamCreate + Agent x 2:
1. Tell the skeptical role to default to the negative verdict and argue from there ("reject unless"), not the neutral one ("evaluate").
2. Tell the affirmative role to engage with pushback genuinely and let evidence move them — explicitly call out the failure modes (don't cave to be agreeable; don't dig in for sport).
3. State the test purpose in both prompts — "team-lead is evaluating whether the pair adds value over solo" makes both members surface their independent reasoning rather than negotiate for consensus.
4. Reserve this pattern for high-judgment work (memory writes, doctrine, trade-proposal phrasing, position-sizing) where the cost of a wrong "keep"/"exclude" is high. Do not use for routine research, data pulls, or single-source extraction — second voice has no independent information to add.
