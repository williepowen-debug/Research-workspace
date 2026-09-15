# CATO foundation feedback — bounded repairs

## Scope and acceptance, recorded before edits

Will approved the recommendations in-session: “Okay can you implement these fixes per your recs?” This covers the launcher correction, local authorship/self-review clarification, and a proposal packet for PROME. His earlier instruction protects PROME, WALTER and BRENT's active files and permits inbox communication. Starting revision: `594c8986d7d1333bb466d13336d70f4278e46e9d`; foreign working changes are present. No pull, active-owner edits, roster activation or RAV retirement is part of this pass.

Acceptance:

- Command inspection succeeds without Codex on PATH; an actual launch still fails clearly with exit 127 when Codex is absent.
- With Codex available, arguments retain the requested Astra model, CATO cwd, repository access, workspace-write/on-request controls and literal task delimiter. Inspection never invokes Codex.
- Future CATO-authored commits identify the implementer independently of the owning directory. Historical commits remain unchanged, with a provenance map here and a startup-visible pointer.
- CATO may maintain and test its earlier implementations, but must not present that work as independent assessment of the same changes. Existing independent receipts retain their bounded scope.
- PROME receives a concrete proposal for a discoverable manual-only boundary and instrument checks. Registration/classification remains proposed until the owner integration pass; no new fleet eligibility is implied.

Neighbour cases: missing CLI is the reported failure; an option-shaped task tests argument overlap; ordinary launch uses a stub, never a second model session. Wrong ownership and concurrency are addressed by exact local paths plus one new self-authored inbox packet. No owner state, Git identity, historical commits or global configuration is changed.

## Provenance of earlier implementation work

These changes were made by the preceding Will-directed Codex session whose review relationship CATO carries forward. Their `PROME:` subjects identify the affected owner, not the actual implementing session. `git show -s --format=full <revision>` confirms the subjects and shared Git identity; the foundation/continuity and linked task records establish session provenance.

| Revision | Work attributable to that Codex session | Review limitation |
|---|---|---|
| `f12c6dc94` | L393 Owed/reference renderer and operational instructions | CATO maintains its own implementation; prior independent code/local-output receipt does not establish hosted delivery. |
| `2ae76c7c4` | L381 instruction reconciliation; L333 evidence reconciliation; L393 preview | Source review is recorded; ordinary-session observations and aggregate trial grading remain distinct. |
| `24b820577` | Review-test fixtures, L247 F4 disposition correction, continuity proposal | Further CATO checks of these changes are author follow-up, not independent verification. |
| `71d554b92` | Revised continuity sample | Proposed sample, not applied live state; CATO authored it. |

Task receipts remain at their existing homes linked by CONTINUITY. This map does not transfer PROME's operational obligations to CATO.

## Results

**Implemented:** moved the CLI-availability guard after command inspection; documented inspection prerequisites in README; extended the existing charter's self-review rule and added the `Implemented-by: CATO` convention; updated continuity with the authorship pointer and current concurrency boundary. Created [PROME's proposal packet](../../../PROME/inbox/2026-09-15_from-CATO_manual-integration-proposal.md), including candidate roster text, the OFF-FLEET definition mismatch and before/after instrument acceptance. No active owner files changed.

**Tested by CATO:** `bash -n` passed. Isolated temporary PATH containing Git and dirname but no Codex: inspection exited 0 and printed the requested command; actual launch exited 127 with the missing-CLI message. With a temporary Codex stub: inspection never invoked it; actual launch passed exact model/cwd/repository/sandbox/approval arguments and preserved an option-shaped task containing shell metacharacters and a newline as one literal argument. Two tasks were rejected with exit 2. CATO local links and scoped `git diff --check` passed. Fixtures used `/tmp`, started no model and were removed by their temporary-directory context.

**Independently verified:** no independent result review in this repair pass. These are CATO-authored implementation and tests responding to PROME's feedback relayed by Will, not blind independent convergence. The earlier foundation review receipts are unchanged.

**Still unresolved:** roster placement and instrument integration, RAV transition, exact backend identity evidence and ordinary operational proof. The packet requests owner disposition; delivery does not establish acceptance or integration. Tool discovery found no native cross-session ListAgents/SendMessage capability, so no live doorbell or acknowledgment is claimed.

**Delivery:** exact-path local commit intended at closeout, with `Implemented-by: CATO`. Push is deferred under root's foreign-dirty-tree startup rule while Will's other sessions are editing; no pull or shared-tree stash. Locate the resulting commit by report path. No claim of remote publication is made here.
