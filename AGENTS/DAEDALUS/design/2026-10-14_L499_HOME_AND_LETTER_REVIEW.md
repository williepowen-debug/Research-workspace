# L499 — WQ-298 standing rule: canon home + letter review (DAEDALUS's leg)

**Written:** 2026-10-14 20:46 ET · **Row:** `PROME/DOCKET.tsv` L499 (owner split: DAEDALUS names the home + reviews the letter · PROME records, runs the blind plan read in the record, makes ONE insertion · one result read) · **Ruling:** `PROME/proposals/2026-09-25_wq297-298-RULED.md` §WQ-298 ③ + the draft clause under "Draft canon clause". Nothing inserted by this note.

## 1. Home — named
| Where | What | Why |
|---|---|---|
| **`FORGE/PREDICTION_DISCIPLINE.md` — ONE new bullet, beside the WQ-288 bullet (:37)** | the clause itself | It is a GRADING procedure (what the owner writes at the grade when a leg's instrument is unreachable). The fleet's ruled grading rules live there (WQ-112 :36, WQ-288 :37, WQ-161 :43) and that is the surface a desk reads at grade time |
| `AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md` **Class 2** `CANNOT-FIRE` row | a pointer only, no restatement (PAT-006) | The token's definition already covers it ("evaluated and found UNGRADEABLE: at least one leg has no metric surface / no producer"). ⚠️ The DOCKET row says "Class 7 cross-ref"; `CANNOT-FIRE` is **Class 2** (gate states). Class 7 is the registry envelope's `scannable` cell and is not the right home. DAEDALUS adds the pointer in its own file after PROME's insertion lands |

Neighbour check (MEMORY MODEL rule: scan the destination for rules that appear to say the opposite): WQ-288 (:37) resolves a row whose Invalidation names no series as NO-VERDICT, and has the owner name the series prospectively. The new clause's "reachable substitute registered prospectively" uses the same prospective-naming discipline, so the two compose. A leg left `CANNOT-FIRE` is not a resolved row, so WQ-112's scoring vintage is untouched. Class 2 `UNOBSERVABLE` (the world may never emit it) stays distinct: an unreachable instrument is "we cannot measure", which is `CANNOT-FIRE`.

## 2. Letter review of the draft clause
> *A registered leg whose named instrument is unreachable from the fleet's boxes is marked `CANNOT-FIRE` at the grade and its instrument is filed once on the paid-data list (`PROME/…`, WQ-298); the owner does not re-argue access at the next grade. An instrument is either bought (Will's pass) or the leg stays `CANNOT-FIRE` until a reachable substitute is registered prospectively.*

| # | Finding | Proposed change |
|---|---|---|
| 1 | **"Unreachable" has no test.** One 403 is a fact about one host (`STATE_VOCABULARY` Class 6, `finding_blocked_mirror_is_not_an_unreachable_primary`). Without a test, the fail-closed rule makes `CANNOT-FIRE` the cheapest grade on any bad day | After "unreachable from the fleet's boxes", insert: "— after the Class 6 reachability check (the publisher's API and listed alternates tried, and each attempt named) —" |
| 2 | **The list path is a placeholder.** `PROME/…` cannot be cited. L498 RESOLVED into a ruling record (WQ-300, 9/26: paid lines declined), and a ruling record is not an appendable list | PROME names an appendable home (e.g. a registry TSV: instrument · desk · leg/gate · date filed · Will's pass) **before** insertion, and the clause cites that path. PROME's call, not mine |
| 3 | "Will's pass" | Keep. It is the ruled one-pass review (WQ-298 ②); WQ-300 shows the pass ran once and declined, so the default branch is the live one |
| 4 | Per-leg vs per-gate | Already per-leg ("a registered leg"), which matches Class 2's weakest-leg rule. No change |

**Verdict:** ACCEPT the clause with changes 1 and 2. Change 2 gates the insertion; change 1 is wording. Next: PROME's blind plan read in the record, then one insertion at `FORGE/PREDICTION_DISCIPLINE.md`, then one result read; DAEDALUS adds the Class 2 pointer.
