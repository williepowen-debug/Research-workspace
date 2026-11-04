# L910 — CLOSEOUT hot/cold rotation plan

**Date:** 2026-11-04. **Owner:** PROME. **Scope:** existing CLOSEOUT rotation only; no new procedure, rule, checker or authority change. **Review:** one independent read-only plan review before editing and one result review after editing, under the existing review budget.

## Current defect

`PROME/CLOSEOUT.md` has regrown beyond its read cap and rotation trigger. `test_closeout_simplification_WQ240.py` carries the registered expected failure. The rotation must finish below 22,785 B (70% of the 32,550 B budget), not merely clear the test's 24,412 B assertion.

## Exact moves

1. In `PROME/CLOSEOUT.md` step 8, move the detailed paragraphs beginning:
   - `**ARGUS cadence`
   - `Concurrent closeouts first follow`
   - `Legacy (schema-1) manifests`
   - `**Live-fleet rule`
   
   into `PROME/CLOSEOUT_PROCEDURES.md` under a new section `## Audit contract details (trigger: Standard/Heavy closeout)`.
2. In step 10, move the detailed paragraphs beginning `⚠️ **Post-freeze foreign arrivals` and `**WQ-583` into that cold section under `### Delivery verification details`.
3. Additionally move:
   - Pre-closeout step 3's paragraph beginning `3. **Orchestrated-desk release` into the cold section under `### Spawn-closeout release`; the hot step retains the actual-closeout/checkpoint distinction, the closeout ask/answer obligation and the ORCH writer command;
   - the step-6 paragraph beginning `6. **Root session-end steps 1b–1e**` into the cold section under `### Root session-end checks`; the hot step retains the root-step references and a pointer to the exact commands;
   - the step-7 paragraph beginning `7. **ALL generation for active surfaces.` into the cold section under `### Generation and deterministic checks`; the hot step retains the full table/done-row/WQ/ORCH command list and the generation-before-freeze order;
   - the step-9 paragraph beginning `At **standard/heavy**` into the cold section under `### Final gate rules`; the hot command block and a pointer remain;
   - the complete step-11 paragraph beginning `11. **Publish the verified artifacts**` into the cold section under `### Publication rule`; the hot step retains the active-deliverable precondition and Helm/Deck state plus a pointer.
4. Preserve in the hot file: the numbered routine, freeze/audit ordering, exact command forms, mark-reviewed distinction, commit→verify→push order, the prohibition on wrapper `--push`, and the verbatim push receipt. Retain the full `python3 PROME/tools/inbox_census.py PROME`, `--record-review --contract /tmp/prome-delivery-plan.json`, `--mark-reviewed "<one line>"` and `--observe /tmp/prome-observed.json` forms, plus the literal `commit_check.py commit --stage -F <msgfile> -- <exact paths>`. Retain the test anchors `LAST step that may` / `ALL generation` / `Renders are NOT read-only` / `Publish the verified artifacts` / `Unmet owed publication for a separately requested active deliverable is reported, never waived`. Replace moved paragraphs with short pointers, not a second copy of their rules. Add `Audit contract details` to the hot conditional-procedures inventory.
5. Update CLOSEOUT's stamp to this rotation and preserve the prior stamp pointer/history. Update the cold file's header to name the new routine-triggered section. Remove the test's expected-failure marker and update its comment only when its actual size assertion passes.
6. Before any source edit, construct the projected file with the exact replacement text and measure it with `PROME/tools/measure.py`; record the result below. After the edit, measure both files again. If CLOSEOUT is at/above 22,785 B, STOP and revise/re-review the plan; no additional unnamed move is authorized. The completed-rotation target remains 22,785 B regardless of the weaker test assertion.
7. Run the closeout tests and relevant structural checks. Preserve every duty and citation in the moved text. No content deletion other than the hot-file duplicate, no root edit, no owner edit, no trade or strategy change.

## Measured projection

`PROME/tools/measure.py /tmp/CLOSEOUT_L910_projected.md` → **22,169 B**, below the 22,785 B completion target. This projection includes every named paragraph move, the updated header, the cold-section inventory entry, and the required command/test anchors; it is not a bare-deletion estimate. No source edit has occurred.

## Invariants / acceptance

- Every moved paragraph is preserved verbatim and remains reachable by an explicit hot-file pointer.
- The hot routine still names the correct execution order and required commands; the cold file is not treated as an optional/no-trigger document.
- CLOSEOUT is below 22,785 B; `test_closeout_simplification_WQ240.py` passes without an expected-failure marker.
- Existing closeout/ARGUS tests and table/claim checks pass; live links remain valid.
- Independent result review follows the moved pointers, checks one rotated-content recovery and one execution-order recovery, and reports any unresolved consequence. Author tests alone do not close L910.

## Neighbours considered

- **Ordinary:** routine closeout retains its executable order.
- **Overlap:** L835's live-fleet paragraph moves verbatim without changing its pending/accepted status.
- **Wrong owner:** only PROME-owned CLOSEOUT/CLOSEOUT_PROCEDURES/test/plan files change.
- **Missing information:** no rule is paraphrased or dropped to meet size; measurement is by measure.py.
- **Concurrent activity:** exact scoped commits only; no foreign files staged.

## Crash recovery — 2026-11-04, Codex

The three independent plan responses were NOT ACCEPTED. The last response found missing cold-section inventory entries and unmatched Markdown markers. Kimi corrected both in its final temporary projection after that response; those corrections have no further independent verdict. Three completed reads exhaust the ordinary episode allowance. No rotation is installed; no further reader is launched under the general catch-up approval.

The exact saved hot draft and the now-prepared cold companion are in `PROME/reports/2026-11-04_kimi-maintenance-recovery/`, with a source/move manifest. All eleven selected paragraphs are preserved verbatim in the cold candidate. The final hot draft differs from the earlier measured projection; use `measure.py` on the saved candidate rather than the superseded figure above. The existing two closeout suites pass against the draft pair, with the size expected-failure disabled only in the temporary test process. Live manuals and the live test marker are unchanged by this recovery.

Implementation remains WITHHELD pending WQ-597: one further plan review and, only after a clean plan and installation, one result/execution review. Stop on a blocking verdict; no open-ended review loop. Original responses, failed results and operator instructions are preserved in the recovery directory.

## WQ-597 approved continuation — 2026-11-04

User approved the named further plan and result/execution reads. Read 4: Codex gpt-6.1-sol `/root/l910_plan`, ACCEPTED the exact saved candidate pair; 11 verbatim moves and 51 overlay tests checked, navigation and two execution scenarios independently exercised. Installed exact pair and removed the obsolete expected-failure marker. Result/execution review PENDING; earlier review history above remains history. Full receipts: `PROME/reports/2026-11-04_approved-maintenance-reviews.md`.

Result/execution read 5 (second named WQ-597 further read), Codex gpt-6.1-sol `/root/maintenance_result`: ACCEPTED. Installed bytes equal saved pair; all 11 manifest hashes preserved; 51 live tests pass without expected-failure; navigation plus rotated-content and execution-order recovery verified. Reviewer devised a Light-tier skip counterexample and found the hot mandatory pointers reject it. L835 remains NOT ACCEPTED; rotation supplies no acceptance of that repair. Explicit closeout receipt held.
