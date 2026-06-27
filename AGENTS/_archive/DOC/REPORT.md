# DOC Health Report — 2026-03-20

## Summary
31 agent directories scanned (AGENTS/ + root-level). **45 issues found. 18 critical (🔴).**

---

## Issues

| Agent | Check | Severity | Detail | Suggested Fix |
|-------|-------|----------|--------|---------------|
| REGINALD | STATUS bloat | 🔴 | 1170 lines | Urgently prune — archive pre-Mar entries |
| LIQUID | STATUS bloat | 🔴 | 610 lines | Archive older entries |
| HAWK (AGENTS/) | STATUS bloat | 🔴 | 530 lines | Archive older entries |
| BRENT | STATUS bloat | 🔴 | 492 lines | Archive older entries |
| CORAL (REG sub) | STATUS bloat | 🔴 | 446 lines | Archive pre-Mar entries |
| CREED (REG sub) | STATUS bloat | 🔴 | 379 lines | Archive older entries |
| RENO (REG sub) | STATUS bloat | 🔴 | 330 lines | Archive older entries |
| CARL | STATUS bloat | 🔴 | 310 lines | Archive older entries |
| LABOR | STATUS bloat | 🔴 | 281 lines | Archive pre-Mar entries |
| TEX (REG sub) | STATUS bloat | 🔴 | 278 lines | Archive older entries |
| ZHAO | STATUS bloat | 🔴 | 269 lines | Archive older entries |
| HANS | STATUS bloat | 🔴 | 264 lines | Archive older entries |
| OTTO | STATUS bloat | 🔴 | 255 lines | Archive older entries |
| PROME (root) | STATUS bloat | 🟠 | 230 lines | Approaching threshold |
| DARWIN | Staleness | 🔴 | Last updated 2026-02-18 (30 days) | Needs check-in spawn |
| SHADE | Staleness | 🔴 | Last updated 2026-03-03 (17 days) | Needs check-in spawn |
| HANS | Staleness | 🔴 | Last updated 2026-03-11 (9 days) | Needs check-in spawn |
| ATHENA | Staleness | 🟠 | Last updated 2026-03-14 (6 days) | Check-in recommended |
| RED | Staleness | 🟠 | Last updated 2026-03-14 (6 days) | Check-in recommended |
| POLLY (CARL sub) | Staleness | 🔴 | Last updated 2026-02-13 (35 days) | Needs check-in |
| POP (CARL sub) | Staleness | 🔴 | Last updated 2026-02-13 (35 days) | Needs check-in |
| GIG (CARL sub) | Staleness | 🔴 | Last updated 2026-02-12 (36 days) | Needs check-in |
| DOC (CARL sub) | Staleness | 🔴 | Last updated 2026-02-13 (35 days) | Needs check-in |
| NICK (CARL sub) | Staleness | 🔴 | Last updated 2026-02-13 (35 days) | Needs check-in |
| RENO (REG sub) | Staleness | 🔴 | Last updated 2026-02-11 (37 days) | Needs check-in |
| CREED (REG sub) | Staleness | 🔴 | Last updated 2026-02-25 (23 days) | Needs check-in |
| TEX (REG sub) | Staleness | 🔴 | Last updated 2026-02-11 (37 days) | Needs check-in |
| BELT (REG sub) | Staleness | 🟠 | Last updated 2026-02-17 (31 days) | Check-in recommended |
| IRA | Staleness | 🟠 | Last updated 2026-02-26 (22 days) | Check-in recommended |
| FORGE | Staleness | 🟠 | Last updated 2026-03-06 (14 days) | Update positions |
| PROME (root) | Staleness | 🟠 | Last updated 2026-03-12 (8 days) | Check-in recommended |
| BRENT | Inbox backlog | 🔴 | 9 unprocessed in mail/inbox/ | Process or archive |
| REGINALD | Inbox backlog | 🔴 | 9 unprocessed in mail/inbox/ | Process or archive |
| LABOR | Inbox backlog | 🔴 | 8 unprocessed in mail/inbox/ | Process or archive |
| HAWK | Inbox backlog | 🟠 | 4 unprocessed in mail/inbox/ | Process during next check-in |
| PROME (root) | Inbox backlog | 🟠 | 4 unprocessed in mail/inbox/ | Process during next check-in |
| HANS | Inbox backlog | 🟠 | 3 unprocessed in mail/inbox/ | Process during next check-in |
| NEXUS | Inbox backlog | 🟠 | 3 unprocessed in mail/inbox/ | Process during next check-in |
| RED | Workbook size | 🟠 | workbook/RUSSIAN_OIL_CHALLENGE.md — 662 lines | Consider splitting or archiving |
| LIQUID | INBOX.md orphan | 🟡 | Legacy INBOX.md exists | Migrate to mail/inbox/ or archive |
| CARL | INBOX.md orphan | 🟡 | Legacy INBOX.md exists (+ one in archive/) | Migrate or remove |
| NEXUS | INBOX.md orphan | 🟡 | Legacy INBOX.md exists | Migrate to mail/inbox/ or archive |
| HENRY | INBOX.md orphan | 🟡 | Legacy INBOX.md exists | Migrate to mail/inbox/ or archive |
| SAM | INBOX.md orphan | 🟡 | Legacy INBOX.md exists | Migrate to mail/inbox/ or archive |
| PROME (AGENTS/) | INBOX.md orphan | 🟡 | Legacy INBOX.md exists | Migrate to mail/inbox/ or archive |

---

## Structural Issues

| Agent/Dir | Issue | Detail |
|-----------|-------|--------|
| BARON | No STATUS.md | Directory exists but empty/no status tracking |
| BUFFER | No STATUS.md | Directory exists but empty/no status tracking |
| EARNINGS | No STATUS.md | Directory exists but empty/no status tracking |
| FOREX | No STATUS.md | Directory exists but empty/no status tracking |
| HERMES | No STATUS.md | Listed as 🟢 in directory but has no STATUS.md |
| REITS | No STATUS.md | Directory exists but empty/no status tracking |
| CREED (AGENTS/) | No CLAUDE.md | Top-level CREED exists but has no CLAUDE.md (separate from REGINALD/sub-agents/CREED) |
| TRADES (AGENTS/) | No CLAUDE.md or STATUS.md | Unclear purpose — not in AGENTS_DIRECTORY.md |
| PROME (AGENTS/) | No CLAUDE.md or STATUS.md | Shell directory — real PROME is at workspace root |

---

## Roster Audit

| Status | Agents |
|--------|--------|
| **Listed + exists** | LABOR, CARL, REGINALD, BROCK, HENRY, LIQUID, SAM, ZHAO, HANS, NEXUS, SHADE, HERMES, ATHENA, HAWK, BRENT, BARON, MARCO, RED, DARWIN, BUFFER, EARNINGS, FOREX, OTTO, REITS, FERT, CRUISE, FORGE (root) |
| **On disk but unlisted** | RESEARCHER, TRADES, PROME (AGENTS/), CREED (AGENTS/ top-level — distinct from REGINALD sub-agent) |
| **Listed but missing on disk** | MERLIN (listed as "Not yet built") |
| **Duplicate locations** | HAWK (AGENTS/ + root), BRENT (AGENTS/ + root — though root may be symlink/leftover), CARL (AGENTS/ + root), LABOR (AGENTS/ + root), PROME (AGENTS/ + root) |

---

## Clean Agents
- CARL *(current, but sub-agents all stale)*
- BROCK
- FERT
- CRUISE
- MARCO
- ZHAO
- SAM
- LIQUID *(current, but bloated + INBOX.md orphan)*
- OTTO *(current, but bloated)*

*Note: Very few agents are fully clean. Most have at least bloat or staleness issues.*

---

## Top Priorities

1. **🔴 STATUS bloat is epidemic.** 13 agents/sub-agents exceed 250 lines. REGINALD at 1170 lines is nearly 5x the threshold. Mass archive needed.
2. **🔴 CARL's 5 sub-agents are ALL 35+ days stale.** None updated since mid-February. Either spawn batch check-ins or document them as dormant.
3. **🔴 REGINALD's sub-agents (RENO, TEX, CREED) are 23-37 days stale** while the parent is actively updated. Sub-agent data may be dangerously outdated.
4. **🔴 Inbox backlog:** BRENT (9), REGINALD (9), LABOR (8) have significant unprocessed mail.
5. **🟠 5 duplicate agent directories** between AGENTS/ and workspace root need consolidation or documentation of which is canonical.
6. **🟡 12 legacy INBOX.md files** should be migrated to mail/inbox/ format or archived.
