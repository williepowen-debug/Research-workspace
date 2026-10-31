> Saved by PROME (prome-34), verbatim except one fixture string at the account-number guard's line reworded so the public-repo guard passes, at 16:32 ET 2026-10-31 from the reviewer's ledger in the session scratchpad. The reviewer's harness scripts and disposable clones lived in that scratchpad and are not preserved. Record of WQ-578: `PROME/reports/2026-10-31_checker-value-sweep.md` § Execution receipt.

# WQ-578 combined independent review: removal batch (G1–G4)

**Reviewer:** one independent read-only reviewer (Opus), 2026-10-31 16:03–16:19 EDT (`date`). The real repository was not edited, staged, stashed or committed: `git status --short` showed 20 paths before and after, and the stash list is empty. Fixtures and throwaway repositories were kept under `…/scratchpad/wq578-review/`.
**Inputs:** the sweep (`PROME/reports/2026-10-31_checker-value-sweep.md`), the WQ-578 row in WILL_QUEUE § RECENTLY DONE, and the uncommitted diff of the 13 named files (+53 / −94 lines).
**Main question (Sloane):** was any removed check the only thing catching a dangerous or costly failure?

## Overall: ACCEPT WITH NAMED RESIDUE

- **❌ = 0.** No removal opens a consequential hole, and no edit breaks a function that is still needed.
- **⚠️ = 7, plus 2 observations.** The most important ⚠️ is W1: the #57 and #58 hooks still run on this machine through the user-level settings file.

## Per-removal verdicts

| # | What was removed | How it could act before | Was it the only catcher of a costly failure? (evidence) | Verdict |
|---|---|---|---|---|
| 6 | Boot fire-time scan plus the written-disposition duty (WQ-467 C4) | ACTION line; never blocked | **No.** (a) The GATES gate-citability check stays and BLOCKS; it already requires every LIVE gate's spec file to be readable. (b) `CLOSEOUT_PROCEDURES.md` Chunk 3 still runs `firetime_check.py` on artifacts that cite a DOCKET row changed in the session. That covers the "canonical date moved, artifact did not" class (the 7/01 WAL case). (c) Any trade still needs TERRY's card, live prices and Will's [Approve] (root rules #4 and #5). (d) The record shows 0 real date errors among ~85 date flags (10/21–10/31). **Today:** I ran the scan at 16:1x and diffed it against the baseline. It shows 6 NEW flags, all benign: the UNG card's `Jan-15` is the option expiry and its `2027-01-08` is the card's own time stop; ISHM's `1/2` is a fraction; the other three are pointer-format items. No real finding is left stranded by the retirement. | KEEP-REMOVED (residue W2) |
| 61 | Root step 1e glued-date command | Advisory | **No.** The Output Canon rule against glued words still applies. The check's main consumer was #6's date parser, which is now gone. | KEEP-REMOVED (residue W5) |
| 7 | "agent freshness" boot line | ADVISE | **No.** The files it flags are a strict subset of what the ACTION "PROME/inbox drained" check flags: inbox files outside `processed/`, versus every unfiled file. The per-desk `--agent` use before a launch stays. | KEEP-REMOVED |
| 21 | Handwritten calendar coverage | ADVISE | **No.** I ran it: `SCRATCH § Calendar` matched 0 dated claims. The section is now only a pointer to the generated calendar. | KEEP-REMOVED |
| 25 | HEARTBEAT amendment chain (boot and closeout) | ADVISE | **No.** It checks document upkeep, and `read_cap_check` already meters HEARTBEAT's size. | KEEP-REMOVED (residue W5) |
| 28 | Boot↔closeout symmetry | ADVISE | **No.** It is bookkeeping on procedure documents. | KEEP-REMOVED (residue W6) |
| 39/40 | Decision Deck publication prerequisites and Deck republish | ADVISE; with `DECISION_DECK_PAUSED = True`, both returned PASS before reading any input | **No.** The Deck is paused (WQ-460), and neither check touches CATO's app. | KEEP-REMOVED (observation O2) |
| 41 | DOCKET changed-row byte cap (closeout gate, pre-commit hook, save hook) | BLOCK, but `docket_row_cap.py` returns 0 before any scan when `DOCKET_ROW_CAP_BYTES` is unset (it is unset) | **No.** Removed or moved rows are refused by `docket_line_stability.py`, which is always on. Tested in a throwaway repo: an inserted row was refused, a deleted row was refused, and an in-place edit was allowed. | KEEP-REMOVED |
| 57 | Commit-subject fallback hook | Would block a subject over 100 characters, but only when the native hooks are missing; the banner installs them every session | **No.** It only checks subject length. | KEEP-REMOVED, but **not actually removed** (W1) |
| 58 | Pipe exit-code hook | Advisory only; exits 0 and never 2 | **No.** It never blocked anything. | KEEP-REMOVED, but **not actually removed** (W1) |
| 59 | DOCKET part of the save hook `forge_validate.py` | Its messages were only ⚠️ (or a ⛔ that is impossible while the cap is dormant), and exit-0 output is hidden | **No.** The gate's DOCKET checks remain. The FORGE/STATUS part (the position-mirror guard) and the GATES part are unchanged. | KEEP-REMOVED |
| G2 | HANDS rows stop raising PASSED / DUE TODAY / AGING / NOT-ISO | ACTION | **No.** The two HANDS rows that guard real deadlines carry due ⏰ markers in Notes, and both parse: #31 (renew credentials before the FFIEC token expires 11/5; ⏰ 2026-11-01, plus a DOCKET 11-01 row and env_doctor's token-expiry warning) and #495 (renew the Call Report login; ⏰ 2026-11-03). The other HANDS rows are research errands. This implements Will's own WQ-538 A ruling. | KEEP (residue W4) |
| G4 | Root step 1c-bis drops "say why not" | Prose | **No.** The flag itself stays, and no money is involved. | KEEP (residue W3) |
| — | Four DOCKET rows (L581, L607, L777, L903) relabelled RETIRED → TOMBSTONE | — | **No.** `docket_view.state_kind` reads both RETIRED and TOMBSTONE as TERMINAL, and line numbers are unchanged. | KEEP |

## G2 fixture results

Method: `g2_fixture.py` imports the HEAD gate and the working-tree gate, points both at a temporary queue file, and records each row's flag.

| Row (fixture) | HEAD gate (before) | Working-tree gate (after) |
|---|---|---|
| HANDS, needed-by passed / due today / undated 60 days / non-ISO date | PASSED / DUE / AGING / NOT-ISO | none (intended) |
| HANDS, ⏰ marker dated yesterday / dated today | none | RE-PRESENT ✓ |
| HANDS, needed-by passed but ⏰ marker in the future | PASSED | none ✓ |
| HANDS, closed in place (✅ DONE) | MISFILED | MISFILED ✓ |
| HANDS, Type written `**HANDS**`, `` `HANDS` ``, `` **`HANDS`** `` or `hands` | PASSED | none ✓ (all recognised) |
| Type `YOUR HANDS` or `DECISION / HANDS` | PASSED | PASSED (not treated as HANDS; the gate stays loud) |
| Type `HANDS / DECISION` | PASSED | none (treated as HANDS) |
| HANDS, ⏰ marker in the **PROME rec** cell / written with a colon / in M/D form | none | **none: silent** (W4) |
| HANDS, impossible ⏰ date `2026-02-30` | none | IMPOSSIBLE DATE ✓ |
| HANDS, old due marker plus a newer re-dated marker | none | RE-PRESENT (the first marker wins; the gate stays loud) |
| DECISION, passed / due today / undated 60 days | PASSED / DUE / AGING | unchanged ✓ |
| CAP (actionable-row count) | 24 | 24 ✓ (HANDS rows still count) |

## ⚠️ findings

Each finding runs: claim → artifact → command → observed → proposed change.

**W1. #57 and #58 are still live on this host.**
- Claim: removing the two hook entries from both repo `settings.json` files retires #57 and #58.
- Artifact: the user-level dispatcher `~/.claude/settings.json`. It was installed by `scripts/install-claude-hooks.py` (PROME/MACHINE_LOCAL.md, "Fleet safeguards") and is the only hook carrier for desk sessions launched from `AGENTS/<NAME>/`.
- Command: I listed the hooks in that file that carry the ROSTER.md repo guard.
- Observed: "Subject guard fallback…" (`commit_subject_guard.py`) and "Pipeline rc advisory…" (`pipeline_rc_block.py`) are both still present. The installer only merges entries by exact command and never removes old ones, so re-running it will not clear them. The laptop is UNKNOWN; it is INFERRED to be the same, since its dispatcher was installed 10/08.
- Proposed: delete the two entries from `~/.claude/settings.json` on the desktop now and on the laptop at the next machine switch, and record that in MACHINE_LOCAL. Otherwise, record that both hooks stay in force. (This is the conservative direction: nothing became unsafe, but the cleanup did not happen.)

**W2. The spine audit runner still assumes fire-time covers the next 7 days.**
- Claim: nothing else relied on the boot fire-time scan.
- Artifact: `PROME/tools/spine_audit.workflow.js`, line 26 and the anchor reader's prompt at line 168 ("scripts/firetime_check.py already validates rows dated within 7 days"). Eligibility for its sample is set to "8 or more days after today".
- Command: `grep -n firetime PROME/tools/spine_audit.workflow.js`
- Observed: PENDING rows dated within 7 days now get no routine check of their source artifacts. The one exception is the closeout run on a DOCKET row changed in that session. `BOOT_MODULES.md` was updated to say this, but the runner still states the old premise.
- Proposed: in the anchor reader's prompt, change "8 or more days" to "1 or more days" and delete the fire-time sentence. This reuses an existing control and adds no new check.

**W3. G4 is contradicted by the tool's own message.**
- Claim: desks no longer explain an un-refreshed ledger.
- Artifact: `scripts/ledger_staleness.py:1065`.
- Command: `grep -n "say why not" scripts/ledger_staleness.py`
- Observed: every nudge still prints "freeze-or-refresh EACH, or say why not in the commit". Desks follow the printed line, so the ritual G4 removes will continue.
- Proposed: send a packet to the tool's owner (last commit `8b1012baf`, DAEDALUS) asking it to drop "or say why not in the commit". PROME should not edit the file itself.

**W4. A malformed ⏰ marker on a HANDS row is now silent.**
- Claim: G2 implements WQ-538 A.
- Artifact: `check_will_queue()`, which searches only cell 6 (Notes) for `⏰\s*re-present\s+YYYY-MM-DD`.
- Command: the fixture rows 914, 915 and 921 above.
- Observed: a marker in the PROME rec cell, a marker with a colon, or a marker in M/D form produces no flag. Before G2, the same row with a passed Needed-by date raised PASSED. Row #559 (a DECISION row) already keeps its ⏰ marker in the PROME rec cell. Today both real HANDS markers (#31 and #495) are in Notes and parse correctly.
- Proposed (pick one): search cells 5 and 6 and allow an optional colon, **or** raise a named flag when a HANDS row's ⏰ text does not parse (the same fail-loud pattern as IMPOSSIBLE DATE). Low priority.

**W5. Live DOCKET obligations still point at retired checks.**
- Claim: G1 and G3 left no stale instruction.
- Artifacts: `PROME/DOCKET.tsv` rows:
  - L855: the chain-check regex fix (next PROME process pass).
  - L852 ask ①: the chain check (due 11-03).
  - L893: "DID THE GUARD WORK? … flat or rising ⇒ bring Will the choice of making it blocking" (due 11-06).
  - L892 part (4): desks act on their step-1e glued-date flags.
- Command: an awk filter for PENDING rows that name a retired check.
- Observed: all four are still PENDING. On 11-06, L893 would have PROME ask Will about making a retired check blocking.
- Proposed: annotate each row in place as OVERTAKEN by WQ-578, with the state token first so the buried-state-token check still reads it correctly.

**W6. Tests pinned to the retired wiring now fail.** Every one of these passed against HEAD. Commands: each test run against the working tree and against a `git archive HEAD` copy.

| Test | Result now | Note |
|---|---|---|
| `test_docket_row_cap` | 6 failures | Its pre-commit cases test the removed row-cap hook |
| `test_gate_action_owed_WQ467` AO6 | 1 failure | It expects the fire-time ACTION line |
| `test_deck_pause_WQ460` | 1 failure | It expects the Deck checks in closeout; its other assertions (review controls) still matter |
| `test_boot_coverage` | 2 subtests fail (1 ≠ 2) | It expects two calendar checks |
| `test_locks_safeguards` | 1 new ERROR (IndexError, line 215) | Lines 209–214, the wrong-repo half, still pass and still matter |
| `test_gate_isolation_L294_F7` MissingInput | Will fail after commit | `check_symmetry` was the only check that read `CLOSEOUT.md` |

The last row is the one test that guards a property still needed: one missing input must not take down the gate. I verified it in a fixture: the working-tree gate with `CLOSEOUT.md` deleted no longer reports "check_symmetry DID NOT RUN". The other 5 failures in that file were already failing at HEAD.

Proposed: trim the assertions about retired wiring, and re-point the L294 probe at an input that a still-wired check reads.

**W7. Count and label drift.**
- `PROME/BOOT.md:37` and boot SKILL item 4 (both copies) still say "five-verdict rules", while step 5 now says "four verdicts".
- The hook `statusMessage` "Post-save validator (FORGE/STATUS, GATES, DOCKET)" in both repo copies and the user-level copy still names DOCKET.
- `PROME/SCRATCH.md:53` still lists "owner fire-time flags and expired allowlist cleanup remain".
- The DAEDALUS packet G3 names (DAEDALUS owns the script) was not found in `AGENTS/DAEDALUS/inbox/` at 16:1x.
- Trivial: the 10/29 BOOT stamp was dropped from BOOT.md's header without being appended to the stamp archive. Git keeps it.
- Proposed: fix the wording at the next edit of each file, and send the DAEDALUS packet.

## Observations (no action required)

- **O1.** #46 was kept because `will_brief.parse_actions()` "still has callers". VERIFIED: its only callers are the full-page brief path (Helm, retired; the `--book-line` mode exits before reaching it) and `will_handbook.py` (CLOSEOUT step 7 says "do not run"). Keeping the test is harmless, and retiring it later would also be safe. The selftest's fixture has no HANDS rows, so the two parsers' agreement on HANDS rows is untested; it matters little while the brief parser is dead.
- **O2.** The Deck resume carriers (DOCKET L580, L663, L734) do not mention that the two Deck checks must be re-wired on resume. Only the code comment says so. This is optional to fix.

## Verified clean

- Every removed gate check was ADVISE or ACTION, or a BLOCK that cannot fail while its cap is unset (#41). No live blocking control was removed.
- The functions remain defined, and an ast scan finds none still called from gate code.
- The working-tree gate runs in a fixture without crashing:
  - boot: 8 blocking / 2 action owed / 17 advisory, matching PROME's figures; the 1 NOT RUN line is specific to the fixture and also appears at HEAD.
  - closeout `--tier light`: no crash.
- In a throwaway repo, the pre-commit hook still refuses a planted account-number line (the fixture's "account no." plus eight digits), a mid-file DOCKET insert and a DOCKET row deletion, and allows an in-place edit.
- Syntax checks pass: `bash -n` on the pre-commit hook, and an ast parse of the gate and the save hook.
- A DOCKET save now exits 0 silently, as before.
- Both repo settings files parse and hold identical hooks. The two boot-skill copies are byte-identical. The queue-parser selftest passes 26/26.
- The root CLAUDE.md edit broke no CANON_PROVENANCE anchors: the same 3 anchors miss at HEAD.
- No live manual, skill, script or desk charter references `firetime_delta`, `04-firetime`, `--check glued`, the agent-freshness gate line, `check_symmetry`, `docket_row_cap`, `commit_subject_guard` or `pipeline_rc_block`. The exceptions are code comments, dated records, W2 and W5.
