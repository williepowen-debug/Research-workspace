# BOND Receipt — 2026-09-29 (Will boot 12:3x ET → closeout ~15:5x ET; PROME prome-e6 doorbells ×4, WALTER ×3, NEXUS ×1)

| File / input | Action | Why | Workbook rows | STATUS change | Outbox / messages |
|---|---|---|---|---|---|
| Live tape 12:3x ET (yfinance, rates_context) | INTEGRATE | Will: "yields continuing to rise" | `KB-BND-361` (→ STALE 15:5x) | top item, bottom line | — |
| PROME doorbell 12:5x (attribution · book · nearest lines) | DELIVER | Will's ask | `KB-BND-362`, `KB-BND-363`; page `analysis/2026-09-29_WQ-317_PARTIAL_same-day-attribution_book-lines.md` | top item, bottom line, rotation (snapshot `2026-09-29b`) | receipt → `PROME/inbox/` + SendMessage |
| PROME follow-up 13:0x (pre-registration) | DELIVER | Will's follow-up | `BND-30`, `BND-31` in `thesis/PREDICTIONS.tsv`; page §6 | scoreboard OPEN 0→2 | SendMessage |
| `inbox/WALTER/SIG-W-20260929-001.md` | INTEGRATE → processed | 9/29 gaps SEARCH-NOT-FOUND | `KB-BND-364`; `board_log.tsv` | — | SendMessage ack |
| PROME 13:4x NEXUS_BRIEF drift + NEXUS read-cap flag | FIX | brief 3 state changes late AND 147% of cap | — | — | `NEXUS_BRIEF.md` re-pinned then rotated (8.3 KB; snapshot `domain/sources/2026-09-29_NEXUS_BRIEF_full-snapshot_pre-cap-rotation.md`); SendMessage ×2 |
| PROME 13:4x AUCTION_HEALTH cold read | BANNER + DOCKET | stale corpus block; bar-rule ambiguity; dealer-max check | ledger preserved `analysis/2026-09-29_PROME-coldread_AUCTION_HEALTH_ledger.md` | — | 10/1 §3d row extended; SendMessage |
| `inbox/WALTER/SIG-W-20260929-003.md` · `-012.md` | INTEGRATE → processed | credit tape; PM path −5bp | `KB-BND-365`, `KB-BND-366`; `KB-BND-346` → CORRECTED; `board_log.tsv` ×2 | top item PM line | SendMessage ack |
| Will: TRADE.md condition | RE-BASE | view inverted vs live tape | — | — | `TRADE.md` (snapshot `archive/2026-09-29_TRADE_pre-view-rebase-snapshot.md`) |
| Treasury par/real CSV 15:55 ET | INTEGRATE | official 9/29 close | `KB-BND-367`; `VX-BND-05` refreshed | dashboard, gates, top, bottom line | NEXUS_BRIEF pin line |
| `inbox/2026-09-29_from-NEXUS_…` | READ (NEXUS committed it, `83e6fe366`) | flag-only | — | — | — |

Catalysts: 10/6 row 'TBA' clause resolved (closeout_check finding). Predictions: OPEN 2 (BND-30/31), none DUE. Ledgers: VX refreshed (VX-BND-05); FLOW unchanged — no transmission channel confirmed or changed today (attribution PARTIAL/UNDETERMINED). Closeout checks: kb_lint rc0 · closeout_check rc1→fixed · claim_check clean · orphan [not yours] only · read_cap BOND rc0. Git: path-scoped commits ×13 + `scripts/safe-push.sh` at closeout.
