# Agent Directory & Routing Guide

> **Updated 2026-07-01 by PROME (Will-approved, cross-agent scope named in commit):** OpenClaw spawn framing retired (spawn-safe/persistent split + `sessions_spawn` template — all agents are Claude Code sessions now); stale static threshold bands replaced with owner-sourced trigger lines. **WALTER: re-own this file at next boot** — especially re-verify the trigger-lines table against your own routing needs.

## Active Agents

All agents run as Claude Code sessions — there is no spawn-safe vs persistent split. Route signals by **writing the owning agent's inbox** (locations below) per `AGENTS/WALTER/design/SIGNAL_PROCESSING_CHECKLIST.md`; live multi-agent orchestration is PROME's lane (teams-mode). Live/Tier-2/dormant classification → `PROME/ROSTER.md` (single source of truth).

| Agent | Domain | Chain | Key Signals |
|-------|--------|-------|-------------|
| **WALTER** | Signal intelligence | All (feeds all) | Images, articles, transcripts, headlines, PDFs |
| **LABOR** | Employment, claims | Credit | NFP, claims, shadow adjustment, FL Wave |
| **CARL** | Consumer credit, housing | Credit | Delinquencies, housing, mortgage stress, consumer ABS |
| **REGINALD** | Regional banks (OZK, WAL) | Credit | KRE/OZK/WAL, CRE concentration, AOCI, bank prints |
| **HENRY** | Market structure, econ data | Credit (velocity) | HY OAS, CCC, VIX, dealer capacity, liquidity |
| **LIQUID** | Funding, Treasury, spreads | All (amplification) | SOFR, repo, TGA, SLR, systemic risk |
| **BROCK** | BDC, private credit, CLOs | PC cascade | Gates, redemptions, marks, NAV, PC stress |
| **SHADE** | PE-insurance-captive | PC cascade | Reinsurance, XOL, annuity, Athene, captives |
| **SAM** | Japan, BOJ, carry trade | Japan | BOJ, USD/JPY, carry unwind, JGB, MOF intervention |
| **HAWK** | Geopolitical, military | Energy | Iran, Hormuz, war escalation, supply disruption |
| **BRENT** | Oil, energy markets | Energy | Brent/WTI, Cushing, crack spreads, OPEC, decoupling |
| **RED** | Adversarial analysis | All | Thesis challenges, steelman requests, consensus breaks |
| **MARCO** | Migration, labor supply | Credit + Energy | Immigration, H-2A, ag labor, demographics |
| **ZHAO** | China, capital flows | Japan + PC | TIC, UST flows, China outflows, Gulf SWF |
| **OTTO** | Auto, consumer DQ | Credit (→ CARL) | Auto loans, delinquency, First Brands, parts |
| **NEXUS** | Cross-agent synthesis | All | Convergence tracking, thesis validation |

## Routing Rules

### Credit Chain (LABOR → CARL → REGINALD)
- Labor market weakness → LABOR
- Consumer credit stress → CARL
- Bank/CRE stress → REGINALD

### PC Cascade (BROCK → SHADE → LIQUID)
- PC gates/redemptions → BROCK
- Insurance/reinsurance → SHADE
- Systemic amplification → LIQUID

### Energy Shock (HAWK → BRENT → HENRY)
- War/geopolitical → HAWK
- Oil market structure → BRENT
- Macro transmission → HENRY

### Capital Flows (ZHAO → LIQUID → SAM)
- China/Gulf UST flows → ZHAO
- Funding stress → LIQUID
- Japan/carry unwind → SAM

## Priority Trigger Lines

**Canonical bands live with their owners** — `FORGE/tools/market-data/config.py`, the RESEARCH-INTAKE lane's auto-emitted alerts, and owner workbooks. Do not grade a print against static bands in this file; the rows below carry the live trigger lines *as of 2026-07-01* with their canonical source. *(The old static Green/Yellow/Red table was badly stale — e.g. it graded HY OAS <300 "green" while the live X1 trigger is >280.)*

| Indicator | Live trigger lines (7/1) | Agents | Canonical source |
|-----------|--------------------------|--------|------------------|
| HY OAS | Bands 240/260/270/280; **>280 sustained = X1 breach** (LIQUID's half); <260 two closes = re-kill | LIQUID, HENRY, PROME | `AGENTS/LIQUID/workbook/KILL_MEMO_HY_OAS_260.md` + intake-lane fred feed (auto-alerts) |
| Wrapper basket (ARCC/FSK/OBDC/BIZD) | Wrappers **leading managers down** = BROCK's X1 half (both halves must fire) | BROCK | `AGENTS/BROCK/` discriminator docs |
| CCC / HY ratio | REGINALD tripwire **3.6×** (quality-dispersion recognition) | REGINALD, HENRY | REGINALD workbook; HEARTBEAT §Regime |
| Brent | Decoupling line **~$74-75** on kinetic shocks (shrug test); level bands secondary | BRENT, HAWK | BRENT boundaries |
| Cushing | **<21M orange / <20M = Boundary #3 red** | BRENT | Intake-lane EIA feed (auto-alerts) |
| USD/JPY | MOF intervention zone **~162-163** (SAM S1; rate-checks = pre-strike tell) | SAM, LIQUID | `AGENTS/SAM/` |
| SOFR-IORB | >+0.25 = funding stress red | LIQUID | `config.py` |
| VIX | Owner band pending (VIOLET) — intake CFTC-VIX feed is track-only until set | VIOLET, HENRY | `AGENTS/VIOLET/` |
| Gas AAA | $3.50 / $4.00 bands *(unverified 7/1 — BRENT/CARL to confirm)* | BRENT, HENRY | CARL GAS_TRACKER / BRENT |

## Inbox Locations

```
AGENTS/{AGENT_NAME}/inbox/
├── signal_YYYY-MM-DD_{description}.md
├── research_YYYY-MM-DD_{description}.md
└── alert_YYYY-MM-DD_{description}.md
```
