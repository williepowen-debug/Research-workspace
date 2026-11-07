# Counterexample read: git_guard reset repair, 2026-11-06

**Verdict: NOT FIXED. 7 ❌, 10 ⚠️.** One of the two incidents the acceptance file names still passes the repaired guard, verbatim.

**State per WQ-229:** IMPLEMENTED, and TESTED by the author (suite 41/41, L294 F6 OK, both re-run here). Not INDEPENDENTLY VERIFIED. Acceptance properties 1 and 2 and the prose clause each fail below.

**Scope:** guard fed by stdin against the working-tree `PROME/tools/hooks/git_guard.py` (M, uncommitted). No repository file edited; `git status` for the three repair paths is unchanged at the end.

## Method

| Step | Size | Artifact in the scratchpad |
|---|---|---|
| My own cases, run through the repaired guard and the pre-repair guard (`git show HEAD:`) | 243 cases | `harness.py`, `harness.out` |
| Real fleet commands replayed through both guards | 787 transcripts, 43,566 Bash commands, 28 distinct with `git … reset` on one line | `transcripts2.py`, `transcripts2.out` |
| What git 2.43.0 really does per form, in throwaway repos | 20 forms | `git_truth.py` |
| Incident replay and extra forms | 6 replayed lines, 18 forms | `final.py` |

- **Harness result:** 73 should-block cases pass and 22 should-pass cases block, by my expected labels. 40 of the 73 sit in X1 to X5 and 7 of the 22 sit in X6 and X7; the rest are ⚠️ classes. The ledger grades them; the raw count is not the finding.
- **Throwaway repos:** `git_truth.py` ran real resets only in temporary repos under the scratchpad. It asserts `rev-parse --show-toplevel` equals the temp directory before each form. Each repo started with A.md and B.md staged; "cleared both" means `diff --cached` went to empty.
- **Hook wiring:** checked by grep only (see Held). Every case here went to the guard script by stdin, as briefed.

## ❌ Blocking defects

### X1. A bare reset followed by a redirect, comment or closing backtick passes; VULCAN's incident command still passes

- **Claim:** Property 1, "any `git reset` that names no path is blocked, whatever its options and whatever follows it on the line." The defect statement names VULCAN's run as a case this repair covers.
- **Artifact:** `git_guard.py:48`; terminator class `(?:$|[;&|)\n])` has no `>`, `<`, digit-redirect, `#` or backtick. `test_git_guard.py` BLOCK has no redirect case. `AGENTS/VULCAN/LESSONS.md:92` (L-98).
- **Command:** `final.py` replay of the 2026-11-06T21:12Z VULCAN transcript command (1,273 chars); `harness.py` cases redir, 2>null, 2>null||true, 2>&1, 2>&1|tail, comment, comment-q, backtick-bare.
- **Observed:** VERIFIED. VULCAN's `git reset -q 2>/dev/null; S=…` is old=0 **new=0**, allowed. VIOLET's `git reset -q; date` is old=0 new=2, so the repair fixed one incident of two. Also rc=0: `git reset -q >/dev/null`, `git reset 2>&1`, `git reset -q 2>&1 | tail -1`, `git reset -q 2>/dev/null || true`, `git reset # unstage`, `` x=`git reset` ``. In the throwaway repo `git reset -q 2>/dev/null` and `git reset -q # note` each cleared both staged files. `` echo `git reset -q` `` blocks only by accident: `\S*` swallows the backtick as part of the option.
- **Proposed change:** add `#`, a backtick, `>`, `<` and `\d+>` to the terminator, or better, replace the three reset regexes with one small check that walks the tokens after `reset` up to a shell terminator, discards redirects, and blocks when no path token remains. Add VULCAN's verbatim form as a fixture. Note `2>/dev/null` is house idiom, so this is the highest-frequency hole.

### X2. `git reset --` with nothing after it passes

- **Claim:** Property 1. The guard comment says "A `--` starts paths"; here no path follows.
- **Artifact:** `git_guard.py:44` and `:48`, negative lookahead `(?!-(?:\s|$))`.
- **Command:** `harness.py` cases --end, q--end, "-- ;", "-- &&", --nl, xargs--; `git_truth.py`.
- **Observed:** VERIFIED. `git reset --`, `git reset -q --`, `git reset -- ; git status`, `git reset -- && git status`, `git reset --\ngit status` and `echo | xargs git reset --` are all rc=0. The three truth-tested forms (`--`, `-q --`, `xargs … --`) each cleared both staged files. `git reset --; git status` blocks, but only because no space follows `--`, so the behaviour flips on one space.
- **Proposed change:** after `--`, require at least one real path token before allowing. The token walk from X1 covers this. Add fixtures.

### X3. Whole-tree pathspecs pass as if they were one path

- **Claim:** Property 2 allows a named path only "when it touches only that path"; the defect is a global unstage of the shared index.
- **Artifact:** `git_guard.py:48`. The add-dot rule at `:42` is the direct precedent: `.` is refused there regardless of cwd.
- **Command:** `harness.py` cases dot, dot-q, dot--, dot/, q--dot, top, top--, star, star2; `git_truth.py`.
- **Observed:** VERIFIED. `git reset .`, `-q .`, `-- .`, `./`, `-q -- .`, `:/`, `-- :/`, `'*'`, `-- '*'` all rc=0. Truth run at the repo top level: `.`, `-- .`, `:/`, `-- '*'` each cleared both staged files. Caveat: from a desk directory `.` is scoped to that directory, and the hook cannot see a `cd`, so blocking `.` will catch a harmless desk-local form. `:/` and `'*'` have no such defence. Commits run from the repo root by house rule, so the global reading is the one that matters.
- **Proposed change:** treat `.`, `./`, `:/` and a lone `*` as "no path named". Add fixtures. The desk-local `.` cost is the same one add-dot already pays.

### X4. `@`, remote refs and mode-plus-ref forms pass

- **Claim:** Property 1, a reset that names no path. Property 2, `reset HEAD` is blocked; `@` is git's alias for HEAD.
- **Artifact:** `git_guard.py:44`, literal `HEAD\b` only. Case-internal inconsistency: the author's fixture `reset --mixed HEAD~1` blocks, the same form with another ref does not.
- **Command:** `harness.py` cases @, q@, origin, mixed-origin, q-origin, soft-origin, keep, merge, @{u}; `final.py` `--soft @`, `--mixed @~1`; `git_truth.py`.
- **Observed:** VERIFIED. rc=0 on `git reset @`, `-q @`, `@{u}`, `origin/master`, `-q origin/master`, `--mixed origin/master`, `--soft origin/master`, `--keep origin/master`, `--merge origin/master`, `--soft @`, `--mixed @~1`. Truth run: `git reset @` cleared both staged files. No live `AGENTS/*/CLOSEOUT.md`, `AGENTS/*/CLAUDE.md`, `docs/`, or `scripts/` recipe prescribes a mode-plus-ref form (`git grep`; the only hits are a processed inbox packet, two reports and an acceptance file), so blocking breaks no current procedure. INFERRED: git rejects paths with `--soft`, `--keep`, `--merge`, so any positional there is a ref; not tested here.
- **Proposed change:** extend the HEAD alternation to `@` and `@{…}`; block `origin/…`; block any positional after a mode option unless it follows `--`. Bare branch names and shas stay undecidable, see W2.

### X5. A shell line continuation defeats every reset rule, including `--hard`

- **Claim:** Property 2, "`--hard` is blocked in every position." Property 1 for the bare form.
- **Artifact:** `git_guard.py:50`, `[^\n;&|]*` stops at the continuation's newline; `:44` and `:48` stop at the backslash. `strip_text` (`:102`) does not join continuations.
- **Command:** `harness.py` cases hard-continue, hard-continue2, cont-q, cont-bare, cont-head; `git_truth.py`.
- **Observed:** VERIFIED. `git reset \<newline>  --hard origin/master` rc=0, as do the `-q`, `HEAD` and bare continuations. Truth run: `git reset \<newline>  --hard` reverted A.md from 2 to 1, so working-tree content was lost. This is the worst single consequence in the ledger.
- **Proposed change:** one line in `strip_text`: replace backslash-newline with a space before the rules run. INFERRED: being at scan level, this reaches every rule, not only reset. Add fixtures.

### X6. False positive: a quoted path with a space is read as no path at all

- **Claim:** Property 2, "a reset that names a path is allowed … with or without `-q`."
- **Artifact:** `_unquote_or_drop`, `git_guard.py:97-99`, returns a space, so the path leaves no token and `:48` sees a bare reset.
- **Command:** `harness.py` cases spaced, spaced-q, spaced-single, subst-q, pathspec-file; `git ls-files`.
- **Observed:** VERIFIED. `git reset -q "ARCHIVED prompts/a b.md"` old=PASS new=BLOCK, a regression. `git reset "a b.md"` and `git reset 'a b.md'` were already blocked. `git reset -- "a b.md"` passes, so a workaround exists, though the message "bare reset" misdirects. The same path produces the block on `git reset -q "$(cat list)"`. Scale: 45 of 41,875 tracked paths contain a space, for example `AGENTS/BARON/research/prompts/ARCHIVED prompts/`. 0 occurrences in the 43,566 replayed commands. Fails safe. ❌ on the property's letter, low frequency; the owner may reasonably rule it ⚠️ with residue, but it needs a ruling rather than silence.
- **Proposed change:** have `_unquote_or_drop` return a neutral placeholder token instead of a space. Untested; this should also let `-C\s+\S+` consume a quoted directory, which would close part of W4. Check it against the add rules before adopting.

### X7. False positive: a commit message with escaped quotes is scanned as a command

- **Claim:** "Prose stays prose: a mention in a message or heredoc body is not blocked."
- **Artifact:** `_QUOTED`, `git_guard.py:61`, is not escape-aware, so `\"` closes the string. The author's prose fixtures use no escaped quote.
- **Command:** `transcripts2.py` commit-form section; `harness.py` cases msg-esc-semi, bash-c-esc.
- **Observed:** VERIFIED. old=0 new=2, all regressions: `git commit A.md -m "the \"git reset -q\" call"`, `git commit A.md -m "use \"git reset --hard\" never"`, `git commit -m "x \"git reset; y\" z" A.md`, and `bash -c "grep \"git reset -q\" f"`. The form with a trailing `-- A.md` passes only because the tail is not a terminator. The `_QUOTED` weakness is inherited (`\"git add -A\"` was already blocked), but this repair widens it to reset. A desk writing up this very incident in the house path-first form trips it. The heredoc message form is clean.
- **Proposed change:** `"((?:[^"\\]|\\.)*)"` in `_QUOTED`, with the matching change to `_SHELL_C`. Add both message forms to ALLOW.

## ⚠️ Residue

Items below are outside "the direct forms", inherited from before this repair, or sanctioned by a property. Each states why it is not ❌.

### W1. Comment lines and unquoted mentions newly block

- **Claim:** Prose stays prose. The clause names messages and heredoc bodies, not shell comments, hence ⚠️.
- **Artifact:** `git_guard.py:48`, `\n` in the terminator plus no comment stripping. `GIT` starts with `\bgit`, which also fires after `.` or `/`.
- **Command:** `harness.py` cases comment-end, comment-semi, comment-q, comment-only, echo-unq-end, echo-unq-q, grep-unq-g, ls-dotgit, cd-git.
- **Observed:** VERIFIED. old=PASS new=BLOCK: `# never git reset\ngit status`, `# no git reset; use a path\ngit status`, `echo never git reset -q`, `ls .git reset`. 0 occurrences in 43,566 replayed commands. A reworded comment clears it.
- **Proposed change:** strip whitespace-preceded `#…` to end of line after quote stripping. Untested; it should also close the comment half of X1.

### W2. Bare branch names and shas pass

- **Claim:** Property 1. Not ❌ because `master` and `d4d4824d90` are lexically identical to file names; no regex can decide.
- **Artifact:** `git_guard.py:48`.
- **Command:** `harness.py` cases master, sha, FETCH_HEAD, ORIG_HEAD, lc-head.
- **Observed:** VERIFIED rc=0. `git_truth.py` showed `ORIG_HEAD` is rc=128 with no prior reset, so its effect is unproven there.
- **Proposed change:** declare as residue in the acceptance file. Do not chase it.

### W3. Abbreviated `--hard`

- **Claim:** Property 2. Not ❌ because the literal `--hard` is covered and nobody types `--ha`.
- **Artifact:** `git_guard.py:50`.
- **Command:** `harness.py` cases hard-abbr, hard-abbr2; `git_truth.py`.
- **Observed:** VERIFIED. `git reset --har origin/master` rc=0. Git honours the prefix: `--har HEAD` and `--ha` both reverted A.md in the truth run. `--har HEAD` and bare `--har` block via other rules.
- **Proposed change:** `--ha(?:r|rd)?\b`, one token, if touching the line anyway.

### W4. Global options outside the `GIT` list

- **Claim:** The `GIT` comment says "any of its global options". The module header says `--git-dir` and `--work-tree` are not covered. These contradict. Inherited across all rules, hence ⚠️.
- **Artifact:** `git_guard.py:17`, `:35-37`.
- **Command:** `harness.py` cases work-tree-sp, namespace, namespace-sp, literal, no-replace, bare, paginate, glob-ps, config-env, -C-quoted-space, -C-nospace, -c-quoted; `final.py`.
- **Observed:** VERIFIED rc=0 on all. `git --git-dir .git reset -q` blocks only by accident (`\bgit` matches inside `.git`); `git --git-dir ../.git/ reset -q` and `git --git-dir /x/repo reset -q` pass, and `git --git-dir .git reset -q` cleared both files in the truth run.
- **Proposed change:** generalise to `--[a-z-]+(?:=\S+)?` plus the known value-taking space forms, and align the two comments.

### W5. Runtime-built commands

- **Claim:** The hook declares these invisible by construction. Two below are not declared.
- **Artifact:** `git_guard.py:10-19`, `:60`.
- **Command:** `harness.py` cases eval, printf-bash, alias, alias-q, alias!, runtime-empty, var-empty, escaped, git.exe, bash -x -c, bash -c -x, find-exec; `final.py` `$(cat list)`.
- **Observed:** VERIFIED rc=0. `git reset -q $(true)` and `echo | xargs git reset --` cleared both files in the truth run. `git.exe` is real on this box at `/mnt/c/Program Files/Git/cmd/git.exe`. Undeclared and cheap: `bash -x -c '…'` and `find … -exec git reset -q \;`.
- **Proposed change:** let `_SHELL_C` accept preceding flags and add `\;` to the terminator. Leave the rest as declared.

### W6. Apostrophe pairing hides a real command

- **Claim:** Inherited `_QUOTED` weakness affecting every rule, not specific to reset, hence ⚠️. Plausible in a multi-line call.
- **Artifact:** `git_guard.py:61`, `:108`.
- **Command:** `harness.py` cases apostrophes, apostrophes2.
- **Observed:** VERIFIED. `# don't\ngit reset -q\n# won't` and `echo it's\ngit reset -q\necho it's` rc=0, because the pair of apostrophes reads as one whitespace-bearing string and is dropped.
- **Proposed change:** strip comments before quotes, or scan quotes line by line. Tangled with W1 ordering; decide them together. Separate episode.

### W7. `git reset --help` and `-h` newly block

- **Claim:** Harmless read-only forms. Rare, not ordinary desk work.
- **Artifact:** `git_guard.py:48`.
- **Command:** `harness.py` cases help-flag, h-flag.
- **Observed:** VERIFIED old=PASS new=BLOCK. `git help reset` passes.
- **Proposed change:** exempt `-h` and `--help`, or leave and declare.

### W8. Path literally named like an option or like HEAD

- **Claim:** Property 2 sanctions "`--hard` is blocked in every position, even with a ref or path", and "`reset HEAD` keeps its existing block."
- **Artifact:** `git_guard.py:44`, `:50`.
- **Command:** `harness.py` cases path-named-hard, --hard.md, HEAD.md, HEAD-notes; `git ls-files`.
- **Observed:** VERIFIED. `git reset -- --hard` and `git reset -- --hard.md` newly block; 0 tracked paths contain `--hard`. `git reset HEAD.md` was already blocked; 1 tracked path matches a HEAD-punctuation name. `git reset -- HEAD.md`, `-- HEAD` and `-- -q` pass.
- **Proposed change:** none. Accept.

### W9. Throwaway-repo fixtures now block

- **Claim:** Property 2 is explicit and the hook cannot see a `cd`, so this is by design. Disclosed because it is the real cost of the repair.
- **Artifact:** replay in `transcripts2.out`.
- **Command:** `transcripts2.py`.
- **Observed:** VERIFIED. Replay outcome over 28 distinct commands: 22 old pass new pass, 2 old block new block, 4 newly blocked. Of the 4, 2 are VIOLET's incident (two near-identical commands, 10,262 and 10,313 chars, both ending in the same true `git reset -q; date`) and 2 are PROME's own `reset --hard` inside scratchpad repos (10-16, 10-29). No newly blocked command was prose. My first reading of the VIOLET hit as prose was wrong: the match is a true `git reset -q; date`.
- **Proposed change:** none. Fixture work moves into a script file, as this read's did.

### W10. Twin global unstages are unlinted, and the suite does not pin the plain path case

- **Claim:** The root rule concerns a global unstage; acceptance scopes only `reset`, so out of scope. Fixture gap is minor.
- **Artifact:** `git_guard.py` RULES; `test_git_guard.py` ALLOW.
- **Command:** `final.py`.
- **Observed:** VERIFIED rc=0: `git restore --staged .`, `git restore --staged :/`, `git rm -r --cached .`, `git read-tree HEAD`. Not truth-tested. ALLOW carries `reset -- A.md` and `reset -q -- A.md` but never `reset A.md` or `reset -q A.md`, which pass here and are Property 2's plain case.
- **Proposed change:** PROME's call whether to extend the rules. Add the two ALLOW fixtures regardless.

## Held

| Check | Result |
|---|---|
| False positives named in the brief | PASS, all correct: `git log reset-notes`, `git show reset.md`, `git show HEAD:reset.md`, `git reflog`, `git reflog show reset`, `git checkout reset`, `git log -- reset`, `git branch reset`, `git bisect reset`, `git help reset`, `git -C reset status`, `git reset-notes`, `git reset.md` |
| Paths | PASS: `git reset A.md`, `-q A.md`, `--quiet A.md`, `-- A.md`, `-q -- A.md B.md`, `-q A.md && git status`, `-q A.md >/dev/null`, `-q A.md # undo`, `(git reset -q A.md)`, a directory, `"$f"`, `for` loop, `xargs … --` |
| Literal names after `--` | PASS: `-- -q`, `-- HEAD`, `-q -- HEAD`, `HEADER.md` |
| Blocked as required | tabs, CRLF, newline chain, `;`, `&`, `\|\|`, subshell, `$()`, `{ …; }`, `if`, `env`, env prefix, `command`, `timeout`, `/usr/bin/git`, `xargs git reset`, `-c`, `-C`, `--no-pager`, `-p`, `bash -c`, `bash -lc`, a real reset after a path reset, `"reset"` quoted, all `--hard` forms other than X5 and W3 |
| Prose | PASS: double- and single-quoted messages, apostrophe inside a message, `$(cat <<'EOF'…)` house form, heredoc bodies, `grep`, `sed`, `python3 -c`, here-string |
| Property 3 N/A, Property 5 N/A | Sound. The hook has no owner knowledge and no state |
| Property 4 | VERIFIED. `[]`, `null`, bad JSON, string `tool_input`, numeric `command` all rc=0 with the advisory; non-Bash rc=0 |
| Backtracking | Clean: four adversarial inputs of 75,000 to 300,000 chars, each under 0.1 s |
| Wiring | One guard file, called from `~/.claude/settings.json`, `.claude/settings.json`, `PROME/.claude/settings.json` (grep only). So the repair reaches all desks once saved; so do its regressions |

**Suggested order, untested:** X5 and X7 are one line each. X1 to X4 and X6 want one token-walking check in place of the three reset regexes, not more regex alternation, which fits "fix the instance or extend a control". The acceptance `reads:` line is left at 0 for the owner to set; this file was read-only against the repo.
