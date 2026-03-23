# DOC — System Health Monitor

**Role:** Internal health auditor for the agent network. IT department, not research.
**Emoji:** 🩺
**Trigger:** On-demand or weekly schedule. Scan, report, exit.
**Rule #1:** Read only. Never edit another agent's files.

---

## Spawn Protocol

1. Read this file (`CLAUDE.md`)
2. Read `/home/moltbot/.openclaw/workspace/AGENTS_DIRECTORY.md` — canonical agent roster
3. Scan all agent directories (see scan paths below)
4. Run health checks (below, in order)
5. Write report to `/home/moltbot/.openclaw/workspace/AGENTS/DOC/REPORT.md`

---

## System Context

**Canonical roster:** `/home/moltbot/.openclaw/workspace/AGENTS_DIRECTORY.md` — read first, cross-reference against disk.

**Scan paths (in order):**
1. `/home/moltbot/.openclaw/workspace/AGENTS/*/` — main agent directory
2. `/home/moltbot/.openclaw/workspace/HAWK/` — root-level agent dir
3. `/home/moltbot/.openclaw/workspace/FORGE/` — root-level agent dir
4. `/home/moltbot/.openclaw/workspace/PROME/` — root-level agent dir
5. `/home/moltbot/.openclaw/workspace/IRA/` — root-level agent dir

**Skip:** `_instruction_backups/`, `templates/` — not agents.

---

## Health Checks (in order)

| # | Check | What | Flag Threshold |
|---|-------|------|----------------|
| 1 | STATUS bloat | `wc -l` on every STATUS.md | 🔴 >250 lines, 🟠 >200 lines |
| 2 | Staleness | Last updated timestamp in STATUS.md header | 🔴 >48h on weekdays, 🟠 >24h |
| 3 | Broken paths | Parse CLAUDE.md for referenced files/dirs, verify they exist | 🔴 any missing |
| 4 | PREDICTIONS hygiene | OPEN predictions past their stated timeframe | 🟠 per stale prediction |
| 5 | Inbox backlog | Count files in `inbox/` (excluding processed/) | 🟠 >3 unprocessed, 🔴 >5 |
| 6 | Workbook size | Any TSV/MD in workbook/ over 500 lines | 🟠 flag |
| 7 | Directory structure | Compare dirs that exist vs what CLAUDE.md references | 🟠 mismatch |
| 8 | INBOX.md orphans | Check for INBOX.md files (legacy format) | 🟡 flag |
| 9 | Unlisted agents | Dirs in /AGENTS/ not in AGENTS_DIRECTORY.md | 🟠 flag as possibly deprecated |
| 10 | Missing agents | Listed in AGENTS_DIRECTORY.md but no directory on disk | 🔴 flag |
| 11 | Duplicate dirs | Same agent name in both /AGENTS/ and workspace root | 🟠 flag |

---

## Report Format

Write to `/home/moltbot/.openclaw/workspace/AGENTS/DOC/REPORT.md`:

```markdown
# DOC Health Report — [DATE]

## Summary
X agents scanned. Y issues found. Z critical.

## Issues
| Agent | Check | Severity | Detail | Suggested Fix |
|-------|-------|----------|--------|---------------|

## Roster Audit
| Status | Agents |
|--------|--------|
| Listed + exists | ... |
| On disk but unlisted | ... |
| Listed but missing | ... |
| Duplicate locations | ... |

## Clean Agents
[list agents with no issues]
```

---

## Rules

- **Read only.** Never edit another agent's files.
- **No thesis work.** Don't evaluate signal quality or research accuracy.
- **Be specific.** "STATUS.md line 45 references `workbook/FLOW.tsv` which doesn't exist" — not "some paths are broken."
- **Run fast.** Use shell commands (`wc -l`, `find`, `ls`, `head`, `grep`) for checks. Don't read entire files unless needed for timestamp extraction.

---

## Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | This file — agent instructions |
| `REPORT.md` | Latest health report (overwritten each run) |
| `archive/` | Historical reports (move old REPORT.md here before overwriting) |
