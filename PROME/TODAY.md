# TODAY.md — Tuesday June 16, 2026

**Objective:** Get Prome state right before more agent/theory work. Current priority is clean orchestration: operate from fresh GitHub state, current market dashboard, and accurate WALTER/NEXUS/LABOR status. **No `AGENTS/*` edits unless Will explicitly scopes them.**

**Current regime:** **Surface tape remains bull/de-risking while tail/private/physical stress stays sticky.** Broad cascade is still not confirmed: HY OAS is **266bps [FRED 6/15]**, only 6bp above the <260 blended-credit kill line; VIX is **16.41**; banks remain bid; Brent is down to **$79.49**. But CCC remains elevated at **937bps [FRED 6/15]**, BIZD is still red, USD/JPY is **160.48**, gas remains high, and Iran/Hormuz physical reopening is not resolved until the 6/19 Geneva/signing track. This is a fragile calm, not systemic repair.

---

## Repo / Prome State

| Item | State | Read |
|---|---|---|
| Git | ✅ clean/synced | `HEAD == origin/master` after Prome state-correction push. |
| Prome boot surfaces | ✅ corrected | TODAY/HEARTBEAT/STATUS/SCRATCH/HANDOFF/ACTIVE_DECISIONS refreshed; FLEET_SCAN + Jun15 week card demoted/superseded. |
| WALTER | 🟠 improved, not fully cleared | 6/16 WALTER repair pushed: Iran anchor re-stamped, registry refreshed, staleness sweep added. Remaining issue is routing/receipt + cron/feed reliability. |
| NEXUS | ✅ review-passed | ORC four-group cross-check upheld matrix; no rows overturned. |
| LABOR | ✅ fixes landed | Functional pushed packet reviewed cleanly; later LABOR hygiene commit fixed stale handoff/push lines. |

---

## Live Market Levels — Dashboard Pull 2026-06-16 ~16:44 ET

| Series | Value | As-of | Zone | Read |
|---|---:|---|---|---|
| HY OAS | **266bps** | **[FRED 6/15]** | 🟢 | Broad credit still refuses cascade; only **6bp** from <260 R3/blended-credit kill. |
| CCC OAS | **937bps** | **[FRED 6/15]** | 🟡 | Tail remains elevated but below 1000 red. |
| Brent | **$79.49** | live | 🟢 | De-escalation priced; physical reopening still unverified. |
| Gas weekly | **4.05** | **[6/15]** | 🔴 | Consumer pressure persists. |
| USD/JPY | **160.48** | live | 🔴 | Carry fuel still loaded despite BOJ hike-as-priced. |
| Initial claims | **229k** | **[6/6]** | 🟡 | Drift, not break; shadow est **284k**. |
| Continuing claims | **1.795M** | **[5/30]** | 🟢 | Still below red band. |
| SOFR | **3.69** | **[6/15]** | 🟡 | Monitor funding plumbing. |
| 10Y Yield | **4.47%** | **[6/15]** | 🟡 | FOMC resolver. |
| CP-TBill Spread | **0.12** | **[6/11]** | 🟢 | Clean. |
| SOFR-IORB | **0.04** | **[6/15]** | 🟢 | Clean, near yellow edge. |
| KRE | **$72.49** | live | 🟢 | Banks not confirming broad cascade. |
| APO | **$138.48** | live | 🟢* | Context: high alts tape contradicts private-credit bear timing. |
| ARES | **$134.98** | live | 🟡 | Elevated; verify close-streak before red. |
| OZK | **$50.35** | live | 🟢 | Above threshold, idiosyncratic/Q2-print gated. |
| WAL | **$81.48** | live | 🟢 | Above threshold; REGINALD idiosyncratic not broad-bank. |
| FXY | **$57.19** | live | 🟡 | BOJ done; TIC/expiry still context. |
| TLT | **$86.19** | live | 🟡 | FOMC resolver; no action without broker/Will truth. |
| BIZD | **$12.62** | live | 🔴 | BDC/private-credit stress remains live. |
| VIX | **16.41** | live | 🟢 | Vol calm; coiled-spring/tail caveat via SKEW/CCC/carry. |

---

## Near Gates — Jun 16–19

| Date / Window | Gate | Owner(s) | Prome read |
|---|---|---|---|
| **Tue 6/16** | Prome state correction | Prome | Do this first: clear stale boot-surface contradictions. |
| **Wed 6/17** | FOMC + dots/SEP + VIX expiry stack | HENRY/LIQUID/RED/VIOLET/NEXUS | Biggest macro resolver. Hawkish-of-pricing stresses R1/R6/vol; dovish/risk-on can push HY <260 and kill R3 blended-credit bear axis. |
| **Thu 6/18** | Claims, May TIC, expiry cluster | LABOR/SAM/LIQUID/Prome | Claims pre-mortem live; TIC/FXY context; expiry cleanup requires broker/Will truth. |
| **Fri 6/19** | Geneva Iran signing / HYG expiry | WALTER/HAWK/BRENT/LIQUID | Iran signing is binary for M-06; HYG Jun $75P remains written off / let expire. |

---

## FOMC Operating Card — Jun 17

**Purpose:** grade the event; do not auto-trade.

| Branch | What to watch | Prome read |
|---|---|---|
| Hawkish-of-pricing | 2Y/front-end repricing higher, VIX/vol re-firms, USDJPY/carry stress | Re-arms macro/carry/vol fragility: R1 + R6 + coiled-spring path. |
| Dovish / risk-on in-line | HY/HYG compression, banks/alts bid, vol crushed | Can kill surviving R3 blended-credit bear axis if HY sustains <260. |
| In-line / unresolved | Mixed 2Y/HYG/VIX, HY holds >260 | Nothing resolves; re-anchor to Jun18 claims/TIC and late-Jun/Jul BDC/PC marks. |

**HY discipline:** HY OAS **266 [FRED 6/15]** is only 6bp from <260. Use live proxies at the event, but do not declare R3 kill on an intraday tick. Confirm with FRED T+1 and require sustained <260.

**Safety:** any trade/expiry action still requires broker/Will truth. Prome may grade, synthesize, and route; Prome does not execute.

---

## Prome Work Queue

| Pri | Work | Action |
|---|---|---|
| 🔴 | **FOMC grading setup** | Use operating card above; refresh dashboard/proxies at event time, confirm HY OAS by FRED next day. |
| 🟠 | **WALTER diagnosis continuation** | WALTER anchor/registry improved; still need routing receipts and cron/feed health. Trace dropped BRENT/HAWK signals if not already resolved. |
| 🟠 | **Position-state reconciliation** | Separate lane only; no expiry action without broker/Will truth. |
| 🟠 | **NEXUS/LABOR propagation** | NEXUS should reflect LABOR standing brief if Will wants it; LABOR functional fixes already good. |
| 🔵 | **Execution-rails design** | Later: prevent another HYG Jun→Dec missed-roll failure by pre-registering ladders/triggers. |

---

## Skip / Guardrails

- No trade execution.
- No `AGENTS/*` edits unless explicitly approved.
- No old May/Jun option rails without broker/Will reconciliation.
- Prices/levels above are from dashboard pull at ~16:44 ET; refresh before reuse.
