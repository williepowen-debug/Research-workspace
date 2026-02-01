# CLAUDE BOOT SEQUENCE

Read these files in order at the start of every session.

---

## STEP 1: Read Project Brief
```
CLAUDE.md
```
Located in project root. Contains:
- What this project is (political-financial intelligence network)
- Current network state (nodes, edges, catalysts)
- Validated patterns (the core insights)
- Clusters and key conflicts
- Research status (active, monitoring, exhausted)
- Tickers to watch
- User context and preferences
- Methodology and evidence standards

**This is the master reference. Read it first.**

---

## STEP 2: Read Latest Session Handoff
```
sessions/SESSION_HANDOFF_[latest date].md
```
Find the most recent file by date. Contains:
- What was done last session
- Data added (new nodes, edges, catalysts)
- Gaps resolved and new gaps identified
- Open threads and next priorities
- Key insights and context for continuing work

**This tells you where we left off.**

---

## STEP 3: Load Data Files (On-Demand)
Only read these when actively working on research:
```
data/NODES.tsv     # Entities (people, companies, funds, orgs)
data/EDGES.tsv     # Relationships between entities
data/CATALYSTS.tsv # Events and triggers to monitor
```

---

## STEP 4: Check Sources (As Needed)
```
sources/SOURCE_LOG.md  # All sources used, organized by date
```

---

## OPERATIONAL NOTES

**Permissions:** You have auto-approval for WebSearch, WebFetch, Read, Edit, Write, Grep, Glob, Task, and common Bash commands. Don't ask - just execute.

**Autonomy:** Run research threads autonomously. Report findings. Check in for major direction changes.

**Documentation:**
- Update TSV files as you work (don't batch)
- Write session handoffs at end of session
- Document dead ends immediately
- Always note sources

**Output format for new data:**
```
N-XXX	Name	Type	Cluster	Role	Policy_Control	Holdings	Tickers	Status
E-XXX	N-From	N-To	TYPE	Evidence	Confidence	Source	Date
```

---

## QUICK START COMMAND

If user says "boot up" or "start session" or "read the files":
1. Read CLAUDE.md
2. Read latest SESSION_HANDOFF_*.md
3. Summarize current state and ask what to work on

---

*Last updated: 2026-01-07*
