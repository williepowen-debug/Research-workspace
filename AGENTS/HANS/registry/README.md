# HANS threshold registry

**Created 2026-08-28**, answering WALTER's question of the same day: *are the UK gilt bands REGISTERED thresholds with a fire-ledger, or informal watch levels?*

**The honest answer at the time it was asked: INFORMAL — and not just the UK bands. This desk had ZERO registries and ZERO fire-ledgers.** Every threshold HANS carried lived as prose in `STATUS.md` and `CLAUDE.md`. `HANS-T-05` (Bund >3.00) had **already fired at 3.29% that same session** with nothing on disk recording it.

⚠️ **The sharp part, recorded because it is the useful part:** in the same session that created these bands, HANS **retired a dormant Belgium threshold** (`COMPLETED_RP-HANS-1.txt:70`) for having no metric surface, wrote `[[finding_banded_threshold_with_no_metric_surface_is_untrippable]]` into `thesis/KILL_TREE.md` — **and then registered six new bands with no metric surface, in prose, in the same file.** Diagnosing a defect class does not immunise you against it. This registry is the fix.

## Files
| File | Purpose |
|---|---|
| `THRESHOLDS.tsv` | **14 rows.** The registry. Bands are HANS-owned and revisable — but a band change is an edit that must be logged in the row's `notes` with a date, never a silent overwrite. |
| `HANS_T_FIRED_LOG.tsv` | **The SINGLE record of fires.** Modelled on `AGENTS/CREED/registry/CREED_T_FIRED_LOG.tsv`. Other desks may read it freely; **never mirror it** — key stale-fire suppression to this file. |

## ⚠️ Read this before scanning — a clean scan of the scannable rows does NOT mean the board is clear

Following CREED's hard-won lesson (WALTER `CLAUDE.md` 6b): **only 6 of the 14 rows are numerically scannable on a daily pull.**

| Class | Rows | Why it cannot be auto-graded |
|---|---|---|
| **SCANNABLE-DAILY (6)** | `T-05` Bund · `T-06` gilt 10Y · **`T-13` gilt 30Y** · `T-07` TTF · `T-08` storage gap · `T-11` EURUSD | — (these are the auto-gradable set) |
| **MONTHLY-PRINT (3)** | `T-01`, `T-02` German Mfg PMI · `T-03` Composite | Monthly survey prints, **not live levels**. Surface as *"last known print + its date."* |
| **EVENT-DRIVEN (1)** | `T-04` ECB deposit rate |
| **🟡 QUALITATIVE-EVENT (1)** | **`T-14`** EU bank/private-credit distress | Scannable only on the 8 scheduled GovC dates plus any emergency meeting. |
| **COMPOUND-TWO-LEG (2)** | `T-09` Italy · `T-10` France | Both a spread leg **and** an absolute-level leg are required. Neither leg alone fires. |
| **🔴 UNINSTRUMENTED (1)** | `T-12` EUR/USD 3M basis | **No feed, no pull, no owner-instrument. It CANNOT fire however far the basis moves.** Last value is 2026-02-13. Registered so the gap is *countable*, not because it works. **Do not count it toward a clean board.** |

**So: 6 auto-gradable, 7 that need a human or a calendar, and 1 that is broken and says so.**

⚠️ **`T-14` and `T-12` look alike and are NOT the same class. Keep them apart.** `T-12` is **UNINSTRUMENTED** — no feed exists, so it cannot fire however far the basis moves. `T-14` **has a live feed** (WALTER news routing + ECB/ESRB publications); it is merely **not numeric**. *A qualitative row with a feed is trippable. An unfed numeric band is not.* Collapsing them into one "can't auto-scan" bucket would quietly convert a working trigger into a dead one.

## Registry → metric-surface map (the check, run on itself 2026-08-28)

**Standing check adopted this session: every registry row must name a metric surface.** Run against `workbook/VX.tsv` on adoption it **failed on 8 of 12 rows** — the vectors existed but the mapping was not written down, which is the same class of defect as having no vector at all: *nobody can verify coverage they cannot see.* Mapping recorded here, at the registry, rather than annotated across 8 VX rows.

| Registry row | Metric surface (`workbook/VX.tsv`) | Note |
|---|---|---|
| `HANS-T-01` / `T-02` | `VX-HANS-8.06` German Manufacturing PMI | ⚠️ `VX-HANS-10.02` **duplicates** 8.06 — update both or neither |
| `HANS-T-03` | *(none — German Composite PMI has no vector)* | 🔴 **GAP.** Tracked in `STATUS.md` only |
| `HANS-T-04` | `VX-HANS-4.01` ECB Deposit Rate | — |
| `HANS-T-05` | **`VX-HANS-3.05` Bund yield (LEVEL)** | Created 8/28 — the row was FIRED with no surface |
| `HANS-T-06` | **`VX-HANS-3.06` UK gilt (LEVEL)** | Created 8/28 with the UK leg |
| `HANS-T-07` | `VX-HANS-8.01` TTF | ⚠️ `VX-HANS-11.02` is a **third surface** on the same number |
| `HANS-T-08` | **`VX-HANS-8.07` storage GAP** | Created 8/28. `8.02` is the *absolute fill* — **paired, not duplicate** |
| `HANS-T-09` | `VX-HANS-3.01` spread + *(no BTP level vector)* | 🔴 **HALF-COVERED** — compound row, level leg unsurfaced |
| `HANS-T-10` | `VX-HANS-3.02` spread + **`VX-HANS-3.07` OAT level** | Both legs surfaced 8/28 |
| `HANS-T-11` | `VX-HANS-2.01` EUR/USD | — |
| `HANS-T-12` | `VX-HANS-2.04` (last value **2026-02-13**) | 🔴 Vector exists but is **197 days stale** — this is *why* T-12 is UNINSTRUMENTED |

**⇒ Three gaps remain and are named rather than closed: `T-03` (no vector), `T-09` (level leg unsurfaced), `T-12` (vector dead).** They are listed so the gaps are countable. **A registry row without a live surface is untrippable however correct its band** `[[finding_banded_threshold_with_no_metric_surface_is_untrippable]]`.

## Standing caveats
- **`T-07` TTF is a FRONT-MONTH contract and it ROLLS.** A delta across a roll is not a price move `[[finding_continuous_front_ticker_rolls_so_deltas_lie]]`.
- **`T-08` measures the GAP to the 5-year norm, not the absolute fill.** Absolute fill rises all summer and reads reassuring while the gap widens — that is exactly what happened Jul→Aug 2026.
- **`T-09`/`T-10` are compound BY DESIGN.** Their spread legs alone read "all clear" through a +33bp common-mode Bund move to a 15-year high. Do not simplify them back to one number.
- **`T-06` UK gilt: WALTER's limit binds — BOND takes anything TIME-CRITICAL on this row.** HANS is Tier 2 and was 43 days dark at the time the leg was assigned.

## Counting fires — the rule, bought 2026-08-28

**FOUR fires are OPEN across four thresholds: `T-05`, `T-07`, `T-08`, `T-02`.** (Five ledger entries; `F-002` is SUPERSEDED by `F-003`.)

⚠️ **A caveat about a band's evidentiary WEIGHT is NOT a decision about whether its fire COUNTS. Never let one become the other.** On the day this registry was built its author said "three bands are currently fired" while the ledger recorded four — **`T-02` was silently dropped from the count because it carried a down-weighting caveat** (its band was written 8/28, after the condition was satisfied 8/21). The caveat was correct and it is still attached. The exclusion was not: the metric genuinely crossed a registered band, and the weakness lives in the band's *predictive claim*, not in the *fact of the crossing*. Caught by WALTER counting the file instead of taking the number — `[[finding_ledger_drift_behind_narrative]]`.

**⇒ Two independent axes. Record both, never merge them:** *did it fire?* (binary, goes in the count) and *how much does this band's fire tell us?* (judgement, goes in the notes). **A quarantine flag must never be able to suppress a fire.**

## Backdated fires
`HANS_T_FIRED_LOG.tsv` opens with **five entries, four of them backdated or retrospective**, because the levels were reached before the ledger existed — two of them while the desk was dark. They are logged as fires with the backdating stated in each row. **Starting the ledger clean today would have made the board look quiet on the day it was loudest.**
