# KB.tsv — Group Index

**Updated:** 2026-03-24 | **Total rows:** 136 | **Groups:** 16

Navigate the KB by investigation cluster. Each group maps to a folder or research file where the full synthesis lives.

---

## Thesis Layer 1: Concentration & Structure

| Group | Rows | Count | Folder / File | What It Covers |
|-------|------|-------|---------------|----------------|
| **CRE_CONCENTRATION** | 007–015, 048–050 | 12 | THESIS.md (core) | 455% CRE/tangible equity, C&D at 197%, RESG 54.4% of loans, $500M hold cap |
| **SHADOW_CRE** | 021–027 | 7 | research/D3_SHADOW_CRE_LEVER.md | MI3 at 37.6% ($1.289B hidden CRE in C&I), NDFI $2.74B debt-on-debt |
| **MEMO_ITEM_3** | 018–020, 087 | 4 | research/D3_SHADOW_CRE_LEVER.md | MI3/C&I ratio worst in peer set, reclassification rebuttal |
| **CAPITAL_LIQUIDITY** | 042–047 | 6 | research/D2_PLEDGED_LOANS_LIQUIDITY.md | 74% loans pledged, $11.9B uninsured deposits, FHLB capacity |

## Thesis Layer 2: Mechanism (Extend-and-Pretend)

| Group | Rows | Count | Folder / File | What It Covers |
|-------|------|-------|---------------|----------------|
| **EXTEND_PRETEND** | 096–097, 099–104 | 8 | **research/D6_EXTEND_AND_PRETEND.md** | 590 mods, 98% classification gap, 59% re-default, NPL forensics. (098 cross-listed → MGMT_CREDIBILITY) |
| **DISTRESSED_LOANS** | 028–036 | 9 | THESIS.md (evidence) | Named problem loans: IQHQ RaDD, Sterling Bay, Boston, Seattle, Santa Monica |
| **LIFE_SCI** | 094–095, 117 | 3 | GEOGRAPHY/ (SD cluster) | $3.2B life sci exposure, Pacific Center sold to SVP, SD cap rate blow-out |
| **MGMT_CREDIBILITY** | 037–041, 069, 085, 093, 098 | 9 | THESIS.md (narrative) | "No concessions" contradiction, CRO vacancy, CFO selling, buyback non-use |

## Thesis Layer 3: Catalyst & Timing

| Group | Rows | Count | Folder / File | What It Covers |
|-------|------|-------|---------------|----------------|
| **ACL_THINNING** | 001–006, 105 | 7 | THESIS.md (core) | ACL 1.16% < NCO 1.18% (reserve inversion), coverage 1.39x declining, NIM compression |
| **MATURITY_WALL** | 016–017, 061–063, 074–078, 080–084, 086, 088–091 | 20 | THESIS.md + sources/V1-V4 | $13.8B 2022 vintage, 36-42mo terms → H1-H2 2026 maturities, interest reserve depletion model, $47M/qtr net burn |

## Geographic Analysis

| Group | Rows | Count | Folder / File | What It Covers |
|-------|------|-------|---------------|----------------|
| **GEOGRAPHY** | 107–116, 118–120 | 13 | **GEOGRAPHY/EXPOSURE_MAP.md** | 58 MSAs mapped, $2.9B distressed cluster (5 metros), FL paradox intro, supervisory mismatch, $2B unleased pipeline. (117 → LIFE_SCI) |
| **FL_PARADOX** | 121–132 | 12 | **GEOGRAPHY/FL_PARADOX/FINDINGS.md** | 4-model stress-test: deposit wall, SB 4-D moat, insurance, Biscayne 21 ($105M), FinCEN, concentration duality |

## Peer Comparison

| Group | Rows | Count | Folder / File | What It Covers |
|-------|------|-------|---------------|----------------|
| **PEER_COMP** | 133–136 | 4 | sources/OZK_PEER_COMP_claude.md (best) | 8-bank Q4 2025 table. OZK 5.4x peer NCO, 7x C&D, coverage BELOW median. WAL thinnest at 90%. |

## Counter-Arguments & Gaps

| Group | Rows | Count | Folder / File | What It Covers |
|-------|------|-------|---------------|----------------|
| **BULL_COUNTER** | 051–055, 064–068, 070–073, 079, 092, 106 | 17 | research/C1-C3 + WEAKNESSES.md | GFC track record (11bps 22yr avg), record EPS $6.18, $1.3B sponsor extractions, 45.9% LTC, thin EV edge |
| **GAP** | 056–060 | 5 | GAP_ANALYSIS_REPORT.md | Known data gaps: short interest undated, IQHQ leasing unknown, Form 4 stale |

---

## Standalone Research (not tied to a single KB group)

These research files exist in `research/` but span multiple KB groups or predate the KB system. They're indexed in `INDEX.md` but not directly reachable from the group tables above.

| File | Topic | Closest KB Groups |
|------|-------|--------------------|
| C1_RECLASSIFICATION_REBUTTAL.md | "MI3 reclassification is normal" rebuttal | BULL_COUNTER, MEMO_ITEM_3 |
| C2_RATE_RELIEF_SCENARIO.md | Do rate cuts save OZK? | BULL_COUNTER, MATURITY_WALL |
| C3_CAPITAL_ABSORPTION_ANALYSIS.md | Thin EV edge counter-argument | BULL_COUNTER |
| D1_LTV_EXTRAPOLATION.md | LTV stress on reappraised loans | CRE_CONCENTRATION, DISTRESSED_LOANS |
| D4_PROBLEM_BANK_COMPARISON.md | OZK vs problem bank thresholds | ACL_THINNING, CRE_CONCENTRATION |
| D5_DIVIDEND_SUSTAINABILITY.md | Dividend cut probability model | CAPITAL_LIQUIDITY |
| 8K_FORCED_DISCLOSURE_FRAMEWORK.md | Pre-announcement triggers & timeline | MGMT_CREDIBILITY |
| INSIDER_ACTIVITY_COMPILED.md | Form 4 compilation | MGMT_CREDIBILITY |
| NDFI_SHADOW_CRE_ANALYSIS.md | $2.74B shadow CRE deep dive | SHADOW_CRE |

---

## KB.tsv Column Legend

| Column | Meaning |
|--------|---------|
| ID | `KB-OZK-NNN` unique identifier |
| Date | When the row was created |
| Group | Cluster tag (maps to this index) |
| Entity | Specific topic within the group |
| Fact | The actual data point or finding |
| Source | Where it came from (filing, LLM, FDIC, etc.) |
| Conf | Confidence: A=high, B=medium, C=low; 1=primary, 2=secondary, 3=derived |
| Epistemic | EMPIRICAL (hard data), ANALYTICAL (derived), ESTIMATE, THEORETICAL |
| Status | ACTIVE, STALE, SUPERSEDED, ARCHIVED |
| Stale_By | Date after which this should be refreshed |
| DerivedFrom | Parent KB row(s) if this builds on prior evidence |
| Vectors | Cross-agent references (→REGINALD, →CARL, etc.) |
| Notes | Analyst commentary, implications, caveats |

---

## Quick Lookup

**By thesis question:**
- "Is OZK too concentrated?" → CRE_CONCENTRATION + SHADOW_CRE + PEER_COMP
- "Are they hiding losses?" → EXTEND_PRETEND + MGMT_CREDIBILITY
- "When do losses hit?" → MATURITY_WALL + ACL_THINNING
- "What about Florida?" → FL_PARADOX (answer: it's fine, not where thesis breaks)
- "What's the bull case?" → BULL_COUNTER

**By earnings prep (Apr 16):**
- Charge-off estimate → ACL_THINNING + DISTRESSED_LOANS + LIFE_SCI
- Management credibility questions → MGMT_CREDIBILITY + EXTEND_PRETEND (098)
- Peer positioning → PEER_COMP (133-136)
- Geographic stress → GEOGRAPHY (111, 114, 117)

---

*Master data → `KB.tsv` | Thesis → `../THESIS.md` | Boot → `../INDEX.md`*
