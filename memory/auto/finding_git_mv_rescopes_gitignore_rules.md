---
name: finding_git_mv_rescopes_gitignore_rules
description: "git mv-ing a directory silently re-scopes every depth-anchored .gitignore rule that matched it — files just appear untracked, nothing warns; git status immediately after any tree move"
metadata:
  type: finding
---

**`git mv`-ing a directory silently re-scopes every `.gitignore` rule that referenced it by depth.** A single `*` in an ignore pattern matches exactly one path segment, so `AGENTS/REGINALD/*/sources/*.pdf` matches `CFG/sources/` but NOT `archive/per-bank/CFG/sources/` — move the tree one level deeper and the rule stops matching with **no warning of any kind**: the previously-ignored files simply appear as untracked in the next `git status`, where they look like new work rather than a side effect.

**Worked case (REGINALD R2 archive, 2026-08-13):** the Will-approved per-bank subtree archive (`git mv` to `archive/per-bank/`) un-ignored ~17 large source binaries (PDFs/xlsx). REGINALD caught it by running `git status` after the move and verified the mechanism both ways with `git check-ignore -v`; PROME applied the re-scoped rules to root `.gitignore` (`cc2e2e063`), following the WAL-promotion precedent of handling ignore semantics in/with the same changelist as the move.

**Why it matters:** untracked large binaries sitting in a shared multi-agent tree are one careless commit away from entering history (public-facing repo), and they pollute every other agent's `orphan_check` as `[not yours]` noise.

**Apply:**
1. **`git status` immediately after ANY tree move** (agent promotion, archive sweep, spinout) — the appearing-untracked-files symptom is the only visible signal.
2. When planning a move, **grep `.gitignore` for the path being moved** and re-scope matching rules in the same changelist (the WAL precedent: "same semantics at the new path").
3. `git check-ignore -v <old-path-example>` vs `<new-path-example>` proves the mechanism in seconds — verify both ways before and after.

**n+1, the mirror image (REGINALD, same day 2026-08-13): the hazard is UNTRACKED-only.** The second archive move of the day (sub-agent fossils, 33 files, same operation) produced ZERO un-ignores — because those files were tracked. Tracked files are immune to ignore-rule re-scoping (ignore rules govern what git *starts* tracking, not what it already tracks); untracked files are exactly what a depth-anchored rule stops shielding. So the post-move `git status` check is mandatory either way, but the risk profile is knowable in advance: `git ls-files <dir> | wc -l` vs a `find` count tells you how much of the tree is exposed before you move it.

Related: [[finding_pathspec_wildcard_ending_at_directory_matches_nothing]] (same single-segment-glob surprise in git pathspecs), [[finding_pathspec_rename_needs_both_paths]], [[finding_gitignored_private_drop_boot_surfaced]] (the discoverability half of ignored files).
