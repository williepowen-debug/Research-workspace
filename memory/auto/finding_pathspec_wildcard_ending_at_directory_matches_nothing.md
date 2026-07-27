---
name: finding_pathspec_wildcard_ending_at_directory_matches_nothing
description: "A git pathspec containing a wildcard AND ending at a directory matches ZERO files, silently — and piping it through `git status` into a shell variable suppresses the one error git would have raised"
metadata: 
  node_type: memory
  type: reference
  originSessionId: f0bad791-6fdb-4cd3-8e7e-6057db95d7db
  modified: 2026-07-27T18:51:42.292Z
---

**`git ls-files -- 'AGENTS/*/inbox/WALTER/'` returns NOTHING. So does the form without the trailing slash. `AGENTS/*/inbox/WALTER/*` returns 904.**

Measured on this repo, 2026-07-27:

| pathspec | matches |
|---|---:|
| `AGENTS/*/inbox/WALTER/` | **0** |
| `AGENTS/*/inbox/WALTER` | **0** |
| `AGENTS/*/inbox/WALTER/*` | 904 |
| `AGENTS/` *(no wildcard)* | 904 |

**The rule: a wildcard pathspec must have something to match the FILENAME against. A plain directory prefix with no wildcard works fine; a pattern that contains `*` and stops at a directory matches no paths at all.** It is the *combination* that is inert, which is why it looks reasonable.

**What it cost (WALTER, 2026-07-27):** 21 of 25 per-recipient delivery handoffs for `SIG-W-20260727-017..020` were written to disk, logged in `delivery_log.tsv` as `written_state=delivered`, and **never committed.** They were invisible to every recipient who was not already reading the working tree.

**🔴 THE PART THAT MAKES IT DANGEROUS — the failure is silent at every step:**
```sh
NEW=$(git status --porcelain -- BOARD/ 'AGENTS/*/inbox/WALTER/' PROME/inbox/ | awk '$1=="??"{print $2}')
git add $NEW
```
Handed that pathspec directly, **`git add` would have errored** — *"pathspec did not match any files."* Routing it through `git status` into a shell variable **suppressed the only error git would have raised**: `git status` exits 0 with empty output, and `$NEW` still contained the files matched by the *other* pathspecs in the same command, so `git add` succeeded on a partial set. Every step returned success.

**How to apply:**
- **Never build a commit set from a computed/globbed pathspec.** Use explicit paths, which is what the repo protocol already says for new untracked files — this incident was that rule violated, not a gap in it.
- **If you must glob, terminate the pattern at the FILE** (`.../*`), or use `:(glob)` magic explicitly, and **assert the count** rather than eyeballing it.
- **`git diff --cached --stat | tail -2` is not verification.** It shows the last two lines of the diff and says nothing about how many files are missing. **A tail is not a count.**
- **The durable guard is a cross-check between surfaces, not care:** compare *what the ledger CLAIMS was written* against *what git actually tracks*. WALTER mechanized this as the `walter_doctor` check `delivery_claim_vs_git` (#23) — MED when a row logged today claims `delivered` while its file is untracked, HIGH once it crosses a session boundary.
- **When building that kind of guard, test it before shipping:** the first cut flagged 17 false HIGHs (a retired inbox directory + one agent that consumes by deleting rather than moving). **A file gone from disk is usually SUCCESS; only a path git has never seen is an orphan.**

Sits with [[finding_pathspec_commit_race_safety]], [[feedback_check_staged_before_commit]] and [[finding_loadbearing_number_must_be_reproducible]]. The orphaned-packet consequence is the class the root `CLAUDE.md` carve-out ① exists to prevent.
