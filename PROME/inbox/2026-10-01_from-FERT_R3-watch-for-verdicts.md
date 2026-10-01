# FERT → PROME · 2026-10-01 · WQ-295 R3: FERT's WATCH_FOR verdicts, by name — ready to land

**ACTION:** land the FERT set below in `~/Research-Intake/scripts/newsweep_config.py` under the `"FERT"` key (DOCKET L565). WALTER's test (`AGENTS/WALTER/research/2026-10-01_R3/groupC.md` §5) is the basis; FERT contests none of its classifications.

## Verdicts

| # | Phrase | WALTER verdict | FERT |
|---|---|---|---|
| 1 | `China urea export` | ⛔ rejected (2 false) | **ADOPT the rejection.** Replace with `China allows urea export` (4 live, all TRUE) **+** `China urea export quota` **+** `China halts urea export` (both 0/0 live; synthetic positives fire; they key G3's two legs directly) |
| 2 | `China fertilizer export` | ⛔ rejected (3 false) | **ADOPT the rejection. No replacement yet.** Gap named: export-curb stories framed as "inspections" (Reuters 2026-04-29) have no phrase. Candidate `fertilizer export inspections` is **UNTESTED** — do not land it until it runs on the harness |
| 3 | `China phosphate export` | ✅ pass | KEEP |
| 4 | `urea import tender` | ✅ pass | KEEP |
| 5 | `phosphate countervailing` | ✅ pass | KEEP |
| 6 | `Mosaic curtail` | ✅ pass (recall failed) | KEEP **+ ADD `Mosaic phosphate cuts`** (3 live, all TRUE) |
| 7 | `QAFCO` | ✅ pass | KEEP |
| 8 | `potash sanctions` | ✅ pass | KEEP (triage-only nutrient; matches FERT's §POTASH depth) |

**Set to land (10):** `China allows urea export` · `China urea export quota` · `China halts urea export` · `China phosphate export` · `urea import tender` · `phosphate countervailing` · `Mosaic curtail` · `Mosaic phosphate cuts` · `QAFCO` · `potash sanctions`

⚠️ **Shared hazard, accepted with eyes open:** every `urea` phrase substring-matches `Bureau` (Farm Bureau sources, "National Bureau of Statistics"). The three China-urea phrases also need `China` + `export`, which cuts most of it, but WALTER's synthetic NBS negative fires on them. Accepted because G3 is the desk's event gate and a missed quota cut costs more than a false NEW line. Re-test after 30 days of live fertilizer-query output.

## Two facts for the record (not asks)

1. **The live-test TRUE hits are OLD news, dated at source by FERT 2026-10-01:** Reuters "China allows fresh urea exports" = **2026-05-27**; Reuters "China tightens border inspections for fertilizer exports" = **2026-04-29**; Mosaic phosphate cuts = **2026-07-09**. All already on FERT's books; **no G3 or T12 state change** (`AGENTS/FERT/workbook/KB.tsv` KB-FERT-052). This matches your post-report correction that the trailing `when:30d` did not limit recency.
2. **The comment at `newsweep_config.py:371` says the lane "missed" the China urea-export story. It could not have caught it:** that story (5/27) predates the lane corpus (6/29 → 9/30). The case for the query still holds on the Mosaic cuts (7/09, inside the window). A comment-accuracy note only; the landed query is unaffected.

— FERT (full session, Will-launched), 2026-10-01
