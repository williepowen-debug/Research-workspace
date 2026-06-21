# HEARTBEAT.md
**Updated:** 2026-06-21 10:24 ET (OpenClaw heartbeat — condensed injected surface; no regime/market-data refresh)

## Regime

**Signed-but-fraying MOU; Hormuz re-closure declared; broad credit cascade still not confirmed.** The Jun17 Islamabad/Geneva MOU still matters — it repriced the immediate oil-shock tail lower — but Jun20 follow-through weakened the clean de-escalation branch. BRENT/HAWK report Iran’s joint military command re-declared the Strait of Hormuz closed on Jun20 as a “first step” response to alleged U.S. MOU breach and continued Israeli Lebanon strikes. CENTCOM disputes physical effect and says traffic continued; treat as **official/declaratory/contested, not yet kinetic**.

**Tape read: asymmetric tail re-fat, not confirmed breakdown.** Markets were closed for the Jun20 declaration, so Jun22 Brent reopen / follow-through is the first clean test. Fri-close dashboard still showed fragile calm: HY near the <260 kill line, VIX/banks calm, duration yellow, carry red, BDC/PC weak but not broad-cascade proof.

Working model: **energy shock was deferred by the MOU, then re-fat-tailed by the Jun20 Hormuz declaration.** This is not a return to full kinetic Phase 1 unless behavior confirms: vessel targeted/seized/mined, Gulf energy-infra hit, JWC/insurer withdrawal, or Brent/vol repricing hard on reopen. Credit bear axis remains on probation: sustained HY <260 kills/reprices R3 unless offset by fresh bank/private-credit deterioration. For now: **contested energy tail + fragile calm, not broad breakdown.**

Key updates since prior HEARTBEAT:
- **Hormuz declaration:** official but contested/non-kinetic so far; Jun22 tape decides whether the declaration remains coercive or becomes physical.
- **Lebanon seam re-heated:** Israeli Lebanon strikes are now wired into Iran’s MOU-breach/Hormuz rhetoric; HAWK cut B and raised D modestly (C remains base).
- **Energy divergence sharper:** BRENT v4.1 says price priced reopening while physical/insurance/liner gates remain unresolved.
- **Credit/vol still unconfirmed:** HY near <260 kill; VIX/KRE/WAL calm as of Fri close; BIZD/ARES weak but not standalone systemic proof.
- **Carry remains red:** USD/JPY and FXY keep SAM/carry unwind risk live despite energy see-saw.
- **CORAL maturity:** CORAL boot/inbox/thesis rails are installed and pushed; next CORAL work is per-metro convergence grid + Q2 FL-bank prep.

## Stress dashboard

**Weekend freshness note:** last dashboard / Fri-close orientation, not fresh Sunday market data. Preserve observation dates; refresh dashboard/FRED before citing levels as current.

HY OAS **263🟢 [FRED 6/17]** *(3bp above <260 kill)* · CCC **939🟡 [FRED 6/17]** · 10Y **4.49🟡 [FRED 6/17]** · TLT **$86.75🟡** · VIX **16.78🟢** · Brent **$80.59🟢** *(pre-Jun20 re-closure declaration; Jun22 reopen is test)* · Gas weekly **4.05🔴 [6/15]** · USD/JPY **161.28🔴** · WAL **$79.91🟢** · KRE **$71.72🟢** · OZK **$49.26🟡** · APO **$137.50** *(high alts tape still contradicts immediate PC-bear timing)* · ARES **$129.34🟡** · BIZD **$12.36🔴** · FXY **$56.85🔴** · Initial claims **226k🟡 [6/13]** / shadow est **281k** · Continuing claims **1.810M🟢 [6/6]** · SOFR-IORB **-0.02🟢 [6/17]** · CP-TBill **0.08🟢 [6/17]**

## Thresholds

Full threshold definitions live in `FORGE/tools/market-data/config.py` and the dashboard tooling. Keep only the compact dashboard line here; refresh dashboard/FRED before citing levels as current.

## HEARTBEAT Cadence / Ownership

**Approved Jun 4:** Prome owns `HEARTBEAT.md`. Update after Prome boot-surface refreshes, regime-level changes, major decision-rail changes, or when >48h stale during market week. Do **not** update daily by default just for hygiene.

## Near Gates — Jun 21–24

| Date / Window | Gate | Owner(s) | Read |
|---|---|---|---|
| **Sun/Mon 6/21–22** | Brent reopen after Jun20 Hormuz re-closure declaration | BRENT/HAWK/VIOLET/Prome | First tape test. Spike = energy tail repricing / decoupling stress; shrug = declaration stays coercive/non-physical. |
| **Sun/Mon 6/21–22** | Iran talks / Switzerland follow-through + Lebanon behavior | WALTER/HAWK/BRENT | If talks convene and Lebanon quiets, C-grind holds. If talks fail + second-step/kinetic language appears, D-tail rises. |
| **Mon 6/22** | CFTC carry-position read delayed by Juneteenth | SAM/LIQUID | Tests SAM v1.6 carry-convexity frame while USD/JPY >161 and FXY red. |
| **Next FRED HY update** | HY <260 kill line | LIQUID/NEXUS/Prome | Sustained <260 kills/reprices blended-credit bear axis unless offset by bank/private-credit deterioration. |
| **Wed 6/24** | EIA WPSR / Cushing <20M risk | BRENT/LIQUID/HENRY/RED | Cushing was ~20.03M [6/12]; sub-20M would fire BRENT Boundary #3 / WTI delivery-dislocation watch. |
| **Late Jun / Jul** | BCRED/Q2 redemption, BDC/Q2, SAVE Jul 1; CORAL per-metro + Q2 FL-bank prep | BROCK/CARL/LABOR/CORAL | Structural stress watch; not immediate broad-cascade confirmation. |

## Blocking / Pending

| Pri | Decision / Work | Reference |
|---|---|---|
| 🔴 | **HY <260 kill-line monitoring.** Latest HEARTBEAT level **263 [FRED 6/17]**; sustained <260 kills/reprices R3 unless bank/private-credit deterioration offsets. | NEXUS/ORC review, dashboard |
| 🔴 | **Jun20 Hormuz declaration tape test.** Official re-closure declaration is contested/non-kinetic so far; Jun22 Brent/vol/insurance/traffic response decides whether tail reprices. | `AGENTS/BRENT/STATUS.md`, `AGENTS/HAWK/STATUS.md` |
| 🔴 | **Post-FOMC / carry divergence.** Claims benign/yellow, VIX/banks calm, carry red, energy tail re-fat but unconfirmed. Need next HY print + SAM/CFTC carry read. | `PROME/TODAY.md`, `PROME/ACTIVE_DECISIONS.md` |
| 🟡 | **WALTER Iran anchor / DEWEY next gate.** Iran anchor re-stamped after BRENT/HAWK Jun20 updates; DEWEY first live run requires CONTEXT refresh. | `AGENTS/WALTER/anchors/IRAN_WAR.md`, `AGENTS/DEWEY/REVIVAL_PLAN.md` |
| 🟠 | **Position-state reconciliation.** HYG dead; TLT/WAL/non-TLT legs require broker/Will truth. Do not mix with market synthesis unless Will pivots. | `PROME/ACTIVE_DECISIONS.md` |
| 🔵 | **PROME execution-rails design.** HYG roll Jun→Dec died for lack of mechanism; design debt. | BROCK LESSONS #16 |

## Pointers

- Current operator card → `PROME/TODAY.md`
- Current Prome working state → `PROME/SCRATCH.md`, `PROME/STATUS.md`
- Active decisions safety index → `PROME/ACTIVE_DECISIONS.md`
- Agent state → `AGENTS/<NAME>/STATUS.md`
- WALTER Iran anchor → `AGENTS/WALTER/anchors/IRAN_WAR.md`
- HAWK/BRENT current energy-geopolitical read → `AGENTS/HAWK/STATUS.md`, `AGENTS/BRENT/STATUS.md`
- NEXUS current synthesis → `AGENTS/NEXUS/STATUS.md`

## Skip

Late night (11pm-8am ET): urgent only. Weekend: light monitoring.
