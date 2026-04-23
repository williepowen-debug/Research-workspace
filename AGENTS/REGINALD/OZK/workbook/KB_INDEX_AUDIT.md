# KB_INDEX Audit Report

**Date:** 2026-03-24 | **Auditor:** Prome (cold-boot simulation)

---

## 1. Cold-Boot Test

**Verdict: INDEX.md → KB_INDEX.md works well.** An agent landing cold can understand the thesis structure in ~5 minutes from these two files alone.

**What works:**
- INDEX.md is excellent as an entry point. Key numbers table gives immediate orientation. Boot sequence with time estimates is practical. File map is comprehensive.
- KB_INDEX.md's thesis-layer organization (Concentration → Mechanism → Catalyst → Geography → Peer → Counter) tells a clear story arc.
- "Quick Lookup" section in KB_INDEX.md is genuinely useful for task-driven navigation.

**What's confusing:**
- INDEX.md "Last session" note says "KB at 93 rows" but the boot table says 136. A cold-boot agent might wonder which is current. The session note is historical context but reads like a current state declaration.
- No explicit mention in KB_INDEX.md of *how* to read KB.tsv (what the 13 columns are, what Conf/Epistemic/Status mean). You have to open the file to find out.

---

## 2. Cross-Reference Accuracy

### EXTEND_PRETEND
- **KB_INDEX says:** Rows 096–104, count **9**
- **Actual KB.tsv:** 096, 097, 099–104 = **8 rows**. Row 098 is tagged `MGMT_CREDIBILITY`.
- **❌ Count is wrong.** Index claims 9, reality is 8. Row 098 ("No concessions" contradiction) was likely moved to MGMT_CREDIBILITY but the index wasn't updated.
- **Synthesis file:** `research/D6_EXTEND_AND_PRETEND.md` exists ✓. Contains no KB row references (see §3).

### GEOGRAPHY
- **KB_INDEX says:** Rows 107–120, count **14**
- **Actual KB.tsv:** 107–116, 118–120 = **13 rows**. Row 117 is tagged `LIFE_SCI`.
- **❌ Count is wrong.** Index claims 14, reality is 13. Row 117 (IQHQ RaDD valuation) is LIFE_SCI, not GEOGRAPHY.
- **Synthesis file:** `GEOGRAPHY/EXPOSURE_MAP.md` exists ✓.

### FL_PARADOX
- **KB_INDEX says:** Rows 121–132, count **12**
- **Actual KB.tsv:** 121–132 = **12 rows** ✓
- **✅ Accurate.**
- **Synthesis file:** `GEOGRAPHY/FL_PARADOX/FINDINGS.md` exists ✓.

### PEER_COMP
- **KB_INDEX says:** Rows 133–136, count **4**
- **Actual KB.tsv:** 133–136 = **4 rows** ✓
- **✅ Accurate.**
- **Synthesis file:** `raw/llm_outputs/OZK_PEER_COMP_claude.md` exists ✓ (note: lives in `sources/`, not `research/`).

### MATURITY_WALL
- **KB_INDEX says:** 20 rows
- **Actual KB.tsv:** 20 rows ✓
- **✅ Accurate.**

---

## 3. Navigation Gaps

### Synthesis files with NO KB row back-references
**This is the biggest structural gap.** Zero research files contain `KB-OZK-NNN` references:
- `research/D6_EXTEND_AND_PRETEND.md` — 0 KB refs
- `research/D3_SHADOW_CRE_LEVER.md` — 0 KB refs
- `research/D2_PLEDGED_LOANS_LIQUIDITY.md` — 0 KB refs
- `GEOGRAPHY/EXPOSURE_MAP.md` — 0 KB refs
- `GEOGRAPHY/FL_PARADOX/FINDINGS.md` — 0 KB refs

`THESIS.md` has 34 KB references — it's the only file that back-references rows. The research files are effectively disconnected from KB.tsv. KB_INDEX.md is the *only* bridge, and it's one-directional (index → file, never file → rows).

### KB groups without dedicated synthesis files
All 16 groups map to *something*, but several map to THESIS.md generically rather than a dedicated deep-dive:
- **ACL_THINNING** → THESIS.md (no standalone analysis)
- **DISTRESSED_LOANS** → THESIS.md (no standalone analysis)
- **MGMT_CREDIBILITY** → THESIS.md (no standalone analysis)

This isn't necessarily wrong — not every group needs its own file — but it means these topics have no deep-dive landing page.

### Orphan synthesis files (no KB_INDEX entry)
These research files exist but aren't referenced in KB_INDEX.md:
- `research/C1_RECLASSIFICATION_REBUTTAL.md` — mapped via BULL_COUNTER but not individually indexed
- `research/C2_RATE_RELIEF_SCENARIO.md` — same
- `research/C3_CAPITAL_ABSORPTION_ANALYSIS.md` — same
- `research/D1_LTV_EXTRAPOLATION.md` — no KB group maps here
- `research/D4_PROBLEM_BANK_COMPARISON.md` — no KB group maps here
- `research/D5_DIVIDEND_SUSTAINABILITY.md` — no KB group maps here
- `research/NDFI_SHADOW_CRE_ANALYSIS.md` — covered by SHADOW_CRE but not listed
- `research/INSIDER_ACTIVITY_COMPILED.md` — no KB group maps here
- `research/8K_FORCED_DISCLOSURE_FRAMEWORK.md` — no KB group maps here

These are all listed in INDEX.md's file map but invisible from KB_INDEX.md. If you're navigating *only* through KB_INDEX, you'd miss half the research folder.

---

## 4. Stale References

| Issue | Location | Status |
|-------|----------|--------|
| EXTEND_PRETEND count says 9, actual 8 | KB_INDEX.md | ❌ Stale |
| GEOGRAPHY count says 14, actual 13 | KB_INDEX.md | ❌ Stale |
| GEOGRAPHY row range "107–120" includes 117 which is LIFE_SCI | KB_INDEX.md | ❌ Misleading |
| EXTEND_PRETEND row range "096–104" includes 098 which is MGMT_CREDIBILITY | KB_INDEX.md | ❌ Misleading |
| INDEX.md "Last session" says "KB at 93 rows" | INDEX.md | ⚠️ Historical but confusing |
| CRE_CONCENTRATION description says "455% CRE/tangible equity" — INDEX.md key numbers say 358% CRE/Tier 1 | KB_INDEX.md vs INDEX.md | ⚠️ Different metrics (tangible equity vs Tier 1) — not wrong but could confuse |
| All file paths in KB_INDEX.md verified to exist | KB_INDEX.md | ✅ Clean |

---

## 5. Recommendations

### Fix Now (5 min)
1. **Fix EXTEND_PRETEND count:** 9 → 8, remove 098 from row range (or note it's cross-listed).
2. **Fix GEOGRAPHY count:** 14 → 13, note 117 is LIFE_SCI not GEOGRAPHY.

### Fix Soon (30 min)
3. **Add KB row anchors to research files.** Each research file should have a header line like:
   ```
   **KB Rows:** 096-097, 099-104 | **Group:** EXTEND_PRETEND
   ```
   This makes navigation bidirectional. Currently it's only top-down.

4. **Add the 9 "orphan" research files to KB_INDEX.md** — either as a new section ("Standalone Research — not tied to a single KB group") or mapped to their closest group. D1, D4, D5, insider activity, 8K framework are all invisible from the navigator.

### Consider (quality of life)
5. **Add a KB.tsv column legend** to KB_INDEX.md — one-liner explaining the 13 columns so agents don't have to open the file to understand the schema.
6. **Separate "row range" from "count"** in KB_INDEX — the row ranges are misleading when they contain gaps (rows reassigned to other groups). Either list exact rows or note exceptions.
7. **Auto-generate KB_INDEX.md** — this file will drift from KB.tsv every time rows are re-grouped. A script that reads KB.tsv and regenerates the index would prevent all the staleness issues found above.

---

*Audit complete. The system is solid — INDEX.md is one of the best cold-boot files I've seen. KB_INDEX.md is a strong navigator with two count errors and one major structural gap (no back-references from synthesis files). The orphan research files are the biggest navigability hole.*
