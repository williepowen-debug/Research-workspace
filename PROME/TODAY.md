# TODAY.md — Sunday May 17, 2026

**Objective:** cleanly absorb Claude Code agent updates, keep Monday decision rails ready, and avoid mistaking quiet public credit/vol for all-clear.

**Current regime:** BDC/private-credit stress is confirmed at the vehicle/income/mark level, but public-credit contagion is still unconfirmed. HY OAS and VIX remain benign; pressure is concentrated in energy, Japan/FX, BDC equities, and regional-bank tape.

---

## 🔴 Priorities

- [x] **Git sync after Claude Code agent push** — pulled cleanly; local `master` now matches `origin/master` at `270b6d1d`.
- [x] **Refresh Prome/OpenClaw state files** — update stale May 14/16 handoff and status language.
- [ ] **Regional-bank decision prep** — use REGINALD May 17 closeout: WAL Investor Day Bucket E B3 fire, WAL 10-Q integration pending, MI3/FFIEC PDD status pending, SSB expiry outcome needs Will confirmation.
- [ ] **BDC/private-credit decision prep** — FSK Strong Bear allows fresh downside discussion; require live bid/ask and Will approval.
- [ ] **May 18 watch** — Iran-war anchor re-verify + TIC March release / Japan UST-flow read.

---

## Latest Dashboard Snapshot

From dashboard run May 17 10:38 ET:
- HY OAS **276bps 🟢**; VIX **18.43 🟢** — no broad cascade confirmation.
- CCC OAS **922bps 🟡**.
- Brent **$109.26 🔴**, gas **$4.50 🔴**.
- USD/JPY **158.73 🔴**.
- KRE **$66.97 🟡**, WAL **$74.42 🟡 / below bear line**.
- APO **$135.38**, above the `$130` watch line.
- ARES **$123.41 🟡**, OZK **$46.73 🟡**, BIZD **$12.61 🔴**.
- Claims: initial **211k**, continuing **1.782M**, shadow-adjusted estimate **266k** — directionally softer, not labor-break confirmation.

---

## Current Decision Posture

### Regional Banks
- REGINALD is elevated. WAL Investor Day finding is bearish-but-not-terminal: Bucket E B3 fired; REG-25 raised to 65%+; no V2.2 promotion without Q&A / 10-Q / MI3 confirmation.
- WAL 10-Q filed 5/11 but still not fully integrated; Schedule O / Table 16 cross-credit inventory test pending.
- MI3 / FFIEC PDD mid-May window passed; status check is now due.
- SSB $95P May 15 execution outcome is pending Will confirmation.

### BDC / Private Credit
- FSK Q1 remains Strong Bear / near Max Bear and validates vehicle-level stress.
- Fresh downside discussion is allowed, preferably liquid longer-dated BIZD/ARCC-type structures if pricing is sane.
- Do not rescue dead June APO/ARES premium by default.
- Public credit remains a constraint: HY OAS <300 and VIX <20 argue against broad cascade confirmation.

### Signal / Routing Architecture
- WALTER owns signal/news routing; Prome owns operational tasking and decision synthesis.
- News-sweep cron route was restored by Prome May 16; recurring signal-flow design should migrate back to WALTER under the new charter.

---

## Files to Trust Today

| File | Trust |
|---|---|
| `HEARTBEAT.md` | Current scenario/levels as of May 16 evening; levels rechecked May 17 and unchanged |
| `PROME/SCRATCH.md` | Fresh May 17 |
| `PROME/STATUS.md` | Fresh May 17 |
| `PROME/HANDOFF.md` | Fresh May 17 after git sync |
| `AGENTS/REGINALD/STATUS.md` | Fresh May 17 closeout; primary for WAL/SSB/Call Report pending work |
| `AGENTS/WALTER/STATUS.md` | Fresh May 17 closeout; primary for signal-routing architecture and callbacks |
| `PROME/POSITIONS.md` | Last known portfolio snapshot from May 8 screenshots; brokerage is execution truth |

---

## Skip / Deprioritize

- Do not spawn REGINALD/CARL/SAM/RED/BRENT.
- Do not treat `PROME/TOSCANINI/QUEUE.md` as live until rebuilt.
- Do not present trade proposals without live prices/option chains and Will approval rails.
