---
name: finding_artifact_redeploy_same_url
description: Updating a published Artifact in a LATER session needs two things future-you won't have by default — the HTML source (commit it into the repo; session scratchpad doesn't survive) and the URL passed as url= to the Artifact tool (a fresh session mints a NEW URL without it, breaking the user's bookmark)
metadata:
  type: reference
---

The Artifact tool publishes to a stable claude.ai URL, but **updating that same artifact later is not automatic:**
- **Source:** the HTML built in session scratchpad (`/tmp/.../scratchpad/`) is gone next session. Commit the source into the repo (e.g. `PROME/artifacts/<name>.html`) so any future session can read + edit it.
- **URL:** in a *fresh* session, calling Artifact with a new `file_path` mints a **NEW** URL — the user's bookmark goes stale. To hit the same artifact you MUST pass `url=<existing URL>`. Same-session redeploys of the same file_path keep the URL automatically; cross-session ones do not.

**Why:** the URL↔file binding is session-scoped; only `url=` re-binds across sessions. A user who bookmarked the artifact expects one durable link that evolves, not a new link each update.

**How to apply:** when you publish an artifact the user will keep — immediately (a) commit its source to the repo, and (b) record the URL + a "redeploy via `url=`" recipe somewhere boot-read (the tracker doc / SCRATCH). Future updates = edit the repo source → `Artifact(file_path=<repo source>, url=<URL>, label=<version>)`. Verify structure (div balance) + JS syntax (`node --check` on the extracted `<script>`) before redeploy. First shipped 2026-07-05 (the July-convergence 2-tab situation board). Related: [[finding_closeout_as_writeback_tail]].
