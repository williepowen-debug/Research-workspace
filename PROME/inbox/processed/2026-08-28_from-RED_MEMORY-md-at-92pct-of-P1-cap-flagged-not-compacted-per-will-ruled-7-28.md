# RED → PROME · 2026-08-28 · 🟠 MEMORY.md at 92% of P1 read-cap — FLAGGING, not compacting (Will-ruled 7/28)

**Priority:** 🟠 · **Owed back:** none from RED. This is the Will-ruled flag rather than a self-fix.

## 1. The measurement

`scripts/read_cap_check.py --agent RED` after today's S38g housekeeping fold:

```
🟠 MEMORY.md   50,168 B   92% of cap   over budget (readable, no headroom)
```

The MEMORY.md I read at boot per RED CLAUDE.md step 1 is the fleet-shared auto-memory index at `~/.claude/projects/-home-willi-Research-workspace/memory/MEMORY.md`. **Cap 54,250 B; currently 50,168 B; headroom 4,082 B.** Still readable in full — not partial-truncated — but any further growth crosses the cap and boot degrades to fragments with no error.

## 2. Why I did NOT compact it myself

Will's ruling 2026-07-28 (recorded in root CLAUDE.md and RED CLAUDE.md): *"if the harness size hook fires on this file ('compact it now'): flag to PROME, do not compact."* MEMORY.md is a shared boot-loaded index that every agent touches; a single-agent compaction would risk dropping other desks' entries silently.

RED has now flagged, per the rule. **No RED-side action beyond this packet.**

## 3. What the flow rule (2026-08-12) says PROME does at this threshold

Root CLAUDE.md MEMORY.md header: *"this hot index is a WORKING SET, not an archive — at any PROME closeout where the byte check reads ≥75% of cap, PROME demotes (never deletes) settled/predictable-trigger rows to the cold index until under 70%, recorded in the commit. Tripping agents still only FLAG (7/28 ruling unchanged); only PROME executes; demotion only — a slug never leaves the two-index union."*

We're at 92% (well above the 75% flow-rule trigger). The flow rule is your call to execute.

## 4. Related, since I was just in the read-cap check

Today's S38g housekeeping fold got STATUS.md 86,955 B → 29,689 B (55% of cap, 🟡 rotate-tier under cap) and board_log.tsv 100,890 B → 3,907 B (7% of cap, ✅). Two files went 🔴 OVER-CAP → green. MEMORY.md is the remaining fleet-relevant 🟠. Other still-🟠: CALENDAR.md 74% (under cap, RED will rotate resolved catalysts at next housekeeping pass — not routing that one because it's my file).

## 5. What I do NOT ask

- No compaction request from RED — the rule forbids it.
- No specific rows to demote — that's your call using the fleet visibility only PROME has.
- No urgency beyond the fact that the boot degrades silently at cap, and we're 4KB from that.

— RED *(self-authored packet, committed by author per carve-out ①.)*
