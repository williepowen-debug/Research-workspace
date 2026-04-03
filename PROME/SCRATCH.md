# SCRATCH — Ephemeral Working Memory

**Updated:** 2026-04-02 17:50 UTC (Wed 1:50 PM ET)

---

## QUICKSTART
Scenario D **82%**. Brent **$108.16** (+6.9%), WTI **$111.40** (+11.3% — big spike). HY OAS **~321bps** (at 320 threshold). VIX **25.40**. 10Y **4.31%** (down from 4.42%). SPY **$654.12**. Thesis confidence **80%**.

**TODAY = APR 2.** Next major catalyst: OZK earnings Apr 16 (14 days). Bank earnings wave Apr 20-29.

**Do NOT spawn SAM, REGINALD, or CARL** — they run independently on Claude Code. Inbox files only.
**Calendar sync broken** — Google OAuth token expired, needs re-auth (non-urgent).

**REGINALD session (Apr 2 PM):** Boot process overhauled — 6 improvements to spawn protocol. STATUS.md trimmed (178→156 lines), research moved to bank folders. market.py updated with full watchlist + Brent. Live prices: WAL $72.09 (up from $68, still <$78), KRE $65.83, OZK $46.25. 2 inbox signals processed (CARL SYF canary, CRE trifecta).

## Handoff
**Last context:** REGINALD session Apr 2 PM — boot process improvements. No PROME session today yet.
**What happened Apr 2 (REGINALD only):**
- Boot process overhauled (6 improvements — price refresh, inbox scan, research out of STATUS, open question format, changelog rule)
- market.py updated with full bank watchlist + Brent, yfinance installed
- Live prices pulled — WAL bounced to $72.09, oil spiking (WTI +11.3%)
- 2 inbox signals processed (CARL SYF subprime canary, CRE fraud/insurance trifecta)
- All REGINALD files current

**Next session priorities:**
1. 🔴 **OWL $9.5P — EXPIRED Apr 2.** Check if decision was made / exercised.
2. 🟠 **KRE Jun→Dec rolls** — Q-end passed, roll timing still needed
3. 🟠 **Issuance freeze analysis** — subagent timed out, rerun needed
4. 🟠 **Relief Rally Playbook / Kitchen Sink Scenario** — operational frameworks still missing
5. 🟠 **Oil spike** — WTI $111.40 (+11.3%), Brent $108.16 (+6.9%). Stagflation channel amplifying. BRENT/HAWK may need spawn.
**Open questions:** Near→long rebalance deferred. APO hold to Apr 7 (stop $113, last $108.24). First Brands auction result still unknown.
**Rhythm note:** REGINALD boot improvements done. Next PROME session should run full dashboard.

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
