# WQ-517 A / DOCKET L796 ❌1: independent counterexample read of `verify()`'s `pending_only` predicate

**Reader:** independent counterexample reader (Opus), read-only against the repo, 2026-10-24.
**Under test:** `PROME/tools/argus_contract.py:350`, which reads `pending_only = target is None or not state['commits']` (working-tree diff vs HEAD 3d0f802a0, 10 changed lines; the code under test did not change during the run).
**Fixtures:** `/tmp/claude-1000/-home-willi-Research-workspace-PROME/b5ac7aae-a816-47d2-9613-7928715259e1/scratchpad/ce517/ce_tests.py` and `ce_tests2.py`. Both subclass the author's `PerimeterPinTests`, so each repo is disposable, the REAL perimeter is committed at the baseline, and `sc.ROOT` is patched. Run with `TMPDIR=<scratchpad>/ce517/tmp`. Each case runs the NEW code through `sc.verify_review` and the PRE-REPAIR code (`git show HEAD:PROME/tools/argus_contract.py` → `old/argus_contract_HEAD.py`) on the same manifest. Raw output: `run1.txt`, `run2.txt` in the same folder.
**Author's suites re-run:** `python3 -m unittest PROME/tools/tests/test_argus_contract.py PROME/tools/tests/test_argus_scope.py` → 71 tests OK. My fixtures: 21 cases run.

## ❌

**❌1 (CE-F, CE-F2, CE-F3): step 10 now passes, rc 0, while an OWNED or PROME-evidenced uncommitted arrival is present.** A nested ignore file in an EXCLUDED folder now takes the advisory branch at `--ref` and hides that arrival. Before the repair, step 10 blocked on this.
- **Claim:** at `--ref`, "the perimeter and ignore files stay strict (`UNCLASSIFIED`)" (`PROME/CLOSEOUT.md:98`, the WQ-517 sentence), and OWNED or PROME-evidenced arrivals are never advisory (Will's letter).
- **Artifact:** `PROME/tools/argus_contract.py:350-351` (the ignore file passes `pending_only`) together with `:153-168` (`never_advisory` probes only `<folder>/.ignore-probe`, the ignore file's OWN folder, not the subtree its patterns govern).
- **Verification:** `CE.test_ceF_claude_gitignore_hides_owned_skill`, `test_ceF2_agents_gitignore_hides_prome_packet`, `test_ceF3_desk_lane_gitignore_hides_shared_inbox`. Steps: freeze → commit `PROME/result` (=A) → write an uncommitted arrival → write an uncommitted ignore file above it → `verify_review(ref=A, paths=['PROME/result'])`.
  - CE-F: `.claude/skills/newskill/SKILL.md` (OWNED) plus `.claude/.gitignore` = `skills/newskill/`.
  - CE-F2: `AGENTS/BROCK/inbox/2026-10-24_from-PROME_x.md` plus `AGENTS/.gitignore` = `*/inbox/*from-PROME*`.
  - CE-F3: the same kind of packet plus `AGENTS/BROCK/.gitignore` = `inbox/`.
- **Observed:** control with no ignore file → rc 1 `UNCLASSIFIED: .claude/skills/newskill/SKILL.md`. With the ignore file, NEW code → **rc 0**; the only line is `FOREIGN-PENDING (advisory … EXCLUDED lane …): .claude/.gitignore` (`AGENTS/.gitignore` and `AGENTS/BROCK/.gitignore` in F2 and F3); `git status --ignored` shows `!! .claude/skills/newskill/SKILL.md`. PRE-REPAIR → rc 1 `UNCLASSIFIED: <ignore file>` in all three. CE-F4 shows the same rc 0 at the working-tree form, which is the known hole DOCKET L835. What WQ-517 changes is that the step-10 backstop is gone too.
- **Grade:** ❌, more lenient than the letter. The net outcome is an OWNED or PROME-evidenced pending arrival passing step 10. Mitigations, stated plainly: this is L835's registered hole extended rather than a new mechanism; the bytes-do-not-ship bound still holds (`git add` refuses an ignored path, and a force-added commit fails as `UNREVIEWED ACTUAL COMMIT PATH`); the precondition is two post-freeze arrivals. However, `CLOSEOUT.md:98` now says ignore files stay strict at step 10, which is false for this case. The L835 row (`DOCKET.tsv:835`) scopes the weakness to "the working-tree gate" and "the pre-commit gate is weakened", which now understates it.
- **Proposed change (pick one):**
  - (a) Minimal, restores pre-repair step 10 for every ignore file: make line 350 `pending_only = target is None or (not state['commits'] and PurePosixPath(path).name not in IGNORE_FILES)`, and add CE-F/F2/F3 as `test_z9…` at `--ref`.
  - (b) Implement L835 ② now (a pattern-prefix test over the pinned rules), which closes both forms.
  - Either way, correct the L835 row's scope sentence. If neither is done, reword `CLOSEOUT.md:98` to the true scope and add "step 10" to L835.

## ⚠️

**⚠️1 (CE-G, CE-G2, CE-G3): the comment's "hence" is false when HEAD does not descend from the target, and the advisory line then mislabels the path.** rc stays 1 through a backstop.
- **Claim:** "no commit in baseline..HEAD, hence outside the delivery commit and outside baseline-to-target history" (`argus_contract.py:345-346`; same wording in `CLOSEOUT.md:98`).
- **Artifact:** `argus_contract.py:287` (the inventory is built against HEAD, not the target) and `:350`. The backstop is `:365-375`, the `changes(baseline, target)` loop.
- **Verification:**
  - CE-G: side branch from A → `BROCK: z` commit P; checkout master; leave `AGENTS/BROCK/z.md` untracked locally; `verify_review(ref=A, snapshot=P)`.
  - CE-G3: freeze → desk commit `AGENTS/BROCK/h.md` → `PROME -> BROCK: p` commit of `AGENTS/BROCK/p.md` → A=commit `PROME/result` → `git reset --soft <baseline>` → `verify_review(ref=A)`.
- **Observed:** CE-G → rc 1, with both `UNCLASSIFIED SNAPSHOT PATH: AGENTS/BROCK/z.md` AND `FOREIGN-PENDING (advisory …): AGENTS/BROCK/z.md`. CE-G3 → rc 1 via `UNCLASSIFIED SNAPSHOT PATH` for both paths, plus advisory lines saying "**no PROME evidence**" for `p.md`, whose commit in baseline..target has a `PROME ->` subject. Pre-repair printed `UNCLASSIFIED` instead. Outcome strict; the labels are wrong.
- **Proposed change:** reword the comment and doc to say "no commit in baseline..HEAD; history in baseline..target is enforced separately by the snapshot-path loop". Optionally drop the advisory line for any path that also produced an `UNCLASSIFIED SNAPSHOT PATH` error.

**⚠️2 (CE-A): stricter than the letter for a foreign commit in delivery..HEAD followed by a pending edit.**
- **Claim:** advisory is allowed for pending paths "outside … baseline-to-target history" (Will).
- **Artifact:** `argus_contract.py:350` keys on baseline..HEAD.
- **Verification:** `test_ceA_head_past_delivery_foreign_commit_then_pending`: A=delivery; `BROCK: desk note` commits `AGENTS/BROCK/y.md` after A; then a pending edit to it; `--ref A`.
- **Observed:** rc 1 `UNCLASSIFIED: AGENTS/BROCK/y.md`, identical to pre-repair. The commit is outside baseline..A, so the letter would permit advisory.
- **Proposed change:** none required (it errs strict; AC2 chose baseline..HEAD on purpose). Declare it as residue.

**⚠️3 (CE-E): lookalike lane names are advisory at `--ref`.**
- **Artifact:** `argus_scope.py:82-108`; matching is case-sensitive with first match wins.
- **Verification:** `test_ceE_case_and_prefix_lookalikes`.
- **Observed:** `prome/state/x.md`, `Prome/state/x.md`, `PROMEX/state/x.md` and `forge/x.md` are UNATTRIBUTED; `PROME/inbox/x.md` is EXCLUDED. All advisory, rc 0. On this ext4 checkout these are genuinely different directories, and none can enter the delivery commit unreviewed. This matches the letter ("not OWNED under the pinned rules").
- **Proposed change:** none in this repair. Whether UNATTRIBUTED arrivals should block stays the L796 rule question already declared as residue.

## ✅

| ID | Case | Observed | vs letter |
|---|---|---|---|
| ✅1 CE-B | Pending deletion of a foreign tracked file, `AGENTS/BROCK/old.md` | rc 0, advisory (pre-repair rc 1) | conforms: pending-only, not OWNED, not evidenced |
| ✅2 CE-B2 | Pending deletion of OWNED `PROME/old` plus the perimeter | rc 1, both `UNCLASSIFIED`, no advisory | strict as required |
| ✅3 CE-C | Staged `git mv PROME/old AGENTS/BROCK/old` | the origin gets a synthesized ` D` and is `UNCLASSIFIED`, rc 1; destination advisory | OWNED half strict |
| ✅4 CE-C2 | Staged rename inside a foreign lane | rc 0, both paths advisory | conforms |
| ✅5 CE-C3 | Desk moves a committed from-PROME packet to `processed/` (pending) | rc 1, both `UNCLASSIFIED` | strict (PROME-evidenced); over-block is declared ⚠️4 residue |
| ✅6 CE-D | Staged-only new foreign file (index `A `) | rc 0, advisory | conforms; staged bytes cannot enter the delivery commit already verified by its actual paths |
| ✅7 CE-D2 | Mode-only change and staged-then-reverted (working bytes == committed bytes) | foreign paths advisory; OWNED `PROME/old` with a mode-only change → `UNCLASSIFIED`, rc 1 | conforms |
| ✅8 CE-A2/A3 | Later PROME-subject commit after the delivery, alone or followed by a desk's pending edit | rc 1 `UNCLASSIFIED`, no advisory | strict |
| ✅9 CE-H | rc 0 with only advisories; then a later unreviewed PROME commit on top of the delivery | rc 0, then rc 1 `UNCLASSIFIED: PROME/later` | the push of HEAD stays covered, because the inventory spans baseline..HEAD |
| ✅10 CE-I | Historical dependency's live file edited after the commit | rc 0, advisory; the dependency stays pinned to its commit (`validate()`) | conforms ("dependencies strict" = the pinned version) |
| ✅11 CE-I2 | Current dependency edited after the commit | rc 0 at `--ref` and rc 1 at the working tree, identical pre- and post-repair | unchanged by this repair (committed bytes are verified) |
| ✅12 | Author's AC1–AC8 (`test_z1`–`test_z8`) plus both suites | 71 tests OK | the original defect, CE1/CE9, is closed |

## Counts

❌ 1 · ⚠️ 3 · ✅ 12. Counterexamples: CE-A, CE-A2, CE-A3, CE-B, CE-B2, CE-C, CE-C2, CE-C3, CE-D, CE-D2, CE-E, CE-F, CE-F2, CE-F3, CE-F4, CE-G, CE-G2, CE-G3, CE-H, CE-I, CE-I2.

**Working tree:** the code under test was unchanged throughout. `git status --short` did differ between start and end, but every difference came from concurrent sessions, not from this reader: commits c15740f5d and 3d0f802a0 committed the two inbox packets; the RULED proposal and two read reports were staged; `CLAUDE.md`, `FORUM/README.md` and `PROME/state/ORCH_*` were modified. All my fixtures live under the scratchpad.

**VERDICT: NOT RESOLVED.** The named defect (CE1/CE9) is fixed and AC1–AC8 hold, but ❌1 is of the class the ruling names: an OWNED or PROME-evidenced pending arrival passes the `--ref` verify with rc 0, hidden by a nested ignore file that now takes the advisory branch there. `CLOSEOUT.md:98` says the opposite. Fix (a) is a one-line restoration.
