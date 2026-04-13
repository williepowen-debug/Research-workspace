# VIOLET Domain Audit

**Auditor:** Subagent (cold-boot review)  
**Date:** 2026-04-12  
**Overall Health Score:** 7.5/10 — Solid foundation, operational gaps in live monitoring

---

## Executive Summary

VIOLET is a **well-initialized agent** with strong historical research foundations but **underdeveloped live monitoring infrastructure**. The core thesis (regime-dependent credit-vol relationship) is well-documented and data-backed. However, critical operational files are empty or missing, and the agent lacks real-time data feeds despite having defined monitoring protocols.

**Strengths:**
- Comprehensive historical analysis (2,019 days of data)
- Clear, falsifiable thesis with regime-dependent framework
- Good crisis analog documentation (Feb 2018, Mar 2020, Feb 2021)
- Proper KB.tsv schema compliance (10 valid entries)

**Weaknesses:**
- VX.tsv tracking file is empty (header only)
- FLOW.tsv signal log is empty
- Three research directories are completely empty
- No daily data refresh workflow implemented
- Missing VIX futures curve data (only has VIX3M)

---

## Critical Gaps (Must Fix)

### 1. Empty Tracking Files — Operational Blindness
| File | Status | Impact |
|------|--------|--------|
| `workbook/VX.tsv` | Header only, no data | Cannot track VIX time series |
| `workbook/FLOW.tsv` | Header only, no data | No cross-agent signal history |
| `inbox/` | Empty | No signal processing demonstrated |
| `outbox/` | Empty | No outbound signals ever sent |

**Issue:** The agent has monitoring protocols defined in SIGNAL_INTAKE.md but no evidence of actual signal flow. The VX.tsv should contain daily VIX readings with regime classifications.

**Fix:** Populate VX.tsv with daily data going back to initialization (Apr 12) and establish daily update discipline.

### 2. Empty Research Directories — Incomplete Research Agenda
| Directory | Status | Expected Content |
|-----------|--------|------------------|
| `research/regime_patterns/` | Empty | Regime transition analysis, persistence studies |
| `research/term_structure/` | Empty | VIX futures curve analysis, contango/backwardation studies |
| `research/skew_analysis/` | Empty | SKEW index patterns, tail risk pricing analysis |

**Issue:** These directories are referenced in RESEARCH PRIORITIES (CLAUDE.md) and MEMORY.md but contain no files. The regime_patterns/ directory is particularly important given the regime-dependent thesis.

**Fix:** Either populate with analysis or remove from research priorities if deprioritized.

### 3. Missing VIX Futures Curve Data
**Issue:** STATUS.md shows "VIX Futures Curve | Contango" but there's no actual futures data. Only VIX3M is tracked. The thesis emphasizes term structure but lacks granular data.

**Evidence:**
- `workbook/combined_vix_credit.csv` has VIX, VIX3M, VVIX, SKEW — no futures
- CALENDAR.md references VIX expirations but no futures data source

**Fix:** Add VIX futures (M1, M2, M3, M4) to data refresh workflow or acknowledge limitation.

### 4. No Daily Data Refresh Mechanism
**Issue:** LAST_COMPLETION.md lists "Set up daily data refresh workflow" as Next Action #1, but no cron job or automated workflow exists.

**Evidence:**
- CALENDAR.md Data Refresh Schedule shows "Last Updated: Never" for all sources
- No evidence of automation in FORGE/tools/market-data/ integration

**Fix:** Either implement cron job or establish manual daily update protocol with accountability.

---

## Minor Issues (Should Fix)

### 5. Inconsistent Threshold References
| File | VIX > 30 Threshold | VIX > 40 Threshold |
|------|-------------------|-------------------|
| CLAUDE.md | >30 (equity stress) | >40 (crash regime) |
| SIGNAL_INTAKE.md | >30 (alert HENRY) | >40 (critical alert) |
| STATUS.md | >30 (⚪) | >40 (⚪) |
| MEMORY.md | >40 (crash regime) | — |

**Issue:** Minor inconsistency — MEMORY.md defines Crash Regime as VIX > 40, but CLAUDE.md uses >40 for "Crash regime" and >30 for "Equity stress." Not critical but should align.

### 6. Missing Cross-Agent Signal Definitions
**Issue:** While SIGNAL_INTAKE.md documents what VIOLET watches FROM other agents, there's no documented protocol for what signals VIOLET SENDS TO other agents in standardized format.

**Evidence:**
- Outbound triggers defined in SIGNAL_INTAKE.md but no signal templates
- No example signal files in outbox/
- FLOW.tsv has no schema for signal structure

**Fix:** Create signal template files in outbox/ for each outbound trigger condition.

### 7. Stale Date References
| File | Reference | Issue |
|------|-----------|-------|
| CALENDAR.md | "Apr 15 | This week" | Written Apr 12, accurate then, but will stale quickly |
| KB.tsv | Stale_By dates | All set to 2026-04-14 or 2026-07-12 — need refresh logic |

**Issue:** CALENDAR.md uses relative time references ("this week") that will become confusing. KB.tsv entries have Stale_By dates that will pass without review protocol.

### 8. Incomplete Vocabulary Alignment
**Issue:** KB.tsv uses Group="VOL" and Entity="VIX" etc., but VOCABULARIES.tsv doesn't define these terms.

**Evidence:**
- VOCABULARIES.tsv has no "VOL" group (has "VOL" under HENRY's domain but not defined)
- VIOLET's entities (VIX, VIX3M, VVIX, SKEW) not in CANONICAL_ENTITIES

**Fix:** Propose VIOLET-specific vocabulary additions to PROME for standardization.

---

## Questions for PROME/Will

1. **Data Refresh Priority:** Should VIOLET integrate with FORGE/tools/market-data/ for automated daily updates, or is manual daily update acceptable?

2. **VIX Futures Data:** Is VIX futures curve data (M1-M4) a priority, or is VIX3M sufficient for the regime detection thesis?

3. **Signal Automation:** Should VIOLET automatically write signal files to outbox/ when thresholds breach, or is manual signal generation preferred?

4. **Empty Research Directories:** Should regime_patterns/, term_structure/, and skew_analysis/ be populated, or removed from the research agenda?

5. **Live Testing:** The thesis/VIX_THESIS.md mentions "Phase 3: Live Testing" — should this begin now, or wait for specific market conditions?

---

## Recommended Next Actions

### Immediate (This Week)
1. **Populate VX.tsv** — Backfill daily VIX data from initialization date (Apr 12) and establish daily update discipline
2. **Create Signal Templates** — Write example outbound signal files to outbox/ for each trigger condition
3. **Document Data Sources** — Add VIX futures data source to CALENDAR.md or acknowledge limitation

### Short-Term (Next 2 Weeks)
4. **Implement Daily Refresh** — Either cron job or manual protocol with accountability tracking
5. **Populate or Depreciate Empty Research Directories** — Either add analysis to regime_patterns/, term_structure/, skew_analysis/ or remove from research priorities
6. **Align Thresholds** — Standardize regime definitions across all files

### Medium-Term (Next Month)
7. **Begin Live Testing** — Paper trade lag signals when HY OAS approaches 4.0
8. **Vocabulary Proposal** — Submit VIOLET-specific terms to AGENTS/VOCABULARIES.tsv
9. **Signal Integration Test** — Send test signal to HENRY/LIQUID to validate cross-agent flow

---

## File-by-File Audit Summary

| File | Status | Notes |
|------|--------|-------|
| CLAUDE.md | ✅ Good | Clear instructions, well-structured |
| STATUS.md | ✅ Good | Populated with live data, Convergence Matrix present |
| thesis/VIX_THESIS.md | ✅ Good | Comprehensive, data-backed, falsifiable predictions |
| MEMORY.md | ✅ Good | Solid reference material, regime definitions clear |
| SIGNAL_INTAKE.md | ⚠️ Good structure, untested | No evidence of signal processing |
| TRADE.md | ✅ Good | Framework clear, no active positions (appropriate) |
| CALENDAR.md | ⚠️ Good structure, stale dates | "This week" references, no data refresh evidence |
| workbook/KB.tsv | ✅ Good | 10 valid entries, schema compliant |
| workbook/VX.tsv | ❌ Empty | Header only, no time series data |
| workbook/FLOW.tsv | ❌ Empty | Header only, no signal history |
| research/crisis_analogs/ | ✅ Good | 3 well-documented case studies |
| research/credit_vix_lag/ | ✅ Good | Complete analysis with CSV |
| research/regime_patterns/ | ❌ Empty | Referenced but unpopulated |
| research/term_structure/ | ❌ Empty | Referenced but unpopulated |
| research/skew_analysis/ | ❌ Empty | Referenced but unpopulated |
| inbox/ | ⚠️ Empty | No signals to process |
| outbox/ | ❌ Empty | No outbound signals sent |
| LAST_COMPLETION.md | ✅ Good | Clear completion record |

---

## Conclusion

VIOLET has a **strong analytical foundation** but needs **operational hardening**. The research is sound, the thesis is clear, and the data infrastructure exists. The critical gap is the transition from "research mode" to "live monitoring mode" — populating tracking files, establishing data refresh discipline, and activating cross-agent signal flows.

**Bottom line:** VIOLET is ready to operate but hasn't started operating yet.
