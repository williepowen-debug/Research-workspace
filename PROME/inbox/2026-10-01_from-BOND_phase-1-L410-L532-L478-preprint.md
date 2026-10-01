# BOND → PROME · 2026-10-01 13:05 ET (phase 1 of 2) · spawn `prome-0c` · DOCKET L410 · L532 · L478 (pre-print) · L0 drain

**Bottom line:** the L0 drain is done (9 items, every sender). For L410, `grade_auction.py` was repaired (I′ suppressed for TIPS, no scope change, so no Will ask; degenerate-row guard built), the seven I′ bars were re-frozen, and the 10/6–10/8 bars are frozen pre-print. The L532 WQ-317 page is DELIVERED with verdict **UNDETERMINED**. BND-30 and BND-31 both resolved **TRUE**. The official **9/30** curve is read. **The 16:15 FR2004 outcome table is pre-stated below, and the AMBIGUOUS-BY-BUCKET branch does not exist under the letter Will approved on 9/26.** No trade, no threshold move, no score change. $0.

## 1. Pre-print letter for L478 (fixed before the number: phase 2 grades on exactly this)
**Re-read:** my 9/25 intent (`AGENTS/BOND/analysis/2026-09-25_Q3_FORUM-7-section7_BOND-rows.md`) said the long-end TOTAL governs and a 3–6Y/long-end divergence is "AMBIGUOUS BY BUCKET, Will's call". **Will's WQ-291 approval on 9/26 SUPERSEDED that intent.** He approved BOND's exact letter (`KB-BND-337`, encoded `ba028b7f0` / THESIS §kill / `KB-BND-342`), which rules the conflicting-bucket question: *"3–6Y alone governs a 5Y fire; long-end TOTAL + 6–7Y reported, never graded; unpublished / revised / cross-break = GAP (no fire)."* ⚠️ **DOCKET L478's text and this spawn's prompt still carry the pre-ruling AMBIGUOUS-BY-BUCKET branch. PROME: please annotate L478 so the consumer read at 16:15 does not look for a branch the letter no longer has.**

Grader: `AGENTS/BOND/analysis/2026-10-01_wq291_grade.py` (unchanged since the 9/28 dry-run; NY Fed `PDPOSGSC-G3L6`, SBN2022+SBN2024). PRE as-of 9/16 = **$47.986B** must reproduce within $1.5M. **MET iff POST as-of 9/23 ≥ $56.586B (Δ ≥ +$8.6B), inclusive: exactly $56,586M = MET.**

| Outcome | Test | What BOND does (no other branch exists) |
|---|---|---|
| **MET** | rc 0, POST ≥ $56.586B | The kill's dealer leg is MET for the 9/23 5Y `I'` fire (54.31 vs the 59.48 bar in force, −5.17pp, nowhere near a tie band). ⇒ **Sept-4 kill letter MET** ⇒ BOND writes a **RECOMMENDATION, "exit all duration shorts"** (TLT Oct-16 82P ×1 + TBT 10 sh), the same evening: a packet to TERRY (card) and one to PROME (WQ row for Will's [Approve]). **No action.** Riders travel verbatim: ① net inventory ≠ proof of warehousing · ② funding window UNGRADED · ③ operational rule, no predictive claim. Matrix, each on its own letter: row 2 3→4 ("composition failure with the FR2004 leg CONFIRMED") · row 1 4→5 ("the paired kill's mechanism leg confirming") ⇒ composite 15→17. Token `kill=MET-REC@2026-10-01` on STATUS/THESIS/TRADE; THESIS v1.2.11. |
| **NOT MET** | rc 0, POST < $56.586B | The dealer leg is NOT MET. The funding window is UNGRADED by ruling, never "not met". ⇒ **KILL NOT FIRED**; the 9/23 fire stays an unpaired `I'` marker. No position, matrix or token change. |
| **GAP, unpublished** | rc 3 | Re-run at ~16:30 / 17:00 / 18:00. If still unpublished at the 10/2 boot, report GAP. **Never a pass, never a fail.** |
| **GAP, revision / mismatch / break** | rc 2 (PRE ≠ $47.986B, a series break between PRE and POST, or a fetch failure) | GAP, no fire (the letter). BOND reports both vintages and the Δ on each. **Whether to grade on a revised PRE is Will's call, and it is the ONLY Will's-call branch** (a WQ row via PROME the same evening). |
| *Divergent buckets* | 3–6Y vs long-end TOTAL disagree | **Not a branch.** 3–6Y decides; the long-end TOTAL and 6–7Y are printed beside it as information. |

Reported beside any outcome, never graded: the long-end TOTAL and 6–7Y Δ (FORUM-7 D3a/D3b numbers go to HENRY, who leads §7). Matrix row 3 (dealer absorption) moves only on its own letter (two consecutive long-end TOTAL builds with weak composition; the 9/30 as-of on 10/8 is the second look).

## 2. L410: quarterly refresh and its two decisions
- **Decision (1), I′ for TIPS: SUPPRESSED in the tool.** The tool now matches the registered spec, so nothing widens or narrows. That keeps it inside BOND's authority, with **no Will ask**. Extending I′ to TIPS would widen the kill's first leg and is **not proposed**: no TIPS base rate exists. `KB-BND-376`.
- **Decision (2), degenerate-row guard: BUILT.** `degenerate_reason()` excludes a row if any of these hold: one leg ≥99.99%; the legs don't reconcile (corpus and TA_WS `competitiveAccepted`); a leg is NaN or negative. It names every exclusion and refuses to grade a degenerate print. **0 rows excluded live.** The founding row `912810TC2` is in no pool the grader reads.
- **Repair, four states** (acceptance written first: `AGENTS/BOND/analysis/2026-10-01_L410_grade_auction_repair_ACCEPTANCE.md`):
  - **IMPLEMENTED** ✅
  - **TESTED** ✅: selftest 38/38; the 9/23 5Y output is byte-identical; the reviewer's 9 counterexamples all pass after the fix.
  - **INDEPENDENTLY VERIFIED** ⚠️ **PARTIAL**: one Opus read found 2 ❌ in v1 (A3: TA_WS reconciliation never applied; A6: the refusal graded a stale original / blocked valid pre-print bars). Both were fixed afterwards and re-tested, but **nobody has read the fixed code**.
  - **STILL UNRESOLVED** 🟡: the 2dp tie band, below.
- **Re-freeze** (`KB-BND-377`; `monitors/AUCTION_HEALTH.md` 10/1 block; script `analysis/2026-10-01_quarterly_Iprime_refreeze.py`):
  - I′ bars: 2Y 54.82 · 3Y 58.90 · 5Y 59.42 · 7Y 57.43 · 10Y 65.05 · 20Y 57.96 (was 61.72; the 9/15 fire entered the window) · 30Y 63.89.
  - **Frozen pre-print for 10/6 3Y $58B · 10/7 10Y-R $39B · 10/8 30Y-R $22B.**
  - One rule: the frozen 2dp snapshot governs, the re-derivation is an audit, and the operator is STRICT on every leg.
  - RED's boundary fixture: NOT FIRED ×7.
  - **The 9/23 OLD fire is CONFIRMED** on a clean pool. The dealer MAX 15.61 is a 5Y new issue; it is no longer provisional.
  - ⚠️ **The fixture found a tool gap:** the tool compares against the unrounded bar, so it can disagree with the governing 2dp bar inside a band of ≤0.005pp. This is docketed for 10/6, before the 3Y grade.
- **NOT done:** the VX-BND-19 "disorderly" qualifier, re-dated to 10/8 (CATALYSTS).

## 3. L532: WQ-317 page DELIVERED, verdict UNDETERMINED
Page: `AGENTS/BOND/analysis/2026-10-01_WQ-317_cross-market-attribution-page.md`; KB row `KB-BND-375`.
- **Ruled out:** JGB cash as the source of 9/22–9/23 (Tokyo was closed for Silver Week).
- **No Asian lead into 9/23:** ACGB fell 4.8bp (RBA F2, BOND's own pull).
- **SHARED and a same-morning US lead both fit** 9/23, 9/24 and 9/28.
- **EXPORTING fits poorly:** JGBs followed the US on 1 of 5 sessions.
- **The evidence that would decide it is named and not held:** 9/23 intraday futures, the PMI release timestamps, OSE night JGB, ACGB after 9/23, CME settlements.

HANS's 10/1 correction (the Bund rallied; Italy and Spain widened) is used as **outside-the-window context only**. Every number on the page was spot-checked against the Treasury CSV, MOF and ACM primaries.

## 4. Curves, predictions and the inbox
- **Official 9/30** (`KB-BND-372`):
  - 30Y **5.64** (+5): highest DGS30 close since **2002-07-08**.
  - 10Y **5.29**: passes its 2007 high, highest since **2002-05-14**.
  - DFII10 2.93: highest since 2008-11-24.
  - Bear steepener (2s30s 76).
  - The US rose **alone**: Bund, AAA and JGB all fell.
- **Official 10/1:** not posted at 12:57 ET (the October file is empty). It goes in phase 2.
- **`BND-30` TRUE** (ACM 9/29 TP share 2.36). **`BND-31` TRUE** (JGB 30Y −2.8bp). Tally 16 TRUE · 13 FALSE · 1 VOID; OPEN 0. The 10/28 FOMC row is still owed by 10/21.
- **L0 drain, 9/9 items, every sender, all moved to `processed/`:**
  - HANS rows + CORRECTION → page + `KB-BND-379`.
  - WALTER R3 → **adopt 7 / decline 9 BY NAME, packet `PROME/inbox/2026-10-01_from-BOND_R3-watch-for-verdicts-adopt-decline.md` (committed `8d2b82879`; a one-line label fix to its VX row rides the phase-1 commit)**. PROME lands the clean set.
  - NEXUS read-cap flag: already rotated 9/29, no action. WQ-340 note: no dispute.
  - PROME WQ-332: hand-grading continues, per-event log.
  - WALTER lane -004/-006 → `KB-BND-378`, -009 → `KB-BND-379`, -018 → `KB-BND-380` (board_log rows 17:00:55Z).

## COMPLETION
STATUS: PARTIAL (phase 1 of 2 DONE; phase 2 = the FR2004 grade + the 10/1 curve on PROME's re-ping after ~16:15 ET)
CHANGED: grade_auction.py (TIPS I′ suppressed; degenerate guard) · AUCTION_HEALTH 10/1 re-freeze · WQ-317 page · KB-BND-372…381 · BND-30/31 TRUE · STATUS/NEXUS_BRIEF/CATALYSTS/SCRATCH · inbox 9→processed
RESULT: WQ-317 = UNDETERMINED · 10/6–10/8 bars frozen · 9/23 OLD fire confirmed clean · FR2004 outcome table pre-stated (3–6Y alone governs; no AMBIGUOUS branch)
GAPS: tool fix not independently re-read · 2dp tie band (docketed 10/6) · VX-19 qualifier (10/8) · 10/1 official curve not yet posted
WILL_NEEDS: none now. Only a rc-2 revised-PRE GAP at 16:15 would need his word; a MET is a rec via TERRY's card
FOLLOW-UP: PROME annotate DOCKET L478 (stale AMBIGUOUS branch) · land the R3 adopt set · re-ping BOND after ~16:15 ET
