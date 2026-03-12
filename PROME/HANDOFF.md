# PROME Handoff

Read this before `/clear` or `/new`.

---

## Before `/clear` — Checkpoint
1. **Append to `memory/YYYY-MM-DD.md`:**
```
## Checkpoint [HH:MM UTC]
**Context:** [one sentence — what we were doing]
**Changed:** [files touched this segment]
**Next:** [what's queued up]
```
2. **`git add -A && git commit -m "checkpoint"`**

## Before `/new` — Full Handoff
1. **`PROME/SCRATCH.md`** — Update QUICKSTART + handoff block for next-me
2. **`memory/YYYY-MM-DD.md`** — Log session work + handoff block
3. **`PROME/STATUS.md`** — Update dashboard
4. **`MEMORY.md`** — Add learnings worth keeping
5. **Commit and push**
5. If applicable: USER.md, PREDICTIONS.md, LESSONS.md, CALENDAR.md, FORGE/STATUS.md

## Session Reset Strategy
- **`/clear`** — Compaction summary rides along (lossy, stacks). 2-3 clears max before `/new`.
- **`/new`** — Fresh session, no compaction. Full file handoff required (context won't survive).

## Handoff Format
```
## Handoff
**Last context:** [first thing next-me needs to know]
**Next tide:** [prioritized actions]
**Open questions:** [unresolved decisions]
**Positions:** [any changes]
**Rhythm note:** [mental state, shorthand developed]
**Today's work:** [brief bullets]
```

## Memory
- **Daily notes:** `memory/YYYY-MM-DD.md`
- **Long-term:** `MEMORY.md` (main session only, never group chats)
