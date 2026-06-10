# WALTER Signal Format Specification v0.10

**v0.10 (2026-06-10):** Added signal lifecycle fields `status` + `status_ref` (optional, retro-applied two-field schema; per BOARD-audit Orch adjudication + Will sign-off 2026-06-10). See "Signal Lifecycle" section. Also records the v0.9 inline enum-add `narrative_channel: houthi` (2026-06-10, small-change rule) in version history per FOLLOW-UP #40.

**v0.9 (2026-06-06):** Added `narrative_channel` field (Iran-cluster mandatory; documents which observer-channel a fragmented-narrative signal leans on). Added INFLATION_TRANSMISSION to the `cluster` enum reference (11th cluster per CLUSTER_TAXONOMY v0.2). Per 5-decision-walkthrough closeout 2026-06-06.

WALTER is the single entry point for external information into the agent network. All incoming data — news, market data, research, observations — is classified, reformatted, and routed by WALTER as standardized signal files delivered to agent inboxes.

---

## Signal File Convention

**Filename:** `SIG-WALTER-{TARGET}-{YYYYMMDD}-{slug}.md`
**Location:** `AGENTS/{TARGET}/inbox/`
**One file per action recipient.** Info recipients get a copy with their name in the filename.

---

## Header Block

Every signal starts with a YAML-style header block fenced by `---`. All fields required unless marked optional.

```
---
signal_id: SIG-W-20260407-001
precedence: IMMEDIATE
timestamp: 2026-04-07T14:30:00Z
source: WALTER
origin: "Financial Times, 2026-04-07"

to: CARL (ACTION)
info: RED, REGINALD
group: THESIS_CORE

signal_type: catalyst
confidence: 0.72
confidence_language: reports
resources: 1
safety_net: clear

word_count: 148

cluster: PC_STRESS                    # optional v0.6 → required v0.7 (added May 5 2026 per CLUSTER_TAXONOMY.md v0.1)

# Optional v0.8 fields (added 2026-05-08 per JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2a + §2d.5; CARL+BRENT+WALTER cosigned, Will-approved 2026-05-08)
cluster_secondary: BANK_COLLATERAL    # optional, comma-separated for 2+ secondaries
signal_role: primary_substance        # optional, 4-value enum
consumer_transmission: pump_pass_through  # optional, 9-value enum (only when CARL on routing line)
consumer_lens: tier_stratified        # optional, 4-value enum (only when consumer-cluster signal + CARL on routing line)
event_window: closed                  # optional, boolean — set 'open' during declared BURST_WINDOW per §2d state machine; default 'closed'

# v0.9 field (added 2026-06-06 per 5-decision-walkthrough closeout; carry-forward from 6/2 Iran-anchor refresh)
narrative_channel: tasnim             # Iran-cluster MANDATORY (7-value enum); null/omit on non-Iran clusters until promoted to wider scope

# Optional dispatch-time fields (added when signal is routed to recipient inboxes)
dispatched: 2026-04-07T14:45:00Z
dispatch_note: "Trimmed from 4-recipient plan to CARL+RED after HENRY already processed"

# v0.10 lifecycle fields (added 2026-06-10; OPTIONAL, retro-applied by WALTER when a signal's framing is overtaken — never at dispatch time)
status: SUPERSEDED                    # 3-value enum: SUPERSEDED / FALSIFIED / EVENT-PASSED. Absence = no lifecycle judgment recorded, NOT an assertion of liveness.
status_ref: "anchors/IRAN_WAR.md verified-as-of 2026-06-10"   # MANDATORY whenever status is present — see Signal Lifecycle section for valid ref forms per enum value
---
```

### Field Definitions

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| `signal_id` | string | `SIG-W-YYYYMMDD-NNN` | Unique ID. W = WALTER-originated. Sequential per day. |
| `precedence` | enum | `FLASH` / `IMMEDIATE` / `PRIORITY` / `ROUTINE` | Processing urgency. See Precedence Levels below. |
| `timestamp` | ISO8601 | — | When WALTER classified this signal. |
| `source` | string | `WALTER` | Always WALTER for v0.1. |
| `origin` | string OR array of strings | Free text OR `["src1", "src2", ...]` | Where the raw information came from. Array form when 2+ sources fold into one signal — see Multi-Origin Signals below. |
| `to` | string | `AGENT (ACTION)` or `AGENT (INFO)` | Primary recipient for this file. Per-recipient files get their own `to:` value when the same signal dispatches to multiple agents. |
| `info` | string | Comma-separated agents | Awareness recipients. Optional. |
| `group` | string | AIG name | Optional. Which Address Indicating Group, if any. |
| `signal_type` | enum | See Signal Types | What kind of signal this is. |
| `confidence` | float | 0.0–1.0 | Numerical confidence score. For machine routing and threshold filters. See Confidence Model below. |
| `confidence_language` | enum | `confirmed` / `reports` / `assessed` / `unconfirmed` | Human-readable confidence tier. For prose context. Must be consistent with `confidence` per the mapping below. |
| `resources` | int | 0 / 1 / 2 | Estimated processing resources needed. |
| `safety_net` | enum | `clear` / `triggered` | Whether safety net override was triggered. |
| `word_count` | int | — | Body word count. FLASH/IMMEDIATE must be ≤200. |
| `cluster` | enum | One of the 11 names in `design/CLUSTER_TAXONOMY.md` (v0.2 added INFLATION_TRANSMISSION) | **v0.7 — Required for new signals dispatched 2026-05-05 and later.** Determines which `/BOARD/INDEX.md` section the dispatch row lands in. Pre-v0.7 historical signals don't have this header field — their cluster placement lives in INDEX section structure only. See CLUSTER_TAXONOMY.md for canonical bucket names + edge-case rules (cross-cluster: substance > mechanism > action-recipient). |
| `cluster_secondary` | enum (comma-separated) | One or more of the 11 cluster names | **v0.8 — Optional.** Multi-cluster signals tag the primary cluster (per CLUSTER_TAXONOMY substance > mechanism > action-recipient resolution rule) AND optionally one or more secondary clusters. Order convention: descending action-relevance for routed agents. Drives batch-folding at recipient boot. See `consumer_transmission` + `signal_role` for related v0.8 routing-augmentation fields. Per JOINT_PROPOSAL §2a.4. |
| `signal_role` | enum | `primary_substance` / `cluster_mediating` / `counter_evidence` / `thesis_confirmation` | **v0.8 — Optional.** Tags the role a signal plays within its cluster's narrative. Distinguishes substance-data from interpretive-mediating signals. Authoritative-voice precedence on `cluster_mediating`: NEXUS > WALTER (tagger) > action-primary (data substance locally). NEXUS owns cluster-narrative-update interpretation; WALTER applies the tag based on cross-cluster observation; action-primary interprets data-substance-locally without authoritatively rewriting cluster narrative. Per JOINT_PROPOSAL §2a.2. |
| `consumer_transmission` | enum | `pump_pass_through` / `wage_pressure` / `wealth_effect` / `policy_pass_through` / `discretionary_demand` / `services_export` / `lng_substitution` / `counter_evidence` / `none` | **v0.8 — Optional.** Tag the transmission mechanism through which a signal reaches CARL's consumer-stress thesis (or transmits energy → consumer through BRENT-side outbound). Allows CARL to batch-fold same-mechanism signals at boot. Tag only when CARL is on the routing line; energy-cluster signals carry it only when consumer-side info recipient is on the routing line. Per JOINT_PROPOSAL §2a.1. |
| `consumer_lens` | enum | `tier_stratified` / `broad_collapse` / `mixed` / `counter` | **v0.8 — Optional.** Codify the K-shape framing distinction for consumer signals. `tier_stratified` = discretionary pullback in mid-tier with top-decile counter-channels intact. `broad_collapse` = multi-tier consumer demand destruction (would route CARL primary action immediately). `mixed` = multi-axis with no clear K-shape signal. `counter` = counter-evidence to consumer-stress thesis. Tag only on consumer-cluster signals with CARL on routing line; energy-cluster signals don't carry. Per JOINT_PROPOSAL §2a.3. |
| `event_window` | enum | `open` / `closed` | **v0.8 — Optional.** Set to `open` for signals dispatched during a declared BURST_WINDOW state per JOINT_PROPOSAL §2d state machine; default `closed`. Lets recipient agents grep for window-context signals at boot and adjust dispatch posture (FLASH burst expected for Phase-2-cluster signals during OPEN). Current state is canonical in `design/EVENT_WINDOW_STATE.md`. Per JOINT_PROPOSAL §2d.5. |
| `narrative_channel` | enum | `tasnim` / `mfa` / `potus` / `centcom` / `idf` / `pakistan_mediator` / `houthi` | **v0.9 — MANDATORY on Iran-cluster signals; null/omit elsewhere.** Documents which observer-channel the signal leans on when narrative is fragmented (current Iran case: Tasnim/IRGC vs Araghchi/MFA vs Trump/POTUS vs CENTCOM operational — same bilateral state has no single ground truth, "channel state is observer-dependent" per IRAN_WAR anchor 6/02). Forces dispatch to surface which observer authored the framing so downstream agents weight accordingly. Trump-rhetoric-tape-not-info SYMMETRIC-rule (per MEMORY 6/02) applies on `potus` tag — both deal-up and deal-down framings get the rhetoric-not-substance treatment. Promote to wider scope (Fed-framework, Asia-China) only when a second fragmented-narrative cluster earns it. Per 5-decision-walkthrough closeout 2026-06-06. **`houthi` added 2026-06-10** (inline enum-add per spec-change small-change rule) — Bab al-Mandab activation made Houthi/Saree declarations a load-bearing observer channel (first use: SIG-W-20260610-001). |
| `status` | enum | `SUPERSEDED` / `FALSIFIED` / `EVENT-PASSED` | **v0.10 — Optional, retro-applied (never set at dispatch).** Lifecycle state of the signal's framing: `SUPERSEDED` = core state-claim or framing overtaken by later events/signals; `FALSIFIED` = the signal's prediction or trigger-state claim failed against subsequent data; `EVENT-PASSED` = its forward calendar window or named event has occurred/lapsed. **Absence of the field = no lifecycle judgment recorded — NOT an assertion that the signal is live.** WALTER applies; consumers grep it the same way they grep `to:` / `cluster_mediating:`. See Signal Lifecycle section. |
| `status_ref` | string | — | **v0.10 — MANDATORY whenever `status` is present.** Provenance for the lifecycle judgment; an unprovenance'd status tag is invalid. Valid ref form per enum value: `SUPERSEDED` → superseding SIG ID **or** anchor verified-as-of stamp (e.g. `anchors/IRAN_WAR.md verified-as-of 2026-06-10`); `FALSIFIED` → fired-log row (e.g. `FALSIFICATION_FIRED_LOG.tsv RED-FT-01 2026-06-04`) **or** falsifying print with date + source; `EVENT-PASSED` → the passed date or event identifier. |
| `dispatched` | ISO8601 | — | **Optional.** Added when the signal is actually dispatched to recipient inboxes (may be later than `timestamp` if drafted-then-dispatched flow is used). |
| `dispatch_note` | string | Free text | **Optional.** Rationale if the dispatch deviated from the original plan: recipient trim, re-route, precedence downgrade, staleness caveat. Paired with `dispatched`. |

---

## Confidence Model

Two confidence fields, both required, both must be consistent. Numerical for machine routing, language for human reading. The two fields are **bound** by the mapping below — they cannot disagree.

| `confidence_language` | `confidence` band | When to use |
|-----------------------|-------------------|-------------|
| `confirmed` | **0.90–1.0** | Official data release (BLS, FRED, SEC, central bank) OR multiple independent authoritative sources verifying same fact. Two-source rule satisfied via golden sources. |
| `reports` | **0.75–0.89** | Single credible named source with direct knowledge (Bloomberg, Reuters, FT, named analyst, SEC filing). Specific verifiable claims. |
| `assessed` | **0.50–0.74** | Synthesis from multiple indicators or agent inference. Not direct evidence but well-supported. |
| `unconfirmed` | **0.30–0.49** | Single source with no corroboration. Should rarely route — usually held or filtered. |
| (filtered) | **<0.30** | Below routing threshold. Goes to kill log, not the archive. |

**Why both fields:** The numerical score lets agents and tools filter mechanically (e.g., RED might want to see signals at 0.50+; REGINALD might only act on 0.85+). The language tier tells humans WHAT KIND of certainty this is — a 0.92 "confirmed" reads very differently from a 0.92 "reports."

**Adjustment factors** (from FILTER_SPEC.md):
- +0.1 if corroborated by second independent source
- +0.1 if consistent with existing agent thesis
- -0.1 if contradicts established data (could be real, but needs higher bar)
- -0.1 if source has history of unreliable reporting
- +0.2 if official government/central bank data release

After adjustments, snap the language tier to the resulting numerical band.

---

## Precedence Levels

| Level | Delivery Target | Word Limit | Use When |
|-------|----------------|------------|----------|
| **FLASH** | Immediate | 200 words | System-threatening. Stop-loss breach, margin call, liquidity trap. |
| **IMMEDIATE** | <30 min | 200 words | Thesis-critical. Threshold breach, convergence confirmed, major catalyst. |
| **PRIORITY** | <3 hours | Unlimited | Significant but not time-critical. Research, position review, deep analysis. |
| **ROUTINE** | <6 hours | Unlimited | Background. Monitoring updates, periodic data, context building. |

**Rule:** If you can't say it in 200 words at FLASH/IMMEDIATE, you don't understand it yet. Distill first, elaborate in a follow-up PRIORITY signal if needed.

---

## Signal Types

| Type | Description | Typical Precedence |
|------|-------------|-------------------|
| `threshold-crossed` | A monitored metric breached a defined level | IMMEDIATE |
| `pattern-match` | A recognized pattern appeared in data | PRIORITY |
| `catalyst` | A known upcoming event occurred or was confirmed | IMMEDIATE |
| `divergence` | Expected correlation broke or reversed | IMMEDIATE |
| `research` | New research, analysis, or report relevant to thesis | PRIORITY |
| `thesis-frame` | Analytical synthesis, institutional framework, or comparative analysis that reframes an existing thesis axis (e.g., MS 1990-vs-2026 oil-shock compare, BRK-vs-SPY quality-flight read, multi-channel convergence analysis). Distinct from `research` (new data/reports) and `pattern-match` (data pattern detection) — this is interpretation/synthesis. | PRIORITY |
| `position-risk` | Information directly affecting an open position | FLASH or IMMEDIATE |
| `context` | Background information, no immediate action | ROUTINE |
| `manual-flag` | Will or an agent flagged something for routing | Varies |

---

## Safety Net Override

After initial classification, WALTER checks override conditions. If ANY trigger, the signal is upgraded to at least IMMEDIATE regardless of initial classification.

**Override triggers:**
- VIX spike > defined threshold
- HY OAS sudden widening (>25bps single session)
- Correlation breakdown between normally correlated assets
- Bid-ask spread widening in held positions (liquidity dry-up)
- Multiple agents flagging same theme within 24 hours (convergence)

When triggered: `safety_net: triggered` and precedence forced to IMMEDIATE or higher.

---

## Body Format

After the header, the signal body follows a fixed structure:

```markdown
## Signal

[1-2 sentence summary of what happened]

## Data

[Specific numbers, quotes, or facts. No interpretation here.]

## Relevance

[Why this matters to the recipient's domain. What it means for the thesis.]

## Source

[Full citation. URL if available.]
```

**FLASH/IMMEDIATE signals:** The Signal + Data sections combined must stay under 200 words. Relevance can be a single sentence.

**PRIORITY/ROUTINE signals:** No word limit, but brevity is still valued.

---

## Multi-Origin Signals — Same-Theme Combine Rule

When 2+ items surface the same underlying event (or specific sub-theme within a domain), fold them into ONE signal with multiple origin attributions rather than dispatching duplicates. Intent is "put like with like" — consolidate redundancy while drafting, not after.

**Combine when ALL of these hold:**

1. **Same canonical domain.** Both items map to the same code from the Domain Vocabulary (LABOR, MACRO_INFLATION, GEOPOL_ENERGY, etc.). Cross-domain items do not combine — they may be thematically adjacent but get routed separately.
2. **Same underlying event OR same specific sub-theme within that domain.** Crisp test for "event" (Iran ship intercept + carrier build-up = same event). Looser test for "sub-theme" — stagflation-pressure as a sub-theme within MACRO_INFLATION merged March CPI + April UMich prelim, extremity-counter as a sub-theme within MARKET_VOL merged Bilello VIX-3wk + SPX-3wk. Domain alone is too broad (Hormuz shipping and Iran nuclear talks are both GEOPOL_ENERGY but different events — don't combine).
3. **Each origin adds independent value.** A new angle, cross-verification, extension, or complementary evidence. Identical reposts of the same image/claim do NOT combine — dup-kill the extras and route one.

**Cross-author is allowed and common.** Of the combines performed through Apr 20 2026, 3 of 5 were cross-author (Flightradar24+Celestyal, disclosetv+BRICSinfo, axios+Polymarket).

**No combine ceiling.** Unlimited origins allowed as long as each adds value.

**Timing — pre-dispatch flexibility, post-dispatch immutability:**

- **Pre-dispatch.** While a signal is still being drafted (in working session, not yet appended to route_log.tsv), items from any arrival path — same Telegram batch, different batch, separate Will message, WALTER-found article, aggregator link — can fold in with multi-origin. The combine decision is made at draft-time, not intake-time.
- **Post-dispatch.** The dispatched signal is immutable (per Editorial Discipline). Later items on the same event take one of two paths: (a) dup-kill if no new value, or (b) follow-up signal that references and extends the prior SIG-ID. No retroactive merging.

**Body conventions for multi-origin signals:**

- Signal + Data sections may cite both origins inline.
- Source section lists ALL origins with their individual URLs/attributions — this is the audit trail for absorbed origins (no new route_log column needed).
- Confidence benefits from cross-verification per the FILTER_SPEC adjustment factors (+0.1 if corroborated by independent source). Don't double-apply — the combine itself doesn't grant a second bonus.

**Historical examples:**

- `SIG-W-20260419-024` (IMMEDIATE → BRENT): `origin: ["@disclosetv CBS carrier build-up Apr 19", "@BRICSinfo Iran rejects 2nd-round talks Apr 19"]` — cross-author, GEOPOL_ENERGY, Iran-escalation event.
- `SIG-W-20260419-017` (PRIORITY → HENRY): `origin: ["@charliebilello VIX -43.7% 3wks", "@charliebilello SPX +11.9% 3wks"]` — same author, MARKET_VOL, extremity-counter sub-theme.
- `SIG-W-20260419-004` (PRIORITY → HENRY): `origin: ["@FinanceLancelot Wyckoff distribution", "@FinanceLancelot NDX 25-yr parabolic"]` — same author, MARKET_VOL, distribution-pattern sub-theme.
- `SIG-W-20260410-001` (IMMEDIATE → CARL): CPI + UMich both MACRO_INFLATION, stagflation-pressure sub-theme (pre-FORMAT_SPEC v0.6, cited as superevent in body).

---

## Signal Lifecycle (`status` / `status_ref`) — v0.10

BOARD is append-only (signal files are never deleted or renamed), so lifecycle state is expressed by **retro-applied YAML tagging**, not removal. One mechanism only — the YAML field pair above; no preamble-block alternative (two mechanisms guarantee drift).

**Application discipline:**
- WALTER is the only writer. Tags are applied retroactively when a signal's framing is overtaken — via the staleness sweep below, at anchor re-stamps, on threshold un-fires, or ad hoc when a dispatch supersedes a prior signal.
- Only actively-misleading signals get tagged. Historically-accurate dispatch-time snapshots (the majority) carry no tag — the BOARD/INDEX.md section-preamble discount rule ("rows are dispatch-time snapshots…") is the blanket advisory covering them.
- Every tag carries `status_ref` provenance per the field table. No ref, no tag.

**Staleness sweep (candidate generation, not adjudication):** the rerunnable sweep greps signal bodies for (a) forward calendar dates now passed, (b) framing language anchored to a superseded anchor-state (e.g. pre-re-stamp Iran war-frames), (c) trigger/threshold state-claims contradicted by the fired-log ledgers or current tape. **Grep patterns are candidate generation and WILL have false negatives — framing staleness isn't always lexical.** That is acceptable by design: any C-class signal the sweep misses is still covered by the section-preamble blanket rule. WALTER reads candidates and adjudicates; the sweep never auto-tags. Pairs with the planned `valid_until` forward-expiry convention (design backlog) — signals carrying explicit expiry self-enumerate in future sweeps.

---

## Domain Vocabulary (Canonical Reference)

**Purpose:** Single canonical list of domain codes used consistently across all WALTER specs and routing decisions. Before Apr 11, ROUTING_TABLE and CHECKLIST used inconsistent domain names (e.g., "Employment / Labor" vs "LABOR"). This section is the source of truth; all other specs reference it.

**Not a header field (yet).** These codes are used in prose, row labels, and routing-decision tables — not yet as a `domain:` YAML field. If we later decide to make `domain:` a machine-filterable header field, update this section and FORMAT_SPEC field table together, per the canonical-source rule in `WALTER/CLAUDE.md`.

### The 15 Canonical Domains

| Code | Scope | Example inputs | Primary action recipient |
|------|-------|----------------|---------------------------|
| `LABOR` | Employment data — NFP, claims, JOLTS, wages, LFPR, U-3, participation | BLS Employment Situation, weekly claims, JOLTS release | CARL |
| `MACRO_INFLATION` | Inflation + growth prints — CPI, PCE, PPI, UMich, GDP, ISM, retail sales | BLS CPI, BEA PCE, UMich SCA, Atlanta Fed GDPNow | CARL |
| `TARIFF_TRADE` | Executive orders, tariff changes, trade deals, retaliation | Trump tariff announcements, USTR actions, trade pauses | CARL |
| `CONSUMER_CREDIT` | Delinquency, student loans, auto, subprime, household debt | NY Fed HH Debt Report, CFPB data, Fitch subprime auto, SoFi 10-K | CARL |
| `BANK_CRE` | Bank earnings, CRE exposure, hidden CRE (MI3/SSFA), NDFI, capital | Q1 earnings, Trepp, H.8, FFIEC call reports, AOCI proposals | REGINALD |
| `FUNDING_LIQUIDITY` | HY OAS, SOFR, repo, RRP, dealer capacity, Treasury auctions | FRED spreads, NY Fed SOFR, Treasury auction results, dealer surveys | LIQUID |
| `PRIVATE_CREDIT` | BDC gates, PC fund redemptions, PIK rates, software PE, PCDR | Bloomberg PC coverage, Fitch PCDR, BDC 10-Qs, Stanger reports | BROCK |
| `INSURANCE_SHADOW` | PE-insurer nexus, reinsurance, Level 3 assets, captive insurers | NAIC filings, Egan Jones reviews, insurance-owned asset manager news | SHADE |
| `OIL_ENERGY` | Crude prices, OPEC, facility damage, refining, shipping | Brent/WTI futures, dated Brent, Kpler flows, EIA, facility strike reports | HAWK |
| `GEOPOL_ENERGY` | Hormuz, Gulf infrastructure strikes, OPEC politics, chokepoints | Tanker tracking, facility damage tracker, Gulf state statements | HAWK |
| `GEOPOL_NON_ENERGY` | Ceasefires, diplomacy, nuclear program, non-supply war developments | Islamabad talks, nuclear inspection updates, ceasefire mechanics | HANS (Tier 2) |
| `JAPAN_BOJ` | USD/JPY, BOJ policy, JGB yields, carry trade, MOF intervention | BOJ meetings, JGB auctions, MOF weekly, USD/JPY intervention zones | SAM |
| `MARKET_VOL` | VIX, index moves, vol regime, dealer gamma, correlation breaks | CBOE VIX, SPX technical levels, MOVE index, put/call ratios | HENRY |
| `ASIA_CONTAGION` | China/HK peg, LGFV, HIBOR-SOFR, Chinese trade policy, supply-chain coercion, export-control regs, EM Asia spillover | EU Chamber reports, PBoC actions, HKMA stats, China export/tariff actions, FT China coverage | ZHAO (Tier 2) |
| `UST_FOREIGN` | TIC flows, foreign holder behavior in US Treasuries, auction demand composition from foreign accounts | Monthly TIC release, Treasury auction stats by foreign share, SAFE announcements | ZHAO (Tier 2) |

### What's deliberately NOT in this enum

- **`THESIS_CONFIRM` / `COUNTER_EVIDENCE`** — these are `signal_type` enum values, not domains. A LABOR signal can be either thesis-confirming or counter-evidence; the two axes are orthogonal.
- **`POSITION_RISK`** — also a `signal_type` value (`position-risk`). Position-specific signals inherit the domain of the underlying position.
- **`BROAD_STRESS`** — an escalation condition (multiple domains firing simultaneously), not a domain itself. Handled via safety net triggers + the `FULL_NETWORK` AIG.
- **`META`** (network coordination, spec changes, registry updates) — meta-signals don't carry a domain; the `signal_type: manual-flag` category captures them.

### How to use the vocabulary

- **ROUTING_TABLE.md** — every row labels its domain with the canonical code in the row header.
- **CHECKLIST.md** — Phase 2 classification and routing decision use the codes directly.
- **Signal file bodies** — when characterizing a signal's topic in prose, use the code (e.g., "this is a MACRO_INFLATION signal with LABOR second-order effects").
- **kill_log.tsv / route_log.tsv Summary column** — feel free to include the code inline for searchability.

### Adding a new domain

New domains earn their place only when:
1. A real signal arrives that doesn't fit any existing code
2. AND the new domain is likely to recur (not a one-off edge case)
3. AND it maps cleanly to a primary action recipient in ROUTING_TABLE

When all three are true: add to this table, bump FORMAT_SPEC version, propagate to ROUTING_TABLE + CHECKLIST per the canonical-source rule.

---

## Address Indicating Groups (AIGs)

Pre-defined recipient groups. Use the group name instead of listing agents individually.

| Group | Agents | Use Case |
|-------|--------|----------|
| `CREDIT_CHAIN` | LIQUID, BROCK, SHADE, REGINALD | Credit stress, funding, bank risk |
| `ENERGY_CHAIN` | HAWK, BRENT | Oil, energy, geopolitical supply |
| `THESIS_CORE` | CARL, REGINALD, SAM | Core thesis signals (labor → credit → repricing) |
| `LABOR_DOWNSTREAM` | CARL, HENRY | Employment data, wage/velocity signals |
| `FULL_NETWORK` | All active agents | System-wide alerts, FLASH signals |
| `ADVERSARIAL` | RED | Challenge requests, counter-evidence |

When a group is used, WALTER writes one file per agent in the group, with `to:` set to the primary action agent and `info:` for the rest — unless the routing table specifies otherwise.

---

## Dual Precedence in Practice

When routing to a group, the action recipient gets higher precedence than info recipients.

**Example:** HY OAS spike routed to CREDIT_CHAIN
- `AGENTS/LIQUID/inbox/SIG-WALTER-LIQUID-20260407-hy-oas-spike.md` → precedence: IMMEDIATE, to: LIQUID (ACTION)
- `AGENTS/BROCK/inbox/SIG-WALTER-BROCK-20260407-hy-oas-spike.md` → precedence: PRIORITY, to: BROCK (INFO)
- `AGENTS/SHADE/inbox/SIG-WALTER-SHADE-20260407-hy-oas-spike.md` → precedence: PRIORITY, to: SHADE (INFO)
- `AGENTS/REGINALD/inbox/SIG-WALTER-REGINALD-20260407-hy-oas-spike.md` → precedence: PRIORITY, to: REGINALD (INFO)

Same signal, same content, different precedence per recipient.

---

## MINIMIZE Protocol

When signal volume exceeds processing capacity, WALTER can declare MINIMIZE.

| Level | What Processes | What Defers |
|-------|---------------|-------------|
| **Normal** | All signals | Nothing |
| **MINIMIZE-1** | FLASH + IMMEDIATE + PRIORITY | ROUTINE deferred |
| **MINIMIZE-2** | FLASH + IMMEDIATE only | PRIORITY + ROUTINE deferred |
| **MINIMIZE-3** | FLASH only | Everything else deferred |

Deferred signals are held in `AGENTS/WALTER/queue/` and released when MINIMIZE is lifted. They are NOT dropped — just delayed.

---

## What This Spec Does NOT Cover (Yet)

- Agent-to-agent direct signals (still allowed, not standardized yet)
- Receipt/acknowledgment protocol (future spec)
- Superevent grouping (future spec, see Signal Registry Draft A)
- Re-triage intervals for queued signals (future spec)
- Escalation/readdressal by receiving agents (future spec)

---

*v0.8 — May 8, 2026 — Added 5 optional header fields per `JOINT_PROPOSAL_2026-05-05_walter_carl_brent.md` §2a + §2d.5 (3-way CARL+BRENT+WALTER cosigned 2026-05-05/06; Will-approved 2026-05-08): `cluster_secondary` (comma-separated, multi-cluster cross-tags) / `signal_role` (4-value enum: primary_substance / cluster_mediating / counter_evidence / thesis_confirmation; authoritative-voice precedence NEXUS > WALTER > action-primary on cluster_mediating) / `consumer_transmission` (9-value enum: pump_pass_through / wage_pressure / wealth_effect / policy_pass_through / discretionary_demand / services_export / lng_substitution / counter_evidence / none; tag only when CARL on routing line) / `consumer_lens` (4-value enum: tier_stratified / broad_collapse / mixed / counter; consumer-cluster signals with CARL on routing line only) / `event_window` (boolean: open|closed default closed; canonical state in `design/EVENT_WINDOW_STATE.md` per §2d state machine). All 5 fields **optional**; backwards-compatible (pre-v0.8 historical signals don't carry them). Forward-only adoption from 2026-05-08 dispatches; no retro-fit. Migration: WALTER tags `cluster_secondary` and `signal_role` always when applicable; `consumer_transmission` and `consumer_lens` only when CARL is on routing line; energy-cluster signals carry `consumer_transmission` only when consumer-side info recipient is on routing line. v0.7 cluster_mediating prose-tag interim discipline (paper-vs-structural / tape-vs-substance / bifurcation / divergence dispatch_note language carried operationally pre-v0.8) **retired** — header field is now canonical. ROUTING_TABLE v0.7 By Tag/By Verdict rules (cluster_mediating auto-cc to RED, CORRECTED-FRAMING auto-cc to RED, falsification_trigger auto-fire) compose with v0.8 — no rule change, just field is now formal not prose. BOARD INDEX section structure unchanged (primary-cluster-only); no INDEX migration. BOARD_LOG.tsv schema unchanged. Propagates to CHECKLIST v0.10 → v0.11 (Phase 2 tagging steps for new fields), ROUTING_TABLE v0.7 → v0.8 (By Boundary Threshold section per §2c, mechanic-aware routing notes), FILTER_SPEC v0.4 → v0.5 (OPEN-window Tuning Rules sub-section per §2d).*

*v0.7 — May 5, 2026 — Added `cluster` field to header schema (required for new signals dispatched 2026-05-05+; pre-v0.7 historical signals don't carry the field, their cluster placement lives in `/BOARD/INDEX.md` section structure only). Enum values from `design/CLUSTER_TAXONOMY.md` v0.1 (10 buckets: IRAN_HORMUZ / POSITIONING_VALUATION / BANK_COLLATERAL / CONSUMER_STAGFLATION / PC_STRESS / HYDROCARBON_INFRA / MISC / AI_INFRA_CAPEX / ASIA_CHINA / FED_FRAMEWORK). CLUSTER_TAXONOMY.md is canonical source — don't invent. Propagates to CHECKLIST v0.9 (cluster-assignment step in Phase 2) and `/BOARD/INDEX.md` cluster-section structure (Pass 2 of cluster-organization refactor).*

*v0.6 — April 20, 2026 (Filter v2 Segment B) — Added Multi-Origin Signals section codifying the same-theme combine rule. `origin` field now accepts array form for multi-origin signals. Combine criteria: same canonical domain AND same underlying event or specific sub-theme AND each origin adds independent value. Pre-dispatch any-arrival-path flexibility; post-dispatch immutability preserved (no retroactive merge). Cross-author combines supported (3 of 5 historical cases). No combine ceiling. Source section in signal body is the audit trail for absorbed origins. Propagates to CHECKLIST v0.7 with new Phase 1 step.*
*v0.5 — April 20, 2026 — Added `thesis-frame` to Signal Types enum. Covers analytical synthesis / institutional framework / comparative analysis content (e.g., MS 1990-vs-2026 oil-shock compare SIG-W-20260419-021, BRK-vs-SPY quality-flight read SIG-W-20260419-013, multi-channel convergence analyses). Distinct from `research` (new data/reports) and `pattern-match` (data pattern detection). Vocabulary gap surfaced in v1 filter review (Filter v2 Segment A). Propagates to ROUTING_TABLE v0.5 with corresponding By Signal Type row.*
*v0.4 — April 14, 2026 — Added 2 canonical domain codes: `ASIA_CONTAGION` (China/HK/LGFV/supply-chain, ZHAO primary) and `UST_FOREIGN` (TIC flows / foreign UST holder behavior, ZHAO primary). Both codes were already in REGISTRY.tsv as ZHAO's declared domain but missing from FORMAT_SPEC canonical list — vocabulary gap surfaced by 2026-04-14 FT China-trade signals SIG-W-20260414-010 and -011. Propagates to ROUTING_TABLE v0.4 with corresponding rows.*
*v0.3 — April 11, 2026 (PM) — Added Domain Vocabulary canonical reference section with 13 codes (LABOR, MACRO_INFLATION, TARIFF_TRADE, CONSUMER_CREDIT, BANK_CRE, FUNDING_LIQUIDITY, PRIVATE_CREDIT, INSURANCE_SHADOW, OIL_ENERGY, GEOPOL_ENERGY, GEOPOL_NON_ENERGY, JAPAN_BOJ, MARKET_VOL). Resolves Gap C. Not introduced as a `domain:` header field — used as shared vocabulary across ROUTING_TABLE, CHECKLIST, and signal bodies.*
*v0.2 — April 11, 2026 — Added optional dispatch-time fields (`dispatched`, `dispatch_note`). Clarified `to:` field supports both `(ACTION)` and `(INFO)` values.*
*v0.1 — April 7, 2026*
