---
name: finding_proposed_rule_must_be_canon_tested
description: test a proposed rule against standing canon for CONTRADICTION before downstream artifacts are written against it — and note that off-repo planning docs escape canon_check entirely
metadata:
  type: finding
---

A ratified planning doc (RAV roster-responsibility plan v4, 2026-08-04) proposed the rule *"every recurring responsibility needs **exactly one owner**, one artifact, one escalation path."* It reads as obviously good governance. **It directly contradicts standing root canon**, which mandates the opposite in terms:

> *"Scoped overlaps are intentional — reconcile shared metrics to **one figure**, don't silo: CORAL↔MARCO (FL migration/tourism) and AEOLUS↔CORAL (FL climate/coastal)."*

Read literally, the new rule would have pushed exactly those pairs to **silo where canon says reconcile** — and the reviewer (RAV) had those same seams on its own preflight list, so it would have been testing them against a rule that contradicts canon. Caught at the Phase 0 ruling table; Will amended the wording to **"one owner OF RECORD"** (overlap legal; ambiguity about who reconciles and who answers for it is not) before any downstream artifact was written.

**Why this class is dangerous specifically:** a proposed rule does no damage while it is prose in a plan. It does damage the moment **downstream artifacts get written against it** — taxonomy, packets, review criteria, agent instructions. Those inherit the contradiction silently and each one is a separate thing to unwind. **The cost of catching it is one grep at ruling time; the cost of missing it scales with everything built afterward.** And the rules most likely to contain a contradiction are the ones that sound most obviously correct — nobody re-reads canon to check "one owner per responsibility."

⚠️ **The mechanism that exists for this class could not have caught it.** DAEDALUS's `canon_check.py` (built 2026-08-03) is purpose-built to find *docs that PRESCRIBE what canon forbids* — but it scans the **repo**, and this plan lived **off-repo** (Will's `Downloads/`, delivered as a file). **Off-repo planning artifacts — the exact place where new rules are drafted — are outside the checker's reach by construction.** Ratification is the moment they cross into the repo's authority, and no automated gate sits at that boundary.

**How to apply:**
1. **At ratification of any new rule/spec/threshold, grep standing canon for the concept before recording the ruling** — not after. The ruling artifact should cite the canon it was checked against.
2. **Suspect the rules that sound most obviously right.** "Exactly one owner," "always X," "never Y" — universals are where contradictions hide, because the exception canon already carved out is invisible to someone writing from first principles.
3. **Fix by amending the WORDING at the source artifact**, not by noting the exception downstream. Here: "exactly one owner" → "one owner of record," carried verbatim into every downstream packet so nothing is written against the original.
4. **Treat off-repo → in-repo as an unguarded boundary.** Any doc that arrives from outside (Downloads, email, a Will paste) and will govern in-repo work gets a manual canon pass, because `canon_check.py` never saw it.
5. Reviewing a plan carefully is **not** the same as canon-testing it — PROME reviewed v3 in full, wrote three amendments, and still did not catch this until drafting the ruling table forced a line-by-line pass against canon.

Related: [[finding_roster_change_propagates_to_all_surfaces]] (the sibling failure caught at the same Phase 0), [[finding_lessons_file_cannot_detect_own_contradictions]], [[finding_doc_mirror_consistency_check]] (canonical wins on drift).
