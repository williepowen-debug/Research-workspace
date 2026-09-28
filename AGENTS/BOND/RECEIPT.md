# BOND RECEIPT — 2026-09-28 16:22 ET (boot, third session of 9/28)

| Item | Disposition |
|---|---|
| Inbox (WALTER lane) | 3 deliveries → `inbox/WALTER/processed/`: -005 → `KB-BND-351` · -007 → `KB-BND-352` · -009 → folded into `KB-BND-350` |
| Inbox (general) | not swept (separate task) |
| Official 9/28 Treasury curve | ✅ pulled (par + real CSV) → `KB-BND-350`; STATUS rates rows, gate table, bottom line |
| Boot checks | docket_check rc0 (verified through 10/8) · corrections rc0 · boot_recompute rc0 · kb_lint rc0 after a Group fix |
| Correction sent | WALTER -007 "Sept issuance settles SECOND" → vintage TIE; packet `AGENTS/WALTER/inbox/2026-09-28_from-BOND_SIG-W-20260928-007-sept-issuance-not-settled.md` (🟡, carve-out ①) |
| Matrix / predictions | 14/35 unchanged · OPEN 0 · no DUE rows |
| Position | TLT Sep-30 77P ×20 HOLD, no add, `$0`; TLT $78.62 [16:19 ET] — TERRY's rail |
| Files written | STATUS · SCRATCH · RECEIPT · KB (+350/351/352) · WALTER inbox packet |
| Git | see commit following this receipt |
| PROME/CATO correction (16:25 packet) | ✅ refi-wall note: two conclusions narrowed in place (A&E-share "concentration" → GAP; aggregate timing → index-level only, CCC/single-name 2026–27 tail UNMEASURED) + mirrors KB-BND-349 / SCRATCH 7b / STATUS 0000②; packet → `inbox/processed/` |
| Will deep-dive: front end | ✅ `analysis/2026-09-28_front-end-led-move.md`, `KB-BND-353` (`e99a4c350`) |
| Will ask: coverage gaps | ✅ `analysis/2026-09-28_coverage-gap-review.md` (`31ed20c42`) |
| Will "go ahead with 1+2+3" | ✅ `monitors/rates_context.py` (selftest 14/14) wired into `boot_recompute.py` (rc=0) · `KB-BND-354` · VX-BND-17 notes · CLAUDE.md FILES row · STATUS Fed-path + ACM/KW rows · T5YIFR 16→15bp fixed (both lines) · STATUS rotated (snapshot `2026-09-28c`, crc32 1800580424) |
| WQ-317 | APPROVED (Will 17:16 ET, verified) — packet left in inbox for the 10/1 session |
