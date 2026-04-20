# WALTER Signal Format Specification v0.5

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

# Optional dispatch-time fields (added when signal is routed to recipient inboxes)
dispatched: 2026-04-07T14:45:00Z
dispatch_note: "Trimmed from 4-recipient plan to CARL+RED after HENRY already processed"
---
```

### Field Definitions

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| `signal_id` | string | `SIG-W-YYYYMMDD-NNN` | Unique ID. W = WALTER-originated. Sequential per day. |
| `precedence` | enum | `FLASH` / `IMMEDIATE` / `PRIORITY` / `ROUTINE` | Processing urgency. See Precedence Levels below. |
| `timestamp` | ISO8601 | — | When WALTER classified this signal. |
| `source` | string | `WALTER` | Always WALTER for v0.1. |
| `origin` | string | Free text | Where the raw information came from. |
| `to` | string | `AGENT (ACTION)` or `AGENT (INFO)` | Primary recipient for this file. Per-recipient files get their own `to:` value when the same signal dispatches to multiple agents. |
| `info` | string | Comma-separated agents | Awareness recipients. Optional. |
| `group` | string | AIG name | Optional. Which Address Indicating Group, if any. |
| `signal_type` | enum | See Signal Types | What kind of signal this is. |
| `confidence` | float | 0.0–1.0 | Numerical confidence score. For machine routing and threshold filters. See Confidence Model below. |
| `confidence_language` | enum | `confirmed` / `reports` / `assessed` / `unconfirmed` | Human-readable confidence tier. For prose context. Must be consistent with `confidence` per the mapping below. |
| `resources` | int | 0 / 1 / 2 | Estimated processing resources needed. |
| `safety_net` | enum | `clear` / `triggered` | Whether safety net override was triggered. |
| `word_count` | int | — | Body word count. FLASH/IMMEDIATE must be ≤200. |
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

*v0.5 — April 20, 2026 — Added `thesis-frame` to Signal Types enum. Covers analytical synthesis / institutional framework / comparative analysis content (e.g., MS 1990-vs-2026 oil-shock compare SIG-W-20260419-021, BRK-vs-SPY quality-flight read SIG-W-20260419-013, multi-channel convergence analyses). Distinct from `research` (new data/reports) and `pattern-match` (data pattern detection). Vocabulary gap surfaced in v1 filter review (Filter v2 Segment A). Propagates to ROUTING_TABLE v0.5 with corresponding By Signal Type row.*
*v0.4 — April 14, 2026 — Added 2 canonical domain codes: `ASIA_CONTAGION` (China/HK/LGFV/supply-chain, ZHAO primary) and `UST_FOREIGN` (TIC flows / foreign UST holder behavior, ZHAO primary). Both codes were already in REGISTRY.tsv as ZHAO's declared domain but missing from FORMAT_SPEC canonical list — vocabulary gap surfaced by 2026-04-14 FT China-trade signals SIG-W-20260414-010 and -011. Propagates to ROUTING_TABLE v0.4 with corresponding rows.*
*v0.3 — April 11, 2026 (PM) — Added Domain Vocabulary canonical reference section with 13 codes (LABOR, MACRO_INFLATION, TARIFF_TRADE, CONSUMER_CREDIT, BANK_CRE, FUNDING_LIQUIDITY, PRIVATE_CREDIT, INSURANCE_SHADOW, OIL_ENERGY, GEOPOL_ENERGY, GEOPOL_NON_ENERGY, JAPAN_BOJ, MARKET_VOL). Resolves Gap C. Not introduced as a `domain:` header field — used as shared vocabulary across ROUTING_TABLE, CHECKLIST, and signal bodies.*
*v0.2 — April 11, 2026 — Added optional dispatch-time fields (`dispatched`, `dispatch_note`). Clarified `to:` field supports both `(ACTION)` and `(INFO)` values.*
*v0.1 — April 7, 2026*
