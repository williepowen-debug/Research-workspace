---
name: finding_rereading_a_rows_conditions_without_its_verdict_cell_regrades_a_dead_card
description: A decision row's CONDITION text invites re-grading with fresh data; its VERDICT lives in another cell (the rec) and may already say KILLED — read the verdict cell before deriving a state from the conditions, and check a kill rule over the whole window, never the latest cells.
metadata:
  type: feedback
symptoms: "may become armable tomorrow", "leg (b) is one cell away", re-deriving a card's state from fresh FRED cells, telling Will a lapsed/killed card is live, a kill line that printed earlier in the window than the cells you read, a ⚖️ block the plan read reverses
---

**What happened (2026-10-15, PROME prome-81):** the 10/14 HY OAS cell printed 325 bp. PROME re-read WQ-365's row TITLE and CONDITION text (leg (a) failed breakout · leg (b) HY ≥321 on the two latest cells) against the fresh cells (316 / 325), concluded "one cell away — Friday decides", and told Will the card "may become armable tomorrow" in a ⚖️ block. The row's REC cell (TERRY's 10/7 verdict, 76c75516b) already said: the card's own KILL line (HY ≤312) had PRINTED on 10/2–10/6 — NOT ARMABLE, lean LAPSE. The plan read of the HEARTBEAT re-base caught it (❌33); PROME corrected Will in the same session. Nothing was traded.

**Why it happens:** a condition cell is written to be graded, so fresh data pulls the reader into grading it; the verdict sits in a different cell (rec / state / disposition) that the condition cell does not point at; and a KILL rule is a window property (did it print at ANY time since arming?) while the reader checks the LATEST cells. Two independent misses stacked: the wrong cell, and the wrong window.

**How to apply:**
- Before deriving a state for any card/gate/row from fresh data, read the row's VERDICT cell (rec, state, disposition) and the owner's latest grade — in that order; if either already names a terminal state (KILLED · LAPSED · NOT ARMABLE · RESOLVED), the fresh data is context, never a re-grade.
- A kill or disarm rule is checked over the WHOLE window since arming, from the owner's record, never from the latest N cells.
- A ⚖️ block that changes what Will might do today is the first thing a blind reader checks — write it from the owner's verdict, not from PROME's arithmetic.
- The owner grades the legs (here TERRY); PROME cites, it does not re-grade.

Related: [[finding_exact_level_authenticates_a_wrong_direction]] (an exact number authenticates the claim beside it) · [[finding_dated_carry_item_has_no_expiry_check]] · [[finding_summary_section_merges_what_the_body_separates]] · [[finding_a_correction_pass_is_unreviewed_work]] (the fix after the final read is unreviewed).
