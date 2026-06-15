# PROME STATUS.md
**Updated:** 2026-06-15 00:05 ET (OpenClaw Prome — context-weight cleanup closeout)

## Core State

**Operational priority:** run from the lighter Jun 14/15 Prome boot path. Boot/handoff/closeout surfaces have been merged, pruned, hardened, and synced; current work is follow-up cleanup plus decision-support lanes, not unfinished boot rehab.

**Current repo reality:** context-weight cleanup has been committed/pushed. Next boot should verify clean/synced before pull. Continue **pathspec-only** staging/commits; push only when Will explicitly approves.

**Regime source:** use `HEARTBEAT.md` for the current market/regime dashboard and near gates. Do not duplicate full price tables here.

**Standing constraint:** **do not edit `AGENTS/*`** unless Will explicitly approves. Agent files are read-only inputs for Prome unless that constraint changes.

---

## Live Surfaces / Ownership

| Surface | Role | Current note |
|---|---|---|
| `HEARTBEAT.md` | Regime, dashboard, thresholds, near gates | Current Jun14 surface-de-risking / tail-stickiness frame. |
| `PROME/TODAY.md` | Operator card / immediate lane | Current Jun14/15 near-term work card. |
| `PROME/ACTIVE_DECISIONS.md` | Safety index for trade/expiry rails | Verification-required until broker/Will reconciliation. |
| `PROME/SCRATCH.md` | Working notes / latest session entry | Current Jun14 closeout/reboot entry point. |
| `PROME/FLEET_SCAN.md` | Conditional fleet map | Read on demand; not mandatory boot context. |
| `PROME/HANDOFF.md` | Live continuity surface | Single live handoff; archive holds older Q2 narrative. |
| `PROME/BOOT.md` / `PROME/CLOSEOUT.md` | Start/end procedures | Slimmed; closeout now manual owner-doc write-back; lean tool-output protocol active. |
| `MEMORY.md` | Durable kernels | Pruned Jun14; original archived in `memory/archive/`. |

---

## Agent / Domain Map for Prome

**Correction:** prior STATUS overstated staleness. Filesystem check on Jun14 showed most core agent `STATUS.md` files refreshed Jun14; BRENT/SAM were later Jun14 refreshes. Treat this table as a routing/freshness index, not domain truth; read the agent status before making decisions.

| Domain | File freshness | Current Prome read |
|---|---|---|
| **LIQUID / Funding-duration-credit** | ✅ Jun13 | TEN closed winner; HYG Jun $75P written off / let expire; HY OAS still tight; duration oscillation, not regime. FOMC/TIC are next macro gates. |
| **VIOLET / Vol** | ✅ Jun14 | Complacency tape with bid tail: VIX crushed, SKEW held, vol entry still blocked by credit Bin-B / HY non-confirmation. |
| **BRENT / Energy** | ✅ Jun14 later | Current owner of physical/price divergence. Brent sub-$90 despite severe physical/chokepoint stress; Monday double-trigger watch live. |
| **HAWK / Geopolitics** | ✅ Jun14 | Gulf/Iran risk updated through Jun13 state; formal Hormuz closure fired but Brent fell, reinforcing decoupling/track-based read. |
| **SAM / Japan** | ✅ Jun14 later | BOJ Jun16 / FXY near-expiry lane live; v1.5.1 annotated with Brent sub-$90, Ueda absence, CFTC peak context. Read current file before acting. |
| **CARL / Consumer** | ✅ Jun14 | Consumer-credit/housing stress intact; LEN/SAVE channels remain structural, but hard labor did not confirm cliff. |
| **LABOR** | ✅ Jun14 | NFP/revisions strengthened hard data; claims drift not cliff. Use shadow-adjustment framework before treating claims as clean truth. |
| **RED / Adversarial** | ✅ Jun14 | Bear case moderated by tape; managed decline / stagflation remain co-modal. Use for challenge framing, not current tape marks. |
| **BROCK / Private credit** | ✅ Jun14 | Private-credit/BDC/gate substance hot; broad cascade still needs HY/VIX/bank transmission confirmation. |
| **REGINALD / Banks** | ✅ Jun14 | Broad bank fade retired; WAL/OZK are idiosyncratic mechanics with Q2-print / loss-recognition gates. |
| **BOND / Auctions-duration** | ✅ Jun14 | Auction/duration context refreshed; integrate with LIQUID for current Treasury/funding read. |
| **HENRY / Market structure** | ✅ Jun14 file refresh, decision freshness still verify | No longer assume “dark” from old map, but confirm whether post-CPI/FOMC GEX/dealer mechanics are actually updated before leaning on it. |
| **NEXUS / Synthesis** | ✅ Jun14 file refresh, decision freshness still verify | No longer assume stale solely from old map; read before using cross-agent synthesis. T-08 remains awareness unless refreshed into trade rail. |
| **WALTER / Routing-news** | ✅ Jun14 file refresh, anchor freshness verify | News/routing registry refreshed, but Iran anchor may still lag HAWK/BRENT; use HAWK/BRENT for current Iran-energy truth unless WALTER anchor is updated. |
| **OTTO / Auto** | ✅ Jun14 | Auto/fraud vectors refreshed enough for routing; not a primary boot-surface driver unless Will pivots to auto/consumer. |
| **MARCO / Migration-labor-supply** | ✅ Jun14 | Labor-supply/ag-data blind-spot owner; read when labor/immigration supply channel matters. |
| **ZHAO / China-capital flows** | 🟡 older root status | Use for structural China/UST/Gulf-flow framing only; verify current data if decision-relevant. |
| **SHADE / PE-insurance** | 🟡 older root status | Important mechanism owner for insurer funding/captive stress; refresh before decision use. |

---

## Current Work Queue

| Lane | Priority | Status / owner note |
|---|---:|---|
| OpenClaw stable update | 🟠 available | Installed `2026.5.6`; npm latest observed `2026.6.6`; beta `2026.6.8-beta.1`. Recommendation: stable update when Will wants maintenance. |
| TODAY/HEARTBEAT dedupe | 🟠 optional | Next context-weight target if continuing surface cleanup. Keep HEARTBEAT as regime/levels owner; TODAY as operator card. |
| Position-state reconciliation | 🟠 pending | Needed before Jun18/19 expiry cleanup; broker/Will truth required. Do not infer positions from old rails. |
| HENRY/NEXUS/WALTER content-freshness check | 🟠 conditional | Files refreshed Jun14; verify actual content freshness before spawning/asking. Needed only if decision-relevant pre-FOMC. |
| Separate-clones migration | 🟠 deferred | Post-Jun16/FOMC calm-window decision packet; do not do halfway. |
| Execution-rails design | 🔵 design debt | HYG Jun→Dec failure remains canonical: thesis needs pre-registered ladders and triggers. |

---

## Rules of Engagement

- **No agent edits** unless Will explicitly changes the constraint.
- **No trade execution without Will approval.**
- **No trade recommendations unless explicitly requested.**
- **No external/public messages without approval.**
- **Old trade rails are verification-required** until broker/Will reconciliation.
- **WALTER routes signals/news; Prome maintains state, tasking, rails, and Will-facing synthesis.**
- **Pathspec commits only;** never `git add .`, `git add -A`, broad reset, force-push, or stash/reset unknown work.
- **Push is Will-coordinated** — commit locally only if approved, push only on Will's explicit call.
- Read current files before editing; verify after edits.

---

## Next Best Action

Next best lane depends on Will's priority:
1. OpenClaw stable update/maintenance (`2026.6.6`) if system upkeep is the goal.
2. Position-state reconciliation if trade/expiry hygiene is the goal.
3. TODAY/HEARTBEAT dedupe if continuing context-weight cleanup.
