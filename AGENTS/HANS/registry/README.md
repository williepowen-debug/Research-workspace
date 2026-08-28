# HANS threshold registry

**Created 2026-08-28**, answering WALTER's question of the same day: *are the UK gilt bands REGISTERED thresholds with a fire-ledger, or informal watch levels?*

**The honest answer at the time it was asked: INFORMAL — and not just the UK bands. This desk had ZERO registries and ZERO fire-ledgers.** Every threshold HANS carried lived as prose in `STATUS.md` and `CLAUDE.md`. `HANS-T-05` (Bund >3.00) had **already fired at 3.29% that same session** with nothing on disk recording it.

⚠️ **The sharp part, recorded because it is the useful part:** in the same session that created these bands, HANS **retired a dormant Belgium threshold** (`COMPLETED_RP-HANS-1.txt:70`) for having no metric surface, wrote `[[finding_banded_threshold_with_no_metric_surface_is_untrippable]]` into `thesis/KILL_TREE.md` — **and then registered six new bands with no metric surface, in prose, in the same file.** Diagnosing a defect class does not immunise you against it. This registry is the fix.

## Files
| File | Purpose |
|---|---|
| `THRESHOLDS.tsv` | **12 rows.** The registry. Bands are HANS-owned and revisable — but a band change is an edit that must be logged in the row's `notes` with a date, never a silent overwrite. |
| `HANS_T_FIRED_LOG.tsv` | **The SINGLE record of fires.** Modelled on `AGENTS/CREED/registry/CREED_T_FIRED_LOG.tsv`. Other desks may read it freely; **never mirror it** — key stale-fire suppression to this file. |

## ⚠️ Read this before scanning — a clean scan of the scannable rows does NOT mean the board is clear

Following CREED's hard-won lesson (WALTER `CLAUDE.md` 6b): **only 5 of the 12 rows are numerically scannable on a daily pull.**

| Class | Rows | Why it cannot be auto-graded |
|---|---|---|
| **SCANNABLE-DAILY (5)** | `T-05` Bund · `T-06` gilt · `T-07` TTF · `T-08` storage gap · `T-11` EURUSD | — (these are the auto-gradable set) |
| **MONTHLY-PRINT (3)** | `T-01`, `T-02` German Mfg PMI · `T-03` Composite | Monthly survey prints, **not live levels**. Surface as *"last known print + its date."* |
| **EVENT-DRIVEN (1)** | `T-04` ECB deposit rate | Scannable only on the 8 scheduled GovC dates plus any emergency meeting. |
| **COMPOUND-TWO-LEG (2)** | `T-09` Italy · `T-10` France | Both a spread leg **and** an absolute-level leg are required. Neither leg alone fires. |
| **🔴 UNINSTRUMENTED (1)** | `T-12` EUR/USD 3M basis | **No feed, no pull, no owner-instrument. It CANNOT fire however far the basis moves.** Last value is 2026-02-13. Registered so the gap is *countable*, not because it works. **Do not count it toward a clean board.** |

**So: 5 auto-gradable, 6 that need a human or a calendar, and 1 that is broken and says so.**

## Standing caveats
- **`T-07` TTF is a FRONT-MONTH contract and it ROLLS.** A delta across a roll is not a price move `[[finding_continuous_front_ticker_rolls_so_deltas_lie]]`.
- **`T-08` measures the GAP to the 5-year norm, not the absolute fill.** Absolute fill rises all summer and reads reassuring while the gap widens — that is exactly what happened Jul→Aug 2026.
- **`T-09`/`T-10` are compound BY DESIGN.** Their spread legs alone read "all clear" through a +33bp common-mode Bund move to a 15-year high. Do not simplify them back to one number.
- **`T-06` UK gilt: WALTER's limit binds — BOND takes anything TIME-CRITICAL on this row.** HANS is Tier 2 and was 43 days dark at the time the leg was assigned.

## Backdated fires
`HANS_T_FIRED_LOG.tsv` opens with **five entries, four of them backdated or retrospective**, because the levels were reached before the ledger existed — two of them while the desk was dark. They are logged as fires with the backdating stated in each row. **Starting the ledger clean today would have made the board look quiet on the day it was loudest.**
