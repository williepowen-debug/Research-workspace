# SCRATCH — Ephemeral Working Memory

**Updated:** 2026-03-31 16:45 UTC (Tue 12:45 PM ET)

---

## QUICKSTART
Scenario D **82%**. War Day 32. Brent **$103** (eased from $108). Gas **$3.99** (at $4 breakpoint). HY OAS **346** 🔴 (widening). CCC OAS **1020** 🔴🔴 (concentrated — cable/media/healthcare/software, NOT broad systemic). CCC/HY ratio ~**2.95** (downgraded as indicator). Thesis confidence **80%**.

**TODAY = APR 1.** OWL $9.5P expires TOMORROW (Apr 2) — decision needed. Treasury + insurance regulators meeting today (PC Stage 3 signal). Tankan survey today (BOJ hike signal).

**Do NOT spawn SAM, REGINALD, or CARL** — they run independently on Claude Code. Inbox files only.
**Calendar sync broken** — Google OAuth token expired, needs re-auth (non-urgent).

## Handoff
**Last context:** Light session Apr 1 (early morning). Confirmed git repo in sync after Claude Code agents pushed. Morning dashboard briefing delivered. No trades executed, no research spawned.
**What happened Apr 1 (this session):**
- Confirmed git repo synced (no lost Prome files)
- Morning briefing: HY OAS 346 (widening), CCC 1020, Brent eased to $103, VIX dropped to 24.8
- Calendar sync broken (Google OAuth expired) — flagged, non-urgent
- Catalyst prep check ran: all 48h catalysts covered (Treasury mtg, Tankan, OWL)

**Next session priorities:**
1. 🔴 **OWL $9.5P Apr 2 — EXPIRES TOMORROW.** Decision needed today. OBDCII unfiled.
2. 🔴 **Treasury + insurance regulators meeting (today)** — watch for PC Stage 3 signals
3. 🔴 **Tankan survey (today)** — BOJ hike signal for SAM
4. 🟠 **KRE Jun→Dec rolls** — Q-end passed, roll timing still needed
5. 🟠 **Issuance freeze analysis** — subagent timed out last session, rerun
6. 🟠 **Relief Rally Playbook / Kitchen Sink Scenario** — operational frameworks still missing
**Open questions:** Near→long rebalance deferred. APO hold to Apr 7 (stop $113, currently $111.42).
**Rhythm note:** Will up early, transitioning to new session. Market opens 9:30.

## Architecture Notes
- **CARL + REGINALD + SAM** are Claude Code on Telegram. DO NOT SPAWN. Inbox signals only.
- Market data dashboard: `FORGE/tools/market-data/dashboard.py`. Cron 4x/day (10,12,14,16 ET weekdays). Hysteresis on VIX (1.5pt) and HY OAS (5bps).
- `fred_spread` source type now supported in dashboard (computes difference of two FRED series).
- CONVERGENCE_TIMELINE.md is the master timing document. All research feeds into it.
- 11 research files in `FORGE/timing/research/`. Do NOT re-read all at boot — use CONVERGENCE_TIMELINE.md as synthesis.

## WILL_QUEUE (current)

| ID | Pri | Item | Status |
|----|-----|------|--------|
| W-001 | 🟡 | ABS trust trigger proximity | Blocked — Bloomberg |
| W-003 | 🔴 | APO Apr — HOLD to Apr 7, stop $113 | APO at $108.42 |
| W-005 | ✅ | FXY Tranche 1 — BUY MON OPEN | APPROVED |
| W-006 | 🔴 | OWL Apr 2 — **2 DAYS** | Check OBDCII |
| W-007 | 🟠 | FABN tranches maturing before Jun 18 | SHADE |
| W-008 | 🟡 | Whalen WGA IRA Bank Book Q1 2026 | Proprietary |
| W-009 | 🟡 | KBRA Private Credit Premium access | Paywalled |
| W-010 | 🔴 | APD Tranche 1 — BUY MON OPEN | APPROVED |
