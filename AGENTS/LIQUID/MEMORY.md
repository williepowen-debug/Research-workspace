# LIQUID — Cross-Session Memory

## Session Notes

### CURRENT SESSION (2026-05-19)

**Context:** Live tape re-verification of Prome's 5/18 pass-through. Pulled dashboard via `FORGE/tools/market-data/dashboard.py` and APO 10-day history via yfinance.

**Delivered:**
1. STATUS.md live re-verification — added "May 19 Live Re-Verification" section with full dashboard table; restamped 5/19. Header status flipped to 🟠.
2. **APO co-trigger discovered as MISSED.** APO closed >$130 starting 5/8 ($133.20), sustained through 5/18 ($134.07, peak $135.52 on 5/14). HEARTBEAT line 80 reassessment trigger fired on 5/12 (Day 3) and has been live for ~6 sessions of LIQUID inattention. Coincides with HY OAS compression run (282 → 276 cycle-tight). Per KILL_MEMO co-trigger language, this is the Trigger C precondition (APO + HY OAS compression concurrent).
3. Updated thresholds table with APO co-trigger row + USD/JPY row; updated cross-domain signals (APO Day 7 → BROCK, 10Y acute → HENRY); trimmed stale Apr-16 Danger Windows/Watch into single forward-looking 5/19 table.
4. 10Y observation refined: not just chronic +30bps, but **acute +12bps on 5/18 alone** — duration channel actively repricing.

**Re-verification confirmed Prome pass-through accurate**, but the live pull surfaced two things the proxy didn't have:
- APO trigger status (proxy noted >$130 in 5/14 signal item #2 only as cited macro, didn't compute the day count)
- 10Y intraday delta (+12bps on 5/18) buried in the chronic +30bps frame

**Still open / blocked on Will:**
- **POSITIONS read still gating.** Now urgent — kill-memo Trigger C precondition has held for ~6 sessions. Need to answer whether HYG put gets cut now or waits for HY OAS confirmation.
- **Thesis framing question sharpened:** cushion isn't 16-20bps with no triggers, it's 16-20bps + APO co-trigger fired + HY OAS in compression. "Life support" reading has more weight.
- BDC Q1 cycle: FSK NAV -9.9% in; OBDC/ARCC/BXSL/MAIN pending.
- Outboxes NOT written this turn (per Will direction). If escalation warranted: BROCK on APO Day 7, HENRY on 10Y acute.

### NEXT SESSION

1. **Read POSITIONS** (`FORGE/POSITIONS`, `FORGE/STATUS.md`). Resolve the cushion-framing question. APO co-trigger has been live ~6+ sessions — this is overdue.
2. **Re-verify tape morning of next session** — APO 5/19 close (Day 8 watch), HY OAS print, 10Y direction.
3. Decide on cross-agent outboxes — BROCK (APO Day 7+), HENRY (10Y acute). Don't write these without first reading POSITIONS context.
4. Pull BDC Q1 baseline into `workbook/BDC_MARK_CONVERGENCE_MONITOR.md` (OBDC/ARCC/BXSL/MAIN).
5. This week's calendar: 20Y auction Wed (VERIFY), initial claims Thu, daily SOFR/HY OAS, APO sustain count.
6. If HY OAS approaches 270, execute KILL_MEMO pre-trigger drill.
7. Monitor gamma-suppression-hypothesis unwind.

### PRIOR SESSION (2026-05-18 PM) — Revival
- 32-day revival. Integrated Prome's revival-proxy packet.
- STATUS.md surgical update (4 edits + new "Thesis-Kill Proximity" + "May 18 Revival Read"). Active channel reframed PLUMBING → DURATION.
- KB-LIQ-051 (SOFR April resolved mechanical), KB-LIQ-052 (Duration regime break May 2026).
- `workbook/KILL_MEMO_HY_OAS_260.md` drafted — 5-tier trigger ladder.
- PLAYBOOK_SOFR_IORB_20260417.md archived to domain/sources/.
- Inbox swept: 21 → 0 (5 synthesized, 14 archived, 2 Prome packets retained as reference).
- Boot doc refresh — CLAUDE.md (broken "removed:" text, KEY THRESHOLDS, FILES), CALENDAR.md (rolled forward), STRATEGY.md, IDENTITY.md, USER.md, CREDIT_THRESHOLDS.md.

### PRIOR-PRIOR (Apr 16 PM)
- Computer crash interrupted; resumed to close out.
- Apr 16 STATUS refresh (SOFR>IORB Apr 15 first cycle breach, credit Path A holding, APO/BIZD reversal, HYG thesis weakened).
- Processed 6-signal inbox (IMF GFSR, TCW Red Lobster, GS whipsaw, SEC PDT, CPI/UMich, March PPI).
- Built PLAYBOOK_SOFR_IORB (now archived) and BDC_MARK_CONVERGENCE_MONITOR scaffold.

### OLDER CONTEXT (see git history + `archive/`)
- Apr 10: Live data refresh — Path A (squeeze resolution) winning. LIQ-01 at 290bps, 30bps below 320 trigger.
- Apr 8: Full data refresh + file structure upgrade (SAM parity). Stagflation trap double confirmed. Japan repatriation upgraded LATENT→ARMED.
- Apr 6: Processed 11-signal inbox batch (PC Stage 3 + plumbing fragility).

## Operating Notes

- **FORGE/tools/market-data/** (dashboard.py, fetch.py) works well for FRED + yfinance series. Use for live pulls.
- **Git protocol:** `reset HEAD → add AGENTS/LIQUID/ → diff --cached --stat → commit → push`. Other agents frequently have uncommitted work in HENRY/REGINALD directories — never stage those.
- **STATUS.md is the single source of truth** for active positions, proposals, thresholds. TRADE.md was retired — no second copy to keep in sync.
- **Inbox processing is its own task.** Don't auto-process on spawn; wait to be told.

## Durable Findings

- Stagflation trap is structural and persistent — double confirmed across two separate oil crashes.
- Q-end SOFR spikes (Mar 31, Apr 2-3) were seasonal, not structural.
- **Apr 15 SOFR-IORB +7bps breach resolved mechanical, not structural** (tax-day TGA build, normalized within 2-3 sessions; KB-LIQ-051). Pattern: 1-day SOFR-IORB sign flip on tax-day mechanics is NOT structural confirmation. Apply the same skepticism to future quarter-end / settlement-window single-print breaches.
- **Active transmission channel can migrate without thesis abandonment.** Bear thesis stayed intact through 32-day gap by migrating from PLUMBING (SOFR-IORB) into DURATION (10Y +30bps, TLT confirms, Brent reflation). When one channel resolves, scan the others before declaring the thesis dead (KB-LIQ-052).
- **Gamma/momentum suppression hypothesis** (per Will/Prome 5/14 signal): positive gamma may suppress VIX/HY OAS even as substance prints (FSK NAV -9.9%, 2nd bank failure, Brent $109) accumulate. The HY OAS 276-282 floor that held May 6 → May 17 may be tape, not substance. Watch for the moment gamma unwinds — HY OAS could gap.
- **Trigger watch can go dormant during agent staleness.** APO crossed >$130 on 5/8 and the HEARTBEAT-grade co-trigger fired on 5/12 (Day 3). LIQUID was stale Apr 16 → May 18 (32 days). The trigger was live for ~6 sessions before live-tape re-verify caught it on 5/19. Pattern: on revival, **don't trust the proxy's narrative summary alone — pull live values for every named threshold in HEARTBEAT line 80 and verify day-counts.** A proxy synthesizing 5 inbox items can cite "APO >$130" as macro context without computing the trigger ladder. The agent's own first-session work after revival should include a full trigger sweep, not just STATUS surgical edits.
- DIFC geopolitical flows de-escalating while domestic structural flows (Japan, TGA) upgrading.
- **Public-equity PC sentiment (APO/BIZD) can decouple from underlying mark divergence** — TCW Red Lobster 98% / par is the canonical example. FSK Q1 NAV -9.9% (5/18) confirms mark catch-down direction. Don't over-weight equity price action for Stage 3 timing.
