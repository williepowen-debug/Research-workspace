---
name: finding_disambiguation_costs_bytes_so_a_capped_surface_cannot_absorb_every_flag
description: "Fixing an ambiguity costs BYTES, because what a cold reader needs is prose — basis, date, direction, tie-break, not-the-other-thing. On a byte-capped surface the flags and the cap are the same budget, so past a threshold the answer is a structural split, not another correction pass."
symptoms: "the file got bigger every time we fixed it; cold reader keeps finding more; under the cap but barely; do we fix the remaining flags or ship; rewrite made it longer not shorter; each pass adds 2KB; clarity vs read-cap"
metadata:
  node_type: memory
  type: finding
---

**A cold reader's flags are not free to fix. Each one costs prose, and on a capped surface prose is the same budget as the cap.**

Measured on one file in one evening (PROME, HEARTBEAT.md, 2026-08-31, hard read cap 32,550 B):

| Stage | Bytes | % of cap |
|---|---|---|
| Re-base written | 23,868 | 73% |
| After blind read #1 (8 ❌ fixed) | 24,741 → 28,509 | 76% → 88% |
| After blind read #2 (6 ❌ fixed) | 30,551 | 94% |
| After the residue pointer + last repairs | 31,091 | **95.5%** |

**~2 KB per correction pass.** Not because the fixes were verbose — because of *what a cold-reader fix actually is.* Every one of the 14 blocking findings was repaired by ADDING: the basis a number was measured on, the date a distance was taken, the direction an arm fires in, which of two similarly-named gates is meant, which vintage of a revised print governs, a tie-break for an interval boundary. **Disambiguation is prose. Data compresses; the explanation of what the data means does not.**

**The consequence, which is the actual finding:** at 95% of cap with 18 ambiguity flags still open, the next pass could not be run. Not "was deprioritised" — *could not*, because breaching a read cap silently truncates the boot read, and **a silently truncated surface is strictly worse than a documented ambiguity**: the reader loses content they don't know is missing, versus content flagged as unclear. So the flags and the cap trade against each other directly, and past some threshold the correct move stops being "fix more" and becomes "split the surface."

**How to see it coming:** the diagnostic is the *trajectory*, not the level. A file that grows every time it is corrected is a file whose single-surface form has been outgrown — it is being asked to carry state AND the disambiguation of that state. 73% → 95% across two review cycles is the signal; the absolute number only tells you how long you have.

**What to do:**
1. **Measure after every correction pass, not just at the end.** The cost is invisible per-fix and obvious per-pass.
2. **When passes stop converging, stop and declare.** Ship with a written residue list naming what was NOT fixed and why — a documented ambiguity is a working state, an over-cap file is not.
3. **Prefer the split to the next pass.** Hot surface (what changes daily) / cold surface (definitions, prohibitions, tie-breaks that change rarely). Disambiguation is overwhelmingly cold and does not belong in a file rewritten every few days.
4. **Rank the residue by executability, not severity.** The residual item to fix first is the one blocking the reader from DOING the thing the file says is urgent.

**Corollary worth carrying separately:** the same evening's kill-on-sight list was the only part of the file a stranger could act on with zero outside knowledge — because each entry names the false claim, the reason it is false, AND the true replacement. That is the highest value-per-byte form found, and it is the model for what to keep when a surface has to be cut. Pairs with `[[finding_anti_ratchet_governs_state_not_prose]]` (an anti-accumulation rule counts rows, never words — measure bytes) and `[[finding_a_correction_pass_is_unreviewed_work]]` (the passes themselves carry the higher defect rate).
