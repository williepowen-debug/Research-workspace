---
name: finding_ownership_claim_is_last_to_move
description: "When the canonical owner of a fact MOVES, the docs/comments declaring who owns it are the last thing updated and the hardest to catch — they were CORRECT when written (often ratified by a named ruling), they live in prose nothing executes, and no check probes 'does this file name the right owner'."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 820ff136-af2b-4816-8675-107e0094d840
  modified: 2026-08-05T13:35:50.918Z
---

**Checks probe VALUES and INSTRUMENTS. Nothing probes "does this file name the right OWNER."** So when canonical ownership of a fact moves from surface A to surface B, the sentences that say *"A is canonical"* survive the move — and they are uniquely hard to catch, for three compounding reasons:

1. **They were CORRECT when written**, usually ratified by a named ruling whose whole subject was ownership. Reviewing the pointer surfaces the ruling that says it is right. **A stale pointer with a citation defends itself.**
2. **They live in comments, docstrings and prose that nothing executes.** A refactor changes the CODE; the claim about the code is untouched and un-run.
3. **The claim and the data diverge silently** — the data is now correct in the new home, so every value-level check passes. The defect is purely in the *pointer*.

**The case (BRENT, 2026-08-04).** A state-replacement pilot moved the machine home for thresholds from `THESIS.md` + hardcoded script tables into a single `REGISTRY.tsv`, proved the refactor value-equivalent 21/21 + 10/10, and shipped. Four days earlier a ruling ("one table, one home, boot reads the pointer") had consolidated ownership *onto THESIS*. The pilot moved the answer and **nothing re-asked the question**, leaving:

- the agent's **`CLAUDE.md` boot section** — the first thing a fresh session reads — still declaring *"THE CANONICAL THRESHOLD REGISTRY IS `thesis/THESIS.md`"*, **citing the script's docstring as its evidence**;
- that **script's docstring** still saying the same thing, referring readers to *"the tables below"* **that the same afternoon's commit had deleted**, while a comment 70 lines lower in the same file declared the opposite. **One file, two contradictory ownership declarations, for a day.**

That docstring has now mis-declared its own canonical source **three times running** (a frozen ledger → the thesis doc → the registry). Neither defect was found by any check — only by reconciling the shipped branch against the plan it was built from.

**★ Corollary from the same audit — a consolidation's coverage metric counts the flattering thing.** The pilot's headline was *"coverage 15 → 46 registered tests."* That counts **enrollment in the new registry**, not **migration of the fact into it**: 10 of 47 rows carried no machine-readable level, and a whole fourth threshold home (a separate script's hardcoded constants, two of which fired red at the next boot) was never touched. **Enrollment and consolidation are different measurements and only one of them is the goal.**

**Why:** moving a fact is a code change with a diff; declaring where the fact lives is prose with no diff discipline. The mover verifies the data landed — which it did — and the pointer is not part of what they tested.

**How to apply:**
- **When you move ownership of anything, grep for the OLD owner's name and repoint every declaration in the same commit.** Treat the ownership sentence as part of the migration payload, not documentation about it.
- **Suspect pointers that cite a ruling.** The citation is evidence the pointer was right *once*, which is exactly the condition under which nobody re-checks it. Ask "has the answer moved since this was ratified?" — not "was this correct?"
- **Read the whole file for a second ownership claim.** Docstrings and header comments contradict inline comments; the newest one is usually right and the loudest one is usually the header.
- **When a consolidation reports coverage, ask what the number counts.** Registered ≠ consolidated. Count rows where the fact actually moved, and separately enumerate the homes you did NOT touch — scope limits belong in the registry's self-description, or it over-claims.
- **A "single source of truth" header is an assertion that needs testing like any other.** If it says *every*, verify *every*.
- Related: [[finding_dead_path_regrows_unless_senders_repointed]] (senders keep a dead PATH alive; this is the same failure for a dead OWNERSHIP CLAIM), [[finding_governance_doc_stale_default_drift]], [[finding_retired_threshold_has_no_publisher]], [[finding_record_of_an_action_is_not_the_action]], [[finding_measure_actionable_not_gross_rate]], [[finding_banner_is_a_warning_not_a_fix]].
