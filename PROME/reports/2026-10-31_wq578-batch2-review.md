> Saved by PROME (prome-34) verbatim at 18:12 ET 2026-10-31 from the reviewer's ledger in the session scratchpad (wq578b2/review-ledger.md); the reviewer's disposable clones and harness scripts lived there and are not preserved. Disposition of every finding: `PROME/reports/2026-10-31_checker-value-sweep.md` § Execution receipt — WQ-578 batch 2.

# WQ-578 batch 2 — combined independent review (L908)

**Reviewer:** one independent read-only reviewer (Opus), 2026-10-31 17:36–18:0x EDT (`date`: 17:36:52 start, 18:02:02 at this write).
**Real repository:** nothing edited, staged, stashed, reset or committed. `git stash list` empty; the index still holds only the batch's three renames; `git status --short` = the batch's 32 paths + the untracked test.
**HEAD moved during the review** ef63cf769 → 34e12169a (WALTER 9faae49a1, 523b76753; CATO 34e12169a). Those commits touch only AGENTS/WALTER, AGENTS/CATO, BOARD and BRENT/HENRY inboxes, so the baseline of every batch file is unchanged.
**Disposable clones** (scratchpad `wq578b2/reviewer/`): `wt` = 34e12169a + `git diff HEAD --binary` + the untracked test (all 33 paths byte-compared to the live tree); `wt_head` = 34e12169a without the batch. Counterexample scripts: `reviewer/ce/ce_spawn.py`, `ce_queue_gates.py`, `ce_memory.py`. Test outputs: `reviewer/res_batch/`, `res_head/`, `res_batch_c2/` (batch committed in the clone only).

## Overall: REJECT as it stands — ❌ 1 · ⚠️ 9 · ℹ️ 8

- **❌ X1** is in the one behaviour the #32 merge adds: on every boot/closeout with a DARK or UNKNOWN spawn row, the merged line says the slate was NOT regenerated and must not be read, although it was just regenerated. One function + one realistic test fixes it; after that the batch is **ACCEPT WITH NAMED RESIDUE** (W1–W9).
- **Main question A:** no removed or merged check was the only catcher of a money, missed-obligation or silent-data-loss failure. One partial exception: the retired calendar-freshness line was the gate's only mechanical surface for a malformed DOCKET date span, which spawn_list and the lands-today check skip silently; it now surfaces only at the BOOT step 2 / CLOSEOUT step 1 regeneration command (W3).
- **B:** no code caller of any deleted function, global, flag or test path remains (repo-wide grep + ast); `--sessions-json` has no live caller. Post-commit, one test breaks (W1); one pinned-wiring test already fails at HEAD and is missing from the claim (W2).
- **C:** five manual/agent passages still describe retired checks (W4, W5); two live DOCKET rows still point at deleted code (W6).
- **D:** no edit outside L908 + the named items. ORCH_LOG/ORCH_INFLIGHT carry only this review's spawn row; the BOOT stamp-archive line is the header rotation.
- **F:** all 22 `build_hashes` pins in `PROME/decisions/app-acceptance.json` match sha256 on disk; the batch touches none (willq_view.py, session_banner.sh, githooks unchanged).

## Findings (claim → artifact → command → observed → proposed)

**❌ X1 — #32: the merged spawn line tells PROME not to read a slate that was just regenerated, exactly when the slate matters.**
- Claim: "a slate failure must make that line ⚠️, never silent"; the line decides "regenerated" from the slate's exit code.
- Artifact: `PROME/tools/prome_gate.py:1388-1391, :1398`; `PROME/tools/spawn_slate.py:590, :641, :688/:696` — spawn_slate WRITES `PROME/state/SPAWN_SLATE.md`, then exits with `spawn_list.render()`'s rc: 1 on any DARK row, 2 on any UNKNOWN row or a FAILED conservation count.
- Command: CE-1 below (DARK row in `wt`, real tools, no mocks).
- Observed: `spawn_slate.py` rc=1 with the slate rewritten 17:41 ("spawn candidates: ORACLE (slot 1 of 4; D:L910)"); gate line: "… DARK: D:L910 ORACLE · … · slate NOT regenerated (spawn_slate.py rc=1; log …) — do not read a stale slate". Same for an UNKNOWN row (rc=2, CE-2). HEAD printed the slate as its own ⚠️ line with its last output line — no false claim. The new test fakes slate rc=0 beside a DARK list (`PROME/tools/tests/test_wq578_batch2.py:124-132`), so it cannot see this. Consequence: on DARK/UNKNOWN boots and closeouts the gate contradicts BOOT.md step 6 (read the slate's top block: spawn candidates, read-first returns — the consumer read that prevents a needless or duplicate spawn). The sweep records DARK-row wakes on 10/31 itself (AEOLUS, DAEDALUS, YURI).
- Proposed: decide "regenerated" from the slate's own output (`spawn_slate · as-of … → PROME/state/SPAWN_SLATE.md` present, `spawn_slate · ⛔ FAILED` absent), never from rc; name a conservation FAILED separately; add SpawnLine cases with slate rc=1 after a write and rc=2 with the FAILED banner.

**⚠️ W1 — test_gate_isolation_L294_F7 gains a 5th failure once the batch is committed; the "identical at HEAD" comparison could not see it.**
- Artifact: `PROME/tools/tests/test_gate_isolation_L294_F7.py:163` (`assertGreater(printed, 20)`); `PROME/tools/tests/gate_fixture.py:70-82` builds its fixture with `git archive HEAD`, so before commit this file tests HEAD's gate, not the batch.
- Command: committed the batch in `wt` only (b5370de28), re-ran the whole suite (`reviewer/bin/run_tests.sh`).
- Observed: `MissingInput.test_independent_checks_still_report`: "only 15 checks printed" (needs > 20; the batch removes or merges 8 boot lines). The real property holds: `test_it_retains_the_same_checks_the_clean_run_produced_minus_the_failed_one` passes. Every other test file: same status and same failure names, committed vs HEAD.
- Proposed: derive the floor from the clean run (clean count minus check_gates_tsv's lines) or set it to the new count; re-run after the commit.

**⚠️ W2 — test_docket_row_cap.py fails 6/6 hook cases at HEAD and with the batch; missing from the claimed failing list.**
- Artifact: `PROME/tools/tests/test_docket_row_cap.py` (Repo.*); `scripts/githooks/pre-commit` (row-cap block removed in CATO's cd0f1a254, 17:28 ET = L908's row-cap half).
- Command: full suite in `wt_head` and `wt`.
- Observed: identical 6 failures in both ("AssertionError: 0 == 0", "'not configured' not found in ''"); the author's run (17:25) predates cd0f1a254. `PROME/tools/docket_row_cap.py` now has no live caller.
- Proposed: trim the hook cases (or retire the file with the tool) in this batch, as batch 1 did; name it in the receipt.

**⚠️ W3 — #20 removed the gate's only mechanical surface for a malformed DOCKET date span.**
- Artifact: retired `check_calendar_views` (HEAD) ran docket_view's strict parser every gate run (`scripts/docket_view.py:101-105` refuses "dots, Unicode dashes, compact digits"); `PROME/BOOT.md:52` and `PROME/CLOSEOUT.md:86-87` now regenerate but say nothing about rc≠0.
- Command: CE-7 (a `2026-10.30` PENDING row owned by ORACLE, in each clone).
- Observed: batch — spawn_list omits the row (0 hits, rc 0), buried-token ✅, lands-today does not see it; only `docket_view.py --write` says "DOCKET-VIEW ✗ rc 2 — L910: malformed date span '2026-10.30' (nothing written)". HEAD — gate line "generated calendar freshness | ⚠️ rc=2 · CANNOT-CERTIFY" on every run (the retired overdue check skipped the row too). The regen still catches it at the same frequency, so ⚠️ not ❌; but the failure is now outside gate.txt and has no instruction attached.
- Proposed: one clause at BOOT step 2 and CLOSEOUT step 1: "rc≠0 ⇒ the calendar is NOT current; fix the DOCKET line it names before relying on the calendar or spawn_list".

**⚠️ W4 — manual/agent text still describing retired checks.**
- Artifacts: `PROME/SYSTEM.md:42` "boot freshness check in `prome_gate.py`" (#20) · `PROME/SYSTEM.md:70` "`prome_gate` advisory drift check" (#24) · `.claude/agents/argus.md:34` = `PROME/.claude/agents/argus.md:34` "`docket_view.py` freshness … ran before the freeze and their verdicts are in PROME's closeout receipt" (#20 — no such verdict exists now, and ARGUS is told not to check it) · `PROME/tools/SESSION_PILOT.md:5` "BOOT.md step 5 owns the procedure" (BOOT step 5 has no presence procedure now) and `:38` "Without `--activity-state`, the boot gate collects current pending files…" (#33).
- Command: grep of the live manuals, runners, agents and registries for every retired check name.
- Proposed: reword the five places (both argus.md copies byte-identical so the parity gate stays green).

**⚠️ W5 — `PROME/ORCHESTRATION_PLAYBOOK.md:251`, rewritten by this batch, says the writer-side refusal "is proposed to DAEDALUS (packet 2026-10-15)"; it has been live since 2026-10-20.**
- Artifact: `scripts/orch_log.py:18-19, :204-219` (`append` refuses a ledger/view count mismatch unless `--acknowledge-unobserved K`); commits 1e997b58b and cf074c5fc (2026-10-20); test `scripts/tests/test_orch_log_view_L736.py`. `PROME/CLOSEOUT.md:36` ("the writer-side refusal is DAEDALUS's (packet 2026-10-15; L733)") is ambiguous the same way.
- Command: `git log -S acknowledge-unobserved -- scripts/orch_log.py`.
- Observed: the refusal is implemented. It is also the strongest evidence that retiring #37 is safe, and the receipt does not cite it.
- Proposed: "the writer has refused a hand-row delta since 2026-10-20 (L736)".

**⚠️ W6 — live DOCKET obligations still pointing at code this batch deletes (batch 1's W5 class).**
- Artifacts: `PROME/DOCKET.tsv` L736 (PENDING, due 2026-10-21): ② "`check_orch_log_observed` compares the view header's `source` path", ③ "run `orch_log.py check` + OBSERVED in `mode_boot` as ADVISORY", ⑦ the OBSERVED wording · L863 (PENDING, due 2026-11-05): "(parity) `docket_view.py:186` ᵒ tag … apply the dated rule there" — the dated rule (`_docket_overdue_annotated`) is deleted with #17.
- Command: awk over PENDING rows naming retired checks or deleted functions.
- Proposed: annotate in place, state token first: L736 ②, ⑦ and ③'s OBSERVED half VOID (#37); L863 parity leg VOID (#17).

**⚠️ W7 — departures from L908's letter not yet recorded as residue (each judged defensible).**
- #2 not done: `scripts/session_banner.sh` byte-identical to HEAD (`git diff HEAD --stat` empty). Defensible: the banner is the only env flag desk and cloud sessions see (`AGENTS/BRENT/demand_destruction/data/eia_2026-09-02.md:38` acted on "boot hook flagged `env_doctor FAIL`"); the gate's copy carries dependents and the WQ-238 tracker; < 1 s.
- #1 "today's rows only" not done: defensible — `PROME/tools/orch_closeout.py:6-7` "all unresolved prior-date touches … never aged away" (COMPLETION_SPEC lifecycle); the closeout line already separates today's named touches from the older count; the 217 KB boot read is gone.
- `summarize_generated` / `summarize_prose` kept as test-only gate code (`prome_gate.py:406-433`), against "unused functions with their tests". Tolerable.
- Proposed: list all three as NOT DONE with reason in the batch-2 execution receipt and in L908's disposition.

**⚠️ W8 — W4's parser rejects the emoji form of ⏰ and flags unrelated ⏰.**
- Artifact: `PROME/tools/prome_gate.py:923-925`.
- Command: CE-4.
- Observed: `⏰️ re-present <date>` (U+23F0 U+FE0F, what emoji pickers type) → "MALFORMED ⏰ #1 — write `⏰ re-present YYYY-MM-DD`…", i.e. it asks for what already looks identical; a quoted ⏰ in Notes, or a ⏰ in a URL in the Item cell → MALFORMED. Each is an ACTION OWED line at boot. All errors are in the loud direction. Live queue: 3 ⏰, none with U+FE0F; both HANDS markers (#31, #495) parse; #559 is a DECISION row.
- Proposed: `⏰️?\s*re-present`; optionally trigger MALFORMED only on ⏰ followed by some form of "re-present".

**⚠️ W9 — CLOSEOUT step 6 keys demotion on "(rc=1)".**
- Artifact: `PROME/CLOSEOUT.md:92` "at ≥75% of the `MEMORY.md` cap (rc=1), demote"; `prome_gate.py:1130` rc=2 text says only "OVER the boot-load cap".
- Observed: at ≥100% the script exits 2 (CE-6: 25,600 B → rc=2). The flow rule applies all the more, but a reader keyed on rc=1 skips it.
- Proposed: "(rc=1 or 2)"; add "demote at this closeout" to the rc=2 text.

**ℹ️ O1** — with the slate failed AND spawn_list timed out, the line reads only "TimeoutExpired: … spawn_list.py" — the slate status is lost (CE-3b); the line is still ⚠️.
**ℹ️ O2** — `prome_gate.py:1346` still prints "the standing WQ-249 backlog — not a boot read"; `:1116` docstring "plus the separately governed auto-memory cap". Cosmetic.
**ℹ️ O3** — `PROME/registry/READS.tsv:227` still names "the agent-freshness check" (batch-1 #7 residue, not this batch).
**ℹ️ O4** — `summarize_memory_length` says "caps file or index missing" when the cause is "not a git work tree" (rc=128, CE-6). Cosmetic; it says read the log.
**ℹ️ O5** — the author's `after_test_docket_state_predicate_L370.txt` reads "Ran 0 tests" (the file is a script). As a script it passes in both trees; so do `test_active_decisions_digest`, `test_contract_probe_acceptance`, `test_presence_reader_contract`. `test_gate_orch_summary` (no pytest) passes 8 + 1 skip in both trees under a 15-line shim (`reviewer/shim/`).
**ℹ️ O6** — the deleted OBSERVED tests were already unrunnable at HEAD (`test_orch_log_wiring_L733`: ImportError `orch_time`); the writer refusal has its own test (W5).
**ℹ️ O7** — L908's "manual prose first" ordering for #33/#37 cannot be checked from an uncommitted diff.
**ℹ️ O8** — `PROME/CLOSEOUT.md:62` ("`willq_view.py --check` parses…") stays true of the tool; `--write` itself refuses a surviving hand copy (`willq_view.py:184`), so regeneration covers both halves of the retired drift check.

## Per-item verdicts (1–17)

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | #33 session presence + `--sessions-json` | ACCEPT (W4) | No live caller passes the flag (repo-wide grep: only 2026-09 plans/patches); no `run_once`/`run_refresh` caller passes a second positional argument; session_presence.py untouched; PROME/tests 5/5 pass both trees. |
| 2 | #37 OBSERVED | ACCEPT (W5, W6) | Writer refuses hand-row deltas since 10-20; `orch_log.py check` still BLOCKING at closeout (gate run in `wt`). Not the only catcher. |
| 3 | #1 WQ-249 at closeout only | ACCEPT; "today only" not done, defensible (W7) | ast test: mode_boot has no `check_orch_closeout`, mode_closeout does; orch_closeout.py:6-7. |
| 4 | #2 env_doctor | NOT DONE; revert complete; defensible (W7) | `git diff HEAD --stat -- scripts/session_banner.sh` empty. |
| 5 | #13–15 GATES upkeep | ACCEPT | CE-5: every flag present under its own label; the 3 BLOCK lines unchanged. |
| 6 | #17 overdue-unannotated | ACCEPT (W6) | Today HEAD's check lists 17 rows (L170 … L828): all 17 are in the calendar's OVERDUE line and in spawn_list's D: rows (0 missing either way). |
| 7 | #20 calendar freshness | ACCEPT WITH RESIDUE (W3, W4) | BOOT step 2, both boot runners, Resume step 2, CLOSEOUT step 1 regenerate; docket_view writes only between markers (hand header preserved, checked). |
| 8 | #24 willq_view drift | ACCEPT (W4, O8) | willq_view.py sha256 matches its pin; BOOT 3b + CLOSEOUT step 2 regenerate. |
| 9 | #27 done rows | ACCEPT | Not in the closeout gate (test + gate run); boot ADVISE line present; CLOSEOUT step 7 runs it pre-freeze. |
| 10 | #32 spawn list + slate | ❌ X1 | CE-1, CE-2. |
| 11 | #35 MEMORY.md | ACCEPT (W9) | Boot gate runs the script, closeout gate does not, CLOSEOUT step 6 before the freeze — coherent with the flow rule. 75% boundary identical to HEAD (19,199 B ok / 19,200 B flagged in both); lines now measured too. |
| 12 | Dead code | ACCEPT (W7) | 15 functions + 8 globals deleted; zero code callers remain (only tests asserting absence); the only unreferenced survivors are the declared keeps (2 Deck checks, 2 summarizers); the 3 tests are pure renames. |
| 13 | W2 spine audit | ACCEPT | `node --check` OK; eligibility "1 or more days after today"; fire-time sentences gone; spineaudit copies identical; BOOT_MODULES row updated. |
| 14 | W4 HANDS ⏰ | ACCEPT (W8) | Colon form parses; rec-cell / M-D / bare → MALFORMED; impossible date named. |
| 15 | O2 Deck notes | ACCEPT | L580/L663/L734 carry the note; rows still lead with their state token (buried-token ✅); functions and the test assertion exist. |
| 16 | forge_validate | ACCEPT | GATES/DOCKET/FORGE save payloads exercised in `wt`: rc 0/0/0; DOCKET silent; FORGE prints its size advisory; no dead import or undefined name (ast). |
| 17 | Tests | PARTIAL (W1, W2, O5) | Uncommitted: every failing file has the same failure names as HEAD (10 files). Committed: test_gate_isolation 4 → 5. test_docket_row_cap (6 failures) missing from the claim. |

## Counterexamples (mine; all in disposable clones or temp fixtures)

| CE | Input | Command | Result |
|---|---|---|---|
| 1 | Due row, owner ORACLE (last self-commit 10/30) → DARK | `wt`: append the row; `python3 PROME/tools/spawn_slate.py --horizon 0`; then `guard(spawn_list_and_slate, "0", …)` | slate rc=1, slate written; line "slate NOT regenerated (spawn_slate.py rc=1 …) — do not read a stale slate" → ❌ X1 |
| 2 | UNKNOWN row; slate written, rc=2 | `reviewer/ce/ce_spawn.py` | same false "NOT regenerated (rc=2)" → ❌ X1 |
| 3a | Slate regeneration times out | `ce_spawn.py` | ⚠️ "slate NOT regenerated (TimeoutExpired …)" ✓ |
| 3b | Slate fails AND spawn_list times out | `ce_spawn.py` | line names only the spawn_list timeout (O1) |
| 4 | 10 HANDS rows: U+FE0F, fullwidth colon, capital R, quoted ⏰ + valid marker, quoted ⏰ only, ⏰ in a URL, bold marker, marker + time, malformed + valid future, colon + 2026-02-30 | `reviewer/ce/ce_queue_gates.py` | MALFORMED ×5 (incl. the look-alike U+FE0F, W8); RE-PRESENT ×3 ✓; malformed + valid future → silent; IMPOSSIBLE DATE ✓ |
| 5 | GATES: INSTRUMENT row with consumer passed + review passed + last_checked blank; JUDGEMENT row with empty consumed_by + review passed | `ce_queue_gates.py` | BLOCK "review_by passed — INSTRUMENT" names G-ALL-I; upkeep line lists "consumer: G-ALL-I …; consumer: G-ALL-J … EMPTY; JUDGEMENT review: G-ALL-J …; INSTRUMENT last_checked BLANK: G-ALL-I" ✓ |
| 6 | MEMORY.md 19,199 B / exactly 75% (19,200 B) / 25,600 B / 150 short lines / no caps file / no MEMORY.md / not a git tree | `reviewer/ce/ce_memory.py` (batch vs HEAD's retired check) | 19,199 ok both; 19,200 flagged both; 25,600 rc=2 (W9); 150 lines flagged now (HEAD missed it); missing inputs → UNKNOWN ⚠️ (never clean); non-git → UNKNOWN with the wrong cause text (O4) |
| 7 | DOCKET row dated `2026-10.30`, PENDING, owner ORACLE | each clone: append, run spawn_list / gate DOCKET checks / `docket_view.py --write`; HEAD's `check_calendar_views` | batch: invisible to spawn_list and lands-today, regen rc 2 "nothing written"; HEAD: gate ⚠️ "generated calendar freshness rc=2" (W3) |
| 8 | The batch as a commit | `wt` commit b5370de28 + full suite | test_gate_isolation MissingInput prints 15, needs > 20 (W1); everything else unchanged |
| 9 | #17 coverage | HEAD `check_docket_overdue` predicate vs today's calendar OVERDUE line and `spawn_list.py --horizon 0 --tsv` | 17 rows; 0 missing from either |
