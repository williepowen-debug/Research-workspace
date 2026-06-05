---
name: finding-subagent-baseline-audit
description: "Sub-agent specs whose job is 'maintain a set' (catalysts, KB rows, trade triggers, signal routes) need explicit baseline-scope audit rubrics, not just incremental-update rubrics. Without baseline audits, the agent extends-from-precedent rather than re-baselines-against-source — and the propagation bug is silent because nothing in the agent's job description surfaces it."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 2ca46311-2089-497f-b2d4-f84fbc8641c1
---

When a sub-agent's job is to maintain a *set* of entries — forward catalysts, KB rows, trade triggers, signal routes, monitored thresholds — the natural spec design is an incremental-update rubric: "add new items, prune resolved items, refresh stale items." This is the obvious framing and it's wrong-by-omission.

**The silent bug:** the rubric tells the agent to *extend* the existing set, not to *audit the existing set against source-of-truth*. So the agent extends from precedent — whatever scope was in the file when it inherited it becomes the de facto scope going forward. If the inherited scope was narrower than source (e.g., scoped by an outdated thesis lens, hand-built by the parent agent under a now-superseded framing), the agent never catches it. The narrowed scope persists indefinitely until something forces a direct investigation.

**The bug doesn't surface because:**
1. The agent isn't told to audit baseline scope, so it doesn't.
2. The parent agent (SAM/CARL/etc) doesn't see the gap because its boot doc reads only what's *in* the file, not what's *missing* from the file.
3. The catalyst countdown / KB count / trigger list all look healthy — they're internally consistent. The gap is structural, not relational.

**The trigger pattern that does surface it:** parent agent asks "investigate why X was missed" rather than "backfill X." Investigate-mode forces the agent to source, which exposes the structural exclusion. Backfill-mode would have added X and moved on.

**Spec fix (the actual finding):** for any sub-agent that maintains a set, add an explicit baseline-scope audit step with two triggers:
- **Periodic** (e.g., monthly for catalysts, weekly for fast-moving sets) — first run of new period fires a full audit against recurring-source-of-truth.
- **Post-miss mandatory** — when parent flags a known-resolved entry that was absent from the set, audit the full release-class / category.

Pair with a **decline-memory mechanism** so the audit converges over time:
- Parent records declined items in a CALIBRATION section (sub-agent read-only).
- Audit reads CALIBRATION before building the proposed delta, excludes declined classes.
- Declination clears only when parent removes the entry (signals the scope-relevance has changed).
- Without this, the audit nags the same declined items every period and the parent stops trusting the output.

Output should be **propose-only** — audit discovers, parent decides what's in-scope under current framing. This preserves the "discovery is fine; acting on it is not" rule that most sub-agents already operate under.

**Validated 2026-06-02 on SAM's KOYOMI:** Run-4 surfaced ~months-old structural exclusion (super-long JGB auctions tracked; 2Y/5Y belly/front silently dropped). Caught only because Will + SAM directed KOYOMI to *investigate* the Jun 2 10Y miss rather than backfill it. Spec amended with monthly + post-miss BASELINE AUDIT (step 2a) + CALIBRATION-based decline-memory.

**Transferable to:**
- KURA (workbook): KB row set could similarly lose categories if SAM's thesis lens shifts and KURA extends-from-precedent.
- METSUKE (trade-doc drift): trigger set in TRADE.md could lose categories of trigger types.
- Any future CARL / REGINALD / BROCK / HENRY sub-agents whose job is set-maintenance.
- Even the parent agents' own catalysts/triggers/monitors: SAM's STATUS.md "what to watch" table is itself a set maintained incrementally; the same bug can hit at parent level (worth a periodic SAM self-audit against THESIS § CATALYST SEQUENCE).

Related: [[finding_subagent_memory_split]] (MEMORY-pair architecture is where the CALIBRATION section lives); [[finding_audit_behavioral_ranking]] (behavioral-impact ranking applies to audit findings too — "set is incomplete" is high-behavioral-impact even when current-set entries look fine).
