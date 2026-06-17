# TODAY.md — Wednesday June 17, 2026

**Objective:** FOMC is today's market resolver; WALTER direct-routing architecture is the next system-work lane after clear. Operate from fresh repo state and refreshed dashboard/proxies before market reads. **No `AGENTS/*` edits unless Will explicitly scopes them; for WALTER changes, instruct/spawn WALTER to edit its own domain.**

**Current regime:** **Surface tape remains bull/de-risking while tail/private/physical stress stays sticky.** Broad cascade is still not confirmed: HY OAS is **271bps [FRED 6/16]**, still above the <260 blended-credit kill line; VIX is **16.55**; banks remain bid; Brent is around **$80.72**. But CCC remains elevated at **944bps [FRED 6/16]**, BIZD is still red, USD/JPY is **160.26**, gas remains high, and Iran/Hormuz physical reopening is not resolved until the 6/19 Geneva/signing track. This is a fragile calm, not systemic repair.

---

## Repo / Prome State

| Item | State | Read |
|---|---|---|
| Git | ✅ pulled cleanly | WALTER's latest GitHub updates pulled; closeout edits local until committed. |
| Prome boot surfaces | ✅ closing out | SCRATCH/HANDOFF/STATUS updated for clear-window continuity; TODAY is now Jun17/FOMC-aware. |
| WALTER | 🟠 tooling improved; delivery change pending | 6/16–17 WALTER self-audit tools landed. Spec/BOARD checks pass; stale cron feeds remain; BOARD-only delivery still needs replacement with recipient-local handoffs. |
| NEXUS | ✅ review-passed | ORC four-group cross-check upheld matrix; no rows overturned. |
| LABOR | ✅ fixes landed | Functional pushed packet reviewed cleanly; later LABOR hygiene commit fixed stale handoff/push lines. |

---

## Live Market Levels — Dashboard Pull 2026-06-17 ~11:00 ET

| Series | Value | As-of | Zone | Read |
|---|---:|---|---|---|
| HY OAS | **271bps** | **[FRED 6/16]** | 🟢 | Broad credit still refuses cascade; **11bp** from <260 R3/blended-credit kill. |
| CCC OAS | **944bps** | **[FRED 6/16]** | 🟡 | Tail remains elevated but below 1000 red. |
| Brent | **$80.72** | live | 🟢 | De-escalation priced; physical reopening still unverified. |
| Gas weekly | **4.05** | **[6/15]** | 🔴 | Consumer pressure persists. |
| USD/JPY | **160.26** | live | 🔴 | Carry fuel still loaded despite BOJ hike-as-priced. |
| Initial claims | **229k** | **[6/6]** | 🟡 | Drift, not break; shadow est **284k**. |
| Continuing claims | **1.795M** | **[5/30]** | 🟢 | Still below red band. |
| SOFR | **3.63** | **[6/16]** | 🟡 | Monitor funding plumbing. |
| 10Y Yield | **4.47%** | **[6/15]** | 🟡 | FOMC resolver. |
| CP-TBill Spread | **0.12** | **[6/11]** | 🟢 | Clean. |
| SOFR-IORB | **-0.02** | **[6/16]** | 🟢 | Clean. |
| KRE | **$72.50** | live | 🟢 | Banks not confirming broad cascade. |
| APO | **$139.76** | live | 🟢* | Context: high alts tape contradicts private-credit bear timing. |
| ARES | **$136.18** | live | 🟡 | Elevated; verify close-streak before red. |
| OZK | **$50.52** | live | 🟢 | Above threshold, idiosyncratic/Q2-print gated. |
| WAL | **$81.69** | live | 🟢 | Above threshold; REGINALD idiosyncratic not broad-bank. |
| FXY | **$57.23** | live | 🟡 | BOJ done; TIC/expiry still context. |
| TLT | **$86.36** | live | 🟡 | FOMC resolver; no action without broker/Will truth. |
| BIZD | **$12.55** | live | 🔴 | BDC/private-credit stress remains live. |
| VIX | **16.55** | live | 🟢 | Vol calm; coiled-spring/tail caveat via SKEW/CCC/carry. |

---

## Near Gates — Jun 17–19

| Date / Window | Gate | Owner(s) | Prome read |
|---|---|---|---|
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

**HY discipline:** HY OAS **271 [FRED 6/16]** is still above <260. Use live proxies at the event, but do not declare R3 kill on an intraday tick. Confirm with FRED T+1 and require sustained <260.

**Safety:** any trade/expiry action still requires broker/Will truth. Prome may grade, synthesize, and route; Prome does not execute.

---

## Prome Work Queue

| Pri | Work | Action |
|---|---|---|
| 🔴 | **FOMC grading setup** | Use operating card above; refresh dashboard/proxies at event time, confirm HY OAS by FRED next day. |
| 🟠 | **WALTER direct-routing architecture** | Instruct/spawn WALTER to supersede BOARD-only with BOARD-first + `AGENTS/{RECIPIENT}/inbox/WALTER/` handoffs; patch `.venv` doctor command; audit/backfill SIG-W-20260610-001/-002 for BRENT if appropriate. |
| 🟠 | **Position-state reconciliation** | Separate lane only; no expiry action without broker/Will truth. |
| 🟠 | **NEXUS/LABOR propagation** | NEXUS should reflect LABOR standing brief if Will wants it; LABOR functional fixes already good. |
| 🔵 | **Execution-rails design** | Later: prevent another HYG Jun→Dec missed-roll failure by pre-registering ladders/triggers. |

---

## Skip / Guardrails

- No trade execution.
- No `AGENTS/*` edits unless explicitly approved.
- No old May/Jun option rails without broker/Will reconciliation.
- Prices/levels above are from dashboard pull at ~16:44 ET; refresh before reuse.
