---
name: sub-agent-naming-identity-over-functional
description: Multi-agent systems with named sub-agents should prefer identity-naming (unique per parent — KOYOMI/FASTOW) over functional-naming (shared — CATALYST/WORKBOOK) at current scale; runtime coordination cost outweighs one-time setup cost when both compare
metadata: 
  node_type: memory
  type: finding
  originSessionId: dfbdc3ab-6524-4fe0-bedd-1de500eee64e
---

When designing the naming convention for sub-agents inside a multi-agent system (e.g., SAM's KOYOMI catalyst-keeper, BRENT's FASTOW catalyst-keeper), default to **identity-based naming** (unique per parent agent, typically thematic to the parent's domain) rather than **functional naming** (shared archetypal names like CATALYST / WORKBOOK / AUDITOR across all parents).

**Why:** The initial framing of this question (BRENT 6/4 PM) overstated the case for functional naming by emphasizing **one-time costs** (compound naming-decision cost: 8 agents × 3-4 sub-agents = 24-32 unique names to invent, ~5 min each per first-build = ~2-3 hours of cumulative naming effort) while under-weighting **recurring costs**.

The recurring cost dominates: **runtime coordination uses names as discriminators in every cross-agent reference.** "FASTOW caught it" is one disambiguation token; "BRENT.CATALYST caught it" forces parent.role notation in every conversation. With 8 parents × functional naming, every reference to "CATALYST" requires a parent disambiguator forever; with identity naming, the name itself carries the parent context. Compounded across thousands of cross-agent conversations and search queries, the runtime cost vastly exceeds the setup cost.

**How to apply:**
1. When a parent agent first builds a sub-agent, pick a name from a thematic convention rooted in the parent's domain (SAM uses Japanese — KOYOMI/KURA/METSUKE; BRENT uses Enron execs — FASTOW now, candidates SKILLING/LAY/WATKINS for future sub-agents). The theme is a coherence aid for the parent's own sub-fleet, not a system-wide pattern.
2. Don't try to enforce a system-wide naming convention across all agents — that re-introduces the runtime-coordination cost the identity naming was meant to avoid.
3. Greppability cost ("find all catalyst-keepers across the system") is real but small at current scale (a per-parent index in CLAUDE.md resolves it; or a top-level `AGENTS/SUBAGENT_REGISTRY.md` if it ever sprawls).
4. **Threshold to revisit:** ~10+ active agents × 3+ sub-agents each (= 30+ unique names). At that scale, namespace size may become unwieldy and the trade-off shifts. Until then, identity > functional.
5. Rename later is cheap when needed (`git mv` + sed pass per agent); committing to functional naming early is a one-way door (you lose the identity-name decisions if you generalize).

**Origin (6/4 — BRENT FASTOW build):** I argued functional naming on cognitive-load grounds; Will pushed back that namespace collision in runtime conversation outweighs the setup cost. Re-evaluated honestly, his framing was right and mine had weighted only the maintainer's view. The trade-off generalizes to any multi-agent system where humans (or other agents) reference sub-agents conversationally — coordination is the recurring cost, naming is the one-time cost.

**Related:** [[feedback_subagent_prompt_discipline]], [[finding_subagent_memory_split]], [[finding_subagent_baseline_audit]], [[finding_subagent_escalation_mode_discriminator]].
