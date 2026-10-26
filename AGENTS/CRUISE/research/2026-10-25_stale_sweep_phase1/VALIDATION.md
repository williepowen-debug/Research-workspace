# Phase 1 validation — October 25, 2026, 22:51 ET

- **170/170 pre-existing owned files unchanged**, SHA-256 compared with `BASELINE.json` after report generation. This covers live state, frozen criteria, ledgers, inbox receipt and the still-pending assignment packet.
- Inventory: 170 unique paths, six fields per row. Findings: 25 unique IDs, ten fields per row; 10 A, 2 B, 4 C and 9 checked-negative cases. No table-shape failures.
- Existing ledger shapes inspected read-only: KB 195 rows / 13 columns; VX 6 / 12; predictions 11 / 9; FLOW 10 / 8 after comment-banner exclusion. No malformed rows.
- KB lifecycle review: five `CURRENT` values are outside the declared schema; 51 past-review candidates include three already `STALE`. These are findings, **not repairs or a claim that the ledger passed enum validation**.
- Deterministic operator-body measurement: first line-start `### ` heading through EOF, UTF-8, 4,470 bytes / CRC32 `4f3bdf32`; current manually typed integrity claim differs. No financial source refresh was used to derive this result.
- Live/frozen files were not rewritten. The RCL guide, NCLH guide, CRU-09 resolver, PREDICTIONS, VX, FLOW, STATUS, TRADE and KB retain their pre-audit hashes.
- The report states per-file inspection limits: 30 full texts read/reused, 5 relevant-section reads, 1 row-metadata/selected-chain ledger review and 134 inventory/header/hash-only files. This is not a full audit of old correspondence, raw source archives or every KB paragraph.
- No network refresh, helper, future-release wait or research process remains running. Phase 2 corrections await PROME's disposition under the committed assignment sequence.

Persistence: exact-path commit and safe-push receipts are delivered to PROME after this artifact is committed; this file does not claim publication before that receipt exists.
