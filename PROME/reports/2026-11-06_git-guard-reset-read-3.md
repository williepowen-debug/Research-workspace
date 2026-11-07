# Counterexample read 3: git_guard reset repair, 2026-11-06 (last allowed read, diff only)

**Verdict: the regression is gone and the guard is safe to leave live, but it is NOT FIXED against its acceptance file. 5 ❌ (one by the brief's letter only), 3 ⚠️.** No real command that HEAD blocks now passes. Read 2's ❌1 to ❌5 all give the right result. Four new defects remain: two forms that clear the shared index still pass, and two ordinary path forms now block.

**State per WQ-229:** IMPLEMENTED, TESTED by the author (suite 82/82, re-run here). Not INDEPENDENTLY VERIFIED.

**Scope:** diff against HEAD 577648987c, confirmed byte-identical to `guard.diff` before starting. No repository file edited; `git status` for the five repair paths is unchanged. Real resets ran only in temp repos under the scratchpad, each after asserting `rev-parse --show-toplevel` equals the temp directory, and each went to `trash`.

## Method

| Step | Size | Scratchpad artifact |
|---|---|---|
| Real commands through HEAD and working tree, whole guard and rule by rule | 793 transcripts, all 43 project dirs, 14,330 distinct commands containing `git` | `r3_replay.py`, `r3_replay.out` |
| Generated: 35 payloads × 21 prefixes × 20 suffixes × 5 spacings | 73,500 | same |
| Random token fuzz | 400,000 | same |
| In-process verdict against the real script's exit code | 155 commands, 0 mismatches | same |
| Read 2's full case list, plus fresh forms, by stdin | 263 + 151 | `r3_cases.py`, `r3_cases.out` |
| What git really does per form | 44 forms | `r3_truth.py`, `r3_truth.out`, `r3_fix.out` |
| How often each shape occurs in real commands | 14,334 distinct | `r3_freq.py`, `r3_freq.out` |
| Scratch candidate fix, never written to the repo | | `r3_fix.py`, `r3_candidate.py`, `r3_fix.out` |

## Question 1: other RULES

| Check | Result |
|---|---|
| Regex text of the 5 other RULES | Identical to HEAD (asserted) |
| Real commands, per-rule difference | **0 of 14,330** |
| Real commands, whole guard | 14,311 allowed by both · 14 blocked by both · 5 newly blocked · **0 blocked at HEAD and allowed now** |
| The 5 newly blocked | All real resets: 2 `reset -q --hard`, VULCAN's `reset -q 2>/dev/null`, VIOLET's `reset -q; date` twice. 0 false positives |
| Generated set | **0 narrowed**. 20,088 newly blocked, every one holds a line continuation |
| Fuzz | 3 narrowed, all one shape, see ❌5 |
| Runtime | Slowest pair of guard calls 2.4 ms |

**Answer: yes, apart from line continuations, with one shape as the exception.** Why it holds: the join changes only `\<newline>` to a space, outside heredoc bodies, so it can only let a rule match more, except where a following `\S+` then takes a different word. That exception is `-C` with its value on the next line, ❌5.

## Question 2: read 2's ❌1 to ❌5

| Item | Result | Note |
|---|---|---|
| ❌1 `_QUOTED` typo hides rules | **Right.** 45/45 across A-groups | Regex is back to HEAD's text |
| ❌2 `'#'` skips the reset rules | **Right.** 7/7 | Comment skip removed. `# note \<newline>git reset -q` also blocks |
| ❌3 quoted command substitution counts as a path | **Right.** 11/11 | Placeholder removed. See ❌1 and ❌2 below for what that removal reopened |
| ❌4 `<ref> --` | **Right.** 5/5 | |
| ❌5 whole-tree spellings | **Right.** 23/23 as read 2 named them | A further spelling passes, see W1 |

Read 2's 263 cases now: 46 wrong against read 2's labels, 22 of those right at HEAD. The 22: 10 are the two declared costs, 6 are W1 and 2 are W6 of read 2, 4 are W4. The other 24 are wrong at HEAD too.

## ❌ Blocking defects

### ❌1. A quoted `-C` directory with a space hides the reset, `--hard` included (fresh)

- **Claim:** Property 2, "`--hard` is blocked in every position." Property 1. Design statement, "every doubt about a reset fails closed."
- **Artifact:** `git_guard.py:37` and `:55`. The string is dropped to a space, so `-C\s+\S+` takes `reset` as the directory and the subcommand is never seen.
- **Command:** `r3_cases.py` group B-C-dropped; `r3_truth.py`.
- **Observed:** VERIFIED rc=0 at both HEAD and working tree. `git -C "$(git rev-parse --show-toplevel)" reset --hard` cleared all 4 staged files and reverted A.md from 2 to 1. The same form with `reset -q`, and bare `reset` from a desk subdirectory, cleared all 4. `git -c "a=b c" reset` also passes. Read 2 held these as blocked, by the placeholder now removed. Not a regression from HEAD. 0 such `-C` forms in 14,334 real commands.
- **Proposed change:** in `_RESET` only, make the `-C`/`-c` value optional, leaving GIT and the other RULES alone: `GIT.replace(r"-C\s+\S+|-c\s+\S+", r"-[Cc](?:\s+\S+)?")`. TESTED on the scratch candidate, see the table below.

### ❌2. A quoted redirect target with a space leaves `>` as a "path" (fresh)

- **Claim:** Property 1, "whatever follows it on the line."
- **Artifact:** `git_guard.py:57` needs a target, the target was dropped, so `>` survives. `:66` does not treat it as wide.
- **Command:** `r3_cases.py` group A-dropped-redirect; `r3_truth.py`.
- **Observed:** VERIFIED rc=0 at both guards. `git reset -q > "log file.txt"`, `git reset > "a b" && ls` and `git reset -q 2>"$(mktemp -d)/e log"` each cleared all 4 staged files. Right in read 2's version, wrong now. 0 real occurrences.
- **Proposed change:** add `<`, `>` and `\` to the character class at `:66`. This also closes read 2's W3 (`find -exec git reset -q \;`) and the `>|` half of W2. TESTED on the candidate.

### ❌3. A literally named file above the current directory blocks (fresh, false positive)

- **Claim:** Property 2, a reset that names a path is allowed when it touches only that path. Not one of the two declared costs. A desk's cwd is `AGENTS/<NAME>/`, and carve-out ① has desks staging packets in another desk's inbox.
- **Artifact:** `git_guard.py:62-66`, `n.startswith("../")` refuses every path that starts upward, where only `../..`-shaped paths are wide.
- **Command:** `r3_cases.py` group F-paths-allow; `r3_truth.py`; `r3_freq.py`.
- **Observed:** VERIFIED old=0 new=2: `git reset -q -- ../PROME/x.md`, `git reset ../X/a.md`, `git reset -q -- ../../AGENTS/WALTER/inbox/2026-11-06_x.md`. Truth from a subdirectory: `git reset -q -- ../E.md` unstaged that file only, 3 of 4 stayed staged. The message says "name the files after --", which the command already did. Frequency: 1 real `git add … ../VULCAN/inbox/…` in 14,334, 0 real `git reset ../…`, so the form is real and rare.
- **Proposed change:** normalize, and treat a path as wide only when nothing but `.` and `..` remains: `n = posixpath.normpath(a) if a else "."`, then `all(p in (".", "..") for p in n.split("/"))`. Also closes W1's `sub/..` forms. TESTED on the candidate.

### ❌4. A file named by a shell variable blocks (fresh, false positive)

- **Claim:** The brief, false positives on ordinary path-scoped desk work are ❌. Not one of the two declared costs. House style names files by variable.
- **Artifact:** `git_guard.py:66`, `$` in the wide class. `:85`.
- **Command:** `r3_cases.py` group F-paths-allow; `r3_truth.py`; `r3_fix.py`; `r3_freq.py`.
- **Observed:** VERIFIED old=0 new=2: `git reset -q -- "$f"`, `for f in a.md b.md; do git reset -q -- "$f"; done`, `git reset -- "AGENTS/$NAME/STATUS.md"`, `git reset -q -- "$PKT" 2>/dev/null`. Truth: `f=A.md; git reset -q -- "$f"` unstaged A.md only. Frequency: 1,660 real `git add` or `git commit` commands name a path by variable, 0 real resets do, so this is the natural recovery shape and it has not yet been tried. It fails loud, and the message again says to do what the command did.
- **The block also has a real reason.** `F=; git reset -q -- $F` cleared the whole index, while the quoted `"$F"` is rc=128 and harmless. The guard cannot tell the two apart because quotes are stripped before the walk. Allowing `$` after `--` would reopen a true global unstage.
- **Proposed change:** owner's ruling, not a code change: keep the block, add it to the declared costs in the acceptance file, and change the message at `:86` to say a path must be written literally. Grading it ❌ reflects the brief's rule; I would not reverse the block.

### ❌5. Letter only: commands blocked at HEAD and allowed now are all commands git refuses, or a real path

- **Claim:** The brief, any command blocked at HEAD and allowed now is ❌.
- **Artifact:** `git_guard.py:135` with `:37`. After the join, `-C` takes the subcommand as its value. HEAD took the `\` as the value. For reset, `:58` is anchored where HEAD's `HEAD\b` was not.
- **Command:** `r3_replay.py` fuzz; `r3_cases.py` group H-narrow; `r3_truth.py`.
- **Observed:** VERIFIED head=2 new=0.
  - Other RULES: `git -C \<newline> commit --amend -m x`, `git -C \<newline> add -A`, `git -C \<newline> push --force`, `git -c \<newline> add -A`. Git really receives `-C commit --amend` and refuses it, rc=128 or 129, nothing staged or moved. 0 real occurrences.
  - Reset: `HEAD:sub`, `HEAD:A.md`, `HEAD..v1`, `HEAD}`, `HEAD,`, `HEAD\;`, `HEAD\`, each rc=128, index unchanged, with `git reset HEAD/x` also refused while no such path exists.
  - `git reset HEAD.md` with the file present unstaged that file only, which is what Property 2 wants.
- **Proposed change:** none in code. Write one line into the acceptance file. Nothing protective was lost.

## ⚠️ Residue

### W1. Spellings that pass the walk (fresh)

- **Claim:** Property 2, "`--hard` is blocked in every position" and "touches only that path". Why not ❌: each needs a spelling no agent has written, 0 in 14,334, and the mode forms also need a bare ref, which is the undecidable residue.
- **Artifact:** `git_guard.py:62-66`; `:77-80`, exact-string mode tests.
- **Command:** `r3_cases.py` groups C-abbrev, D-wide; `r3_truth.py`.
- **Observed:** VERIFIED rc=0 at both guards. Whole-tree spellings, each clearing all 4: `git reset sub/..`, `git reset -- sub/desk/../..`, `./sub/../`, `git reset -- <repo toplevel>` as an absolute path, `git reset -- ~+`. Abbreviated modes, which git accepts: `git reset --har v1` moved HEAD, cleared the index and reverted A.md; `--ha v1` the same; `--mix v1` and `--sof v1` moved HEAD. Named top-level directory: `git reset -- AGENTS` unstages everything under it, with A.md and HEAD.md left staged; this one is declared residue, not a spelling.
- **Proposed change:** the normalize in ❌3 closes the `..` forms. Treating a leading `/` or `~` as wide closes the rest, at the cost of blocking an absolute path to a real file; the candidate does this and it hits 0 real commands. For modes, block any `--` option that is a prefix of a mode. Untested.

### W2. Other commands the doubts now block (fresh, only widens)

- **Claim:** Property 2 and ordinary commands stay allowed. Why not ❌: not ordinary, 0 real occurrences for each, and all fail loud.
- **Artifact:** `git_guard.py:66`, `:82`, `:85`; `\bgit` in GIT at `:37`.
- **Command:** `r3_cases.py` groups F-paths-allow, G-not-reset.
- **Observed:** VERIFIED old=0 new=2:
  - Narrow globs: `git reset -q -- AGENTS/X/inbox/*.md`, truth-tested as touching only its match.
  - Piped lists: `echo A.md | xargs git reset -q --`. Truth-tested as unstaging A.md only. Blocking this is right on an empty list, per read 1's X2. 3 real `xargs … git add` commands.
  - A ref plus named path: `git reset origin/master -- A.md`, `git reset -q HEAD~0 -- A.md`. Only touches A.md, and the message wrongly says global unstage. `git reset v1 -- A.md` is allowed, so the two disagree.
  - Help: `git reset --help`, `git reset -h`.
  - Unquoted words: `echo git reset`, `man git reset`, `cd .git reset`, `python3 tools/git reset`.
- **Proposed change:** test `_REFLIKE` only when no path follows `--`, but keep the HEAD block that acceptance requires. Add the help options to the walk. Declare the rest.

### W3. Read 2's residue, status

| Item | Status |
|---|---|
| W1 `_REFLIKE` | Partly closed. `HEADER.md` is allowed. `origin/notes.md`, `upstream/x.md`, `backup~`, `notes~1.md`, `a^b.md`, `@notes.md` still block; `--` is the way through |
| W2 redirect forms | Open: `>|`, `<<<`, `{fd}>x`, `git >/dev/null reset -q` |
| W3 `find -exec … \;` | Open, closed by ❌2's change |
| W4 join widens `.*` in add and commit | Open, generated `git add A.md && \<newline> ls -A` blocks. 0 real commands |
| W5 bare refs | Open. `git reset master` and `refs/heads/master` pass. Truth: `refs/tags/v1` cleared the index and moved HEAD. **The acceptance file still does not declare this** |
| W6 `--mixed -- A.md`, `--pathspec-from-file=` | Open |
| W7 `_SHELL_C` not escape-aware | Not re-run. Regex text unchanged from HEAD |
| W8 partial globs | Closed by refusing all globs, cost in W2 above |

## Candidate fix, scratch only

`r3_candidate.py`, three lines plus `_wide_path`. **It is unreviewed.** This was the last read, so applying it leaves the WQ-229 state at TESTED, not INDEPENDENTLY VERIFIED.

| Check | Result |
|---|---|
| Suite | 82/82 |
| Read 2 cases wrong | 46 down to 38; the 8 that moved all moved right |
| Fresh forms | 28 of 28 right, including ❌1, ❌2, ❌3 and the `..` and absolute forms of W1 |
| Real commands, against the working tree | 0 of 14,335 differ |
| Still open | ❌4 and ❌5 by design, `--har`, W2, bare refs |

## Held

| Shape | Result |
|---|---|
| Path-scoped desk forms | Right: `git reset -- AGENTS/X/STATUS.md`, `-q`, several files, `.gitignore`, `./STATUS.md`, `git -C ../.. reset -- …`, a trailing `2>/dev/null`, `&& git status`, `# comment` |
| Quoted prose | Right: commit messages, heredoc bodies, `python3 -c`, `git log --grep=reset`, `git bisect reset`, `git reset-notes` |
| Reset followed by shell syntax | Right: `&`, `&&`, `\|`, `)`, `;`, `if … ; then` |
