---
name: finding_grep_respects_gitignore_so_ignored_zones_are_invisible
description: The harness `grep` is a shell function running with --ignore-files, so a recursive sweep from the repo root silently skips every gitignored path — "I grepped the repo and found nothing" is a false negative for ignored zones
metadata:
  type: reference
---

`grep` in Claude Code sessions on this box is **not** GNU grep — it is a shell
function (`type grep` to see it) that execs `claude -G --ignore-files --hidden
-I --exclude-dir=.git …`. **`--ignore-files` makes it honor `.gitignore`.**

**Consequence:** `grep -rn "X" .` from the repo root **silently returns zero
hits inside gitignored paths.** No warning, no "skipped N dirs" line — the
scan simply reports absence. Measured live 2026-08-19: a repo-root sweep for a
string returned only unrelated hits while three files under `WILL/private/`
contained it 5 times; `grep -rn "X" ./WILL` found all three immediately.
**Naming the path explicitly works; walking from the root does not.**

**Ignored zones in this repo that a root sweep cannot see:** `WILL/private/`,
`WILL/trading-journal/`, `.venv/`, every `.env` (incl. the credential
single-home `FORGE/tools/market-data/.env`), REGINALD/WAL/SHADE source PDFs,
`__pycache__`, `*.log`.

**Fix, when the answer must be complete:**
- Name the path explicitly: `grep -rn "X" ./WILL ./FORGE` — works inside ignored trees.
- Or bypass the function: `command grep -rn "X" .` / `\grep`.
- Or, when you specifically want tracked files only, say so — that is a
  legitimate scope, just declare it rather than calling it "the repo."

**Why it matters beyond convenience:** every "does anything still reference X
before I delete/rename it?" sweep under-reports by exactly the ignored set, and
ignored zones are where the *private* consumers live. Same failure family as
[[finding_comprehensive_grep_over_sampling]] and
[[finding_git_mv_rescopes_gitignore_rules]] — a scan certifies its SCOPE, not
your question ([[finding_verification_zero_is_ambiguous]]). Pairs with
[[finding_gitignored_private_drop_boot_surfaced]]: gitignored material needs a
deliberate discovery path precisely because the ordinary tools cannot see it.
