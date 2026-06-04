# TODAY.md — Thursday June 4, 2026

**Objective:** Refresh Prome's boot surface after the Jun 3-4 GitHub updates. Keep this as state hygiene: update current dashboard, ingest the HENRY/SAM Prome signals, and identify next safe lanes. Do **not** turn this into position reconciliation unless Will explicitly asks.

**Current regime:** Divergence persists. Public credit and vol remain calm — HY OAS **275bps [FRED 6/3 close]**, VIX **15.40** — while stress remains visible in USD/JPY near **160**, BIZD/BDC marks, gas/energy, and duration. Treat this as **substance/tape divergence**, not broad cascade confirmation.

---

## 🔴 Today's Work — Prome Boot Refresh

| Priority | Work | Status |
|---|---|---|
| 🔴 | Pull GitHub source-of-truth | ✅ Done — fast-forward to `687e2968`; later Prome commit `55e5b634` pushed. |
| 🔴 | Ingest HENRY TLT supersession | ✅ Done — `PROME/ACTIVE_DECISIONS.md` updated. |
| 🔴 | Ingest SAM pathspec migration audit | ✅ Done — tracker created; Prome self-fix done. |
| 🔴 | Refresh stale Jun 2 boot surfaces | In progress — `SCRATCH`, `TODAY`, `STATUS`, `FLEET_SCAN`. |
| 🟠 | Refresh root `HEARTBEAT.md` | Next optional lane; still Jun 2 injected root state. |
| 🟠 | Position-state reconciliation | Deferred; separate pass only. |
| 🟡 | Per-agent pathspec migrations | Tracker live; owner edits pending for BRENT/HENRY/MARCO/OTTO/OZK/VIOLET/WALTER. |

---

## Live Market Levels — Jun 4 ~17:30 ET dashboard

| Series | Value | As-of | Zone | Read |
|---|---:|---|---|---|
| HY OAS | **275bps** | **[FRED 6/3 close]** | 🟢 | Public credit still calm; no broad cascade confirmation. |
| CCC OAS | **947bps** | **[FRED 6/3 close]** | 🟡 | Lower-quality stress persists but not transmitting through HY. |
| VIX | **15.40** | live | 🟢 | Vol refuses confirmation. |
| Brent | **$95.14** | live | 🟡 | Energy risk still elevated, not >$100 red. |
| Gas weekly | **4.30** | **[6/1]** | 🔴 | Consumer pressure remains red. |
| USD/JPY | **160.01** | live | 🔴 | At/above intervention-zone psychological line; SAM channel live. |
| 10Y Yield | **4.46%** | **[6/2]** | 🟡 | Duration pressure elevated. |
| TLT | **$85.50** | live | 🟡 | Relevant to Jun $85P catalyst salvage; no new action without Will/trigger. |
| KRE | **$69.98** | live | 🟢 | Bank tape still not confirming bear acceleration. |
| WAL | **$80.74** | live | 🟢 | Above prior bear lines; Q2-print issue remains later. |
| OZK | **$49.21** | live | 🟡 | Watch but not acute Prome task today. |
| APO | **$128.41** | live | 🟡 | PC thesis unresolved; no fresh action from boot refresh. |
| ARES | **$130.50** | live | 🟡 | BDC/PC pressure visible but not public-credit cascade. |
| BIZD | **$12.70** | live | 🔴 | BDC/private-credit mark stress persists. |
| Initial claims | **225k** | **[5/30]** | 🟡 | Shadow-adjusted est **280k**; labor channel deteriorating but not headline-break. |
| Continuing claims | **1.777M** | **[5/23]** | 🟢 | Not yet confirming labor cascade. |
| SOFR-IORB | **-0.04** | **[6/3]** | 🟢 | No acute reserve-pressure signal. |

Dashboard summary remains: elevated but not cascade.

---

## Agent / System State to Carry Forward

- **HENRY → PROME:** TLT 5/22 ticket superseded Jun 3. Jun $85P held as small catalyst bet into NFP/CPI/FOMC; Sep add deferred until CPI confirmation.
- **SAM → PROME:** Per-agent `CLAUDE.md` pathspec migration is load-bearing. Prome/SAM done; remaining owner edits tracked in `PROME/PATHSPEC_MIGRATION_STATUS.md`.
- **BROCK:** Jun 4 sweep added OTF/BCRED/OCIC Q1 reads; convergence reportedly 46→55 in commit summary. Needs separate read if PC/BDC decision becomes live.
- **LABOR:** Claims now **225k [5/30]**, shadow-adjusted **280k**; labor channel moved yellow on dashboard.
- **BRENT/SAM:** Energy remains yellow; USD/JPY is the sharper red live threshold at **160.01**.
- **RED/REGINALD/MARCO/OTTO:** Many Jun 3-4 updates landed. Do not absorb all domain detail in Prome boot; use domain owners when decisions require depth.

---

## Do / Do Not Today

**Do:**
- Keep boot surfaces current and explicit about stale-vs-superseded rails.
- Use pathspec commits only.
- Treat `HEARTBEAT.md` refresh as next separate root-state step.
- Route/domain-refresh via owning agents instead of Prome absorbing everything.

**Do not:**
- Use old May `BROKER_PENDING` or 6/18 trigger language as actionable.
- Treat TLT Sep add as live before CPI gate.
- Bulk-edit other agents' `CLAUDE.md` files unless Will overrides owner isolation.
- Upgrade to cascade language while HY/VIX remain green.

---

## Pending After Boot Refresh

1. Verify and commit this boot refresh.
2. Optional next: refresh root `HEARTBEAT.md` with Jun 4 dashboard and Jun 3-4 operational notes.
3. Optional next: coordinate pathspec migration owners.
4. Separate later: position-state reconciliation.
