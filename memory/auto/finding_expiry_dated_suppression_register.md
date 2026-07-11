---
name: expiry-dated-suppression-register
description: "Pattern for suppressing known-benign monitor flags without rot: a TSV register where every row carries a MANDATORY expiry date; past expiry the row stops suppressing and raises its own flag, so no suppression can outlive its verification. Validated twice same-day 2026-07-11 (firetime allowlist + dashboard parked-agents)."
metadata: 
  node_type: memory
  type: reference
  originSessionId: e7bfb5dd-ea2c-4a2f-804f-3cb37e108c21
---

**The pattern:** when a monitoring surface (boot check, staleness scan, dashboard) keeps flagging things that are *verified benign* (a contract label misparsed as a date; an agent quiet by plan until a known catalyst), don't hardcode exceptions and don't tolerate a manual "known flags" ritual. Build a small TSV register where each row = `target + pattern/scope + expires + added + reason`, with three non-negotiable behaviors:

1. **Expiry is mandatory — no permanent suppressions.** The expiry date is the re-verification (or re-activation) deadline, chosen from the underlying fact (contract roll date, catalyst date, planned quiet-until).
2. **An expired row that still matches RE-FLAGS loudly** (e.g. `ALLOWLIST EXPIRED — re-verify, then renew or delete`) — the suppression converts back into a flag instead of silently continuing or silently vanishing. Rot cannot hide.
3. **Malformed rows fail loud and suppress nothing** — a broken register must never hide real flags.

**Why:** the alternative failure modes are both proven in this repo: (a) permanent exceptions rot into masks (the class where a dead ledger keeps citing rows as current), and (b) manual known-flags lists in session state (the pre-7/11 SCRATCH §Cautions ritual) make every reader re-litigate the same benign flags and train them to ignore rc≠0 — alarm fatigue that eventually eats a real flag.

**Instances:** `scripts/firetime_allowlist.tsv` (firetime_check known-benigns — seeded w/ a futures contract-label misparse and an artifact-relative-path false positive) and `PROME/tools/dashboard_parked.tsv` (fleet-dashboard "quiet by design" agents — parked_until = reactivation date, staleness resumes automatically; inbox flags stay on while parked). Both born 2026-07-11, Will-approved.

**How to apply:** any new checker that accumulates tolerated flags gets this register shape from day one; when reviewing an existing checker, a standing "known benign" note in prose is the smell that this pattern is owed. Related: [[finding_ledger_drift_behind_narrative]], [[finding_passive_surface_rot_push_not_dashboard]].
