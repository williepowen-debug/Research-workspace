# REGINALD whole-profile refresh — reader reports index (PAT-100 companion)

Index stub under the canonical name; the raw reader tables, coverage lists and route lists live in the per-reader cluster files beside it. Synthesis: `runs/2026-10-30_REGINALD_REFRESH.md` → `profiles/REGINALD.md`.

| Reader | Cluster | File | Coverage section |
|---|---|---|---|
| R1 | Architecture / spine (charter, STATUS family, SCRATCH, MEMORY, LESSONS, CALENDAR, ROADMAP, NEXUS_BRIEF, DECK_EVIDENCE, BANK_EXPOSURE_MATRIX, thesis, kernel, boot path, read cap) | `R1_ARCHITECTURE.md` | §I |
| R2 | Ledgers, falsification, guards (workbook, registry, scripts, TRADE/POSITIONS, guard runs) | `R2_LEDGERS_GUARDS.md` | §I |
| R3 | Flows, consumers, review reconciliation, per-leg ladder (git, inbox/outbox, consumers/producers, DOCKET/GATES) | `R3_FLOWS_REVIEW.md` | §11 |
| R4 | Per-bank tree, reports, research (domain/, reports/, research/, earnings_briefs, sources, archives) | `R4_BANK_TREE.md` | §H |

All four: Claude Opus (general-purpose, model pinned), read-only on tracked files, never launching or messaging REGINALD. Launched 2026-10-30 ~16:41 ET at HEAD `9f0975860` (DAEDALUS session 3, Will "yes go ahead" 16:40 ET). Prior profile preserved at `profiles/_prior/REGINALD_2026-10-30_before_refresh.md` (crc32 1434954275).
