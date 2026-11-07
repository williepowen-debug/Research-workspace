# Counterexample read 2: git_guard reset repair, 2026-11-06

**Verdict: NOT FIXED, and not safe to save as it stands. 5 ❌, 8 ⚠️.** X1 to X6 now give the right result, X7 is 3 of 4, but the `_QUOTED` change has a regex typo that hides `git add -A`, `git add .`, `commit --amend`, `commit -a` and `push --force` from rules HEAD enforces. A real WALTER `git commit -q --amend` command that HEAD blocks passes the working-tree guard.

**State per WQ-229:** IMPLEMENTED, TESTED by the author (suite 68/68, re-run here). Not INDEPENDENTLY VERIFIED. The working-tree guard is live for every desk, because the hook reads this file directly (read 1 Held, grep only): the ❌1 regression is in effect now, uncommitted.

**Scope:** the diff, against the working-tree `PROME/tools/hooks/git_guard.py`, by stdin. No repository file edited; `git status` for the four repair paths is unchanged. Real resets ran only in throwaway repos under the scratchpad, with `rev-parse --show-toplevel` asserted equal to the temp directory first. One scratch file of my own (`redir.tmp`, a test redirect target) was removed with `rm`, not `trash`.

## Method

| Step | Size | Artifact in the scratchpad |
|---|---|---|
| X1 to X7 plus fresh cases through HEAD, working tree, and a one-token repair copy | 263 cases | `read2.py`, `read2.out` |
| Real git behaviour per form | 30 forms | `git_truth2.py`, `truth2.out`, `read2b.py` |
| Real fleet commands replayed through all three | 788 transcripts, 14,254 to 14,271 distinct commands containing `git` (the count moved between runs, the transcripts are live) | `replay2.py`, `replay2.out`, `read2c.py`, `read2c.out` |
| Candidate repairs on scratch copies only | `git_guard_FIX1.py`, `git_guard_FIX2.py` | `read2d.py` |

**Harness tally:** 60 of 263 cases are regressions against HEAD (wrong now, right at HEAD). By cause: 37 `_QUOTED`, 7 QUOTEDARG, 2 comment skip, 10 `_REFLIKE`, 4 continuation join. The other wrong cases were already wrong at HEAD; many are deliberate probes of undecidable residue, so the count is not a defect count.

## Question 1: X1 to X7

| Item | Result | Note |
|---|---|---|
| X1 redirect, comment, backtick | 10/10 right | VULCAN's form `git reset -q 2>/dev/null; S=…` blocks, also in the verbatim transcript replay |
| X2 `--` with nothing after | 7/7 right | Sibling `<ref> --` is ❌4 |
| X3 whole-tree pathspecs | 9/9 right as named | Same class outside the literal set is ❌5 |
| X4 `@`, remote refs, mode plus ref | 11/11 right | |
| X5 line continuation | 5/5 right | |
| X6 quoted path with a space | 4/4 right | Cost is ❌3 |
| X7 escaped quotes in a message | **3/4, fail** | `git commit -m "x \"git reset; y\" z" A.md` is old=0 new=2. The 3 that pass, including the suite's own fixture, pass by accident, see ❌1 |

## ❌ Blocking defects

### ❌1. `_QUOTED` typo: a backslash inside a double-quoted string hides every rule, a regression in all the other RULES

- **Claim:** Diff intent, an escape-aware string match (read 1's `"((?:[^"\\]|\\.)*)"`). Brief: a regression in the other RULES is the worst finding.
- **Artifact:** `git_guard.py:87`. It is a raw string written with Python-escape doubling: `(?:[^\"\\\\]|\\\\.)*`. `\\\\.` means two literal backslashes then a character, so a single backslash matches neither branch. Any double-quoted string containing one backslash fails to match at its opening quote. The regex then pairs that string's CLOSING quote with the next string's OPENING quote and drops everything between as prose, across lines.
- **Command:** `read2.py` groups A-add-A, A-add-dot, A-amend, A-force, A-commit-a, A-nospace, B-prose; `read2b.py` prints the scan; `replay2.py` and `read2c.py` real commands.
- **Observed:** VERIFIED.
  - Scan: `echo "a\b"; git add -A; echo "c d"` becomes `echo "a\b QUOTEDARG c d"`.
  - Rule hiding: 31 of 31 cases old=2 new=0, across all five non-reset rules. Examples: `grep -E "foo\|bar" f.txt; git add -A; echo "all done"`, `printf "x\n" && git commit -a -m x && echo "done now"`, and a commit message containing `\$6.66` followed on a later line by `git push --force origin master`. Several lines between the two strings do not help.
  - Reset: the same 12 forms with `git reset` and `git reset --hard` pass (HEAD also passed these, the repair does not reach them).
  - Real fleet command: the replay's only old-block-new-pass is a WALTER command (633 chars, `printf "…\n\nCo-Authored-By…\n" "$B" > …msg11.txt && git commit -q --amend -F … && git log -1 --format="%h %s"`). HEAD blocks, working tree passes. Whether it ran at the time was not checked; the point is the parse.
  - Scale: 2,350 of 14,271 distinct real commands scan differently from the corrected regex; in 82 of them the shipped parser loses a `git add/commit/push/reset` that the corrected regex sees. `printf "…\n"` and `\$` inside a double-quoted string are house style.
  - The opposite failure too: prose with a backslash is no longer prose. 5 regressions, `git commit A.md -m "cost \$5; git add -A is forbidden"` is old=0 new=2. This is X7's surviving case. The suite fixture `the \"git reset -q\" call` passes only because the walk reads `-q\` as an option and the leftover QUOTEDARG as a path; `--hard\` likewise escapes the `--hard` test. Green for the wrong reason.
- **Proposed change:** one token: `_QUOTED = re.compile(r"'([^']*)'|\"((?:[^\"\\]|\\.)*)\"")`. TESTED on `git_guard_FIX1.py` (which also adds `re.S`; not needed once continuations are joined, but harmless): all 45 A-group cases and all 7 B-prose cases right, X7 4/4, replay old-block-new-pass goes to 0. Add to BLOCK: `echo "a\b"; git add -A; echo "c d"` and the `printf "x\n"` form with `commit --amend`. Add to ALLOW: `git commit A.md -m "x \"git reset; y\" z"`.

### ❌2. The comment skip reads an unquoted `'#'` as a shell comment, so every reset rule, `--hard` included, is skipped on that line

- **Claim:** Property 1 "whatever follows it"; Property 2 "`--hard` is blocked in every position", "`reset HEAD` keeps its existing block."
- **Artifact:** `git_guard.py:65-67`, run on the scan after `_unquote_or_drop` (`:124-126`) has stripped the quotes from a whitespace-free string. `:132` adds a second form.
- **Command:** `read2.py` group C-comment; `git_truth2.py`.
- **Observed:** VERIFIED. 0 of 7 right. `echo '#'; git reset --hard origin/master` rc=0. `grep "#" f.txt; git reset --hard` and `echo '#'; git reset HEAD` are old=2 new=0, regressions in the reset rules themselves. `cut -d '#' -f1 f.txt; git reset -q 2>/dev/null` passes. Truth run: `echo '#'; git reset --hard` reverted A.md from 2 to 1 and cleared the index. Second form: `# note \<newline>git reset -q`. Bash does not continue a comment, so the reset is real and cleared the index; the join at `:132` folds it into the comment.
- **Proposed change:** in `_unquote_or_drop`, a quoted body containing `#` stays a placeholder: test `[\s#]` instead of `\s`. TESTED on `git_guard_FIX2.py`: both `--hard` cases block, `# git reset -q is forbidden`, `ls # git reset -q` and `git reset 'a#b.md'` stay allowed. The continuation-in-comment form is not fixed by this; leave it as residue.

### ❌3. QUOTEDARG counts as a path, so a quoted command substitution is a "named file"

- **Claim:** Property 1, a reset that names no path is blocked. The brief's `QUOTEDARG` as the only argument.
- **Artifact:** `git_guard.py:88` and `:126`, with `:80-81`.
- **Command:** `read2.py` group F-quotedarg; `git_truth2.py`.
- **Observed:** VERIFIED. 7 regressions, old=2 new=0: `git reset "$(git rev-parse HEAD)"`, `git reset "$(git merge-base HEAD origin/master)"`, `git reset "$(git rev-parse --show-toplevel)"`, plus `" "` and `":/ "`. `git reset -q "$(git rev-parse HEAD)"` also passes (HEAD passed that one too). Truth: the first form cleared all 3 staged files, the `--show-toplevel` form too, and `-q "$(git rev-parse HEAD~1)"` cleared them and moved HEAD. Note `git merge-base HEAD origin/master` is a root Git Protocol idiom, so this is the plausible shape. 0 occurrences in the replay. HEAD caught these by accident of dropping the string, and the module header declares runtime-built commands invisible, but the regression is real and decidable at the text level.
- **Proposed change:** a dropped string containing `$(` or a backtick returns a distinct placeholder, and `reset_violation` refuses it as "cannot name a path". Cost: `git reset -q "$(cat list)"` blocks, as it did at read 1 without `-q`. Untested.

### ❌4. `<ref> --` passes: the `--` proves the positional is a ref, and the walk counts it as a path

- **Claim:** Property 1. Same class as X2: `--` with nothing after it. Unlike read 1's W2 this one IS decidable.
- **Artifact:** `git_guard.py:80-81`, `paths = positional + post`.
- **Command:** `read2.py` group E-refs-decidable; `git_truth2.py`.
- **Observed:** VERIFIED. 0 of 5 right, all rc=0: `git reset master --`, `git reset -q v1.0 --`, `git reset d4d4824d90 --`. Truth: `git reset master --` cleared all 3 staged files; `git reset -q v1 --` cleared them and moved HEAD.
- **Proposed change:** refuse when `dd is not None and not post`. TESTED on `git_guard_FIX2.py`: both block.

### ❌5. The whole-tree set is literal, so X3 returns one spelling over

- **Claim:** Property 2, allowed only "when it touches only that path." The defect is a global unstage.
- **Artifact:** `git_guard.py:58`, exact-string `_WHOLE_TREE`.
- **Command:** `read2.py` group G-tree; `git_truth2.py`; `read2b.py`.
- **Observed:** VERIFIED rc=0, each truth-tested to clear the staged set: `git reset '**'`, `':(glob)**'`, `':(top)*'`, `'./*'`, `./.`, `.//`, `'*.md'`, `git reset -- ':!x.md'`, `-- ':(exclude)x.md'`. From a two-level desk directory `git reset ../..` cleared all 3 and `..` cleared everything under its parent directory. Also rc=0, not truth-tested: `'**/*'`, `':(top,glob)**'`, `?*`, `'[A-Z]*'`. HEAD passed these too, so this is unrepaired, not a regression. `../..` is the one that matters: a desk's cwd is `AGENTS/<NAME>/`, so it is the true whole-tree spelling from a desk, more so than `.`, which X3 had to accept as a cost. `git reset ':!x.md'` without `--` is rc=128, harmless.
- **Proposed change:** test the shape, not a set: refuse a path that has no character other than `.` and `/`, a path beginning `:` (pathspec magic, except a plain `:/name`), and a path that is only glob characters plus `/`. `'*.md'` is a judgement call, see W8. Untested.

## ⚠️ Residue

Each states why it is not ❌.

### W1. `_REFLIKE` is unanchored at the end, so ordinary paths read as refs

- **Claim:** Property 2. Not ❌ because it fails safe, `--` works around it, and it reaches 0 tracked paths in repo-relative form, against X6's 45.
- **Artifact:** `git_guard.py:57`. `^(?:HEAD|…)` has no right boundary and `[~^]` matches anywhere.
- **Command:** `read2.py` group H-pathfp; `read2b.py` against `git ls-files`.
- **Observed:** VERIFIED old=0 new=2: `git reset HEADER.md` (read 1 Held it as PASS), `-q HEADER.md`, `origin/notes.md`, `upstream/x.md`, `backup~`, `notes~1.md`, `a^b.md`, `@notes.md`. Truth: `git reset HEADER.md` unstaged that file only. Tracked: 0 of 41,880 repo-relative; 1 by basename, `HEAD-REVIEW.md`, reachable only from a desk-relative path and already blocked at HEAD. The message also says "reset HEAD" for a path.
- **Proposed change:** `^(?:HEAD|@|FETCH_HEAD|ORIG_HEAD|MERGE_HEAD)(?:$|[~^@])|^(?:origin|upstream)/|[~^]\d*$|@\{`. Untested.

### W2. Redirect forms the regex does not parse become "paths"

- **Claim:** Property 1 "whatever follows it". Not ❌ because no replayed command uses them and the fix is one token, but fold it in if touching the line.
- **Artifact:** `git_guard.py:56`.
- **Command:** `read2.py` group D-redirect; `git_truth2.py`.
- **Observed:** VERIFIED rc=0: `git reset -q >| /tmp/x` (the `>` survives as a positional; truth cleared the index), `git reset >|/tmp/x`, `git reset <<< x`, `git reset -q {fd}>x`, `git >/dev/null reset -q` (truth cleared; GIT does not expect a redirect, inherited across all rules). All other odd spacing is right: `2> /dev/null`, `> /dev/null`, `&>`, `&> `, `>>log`, `>&2`, `2>&1>/dev/null`, `2>&-`, `> "log file.txt"`, `</dev/null`. Path with redirect stays allowed, `git reset A.md>/dev/null`.
- **Proposed change:** `\d*(?:>>?\|?|<<?<?)&?\s*…`. Untested.

### W3. `find -exec git reset -q \;` passes because the `\` is a positional

- **Claim:** Read 1 W5 carried, not closed; the walk's `;` terminator leaves the backslash as an argument.
- **Artifact:** `git_guard.py:55`, `:70`.
- **Command:** `read2.py` group I-find; `git_truth2.py`.
- **Observed:** VERIFIED rc=0; truth `find A.md -exec git reset -q \;` cleared all 3. Not ❌: unusual form, no replay hit.
- **Proposed change:** drop a bare `\` token in `args`. Untested.

### W4. Continuation join widens the `.*` in the add and commit rules across `&&`

- **Claim:** Ordinary commands stay allowed. Not ❌ because the replay shows 0 such blocks in 14,271 and the same false positive already exists on one line.
- **Artifact:** `git_guard.py:132` with RULES `:40`, `:48`.
- **Command:** `read2.py` group J-allow.
- **Observed:** VERIFIED old=0 new=2: `git add A.md && \<newline> ls -A`, `git add A.md && \<newline> python3 x.py --all`, `git commit A.md -m "x y" && \<newline> ls -a`, `… \<newline>  && python3 tool.py -a`. Multi-line `&& \` chains are a real style, so `--all` on a later tool is the live risk. It fails loud.
- **Proposed change:** `[^\n;&|]*` in place of `.*` in those two rules. Untested, and check it against the RAV fixtures.

### W5. Bare refs: the acceptance file still does not declare them; two more are decidable

- **Claim:** Read 1 W2 said to declare as residue. It is not in the acceptance file.
- **Artifact:** `PROME/tools/tests/ACCEPTANCE_git_guard_reset_2026-11-06.md`; `git_guard.py:57`.
- **Command:** `read2.py` group E-refs-residue; `git_truth2.py`.
- **Observed:** VERIFIED rc=0: `git reset master`, `v1.0`, `-q v1.0`, `d4d4824d90`, `feature/x`, `refs/heads/master`, `refs/remotes/origin/master`. Truth: `git reset v1` cleared and moved HEAD. `refs/` is a decidable prefix. Mode forms all block (`--soft v1.0`, `--mixed master`, `--keep v1.0`), and so do `master~1`, `v1.0^`, `stash@{0}`, `HEAD@{1}`.
- **Proposed change:** add `refs/` to `_REFLIKE`; write the bare-name residue into the acceptance file.

### W6. New path false positives from the mode and option logic

- **Claim:** Property 2. Not ❌: rare, and git deprecates the first.
- **Artifact:** `git_guard.py:75-76`, `:81`.
- **Command:** `read2.py` group H-pathfp; `git_truth2.py`; `read2b.py`.
- **Observed:** VERIFIED old=0 new=2: `git reset --mixed -- A.md` (truth: unstages A.md only, with a deprecation warning), `git reset --pathspec-from-file=list.txt` (truth: unstages only the listed file). The space form `--pathspec-from-file list.txt` passes, so the two spellings disagree.
- **Proposed change:** accept and declare.

### W7. `_SHELL_C` remains not escape-aware, read 1's X7 half

- **Claim:** Read 1 X7 proposed the matching change to `_SHELL_C`; the diff did not make it. Inherited: HEAD passes these too.
- **Artifact:** `git_guard.py:86`.
- **Command:** `read2d.py`.
- **Observed:** VERIFIED old=0 new=0: `bash -c "echo \"x\"; git add -A"` and `bash -c "echo \"x y\"; git reset --hard"`. The body ends at the first `\"`, and the tail is dropped as a string.
- **Proposed change:** the same escape-aware body in `_SHELL_C`, single-token care, separate episode if the budget is spent.

### W8. Decide `'*.md'` and the other partial globs

- **Claim:** Property 2 says "that path"; a glob is a set. Not ❌ because a glob can be narrow, for example `'AGENTS/X/*.md'`.
- **Artifact:** `git_guard.py:58`.
- **Command:** `git_truth2.py`.
- **Observed:** VERIFIED `git reset '*.md'` cleared all 3 staged files, as all were `.md`. In this repo that would be nearly everything.
- **Proposed change:** owner's ruling: refuse a glob with no literal directory prefix, or declare.

## Question 2, what held

| Shape | Result |
|---|---|
| `reset` as a value after another subcommand | PASS 20/20 allowed: `git log --grep reset`, `git stash push -m reset`, `git config alias.r reset`, `git -C reset status`, `git -c reset status`, `git log -p reset`, `git -C /x log reset`, `git submodule foreach reset`, `git tag reset`, `legit reset`, `git reset-notes`, `git reset.md` |
| QUOTEDARG against the other RULES, with a quoted space beside the flag | PASS 19/19 blocked, 9 of them newly (`git -C "my dir" add .`, `git -c "a b=c" commit --amend`, six continuation forms), so the placeholder and the join each closed something |
| Path with the walk | PASS `git reset A.md>/dev/null`, `-q A.md 2>&1`, `A.md >x 2>&1`, `-q -- A.md 2>/dev/null \|\| true` |
| Global options, including a quoted `-C` directory | PASS blocks `git -C "my dir" reset -q`, `git -c "a=b c" reset`, read 1 W4 in part |

## Question 3: replay

| Check | Result |
|---|---|
| `PROME/tools/hooks/test_git_guard.py` | PASS 68/68, re-run here. It does not exercise ❌1 to ❌5 |
| Newly blocked real commands | 5 of 14,254, 0 false positives: VULCAN's incident, VIOLET's two, and two `reset --hard` in scratchpad repos (read 1 W9, by design) |
| Old block, new pass | 1, ❌1's WALTER `--amend` |
| With `git_guard_FIX1.py` | Old block, new pass goes to 0 |

**Regressions left after the ❌1 token alone:** 23 harness cases, all listed under ❌2, ❌3, W1, W4 and W6 (`read2c.out`).

**Suggested order, ❌1 first because it is live:** ❌1 and ❌2 and ❌4 are one token, one character class and one condition, and those three are tested on the scratch copy. ❌3 and ❌5 are small but untested. Read budget: this was the second read. WQ-178 allows a third only when a ❌ fix on the result changes a rule's meaning, or on Will's word; PROME decides whether these fixes meet that test. A fix made after the final read stays unreviewed. The acceptance `reads:` line is left for the owner to set.
