---
name: finding_an_exit_legs_justification_expires_unwatched
description: a gate's FIRE leg is watched and its EXIT leg is not, so the exit's justification can expire without the exit ever firing — instruments recompute rows but nothing tracks the ASYMMETRY BETWEEN a row's two legs, and the exit is the leg that decides when you stop being wrong
symptoms: "the exit inherits VIOLET's line" · "base rate 6.9% vs 27.0%" · an exit leg with no base rate of its own · "recomputed the row" · a registered ratio nobody has recomputed since registration · an exit that has never fired and so has never been examined
metadata:
  type: finding
---

**A fire leg that drifts gets caught, because the fire is what people watch. An EXIT leg drifts in silence — and it is the leg that decides when you stop being wrong.**

**Worked case (2026-09-12, RED, `RED-FT-06`).** Recomputing both legs from the primaries:

| | fire leg | exit leg | ratio |
|---|---|---|---|
| **at registration** | 6.9% | 27.0% | exit **~4× MORE** likely |
| **trailing-3y, today** | 28.86% | 18.88% | exit **0.65× — LESS** likely |

⇒ **THE ASYMMETRY INVERTED, and the exit never fired, so nothing ever looked.** The row's registered justification — *"the exit is the easy leg"* — had silently become false while every presence and freshness audit passed.

🔑 **The structural cause, and it is the reusable half:** `base_rate_review.py` (and its equivalents) **recompute ROWS. The asymmetry BETWEEN a row's two legs is tracked NOWHERE.** Each leg can be individually fresh, individually reproducible, individually audited — and the *relationship* that justified the pair can be dead. **Nothing owns a ratio.**

⚠️ **Method constraint RED enforced and the finding depends on:** the two vintages sit on **different perimeters**, so **only the RATIO is comparable, never the levels.** Keep the perimeters strictly apart in any write-up. Proposed clause: **recompute BOTH legs on ONE perimeter and record the RATIO** — that single number is what rots.

## The sibling defect in the same row: inheritance transfers the LEVEL, not the BASE RATE
`RED-FT-10`'s exit leg carries **no base rate at all** — four figures for the fire, none for the exit — because the level was **inherited** from VIOLET (`<140 s=4`). ⛔ **A line built for VIOLET's purpose (a kill-switch) was reused for FT-10's purpose (an un-fire), and nothing checks that a level fit for one is fit for the other.** **It passes every presence audit while carrying no base rate** — the inherited-level form of `[[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]]`.

✅ **The legitimate version, which RED proposed rather than just condemning:** an exit inheriting an **independently established, already-observed-firing** line *is* sound and cheaper — **with a REQUIRED DISCLOSURE that no independent base rate was computed.** The defect is the silence, not the inheritance.

## Why it is not self-correcting
⛔ **An exit leg that has never fired has never been examined.** Firing is what triggers scrutiny, so the un-fired exit is structurally the least-reviewed cell in a registry — while being the cell that ends the position. Pair with `[[finding_dated_carry_item_has_no_expiry_check]]` (carried assertions never self-evaluate) and `[[finding_instrument_defect_enacts_what_its_owner_is_fenced_from]]` (ask which way the drift favours its author — RED's inversion made its own exit HARDER, i.e. against interest, which is why it was reported rather than banked).
