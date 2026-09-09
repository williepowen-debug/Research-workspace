# Validation — September 9 pre-STEO review

- Offline analyze.py completed: exact September 7/August 31 retail series/date checks; all requested strikes found with valid bid/ask and no existing quote flags; seven STEO series extracted; every monthly production/consumption/net-withdrawal identity agrees within 1e-6 mb/d; existing OPEC Q3 baseline reproduced.
- Prediction comparison against saved before-image: 30 rows; only BRT-29 Notes changed. All claims, confidences, windows, status, outcome, invalidation and resolution fields identical.
- Calendar generator/check passed (20 events); standing-state reconciliation check passed. Retail event marked READ, STEO event remains scheduled/pending.
- Explicit 32,550-byte bound checked on STATUS, TRADE, CLAUDE, SCRATCH and NEXUS. STATUS 31,927 bytes after rendering; read_cap_check.py passes with its rotation advisory. Its larger displayed heuristic cap is not the binding budget.
- Relative links in the new report, STATUS and TRADE resolve. git diff --check passes.
- Weekday check: one existing STATUS flag interprets 'Sun Jan 31' as 2026; its surrounding catalyst row is January 31, 2027, which is Sunday. No correction warranted. New report has no weekday flags.
- Orphan check: no uncommitted paths outside BRENT.
- Consumer scans reviewed; dated raw observations/premise history preserved. Live holding mirror and obligation inventory corrected. TERRY scaffold discrepancy recorded for its owner; no external send. See consumer-dispositions.md.
- Ledger nudge reports age/cadence advisory. TRADE and CATALYSTS receive substantive updates this commit. INCIDENTS unchanged because no newer primary-confirmed operating state; board_log unchanged because no packet consumed; REGISTRY unchanged because no letter/instrument changed; LESSONS_INDEX unchanged because no lesson added. KB/VX/FLOW remain frozen. No cosmetic stamps.

Limits: option feeds delayed; no broker access/fill confirmation. Monthly STEO publication and the next weekly physical release are pending. Baseline data re-fetch is not a fresh observation. Future data capture must use a new output location to preserve this evidence.
