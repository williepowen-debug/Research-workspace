# FALCON whole-profile refresh — reader reports index (PAT-100 companion)

Index stub under the canonical name; the raw reader tables, coverage lists and route lists live in the per-reader cluster files beside it. Synthesis: `runs/2026-10-30_FALCON_REFRESH.md` → `profiles/FALCON.md`.

| Reader | Cluster | File | Coverage section |
|---|---|---|---|
| R1 | Architecture / spine (charter, STATUS, MEMORY, LESSONS, SCRATCH, NEXUS_BRIEF, SOURCES, LAST_COMPLETION, thesis, proposals, boot path, read cap, READS) | `R1_ARCHITECTURE.md` | §I |
| R2 | Ledgers, falsification, guards (workbook incl. VX bands and EXIT_PROTOCOL, PREDICTIONS, registry, scripts, board_log, guard runs) | `R2_LEDGERS_GUARDS.md` | §I |
| R3 | Flows, consumers, research/reports/domain census, per-leg ladder (git, inbox/outbox, consumers/producers, DOCKET/GATES) | `R3_FLOWS_REVIEW.md` | §11 |

All three: Claude Opus (general-purpose, model pinned), read-only on tracked files, never launching or messaging FALCON. Launched 2026-10-30 ~17:38 ET at HEAD `b2188833f` (DAEDALUS session 3, Will "Okay go ahead" 17:37 ET). FALCON's last commit before launch: `475f2dea6` 16:49:55 (relaunch under DOCKET L886); possibly live. Prior profile preserved at `profiles/_prior/FALCON_2026-10-30_before_refresh.md` (crc32 3140782960).
