# HOMER refresh 2026-10-28 — READER_REPORTS companion (index; PAT-100 contract = filename AND substance)

The three readers' raw deliverables are persisted verbatim, each in its own file (the substance); this index is the pointer map and the consolidated coverage-limit list.

| Reader | Cluster | File | Bytes | Sections |
|---|---|---|---|---|
| R1 | architecture: charter, STATUS, LESSONS, OBLIGATIONS_OTHERS, brief, MEMORY, SCRATCH, LAST_COMPLETION | `runs/2026-10-28_HOMER_REFRESH_READERS/R1_ARCHITECTURE.md` | 32,011 | 1 identity · 2 anatomy · 3 boot protocol · 4 judgment · 5 richness · 6 DO-NOT-TOUCH · 7 old-profile reconciliation · 8 routing (R1–R13) · 9 limits |
| R2 | thesis/, workbook/, registry/, docket/, state_vectors/, tools/ | `…/R2_LEDGERS_GUARDS.md` | 32,089 | 1 ledger register · 2 invalidation inventory (20 rows) · 3 handle · 4 predictions · 5 TRADE/reading A · 6 guards both directions · 7 reconciliation · 8 routing (10) · 9 limits |
| R3 | reports/, inbox (29 packets read whole), outbox, board_log, DOCKET/GATES/WQ rows, card + 8/22 review | `…/R3_FLOWS_REVIEW.md` | 32,439 | 1 inbox · 2 consumers · 3 outbox · 4 open rows · 5 card/review/profile reconciliation · 6 reports · 7 routing · 8 limits |

**Where each slice landed:** profile §1 ← R1 §1; §2 ← R1 §2 + R2 §1; §3 ← R2 §2–4; §3b ← R2 §2, §6; §4 ← R2 §1, §6; §5 ← R1 §6 + R2 §7; §6 ← R2 §5 + R3 §2, §5; §7 ← R1 §8, R3 §1, §4.

**Consolidated not-read / limits:** cold registers beyond line 40 (crc pins not recomputed); eight workbook ledger bodies (~556 KB) header-lint and targeted rows only; `docket/CATALYSTS.tsv` row 3 ~35 KB unread; `board_log.tsv` rows 2–77; the 8/22 reader reports beyond their route lists; no web verification that the passed-date prints have published; `falsification_scan` behaviour on AEOLUS/MIDAS/OSPREY not checked by R2 (DAEDALUS ran the fleet scan: unchanged); R3 checked DOCKET/GATES/WQ only, not PROME SCRATCH or ORCH_LOG for a HOMER wake.
