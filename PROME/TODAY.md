# TODAY.md — Wednesday June 17, 2026

**Objective:** Close this window with WALTER Routing v2 shipped and FOMC in the rearview. Next fresh window should choose: post-FOMC synthesis or WALTER Phase 2 follow-through. **No `AGENTS/*` edits unless Will explicitly scopes them. No trade/expiry action without broker/Will truth.**

**Current regime:** HEARTBEAT is still pre-FOMC. Do not rely on the first QQQ impulse alone for regime. The post-FOMC snapshot shows **HY OAS still 271bps [FRED 6/16]** above the <260 kill line, **CCC 944bps [6/16]**, **VIX 18.36**, **USD/JPY 160.71**, and **BIZD $12.34**. Surface tape is not broad-cascade confirmation, but vol/carry/private-credit stress remain sticky. Confirm HY via FRED T+1 on 6/18 before grading the R3/blended-credit branch.

---

## Repo / Prome State

| Item | State | Read |
|---|---|---|
| Git | ✅ synced before closeout edits | WALTER pushed; Prome pulled and reviewed. Prome closeout edits local until committed. |
| WALTER Routing v2 | ✅ Phase 1 shipped | BOARD-first archive + recipient-local `inbox/WALTER/` delivery lane landed. New doctor checks pass. |
| WALTER consumption | 🟠 pending | Phase 2 recipient consume-step rollout remains; anti-rot telemetry will nag after 2d if backfills unconsumed. |
| FOMC | 🟠 happened; synthesis pending | Initial QQQ read: risk-off impulse, flush, absorption bounce/retest. Need cross-asset read + T+1 HY. |
| Position truth | 🟠 unreconciled | No expiry action without broker/Will truth. |

---

## Live Market Levels — Dashboard Pull 2026-06-17 ~16:20 ET

| Series | Value | As-of | Zone | Read |
|---|---:|---|---|---|
| HY OAS | **271bps** | **[FRED 6/16]** | 🟢 | Still above <260 R3/blended-credit kill. Need 6/18 FRED confirmation. |
| CCC OAS | **944bps** | **[FRED 6/16]** | 🟡 | Tail remains elevated, below red. |
| Brent | **$78.83** | live | 🟢 | De-escalation priced; physical reopening still not fully verified. |
| Gas weekly | **4.05** | **[6/15]** | 🔴 | Consumer pressure persists. |
| USD/JPY | **160.71** | live | 🔴 | Carry risk still loaded / worse than morning. |
| Initial claims | **229k** | **[6/6]** | 🟡 | Drift, not break; shadow est **284k**. |
| Continuing claims | **1.795M** | **[5/30]** | 🟢 | Still below red band. |
| SOFR | **3.63** | **[6/16]** | 🟡 | Monitor funding plumbing. |
| 10Y Yield | **4.43%** | **[6/16]** | 🟡 | Post-FOMC read needed. |
| CP-TBill Spread | **0.12** | **[6/16]** | 🟢 | Clean. |
| SOFR-IORB | **-0.02** | **[6/16]** | 🟢 | Clean. |
| KRE | **$71.11** | live | 🟢 | Banks not confirming broad cascade. |
| APO | **$138.91** | live | 🟢* | High alts tape still contradicts immediate PC-bear timing. |
| ARES | **$128.35** | live | 🟡 | Back in yellow band. |
| OZK | **$49.00** | live | 🟡 | Slipped into yellow; idiosyncratic/Q2-print gated. |
| WAL | **$78.43** | live | 🟢 | Barely above green threshold. |
| FXY | **$57.09** | live | 🟡 | TIC/expiry context remains. |
| TLT | **$86.33** | live | 🟡 | No action without broker/Will truth. |
| BIZD | **$12.34** | live | 🔴 | BDC/private-credit stress remains live. |
| VIX | **18.36** | live | 🟢/near 🟡 | Vol woke up but not red; watch post-FOMC persistence. |

---

## Near Gates — Jun 18–19

| Date / Window | Gate | Owner(s) | Prome read |
|---|---|---|---|
| **Thu 6/18** | Claims, May TIC, FRED HY update, expiry cluster | LABOR/SAM/LIQUID/Prome | Claims pre-mortem live; HY <260 confirmation/denial matters; expiry cleanup requires broker/Will truth. |
| **Fri 6/19** | Geneva Iran signing / HYG expiry | WALTER/HAWK/BRENT/LIQUID | Iran signing is binary for M-06; HYG Jun $75P remains written off / let expire. |
| **Late Jun/Jul** | BCRED/Q2 redemption, BDC/Q2, SAVE Jul 1 | BROCK/CARL/LABOR | Structural stress watch; not immediate broad-cascade confirmation. |

---

## Post-FOMC Operating Card

**Purpose:** grade the event; do not auto-trade.

| Branch | What to watch | Prome read |
|---|---|---|
| Hawkish-of-pricing | 2Y/front-end repricing higher, VIX persists >18/20, USDJPY/carry stress, TLT weak | Re-arms macro/carry/vol fragility: R1 + R6 + coiled-spring path. |
| Dovish/risk-on compression | HY/HYG compression, banks/alts bid, vol crushed, QQQ reclaims pre-FOMC range | Can kill surviving R3 blended-credit bear axis only if HY sustains <260. |
| Mixed/unresolved | HY holds >260, VIX wakes but credit/banks hold, QQQ whipsaw | Re-anchor to Jun18 claims/TIC and late-Jun/Jul BDC/PC marks. |

**HY discipline:** HY OAS **271 [FRED 6/16]** is still above <260. Use live proxies, but do not declare R3 kill on intraday action. Confirm with FRED T+1 and require sustained <260.

---

## Prome Work Queue

| Pri | Work | Action |
|---|---|---|
| 🔴 | **Post-FOMC synthesis** | Fresh dashboard/proxies; check 2Y/HYG/VIX/USDJPY/TLT; confirm HY OAS T+1. |
| 🟠 | **WALTER Phase 2 consumption rollout** | Coordinate recipient consume-step; OpenClaw agents first; avoid direct recipient edits unless scoped. |
| 🟠 | **Quick-WALTER acceptance test** | PROME-spawned test of route-only path, delivery_log, and Iran-anchor guard. |
| 🟠 | **IMMEDIATE/FLASH → Claude Code push rail** | Prome to operate clean-tree scoped commit + normal push only under urgent policy. |
| 🟠 | **Position-state reconciliation** | Separate lane only; no expiry action without broker/Will truth. |
| 🔵 | **Execution-rails design** | Later: prevent another HYG Jun→Dec missed-roll failure by pre-registering ladders/triggers. |

---

## Skip / Guardrails

- No trade execution.
- No `AGENTS/*` edits unless explicitly approved.
- No old May/Jun option rails without broker/Will reconciliation.
- WALTER delivery-lane exception is narrow; not a general inbox/outbox/HERMES revival.
- HEARTBEAT needs post-FOMC update only after synthesis, not from the first impulse alone.
