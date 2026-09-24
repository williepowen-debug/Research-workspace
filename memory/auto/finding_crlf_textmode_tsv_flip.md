---
name: finding_crlf_textmode_tsv_flip
description: TWO independent ways a programmatic edit silently rewrites a WHOLE state file — text-mode CRLF→LF flip, and csv.writer re-quoting — producing a destructive whole-file diff that buries your real 1-line change; the reliable guard is the git diff line count, not the CR count
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

---

## ⚠️ SECOND MECHANISM — `csv.writer` re-quoting (CARL 2026-08-12). It DEFEATS the guard above.

There are **two independent ways** to silently rewrite a whole state file, and the CR-count check only catches one.

**`csv.writer(...).writerows(rows)` re-derives every field's quoting from scratch.** Hand-maintained TSVs routinely carry quotes the library would not add (e.g. a field quoted because it contains a comma — irrelevant to a TAB-delimited file, so `QUOTE_MINIMAL` strips it). Result: **every row rewritten**, same as the CRLF flip.

**Why this is worse than the CRLF case:** `csv.writer`'s default `lineterminator` is **`\r\n`**, so on a CRLF file it *preserves* line endings — **`grep -c $'\r'` is unchanged before and after, and step 1 above passes clean while the whole file has been rewritten.** On an LF file it does the reverse and injects CRLF everywhere.

**Both mechanisms, same session, two files in one directory (CARL 8/11-12):**
- `workbook/KB.tsv` (**LF**) — a 1-row append via `csv.writer` → `379 insertions(+) / 378 deletions(−)`. Reverted; re-appended as raw text → `1 insertion(+)`.
- `thesis/PREDICTIONS.tsv` (**CRLF**) — a 2-field string replace in text mode → `29/29`, the entire file. **Could not `git checkout`** — the same file held an hour of uncommitted grading work — so it had to be repaired in place: `data.replace(b'\n', b'\r\n')` after asserting no `\r\n` remained. Back to `3/3`, the rows actually touched.

**Line-ending convention is PER FILE, not per repo or per directory** — `KB.tsv` is LF and `PREDICTIONS.tsv` is CRLF, siblings under one agent. Never infer one from the other. (Matches the RED observation above: mixed even within one agent dir.)

**The guard that actually works, and the one to run:**
1. **`git diff --stat <file>` after EVERY programmatic edit. The insertion count must equal the number of rows you meant to change.** This is mechanism-independent — it catches quoting, line endings, encoding, and trailing-newline changes at once. The CR-count check (step 1 above) is necessary but **not sufficient**.
2. **Prefer appends over rewrites.** A raw append (`open(p,'a')` writing the file's own terminator) touches nothing existing.
3. **Never `csv.writer` a hand-maintained ledger.** Read with `csv.reader` if you need parsing, but write by string surgery on the raw bytes.
4. **Check for a trailing newline before appending** — `raw.endswith('\n')` — or your row fuses onto the last one.
5. **Repair beats revert when the file holds uncommitted work.** `git checkout` is the reflex and it would have destroyed an hour of grading; convert the endings in place instead.

**Meta-lesson worth more than the mechanics:** this memory already existed, in full, with the correct fix — and CARL hit the class anyway, twice, in one session. Reading a trap taxonomy at boot is not the same as running its check at the moment of writing ([[finding_threshold_spec_fails_before_world]] has the identical shape at registration-time). **The check has to fire where the edit happens: make `git diff --stat` reflexive after touching any shared TSV.** Sibling class: [[finding_printf_format_tsv_append_corruption]].

**Instance n=4 (BOND, 2026-09-24) — the guard FIRED and was not read.** A `csv.writer` rewrite of `AGENTS/BOND/workbook/KB.tsv` to flip 2 rows re-quoted **14 other rows** whose text contains `"`; `git diff --stat` printed **26 insertions / 15 deletions** where 2 row changes were expected — on screen — and it was committed anyway. Caught only on the NEXT file (VX.tsv: 6 lines for 4 rows). Repaired by restoring the unintended rows byte-for-byte from the pre-session commit (no amend). **The operational addition: the diff-count guard only works if you compare it to the number you EXPECTED before looking — write the expected row count down first, then read `--stat` against it.** Safe idiom for these TSVs: `line.split("\t")` / `"\t".join(...)`, never `csv`.
