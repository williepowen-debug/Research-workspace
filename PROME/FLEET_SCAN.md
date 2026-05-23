# FLEET_SCAN — 2026-05-23

**Scanner:** fleet-scanner-2026-05-23 (subagent of Prome)
**Coverage:** active `AGENTS/*/STATUS.md` heads, inbox counts, recent commits, PROME state files, HEARTBEAT, live dashboard compact.
**Read budget:** first ~30 lines per STATUS; `git log` recency; inbox/outbox/file-presence scans for Jun18 calibration; no domain-agent files edited.
**Heavy reads delegated; this file is Prome's working surface.**

## Executive Read

The 5/22 GitHub pull materially refreshed the fleet: HAWK was consolidated into an **armed-pause / controlled-grind** frame, CARL recovered from the crash and committed its closeout, WALTER pushed a high-volume triage day, BRENT added Friday data, OTTO completed a P0 sweep, and SENTRY feed updates landed 5/23. The orchestral state is cleaner than the old 5/18 scan, but the decision layer is now concentrated in one live execution item and one missing-calibration loop.

**Live tape from 5/23 boot dashboard:** HY OAS **278bps [5/21]** · CCC **939bps [5/21]** · Brent **$103.54** · USD/JPY **159.15** · WAL **$78.59** · KRE **$69.37** · TLT **$84.68** · BIZD **$12.38** · VIX **16.70**. Public credit/vol still refuse cascade confirmation; stress remains duration/energy/FX/BDC concentrated.

**Most important operational fact:** `PROME/action-cards/TLT_JUN18_DECISION_2026-05-22.md` is **Will-approved but unexecuted**. No broker action occurred after approval because of the crash. Monday 5/25 is closed; earliest execution is **Tuesday 5/27 open**, subject to C1–C5 guardrails.

## 1. Health Table

> Inbox count = files currently in top-level `inbox/`. Commit recency uses latest git commit touching the agent dir; route-only / cross-agent commits are not always domain-owned, so read the note column.

| Agent | STATUS freshness | Latest commit touching dir | Inbox | Position relevance | Catalyst / note |
|---|---:|---|---:|---|---|
| **PROME** | 5/22 | 5/21 path-touch; 5/22 PROME closeout exists in repo history | 2 | 🔴 execution rails | TLT action card approved/unexecuted; Jun18 v0.2 pending |
| **WALTER** | 5/22 | 5/22 `10340be4` | 1 | 🟠 routing | 5/22 heavy triage: 9 cluster_mediating + 2 counter_evidence; signal-routing owner |
| **HAWK** | 5/22 | 5/22 `63824328` | 0 | 🟠 kinetic → Brent | May 23 close recheck due: if no Gulf/framework text, mark hold expired → May 25-29 grind/re-ratchet pressure |
| **BRENT** | 5/20 | 5/22 `c2b7949b` | 4 | 🔴 energy shock | Friday data landed; Brent still >$100 red but off peak |
| **CARL** | 5/22 | 5/22 `7a18ddbf` / `5e5f981b` | 0 | 🟠 consumer/auto | Crash recovery committed; no longer showing inbox backlog |
| **OTTO** | 5/22 | 5/22 `1d2e4ace` | 0 | 🟡 auto/ABS | First Brands public outcome still recheck; Wilmington full-exit thesis weakened |
| **REGINALD** | 5/21 | 5/21 PROME-authored SIG commit | 8 | 🔴 WAL/KRE/EGBN | Jun18 calibration reply still missing; V2.2 Bear-medium dominant remains live |
| **BROCK** | 5/21 | 5/21 PROME-authored SIG commit | 4 | 🔴 BDC/private credit | Jun18 calibration reply still missing; BIZD $12.38 red, HY OAS benign |
| **HENRY** | 5/21 | 5/21 `0fa03ced` | 1 | 🔴 TLT/duration | PROME artifacts record 5/22 TLT reply; reply file itself not present in current HENRY outbox after pull |
| **VIOLET** | 5/21 | 5/21 `4bb1932d` | 1 | 🟠 vol clock | R11 clock window 5/28-6/02; VIX 16.70 still not transmitting |
| **NEXUS** | 5/21 | 5/22 HAWK path-touch | 2 | 🟠 synthesis | Stage-2-late divergence reset fresh; next synthesis after Jun18/HAWK updates |
| **LIQUID** | 5/20 | 5/22 HAWK path-touch | 2 | 🔴 funding/duration | HY OAS 278 still 18bps above 260 kill; TLT red; duration channel live |
| **BOND** | 5/20 | 5/21 `c6dc9b2d` | 1 | 🟠 auctions/TLT | June 9-11 nominal 10Y matrix deployment is next hard test |
| **SAM** | 5/21 | 5/21 `a5852d99` | 7 | 🟠 Japan/FXY | USD/JPY 159.15 intervention zone; Sep $60C proposal still pending cheaper entry |
| **RED** | 5/21 | 5/22 HAWK path-touch | 1 | 🔴 adversarial | Instrument-timeline mismatch is central; do not spawn persistent RED |
| **LABOR** | 5/04 | 5/17 route commit | 9 | 🟠 labor credit chain | Claims remain green; not front-of-queue unless labor breaks |
| **OZK** | 4/24 | 4/24 `83d7348b` | 1 | 🔴 OZK puts | Position hygiene stale; not acute vs TLT/Jun18 rails |
| **SHADE** | 3/26 | 5/10 route commit | 8 | 🟠 PE-insurer | Defer unless APO/PE-captive thread reopens |
| **ZHAO** | 4/02 | 5/22 HAWK path-touch | 9 | 🟡 China/Japan adjunct | Stale but not urgent before TIC/China catalyst |
| **MARCO / HANS** | 4/23-4/30 | 4/30 | 0 / 2 | 🟡 indirect | Defer |
| **SENTRY** | 5/09 | 5/23 `057469d2` | 0 | 🟡 infra | Feed update landed today; operational |
| **ORACLE / CRUISE / FERT / ATHENA** | 4/01 or older | old | 0-1 | 🟢/🟡 | Dormant/defer |

## 2. Stale Agents — Decision Needed

| Agent | Why it matters now | Recommendation |
|---|---|---|
| **REGINALD** | Direct owner of KRE/WAL/EGBN Jun18 roll triggers; inbox has 8 files and no observed Jun18 calibration reply in current outbox scan. | **Do not spawn** (persistent). Track missing reply until 5/24 EOD default-pass; consolidate v0.2 with/without it. |
| **BROCK** | Direct owner of HYG / public-credit / BDC trigger language; BIZD is red while HY OAS is still benign. No Jun18 calibration reply found. | **Do not force domain work yet.** Default-pass at 5/24 EOD unless BROCK replies. |
| **HAWK** | May 23 close recheck is due on the Gulf/framework hold. | **Update state only after recheck.** If no framework, label hold expired and shift to May 25-29 grind/re-ratchet watch. |
| **TODAY.md / CALENDAR.md** | `TODAY.md` is still Sunday May 17; calendar context is stale relative to TLT 5/27, HAWK 5/23, VIOLET 5/28-6/02, Jun18. | Refresh after TLT/Jun18 rails are stabilized; do not let stale date surface to Will. |
| **OZK / SHADE / ZHAO / LABOR** | Stale but lower immediate position/timing pressure. | Defer; avoid completionism. |

## 3. Open Proposals / Decisions Awaiting Will

| Date | Artifact / agent | Decision | Status |
|---|---|---|---|
| 2026-05-22 | `PROME/action-cards/TLT_JUN18_DECISION_2026-05-22.md` | Sell 3 × TLT Jun18 $85P; buy 1 × TLT Sep19 $85P | ✅ **Approved; unexecuted pending Tue 5/27 open** |
| 2026-05-22 | `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` | Approve v0.2 trigger rails for HYG/EGBN/WAL/KRE cluster | 🟠 v0.1; BROCK + REGINALD calibration missing; HENRY leg converted to TLT action card |
| 2026-05-21 | SAM | Sep18 $60C × 5-10 contracts | 🟠 pending post-CPI cheaper entry |
| 2026-05-21 | FORGE rehab carry | FXY $58C reconciliation; TLT $88P May15 disposition unknown; APD long thesis tag | 🟡 needs portfolio reconciliation, not domain analysis |
| 2026-04/05 | VIOLET trade adjudication | 4/15 VIX/SKEW trade 60d window | 🟡 closes ~6/12 |

## 4. Upcoming Catalysts (next 14 days)

| Date | Catalyst | Owner | Readiness |
|---|---|---|---|
| **Sat 5/23 close** | HAWK Gulf/framework recheck | HAWK / Prome | 🟠 due now |
| **Sun 5/24 EOD** | BROCK + REGINALD Jun18 calibration default-pass deadline | Prome + domain agents | 🔴 missing replies as of local inbox/outbox scan |
| **Mon 5/25** | Memorial Day market holiday | Prome / Will | ✅ no TLT execution window |
| **Tue 5/27 open** | TLT approved roll execution earliest window | Will executes; Prome logs | 🔴 highest operational priority |
| **Wed-Fri 5/28-6/02** | VIOLET/HENRY R11 analog clock window | VIOLET / HENRY | 🟠 R11 clock running; VIX still calm |
| **Fri 6/06 EOD** | TLT 6/06 HENRY time backstop | HENRY / Prome | 🔴 if not executed/if guardrails fire |
| **Jun 9-11** | BOND matrix v2 nominal 10Y deployment | BOND / LIQUID / HENRY | 🟠 rescheduled from TIPS misread |
| **~Jun 12** | VIOLET 4/15 trade 60d adjudication | VIOLET / Prome | 🟡 |
| **Jun 16 close** | Jun18 cluster hard backstop | Prome / Will | 🔴 no-trigger = let expire |
| **Jun 18** | Expiry cluster + AOCI comment close/FOMC window nearby | Prome / agents | 🔴 |

## 5. Cross-Agent Contradictions / Red Flags

**Substance still bearish; tape still refuses transmission.** BROCK/REGINALD/HENRY/VIOLET/NEXUS all point to Stage-2-late divergence or trap dynamics, but live tape says HY OAS **278 [5/21]**, VIX **16.70**, WAL **78.59**, KRE **69.37**. That is not all-clear; it is a constraint against broad cascade adds and a warning that June theta can die before thesis realization.

**Duration is the paying channel, not credit.** TLT is red at **84.68**, 10Y remains red, and the TLT Jun winner is the only 6/18 cluster sub-leg with actual salvage value. This is why the approved TLT card is more urgent than the lower-premium HYG/WAL/KRE dead-stack.

**Artifact integrity note:** PROME action card + TRADE_DECISIONS record HENRY's 5/22 TLT reply and Will approval. The referenced `AGENTS/HENRY/outbox/REPLY-PROME-2026-05-22-tlt-decision.md` and 5/22 HENRY inbox SIG are not present in the current filesystem after pull (likely untracked/not pushed in the crash window). Treat PROME action card + TRADE_DECISIONS as canonical unless HENRY later reconstructs its own outbox.

**Calendar-state risk:** `TODAY.md` still says Sunday May 17. This is operationally dangerous if surfaced unfiltered; do not quote it as current.

## 6. Top 5 Moves (ranked by orchestral rubric)

1. 🔴 **Prepare Tuesday 5/27 TLT execution check + post-fill logging path** — score **19.5**
   *Owner: Prome/Will. Approved but unexecuted trade is a live operational gap. Before Tuesday open: rerun dashboard/price, test C1-C5, then Will places orders if still valid. After fills: update FORGE/STATUS, TRADE_DECISIONS, action card.*

2. 🔴 **Jun18 trigger-set v0.2 consolidation by 5/24 EOD default-pass** — score **17.0**
   *Owner: Prome. BROCK + REGINALD replies are still missing; HENRY leg already became TLT action card. Consolidate either with late replies or explicit default-pass assumptions so Will can approve rails before theta cliff.*

3. 🔴 **HAWK May 23 close recheck** — score **14.5**
   *Owner: HAWK/Prome. If no Gulf/framework text, update orchestral state to “hold expired without framework; May 25-29 grind/re-ratchet pressure active.” This affects Brent/HENRY/NEXUS framing but is not a trade by itself.*

4. 🔵 **Refresh TODAY.md / catalyst surface after the above three are stabilized** — score **12.0**
   *Owner: Prome. TODAY.md is May 17 stale and now missing TLT 5/27, VIOLET 5/28-6/02, Jun18 rails. Do after live execution/catalyst items so it doesn't become another stale rewrite.*

5. 🔵 **NEXUS/RED-style divergence synthesis after Jun18 v0.2 + HAWK recheck** — score **11.5**
   *Owner: NEXUS or Prome summary. The question is not “is stress real?” but “does realization beat theta?” Needs TLT/Jun18/HAWK inputs first.*

**Bench / defer:** CARL recovery appears committed and inbox cleared; OZK/SHADE/ZHAO/LABOR stale states are real but lower position/time pressure. Do not let hygiene crowd out TLT + Jun18 rails.

## 7. Open Loops

| Loop | Status | Next action |
|---|---|---|
| TLT action card | ✅ approved / ❌ unexecuted | Tue 5/27 pre-open condition check; Will broker execution if valid; Prome logs fills |
| BROCK Jun18 calibration | Missing as of local inbox/outbox scan | Wait until 5/24 EOD, then default-pass or integrate reply |
| REGINALD Jun18 calibration | Missing as of local inbox/outbox scan | Same as BROCK |
| HENRY TLT reply artifact | PROME has canonical decision record; HENRY outbox file absent after pull | Do not block execution; HENRY can reconstruct on next boot if needed |
| HAWK May 23 recheck | Due | Reclassify hold if no framework text by close |
| TODAY.md | Stale May 17 | Refresh after urgent loops |
| CARL crash recovery | Latest commits landed; inbox 0 | No Prome action unless CARL flags residual tmp/dirty state later |
| FORGE trigger set | v0.1 draft | v0.2 after calibrations/default-pass; Will approval gate |
