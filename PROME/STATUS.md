# PROME STATUS.md
**Updated:** 2026-05-14 10:25 ET

## Core State

**Regime:** BDC/private-credit credit/mark stress is confirmed by FSK, but public-credit contagion is not confirmed. Surface tape remains mechanically calm: HY OAS <300 and VIX <20. Understructure stress persists in BDC equities, regional banks, energy, and USD/JPY.

**Working model:** fragile melt-up / vol-suppressed tape. Momentum + positive gamma + 0DTE may be suppressing VIX; treat as air-pocket risk overlay, not standalone short signal.

---

## Active Decision Layer

| Artifact | Status | Purpose |
|---|---|---|
| `HEARTBEAT.md` | ✅ Fresh May 14 08:26 | Scenario, levels, catalyst/position rails |
| `PROME/HANDOFF.md` | ✅ Clear-ready May 14 10:25 | Fresh-session handoff |
| `PROME/SCRATCH.md` | ✅ Fresh May 14 10:25 | Ephemeral next-action state |
| `PROME/TODAY.md` | ✅ Fresh May 14 10:25 | Today's priorities/levels |
| `PROME/action-cards/FSK_MAY11_ACTION_CARD.md` | ✅ Active | FSK Q1 branch-to-action rails |
| `PROME/action-cards/REGIONAL_BANK_WEEKEND_TRIAGE_MAY9.md` | ✅ Active | Bank expiry / Call Report triage rails |
| `FORGE/signals/2026-05-14_gamma_momentum_factor_squeeze.md` | ✅ New | Gamma/momentum/vol suppression signal |

---

## Pending Work

| Action | Pri | Status |
|---|---:|---|
| **Regional-bank Call Report triage** | 🔴 | Needs MI3/RCON2746, NDFI/warehouse/fund finance, ACL/NCO/nonaccrual migration, FHLB/brokered deposits/liquidity. Apply bank action card. |
| **Bank decision prompt** | 🔴 | Prome-owned synthesis: May cleanup, June salvage/roll, Sep-Dec runway, ZION kill/retain. |
| **BDC/private-credit decision prompt** | 🔴 | FSK Strong Bear permits fresh downside discussion. Needs live pricing and Will approval before any trade. |
| **Gamma/vol-suppression follow-up** | 🟠 | Routed to HENRY, VIOLET, LIQUID, NEXUS. Watch whether VIX <20 is mechanical and whether momentum unwind hits BIZD/KRE/HYG. |
| **GCRED / OTF / BCRED / CTAC 10-Q watch** | 🟠 | Real Stage 3 forced-mark tests after OBDC/FSK. |
| **ZION scaffold expansion** | 🟠 | REGINALD-owned. ZION is under-researched, not exonerated; Jul put remains kill/no-roll if usable bid unless Call Report evidence changes picture. |
| **Old Toscanini QUEUE/WILL_QUEUE cleanup** | 🟡 | Stale; lower priority than live decision rails. |

---

## Agent / Domain Notes

| Domain | Status | Note |
|---|---|---|
| BROCK / private credit | 🔴 | FSK validates stress. Need fresh-capital decision rails, not blind June rescue. |
| REGINALD / banks | 🔴 | Persistent/managed — do not spawn. Current book needs Call Report and expiry triage. |
| VIOLET / vol | 🟠 | New gamma signal: VIX may be mechanically suppressed. |
| HENRY / market structure | 🟠 | Momentum/gamma/0DTE signal routed; assess air-pocket risk. |
| LIQUID | 🟠 | HY OAS benign is main falsification pressure; watch <260 sustained and funding stress. |
| NEXUS | 🟠 | Spawn only if multiple domains converge; currently has signal for synthesis hook. |
| WALTER | 🟢 | Owns signal/news routing. Prome should not absorb routine routing. |
| PROME | 🔴 | Chief of staff: maintain rails/state, assign decision work, synthesize outputs into Will-ready prompts. |

---

## Rules of Engagement

- **No trade execution without Will approval.**
- **No fresh broad cascade short** while HY OAS <300 and VIX <20.
- **No broad bank-premium add** unless Call Reports/tape move to Bear / Strong Bear.
- **No rolling every losing June contract.** Prefer one or two higher-delta roll candidates if confirmed.
- **Do not panic-sell Sep/Dec runway into green tape.**
- **Do not spawn REGINALD, CARL, SAM, RED, or BRENT.**
- **Do not commit/stash/pull/reset dirty git state without Will approval.**

---

## Freshness Table

| File | Status |
|---|---|
| `HEARTBEAT.md` | ✅ May 14 08:26 |
| `PROME/TODAY.md` | ✅ May 14 10:25 |
| `PROME/STATUS.md` | ✅ May 14 10:25 |
| `PROME/SCRATCH.md` | ✅ May 14 10:25 |
| `PROME/HANDOFF.md` | ✅ May 14 10:25 |
| `PROME/POSITIONS.md` | May 8 screenshot snapshot; brokerage is execution truth |
| `PROME/TOSCANINI/QUEUE.md` | Stale Mar 26; do not use as live proposal list |
| `PROME/TOSCANINI/WILL_QUEUE.md` | Stale; historical only until refreshed |

---

## Next Best Action

Fresh session should read `PROME/HANDOFF.md`, refresh dashboard, then build bank + BDC decision prompts. If live domain-agent outputs are unavailable, Prome should do the minimum direct analysis needed to avoid leaving Will blind, while preserving agent ownership boundaries.
