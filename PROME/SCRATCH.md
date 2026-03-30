# SCRATCH — Ephemeral Working Memory

**Updated:** 2026-03-30 22:00 UTC (Mon 6:00 PM ET)

---

## QUICKSTART
Scenario D **85%**. War Day 29. Account **~$55,689 (+111.5%)**. Brent **$107-108**. Gas **$3.96 → $4 BREACHED**. HY OAS **342**. CCC OAS **1013**. CCC/HY ratio **2.96** (unprecedented). Cash ~$12K (21.6%).

**TIMING FRAMEWORK COMPLETE.** 11 research files in `FORGE/timing/research/`. CONVERGENCE_TIMELINE.md rewritten (338 lines). 2026 ≈ late Q3/early Q4 2007. Insurance stress Q2-Q3'26. Bank stress late '26. Peak selling Q1-Q2'27.

**New dashboard indicators:** CP-Tbill (0.15 🟢), SOFR-IORB (-0.02 🟢), BIZD (BDC ETF, Tier 2).

## Handoff
**Last context:** Deep research session — synthesized 8 external LLM responses (3 Gorton framework, 4 Z.1 Flow of Funds, 1 LIBOR-OIS replacement) into comprehensive timing framework. All saved in `FORGE/timing/research/`.
**Next tide:**
1. 🔴 **FXY + APD buy at open** (both approved)
2. 🔴 **OWL Apr 2 — 2 DAYS.** Check OBDCII.
3. 🔴 **APO stop $113** — currently $108.42
4. 🔴 **Quarter-end SOFR watch** — Perli says ampleness at Q1 2019 levels + zero RRP
5. 🟠 **SAM KB.tsv** — Will requested, still not done
6. 🟠 **STATUS.md refresh** — BROCK/LIQUID stale given new research
7. 🟠 **Issuance freeze agent** — spawned earlier, never checked results
8. 🟠 **QUEUE.md Batch 5/9 reassessment** — some items overtaken by events
9. 🟡 **Research gaps:** PE-insurer→FABN transmission, Egan-Jones cascade, Norinchukin↔CLO loop, OFR Brief 26-02
**Open questions:** Near→long rebalance still deferred (61/39 inverted, RED says 22/78). KRE Jun→Dec roll pricing needed.
**Positions:** No changes today. FXY + APD approved for Mon open.
**Rhythm note:** Will in deep research mode tonight. Responsive to prompts. Wants concise summaries not raw docs.
**Today's work:**
- Saved 8 research responses (Gorton ×3, Flow of Funds ×4, LIBOR-OIS ×1)
- Added CP-Tbill, SOFR-IORB, BIZD to dashboard + `fred_spread` handler
- Rewrote CONVERGENCE_TIMELINE.md (338 lines, subagent)
- Identified 7 new research gaps from cross-referencing all findings
- Dispatched CARL + SAM daily check-ins

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
