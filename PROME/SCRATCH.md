# SCRATCH — Ephemeral Working Memory

**Updated:** 2026-03-31 16:45 UTC (Tue 12:45 PM ET)

---

## QUICKSTART
Scenario D **82%**. War Day 31. Brent **$108-112**. Gas **$4 BREACHED 🔴**. HY OAS **342**. CCC OAS **1013** (but **concentrated** — cable/media/healthcare/software, NOT broad systemic; see CHANGELOG). CCC/HY ratio **2.96** (downgraded as indicator). Thesis confidence **80%** (was 85%).

**TIMING THESIS BUILT.** `FORGE/timing/thesis/` — NARRATIVE, TIMELINE, PREDICTIONS (22 calls), CHANGELOG, LECTURE. Plus `FORGE/timing/STATUS.md`. CCC sector decomposition completed (3 sources). Thesis now rests on **transmission channels** not CCC as standalone.

**Key change today:** CCC/HY ratio downgraded from "most important finding" to "partially distorted signal." 2015-16 energy analog for CCC, not 2007 GFC. Five of six convergence pillars remain intact.

**Do NOT spawn SAM, REGINALD, or CARL** — they run independently on Claude Code. Inbox files only.

## Handoff
**Last context:** Major thesis-building session in `FORGE/timing/`. Built thesis subfolder, then ran CCC decomposition research that **downgraded** CCC/HY ratio as systemic indicator. Confidence 85%→80%.
**What happened today (Mar 31):**
- Built `FORGE/timing/STATUS.md` — monitoring dashboard for timing research
- Built `FORGE/timing/thesis/` subfolder: NARRATIVE.md, TIMELINE.md, PREDICTIONS.md (22 calls), CHANGELOG.md, LECTURE.md (TTS script)
- **CCC SECTOR DECOMPOSITION (critical finding):** Three independent analyses (Perplexity, Claude, Gemini) all show CCC at 1013bp is concentrated in cable/media (~24-30%), healthcare (~15%), software (~5-8%) — NOT broad systemic. Ex-software CCC OAS ~930-960bp. Ex-software+cable ~650-780bp. 2015-16 energy analog, not 2007 GFC. **Thesis adjusted accordingly.** Logged in CHANGELOG.md, updated NARRATIVE, PREDICTIONS, STATUS.
- FXY Tranche 1 approved and executed (+4 shares @ ~$57.68, now 8 shares total)
- SAM/ZHAO/OTTO daily check-ins ran (SAM: Mimura "decisive," USD/JPY 159.13, 65% May hike pricing)
- Calendar sync token expired (non-urgent, needs re-auth)
- **Do NOT spawn SAM, REGINALD, or CARL** — they run independently on Claude Code now. Communicate via inbox files.
- Issuance freeze subagent was spawned but timed out — check results or re-run

**Next session priorities:**
1. 🔴 **OWL $9.5P Apr 2 — TOMORROW.** Decision needed.
2. 🟠 **Issuance freeze analysis** — check subagent output or re-run. Key gap: at what OAS does HY issuance freeze? Affects timeline.
3. 🟠 **Relief Rally Playbook** — pre-written decision framework for positions during relief rallies. Operational, not research.
4. 🟠 **Kitchen Sink Scenario** — what does BTFP 2.0 look like for PC? Model the intervention risk for Dec positions.
5. 🟡 **Norinchukin × CLO × Yen feedback loop** — cross-contagion quantification (SAM×BROCK)
6. 🟡 **LECTURE.md** — may need update to reflect CCC downgrade (currently says "keep your eyes on the CCC/HY ratio" as closing line)
**Open questions:** Near→long rebalance still deferred. KRE Jun→Dec roll timing (LIQUID flagged: post Q-end = worse fills — Q-end was today).
**Rhythm note:** Will was walking + cleaning, wanted text scripts for Speechify. Engaged in deep thesis work. Good discipline on questioning blind spots.
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
