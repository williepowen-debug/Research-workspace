# RED `archive/` — retired-but-preserved working files

**Recreated 2026-08-12 (S30 / T8), Will-ruled: *"RED should have its own archive."***

## What this is

The destination for the root-`CLAUDE.md` retirement rule: a file that is **>60 days old AND not boot-read AND not referenced by a live doc** gets `git mv`'d here rather than deleted. It exists so retirement is **lossless and reversible** — the alternative is a research graveyard in `challenges/`, `research/` and `reports/`, or deletion.

**Nothing here is live. Do not cite a figure from this directory as current.** Live surfaces: `STATUS.md` (state), `thesis/CHANGELOG.md` (analytical history), `MAINTENANCE.md` (structural history), `workbook/*.tsv` (ledgers).

## Why it had to be recreated

`AGENTS/RED/archive/` was **deleted on 2026-06-30** by `1cb18fbc3` *("PROME: prune dead 0-ref agent archives (public-prep track A)")*, which removed **38 RED files** across 12 agents fleet-wide.

⚠️ **The prune's "0-ref" premise was FALSE for at least two of RED's files, and the dangling references outlived the content by six weeks:**

| Deleted file | Was referenced by |
|---|---|
| `archive/RED_SKELETON.md` | `CLAUDE.md` FILES table **and** `MEMORY.md` |
| `archive/status_snapshots/STATUS_2026-04-02.md` | a **live markdown link in `MEMORY.md`** — a boot-read file |

**Every deleted file remains recoverable at `1cb18fbc3^`.** The content was never lost; what broke were the pointers. Those pointers now cite the SHA instead of claiming a path that does not exist — see `CLAUDE.md` and `MEMORY.md`.

**The prune itself is NOT reversed here.** It was a deliberate public-prep decision that is not RED's to undo; this directory is a working destination going forward. *If any pruned file should come back, that is a Will/PROME call and the SHA above is where it lives.*

## What was archived into it on 2026-08-12

**14 files**, each verified unreferenced by any live RED surface **under both a loose and a strict reading** of "referenced" (loose counts a received `inbox/processed/` packet; strict counts only RED's own live docs — the two readings differed on exactly one file).

⚠️ **The reference-check found the opposite of what the audit extrapolated.** The 8/12 architecture audit spot-checked *"5 of 5 oldest — UNREFERENCED."* **That was accurate about those five and badly unrepresentative of the population: 19 of 33 candidates (58%) turned out to be REFERENCED.** Age correlates with reference-status, so **ranking candidates by age and sampling the top biases the estimate toward "unreferenced"** — generalizing from it would have retired 19 files that live surfaces cite. *(ML-RED-175.)*

**Held back deliberately:** `challenges/KRE_EXECUTIVE_SUMMARY.md` — unreferenced on the strict reading, but it is one half of the **R13 name collision** (two different documents share that basename with **opposite verdicts**: this one red-teams KRE at 45% *"WILL LOSE MONEY"*, `workbook/KRE_EXECUTIVE_SUMMARY.md` is a 75% *"A-"* bull case). **Archiving one half while the other stays live makes the collision worse** — a reader finding the survivor would have no signal that a contradicting twin exists. Resolve the collision first (T11), then retire.
