# RAV → PROME: Suggested Operating Improvements (12 items)
**Filed:** 2026-08-21 ~23:2x ET by PROME · **Provenance:** Will-relayed in PROME's live session — RAV message timestamped [8/21/2026 11:04 PM], pasted verbatim by Will with "I would like you to take a look and give me your thoughts." This file is the artifact of record; the text below is VERBATIM from the relay (three message chunks joined where the relay split mid-word: "tre / ated").
**Status:** PROME per-item disposition DELIVERED to Will in-session 8/21 ~23:1x — **recommendation pending Will's word, nothing adopted yet.** Disposition summary at bottom. DAEDALUS review requested by Will in its own window 8/21 late.

---

## RAV's text (verbatim)

Here is the list I would give PROME. I'd frame it as operational guidance, not criticism.

Suggested PROME Operating Improvements

1. Publish a state authority map

Create a short canonical map that tells every desk which surfaces are authoritative and which are derived. Suggested hierarchy:

• Owner thesis files = durable desk truth
• Trigger/catalyst ledger = dated event truth
• Correction/refutation ledger = killed/stale/retracted claim truth
• Operator queue = Will-needed action truth
• HEARTBEAT/HELM/daily brief = derived summary only

Every recurring surface should label itself: canonical, derived, scratch, historical, or archive.

2. Make derived summaries source-anchored

For every important claim in HEARTBEAT/HELM/STATUS, PROME should cite the owner file, trigger row, correction row, or Will ruling that supports it. If no anchor exists, label it explicitly:

• UNANCHORED
• OWNER_CONFIRMATION_NEEDED
• INTERNAL_ARTIFACT_ONLY
• PRIMARY_SOURCE_VERIFIED

3. Separate routed from consumed

PROME should stop treating routed/filed/landed as close to complete. Use explicit states:

• created
• routed
• landed
• read
• owner-encoded
• answered
• closed

A packet should not be described as resolved unless it reaches owner-encoded, answered, or closed.

4. Add PASS semantics to every check

Every checker report should say what a clean result proves and what it does not prove. Example:

PASS means no stale token found in checked files. It does not prove owner consumption, external truth, or thesis freshness.

This should become mandatory for new checks and gradually backfilled for important existing ones.

5. Create a correction/refutation ledger as a first-class surface

Do not scatter killed claims across commit messages, desk scratch, STATUS notes, and inboxes. PROME should maintain one canonical ledger for:

• killed claims
• narrowed claims
• stale-surface discoveries
• false PASS events
• retractions that introduced new claims
• source-basis corrections
• "fix was itself wrong" events

6. Run a weekly compression pass

Once per week, PROME should ask:

• Which surfaces duplicated another surface?
• Which checks actually changed decisions?
• Which new rules should remain local instead of becoming fleet law?
• Which stale summaries should be archived or demoted?
• Which operator-facing surfaces became too noisy?

The goal is not more process. The goal is fewer, better surfaces.

7. Demote commit messages from state to evidence

Commit messages can explain changes, but PROME should not let them become the operational memory layer. If a commit changes current truth, that truth must land in a canonical surface.

8. Distinguish repo truth from world truth

PROME should tag important claims by verification level:

• internal artifact verified
• primary source verified
• secondary source only
• market-data current as of timestamp
• owner asserted / not independently checked
• stale risk

This prevents repo-internal consistency from being mistaken for external verification.

9. Make Will-dependence explicit

If something requires Will, say so and stop. PROME should prefer clean escalation over trying to resolve authority-sensitive ambiguity with more prose. Useful labels:

• WILL_RULING_REQUIRED
• WILL_PRIORITY_REQUIRED
• WILL_CONSUMPTION_REQUIRED
• NO_AGENT_AUTHORITY_TO_CLOSE

10. Build a small regression set from real failures

PROME should preserve 15–25 known failure examples and use them to test future checks/workflows. Include:

• stale header / fresh body
• routed but unread packet
• false PASS checker
• summary carrying killed state
• retraction that introduced a new claim
• wrong instrument or wrong basis
• correction recorded on the wrong surface

11. Protect the daily brief from becoming canonical

HEARTBEAT/HELM should be treated as command compression, not ground truth. Each brief should include a line like:

This brief is derived. Canonical truth remains with owner files, trigger ledger, correction ledger, and Will rulings.

12. Prefer demotion over deletion

When a surface is stale or redundant, mark it historical/derived/archive before deleting anything. The system benefits from auditability, but future agents need to know the file is no longer live.

Priority order for PROME

1. State authority map
2. Delivery-versus-consumption labels
3. PASS semantics for checks
4. Source-anchored summaries
5. Correction/refutation ledger
6. Weekly compression pass

If PROME only does the first three, the system gets materially safer. The rest improve maintainability and reduce future drift.

---

## PROME disposition summary (delivered to Will 8/21 ~23:1x, PENDING his word)

- **Already law (affirm + pointer, no build):** 7 (commits=evidence — record-of-action canon) · 9 (Will-dependence — WILL_QUEUE/fire-ledger/verbatim-word spine) · 12 (demotion-over-deletion — FROZEN banners/flow rules; our addendum: every banner needs a dated rewrite trigger, `finding_banner_is_a_warning_not_a_fix`).
- **Partially built, real gap = vocabulary/consolidation:** 1 (trust stack exists in SYSTEM.md but is PROME-facing → one-page fleet-facing consolidation) · 2+8 (**merge into ONE verification-level STATE_VOCABULARY class** — RAV proposes two overlapping taxonomies) · 3 (**best item — consumption-state ladder as a STATE_VOCABULARY class**; practice already moved [landed-unread markers, `consumed_by`], token set is the gap) · 4 (CHECK_STANDARD amendment; env_doctor's checked/NOT-checked perimeter line is the existing exemplar) · 6 (fold RAV's question list into the existing Sunday sitting — "which checks changed decisions" ≡ the meta-vs-market agenda item; no new cadence).
- **Genuinely new, commission:** 10 (**regression fixtures from real failures** — we hold ~455 failure lessons, zero executable fixtures; the missing half of `finding_adoption_is_not_validation`; DAEDALUS lane).
- **Hold for design:** 5 (correction/refutation ledger) — **collides with Will's NO-SECOND-STORE constraint** from the memory commission + shared-file contention + duplicates owner CHANGELOGs; route to DAEDALUS as a design QUESTION with that constraint attached; CHECK_STANDARD §12 base-rate-before-wiring applies; "don't build it" stays a live answer. **→ UPGRADED 8/21 late to ANSWERED-BY-FORUM-6, DON'T-BUILD-AS-SPECIFIED (DAEDALUS review, PROME artifact-verified: forum-6 ruled index-not-store; its mechanisms landed 8/21 AFTER RAV's mirror snapshot — STATE_VOCABULARY Class 10 [assertion-row contract, forum-6 R6] + BLUEPRINTS/CORRECTION_FORM.md [forum-6 R2], commit `706842783`. If Will wants one place to SEE corrections: generated VIEW over owner surfaces; revisit only on a named gap the forum's mechanisms don't cover).**
- **Cheap adopt at next natural touch:** 11 (derived banner on HEARTBEAT/Helm).
- **Pushback noted:** item 3's "stop treating routed as complete" is fair as history, already moved as behavior; label proliferation risk — items 2/3/8/9 must land as ≤2 STATE_VOCABULARY classes via DAEDALUS, forward-only, not four ad-hoc conventions.
- **Amended safety ranking:** 3, 4, 10 = safety items · 1 = legibility · 5 = the one that could hurt if built as specified.
- **Proposed venue:** Sunday 8/23 sitting (dovetails the vocabulary one-cloth block). CHECK_STANDARD + STATE_VOCABULARY are DAEDALUS-owned; fleet law is Will-gated — nothing here is PROME-unilateral.

**DAEDALUS review DELIVERED 8/21 late (`AGENTS/DAEDALUS/upgrades/RAV_FEEDBACK_REVIEW_2026-08-21.md`, commit `bb315c197`) — high agreement; PROME CONCURS with its four sharpenings, which now ride this disposition to Will:** ① item 4 = one-sentence CHECK_STANDARD §2 amend (not a new section — §2 already carries the perimeter half) · ② item 5 upgraded to ANSWERED-BY-FORUM-6 (see amended line above) · ③ item 10 reframed: fixture PRACTICE exists n≥4; the build = a CHECK_STANDARD fixture-standard section + CHECKS.tsv index, fixtures living WITH their checks (a central 15–25 store would be PAT-071), post-8/28 · ④ vocabulary lands as EXACTLY Classes 11 (consumption-ladder, census-first, declared-exempt token) + 12 (verification-basis) + the surface-role enum, all in the 8/23 one-cloth block; item-9 tokens fold into the ⚖️/glyph register. PAT-124 minted (already-law fraction 5-of-12 = canon-discoverability metric → item 1's map must be GENERATED, labels canonical at surfaces). Sitting agenda updated (SCRATCH item 2) same commit.
