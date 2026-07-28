---
name: finding_pathspec_wildcard_ending_at_directory_matches_nothing
description: "A globbed git pathspec can add NOTHING while returning success — n=2 in two days, different globs, same cause: the stderr that would have said so was suppressed. Explicit paths, never suppress git add's stderr, verify by COUNT"
metadata: 
  node_type: memory
  type: reference
  originSessionId: f0bad791-6fdb-4cd3-8e7e-6057db95d7db
  modified: 2026-07-28T14:22:40.507Z
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

---

## 🔴 RECURRED 2026-07-28 — n=2 IN TWO DAYS. DIFFERENT GLOB, IDENTICAL CAUSE, AND THE AUTHOR OF THIS FILE IS THE ONE WHO REPEATED IT.

```sh
git add BOARD/SIG-W-20260728-00{3,4,5,6}-*.md \
        AGENTS/{VULCAN,LIQUID,SAM,...15 agents...}/inbox/WALTER/SIG-W-20260728-00{3,4,5,6}-*.md 2>/dev/null
```

**Brace expansion produced the full 15×4 cross-product, but most recipients hold only a SUBSET** (VULCAN got `-003` and not `-004/-005/-006`). **`git add` aborts entirely if ANY pathspec matches nothing — so it added NOTHING — and `2>/dev/null` swallowed the one error that would have said so.** The commit then reported **"4 files changed"** when the work was ~30: **28 files (4 BOARD signals + 24 handoffs) left untracked while `delivery_log` already claimed them written.**

**🔑 THE GENERALISATION, which is what makes this worth re-reading rather than a second anecdote:**
- **The 7/27 instance and the 7/28 instance share NO mechanical detail.** One was a wildcard stopping at a directory; the other was a brace cross-product with missing members. **Learning "don't end a glob at a directory" would NOT have prevented the second one.**
- **What they share is the SHAPE: a computed/globbed pathspec, plus something that hid git's stderr.** On 7/27 it was routing through `git status` into a shell variable; on 7/28 it was a literal `2>/dev/null`. **The glob is the hazard; suppressing stderr is what makes it silent.**
- **⇒ The durable rule is not about glob syntax at all. It is: NEVER SUPPRESS `git add`'s STDERR, and never build a commit set from a pattern.** git *does* tell you — both times it was prevented from speaking.

**What caught it (7/28):** the commit summary line. **"4 files changed" against ~30 files of work is a tripwire that needs no tooling** — a commit reporting far fewer files than the session produced is itself the alarm. *(`delivery_claim_vs_git` would also have caught it at the next boot; the summary line caught it in ten seconds.)*

**Recovery recipe that worked, and is now the default for any multi-recipient commit:**
```sh
git status --porcelain | awk '$1=="??"{print $2}' | grep -E '<scope regex>' > /tmp/tocommit.txt
grep -vE '<allowed scope>' /tmp/tocommit.txt   # scope-check BEFORE adding
xargs -a /tmp/tocommit.txt git add --          # stderr VISIBLE, rc checked
git diff --cached --name-only | wc -l          # a COUNT, not a tail
```

---

**How to apply:**
- **Never build a commit set from a computed/globbed pathspec.** Use explicit paths, which is what the repo protocol already says for new untracked files — this incident was that rule violated, not a gap in it.
- **If you must glob, terminate the pattern at the FILE** (`.../*`), or use `:(glob)` magic explicitly, and **assert the count** rather than eyeballing it.
- **`git diff --cached --stat | tail -2` is not verification.** It shows the last two lines of the diff and says nothing about how many files are missing. **A tail is not a count.**
- **The durable guard is a cross-check between surfaces, not care:** compare *what the ledger CLAIMS was written* against *what git actually tracks*. WALTER mechanized this as the `walter_doctor` check `delivery_claim_vs_git` (#23) — MED when a row logged today claims `delivered` while its file is untracked, HIGH once it crosses a session boundary.
- **When building that kind of guard, test it before shipping:** the first cut flagged 17 false HIGHs (a retired inbox directory + one agent that consumes by deleting rather than moving). **A file gone from disk is usually SUCCESS; only a path git has never seen is an orphan.**

Sits with [[finding_pathspec_commit_race_safety]], [[feedback_check_staged_before_commit]] and [[finding_loadbearing_number_must_be_reproducible]]. The orphaned-packet consequence is the class the root `CLAUDE.md` carve-out ① exists to prevent.
