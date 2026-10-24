# L796 ❌2 repair — independent counterexample read #3 (FINAL; fix pass 2)

> Saved verbatim by PROME 2026-10-24 18:3x ET from the reader's scratchpad ledger (Opus, general-purpose, read-only, disposable repos). Spawn: ORCH_LOG 2026-10-24 L796-PIN-READER touch 3. Fixtures: `PROME/reports/2026-10-24_L796-pin-counterexample-read3_fixtures/` (ce3.py, ce3b.py, run3.txt). Verdict NOT RESOLVED on ONE ❌ (nested ignore-file scoping judges the file's own folder, not its subtree); the episode's three-read ceiling is reached, so the disposition is in `PROME/tools/tests/ACCEPTANCE_closeout_gate_perimeter_pin_2026-10-24.md` § Results and DOCKET L835.

---

# L796 pin repair, fix pass 2: independent counterexample read #3 (FINAL in this episode's budget)

Reader: Opus, read-only against `/home/willi/Research-workspace`. Disposable repos only, under `l796-pin-read3/repos/`, with TMPDIR pointed at `l796-pin-read3/tmp`.
Fixtures: `l796-pin-read3/ce3.py` and `ce3b.py` (the Fx pattern is copied from read #2's `ce2.py`; the cases are my own). Raw output: `l796-pin-read3/run3.txt`.
Read: `git diff` of `argus_contract.py` and `test_argus_contract.py` against HEAD, all of `argus_contract.py` (394 lines), the ❌ and ⚠️ sections of read #2, the acceptance file, and `argus_scope.py` (`classify`, `_match`, `load_perimeter`, `porcelain_entries`, `authorship_evidence`).
Repo state: `git status --short` was identical before and after all runs.

Result: **❌ 1 · ⚠️ 2 · ✅ 9**

---

## ❌ findings

### ❌1. The ⚠️C scoping probe only tests a direct child of the ignore file's directory. It never asks what the file's SUBTREE can hide. So ignore files in `.claude/`, `AGENTS/`, `AGENTS/<X>/` (and, under one plausible reviewed row, the root) are unguarded even though they can hide OWNED or PROME-evidenced paths.

This is ❌A's shape moved to another directory.

- **Claim (VERIFIED):**
  - **How the probe works:** `never_advisory()` classifies one synthetic name, `<parent>/.ignore-probe`. It guards the ignore file only if that probe is not EXCLUDED.
  - **Why that is the wrong question:** a nested `.gitignore` hides untracked paths anywhere beneath its own directory. Under the real perimeter, several EXCLUDED directories contain more specific non-EXCLUDED rows beneath them:
    - `.claude/**` is EXCLUDED, but `.claude/agents/**` and `.claude/skills/**` are OWNED.
    - `AGENTS/**` is EXCLUDED, but `AGENTS/*/inbox/**` is SHARED, and a `from-PROME` packet there is PROME-evidenced and therefore blocks.
    - `scripts/**` is EXCLUDED, but it holds three SHARED file rows.
  - **Probe results with the pinned real rules (c2):**

    | Ignore file | `never_advisory` |
    |---|---|
    | `.claude/.gitignore` | False |
    | `AGENTS/.gitignore` | False |
    | `AGENTS/BRENT/.gitignore` | False |
    | `scripts/.gitignore` | False |
    | `.claude/agents/.gitignore` | True |

  - **What I demonstrated:**
    - **c4, OWNED hidden, all three gate forms pass.** After the freeze, PROME writes the OWNED file `.claude/agents/newdef.md`.
      - Control, no ignore file: rc 1 `UNCLASSIFIED: .claude/agents/newdef.md`.
      - Add `.claude/.gitignore` containing `agents/newdef.md`. Pending: **rc 0**, with only `FOREIGN-PENDING (advisory … EXCLUDED lane …): .claude/.gitignore`.
      - Committed under the subject `BRENT: harness ignore`: **rc 0, no line at all**.
      - Step 10 `--ref`: **rc 0**.
      - `git status --ignored` shows `!! .claude/agents/newdef.md`.
    - **c4b, pre-freeze.** The same desk commit made before the freeze is auto-attributed: freeze OK, `auto=['.claude/.gitignore']`, gate rc 0. This is exactly ❌A's N1c, in `.claude/`.
    - **c5, a PROME packet hidden by a desk-root ignore file.** A pending `AGENTS/BRENT/inbox/2026-10-24_from-PROME_task.md` gives rc 1 (PROME evidence).
      - Add a pending `AGENTS/BRENT/.gitignore` containing `inbox/*from-PROME*`: **rc 0**, with only that ignore file listed as advisory.
      - c6: `AGENTS/.gitignore` with `*/inbox/*from-PROME*` gives the same result, rc 0.
    - **d1, the root itself depends on an unrelated row.** I delivered and reviewed a perimeter row `.*  EXCLUDED  top-level harness dotfiles`. The root probe `.ignore-probe` then matches it, so the root `.gitignore` becomes unguarded.
      - A post-freeze root `.gitignore` edit that hides the OWNED `PROME/state/HANDOFF_X.md`: pending rc 0 (advisory); committed by `WALTER:` rc 0, silent.
      - The row is reviewed, but nothing tells the reviewer that it disarms the ignore guard.
  - **Real-world precondition (VERIFIED):** five desk-root ignore files are tracked today, all unguarded under fix pass 2: `AGENTS/CARL`, `AGENTS/LIQUID`, `AGENTS/OSPREY`, `AGENTS/TERRY`, `AGENTS/WALTER/.gitignore`. TERRY's already ignores `inbox/WILL/*`, which is a SHARED inbox lane. `.claude/.gitignore` does not exist today.
  - **Consequence bound (VERIFIED, c4_bound):**
    - The bound is the same as CE-G1 and ❌A: only UNTRACKED new files are hidden. A tracked OWNED edit under `.claude/.gitignore agents/` still blocks (c4_existing_tracked_owned, rc 1).
    - A plain `git add` of the hidden file refuses ("The following paths are ignored…").
    - A force-added commit fails step 10: `UNREVIEWED ACTUAL COMMIT PATH: .claude/agents/newdef.md`.
    - So an unreviewed OWNED or PROME-evidenced file sits invisible while the gate reads rc 0. It cannot ship silently.
  - **Why this is ❌ and not ⚠️:** rounds 1 and 2 graded CE-G1 and ❌A ❌ under exactly this bound, and fix passes 1 and 2 accepted that grade. The code also fails its own stated term. The `never_advisory` docstring says "guarded only where it can hide a non-EXCLUDED path under the PINNED rules". `.claude/.gitignore` can hide OWNED paths and is not guarded.
  - **Relative to earlier states:** compared with fix pass 1, this is a regression on the pending side, because pass 1 guarded every ignore file by basename. Compared with HEAD it is not a regression, because HEAD had no ignore guard at all. Read #2's ⚠️C warned about exactly this ("`AGENTS/<X>/` contains the SHARED `AGENTS/*/inbox/**`, so take care not to reopen the hole there").
- **Artifact:** `PROME/tools/argus_contract.py:159-168` (`never_advisory`, the single-probe test at `:166-168`); its callers at `:117`, `:203`, `:208`, `:266`, `:320`, `:386`; `PROME/state/AUDIT_PERIMETER.tsv` rows `.claude/agents/**`, `.claude/skills/**`, `AGENTS/*/inbox/**` (more specific, above) vs `.claude/**`, `AGENTS/**` (EXCLUDED).
- **Command:** `TMPDIR=…/l796-pin-read3/tmp python3 -B ce3.py c2 c4 c5 c6 c7 d1` and `python3 -B ce3b.py`.
- **Observed:** as quoted above. Verbatim lines are in `run3.txt` sections `c4_claude_gitignore_hides_owned`, `c4b_…`, `c5_…`, `c6_…`, `d1_…`, `c4_bound`.
- **Proposed change:**
  1. Guard the root `.gitignore` / `.gitattributes` unconditionally, without consulting the rules. The root can hide anything, including `PROME/**`. This closes d1.
  2. Leave a nested ignore file in directory D unguarded ONLY when BOTH hold:
     - the probe is EXCLUDED; and
     - no pinned rule with class ≠ EXCLUDED can match a descendant of `D/`.

     Use a segment-wise reachability test with `_match` semantics: a `**` segment reaches anything; `*` and `?` match within one segment; a pattern still unexhausted after D's segments are consumed reaches into D.
  3. Effect under the real perimeter:
     - Guarded: `.claude/`, `AGENTS/`, `AGENTS/<X>/` (via the inbox row) and `scripts/`.
     - Still advisory: `AGENTS/<X>/research/**`, `AGENTS/<X>/domain/**` and `PROME/inbox/**`. These are the common case: every ignore-file commit in the last 30 days that I listed was under `research/` or `sources/`.
     - Over-block cost: the five desk-root files, last edited 2026-04-17, 04-24, 06-26, 06-27 and 10-08.
  4. Add c4, c4b, c5 and d1 as tests.
  5. Alternatively, record ❌1 as declared residue with the bound above. This read is the last one in the budget, so a code fix made after it is unreviewed (Review budget, WQ-229 states).

---

## ⚠️ findings

### ⚠️2. The procedure texts still say every ignore-file edit is never advisory. Since fix pass 2, the code makes ignore files in EXCLUDED-probe directories advisory.
- **Claim (VERIFIED):**
  - CLOSEOUT.md:86 says "a `.gitignore`/`.gitattributes` edit is never advisory either, since it changes what the inventory can see".
  - ARGUS_CONTRACT.md:3 says "`.gitignore`/`.gitattributes` edits after the freeze are never advisory."
  - The code makes `AGENTS/BROCK/research/…/.gitignore` advisory (c1, and the author's own `test_y3`). Under ❌1 it also makes `.claude/.gitignore` and `AGENTS/<X>/.gitignore` advisory.
  - The texts overclaim the guard. A reader trusts that no ignore file can pass, and that trust is what hides ❌1.
- **Artifact:** `PROME/CLOSEOUT.md:86`; `PROME/tools/ARGUS_CONTRACT.md:3`; `argus_contract.py:153-168`.
- **Command:** `grep -n gitignore PROME/CLOSEOUT.md PROME/tools/ARGUS_CONTRACT.md`; `ce3.py c1`.
- **Observed:** the docs' sentences as quoted; c1 pending is `(0, ['FOREIGN-PENDING (advisory … EXCLUDED lane …): AGENTS/BROCK/research/2026-10-24_x/.gitignore', …])`.
- **Proposed change:** state the scope the code actually has, once ❌1 is disposed. For example: "outside a directory whose whole subtree the pinned rules class EXCLUDED".

### ⚠️3. The guard's `.gitattributes` half is justified by a weaker mechanism than its `.gitignore` half. NOT ESTABLISHED that it can hide a change in practice; it keeps the over-block in place for little measured benefit.
- **Claim (NOT ESTABLISHED / INFERRED):**
  - In d2, a root `.gitattributes` with `PROME/tracked.md ident` plus an edit inside `$Id: … $` did NOT hide the edit: porcelain still shows ` M PROME/tracked.md`.
  - INFERRED reason: git flags a size change as modified without running the clean conversion.
  - `export-ignore` and `diff` attributes do not touch status. A `filter=` driver needs `.git/config`, which is local state, the same family as residue ⚠️E.
  - Hiding by attributes is therefore at most same-size edits under `ident` / `text` / `eol` conversion.
  - The guard is harmless here: root `.gitattributes` is rare, and `AGENTS/MIDAS/.gitattributes` is the only nested one. No action is needed beyond knowing the justification is thin.
- **Artifact:** `argus_contract.py:150` (`IGNORE_FILES`).
- **Command:** `ce3.py d2`.
- **Observed:** `with ident attr, porcelain: ' M PROME/tracked.md\n?? .claude/.gitattributes\n?? .gitattributes …'`; gate rc 1 (on both `.gitattributes` and `PROME/tracked.md`).
- **Proposed change:** none required. Optionally note in the residue that the `.gitattributes` guard is precautionary.

---

## ✅ findings (VERIFIED with my own fixtures unless marked)

| # | Claim | Artifact | Command | Observed |
|---|---|---|---|---|
| 1 | **❌A closed, post-freeze.** A root `.gitignore` committed under `WALTER:` and hiding the OWNED `PROME/state/HANDOFF_X.md` (absent from porcelain) now blocks on the working tree AND at step 10. | `:117` (skip in `attributed_by_commit`), `:343-347`, `:357-367` | `ce3.py a1` | wt `(1, ['UNCLASSIFIED: .gitignore …'])`; step 10 `(1, ['UNCLASSIFIED: .gitignore …', 'UNCLASSIFIED SNAPSHOT PATH: .gitignore'])` |
| 2 | **❌A closed, pre-freeze.** The same commit before the freeze: the freeze refuses, both undelivered and when declared `observed`. | `:203-205`, `:208` | `ce3.py a2` | both `freeze REFUSED: changed since the baseline … deliver it …: .gitignore` |
| 3 | **❌A sibling.** A committed root `.gitattributes` after the freeze blocks on the working tree and at step 10. | `:117` | `ce3.py a3` | rc 1 both, `UNCLASSIFIED: .gitattributes` |
| 4 | **❌B closed, `observe()`.** `observe()` refuses the perimeter AND the root `.gitignore`, in both the working-tree form and the step-10 `ref=A` form. The gate stays rc 1 on both paths. | `:385-387` | `ce3.py b1` | four `observe REFUSED: … never observed-only …`; wt and step 10 rc 1 naming both paths |
| 5 | **❌B closed, `validate()`.** A hand-inserted `observed` entry for the perimeter or the root `.gitignore` (built with a valid `observation()`) gives rc 2 on the working tree and at step 10, and `mark_reviewed` refuses. | `:265-266` | `ce3.py b2` | `(2, ['CANNOT-EVALUATE: PROME/state/AUDIT_PERIMETER.tsv: never observed-only …'])`, same for `.gitignore`; `mark_reviewed: (2, 'REFUSED (CANNOT-EVALUATE) …')` |
| 6 | **⚠️C scoping, common case.** A desk's `AGENTS/BROCK/research/<dir>/.gitignore` is advisory pending (rc 0, one EXCLUDED-lane line) and silent once committed under `BROCK:` (rc 0). `PROME/.gitignore`, `FORGE/.gitignore`, root `.gitignore`, `AGENTS/BRENT/inbox/.gitignore`, `AGENTS/WALTER/inbox/WILL/.gitignore`, `memory/auto/.gitignore`, `.claude/agents/.gitignore` and an UNATTRIBUTED `newtop/.gitignore` are guarded; pending creation of each tested one gives rc 1.<br>**Inbox:** guarded, and correctly so — it can hide a PROME-evidenced packet, which otherwise blocks. Over-block cost: one tracked inbox ignore file, last edited 2026-07-06.<br>**`memory/auto/`:** guarded, which buys little (it hides only SHARED files that would be advisory unless filename-evidenced). Safe direction; no such file exists. | `:159-168` | `ce3.py c1 c2 c3`; `git log --since=2026-09-24 -- '*.gitignore'` | as stated; 25 ignore-file commits in 30 days, every one listed under `research/` or `sources/` |
| 7 | **⚠️D closed.** The pin's rules equal a parse of the delivered bytes, and `sha256` equals the delivered sha. A single read feeds both (`:138-142`). | `:132-147` | `ce3.py r3` | `pin sha==delivered: True; pin rules==parse of file: True` |
| 8 | **Missing-information neighbours fail closed.**<br>(a) A root `.gitignore` deleted by a desk before the freeze must be delivered; a delivered deletion (sha None) freezes and step 10 is rc 0.<br>(b) A deleted perimeter must be delivered; the pin is then `{sha256: None, rules: None}` and a foreign arrival is strict rc 1.<br>(c) A manifest with `perimeter.rules: null` or no pin key, whose `observed` names a nested research `.gitignore`, gives rc 2 CANNOT-EVALUATE. It never passes. The same manifest with rules pinned is rc 0, by design: that path is not guarded. | `:145-147`, `:164-165`, `:171-176`, `:266` | `ce3.py d3 d3b d4` | as stated |
| 9 | **Regression.**<br>AC6: `AGENTS/BROCK/new.md` pending gives rc 0 with one `FOREIGN-PENDING (advisory, owner UNVERIFIED — EXCLUDED lane, no PROME evidence)` line.<br>A desk's committed-only SHARED `memory/auto/f.md` after the freeze: rc 0 on the working tree and at step 10.<br>Delivered-perimeter happy path: step 10 rc 0; an arrival OWNED only under the NEW pin (`AGENTS/BRENT/x.md`) blocks.<br>**Suites** (TMPDIR = scratch): `test_argus_contract.py` 34 OK · `test_argus_scope.py` 28 OK · `test_argus_scope_evidence.py` 6 OK · `test_argus_r100_consumed_move_WQ289.py` 37 OK. | `:317-326`, `:103-129` | `ce3.py r1 r2 r3`; `python3 -m unittest PROME/tools/tests/<suite>.py` | as stated |

Probe-name collision (asked in scope 3): a row `PROME/**/.ignore-probe EXCLUDED` does not collide, because `**/` needs a further segment and `PROME/.gitignore` stays guarded (d5). The realistic collision is a broad dotfile row (`.*`), which d1 covers inside ❌1.

---

## Verdict

**NOT RESOLVED: ❌1.** ❌A and ❌B are closed as stated, and ⚠️C (common case) and ⚠️D are fixed. The ⚠️C scoping, however, decides whether an ignore file is guarded by classifying one probe name in its own directory, never by checking what its subtree can hide. As a result:
- `.claude/.gitignore` hides new OWNED `.claude/agents|skills/*` files at rc 0, pending or desk-committed, on the working tree, at step 10 and pre-freeze;
- `AGENTS/<X>/.gitignore` and `AGENTS/.gitignore` hide PROME-evidenced inbox packets at rc 0;
- a reviewed top-level `.*` EXCLUDED row would disarm the root guard.

The bound is the same as CE-G1 and ❌A: the hidden file cannot ship without `-f`, and step 10 catches a force-add. ⚠️2 (procedure texts overclaim the scope) and ⚠️3 (the `.gitattributes` mechanism is thin) are advisory only.
