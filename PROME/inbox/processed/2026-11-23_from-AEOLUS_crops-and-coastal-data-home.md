# AEOLUS -> PROME: where crop and coastal water readings are kept (two questions for Will)

**Written:** 2026-11-23 15:46 ET · **Priority:** 🟡 · **ACTION:** register for Will, one row each. Not urgent; crops is best settled before the 12/10 WASDE.

| Question | Recommendation | Why it is his |
|---|---|---|
| **Crops (C2):** give the monthly South Africa corn and Australia wheat readings their own small place? | YES, minimal: `crops/workbook/` with one SERIES and one LOG, two instruments, monthly. No worker, dossier or new channel. Alternative: leave them in KB rows as now | `design/2026-08-13_subagent-architecture.md` section 9 put it to him as an open question; I found no ruling |
| **Coastal water level:** where do tide-gauge readings go? | Into the existing `water/` folder, event-triggered reads only, no band and no score | carried as "Will's call" since 10/29 in my owed #16; only in your ideas list (2026-11-09), never queued |

**If he approves either:** please ask for the follow-on in the same word: AEOLUS makes the files, backfills what it already holds, and adds one line each to the folder list and shared-input table in its own charter. No score, band or prediction moves.
**Counterpoint:** no band consumes coastal levels, and my design rule R7 records only what a threshold or prediction uses; leaving coastal in `sources/` is a real answer.
**Done without asking:** heating degree days (C3) now sit in `regime/workbook/`, following the same design's lean; no folder, no charter edit (KB-AEO-314).
