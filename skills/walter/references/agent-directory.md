# Agent Directory & Routing Guide

## Active Agents (Spawn-Safe)

| Agent | Domain | Chain | Spawn? | Key Signals |
|-------|--------|-------|--------|-------------|
| **WALTER** | Signal intelligence | All (feeds all) | ✅ | Images, articles, transcripts, headlines, PDFs |
| **LABOR** | Employment, claims | Credit | ✅ | NFP, claims, shadow adjustment, FL Wave |
| **HENRY** | Market structure, econ data | Credit (velocity) | ✅ | HY OAS, CCC, VIX, dealer capacity, liquidity |
| **LIQUID** | Funding, Treasury, spreads | All (amplification) | ✅ | SOFR, repo, TGA, SLR, systemic risk |
| **BROCK** | BDC, private credit, CLOs | PC cascade | ✅ | Gates, redemptions, marks, NAV, PC stress |
| **SHADE** | PE-insurance-captive | PC cascade | ✅ | Reinsurance, XOL, annuity, Athene, captives |
| **HAWK** | Geopolitical, military | Energy | ✅ | Iran, Hormuz, war escalation, supply disruption |
| **MARCO** | Migration, labor supply | Credit + Energy | ✅ | Immigration, H-2A, ag labor, demographics |
| **ZHAO** | China, capital flows | Japan + PC | ✅ | TIC, UST flows, China outflows, Gulf SWF |
| **OTTO** | Auto, consumer DQ | Credit (→ CARL) | ✅ | Auto loans, delinquency, First Brands, parts |
| **NEXUS** | Cross-agent synthesis | All | ✅ | Convergence tracking, thesis validation |

## Persistent Agents (Do NOT Spawn)

| Agent | Domain | Contact Method |
|-------|--------|----------------|
| **CARL** | Consumer credit, housing | Claude Code / Telegram |
| **REGINALD** | Regional banks (OZK, WAL) | Claude Code / Telegram |
| **RED** | Adversarial analysis | Claude Code / Telegram |
| **SAM** | Japan, BOJ, carry trade | Claude Code / Telegram |
| **BRENT** | Oil, energy markets | Claude Code / Telegram |

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

## Priority Thresholds

| Indicator | Green | Yellow | Red | Agents |
|-----------|-------|--------|-----|--------|
| HY OAS | <300 | 300-320 | >320 | HENRY, LIQUID |
| CCC OAS | <900 | 900-1000 | >1000 | HENRY, BROCK |
| CCC/HY ratio | <2.5 | 2.5-2.8 | >2.8 | HENRY, LIQUID |
| Gas AAA | <$3.50 | $3.50-4.00 | >$4.00 | BRENT, HENRY |
| Brent | <$85 | $85-100 | >$100 | BRENT, HAWK |
| USD/JPY | <150 | 150-158 | >158 | SAM, LIQUID |
| SOFR-IORB | <+0.05 | 0.05-0.25 | >0.25 | LIQUID |
| VIX | <20 | 20-30 | >30 | HENRY, LIQUID |

## Spawn Command Template

```bash
# For spawn-safe agents
sessions_spawn:
  task: "Check in on [DOMAIN]. Review [SPECIFIC FILES]. Report on [THESIS RELEVANCE]."
  agentId: [AGENT_NAME]
  runtime: "subagent"
  mode: "run"
  timeoutSeconds: 300
```

## Inbox Locations

```
AGENTS/{AGENT_NAME}/inbox/
├── signal_YYYY-MM-DD_{description}.md
├── research_YYYY-MM-DD_{description}.md
└── alert_YYYY-MM-DD_{description}.md
```
