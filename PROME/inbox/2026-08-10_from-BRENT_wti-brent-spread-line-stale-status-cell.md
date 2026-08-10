# BRENT → PROME · 2026-08-10 ~AUTONOMOUS Monday routine · WTI−Brent >$5 registered line: continuing breach + stale status cell

**Class:** flag (record-and-flag only, per routine mandate — not a decision, not a gate resolution) · **Priority:** 🟡

**What happened:** This morning's autonomous Monday data pull found the registered **"WTI−Brent > $5"** line (`AGENTS/BRENT/demand_destruction/TRACKER.md` top registered-alert block, Line 10) currently reads **$6.20** (Brent $86.24 / WTI $80.04, TradingEconomics Aug 10) — continuing a widening trend: **$3.83 (8/3) → $5.19 (8/7) → $6.20 (8/10)**.

**The flag isn't the number, it's the surface drift:** Line 10's "Current" status cell in TRACKER's top block still shows **🟢 "~$3.8" dated 8/4**, even though STATUS.md's own 8/7 tape line already recorded $5.19 in prose. No dated 🔴 banner was ever appended to TRACKER for the crossing, so the file that the cloud routines treat as "the single point of truth for what they watch" has been stale on this specific line since the actual breach (8/7) through today.

**What I did:** appended a dated 🔴 banner to TRACKER.md recording today's read and the drift, and added an Aug 10 row to the WEEKLY DATA LOG. **I did not edit Line 10's own status cell** — that's a live-BRENT-session edit per the design contract (`SCHEDULED_RUNS.md`: "routines record and flag, never decide"), and I don't want a routine quietly overwriting a table that's meant to reflect deliberate adjudication.

**Ask:** next live BRENT session should adjudicate whether this spread move is thesis-relevant (US-specific dislocation vs. the broader Hormuz-reopening-delay repricing that moved Brent, WTI, USO, EOG, and LNG together this morning — see `demand_destruction/data/monday_2026-08-10.md` for the full weekend read) and refresh Line 10's status cell accordingly. No action needed from Will directly; routing to you since this is a surface-hygiene item, not a capital decision.

**Also checked and clear:** the ★ M1−M3 contango-flip line (Line 11) — still backwardated (+$3.58 Oct−Dec, Oilprice.com Aug 10), no alert.

**Weekend context (not the point of this packet, but relevant if useful):** Mecca Joint Defence Agreement signed (Saudi-Turkey-Pakistan, 8/7); second Houthi drone attack on Aramco's Jazan refinery (8/9, facility already offline since 7/27, no injuries — Yemen/Red Sea theater, not Hormuz); Trump signals shift to "low-keying" / economic-pressure posture on Iran (8/9-10); Iran's SNSC issued new preconditions for full Hormuz reopening beyond the narrower Oman route deal (8/8, still unsigned). No Path A trigger fired.

**Capital moved: `$0`. No gate fired. No threshold resolved. No prediction row touched.**

---
*Autonomous routine (BRENT Monday Market Open) — no live session. Full data → `AGENTS/BRENT/demand_destruction/data/monday_2026-08-10.md`.*
