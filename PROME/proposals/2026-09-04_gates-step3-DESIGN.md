# GATES.tsv STEP 3 — a DESIGN to Will (DOCKET L256; WQ-176) · PROME 2026-09-04 ~09:3x ET

**Status:** DESIGN, not an edit. Nothing in `PROME/GATES.tsv` changes until Will's word AND per-row owner confirms. Measurement = `PROME/tools/measure.py` + a column census of the 20 live rows (this session).

## Where the file is
| Measure | Value |
|---|---|
| File | **51,474 B = 158% of the 32,550 B READ_CAP budget**; 13 header comment lines = **7,380 B**; 20 data rows = 43,722 B (mean 2,186 B) |
| `condition` | **15,237 B — 18 of 20 cells >400 B** (LIQ-069 1,910 · HY-REKILL 1,627 · LIQ-079 1,236 · LIQ-076 1,035 · LIQ-072 1,023 · CORAL-MSI-01 1,002 · FALCON-001 844 · REG-T02 709 · …) — whole owner letters, contra the ENVELOPE rule "summary + pointer only" |
| `consequence_on_fire` | 5,783 B — 3 cells >400 B (LIQ-079 864 · HY-REKILL 833 · FLG-T08 829) |
| `last_checked` | 5,767 B — 6 cells >400 B (CORAL-MSI-01 732 · OSPREY-001 692 · REG-T02 571 · FERT-G3 524 · FALCON-001 464 · HY-REKILL 431); `state` cells already ≤227 B after 9/3 |
| `source` / `review_by` | one cell each >400 B (FALCON-001 617 · TERRY-007 593) |

Step 2 (9/3) archived 14 terminal rows and rotated prior-chains; the file still sits 19 KB over budget because the mass is in the LIVE rows' letters, not in history.

## The design — three legs, byte-targeted
| Leg | Rule | Saves (est.) |
|---|---|---|
| **① `condition` → ≤400 B summary + `definition_surface` pointer** | every cell >400 B is cut to the fire test in one sentence + its unit/vintage/operator + `→ <owner letter path>`; the full letter is archived VERBATIM to `PROME/archive/GATES_CONDITION_LETTERS_2026-09-XX.md` with a per-row entry-crc32, and the row's `definition_surface` names the owner's canonical letter (the owner's file, never the archive, is the grading surface). **Owner CONFIRM per row before the cut** (LIQUID ×4 · CORAL · FLG · FALCON · REGINALD · FERT · TERRY · BRENT · BROCK · NEXUS · OSPREY — one packet each, reply = the ≤400 B summary in the owner's own words or "cut as PROME drafted"). **HY-REKILL exempt** (WQ-162: the self-grading letter lives in the cell by ruling until LIQUID folds it into its KB). | ~8,500 B |
| **② `consequence_on_fire` + `last_checked` + `source` + `review_by` ≤400 B** (state-class cells ≤220 B, already met) | consequence >400 B → the ACTION line + pointer (LIQ-079 · FLG-T08; HY-REKILL exempt as above); `last_checked` keeps ONLY the latest dated read (prior reads → `GATES_STATE_HISTORY`, which already exists for this purpose); `source`/`review_by` trimmed to path + date + one clause. No owner confirm needed — these are PROME's envelope cells. | ~3,000 B |
| **③ Header comments → `PROME/GATES_README.md`** | the 13 comment lines (7,380 B: citation convention, vocabulary, archive stamps, step-2 record) move VERBATIM to a README the file's first line points at; the TSV keeps ONE comment line (owner · vocabulary pointer · README pointer · archive stamps). Rationale: `prome_gate` and every reader parse the rows, not the prose; the prose is boot-read by nobody but costs every PROME whole-read. | ~6,700 B |

**Byte target:** 51,474 → **≈33,000 B after ①+② (≈101%)** → **≈26,300 B after ③ (≈81%)**, under the 100% line and with a 6,000 B registration headroom before the 100% re-breach; the ≥75% rotate trigger would still read hot, so **the standing rule "every NEW registration pairs with a same-commit compaction" stays in force until a step 4** (per-row `state` → GATES_STATE_HISTORY on every touch, mechanized in the apply script) brings it under 70%.

## Order + safeguards
1. **Will's word on ①②③** (this row). 2. **③ first** (PROME-only, no owner dependency; a cold read of the README + the one-line header; committed same-commit with the move — `finding_liveness_gate_keyed_on_an_artifact_that_must_exist_first`). 3. **②** in one commit under a pre-edit blind read of the diff. 4. **①** row by row as confirms land (LIQUID's four rows in one packet; a row whose owner is dark >7d gets PROME's draft summary with `⚠️ PROME-drafted, owner confirm owed` in the cell — never silently). 5. Post-edit blind read to ❌ = 0 (WQ-165 stop). 6. Gate meter re-stamped in the header; DOCKET L256 → RESOLVED with the final `measure.py` receipt.

**What this does NOT do:** no threshold moves; no state token changes; no row deleted; letters lost nowhere (owner file + verbatim archive with crc); `fleet_dashboard` gate-tile parsing keys on `gate_id`/`state`/`review_by` and is unaffected (tested at step 2).
