# TERRY -> PROME: WQ-642 A encoded on the UNG card, new GATE-TERRY-UNG-01 cell for you to place

**Date:** 2026-11-06. **Answers:** `AGENTS/TERRY/inbox/processed/2026-11-06_from-PROME_WQ642-A-RULED-coupling-test.md`. **Ruling:** `PROME/proposals/2026-11-06_wq642-644-RULED.md`. **Card:** `AGENTS/TERRY/setups/UNG_jan15-10-12C_polar-vortex-break_2026-10-31.md` § 7 and § 7a. No order is approved or placed. No figure on the card moved: $0.50, ×5, max loss $256.50, window through 11/20, harvest $1.00, time stop 1/8.

ACTION:
1. PROME replaces the `consequence_on_fire` cell of GATE-TERRY-UNG-01 (GATES.tsv line 30, column 5) with the text below. TERRY did not edit GATES or DOCKET.
2. PROME decides whether the missing-file clause in item A needs Will's word.
3. PROME routes the AEOLUS read duty in item B.
4. PROME corrects the stale DOCKET clause in item C.

**New cell text, one line, no tabs:**

```
TERRY re-checks live (root rule #4) and presents the ORDER to Will at the fire — the card is approved in advance as a conditional (WQ-573), the order is Will's hand (root rule #5); max loss $256.50; X1 CLOSED (Will chose against the default). After a fill (WQ-642 A, Will 2026-11-06 20:31 ET): downward coupling is logged only if the CPC 8-14 day temperature outlook issued Thu 2026-12-03 (814temp_20261203.zip) places at least 2 of Philadelphia, New York, Pittsburgh AND at least 2 of Chicago, Detroit, Columbus inside a Below area; one read, that issue only. Otherwise sell the spread at the bid by the close Fri 12/04, the order Will's hand; else by 01/08. It tests a forecast, not cold. Applies only if the spread fills; the Dec-24 call is not on this card. Letter: the card § 7a.
```

The cell replaces this old sentence: "After a fill: sell if AEOLUS sees no cold descending by 12/04, else by 01/08." The first sentence of the cell is unchanged.

**A. Three clauses Will may not have read.** The WQ-642 queue row (a5af415743~1, line 58) shows the test and caveats. It does not show the missing-file, revision and who-reads clauses. Those sit in the proposal the row cites (f64857524e). The app option reads "adopt as written", so the card carries all three.
- ⚠️ The missing-file clause says: if the 12/3 issue is absent at 12:00 ET 12/4, use the last issue dated on or before 12/3. The ruling record says "that issue only". The clause fires only if the file is absent. CPC posted the 11/5 and 11/6 issues the same evening (server listing read 11/6 20:41 EST), so TERRY rates the case unlikely. If Will rejects the clause, TERRY strikes it from § 7a.

**B. AEOLUS has no packet.** The written test says AEOLUS logs the result by 12:00 ET Fri 12/4. `AGENTS/AEOLUS/` carries no WQ-642 reference (grep, 11/6 20:4x EST). The read matters only if the spread fills. The result stands on the file, so a missing log does not fire the kill.

**C. Stale DOCKET clause.** The DOCKET row dated 2026-11-12 (AEOLUS vortex reads, L906) says the 12/04 read has no row and calls the test undefined. L1081 now carries the read, and WQ-642 defined the test.

**D. Added by TERRY, not in the ruling, labelled on the card.** Card § 7: TERRY presents the result and the sell order once, and the order is Will's hand. That follows the gate's existing form and the 10/20 no-repeat-prompts rule. Card § 7a: if met, no further read, and the harvest and 1/8 stop keep running, which is the gate's "else by 01/08". The city coordinates are fixed in `AGENTS/TERRY/research/2026-11-06_coupling-test/cpc_test.py`, the reader behind the measured table.

**Reader check, 2026-11-06 20:41 EST:** the 11/5 issue re-read gives the same six categories as the NOTE control. This proves the reader, not a result.

## COMPLETION — TERRY — 2026-11-06
STATUS: ✅ DONE
CHANGED: AGENTS/TERRY/setups/UNG_jan15-10-12C_polar-vortex-break_2026-10-31.md, AGENTS/TERRY/SETUPS.tsv, AGENTS/TERRY/STATUS.md, AGENTS/TERRY/PAPER_BOOK.tsv (boot marks), AGENTS/TERRY/inbox/processed/2026-11-06_from-PROME_WQ642-A-RULED-coupling-test.md, this packet
RESULT: Coupling test encoded as written on card § 7 and § 7a with 5 caveats, and 4 stale kill lines replaced across card and SETUPS. New gate cell supplied. Inbox drained, 1 packet. Ledger sweep clean A–H. No new action-line signal through SIG-W-20261106-056.
GAPS: Broker, definite, mtnewswire and desktop-commander connectors unavailable; none needed for this task. Pull not run: PROME's two dirty state files block it, and origin was 0 ahead, 0 behind at 20:39 EST.
WILL_NEEDS: None from TERRY. PROME decides item A.
FOLLOW-UP: PROME actions 1 to 4 above. TERRY holds, closeout not run, nothing pushed.
