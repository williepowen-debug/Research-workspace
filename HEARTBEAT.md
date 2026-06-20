# HEARTBEAT.md
**Updated:** 2026-06-19 20:26 ET (OpenClaw heartbeat — Geneva MOU signed; energy tail risk deferred, HY kill still unconfirmed)

## Regime

**Geneva de-escalation branch fired; broad credit cascade still not confirmed.** The 6/19 Iran/Geneva binary resolved toward de-escalation: U.S. reporting says the United States and Iran signed a memorandum of understanding that reopened the Strait of Hormuz and established a ceasefire framework, with a new **60-day negotiation window** around Iran nuclear commitments. Iran’s strait authority reportedly waived transit-related fees during the negotiation period while requiring 48h transit requests. This defers the immediate Hormuz/oil-shock tail, but it does not eliminate it: Trump explicitly warned that if talks fail, renewed strikes could again bottle up oil flows through the strait.

**Tape read: de-escalation + calm, not system break.** Current dashboard: HY OAS **263bps [FRED 6/17]**, CCC **939bps [6/17]**, Brent **$80.59**, VIX **16.78**, KRE **$71.72**, WAL **$79.91**, TLT **$86.75**, 10Y **4.49 [6/17]**. Banks/vol are not confirming cascade stress; duration is still yellow but not disorderly. Carry remains the main red macro stress: USD/JPY **161.28🔴**, FXY **$56.85🔴**. BDC/PC weakness persists at the margin with BIZD **$12.36🔴**, ARES **$129.34🟡**, but not enough by itself to confirm broad cascade.

Working model: **energy shock deferred; post-FOMC/carry divergence unresolved.** The Geneva MOU weakens the HAWK/BRENT immediate oil-shock path and makes M-06 less acute, but the 60-day fuse leaves a late-August re-escalation option. The credit bear axis remains on probation: HY OAS at **263 [6/17]** is still only 3bp above the <260 blended-credit kill line. Sustained <260 still kills/reprices R3 unless offset by fresh bank/private-credit deterioration. For now: **fragile calm, not breakdown.**

Key updates since prior HEARTBEAT:
- **Geneva gate resolved de-escalatory:** U.S.–Iran MOU signed; Strait/Hormuz reopening + ceasefire framework; 60-day negotiation window creates new fuse rather than final peace.
- **Energy tail risk deferred:** Brent **$80.59** is green/below stress thresholds; falling crude should be read as geopolitical de-escalation, not proof the physical system is structurally repaired.
- **HY kill still not confirmed:** HY OAS **263 [FRED 6/17]** remains 3bp above <260. No new FRED HY print in dashboard yet.
- **Vol/banks calm:** VIX **16.78**, KRE **$71.72**, WAL **$79.91** argue against immediate cascade confirmation.
- **Carry remains red:** USD/JPY **161.28🔴**, FXY **$56.85🔴** keep SAM/carry unwind risk live despite energy de-escalation.
- **Private-credit/BDC weak spot persists:** BIZD **$12.36🔴**, ARES **$129.34🟡** remain the offset to otherwise calm credit/bank tape, but not standalone broad-cascade proof.
- **CORAL Phase 1 maturity scaffold completed and pushed:** `SCRATCH.md`, `NEXUS_BRIEF.md`, `board_log.tsv`, and boot/write-back protocol are now on origin in commit `08c0d42b`.

## Stress dashboard

HY OAS **263🟢 [FRED 6/17]** *(3bp above <260 kill)* · CCC **939🟡 [FRED 6/17]** · 10Y **4.49🟡 [FRED 6/17]** · TLT **$86.75🟡** · VIX **16.78🟢** · Brent **$80.59🟢** · Gas weekly **4.05🔴 [6/15]** · USD/JPY **161.28🔴** · WAL **$79.91🟢** · KRE **$71.72🟢** · OZK **$49.26🟡** · APO **$137.50** *(high alts tape still contradicts immediate PC-bear timing)* · ARES **$129.34🟡** · BIZD **$12.36🔴** · FXY **$56.85🔴** · Initial claims **226k🟡 [6/13]** / shadow est **281k** · Continuing claims **1.810M🟢 [6/6]** · SOFR-IORB **-0.02🟢 [6/17]** · CP-TBill **0.08🟢 [6/17]**

## Thresholds

| Indicator | Green | Yellow | Red | Current |
|---|---|---|---|---|
| HY OAS | <300 | 300-320 | >320 | **263🟢 [FRED 6/17]** *(3bp above <260 kill)* |
| CCC OAS | <900 | 900-1000 | >1000 | **939🟡 [FRED 6/17]** |
| 10Y Treasury | <4.40 | 4.40-4.75 | >4.75 | **4.49🟡 [FRED 6/17]** |
| TLT | >$88 | $85-88 | <$85 | **$86.75🟡** |
| Brent | <$85 | $85-100 | >$100 | **$80.59🟢** |
| Gas weekly | <$3.75 | $3.75-4.00 | >$4.00 | **4.05🔴 [6/15]** |
| USD/JPY | <150 | 150-158 | >158 | **161.28🔴** |
| VIX | <18 | 18-25 | >25 | **16.78🟢** |
| SOFR-IORB | <+0.05 | 0.05-0.25 | >0.25 | **-0.02🟢 [6/17]** |
| KRE | >$69 | $65-69 | <$65 | **$71.72🟢** |
| WAL | >$78 | $72-78 | <$72 | **$79.91🟢** |
| OZK | >$50 | $45-50 | <$45 | **$49.26🟡** |
| APO | <$125 | $125-130 | >$130 x3 sessions | **$137.50** *(reassess context; not standalone trigger)* |
| ARES | <$125 | $125-132 | >$132 x3 sessions | **$129.34🟡** |
| BIZD | >$13 | $12.50-13 | <$12.50 | **$12.36🔴** |
| Initial claims | <220k | 220-245k | >245k | **226k🟡 [6/13]**; shadow est **281k** |
| Continuing claims | <1.80M | 1.80-1.90M | >1.90M | **1.810M🟢 [6/6]** |

## HEARTBEAT Cadence / Ownership

**Approved Jun 4:** Prome owns `HEARTBEAT.md`. Update after Prome boot-surface refreshes, regime-level changes, major decision-rail changes, or when >48h stale during market week. Do **not** update daily by default just for hygiene.

## Near Gates — Jun 20–22

| Date / Window | Gate | Owner(s) | Read |
|---|---|---|---|
| **Fri/Sat 6/19–20** | Post-Geneva follow-through + HY print availability | WALTER/HAWK/BRENT/LIQUID/VIOLET/Prome | MOU signed reduces immediate oil shock, but follow-through matters: Strait traffic, Iranian compliance language, Israel/Hezbollah behavior, and whether Brent/VIX stay calm. |
| **Fri/Sat 6/20** | CFTC carry-position read | SAM/LIQUID | Tests SAM v1.6 carry-convexity frame while USD/JPY >161 and FXY red. |
| **Next FRED HY update** | HY <260 kill line | LIQUID/NEXUS/Prome | Sustained <260 kills/reprices blended-credit bear axis unless offset by bank/private-credit deterioration. |
| **Late Jun / Jul** | BCRED/Q2 redemption, BDC/Q2, SAVE Jul 1 | BROCK/CARL/LABOR | Structural stress watch; not immediate broad-cascade confirmation. |

## Blocking / Pending

| Pri | Decision / Work | Reference |
|---|---|---|
| 🔴 | **HY <260 kill-line monitoring.** Latest HY **263 [FRED 6/17]**; <260 still not confirmed but very close. Sustained <260 kills/reprices R3 blended-credit axis unless bank/private-credit deterioration offsets. | NEXUS/ORC review, dashboard |
| 🔴 | **Post-FOMC branch confirmation.** Claims benign/yellow, VIX/banks calm, energy shock deferred; carry remains red and HY remains near kill. Need next HY print + SAM/CFTC carry read. | `PROME/TODAY.md`, `PROME/ACTIVE_DECISIONS.md` |
| 🟠 | **Geneva 60-day fuse.** Immediate M-06 oil shock deferred, but late-August re-escalation risk is now the tail. Watch Strait/Hormuz implementation and nuclear-talk language. | WALTER/HAWK/BRENT anchors |
| 🟠 | **WALTER Phase 2 consumption rollout.** OpenClaw consume paths are working; CORAL Phase 1 now has WALTER board-log intake. Remaining work is CC recipient self-apply and later CC push/urgent-delivery automation. | `AGENTS/WALTER/STATUS.md`, `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` |
| 🟠 | **Jun18/19 expiry cleanup.** HYG dead; TLT/WAL/non-TLT legs require broker reconciliation. | `PROME/ACTIVE_DECISIONS.md` |
| 🟠 | **Position-state reconciliation pass.** Separate future task; do not mix with market synthesis unless Will pivots. | `PROME/ACTIVE_DECISIONS.md` |
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
