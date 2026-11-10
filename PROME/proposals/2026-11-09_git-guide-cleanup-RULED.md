# Git guide bounded cleanup — RULED

**Word:** Will, PROME window, 2026-11-09 22:27 ET, verbatim: *"Clean up the Git guide. Move settled historical material out of the live instructions and replace duplicated or conflicting recipes with pointers to their authoritative home. Preserve current safeguards, exceptions, pauses and unresolved obligations. This authorizes the bounded cleanup, not a wider manual redesign."*
**Source of the finding:** CATO `AGENTS/CATO/runs/2026-11-09_2050_process-value-review.md` § PV6; spine audit of 2026-11-07, Git guide row (cookbook paragraphs read as two closeout commit routes).
**Target:** `PROME/GIT_COORDINATION.md`. Pre-edit text: `PROME/archive/GIT_COORDINATION_2026-11-09_pre-cleanup.md` (a byte copy of the file at commit f1c9fd303f under a banner).

## What moves out of the live file

1. § YEYOU, the YEYOU push exception paragraph, § YEYOU Landing Rail, § Reporting, the Boot Integration bullet naming YEYOU, the struck YEYOU clause in Hard Rules, and the founding-two clause in Scope. YEYOU was retired 2026-09-05. A short § History points to the archive.
2. Dated provenance inside the cookbook and Hard Rules (who found what, when). It stays in the archive copy and in `git log -p`.

## What is replaced by a pointer

1. The two adjacent cookbook paragraphs that read as different closeout routes become one table: candidate closeout → `PROME/CLOSEOUT.md` step 10; every other PROME commit → the `commit_check.py` wrapper; broken wrapper → the raw recipe.
2. The raw pathspec recipes, which appeared twice here and again in `docs/GIT_WORKTREE_PROCEDURES.md` § Before committing, are replaced by a pointer to that section.
3. The cookbook's copy of the non-ff recovery text points to § Push Discipline, kept verbatim, and root session-end step 3.

## Invariants (nothing below may change meaning)

- No broad index operations, no amend, no force; messages by `-F` file; pathspec commits; repo-root cwd.
- PROME commits go through the wrapper; the raw form only when the wrapper is broken, declared in the commit body.
- `--push` on the wrapper forbidden at the closeout commit; verify against the delivery SHA, never HEAD; the review gates the push.
- Renames name both paths. Literal filenames only. Stage, commit, verify each pass before any push.
- Non-ff: never force; overlap check first, before any autostash; tripwires unchanged (§ Push Discipline verbatim).
- Carve-outs ①–⑤ mirror, Gate C custody mirror, orphan check and its memory exception: untouched.
- Auto-push exceptions TERRY and WALTER: unchanged.
- Root `CLAUDE.md` / `AGENTS.md`-core commits still need Will's scope.

## Reads (review budget, WQ-178 class: verbatim move plus manual edit)

- **Plan read** (Sonnet cold reader, 2026-11-09 22:3x ET, on the proposed text before any edit): ❌ 1, ⚠️ 6, no live rule lost; four of five pointers resolved. The ❌ was the archive copy not yet existing; it is created in the same commit as the rewrite. Two flags were meaning-class and fixed before the edit: the table had no row for a desk without the wrapper (restored), and a claim that `--stage` is needed for new files and renames had no support (removed).
- **Result read** (second Sonnet cold reader, 2026-11-09 22:3x ET, on the edited file, four situations of its own executed): ❌ 0, ⚠️ 5; eight of eight invariants carried; every pointer resolves. No edit was made after this read.

## Declared residue (flags not fixed, by the review budget)

- The verify command in the cookbook's `--push` rule omits `--paths`; the full command is in `PROME/CLOSEOUT.md` step 10, which the table names as the home.
- The cookbook does not say when `--stage` is required; the wrapper refuses an untracked path on its own.
- § Push Discipline's post-rename assertion names `AGENTS/<ME>/`; for PROME the directory is `PROME/`. Present before this edit.
- Purpose names `SYSTEM.md` without its `PROME/` prefix. Present before this edit.
- The raw-recipe home (`docs/GIT_WORKTREE_PROCEDURES.md`) shows inline `-m` forms beside its own `-F` rule; that file is root-class and outside this cleanup.
- From the plan read: "never the raw form" for PROME is carried by the table's exception wording, not as its own sentence; the dropped § Reporting line on the archived inbox is covered by Purpose.

**Completion states:** IMPLEMENTED · INDEPENDENTLY VERIFIED by the result read as to carried rules and pointers. Not executed live: no closeout has yet been run from the edited text.
