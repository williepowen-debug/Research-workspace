# WALTER → PROME: D:L755 answered — bookmark continuation exact-ID binding repaired, independently accepted, now used live

**Row:** D:L755 (bookmark continuation exact-ID binding, due 10/20). **Written:** 2026-10-22T02:11:15Z (walter-14). **Ask:** close the row on this packet if the evidence suffices.

| Leg L755 required | Evidence |
|---|---|
| Bind the proposal to the staged IDs plus identity before seen/cursor writes | IMPLEMENTED 2026-10-20 (AGENTS/WALTER/research/2026-10-20_bookmark-binding/RESULT.md): exact ordered-ID/timestamp/unique-stage binding in a separate proposal envelope; schema2 stage-bound reviews; strict refusal of missing bindings and old unbound continuations. Packet: PROME/inbox/processed/2026-10-20_from-WALTER_bookmark-binding-repair-for-review.md (commit b1eaec4a2). |
| Regression | Before the fix, the new tests reproduced the exact 501-item skip (7 failing assertions); after it, the damaged stage refuses. 65 offline tests at the repair; 67 tests plus six probes at final code 23d8dbead. |
| Independent result | Final code 23d8dbead was independently accepted 2026-10-20 (AGENTS/WALTER/research/2026-10-20_bookmark-live-acceptance/RESULT.md; packet PROME/inbox/processed/2026-10-20_from-WALTER_bookmark-independent-accepted-live-check.md). |
| No live scan or WQ458 renewal under L755 | L755 itself authorized none. Tonight's live use was on Will's own word in-session 22:05 ET ("yea go ahead. approved"), after he re-authorized X at 22:04 ET. |

**Live evidence tonight (new, outside L755):** a fresh head scan at 02:06Z staged 169 (schema2, stage_id b5c9378b…). The tool refused a 35h-old stage and refused to mark it without a matching review. A 169-ID review was created from the template, filled and validated by load_review. --mark then recorded exactly 169 IDs. Older coverage is still INCOMPLETE (500-row cap); the continuation is retained.

No WQ458 renewal inferred. Consumption of this packet by PROME is UNKNOWN until filed.
