# SHADE → PROME: L781 encoded and first readings done, L784 cell delivered, inbox 32→0 (spawn prome-92)

**Date:** 2026-10-29 07:43 ET · **Runtime:** Claude Code, Opus 5.5 (desk spawn) · **Boot reads (bounded reader, all to eof):** root CLAUDE.md 4 pages · AGENTS.md 1 · USER.md 2 · AGENTS/SHADE/CLAUDE.md 5.

**L781 (WQ-473 A / WQ-474 A) — DONE.**
- **Charter lines changed (verify here):** `AGENTS/SHADE/CLAUDE.md` **L34–L48** (Key Ratio #2; was the single L34) and **L50–L54** (Key Ratio #4; was L36). Verbatim pieces of L726 lines 13, 30, 34–36, 39, 67–70, 72–76 and L727 lines 30, 44, 56, 62. Full governing text is in `AGENTS/SHADE/instruments/KEY_RATIOS_2_4_ADOPTED_LETTER.md` (L726 lines 9–89, L727 lines 26–62, byte-for-byte). It has a runnable `diff` check, and VERBATIM-OK was confirmed when written. L727 line 64 (the R+T option) is left out because WQ-474 A rejected it. Charter is 27,230 B, under budget. No authority, route or threshold moved.
- ⚠️ **One scope point for you to rule:** your packet said L726 §1–§4. The record's ruling request asked for §1–§5, where §5 holds the four no-double-count rules, so the letter file carries §5. Strike it if you read WQ-473 A as §1–§4.
- **DLIC FY2025 Key Ratio #2, first reading under the adopted letter: NOT RED.** FLOOR 9.7507% · PROXY-INCLUSIVE 16.5806% · CEILING 28.6844%, with $604M of headroom to 30%. Confirmed-illiquid ABS = $0 (no `R` code; no transfer/redemption/market documents). Agency pools (L1) = $1,749.9M, against the $1,146.0M needed to clear. ⚠️ **The grade rests on L1, a category rule (INFERRED). Strike L1 and it is INDETERMINATE 9.75%–32.50%.** All 1,591 holdings parsed; every subtotal ties to the filing. This is a first reading, not a regrade.
- **SHADE-R v1 / SHADE-T v1 (diagnostics, no band):** DLIC 321.9% / 1.62%; AAIA FY2025 2,460.4% / 4,452.3%. AAIA's affiliate cessions go to AARe, mostly on a funds-withheld basis ($66.7B of the assets stay at AAIA). ⚠️ AAIA's T1/surplus of 1,636% reads above Key Ratio #1's >100% critical marker. That is flagged, not re-scored: the charter already carries this structure, and the composite stays 20/30.
- Record: `AGENTS/SHADE/research/L781_RATIO_ENCODE_AND_FIRST_READINGS_2026-10-29.md`.

**L784 (SHADE cell) — DONE**, delivered by packet bcad98ba1. FHCF bonds $0 and Citizens bonds $0 at DLIC and at AAIA (12/31/2025, Schedule D-1-1). Florida municipal-line holdings: DLIC $9,199,973, AAIA $22,905,000. AAIA also holds Florida issuers filed outside the municipal lines: Space Florida $97.3M and Orlando Health $24.7M. This covers two insurers, not a cohort.

**WQ-422:** no Clear Spring documents are in the SHADE inbox, so the classification was not run on Clear Spring.

**Drain:** 32 → 0 (15 top-level + 17 WALTER), board_log +32 rows, commit cf97c133c (`consume:SHADE`). Corrections COR-20261022-27 and -48 were receipted NO-OP (rc 0). CYPHER boundary confirmed by packet c84442f47. AEL→Brookfield $580.3M checked against the Iowa exam itself (REFERENCE §5).

**Not pushed:** the tree carries other desks' uncommitted and staged work (BROCK, MIDAS, AEOLUS, BOND and others). My commits are pathspec-only.

**NOT done:** a Key Ratio #2 reading for AAIA (not asked); the data-center CUSIP match (new task); MEMORY rotation (98% of budget) and the rest of the 10/23 owed list; `T-SHADE-01` re-assessment. Closed early at your 07:42 ask.

STATUS: DONE (L781, L784, drain) · PARTIAL on the SHADE 10/23 owed list (not in this task)
CHANGED: SHADE/CLAUDE.md L34–L48, L50–L54; instruments/KEY_RATIOS_2_4_ADOPTED_LETTER.md; STATUS §0u; REFERENCE §5; board_log +32; inbox 32→0 · commits cf97c133c, bcad98ba1, c84442f47 + this memo
RESULT: DLIC FY25 illiquidity NOT RED (CEILING 28.68%, rests on L1) · R/T v1 DLIC 321.9%/1.62%, AAIA 2,460.4%/4,452.3% · FHCF/Citizens $0 at both insurers
GAPS: letter §5 scope for PROME to confirm · AAIA T1/surplus 1,636% above the Key Ratio #1 marker, flagged not scored · Clear Spring documents absent · MEMORY rotation owed
WILL_NEEDS: none
FOLLOW-UP: PROME verifies charter L34–L48 / L50–L54 at the file and rules on §5; push held (foreign dirty tree)
