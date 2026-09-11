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

---

## DECLARED RESIDUE — independent review, 2026-09-11 ~19:0x ET

The independent reader (counterexample mandate, throwaway fixtures, `5ac1d4f28`) returned **2 ❌ and 6 ⚠️**
after the author's 20 tests passed. ⭐ **This is the case FOR the discipline, not a footnote to it:** both ❌ are
**live-reachable on this repository's own graph**, and both were invisible to the author's suite because the
suite tested the reported reproduction rather than its neighbours.

**FIXED (❌ only, per the read-budget rule):**
- **F-1 — the watermark could be a commit that is not a closeout.** `(?:\w+\s+)?closeout\b` matched
  `00afa8b99 "PROME: CLOSEOUT symmetry table — …"`. Measured on the real graph: true scope 37 commits / 63
  paths, tool-picked scope 26 / 34 — **11 commits and 29 paths silently dropped**, including `HEARTBEAT.md` and
  three outbound packets; the fixture flipped to `SKIP` so ARGUS would not have spawned at all. The author's
  test checked a `closeout` mention at the END of a subject, never at token 1.
- **F-2 — a recipient consuming a PROME packet was claimed as PROME authorship.** `.*from-PROME` crossed the
  `processed/` segment; 16 live commits claimed, ≥3 another desk's (`ef3a11436`, `15312dc7d` LABOR consuming;
  `08fa7a7b9`). The consume-move is a constant fleet shape, not a corner. Anchored to the inbox top level.
- 5 regression tests added (20 → 25). Both fixes verified against the actual false-positive strings.

**NOT FIXED — declared residue, ranked by reachability:**

| # | Finding | Reachability | Why deferred |
|---|---|---|---|
| F-5 | `memory/YYYY-MM-DD.md` claimed by FILENAME PATTERN — the exact thing condition 3 forbids for shared dirs; another desk's pending edit to the daily note is claimed | **LIVE** (desk-prefixed subjects touch `memory/20*.md`) | correctness fix, but it is a PERIMETER redesign and belongs with CODEX point 4 |
| F-4 | a PROME pending artifact in another desk's inbox without `from-PROME` in its name is silently dropped — incl. the ratified `MSG-*.md` coded route, which can never contain it | **LIVE** | same redesign; the silent-drop direction is the wrong one and it is the first thing point 4 must fix |
| F-6 | one `[PENDING]` token for three prescribed reads; no per-path porcelain state in `--json`; deleted-file case absent from both `argus.md` copies | LIVE, low harm | needs a matched change in both agent copies |
| F-3 | non-ASCII path: `git show --name-only` C-quotes, `status -z` does not ⇒ OVERLAP guard misses, threshold over-counts, prescribed read returns 0 bytes | **LATENT — 0 non-ASCII tracked paths today** | one-flag fix (`-c core.quotePath=false`), but it is a ⚠️ and the rule is fix-❌-only |
| F-7 | pending `git mv` of a PROME file OUT of the perimeter hides the origin's disappearance | low | fix is "keep the origin when owned and destination is not" |
| F-8 | gitignored PROME output invisible | n/a by design | wants one docstring sentence |

**Outside anyone's coverage, stated so it is not mistaken for tested:** runtime precedence between the two
`argus.md` copies; ARGUS's own behaviour given a correct scope; the declared-OPEN intervening-domain-commit
limit; the `MAX_LOOKBACK` boundary; and the tool's two non-atomic snapshots (`git status` then `git show`) under
a concurrent second session.

## ⛔ STATUS OF F1 AFTER INDEPENDENT REVIEW

**IMPLEMENTED** · **TESTED** (25) · **NOT INDEPENDENTLY VERIFIED** — the reviewer's verdict was *"IMPLEMENTED,
not VERIFIED"*, and the two ❌ it found have since been changed, so **the reviewed candidate is no longer the
current one.** A second independent pass is required before anyone calls F1 fixed. PROME does not claim it.

---

## ⛔ CORRECTION — F1 IS OPEN ON A CONTRACT VIOLATION, NOT MERELY UNVERIFIED (external review, 19:0x ET)

> "A known violation of an acceptance condition remains a blocker, even if the reviewer labels it ⚠️. Silently
> excluding legitimate PROME messages and claiming another agent's edits violate the scope contract. Calling
> them 'lesser findings' doesn't reduce their effect."

**This is the correction that matters most tonight, and the error is mine, not the reviewer's.** The reviewer
graded severity; **the acceptance conditions are MINE and they are the contract.** I let an external severity
label override my own stated conditions, then wrote "six lesser findings" over two known contract violations.
That is `[[finding_a_flag_resolved_in_the_wrong_direction_launders_the_defect]]` — the detector fired correctly
and the defect shipped anyway, with the flag now serving as evidence it was considered.

**The two BLOCKERS, restated against the conditions they actually break:**

| Was | Is | Condition broken |
|---|---|---|
| F-4 ⚠️ | 🔴 **BLOCKER** — a PROME pending artifact in another desk's inbox lacking `from-PROME` in its filename is SILENTLY DROPPED. Includes the ratified `MSG-*.md` coded route (root `CLAUDE.md`, Direct Messaging v1), which **can never contain that string**. | **Condition 1** — "every pending change in the intended closeout is visible." |
| F-5 ⚠️ | 🔴 **BLOCKER** — `memory/YYYY-MM-DD.md` is claimed by FILENAME PATTERN, so another desk's pending edit to the shared daily note enters PROME's audit scope. | **Condition 2** — "unrelated work is excluded"; and it is the precise practice **Condition 3** forbids for shared directories. |

⇒ **F1 STATUS: OPEN.** Not "implemented, awaiting verification." OPEN, on two known violations of its own
acceptance conditions. Either they are resolved, or Will approves a NARROWER contract with the limitation
written into it — an option, but his to take, not PROME's to assume by relabelling.

**STOPPING RATHER THAN PATCHING, deliberately.** The correction limit exists to stop a session, not to lower a
standard. `argus_scope.py` has taken four correction passes tonight; a fifth at 19:0x, against a contract that
is itself being redesigned, is how the next defect enters. **The sound outcome is "stop tonight, resume with
these blockers named,"** and that is what this is. `[[finding_a_correction_pass_is_unreviewed_work]]`.

**ONE MORE OWED THING, and it is a real gap in what I shipped:** the five new tests pin the reviewer's
discoveries as STRINGS (`"PROME: CLOSEOUT symmetry table…"`, a `processed/` path). That preserves the finding
and does **not** test the PROPERTY — *a subject ABOUT closeout is never a watermark*; *consumption is never
authorship*. String tests pass while the next unseen instance of the same property walks through. Property
tests are owed with the redesign, not instead of it.

## ⭐ THE PATTERN THE REVIEWER NAMED, which is the actual finding of the whole evening

> "The recurring failures now cluster around inferring ownership and audit boundaries from filenames and prose.
> That is evidence about the design, not merely missing regex cases."

Every defect in this tool — F1's watermark, F2's `processed/` crossing, F-4's filename key, F-5's date pattern,
the lineage-inference caveat — is the SAME design choice: **authorship and boundaries RECONSTRUCTED from commit
subjects and file names rather than recorded.** Four regex repairs have not changed that, and a fifth will not.
This is why the next session is a redesign and not another patch.
