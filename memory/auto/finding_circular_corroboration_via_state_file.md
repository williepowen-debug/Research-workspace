---
name: finding-circular-corroboration-via-state-file
description: "When N agents agree on a derivable fact, check whether they sourced it independently OR read it from a shared state file — majority-agreement on derived facts is circular if the state file is the upstream source. Independence discipline applies to your own state, not just news sources."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 50b9b481-5763-4da2-a61d-0f74ff06ff99
---

When an agent-set appears to corroborate a derivable fact (a date, a threshold mark, a scenario weight, a prediction target), check whether each agent independently sourced it OR read it from a shared state file (STATUS.md, CALENDAR, root docs). Majority-agreement on derived facts can be circular if the state file is the upstream source for the agreeing agents.

**Why:** NEXUS STATUS said May CPI was 6/12. HAWK + BRENT briefs also said 6/12. That 2/3 majority looked like corroboration. Authoritative BLS = 6/10. VIOLET + SAM (calendar-disciplined) had 6/10. HAWK + BRENT likely ingested 6/12 from upstream STATUS — they didn't independently source the BLS calendar. The "majority" was NEXUS's own error reflected back. This is NEXUS's own independence discipline ("3 agents reading one Reuters article ≠ convergence") applied to its own state file as an *error source* — but the discipline doesn't fire automatically when the upstream is your own work.

**How to apply:** Any time an agent-set agrees on something derivable from a shared state file:
- Check the *source chain*: did each agent independently source it (BLS calendar, Treasury auction calendar, Reuters primary, exchange feed) OR is the agent's brief/STATUS plausibly reading from your shared state?
- Verify load-bearing derived facts against external primaries before propagating — especially dates, thresholds, and scenario probability targets, which look factual but are easily contaminated.
- Treat agreement on a *raw observation* (a price print, a CFTC number, a CB transcript line) differently from agreement on a *derived fact* (a date, a threshold, a probability). Raw observations are independent if sourced from different feeds; derived facts are independent only if independently computed.
- The trap is one-way: if every agent disagrees with the shared state, you'll catch it immediately. If everyone agrees with it, the agreement looks like proof — that's when the discipline must fire.

**Relation to adjacent disciplines:** Distinct from [[feedback-verify-existence-external-primaries]] (fleet silence ≠ event didn't happen — that's the opposite direction). Distinct from Discipline F shared-antecedent test ([[finding-shared-antecedent-independence-test]] — that's about latent causal assumptions, not propagated facts). This is *propagation correlation* — the state file as a fact-source that contaminates downstream "independent" reads.

**Generalization:** any shared substrate (state files, root CLAUDE.md, calendar docs, prediction-ledger source-of-truth) can propagate its errors as fake-majority convergence. The bigger the substrate's reach, the wider the contamination. Worth a periodic external-primary audit on the highest-touch derived facts in shared substrate.

**Validated:** 2026-06-08, NEXUS Type-B synthesis pass — CPI date 6/12→6/10 catch.
