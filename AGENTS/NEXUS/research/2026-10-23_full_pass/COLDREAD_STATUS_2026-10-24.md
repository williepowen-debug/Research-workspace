Model: Sonnet 5.5 (claude-sonnet-5-5) · date: Sat Oct 24 11:33:06 EDT 2026
COLDREAD of AGENTS/NEXUS/STATUS.md (24.5 KB)

## 1. POINTER INTEGRITY
- Antecedent row (L39): "Context roots, none a break vote; states as of 10/23 -> `STATUS_COLD.md` §H22A." Target STATUS_COLD.md L1717: "### §H22A — ANTECEDENT MAP context-root rows R6 · R8 · R11 · R12 · Climate/power · R5, states as of the 10/23 PM full pass (crc32 ..., 1237 B)". EXISTS, all six rows present. Pointer carries resolvers: BOJ 10/29-30, TIC ~mid-Nov, Plenum 10/26-29 + 11/10 clocks, MWD 10/27, WATT/CORAL 10/29, R5 none registered. Actionable. Docket cross-check: BOJ 10/29, Plenum 10/26-29, MWD 10/27 agree. CORAL MSI 10/29, Sept TIC, R11 "11/10 clocks" have no docket row (docket L109-112 has only PRED-38/CPI on 11/10) - not a disagreement, but no dated wake on the board.
- Threshold row (L81): "Dated owner states -> `STATUS_COLD.md` §H22B." Target L1726: "### §H22B — THRESHOLD 'Other owner states' row (crc32 e0c2c64b, 190 B)". EXISTS. Hot row keeps names and state tokens but drops dates and resolvers (Rhine FIRED, no date; FLG RED, no CRE count). No resolver named in the pointer; the stranger must open cold file to get dates.
- Header (L3): "Delta annotation 1 of 2 (10/23 22:1x catch-up) -> `STATUS_COLD.md` §H22C". Target L1730: "### §H22C — header delta-annotation sentence, 10/23 22:1x ET catch-up (crc32 3bbb9ca5, 243 B)". EXISTS. Pointer says "1 of 2" but no annotation 2 is visible anywhere; reader cannot tell whether a second one exists.

## 2. THE CORRECTED SENTENCE
L9: "Approved NOT-FIRED cards (WQ-513/514): HYG on REG-T-04 (HY OAS >350 ×3 — my letters' ICE HY series, count once) · ORCL on ORCL's own 5Y CDS ≥350 with ORCL ≥$120 (a different instrument, correlated not identical) [corrected 10/24, reviewer via Will]."
A stranger reads two different triggers: yes (HY OAS index vs ORCL's own CDS; "a different instrument" explicit). "count once" is attached only to the HYG clause. Residual: "HY OAS >350" with ">" vs matrix M-01 "HY ≥350" is a boundary difference (owner's REG-T-04 vs NEXUS letter) - only the first is stated here. "5Y CDS ≥350" has no unit (bp implied).

## 3. INTERNAL CONTRADICTIONS
- No root ID is orphaned: R7 and R10 stay live (L40-41); R2/R9/R3/R4/R1 live. Matrix roots R1,R3,R4,R7,R8,R10,R2/R9 all resolvable. R8 (M-10) and R5 (M-06 "R2 row"? M-06 cites R2/R9 only) fine. Context roots named in L30 ("R2/R9/R10/R11/R12 are context roots") - R11/R12 state only in cold file, reachable via L39 pointer; no matrix row cites them.
- L30 lists R10 as a context root, but the live R10 row (L41) and M-05/M-11 weigh it with evidence; L30 also lists R5/R6 nowhere (they are in pointer row). Minor.
- Resolver dates in pointer vs docket: no contradiction found (see s1).
- Orphan phrase: L39 pointer says WATT "P1 5 -> 3 [10/22]" and R5 "Brent -> CPI only if sustained" - copies of cold content, fine. Rhine "FIRED" in L81 with no date while L65-66 etc. don't cite it.
- Duplication: "count once" HY series appears in L7, L9, L73, L90 - consistent.
- Trading line L9 names "REG-T-04 (HY OAS >350 ×3)"; L49 says "REG-T-04 (HY >350) run 0 of 3" consistent.

## 4. COLD-READER MISREADS
1. L3 "Delta annotation 1 of 2" - no "2 of 2" exists on the board.
2. L81 "LIQ-069 FIRED (not RELEASED)" vs M-09 "LIQ-069 2-of-2" - the hot row dropped "2-of-2"; stranger can't tell what fired.
3. L81 "Rhine FIRED" / "BOND one-shot MET" - no date, no desk, no resolver in hot row.
4. L39 "Plenum ... + 11/10 clocks (R11)" - which clocks undefined on board.
5. L5 "neither can fire before 10/27" vs L7 "Earliest UP fire = cell 5 (obs Mon 10/26, read Tue 10/27)": consistent, but "one cell into opposite-signed runs" jargon.
6. L9 "reviewer via Will" - unnamed reviewer.
7. L98 "CYPHER 9 of 9 rows NOT-FIRED (new desk; 15/40 ...)" undefined scores.
8. L95 "the 8 lines above" - table L86-93 is 8 rows but rule text counts lines "above" across two tables.

## 5. BROKEN POINTERS
Tested 8 backticked repo paths: BRIEFS_MAP.md, CONFIRMED.md, PREDICTIONS_MONITOR.md, STATUS_COLD.md, analysis/WQ342_grading_log.tsv, research/2026-10-23_full_pass/RECORD.md, research/2026-10-23_full_pass/ (relative to AGENTS/NEXUS/), FORGE/STATUS.md (relative to repo root). All exist. Also STATUS_COLD §H16 (L1435) and §H21 (L1692) exist. Missing: none.

## 6. VERDICT
❌ 0 - nothing found that would mislead a reader acting on it.
⚠️ 6:
 1. Header "Delta annotation 1 of 2" with no annotation 2 - fix: state "no annotation 2 this pass" or drop "of 2".
 2. Other-owner-states pointer row carries no dates/resolvers (Rhine, FLG, BOND) - fix: keep the as-of dates in the hot row.
 3. LIQ-069 "FIRED" lost its "2-of-2" qualifier in the hot row - fix: restore.
 4. R11 "11/10 clocks" and CORAL MSI 10/29, Sept TIC have no docket row - fix: docket row or "no wake registered".
 5. "5Y CDS ≥350" lacks unit; HYG ">350" vs M-01 "≥350" boundary differs unflagged - fix: add "bp" and note owner's strict ">".
 6. "reviewer via Will" unnamed - fix: name the reviewer or cite the packet.
