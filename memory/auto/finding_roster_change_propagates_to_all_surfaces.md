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

**n+1, 2026-08-04 — and the new angle is that the BLIND SPOT IS INHERITED BY THE PLANS THAT PROPOSE CHANGING THE ROSTER.** A ratified roster-migration plan (RAV v4) listed the Phase-1 file targets as `PROME/ROSTER.md`, `AGENTS/_INDEX.md`, and *"root `AGENTS.md` **or other mirrored boot-orientation surfaces, IF** they carry active lists."* Root `CLAUDE.md:26` **does** carry one and **was not named** — so the plan to fix roster taxonomy would have edited the roster and left the auto-injected mirror behind, i.e. reproduced this exact finding while executing a project whose stated goal is killing this class. Caught at Phase 0 and promoted to a **named, Will-gated step** before any edit ran. **The point sharper than "sweep the mirrors": the surface where drift hides longest also hides from the DESIGN DOCS that plan changes to it.** When scoping any taxonomy/roster/state migration, enumerate the mirrors *yourself* from a grep; do not trust the plan's file list, however carefully reviewed — a conditional clause ("if they carry active lists") reads as coverage while asserting nothing.

Related: [[finding_doc_mirror_consistency_check]] (canonical wins on drift), [[finding_verification_correction_downstream_propagation]] (grep derivatives after a fix), [[finding_verify_roster_by_commit_activity]] (how ROSTER itself is derived), [[finding_proposed_rule_must_be_canon_tested]] (the sibling failure at the same Phase 0 — a proposed rule that contradicted standing canon).

**n+2, 2026-07-25 (WALTER) — the surface a reference-sweep structurally CANNOT catch: the parent's THRESHOLD REGISTRY.**
A promotion/spinout sweep covers files, refs, INDEX, ROSTER and FLEET_MAP — all **documents that MENTION the child**. It does not cover **registries owned by the parent that ACT on the child**, because those are a **behavioural** surface, and they only fail **at fire time**.

**Instance.** WAL was promoted out of REGINALD on 2026-07-25 with a thorough six-stage cutover. **`REG-T-02` (`WAL-PRICE < 78`, sustain 1) still read `recipient_chain = "REGINALD action / Will"`.** So on the day WAL trades below $78, the boot scan fires IMMEDIATE to REGINALD and Will — **and the agent whose entire book is that ticker is not on the action line of its own name's price trigger.** Sustain 1 means there is no second day to catch it. Nobody had looked, because a ref-rewrite pass has no reason to open a TSV of thresholds.

**⇒ Add to any promotion/spinout checklist, as its own named step: *"does any registered trigger, gate or prediction in the PARENT's registries name the promoted entity as its METRIC?"*** Then fix the `recipient_chain`. (The OZK precedent likely has the same shape.) Note the lane discipline that still applies: flag the edit to the owning desks rather than editing another agent's canonical registry yourself.

Related: [[finding_banded_threshold_with_no_metric_surface_is_untrippable]] · [[finding_retired_threshold_has_no_publisher]]
