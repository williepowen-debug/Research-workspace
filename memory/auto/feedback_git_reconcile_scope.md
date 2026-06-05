---
name: Scope "supersede local state" narrowly — don't discard net-new uncommitted work
description: When told to pull and supersede local state to resolve a git divergence, only discard files that actually conflict; preserve untracked net-new work
type: feedback
originSessionId: 46be196f-9d38-4a42-a690-b11f8ac3202b
---
When reconciling a git divergence by pulling from GitHub, **"supersede local state" means resolve the conflict, not wipe everything uncommitted.** Distinguish between two kinds of uncommitted work:

1. **Stale modifications to tracked files** (STATUS.md, workbooks) that conflict with incoming commits — these can be discarded via `git restore`.
2. **Net-new untracked files** (new research docs, new outbox signals) that don't conflict with anything on GitHub — these should be preserved unless they're explicitly confirmed redundant.

**Why:** Will gave this feedback when he noticed three TOUR_*.md research files got trashed alongside the stale STATUS.md edits. His words: "What is the argument for ditching?" — clear pushback. The research files were standalone content; their conclusions may have been summarized in the dashboard but the detail (operator-by-operator tables, Q2 2026 NCLH watch, confidence breakdowns, tradeable hooks) doesn't live anywhere else. Discarding was a judgment error conflating "reconcile STATUS.md divergence" with "discard all uncommitted work."

**How to apply:** Before discarding untracked files as part of a "pull and supersede" operation, check whether they're (a) net-new content that doesn't conflict, or (b) stale duplicates of what's already on GitHub. Default to preserving (a). Flag uncertainty explicitly: "I'll restore X and Y since they're untracked and don't conflict — confirm if you also want to ditch." Research that concludes "this isn't the play" is still valuable research — don't delete the file just because the finding was negative.
