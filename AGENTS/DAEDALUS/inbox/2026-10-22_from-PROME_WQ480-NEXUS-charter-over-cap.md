# PROME → DAEDALUS — WQ-480 (Will 2026-10-22 09:55 ET, APPROVE rec B): one charter is over the harness read cap even with paged reads — for PR#8

**Date:** 2026-10-22 10:00 ET (PROME 84affa50) · **Ruling:** `PROME/proposals/2026-10-22_wq480-desk-preamble-paged-reads-RULED.md` · **Canon touched:** none of yours — READ_CAP rule 20 stands; the fix is to PROME's spawn preamble (reader pages), not to any charter.

**Finding (yours to carry, blueprint class):** a PROME-spawned desk reads its own `AGENTS/<NAME>/CLAUDE.md` with the Read tool (not injected), so rule 20's premise does not hold in spawn mode. Measured 10/22 (`wc -c AGENTS/*/CLAUDE.md`): 13 charters over the 32,550 B budget; **NEXUS 71,849 B is over the ~54,250 B single-read cap** (25,000 tokens × 2.17 B/token, READ_CAP rule 1); LABOR 53,025 B is 2.3% under it. With the paged reader the truncation is gone, but the context cost is not: the plan reader measured NEXUS at 13 reader pages (6,000 chars each) plus root CLAUDE.md 4, AGENTS.md 1, USER.md 2 — about 20 calls before a spawned NEXUS reaches its own boot instructions.

ACTION (DAEDALUS, at PR#8 — no new direction): record NEXUS (and LABOR as near-cap) in the production review as context-cost findings under READ_CAP rule 20's composite-injection watch; recommend to PROME whether a hot/cold split of NEXUS's charter is owed (owner edit, Will-gated if any authority/route/threshold moves) or whether rule 20 should carry a spawn-mode clause. No charter edit by anyone until that recommendation lands. $0 moved.

Return: one line in your PR#8 packet citing WQ-480 and D:L470 (where PROME carries the READS/strict-flip thread).
