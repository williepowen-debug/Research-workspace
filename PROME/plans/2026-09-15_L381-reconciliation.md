# L381 bounded instruction reconciliation — plan

Will requested work on L381, L393 and L333 in this session. L381 authorizes reconciliation with NO change to authority. This plan covers L381 only; the two-session behavioral observation remains owed after implementation. No new scorecard, policy, authority tier or blocking check.

## Acceptance conditions

- Existing spawn grants, conditions, caps, roster restrictions and same-minute preflight still govern; no blanket wave approval is imposed and no permission is widened.
- Completion is compared against the original obligation, artifacts and owner-state write-back; source verification uses the bounded stopping condition recorded at DOCKET L381.
- WQ-249 remains the single rule for closeout-ask scope/outcomes. Idle/committed/clean is not substituted for an ask receipt.
- Updated decisions reach their owner and affected display sources/renders. Publication retains CLOSEOUT's verification/order/prerequisites and may remain explicitly incomplete.
- Existing delivery path/carve-outs and final desk closeout are not contradicted by the older spawn template.
- Keep all unrelated rules intact; update affected document stamps with this maintenance scope. Closeout runners already point to the edited manual step; confirm copy parity, with no gratuitous runner rewrite.
- Track implementation separately from observation in existing DOCKET L381; L378 mechanization is not discharged by prose edits.

## Exact proposed replacements

### 1. PROME/ORCHESTRATION_PLAYBOOK.md

Before:

```text
Get ONE launch approval for the whole wave — not per-agent drip.
```

After:

```text
Apply the existing grants, conditions, caps and preflight in `PROME/CLAUDE.md` § Ask First / Do Not Do Autonomously and § Session Process Controls; batch only approvals those rules actually require.
```

### 2. PROME/ORCHESTRATION_PLAYBOOK.md

Before:

```text
5. **Canon the same hour a verdict verifies** — HEARTBEAT amendment, DOCKET row, GATES.tsv state flip. Never batch canon to closeout; a crash loses it.
```

After:

```text
5. **Integrate the same hour a verdict verifies** — follow `PROME/COMPLETION_SPEC.md` § How Prome Uses This to update the affected owner records, including WILL_QUEUE when applicable. Carry changed decisions through the affected Helm/Deck sources and renders; publication and its prerequisites follow `PROME/CLOSEOUT.md` § The routine and § Delivery. Record incomplete publication explicitly. Do not defer verified owner-record updates to closeout; a crash loses them.
```

### 3. PROME/ORCHESTRATION_PLAYBOOK.md

Before:

```text
**no files outside `AGENTS/<NAME>/`**.
```

After:

```text
**path scope and self-authored delivery packets per root `CLAUDE.md` Git Protocol, including its existing carve-outs**.
```

### 4. PROME/ORCHESTRATION_PLAYBOOK.md

Before:

```text
5. Deliverables, exactly: files in own dir → **pathspec commit recipe from repo root** (incl. the pre-commit `git status -- AGENTS/<NAME>/` check) → do-not-push → **word-capped SendMessage summary (≤150-200 words)**.
```

After:

```text
5. Deliverables: artifacts and owner-state write-back → pathspec commits from repo root under root Git Protocol → delivery per `PROME/COMPLETION_SPEC.md`, with a **SendMessage summary ≤150–200 words**. The final touch runs the desk closeout specified in § Two-tier orchestrated-desk model; delivery alone does not establish closeout.
```

### 5. PROME/ORCHESTRATION_PLAYBOOK.md

Before:

```text
**PROME closeout hook:** before closing, send each live spawned desk the final run-your-closeout ping, then verify idle + last delivery committed (`PROME/CLOSEOUT.md` pre-closeout step).
```

After:

```text
**PROME closeout hook:** follow `PROME/CLOSEOUT.md` § Pre-closeout item 3; idle status and committed delivery do not establish that the closeout ask occurred.
```

### 6. PROME/COMPLETION_SPEC.md

Before:

```text
1. Read COMPLETION block from sub-agent output.
```

After:

```text
1. Compare the original task and its acceptance conditions with the delivered artifacts and owner-state write-back; use the COMPLETION block as an index, not proof. Distinguish assignment, delivery, integration and closeout. For repairs, apply `PROME/CLAUDE.md` § Session Process Controls (repair-completion discipline). When a claim changes a proposed capital action or the stated basis of an existing ruling, verify the decisive premise against source evidence, including instrument identity, comparison basis, and the calculation or inference connecting evidence to conclusion. PROME may obtain this verification from the responsible desk and inspect its evidence; repeating the entire research is unnecessary. If verification is unavailable, mark the premise unresolved and withhold dependent conclusions while unrelated work continues.
```

### 7. PROME/COMPLETION_SPEC.md

Before:

```text
3. If FOLLOW-UP is not "None" → capture the next action in the owner file (`PROME/SCRATCH.md` for immediate continuity, `PROME/STATUS.md` for work queue, or an agent inbox for routed domain work).
```

After:

```text
3. If FOLLOW-UP is not "None", reconcile it with the original obligation and register remaining work in its existing owner: DOCKET for dated obligations, GATES for gate state, WILL_QUEUE for Will-owned decisions, or the recipient inbox for routed domain work. SCRATCH carries the resume point and information registered nowhere else; STATUS may point to selected operational work. Do not restate registered obligations in either.
```

### 8. PROME/COMPLETION_SPEC.md

Before:

```text
4. If the work produced a system/process decision, log it in the appropriate live owner file. Trade/portfolio decisions go to FORGE/TERRY + broker truth *(the legacy `PROME/TRADE_DECISIONS.md` log was archived 2026-06-30)*; non-trade architecture/state decisions go to `PROME/STATUS.md`/`PROME/HANDOFF.md` as appropriate.
```

After:

```text
4. Integrate verified changes into the owner records specified by `PROME/CLOSEOUT.md` § Boot↔Closeout symmetry — ONE HOME PER FACT. Trade/portfolio records remain FORGE/TERRY with broker/Will truth off-repo; Will's rulings belong in WILL_QUEUE. Update affected Helm/Deck sources and renders; follow CLOSEOUT's generation, verification and publication order, and report publication that remains incomplete. HANDOFF navigates to these records; it does not duplicate the decision.
```

### 9. PROME/CLOSEOUT.md

Before:

```text
3. **Orchestrated-desk release (ANY tier):** tell each named desk spawned this session to run its own closeout; verify idle + last delivery committed (desk `(orch)` commits). Desk-dir residue is in-flight; never sweep it on respawn. Log final touch in `PROME/state/ORCH_LOG.tsv`. Single home: `PROME/ORCHESTRATION_PLAYBOOK.md` §Two-tier.
```

After:

```text
3. **Orchestrated-desk release (ANY tier):** enumerate and disposition the desk touches required by `PROME/CLAUDE.md` § Session Process Controls, Spawn-closeout discipline (WQ-249), including its scope and four reported outcomes. Record the closeout ask and answer, or that the desk went dark before the ask, in `PROME/state/ORCH_LOG.tsv` before the closeout commit. Idle status and committed delivery are supporting evidence, not proof of the ask. Desk-dir residue is in-flight; never sweep it on respawn. Desk lifecycle: `PROME/ORCHESTRATION_PLAYBOOK.md` § Two-tier orchestrated-desk model.
```

## Verification and remaining work

Independent plan read before editing, then independent result read. Check each substitution, existing grants, the runner/manual route and Git diff. No operational boot or desk spawn is needed to test these text changes. Observe two ordinary completed orchestration sessions using existing task/ORCH_LOG and artifact evidence; do not count this editorial session. Result cannot be called behaviorally proven before that observation.

## Independent plan review and declared residue — 2026-09-15

Reader `l381_plan` found one blocker: “this session” narrowed WQ-249’s day-based enumeration across a restart. Proposed replacement 9 now defers the selector entirely to WQ-249. Independent counterexample: a morning HENRY touch remains owed after an afternoon restart.

Warnings retained under WQ-178: the existing playbook Model tiering Git bullet still carries older own-directory/sweep wording; COMPLETION_SPEC’s Purpose still foregrounds SCRATCH/STATUS and avoiding full-output parsing. This bounded reconciliation does not certify every instruction in these files.

## Independent result receipt — 2026-09-15

Reader `l381_result`: no blockers, no additional warnings. Verified grants/caps/preflight, exact source-check stopping condition, WQ-249 scope/outcomes, publication prerequisites and runner/manual route. Independent counterexamples: a fifth due-row launch still exceeds the cap; clean idle delivery still lacks an ask; unavailable publication remains incomplete; unresolved source evidence withholds dependent conclusions only. The two plan warnings remain declared residue.

Checks: both closeout runner copies byte-identical via measure.py; Git diff whitespace check passed. Instruction implementation is independently source-verified. Two ordinary-session observations are STILL UNRESOLVED; this editorial session does not count.
