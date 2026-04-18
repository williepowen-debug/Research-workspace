# PROME HANDOFF
**Date:** 2026-04-18 17:05 ET
**Status:** ✅ Complete — File migration finished

---

## Session Summary

**Work completed:** Repository cleanup — Prome files migrated to scoped directories

### Files Moved

| File | Old Location | New Location |
|------|--------------|--------------|
| **HEARTBEAT.md** | `/workspace/HEARTBEAT.md` | `PROME/state/HEARTBEAT.md` |
| **MEMORY.md** | `/workspace/MEMORY.md` | `PROME/state/MEMORY.md` |
| **SOUL.md** | `/workspace/SOUL.md` | `PROME/identity/SOUL.md` |
| **USER.md** | `/workspace/USER.md` | `PROME/identity/USER.md` |
| **IDENTITY.md** | `/workspace/IDENTITY.md` | `PROME/identity/IDENTITY.md` |

### References Updated

| File | Changes |
|------|---------|
| `PROME/BOOT.md` | Updated injection paths, doc ownership table, memory lifecycle, git protocol |
| `AGENTS.md` | Added identity/state file location notes |
| `PROME/identity/IDENTITY.md` | Updated pointer to `PROME/identity/SOUL.md` |

### Directory Structure

```
PROME/
├── identity/          # Who Prome is
│   ├── SOUL.md
│   ├── USER.md
│   └── IDENTITY.md
├── state/             # Operational state
│   ├── HEARTBEAT.md
│   └── MEMORY.md
├── BOOT.md            # (already existed, canonical)
├── HANDOFF.md         # This file
├── SCRATCH.md
├── TODAY.md
├── STATUS.md
├── POSITIONS.md
├── PREDICTIONS_MONITOR.md
├── TOSCANINI/
└── ...
```

---

## Current State (Ground Truth)

**Date:** Saturday, April 18, 2026 — 5:05 PM ET
**Scenario:** D dominant (82%)
**War Day:** 45

### System State
- All Prome files migrated and references updated
- Git commits pending (see below)
- Boot sequence verified: `PROME/BOOT.md` already canonical, no root BOOT.md conflict

### Unchanged (System-Wide)
These files remain at root and were NOT touched:
- `AGENTS.md`
- `AGENTS_DIRECTORY.md`
- `CLAUDE.md`
- `COP.md`
- `README.md`
- `LICENSE`
- `TOOLS.md`
- `CALENDAR.md`
- `LESSONS.md`

---

## Git Commit Notes

**Files to stage:**
```bash
git add PROME/state/HEARTBEAT.md PROME/state/MEMORY.md \
        PROME/identity/SOUL.md PROME/identity/USER.md PROME/identity/IDENTITY.md \
        PROME/BOOT.md PROME/HANDOFF.md AGENTS.md
```

**Deleted (root level):**
- `HEARTBEAT.md`
- `MEMORY.md`
- `SOUL.md`
- `USER.md`
- `IDENTITY.md`

---

## For Next Claude Session

**Boot sequence is unchanged** — `PROME/BOOT.md` remains the entry point.

The system prompt injection paths will need updating on the OpenClaw side to reference:
- `PROME/identity/SOUL.md` instead of `SOUL.md`
- `PROME/identity/USER.md` instead of `USER.md`
- `PROME/state/HEARTBEAT.md` instead of `HEARTBEAT.md`
- `PROME/state/MEMORY.md` instead of `MEMORY.md`

**Ready for Will to pull and verify.**
