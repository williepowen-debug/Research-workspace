# BROCK UPGRADE PLAN

*Audit date: March 6, 2026 — compared against HENRY and REGINALD gold standards*

## CLAUDE.md Gaps

1. **No "File > verbal" rule** — HENRY/REGINALD both have the explicit `⚠️ File > verbal` callout. BROCK's CLAUDE.md lacks it.
2. **No "#1 RULE: Always WRITE to STATUS.md"** — Both standards open with this. BROCK lacks it.
3. **No stale data rules** — HENRY has VX.tsv staleness handling, STATUS.md >24h rules. REGINALD has Call Report quarter-lag rules. BROCK has none.
4. **No "Don't maintain stale copies" rule** — Missing entirely.
5. **No source tags ([CONF]/[EST])** — Neither CLAUDE.md nor STATUS.md uses confidence source tagging.
6. **No convergence matrix / 5-point scale** — HENRY/REGINALD use structured threshold tables with color-coded status. BROCK has informal watchlist but no systematic scoring matrix.
7. **No exit rules / falsification (4 categories)** — HENRY has THESIS_VALIDATION.md with confirmation/invalidation criteria. REGINALD has the same. BROCK has EXPECTED_SIGNALS.md but no formal falsification framework.
8. **No BOTTOM LINE requirement** — Neither CLAUDE.md nor STATUS.md enforces a bottom-line summary block.
9. **Missing LESSONS.md** — HENRY and REGINALD both reference LESSONS.md in spawn protocol. BROCK has no LESSONS.md file at all.
10. **No explicit output rules section** — HENRY/REGINALD have "Tables > prose", "STATUS.md stays under 250 lines", "Separate SIGNAL from INTERPRETATION." BROCK lacks all of these.
11. **No inbox processing protocol** — HENRY/REGINALD have detailed 6-step inbox processing with cross-reference to workbook. BROCK's mail section is lighter (mentions it but lacks the structured protocol).
12. **Prediction ID format undefined** — HENRY uses `HEN-xx`, REGINALD uses `REG-xx`. BROCK's CLAUDE.md doesn't specify a `BRK-xx` format (though PREDICTIONS.tsv exists at root, not in workbook).
13. **Still says "sub-agent of REGINALD"** at bottom — REGINALD's CLAUDE.md clarifies BROCK is a "top-level agent, not a sub-agent." BROCK's own CLAUDE.md contradicts this.
14. **No workbook schema documentation** — HENRY/REGINALD document exact column schemas for KB.tsv, VX.tsv, FLOW.tsv. BROCK's FILES table just lists names with no schema info.
15. **Upcoming catalysts are stale** — Lists Feb 25, Feb 27 dates as upcoming (now past).

## STATUS.md Gaps

1. **Line count OK (142)** — Under 250 limit. ✅
2. **No source tags** — Values lack [CONF]/[EST] tagging throughout.
3. **No "Last context" line** — No quick-orient header for cold boot.
4. **No VOL REGIME equivalent block** — HENRY maintains a 5-line vol regime block. BROCK has no equivalent structured regime summary.
5. **No BOTTOM LINE section** — Missing top-of-file synthesis.
6. **Contains two "PRIOR STATE" delta tables** — 30+ lines of historical deltas that belong in daily notes or workbook, not STATUS.md. Adds bulk without aiding cold boot.
7. **SOURCES section at bottom** — Lists source names but no dates. Should be trimmed or moved.

## Workbook Gaps

1. **No KB.tsv** — HENRY has 88+ entries, REGINALD has 116+. BROCK has none. This is the knowledge base — the most important long-term memory file.
2. **No PREDICTIONS.tsv in workbook** — There's a root-level `PREDICTIONS.tsv` (21 lines) but CLAUDE.md references `workbook/PREDICTIONS.tsv`. Inconsistent location.
3. **No THESIS_VALIDATION.md** — Both HENRY and REGINALD have this. BROCK has EXPECTED_SIGNALS.md which partially covers it but lacks the structured confirmation/invalidation framework.
4. **No VX_HISTORY.tsv** — No archive for slow-moving vectors.
5. **Has good files:** VX.tsv ✅, FLOW.tsv ✅, ML.tsv ✅, plus domain-specific BANK_BDC_MATRIX.tsv and BDC_CASH_COVERAGE.tsv ✅

## Mail System

- ✅ Full mail directory pattern exists: `mail/inbox/`, `mail/outbox/`, `mail/inbox/processed/`, `mail/outbox/delivered/`
- ⚠️ 6 unprocessed signals in inbox (oldest from Feb 24 — 10 days stale)
- ✅ 5 processed signals exist
- Mail system is structurally correct but operationally behind

## Priority Order

1. **Add LESSONS.md** — No institutional memory of mistakes. Every other agent has this. Critical for spawn quality.
2. **Fix CLAUDE.md core rules** — Add `File > verbal`, `#1 RULE: WRITE to STATUS.md`, stale data rules, output rules (tables > prose, 250-line limit). These are the behavioral guardrails.
3. **Add source tags ([CONF]/[EST])** — STATUS.md values need confidence provenance. Without this, stale/estimated data looks the same as confirmed.
4. **Create KB.tsv** — BROCK has no knowledge base. All research is ephemeral without it. Use REGINALD's 14-column schema.
5. **Add BOTTOM LINE block to STATUS.md** — Cold boot orientation. One paragraph: what's the state, what matters most right now.
6. **Prune STATUS.md** — Remove the two "PRIOR STATE" delta tables (move to workbook or daily notes). Add "Last context" line at top.
7. **Create THESIS_VALIDATION.md** — Formalize falsification criteria. Convert EXPECTED_SIGNALS.md into proper 4-category exit rules.
8. **Fix identity: top-level agent, not sub-agent** — CLAUDE.md bottom line says "sub-agent of REGINALD" but BROCK is a top-level agent per REGINALD's own CLAUDE.md.
9. **Standardize prediction ID format** — Define `BRK-xx` and move PREDICTIONS.tsv to consistent location (root or workbook, not both referenced).
10. **Process stale inbox** — 6 signals unread, oldest 10 days. Spawn for inbox duty.
