---
name: finding_gh_run_watch_exit_status_unreliable
description: "`gh run watch --exit-status` can report failure on a run that actually succeeded; confirm via `gh run view --json conclusion`"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 1f8a06d0-723c-4698-b9ff-0f38c7b250f3
---

`gh run watch <id> --exit-status` returned exit code 1 for a GitHub Actions run that actually **succeeded** — every step green, conclusion "success", artifacts committed (observed 2026-06-29 on the RESEARCH-INTAKE `collect` workflow, twice). The non-zero exit was a `watch` artifact (a polling/connection blip), not a real failure.

**Why it matters:** if you gate "did the run pass?" on `gh run watch`'s exit code, you'll get false failures and may needlessly re-run, roll back, or report a problem that isn't there.

**How to apply:** treat `gh run watch` exit status as advisory only. Confirm the true outcome with `gh run view <id> --json conclusion --jq '.conclusion'` (and `--json jobs` / `--log-failed` to locate a genuinely failed step). Also ground-truth the *effect* — did the expected commit/artifact actually land. Same spirit as [[finding_fail_loud_on_incomplete_data]]: verify the real signal, not the wrapper's exit code.
