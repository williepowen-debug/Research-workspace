---
name: finding_sustain_count_role_discriminating_power
description: "A registered trigger needs a stated ROLE, not just a derived number — test what the instrument can and cannot catch; the derivation may return \"this tool can't catch that failure class\""
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2abdfc56-b5f2-4491-97e6-16215724720d
---

Deriving a sustain count n for a trigger (e.g., "VIX >23 close-and-hold, n consecutive closes") is incomplete until you test the instrument's **discriminating power** against the failure class it's meant to catch. VIOLET CHG-RED-033 (6/10/26): the empirically-derived n=5 was sound, but destination-RIGHT and destination-WRONG analogs both produced the same max run (4) — run-length above a level could not separate fine-retest from fatal re-arm. The one clear historical failure (2024-12) failed at the *window boundary*, not on mid-window run-length (its run read 2→4→7 as the window end slid 5 days).

**Why:** an undefined "sustained" gets adjudicated under fire; but a defined-n trigger silently sold as "the invalidation" is worse — it certifies falsifiability the instrument doesn't have. Failure classes live in different places (run-length, window-end, composition); each needs the instrument that can see it.

**How to apply:** when registering any sustain/threshold trigger: (1) derive n empirically from analog paths, not symmetry with another metric's convention; (2) run the derivation on BOTH outcome classes and check whether the statistic separates them; (3) register the trigger's ROLE explicitly — tail-stop (bounds unprecedented paths) vs failure-catcher — and name which clause carries the real falsification weight (e.g., credit tripwires PRIMARY, time-box carries window-end failures, n=5 tail-stop). Relevant to any agent carrying s=N registry triggers ([[feedback_script_labels_match_thesis]]; sibling of [[finding_threshold_vs_mechanism]], [[finding_catalyst_path_decoupling]]).
