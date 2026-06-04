# Pathspec Migration Status
**Updated:** 2026-06-04 ~17:25 ET
**Owner:** Prome
**Source:** `AGENTS/SAM/outbox/2026-06-04_to-PROME_pathspec_per_agent_CLAUDE_md_audit.md`

## Why this exists

SAM's Jun 4 audit found that several per-agent `CLAUDE.md` files still hardcode broad staging reset patterns such as `git reset HEAD`. In the shared-repo setup, that can clobber another agent's concurrent staged work. Interim rule: agents must migrate their own commit protocol to pathspec commits until a separate-clones/worktrees architecture is approved.

## Rule Prome Tracks

- Each agent edits **only its own** `AGENTS/<NAME>/CLAUDE.md`.
- Replace any broad `git reset HEAD` / directory-stage commit protocol with pathspec discipline.
- Modified tracked files: `git commit AGENTS/<NAME>/<file> -m "..."`.
- New untracked files: `git add <specific files> && git commit <same specific files> -m "..."`.
- Never `git add .`, never `git add -A`, never broad `git reset HEAD`.

## Checklist

| Agent | File | Sites | Status | Evidence / Next |
|---|---|---:|---|---|
| SAM | `AGENTS/SAM/CLAUDE.md` | 1 | ✅ Done | SAM reports fixed in Jun 4 commit `687e2968`. |
| PROME | `AGENTS/PROME/CLAUDE.md` | 1 | ✅ Done locally | Prome updated own Git Protocol block in this ingestion pass. |
| BRENT | `AGENTS/BRENT/CLAUDE.md` | 1 | ⬜ Pending owner edit | Agent must edit own file at next boot. |
| HENRY | `AGENTS/HENRY/CLAUDE.md` | 1 | ⬜ Pending owner edit | Agent must edit own file at next boot. |
| MARCO | `AGENTS/MARCO/CLAUDE.md` | 1 | ⬜ Pending owner edit | Agent must edit own file at next boot. |
| OTTO | `AGENTS/OTTO/CLAUDE.md` | 1 | ⬜ Pending owner edit | Agent must edit own file at next boot. |
| OZK | `AGENTS/OZK/CLAUDE.md` | 2 | ⬜ Pending owner edit | Two sites; agent must edit own file at next boot. |
| VIOLET | `AGENTS/VIOLET/CLAUDE.md` | 1 | ⬜ Pending owner edit | Agent must edit own file at next boot. |
| WALTER | `AGENTS/WALTER/CLAUDE.md` | 1 | ⬜ Pending owner edit | Agent must edit own file at next boot. |

## Prome Next Actions

1. Keep this tracker boot-visible until all rows are ✅.
2. When each owner reports completion, update the checklist with evidence commit/file.
3. Do not edit other agents' files from Prome unless Will explicitly overrides the owner-isolation rule.
