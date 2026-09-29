# BOND → PROME — 9/29: row 4 MET on HY 302 (composite 15/35) + L0 drain 3/3

**Spawn:** prome-82, DOCKET L525, 2026-09-29 10:24 ET. **Data:** FRED fredgraph CSV direct, read 10:24 ET. **All 9/28 cells had posted by then**, so no polling was needed (B, IG and BBB were absent at PROME's 10:22 read). Evidence rows: `AGENTS/BOND/workbook/KB.tsv` `KB-BND-359` (credit) and `KB-BND-360` (SAM supply).

## Task 1 — my own observations, graded on my own letters

| Observation (9/28 memo `e64d22669`) | Letter | 9/28 cell | Verdict |
|---|---|---|---|
| **Row 4** (matrix row 4 Upgrade Trigger) | "HY >300 with velocity" | HY **302** (+9); 3-session **+29bp** (9/23→9/28) = **98th pct** of 782 windows (FRED ICE span 2023-09-30→) | ✅ **MET → row 4 2→3, composite 14→15/35** (re-summed 4+3+2+3+1+1+1) |
| IG joining | IG 15-session ≥ +6 (LIQUID D1 companion) | IG 83; 15-session **+2** | ❌ NOT met |
| BBB joining | BBB 15-session ≥ +7 | BBB 102; 15-session **+3** | ❌ NOT met |
| B (LIQUID's D1, LIQUID grades) | B 15-session ≥ +28 ×3 with CCC widening | B 309; 15-session **+32**, CCC +18 | 1st qualifying obs of 3. **Not BOND's grade.** |

Other 9/28 cells: BB 183 (15-session +28) · CCC **1146 = new 3y-span max** (prior 1137 [2025-04-07]) · CCC−BB 963 · HY yield 8.03%. I re-checked the method before using it: my 15-session calc reproduces the 9/25 figures (CCC +74 / B +23 / BB +21 / BBB 0 / IG 0).

**Speed-vs-level, one line:** broad repricing is **still NOT shown** on the letter, because IG/BBB 15-session changes are only +2/+3 and their levels sit at the 43rd/36th percentile. The new fact is that IG/BBB 3-session speed (+6/+7, ≈97th pct) is the first movement beyond high yield. That is speed only, on a different window. The +6/+7 numbers equal the 15-session bars by coincidence and are **not a pass.**

⚠️ **Caveats that travel with row 4:**
- ⛔ This is a **BOND marker only, NOT a capital reopen.** X1 was CLOSED on 8/28 (`KB-BRK-219`). It reopens only through BROCK's 10/02 sitting (DOCKET L494), then TERRY and Will.
- The row moved on **one first-published ICE cell, 2bp over the line.** If ICE revises it to ≤300, row 4 gets re-graded.
- TRADE.md's separate analytical-reopen line is "HY >300 ×3 sessions". On that line 9/28 is session 1 of 3.

**Composition (LIQUID's caveat):**
- 9/25: BB +12 on a rates-flat day with CHTR −3.9%.
- 9/28: BB +7 on a rates-up day (10Y +7), with CHTR only −1.3% (112.91→111.40, yfinance) and IG/BBB also widening. That looks **more like breadth than one sector on 9/28**.
- Index OAS cannot split out sectors, so **sector vs breadth stays UNRESOLVED.**

RED-FT-01 is RED's call. D1 is LIQUID's.

## Task 2 — L0 drain, WHOLE inbox (3/3, every sender)

| Item | Disposition | Where |
|---|---|---|
| PROME `2026-09-28_…WQ-317-cross-market-attribution-read.md` | Consumed as task registration; **not started** (spawn scoped to observation + drain) | → `inbox/processed/`. The obligation is now a CATALYSTS 10/2 row |
| SAM `2026-09-29_…WQ-317-JGB-FX-rows…` | INTEGRATE | `KB-BND-360`. Japan cash JGB market was **closed 9/21–9/23**, so JGB cash cannot be the source of the 9/22–9/23 US leg (inference). SAM has no intraday JGB timestamps |
| WALTER `SIG-W-20260928-018` | `noted`. It duplicates `KB-BND-350`, which BOND pulled first | → `inbox/WALTER/processed/`. Row in **`AGENTS/BOND/board_log.tsv` (CREATED: BOND had no §5 ledger)**. Commit declares `consume:BOND` |

**WQ-317 inputs:** SAM's rows are in. **HANS's EU/UK rows have NOT been received.** HANS has made no commit since the 9/28 17:17 packet, which is still unconsumed in `AGENTS/HANS/inbox/`. The letter covers this: if HANS is still absent on 10/1, I write from HANS's committed surfaces and mark the gap.

**Also found:** the 10/1 WQ-291 FR2004 grade and the 10/2 WQ-317 page were owed deliverables with **no BOND docket row** (`grep WQ-291` on CATALYSTS returned 0). Both rows are now added.

**Not pre-empted:** L410 10/01 refresh, WQ-291 FR2004 read (Thu 10/1 ~16:15), X1 (L494). STAND DOWN; `$0`; no trade proposal; no threshold moved.

**Controls:**
- docket_check rc0, corrections rc0, boot_recompute rc0, kb_lint conformant, claim_check clean, read_cap rc0.
- **closeout_check rc=1.** One hit, `CATALYSTS.tsv:14`. It is a pre-existing provenance stamp ("seen by docket_check 2026-09-28"), not a pending item. I looked and left it.
- **Rotation residue:** CATALYSTS is at 73% of budget and STATUS at 74%. Both sit in the 70–75% band, so rule 5's <70% stop is owed. The CATALYSTS rotation is due at the 10/1 session, when the 9/30 row has fired.
- `git pull` SKIPPED: the tree carries CRUISE/PROME/RED uncommitted work.

## COMPLETION — BOND — 2026-09-29
STATUS: ✅ DONE
CHANGED: AGENTS/BOND/{STATUS.md, SCRATCH.md, RECEIPT.md, TRADE.md, board_log.tsv (new), workbook/KB.tsv (+359,+360), workbook/VX.tsv (VX-BND-02 2→3), docket/CATALYSTS.tsv (+10/1 WQ-291, +10/2 WQ-317), domain/sources/2026-09-29_STATUS_full-snapshot_pre-row4-rotation.md}; 3 inbox packets → processed/; this memo
RESULT: Row 4 MET on its letter: HY 302 [9/28] >300 with +29bp/3 sessions (98th pct), so row 4 goes 2→3 and the composite 14→15/35. This is a marker only, NOT a capital reopen (X1 closed; BROCK 10/02). IG/BBB 15-session +2/+3 miss +6/+7, so broad repricing is still not shown (speed only). B 15-session +32 = LIQUID's D1 obs 1 of 3. L0 drain 3/3.
GAPS: Row 4 rests on one first-published cell 2bp over the line; a revision re-grades it. Sector vs breadth UNRESOLVED from index OAS. HANS WQ-317 rows not received. closeout_check rc=1 on one pre-existing provenance-stamp hit (looked, left). CATALYSTS and STATUS still owe rotation to <70%.
WILL_NEEDS: None
FOLLOW-UP: 9/29–9/30 HY cells (sessions 2–3 of TRADE's ×3 line; LIQUID's D1). 10/1 WQ-291 FR2004 grade + L410 refresh. 10/2 WQ-317 page (HANS gap rule).
