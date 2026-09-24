# pipeline_rc_guard.py v4 — build record (2026-09-24)

**Subject:** `scripts/pipeline_rc_guard.py` (repo-root, DAEDALUS grant) · **Trigger:** PROME packet 2026-09-18, WQ-244, five independent-reader findings · **Builder:** DAEDALUS build subagent (team-lead spawn) · **Standard:** CHECK_STANDARD §3 (for every change, the warning is shown firing on a case that should fire and staying silent on a clean one, using the exact commands), §9 (exit codes), PAT-172 (the suite checks its own drill count).
**Not touched:** `PROME/tools/hooks/pipeline_rc_block.py` (PROME's wrapper, read only). The `diagnose(cmd) -> (hit, message)` signature is unchanged. The exported names the wrapper imports (`diagnose`, `PIPE_THEN_RC` with group `gate`, `ALREADY_SAFE`, `_diagnose_three_state`) all still exist.
**Uncommitted.** The build subagent had no mutating git. File md5: before `40698bcc60bf04dfc6f239e00863c508` (= HEAD), after `0795e722d34f3049a6bc24292d0dc41e`. Diff: +259 / −33 lines.
⚠️ **Correction to the spawn brief:** it describes the wrapper as a BLOCKING hook. It has been **ADVISORY since WQ-263** (Will 2026-09-22; see the wrapper's docstring line 2 and `_handle`): a confirmed hit prints a warning and exits 0.

## Dispositions

| # | Finding | Disposition | Diff summary |
|---|---|---|---|
| 1 | Recogniser 1 had no command-word test | **FIXED** | New `_invocation_spans(seg, lift_c)` is ONE token walk shared by both recognisers. It skips env assignments, reserved words, `(`/`{ `, and prefix commands (`time env nice sudo timeout nohup stdbuf exec`; `command` unless followed by `-v/-V/-p`). It returns the command word, plus the interpreter's first non-flag argument when the command word is an interpreter. With `lift_c` it also looks inside `bash -c "…"` / `eval "…"` bodies. New `_gate_in_command_position()` (segment separators `|& \|\| && \| ; \n & \` ( {␠`; `&` inside redirections like `2>&1` is not a separator) and `_pipe_then_rc_hit()`, which tries EVERY gate token anchored at its own position. Flag-shaped gates (`--selftest`/`--check`) count only after a command that runs a script. `PIPE_THEN_RC` also no longer lets a pipe after a `&&` count. `_command_word_tool()` (recogniser 2) now uses the same walk. |
| 2 | Bare-word `PIPESTATUS\|pipefail` allowlist | **FIXED** | `ALREADY_SAFE` now matches only real uses: unescaped `${PIPESTATUS`/`$PIPESTATUS`, and `set [-x …] -o pipefail` / `set -eo pipefail`. `set +o pipefail` does not count. New `_strip_comments()` removes shell comments before the check. `THREE_STATE_SAFE` had the same bare words; they are replaced with the same patterns and searched on the comment-stripped command. |
| 3 | `if <gate> \| tail; then` · `<gate> && ok \|\| FAILED` | **DECLARED** | Listed as out of scope in the docstring and pinned with 2 drills (want=False), so if either case ever starts being caught, a drill changes. |
| 4 | `\|&` not a pipe | **FIXED** | `PIPE_THEN_RC`: `\|&?\s*(?:SWALLOWERS)`. `_segments_before`: `\|&` is split as one separator, so the segment is no longer `& y`. |
| 5 | Process substitution around a gate | **DECLARED** | Listed in the docstring and pinned with 2 drills (want=False). |

**Side effects of sharing the token walk with recogniser 2 (both drilled):** one false positive removed: `command -v verify_push.sh || echo missing` fired under v3 because `command` was treated as an interpreter. One missed case now caught: `time python3 scripts/read_cap_check.py … || echo bad` was missed under v3.

## Drills (exact commands, run 2026-09-24)

**Fire cases (hit=True):**
```
✓ hit=True  want=True   V4-F2 CAPABLE — the word in a COMMENT is not a use        [… | tail -1; echo $?  # remember PIPESTATUS next time]
✓ hit=True  want=True   V4-F2 CAPABLE — `set +o pipefail` turns it OFF
✓ hit=True  want=True   V4-F4 CAPABLE — `|&` VERBATIM                             [python3 scripts/validate_all.py |& tail -1; echo $?]
✓ hit=True  want=True   V4-F1 CAPABLE — an argument mention FIRST must not consume the real defect after it
✓ hit=True  want=True   V4-F1 CAPABLE — defect inside a `bash -c` body
```
**Clean cases (hit=False):**
```
✓ hit=False want=False  V4-F1 — gate NAME is grep's search argument               [grep -rn "read_cap_check" AGENTS/ | head -20; echo $?]
✓ hit=False want=False  V4-F1 — `ls` of a glob                                    [ls scripts/*_check.py | wc -l; echo "rc=$?"]
✓ hit=False want=False  V4-F1 — gate NAME is grep's argument mid-pipeline         [git log --oneline -50 | grep validate_all | head -3; echo $?]
✓ hit=False want=False  V4-F1 — `sed -n` of the gate's source                     [sed -n "1,40p" scripts/read_cap_check.py | head -20; echo $?]
✓ hit=False want=False  V4-F1 — `find -name` pattern                              [find . -name "*_gate.py" | wc -l; echo $?]
✓ hit=False want=False  V4-F2 CLEAN — `set -eo pipefail` is a use
✓ hit=False want=False  V4-F4 CLEAN — `|&` with PIPESTATUS read
```
**Before the edits, v3's `diagnose()` on the same commands:** all 5 F1 commands hit=True. The comment-mention and `|&` commands were hit=False. `command -v verify_push.sh || echo missing` was hit=True.
**The new drills can fail:** swapping the new suite's `diagnose` for v3's gives **67/85**. The 18 drills that fail under v3 are exactly the V4 fire and clean cases above plus the F1 flag, lookup, brace and r2 cases.
**Running the real hook (JSON on stdin):** the `|&` command prints the full ⚠️ warning on stderr, hook rc=0. The grep argument-position command prints nothing, hook rc=0.

## Selftest totals

`python3 scripts/pipeline_rc_guard.py --selftest` → **`✅ PIPELINE-RC-GUARD SELFTEST 85/85 drill(s) behaved`**, rc 0. Full output: scratchpad `fix-rc-guard/selftest_v4.txt`.
Drill count: **53 before, 85 after** (+32: F1 17 incl. 2 recogniser-2 cases, F2 7, F4 4, perimeter pins 4). `EXPECTED_DRILLS` = 85. The count check was tested: with the constant still at 53, the run printed `SUITE SIZE CHANGED: 85 … says 53`, 84/85, rc 1.
**Committed-corpus check** (1,121 committed `.md/.sh/.tsv` lines containing a pipe AND `$?`/`||`): v3 had 6 hits, v4 has 1, and there are 0 new hits. The 5 that went away are prose quoting the F1 reader's own commands. The 1 that remains is the 2026-09-12 `verify_push.sh … || { … NOT ON ORIGIN … }` defect quoted word for word, so that hit is correct. PAT-083: this corpus cannot measure how often the guard catches real defects in commands typed live.

## PROME's wrapper, re-run (not edited)

`python3 PROME/tools/hooks/pipeline_rc_block.py --selftest` → **`❌ PIPELINE-RC-BLOCK SELFTEST 34/36`** (was 36/36). Both failures are expected consequences of this fix. Neither is a regression in a verdict the wrapper gives:
1. `r5 ❌10 PERIMETER … gate |& tail; echo $? -> 0 today, declared`: this drill pinned F4 as a known miss, and the case now warns correctly. **PROME: change want to 2.**
2. `verdict() names a suppressed raw hit`: this drill feeds in `grep -rn "read_cap_check" … | head -20; echo $?`, which `diagnose()` no longer flags, so there is nothing for the wrapper to suppress. **PROME: point it at an input the wrapper still suppresses (e.g. the r3 ❌7 later-command case) or delete it along with the layer.**
All the wrapper's other hit/no-hit drills still pass (B6/B7/B8, r3 ❌5/❌6/❌7, r4 ❌3–❌6, r5 ❌4/❌5/❌9).
**Duplication (for PROME to decide; I did not touch it):** the wrapper's `_gate_in_command_position` (plus its prefix/`command`/brace walk) now **duplicates** v4's. On the wrapper's own B7 / r4 ❌6 / r5 ❌5 inputs, bare `diagnose()` and `verdict()` now agree (no hit from either). The wrapper layers that are **NOT duplicated** and still change verdicts: heredoc-body dropping (r5 ❌4), blanking `|` `;` `&` inside quotes (r1 ❌3, r4 ❌4), and the check that `$?` is read immediately after the pipeline (r3 ❌7). The `-c`/`eval` lifting is only partly duplicated (v4 looks inside the body for recogniser 1 only). The wrapper's acceptance condition **B5 "the DAEDALUS file is byte-unchanged"** is broken by definition.

## What remains (listed in the docstring's PERIMETER block)
- F3, F5 as listed above.
- A real-use construct inside a single-quoted string (`echo 'set -o pipefail'`) still exempts, because single quotes are not matched in pairs (`don't` would pair wrongly).
- Standalone, a `;` inside a double-quoted string can create a false segment. The wrapper blanks it first.
- `sudo -u <user> <gate>` treats `<user>` as the command word.
- A `$?` that belongs to a later command (`gate | tail; git status; echo $?`) still fires in the bare recogniser. Only the wrapper's r3 ❌7 layer suppresses it.
- Not re-reviewed by an independent reader. The last five rounds (wq244cold1–5) each found something new. v4 is a port plus three fixes, not a converged guard.
