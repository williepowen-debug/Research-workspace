# Root `CLAUDE.md` active-list mirror — DRAFT EDIT, awaiting Will's ruling

**Status:** 🔒 **DRAFTED, NOT APPLIED.** Root `CLAUDE.md` is auto-injected fleet-wide; per Will's 2026-08-04 ruling this mirror is a **named, Will-gated Phase 1 step** — *"PROME may packet the needed mirror edit, but should not silently move root canon/auto-injected boot surfaces."*
**Drafted:** 2026-08-05 (PROME), immediately after the Phase 1 taxonomy pass on `PROME/ROSTER.md`.
**Target:** root `CLAUDE.md` line 26, the `**Active agents (verified …)**` paragraph.

---

## Why this exists

`PROME/ROSTER.md` now splits its live roster into five descriptive classes. Root `CLAUDE.md:26` carries a **mirror** of that roster and cites `PROME/ROSTER.md` as its source of truth. Until this edit lands, **root is one taxonomy behind by design** — flagged on ROSTER's own header so no reader mistakes the lag for drift.

**Membership is unchanged**, which bounds the risk precisely: root's *list of names* is still correct today. Only the bucket vocabulary is newer in ROSTER. Nothing operational depends on this edit.

**Rot history on this exact pair** (why it is a step and not a footnote): the WP-W2 line read "still open" for **9 days** past its own closing commit `37ee2748e`; OZK's dormant→ACTIVE flip lagged root until 7/25.

## What changes — and what deliberately does not

**Does NOT change:** the list of active agent names · Tier-2 · Special · any dagger footnote · any operational instruction · the reconcile pointer to `PROME/ROSTER.md`.

**Changes:** adds one sentence naming the five descriptive classes and stating they are descriptive-only, so a fleet-wide boot read is not left with the superseded "one flat active list" mental model.

**Deliberately NOT proposed:** re-listing all 30 agents under class headings in root. That would duplicate a high-churn field into an auto-injected surface — the precise failure this migration exists to end (`[[finding_roster_change_propagates_to_all_surfaces]]`). **Root should point, not mirror the churny part.**

---

## The edit

**Insert ONE sentence** at the end of the existing `**Active agents …**` paragraph (root `CLAUDE.md:26`), immediately before the closing `*(Dormant / Retired / Archive-source taxonomy → `PROME/ROSTER.md` …)*` clause. Nothing else in the paragraph is touched.

> **★ As of 2026-08-05 `PROME/ROSTER.md` splits these ACTIVE agents into five DESCRIPTIVE classes — ORGANIZING / SERVICE · REVIEW / QC · DOMAIN ACTIVE · PROVISIONAL ACTIVE · EVENT-DRIVEN SPECIALIST — with membership unchanged (30 in, 30 out). The classes change no routing, boot priority, DAEDALUS grading, WALTER delivery or NEXUS read obligation; `PROVISIONAL ACTIVE` and `EVENT-DRIVEN SPECIALIST` are cadence/proof descriptions, NOT demotions or lesser authority. Read class in `PROME/ROSTER.md` — do not re-list agents by class here.**

## Verification if approved

1. Confirm the edit touches **only** that paragraph — `git diff -- CLAUDE.md` should show one paragraph, zero name changes.
2. Confirm the name list still matches ROSTER's ACTIVE set (30) by name-set diff, not by eye.
3. Drop the "one taxonomy behind by design" caveat from `PROME/ROSTER.md`'s header in the **same commit**, so the two never disagree about whether they agree.

## If declined or deferred

No action needed and nothing breaks. ROSTER's header already discloses the lag and explains it is Will-gated, so a reader who notices the difference is told why. The caveat simply stays until Will rules.
