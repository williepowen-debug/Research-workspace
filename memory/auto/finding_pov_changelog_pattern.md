---
name: pov-changelog-pattern
description: "Extend an agent's thesis CHANGELOG.md from formal-version-only to include intra-version POV pivots; preserves narrative arc when STATUS gets pruned"
metadata: 
  node_type: memory
  type: finding
  originSessionId: ed5e7f4f-7858-4fd2-83ef-c223973fba68
---

**Pattern (LIQUID 5/20):** When pruning historical narrative from an agent's STATUS.md (e.g. deleting a multi-week-old "April Refresh" section to bring line count under ceiling), the literal facts are usually safe in KB.tsv but the **trajectory** — how the agent's read evolved over time — is not. Two separate state files leave a gap:

- **KB.tsv** captures point-in-time durable findings well, but reads as a flat list. You can't reconstruct "when did LIQUID change its mind about X, and why" by scanning it.
- **thesis/CHANGELOG.md** captures formal thesis-document revisions (v1 → v2), but these are rare — months apart. Intra-version pivots (e.g. "Apr 16 SOFR breach added as plumbing watch → May 18 resolved mechanical → May 20 channel migrated to duration") happen weekly and never get logged.

**The fix:** Extend CHANGELOG.md to also log dated POV-pivot entries between formal version sections. Schema per entry:
- **Prior view** (what the agent believed before)
- **Revised view** (what changed)
- **Trigger** (the data point or signal that forced the update)
- **Anchored in** (the KB entry or file where the finding now lives durably)

Reverse-chronological. Lives between the latest version and prior version sections so the most recent pivots read first.

**Why this works:** Captures the *arc* without re-litigating the *finding* (KB.tsv still owns the finding). When a future session asks "wait, why did we abandon the SOFR-IORB watch?" the CHANGELOG POV log answers in 4 lines with a pointer to KB-LIQ-051. Without it, future-self has to reconstruct from git blame + KB cross-refs + STATUS archaeology — and often the original framing is gone.

**How to apply:**
- Triggered when pruning multi-week-old narrative from a STATUS-equivalent live-state doc. Before deleting, capture the POV shift in CHANGELOG.
- Format the entries before the prune, not after — easier to write while the prior view is still on screen.
- Cross-link to the durable anchor (KB-XXX entry) where the literal finding lives — keeps CHANGELOG lean and KB-as-source-of-truth.
- Apply to agents with a thesis/CHANGELOG.md (LIQUID has one). Transferable to CARL, BROCK, HENRY when they have equivalent docs. For agents without one, consider creating it as part of the same refactor — it's a small file.

**Don't:**
- Don't log every observation as a POV pivot — only ones that changed *what the agent watches* or *how the agent interprets*. A dashboard refresh isn't a pivot; "we used to think X was the active channel, now Y is" is.
- Don't duplicate KB.tsv content in the CHANGELOG entry — link to it.
- Don't backfill POV pivots from deep git history at the start. Backfill 3-5 recent ones to demonstrate the pattern, then accrete forward.
