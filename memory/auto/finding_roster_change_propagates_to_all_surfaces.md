---
name: finding_roster_change_propagates_to_all_surfaces
description: roster/state change must propagate to every mirror surface; inline copies drift — point to the owner doc, don't duplicate the churny part
metadata:
  type: finding
---

When the authoritative roster (`PROME/ROSTER.md`) was reconciled, the SAME fact was mirrored in ≥6 other surfaces — root `CLAUDE.md` inline list, `AGENTS.md` table, `AGENTS/_INDEX.md`, `AGENTS/_NETWORK.md` topology, and the 5 `AGENTS/_*.md` group files — and **every one had silently drifted**: retired agents shown as live, broken folder-links to `_archive/`-moved or outright-deleted dirs, and tier labels that were flatly false ("archive-source, left in place" — the folders had actually been pruned). Fixing ROSTER instantly re-exposed the drift in each mirror; the inline copy inside the auto-injected/boot-read doc (`CLAUDE.md`) is where drift hides longest because nobody re-greps it.

**Why:** duplicated lists rot independently. A single retirement/revival must be hand-propagated to N surfaces, and the highest-churn field (dormant/retired/archive *status*) is exactly the one most often duplicated inline for "convenience." Update cadence of the mirror < churn rate of the field ⇒ guaranteed silent drift.

**How to apply:**
1. **Point, don't duplicate the churny part.** Keep ONE authoritative copy of a high-churn field (ROSTER) and have every other surface POINT to it. Root `CLAUDE.md` now lists Active+Tier-2 inline (rare change, high boot value) but points the Dormant/Retired/Archive-source taxonomy to `PROME/ROSTER.md`.
2. **After any roster/state change, sweep every mirror** — grep all roster/index/topology surfaces, don't sample ([[finding_comprehensive_grep_over_sampling]]).
3. **Verify folder existence on disk before trusting a tier label** — `ls AGENTS/<NAME>` / check `_archive/`; a doc saying "left in place" was wrong.
4. General rule: **prefer a pointer over a mirror whenever the mirrored field churns faster than the surface's own update cadence.**

Related: [[finding_doc_mirror_consistency_check]] (canonical wins on drift), [[finding_verification_correction_downstream_propagation]] (grep derivatives after a fix), [[finding_verify_roster_by_commit_activity]] (how ROSTER itself is derived).
