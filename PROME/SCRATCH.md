# SCRATCH — Ephemeral Working Memory

**Updated:** 2026-03-27 22:10 UTC (Fri 6:10 PM ET)

---

## QUICKSTART
Scenario D **85%** (HAWK raised). War Day 27. Account **$55,689 (+111.5%)**. Brent **$108-112**. Gas **$4 BREACHED**. HY OAS ~319. NOPI **55-59 (exceeds 1973 embargo)**. Cash ~$12K (21.6%).

**Nasdaq in correction.** S&P longest losing streak since '22. PC Stage 3 confirmed (Barron's + Bloomberg same day). USD/JPY **160 BREACHED**. JGB 40Y **3.924%** (+5.83% single day).
**Book inverted:** 61% near / 39% long. T-19 recommends 22/78 rebalance. Will deferred.

## Session 9 Summary (Signal Triage + SAM + Cron)
- **8 signals triaged** from Will's screenshots → 9 inbox files across 8 agents
  - Qatar FM 90 cargoes (BRENT/HAWK/HANS)
  - JGB selloff + USD/JPY 160 (SAM/ZHAO)
  - Apollo co-founder + MFS Bloomberg — PC narrative mainstream (BROCK/SHADE)
  - Stagflation regime + FedWatch no cuts (HENRY/LIQUID)
- **SAM spawned** — FXY Entry Decision Card delivered. **Will approved tranche 1 for Monday open.**
- **FXY price corrected** — SAM had $24, actual is **$57.36**. Decision card in STATUS.md fixed:
  - Entry: ~$57.36 | Stop: ~$55.05 (USD/JPY 167) | Target: ~$60-62 (USD/JPY 148-152)
  - Tranche 1 Mon: +4 shares (~$229) | Full: 12 shares (~$688)
- **USD/JPY monitoring cron BUILT AND LIVE** — runs every 30min Tokyo hours (23:00-06:00 UTC Mon-Fri). Alerts on threshold breach, silent otherwise. State file prevents spam.
- **H.8 auto-update completed** (REGINALD cron) — C&I vs CRE divergence +6.1pp, ALLL reserve release 3rd month, NDFI first decline. Will briefed in detail.
- **HERMES PM delivered** — H.8 findings routed to NEXUS/HENRY/LIQUID/CARL inboxes
- **TODAY.md rewritten** for Mon Mar 31 — FXY buy is first line item at open
- **CARL + REGINALD + SAM** are Claude Code on Telegram. DO NOT SPAWN.

## IMMEDIATE NEXT SESSION
1. 🔴 **Build SAM KB.tsv** — Will explicitly requested this. Extract ~40-50 key facts from STATUS, research files, repatriation brief into structured KB. Use two-pass method (extraction → formatting). This is prep for SAM Claude Code promotion.
2. 🟠 Update STATUS.md agent dashboard (BROCK/BRENT/HAWK completions from Session 8 still not reflected)
3. 🟠 Reassess QUEUE.md Batch 5 — many tasks overtaken by events
4. 🟠 Check OBDCII — did it drop? OWL decision by Mon.
5. 🟡 BOND → AGENTS_DIRECTORY.md

## WILL_QUEUE (current)

| ID | Pri | Item | Status |
|----|-----|------|--------|
| W-001 | 🟡 | ABS trust trigger proximity | Blocked — Bloomberg |
| W-003 | 🔴 | APO Apr — HOLD to Apr 7, stop $113 | APO at $108.42 |
| W-005 | 🟠 | FXY Tranche 1 — **BUY MON OPEN** ~$57.36, +4 shares | **APPROVED** |
| W-006 | 🔴 | OWL Apr — ITM at $8.84 | **4 DAYS.** Check OBDCII. |
| W-007 | 🟠 | FABN tranches maturing before Jun 18 | SHADE |
| W-008 | 🟡 | Whalen WGA IRA Bank Book Q1 2026 | Proprietary |
| W-009 | 🟡 | KBRA Private Credit Premium access | Paywalled |

## Architecture Notes
- SAM USD/JPY cron: `AGENTS/SAM/tools/usdjpy_monitor.sh`, state at `.usdjpy_alert_state`
- **SAM promoted to Claude Code** (like CARL/REGINALD). DO NOT SPAWN. Inbox signals only.
- Group chat test (Prome + CARL + REGINALD) still pending
- **Market data dashboard COMPLETE** — `FORGE/tools/market-data/dashboard.py`. Cron every 5min. Morning briefing 6 AM ET. Web panel at :8080/api/stress. All thresholds in `config.py` (single source of truth for CLI + web dashboard).
- **System timezone set to ET** (was UTC). All timestamps now Eastern.
