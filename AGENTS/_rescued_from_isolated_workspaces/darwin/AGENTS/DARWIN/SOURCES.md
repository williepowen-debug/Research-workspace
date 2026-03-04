# SOURCES.md - Darwin's Monitoring Sources

Last updated: 2026-02-18

## Tier 1: Daily (core signal)

| Source | URL | What to look for |
|--------|-----|-----------------|
| Hacker News | https://news.ycombinator.com/ | AI/agent/LLM posts >300pts |
| Simon Willison | https://simonwillison.net/ | Model releases, agent patterns, tools — best human curation |
| GitHub Trending | https://github.com/trending + `/python?since=daily` | New AI/agent repos, skill ecosystems |
| GitHub Search | `topic:agents created:>LAST_SCAN stars:>50` | Newly launched agent tools |
| Anthropic Blog | https://www.anthropic.com/news | Model releases, API changes |
| OpenClaw GitHub | https://github.com/openclaw + ecosystem | Skills, plugins, extensions |
| llm-stats.com | https://llm-stats.com/llm-updates | Real-time model release tracker — daily |

## Tier 2: Weekly (slower signal)

| Source | URL | What to look for |
|--------|-----|-----------------|
| arXiv cs.AI | https://arxiv.org/list/cs.AI/recent | Agent memory, orchestration, retrieval |
| arXiv cs.CL | https://arxiv.org/search/?query=multi-agent+LLM&order=-announced_date_first | Multi-agent frameworks |
| GitHub Blog | https://github.blog/ai-and-ml/ | Infrastructure changes affecting agents |
| VentureBeat AI | https://venturebeat.com/ai/ | New tools, funding signals |
| DEV.to | https://dev.to/t/agents + /t/mcp | MCP developments, practitioner posts |

## Tier 3: Occasional (spot checks)

| Source | URL | What to look for |
|--------|-----|-----------------|
| mem0 releases | https://github.com/mem0ai/mem0/releases | Memory API changes |
| browser-use | https://github.com/browser-use/browser-use | Browser agent improvements |
| MCP Registry | https://github.com/modelcontextprotocol/servers | New official MCP servers |
| RAGFlow releases | https://github.com/infiniflow/ragflow/releases | RAG improvements |
| WebMCP spec | https://webmcp.link | W3C standard updates |
| llms.txt registry | https://llmstxt.org | Sites publishing machine-readable access instructions |

## Search Queries (GitHub API)

```bash
# New agent repos this month
curl "https://api.github.com/search/repositories?q=stars:>50+created:>LAST_MONTH+topic:agents&sort=stars"

# New MCP servers
curl "https://api.github.com/search/repositories?q=stars:>20+created:>LAST_MONTH+topic:mcp&sort=stars"

# OpenClaw ecosystem
curl "https://api.github.com/search/repositories?q=openclaw&sort=stars"
```

## Notes

- GitHub trending page is JS-rendered; use GitHub Search API instead
- Rate limit on Brave Search: 1 req/sec, 2000/month — batch searches carefully
- VentureBeat blocks crawlers; use web_search to find articles then fetch
- arXiv full listings need specific search queries, not /list/recent (returns IDs only)
