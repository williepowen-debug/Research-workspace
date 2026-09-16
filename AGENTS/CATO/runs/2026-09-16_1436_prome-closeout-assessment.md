# PROME closeout assessment and bounded next pass

Will asked CATO to help with PROME's September 16 closeout assessment. Snapshot: `dd71d926b23b2b6deae4b5c005fbf09ce9acfa93`, approximately 14:36 ET. Other desks have active dirty and staged files. CATO did not run PROME's operational closeout, change owner files, send messages, spawn reviewers, or edit policy. This report is an independent assessment of the inspected current procedure and a concrete next-pass proposal, not the required audit of a finished candidate.

## Judgment

PROME correctly says Standard closeout was not completed. The retained bounce log has one failing blocking check naming five docket obligations; it does not have five separate failing checks. Review was advisory at Bounce, and its manifest belonged to a prior baseline. The checkpoint preserved state without completing Standard generation, final-candidate review or publication.

One qualification: the existing tier table expressly permits Bounce for an immediate restart and sets no artifact-count ceiling on it. Large accumulated changes do not, by themselves, prove selection of Bounce violated that table. The failure is treating preservation as completion, or letting the restart erase accumulated closeout debt. PROME explicitly labels the checkpoint incomplete. If Will requested a full closeout, his request governs. A future clarification should distinguish checkpointing from discharging the accumulated session obligations, rather than retroactively inventing a Bounce size rule.

One full run is the right next operational test. It can demonstrate that run's success; it cannot establish general reliability. If native publication or a required reviewer is unavailable, finish independent feasible steps and report the exact incomplete stage. Do not promise all three delivery states in an environment whose prerequisites are not established.

## Verified defects and limits

1. **Tier contract is inconsistent across surfaces.** `PROME/CLOSEOUT.md` gives Bounce an optional small SCRATCH checkpoint, labels audit step 8 Standard/Heavy, and labels publication Standard+. But routine step 10 unconditionally requires reviewed-byte verification before push; the skill unconditionally walks generation, audit and publication. Additionally `.claude/agents/argus.md` and its cited WQ-226 record skip ARGUS below three commit paths, while the Standard gate requires REVIEWED regardless of path count. The present large candidate does not qualify for that small-set exception, but the rule needs explicit precedence eventually. Canon/runner parity alone does not resolve this contradiction.

2. **The docket gate has two independently reproduced false-negative paths.** `prome_gate.py:424` uses `r[3].split("(")[0] != "PENDING"`; line 433 accepts any COVERED substring. Isolated temporary ledgers, same current date and PROME owner:

   | Status | Notes | Actual gate result |
   |---|---|---|
   | PENDING | empty | blocks |
   | PENDING | NOT COVERED; no owner accepted | passes |
   | PENDING — still owed | empty | passes |

   This confirms more than weak coverage evidence: ordinary annotated pending text can disappear before coverage is examined. Use the existing L370/queue-parser workstream for a bounded repair. Meanwhile a real closeout must enumerate obligations at their records and verify coverage evidence, not equate rc=0 with accepted handoff. CATO did not change states or append COVERED to make anything pass.

3. **The overnight defect is repaired in `fa7bfe77d`.** CATO inspected the through-date selector and the evidence-first exclusion of completed prior touches, and reran all 17 tests successfully. The prior CATO medium date-boundary finding is resolved for this tested scope. Historical UNKNOWNs remain evidence gaps, not active-session claims. A useful presentation change would show current-date touches and known carried obligations first, with a separately labeled historical-uncertainty count and full dated detail retained in the existing log. Do not close, delete, or downgrade UNKNOWN rows merely to quiet output; ownership/age alone does not prove completion. Any categorization must retain unidentified rows and cannot certify completeness from date alone.

4. **Reviewer/runtime identity needs explicit handling.** The current ARGUS definition specifies an Opus auditor, fresh context, computed baseline/perimeter and a particular trial. An Astra/CATO review can supply independent evidence on work it did not implement; it must not silently be recorded as the named Opus trial run. A bounded substitution needs Will's explicit ruling if that is the chosen path. CATO's own earlier changes in PROME remain author-follow-up for CATO; a finished-candidate review must preserve that limit and use another independent reader for those changes. No such substitution or final-candidate certification is granted by this assessment.

## Concrete next Standard closeout

Keep execution with PROME. Use existing records and retain one short receipt in its current session report; no new recurring ledger or universal checklist is needed.

1. **Set scope and prerequisites before editing.** Select Standard over the accumulated work since the recorded review baseline; a restart must not move that baseline. Inventory exact authored paths, including prior CATO/other-author edits under PROME paths (L402), instead of asserting the path classifier proves authorship. Establish the reviewer and native private Helm/Deck/ruling-store access. Local HTML and Sites tools do not establish access to the existing Claude artifact. If unavailable, state which downstream stage remains incomplete.
2. **Disposition the five current docket obligations using different evidence, not one blanket token:**

   | Row | First action at this snapshot |
   |---|---|
   | L318 BRENT SPR | Read `PROME/inbox/2026-09-16_from-BRENT_eia-resolver-and-expiring-call.md` and its cited EIA evidence. BRENT has delivered Branch A; PROME consumption/record integration is still needed. Preserve the DOE-program caveat and owner grade. CATO inspected the packet, not the EIA cells for a new grade. |
   | L276 VIOLET | Grade depends on the close. Establish actual post-close coverage or the row's existing dark-owner pre-fetch fallback; do not fabricate an intraday grade or infer coverage from a sent packet. |
   | L310 FERT | Obtain the owner result or actual accepted coverage under current launch/preflight rules. An old grade or named owner is not today's delivery. |
   | L350 read budgets | Apply the row's actual contract: carry measured constraints into next launch briefs; desks own repairs, no between-brief chase. Do not interpret disposition as requiring all desk rotations now. |
   | L352 telemetry | Its amended notes withdraw the REGINALD mirror remedy and put the fix at WALTER question 5. Check that owner evidence; do not ask REGINALD to implement the superseded mirror. |

   These are proposed next actions, not completed dispositions. Re-read current rows before acting; owner files are moving.
3. **Finish state and derived outputs before freeze.** Follow the existing symmetry table, targeted updates/no-ops, residual triggers and source-then-render order. Do not renew old review status over new bytes. Preserve unfinished owner tasks instead of absorbing their work into PROME.
4. **Freeze and obtain actual independent findings.** Scope must include committed plus pending changes and the rendered pair. After fixes, regenerate affected artifacts, re-freeze and re-review changed portions. Record actual reviewer identity, inspected revisions, finding dispositions and exclusions. A manifest hash verifies identity, not whether a person/model performed an audit.
5. **Gate, exact-path commit, committed-byte verification, safe-push, publication.** Run the actual Standard gate; rc=1/2 stays incomplete. Verify the same exact paths in the resulting commit before PROME initiates push. Fresh ancestry confirms the pushed commit. Foreign dirty files alone do not ban pushing; they constrain staging and recovery. Another desk's push can carry shared committed work, so do not confuse remote presence with successful PROME review. Publish only verified artifacts to their existing private destinations and verify links/store readback. Report COMMITTED / PUSHED / PUBLISHED separately, including a partial result.

## Bounded clarification to consider after the exercise

Proposed intent, NOT installed policy: “Bounce preserves continuity for an immediate restart; it does not certify or reset the accumulated Standard closeout. Its resume pointer carries that obligation. Each tier must name exactly which review, commit, verification and publication steps apply; a lightweight checkpoint is not a reviewed Standard delivery.”

Before installing wording, settle the Light/Bounce push contract and the ARGUS small-set exception explicitly; mirror the resulting branches in the runner and gate. This is a small reconciliation of existing controls, not justification for a broad closeout rewrite. For historical noise, improve ordering and summaries while preserving evidence. For coverage, fix parsing plus the evidence requirement; substring cleanup alone is insufficient.

## Evidence and completion

Read current CLOSEOUT, runner, assessment and bounce handoff; retained bounce gate output `/tmp/prome-bounce-gate-20260916.txt`; selected gate/manifest code; ARGUS definition and cited trial record; L381 plan/limits; five docket rows; BRENT packet; overnight repair record and tests. No live full gate, generator, review-manifest mutation, owner-message send or publication performed. Test writes stayed under /tmp; PYTHONDONTWRITEBYTECODE was set.

This assessment is complete; the full Standard closeout and any canonical changes remain PROME work requiring their existing authority, review and capability conditions. Next CATO action: orient and await Will; if assigned the finished-candidate review, inspect its frozen scope and authorship before accepting independent coverage. Commit/push receipt for CATO's report is delivered in-session.
