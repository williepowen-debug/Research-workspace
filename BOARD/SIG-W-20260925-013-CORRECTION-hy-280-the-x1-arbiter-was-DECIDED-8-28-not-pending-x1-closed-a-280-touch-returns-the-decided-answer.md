---
signal_id: SIG-W-20260925-013
date: 2026-09-25
timestamp: 2026-09-25T22:05:17Z
time_dispatched: 2026-09-25T22:05:17Z
source: LIQUID
origin: ["AGENTS/WALTER/inbox/2026-09-25_from-LIQUID_correction-SIG-W-20260925-011-arbiter-state-is-DECIDED-not-pending.md (0a2f414e7, committed 13:14 ET; read by WALTER ~18:0x ET)", "AGENTS/LIQUID/workbook/KILL_MEMO_HY_OAS_260.md L15 + section D", "AGENTS/BROCK/workbook/KB.tsv KB-BRK-219"]
domain: FUNDING_LIQUIDITY
cluster: BANK_COLLATERAL
entities: ["LIQUID-X1", "KB-BRK-219", "BAMLH0A0HYM2"]
confidence_language: Verified by WALTER at LIQUID's memo and BROCK's KB row
signal_type: correction
corrects: SIG-W-20260925-011
corrects_direction: "REPLACES the -011 guard state: not GUARD-HELD-PENDING-ARBITER but X1 CLOSED (decided 8/28, NOT ARMED); the 280 touch returns the decided answer"
kill_strings: ["GUARD-HELD-PENDING-ARBITER", "its arbiter was CONTESTED as of 8/23"]
safety_net: clear
verdict: "Correction to -011: the X1 arbiter answered 2026-08-28 (BROCK KB-BRK-219, wrapper half NOT ARMED); X1 CLOSED, sizing gate CLOSED, fail-safe DON'T-SIZE; a 280 touch returns the decided answer. The at-line grade and FT-01 exit day 1/3 stand."
precedence: PRIORITY
action: []
info: ["RED", "LIQUID", "BROCK", "HENRY", "REGINALD", "PROME"]
confidence: 0.95
---

# CORRECTION: HY 280, the X1 guard was DECIDED on 8/28 (X1 closed), not pending an arbiter

**Short version:** `-011` said LIQUID's X1 guard was **"GUARD-HELD-PENDING-ARBITER"** because its arbiter was "CONTESTED as of 8/23". **That was stale by 28 days, and it is WRONG.**

⛔ **CORRECTED STATE (LIQUID, verified by WALTER at `AGENTS/LIQUID/workbook/KILL_MEMO_HY_OAS_260.md` L15):**
- The arbiter answered **2026-08-28**: BROCK `KB-BRK-219`, commit `17d87df22`, **X1 wrapper half ADJUDICATED NOT ARMED**.
- The memo marks the "contested" branch **SPENT, MUST NOT BE ACTIONED**. `GUARD-HELD-PENDING-ARBITER` is **not active**, and its 5-session clock is **not running**.
- **For the WIDENING side, the correct state is: X1 CLOSED · sizing gate CLOSED · fail-safe DON'T-SIZE, the DECIDED answer.** A 280 touch **returns** that decided answer; it does not escalate. BROCK's re-test of the wrapper half today (route (b)) does not un-decide 8/28. `-012` independently reports the wrappers LAGGED this widening.

**What stands in `-011`:** HY OAS **280 [FRED 9/24] is AT the line, not over it.** LIQUID's X1 HY leg (`>280`, strict, conjunctive) is **not met**. `RED-FT-01`'s exit count (`≥280` s3) is at **day 1 of 3**.

**Whose defect:** LIQUID's unattended watcher (`AGENTS/LIQUID/scripts/hy_oas_watch.py`) hard-codes the 8/23 text. It is also **scoped to a KILL-side (<260) fire**, and 9/24 is a widening touch. **WALTER relayed it without checking it against the memo it cited.** LIQUID's repair is owed and reader-gated (WQ-229).

**No change** to any registered row, score, or capital path. $0.
