# REGINALD SELF-AUDIT REPORT
**Generated:** 2026-03-05 18:25 UTC  
**Auditor:** REGINALD subagent (self-audit task)  
**Scope:** Full domain — STATUS.md, CLAUDE.md, LESSONS.md, PREDICTIONS.tsv, workbook/*, domain/*, inbox/, OUTBOX.md, BANK_EXPOSURE_MATRIX.md, OZK/, RESEARCH_STATUS.md, SUB_AGENTS.md + sub-agent STATUS files  

---

## PRIORITY SUMMARY

| Priority | Count | Items |
|----------|-------|-------|
| 🔴 Fix Now | 6 | Hormuz contradiction, BROCK path mismatch, inbox unprocessed, OUTBOX structure, CREED inbox stale, STATUS bloat |
| 🟠 Fix Soon | 7 | Stale VX prices, SUB_AGENTS.md errors, RENO/TEX staleness, orphaned files, RESEARCH_STATUS.md outdated, earnings_briefs unlisted |
| 🟡 Nice to Have | 5 | CLEANUP_PLAN.md unlisted, workbook naming, BELT unlisted in CLAUDE.md, RENO/TEX empty predictions, VX_HISTORY.tsv empty |

---

## 🔴 FIX NOW

### 1. STATUS.md — Stale Contradictory Hormuz Section (Lines 147-162)
**File:** `STATUS.md`, lines 147–162  
**Issue:** The "HORMUZ → FLORIDA ENERGY SHOCK CASCADE" section still contains the original **wrong** Brent price of "$118-125" in its narrative body (line 147: `"Brent ~$118-125, +10% this week"`), immediately followed by a correction note at line 157 saying that was wrong. The correction note is right, but the original wrong paragraph is still there. Any spawn reading quickly will see the $118-125 and miss the retraction buried below. This is a **live data contradiction within STATUS.md itself**.  
**Fix:** Delete or overwrite lines 147-156 (the original Hormuz section) with a corrected version showing $81.40. Keep the correction context but eliminate the contradictory $118-125 claim.

### 2. STATUS.md — "ATHENE MAPPING — PENDING" vs "RESOLVED" Contradiction
**File:** `STATUS.md`, lines 74 and 170-172  
**Issue:** Line 74 under "PRIVATE CREDIT → BANK TRANSMISSION MAP" says:  
> "**ATHENE MAPPING — PENDING:** BROCK Priority 1 from Feb 27. Which regional banks hold concentrated Athene/Apollo insurer deposits? This is the Stage 4 tripwire and has **NOT** been researched."  

But lines 170-172 under "ATHENE MAPPING — NOW LIVE" say it's **RESOLVED** (ARI → Athene $9B CRE transfer identified).  
**Fix:** Update line 74 to say "RESOLVED — see ATHENE MAPPING section below." Remove or mark the pending language.

### 3. BROCK — Path Mismatch Across Files
**File:** `SUB_AGENTS.md` line 14 vs `CLAUDE.md` line 165  
**Issue:**  
- `SUB_AGENTS.md` says BROCK is at `sub-agents/BROCK/` (doesn't exist under REGINALD)  
- `CLAUDE.md` line 165 correctly says BROCK is at `AGENTS/BROCK/STATUS.md` (top-level agent)  
- BROCK is NOT a sub-agent — it lives at `/home/moltbot/.openclaw/workspace/AGENTS/BROCK/`  
- `SUB_AGENTS.md` also incorrectly describes CORAL's domain as "CLO / Structured Credit" (CORAL is Florida real estate; that's RENO/CREED domain mix)  
**Fix:** Correct BROCK location in `SUB_AGENTS.md`. Fix CORAL domain description. Clarify in SUB_AGENTS that BROCK is a peer agent, not sub-agent.

### 4. INBOX — 2 Unprocessed Signals (Both 🔴 Priority)
**Files:** `inbox/2026-03-04_carl_fl_ui_cliff.md`, `inbox/2026-03-04_hans_european_bank_stress.md`  
**Contents:**  
- **CARL signal:** FL UI exhaustion cliff Mar 24 / Apr 26. WARN cohorts (Dec 2025 layoffs) exhausting 12-week benefits starting Mar 24. CARL requesting REGINALD model credit impact on FL DQ trajectory. 🔴 Priority.  
- **HANS signal:** European bank stress — MFS fraud (Barclays £600M, Jefferies £100M), war risk insurance withdrawal (7/12 P&I clubs by Mar 5), iTraxx Senior Financial ~95bps. Watch DB, BNP, SocGen CDS. 🔴 Priority. Note: STATUS.md shows Barclays £500M from Bloomberg vs this signal's £600M — **values differ**.  
**Fix:** Process both signals. The FL UI cliff (Mar 24) is now <3 weeks away — time-sensitive. The iTraxx/MFS data updates STATUS.md signal dashboard. Also reconcile the Barclays £500M (Bloomberg/STATUS.md) vs £600M (HANS signal) discrepancy.

### 5. CREED INBOX — Unprocessed Signal
**File:** `sub-agents/CREED/inbox/2026-02-27_office_reit_selloff.md`  
**Issue:** A 🟠 priority signal dated Feb 27 (6 days ago) sits unprocessed in CREED's inbox. Contains office REIT selloff data (HPP -10.24%, SLG -8.84%, etc.) plus FDIC CRE data.  
**Fix:** Process or instruct CREED to process. Relevant to STATUS.md office CMBS tracking.

### 6. STATUS.md Size — 216 Lines vs 250-Line Limit (Near Threshold)
**File:** `STATUS.md`  
**Issue:** STATUS.md is 216 lines, approaching the 250-line ceiling in CLAUDE.md rules. The Hormuz section alone is ~20 lines of partially-stale narrative. The "FLORIDA MIGRATION — STRUCTURAL BREAK" section has substantial tables that could be pointers to domain files.  
**Fix:** After fixing the Hormuz contradiction (#1), take the opportunity to compress. Remove the corrected Hormuz narrative to a 3-line summary with pointer to `domain/sources/`. Target 180-190 lines.

---

## 🟠 FIX SOON

### 7. VX.tsv — Multiple Stale Price Rows (Non-KRE Bellwethers)
**File:** `workbook/VX.tsv`  
**Issue:** Several bellwether price rows have old dates:  
- VX-REG-6.02 (VLY): `$11.77` dated **2026-02-05** (28 days stale)  
- VX-REG-6.03 (FLG): `$13.93` dated **2026-01-30** (33 days stale)  
- VX-REG-6.05 (CFG): `$64.00` dated **2026-02-02** (31 days stale)  
- VX-REG-6.07 (KEY): `$21.20` dated **2026-01-26** (38 days stale)  
- VX-REG-6.08 (ZION): `$60.50` dated **2026-01-26** (38 days stale) — and we have a $57.5P position on ZION  
- VX-REG-6.09 (AUB): `$37.00` dated **2026-02-01**  
- VX-REG-6.10 (EGBN): `$26.76` dated **2026-02-01** (we hold $25P Jun on EGBN)  
- VX-REG-6.06 (CMA): marked "merger closed Feb 1" at $95 — CMA merged into Fifth Third, row may be obsolete  
STATUS.md correctly notes "KRE price in VX is stale — use watchlist table" but doesn't say ALL bellwether rows are stale. The VX rows show [STALE] guidance is not applied consistently.  
**Fix:** Mark stale rows. Update prices or apply [STALE] tag per CLAUDE.md rules.

### 8. SUB_AGENTS.md — Outdated Last Sync Dates and Errors
**File:** `SUB_AGENTS.md`  
**Issue:**  
- Last Sync for CREED: **2026-02-13** — CREED STATUS shows last updated **2026-02-25** (12 days newer)  
- Last Sync for BROCK: **2026-02-14** — BROCK is heavily referenced in STATUS.md with Mar 3-4 data (TCPC fraud etc.) — sync tracker is ~18 days behind  
- Last Sync for CORAL: **2026-02-11** — CORAL STATUS shows last updated **2026-03-03** (20 days newer)  
- BELT is listed in STATUS.md sub-agent dashboard but NOT in SUB_AGENTS.md directory  
**Fix:** Update Last Sync Tracker. Add BELT to directory.

### 9. RENO/TEX STATUS.md — 22 Days Stale
**Files:** `sub-agents/RENO/STATUS.md`, `sub-agents/TEX/STATUS.md`  
**Issue:** Both show **Last Updated: 2026-02-11** — 22 days ago. These sub-agents are listed as "Dormant" in RESEARCH_STATUS.md. STATUS.md sub-agent dashboard does NOT list RENO or TEX at all (only CREED, BROCK, CORAL, BELT). If they're dormant, CLAUDE.md lists them in FILES table as active. If active, their STATUS files are badly stale.  
**Fix:** Either: (a) mark them as dormant in CLAUDE.md and move to archive per Step 2 of CLEANUP_PLAN, or (b) spawn them for updates. Decision deferred to Will per CLEANUP_PLAN Step 2 (answer already received: keep active). Since they're kept active, flag for update.

### 10. Orphaned Files — Not in CLAUDE.md FILES Table
**Issue:** Multiple active files not listed in CLAUDE.md:  
- `CLEANUP_PLAN.md` — at root, references ongoing work, no CLAUDE.md mention  
- `RESEARCH_STATUS.md` — 17+ research packages tracked, last updated **2026-02-15** (18 days stale), not in FILES table  
- `SUB_AGENTS.md` — coordination doc at root, not in FILES table  
- `earnings_briefs/` — directory with VLY_Q1_2026.md, not listed in FILES table  
- `session_archive/` — directory with SESSION_LOG_2026-03-03.md, not listed in FILES table  
- `sources/` — directory with 4 source docs, not listed in FILES table  
- `workbook/OTTO_INTEL.md` — listed in FILES table ✅ (307 lines, cross-agent intel)  
- `workbook/THESIS_VALIDATION.md` — NOT listed in FILES table  
**Fix:** Add all to CLAUDE.md FILES table with descriptions.

### 11. RESEARCH_STATUS.md — 18 Days Stale
**File:** `RESEARCH_STATUS.md`  
**Issue:** Last updated **2026-02-15**. STATUS.md references research items from Feb-Mar 2026 that aren't reflected here (TCPC fraud research, MFS fraud contagion, Athene mapping, FDIC Q4 data, Bloomberg MFS confirmation). The "NEXT RESEARCH PRIORITIES" section lists PSEC/FSK Q4 analysis as 🔴 HIGH — this appears to have been completed and resolved (FSK div -31% confirmed, PSEC PIK corrected to 8.6%).  
**Fix:** Update RESEARCH_STATUS.md or acknowledge it's now superseded by STATUS.md and archive it.

### 12. OZK/STATUS.md — Price May Be Stale
**File:** `OZK/STATUS.md`  
**Issue:** Price shown as "~$49" with no date. STATUS.md says "~$45.5 est" for Mar 3. OZK/STATUS last updated **2026-02-25**. Position listed as "PENDING — Aug $40P recommended" but STATUS.md shows `$42.5P Aug ✅` (position taken). Contradiction: OZK/STATUS.md doesn't know the position was entered.  
**Fix:** Update OZK/STATUS.md with: (1) current price ~$45.5, (2) position status changed to ACTIVE (42.5P Aug entered), (3) last updated date.

---

## 🟡 NICE TO HAVE

### 13. workbook/ML.tsv — Naming Convention (Should be KB.tsv?)
**File:** `workbook/ML.tsv`  
**Issue:** CLEANUP_PLAN.md Step 5 notes renaming ML.tsv → KB.tsv to match KB (knowledge base) standard. CLAUDE.md still calls it ML.tsv. This inconsistency exists across all sub-agents (CREED, CORAL, RENO, TEX all have ML.tsv). Decision deferred but worth tracking.  
**Note:** Low priority — functional naming, not broken.

### 14. BELT — Not Listed in CLAUDE.md FILES Table
**Issue:** BELT has its own STATUS.md at `sub-agents/BELT/STATUS.md` and appears in STATUS.md sub-agent dashboard. Not listed in CLAUDE.md FILES table under Sub-Agent Files. No CLAUDE.md or workbook for BELT — appears more limited than full sub-agents.  
**Fix:** Add to CLAUDE.md FILES table. Clarify BELT's scope (geographic diffusion, read-only status monitor).

### 15. RENO/TEX Workbook PREDICTIONS.tsv — Empty (Header Only)
**Files:** `sub-agents/RENO/workbook/PREDICTIONS.tsv`, `sub-agents/TEX/workbook/PREDICTIONS.tsv`  
**Issue:** Both files contain only the header row, no data. These agents ran 7+ research sessions each. No falsifiable predictions were recorded.  
**Fix:** If these agents are being kept active, populate with predictions or formally mark as "no predictions domain."

### 16. workbook/VX_HISTORY.tsv — Empty (Header Only)
**File:** `workbook/VX_HISTORY.tsv`  
**Issue:** File exists but contains only the header row. Purpose is to archive slow-moving VX rows, but nothing has been archived there yet.  
**Fix:** When next VX pruning occurs (step per CLEANUP_PLAN), populate this file.

### 17. CLEANUP_PLAN.md — Root-Level File, Untracked
**File:** `CLEANUP_PLAN.md`  
**Issue:** Created 2026-03-05 (today), documents the Will-approved cleanup plan. Not referenced in CLAUDE.md FILES table. Should be either: (a) listed as an active operations doc, or (b) moved to workbook/ once Step 1 (this audit) is complete.  
**Fix:** Add to CLAUDE.md or move to workbook/ after audit is delivered.

---

## OUTBOX STRUCTURE

**Current:** OUTBOX.md has only a format template and a HERMES delivery timestamp. No PENDING/DELIVERED sections.  
**Assessment:** This is actually **correct** — all signals were cleared by HERMES at 12:47 UTC Mar 4. OUTBOX is clean. However, the format template doesn't show PENDING/DELIVERED headers. If signals accumulate between HERMES runs, there's no organizational structure to distinguish pending vs delivered.  
**Recommendation 🟡:** Add explicit `## PENDING` and `## DELIVERED` section headers as boilerplate so future signals have a home. Not urgent since HERMES clears frequently.

---

## SUB-AGENT STATUS SUMMARY

| Agent | Last Updated | Staleness | Active? | Issues |
|-------|-------------|-----------|---------|--------|
| **CREED** | 2026-02-25 | 8 days | ✅ Active | Inbox signal unprocessed (Feb 27); STATUS within tolerance |
| **CORAL** | 2026-03-03 | 2 days | ✅ Active | Current ✅ |
| **RENO** | 2026-02-11 | 22 days | ⚠️ Dormant | Per RESEARCH_STATUS; no workbook predictions |
| **TEX** | 2026-02-11 | 22 days | ⚠️ Dormant | Per RESEARCH_STATUS; no workbook predictions |
| **BELT** | 2026-02-17 | 16 days | 🟡 Monitor | No CLAUDE.md; limited scope; not in FILES table |

---

## FILES TABLE COVERAGE CHECK (CLAUDE.md)

### Listed in CLAUDE.md ✅
- STATUS.md, LESSONS.md, inbox/, OUTBOX.md, BANK_EXPOSURE_MATRIX.md, PREDICTIONS.tsv, OZK/, domain/sources/, research/, workbook/VX.tsv, workbook/ML.tsv, workbook/FLOW.tsv, workbook/THESIS_VALIDATION.md ❌ (NOT listed — see #10), workbook/OTTO_INTEL.md
- Sub-agents: BROCK (wrong path), CREED ✅, CORAL ✅, TEX ✅, RENO ✅

### Missing from CLAUDE.md FILES table ❌
- `CLEANUP_PLAN.md`
- `RESEARCH_STATUS.md`
- `SUB_AGENTS.md`
- `earnings_briefs/`
- `session_archive/`
- `sources/`
- `workbook/THESIS_VALIDATION.md`
- `workbook/archive/`
- `sub-agents/BELT/` (any reference)

---

## PREDICTION HYGIENE CHECK

| Pred | Timeframe | Status | Issue? |
|------|-----------|--------|--------|
| REG-01 | Through 2026 | OPEN | ✅ Fine |
| REG-02 | H1 2026 | OPEN | ✅ Fine |
| REG-03 | H2 2026 | OPEN | ✅ Fine |
| REG-04 | Q2-Q3 2026 | OPEN | ✅ Fine |
| REG-05 | H2 2026 | OPEN | ✅ Fine |
| REG-06 | H2 2026 | OPEN | ✅ Fine |
| REG-07 | Q2-Q3 2026 | OPEN | ✅ Fine |
| REG-08 | H1 2026 | OPEN | ⚠️ KRE hit ~$67.48 (Mar 4); threshold was <$65; still open |
| REG-09 | Apr 2026 | OPEN | ✅ Fine (Q1 earnings not yet) |
| REG-10 | 2026 | FAILED | ✅ Resolved correctly (PSEC maintained Feb 9-10) |
| REG-11 | H1 2026 | CONFIRMED | ✅ Resolved correctly (FSK -31% Feb 25) |
| REG-12 | Q2 2026 | OPEN | ✅ Fine |
| REG-13 | H1 2026 | OPEN | ⚠️ 8 channels now simultaneously firing per STATUS.md — this may be confirmable now |
| REG-14 | Q1-Q2 2026 | OPEN | ⚠️ WAL -25%+ vs KRE -8.9% = multi-channel banks ARE underperforming; resolve? |
| REG-15 | Q2 2026 | OPEN | ✅ Fine (Call Report data not yet) |
| REG-16 | H1 2026 | OPEN | ✅ Fine (Apr 16 earnings) |
| REG-17 | 2026 | OPEN | ✅ Fine |
| REG-18 | H1 2026 | OPEN | ✅ Fine |
| REG-19 | Q2 2026 | OPEN | ✅ Fine |

**Hygiene Issue:** REG-13 and REG-14 may be confirmable now based on STATUS.md data — flag for review. No past resolve dates are unresolved.

---

## DATA CONTRADICTIONS SUMMARY

| # | Files | Contradiction | Severity |
|---|-------|---------------|----------|
| 1 | STATUS.md lines 74 vs 170 | Athene mapping PENDING vs RESOLVED | 🔴 |
| 2 | STATUS.md lines 147 vs 157 | Brent $118-125 vs $81.40 in same file | 🔴 |
| 3 | inbox/hans vs STATUS.md | Barclays £600M (HANS) vs £500M (STATUS.md) | 🟠 |
| 4 | OZK/STATUS.md vs STATUS.md | OZK position PENDING vs ACTIVE ($42.5P Aug ✅) | 🟠 |
| 5 | SUB_AGENTS.md vs CLAUDE.md | BROCK at sub-agents/BROCK/ vs AGENTS/BROCK/ | 🔴 |
| 6 | STATUS.md vs SUB_AGENTS.md | CORAL described as "CLO/Structured Credit" vs Florida | 🟠 |

---

## STRUCTURAL ISSUES

1. **Root-level clutter:** CLEANUP_PLAN.md, RESEARCH_STATUS.md, SUB_AGENTS.md, BANK_EXPOSURE_MATRIX.md are all at root. Per CLEANUP_PLAN Step 6, reference docs should move to domain/ or workbook/. Will confirmed BANK_EXPOSURE_MATRIX is current — it belongs in domain/sources/ or has its own root home.  
2. **session_archive/** exists but not referenced anywhere in CLAUDE.md. Contains SESSION_LOG_2026-03-03.md. STATUS.md bottom note references it.  
3. **sub-agents/CREED/** has two duplicate DC-DOGE files: `RP-CREED-10_DC-DOGE-Federal-Employment-CRE-Impact.md` AND `RP-CREED-10_DC_OFFICE_FEDERAL_WORKFORCE.md` — same RP-CREED-10 ID, different filenames. Possible duplicate/split research.

---

*Audit complete. Priority order: process inbox signals (🔴 time-sensitive — Mar 24 cliff approaching), fix STATUS.md contradictions, correct BROCK path, update OZK/STATUS.md position status.*
