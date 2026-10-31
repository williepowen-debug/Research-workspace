---
name: feedback_fewer_checkers_and_rules
description: Will wants FEWER checkers, gates and rules in the fleet — fix the instance or improve an existing control; propose retiring controls that do not earn their keep
symptoms: about to add a new check, gate, boot line, registry, acceptance file or charter rule; a review cycle keeps finding gaps in a new control; the backlog holds approved-but-unbuilt process items
metadata:
  type: feedback
---

Will, 2026-10-31 15:18 ET in PROME's chat, verbatim: "Right I agree with you but I do think we want to limit our excess amount of checkers and rules etc" — said right after he dropped the WQ-295 R2 cadence-wake rule (WQ-576), which four review rounds had held back because its new alarm could read "all clear" on a damaged input. Same day: the process ceiling suspended (WQ-566) and "fewer round trips" (USER.md).

**Why:** every new checker brings its own failure modes, review rounds and upkeep; the 10/31 cadence encode spent four reviews on the alarm's own edge cases and never went live. Will weighs that cost above the benefit when dated rows, the aged-action rule and his own catch-up spawns already cover most of the ground.

**How to apply:** default to NOT adding a control. When a defect appears, fix the instance, or repair or extend an existing control (WQ-229's own preference), and say why a new one is not needed. Before building an approved-but-unbuilt process item, ask whether it still earns its keep, and propose retiring the ones that only add checking. A new checker needs a concrete, recurring miss behind it and Will's word. Related: [[feedback_experiments_run_light_not_fleet_process]] · [[finding_mechanize_the_cap_not_the_ritual]] (the tension: mechanize only what actually recurs).
