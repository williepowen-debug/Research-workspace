# WQ-517 A fix pass 1: read #2 (narrow counterexample read of the IGNORE_FILES name test)

**Reader:** independent counterexample reader (Opus). Read-only against the repo. Run on 2026-10-24, finishing 19:53 ET (clock: `date`).
**Under test:** `PROME/tools/argus_contract.py:354`, `pending_only = target is None or (not state['commits'] and PurePosixPath(path).name not in IGNORE_FILES)`, with `IGNORE_FILES` defined at `:150`. Tests `test_z9`, `test_z9b` and `test_z9c` are in `PROME/tools/tests/test_argus_contract.py`. The code under test did not change during the run.
**Three versions per case:** each case runs against
- NEW, the live code;
- FIRSTCUT, the live code with only the fix-pass-1 name test removed (`old/argus_contract_FIRSTCUT.py`; `diff` shows that one line);
- PRE-REPAIR, `git show HEAD:PROME/tools/argus_contract.py`.

**Fixtures:** everything is under `/tmp/claude-1000/-home-willi-Research-workspace-PROME/b5ac7aae-a816-47d2-9613-7928715259e1/scratchpad/ce517b/`:
- `ce_tests.py` and `ce_tests2.py` are read #1's fixture scripts, copied unchanged.
- `ce_tests3.py` holds the new cases, CE-J to CE-N.
- `swap_firstcut.py` runs the author's `PerimeterPinTests` against a module you name.
- Raw output is in `run_F.txt`, `run3.txt`, `run2b.txt`, `run_suites.txt` and `run_swap.txt`.

Run with `cd <that dir> && TMPDIR=<that dir>/tmp python3 -m unittest ce_tests3` (or `ce_tests`, `ce_tests2`).

## ❌
None.

## ⚠️

**⚠️1 (CE-N2, CE-N3): a nested ignore file COMMITTED under a desk subject still hides an OWNED arrival at step 10, with rc 0. This happens in all three versions.**
- **Claim:**
  - DOCKET L835's appended note (`PROME/DOCKET.tsv:835`) says that after fix pass 1 "this row's scope stays the WORKING-TREE gate only".
  - `PROME/CLOSEOUT.md:98` says "the perimeter and ignore files stay strict (`UNCLASSIFIED`)" at the `--ref` verify.
- **Artifact:** `argus_contract.py:117` (`attributed_by_commit` skips only `never_advisory` paths) together with `:153-168` (`never_advisory` probes only the ignore file's own folder). The fix at `:354` covers pending paths only. A committed-only path never reaches it, because WQ-485 A attributes it at `:332` first.
- **Command:**
  - `CE3.test_ceN2_desk_commits_ignore_after_delivery_no_pending`: freeze; commit `PROME/result` as A; write an uncommitted `.claude/skills/newskill/SKILL.md` (OWNED); the desk commits `.claude/.gitignore` = `skills/newskill/` under the subject `BROCK: harness ignore`; then run `verify(ref=A)`.
  - `test_ceN3` is the same case with the ignore file committed between the baseline and the freeze.
- **Observed:** NEW, FIRSTCUT and PRE-REPAIR all return **rc 0** with no line about either path. The working-tree form also returns rc 0. Control: CE-F's run with no ignore file returns rc 1 `UNCLASSIFIED: .claude/skills/newskill/SKILL.md`.
- **Grade:** ⚠️, not ❌, for three reasons:
  - The behaviour pre-dates WQ-517 and is identical in all three versions, so this episode did not make the gate more lenient.
  - The path is not "advisory treatment of a pending-only path". It goes through WQ-485 A's commit attribution, which is a different ruling, so Will's 10/24 wording does not reach it.
  - L835's own body already names this form ("rc 0, no line when the ignore file is committed under a desk subject").

  What is wrong is the scope sentence: the new L835 note and `CLOSEOUT.md:98` both imply that step 10 is now safe from ignore files, and that is false for the committed route. The bound is unchanged: bytes do not ship.
- **Proposed change:**
  - Reword the L835 note to: "the PENDING route is strict at --ref/--snapshot; the COMMITTED-under-a-desk-subject route (attributed_by_commit) still hides at both gates".
  - Narrow `CLOSEOUT.md:98` to "pending ignore files".
  - L835 fix ②, which repairs `never_advisory` itself, closes all three consumers (`:117`, `foreign_pending`, and the working-tree branch). Port CE-N2 as a test when ② lands.

**⚠️2 (CE-M, CE-M2, CE-M3, CE-L): stricter than the letter. A desk's own deletion, rename or routine edit of a nested ignore or attributes file, made after the freeze, blocks step 10 while step 8 lists it as advisory.**
- **Claim:** Will allows advisory treatment for pending-only paths that are not OWNED and not PROME-evidenced. "Only" sets a ceiling, not a mandate.
- **Artifact:** `argus_contract.py:354`.
- **Command:**
  - `test_ceM_deleted_nested_ignore_file`: a tracked `AGENTS/BROCK/.gitignore`, deleted (porcelain ` D`).
  - `test_ceM2_rename_out_of_and_into_the_name`: `git mv .gitignore gi.bak` and `notes` to `sub/.gitignore`.
  - `test_ceM3_pending_edit_of_tracked_nested_ignore_file`: `AGENTS/BROCK/research/.gitignore` gains `*.log`.
  - `test_ceL_gitattributes_export_ignore_and_filter`: a new `AGENTS/BROCK/.gitattributes` with `* export-ignore` and `*.md filter=hide`.
- **Observed:**
  - NEW returns rc 1 `UNCLASSIFIED: <ignore file>` in each case.
  - FIRSTCUT returns rc 0 with an advisory line.
  - PRE-REPAIR returns rc 1, identical to NEW.
  - The working-tree form of CE-M3 returns rc 0 with an advisory line, unchanged.
  - In CE-M2 the non-ignore-named halves (`gi.bak`, `notes`) stay advisory under NEW.
- **Grade:** ⚠️. It errs strict, matches the pre-repair code, and is the outcome the acceptance intends ("every ignore file keeps the PRE-REPAIR strict behaviour"). The practical cost is that the step-8/step-10 race Will removed comes back for this one file class. L835's body notes this is common: 25 of 25 recent ignore-file commits were in research/sources folders. A deletion or rename only REVEALS paths, so it cannot hide anything.
- **Proposed change:** none in this episode. Declare it as residue. It belongs to L835's "live-fleet rule" question, which is Will's call.

**⚠️3 (CE-K): `.git/info/exclude` hides an OWNED arrival, with rc 0 in every version and at both forms.**
- **Artifact:** the inventory comes from `argus_scope.py:579` (`git status --porcelain`). `.git/` is outside porcelain, and `path_ok` rejects `.git` parts anyway.
- **Command:** `test_ceK_git_info_exclude_hides_owned`.
- **Observed:** NEW, FIRSTCUT and PRE-REPAIR all return rc 0, and the working-tree form returns rc 0. Porcelain lists nothing.
- **Grade:** ⚠️ out of scope, as expected. No path is involved, so no name test can see it. It is already declared in L835's residue ("`.git/info/exclude` leave no porcelain trace"). The same applies to `core.excludesFile` (none is set in the live repo: `git config --show-origin --get-regexp core.excludesfile` returns nothing) and to a filter driver defined in `.git/config`.
- **Proposed change:** none.

## ✅

| ID | Case | Command | Observed (NEW / FIRSTCUT / PRE-REPAIR) | vs letter |
|---|---|---|---|---|
| ✅1 | **Read #1 ❌1 closed: CE-F, CE-F2, CE-F3** (`.claude/.gitignore` over an OWNED skill; `AGENTS/.gitignore` and `AGENTS/BROCK/.gitignore` over a from-PROME packet) | `ce_tests.CE.test_ceF*` (`run_F.txt`) | rc 1 `UNCLASSIFIED: <ignore file>` / rc 0 (read #1's result) / rc 1. NEW matches PRE-REPAIR exactly | conforms |
| ✅2 | Working-tree form unchanged (CE-F4, CE-M3 WT, CE-N2 WT) | same files | rc 0 with an advisory line for the nested ignore file, as before. `target is None` short-circuits `:354`, so the name test cannot run at that form | unchanged. That gap is L835, out of scope |
| ✅3 | CE-J: `.claude/.GITIGNORE` = `skills/newskill/`, with and without `core.ignorecase=true` (ext4) | `test_ceJ_uppercase_GITIGNORE_with_and_without_ignorecase` | rc 1 `UNCLASSIFIED: .claude/skills/newskill/SKILL.md` in all three. Git does not read the variant, so the arrival stays visible. The variant itself is advisory under NEW | conforms. The variant has no power to hide anything |
| ✅4 | CE-J2: `.gitignore~`, `.gitignore.bak`, `.gitignore ` (trailing space), `.gitignore` plus U+200B, each = `inbox/`, over a from-PROME packet | `test_ceJ2_suffix_and_space_variants` | rc 1 `UNCLASSIFIED: …from-PROME_x.md` in all three. The variants are advisory under NEW/FIRSTCUT and strict under PRE-REPAIR | conforms |
| ✅5 | CE-J3: a DIRECTORY named `.gitignore/` holding a file named `inbox`, plus `AGENTS/.gitignore/.gitignore` = `*` | `test_ceJ3_directory_named_gitignore` | rc 1. The packet stays visible. Git did not list `AGENTS/.gitignore/.gitignore` at all: the inner file ignores itself (`*`), which is the "self-ignoring nested .gitignore" residue L835 already names. `AGENTS/BROCK/.gitignore/inbox` is advisory | conforms |
| ✅6 | CE-K2, K3, K4: nested repositories (`git init` in `AGENTS/BROCK/inbox/data/`; a `gitdir:` FILE at `AGENTS/NEWDESK/`; `.claude/` as a nested repo over an OWNED skill). Porcelain collapses each into one `?? <dir>/` entry that hides a from-PROME or OWNED file | `test_ceK2/K3/K4` | **rc 2 `CANNOT-EVALUATE: [Errno 21] Is a directory`** in all three versions and at the working tree | fails closed (rc 2 is "not a pass", `argus_scope.py:410`; blocking at standard/heavy, `CLOSEOUT.md:90`). This was a candidate ❌; it does not reproduce |
| ✅7 | CE-N: the desk commits `.claude/.gitignore` after the delivery, then pending-edits it | `test_ceN_desk_commits_ignore_after_delivery_then_pending_edit` | rc 1 `UNCLASSIFIED: .claude/.gitignore` in all three (it has commits, so it is not pending-only) | strict |
| ✅8 | Fix pass 1 changed no z1–z8 behaviour | `python3 swap_firstcut.py old/argus_contract_FIRSTCUT.py` vs the live module (`run_swap.txt`) | Under FIRSTCUT every `PerimeterPinTests` case passes except `test_z9`, `test_z9b` and `test_z9c`. Under the live code all pass. So z1–z8 (and y-series) are identical across the fix, and z9/z9b/z9c discriminate: each fails on the unfixed code | conforms |
| ✅9 | All of read #1's other outcomes unchanged | `run1.txt`+`run2.txt` vs `run3.txt`+`run2b.txt`, NEW rc lines (20 cases) | Only CE-F, CE-F2 and CE-F3 flip from rc 0 to rc 1. The other 17 labelled outcomes are byte-identical | no collateral change |
| ✅10 | Author's suites | `cd /home/willi/Research-workspace && python3 -m unittest PROME/tools/tests/test_argus_contract.py PROME/tools/tests/test_argus_scope.py` | **74 tests OK** (read #1 ran 71; this adds z9, z9b and z9c) | — |

## Counts
❌ 0 · ⚠️ 3 · ✅ 10.

Fresh counterexamples (16 test methods): CE-J, CE-J (ignorecase), CE-J2, CE-J3, CE-K, CE-K2, CE-K3, CE-K4, CE-L, CE-M, CE-M2, CE-M3, CE-N, CE-N2, CE-N3. Read #1's CE-F, CE-F2, CE-F3 and CE-F4 were re-run, and its remaining 17 fixtures were re-run as a regression check.

**Working tree:** I created no files in the repository and edited none; all fixtures live under the scratchpad. Between my start and end snapshots of `git status --short`, one path changed: ` M PROME/proposals/2026-10-24_wq505-486-517-493-488-RULED.md`. A concurrent session made that change, not this reader. The code under test (`git diff HEAD --stat`, 14 and 112 lines) was unchanged throughout.

**VERDICT: RESOLVED WITH RESIDUE.** Read #1's ❌1 is closed. CE-F, CE-F2 and CE-F3 now return rc 1, identical to the pre-repair code, and z1–z8 and the working-tree form are unchanged. No name variant, attributes file, deletion or nested repository makes the gate more lenient than the pre-repair code. The residue is three items:
- ⚠️1: a COMMITTED nested ignore file still hides at step 10. This pre-dates WQ-517, but the L835 note and `CLOSEOUT.md:98` now describe its scope wrongly.
- ⚠️2: a deliberate over-block of a desk's own ignore-file edits.
- ⚠️3: `.git/info/exclude`, already declared.
