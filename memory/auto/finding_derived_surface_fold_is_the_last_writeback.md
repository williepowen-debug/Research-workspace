---
name: finding_derived_surface_fold_is_the_last_writeback
description: 5-of-5 stale derived surfaces were mid-session writes with later primary work — fix is ORDERING (fold last, before git), not compliance; check fold-commit-time ≥ last primary-commit-time
metadata:
  type: finding
---

**Finding (2026-07-31, NEXUS fleet brief audit, batches 1–3):** every CONTENT-STALE derived surface found in a 25-agent audit — 5 of 5 (WAL, CORAL, OSPREY, HAWK, BROCK NEXUS_BRIEFs) — was written **mid-session and then left behind by later same-session primary-file work**. Zero agents skipped the refresh; all sequenced it wrong. The misses included an owner's own gate FIRE (OSPREY, adjudicated the day after its brief said "fires tomorrow if...") and a prediction falsification landing 25 minutes after the brief that still said the work was "left undone" (HAWK FLOW-13).

**Why:** "refresh X every closeout" reads as satisfied the moment X is touched, so agents fold the derived surface when the content feels ready — mid-session — and the session's tail (closeout passes, late adjudications, register freezes) lands only on the primary. The derived surface then advertises a state its own author has superseded, which is worse than obvious staleness because the stamp looks current. Compliance metrics can't catch it: compliance was 100%.

**How to apply:** any derived/secondary surface refreshed "every session" (NEXUS_BRIEF, dashboard mirror, SCRATCH summary, board pin) must be folded as the **LAST write-back of the session — after the final primary-file write, immediately before git commit**. Mechanical check: derived-surface commit time ≥ the session's last primary-file commit time (one `git log -1` comparison). Ratified for NEXUS briefs as schema amendment 10 (Will-approved 2026-07-31, `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` row 20). Related but distinct: [[finding_banner_is_a_warning_not_a_fix]] (banner ≠ refresh), [[finding_completion_stamp_skip_reads_as_current]] (skipped stamp), [[finding_seeded_selfsweep_secondary_surface_rot]] (secondary surfaces rot first) — this one is the ORDERING defect inside a session that DID refresh.
