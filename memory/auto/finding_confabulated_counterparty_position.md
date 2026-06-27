---
name: finding_confabulated_counterparty_position
description: an agent can flag a "divergence" against a counterparty position it CONFABULATED (+ cite a fabricated source file); verify the attributed stance AND its cited source EXIST before reconciling, or you launder the phantom into your own state
metadata:
  type: finding
---

A flagged cross-agent "divergence" is only real if the counterparty's position is real. An agent can attribute a specific stance to another agent (or the coordinator), cite a source for it, and frame its own update as "diverging" — when the attributed stance and the cited source **do not exist**. If the coordinator accepts the framing and edits shared state to "reconcile," it launders the confabulation into the record as if it were a real position.

**Concrete (2026-06-27, NEXUS→PROME):** NEXUS's 11-day re-anchor flagged "I diverge from PROME's coordination read, which called for flipping to Grind 55%+" and cited a `PROME/coordination` digest. Ground truth: that digest **never existed** (no git history), no PROME doc held a "Grind 55%+" stance, and PROME doesn't even run the Break/Grind/Unresolved probability framework — that's NEXUS's own. NEXUS had projected a naive post-FOMC extrapolation of its *own* prior grind-lean (~47% at its 6/16 anchor) onto PROME, invented a source file, and dressed its update as a divergence. PROME initially accepted it and edited HEARTBEAT to "supersede PROME's Grind 55%+ lean" — laundering the phantom — before a (Will-prompted) provenance check caught it.

**Why:** a divergence framing is persuasive — it implies two *independent* reads converging on a disagreement. But the "two reads" can be one read plus a confabulated foil. LLM agents readily invent plausible-sounding source files and counterparty positions, especially when re-anchoring after a long dark window (no fresh ground truth on what the counterparty actually holds).

**How to apply:** when an agent flags a divergence against your (or another agent's) position, BEFORE reconciling: (1) confirm the **cited source actually exists** — `ls`/`git log` the file it names; a fabricated `PROME/coordination`-style path is the tell; (2) confirm **you actually hold the attributed stance** (don't reason "that sounds like something I'd say"); (3) if either fails, the divergence is a phantom — keep the agent's substantive analysis (often sound standalone), discard the counterparty framing, and do NOT edit shared state to "reconcile." Coordinator-specific: you are the laundering vector — your reconciliation edit is what turns a confabulation into "fact." Pairs with [[finding_circular_corroboration_via_state_file]] and [[feedback_verify_counts_before_propagating]].
