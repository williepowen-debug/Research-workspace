# JOINT_PROPOSAL — WALTER sections — 2026-05-05

*WALTER-drafted sections of the joint WALTER+CARL proposal from the 6-turn LIAISON dialog 2026-05-05. CARL drafts sections 1 (context), 3a (Post_Hoc_Conf shipped), 3c (DATA_RELEASE_CALENDAR), 4 (locked-decisions list). Final stitch lives at repo-root `design/JOINT_PROPOSAL_2026-05-05.md` (Will-mediated).*

---

## SECTION 2a — FORMAT_SPEC v0.8 (4 field additions, co-signed CARL+WALTER)

**Status:** Drafted, awaiting Will sign-off. Co-signed by CARL (LIAISON Turn 5). Pre-cosigned: yes.
**Cost:** $0 (structural-only).
**Origin:** LIAISON Turns 1-4 (Q1, Q6, Q9, Q15 → final v0.8 enum).
**Files affected:** `AGENTS/WALTER/design/SIGNAL_FORMAT_SPEC.md` (canonical), `SIGNAL_PROCESSING_CHECKLIST.md` (Phase 2 cluster/role/lens/transmission tagging step), `ROUTING_TABLE.md` (mechanic-aware routing).

### 2a.1 — `consumer_transmission` (optional enum, header field)

**Purpose:** Tag the transmission mechanism through which a signal reaches CARL's consumer-stress thesis. Allows CARL to batch-fold same-mechanism signals at boot rather than disposition each individually.

**Enum values (8):**
```
pump_pass_through       — oil/gas → retail pump → CPI energy → consumer-burden
wage_pressure           — labor data → wage growth / employment cost index
wealth_effect           — equity-portfolio-driven (top 40%) → discretionary spend
policy_pass_through     — tariff / regulatory / fiscal → consumer-cost / income
discretionary_demand    — observation-side demand-destruction (restaurants, theme parks, cruise, leisure travel)
services_export         — international-inbound demand (US-tourism-receipts, hospitality-foreign)
counter_evidence        — within-cluster counter-thesis data
none                    — no consumer-stress transmission, info-only for cluster context
```

**Today's signals retagged:**
- `-001` IEA crude inventory → `pump_pass_through`
- `-002` IEA LNG → `pump_pass_through` (gas-electricity-cost cross)
- `-003` EIA US gasoline decade-low → `pump_pass_through`
- `-006` ISM Services + JOLTS → `wage_pressure` (multi-axis MACRO+LABOR)
- `-007` Factory Orders counter → `counter_evidence`
- `-008` AHLA WC hotel → `services_export` (NEW — observation-side gap closed by CARL's Q3-Turn3 suggestion)
- `-009` Wirth Milken → `pump_pass_through`
- `-010` Black Box restaurants → `discretionary_demand` (NEW — observation-side)
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

**Authoritative-voice precedence on cluster_mediating signals:** NEXUS > WALTER (tagger) > action-primary (data substance locally). NEXUS owns cluster-narrative-update interpretation; WALTER applies the tag based on cross-cluster observation; action-primary interprets data-substance-locally without authoritatively rewriting cluster narrative. (See LIAISON Turn 4 Q16 for full precedence rule.)

### 2a.3 — `consumer_lens` (optional enum, header field)

**Purpose:** Codify the K-shape framing distinction for consumer signals. Different routing/disposition paths.

**Enum values (4):**
```
tier_stratified         — discretionary pullback in mid-tier with top-decile counter-channels intact (today's -010 Black Box pattern)
broad_collapse          — multi-tier consumer demand destruction (would route CARL primary action immediately)
mixed                   — multi-axis with no clear K-shape signal (today's -006 demand cooling + labor absorbing)
counter                 — counter-evidence to consumer-stress thesis (today's -007 Factory Orders beat)
```

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
- For new signals dispatched 2026-05-06 onward: WALTER tags `cluster_secondary` and `signal_role` always when applicable; `consumer_transmission` and `consumer_lens` only when CARL is on the routing line.
- BOARD INDEX section structure unchanged (primary-cluster-only); no INDEX migration required.
- BOARD_LOG.tsv schema (CARL's side) unchanged on these fields — CARL reads them out of signal headers when dispositioning.

### 2a.7 — Q-trail

- LIAISON Q1 / Q6 / Q9 / Q15 (CARL→WALTER) → WALTER Turn 4 PROPOSAL → CARL Turn 5 ACCEPT (with `discretionary_demand` + `services_export` enum extension and `cluster_secondary` order convention).

---

## SECTION 2b — Scheduled lightweight scan workflow

**Status:** Drafted, awaiting Will sign-off (cost-budget call).
**Cost:** ~$0.30-0.50/wk recurring (5-7 scans × ~$0.05 each).
**Origin:** LIAISON Q8 (CARL→WALTER) → WALTER Turn 4 PROPOSAL → CARL Turn 5 STRONGLY WANTS.
**Files affected:** WALTER cron-equivalent (no specific file yet — first implementation), reads `AGENTS/CARL/DATA_RELEASE_CALENDAR.md` (CARL self-task this week).

### 2b.1 — Problem

CARL's primary-data sources (NY Fed HHDC, BLS CPI/PPI/PCE/JOLTS/NFP, Freddie PMMS, AAA pump price, ABS 10-D filings) currently bottleneck on CARL's own session frequency. Refresh staleness is 5-15 days. Today (-006 ISM/JOLTS) caught the BLS releases via Daly Asset Management aggregator pickup — not via my own scheduled pull. Real gap.

### 2b.2 — Mechanism

- WALTER cron-equivalent reads `AGENTS/CARL/DATA_RELEASE_CALENDAR.md` (CARL self-task ETA this week — extends current `EARNINGS_WATCH_Q1.md` to year-rolling format).
- Calendar columns: `Date | Time (ET) | Source | Release | Cadence | CARL-Vector | Notes` (CARL Turn 5 accept).
- Cron fires lightweight Sonnet scan ~1h before each release, then again ~5 minutes post-release.
- Pre-release scan: confirm release-day-of, prepare verify-research framework. Post-release scan: pull primary-source numbers, dispatch to CARL within minutes.

### 2b.3 — Coverage estimate

Based on CARL's listed primary-data sources:
- BLS CPI/PPI/PCE/JOLTS/NFP: ~5 monthly releases × 12 = ~60/yr (~1.2/wk avg, varies)
- Freddie PMMS: ~52/yr (1/wk Thursday)
- AAA pump: ~365/yr daily (could batch into weekly during normal regime, daily during Iran-cluster regime)
- ABS 10-D: variable, ~2-4/month
- NY Fed Q1 HHDC: 4/yr (quarterly)
- **Total: ~5-7 active scans/week** at typical cadence.

### 2b.4 — Cost projection

- Per-scan: ~$0.05 (Sonnet, 1-2 tool uses, primary-source pull + verify-research lite)
- Weekly total: $0.30-0.50/wk
- Monthly total: ~$1.20-2.00/month
- **Annual: ~$15-25/year**

### 2b.5 — Deliverable

Dispatched signals to CARL with `signal_role: primary_substance` + `consumer_transmission: <mechanism>` tags within minutes of release. Tightens CARL refresh from "5-15 days behind" → "2-3 days behind" (depending on CARL boot cadence per Q5 decision).

### 2b.6 — Kill-trigger

Scrap the workflow if any of:
- (a) Monthly cost overrun >2x budget (>$4/month sustained for 2 consecutive months)
- (b) Signal-quality degradation (false-positive rate >20% on dispatched scans, measured by CARL `Post_Hoc_Conf` deltas)
- (c) CARL feedback that auto-pushed signals are net-noise (3+ consecutive INFO_ONLY-or-REFERRED dispositions on auto-pushed signals indicates wrong calibration)

### 2b.7 — Q-trail

- LIAISON Q8 (CARL→WALTER) → WALTER Turn 4 PROPOSAL → CARL Turn 5 STRONGLY WANTS.

---

## SECTION 3b — ROUTING_TABLE v0.6 (Iran-cluster CARL-info override) — WALTER self-task

**Status:** Drafted, will ship next session (FYI to Will, no sign-off needed beyond awareness).
**ETA:** Next WALTER session.
**Files affected:** `AGENTS/WALTER/design/ROUTING_TABLE.md` v0.5 → v0.6.
**Origin:** LIAISON Q3 (CARL→WALTER) → WALTER Turn 2 DECISION → CARL Turn 3 SHARPENING → WALTER Turn 4 DECISION (locked thresholds).

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

- LIAISON Q3 (CARL→WALTER, Turn 1) → WALTER Turn 2 DECISION (calibrate going forward) → CARL Turn 3 SHARPENING (concrete thresholds) → WALTER Turn 4 LOCK (hardcode rule).

---

## SECTION 3d — `design/CROSS_REFS/CARL.md` cache (WALTER self-task)

**Status:** Drafted, will ship next session (FYI to Will).
**ETA:** Next WALTER session.
**Files affected:** New `AGENTS/WALTER/design/CROSS_REFS/CARL.md` (cache file).
**Origin:** LIAISON Q14 (WALTER→CARL, Turn 2) → CARL Turn 3 IDENTIFIER INDEX DISCLOSED → WALTER Turn 4 PROPOSAL → CARL Turn 5 ACCEPT (with freshness mechanism).

### 3d.1 — Purpose

Local cache of CARL's identifier indexes (Vector / KB / CRL / FLOW / SCHEMA). Lets WALTER cross-reference CARL Vector / KB IDs in `dispatch_note` at dispatch-time without re-grepping CARL's tree on every dispatch.

**Example dispatch_note enhancement:**

> Before (today's -003): "*CARL info — pump-price → CPI energy → consumer-stagflation transmission*"
> After (with cache): "*CARL info — `consumer_transmission: pump_pass_through`; transmits to CARL Vector #5 Gas Squeeze (KB-CARL-259); folds to CRL-08 Fed-reaction-function reprice*"

Tightens CARL's disposition loop because CARL can fold straight to the right vector without inferring (CARL Turn 3 explicit ask).

### 3d.2 — Cached content

From CARL (Turn 3 paths):
- Vectors V1-V14/V16 → from `AGENTS/CARL/thesis/THESIS.md` convergence-matrix table
- VX-CARL-{NN} indicators → from `AGENTS/CARL/workbook/VX.tsv`
- CRL-NN predictions → from `AGENTS/CARL/thesis/PREDICTIONS.tsv`
- KB-CARL-NNN claims → from `AGENTS/CARL/workbook/KB.tsv`
- FLOW-CARL-N.NN transmission → from `AGENTS/CARL/workbook/FLOW.tsv`
- SCHEMA → from `AGENTS/CARL/workbook/SCHEMA.tsv`

Cache file: extracts the most-frequently-referenced IDs + their one-line summaries into a compact lookup table. Full data stays in CARL's tree.

### 3d.3 — Freshness mechanism (CARL Turn 5)

**Refresh trigger** (dual):
- **THESIS.md version-string change** (e.g., `v2.5.1` → `v2.5.2`). WALTER reads first line of CARL's THESIS.md at boot; compares to cached version. Mismatch → refresh cache.
- **`workbook/SCHEMA.tsv` mtime change.** WALTER stat's the file at boot; compares to cached mtime. Mismatch → refresh cache.

Either triggers full cache rebuild. **Heads-up from CARL Turn 5:** v2.5.2 thesis revision in next 2-4 weeks (services-export sub-vector from KB-281 + 8 PENDING_VERIFY hardening items). Cache will refresh automatically when CARL bumps the version string.

### 3d.4 — Generalization

Once the pattern proves out for CARL, generalize to:
- `design/CROSS_REFS/HENRY.md` when HENRY's identifier index stabilizes
- `design/CROSS_REFS/BRENT.md` for energy-cluster cross-refs
- `design/CROSS_REFS/RED.md` for adversarial-frame cross-refs

Each follows the same pattern: cache file + dual freshness trigger + dispatch-time lookup.

### 3d.5 — Q-trail

- LIAISON Q14 (WALTER→CARL, Turn 2) → CARL Turn 3 PATHS DISCLOSED → WALTER Turn 4 PROPOSAL (cache) → CARL Turn 5 ACCEPT (with freshness mechanism).

---

## Pre-cosign

WALTER self-cosigns sections 2a + 2b + 3b + 3d as drafted. CARL co-sign on 2a is from LIAISON Turn 5 ("Pre-cosign FORMAT_SPEC v0.8 on my side: confirmed").

CARL drafts sections 1 (context), 3a (Post_Hoc_Conf shipped commit `d26aaab2`), 3c (DATA_RELEASE_CALENDAR.md ETA), and 4 (locked-decisions full list) to `AGENTS/CARL/design/JOINT_PROPOSAL_2026-05-05_carl_sections.md` (or wherever CARL prefers).

Final stitch lives at repo-root `design/JOINT_PROPOSAL_2026-05-05.md` — Will-mediated integration. Each agent commits own sections within its own tree (git-isolation preserved); Will commits the final stitch from repo root.

---

*Q-trail summary: 6-turn LIAISON dialog (CARL Turn 1 → WALTER Turn 6, 2026-05-05 22:00 → 2026-05-06 01:05 UTC). Source canonical: `AGENTS/CARL/handoff_WALTER/LIAISON.md`.*
