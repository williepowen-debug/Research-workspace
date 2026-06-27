---
name: finding_verify_roster_by_commit_activity
description: "verify a roster/registry's membership by git-commit activity, not the curated list — curated rosters silently drift"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 15ed84fa-90f7-4146-8637-e1162df61c56
---

A curated agent roster (the "Active agents" list in a CLAUDE.md / registry) silently drifts from reality: the list is maintained by hand-edit, but whether an agent is actually *running* lives in the git log. On a 2026-06-27 verified-active pass the curated root-`CLAUDE.md` roster was materially wrong — **VIOLET** (118 commits/30d, the 2nd-most-active domain agent) was UNSLOTTED; **OZK** sat in *Active* with 0 commits/60d (cold 63 days); **DARWIN** was listed Tier-2 but its directory was already in `_archive` (phantom).

**Why:** rosters are prose-edited and lag; commit cadence is ground truth for "is this agent alive." A prose guess just re-encodes the drift — which is exactly why the root CLAUDE.md note demanded "a verified-active pass, not a prose guess."

**How to apply:** to reconcile a roster/registry, build a per-member **activity map first** — `git log --since=<60d> --pretty=%s | grep -cE '^NAME'` per agent + STATUS mtime + self-declared domain — and classify by that (Active / Tier-2 / Dormant / Retired), then diff against the curated list and fix the deltas. Park the verified classification in a durable doc (e.g. `PROME/ROSTER.md`) so the next refresh diffs instead of re-deriving. Corollary caught the same session: **check cross-dir consumers before archiving a "stale" doc** — `PROME/PREDICTIONS_MONITOR.md` looked like a dead PROME artifact but a `grep -rl` found it's NEXUS's live boot-read ledger (mislocated), so it was retained, not archived. Related: [[finding_board_lags_agents_not_vice_versa]], [[finding_external_consumer_check_before_restructure]].
