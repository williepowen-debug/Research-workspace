# BOARD Consumption Spec

**Version:** v0.1
**Created:** 2026-04-20
**Owner:** WALTER
**Status:** Shipped. Propagation to agent CLAUDE.md files pending.

---

## Purpose

Every BOARD signal is archived at `/BOARD/` with `/BOARD/INDEX.md` as the discovery table. WALTER owns all writes. **Agents need a way to boot, identify new-to-them BOARD signals, read them, and record disposition** — without re-reading 57+ signals every session or missing new ones.

This spec defines the per-agent tracking mechanism that turns BOARD from write-only archive into a functioning pub/sub layer.

## Decision Summary

Each agent maintains `AGENTS/<NAME>/board_log.tsv` — a local, append-only record of which BOARD signals the agent has read and what it did with them. Boot sequence reads INDEX + own board_log, processes the diff.

Option decided 2026-04-20 (Will msg 938) from 4 surveyed:

| Option | Chosen? | Reason |
|--------|---------|--------|
| Watermark (single timestamp in STATUS.md) | ❌ | Too coarse — can't distinguish acted vs ignored within a batch |
| Signal Ledger inside STATUS.md | ❌ | Mixes state with config; inflates STATUS.md; hard to tail |
| **Per-agent TSV (`board_log.tsv`)** | ✅ | Clean separation; greppable; matches existing route_log.tsv / kill_log.tsv pattern in WALTER |
| Git-native (diff INDEX since agent's last commit) | ❌ | Fragile — breaks if agent doesn't commit regularly |

---

## Schema

File: `AGENTS/<NAME>/board_log.tsv`

Tab-separated, one row per consumed signal, append-only.

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| `timestamp_read` | ISO 8601 UTC | yes | When agent read the signal (e.g., `2026-04-21T14:32:00Z`) |
| `signal_id` | string | yes | Matches BOARD filename (`SIG-W-YYYYMMDD-NNN`) |
| `disposition` | enum | yes | One of: `acted` / `noted` / `deferred` / `info-only` / `skipped` |
| `notes` | free text | no | Optional. Link to agent output, why deferred, why skipped, etc. |

### Disposition values

| Value | Meaning |
|-------|---------|
| `acted` | Incorporated into this session's analysis, position decision, or downstream dispatch |
| `noted` | Read and filed; no action this boot, no follow-up expected |
| `deferred` | Will revisit — use `notes` to say when/why (e.g., "post-OWL earnings Apr 30") |
| `info-only` | Agent is named in the `info` column of INDEX; read for awareness, no action expected |
| `skipped` | Agent judged irrelevant despite WALTER routing — rare; create paper trail for routing-disagreement audit |

### Header row

Files initialize with this exact header:

```
timestamp_read	signal_id	disposition	notes
```

---

## Retention

**No cap.** Files grow append-only.

- At ~150 signals/month = ~1,800/year, the file stays <1MB even at 10-year horizon.
- Boot scan is O(ms) at that scale.
- Adding cap logic now = complexity for zero current benefit. If boot speed becomes real issue later, add tail-N read logic; do not archive.

Entire file is in git. Audit trail permanent.

---

## Agent Boot Step Template

Each agent's `AGENTS/<NAME>/CLAUDE.md` adds this block to the boot sequence (typically immediately after reading STATUS.md / MEMORY.md / LAST_COMPLETION.md and before starting the task):

```markdown
### BOARD signal intake

After reading STATUS/MEMORY/LAST_COMPLETION, scan BOARD for signals new to you:

1. If `AGENTS/<YOU>/board_log.tsv` does not exist, create it with this header row:
   ```
   timestamp_read	signal_id	disposition	notes
   ```
2. Read `/BOARD/INDEX.md`. Note rows naming you in the `to` column (action recipient) or `info` column (awareness recipient).
3. Read your own `AGENTS/<YOU>/board_log.tsv`. Note which `signal_id` values are already logged.
4. For each INDEX row naming you that is NOT yet in your board_log:
   - Read the BOARD file: `/BOARD/<signal_id>-<slug>.md`
   - Decide disposition: `acted` / `noted` / `deferred` / `info-only` / `skipped`
   - Append one row to `board_log.tsv` with disposition and (optionally) a brief note
5. Let `acted` signals inform this session's work.
```

Each agent replaces `<YOU>` with their own name (e.g., `AGENTS/BROCK/board_log.tsv`).

---

## Initialization

Each agent creates its own `board_log.tsv` on first boot after this spec propagates — **WALTER does NOT pre-create files in other agents' directories** (git isolation rule).

First-boot logic (included in the template below): if `AGENTS/<YOU>/board_log.tsv` does not exist, create it with the header row, then proceed with normal boot-step scan. After first run, the file exists and boot-step just appends.

**No backfill.** Historical BOARD signals (SIG-W-20260410-001 through current) are NOT auto-logged; if an agent wants to retrospectively consume, they can:

- Log the whole history at first boot as `disposition: noted` (paper-trail only), or
- Skip the history and only track forward from the first post-spec boot.

Default = skip-history. Retrospective consumption is optional per agent.

---

## WALTER's Role

WALTER:
- Continues to own all `/BOARD/` writes (signal files + INDEX.md rows + route_log appends).
- **Does NOT write to any agent's `board_log.tsv`.** That file is owned by the agent.
- Can `grep` across agent `board_log.tsv` files to audit which signals have been consumed vs. orphaned — useful for COP integration or surfacing routing gaps.

Agents:
- Own their own `board_log.tsv` (append at boot per the template above).
- Never write to another agent's `board_log.tsv`.
- Never write to `/BOARD/` itself — BOARD is WALTER-only.

---

## Propagation Status

Active agents needing the boot-step block added to their `CLAUDE.md` (14 Tier 1):

| Agent | Platform | CLAUDE.md owned by | Status |
|-------|----------|--------------------|--------|
| CARL | Claude Code | self-edit | pending |
| REGINALD | Claude Code | self-edit | pending |
| SAM | Claude Code | self-edit | pending |
| RED | Claude Code | self-edit | pending |
| BROCK | OpenClaw | Prome / Will | pending |
| LIQUID | OpenClaw | Prome / Will | pending |
| HENRY | OpenClaw | Prome / Will | pending |
| HAWK | OpenClaw | Prome / Will | pending |
| BRENT | OpenClaw | Prome / Will | pending |
| LABOR | OpenClaw | Prome / Will | pending |
| NEXUS | OpenClaw | Prome / Will | pending |
| VIOLET | OpenClaw | Prome / Will | pending |
| PROME | OpenClaw | Prome / Will | pending |
| SHADE | OpenClaw | Prome / Will | pending |

**WALTER does not edit other agents' CLAUDE.md files** (per root CLAUDE.md git isolation rule). Each agent (or Will as operator) applies the boot-step block using the template above. Once applied, the agent creates its own `board_log.tsv` on first boot via step 1 of the template.

---

## Future Extensions (Deferred)

- **Cross-agent query:** WALTER could surface "signals with 0 consumers after 7 days" as routing-gap telemetry. Not in v0.1.
- **Disposition analytics:** agent-level skipped-rate tracking to detect persistent WALTER mis-routing. Not in v0.1.
- **COP integration:** include per-agent "unread BOARD count" in COP when COP refresh resumes. Not in v0.1.

---

## Version History

- **v0.1** — 2026-04-20 — initial spec shipped. Defaults approved by Will via Telegram msg 938.
