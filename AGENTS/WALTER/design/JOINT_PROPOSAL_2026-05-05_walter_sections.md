# JOINT_PROPOSAL — WALTER sections — 2026-05-05/06

*WALTER-drafted sections of the **3-way joint proposal** from WALTER ↔ CARL LIAISON (Turns 1-7, 2026-05-05 → 06) and WALTER ↔ BRENT LIAISON (Turns 1-4, 2026-05-05 → 06). CARL drafts §1 (context) + §3a (Post_Hoc_Conf shipped) + §3c (DATA_RELEASE_CALENDAR) + §4 (locked decisions). BRENT drafts §1-coda + §2e (BRENT cosign + lng_substitution rationale) + §4-coda. WALTER drafts §2a + §2b + §2c + §2d + §3b + §3d. Final stitch lives at repo-root `design/JOINT_PROPOSAL_2026-05-06_walter_carl_brent.md` — WALTER stitches when all 3 per-agent files land.*

---

## SECTION 2a — FORMAT_SPEC v0.8 (4 field additions, co-signed CARL+BRENT+WALTER)

**Status:** Drafted, awaiting Will sign-off. Co-signed by CARL (LIAISON Turn 5: "Pre-cosign FORMAT_SPEC v0.8 on my side: confirmed"). Co-signed by BRENT (LIAISON Turn 3: "BRENT cosigns" with `lng_substitution` enum extension). Three-way pre-cosign.
**Cost:** $0 (structural-only, all fields optional).
**Origin:** CARL LIAISON Turns 1-4 (Q1, Q6, Q9, Q15 → initial v0.8 enum); BRENT LIAISON Turns 1-3 (Q2 → `lng_substitution` extension; `refining_margin_pass_through` push-back accepted).
**Files affected:** `AGENTS/WALTER/design/SIGNAL_FORMAT_SPEC.md` (canonical), `SIGNAL_PROCESSING_CHECKLIST.md` (Phase 2 cluster/role/lens/transmission tagging step), `ROUTING_TABLE.md` (mechanic-aware routing).

### 2a.1 — `consumer_transmission` (optional enum, header field)

**Purpose:** Tag the transmission mechanism through which a signal reaches CARL's consumer-stress thesis (or transmits energy → consumer through BRENT-side outbound). Allows CARL to batch-fold same-mechanism signals at boot rather than disposition each individually.

**Final v0.8 enum (9 values):**
```
pump_pass_through       — oil/gas → retail pump → CPI energy → consumer-burden
wage_pressure           — labor data → wage growth / employment cost index
wealth_effect           — equity-portfolio-driven (top 40%) → discretionary spend
policy_pass_through     — tariff / regulatory / fiscal → consumer-cost / income
discretionary_demand    — observation-side demand-destruction (restaurants, theme parks, cruise, leisure travel)
services_export         — international-inbound demand (US-tourism-receipts, hospitality-foreign)
lng_substitution        — LNG redirect → US/EU gas prices → heating-fuel substitution (BRENT-Turn-1 extension)
counter_evidence        — within-cluster counter-thesis data
none                    — no consumer-stress transmission, info-only for cluster context
```

**Push-back trail (Q-trail):** BRENT Turn 1 originally proposed two extensions: `lng_substitution` AND `refining_margin_pass_through`. WALTER Turn 2 accepted `lng_substitution` (genuinely distinct mechanism — heating-fuel substitution, not vehicle-pump) and pushed back on `refining_margin_pass_through` (subset of `pump_pass_through` — refining margin → wholesale → retail pump is the dominant pathway, folds in dispatch_note prose). BRENT Turn 3 accepted push-back: "compositional, not mechanical — mea culpa." Final 9-value enum locked.

**Today's signals retagged:**
- `-001` IEA crude inventory → `pump_pass_through`
- `-002` IEA LNG → `lng_substitution` (re-tagged from `pump_pass_through` per v0.8 enum lock)
- `-003` EIA US gasoline decade-low → `pump_pass_through`
- `-006` ISM Services + JOLTS → `wage_pressure` (multi-axis MACRO+LABOR)
- `-007` Factory Orders counter → `counter_evidence`
- `-008` AHLA WC hotel → `services_export`
- `-009` Wirth Milken → `pump_pass_through` (via refining-margin component, prose tag)
- `-010` Black Box restaurants → `discretionary_demand`
- `-012` Brent tape divergence → `pump_pass_through` (cluster-mediating, see signal_role)

### 2a.2 — `signal_role` (optional enum, header field)

**Purpose:** Tag the role a signal plays within its cluster's narrative. Distinguishes substance-data from interpretive-mediating signals.

**Enum values (4):**
```
primary_substance       — direct data event/observation (e.g., -006 ISM print)
cluster_mediating       — interpretive layer affecting cluster narrative (e.g., -012 Brent tape vs cluster-substance divergence)
counter_evidence        — within-cluster counter-thesis (e.g., -007 Factory Orders vs stagflation thesis)
thesis_confirmation     — explicit thesis-validating signal
```

**Authoritative-voice precedence on cluster_mediating signals:** NEXUS > WALTER (tagger) > action-primary (data substance locally). NEXUS owns cluster-narrative-update interpretation; WALTER applies the tag based on cross-cluster observation; action-primary interprets data-substance-locally without authoritatively rewriting cluster narrative. (See CARL LIAISON Turn 4 Q16 + BRENT LIAISON Turn 2 Q3 for full precedence rule.)

**Substance/narrative line (BRENT LIAISON Turn 2 → Turn 3):** "if you can defend the read with a workbook citation (KB-AGT-NNN, FLOW-AGT-X.YY), it's substance — write authoritatively. If it's cross-cluster narrative ('market is pricing scenario B over A'), it's narrative — flag pending NEXUS." Action-primary writes substance authoritatively; narrative-interpretation gets `[AGT-placeholder-narrative pending REQ-NEXUS-{date}]` tag in dispatch_note or BOARD_LOG Notes until NEXUS spawns.

### 2a.3 — `consumer_lens` (optional enum, header field)

**Purpose:** Codify the K-shape framing distinction for consumer signals. Different routing/disposition paths.

**Enum values (4):**
```
tier_stratified         — discretionary pullback in mid-tier with top-decile counter-channels intact (today's -010 Black Box pattern)
broad_collapse          — multi-tier consumer demand destruction (would route CARL primary action immediately)
mixed                   — multi-axis with no clear K-shape signal (today's -006 demand cooling + labor absorbing)
counter                 — counter-evidence to consumer-stress thesis (today's -007 Factory Orders beat)
```

(BRENT noted Turn 1: "doesn't apply to BRENT-side dispatches" — energy-cluster signals typically don't carry `consumer_lens`; only consumer-cluster signals do.)

### 2a.4 — `cluster_secondary` (optional, comma-separated)

**Purpose:** Multi-cluster signals tag a primary cluster (per CLUSTER_TAXONOMY substance > mechanism > action-recipient resolution rule) AND optionally one or more secondary clusters for cross-cluster visibility.

**Order convention** (CARL Turn 5): primary by substance, secondary comma-separated by **descending action-relevance for routed agents**.

**Example:** Future CMBS multifamily delinquency print:
```
cluster: BANK_COLLATERAL
cluster_secondary: HOUSING_PRICES, CONSUMER_STAGFLATION
```
Primary discoverability preserved (signal lands in BOARD INDEX BANK_COLLATERAL section). Secondary tags drive batch-folding at recipient boot — CARL diffs by `cluster_secondary` containing `CONSUMER_STAGFLATION` and folds.

### 2a.5 — Updated header schema example (post-v0.8)

```yaml
---
signal_id: SIG-W-20260601-001
precedence: PRIORITY
timestamp: 2026-06-01T09:30:00Z
source: WALTER
origin: "..."

to: REGINALD (ACTION)
info: CARL, BROCK, RED, NEXUS
group: CREDIT_CHAIN

signal_type: threshold-crossed
signal_role: primary_substance       # NEW v0.8
confidence: 0.85
confidence_language: reports
resources: 1
safety_net: clear

word_count: 280

cluster: BANK_COLLATERAL
cluster_secondary: HOUSING_PRICES, CONSUMER_STAGFLATION    # NEW v0.8 (optional)
consumer_transmission: discretionary_demand                # NEW v0.8 (optional)
consumer_lens: tier_stratified                             # NEW v0.8 (optional)
---
```

### 2a.6 — Migration / backwards compatibility

- All four fields are **optional** for pre-v0.8 historical signals (most don't carry them).
- For new signals dispatched 2026-05-06 onward: WALTER tags `cluster_secondary` and `signal_role` always when applicable; `consumer_transmission` and `consumer_lens` only when CARL is on the routing line; energy-cluster signals carry `consumer_transmission` only when consumer-side info recipient is on the routing line.
- BOARD INDEX section structure unchanged (primary-cluster-only); no INDEX migration required.
- BOARD_LOG.tsv schema (CARL + BRENT) unchanged on these fields — recipients read them out of signal headers when dispositioning.

### 2a.7 — Q-trail

- CARL LIAISON Q1 / Q6 / Q9 / Q15 (CARL→WALTER) → WALTER Turn 4 PROPOSAL → CARL Turn 5 ACCEPT (with `discretionary_demand` + `services_export` enum extension and `cluster_secondary` order convention).
- BRENT LIAISON Q2 (BRENT→WALTER, Turn 1) → WALTER Turn 2 ACCEPT `lng_substitution` + PUSH-BACK `refining_margin_pass_through` → BRENT Turn 3 ACCEPT push-back, full 9-value enum locked.

---

## SECTION 2b — Scheduled lightweight scan workflow

**Status:** Drafted, awaiting Will sign-off (cost-budget call).
**Cost:** ~$0.30-0.50/wk recurring for CARL-primary; ~$0.40-0.60/wk additional for BRENT-primary if BRENT calendar lands. Total $0.70-1.10/wk if both. Hard cap $1.50/wk.
**Origin:** CARL LIAISON Q8 (CARL→WALTER) → WALTER Turn 4 PROPOSAL → CARL Turn 5 STRONGLY WANTS. BRENT LIAISON Turn 1 noted likely BRENT-side calendar extension post-back-disposition pass.
**Files affected:** WALTER cron-equivalent (no specific file yet — first implementation), reads `AGENTS/CARL/DATA_RELEASE_CALENDAR.md` (CARL self-task this week) + `AGENTS/BRENT/workbook/DATA_RELEASE_CALENDAR.md` (BRENT self-task post-back-disposition pass).

### 2b.1 — Problem

CARL's primary-data sources (NY Fed HHDC, BLS CPI/PPI/PCE/JOLTS/NFP, Freddie PMMS, AAA pump price, ABS 10-D filings) currently bottleneck on CARL's own session frequency. Refresh staleness is 5-15 days. Today (-006 ISM/JOLTS) caught the BLS releases via Daly Asset Management aggregator pickup — not via my own scheduled pull. Real gap.

BRENT's primary-data sources (EIA WPSR Wednesdays, Baker Hughes Fridays, OPEC MOMR monthly, IEA OMR monthly, CFTC COT Tuesdays, Platts Dated Brent daily) similar bottleneck. BRENT pulls primary-source on session boots; scheduled-scan workflow would tighten the loop.

### 2b.2 — Mechanism

- WALTER cron-equivalent reads `AGENTS/CARL/DATA_RELEASE_CALENDAR.md` + `AGENTS/BRENT/workbook/DATA_RELEASE_CALENDAR.md`.
- Calendar columns: `Date | Time (ET) | Source | Release | Cadence | Vector | Notes` (CARL Turn 5 accept; BRENT mirrors).
- Cron fires lightweight Sonnet scan ~1h before each release, then again ~5 minutes post-release.
- Pre-release scan: confirm release-day-of, prepare verify-research framework. Post-release scan: pull primary-source numbers, dispatch to action-primary within minutes.

### 2b.3 — Coverage estimate

**CARL-side (~5-7 active scans/week):**
- BLS CPI/PPI/PCE/JOLTS/NFP: ~5 monthly releases × 12 = ~60/yr
- Freddie PMMS: ~52/yr (1/wk Thursday)
- AAA pump: ~365/yr daily (could batch into weekly during normal regime, daily during Iran-cluster regime)
- ABS 10-D: variable, ~2-4/month
- NY Fed Q1 HHDC: 4/yr (quarterly)
- ISM Services + Manufacturing, Empire/Phila Fed, Conference Board CCI, Initial Claims, retail sales, UMich preliminary + final ≈ ~15 monthly + ~52 weekly

**BRENT-side (~3-5 active scans/week):**
- EIA WPSR: ~52/yr (1/wk Wed)
- Baker Hughes rig count: ~52/yr (1/wk Fri)
- OPEC MOMR: ~12/yr (monthly)
- IEA OMR: ~12/yr (monthly)
- CFTC COT: ~52/yr (1/wk Tue)
- Platts Dated Brent / 3:2:1 crack: daily but lightweight enough to fold into existing data tools

**Total: ~8-12 active scans/week.**

### 2b.4 — Cost projection

- Per-scan: ~$0.05 (Sonnet, 1-2 tool uses, primary-source pull + verify-research lite)
- CARL weekly: $0.30-0.50
- BRENT weekly: $0.20-0.40
- Total weekly: $0.50-1.00
- Annual: ~$25-50/year

### 2b.5 — Deliverable

Dispatched signals to CARL or BRENT with `signal_role: primary_substance` + `consumer_transmission: <mechanism>` (CARL-side) or `energy_transmission: <mechanism>` (BRENT-side, post-v0.9) tags within minutes of release. Tightens refresh from "5-15 days behind" → "2-3 days behind" (depending on agent boot cadence per Q5 decision).

### 2b.6 — Kill-trigger

Scrap the workflow if any of:
- (a) Monthly cost overrun >2× budget (>$8/month sustained for 2 consecutive months)
- (b) Signal-quality degradation (false-positive rate >20% on dispatched scans, measured by `Post_Hoc_Conf` deltas)
- (c) Recipient-agent feedback that auto-pushed signals are net-noise (3+ consecutive INFO_ONLY-or-REFERRED dispositions on auto-pushed signals indicates wrong calibration)

### 2b.7 — Q-trail

- CARL LIAISON Q8 (CARL→WALTER) → WALTER Turn 4 PROPOSAL → CARL Turn 5 STRONGLY WANTS.
- BRENT LIAISON Turn 1 noted scheduled-scan extension to BRENT-primary calendar likely; BRENT Turn 3 confirmed self-task ETA post-back-disposition pass.

---

## SECTION 2c — BRENT-IMMEDIATE threshold-cross dispatch list (NEW from BRENT LIAISON)

**Status:** Drafted, awaiting Will sign-off. BRENT proposed Turn 1; WALTER redlined Turn 2 (#5 PRIORITY-not-IMMEDIATE, #6 dual-extremum); BRENT accepted Turn 3 with refinements (#5 ≥2× trailing 30-day median operational definition, #6 single-day ≥$50 inverse trigger); WALTER locked Turn 4.
**Cost:** $0 (routing-rule update). Detection logic exists (FORGE/tools/market-data + EIA scheduled scans).
**Origin:** BRENT LIAISON Q4 (BRENT→WALTER, Turn 1) → WALTER Turn 2 ACCEPT-WITH-REDLINES → BRENT Turn 3 ACCEPT-WITH-REFINEMENTS → WALTER Turn 4 LOCK.
**Files affected:** `AGENTS/WALTER/design/ROUTING_TABLE.md` (new "By Boundary Threshold" section, parallel to "By Signal Domain" + "By Signal Type"), `AGENTS/BRENT/workbook/PREDICTIONS.tsv` (BRT-04 / BRT-08 / BRT-15 cross-refs).

### 2c.1 — 8-row threshold list (locked Turn 3 → Turn 4)

| # | Threshold | Precedence | Routing | Cadence |
|---|-----------|------------|---------|---------|
| 1 | Brent close ≥$120 sustained 3 sessions | IMMEDIATE | BRENT-primary; info CARL/HENRY/LIQUID/SAM/HAWK/RED | 2-3 sess sustained = dispatch |
| 2 | Brent close ≤$75 sustained 3 sessions | IMMEDIATE | BRENT-primary; info CARL/HENRY/LIQUID/RED | 2-3 sess sustained = dispatch |
| 3 | Cushing <20M bbl single print | IMMEDIATE | BRENT-primary; info LIQUID/HENRY/RED | Single print = dispatch (operational minimum, WTI dislocation risk) |
| 4 | HY Energy OAS >400bps | IMMEDIATE | BRENT-primary; info LIQUID-cross-feed (LIQUID may want primary depending on broader-credit context — flag at dispatch) | 2-3 sess sustained = dispatch |
| 5 | VLCC Worldscale ≥2× trailing 30-day median sustained | PRIORITY | BRENT-primary; info HAWK/SAM/RED | Sustained-cross-from-baseline (≥3 sess) — operational definition avoids absolute-threshold drift in war-risk-elevated baseline |
| 6 | Gasoline crack — re-cross from <$30 back ≥$30 OR single-day spike ≥$50 | IMMEDIATE | BRENT-primary; info CARL/HENRY/RED | Threshold-cross logic only; standing $42 baseline = no fresh dispatch. Inverse extremum captures demand-destruction-via-crack-collapse OR refinery-substitution-exhausted scenarios |
| 7 | US oil rigs +50 from 408 trough | PRIORITY | BRENT-primary; info CARL (capex/wage)/HENRY/RED | 2-3 sess sustained = dispatch |
| 8 | Brent 3:2:1 crack >$50/bbl | IMMEDIATE | BRENT-primary; info CARL (refining-margin pass-through)/HENRY/REGINALD (refinery-bank) | 2-3 sess sustained = dispatch |

### 2c.2 — Cadence convention (locked)

- **Single-day breach** = watch (no dispatch)
- **2-3 sessions sustained** = dispatch
- **Single-print operational minima** (#3 Cushing): dispatch on the print itself
- **Re-fire convention:** after initial cross, no re-fire on continued state; only on re-cross of boundary in either direction. Sustained-above-#1 stays one signal until it falls back below or escalates further to a higher threshold

### 2c.3 — Detection responsibility

- **WALTER:** monitors price/spread/inventory data via FORGE/tools/market-data + EIA/Baker Hughes scheduled scans (per §2b)
- **BRENT:** mirrors via own data tools and STATUS refresh
- **Convention:** BRENT-fire-as-primary on threshold-cross dispatches; WALTER-fire-as-fallback if BRENT stale (>5d STATUS lag)

### 2c.4 — Adds to ROUTING_TABLE

New "By Boundary Threshold" section (parallel to existing "By Signal Domain" + "By Signal Type"). Threshold-cross signals carry `signal_type: threshold-crossed` + `cluster: IRAN_HORMUZ` (or successor cluster post-Phase-2) + boundary-row reference in dispatch_note (e.g., `boundary: §2c-row-1`).

### 2c.5 — Q-trail

- BRENT LIAISON Q4 (BRENT→WALTER, Turn 1, 8-row list proposed) → WALTER Turn 2 ACCEPT-WITH-REDLINES (#5 PRIORITY-not-IMMEDIATE; #6 standing-state-not-fresh-dispatch) → BRENT Turn 3 ACCEPT (with #5 ≥2× median definition + #6 dual-extremum >$50 inverse trigger) → WALTER Turn 4 LOCK.

---

## SECTION 2d — BURST_WINDOW protocol (NEW from BRENT LIAISON)

**Status:** Drafted, awaiting Will sign-off. BRENT raised need Turn 1 Q5 (LESSONS #11/#16 — price collapses Day 3-8 of announcement; slow dispatch cadence misses 80% of move); WALTER drafted Turn 2 (state machine + threaded Telegram); BRENT refined Turn 3 (BRENT-declares-open / WALTER-declares-close); WALTER codified Turn 4 + answered Q15 cost-asymmetry.
**Cost:** $0 base; ~$0.05-0.20 per false-positive window declaration (bounded operational cost).
**Origin:** BRENT LIAISON Q5 (BRENT→WALTER, Turn 1) → WALTER Turn 2 PROPOSAL → BRENT Turn 3 ACCEPT-WITH-REFINEMENT (asymmetric declaration) → WALTER Turn 4 STATE-MACHINE-LOCK.
**Files affected:** `AGENTS/WALTER/design/FILTER_SPEC.md` (new sub-section under Tuning Rules), `SIGNAL_PROCESSING_CHECKLIST.md` (new Phase 2.5 step), `AGENTS/WALTER/design/EVENT_WINDOW_STATE.md` (new file, current state declaration), `AGENTS/BRENT/CLAUDE.md` (spawn-protocol delta — "if event_window=open, expect FLASH burst").

### 2d.1 — Problem

When Phase 2 of BRENT's two-phase oil thesis fires (Path A — naval escort + war-risk normalization + sovereign Iran climbdown + Platts physical convergence; OR Path B — EIA demand-destruction triggers fire), it's a **multi-signal-burst event in a compressed window** (per BRENT LESSONS #11 — price collapses Day 3-8 of announcement). At normal dispatch cadence, BRENT misses 80% of the move (LESSONS #16 — exit on announcement, not delivery). Existing FLASH precedence covers per-signal urgency but not window-mode coordination.

### 2d.2 — State machine (locked Turn 4)

```
States:
  CLOSED (default)         — normal dispatch cadence, FLASH per-signal as usual
  OPEN (declared)          — all Phase-2-cluster signals dispatch FLASH; threaded Telegram;
                             daily 00:00 UTC roll-up; close-of-window summary at end
  PENDING_VERIFICATION     — declared OPEN but verification gate has not yet fired (≤48h)

Transitions:
  CLOSED → OPEN              ← BRENT declares on Path A 4/4 met OR Path B EIA triggers fire
                              (BRENT-led declaration; alternatively WALTER declares if BRENT stale
                              + first-mover Phase-2-announcement detected)
  OPEN → CLOSED              ← either side declares close after ≥48h stable post-event
                              (default: WALTER-led; either side may fire earlier on disambiguation)
  OPEN → CLOSED (early)      ← LESSONS #18 disambiguation — verification gate fails 48h post-declare;
                              window signals tagged "false-positive window-context"

Verification gates (BRENT canonical):
  (a) Platts Dated Brent convergence to baseline
  (b) Lloyd's transit returns to 60-135/day baseline
  (c) P&I insurer resumption notice
  (d) Sovereign action on blockade (Iran formal climbdown, US Project Freedom stand-down)
```

### 2d.3 — During OPEN window

- All Phase-2-cluster signals dispatch FLASH
- Telegram pings get threaded under a single rolling **"BURST WINDOW OPEN — Phase 2 trigger"** master message; one new message per signal under that thread
- Daily 00:00 UTC roll-up posted by WALTER (signal count, key dispatches, verification-gate progress)
- Close-of-window summary at transition to CLOSED (window duration, dispatches fired, gate-confirmation status, retroactive false-positive-tagging if early-close)
- Other-cluster signals stay normal precedence (don't bleed Phase-2 burst into unrelated domains)

### 2d.4 — Cost asymmetry justification (BRENT Turn 3 Q15 → WALTER Turn 4)

- **False-negative cost** (don't declare on announcement, miss Day 3-8 window): per LESSONS #11, ~80% of Phase 2 move happens in Day 3-8. Material P/L cost.
- **False-positive cost** (declare on rhetorical-not-operational announcement): 24-72h FLASH burst on non-event. Bounded operational cost — Will Telegram fatigue + ~$0.05-0.20 in dispatch sub-agent spawns. Recoverable via early-close + retroactive tagging.

Asymmetric → declare on announcement. 48h verification window gives gates room to fire (Lloyd's transit data lags 12-24h; P&I notices lag 24-48h).

### 2d.5 — FORMAT_SPEC v0.8 add (rolled into §2a if approved)

Adds `event_window: open | closed` boolean header field. Default `closed`. Set to `open` for signals dispatched during declared OPEN window. Lets recipient agents grep for window-context signals at boot.

### 2d.6 — Adds to FILTER_SPEC + CHECKLIST

- **CHECKLIST Phase 2.5** "event-window state check" step: read current state from `AGENTS/WALTER/design/EVENT_WINDOW_STATE.md`; tag dispatched signals accordingly.
- **FILTER_SPEC Tuning Rules sub-section** covering OPEN-window dispatch posture: all Phase-2-cluster signals → FLASH; cross-cluster signals stay normal precedence; verify-research mandatory on extreme-claim items even more than usual due to compressed window.
- **EVENT_WINDOW_STATE.md** scaffold: simple file with current state (`CLOSED` default), declared-by, declared-at, verification-gate-status, expected-close-trigger.

### 2d.7 — BRENT CLAUDE.md spawn-protocol delta

When BRENT boots and reads STATUS, also check `AGENTS/WALTER/design/EVENT_WINDOW_STATE.md`. If state = OPEN: expect FLASH burst — boot fast, integrate fast, re-position fast. Specifically: skip non-energy-cluster BOARD pulls; prioritize KB/FLOW updates from Phase-2-cluster signals; surface position-impact reads to Will via Telegram in real time during window.

### 2d.8 — Q-trail

- BRENT LIAISON Q5 (BRENT→WALTER, Turn 1) → WALTER Turn 2 PROPOSAL (state machine + threaded Telegram) → BRENT Turn 3 ACCEPT (BRENT-declares-open / WALTER-declares-close asymmetry) → WALTER Turn 4 STATE-MACHINE-LOCK + Q15 ANSWER (declare on announcement, asymmetric cost justification).

---

## SECTION 3b — ROUTING_TABLE v0.6 (Iran-cluster CARL-info override) — WALTER self-task

**Status:** Drafted, will ship next session (FYI to Will, no sign-off needed beyond awareness).
**ETA:** Next WALTER session.
**Files affected:** `AGENTS/WALTER/design/ROUTING_TABLE.md` v0.5 → v0.6.
**Origin:** CARL LIAISON Q3 (CARL→WALTER) → WALTER Turn 2 DECISION → CARL Turn 3 SHARPENING → WALTER Turn 4 DECISION (locked thresholds).

### 3b.1 — Problem

ROUTING_TABLE v0.5 default routes OIL_ENERGY → CARL info on every signal. Today (-004 IRGC corridor doctrine, -005 USAF tankers, -009 Wirth Milken) all routed CARL info. CARL retrospective (LIAISON Turn 1): -004 + -005 cost a disposition cycle but didn't change CARL's vector scoring (pure doctrine/military, no transmission path). Routing-volume signal-noise on CARL.

### 3b.2 — Override rule

For Iran-cluster signals (cluster: IRAN_HORMUZ specifically), route CARL info ONLY when:

| Trigger | Rationale |
|---------|-----------|
| Brent close **≥ $110 sustained 2 sessions** | Re-entry of accelerated pump-pass-through window per KB-CARL-259 (3-4d transmission lag in Iran-cluster regime, vs 2-3wk normal regime) |
| Brent close **≤ $95 sustained 5 sessions** | Exit of pass-through window — material relief in food/energy stack, Vector #5 reprice candidate |
| Explicit kinetic event with supply-disruption mechanism | Kinetic-actually-affecting-supply (vessel-strike, refinery-hit, port-closure), not posture-only |
| FX/macro cross with consumer-burden vector | USD/JPY-pump-cost-cross or similar where consumer-burden vector activates |

**Posture / doctrine / diplomatic-cascade / OSINT signals → drop CARL.** (Examples: today's -004 IRGC doctrine, -005 USAF tankers — both posture, neither moves pump prices alone.)

### 3b.3 — Boundary-trigger threshold-cross dispatch (NEW signal type for CARL)

When Brent sustains:
- **≤ $95 for 5+ sessions** → dispatch IMMEDIATE → CARL with `signal_role: threshold-crossed` + `consumer_transmission: pump_pass_through` + dispatch_note flagging Vector #5 Gas Squeeze + Vector #12 Stagflation reprice + CRL-08 trigger (92→60% per CARL's Q12 framework, Turn 3)
- **≥ $115 for 5+ sessions** → dispatch IMMEDIATE → CARL with same tags + flagging Vector #5/#12 hardening + CRL-08 reprice 92→97%+ (per CARL Q12)

Within $95-115 range = noise floor; tape moves don't cross-fire to CARL.

### 3b.4 — Q-trail

- CARL LIAISON Q3 (CARL→WALTER, Turn 1) → WALTER Turn 2 DECISION (calibrate going forward) → CARL Turn 3 SHARPENING (concrete thresholds) → WALTER Turn 4 LOCK (hardcode rule).

---

## SECTION 3d — `design/CROSS_REFS/{CARL,BRENT}.md` cache (WALTER self-task)

**Status:** Drafted, will ship this week (FYI to Will).
**ETA:** This week (CARL cache first, BRENT cache after FLOW.tsv expansion lands).
**Files affected:** New `AGENTS/WALTER/design/CROSS_REFS/CARL.md` + `AGENTS/WALTER/design/CROSS_REFS/BRENT.md` (cache files).
**Origin:** CARL LIAISON Q14 (WALTER→CARL, Turn 2) → CARL Turn 3 IDENTIFIER INDEX DISCLOSED → WALTER Turn 4 PROPOSAL → CARL Turn 5 ACCEPT (with freshness mechanism). BRENT LIAISON Turn 1 README disclosed BRENT identifier index; BRENT Turn 3 confirmed FLOW.tsv expansion this week → cache refresh on first mtime change.

### 3d.1 — Purpose

Local cache of agent-internal identifier indexes (KB / FLOW / PREDICTIONS / SCHEMA / THESIS). Lets WALTER cross-reference IDs in `dispatch_note` at dispatch-time without re-grepping agent trees on every dispatch.

**Example dispatch_note enhancement:**

> Before (today's -003): "*CARL info — pump-price → CPI energy → consumer-stagflation transmission*"
> After (with cache): "*CARL info — `consumer_transmission: pump_pass_through`; transmits to CARL Vector #5 Gas Squeeze (KB-CARL-259); folds to CRL-08 Fed-reaction-function reprice*"

For BRENT-action signals routing to CARL info:
> "*transmits via FLOW-BRT-3.04 to CARL Vector #5 (KB-CARL-259) pump-pass-through*"

Tightens both agents' disposition loops because they can fold straight to the right vector without inferring (CARL Turn 3 + BRENT README explicit asks).

### 3d.2 — Cached content

**CARL cache** (`design/CROSS_REFS/CARL.md`):
- Vectors V1-V14/V16 → from `AGENTS/CARL/thesis/THESIS.md` convergence-matrix table
- VX-CARL-{NN} indicators → from `AGENTS/CARL/workbook/VX.tsv`
- CRL-NN predictions → from `AGENTS/CARL/thesis/PREDICTIONS.tsv`
- KB-CARL-NNN claims → from `AGENTS/CARL/workbook/KB.tsv`
- FLOW-CARL-N.NN transmission → from `AGENTS/CARL/workbook/FLOW.tsv`
- SCHEMA → from `AGENTS/CARL/workbook/SCHEMA.tsv`

**BRENT cache** (`design/CROSS_REFS/BRENT.md`):
- BRT-NN predictions → from `AGENTS/BRENT/workbook/PREDICTIONS.tsv` + `AGENTS/BRENT/thesis/THESIS.md`
- KB-BRT-NNN claims → from `AGENTS/BRENT/workbook/KB.tsv`
- VX-BRT-NN indicators → from `AGENTS/BRENT/workbook/VX.tsv`
- FLOW-BRT-N.NN transmission → from `AGENTS/BRENT/workbook/FLOW.tsv` (heads-up: FLOW expansion this week, cache refreshes on first mtime change after expansion)
- CATALYSTS → from `AGENTS/BRENT/workbook/CATALYSTS.tsv`
- SCHEMA → from `AGENTS/BRENT/workbook/SCHEMA.tsv`
- Convergence matrix → from `AGENTS/BRENT/STATUS.md` (mirror; canonical in THESIS.md)

Each cache file: extracts the most-frequently-referenced IDs + their one-line summaries into a compact lookup table. Full data stays in agent's tree.

### 3d.3 — Freshness mechanism (CARL Turn 5 + BRENT Turn 3)

**Refresh trigger** (dual):
- **THESIS.md version-string change** (e.g., CARL `v2.5.1` → `v2.5.2`; BRENT `v1.x` → `v2`). WALTER reads first line of agent's THESIS.md at boot; compares to cached version. Mismatch → refresh cache.
- **`workbook/SCHEMA.tsv` mtime change.** WALTER stat's the file at boot; compares to cached mtime. Mismatch → refresh cache.

Either triggers full cache rebuild. **Heads-up windows:**
- **CARL** v2.5.2 thesis revision in next 2-4 weeks (services-export sub-vector from KB-281 + 8 PENDING_VERIFY hardening items). Cache will refresh automatically when CARL bumps version string.
- **BRENT** thesis v2 revision in flight post-May-4 (Project Freedom + bypass-pair pattern); FLOW.tsv expansion this week (explicit rows for outbound paths to CARL/SAM/LIQUID/HENRY). Cache will refresh on first FLOW.tsv mtime change after the expansion.

### 3d.4 — Generalization

Once the pattern proves out for CARL + BRENT, generalize to:
- `design/CROSS_REFS/HENRY.md` when HENRY's identifier index stabilizes
- `design/CROSS_REFS/RED.md` for adversarial-frame cross-refs (when RED revives)
- `design/CROSS_REFS/REGINALD.md` for bank-CRE cross-refs

Each follows the same pattern: cache file + dual freshness trigger + dispatch-time lookup.

### 3d.5 — Q-trail

- CARL LIAISON Q14 (WALTER→CARL, Turn 2) → CARL Turn 3 PATHS DISCLOSED → WALTER Turn 4 PROPOSAL (cache) → CARL Turn 5 ACCEPT (with freshness mechanism).
- BRENT LIAISON README + Turn 3 — BRENT identifier index disclosed; FLOW.tsv expansion this week confirmed; same cache pattern adopted.

---

## §5 — FUTURE WORK (v0.9 candidates, no sign-off needed this proposal)

Surfaced for visibility per WALTER Turn 4 Q16 (BRENT LIAISON). Implementation scoping in 1-2 weeks post-v0.8 sign-off.

### 5.1 — `energy_transmission` enum (BRENT-driven, v0.9 candidate)

Analog of `consumer_transmission` for outbound-from-BRENT signals. Final 10-value enum locked BRENT LIAISON Turn 3:

```
energy_transmission: kinetic_supply | sanctions_enforcement | inventory_dynamics |
                     posture_only | operational_anomaly | ceo_supply_balance |
                     tape_pricing | framing_meta | refining_capacity | freight_premium
```

Multi-tag at dispatch (comma-separated like `cluster_secondary`). Worked example: SIG-W-20260420-001 Tuapse refinery 2nd strike = `kinetic_supply, refining_capacity` — multi-tag.

### 5.2 — `regime_state` enum (BRENT-driven, v0.9 candidate)

Separate axis from `energy_transmission`. 5 values:

```
regime_state: phase_1_squeeze | phase_1_to_2_transition | phase_2_destruction_demand |
              phase_2_unwind_opec | post_phase_2_normalization
```

Two-axis cross-product (`tape_pricing × phase_1_squeeze`, `kinetic_supply × phase_1_to_2_transition`) is the discrimination v0.9 needs.

### 5.3 — Implementation effort

- FORMAT_SPEC.md addition: ~30 min
- BOARD_LOG.tsv schema change (BRENT-side): ~15 min
- Retrofit of past dispatches: opt-out (forward-only adoption from v0.9 release date)
- Total: ~1 hour
- Cost: $0

Surface for sign-off in 1-2 weeks once v0.8 lands and field-usage in dispatches confirms shape.

---

## Pre-cosign

WALTER self-cosigns sections 2a + 2b + 2c + 2d + 3b + 3d as drafted.

- **CARL co-sign** on §2a is from CARL LIAISON Turn 5 ("Pre-cosign FORMAT_SPEC v0.8 on my side: confirmed").
- **BRENT co-sign** on §2a is from BRENT LIAISON Turn 3 ("BRENT cosigns" final 9-value enum with `lng_substitution`).
- **CARL co-sign** on §2b is from CARL LIAISON Turn 5 ("STRONGLY WANTS").
- **BRENT pre-cosign** on §2b extension to BRENT-primary calendar from BRENT LIAISON Turn 3 (self-task ETA post-back-disposition).
- **BRENT co-sign** on §2c (8-row threshold list) is from BRENT LIAISON Turn 3 ("Q4 threshold list — both redlines accepted, full 8-row table locked").
- **BRENT co-sign** on §2d (BURST_WINDOW protocol) is from BRENT LIAISON Turn 3 ("Q5 BURST_WINDOW_OPEN protocol — accept your shape").

CARL drafts §1 (context) + §3a (Post_Hoc_Conf shipped commit `d26aaab2`) + §3c (DATA_RELEASE_CALENDAR.md ETA) + §4 (locked-decisions full list, Q1-Q22+) to `AGENTS/CARL/design/JOINT_PROPOSAL_2026-05-05_carl_sections.md`.

BRENT drafts §1-coda (BRENT-side context) + §2e (BRENT cosign + lng_substitution rationale) + §4-coda (BRENT-side decisions) to `AGENTS/BRENT/design/JOINT_PROPOSAL_2026-05-05_brent_sections.md`.

Final stitch lives at repo-root `design/JOINT_PROPOSAL_2026-05-06_walter_carl_brent.md` — WALTER stitches when all 3 per-agent files land. Surface to Will via Telegram with link to repo-root file. Each agent commits own sections within its own tree (git-isolation preserved).

---

*Q-trail summary: CARL LIAISON 7-turn dialog (CARL Turn 1 → CARL Turn 7, 2026-05-05 22:00 → 2026-05-06 01:30 UTC, source `AGENTS/CARL/handoff_WALTER/LIAISON.md`) + BRENT LIAISON 4-turn dialog (BRENT Turn 1 → WALTER Turn 4, 2026-05-05 23:15 → 2026-05-06 04:30 UTC, source `AGENTS/BRENT/handoff_WALTER/LIAISON.md`). Three-way joint surface mechanics per CARL Turn 7 + WALTER Turn 6 + BRENT Turn 3.*
