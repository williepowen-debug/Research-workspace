---
name: finding_lessons_file_cannot_detect_own_contradictions
description: A prose lessons/LEARNINGS file cannot detect its own contradictions, so when two entries disagree the one written FIRST wins by default in every spec drafted afterwards — give lessons machine-comparable asserts and check them automatically.
metadata:
  type: feedback
---

**Every agent keeping a `LESSONS.md`-style file has this defect and cannot see it.** Prose lessons accumulate, some of them disagree, **nothing in the process ever forces a reconciliation** — so when a spec gets drafted, whichever lesson the author happened to recall (usually the older, more-repeated one) wins **silently**. The newer lesson, often the one carrying the empirical record, is simply not consulted.

**Case (BRENT, 2026-07-30).** Four separate live defects in a single day traced to this one root:

| Conflict | What happened |
|---|---|
| L18 vs L19 | Opposite directional claims about the **same instrument**. L18 was written first and got copied into a **capital-governing gate the operator had ratified**; L19 — which carried the failed-prediction evidence — was never consulted. |
| L11 & L16 vs L18 | *"Act on the announcement"* vs *"require physical verification."* The spec sided with L18. **L18 was outvoted 2-to-1 and nobody knew**, because no one had ever laid the three side by side. |
| L21 vs a falsifier | A falsifier written **one day after** the operator ratified L21's fix violated L21 exactly (forced a weekly survey and a daily price into one shared window; **1 fire in 155 weeks**). *Fixing an instance is not fixing the class.* |
| L15 scope drift | A structure spec written for a **slow** trade was inherited by a **fast** one. **Two different trades sharing one spec**, and nothing recorded which trade the spec was for. |

## The structural fix — three parts, and the third is the one that matters

1. **Give every lesson MACHINE-COMPARABLE ASSERTS.** A companion `LESSONS_INDEX.tsv` with `id · headline · scope · concepts · asserts · status · tension_with · resolution`. **`asserts` are `key=value`** (e.g. `entry_timing=ON_ANNOUNCEMENT`). **A contradiction becomes detectable: two lessons sharing an ASSERT KEY with different VALUES.** Prose cannot be diffed; `key=value` can.
2. **Tag resolutions PER KEY** — `[<assert_key>:RESOLVED]` / `[<assert_key>:OPEN]`. Without this, one lesson's resolution note silently marks an *unrelated* tension as settled. (Hit this immediately: a lesson in two separate conflicts had one resolution field, and it wrongly cleared both.)
3. **⚠️ PUT THE CHECK IN THE BOOT KIT, NOT IN THE INSTRUCTIONS FILE.** A documented command is still a remembered ritual — and *the entire defect class came from lessons nobody re-read.* Writing "remember to check for conflicts" into the very file that already failed to be re-read fixes nothing. → `[[finding_mechanize_the_cap_not_the_ritual]]`

**Also worth encoding: `scope`.** Half the failures were not contradictions at all but **scope drift** — a lesson correct in context A silently applied to context B. A lesson with no declared scope will be over-applied.

## Distinguish the two report classes

- **`KNOWN, UNRESOLVED`** — the tension is declared; someone looked and chose not to (or could not) settle it. **Acceptable, if visible.**
- **🔴 `UNDECLARED`** — neither lesson names the other. **This is the dangerous class**: nobody has ever adjudicated them, so the default winner is decided by write-order.

**Validation, and the reason to actually build it rather than plan it:** the checker surfaced a contradiction on its **first run** that a full manual audit that same day had missed — and that finding **inverted the weight of evidence** on a live, operator-ruled spec decision. The manual audit was careful and still lost to write-order bias; only the mechanical pairwise scan is immune to it.

**Related:** `[[finding_compound_gate_jointly_unsatisfiable]]` (the specs these lessons seed), `[[finding_threshold_spec_fails_before_world]]`, `[[finding_record_of_an_action_is_not_the_action]]`, `[[finding_seeded_selfsweep_secondary_surface_rot]]`.
