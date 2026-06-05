---
name: Sub-agent Prompt Discipline
description: When spawning research sub-agents, 4 rules to keep returns efficient without over-templating
type: feedback
originSessionId: 1c71cf68-1772-4e62-a2be-566f76ade21d
---
When spawning research/verify sub-agents, apply 4 rules to the prompt:

1. **Lead with the specific decision** the result will inform (not just the research question). E.g., "WALTER needs to decide whether to route this as IMMEDIATE/PRIORITY/ROUTINE" rather than "tell me about X."
2. **Hard word cap on the TOTAL deliverable**, sized to task: ~400 for claim-verify, ~500 for event-verify, ~800 for transmission-chain research. Without a total cap, agents write to the ceiling. **Critical subtlety:** per-question budgets multiply — "100-200 words each × 7 questions" reads as "700-1400 ceiling" to the agent, and they'll write to the top. Always state a single total cap. Per-section budgets are optional guidance, never the only bound.
3. **Instruct "prioritize decision-usefulness over comprehensiveness."** Cuts background prose the caller already has.
4. **Require a VERDICT line at the top**, not buried. Single sentence, decision-useful. If reader only sees one line, it's that line.

**Why:** Apr 20 2026 session — NV HOA transmission-chain sub-agent returned ~1,400 words, of which ~500 were background I already had (AB125 summary, Silver State Bank story). ~30% waste. Blue Owl verification sub-agent ran the same day returned ~600 words with ~0% waste because prompt was tight on task + bounded.

**How to apply:** Every time I write a sub-agent prompt. Don't build a spec/template file — Will pushed back on standardization as over-plumbing for WALTER's ~10-15-lifetime sub-agent volume. Keep it as personal discipline when writing prompts, not a doc to maintain.

**Corollary:** Don't over-constrain sub-agent format. Rigid "VERDICT + 3 bullets" risks missing nuances the agent would otherwise surface (e.g., Blue Owl's "Rees not party to filing" found because prompt allowed the agent to roam within the task). Balance: tight on *length and decision-focus*, loose on *structure within the body*.
