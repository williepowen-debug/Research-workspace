# MEMORY.md — HOMER Durable Notes

*Will's working preferences, do-not-touch quirks, and provenance facts that don't belong in STATUS (live data) or LESSONS (mistake patterns). Thin by design — grows only with genuinely durable facts.*

---

## Promotion Provenance

- **2026-07-12:** Promoted from `AGENTS/CARL/sub_agents/HOMER/` to top-level `AGENTS/HOMER/` via `git mv` (history preserved). Will-directed, same-day execution — overrode CARL's own recommendation to wait until the post-7/24 quiet window (compressed review, not skipped; DAEDALUS structural review at `AGENTS/DAEDALUS/builds/homer_promotion/PROMOTION_REVIEW.md`). Case originated from CARL: `AGENTS/DAEDALUS/inbox/2026-07-12_from-CARL_homer-promotion-case.md`.
- Zero live external consumers existed outside CARL's tree at promotion time (verified by DAEDALUS's comprehension pack) — the lowest-risk promotion of the OZK/CORAL/AEOLUS/HOMER precedent set.
- HOMER jumped the ROSTER promotion queue ahead of WAL (Will's explicit 7/12 call, recorded not re-litigated — WAL remains next-candidate).

## Do-Not-Touch / Structural Quirks

- **`workbook/KB.tsv` is FROZEN (2026-07-10)** — parent-era canonical KB, ~65 rows, CARL_ID provenance column intact. Do not append to it; do not renumber it. New rows go to `workbook/KB_LIVE.tsv`. The freeze banner is the row-ID-stability contract — breaking it breaks the delegation provenance CARL's own KB still cites.
- **`state_vectors/corrected/` is a retrieval hazard, not a normal subdirectory.** It holds exactly one withdrawn/superseded SV (SV-HOMER-2026-06-08-01). CARL's old harvest globs (and any future search) do NOT descend into `corrected/` — a valid/live SV must never be filed there. Kept as historical record only; the SV channel itself is retired (see CLAUDE.md).
- **`archive/` holds pre-promotion build artifacts** (GAP_ANALYSIS.md, REPORT.md, SPAWN1_DATA_REFRESH.md, UPDATE_PLAN.md) — Apr-vintage, already flagged in-file as archive candidates by the 7/10 verification pass. Historical record; no action needed unless a future sweep wants to prune further per the Data Hygiene >60d rule.
- **`domain/` exists but is empty** — carried over from the pre-promotion structure, no files as of promotion. Leave as-is; a future session may populate it with research/deep-dives per the original CLAUDE.md's Key Files intent.

## Cross-Agent Facts Worth Remembering

- REGINALD independently sources the same monthly Trepp CMBS-MF print HOMER now owns — predates the promotion, not caused by it. See LESSONS.md + docket for the pending reconciliation.
- CREED (Tier-2, spawned-as-needed) has no live workbook of its own as of its 2026-07-04 STATUS — an MF-absorb decision here is a scope decision (who owns the row going forward), not a file migration.
