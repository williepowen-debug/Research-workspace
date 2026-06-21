# Boot-Surface Refresh — Phase 2 Edit Map
**Created:** 2026-06-14 ~17:10 ET  
**Owner:** Prome  
**Scope:** Edit map only. **No boot-surface rewrites yet. No agent files edited.**

## Purpose

Convert Phase 0/1 findings into a file-by-file boot-surface refresh plan. This is the checkpoint before Phase 3 edits.

Sources:
- `PROME/BOOT_SURFACE_REFRESH_2026-06-14_PHASE0.md`
- `PROME/BOOT_SURFACE_REFRESH_2026-06-14_PHASE1.md`
- Current stale surfaces: `HEARTBEAT.md`, `PROME/TODAY.md`, `PROME/STATUS.md`, `PROME/SCRATCH.md`, `PROME/FLEET_SCAN.md`, `PROME/ACTIVE_DECISIONS.md`
- Live dashboard pulled Phase 0
- Bounded read-only agent header inspection Phase 1

---

## 1. Core Regime Replacement

### Replace old Jun 7–8 frame

Old boot surfaces repeatedly say:

> Substance/tape divergence is narrowing; vol joined the stress column; HY OAS is the sole remaining tape refusal; CPI/refunding week is ahead.

This is now stale / wrong.

### New working frame

Use this as the canonical refresh language:

> **Broad cascade is still not confirmed. The event-vol spike faded, HY OAS remains tight, banks rallied, and Brent collapsed sub-$90. But the structural/tail side did not heal: CCC remains sticky, SKEW stayed bid through the VIX crush, private-credit/BDC stress widened, consumer-credit stress persists, Japan/BOJ risk is live, and physical energy/chokepoint stress remains severe despite the price collapse. Current regime is not “stress everywhere”; it is “surface tape de-risked while tail/private/physical stress stayed sticky.”**

Short version for cramped surfaces:

> **Surface tape de-risked; tail/private/physical stress stayed sticky. No broad cascade until HY OAS breaks.**

### Current dashboard anchor to use

From Phase 0 dashboard:

- HY OAS **278bps [FRED 6/11]** 🟢
- CCC OAS **956bps [FRED 6/11]** 🟡
- Brent **$87.33** 🟡
- VIX **17.68** 🟢
- USD/JPY **160.18** 🔴
- Gas weekly **4.15 [6/8]** 🔴
- Initial claims **229k [6/6]** 🟡; shadow est **284k**
- Continuing claims **1.795M [5/30]** 🟢
- SOFR-IORB **-0.05 [6/11]** 🟢
- 10Y **4.45 [6/11]** 🟡
- KRE **$73.41** 🟢
- WAL **$83.67** 🟢
- OZK **$52.10** 🟢
- APO **$133.88** — dashboard green but trigger context: >$130 ×4 closes fired reassess obligation
- ARES **$134.90** 🟡
- BIZD **$12.71** 🔴
- FXY **$57.26** 🟡
- TLT **$85.77** 🟡

Caveat: market-data dashboard emitted useful output but exited code 1. Treat data as usable, but later verify script health.

---

## 2. Near Gates / Calendar Replacement

Replace Jun 8–12 week-ahead slate with current near-horizon gates:

| Date / Window | Gate | Owner(s) | Boot-surface implication |
|---|---|---|---|
| **Mon Jun 15** | Brent/BRENT double-trigger watch: M1-M3 completion + sub-$88/XLE re-eval if tape holds | BRENT/HAWK | Energy tape priced de-escalation; physical stress coiled. Watch whether Brent confirms demand-destruction/curve flattening. |
| **Mon Jun 16** | BOJ + Sumitomo Life FY2025 ESR | SAM | Japan/FXY near gate; MOF/intervention odds marked down but BOJ risk remains. |
| **Tue/Wed Jun 16–17** | FOMC + dots/SEP | HENRY/LIQUID/RED/VIOLET | Biggest macro resolver. Duration oscillation, Fed hike/cut repricing, vol-event premium, and TLT salvage all converge here. |
| **Wed Jun 17** | VIX quarterly / M1 expiry stack | VIOLET | Complacency tape + bid tail; entry blocked by Bin-B credit unless tree changes. |
| **Thu Jun 18** | May TIC = April flows; Jun18 option cluster / salvage backstop | SAM/LIQUID/Will/Prome | Foreign-flow / Japan/Belgium proxy; expiry cleanup/reconciliation, not stale trigger execution. |
| **Fri Jun 19** | HYG Jun $75P expires worthless per LIQUID write-off | LIQUID/Will | Do not surface as actionable. |
| **Jun 8–22** | HAW-11 leakage window / T-08 correlated-fragility node | HAWK/NEXUS/Prome | Portfolio-fragility awareness, not trade rail. |
| **Late Jun / Jul** | BCRED/Q2 redemption, BDC/PC Q2 print setup, SAVE Jul 1 | BROCK/CARL/LABOR | Structural stress watch; not immediate broad-cascade confirmation. |

---

## 3. File-by-File Edit Map

### A. `PROME/SCRATCH.md`

**Current problem:** full Jun 8 infra-session handoff. It says next entry is Tue/Wed CPI prep and BOND matrix v2, all stale.

**Action:** full rewrite.

**New structure:**
1. Header: `Last Updated: 2026-06-14 PM ET — post-pull boot-surface refresh Phase 0–2`
2. `What Just Happened`
   - Repo pulled huge Jun 8–14 update; clean at `c87c00ac` before phase notes.
   - Phase 0 baseline written.
   - Phase 1 bounded agent inspection written.
   - Phase 2 edit map written.
   - No agent files edited; only Prome checkpoint notes created.
3. `Current Working Regime`
   - Surface tape de-risked; tail/private/physical sticky.
   - Dashboard anchor summarized.
4. `Immediate Next Steps`
   - Phase 3 boot-surface rewrites in order: TODAY → STATUS → ACTIVE_DECISIONS → FLEET_SCAN → HEARTBEAT; SCRATCH can be first/last depending cadence.
   - After edits, verify with `git diff --stat` and maybe compact dashboard.
5. `Cautions`
   - HENRY/NEXUS/WALTER stale; do not lean on pre-CPI headers.
   - WALTER Iran anchor stale vs HAWK/BRENT Jun 13.
   - Broker/position truth unreconciled; old rails verification-required.
   - HYG written off by LIQUID; do not surface.
6. `Open Questions for Will`
   - Whether to keep phase notes as audit trail or delete/archive after boot surfaces are refreshed.
   - Whether to refresh WALTER Iran anchor / HENRY / NEXUS after boot surfaces.

**Preserve from old SCRATCH:** two-machine model / push-is-Will-coordinated / pathspec guardrails if still useful, but demote from main story to cautions or omit if duplicated in STATUS.

---

### B. `PROME/TODAY.md`

**Current problem:** dated Sunday Jun 7 → Monday Jun 8; all catalysts stale.

**Action:** full rewrite as `Sunday Jun 14 → Monday Jun 15, 2026` or `Monday Jun 15 prep`.

**New objective:**

> Post-pull catch-up and boot-surface refresh. Re-anchor Prome from Jun 7–8 to Jun 14 state before any new market work. Near gates: BOJ Jun 16, FOMC/VIX expiry Jun 17, TIC/6-18 expiry Jun 18, HAW-11 through Jun 22.

**Sections to include:**
1. `Objective`
   - Finish boot-surface refresh; no agent edits.
2. `Current Regime`
   - Surface tape de-risked / tail-private-physical sticky.
3. `Live Market Levels`
   - Use Phase 0 dashboard anchor.
4. `Today / Next 48h Checklist`
   - Phase 3 edits.
   - Optional: run dashboard again before HEARTBEAT final if edits happen later.
   - Do not do broker/trade optimization unless Will explicitly pivots.
5. `Near Catalyst Slate`
   - Mon Jun 15 Brent double-trigger watch.
   - Jun 16 BOJ.
   - Jun 17 FOMC/VIX expiry.
   - Jun 18 TIC / expiry cleanup.
   - Jun 22 HAW-11 window.
6. `Do / Do Not`
   - Do: route market structure to current owners; mark stale dependencies; preserve verification-required trade rails.
   - Do not: treat CPI/refunding as upcoming; say vol joined stress; execute old 6/18 rails; surface HYG as actionable; edit agents.

**Delete/supersede:**
- Week Prep status table.
- Jun 8–12 catalyst slate.
- Mon 6/8 do/do-not language.
- “Boot surfaces are current” claim.

---

### C. `PROME/STATUS.md`

**Current problem:** says Jun 8 infra session is current; agent table heavily stale.

**Action:** surgical-to-medium rewrite, not necessarily full replacement.

**Update header:**
- `Updated: 2026-06-14 PM ET — post-pull boot-surface refresh Phases 0–2`

**Core State replacement:**
- Operational priority: **boot-surface catch-up after large GitHub pull**, not market optimization.
- Regime: surface de-risked / tail-private-physical sticky.
- Dashboard anchor: Phase 0 levels.

**Sync / Repo State:**
- Repo was clean/synced at Phase 0 (`c87c00ac`, ahead/behind 0/0).
- Current working tree now contains Prome phase-note files:
  - `PROME/BOOT_SURFACE_REFRESH_2026-06-14_PHASE0.md`
  - `PROME/BOOT_SURFACE_REFRESH_2026-06-14_PHASE1.md`
  - `PROME/BOOT_SURFACE_REFRESH_2026-06-14_PHASE2_EDIT_MAP.md`
- No agent files edited.
- Push remains Will-coordinated.

**Prome Boot Surface Trust table:**
Update to something like:

| Surface | Trust | Note |
|---|---|---|
| `PROME/SCRATCH.md` | 🔴 stale Jun 8 | Rewrite Phase 3. |
| `PROME/TODAY.md` | 🔴 stale Jun 7/8 | Replace with Jun 14/15. |
| `PROME/STATUS.md` | 🟠 being refreshed | This file. |
| `PROME/FLEET_SCAN.md` | 🔴 stale Jun 7 | Rewrite from Phase 1 map. |
| `PROME/ACTIVE_DECISIONS.md` | 🟠 stale rails | Needs CPI/refunding/HYG updates; verification-required remains. |
| `HEARTBEAT.md` | 🔴 stale Jun 7 | Rewrite last. |
| Phase notes | ✅ current | Phase 0/1/2 audit trail. |

**Agent / Domain State table:**
Replace current Jun 7/8 table with Phase 1 domain deltas. Suggested compact rows:

- LIQUID ✅ Jun 13: HYG written off; TEN closed; duration oscillation; FOMC/TIC next.
- VIOLET ✅ Jun 14: VIX 17.68 complacency; SKEW bid; Bin-B blocks entry.
- BRENT ✅ Jun 13: physical/price divergence; Brent sub-$90; Path A/B both advancing.
- HAWK ✅ Jun 13: C42/B32/D26; formal Hormuz closure but Brent fell; HAW-11 window.
- SAM 🟠 Jun 14 partial: BOJ live; MOF odds down; pending Ueda/CFTC/carry re-mark.
- CARL ✅ Jun 14: LEN cut; UMich expectations relief; core consumer stress intact.
- LABOR ✅ Jun 14: NFP/revisions strong; claims drift; AI cuts; labor cliff not firing.
- RED ✅ Jun 13: NB 57/conf 70; managed/stagflation co-modal; tape bull-side.
- BROCK 🟠 Jun 8 but still load-bearing: PC gate cascade; macro HY refuses.
- REGINALD 🟠 Jun 8: broad cohort fade retired; WAL idiosyncratic; bank tape green.
- BOND 🟠 Jun 9 superseded in part by LIQUID Jun 13 auction read.
- HENRY 🔴 stale/dark post-CPI; needed for GEX/flip level.
- NEXUS 🔴 stale Jun 8; T-08 useful but needs refresh.
- WALTER 🟠 Jun 10; Iran anchor stale vs Jun 13; routing infra updated.
- OTTO 🟠 infra refresh, domain data stale.

**Current Work Queue:**
Replace with boot-refresh ladder:
1. Phase 3 rewrite `SCRATCH` + `TODAY`.
2. Rewrite `STATUS` and `ACTIVE_DECISIONS`.
3. Rewrite `FLEET_SCAN`.
4. Rewrite `HEARTBEAT` last.
5. Decide phase-note retention/commit.
6. Optional follow-ups: HENRY revival, WALTER Iran anchor refresh, NEXUS fleet scan.

**Rules of Engagement:**
Preserve: no agent edits; no trade execution; pathspec; push Will-coordinated.

**Next Best Action:**

> Execute Phase 3 boot-surface rewrites in approved order; stop before commit/push; verify diff; surface any uncertainty.

---

### D. `PROME/ACTIVE_DECISIONS.md`

**Current problem:** trade rails still anchored to CPI/refunding before they resolved; HYG still indirectly present through old cluster; candidate rows stale.

**Action:** surgical rewrite. Keep short.

**Header:** update to Jun 14.

**Current Mode:**
- Still `Verification Required`, but reason changes:
  - Post-pull catch-up; position/broker truth unreconciled.
  - CPI/refunding gates have passed; do not use pre-CPI rails.
  - LIQUID says HYG $75P is written off / let expire 6/19; stop surfacing as action.

**Live Decision Index revisions:**

1. **TLT Jun 18 $85P + Sep add gate**
   - Change state to `DEFERRED / FOMC-RESOLVER / VERIFICATION_REQUIRED`.
   - Next: do not add from stale CPI/refunding logic. CPI hot occurred but auction results/LIQUID later say duration oscillation, not regime; FOMC 6/17 resolver. Need broker/Will truth before any expiry action.
   - Backstop: before any TLT action / Jun18 expiry.
   - Source add: LIQUID Jun 13 STATUS; RED position reconcile if used.

2. **6/18 theta-killer cluster**
   - Keep, but update:
     - 4 calendar days to expiry as of Jun 14.
     - Old May rails verification-required.
     - HYG leg explicitly dead/written off per LIQUID.
     - BROCK R2.5 monitor: HY OAS 278, still below 285 heads-up; no execution.
     - WAL/TLT actual marks require broker reconciliation.
   - This row should be about **expiry cleanup / reconcile**, not execution trigger.

3. **Separate-clones fleet migration**
   - Keep unchanged but update timing: post-Jun 16/FOMC calm window approaching.
   - Add phase notes: Prome boot-surface refresh is prerequisite; HENRY dark/gex and WALTER anchor may influence migration readiness but not block decision packet.

**Potential new row:**
- `FOMC 6/17 decision framework / cross-domain resolver` as `DRAFT/LOGGED`, owner Prome/RED/LIQUID/HENRY, next = assemble only if Will asks. But caution: ACTIVE_DECISIONS should stay non-terminal decisions, not catalyst list. Consider leaving FOMC in TODAY/HEARTBEAT instead unless there is a concrete Will decision packet.

**Candidate rows cleanup:**
- VIOLET 4/15 adjudication: update to point to VIOLET Jun 14 — no open position, fade gated; not active unless Will asks.
- FXY $58C: promote? It is a real near-expiry Will-held SAM position. But if no broker reconciliation, keep candidate row: `FXY Jun18 $58C salvage — Will decided hold Jun 10 per SAM; verify if needed before expiry`.
- WAL Sep puts remain candidate, not active.
- HYG should not remain candidate/actionable.

---

### E. `PROME/FLEET_SCAN.md`

**Current problem:** Jun 7 scan is stale and should be fully replaced.

**Action:** full rewrite from Phase 1 map.

**New title:** `FLEET_SCAN — 2026-06-14`

**Coverage:**
- Phase 0 dashboard.
- Phase 1 bounded headers.
- Prome-routed outboxes.
- No deep domain research / no agent edits.

**Executive Read:**
Use the canonical frame: surface de-risked, tail/private/physical sticky.

**Top Updates Since Jun 8:**
1. VIX spike faded 21.75/22-ish → 17.68; SKEW stayed bid.
2. HY OAS 278 tight; CCC 956 sticky.
3. Brent sub-$90 while physical stress severe; formal Hormuz closure decoupled from price.
4. LIQUID wrote off HYG, TEN closed; duration oscillation.
5. CARL: LEN guide cut + energy expectations relief; consumer stress intact.
6. LABOR: hard data beat/revisions, claims drift, AI cuts.
7. SAM: MOF odds down, BOJ still live.
8. RED: net bear 57/conf 70, managed/stagflation co-modal.
9. BROCK: PC gate cascade still hot, macro HY refuses.
10. REGINALD: broad cohort bank fade retired; WAL idiosyncratic.

**Prome Surface State:**
List trust states and Phase note checkpoints.

**Agent / Domain Snapshot:**
Use STATUS table content, maybe slightly more narrative.

**Cross-Agent Contradictions / Cautions:**
- Vol complacency vs SKEW/CCC tail.
- Brent tape de-escalation vs physical/chokepoint stress.
- Labor hard-data strength vs consumer-credit deterioration.
- PC substance vs macro HY tightness.
- Bank tape rally vs idiosyncratic WAL/OZK Q2 risk.
- WALTER anchor stale vs HAWK/BRENT.
- HENRY dark for GEX/flip level.

**Top 5 Operational Moves:**
1. Finish boot-surface refresh.
2. Pre-FOMC/FOMC framework only if Will asks; otherwise preserve attention.
3. Track BOJ/SAM and FXY near-expiry state.
4. Refresh HENRY/NEXUS/WALTER anchor after boot surfaces.
5. Position reconciliation pass after boot refresh, separate task.

**Gaps:**
- Broker/fill truth unreconciled.
- HENRY/NEXUS stale.
- WALTER Iran anchor stale.
- OTTO domain stale.
- Dashboard script exits code 1.

---

### F. `HEARTBEAT.md`

**Current problem:** stale root injected regime file. Must be updated last because it compresses final synthesis.

**Action:** full rewrite or heavy surgical rewrite. Recommended: heavy rewrite preserving structure.

**Header:** `Updated: 2026-06-14 ~ET (OpenClaw Prome — post-pull boot-surface refresh)`

**Regime:**
Canonical frame:

> Surface tape de-risked while tail/private/physical stress stayed sticky. Broad cascade is not confirmed; HY OAS remains tight at 278. Vol event spike faded to VIX 17.68, but SKEW stayed bid and CCC remains sticky. Brent collapsed sub-$90 despite formal Hormuz closure and severe physical stress. Banks rallied; WAL/OZK/KRE green. Private credit and consumer balance-sheet stress remain live. FOMC/BOJ/TIC/expiry are near gates.

**Key updates bullets:**
- VIX faded / SKEW held.
- HY OAS 278 / CCC 956.
- Brent sub-$90 / physical-price divergence.
- LIQUID: HYG written off, TEN closed, duration oscillation.
- SAM: BOJ live, MOF odds down.
- CARL/LABOR split: consumer stress vs hard-data labor strength.
- RED re-anchor NB 57/conf 70.
- BROCK: PC Stage 2→3 substance hot; macro HY no confirmation.
- HENRY/NEXUS/WALTER stale dependencies to refresh.

**Stress Dashboard:**
Replace with Phase 0 values.

**Thresholds:**
Update Current column:
- HY OAS 278 [FRED 6/11]
- CCC 956 [FRED 6/11]
- 10Y 4.45 [FRED 6/11]
- TLT 85.77
- Brent 87.33
- Gas 4.15 [6/8]
- USD/JPY 160.18
- VIX 17.68
- SOFR-IORB -0.05 [6/11]
- KRE 73.41
- WAL 83.67
- OZK 52.10
- APO 133.88 (threshold semantics may make it red if >130 ×3 sessions; dashboard says green due config mismatch. Add note: `>130 x4 reassess fired per LIQUID/BROCK context`.)
- ARES 134.90 (likely red/yellow depending config; current table says >132 x3 sessions red, so mark carefully after checking if x3 closes satisfied. Phase 0 dashboard says yellow; do not overstate without close streak verification.)
- BIZD 12.71 (table says $12.50-13 yellow, but dashboard printed red; preserve dashboard red or note config discrepancy.)
- Claims 229k [6/6], shadow 284k
- Continuing 1.795M [5/30]

**Week Ahead:**
Replace Jun 8–12 with Jun 15–22 gates.

**Blocking / Pending:**
New priority table:
- 🔴 Boot-surface refresh Phase 3.
- 🔴 FOMC Jun 17 / VIX expiry stack: framework if Will asks; not auto-trade.
- 🟠 BOJ Jun 16 / FXY near-expiry state.
- 🟠 Jun 18/19 expiry cleanup / position reconciliation; HYG dead, TLT/WAL verify.
- 🟠 WALTER Iran anchor stale vs HAWK/BRENT Jun 13.
- 🟠 HENRY/NEXUS stale post-CPI; refresh after surfaces.
- 🟠 Separate-clones post-Jun16.
- 🔵 Execution-rails design debt.

**Pointers:**
Update:
- Phase notes files.
- Current agent sources.
- Remove `WEEK_2026-06-08` as primary pointer; either archive or mark stale. If creating new week card is part of Phase 3, point to it. If not, say `TODAY.md` owns near gates until new week card exists.

---

## 4. What to Delete / Supersede Across Surfaces

Remove or clearly supersede:
- “Vol joined the stress column” as current statement.
- “HY OAS is sole remaining tape refusal” as sole framing; still important but now paired with vol fade/banks rally/Brent collapse.
- CPI 6/10 and Treasury refunding as upcoming gates.
- BOND matrix v2 pre-Wed action.
- TLT Sep add triggered by CPI/refunding as live pre-event logic.
- HYG as an actionable or salvageable position.
- “Boot surfaces are current” claims from Jun 7/8.
- Any “11 days to expiry” / old countdown language.
- Broad bank cascade language; REGINALD narrowed to idiosyncratic WAL/OZK.
- Labor cliff language unsupported by NFP/revisions.

---

## 5. What to Preserve

Preserve:
- No broad cascade until HY OAS confirms.
- PC/private-credit Stage 2→3 substance remains hot.
- Tail stress: CCC sticky + SKEW bid.
- Consumer-credit stress and SAVE Jul 1 drag.
- Japan/BOJ risk and FXY near-expiry relevance.
- HAW-11/T-08 correlated-fragility as awareness, not trade rail.
- Position/broker reconciliation still separate and required.
- Push is Will-coordinated; pathspec only.
- No agent edits unless Will explicitly approves.
- Separate-clones post-Jun16 as structural fix.

---

## 6. Open Questions Before Phase 3 Edits

No blocking questions, but these should be surfaced to Will:

1. **Phase notes retention:** Keep Phase0/1/2 files as audit trail, archive them after refresh, or delete after their conclusions are folded into boot surfaces?
2. **New week card:** Should Phase 3 create `PROME/action-cards/WEEK_2026-06-15.md`, or should `TODAY.md` carry near gates for now?
3. **WALTER Iran anchor:** After boot surfaces, should Prome request/route WALTER anchor refresh instead of relying on HAWK/BRENT deltas?
4. **HENRY/NEXUS refresh:** After boot surfaces, should Prome spawn/route refresh tasks for HENRY/NEXUS, or wait until Will asks around FOMC?
5. **Position reconciliation:** Treat as separate future phase unless Will pivots. Do not combine with boot refresh.

Recommendation:
- Keep phase notes until Phase 3 is complete; then either commit as audit trail or archive under a dated `PROME/archive/` subdirectory if needed.
- Create a new week card only if Phase 3 has enough time; otherwise update `TODAY.md` and `HEARTBEAT.md` first.

---

## 7. Recommended Phase 3 Edit Order

Best order to minimize context drift:

1. **`PROME/TODAY.md`** — fastest stale-risk removal; new near-gate operator card.
2. **`PROME/SCRATCH.md`** — session handoff / phase state. Could also be first; either is fine.
3. **`PROME/STATUS.md`** — operational + fleet trust table.
4. **`PROME/ACTIVE_DECISIONS.md`** — trade rails verification-required / stale logic cleanup.
5. **`PROME/FLEET_SCAN.md`** — fleet synthesis after STATUS/decisions are coherent.
6. **`HEARTBEAT.md`** — regime compression last.
7. Optional **new week card** if Will wants durable calendar artifact.
8. Verify: `git diff --stat`, read updated headers, run compact dashboard if needed.

Important: Do not edit `AGENTS/*` in Phase 3 unless Will explicitly changes the constraint.

---

## 8. Minimal Phase 3 Success Criteria

Phase 3 is successful if:

- No boot surface says Jun 8–12 catalysts are upcoming.
- No surface claims “vol joined stress” as current regime.
- Current dashboard levels are stamped with as-of dates.
- HYG is not surfaced as actionable.
- Old 6/18 trade rails are explicitly verification-required.
- HENRY/NEXUS/WALTER stale dependencies are labeled.
- Near gates are BOJ/FOMC/VIX expiry/TIC/expiry cleanup/HAW-11, not CPI/refunding.
- No agent files are edited.
