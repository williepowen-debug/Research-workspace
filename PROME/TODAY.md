# TODAY.md — Sunday June 21, 2026

**Objective:** Close out the AGENTS/PROME organization pass cleanly and preserve the current market frame without pretending we refreshed live data.

**Current regime:** unchanged from `HEARTBEAT.md`: **signed-but-fraying MOU / contested Hormuz re-closure / unresolved credit-carry divergence.** Iran’s Jun20 Hormuz re-closure declaration remains official/declaratory/contested, not yet kinetic. Energy tail is re-fat, but broad credit cascade is still unconfirmed. No live market refresh was run in this closeout session; use HEARTBEAT/FRED/dashboard refresh before citing fresh levels.

---

## Repo / Prome State

| Item | State | Read |
|---|---|---|
| Git | ✅ clean/synced before closeout | Two cleanup commits pushed: grouped AGENTS indexes and canonical network/path cleanup. |
| AGENTS grouped views | ✅ installed | `AGENTS/_INDEX.md` plus group files; canonical agent dirs remain flat as `AGENTS/<NAME>/`. |
| AGENTS topology map | ✅ installed | `AGENTS/_NETWORK.md` is now canonical topology/transmission map. |
| Dashboard network | ✅ updated | Main dashboard Network tab mirrors canonical map; standalone `dashboard/network.html` is pointer/redirect to avoid drift. |
| PROME path cleanup | ✅ pushed | Live Prome docs no longer point at retired `PROME/TOSCANINI/`; moved inbox/outbox references fixed where canonical targets existed. |
| Position truth | 🟠 unreconciled | No expiry/trade action without broker/Will truth. |

---

## Live Market Levels

No fresh market data was pulled in this closeout session. Use `HEARTBEAT.md` as the regime pointer and run the market dashboard / FRED fetch before citing new levels.

Last HEARTBEAT frame: HY OAS **263 [FRED 6/17]** near <260 kill; CCC **939 [FRED 6/17]**; Brent **$80.59** pre-Jun20 declaration; VIX **16.78**; KRE/WAL calm; USD/JPY/FXY carry stress red; BIZD weak.

---

## Near Gates — Jun 21–24

| Date / Window | Gate | Owner(s) | Prome read |
|---|---|---|---|
| **Sun/Mon 6/21–22** | Brent reopen after Jun20 Hormuz re-closure declaration | BRENT/HAWK/VIOLET/Prome | First tape test. Spike = energy tail repricing / decoupling stress; shrug = declaration stays coercive/non-physical. |
| **Sun/Mon 6/21–22** | Iran talks / Switzerland follow-through + Lebanon behavior | WALTER/HAWK/BRENT | If talks convene and Lebanon quiets, C-grind holds. If talks fail + second-step/kinetic language appears, D-tail rises. |
| **Mon 6/22** | CFTC carry-position read delayed by Juneteenth | SAM/LIQUID | Tests SAM v1.6 carry-convexity frame while USD/JPY >161 and FXY red. |
| **Next FRED HY update** | HY <260 kill line | LIQUID/NEXUS/Prome | Sustained <260 kills/reprices R3 unless offset by bank/private-credit deterioration. |
| **Wed 6/24** | EIA WPSR / Cushing <20M risk | BRENT/LIQUID/HENRY/RED | Cushing was ~20.03M [6/12]; sub-20M fires BRENT Boundary #3 / WTI delivery-dislocation watch. |
| **Late Jun/Jul** | CORAL per-metro grid + Q2 bank prep | CORAL/Prome | New thesis rails installed; next analytical work is geography convergence and Q2 bank diagnostics. |

---

## Prome Work Queue

| Pri | Work | Action |
|---|---|---|
| ✅ | **AGENTS grouped directory views** | Pushed. Use `AGENTS/_INDEX.md`; do not move canonical dirs casually. |
| ✅ | **Canonical agent network map** | Pushed. Use `AGENTS/_NETWORK.md`; dashboard is rendering only. |
| ✅ | **PROME stale path cleanup** | Pushed. Retired Toscanini refs demoted; live Prome path checks clean. |
| 🔴 | **Jun22 Brent / Hormuz tape test** | Watch Brent/vol/traffic/insurance behavior after declaration. |
| 🔴 | **HY <260 kill-line monitoring** | Latest HEARTBEAT level 263; sustained <260 kills/reprices R3 unless bank/PC deterioration offsets. |
| 🟡 | **SAM CFTC/carry gate** | Juneteenth-delayed read tests carry-convexity survival. |
| 🟡 | **WALTER stale upstream feeds / registry drift** | Will to handle WALTER points personally; Prome monitors only unless scoped. |
| 🟡 | **CORAL per-metro convergence grid** | Build Miami/Tampa/Orlando/Jax/SW-FL grid when CORAL lane resumes. |
| 🟠 | **Position-state reconciliation** | Separate lane only; no expiry action without broker/Will truth. |
| 🔵 | **Execution-rails design** | HYG Jun→Dec failure remains design debt. |

---

## Skip / Guardrails

- Do not edit WALTER specs/state from Prome unless Will explicitly scopes it.
- Do not make shared auto-memory index changes during active agent work; coordinate first.
- Do not maintain multiple live agent network maps.
- Do not physically reorganize `AGENTS/<NAME>/` folders without a migration pass.
- No trade execution.
- No old May/Jun option rails without broker/Will reconciliation.
