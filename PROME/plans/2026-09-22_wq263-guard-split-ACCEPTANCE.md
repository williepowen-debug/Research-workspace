# WQ-263 guard split — acceptance conditions (written BEFORE the edit, WQ-229)

**Ruling:** Will 2026-09-22 19:37 / 19:51 ET, *"WQ-263 approved"* then *"Ok yes with CATO fix"*. Record: `PROME/WILL_QUEUE.md` WQ-263.

The acceptance conditions below are the test list.
- **P1** `pipeline_rc_block.py`: a CONFIRMED recogniser hit exits **0**, never 2. The guard's diagnosis is still written to stderr and labelled ADVISORY. All fail-open paths are unchanged.
- **S1** `commit_subject_guard.py` exits **2** only when ALL of these hold:
  - the message is a literal `-m`/`--message` value;
  - the subject is over the cap;
  - the SAME commit is found by a RAW top-level parse, with no `bash -c`/`eval`/backtick lift and no ANSI-C normalisation;
  - in that parse, `git` is the segment's command word after env assignments and the transparent heads `{ } ! if then else elif do while until`;
  - there is no prefix command (`time env nice sudo timeout nohup stdbuf exec command`);
  - there is no `--dry-run`;
  - there is no `$VAR`, `$(…)` or backtick in the message.
- **S2** Every `-F`/`--file` verdict, including `-F -` with a stdin heredoc, is ADVISORY: exit 0 with a visible "over cap (inferred)" line.
- **S3** CATO's three reproduce as exit 0: `command -v git commit -m <long>` · `env printf %s git commit -m <long>` · `timeout 1 echo git commit -m <long>`.
- **S4 (stated cost):** `env FOO=1 git commit -m <long>` · `timeout 5 git commit -m <long>` · `sudo -u x git commit -m <long>` · `bash -c '…'` · `eval` · backtick · `$'…'` forms now WARN (exit 0), not block.
- **S5** Still BLOCKS:
  - plain `git commit -m <101>`
  - `-am` and `-qm`
  - `--message=`
  - `-m<msg>` attached
  - `git -C path commit -m`
  - `/usr/bin/git`
  - two commits where the second is long
  - `{ …; }` / `if … then`
  - a backslash-newline continuation
  - a two-line joined subject
  - leading whitespace counted
  - `FOO=1 git commit` (a bare assignment is not a prefix command)
- **S6** Every prior drill that expected `allow` or `unknown` still gets it. No new false block.

**(c) Shared command-position function:** DEFERRED, declared. With the wrapper advisory (P1), the blocking path lives in ONE hook only, so the shared function no longer guards a block. It becomes worth doing only if either hook blocks again. It is registered as residue here, not silently dropped.

**Neighbours considered:**
- ordinary: S5
- overlap: a raw/lifted mismatch ⇒ warn, never block
- wrong owner: `scripts/pipeline_rc_guard.py` (DAEDALUS) is byte-unchanged
- missing information: unparseable ⇒ UNKNOWN, as before
- concurrent: every session on the box loads the hooks, so the suites run before commit and a broken hook fails OPEN by its own wiring

**⚠️ Known limit, not fixed:** an exit-0 advisory goes to stderr. Whether Claude Code shows exit-0 PreToolUse stderr to the model is UNVERIFIED here. If it does not, "advisory" is effectively silent, and C1 in `validate_all` remains the after-the-fact check.
