---
name: finding_crlf_textmode_tsv_flip
description: Python text-mode write silently converts CRLF→LF across the WHOLE file → destructive whole-file diff + merge risk; edit CRLF state files in binary mode
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2deb9ef6-cca2-4435-981b-c119a048b089
---

Many shared state files carry CRLF line endings and are MIXED even within one agent dir (RED: VX.tsv / KB.tsv / CATALYSTS.tsv / CHALLENGES.tsv are CRLF; ML.tsv / VX_HISTORY.tsv are LF). A Python `open(p).read() … write()` in TEXT mode strips CRLF→LF across the ENTIRE file (universal-newlines on read, `\n`-only on write), producing a destructive whole-file diff — *every* line shows as changed — even when you only edited one row.

**Why it matters:** the phantom diff buries the real 1-line change and races other agents' edits to the same shared file on the branch = high merge-conflict risk. It also masquerades as content corruption until you check.

**How to apply:**
1. `grep -c $'\r' <file>` before AND after any programmatic edit — count must not change.
2. Edit CRLF files in BINARY mode: `data.split(b"\n")`, modify the target line, preserve its trailing `b"\r"`, `b"\n".join(...)`, write `"wb"`.
3. `printf`-appended rows (LF) into a CRLF file are NON-destructive (clean +N, existing lines untouched) — appends are fine; it's in-place rewrites that flip the file.
4. If you flip a file by accident: `git restore --source=HEAD --staged --worktree <path>` then re-apply in binary mode.

Caught + fixed mid-sweep on VX.tsv (RED 6/23): text-mode edit flipped 26 lines; restored from HEAD, re-applied binary, back to a 1-line diff. Related: [[finding_pathspec_commit_race_safety]], [[finding_concurrent_commit_index_race]].
