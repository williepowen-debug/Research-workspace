# L511 — REVIEW BUDGET: one rule for WQ-165 · WQ-178's third read · WQ-299 R2 · the two-correction stop — RULED 2026-09-26 20:03 ET

**Owner:** PROME · **Session:** PROME boot session after `prome-1d` (directed PROME review, Will present) · **DOCKET:** L511 item ① (item ② rotation shortfall unaffected)
**Class under WQ-299 R1:** PROCESS — this session's one process change, on Will's direction.

## Will's ruling (verbatim, 2026-09-26 20:03 ET, pasted in-session)

> Approved with these amendments:
>
> 1. Withholding follows consequence, not defect class. Any unresolved defect that could materially change a decision or instruction must be withheld, including a consequential basis or pointer error. This applies at early stop as well as the ceiling. If no reliable source or prior version exists, mark the guidance unavailable; don't point readers to a known-bad version.
>
> 2. Finish the runner alignment. Remove step 2's remaining permission to fix any warning that takes one line. Apply WQ-178's warning-as-residue rule and its existing one-word-typo exception.
> 3. Approve the procedure execution exception and put it in the canonical Review budget. The runner should point there. It occupies the third read within the ceiling. A clean text review does not establish executability or cancel a required execution check. An unperformed required check remains explicitly pending and unverified.
>
> 4. Record the actual review history before implementation. Save the dated ruling and carry forward the applicable reads already performed, including CATO's scoped proposal reviews. Approval does not reset the count. If the remaining budget cannot accommodate the independent result review and required read-only execution check for this L511 change, I explicitly authorize those named checks for this implementation only.
>
> Implement this once, complete the applicable checks, report the disposition and delivery, then stop. No further general proposal round.

Earlier words on this episode: Will 19:17 ET directed the bounded review ("Start with the review-limit conflict at L511 … No implementation, new tool, additional desk wake or general audit yet"). He then relayed CATO's review of candidate v1 and CATO's assessment of candidate v2.

## Review history of this episode (carried forward; approval does not reset it)

| # | Read | Object | Result | Evidence |
|---|---|---|---|---|
| 1 | CATO, scoped independent plan review | candidate v1 (PROME in-session 19:3x ET) | Approve consolidation with one bounded revision: the continuity exception ships actionable errors; WQ-178's narrower limits and the UNKNOWN rule omitted; new-state exception too broad; runner only partly aligned; PROME's review-history claim false | `983e1aafa` (19:23 ET) |
| 2 | CATO, scoped independent plan review | candidate v2 (PROME in-session 19:5x ET) | Withholding must follow consequence (WR23 remainder); step 2 one-line-⚠️ permission remains (WR26); procedure exception recommended, with its home in canon | `ca93d5f14` (20:01 ET) |
| 3 | Independent result review (coldreader, opus) | implemented texts A–D | see § Result below | ORCH_LOG row at spawn |
| 4 | Read-only execution check (general-purpose stranger, opus) of `/coldread` | runner as written | see § Result below | ORCH_LOG row at spawn |

**Budget arithmetic.**
- Reads 1–2 used two of three slots.
- Read 3 (the result review) is the last in-ceiling slot, so the procedure exception cannot also give the execution check that slot.
- Read 4 therefore runs **only under Will's named authorization** (amendment 4: "for this implementation only"), not under the exception.
- No further read is authorized.

## Final candidate as ruled — the texts transplanted once

**A. `PROME/CLAUDE.md` § Session Process Controls:** replaces the whole "Two-correction stop:" bullet, in the same position. Text: the bullet recorded in the commit's diff (source = this record's § A-text below).

**B. `PROME/CLAUDE.md` WQ-178 "Read budget" bullet:**
- **Delete** from "**A THIRD read is allowed once…**" through the end of the "**Repair-episode cap (WQ-299 R2 …)** …" passage ("…a new episode."). The origin note inside that span is kept.
- **Replace with:** "The third read, the episode ceiling, withholding at the limit and the correction count → the **Review budget** bullet in this section. *(Origin: 9/4 — …)* **(WQ-299 R2)** An externally blocked repair is recorded as blocked in the closeout report — it neither disappears nor becomes a standing prohibition on necessary maintenance."

**C. `PROME/CLOSEOUT_PROCEDURES.md` § Byte-flow blind-reader bullet:** the "**Stop rule (WQ-165):** …ship." sentence is replaced by the "**Stop and budget:** …" sentence (§ C-text). The class definitions and the Runner pointer stay.

**D. `/coldread`, both copies (root `.claude/skills/coldread/SKILL.md` and `PROME/.claude/skills/coldread/SKILL.md`):**
- description → "re-runs within `PROME/CLAUDE.md` § Review budget (WQ-165's early stop inside it)";
- step 2 → ❌ fixed within the budget or withheld; ⚠️ declared as residue (WQ-178) unless the fix is a one-word typo (the one-line-⚠️ permission removed);
- step 4 → re-run only while the budget allows; rules → the canon bullet; class definitions → CLOSEOUT_PROCEDURES;
- step 5 → the execution pass counts inside the budget, with a pointer to the canon bullet's procedure exception;
- steps 1, 3 and 6 unchanged.

**Amendment 1 is applied in A** (Disposition) and **in C**. **Amendment 2** is in D step 2. **Amendment 3** is in A (Procedure exception) and D step 5 (pointer only).

## The three cases (as ruled)

- **Resolved defect.** Plan read, then result read with ❌ = 0 ⇒ INDEPENDENTLY VERIFIED.
- **Unresolved consequential defect at an early stop or the limit.** It is withheld: a pointer to its source and last reliable version, or marked UNAVAILABLE. Yesterday's "next process slot" claim becomes *"governed by R1 (`PROME/CLAUDE.md`); no date asserted."*
- **New defect, same file.** A sourced receipt ("routing PENDING until a WALTER commit evidences it") goes in without a read. A materially different defect is a new episode. The same defect found again stays in its episode, with its count carried.

## Queue registration

Not registered as a WILL_QUEUE row. The boot gate showed rows more than 7 days past needed-by (WQ-187, WQ-204), so WQ-299 R4 requires a triage table before any new row is registered this session. This record + DOCKET L511 are the decision's homes.

## § A-text (verbatim, transplanted once)

- **Review budget (L511, Will-ruled 2026-09-26 20:03 ET; consolidates WQ-165 · WQ-178's third-read clause · WQ-299 R2 · the WQ-140 two-correction stop; record `PROME/proposals/2026-09-26_L511-review-budget-RULED.md`):** **Episode** — one change to one artifact (a repair, a canon edit, a rotation, an archival split), first edit to disposition; a read spanning several artifacts counts once in each; a new session, a renamed defect or a new label never resets an episode's count, and approval does not reset it; a later, materially different defect is a new episode. **Reads** — WQ-178 governs its classes: one plan read, one result read, and a third ONLY when a ❌ fix on the result changed a rule's meaning, for rotations and archival splits as for canon; a byte count, a stamp or a pointer form never earns a read. Three independent reads per episode is the outer ceiling, never an allowance; parallel readers each count; Will may authorize a named further read. Missing read history is UNKNOWN: a baseline read of the acceptance file (`reads:` line, `PROME/tools/tests/README.md`) precedes any further round, and a count is never invented. **Procedure exception** — on a procedure file (a manual, runner or skill executed as written), a required read-only execution check may occupy the third read within the ceiling without a rule-meaning fix — never a fourth, never an automatic third on other work. A clean text review does not establish executability or cancel a required execution check; an unperformed required check stays explicitly PENDING · UNVERIFIED and disclosed, and any further read needs Will's named authorization. **Early stop (WQ-165's test, inside the budget)** — stop at ❌ = 0, or after two consecutive reads whose ❌ are all basis/pointer class; an action-class ❌ forces another read only while the budget allows one, and past that point forces a disposition, never an extra read. **Disposition (WQ-229 states)** — a fix made after the final read is unreviewed and never INDEPENDENTLY VERIFIED. **Withholding follows consequence, not defect class:** any unresolved defect that could materially change a decision or instruction — a consequential basis or pointer error included — is WITHHELD from operational use, at an early stop as at the ceiling, whatever the file: the claim or instruction is replaced by a pointer to its authoritative source and last reliable version (a commit); where no reliable source or prior version exists it is marked UNAVAILABLE — do not act, never pointed at a known-bad version. Evidence stays in git and required archives; the defect goes into the closeout report and a DOCKET row; a tool or gate is withdrawn or disabled (R2). A STILL UNRESOLVED label beside a live instruction does not satisfy this. **Corrections (the two-correction stop)** — two correction passes on one file in a session (a pass = one sitting's fixes, committed or not) ⇒ any further correction to that file needs an independent read, counted inside its episode's budget — `[[finding_a_correction_pass_is_unreviewed_work]]`. A **sourced receipt** — a dated fact with its source that changes no existing claim or instruction (e.g. *"onward routing PENDING until a WALTER commit evidences it"*) — is not a correction and needs no read beyond the closeout's own; an addition that approves, changes a quantity, re-grades or claims completion alters the instruction it touches, even appended, and needs that change's applicable review.

## § B-text

The third read, the episode ceiling, withholding at the limit and the correction count → the **Review budget** bullet in this section. *(Origin: 9/4 — five reads on one README, three on one canon bullet; each tidy pass generated the next pass's flags.)* **(WQ-299 R2)** An externally blocked repair is recorded as blocked in the closeout report — it neither disappears nor becomes a standing prohibition on necessary maintenance.

## § C-text

**Stop and budget:** a rotation or re-base is one episode under `PROME/CLAUDE.md` § Session Process Controls → Review budget — WQ-165's early stop runs inside WQ-178's reads; at an early stop or at the limit, any unresolved defect that could materially change a decision or instruction is withheld per that bullet (pointer to source + last reliable version, or UNAVAILABLE), never shipped as live guidance; declare ⚠️ and unreviewed fixes as residue in the commit.

## Result (reads 3–4) and episode disposition — 2026-09-26 20:1x ET

**Read 3 — result review** (coldreader, opus, blind; the last in-ceiling slot). Score: 17/28 ✅ · 10 ⚠️ · 1 ❌. Verdict *"no"*.
- **Canon:** complete. All four amendments are in `PROME/CLAUDE.md` § Review budget. No stale stop rule, one-line-⚠️ permission or "re-run until" wording is live anywhere; 13/13 pointers resolve.
- **❌14:** the runner's step 2 and CLOSEOUT_PROCEDURES routed every ⚠️ to residue by grade. A decision-changing basis error that a reader grades ⚠️ would therefore ship live, against amendment 1.

**Read 4 — read-only execution** of `/coldread` (general-purpose, opus; Will-authorized by name). 4 of 6 steps PASS. Findings:
- step 4's "SCRATCH executed-list" is a dead pointer;
- step 5's "AFTER ❌ = 0" precondition could keep a required execution check from ever running under the procedure exception;
- the reader type and brief for rotations are inconsistent (runner: `coldreader` + claims; Byte-flow: Explore + ground-truth questions);
- ⚠️ residue location is inconsistent (the artifact per WQ-178, the commit per Byte-flow);
- the rotation plan read is required by canon but absent from the recipe;
- no literal template exists for a withheld or UNAVAILABLE line;
- the step-5 spawn doesn't say opus.

**Post-read edits (one edit per file, after the final read, therefore UNREVIEWED).** Each applies the canon's own consequence rule:
- `/coldread` step 2 (both copies): *"but a ⚠️ or ❌ that could materially change a decision or instruction is withheld whatever its grade"*, with a pointer to § Review budget.
- `/coldread` step 4: the dead "SCRATCH executed-list" target removed.
- `/coldread` step 5: the precondition now reads *"after the reading passes — at ❌ = 0, or in the third read under the procedure exception, whichever comes first"*.
- `CLOSEOUT_PROCEDURES.md:14`: the same consequence exception on its residue clause.
- **No further edit to `PROME/CLAUDE.md`.**

**Disposition (WQ-229 states):**

| Part | State |
|---|---|
| Canon bullet + WQ-178 bullet edit | IMPLEMENTED · TESTED (execution check ran) · INDEPENDENTLY VERIFIED-WITH-RESIDUE (read 3: canon complete, no ❌ in the canon text) |
| Runner + CLOSEOUT_PROCEDURES post-read edits | IMPLEMENTED · **NOT independently verified** (made after the final read) · STILL UNRESOLVED as to review |

Each post-read edit narrows toward the canon text that read 3 verified, so none creates a new operational instruction beyond it. No further read is authorized; the episode is closed.

**Declared residue (⚠️, left by name — none worked this episode):**
1. "sitting" vs "session" in the Corrections clause; the dropped "typo fixes count" and "each ❌-fix pass counts" (read 3 ⚠️15).
2. "while the budget allows one": the ceiling vs WQ-178's conditional third read (⚠️16).
3. Whether a consequential fix made after the final read is shipped or withheld beyond the withholding clause (⚠️17).
4. When an execution check is "required" is defined only in the runner (⚠️19).
5. "Last reliable version" for a newly ruled canon bullet (⚠️20, CE4).
6. The rotation plan read is required by canon but absent from the Byte-flow recipe and the runner (⚠️21, exec #4).
7. This episode ran two plan reads — CATO on v1 and on v2, on Will's direction — against "one plan read" (⚠️22).
8. `PROME/tools/tests/README.md:43-51` restates WQ-299 R2 as a second home (⚠️23).
9. The review owed for an appended approval or quantity change outside WQ-178's classes is undefined (⚠️28).
10. The reader type and brief for rotations are inconsistent (exec #1).
11. ⚠️ residue location — artifact vs commit (exec #2).
12. No literal template for a withheld or UNAVAILABLE line (exec #5).
13. The step-5 spawn doesn't name opus (exec Q5).

Full reader ledger: session scratchpad `l511result.md` (session-local; this section is the durable summary).

## Acceptance (Will, verbatim, 2026-09-26 20:16 ET, pasted in-session)

> Accept the delivery and stop this review episode. No fifth read or further repair round.
>
> Preserve the separate dispositions:
>
> - Canon: independently verified with the declared residue.
> - Runner and closeout changes after the final read: implemented, independently unverified.
> - Required execution validation: incomplete; four of six steps passed on the version checked.
>
> Withhold the affected unverified guidance from operational use and use the verified canonical rule as the governing reference. Carry that limitation and the incomplete execution check in the next authorized continuity write. L511① may be marked implemented, but must not imply the whole procedure is verified or executable.
>
> At the next rotation, the canonical requirement for a plan read still applies even though the closeout recipe omits it. Declaring that omission as a warning does not waive the requirement.
>
> No new process project follows from the remaining residue.

**Applied 20:1x ET:**
- ⛔ WITHHELD markers added at the top of `/coldread` (both copies, identical) and on the "Stop and budget" sentence in `CLOSEOUT_PROCEDURES.md:14`. Each points to `PROME/CLAUDE.md` § Review budget as the governing rule.
- The withheld wording is left in place, marked. It is neither deleted nor re-worked, per "no further repair round".
- DOCKET L511 ① now reads IMPLEMENTED, with the three dispositions kept separate, the carry obligation and the plan-read requirement.

**Carried to the next authorized continuity write (SCRATCH/STATUS at closeout):**
- the withholding and the incomplete execution check;
- the plan-read requirement at the next rotation.

The episode is CLOSED.
