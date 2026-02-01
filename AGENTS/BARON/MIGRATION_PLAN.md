# Migration Plan: Trump Network Reorganization

**Created:** 2026-01-12
**Purpose:** Guide for fresh Claude session to reorganize project structure
**Status:** READY FOR IMPLEMENTATION

---

## Overview

This document outlines a plan to:
1. Move the project out of OneDrive (fixes sync interference issues)
2. Initialize git version control (enables recovery from mistakes)
3. Reorganize into domain-based sub-divisions (easier to work with)

The user has no git experience - Claude should handle all technical steps and provide simple commands for ongoing use.

---

## Step 1: Move Project and Initialize Git

### 1.1 Create new location and copy files

```bash
mkdir -p /c/Users/willi/projects
cp -r "/c/Users/willi/OneDrive/Desktop/trump-network" "/c/Users/willi/projects/trump-network"
cd /c/Users/willi/projects/trump-network
```

### 1.2 Initialize git

```bash
git init
git add .
git commit -m "Initial commit - migrated from OneDrive"
```

### 1.3 Verify

```bash
git status
git log --oneline
```

### 1.4 Create .gitignore (optional)

```
# Ignore temporary files
*.tmp
*~
.DS_Store
```

---

## Step 2: Reorganize Into Domains

### 2.1 Target Structure

```
/trump-network
  .git/
  CLAUDE.md              # Shortened boot file
  STATE.md               # Quick reference: counts, triggers, open questions

  domains/
    defense/
      OVERVIEW.md        # Defense-specific context
      nodes.tsv          # Clusters: C1, C5, C12 (partial)
      edges.tsv          # Defense-related edges only
      catalysts.tsv      # Defense-related catalysts

    housing/
      OVERVIEW.md
      nodes.tsv          # Clusters: C10, C11
      edges.tsv
      catalysts.tsv

    energy/
      OVERVIEW.md
      nodes.tsv          # Cluster: C7
      edges.tsv
      catalysts.tsv

    finance/
      OVERVIEW.md
      nodes.tsv          # Clusters: C2 (SEC/crypto), C3, C4
      edges.tsv
      catalysts.tsv

    media/
      OVERVIEW.md
      nodes.tsv          # Cluster: C6
      edges.tsv
      catalysts.tsv

    cross-domain/
      OVERVIEW.md        # Nodes spanning multiple domains
      nodes.tsv          # Leo, Miller, DOGE, Vought, P2025
      edges.tsv          # Cross-domain connections

  reference/
    PATTERNS.md          # All 27 patterns (moved from CLAUDE.md)
    EXHAUSTED.md         # Dead ends (moved from RESEARCH_STATUS.md)
    METHODOLOGY.md       # Research methods, evidence standards

  sessions/
    (existing handoff files)
    CONSOLIDATED HANDOFF.md

  research/
    prompts/
    results/

  archive/
    OLD_NODES.tsv        # Original unified files (backup)
    OLD_EDGES.tsv
    OLD_CATALYSTS.tsv
    OLD_CLAUDE.md
    OLD_RESEARCH_STATUS.md
```

### 2.2 Domain Assignments

**Defense Domain (C1, C5, C12)**
- C1: 1789 Capital (Trump Jr, Malik, Buskirk, portfolio companies)
- C5: Pentagon/Cerberus (Feinberg, Hegseth, Witt, Homan, defense contractors)
- C12: Clean Beneficiaries (Rocket Lab, Beck, Khosla - defense-related)
- Key nodes: N-011 to N-018, N-027 to N-033, N-039, N-062-063, N-084-088, N-119, N-168-179, N-218-230, N-272-290

**Housing Domain (C10, C11)**
- C10: Housing Policy (Pulte, Turner, Moreno)
- C11: SFR/BTR Transition (Schwarzman, Rowan, INVH, AMH, PHM)
- Key nodes: N-208 to N-217, N-231, N-257-269

**Energy Domain (C7)**
- C7: EPA/Energy (Wright, Oklo, Burgum, Hamm, Zeldin, Kushner, MBS, PIF)
- Key nodes: N-076 to N-082, N-089-094, N-103-116

**Finance Domain (C2 partial, C3, C4)**
- C2 (SEC/crypto): Atkins, Sacks, Securitize, BitGo, crypto companies
- C3: Lutnick/Cantor, Tether, Bitcoin SPACs
- C4: Treasury (Bessent, Miran, Gibbens)
- Key nodes: N-001 to N-010, N-019-026, N-034-038, N-040-041, N-048-075, N-122-128, N-181-195

**Media Domain (C6)**
- C6: MAGA Media (Carr, Sinclair, Nexstar, Fox, Rumble)
- Key nodes: N-025, N-047, N-118, N-137-167

**Cross-Domain**
- Leonard Leo (N-110, all clusters)
- Stephen Miller (N-123, C5 + policy)
- Russell Vought (N-117, C4 + all agencies)
- Project 2025 (N-116)
- SCOTUS overlay (N-157-164)
- Bondi/DOJ (N-196-206)
- Key nodes: N-110, N-116-117, N-123-124, N-129-136, N-157-164, N-196-206, N-239-256

### 2.3 Implementation Steps

1. Create directory structure
2. Archive original files to archive/
3. Split NODES.tsv by domain (grep by cluster or node ID ranges)
4. Split EDGES.tsv (edges where both nodes are in same domain go to that domain; cross-domain edges go to cross-domain/)
5. Split CATALYSTS.tsv by related nodes
6. Create domain OVERVIEW.md files (extract relevant sections from CLAUDE.md)
7. Create slim CLAUDE.md (boot instructions only)
8. Create STATE.md (current status quick reference)
9. Create reference/PATTERNS.md (move patterns table)
10. Create reference/EXHAUSTED.md (move from RESEARCH_STATUS.md)
11. Git commit after each major step

---

## Step 3: New File Contents

### 3.1 New CLAUDE.md (Slim Boot File)

```markdown
# CLAUDE.md - Trump Financial-Policy Network

## WHAT THIS IS
Political-financial intelligence project mapping conflicts of interest between Trump 2.0 officials and companies benefiting from their policy decisions.

## BOOT SEQUENCE
1. Read this file
2. Read STATE.md (current status, active triggers)
3. Read latest session handoff in sessions/
4. Load domain files as needed for the task

## STRUCTURE
- domains/ - Research organized by topic (defense, housing, energy, finance, media, cross-domain)
- reference/ - Patterns, methodology, exhausted threads
- sessions/ - Handoff notes
- research/ - External research workflow

## DOMAIN OVERVIEW
| Domain | Focus | Key Tickers |
|--------|-------|-------------|
| defense | 1789, Pentagon, Cerberus, DOGE | PLTR, RKLB, VLD |
| housing | FHFA, HUD, SFR/BTR | PHM, INVH, AMH, BX |
| energy | DOE, EPA, oil, nuclear | OKLO, LBRT, CVX, COP |
| finance | Treasury, SEC, crypto | BTGO, SECZ, XXI |
| media | FCC, broadcasters | RUM, SBGI, NXST |
| cross-domain | Leo, Miller, P2025, SCOTUS | - |

## WORKING IN A DOMAIN
When user asks about a topic:
1. Identify the domain
2. Read domains/[domain]/OVERVIEW.md
3. Load that domain's TSV files
4. Check cross-domain/ for related connections

## GIT COMMANDS (for user)
Save snapshot: git add . && git commit -m "description"
Restore file: git checkout -- filename
See history: git log --oneline

## OPERATIONAL PREFERENCES
(Keep existing preferences from current CLAUDE.md)
```

### 3.2 STATE.md Template

```markdown
# Current State

**Last Updated:** [DATE]
**Network:** X nodes | Y edges | Z catalysts | 27 patterns

## Active Triggers (Next 30 Days)

| Date | Event | Domain | Tickers |
|------|-------|--------|---------|
| Jan 20-24 | Davos - BTR exemption details | housing | PHM, INVH, AMH |
| Feb 6 | Hegseth contractor list | defense | LMT, RTX, NOC |

## Open Questions
- BTR carve-out language (Davos trigger)
- Pulte OGE 278 PHM holdings detail

## Recent Changes
- 2026-01-12: Added Rocket Lab / Clean Cover pattern (defense)
- 2026-01-11: Housing thesis revised to Long all BTR ecosystem

## Quick Reference
- Patterns: reference/PATTERNS.md
- Dead ends: reference/EXHAUSTED.md
- Methods: reference/METHODOLOGY.md
```

### 3.3 Domain OVERVIEW.md Template

```markdown
# [Domain] Overview

## Key Players
| Node | Name | Role | Exposure |
|------|------|------|----------|

## Clusters in This Domain
- CX: [description]

## Domain-Specific Patterns
[patterns that primarily apply to this domain]

## Current Thesis
[trading thesis for this domain]

## Active Catalysts
[upcoming triggers for this domain]

## Key Conflicts
[major conflicts in this domain]
```

---

## Step 4: Ongoing Git Usage

### For User (Simple)

**End of each session:**
```bash
cd /c/Users/willi/projects/trump-network
git add .
git commit -m "Session end - [brief description]"
```

**If a file gets corrupted:**
```bash
git checkout -- path/to/file
```

**See what changed:**
```bash
git diff
git log --oneline -10
```

### For Claude (Handle Automatically)

- Commit after major changes during session
- Use descriptive commit messages
- Check git status if file issues occur

---

## Step 5: Verification Checklist

After migration, verify:

- [ ] Project exists at /c/Users/willi/projects/trump-network
- [ ] git log shows initial commit
- [ ] All 6 domain folders exist with nodes.tsv, edges.tsv, catalysts.tsv
- [ ] reference/ contains PATTERNS.md, EXHAUSTED.md, METHODOLOGY.md
- [ ] archive/ contains original files
- [ ] New CLAUDE.md is slim (<100 lines)
- [ ] STATE.md exists with current status
- [ ] Total node count across domains matches original (~290)
- [ ] Total edge count across domains matches original (~522)
- [ ] sessions/ and research/ folders preserved

---

## Notes for Implementing Claude Session

1. **Do Step 1 first** (move + git init) before any reorganization
2. **Commit after each major step** so user can recover if something goes wrong
3. **Preserve original files in archive/** before splitting
4. **Test counts** after splitting to ensure nothing lost
5. **User has no git experience** - handle all git operations, just teach the 2 basic commands
6. **OneDrive copy can be deleted** after user confirms new location works

---

## Estimated Time

- Step 1 (move + git): 5 minutes
- Step 2 (reorganize): 30-45 minutes
- Step 3 (new files): 20-30 minutes
- Step 4 (teach git): 5 minutes
- Step 5 (verify): 10 minutes

**Total: ~1-1.5 hours**

Could be split across sessions:
- Session A: Steps 1-2 (move, git, split files)
- Session B: Steps 3-5 (new docs, verify)

---

*This plan created by Claude session 2026-01-12*
