# fred_pull `--start` bug — blast-radius sweep: EMPTY (2026-07-16 ~10:15 PM ET, PROME, Will-approved)

**The bug (fixed `fef252d9`, DEWEY 7/16):** `fetch()` applied `limit=10` even with `start=`; since `start` flips sort to ascending, any date-ranged pull returned the **ten OLDEST rows of the range, silently, with plausible dates**. Fabrication-adjacent class. DEWEY's 7/16 reports flagged: "any prior date-ranged FRED citation by any agent is suspect — PROME's call whether a sweep is warranted." Will approved the sweep 7/16 PM.

## Scope
`fred_pull.py` lives in `AGENTS/DEWEY/scripts/` and greps show **no consumer outside DEWEY** (worktree copies excluded). Pre-fix DEWEY reports ranked by FRED-history claim density → 5 candidates. Corruption signature to hunt: range-aggregate stats (records, percentiles, "since 20XX") or "current" values sourced from a `--start` pull; latest-value reads (default path) and fredgraph pulls are unaffected by construction.

## Per-report verdicts

| Report | Verdict | Basis |
|---|---|---|
| **2026-07-02 HY/CCC widening decomposition** (fed Gate A context) | ✅ **CLEAN — every load-bearing figure reproduced exactly** with the fixed puller | Gap 8.06 [6/30] ✓ · window-max 8.31 [2025-04-07] ✓ · "3 prior days ≥8.06 (2024×1, 2025×2)" ✓ EXACT under ≥ semantics (2024-08-05 = 8.06 tie — the Aug-2024 carry-unwind day; 2025-04-07 8.31, 2025-04-08 8.10; the word "exceeded" was loose for the tie, count and year-split correct) · CCC/BB record 6.07× [6/22] ✓ + Apr-2025 3.72× ✓ + top-8-all-current-episode ✓ (with data ≤7/1: 7 June days + 7/1 itself) · CCC/HY 3.57× [6/17 + 6/22] ✓ (3.570/3.574) · HY 283/280/275/274 [6/26→7/1] ✓ all four · Feb–May >280 on 70/87 days, peak 346 [3/30] ✓ · CCC 9.70→9.68, BB 163 ✓. Full-window rankings could NOT have come from a corrupted 10-row pull — the report demonstrably ran on complete data (its own sourcing line: `fred_pull.py` **+ fredgraph**). |
| **2026-07-09 funding-seizure X1 gate** (fed the X1 redefinition) | ✅ CLEAN — wrong claim-class for the bug | Its FRED table is **latest published values only** (SOFR/IORB/SOFR99/EFFR/RRP/TOTRESNS; SOFR99 is FRED's own daily-percentile *series*, not a computed range stat). Spot-check exact: SOFR 3.58 / IORB 3.65 = −7bp [7/8] ✓. Its +25/+50bp thresholds are self-declared "illustrative, not calibrated" — the calibration was 07b's job, which is where the bug was caught live. |
| 2026-06-27 housing-distress inflection | ✅ CLEAN — no FRED-derived stats | "Highest since 2020/2009/2018" claims are ATTOM / ICE loan-level / NMN sourced; zero FRED citations in the file. |
| 2026-06-27 muni-fiscal stress | ✅ CLEAN | Zero FRED citations. |
| 2026-06-26 FL property-tax amendment | ✅ CLEAN | Zero FRED citations. |

## Verdict
**Blast radius EMPTY. No prior report carries a bug-corrupted figure; nothing to correct or propagate.** The bug's only real-world victim was the 7/16 07b calibration run itself, which hit it building the SOFR99−IORB percentile series, caught it, worked around it (`all_data=True`), and fixed it same-session. The standing "any prior date-ranged FRED citation is suspect" flag in DEWEY's 7/16 reports is **CLOSED** by this sweep (note → DEWEY inbox).

*Method note: verification ran through the FIXED `fred_pull.fetch(start=)` path itself (787 rows/series, 2023-07-17→2026-07-15, truncation warnings firing correctly) — so this sweep double-served as a live regression test of the fix. Script: scratchpad (session-local); figures above are the durable record.*
