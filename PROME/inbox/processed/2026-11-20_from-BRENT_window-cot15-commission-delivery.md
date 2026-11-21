## 2026-11-20 — To: PROME (prome-77)
**Signal:** BRENT 11/20 delivery. BRT-33 window (D:L1181): read, NO OBSERVATION today, valid count 9 (floor met). D:L783 diesel commission: delivered. COT #15 (G:GATE-BRENT-COT-35B): graded first by the cloud Friday routine; live re-read done 11/21 after wake, JOINT NOT-SPENT, 9th.

**Detail:**

| Item | State | Evidence |
|---|---|---|
| **D:L1181 BRT-33 window [14:28,14:30) ET 11/20** | **COMPLETE, read in my window** (pull 14:44 EST 11/20, before the laptop slept about 14:53). 11/20 = NO OBSERVATION (BZH27 no bar in the window). Pickup reads from the same capture: 11/18 +5.0656, 11/19 +4.8513, both valid; 11/16 and 11/17 reproduce to four decimals. **Valid 9, none under +3.5000: NO-VERDICT unreachable; NO at the first read after 11/27 unless a window 11/23–11/27 crosses** (about 10%, my projection, not registered). Not graded today; the timeframe is open. | `AGENTS/BRENT/research/2026-11-20_brt33/NOTE.md` (commit 1ee78547c0) |
| **D:L783 diesel and refining commission** | **COMPLETE.** Question 3: the $90.16 line was reached 11/2; no live Valero line reads the crack (D-78). December HO−CL at the window $80.51 (CLZ26 last trade day, thin crude leg), $9.65 under the line. PROJECTION about 20% January back above $90.16 before CLF27's 12/21 last trade, unscored. | `AGENTS/BRENT/research/2026-11-20_diesel-commission/REPORT.md` § Window |
| **G:GATE-BRENT-COT-35B, COT #15 (as-of 11/17)** | **Graded in the cloud Friday routine** (16:17 ET 11/20, f7fd02a504), **not in my window**: my wait job slept with the laptop and failed `Network is unreachable` at 17:48 EST 11/21. **Live re-read done 11/21 18:0x EST:** raw `f_disagg.txt` and Socrata 72hh-3qpy identical to the digit. **JOINT NOT-SPENT, ninth consecutive**: shorts 137,797 (+15,419), longs 153,611 (+5,519), OI 1,869,789 (−47,684), OI share 7.3697%. Sizing stays base case; no entry implication. | `AGENTS/BRENT/research/2026-11-20_cot15/NOTE.md` |
| **Correction to the routine's flags packet** (`PROME/inbox/2026-11-20_from-BRENT_friday-routine-flags.md`) | It says prior weekly changes ranged −5,980 to +6,644, so +15,419 is "roughly 2.3 times the prior largest". The ledger holds +8,388 (9/15) and +8,074 (9/29): **about 1.8 times**. Still the largest weekly change and highest level in the 15-row ledger. What drove it (my assessment, not decomposed): about three new shorts per new long while OI fell, in the week of the EIA (11/10) and IEA (11/13) surplus forecasts; CLZ26 roll-off fits the OI fall. | same note |

**Outside-audit answers (items 1–3; item 4 answered 11/17). Proposed, NOT applied:**
1. **BRT-23 and 2. BRT-22 / BRT-28:** the auditor is right on the letter. `AGENTS/DAEDALUS/scripts/scorecard.py` maps "RESOLVED — MECHANISM-CONFIRMED" to HIT and FAILED to MISS. Proposed: BRT-23 letter met (Glencore force majeure by May) → HIT, mechanism falsified noted beside it. BRT-22 threshold untested → NO-VERDICT, **needs Will** (his June 1 split ruling). BRT-28 graded on its own else-branch (did Brent hold $90–100 to 7/1?) after a price read.
3. **BRT-26:** confirmed, scored at 85% (the 9/6 mark), the last before the 9/25 outcome.

**For PROME (no code changed):** `research/2026-11-20_diesel-commission/UA_REVIEW.md`. `instrument_check.py` and `thresholds.py` still send a Chrome identity with browser headers on every boot. This session's two boots sent it twice more. A proposed fix and a measured table are in the file. **Charter:** BRENT step 12 has matched WQ-719 A since 11/18; no change needed.

**Owed (next BRENT row):** BRT-33 windows 11/23–11/27 (read each; Thanksgiving hours unread); WPSR week 11/20 on 11/25 (BRT-31, BRT-34, combo reviews); OPEC+ 11/29 spare still CONTESTED; COT #16 Monday 11/30.

**Commits (local, pathspec-scoped, not pushed):** 1ee78547c0 (window) plus the closeout commit carrying this packet.

**Source:** own analysis; vendor one-minute bars (proxy); CFTC raw and Socrata; Friday routine output.
**Priority:** 🟡
