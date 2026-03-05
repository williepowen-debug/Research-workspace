# HENRY SELF-AUDIT — MAR 5B
**Generated:** 2026-03-05 UTC
**Auditor:** HENRY subagent (self-audit, second pass)
**Note:** Previous audit (workbook/SELF_AUDIT_REPORT.md) resolved STATUS.md line count, OUTBOX structure, and LESSONS.md date. This report focuses on **new or still-open issues only.**

---

## SUMMARY

| Severity | Count | Issues |
|----------|-------|--------|
| 🔴 Fix now | 3 | Duplicate ML IDs, broken file reference, HEN-01 resolution unstaged |
| 🟠 Fix soon | 4 | CLAUDE.md SPAWN PROTOCOL path wrong, ML-HEN-075 data error, VX.tsv still 76% stale, PREDICTIONS H2 result field |
| 🟡 Nice to have | 2 | workbook/ML.tsv out-of-order entry, research/ not in FILES table |

---

## 🔴 CRITICAL — FIX NOW

### 🔴 1. workbook/ML.tsv — DUPLICATE IDs ML-HEN-074 AND ML-HEN-075

**File:** `workbook/ML.tsv`, lines 75–78
**Issue:** Two entries share ID `ML-HEN-074` and two share ID `ML-HEN-075`:

- Line 75: `ML-HEN-074` — "Mar 3 Close Cross-Check vs Web Sources" (VERIFY domain)
- Line 77: `ML-HEN-074` — "Mar 3 EOD CONFIRMED: SPX 6,816.63..." (MACRO domain)
- Line 76: `ML-HEN-075` — "HEN-01 Assessment: 10Y Rising..." (MACRO domain)
- Line 78: `ML-HEN-075` — "Jan ADP = 22K vs 46K expected..." (LABOR domain)

The second ML-HEN-074 (line 77, MACRO/confirmed closes) and second ML-HEN-075 (line 78, LABOR/Jan ADP) appear to be entries that were appended later to correct or supplement earlier entries but given IDs that were already used.

**Fix:** Renumber line 77 to `ML-HEN-074B` or `ML-HEN-087` and line 78 to `ML-HEN-088`. Update any cross-references in PREDICTIONS.tsv or STATUS.md.

---

### 🔴 2. STATUS.md Line 71 — BROKEN FILE PATH REFERENCE

**File:** `STATUS.md`, line 71
**Value:** `See domain/research/GEX_CTA_DEEP_DIVE_MAR3.md`
**Actual path:** `research/GEX_CTA_DEEP_DIVE_MAR3.md`

The file exists at `AGENTS/HENRY/research/GEX_CTA_DEEP_DIVE_MAR3.md` — not inside `domain/`. Any subagent following the STATUS.md reference will get a file-not-found.

**Fix:** Change line 71 to `See research/GEX_CTA_DEEP_DIVE_MAR3.md`

---

### 🔴 3. HEN-01 (NFP Feb <100K) Resolves TOMORROW — No Resolution Protocol Staged

**File:** `PREDICTIONS.tsv`, row HEN-01
**Resolve_Date:** 2026-03-06 (tomorrow)
**Issue:** No note in PREDICTIONS.tsv or STATUS.md about resolution protocol — who spawns HENRY, what data source to use (BLS.gov NFP release ~8:30 AM ET), what counts as "confirmed." If HENRY isn't explicitly spawned on Mar 6, this expires unresolved.

**Fix:** Add to PREDICTIONS.tsv HEN-01 Notes: "Resolves Mar 6 8:30 AM ET. Data source: BLS.gov NFP release. PROME to spawn HENRY morning of Mar 6." Add to OUTBOX.md: flag PROME to spawn HENRY on Mar 6.

*(This was flagged in the previous audit but appears unactioned.)*

---

## 🟠 SIGNIFICANT — FIX SOON

### 🟠 4. CLAUDE.md SPAWN PROTOCOL Step 5 — Wrong Path

**File:** `CLAUDE.md`, line 24
**Value:** `Research detail → \`domain/sources/\``
**Actual location of research outputs:** `research/outputs/` (not `domain/sources/`)

There is a `domain/sources/` directory (`domain/sources/Lighthouse_Macro_Prices_Framework_2026-02.md`) but the bulk of HENRY's research outputs live in `research/outputs/cluster_*/`. A subagent following step 5 literally would write to the wrong place.

**Fix:** Update step 5 to: `Research detail → \`research/outputs/\` (or \`domain/sources/\` for external reference docs)`

---

### 🟠 5. workbook/ML.tsv Line 76 — ML-HEN-075 Data Error (Stale Confidence Value)

**File:** `workbook/ML.tsv`, line 76
**Entry:** ML-HEN-075, "HEN-01 Assessment: 10Y Rising..." 
**Content says:** "HEN-01 (NFP <100K, 60%) MAINTAINED"
**Contradiction:** PREDICTIONS.tsv and STATUS.md both show HEN-01 at **70%** (upgraded after Jan ADP). The 60% figure in this entry is from a pre-upgrade assessment.

This creates a misleading internal record — a future agent reading ML-HEN-075 would see 60% confidence when the canonical PREDICTIONS.tsv says 70%.

**Fix:** Correct the text in ML-HEN-075 (line 76) to read "HEN-01 (NFP <100K, 70%) MAINTAINED" — reflecting the post-ADP upgrade.

---

### 🟠 6. workbook/VX.tsv — Still 76% Stale (Previous Audit Open Item)

**File:** `workbook/VX.tsv`
**Status:** Previous audit flagged 69/91 rows stale. Current file has 44 rows visible (compressed by section comment references). The top 5 rows are current (Mar 3-4 data) but the commented-out slow-moving rows are still archived by reference only.

The primary concern: **VX-HEN-4.01 (VIX Level)** shows 26.43 from Mar 3, but VIX compressed to ~24-25 on Mar 4 after Iran peace-talk rally. The row is marked Mar 3 but STATUS.md now shows ~24-25 est for Mar 4. Not yet updated.

**Fix:** On next session spawn, update VX-HEN-4.01 to Mar 4 closing value once confirmed. Consider whether the 5-row "current" section accurately reflects Mar 4 levels or is still Mar 3.

---

### 🟠 7. PREDICTIONS.tsv — H2 Result Field Ambiguous

**File:** `PREDICTIONS.tsv`, row H2
**Status:** STALE, Result: INVALID
**Issue:** The Notes say "Condition structurally invalid — vol regime shifted." Result says "INVALID" which is correct, but the previous audit flagged this and the field was updated. Verify it now reads "INVALID" not "N/A" (was "N/A" before previous audit). ✅ Confirmed fixed — Result is now "INVALID." No action needed, marking as verified.

---

## 🟡 MINOR — NICE TO HAVE

### 🟡 8. workbook/ML.tsv Entry Out of Order — ML-HEN-068 After ML-HEN-069

**File:** `workbook/ML.tsv`
**Issue:** ML-HEN-069 (line 69, Mar 4 pre-market IWM cascade) appears before ML-HEN-068 (line 70, Feb 27 triple confluence). The IDs suggest 068 should precede 069, but chronologically ML-HEN-068 (Feb 27) predates ML-HEN-069 (Mar 4). Looks like 068 was backfilled after 069 was written.

**Impact:** Low — entries are date-stamped, so chronological queries still work. IDs are out of sequence but not wrong.

**Fix:** Note at top of workbook/ML.tsv: "IDs are sequential by creation, not by event date. ML-HEN-068 was backfilled after ML-HEN-069."

---

### 🟡 9. CLAUDE.md FILES Table — research/ Directory Not Listed

**File:** `CLAUDE.md`, FILES table
**Issue:** The FILES table lists domain/, workbook/, inbox/, OUTBOX.md, etc. but does NOT list `research/` even though it contains:
- `research/GEX_CTA_DEEP_DIVE_MAR3.md` (referenced in STATUS.md)
- `research/outputs/` (8+ cluster outputs)
- `research/prompts/` (12+ research prompts)
- `research/prompts/README.md`

A spawned agent reading CLAUDE.md would have no idea the research/ directory exists.

**Fix:** Add to FILES table: `\`research/\`` — Research outputs and prompts from LLM deep-dives.`

---

## VERIFICATION CHECKLIST — Previous Audit Items

| Item | Previous Status | Current Status |
|------|----------------|----------------|
| STATUS.md line count | 247 (near limit) | ✅ 167 lines — FIXED |
| OUTBOX.md structure | No delivery sections | ✅ Has PENDING/DELIVERED — FIXED |
| LESSONS.md last-reviewed date | 2026-02-27 (stale) | ✅ 2026-03-05 — FIXED |
| H2 Result field (N/A → INVALID) | N/A | ✅ Now "INVALID" — FIXED |
| HEN-01 resolution protocol | Unactioned | 🔴 Still not staged |
| STATUS.md tariff data contradiction | 3/4 vs 9/12 | ✅ Appears resolved in current STATUS.md |

---

## FRICTION POINTS — CLAUDE.md Instruction Quality

1. **SPAWN PROTOCOL step 5 path error** (see 🟠4 above) — actionable friction.
2. **"INBOX processing is a separate task"** — clear and good.
3. **Stale Data Rules** — the ">50% stale, note it and move on" rule is practical. Slightly ambiguous: does "move on" mean don't update VX.tsv at all, or just don't read it? Suggest: "skip reading stale rows; still write new data to current rows."
4. **"STATUS.md stays under 250 lines"** — the limit was nearly breached before. Consider reducing target to 200 lines with explicit pruning rule: "If >200 lines at session end, archive one section to workbook/."

---

*End of audit. Fix 🔴 items before next HENRY spawn, especially HEN-01 resolution staging given Mar 6 NFP.*
