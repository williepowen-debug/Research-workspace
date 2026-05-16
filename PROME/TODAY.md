# TODAY.md — Thursday May 14, 2026

**Objective:** keep decision rails clean while tape remains mechanically calm. Do not confuse VIX/HY calm with all-clear; do not treat gamma extremes as standalone short confirmation.

**Current regime:** BDC/private-credit stress confirmed by FSK, but public-credit contagion still unconfirmed. HY OAS and VIX remain benign; stress is concentrated in BDC equities, regional-bank tape, energy, and USD/JPY.

---

## 🔴 Priorities

- [ ] **Refresh live dashboard before citing levels** — `python3 FORGE/tools/market-data/dashboard.py --compact`.
- [ ] **Regional-bank Call Report triage** — WAL, OZK, EGBN, CFG, VLY, ZION, FITB, SSB/HBAN as needed.
- [ ] **Bank decision prompt** — May cleanup, KRE/WAL June salvage/roll, OZK/KRE/WAL runway, ZION kill/retain.
- [ ] **BDC/private-credit decision prompt** — FSK Strong Bear allows fresh downside discussion; use live pricing and avoid rescuing dead June premium by default.
- [ ] **Gamma/vol-suppression follow-through** — HENRY/VIOLET/LIQUID/NEXUS signal routed; determine if VIX <20 is mechanical suppression.

---

## Active Action Cards

| Card | Purpose | Status |
|---|---|---|
| `PROME/action-cards/FSK_MAY11_ACTION_CARD.md` | FSK branch → private-credit/BDC action | Active; FSK classified Strong Bear / near Max Bear |
| `PROME/action-cards/REGIONAL_BANK_WEEKEND_TRIAGE_MAY9.md` | Bank expiry / Call Report triage rails | Active; apply to KRE/WAL/OZK/ZION/etc. |
| `PROME/action-cards/TEMPLATE.md` | Standard future card format | Ready |

---

## Latest Dashboard Snapshot

From May 14 08:26 ET dashboard:
- HY OAS **282bps 🟢**; VIX **17.85 🟢** — no cascade confirmation.
- CCC OAS **937bps 🟡**.
- Brent **$103.87 🔴**, gas **$4.50 🔴**.
- USD/JPY **157.89 🟡 / near red**.
- KRE **$67.14 🟡**, WAL **$74.97 🟡 / bear-line breach**.
- APO **$131.60**, above $130 watch.
- BIZD **$12.57 🔴**.
- Claims: initial **200k**, continuing **1.766M** — not labor-break confirmation.

---

## Current Decision Posture

### BDC / Private Credit
- FSK Q1 = **Strong Bear / near Max Bear**.
- Fresh downside discussion is allowed, but only with live bid/ask and Will approval.
- Prefer liquid longer-dated BIZD/ARCC-type structures if pricing is sane.
- Do not default to rescuing June APO/ARES premium.

### Regional Banks
- WAL/KRE are yellow; WAL touched/breached $75 bear line.
- No broad bank-premium add without Call Report/tape confirmation.
- ZION remains **under-researched, not exonerated**; Jul put posture remains kill/no-roll if usable bid unless MI3/RCON2746 changes picture.

### Gamma / Market Structure
- Momentum factors dominate; quality/value/dividend yield lag.
- Positive gamma + 0DTE may be suppressing VIX and smoothing the index.
- Treat as fragility overlay: bearish only if momentum leaders crack + VIX wakes up + KRE/WAL/HYG/BIZD weaken together.

---

## Files to Trust Today

| File | Trust |
|---|---|
| `HEARTBEAT.md` | Current scenario/levels as of May 14 08:26 ET |
| `PROME/HANDOFF.md` | Clear-ready handoff as of May 14 10:25 ET |
| `PROME/POSITIONS.md` | Last known portfolio snapshot from May 8 screenshots; brokerage is execution truth |
| `PROME/action-cards/FSK_MAY11_ACTION_CARD.md` | Current FSK workflow |
| `PROME/action-cards/REGIONAL_BANK_WEEKEND_TRIAGE_MAY9.md` | Current bank triage workflow |
| `FORGE/signals/2026-05-14_gamma_momentum_factor_squeeze.md` | Latest market-structure signal |

---

## Skip / Deprioritize

- Do not spawn REGINALD/CARL/SAM/RED/BRENT.
- Do not refresh stale Toscanini queues before live decision rails.
- Do not commit/stash/pull/reset dirty git state without explicit approval.
