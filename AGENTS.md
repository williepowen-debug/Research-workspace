# AGENTS.md - Your Workspace

## System Purpose

Research operation tracking systemic financial risk. Goal: detect stress transmission early enough to position ahead of consensus.

**Transmission Chain:**
```
LABOR → CARL → REGINALD → market repricing
         ↓
       HENRY (velocity) → LIQUID (amplification)

SAM (Japan) runs parallel — can trigger independently via carry unwind

NEXUS synthesizes across all agents → convergence/contradiction detection → PROME
```

---

## Boot

At session start, read `PROME/BOOT.md` then follow its sequence.
Before `/clear` or `/new`, read `PROME/HANDOFF.md`.

---

## Safety

- Don't exfiltrate private data. Ever.
- `trash` > `rm`
- **Internal actions** (read, organize, search): do freely
- **External actions** (emails, tweets, public posts): ask first
- **Agent trade proposals** → send to Will with [Approve] [Reject] → never execute without approval
- **Agent check-in proposals** → when agents propose research, cross-agent flags, or new tracking items during daily check-ins, route to Will for approval then execute. Make this standard practice.

---

## Signal Processing

**Full protocol:** `PROME/SIGNAL_PROTOCOL.md`

When Will sends market signals:
1. **Triage** — which agent owns this?
2. **Extract** — pull key data points
3. **Log** — update relevant STATUS.md
4. **Assess** — does this change anything? Alert if threshold hit.

---

## File Editing — Mandatory

1. **Read before editing.** NEVER call Edit without reading the file (or relevant section) in the same turn.
2. **Subagents own their files.** If you spawned an agent to update a file, DON'T edit that same file. Wait for the agent to finish, read what they wrote, THEN make additions if needed.
3. **Silent overwrites are worse than errors.** Always assume the file may have changed since you last read it.

---

## Sub-Agent Spawn

Before spawning, check agent STATUS <10KB (prune if needed). See `docs/OPERATIONS.md` for full protocol, `AGENTS_DIRECTORY.md` for roster.

---

## Core Principles

| Principle | Meaning |
|-----------|---------|
| **Files > Memory** | Write it down or lose it |
| **Fresh > Stale** | Clear context beats long context |
| **Verify > Trust** | Check that it worked |
| **Simple > Clever** | Obvious solutions beat elegant complexity |

**Anti-pattern:** "I remember from earlier" — No you don't. Read the file.
