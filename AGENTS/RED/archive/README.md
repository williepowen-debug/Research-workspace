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

## What was archived into it on 2026-08-20 (S33, Phase 2)

**3 files**, every one verified zero-reference on **four** axes before moving: RED's live docs, RED's TSV ledgers (`workbook/` · `docket/` · `registry/`), and a **fleet-wide external-consumer grep** (`finding_external_consumer_check_before_restructure` — another agent's link breaks on a move just as badly as your own).

| File | Vintage | Reference status |
|---|---|---|
| `workbook/CHG-RED-005_EVENING_CHALLENGE.md` | 2026-02-18 | zero on all four axes |
| `workbook/CHG-RED-005_REVISED.md` | 2026-02-18 | zero on all four axes |
| `workbook/RUSSIAN_OIL_CHALLENGE.md` | 2026-03-04 | sole referrer is `AGENTS/_archive/DOC/REPORT.md` — itself archived. An archive→archive link is coherent; the move **improves** it |

**⚑ Held back, and the reason is a finding the 8/12 pass did not have: THE CANDIDATE LIST IS NOT A LIST OF FILES, IT IS A GRAPH.** Three more qualified on age and on RED's own live-doc scan — `challenges/KRE_CHALLENGE.md` (2/20), `challenges/KRE_CHALLENGE_SUMMARY.md` (4/03), `challenges/KRE_DEBATE_PREP.md` (4/03) — and the external check found they are **cross-linked to each other and to `workbook/KRE_EXECUTIVE_SUMMARY.md`**, which is one half of the R13 name collision already held back above. **Retiring the leaves while the root waits on T11 would leave that root pointing into `archive/` — strictly worse than leaving the cluster alone**, and it is the same reasoning that held the root back in the first place, applied one edge further out. **The whole KRE cluster moves together after T11, or not at all.**

**Method note for the next pass:** age-ranking plus a live-doc grep is necessary and not sufficient. Run the **external** grep too, and then ask whether a survivor points at anything you are about to move. A file with zero referrers can still be a **referrer**, and that direction is invisible to a check that only counts inbound links.


## 2026-10-15 (S53) — KRE February debate set archived; the R13 basename collision is RESOLVED

Moved under the retirement rule on Will's 10/14 item #16 (the files still said FHLB "$480B", corrected 10/14 in the live `workbook/KRE_EXECUTIVE_SUMMARY.md`): `challenges/KRE_CHALLENGE.md` → `KRE_CHALLENGE_2026-02-20.md` · `challenges/KRE_CHALLENGE_SUMMARY.md` → `KRE_CHALLENGE_SUMMARY_2026-04-02.md` · `challenges/KRE_DEBATE_PREP.md` → `KRE_DEBATE_PREP_2026-04-02.md` · `challenges/KRE_EXECUTIVE_SUMMARY.md` → `KRE_EXECUTIVE_SUMMARY_2026-02-20_challenges-copy.md`. Each carries a DATED-HISTORY banner naming the wrong figure. **The held-back R13 collision (two `KRE_EXECUTIVE_SUMMARY.md` with opposite verdicts) no longer exists: the only file of that basename is the live `workbook/` one.** The three index-style references in the live summary now point here (clause ②: an index reference is not a live-doc reference, so these were retirement-eligible). Qualifier: the "challenges-copy" file is the Feb-20 verdict (thesis valid 75%, timing mispriced); the live workbook file is the 10/14-corrected successor.


## 2026-10-15 (S53) — retirement sweep on the cold audit (check 6): 10 files moved, 0 held

Rule: >60d since last commit, not boot-read, not referenced by a live analytical/protocol doc (clause ②: references from RED's own append-only logs — `ML.tsv`, `OUTBOX.md`, `thesis/CHANGELOG.md`, `MAINTENANCE.md` — and from `archive/` or `inbox/*/processed/` are RECORDS, not live docs a reader travels; RED rules so here, on the owner's call the audit left open). Moved verbatim, basenames unchanged: `challenges/SSB_CHALLENGE.md` (8/07) · `challenges/VIOLET_SAM_RESPONSE_GRADING_2026-06-11.md` · `challenges/VIOLET_SKEW_CHALLENGE.md` (4/19) · `challenges/SAM_PREBOJ_STRESSTEST_2026-06-10.md` · `research/STALENESS_AUDIT_2026-06-02.md` · `research/WAL_OZK_APR21_FRAMEWORK.md` (4/18) · `outbox/2026-07-10_to-PROME_chg041-final-grade.md` · `outbox/2026-07-24_to-PROME_chg043-premium-breadth-redteam.md` · `outbox/2026-07-24_to-PROME_s24-remark-and-grades.md` · `outbox/2026-07-29_to-PROME_fomc-graded-registry-closed-remark.md`. Not moved: `LAST_COMPLETION.md` (eligible 10/16, charter keeps it on disk as a dated artifact — archive it then); `MEMORY_ARCHIVE.md` and `CHALLENGE_IMPACT_LEDGER.md` (charter-named; CHALLENGE_IMPACT_LEDGER FROZEN-bannered today instead, census 43 of now 54 challenges); `thesis/TIMELINE.md` (FROZEN-bannered today, v3 6/22 framework superseded by the six-hypothesis set).
