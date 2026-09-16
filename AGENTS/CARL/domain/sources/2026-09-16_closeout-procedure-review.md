# CARL closeout procedure review — September 16

**Verdict:** the core write-back sequence is sound; the procedure had concrete stale references and missing execution cues. Corrected those within CARL's scope. This does not retroactively complete the prior partial closeout or erase its housekeeping debt.

## Evidence and corrections

| Finding | Evidence | Correction |
|---|---|---|
| Ambiguous root/local push path; local helper lacks verified remote receipt | CARL local script ended in a bare `Pushed.`; root script performs post-push fetch and ancestry check. DAEDALUS September12 packet had already identified the defect. | Replace local implementation with a delegate to root; preserve arguments, cwd and exit code. Charter explicitly invokes root script and root non-ff recovery rules. |
| WQ-227 approved assertion absent from closeout steps | September11 approval packet says add the card line; `board_gap.py --closeout` already implements it. | Wire existing command and actual-output receipt into step13d; no new approval requested. Cursor/receipt coverage is not substantive review or whole backlog count. |
| Wrong prediction mirror in check instructions | Step15 still pointed at STATUS; checker and Doc Ownership use PREDICTIONS_MIRROR. | Correct path; keep hard consistency gate unchanged. |
| Retirement shorthand drops root exceptions | Local step13c omitted pending-event exemption and index-only reference rule. | Point to canonical root rule and spell out those safeguards; incomplete reference review cannot be called complete. |
| Line cap can pass while memory exceeds byte budget | Local100-line rule versus root32550-byte whole-read budget; existing MEMORY breach. | Make both visible and include root read-cap check. No higher cap or exemption introduced. |
| Root conditional checks easily omitted | Local Git shorthand did not enumerate consumer/orphan/weekday/ledger/auto-memory checks. | Add executable checklist with applicability and evidence, preserving root authority and authored scope. |
| Handoff template stale | “awaiting HERMES”; all old TSVs called stale; every present inbox item called unprocessed; past event would disappear under literal future-date rule. | WALTER/current authority routing, explicit delivery/disposition, frozen/reference distinction, dated next action for an unreviewed past event. |
| Partial event could be pruned too early | “data integrated” allowed statement-only processing to remove a multi-part event. | Prune when fully integrated/graded; retain remaining component and review date. BRENT already clearly distinguishes expired date from completed grade. |
| No honest completion summary | Git success and one checker could stand in for the entire procedure. | Template receipt separates checks, conditional duties, approval continuity and remote delivery. Mandatory failures/unperformed duties mean partial closeout, even after successful push. |
| Harness assumptions | Memory promotion points only to Claude alias and assumes automatic loading. | Name repository memory store and root handling; Codex must explicitly read memory and disclose unavailable capabilities. |

## Comparison with other desks

- **PROME/CLOSEOUT.md:** good separation of pre-closeout scope, conditional work, mandatory checks and publication. It explicitly distinguishes incomplete checks from failures and says foreign dirty work need not block scoped commits/push. PROME has approved tiers; those are **not copied into CARL**, whose every-session requirements remain in force.
- **AGENTS/BRENT/CLAUDE.md:** useful distinction between an expired event date and a graded event, and between inbox triage and deep processing. CARL's partial-event wording now makes that distinction explicit without adopting BRENT's different retention window or generated-calendar architecture.
- **AGENTS/SAM/CLAUDE.md:** same useful final-brief ordering, but also old HERMES and abbreviated non-ff wording. It is a comparator, not a source to copy over root rules.
- **AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md:** actual header stamp and reference to current STATUS commit matter; appending a timestamp elsewhere does not refresh the header. Existing brief obligation retained; no new NEXUS policy or gate created.

## Correction to the operator-facing assessment

The previous answer was too broad when it treated pending research and all remaining inbox items as closeout failures. A research backlog may remain if disposition and next action are clear. A consumed delivery copy still requires filing under the existing rule; presence alone does not prove it was consumed. Likewise unavailable native messaging is not evidence that a packet was delivered, and the reviewed session did not establish a complete dispatch audit. Do not claim either full routing completion or an exhaustive list of missed mandatory sends without that assessment.

Actual execution omissions remain: retirement review unfinished, MEMORY over budget, other surfaces above the rotation target, incomplete template compliance, and the closeout-only turn appended a timestamp without refreshing the brief header. Successful commits/pushes were real; “full closeout complete” was not supported.

## Validation and remaining scope

- `bash -n` passes for push delegate. Nine isolated checks in a temporary repository (including a path with spaces) cover calls from root, CARL and unrelated cwd, exact argument forwarding and exit0/1/2 propagation. No live push was used as the regression test.
- Consistency:0hard/6existing soft; roadmap index matches; BOARD assertion produced; changed procedure/template weekday check clean.
- Read-cap check still fails on existing MEMORY debt. Procedure repair is not data cleanup; root thresholds remain binding. Research retirement review remains incomplete. No new market evidence, scores, probabilities or registered triggers changed.
- Six child CLAUDE closeout sections have historical inconsistencies, but at least PHAN explicitly supersedes its old section with DOSSIER§8. A child-by-child check of active entry points is needed before asserting all six lack Git handling. No child procedures edited or agents launched here.
- No other agent/root procedure edited. No full closeout runner or new tier system introduced. Existing scripts check specific invariants; they cannot prove evidence review, approval continuity or legitimate non-applicability from an exit code alone.

The three corrected implementation surfaces are `CLAUDE.md`, `templates/SCRATCH.template.md` and `scripts/safe-push.sh`. Their prior text remains in Git history.
