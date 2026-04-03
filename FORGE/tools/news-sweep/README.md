# News Sweep — v2

Thesis-tagged news monitoring with entity classification, WATCH_FOR gap detection, and agent inbox routing.

## Quick Start
```bash
# Full sweep with Telegram-friendly output
python3 FORGE/tools/news-sweep/sweep.py --compact

# Full sweep + route to agent inboxes
python3 FORGE/tools/news-sweep/sweep.py --compact --route

# Single agent view
python3 FORGE/tools/news-sweep/sweep.py --compact --agent BROCK

# Full markdown output
python3 FORGE/tools/news-sweep/sweep.py

# JSON output
python3 FORGE/tools/news-sweep/sweep.py --json
```

## Schedule
- **M-F 8:30 AM ET**: auto (cron, before agent check-ins)
- **On-demand**: when Will asks

## Architecture

**Sources** (~45 sec sweep):
- 15 Google News RSS feeds (thesis-specific queries)
- 3 RSS feeds (FT, BBC Business, BBC World)
- 1 web scrape (ZeroHedge)

**Classification pipeline** (per article):
1. Noise filter → skip junk (CRE awards, FDIC conferences, etc.)
2. Keyword scoring → ALERT / WATCH / NORMAL
3. Entity matching → known entity? which agents?
4. WATCH_FOR matching → does this fill an agent's knowledge gap?
5. Escalation qualifier → known entity + "SEC"/"bankruptcy"/etc. = DEVELOPMENT

**Classifications:**
| Classification | Meaning | Routed? | Will sees? |
|---|---|---|---|
| NEW_WATCH_HIT | Matches agent WATCH_FOR list | ✅ | ✅ 🔴 |
| NEW_ALERT | Unknown entity + alert keyword | ✅ | ✅ 🔴 |
| DEVELOPMENT | Known entity + escalation qualifier | ✅ | ✅ 🟡 |
| NEW_WATCH | Unknown entity + watch keyword | ✅ | ✅ 🟡 |
| NEW | No special match, tagged by query | ✅ | Count only |
| KNOWN | Known entity, no escalation | ❌ suppressed | Density count |
| NOISE | Matched noise filter | ❌ suppressed | ❌ |

**Outputs:**
- Agent inboxes: `AGENTS/{name}/inbox/sweep_{date}_{time}.md`
- Latest: `FORGE/tools/news-sweep/latest.json` + `latest.md`
- Seen cache: `FORGE/tools/news-sweep/.cache/seen.json` (24h dedup)

## Config Files
- `config.py` — ALL configuration:
  - `GOOGLE_NEWS_QUERIES` — search feeds
  - `RSS_FEEDS` / `WEB_SCRAPE` — direct sources
  - `SOURCE_WEIGHT` — quality ranking
  - `ENTITY_INDEX` — known entities → agents (manually curated)
  - `WATCH_FOR` — agent gap lists (maintained by Prome)
  - `ALERT_KEYWORDS` / `WATCH_KEYWORDS` — keyword scoring
  - `ESCALATION_QUALIFIERS` — KNOWN → DEVELOPMENT triggers
  - `NOISE_TITLE_PATTERNS` — auto-skip patterns

## Maintenance
- **ENTITY_INDEX**: Update after major STATUS changes. ~50 entities.
- **WATCH_FOR**: Update after agent check-ins produce COMPLETION_SPECs. Prome owns this.
- **Noise filters**: Add patterns when junk slips through.
- **Source weights**: Adjust if source quality changes.

## Design Principles
Based on research (TDT/FSD, Trilogy Knowledge Tree, Salesforce EDR, Google Memory Bank, DeepMind multi-agent):
- **Forward-looking** (WATCH_FOR) over backward-looking (known signals)
- **Centralized sweep** (supervisor pattern) — agents are processors, not collectors
- **Entity index** for cross-agent routing and convergence detection
- **Source weighting** for quality-ranked dedup
- **Two-tier memory**: inbox = short-term, STATUS = long-term
