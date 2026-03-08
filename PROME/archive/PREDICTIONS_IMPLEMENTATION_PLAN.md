# PREDICTIONS.tsv Implementation Plan

**Status:** Ready to execute after next handoff
**Estimated time:** 15-20 min (scripted)

---

## What

Replace FL.tsv (stale catalyst calendar) with PREDICTIONS.tsv (falsifiable forecasts with tracking).

**Format:**
```
Pred_ID | Date_Made | Prediction | Confidence | Timeframe | Status | Date_Resolved | Outcome | Notes
```

**Status values:** OPEN, CONFIRMED, FAILED, EXPIRED, PARTIALLY

## Steps

### 1. Create PREDICTIONS.tsv for each agent (~5 min, scripted)
- Create `workbook/PREDICTIONS.tsv` with header row for all 13 agents
- Migrate any valuable FL.tsv entries (future-dated catalysts → predictions)
- Delete or archive FL.tsv

### 2. Update agent instruction files (~5 min, scripted)
- Replace FL.tsv references with PREDICTIONS.tsv in each agent's AGENTS.md/CLAUDE.md
- Add prediction logging rules (already in CLAUDE_TEMPLATE.md)

### 3. Seed with existing predictions (~10 min)
- Scan each agent's STATUS.md and PREDICTIONS.md for existing forecasts
- Convert to PREDICTIONS.tsv format
- Key sources: HENRY (market calls), LIQUID (spread predictions), SAM (carry unwind timing), HANS (ceasefire), CARL (DQ thresholds)

### 4. Add resolution protocol to template
- At session boot, agents check PREDICTIONS.tsv for expired/resolvable entries
- Update Status + Outcome columns
- Log resolution to ML.tsv for audit trail

### 5. Weekly scoring (future)
- Script to scan all PREDICTIONS.tsv, calculate hit rates by agent
- Surface to WILL/INBOX.md: "Agent accuracy this week: HENRY 4/5, CARL 2/3..."
- This is the feedback loop that makes the system self-improving

## Dependencies
- Template already updated ✅
- BUILD_AGENT.md already updated ✅
- Just needs file creation + instruction file updates

## Rollback
Keep FL.tsv archived in `workbook/deprecated/` for 2 weeks, then delete.
