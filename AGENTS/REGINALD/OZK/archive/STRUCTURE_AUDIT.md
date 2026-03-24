# OZK Structure Audit
**Date:** 2026-03-24 | **Auditor:** Subagent (structure-audit session)
**Scope:** Full folder tree — 42 files across root, research/, sources/, workbook/

---

## 1. STRUCTURAL AUDIT

### Overall Assessment: B+
The folder is well-organized post-restructure (Mar 23). The root/research/sources/workbook hierarchy is clean. The main weakness is **three overlapping planning documents** that should now be collapsed post-KB migration, and two audit reports that serve different purposes but have confusingly similar names.

### What Works
- `root/` holds strategic documents (THESIS, EVIDENCE, SCENARIOS, WEAKNESSES, STATUS)
- `research/` holds deep-dive sub-analyses (C1-C3 rebuttals, D1-D5 opportunities, individual loans)
- `sources/` holds raw extractions and external documents (FDIC, FFIEC, insider scans)
- `workbook/` holds KB.tsv + migration metadata — correct isolation

### Reading Order — Cold-Boot Agent
No README or INDEX exists. A cold-boot agent currently has no obvious entry point. **Recommend creating INDEX.md** (see Section 5 for proposed boot sequence).

### Naming Issues
- `AUDIT_REPORT.md` (general pre-migration audit) vs `AUDIT_REPORT_MAR23.md` (specific contradictions audit, Mar 23-24) — confusingly similar names for different purposes.
- Both are primarily historical artifacts post-KB migration. The live audit output is now `GAP_ANALYSIS_REPORT.md`.

---

## 2. GAP SCAN: KB.tsv vs GAP_ANALYSIS_REPORT.md

### KB.tsv Status
63 rows (1 header + 63 data rows). Breakdown by group:
- ACL_THINNING: 7, CRE_CONCENTRATION: 16, MATURITY_WALL: 5, MEMO_ITEM_3: 3, SHADOW_CRE: 6, DISTRESSED_LOANS: 8, MGMT_CREDIBILITY: 5, CAPITAL_LIQUIDITY: 6, BULL_COUNTER: 5, GAP: 5

### Gaps in GAP_ANALYSIS_REPORT.md NOT in KB.tsv

**GAP_ANALYSIS_REPORT.md has 10 numbered gaps. Coverage in KB:**

| GAP Report Item | KB Coverage | Assessment |
|---|---|---|
| GAP 1: Life sciences vacancy stale | ✅ KB-OZK-060 (IQHQ vacancy stale) | Partial — covers IQHQ but not broader vacancy data staleness |
| GAP 2: TDR/modification data absent | ❌ Not captured | **Missing** — entire TDR angle has no KB row |
| GAP 3: State-level RC-C | ✅ KB-OZK-056 | Captured |
| GAP 4: FHLB collateral haircuts | Partial note in KB-OZK-045 | GAP row not created; D2 mechanics incomplete |
| GAP 5: Peer ACL/NCO table shallow | ❌ Not captured | **Missing** — no KB row flagging peer comp as a gap |
| GAP 6: Short interest undated | ❌ Not captured | **Missing** — SI data appears across files but no GAP row for staleness |
| GAP 7: 8-K monitoring | ❌ Not captured | **Missing** — now time-sensitive (window opened Mar 25) |
| GAP 8: Affinius $2.7B bond source | Partial note in KB-OZK-024 | Notes say "Deep research" but no GAP row for sourcing failure |
| GAP 9: Interest reserve depletion timeline | ❌ Not captured | **Missing** — KB-OZK-016 has the raw data but no GAP row for modeling it |
| GAP 10: Dividend / board precedent | ❌ Not captured | Low priority, acceptable |

**GAP rows needed in KB.tsv (add as new rows):**
1. `GAP | TDR_Modifications | No TDR/modification data pulled. FFIEC RC-N Memo + RC-C Memo Item 1 have it.`
2. `GAP | Peer_ACL_Table | Only 2 named peers. Need ZION, WAL, COLB, FNB for Q4 2025 FDIC data.`
3. `GAP | Short_Interest_Stale | SI "14-15%" undated/unsourced. FINRA published biweekly — pull before earnings.`
4. `GAP | EDGAR_8K_Watch | 8-K monitoring not established. CIK 0001609065 SEC RSS. Window NOW.`
5. `GAP | Reserve_Depletion_Model | $7.0B construction on interest reserves. No model for when reserves exhaust.`

**Unsourced claims in GAP_ANALYSIS_REPORT.md Part 2 — KB coverage:**
- Claim #1 (Bioterra): KB-OZK-057 ✅
- Claim #2 (DBRS vintage): KB-OZK-062 ✅
- Claim #3 (KBRA): Notes in KB-OZK-007 but no dedicated GAP row for KBRA access ❌
- Claim #4 (Affinius): KB-OZK-024 partial ✅
- Claims #5-8: Not captured as GAP rows

### Gaps in KB.tsv NOT in GAP_ANALYSIS_REPORT.md
- KB has 5 GAP rows; report has 10 gaps — KB is incomplete (confirmed above)
- KB-OZK-059 (NCO mislabel) is `CORRECTED` status — fine, accurate
- No material gaps in KB that don't exist in the report

---

## 3. NEW RESEARCH ANGLES (Tradeable, Not Just Complete)

These are NOT in GAP_ANALYSIS_REPORT.md and would make the thesis more **tradeable** — i.e., sharper catalysts, tighter timing, or clearer price targets.

### ANGLE A: Interest Reserve Exhaustion Calendar (HIGH PRIORITY)
**The ask:** Model which construction loans exhaust their interest reserves by quarter. Inputs are in the folder: $7.0B construction on reserves, $108.6M capitalized Q4 (=~$433M/year), average reserve funded at origination (12-18 months of interest is standard). If loans were originated 2022 with 18-month reserves, reserves started exhausting mid-2024. If 36-month reserves, exhaustion hits Q1-Q2 2026 — now. This converts the maturity wall from a narrative into a **quantity and a quarter**.
**Why it's tradeable:** "X billion in construction loans exhaust interest reserves by Q2 2026, forcing $Y nonaccrual additions" is a specific falsifiable forecast. If correct and Q1 2026 earnings show a step-up in nonaccrual additions beyond what the Street models, you have edge.
**Data needed:** OZK's interest reserve policy (earnings call transcripts), RC-B data, back-of-envelope from RCONG376 trend.

### ANGLE B: Sell-Side Consensus Gap (MEDIUM PRIORITY)
**The ask:** Current sell-side ratings and EPS consensus for Q1 2026. Are analysts modeling $50M in quarterly NCOs? More? Less?
**Why it's tradeable:** The best short setups have bullish consensus + deteriorating fundamentals. If the Street is modeling $35M NCOs for Q1 2026 and the maturity wall delivers $65M, that's a direct earnings surprise catalyst. If consensus already models $60M, the surprise isn't there. This is 15 minutes on TipRanks/MarketBeat — and it defines how much of the bear case is already priced.
**Data needed:** MarketBeat or TipRanks consensus EPS and revenue estimates for Q1 2026.

### ANGLE C: OZK's GFC Track Record (HIGH PRIORITY — Thesis Stress Test)
**The ask:** Pull FDIC CERT 110 data for 2007-2012. What were OZK's NCO rates, noncurrent ratios, and ACL coverage during the GFC?
**Why it's tradeable:** The single strongest bull argument is "Gleason has never lost." If OZK's 2009-2010 NCO rate was <20bps while peers were at 2-3%, that's a genuinely powerful counterargument requiring a very specific "this time is different" rebuttal. If OZK's 2009-2010 NCO rate was 80-100bps (still below current trajectory), the bull case collapses. Either way, the answer sharpens conviction — and conviction sizing.
**Data needed:** FDIC API, CERT 110, historical quarterly data. 30-minute pull.

### ANGLE D: Competitor Construction Lenders' Maturity Wall Experience (MEDIUM PRIORITY)
**The ask:** What happened to other banks that were heavy 2022 construction lenders? Did they see a spike in noncurrent construction loans in Q3-Q4 2025?
**Why it's tradeable:** If peers show a 2022-vintage maturity wall effect — rising construction noncurrent in 2025-2026 — it validates the thesis mechanism at an industry level. If peers don't show it (because their borrowers are successfully refinancing), the maturity wall thesis is OZK-specific and may be overstated.
**Data needed:** FDIC QBP construction noncurrent trends by quarter (already have Q4 2025). Pull Q1-Q4 2025 quarterly to see if there's a step-up pattern.

### ANGLE E: Options Market Implied Move vs. Historical Earnings Moves (LOW-MEDIUM)
**The ask:** What is the options market implying for the Apr 16 earnings move? What has OZK's historical 1-day earnings move been over the last 8 quarters?
**Why it's tradeable:** If options imply ±8% and OZK's historical earnings move has been ±4-5%, the puts are rich (theta drag is your enemy). If implied move is ±6% and historical is ±10%, the puts are cheap. This is direct position sizing input.
**Data needed:** Current options chain (available on any brokerage), historical earnings move data (TipRanks/Earnings Whispers).

---

## 4. FILE CONSOLIDATION RECOMMENDATIONS

### EVIDENCE.md vs KB.tsv
**Verdict: Archive EVIDENCE.md, but not yet.**
EVIDENCE.md served as proto-KB before KB.tsv was built. Now that KB.tsv has 63 rows covering the same ground with proper sourcing and confidence tagging, EVIDENCE.md is redundant for *claims*. However, EVIDENCE.md retains value as a **narrative summary document** — it presents tables and context that KB.tsv rows don't. A cold-boot agent can read EVIDENCE.md in 5 minutes and understand the data landscape; scanning 63 KB.tsv rows is slower.

**Recommendation:** Keep EVIDENCE.md until after Apr 16 earnings. After Q1 2026 data is incorporated, archive it to `archive/EVIDENCE_PRE_Q1_2026.md`. Update THESIS.md to reference KB.tsv instead of EVIDENCE.md in its footer.

### GAP_CLOSURE_PLAN.md vs GAP_ANALYSIS_REPORT.md vs RESTRUCTURE_REVIEW.md
**Verdict: Three docs that should compress to one.**

| File | Purpose | Status |
|---|---|---|
| GAP_CLOSURE_PLAN.md | Fix tracker (7 fixes, execution status) | 6/7 fixes COMPLETE. Mostly done. |
| GAP_ANALYSIS_REPORT.md | Deep gap analysis + Part 1-7 findings | The live reference. This is the current audit standard. |
| RESTRUCTURE_REVIEW.md | KB migration plan and schema decision | Migration complete. Purpose served. |

**Recommendation:**
- **Archive RESTRUCTURE_REVIEW.md** → `workbook/archive/RESTRUCTURE_REVIEW.md`. Migration is done, schema chosen. It's institutional memory, not active reference.
- **Archive GAP_CLOSURE_PLAN.md** → `archive/GAP_CLOSURE_PLAN_MAR23.md`. All 7 fixes complete. Remaining open items (Dallas PDNA, state RC-C, FHLB) are now captured in KB.tsv GAP rows.
- **Keep GAP_ANALYSIS_REPORT.md** as the primary analytical audit document. It's the deepest and most recent.

### Two AUDIT_REPORT files
**Verdict: Different purposes — rename, don't merge.**

| File | Content | Verdict |
|---|---|---|
| AUDIT_REPORT.md | Pre-migration consistency audit (denominator conflicts, CRE ratios, charge-off figures) | Archive — all issues resolved or noted in KB.tsv |
| AUDIT_REPORT_MAR23.md | Post-fix integrity audit (B-gap list, A-data checks, C-weaknesses, D-opportunities) | Keep as historical context — some sections still live |

**Recommendation:** Rename to `archive/AUDIT_V1_PRE_MIGRATION.md` and `archive/AUDIT_V2_MAR23.md`. The active audit is now `GAP_ANALYSIS_REPORT.md`.

### STATUS.md
**Verdict: Current but one stale data point.**
STATUS.md price shows "~$49" while SCENARIOS.md uses "~$42-44" — a $7 gap flagged in GAP_ANALYSIS_REPORT.md as "INCONSISTENT." The SCENARIOS.md figure appears more current. STATUS.md also shows the research agenda with "8-K EDGAR watch begins" as "Pending" — this window is NOW (Mar 25+).

**Recommendation:** Update STATUS.md price to ~$43 and mark 8-K watch as "ACTIVE — check daily." Otherwise current. Keep — it's the dashboard.

### Files that can be archived immediately (low risk)
1. `RESTRUCTURE_REVIEW.md` — migration complete
2. `GAP_CLOSURE_PLAN.md` — all fixes done, open items in KB.tsv
3. `AUDIT_REPORT.md` — superseded by MAR23 version and GAP_ANALYSIS_REPORT
4. `EXTERNAL_PROMPTS.md` — check if still needed (likely prompt templates that can archive)

---

## 5. AGENT BOOT OPTIMIZATION

### The Problem
A cold-boot REGINALD agent currently has no INDEX, no README, and no explicit reading order. The folder has 42 files. Reading everything takes 30+ minutes and 50K+ tokens. That's too slow for a pre-earnings sprint.

### Minimum Read Set (7 files, ~15 min, ~15K tokens)

**Tier 1 — Read First (5-8 min)**
1. `STATUS.md` — Current price, positions, catalyst calendar, what's changed. The dashboard. Read this FIRST.
2. `THESIS.md` — The full bear case. Everything else refers back to this. Non-negotiable.
3. `SCENARIOS.md` — Price targets, probability weights, position sizing. Tells you what success looks like.

**Tier 2 — Read if doing research (5-7 min)**
4. `GAP_ANALYSIS_REPORT.md` — What's missing, what's stale, what the priority actions are. Prevents re-discovering known gaps.
5. `workbook/KB.tsv` — The data spine. Cross-reference claims here before asserting them.

**Tier 3 — Task-specific (read when relevant)**
6. `EARNINGS_PREP.md` — Only needed in the 2 weeks before Apr 16. Has watch list, questions, RC-C data.
7. `WEAKNESSES.md` — Only needed if stress-testing or writing rebuttals.

**Never need on boot:**
- `research/C1-C3/`, `research/D1-D5/` — Deep dives. Read only if task involves that specific topic.
- `sources/` — Raw data. Read only to verify a specific claim.
- `AUDIT_REPORT.md`, `AUDIT_REPORT_MAR23.md`, `GAP_CLOSURE_PLAN.md`, `RESTRUCTURE_REVIEW.md` — Historical. Not needed unless doing meta-work.
- `10K_ANALYSIS_2024.md`, `TEMPLE8_SHORT_THESIS_MAR2026.md` — Reference documents, not active.

### Proposed INDEX.md Content

Create `AGENTS/REGINALD/OZK/INDEX.md` with:
```
# OZK — Quick Start

**Thesis:** Short. HIGH conviction. Reservoir of unrecognized CRE losses.
**Positions:** $42.5P May 15 (2), $45P Aug 21 (2)
**Primary catalyst:** Apr 16 Q1 2026 earnings

## Boot Sequence
1. STATUS.md — Dashboard (price, positions, what's changed)
2. THESIS.md — Full bear case
3. SCENARIOS.md — Price targets + position sizing
4. GAP_ANALYSIS_REPORT.md — What's missing, what to do next
5. workbook/KB.tsv — Data spine (63 rows, cite by KB-OZK-NNN)

## Task-Specific Files
| Task | Read |
|---|---|
| Pre-earnings prep | EARNINGS_PREP.md |
| Rebuttal / stress test | WEAKNESSES.md |
| Specific loan detail | EVIDENCE.md |
| Deep rebuttal (C1-C3) | research/C1_*, C2_*, C3_* |
| Opportunity analysis | research/D1_*..D5_* |
| Shadow CRE / NDFI | research/NDFI_SHADOW_CRE_ANALYSIS.md |
| Insider signals | sources/INSIDER_SCAN_OZK.md |
| FDIC data | sources/FDIC_QBP*, FDIC_API_CALL_REPORT* |

## Key Numbers (Q4 2025)
- Price ~$43 | TBV $46.48 | P/TBV 0.93x
- ACL/Noncurrent: 1.39x (FDIC basis)
- CRE/Tier 1: 358% | CRE/Total RBC: 302%
- Noncurrent: $341M (1.07%, up 128% QoQ)
- FY2025 NCO rate: 1.18% | Q4 quarterly: 0.64%
- IQHQ: 97% vacant, ~Aug 2028 maturity
```

---

## 6. SUMMARY ACTION LIST

### Do Now (Before Apr 16)
| Priority | Action | Time |
|---|---|---|
| 🔴 | Create `INDEX.md` with boot sequence | 15 min |
| 🔴 | Update STATUS.md price to ~$43, mark 8-K watch ACTIVE | 5 min |
| 🔴 | Add 5 missing GAP rows to KB.tsv (TDR, peer comp, SI, EDGAR, reserve model) | 15 min |
| 🟡 | Pull sell-side consensus (Angle B) — 15 min, direct input to position sizing | 15 min |
| 🟡 | Pull GFC track record FDIC CERT 110 2007-2012 (Angle C) | 30 min |
| 🟡 | Model interest reserve exhaustion calendar (Angle A) | 1 hour |

### Archive After Apr 16 (Housekeeping)
| Action |
|---|
| Archive RESTRUCTURE_REVIEW.md → workbook/archive/ |
| Archive GAP_CLOSURE_PLAN.md → archive/ |
| Archive AUDIT_REPORT.md, AUDIT_REPORT_MAR23.md → archive/ |
| Archive EVIDENCE.md → archive/EVIDENCE_PRE_Q1_2026.md |
| Snapshot KB.tsv → workbook/archive/KB_Q1_2026.tsv |

### Post-Apr 16 Earnings
- Update STATUS.md with Q1 actuals
- Refresh stale KB rows (anything with Stale_By: 2026-04-30)
- Decide on Wave 2-3 positioning based on earnings
- Update SCENARIOS.md with revised price targets

---

*Written by structure-audit subagent | 2026-03-24*
