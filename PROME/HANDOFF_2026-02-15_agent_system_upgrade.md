# HANDOFF: Agent System Upgrade
**Date:** 2026-02-15
**Session:** Agent architecture redesign with Will
**Status:** OTTO complete, SAM next

---

## What We Decided

### 1. File Structure (Per Agent)

| File | Purpose | Changes Often? |
|------|---------|----------------|
| **CLAUDE.md** | Instructions + Domain (merged) | Rarely |
| **STATUS.md** | Live dashboard with standardized header | Frequently |
| **PREDICTIONS.md** | Falsifiable claims with timeframes | Weekly |
| **TRADE.md** | Position ideas | As needed |
| **workbook/** | VX/ML/FL/FLOW.tsv | Per session |
| **research/outputs/** | RP-XXX-x.x packages | Per research |

### 2. Coordination Model (Hybrid)

- **AGENTS/SIGNALS.md** — Central ticker for cross-agent alerts
- **STATUS.md headers** — Standardized "Signal Status" + "Outbound Signals" section
- **Prome's routine:**
  - Heartbeats: Check SIGNALS.md only
  - Daily: Scan STATUS.md headers
  - Weekly: Full STATUS.md reads

### 3. What We Archived

- SKELETON.md → Merged into CLAUDE.md
- EXPECTED_SIGNALS.md → Signal triggers now in CLAUDE.md
- handoffs/ → Not using this system

---

## OTTO Reference Implementation

**OTTO is the template.** Follow its structure exactly.

### CLAUDE.md Structure
1. Identity (name, domain, voice, mission)
2. Domain Scope (what it watches, data sources)
3. Current Thesis (primary + secondary, link to STATUS.md)
4. Startup Protocol (what to read on spawn)
5. Closing Protocol (what to update)
6. Coordination (who talks to whom, signal triggers with historical precedents)
7. Research Convention (RP-XXX-x.x naming)
8. Prediction Convention
9. Trade Flow
10. Domain-specific reference material (mechanisms, thresholds, glossary)
11. Invalidation Framework
12. File Structure

### STATUS.md Header (Standardized)
```markdown
# [AGENT] STATUS

**Signal Status:** 🟢/🟡/🔴 [STATUS] | **Last Updated:** YYYY-MM-DD HH:MM UTC

**Summary:** [One line]

[Other metrics]

## Outbound Signals (for Prome)

| To | Priority | Signal |
|----|----------|--------|
| AGENT | 🔴/🟠/🟡 | Description |
```

### PREDICTIONS.md Structure
- Active predictions with: #, claim, timeframe, confidence, status, invalidation
- Imminent predictions (next 7 days) highlighted
- Thesis validation criteria (confirmed/invalidated checkboxes)
- Scenario probabilities
- Cross-agent dependencies
- Resolved predictions with outcomes
- Calibration stats

---

## Next: SAM

### Current SAM Files (check these)
- STATUS.md — 13KB, likely needs header update
- CLAUDE.md — Unknown if exists
- SKELETON.md — May exist, needs merge
- PREDICTIONS.md — Unknown if exists

### SAM-Specific Context
- Domain: Japan macro / yen / carry trade / BOJ
- Critical catalyst: **Feb 19** — Shunto wages + 20Y JGB auction
- If both fire (Shunto ≥3.5% AND JGB BTC <2.0x) = Path D trigger
- Coordinates with: HENRY (market structure), LIQUID (UST flows), PROME

### Process for SAM
1. Read current SAM files (STATUS.md, any CLAUDE.md/SKELETON)
2. Draft CLAUDE.md v2 following OTTO template
3. Add standardized header to STATUS.md
4. Create/update PREDICTIONS.md (extract from STATUS.md if embedded)
5. Archive deprecated files
6. Test: Can a spawned SAM agent do its job with just CLAUDE.md + STATUS.md?

---

## Will's Preferences (This Session)

- Go slow, one section at a time
- Don't make mistakes
- OTTO is the gold standard
- Historical precedents add value to signal triggers

---

## Files Created/Modified Today

**Created:**
- `AGENTS/SIGNALS.md` — Cross-agent ticker
- `AGENTS/OTTO/CLAUDE.md` v2 — Merged template

**Modified:**
- `AGENTS/OTTO/STATUS.md` — Added standardized header
- `AGENTS/OTTO/PREDICTIONS.md` — Marked confirmed, added new predictions

**Archived:**
- `AGENTS/OTTO/archive/OTTO_SKELETON_v2.0_archived.md`
- `AGENTS/OTTO/archive/EXPECTED_SIGNALS_v1.0_archived.md`
- `AGENTS/OTTO/archive/OTTO_HANDOFF_TEMPLATE_archived.md`

---

## Resume Instructions

1. Read this handoff
2. Read `AGENTS/OTTO/CLAUDE.md` as template
3. Read `AGENTS/SAM/STATUS.md` for current state
4. Check what SAM files exist
5. Proceed with SAM upgrade, one section at a time

---

*Handoff created: 2026-02-15 18:16 UTC*
