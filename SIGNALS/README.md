# SIGNALS — Signal Routing System

## Purpose
Central depot for extracted signals, images, and agent-specific routing. Prome deposits here; agents read from here.

## Directory Structure

```
SIGNALS/
├── inbox/          # Raw signals before routing (general dump)
├── agents/         # Agent-specific signals (token-efficient)
│   ├── HAWK/
│   ├── BRENT/
│   ├── REGINALD/
│   ├── CARL/
│   ├── LIQUID/
│   ├── SAM/
│   ├── ZHAO/
│   ├── LABOR/
│   ├── MARCO/
│   ├── BROCK/
│   ├── SHADE/
│   ├── OTTO/
│   ├── HENRY/
│   ├── RED/
│   └── NEXUS/
├── images/         # Original image files (PNG, JPG)
├── briefings/      # SENTRY cross-domain synthesis (future)
└── archive/        # Signals >30 days old
```

## File Naming Convention

```
YYYY-MM-DD-topic[-source].md
```

Examples:
- `2026-04-30-brent-122-spike.md`
- `2026-04-30-hban-earnings-beat.md`
- `2026-04-30-iran-hormuz-closure.md`

## Format Template

```markdown
# Signal: [Topic]
**Date:** YYYY-MM-DD
**Source:** [URL, image, tweet, etc.]
**Routed to:** [Agent names]
**Priority:** 🔴 / 🟠 / 🟡 / 🟢

## Extracted Content
[Text extracted from image, or summary of signal]

## Key Points
- Point 1
- Point 2

## Context
[How this relates to current thesis/positions]

## Action Required
[What agent should do with this]
```

## Routing Rules

| Signal Type | Route To |
|-------------|----------|
| Iran/Israel/Military | HAWK |
| Oil/Energy/Diesel | BRENT |
| Bank Earnings/CRE | REGINALD |
| Consumer/Credit/Auto | CARL, OTTO |
| Rates/Fed/Treasury | LIQUID, HENRY |
| Japan/BOJ/Yen | SAM |
| China/Capital Flows | ZHAO |
| Jobs/Claims/Labor | LABOR |
| Immigration/Border | MARCO |
| BDC/Private Credit | BROCK |
| PE/Insurance | SHADE |
| Cross-domain / Synthesis | NEXUS, RED |

## Agent Instructions

On boot or check-in, read your folder:
```bash
ls SIGNALS/agents/{YOUR_NAME}/
```

Process signals in priority order (🔴 first). Move processed signals to `archive/` or mark as read.

## Prome Instructions

When Will forwards a signal:
1. Analyze image/text
2. Determine relevant agent(s)
3. Write to `SIGNALS/agents/{NAME}/YYYY-MM-DD-topic.md`
4. Git add + commit + push
5. Optionally notify agent via Telegram

---
*Created: 2026-04-30*
