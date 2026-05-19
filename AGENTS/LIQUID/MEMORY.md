# LIQUID — Cross-Session Memory

## Session Notes

### CURRENT SESSION (2026-05-18 PM)

**Context:** 32-day revival session. Prome's revival proxy prepared a packet + STATUS draft in inbox; LIQUID integrated and pushed.

**Delivered:**
1. STATUS.md surgical update — 4 edits + new "Thesis-Kill Proximity" + "May 18 Revival Read" sections. Header restamped to 5/18; active channel reframed PLUMBING → DURATION. Apr 16 narrative preserved verbatim.
2. KB-LIQ-051: SOFR April breach resolved mechanical (clean negative finding — plumbing-leak hypothesis falsified for April; tax-day TGA build, as suspected).
3. KB-LIQ-052: Duration regime break May 2026 (new active channel — 10Y +30bps, TLT confirms, Brent reflation feeding April-CPI loop).
4. `workbook/KILL_MEMO_HY_OAS_260.md` drafted — pre-written 5-tier trigger ladder (270 pre-trigger → 265 trigger A → 260 intraday B → 260 sustained C), verification steps, PROME-notification template.
5. PLAYBOOK_SOFR_IORB_20260417.md archived to `domain/sources/` (resolved-mechanical header).
6. Inbox swept: 21 → 0. Top 5 synthesized into KB/STATUS; 14 May-9 batch archived as cross-agent-primary; 2 Prome packets retained as reference. `inbox/processed/BATCH_INTEGRATION_2026-05-18.md` records disposition.
7. Boot doc refresh — CLAUDE.md (broken "removed:" text, KEY THRESHOLDS table, FILES table), CALENDAR.md (rolled to May 19–23 / 26–30 / June), STRATEGY.md, IDENTITY.md, USER.md, CREDIT_THRESHOLDS.md (header flag).

**Live numbers used this session were Prome pass-through, not LIQUID-direct.** Re-verify on next dashboard fetch:
- HY OAS 280 (5/18) / closest of cycle 276 on 5/17
- 10Y 4.59, TLT $83.56, Brent $109.30, BIZD $12.52
- SOFR 3.55, SOFR-IORB -10bps
- VIX 17.82, USD/JPY 158.83, KRE $67.92

**Still open / blocked on Will:**
- **POSITIONS context not read.** Proxy didn't reach `FORGE/POSITIONS` / `FORGE/STATUS.md`. Kill memo lists categories; actuals need confirmation.
- **Thesis framing question deferred:** is the 16-20bps cushion above 260 = "grinding but intact" (refine duration detection) or "life support" (centerpiece kill memo)?
- BDC Q1 earnings cycle live but largely unprocessed in `BDC_MARK_CONVERGENCE_MONITOR.md` (FSK NAV -9.9% in; OBDC, ARCC, BXSL, MAIN pending).
- HYG $75P Jun x10 — thesis weakened per Apr 16 still pending decision; if HY OAS triggers fire (see kill memo) this position cuts.

### NEXT SESSION

1. **Re-verify live tape vs Prome pass-through.** Dashboard or fetch.py — HY OAS, 10Y, TLT, Brent, SOFR, BIZD, KRE. Reconcile any drift.
2. **Read POSITIONS** (`FORGE/POSITIONS`, `FORGE/STATUS.md`) and answer the cushion-framing question — grinding-but-intact vs life-support.
3. Pull BDC Q1 earnings data into `workbook/BDC_MARK_CONVERGENCE_MONITOR.md` baseline (OBDC, ARCC, BXSL, MAIN — FSK already in at -9.9% NAV).
4. Process this week's calendar (20Y auction Wed/VERIFY, initial claims Thu, daily SOFR/HY OAS).
5. If HY OAS approaches 270, execute KILL_MEMO pre-trigger drill — re-read POSITIONS and pre-stage exit orders.
6. Monitor for gamma-suppression-hypothesis (5/14 signal) unwind — if VIX gaps OR HY OAS gaps wider on momentum unwind, the floor at 276-282 cracks.

### PRIOR SESSION (Apr 16 PM)
- Computer crash interrupted; resumed to close out.
- Committed Apr 16 STATUS refresh (SOFR>IORB Apr 15 first cycle breach, credit Path A holding, APO/BIZD reversal, HYG thesis weakened).
- Processed 6-signal inbox (IMF GFSR, TCW Red Lobster, GS whipsaw, SEC PDT, CPI/UMich, March PPI).
- Built PLAYBOOK_SOFR_IORB (now archived as resolved-mechanical) and BDC_MARK_CONVERGENCE_MONITOR scaffold.
- Archived 4 legacy files (TRADE.md, LAST_COMPLETION.md, INBOX.md, OUTBOX.md).

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
- DIFC geopolitical flows de-escalating while domestic structural flows (Japan, TGA) upgrading.
- **Public-equity PC sentiment (APO/BIZD) can decouple from underlying mark divergence** — TCW Red Lobster 98% / par is the canonical example. FSK Q1 NAV -9.9% (5/18) confirms mark catch-down direction. Don't over-weight equity price action for Stage 3 timing.
