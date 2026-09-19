# HEARTBEAT dashboard projections

Derived display text, not independent authority. Source: `../HEARTBEAT.md`.
Each amendment requires exactly one numbered projection. Review all affected
one/channel/ticker fields when changing source prose; refresh source_sha256 over
the exact > AMENDMENT paragraph without its trailing newline. Later amendments
win. Missing, malformed or stale projections withhold the dashboard summary and
levels. Hash agreement proves synchronization, not semantic completeness.
At a HEARTBEAT re-base, remove projections for amendments folded into the base.
This companion keeps render metadata outside the boot-read byte budget.

*⛔ **PRIOR (SUPERSEDED 2026-09-19 13:2x by amendment #1 — see the paragraph above; this one's "nothing is projected" instruction is DEAD).** Nineteenth base 2026-09-19 (Sat, markets closed) at its writing: **chain 0 — no amendments.** The eighteenth base's Amendment #1 (BOJ +25bp 7–2 · first clean SOFR/IORB pair −5bp · 9/17 credit cells flat), Amendment #2 (SAM's L34 grade + the dovish-dissent CORRECTION to #1 · RED's FT-10 grade 0-of-4) and Amendment #3 (HENRY L411 post-opex board · VIOLET L277 leg 3 · the 9/17 H.15 cells · the 9/18 closes · the stale-bar guard) were FOLDED INTO THE BASE at the ~11:2x ET re-base and **their projections are REMOVED here per this file's own rule**; the amendment blocks themselves are rotated verbatim to `PROME/HEARTBEAT_COLD.md` §A19 / §A20 / §A21 (entry-crc32 2358365206 · 712775133 · 3493617609). ⛔ **Found by the nineteenth base's blind RESULT read: this file still declared the eighteenth base and chain 3 after the re-base had been written, and `fleet_dashboard.py` was returning BUILD FAILED — 'each HEARTBEAT amendment needs one reviewed dashboard projection'. The derived view was DEAD, not stale, and nothing in the re-base itself would have surfaced it.** **Nothing is projected until the next `> **AMENDMENT #1` block is appended to the nineteenth base** — at which point it needs exactly one numbered projection with a `source_sha256` over its exact paragraph.*


*Nineteenth base + **chain 1** — Amendment #1 (2026-09-19 closeout: the GLD and TBT counts in the base are DISPUTED by an untranscribed 9/16 broker capture; no market data changed and no level was substituted) projected below.*

```dashboard-amendment
{
  "amendment": 1,
  "source_sha256": "4879e9907aa722fd420a769aa853f3ad7a2de9df090eb75fa4cbab5a8d69c8af",
  "set": {
    "one": "September 19, closeout: the position counts in the regime file are DISPUTED, not current. A Will-supplied broker capture of 2026-09-16 13:57 ET \u2014 recorded in one report file and propagated nowhere for three days \u2014 contradicts the mirror on six cells, two of them here (GLD 16 vs 17, TBT 14 vs 10). Not substituted: it is a visual read of two undated screenshots with no activity view, which is not an export. Reconcile owed, DOCKET L448.",
    "channels": {},
    "ticker": {}
  }
}
```

*Prior: Eighteenth base 2026-09-17 (evening): chain 3 — two projections (Japan/carry and the SAM/RED owner grades), both folded at the nineteenth re-base.*
*Prior: Seventeenth base 2026-09-17 (morning): chain 3 — three Rates-channel projections, all folded at the eighteenth re-base.*

*Prior: Fifteenth base 2026-09-12: **chain 0 — no amendments.** The fourteenth base's Amendment #1 (closeout write-back 12:1x) and Amendment #2 (the Saudi MoE Petroline shutdown statement) were FOLDED INTO THE BASE at the 2026-09-12 re-base and their projections are REMOVED here per this file's own rule; the amendment blocks themselves are rotated verbatim to `PROME/HEARTBEAT_COLD.md` §A14 / §A15 (entry-crc32 3012472809 · 1121796424). **Nothing is projected until the next `> **AMENDMENT #1` block is appended to the fifteenth base** — at which point it needs exactly one numbered projection with a `source_sha256` over its exact paragraph.*

*⛔ **ONE ORPHANED PROJECTION REMOVED 2026-09-19 at the nineteenth re-base: amendment #3 of the EIGHTEENTH base (Equity-vol · Rates · Credit) was still present in this file, sitting immediately below a PRIOR note that declared projections removed.** It was left behind by an earlier re-base and it is the reason `fleet_dashboard.py` returned BUILD FAILED: the builder requires len(amendments) == len(projections), and with the nineteenth base at chain 0 a single surviving block is a mismatch just as surely as a missing one. Its content is fully carried by the nineteenth base (§5 · §2 · §3) and the amendment block itself is verbatim at `PROME/HEARTBEAT_COLD.md` §A21, so nothing is lost. 🔑 **The lesson for this file's own rule: 'remove projections for amendments folded into the base' had no CHECK, so a miss was invisible until the builder failed — and the builder's failure message names the amendment side, not the orphan side.** `[[finding_guard_correctness_and_wiring_are_independent]]`*
