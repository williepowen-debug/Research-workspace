---
name: domain-agent-steelman-backstop
description: "When Prome+Will lean toward an answer, explicitly invite the domain agent to push back rather than just confirm — catches Prome reasoning errors and produces strictly better outcomes than Prome+Will alone"
metadata: 
  node_type: memory
  type: finding
  originSessionId: f0f985b0-9a14-43dc-9b94-8e5ec72d51fe
---

When Prome and Will converge on a recommendation in a multi-step deliberation, **explicitly invite the domain agent to push back with a steelman of an alternative** rather than asking him to confirm the recommendation.

**Validated 2026-05-21 BOND Matrix v2 Q1:** Prome synthesized an "Option C: flat <50% on offering convention" recommendation, claimed it would catch the 5/12 10Y print. Will endorsed it. The message to BOND framed the question as "evaluate Option C; steelman whichever you actually prefer, don't capitulate just because Prome+Will lean simpler." BOND responded with Option (c) pure per-tenor percentile and three arguments: (1) any flat threshold embeds a hidden uniformity assumption across tenors with structurally different baselines; (2) compound OR-logic is operationally fragile (flat becomes habit, percentile becomes footnote); (3) one coherent question ("was demand weak for this tenor?") beats a multi-rule hybrid. Will + Prome immediately conceded. BOND was right.

**Side benefit caught in the same exchange:** Prome's framing of Option C contained a math error (claimed 51.5% < 50% would catch the 5/12 print — 51.5% is HIGHER than 50%). Prome caught the error before sending and corrected openly to Will. The explicit-steelman framing made the correction natural rather than face-saving.

**Why:** Prome operates on synthesized summaries of sub-agent work, not direct domain data. Math errors and framing drift accumulate. Domain agents working from their own files + spawned datasets see things Prome can't. When Prome and Will both lean simple/clean, simplicity bias compounds. The steelman framing breaks the bias — and yields better answers ~consistently.

**How to apply:**
- When walking through multi-question decisions with a domain agent (like the Q1-Q5 walkthrough), and Prome+Will have converged on a leaning, **don't ask the domain agent to confirm**. Ask him to push back. Phrase explicitly: "Don't capitulate just because Prome+Will lean X. If the data argues for Y, say so. Steelman whichever you actually prefer."
- Use this on ALL multi-step domain decisions, not just ones where Prome suspects he's wrong. The error-catching value is highest precisely when Prome doesn't suspect.
- Related: [[finding_framing_precision_overlay]] (when sub-agent output is conceptually right but literally overspecified — same family of issues from the inverse direction).
- Also related: [[feedback_subagent_prompt_discipline]] — steelman invitations are a sub-agent prompt discipline addition.

**Counter-pattern to avoid:**
- Don't ask "do you agree with C?" — that biases toward confirmation.
- Don't ask "is C right?" — that biases toward yes/no, not toward the better alternative.
- Don't omit the explicit anti-capitulation language — agents (like humans) default to lower-friction confirmation when the framing is ambiguous.
