# HEARTBEAT.md

## Current State
**Updated:** 2026-05-09 11:20 ET

**Regime:** Private-credit thesis intact but timing slowed. OBDC Q1 landed **MIXED / earnings-quality bear**: NAV -2.7% QoQ to $14.41, BRK-27 did **not** fire, National Dentex held at ~45.5¢, non-accruals improved, but adjusted NII fell to $0.31, base dividend reset to $0.31, PIK income elevated at 11.7%, and repayments/sales far exceeded new commitments. Translation: **grind, not cascade.**

**Stress dashboard:** HY OAS **279bps 🟢**; CCC OAS **915bps 🟡**; Brent **$101.52 🔴**; gas **$4.45 🔴**; USD/JPY **156.64 🟡**; SOFR-IORB **-0.05 🟢**; VIX **17.23 🟢**; KRE **$69.80 🟢**; APO **$130.35 🟢/$130 watch**; BIZD **$12.78 🔴**.

**Scenario read:** D remains dominant, but the active transmission mode is now **slow destabilization / delayed credit recognition**, not immediate Stage 3 forced marks. Public tape is risk-on/benign in credit and vol; physical energy and private-credit vehicle economics remain the pressure points.

**Key updates (May 8-9):**
- OBDC read complete: **MIXED**, not BEAR/MAX BEAR. APO/private-credit thesis preserved; no aggressive add signal.
- APO is back over the $130 watch line intraday (**$130.35**); sustained 3-session reclaim remains the position-specific kill/reassess trigger.
- HY OAS at **279bps** is the biggest falsification risk; 260bps sustained remains the private-credit overlay thesis-kill zone.
- News sweep flagged fresh BROCK/LIQUID alerts: Blue Owl Q1 miss/dividend-cut framing, Gulf bank deposit-flight risk, and bank-failure headlines.
- FSK pre-build is complete: `AGENTS/BROCK/domain/sources/FSK_PREBUILD_MAY11.md`.
- System map created: `PROME/SYSTEM.md`.
- Decision-support layer created: `PROME/DECISION_FLOW.md`, `PROME/action-cards/TEMPLATE.md`, `PROME/action-cards/FSK_MAY11_ACTION_CARD.md`, `PROME/action-cards/REGIONAL_BANK_WEEKEND_TRIAGE_MAY9.md`, and `PROME/TRADE_DECISIONS.md`.
- `PROME/TODAY.md` and `PROME/STATUS.md` refreshed for Saturday May 9 weekend build mode.

## Thresholds

| Indicator | Green | Yellow | Red | Current |
|-----------|-------|--------|-----|---------|
| HY OAS level | <300 | 300-320 | >320 | **279 🟢** |
| CCC OAS | <900 | 900-1000 | >1000 | **915 🟡** |
| Brent | <$85 | $85-100 | >$100 | **$101.01 🔴** |
| Gas AAA/wkly | <$3.50 | $3.50-4.00 | >$4.00 | **$4.45 🔴** |
| USD/JPY | <150 | 150-158 | >158 | **156.59 🟡** |
| SOFR-IORB | <+0.05 | 0.05-0.25 | >0.25 | **-0.05 🟢** |
| VIX | <20 | 20-30 | >30 | **17.36 🟢** |
| KRE | >$69 | $65-69 | <$65 | **$70.00 🟢** |
| APO | <$130 | $130 watch | >$130 x3 sessions | **$130.35 🟡 watch** |
| BIZD | >$13.00 | $12.50-13.00 | <$12.50 | **$12.82 🔴** |

## Catalyst Calendar (next 7 days)

| When | Event | Status |
|------|-------|--------|
| **Fri 5/8** | HEARTBEAT refresh | ✅ Complete |
| **Fri 5/8** | FSK baseline/pre-build | ✅ Complete — `FSK_PREBUILD_MAY11.md` |
| **Mon 5/11** | FSK Q1 release/read | 🔴 BROCK — next private-credit test |
| **May 1-10 window** | Q1 bank Call Reports | 🔴 REGINALD — MI3 / warehouse / NDFI check; apply `PROME/action-cards/REGIONAL_BANK_WEEKEND_TRIAGE_MAY9.md` |
| **TBD** | GCRED / OTF / BCRED / CTAC 10-Qs | 🔴 Real Stage 3 forced-mark tests |
| **Daily** | HY OAS vs 260 thesis-kill zone | 🔴 LIQUID/BROCK |
| **Daily** | APO $130 sustained reclaim | 🔴 Active watch — back above $130 intraday May 8 |

## Position Decisions Pending

| Pri | Decision | Framework |
|-----|----------|-----------|
| 🔴 | **APO puts — hold/roll/cut** | OBDC says hold/roll bias; no add. Reassess if APO >$130 for 3 sessions or HY OAS <260 sustained. |
| 🔴 | **FSK read** | Baseline + action card complete; classify Q1, apply `PROME/action-cards/FSK_MAY11_ACTION_CARD.md`, then log any decision. |
| 🟠 | **ARES $95P Jun** | Hold through ARES/BDC wave only if FSK/GCRED/OTF show mark pressure; otherwise June theta risk rises. |
| 🟠 | **BIZD / BDC sector** | BIZD weak despite benign OAS; watch income/NAV grind vs forced-mark break. |
| 🔴 | **KRE / WAL / OZK bank shorts** | Regional-bank triage card complete: `PROME/action-cards/REGIONAL_BANK_WEEKEND_TRIAGE_MAY9.md`. Next: Call Report checks + Monday prompt. |

## Active Spawns
None active as of 2026-05-09 11:20 ET.

## Operating Notes
- Architecture map: `PROME/SYSTEM.md`. Decision flow: `PROME/DECISION_FLOW.md`. Current action cards: `PROME/action-cards/`.
- `PROME/TODAY.md`, `PROME/STATUS.md`, and `PROME/SCRATCH.md` are refreshed for May 9 weekend build mode. `PROME/HANDOFF.md` is clear-ready as of May 9 21:25 ET. `PROME/TOSCANINI/QUEUE.md` remains stale and should not be treated as current ground truth until refreshed. `PROME/POSITIONS.md` was refreshed from Will screenshots on May 8 14:17 ET.
- ZION correction: ZION is **under-researched, not exonerated**. Scaffold created at `AGENTS/REGINALD/ZION/INDEX.md`; REGINALD inbox request written at `AGENTS/REGINALD/inbox/PROME-20260509-zion-scaffold-fill-request.md`. Current ZION Jul put trade posture remains kill/no-roll if usable bid unless Call Report MI3/RCON2746 surprises.
- Market levels above come from `FORGE/tools/market-data/dashboard.py --compact` run May 8 12:26 ET.
- Current OBDC interpretation comes from `PROME/HANDOFF.md` + local OBDC filings/pre-build read.
- CARL/REGINALD/SAM/RED/BRENT are persistent/managed agents; do **not** spawn sub-agents for those five.

## Skip
Late night (11pm-8am ET): urgent only. Weekend: light monitoring.
