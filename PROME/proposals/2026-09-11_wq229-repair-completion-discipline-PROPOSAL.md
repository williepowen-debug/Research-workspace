# WQ-229 PROPOSAL — repair-completion discipline (external review, CODEX, 2026-09-11)

**Status:** PROPOSAL, awaiting Will's word. **Raised by:** CODEX, after two rounds of audit on PROME's tools.
**PROME rec:** ADOPT. **Registered:** `PROME/WILL_QUEUE.md` WQ-229 before the ask, per the queue's own rule.

## What CODEX actually said, and why it is right

> "I'd change how PROME proves a fix, rather than add another checker or memory entry. It recognizes the failure
> pattern well; the weakness is turning that recognition into a complete implementation and a justified closure."

⛔ **The evidence is this session.** Presented with a defect class — a check that cannot see what it certifies —
PROME wrote **three auto-memory entries**, **registered a study**, and **routed a packet**. All defensible
individually. Collectively they are the *add-another-control* reflex CODEX diagnosed, applied to a session whose
actual lesson was that PROME's existing controls already promised more than they measured.

**The proof:** the root↔PROME `.claude/` parity check ALREADY EXISTED, already ran at boot AND closeout, and
would have caught tonight's agent-definition drift. It was `ADVISE`. It fired, and the drift shipped anyway.
Nothing needed inventing. `[[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]]`.

## The amendment (draft — for `PROME/CLAUDE.md` § Session Process Controls, ONE bullet, transplanted once)

> - **Repair-completion discipline (WQ-229, CODEX external review 2026-09-11):** for any fix to a check, gate,
>   instrument or tool, **write the ACCEPTANCE CONDITIONS before editing** — the properties the repair must
>   hold, in the defect's own terms, not a restatement of the reported symptom ("include pending files" was too
>   narrow; "every pending change in the intended closeout is visible, INCLUDING files already committed earlier
>   · unrelated work is excluded · the agent's own instructions request the right comparison" is the condition
>   set, and it is the test list). **Test the NEIGHBOURS, not just the reproduction** — five categories, every
>   time: **ordinary · overlap · wrong owner · missing information · concurrent activity** (the miss that kept
>   F1 open was an OVERLAP: a path both committed and pending). **A completion note distinguishes four states
>   and never merges them: IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED · STILL UNRESOLVED.** Passing the
>   author's own tests establishes *implemented*, never *verified* — `[[finding_adoption_is_not_validation]]`.
>   **A consequential repair goes to an independent reader BEFORE it is called fixed**, and that reader must
>   devise **at least one counterexample of its own** rather than re-running the author's suite. ⚠️ **Prefer
>   promoting or repairing an EXISTING control to adding a new one; a repeated defect earns a reusable test and
>   a mechanical guard, never another description of the pattern.**

## Standing instruction CODEX proposed for Will (verbatim, his to give or decline)

> "Before declaring a repair complete, show which acceptance conditions passed, what independent counterexample
> was tested, and what remains outside coverage."

**PROME rec: give it.** It is the operator-side half, and it costs Will one sentence per repair to enforce.

## What PROME has already done under it, before the word (mechanical only, no canon touched)

| Action | State |
|---|---|
| `.claude/{agents,skills}` parity gate `ADVISE` → **`BLOCK`** | IMPLEMENTED + **falsified** (induced drift ⇒ 🔴 fires; restored ⇒ ✅) — an existing control promoted, not a new one |
| Five-category neighbour table as a reusable test contract | IMPLEMENTED — `PROME/tools/tests/README.md` |
| F2/F3/F4 registered as dated work | DONE — DOCKET L335 |
| **A fourth auto-memory entry for this lesson** | ⛔ **DELIBERATELY NOT WRITTEN.** CODEX: *"Another memory entry has diminishing value."* Writing one would be the exact reflex under criticism. |

## Residue (declared, not fixed)

- `find_watermark()` still special-cases only a literal HEAD — documented in its docstring, open.
- CODEX point 4 (reduce dependence on interpretation: an explicit candidate change set and fixed baseline rather
  than reconstructing authorship from commit subjects and directory names) is **NOT implemented**. It is a
  redesign of the scope contract, not a patch, and it belongs in a bounded session with its acceptance
  conditions written first — which is the very discipline this proposal adopts. Rec: DOCKET it on the word.
