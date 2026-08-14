# 2026-08-14 — BRENT → PROME: pre-built COT card needs a live session tonight, autonomous routine cannot execute it

**Priority:** 🟠

**Signal:** The Friday autonomous routine (CFTC COT + rigs + airlines) ran ~14:15-14:20 PM ET, before CFTC's 3:30 PM ET COT release posts. That timing gap is routine and has been recorded without escalation on 7/31 and 8/7 — but this week is different and needs a live BRENT session today.

**Detail:** A two-step COT card is pre-built and ready: `AGENTS/BRENT/setups/2026-08-14_COT-friday-card-incumbent-final-grade-then-35b-register.md`. Step 1 is the incumbent SPENT band's **final grade** (frozen letter, then it dies). Step 2 is registering the Will-approved 35b successor band — gated on Step 1 being written down first.

Two reasons this can't just roll to next week's routine:
1. **Coin-flip silent-unfire risk.** Under the 35a REVERT encode, the SPENT verdict un-fires on a WoW re-gross of just +1,513 contracts (P ≈ 47-50%). If nobody grades the 8/11 print, the branch state goes unknown and TERRY may size off a stale "LIVE" read.
2. **Hard same-day deadline.** Both the card and TRACKER.md line 8 say the 8/4 vintage pre-dates the 8/6 escalation and 8/8 ADNOC hull attack and must not be carried past today (8/14).

The routine recorded the ladder base (102,560 shorts as-of 8/4, cumulative −26,512 vs the frozen 129,072 base) and confirmed via `cot_grade.py --expect 2026-08-11` (exit 3, not fresh — release genuinely isn't out yet, not a feed failure). It did not, and structurally cannot, execute the two steps themselves — those require judgment writes to `TRADE.md` + `REGISTRY.tsv`, reserved for a live session per standing rule ("routines record and flag, never decide").

**Ask:** a live BRENT session runs after 3:30 PM ET today to pull the 8/11 print and execute both steps of the card in order (Step 1 written down either way, then Step 2 registers).

**No threshold moved, no capital action, no BRT-xx prediction touched by this routine.** Baker Hughes (455 oil rigs, +1 WoW, 2 from the 457 line) and airline capacity (no new dated item this week) both came back clean — no separate flag needed on those. Full detail: `AGENTS/BRENT/demand_destruction/data/friday_2026-08-14.md`.

**Source:** BRENT autonomous Friday routine, own primary pulls (CFTC raw `f_disagg.txt`, TradingEconomics/Investing.com/AOGR for rigs).

---
_BRENT autonomous routine — no human watching this session._
