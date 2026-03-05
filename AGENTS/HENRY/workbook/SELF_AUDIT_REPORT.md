# HENRY SELF-AUDIT REPORT
**Generated:** 2026-03-05 UTC
**Auditor:** HENRY subagent (self-audit)
**Scope:** All files in AGENTS/HENRY/

---

## SUMMARY

| Severity | Count | Category |
|----------|-------|----------|
| 🔴 Fix now | 3 | OUTBOX undelivered, HEN-01 imminent resolution, data contradiction |
| 🟠 Fix soon | 5 | STATUS.md near limit, VX.tsv mass staleness, LESSONS.md stale, OUTBOX no delivery markers, Beige Book inconsistency |
| 🟡 Nice to have | 4 | Orphaned files, cluster_8 missing prompt, workbook ML.tsv format confusion, TRADE.md deprecated note |

---

## 🔴 CRITICAL ISSUES

### 🔴 1. OUTBOX.md — No Delivery Confirmation Markers
**File:** `OUTBOX.md` (122 lines)
**Issue:** The Beige Book analysis letter (dated 2026-03-05 01:00 UTC, To: WILL) has no delivery status. CLAUDE.md says "HERMES delivers" — but there's no DELIVERED/PENDING flag anywhere in the file. It's unclear whether this report ever reached Will or is sitting unread.
**Action:** Confirm delivery with HERMES, or add a `**Status: DELIVERED/PENDING**` header to OUTBOX entries.

### 🔴 2. HEN-01 Resolves TOMORROW (2026-03-06) — No Resolution Protocol Staged
**File:** `PREDICTIONS.tsv`, row 2
**Issue:** HEN-01 (NFP Feb <100K, 70%) resolves 2026-03-06. Today is 2026-03-05. There's no note in STATUS.md or PREDICTIONS.tsv about who resolves this or what data source to use. If HENRY isn't spawned on Mar 6, this prediction goes unresolved past its date.
**Action:** Add resolution note to PREDICTIONS.tsv. Flag in OUTBOX for PROME to spawn HENRY on NFP day.

### 🔴 3. Beige Book Tariff Data Contradiction
**File:** `STATUS.md` line 59 vs line 227
- Line 59 (SESSION LOG): "3 of 4 districts citing tariffs for price pressures" 
- Line 227 (BEIGE BOOK SCORECARD): "9/12 districts" for margin squeeze
- OUTBOX.md line ~105: notes this inconsistency explicitly ("synthesis says 3 of 4... document says 9/12")

**Issue:** The STATUS.md session log headline says "¾ districts" (from the initial Beige Book summary), but the full scorecard says 9/12. These refer to slightly different metrics (tariff MENTIONS vs price squeeze breadth) but the inconsistency is confusing and the status header at line 1 uses "¾ DISTRICTS CITING TARIFFS" which is the less accurate framing.
**Action:** Clarify in STATUS.md: "3/4 districts reported tariff-driven price ACCELERATION; 9/12 cited tariff price pressures overall."

---

## 🟠 SIGNIFICANT ISSUES

### 🟠 4. STATUS.md Near 250-Line Limit
**File:** `STATUS.md`
**Line count:** 247 lines (limit: 250)
**Issue:** Three lines from the hard limit. Any meaningful update will breach the cap. The file cannot absorb NFP resolution, FOMC updates, or any new signal without pruning first.
**Action:** Archive the detailed SESSION LOG (lines ~60-100) to `workbook/SESSION_LOG_MAR4.md`. The ISM/ADP data is already summarized in the signal dashboard. This should free 20-30 lines.

### 🟠 5. workbook/VX.tsv — 69/91 Rows Are STALE (76%)
**File:** `workbook/VX.tsv`
**Issue:** 69 of 91 rows contain `[STALE]` in the Notes column. CLAUDE.md's Stale Data Rules say: "If >50% stale, note it and move on." We are at 76% stale. Most stale rows are dated 2026-01-26 (6 weeks ago). Only the GAM domain rows (VX-HEN-9.xx) and a few SEN rows have been updated to Mar 3.
**Specifically stale and high-relevance:**
- VX-HEN-4.01 (VIX Level): shows 26.43 from Mar 3 — but VIX compressed on Mar 4 to ~24-25 (still in STATUS.md as EST not CONF)
- VX-HEN-4.02 (Put/Call Ratio): 2026-01-26, marked stale
- VX-HEN-7.01 (Insider Sell/Buy): 2026-01-26, pre-Feb27
- VX-HEN-11.01-11.03 (COT): 2026-02-03, stale
**Action:** On next spawn, refresh at minimum: VX-HEN-4.01, VX-HEN-4.02, VX-HEN-7.01, VX-HEN-9.01 (GEX), VX-HEN-9.06 (IV Percentile). Archive deeply stale rows (>6 weeks, slow-moving metrics) to `workbook/VX_HISTORY.tsv`.

### 🟠 6. LESSONS.md Not Reviewed Since 2026-02-27
**File:** `LESSONS.md`
**Issue:** "Last reviewed: 2026-02-27" — 6 days ago. Mar 3-4 generated significant new lessons (LIQUID HY OAS model was 30bps too high two sessions in a row; ADP consensus revision framing; peace-talk-as-catalyst pattern). None are captured in LESSONS.md.
**Missing lessons to add:**
1. LIQUID's HY OAS model overestimates by ~30bps (repeat error). Don't use LIQUID's estimates directly — apply -30bps discount.
2. ADP consensus revision: market revised consensus from 130K to 50K, then called +63K a beat. Verify consensus at time of release, not post-revision.
3. Peace talk leaks → temporary VIX compression not fundamentally resolved. Don't adjust thesis on geopolitical headlines alone.
**Action:** Update LESSONS.md and reset last-reviewed date.

### 🟠 7. OUTBOX.md Has No Structural Delivery Tracking
**File:** `OUTBOX.md`
**Issue:** The file is a single continuous document (the Beige Book letter). There's no `---DELIVERED---` section, no pending queue, no status flags. CLAUDE.md says "OUTBOX.md: Outgoing signals (HERMES delivers)" but the file contains a full-length letter to Will with no way to confirm delivery or add new signals without confusing formats.
**Action:** Add a header section: `## PENDING DELIVERY` and `## DELIVERED` to separate queue state from content. Or clear the OUTBOX once delivered and archive to `workbook/`.

### 🟠 8. H2 in PREDICTIONS.tsv — Resolve Date Was 2026-03-05 (Today), Listed as STALE
**File:** `PREDICTIONS.tsv`, row 3
**Issue:** H2 has `Status: STALE`, `Resolve_Date: 2026-03-05`, `Result: N/A`. The status says it was retired (VIX condition broken), which is correct. But the Result field is "N/A" when it should be "MISS" or "INVALID" (condition never met). This is accurate enough but could confuse the prediction hygiene log.
**Action:** Change Result from "N/A" to "INVALID — precondition never met" for clarity.

---

## 🟡 MINOR ISSUES

### 🟡 9. Orphaned Files Not Referenced in CLAUDE.md
**Files:**
- `workbook/CTA_CREDIT_IMPLEMENTATION_SUMMARY.md` — not in CLAUDE.md FILES table
- `workbook/SESSION_LOG_MAR3.md` — not in CLAUDE.md FILES table  
- `workbook/ISM_SYNTHESIS_MAR4.md` — referenced in STATUS.md footer but not CLAUDE.md
- `workbook/VOL_TRADE_ANALYSIS_FEB2026.md` — not referenced anywhere
- `workbook/TRADE_DEPRECATED_MAR4.md` — referenced implicitly (CLAUDE.md says TRADE.md deprecated)
- `sources/` directory (3 Burry files) — referenced in STATUS.md as archive but not in CLAUDE.md FILES table
- `research/` directory (entire tree) — not mentioned in CLAUDE.md FILES table
**Action:** Either add to CLAUDE.md FILES table or add a note: "see workbook/ and research/ for archived analysis."

### 🟡 10. research/prompts/cluster_8 Has No Corresponding Output
**Path:** `research/prompts/cluster_8_systematic_flows/` — prompt exists
**Path:** `research/outputs/cluster_8_systematic_flows/RP-HEN-8.1_systematic_flow_mapping_output.md` — output EXISTS
**Status:** Actually not missing, cluster_8 output is present. ✅ No action needed.
*(Clusters 4 and 5 have prompts but NO outputs — may be incomplete research.)*

### 🟡 11. workbook/ML.tsv vs Root ML.tsv — Format Confusion Risk
**Files:** `workbook/ML.tsv` (89 rows, format: ID/Date/Domain/Title/Content/Confidence/Links) vs `ML.tsv` (8 rows, format: Date/Event/My_Est/Actual/Consensus/Error/Direction_Correct/Notes)
**Issue:** CLAUDE.md explicitly says these are DIFFERENT ("Root TSVs are canonical. workbook/ is reference/archive."). However, the workbook/ML.tsv has a completely different format from root ML.tsv. The naming is confusing — workbook/ML.tsv is actually the **knowledge base** (research findings), while root ML.tsv is the **data release accuracy log**. Both are named ML.tsv.
**Action:** Consider renaming `workbook/ML.tsv` to `workbook/KB.tsv` (Knowledge Base) to eliminate name collision confusion. Update CLAUDE.md FILES table accordingly.

### 🟡 12. ECON_CALENDAR.md — Needs Verification After NFP
**File:** `domain/ECON_CALENDAR.md`
**Issue:** Calendar covers Mar-Jun 2026. NFP Mar 6 is tomorrow's key event (HEN-01). After NFP resolves, the calendar should be updated to reflect the result and any forward calendar adjustments.
**Action:** Post-NFP, update ECON_CALENDAR.md with NFP result and flag next data point (CPI Mar 11).

---

## FILE EXISTENCE CHECK vs CLAUDE.md FILES TABLE

| File | Referenced In | Exists? | Status |
|------|--------------|---------|--------|
| `STATUS.md` | CLAUDE.md | ✅ | OK |
| `LESSONS.md` | CLAUDE.md | ✅ | OK (stale) |
| `inbox/` | CLAUDE.md | ✅ | OK (empty — all processed) |
| `OUTBOX.md` | CLAUDE.md | ✅ | OK (no delivery markers) |
| `PREDICTIONS.tsv` | CLAUDE.md | ✅ | OK |
| `ML.tsv` | CLAUDE.md | ✅ | OK |
| `domain/ECON_CALENDAR.md` | CLAUDE.md | ✅ | OK |
| `domain/BEIGE_BOOK_MAR4_2026.md` | CLAUDE.md | ✅ | OK |
| `workbook/ML.tsv` | CLAUDE.md | ✅ | OK (format confusion — see #11) |
| `workbook/VX.tsv` | CLAUDE.md | ✅ | OK (76% stale — see #5) |
| `workbook/FLOW.tsv` | CLAUDE.md | ✅ | OK |

**All referenced files exist. No missing files.**

---

## ORPHANED FILES (Exist But Not Referenced in CLAUDE.md)

| File | Last Modified | Risk |
|------|--------------|------|
| `workbook/CTA_CREDIT_IMPLEMENTATION_SUMMARY.md` | Unknown | Low — useful archive |
| `workbook/SESSION_LOG_MAR3.md` | 2026-03-03 | Low — archive |
| `workbook/ISM_SYNTHESIS_MAR4.md` | 2026-03-04 | Low — referenced in STATUS footer |
| `workbook/VOL_TRADE_ANALYSIS_FEB2026.md` | ~2026-02 | Low — archive |
| `workbook/TRADE_DEPRECATED_MAR4.md` | 2026-03-04 | Low — explicitly deprecated |
| `workbook/VX_HISTORY.tsv` | Unknown | Low — archival |
| `sources/Burry_*.md` (3 files) | 2026-02 | Low — referenced in STATUS |
| `research/` (entire tree) | Various | Low — useful but unindexed |
| `archive/` (entire tree) | Various | Low — explicitly archived |
| `domain/sources/` | Various | Low — research inputs |

---

## PREDICTION HYGIENE CHECK

| ID | Resolve Date | Status | Issue |
|----|-------------|--------|-------|
| HEN-01 | 2026-03-06 | ACTIVE | ⚠️ Resolves TOMORROW — needs resolution protocol |
| H2 | 2026-03-05 | STALE | 🟠 Result should be "INVALID" not "N/A" |
| HEN-04 | 2026-03-18 | ACTIVE | ✅ 13 days out, on track |
| H1, H5, H7 | 2026-03-31 | ACTIVE | ✅ 26 days out |
| HEN-02, HEN-03 | 2026-04-06 | ACTIVE | ✅ OK |
| H4 | 2026-06-30 | ACTIVE | ✅ Long-duration, OK |
| HEN-05 | 2026-05-10 | ACTIVE | ✅ OK |

**No overdue unresolved predictions.** HEN-01 is imminent.

---

## DATA QUALITY SUMMARY

**Root ML.tsv (7 data rows):** Complete. All fields populated. Direction_Correct column has "N/A" on rows where it's not applicable — acceptable.

**workbook/ML.tsv (88 data rows):** Complete format. All entries have ID, Date, Domain, Title, Content, Confidence, Links. No gaps found in spot-check.

**workbook/VX.tsv (91 rows):** 76% stale. High-relevance rows (GAM domain) updated through Mar 3. BID domain rows all dated 2026-01-26 and marked slow-moving — acceptable for those metrics. SEN/COT domain rows dated 2026-01-26 to 2026-02-03 — should be refreshed.

**workbook/FLOW.tsv:** Spot-checked. Format inconsistency — rows 1-5 have 6 columns (no date/status fields), rows 6+ have 8+ columns with ACTIVE/ARMED status appended inline. Not a structural break but makes TSV parsing inconsistent. 🟡 Minor.

---

## PRIORITY ACTION LIST

1. 🔴 Confirm OUTBOX delivery to Will — verify Beige Book letter was received
2. 🔴 Stage HEN-01 resolution for 2026-03-06 NFP (add note to PREDICTIONS.tsv, alert PROME)
3. 🔴 Fix STATUS.md Beige Book tariff framing (line 1 header + line 59)
4. 🟠 Prune STATUS.md to <230 lines before next spawn (archive Mar 4 session log)
5. 🟠 Update LESSONS.md with 3 new lessons from Mar 3-4
6. 🟠 Fix H2 Result field: "N/A" → "INVALID — precondition never met"
7. 🟠 Add delivery tracking structure to OUTBOX.md
8. 🟡 Consider renaming workbook/ML.tsv → workbook/KB.tsv
9. 🟡 Add workbook/ and research/ overview to CLAUDE.md FILES table
10. 🟡 Post-NFP: update ECON_CALENDAR.md
