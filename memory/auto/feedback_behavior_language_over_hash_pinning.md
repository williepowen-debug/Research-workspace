---
name: behavior-language-over-hash-pinning
description: "When writing state files (SCRATCH, HANDOFF, STATUS), favor behavior-language over commit-hash references — hash pins decay 2-3 commits stale within 48h despite refresh discipline"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d7a1fb7a-828b-4ebd-88ab-39b07cb8b670
---

When describing repo state in state files (SCRATCH.md, HANDOFF.md, STATUS.md), favor behavior-language ("clean, synced to origin", "no uncommitted changes outside PROME/") over hash-pinning ("local master at 8a44dbe2").

**Why:** Caught 2026-05-17/18: PROME state files refreshed at HEAD `8a44dbe2` drifted 2-3 commits stale within 24h as BRENT, SENTRY, and Prome itself landed new commits. The hash references became silently misleading without any single file feeling "wrong." Cleanup pass on May 17 fixed it; Phase 3 dry run surfaced the pattern.

**How to apply:** When you're about to write a sentence like "HEAD is at <hash>", ask whether the next reader will care about the hash or the *condition* (clean / synced / diverged). If condition, write the condition. Pin hashes only when the hash itself is load-bearing (e.g., "fast-forwarded from X to Y" in a one-shot migration handoff). Related: [[verify-counts-before-propagating]] — same family of "verify state before restating" hygiene.
