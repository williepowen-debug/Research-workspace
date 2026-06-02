# TODAY.md — Tuesday June 2, 2026

**Objective:** Keep Prome safe to boot from after the Jun 2 catch-up. Phase 1 is factual cleanup only: remove completed/pending-process residue, fold in WALTER/SENTRY updates, and leave HEARTBEAT for a separate careful refresh.

**Current regime:** Divergence persists. Public credit and vol remain calm — HY OAS **272bps [FRED 6/1 close]**, VIX **16.18** — while stress remains visible in Japan/FX, energy, BDC/private-credit marks, and duration. Treat this as **substance/tape divergence**, not broad cascade confirmation.

---

## 🔴 Today's Work — Prome State Rehab

| Priority | Work | Status |
|---|---|---|
| 🔴 | Sync local repo to GitHub source-of-truth | ✅ Done — `master` matches `origin/master` at `e8e11442` |
| 🔴 | Discard stale local generated edits that blocked pull | ✅ Done with Will approval |
| 🔴 | Refresh stale Prome boot surfaces | ✅ Done and pushed (`79a66053`) |
| 🔴 | Disable SENTRY scheduled feed pushes | ✅ Done and pushed (`e8e11442`); manual `workflow_dispatch` preserved |
| 🟠 | Identify agent state changes since Prome went stale | ✅ Bounded fleet scan complete |
| 🟠 | Integrate WALTER Jun 2 Iran-anchor refresh | ✅ Phase 1 cleanup target; WALTER commit `ddb94d13` landed during rebase |
| 🟠 | Reconcile trade rails / fills / active decisions | Deferred by Will: not the focus right now |
| 🟡 | Refresh HEARTBEAT | Pending Phase 3; do not trust old HEARTBEAT levels |

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
- **BRENT:** Fresh Jun 1, with WALTER Jun 2 correction. Iran/energy stress re-armed, but channel state is now **contested**: Tasnim/IRGC suspension vs MFA/Trump ongoing/rapid-pace denial. Treat Trump rhetoric as tape-not-info in both directions unless substance confirms.
- **VIOLET:** Fresh Jun 1. R11 analog is dead / gradual fade won. R12 technically terminated, but spot/SKEW watch near re-establishment. Timing reset toward later windows.
- **MARCO:** Fresh Jun 1. Acute crisis softened, but structural ag-labor and Canadian-travel channels remain live.
- **CARL:** Fresh enough May 31. Consumer/stagflation hardened on GDP/PCE, but not today's state-rehab bottleneck.
- **WALTER:** Fresh Jun 2. Iran anchor reverified; current frame is **narrative-fork + kinetic-acceleration**. Kuwait strike cadence is load-bearing; Bab al-Mandab remains rhetorical only; next anchor boundary 2026-06-09.
- **REGINALD / BROCK / HENRY / LIQUID / BOND:** Domain heads are stale by 1-2 weeks. Do not chase completionism today; revive when a concrete signal/decision requires it.

---

## Do / Do Not Today

**Do:**
- Make Prome boot surfaces current and explicit about stale rails.
- Keep GitHub as source-of-truth; show diff before any commit/push.
- Use live dashboard before citing levels.
- Keep WALTER/news routing as WALTER-owned; Prome should carry the Jun 2 anchor frame rather than re-routing it.

**Do not:**
- Treat May 26/27 `BROKER_PENDING` or trigger language as actionable without reconciliation.
- Make trade recommendations in this rehab pass.
- Spawn persistent agents casually.
- Use broad git staging.

---

## Pending After State Rehab

1. Finish Phase 1 factual cleanup diff for Prome boot files.
2. Phase 2: add fresh OpenClaw handoff block to `PROME/HANDOFF.md`.
3. Phase 3: refresh root `HEARTBEAT.md` with live dashboard + Jun 2 regime state.
4. Later/separate: Prome inbox triage and position-state reconciliation if Will asks.
