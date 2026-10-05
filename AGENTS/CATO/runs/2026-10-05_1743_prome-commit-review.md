# PROME October 5 commit review

## Current assessment

Retain the installed boot/runtime/Git improvements. Make one bounded correction to the dormant docket cap before activating it: its commit hook checks staged rows against an unstaged policy file. No rollback of the rest of the bundle is warranted by this review. Will requested review of today's recent PROME commits; this is review and advice, not authorization to change PROME's active files or select a cap.

Pinned revision: `a441d4fa8ccf20b64e45d976ce2b5400635a5bda`, master, October 5, 2026. Inventoried 16 PROME-subject commits dated October 5 ET. Deep review focused on the consequential product changes in `39178712a` (boot/coverage), `2a72c60bc` (Git/hooks), `a441d4fa8` (closeout/cap/parser), and the WQ-385 instruction/acceptance records. Supporting delivery/boot records were checked for claimed versus demonstrated outcomes. This is not line-by-line certification of every generated render, source figure, old ledger row, or every historical clause moved into archives.

Owner work was already dirty in PROME and shared daily memory. No pull, owner edits, messages, launches, live boot, BOARD advancement, production hook installation or server mutation. Tests and counterexamples ran against a complete `git archive` export in `/tmp/cato-prome-oct5-review` or disposable fixture repositories. Product source paths remained unchanged against the pin at the final pre-report comparison; live dashboard state was separately dirty and excluded. Exact model not exposed; Codex shell and local Python/Git were used, not inferred Claude capabilities.

## PR1 — Medium: an unstaged cap edit changes what a docket commit is allowed to contain

**VERIFIED; introduced by a441d4fa8.** `PROME/tools/docket_row_cap.py:54–62,139–148` reads `scripts/harness_caps.env` from the working tree even under `--staged`. Only the docket candidate uses the commit index (`:PROME/DOCKET.tsv`, lines 156–159). The native `scripts/githooks/pre-commit` calls precisely that staged mode. The row and its governing policy can therefore come from different versions during normal shared-tree/path-scoped commits.

Independent disposable reproduction, using the actual hook and checker:

| Fixture | Result of committing only PROME/DOCKET.tsv |
|---|---|
| Committed cap 2,000; append a 2,050-byte row; config unchanged | Refused, rc 1, NEW-OVER-CAP |
| Same committed policy/row; remove cap key only from unstaged config | Commit succeeds, rc 0, reports dormant; HEAD still contains cap 2,000 |
| Same committed policy/row; raise cap to 10,000 only in unstaged config | Commit succeeds silently, rc 0; HEAD still contains cap 2,000 |

These are synthetic policy values, not recommended fleet limits. No hook bypass or force operation was used. An ordinary unfinished config edit by another session is enough; this does not require deliberate evasion. Conversely, an unstaged tighter cap could wrongly block an otherwise valid commit.

**Consequence and limit:** a deployed cap can be bypassed by a working-tree setting that is not part of the commit. Today's actual cap is unset, as the implementation receipt explicitly discloses, so no existing over-cap production commit or current active-policy violation is established. This is an activation prerequisite, not a reason to halt unrelated research or roll back all safeguards.

**Owner correction / closure:** PROME should make staged mode resolve the policy from the same effective Git index as the docket, honoring `GIT_INDEX_FILE`; keep working-tree policy for save/working-tree checks. Distinguish an intentionally unset indexed key from an unreadable policy blob. Acceptance: unchanged policy rejects the oversized row; unrelated unstaged removal/raise/tightening has no effect; a deliberately staged policy change is evaluated with its candidate; pathspec/alternate-index cases retain that behavior. Do not select a numerical cap as part of this fix. CATO has not implemented it.

## What holds up

- **Boot matcher (prior B8): CLOSED within the original reproduction scope.** Independently replayed CATO's original October 4 orchestration log. The new representation expands byte-for-byte to the original, including order and multiplicity; 12 compact pages versus the prior 14. Four groups contain 477 identities; the remaining singleton is preserved verbatim (478 known-gap rows overall). This is saved-case improvement, not a measured live-boot time saving.
- **Explicit charter coverage (prior B10): CLOSED within the runtime-overlay scope.** Focused tests cover missing charters, aliases, scoped-to-whole promotion, caller-declared injection and receipt propagation. Independent explicit-mode CLI returned assessed=1, reads=9, charter_reads=2, over_budget=0, over_cap=0, manifest_defects=0 at the pinned export. It still reports rotation_due=1. This does not recertify every desk's manifest. Prior B9's larger historical-reading cost remains; no changed historical-read contract or speed claim is accepted here.
- **Closeout declarations:** missing declarations and own stale references block in the tested cases; orange candidates retain advisory meaning. An independently constructed untracked/unindexed declared memory was correctly blocked by the real wrapped checker. The new wrapper comment understates that checker's existing missing-index handling, but no functional false pass was reproduced. Fleet candidate/packet disposition and applicable mirror-map checks remain manual obligations, as the v4 assessment discloses.
- **Artifact parsing:** independently confirmed the earlier leading-dot, `:312`, legacy bare-plus and plus-bearing-filename cases. Existing tests have no dedicated firetime-parser suite; these direct cases are bounded evidence, not arbitrary-path coverage. Blanket ignored-pointer treatment remains the owner's disclosed design concern, not a newly proven production defect here.
- **Git safeguards:** disposable suites pass for native subject/push guards, conflicting-hook preservation, installer idempotence and settings merge cases. CATO did not reinstall hooks, invoke Claude, inspect private user configuration, or authenticate GitHub protection settings. Desktop/GitHub deployment and laptop installation limits remain owner-reported.
- **Runtime compatibility:** the approved eight-file instruction changes preserve shared identity/authority and distinguish incomplete discovery from owner absence. Committed results qualify BOND as an existing-owner demonstration with launch origin unverified; Claude/mixed cases are deferred, not PASS. The midday boot receipt supersedes the morning approval-blocked status for HENRY/VULCAN/TERRY with observed interrupted/notLoaded, without claiming closeout. Native transcripts and live pair behavior were not independently exercised. In-flight owner updates to that results file were excluded.

## Verification record

All commands below ran on the pinned disposable export, Python 3 with `-B -W error::ResourceWarning`, through unittest discovery:

| Pattern under PROME/tools/tests | Tests | Result |
|---|---:|---|
| test_closeout*.py | 39 | PASS |
| test_boot*.py | 46 | PASS |
| test_locks_safeguards.py | 14 | PASS |
| test_docket_row_cap.py | 19 | PASS |
| test_repeat_boot.py | 33 | PASS |
| test_orch_closeout.py | 17 | PASS |
| Total | 168 | PASS |

Independent probe source and outputs: [probe.py](2026-10-05_prome-commit-evidence/probe.py), [probes.json](2026-10-05_prome-commit-evidence/probes.json), [explicit-readcap.txt](2026-10-05_prome-commit-evidence/explicit-readcap.txt). Run the probe against a complete export of the pinned commit; it imports that export's fixture helpers and creates its own disposable Git repositories. Negative memory probe initially had an incomplete fixture constants file; corrected to the full pinned constants and rerun. Blocking result persisted and the unrelated length check then passed. No production failure is inferred from that fixture-preparation issue.

Implemented by CATO: this review, evidence and continuity updates only. Tested: listed suites and independent probes. Independently verified: the bounded product behaviors above, including PR1. Still unresolved: PR1 owner repair, cap choice/activation, laptop installation, live Claude/mixed compatibility, hosted publication and practical ordinary-boot benefit. Existing owner approvals survive; this review starts none of those tasks.

## Delivery and stop condition

Review complete; recommended next action is the single PR1 correction before cap activation, then its specific staged-policy counterexamples. No additional broad audit or recurring check proposed. Return to Will and await direction. Other pending CATO work, the desk-closeout proposal and forecast-pilot approval remain at their existing resume points.

Closeout checks: all six weekday inputs were first verified readable, then passed: PROME/DOCKET.tsv, GATES.tsv, WILL_QUEUE.md, CATO/CONTINUITY.md, this report and the continuing boot report. Optional CATO STATUS/CALENDAR/CATALYSTS files remain absent and were omitted. Direct startup measurements: CATO AGENTS 6,465 B, CHARTER 9,921 B, CONTINUITY 22,111 B; root CLAUDE 24,961 B, USER 5,200 B, AGENTS 5,313 B, all below 32,550 B. Generic CATO read-cap returned rc2 CANNOT-EVALUATE for absent local CLAUDE.md, not PASS. Orphan advisory exposed only the preserved owner files already dirty in PROME and shared daily memory; CATO authored no outside packets or shared-log rows. Scoped whitespace clean; staged list empty before delivery staging. No STATUS/ledger, auto-memory, or shared threshold change triggered additional conditional checks. Exact Git receipt is delivered in-session; no hosted publication applies to this local review.
