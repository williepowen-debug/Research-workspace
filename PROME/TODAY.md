# TODAY.md — Tuesday June 2, 2026

**Objective:** Get Prome caught up and safe to boot from. Do not optimize trade decisions in this pass; fix state staleness, distinguish live evidence from historical rails, and prevent stale May 26/27 surfaces from misleading future sessions.

**Current regime:** Divergence persists. Public credit and vol remain calm — HY OAS **272bps [FRED 6/1 close]**, VIX **16.18** — while stress remains visible in Japan/FX, energy, BDC/private-credit marks, and duration. Treat this as **substance/tape divergence**, not broad cascade confirmation.

---

## 🔴 Today's Work — Prome State Rehab

| Priority | Work | Status |
|---|---|---|
| 🔴 | Sync local repo to GitHub source-of-truth | ✅ Done — `master` matches `origin/master` at `e17a4c90` |
| 🔴 | Discard stale local generated edits that blocked pull | ✅ Done with Will approval |
| 🔴 | Refresh stale Prome boot surfaces | In progress — SCRATCH / TODAY / STATUS / FLEET_SCAN / ACTIVE_DECISIONS |
| 🟠 | Identify agent state changes since Prome went stale | ✅ Bounded fleet scan complete |
| 🟠 | Reconcile trade rails / fills / active decisions | Deferred by Will: not the focus right now |
| 🟡 | Decide whether to commit/push Prome refresh | Pending after diff review |

---

## Live Market Levels — Jun 2 ~09:45 ET dashboard

| Series | Value | As-of | Zone | Read |
|---|---:|---|---|---|
| HY OAS | **272bps** | **[FRED 6/1 close]** | 🟢 | Public credit still calm; no broad cascade confirmation |
| CCC OAS | **946bps** | **[FRED 6/1 close]** | 🟡 | Lower-quality stress persists but not transmitting through HY |
| VIX | **16.18** | live | 🟢 | Vol refuses confirmation |
| Brent | **~$95.05** | live | 🟡 | Re-accelerated from MOU optimism; below prior red >$100 zone |
| Gas weekly | **4.47** | **[5/25]** | 🔴 | Consumer pressure still red |
| USD/JPY | **159.79** | live | 🔴 | Near 160 intervention zone; SAM channel live |
| 10Y Yield | **4.45%** | **[5/29]** | 🟡 | Duration pressure still elevated |
| TLT | **~$85.75** | live | 🟡 | Rail state must be reconciled before any use |
| KRE | **~$69.20** | live | 🟢 | Bank tape not confirming bear acceleration |
| WAL | **~$79.55** | live | 🟢 | Above prior bear lines; Q2-print issue remains later, not today |
| APO | **~$128.71** | live | 🟡 | Back below $130 watch but PC thesis not resolved |
| BIZD | **~$12.74** | live | 🔴 | BDC/private-credit mark stress persists |
| Initial claims | **215k** | **[5/23]** | 🟢 | Shadow-adjusted est **270k**; labor not yet headline-breaking |
| Continuing claims | **1.786M** | **[5/16]** | 🟢 | Still not confirming labor cascade |

Dashboard summary: **3🔴 / 9🟡 / 8🟢 — elevated, not cascade.**

---

## Agent-State Changes to Carry Forward

- **SAM:** Fresh Jun 1. BOJ Jun 16 is the dominant single-path catalyst; market priced hike ~88%, SAM marks 70%. USD/JPY near 160; intervention risk reactivated. Sep $60 calls explicitly not warranted under v1.5.
- **BRENT:** Fresh Jun 1. Iran talks suspension + Kuwait missile volley re-armed Phase 1; Brent around $95. Trump “deal close” rhetoric downgraded unless real substance follows.
- **VIOLET:** Fresh Jun 1. R11 analog is dead / gradual fade won. R12 technically terminated, but spot/SKEW watch near re-establishment. Timing reset toward later windows.
- **MARCO:** Fresh Jun 1. Acute crisis softened, but structural ag-labor and Canadian-travel channels remain live.
- **CARL:** Fresh enough May 31. Consumer/stagflation hardened on GDP/PCE, but not today's state-rehab bottleneck.
- **WALTER:** Last refreshed May 27; likely stale relative to Jun 1 Iran/BRENT shift. Routing owner should get anchor refresh after Prome files are clean.
- **REGINALD / BROCK / HENRY / LIQUID / BOND:** Domain heads are stale by 1-2 weeks. Do not chase completionism today; revive when a concrete signal/decision requires it.

---

## Do / Do Not Today

**Do:**
- Make Prome boot surfaces current and explicit about stale rails.
- Keep GitHub as source-of-truth; show diff before any commit/push.
- Use live dashboard before citing levels.
- Route WALTER/news refresh after state rehab if time remains.

**Do not:**
- Treat May 26/27 `BROKER_PENDING` or trigger language as actionable without reconciliation.
- Make trade recommendations in this rehab pass.
- Spawn persistent agents casually.
- Use broad git staging.

---

## Pending After State Rehab

1. Review diff for the refreshed Prome files.
2. Ask Will whether to commit/push the Prome refresh.
3. Then choose next catch-up target: WALTER Iran anchor, Prome inbox triage, or a formal fleet-scan commit.
